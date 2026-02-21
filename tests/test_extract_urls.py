"""Tests voor scripts/extract_urls.py."""

import sys
from pathlib import Path

# Voeg scripts/ toe aan sys.path zodat we extract_urls kunnen importeren
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from extract_urls import (
    classify_url,
    clean_url,
    extract_all,
    extract_urls_from_file,
    is_excluded,
    normalize_github_url,
)

# --- clean_url() ---


class TestCleanUrl:
    def test_trailing_punctuatie(self):
        assert clean_url("https://example.com/path.") == "https://example.com/path"
        assert clean_url("https://example.com/path,") == "https://example.com/path"
        assert clean_url("https://example.com/path;") == "https://example.com/path"
        assert clean_url("https://example.com/path:") == "https://example.com/path"
        assert clean_url("https://example.com/path!") == "https://example.com/path"
        assert clean_url("https://example.com/path?") == "https://example.com/path"

    def test_gebalanceerde_haakjes(self):
        # Ongebalanceerde ) wordt verwijderd
        assert clean_url("https://example.com/path)") == "https://example.com/path"
        # Gebalanceerde () blijft behouden
        assert clean_url("https://example.com/path(1)") == "https://example.com/path(1)"
        # Dubbel ongebalanceerd
        assert clean_url("https://example.com/path))") == "https://example.com/path"

    def test_gebalanceerde_brackets(self):
        assert clean_url("https://example.com/path]") == "https://example.com/path"
        assert clean_url("https://example.com/path[1]") == "https://example.com/path[1]"

    def test_footnote_markers(self):
        assert clean_url("https://example.com/path¹") == "https://example.com/path"
        assert clean_url("https://example.com/path²³") == "https://example.com/path"

    def test_trailing_slash(self):
        assert clean_url("https://example.com/path/") == "https://example.com/path"

    def test_combinatie(self):
        # Trailing punctuatie + slash
        assert clean_url("https://example.com/path/.") == "https://example.com/path"

    def test_geen_wijziging(self):
        assert clean_url("https://example.com/path") == "https://example.com/path"


# --- is_excluded() ---


class TestIsExcluded:
    def test_example_domains(self):
        assert is_excluded("https://example.com/test") is True
        assert is_excluded("https://api.example.com/v1") is True
        assert is_excluded("https://sub.example.nl/test") is True

    def test_localhost(self):
        assert is_excluded("http://localhost:8080") is True
        assert is_excluded("http://127.0.0.1:3000") is True

    def test_namespace_urls(self):
        assert is_excluded("https://www.w3.org/2001/XMLSchema") is True
        assert is_excluded("https://schemas.xmlsoap.org/soap/envelope/") is True

    def test_fsc_voorbeeld_urls(self):
        assert is_excluded("https://service.example/api") is True
        assert is_excluded("https://inway.provider.example/service") is True

    def test_echte_urls_niet_uitgesloten(self):
        assert is_excluded("https://github.com/logius-standaarden/test") is False
        assert is_excluded("https://gitdocumentatie.logius.nl/publicatie/dk") is False
        assert is_excluded("https://www.forumstandaardisatie.nl/open-standaarden") is False


# --- classify_url() ---


class TestClassifyUrl:
    def test_github_repo(self):
        url = "https://github.com/logius-standaarden/Digikoppeling-Koppelvlakstandaard-REST-API"
        assert classify_url(url) == "github_repo"

    def test_published_doc(self):
        url = "https://gitdocumentatie.logius.nl/publicatie/dk/architectuur"
        assert classify_url(url) == "published_doc"

    def test_draft_doc(self):
        url = "https://logius-standaarden.github.io/OAuth-NL-profiel"
        assert classify_url(url) == "draft_doc"

    def test_forum(self):
        url = "https://www.forumstandaardisatie.nl/open-standaarden/digikoppeling"
        assert classify_url(url) == "forum"

    def test_onbekende_url(self):
        assert classify_url("https://www.google.com") is None
        assert classify_url("https://docs.python.org/3/") is None


# --- normalize_github_url() ---


