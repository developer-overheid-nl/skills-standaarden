#!/usr/bin/env python3
"""Controleer vastgestelde (DEF) versies in de skills tegen gitdocumentatie.logius.nl.

Voor elke `[vX.Y.Z](https://gitdocumentatie.logius.nl/publicatie/<domein>/<slug>/)`
in de skill-bestanden wordt de gepubliceerde pagina opgehaald en vergeleken op:

- **versie**: de versie in de skill vs. de versie die de pagina zelf noemt
- **status**: `specStatus` moet `DEF` zijn; een `VV` (versie ter vaststelling) of
  `WV` (werkversie) hoort niet in een "Vastgesteld"-kolom te staan

Achtergrond: op 2026-09-15 bleek de *latest*-verwijzing van het OIN-Stelsel naar
een VV-versie te wijzen, waardoor de skills een niet-vastgestelde versie als
vastgesteld presenteerden. Zie skills/ls-iam/conflicts.md.

Gebruik:
    uv run python scripts/check_def_versions.py            # alle skills
    uv run python scripts/check_def_versions.py --json     # machineleesbaar
"""

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"
BASE_URL = "https://gitdocumentatie.logius.nl/publicatie/"
USER_AGENT = "skills-standaarden-def-check/1.0"
TIMEOUT = 30

# [v2.2.2](https://gitdocumentatie.logius.nl/publicatie/dk/oin/)
# Ook versie-specifieke paden: .../publicatie/api/adr/2.2.1/
# Alleen een kale versie als linktekst telt als versieclaim: `[v2.2.2](...)`.
# Een beschrijvende linktekst ("v1.1.0 op gitdocumentatie") is proza, geen tabelclaim.
CLAIM_PATTERN = re.compile(
    r"\[v([0-9]+(?:\.[0-9]+)*(?:-[0-9]+)?)\]\("
    r"(https://gitdocumentatie\.logius\.nl/publicatie/[a-z0-9-]+/[a-z0-9-]+/(?:[0-9][^/)]*/)?)\)"
)

CANONICAL_PATTERN = re.compile(r'canonical" href="\./([^"]+)"')
SPEC_STATUS_PATTERN = re.compile(r'"specStatus":\s*"([A-Z]+)"')
TITLE_PATTERN = re.compile(r"<title>([^<]*)</title>", re.IGNORECASE)
# ReSpec-titel eindigt op het versienummer: "Digikoppeling ... REST-API 4.0.1"
TITLE_VERSION_PATTERN = re.compile(r"([0-9]+(?:\.[0-9]+)*(?:-[0-9]+)?)\s*$")


def fetch(url):
    """Haal een pagina op; geef de body terug of None bij een fout."""
    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None


def resolve_published(url):
    """Volg de latest-redirect en lees versie + specStatus van de doelpagina.

    Geeft (versie, spec_status, resolved_url) terug. De pagina op het domeinpad is
    meestal een redirect-stub naar de laatste versie; soms staat de inhoud er direct.
    """
    body = fetch(url)
    if body is None:
        return None, None, url

    canonical = CANONICAL_PATTERN.search(body)
    if canonical:
        target = canonical.group(1).strip("./").rstrip("/")
        resolved = f"{url.rstrip('/')}/{target}/"
        body = fetch(resolved)
        if body is None:
            return None, None, resolved
        url = resolved

    spec_status = None
    match = SPEC_STATUS_PATTERN.search(body)
    if match:
        spec_status = match.group(1)

    # De <title> is leidend voor de versie: publishVersion noemt soms de vorige versie.
    version = None
    title = TITLE_PATTERN.search(body)
    if title:
        version_match = TITLE_VERSION_PATTERN.search(title.group(1).strip())
        if version_match:
            version = version_match.group(1)

    return version, spec_status, url


def collect_claims():
    """Verzamel alle DEF-versieclaims uit de skill-bestanden, gegroepeerd per URL."""
    claims = {}
    for path in sorted(SKILLS_DIR.rglob("*.md")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for version, url in CLAIM_PATTERN.findall(line):
                location = f"{path.relative_to(SKILLS_DIR.parent)}:{line_number}"
                claims.setdefault(url, []).append((version.strip(), location))
    return claims


def check(url, claimed):
    """Vergelijk de claims voor één URL met de gepubliceerde pagina."""
    published, spec_status, resolved = resolve_published(url)
    problems = []

    if published is None:
        problems.append(
            {
                "soort": "onbereikbaar",
                "melding": f"kon de gepubliceerde versie niet lezen op {resolved}",
            }
        )
        return problems, published, spec_status

    if spec_status is not None and spec_status != "DEF":
        problems.append(
            {
                "soort": "status",
                "melding": (
                    f"{resolved} heeft specStatus {spec_status}, geen DEF; "
                    "een niet-vastgestelde versie hoort niet in een Vastgesteld-kolom"
                ),
            }
        )

    for version, location in claimed:
        if version.lstrip("v") != published:
            problems.append(
                {
                    "soort": "versie",
                    "melding": (
                        f"{location} noemt v{version.lstrip('v')}, gepubliceerd is {published}"
                    ),
                }
            )

    return problems, published, spec_status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="output als JSON in plaats van tekst")
    args = parser.parse_args()

    claims = collect_claims()
    if not claims:
        print("Geen DEF-versieclaims gevonden in de skills.", file=sys.stderr)
        return 0

    results = {}
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(check, url, claimed): url for url, claimed in claims.items()}
        for future in futures:
            url = futures[future]
            problems, published, spec_status = future.result()
            results[url] = {
                "problemen": problems,
                "gepubliceerd": published,
                "spec_status": spec_status,
            }

    failures = {url: data for url, data in results.items() if data["problemen"]}

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False, sort_keys=True))
        return 1 if failures else 0

    for url in sorted(failures):
        print(f"\n{url}")
        for problem in failures[url]["problemen"]:
            print(f"  [{problem['soort']}] {problem['melding']}")

    checked = len(results)
    if failures:
        print(f"\n{len(failures)} van {checked} gecontroleerde publicaties wijkt af.")
        return 1

    print(f"Alle {checked} gecontroleerde publicaties komen overeen (specStatus DEF).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
