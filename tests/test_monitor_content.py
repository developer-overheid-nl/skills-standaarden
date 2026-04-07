"""Tests voor scripts/monitor_content.py."""

import hashlib
from unittest.mock import call, patch

import requests
import responses
from monitor_content import (
    check_http_resource,
    detect_changes,
    extract_visible_text,
    fetch_with_retry,
)

# --- extract_visible_text() ---


class TestExtractVisibleText:
    def test_body_tekst_behouden(self):
        html = "<html><body><h1>Titel</h1><p>Standaard tekst.</p></body></html>"
        result = extract_visible_text(html)
        assert "Titel" in result
        assert "Standaard tekst." in result

    def test_scripts_verwijderd(self):
        html = '<body><p>content</p><script>var x = "secret";</script></body>'
        result = extract_visible_text(html)
        assert "content" in result
        assert "secret" not in result

    def test_styles_verwijderd(self):
        html = "<body><style>.cls { color: red; }</style><p>zichtbaar</p></body>"
        result = extract_visible_text(html)
        assert "zichtbaar" in result
        assert "color" not in result

    def test_noscript_verwijderd(self):
        html = "<body><noscript>JS required</noscript><p>content</p></body>"
        result = extract_visible_text(html)
        assert "content" in result
        assert "JS required" not in result

    def test_html_tags_verwijderd(self):
        html = '<body><div class="wrapper"><a href="/link">tekst</a></div></body>'
        result = extract_visible_text(html)
        assert "tekst" in result
        assert "<div" not in result
        assert "href" not in result

    def test_whitespace_genormaliseerd(self):
        html = "<body><p>veel   spaties</p>\n\n\n<p>en  regels</p></body>"
        result = extract_visible_text(html)
        assert "veel spaties" in result
        assert "en regels" in result
        assert "\n" not in result

    def test_drupal_framework_ruis_genegeerd(self):
        """CMS-framework code verdwijnt omdat het in script-tags zit."""
        html = (
            "<body>"
            '<script data-drupal-selector="drupal-settings-json">'
            '{"ajaxPageState":{"libraries":"eJxdzUEOAi"}}'
            "</script>"
            "<p>Echte content</p>"
            "</body>"
        )
        result = extract_visible_text(html)
        assert "Echte content" in result
        assert "ajaxPageState" not in result
        assert "libraries" not in result

    def test_liferay_framework_ruis_genegeerd(self):
        """Liferay tokens en config verdwijnen omdat ze in script-tags zitten."""
        html = "<body><script>Liferay.authToken = '9zmfQSYt';</script><p>PDOK content</p></body>"
        result = extract_visible_text(html)
        assert "PDOK content" in result
        assert "authToken" not in result

    def test_zonder_body_tag(self):
        """Werkt ook als er geen <body> tag is (bijv. plain HTML fragment)."""
        html = "<h1>Titel</h1><p>Tekst</p>"
        result = extract_visible_text(html)
        assert "Titel" in result
        assert "Tekst" in result

    def test_multiline_script(self):
        html = (
            "<body>"
            "<script>\n"
            "  var config = {\n"
            '    token: "abc123"\n'
            "  };\n"
            "</script>"
            "<p>content</p>"
            "</body>"
        )
        result = extract_visible_text(html)
        assert "content" in result
        assert "token" not in result


# --- detect_changes() ---


