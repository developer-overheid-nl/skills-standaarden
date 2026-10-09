#!/usr/bin/env python3
"""Controleer de standaardenlijst van de Forum-beslisboom tegen een vastgelegde lijst.

De Beslisboom Open Standaarden van het Forum Standaardisatie routeert naar een
vaste set standaarden. De dekkingstabel in skills/ls/SKILL.md rust op die set.
Dit script haalt de titels op via de JSON:API en vergelijkt ze met
scripts/forum_standards.json:

- **toegevoegd**: staat in de beslisboom, niet in de vastgelegde lijst
- **verwijderd**: staat in de vastgelegde lijst, niet meer in de beslisboom

Achtergrond: de API zat tot 2026-10-09 in de content-monitoring op body-hash.
Die vuurde veertien keer zonder dat de lijst veranderde, dus de URL is daar
uitgesloten. Deze controle vergelijkt alleen wat ertoe doet: welke standaarden
erin staan.

Gebruik:
    uv run python scripts/check_forum_standards.py            # vergelijk
    uv run python scripts/check_forum_standards.py --update   # leg huidige lijst vast
"""

import argparse
import json
import sys
from pathlib import Path

import requests

BASELINE_PATH = Path(__file__).resolve().parent / "forum_standards.json"
API_URL = (
    "https://www.forumstandaardisatie.nl/jsonapi/node/decision_tree"
    "?include=decisionTreeSteps.questions.answers.standards"
    "&fields%5Bnode--decision_tree%5D=title%2CdecisionTreeSteps"
    "&fields%5Bparagraph--decision_tree_step%5D=title%2Cquestions"
    "&fields%5Bparagraph--decision_tree_question%5D=question%2Canswers"
    "&fields%5Bparagraph--decision_tree_answer%5D=answer%2Cstandards"
    "&fields%5Bnode--standaarden%5D=title%2Cpath"
)
STANDARD_TYPE = "node--standaarden"
USER_AGENT = "skills-standaarden-beslisboom-check/1.0"
TIMEOUT = 30


def fetch_standards():
    """Haal de titels van alle standaarden in de beslisboom op. None bij een fout."""
    try:
        response = requests.get(API_URL, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT)
        response.raise_for_status()
        included = response.json().get("included", [])
    except (requests.RequestException, ValueError):
        return None
    titles = {
        item["attributes"]["title"].strip()
        for item in included
        if item.get("type") == STANDARD_TYPE
    }
    return sorted(titles)


def load_baseline(path=BASELINE_PATH):
    return json.loads(path.read_text(encoding="utf-8"))


def compare(baseline, current):
    """Retourneer (toegevoegd, verwijderd) ten opzichte van de vastgelegde lijst."""
    added = sorted(set(current) - set(baseline))
    removed = sorted(set(baseline) - set(current))
    return added, removed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update", action="store_true", help="leg de huidige lijst vast als nieuwe basis"
    )
    args = parser.parse_args()

    current = fetch_standards()
    if not current:
        # Een lege lijst is geen geldige uitkomst: dan is de API of de query stuk.
        print("onbereikbaar: de beslisboom-API gaf geen standaarden terug")
        return 1

    if args.update:
        text = json.dumps(current, ensure_ascii=False, indent=2) + "\n"
        BASELINE_PATH.write_text(text, encoding="utf-8")
        print(f"{len(current)} standaarden vastgelegd in {BASELINE_PATH.name}")
        return 0

    baseline = load_baseline()
    added, removed = compare(baseline, current)
    for title in added:
        print(f"toegevoegd: {title}")
    for title in removed:
        print(f"verwijderd: {title}")
    if added or removed:
        print(f"\nBeslisboom: {len(current)} standaarden, vastgelegd: {len(baseline)}")
        return 1

    print(f"Beslisboom ongewijzigd: {len(current)} standaarden")
    return 0


if __name__ == "__main__":
    sys.exit(main())