class TestNormalizeGithubUrl:
    def test_tags_verwijderd(self):
        assert (
            normalize_github_url("https://github.com/logius-standaarden/test-repo/tags")
            == "https://github.com/logius-standaarden/test-repo"
        )

    def test_tree_main_verwijderd(self):
        assert (
            normalize_github_url("https://github.com/logius-standaarden/test-repo/tree/main")
            == "https://github.com/logius-standaarden/test-repo"
        )

    def test_blob_verwijderd(self):
        assert (
            normalize_github_url(
                "https://github.com/logius-standaarden/test-repo/blob/main/README.md"
            )
            == "https://github.com/logius-standaarden/test-repo"
        )

    def test_issues_verwijderd(self):
        assert (
            normalize_github_url("https://github.com/logius-standaarden/test-repo/issues")
            == "https://github.com/logius-standaarden/test-repo"
        )

    def test_passthrough_base_url(self):
        url = "https://github.com/logius-standaarden/test-repo"
        assert normalize_github_url(url) == url

    def test_passthrough_niet_logius(self):
        url = "https://github.com/other-org/some-repo/tags"
        assert normalize_github_url(url) == url


# --- extract_urls_from_file() ---


class TestExtractUrlsFromFile:
    def test_sample_skill(self):
        fixture = Path(__file__).parent / "fixtures" / "sample_skill.md"
        results = extract_urls_from_file(fixture)

        urls = [r["url"] for r in results]

        # GitHub repo URL moet genormaliseerd zijn (geen /tags)
        assert "https://github.com/logius-standaarden/test-repo" in urls
        # Published doc
        assert "https://gitdocumentatie.logius.nl/publicatie/dk/architectuur" in urls
        # Draft doc
        assert "https://logius-standaarden.github.io/test-repo" in urls
        # Forum
        assert "https://www.forumstandaardisatie.nl/open-standaarden/digikoppeling" in urls

        # Excluded URLs moeten NIET voorkomen
        excluded_urls = [u for u in urls if "example.com" in u or "example/" in u]
        assert excluded_urls == []

    def test_skill_naam_detectie(self):
        fixture = Path(__file__).parent / "fixtures" / "sample_skill.md"
        results = extract_urls_from_file(fixture)

        # Het bestand staat niet onder skills/<naam>/, dus skill_name is None
        # Dit is correct gedrag voor bestanden buiten de skills-directory
        for r in results:
            assert r["source_file"] == str(fixture)

    def test_types_correct(self):
        fixture = Path(__file__).parent / "fixtures" / "sample_skill.md"
        results = extract_urls_from_file(fixture)

        type_map = {r["url"]: r["type"] for r in results}
        github_url = "https://github.com/logius-standaarden/test-repo"
        pub_url = "https://gitdocumentatie.logius.nl/publicatie/dk/architectuur"
        draft_url = "https://logius-standaarden.github.io/test-repo"
        forum_url = "https://www.forumstandaardisatie.nl/open-standaarden/digikoppeling"
        assert type_map[github_url] == "github_repo"
        assert type_map[pub_url] == "published_doc"
        assert type_map[draft_url] == "draft_doc"
        assert type_map[forum_url] == "forum"


# --- extract_all() deduplicatie ---


class TestExtractAll:
    def test_deduplicatie(self, tmp_path):
        """Dezelfde URL in meerdere bestanden wordt maar één keer opgenomen."""
        skill_dir = tmp_path / "skills" / "test-skill"
        skill_dir.mkdir(parents=True)

        url = "https://github.com/logius-standaarden/shared-repo"

        (skill_dir / "SKILL.md").write_text(
            f"---\nname: test\ndescription: test\nmodel: sonnet\n---\n\nRepo: {url}\n"
        )
        (skill_dir / "reference.md").write_text(f"# Ref\n\nZie ook: {url}\n")

        results = extract_all(tmp_path / "skills")
        urls = [r["url"] for r in results]

        assert urls.count(url) == 1

    def test_lege_directory(self, tmp_path):
        """Lege skills directory geeft lege lijst."""
        skill_dir = tmp_path / "skills"
        skill_dir.mkdir()
        assert extract_all(skill_dir) == []
