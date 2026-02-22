#!/usr/bin/env python3
"""Extraheer monitorbare URLs uit skill-bestanden.

Scant SKILL.md, reference.md en conflicts.md in de skills-directory.
Classificeert URLs per type (github_repo, published_doc, draft_doc, forum).
Output als platte URL-lijst (voor lychee) of JSON manifest (voor content monitoring).
"""

import argparse
import json
import re
import sys
from pathlib import Path

# URL-patronen per type
URL_PATTERNS = {
    "github_repo": re.compile(r"https://github\.com/logius-standaarden/[A-Za-z0-9._-]+"),
    "published_doc": re.compile(r"https://gitdocumentatie\.logius\.nl/publicatie/[^\s\)\]\"'>]+"),
    "draft_doc": re.compile(r"https://logius-standaarden\.github\.io/[^\s\)\]\"'>]+"),
    "forum": re.compile(r"https://www\.forumstandaardisatie\.nl/[^\s\)\]\"'>]+"),
}

# URLs die geen echte bronnen zijn (voorbeelden, namespaces, etc.)
EXCLUDE_PATTERNS = [
    re.compile(r"https?://example\.com"),
    re.compile(r"https?://api\.example\.com"),
    re.compile(r"https?://.*\.example\.(com|nl|org)"),
    re.compile(r"https?://localhost"),
    re.compile(r"https?://127\.0\.0\.1"),
    re.compile(r"https?://www\.w3\.org/"),
    re.compile(r"https?://schemas\.xmlsoap\.org/"),
    re.compile(r"https?://docs\.oasis-open\.org/"),
    re.compile(r"https?://www\.oasis-open\.org/"),
    re.compile(r"https?://service\.example"),
    re.compile(r"https?://sender\.example"),
    re.compile(r"https?://receiver\.example"),
    re.compile(r"https?://inway\.provider\.example"),
    re.compile(r"https?://manager\.example"),
    re.compile(r"https?://directory\.example"),
    re.compile(r"https?://provider-manager\.example"),
    # Publicatie-Preview verandert by design meerdere keren per dag (preview builds)
    re.compile(r"https?://github\.com/logius-standaarden/Publicatie-Preview"),
]

# Markdown-extractie regex: vindt alle URLs in tekst
URL_RE = re.compile(r"https?://[^\s\)\]\"'>]+")


def is_excluded(url: str) -> bool:
    """Controleer of een URL uitgesloten moet worden."""
    return any(pattern.search(url) for pattern in EXCLUDE_PATTERNS)


def classify_url(url: str) -> str | None:
    """Classificeer een URL. Retourneert None als niet relevant."""
    for url_type, pattern in URL_PATTERNS.items():
        if pattern.match(url):
            return url_type
    return None


def clean_url(url: str) -> str:
    """Verwijder trailing interpunctie en markdown-artefacten."""
    # Verwijder trailing interpunctie die geen deel uitmaakt van de URL
    url = url.rstrip(".,;:!?")
    # Verwijder trailing ) alleen als er geen bijbehorende ( in de URL zit
    while url.endswith(")") and url.count("(") < url.count(")"):
        url = url[:-1]
    # Verwijder trailing ] idem
    while url.endswith("]") and url.count("[") < url.count("]"):
        url = url[:-1]
    # Verwijder eventuele footnote-markers zoals ¹
    url = re.sub(r"[¹²³⁴⁵⁶⁷⁸⁹⁰]+$", "", url)
    # Verwijder trailing /
    url = url.rstrip("/")
    return url


# Regex om GitHub repo-URLs te normaliseren naar base repo pad
_GITHUB_REPO_BASE_RE = re.compile(
    r"(https://github\.com/logius-standaarden/[A-Za-z0-9._-]+)"
    r"(?:/(?:tags|tree|blob|issues|pulls|releases|actions|wiki|discussions|commit|compare)(?:/.*)?)?$"
)


