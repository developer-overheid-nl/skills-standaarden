"""Tests voor scripts/check_forum_standards.py."""

import json

import responses
from check_forum_standards import API_URL, BASELINE_PATH, compare, fetch_standards, load_baseline


def api_response(titles):
    """Verkorte JSON:API-respons: standaarden tussen de andere included-typen."""
    included = [{"type": "paragraph--decision_tree_step", "attributes": {"title": "Stap 1"}}]
    included += [{"type": "node--standaarden", "attributes": {"title": title}} for title in titles]
    return json.dumps({"data": [], "included": included})


# --- fetch_standards() ---


class TestFetchStandards:
    @responses.activate
    def test_alleen_standaarden_gesorteerd_en_uniek(self):
        responses.add(responses.GET, API_URL, body=api_response(["TLS", "DNSSEC", "TLS"]))
        assert fetch_standards() == ["DNSSEC", "TLS"]

    @responses.activate
    def test_witruimte_rond_titel_telt_niet(self):
        responses.add(responses.GET, API_URL, body=api_response(["TLS ", "TLS"]))
        assert fetch_standards() == ["TLS"]

    @responses.activate
    def test_serverfout_geeft_none(self):
        responses.add(responses.GET, API_URL, status=503)
        assert fetch_standards() is None

    @responses.activate
    def test_geen_json_geeft_none(self):
        responses.add(responses.GET, API_URL, body="<html>onderhoud</html>")
        assert fetch_standards() is None

    @responses.activate
    def test_zonder_included_geeft_lege_lijst(self):
        responses.add(responses.GET, API_URL, body=json.dumps({"data": []}))
        assert fetch_standards() == []


# --- compare() ---


class TestCompare:
    def test_gelijk(self):
        assert compare(["DNSSEC", "TLS"], ["TLS", "DNSSEC"]) == ([], [])

    def test_toegevoegd(self):
        assert compare(["TLS"], ["DNSSEC", "TLS"]) == (["DNSSEC"], [])

    def test_verwijderd(self):
        assert compare(["DNSSEC", "TLS"], ["TLS"]) == ([], ["DNSSEC"])

    def test_hernoemd_telt_als_toegevoegd_en_verwijderd(self):
        assert compare(["StUF"], ["StUF 3"]) == (["StUF 3"], ["StUF"])


# --- vastgelegde lijst ---


class TestBaseline:
    def test_gesorteerd_en_uniek(self):
        baseline = load_baseline()
        assert baseline == sorted(set(baseline))

    def test_aantal_komt_overeen_met_skill(self):
        # ls/SKILL.md noemt het aantal; de dekkingstabel en deze lijst horen samen te wijzigen.
        skill_path = BASELINE_PATH.parent.parent / "skills" / "ls" / "SKILL.md"
        skill = skill_path.read_text(encoding="utf-8")
        assert f"De beslisboom kent {len(load_baseline())} standaarden" in skill