class TestDetectChanges:
    def test_eerste_run_geen_changes(self):
        """Eerste run (previous=None) geeft geen changes."""
        current = {"last_commit_sha": "abc1234"}
        assert detect_changes("https://example.com", current, None) == []

    def test_zelfde_state(self):
        """Geen wijzigingen als state identiek is."""
        current = {"last_commit_sha": "abc1234", "latest_tag": "v1.0"}
        previous = {"state": {"last_commit_sha": "abc1234", "latest_tag": "v1.0"}}
        assert detect_changes("https://example.com", current, previous) == []

    def test_nieuwe_commit(self):
        current = {
            "last_commit_sha": "new1234",
            "last_commit_date": "2024-01-15",
        }
        previous = {"state": {"last_commit_sha": "old5678"}}
        changes = detect_changes("https://example.com", current, previous)
        assert len(changes) == 1
        assert "Nieuwe commit" in changes[0]
        assert "new1234"[:7] in changes[0]

    def test_nieuwe_tag(self):
        current = {"latest_tag": "v2.0"}
        previous = {"state": {"latest_tag": "v1.0"}}
        changes = detect_changes("https://example.com", current, previous)
        assert len(changes) == 1
        assert "Nieuwe tag" in changes[0]
        assert "v2.0" in changes[0]

    def test_archived(self):
        current = {"archived": True}
        previous = {"state": {"archived": False}}
        changes = detect_changes("https://example.com", current, previous)
        assert "Repository is gearchiveerd" in changes

    def test_body_hash_gewijzigd(self):
        current = {"body_sha256": "newhash"}
        previous = {"state": {"body_sha256": "oldhash"}}
        changes = detect_changes("https://example.com", current, previous)
        assert len(changes) == 1
        assert "body hash" in changes[0]

    def test_etag_suppressie_bij_body_change(self):
        """Als body hash al gewijzigd is, wordt ETag change onderdrukt."""
        current = {"body_sha256": "newhash", "etag": "new-etag"}
        previous = {"state": {"body_sha256": "oldhash", "etag": "old-etag"}}
        changes = detect_changes("https://example.com", current, previous)
        assert len(changes) == 1
        assert "body hash" in changes[0]
        # ETag change is onderdrukt
        assert not any("ETag" in c for c in changes)

    def test_etag_zonder_body_change(self):
        """ETag change wordt genegeerd als body hash beschikbaar en ongewijzigd is."""
        current = {"body_sha256": "same", "etag": "new-etag"}
        previous = {"state": {"body_sha256": "same", "etag": "old-etag"}}
        changes = detect_changes("https://example.com", current, previous)
        assert len(changes) == 0

    def test_error_in_current(self):
        """Errors geven geen changes (worden apart afgehandeld)."""
        current = {"error": "HTTP 500"}
        previous = {"state": {"body_sha256": "hash"}}
        assert detect_changes("https://example.com", current, previous) == []

    def test_last_modified_zonder_body_change(self):
        """Last-Modified change wordt genegeerd als body hash beschikbaar en ongewijzigd is."""
        current = {"body_sha256": "same", "last_modified": "Tue, 02 Jan 2024"}
        previous = {"state": {"body_sha256": "same", "last_modified": "Mon, 01 Jan 2024"}}
        changes = detect_changes("https://example.com", current, previous)
        assert len(changes) == 0

    def test_last_modified_suppressie_bij_body_change(self):
        """Last-Modified change wordt onderdrukt als body hash al gewijzigd is."""
        current = {"body_sha256": "new", "last_modified": "Tue, 02 Jan 2024"}
        previous = {"state": {"body_sha256": "old", "last_modified": "Mon, 01 Jan 2024"}}
        changes = detect_changes("https://example.com", current, previous)
        assert len(changes) == 1
        assert "body hash" in changes[0]
        assert not any("Last-Modified" in c for c in changes)

    def test_etag_zonder_body_hash(self):
        """ETag change wordt wel gemeld als er geen body hash beschikbaar is."""
        current = {"etag": "new-etag"}
        previous = {"state": {"etag": "old-etag"}}
        changes = detect_changes("https://example.com", current, previous)
        assert len(changes) == 1
        assert "ETag" in changes[0]

    def test_last_modified_zonder_body_hash(self):
        """Last-Modified change wordt wel gemeld als er geen body hash beschikbaar is."""
        current = {"last_modified": "Tue, 02 Jan 2024"}
        previous = {"state": {"last_modified": "Mon, 01 Jan 2024"}}
        changes = detect_changes("https://example.com", current, previous)
        assert len(changes) == 1
        assert "Last-Modified" in changes[0]

    def test_nieuwe_key_geen_change(self):
        """Key die niet in previous state zit triggert geen change."""
        current = {"latest_tag": "v1.0"}
        previous = {"state": {}}  # Geen latest_tag in vorige state
        assert detect_changes("https://example.com", current, previous) == []