def normalize_github_url(url: str) -> str:
    """Normaliseer GitHub URL naar base repo pad (verwijder /tags, /tree/main, etc.)."""
    match = _GITHUB_REPO_BASE_RE.match(url)
    if match:
        return match.group(1)
    return url


def extract_urls_from_file(
    filepath: Path,
) -> list[dict]:
    """Extraheer en classificeer URLs uit een bestand."""
    results = []
    text = filepath.read_text(encoding="utf-8")

    # Bepaal skill-naam uit pad (skills/<skill-name>/...)
    parts = filepath.parts
    skill_name = None
    for i, part in enumerate(parts):
        if part == "skills" and i + 1 < len(parts):
            skill_name = parts[i + 1]
            break

    for match in URL_RE.finditer(text):
        raw_url = match.group(0)
        url = clean_url(raw_url)

        if is_excluded(url):
            continue

        url_type = classify_url(url)
        if url_type is None:
            continue

        # Normaliseer GitHub URLs naar base repo pad
        if url_type == "github_repo":
            url = normalize_github_url(url)

        results.append(
            {
                "url": url,
                "type": url_type,
                "skill": skill_name,
                "source_file": str(filepath),
            }
        )

    return results


def extract_all(skills_dir: Path) -> list[dict]:
    """Extraheer URLs uit alle skill-bestanden."""
    all_urls: list[dict] = []
    seen_urls: set[str] = set()

    # Scan alle relevante bestanden
    for pattern in ["*/SKILL.md", "*/reference.md", "*/conflicts.md"]:
        for filepath in sorted(skills_dir.glob(pattern)):
            for entry in extract_urls_from_file(filepath):
                if entry["url"] not in seen_urls:
                    seen_urls.add(entry["url"])
                    all_urls.append(entry)

    return all_urls


def output_lychee(urls: list[dict], output: Path | None) -> None:
    """Schrijf platte URL-lijst voor lychee."""
    lines = sorted({entry["url"] for entry in urls})
    text = "\n".join(lines) + "\n"
    if output:
        output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)


def output_json(urls: list[dict], output: Path | None) -> None:
    """Schrijf JSON manifest met classificatie."""
    # Groepeer per URL, met lijst van skills/bronbestanden
    manifest: dict = {}
    for entry in urls:
        url = entry["url"]
        if url not in manifest:
            manifest[url] = {
                "url": url,
                "type": entry["type"],
                "skills": [],
                "source_files": [],
            }
        if entry["skill"] and entry["skill"] not in manifest[url]["skills"]:
            manifest[url]["skills"].append(entry["skill"])
        if entry["source_file"] not in manifest[url]["source_files"]:
            manifest[url]["source_files"].append(entry["source_file"])

    result = {
        "total_urls": len(manifest),
        "by_type": {},
        "urls": list(manifest.values()),
    }

    # Tel per type
    for entry in manifest.values():
        url_type = entry["type"]
        result["by_type"][url_type] = result["by_type"].get(url_type, 0) + 1

    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if output:
        output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extraheer monitorbare URLs uit skill-bestanden")
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=Path("skills"),
        help="Pad naar skills-directory (default: skills)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Outputbestand (default: stdout)",
    )
    parser.add_argument(
        "--format",
        choices=["lychee", "json"],
        default="lychee",
        help="Outputformaat (default: lychee)",
    )
    args = parser.parse_args()

    if not args.skills_dir.is_dir():
        print(f"FOUT: {args.skills_dir} is geen directory", file=sys.stderr)
        sys.exit(1)

    urls = extract_all(args.skills_dir)

    if not urls:
        print("WAARSCHUWING: geen URLs gevonden", file=sys.stderr)
        sys.exit(1)

    if args.format == "lychee":
        output_lychee(urls, args.output)
    else:
        output_json(urls, args.output)

    print(f"Gevonden: {len(urls)} unieke URLs", file=sys.stderr)


if __name__ == "__main__":
    main()
