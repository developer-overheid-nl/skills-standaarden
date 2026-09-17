"""Tests voor scripts/check_def_versions.py."""

import responses
from check_def_versions import CLAIM_PATTERN, check, resolve_published

BASE = "https://gitdocumentatie.logius.nl/publicatie/dk/oin/"

REDIRECT_STUB = """<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to v2.2.2</title>
<link rel="canonical" href="./2.2.2/">
"""


# Verkorte weergave van een ReSpec-publicatie: de titel eindigt op het versienummer.
def respec_page(title, spec_status):
    return f"""<!DOCTYPE html>
<html><head><title>{title}</title>
<script>var respecConfig = {{"specStatus": "{spec_status}", "publishVersion": "0.0.0"}};</script>
</head><body>Inhoud</body></html>
"""


# --- CLAIM_PATTERN ---


class TestClaimPattern:
    def test_kale_versie_is_claim(self):
        line = f"| [v2.2.2]({BASE}) |"
        assert CLAIM_PATTERN.findall(line) == [("2.2.2", BASE)]

    def test_versiespecifiek_pad(self):
        url = "https://gitdocumentatie.logius.nl/publicatie/api/adr/2.2.1/"
        assert CLAIM_PATTERN.findall(f"[v2.2.1]({url})") == [("2.2.1", url)]

    def test_beschrijvende_linktekst_is_geen_claim(self):
        # "v1.1.0 op gitdocumentatie" is proza in conflicts.md, geen tabelclaim.
        line = f"- gepubliceerde versie [v1.1.0 op gitdocumentatie]({BASE})"
        assert CLAIM_PATTERN.findall(line) == []

    def test_jaarversie_zonder_punten(self):
        url = "https://gitdocumentatie.logius.nl/publicatie/dk/roadmap/"
        assert CLAIM_PATTERN.findall(f"[v2026-2027]({url})") == [("2026-2027", url)]


# --- resolve_published() ---


class TestResolvePublished:
    @responses.activate
    def test_volgt_canonical_redirect(self):
        responses.add(responses.GET, BASE, body=REDIRECT_STUB)
        responses.add(
            responses.GET,
            f"{BASE}2.2.2/",
            body=respec_page("OIN Stelsel 2.2.2", "DEF"),
        )
        version, spec_status, resolved = resolve_published(BASE)
        assert version == "2.2.2"
        assert spec_status == "DEF"
        assert resolved == f"{BASE}2.2.2/"

    @responses.activate
    def test_pagina_zonder_redirect(self):
        responses.add(responses.GET, BASE, body=respec_page("Wat is Digikoppeling? 1.1.2", "DEF"))
        version, spec_status, _ = resolve_published(BASE)
        assert version == "1.1.2"
        assert spec_status == "DEF"

    @responses.activate
    def test_titel_is_leidend_boven_publishversion(self):
        # publishVersion noemt soms de vórige versie; de titel is de actuele.
        responses.add(responses.GET, BASE, body=respec_page("Digikoppeling Beheermodel 1.8", "DEF"))
        version, _, _ = resolve_published(BASE)
        assert version == "1.8"

    @responses.activate
    def test_onbereikbaar(self):
        responses.add(responses.GET, BASE, status=503)
        version, spec_status, _ = resolve_published(BASE)
        assert version is None
        assert spec_status is None


# --- check() ---


class TestCheck:
    @responses.activate
    def test_versie_komt_overeen(self):
        responses.add(responses.GET, BASE, body=REDIRECT_STUB)
        responses.add(responses.GET, f"{BASE}2.2.2/", body=respec_page("OIN Stelsel 2.2.2", "DEF"))
        problems, published, spec_status = check(BASE, [("2.2.2", "skills/x:1")])
        assert problems == []
        assert published == "2.2.2"
        assert spec_status == "DEF"

    @responses.activate
    def test_verouderde_versie_gemeld(self):
        responses.add(responses.GET, BASE, body=REDIRECT_STUB)
        responses.add(responses.GET, f"{BASE}2.2.2/", body=respec_page("OIN Stelsel 2.2.2", "DEF"))
        problems, _, _ = check(BASE, [("3.0.0", "skills/ls-dk/SKILL.md:47")])
        assert [p["soort"] for p in problems] == ["versie"]
        assert "skills/ls-dk/SKILL.md:47" in problems[0]["melding"]

    @responses.activate
    def test_niet_vastgestelde_status_gemeld(self):
        # De aanleiding voor dit script: een VV-versie in een Vastgesteld-kolom.
        url = f"{BASE}3.0.1/"
        responses.add(responses.GET, url, body=respec_page("OIN Stelsel 3.0.1", "VV"))
        problems, _, spec_status = check(url, [("3.0.1", "skills/ls-dk/SKILL.md:47")])
        assert [p["soort"] for p in problems] == ["status"]
        assert spec_status == "VV"

    @responses.activate
    def test_onbereikbaar_gemeld(self):
        responses.add(responses.GET, BASE, status=500)
        problems, _, _ = check(BASE, [("2.2.2", "skills/x:1")])
        assert [p["soort"] for p in problems] == ["onbereikbaar"]