# --- fetch_with_retry() ---


class TestFetchWithRetry:
    @responses.activate
    def test_succes(self):
        responses.add(responses.GET, "https://test.com/page", body="OK", status=200)
        resp = fetch_with_retry("https://test.com/page", max_retries=1)
        assert resp is not None
        assert resp.status_code == 200

    @responses.activate
    @patch("monitor_content.time.sleep")
    def test_429_retry_after(self, mock_sleep):
        """429 met Retry-After header wordt gerespecteerd."""
        responses.add(
            responses.GET,
            "https://test.com/page",
            status=429,
            headers={"Retry-After": "2"},
        )
        responses.add(responses.GET, "https://test.com/page", body="OK", status=200)

        resp = fetch_with_retry("https://test.com/page", max_retries=2)
        assert resp is not None
        assert resp.status_code == 200
        mock_sleep.assert_called_once_with(2)

    @responses.activate
    @patch("monitor_content.time.sleep")
    def test_timeout_retries(self, mock_sleep):
        """RequestException triggert retry met backoff."""
        responses.add(
            responses.GET,
            "https://test.com/page",
            body=requests.ConnectionError("timeout"),
        )
        responses.add(
            responses.GET,
            "https://test.com/page",
            body=requests.ConnectionError("timeout"),
        )
        responses.add(
            responses.GET,
            "https://test.com/page",
            body=requests.ConnectionError("timeout"),
        )

        resp = fetch_with_retry("https://test.com/page", max_retries=3)
        assert resp is None
        # Exponential backoff: attempt 0 = 5s, attempt 1 = 10s, attempt 2 = geen sleep
        assert mock_sleep.call_args_list == [call(5), call(10)]

    @responses.activate
    def test_404_geen_retry(self):
        """4xx responses (behalve 429) worden direct teruggegeven."""
        responses.add(responses.GET, "https://test.com/page", status=404)
        resp = fetch_with_retry("https://test.com/page", max_retries=3)
        assert resp is not None
        assert resp.status_code == 404


# --- check_http_resource() ---


class TestCheckHttpResource:
    @responses.activate
    def test_succes_met_etag_en_body(self):
        body = "<html><body>Test content</body></html>"
        responses.add(
            responses.GET,
            "https://test.com/doc",
            body=body,
            status=200,
            headers={"ETag": '"abc123"', "Last-Modified": "Mon, 01 Jan 2024 00:00:00 GMT"},
        )

        result = check_http_resource("https://test.com/doc")
        assert result["etag"] == '"abc123"'
        assert result["last_modified"] == "Mon, 01 Jan 2024 00:00:00 GMT"
        expected_hash = hashlib.sha256(extract_visible_text(body).encode()).hexdigest()
        assert result["body_sha256"] == expected_hash

    @responses.activate
    def test_error_response(self):
        responses.add(responses.GET, "https://test.com/doc", status=500)
        result = check_http_resource("https://test.com/doc")
        assert "error" in result
        assert "500" in result["error"]

    @responses.activate
    @patch("monitor_content.time.sleep")
    def test_geen_response(self, _mock_sleep):
        responses.add(
            responses.GET,
            "https://test.com/doc",
            body=requests.ConnectionError("fail"),
        )
        responses.add(
            responses.GET,
            "https://test.com/doc",
            body=requests.ConnectionError("fail"),
        )
        responses.add(
            responses.GET,
            "https://test.com/doc",
            body=requests.ConnectionError("fail"),
        )
        result = check_http_resource("https://test.com/doc")
        assert result == {"error": "Geen response"}

    @responses.activate
    def test_zonder_body_hash(self):
        responses.add(
            responses.GET,
            "https://test.com/doc",
            body="content",
            status=200,
        )
        result = check_http_resource("https://test.com/doc", hash_body=False)
        assert "body_sha256" not in result
