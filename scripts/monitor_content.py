#!/usr/bin/env python3
"""Detecteer content-wijzigingen in bronnen van Logius standaarden.

Vergelijkt de huidige staat van URLs met een opgeslagen checksums.json.
Verschillende detectiemethoden per URL-type:
- github_repo: GitHub API (commit SHA, laatste tag, archived status)
- published_doc/draft_doc/forum: HTTP ETag/Last-Modified + SHA256 van genormaliseerde body

Maakt GitHub Issues aan bij gedetecteerde wijzigingen.
"""

import argparse
import contextlib
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

import requests

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
CONSECUTIVE_FAILURE_THRESHOLD = 3
USER_AGENT = "logius-standaarden-monitor/1.0"
API_DELAY = 0.5  # Vertraging tussen API calls om rate limits te voorkomen


def github_headers() -> dict:
    """HTTP headers voor GitHub API calls."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def fetch_with_retry(
    url: str,
    headers: dict | None = None,
    max_retries: int = 3,
) -> requests.Response | None:
    """HTTP GET met exponential backoff en Retry-After support."""
    if headers is None:
        headers = {}
    headers.setdefault("User-Agent", USER_AGENT)
    for attempt in range(max_retries):
        delay = min(5 * (2**attempt), 60)
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code in (429, 503):
                retry_after = resp.headers.get("Retry-After")
                wait = int(retry_after) if retry_after else delay
                time.sleep(wait)
                continue
            return resp
        except requests.RequestException:
            if attempt < max_retries - 1:
                time.sleep(delay)
    return None


def extract_visible_text(html: str) -> str:
    """Extraheer alleen de zichtbare tekst uit HTML.

    Verwijdert alle scripts, styles, HTML-tags en normaliseert whitespace.
    Dit is robuust tegen CMS-framework wijzigingen (Drupal cache rebuilds,
    Liferay token rotatie, etc.) omdat alleen de leesbare content overblijft.
    """
    # Gebruik alleen de <body> als die er is
    body_match = re.search(r"<body[^>]*>(.*)</body>", html, flags=re.DOTALL)
    text = body_match.group(1) if body_match else html
    # Verwijder niet-zichtbare elementen
    text = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.DOTALL)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.DOTALL)
    text = re.sub(r"<noscript[^>]*>.*?</noscript>", " ", text, flags=re.DOTALL)
    # Verwijder alle HTML-tags
    text = re.sub(r"<[^>]+>", " ", text)
    # Normaliseer whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def check_github_repo(url: str) -> dict:
    """Check GitHub repo status via API."""
    # Extraheer org/repo uit URL
    match = re.match(r"https://github\.com/([^/]+/[^/]+)", url)
    if not match:
        return {"error": "Ongeldige GitHub URL"}

    repo_path = match.group(1)
    result: dict = {}

    # Haal repo info op (inclusief archived status)
    resp = fetch_with_retry(f"{GITHUB_API}/repos/{repo_path}", headers=github_headers())
    if resp and resp.status_code == 200:
        data = resp.json()
        result["archived"] = data.get("archived", False)
        result["default_branch"] = data.get("default_branch", "main")
    elif resp:
        return {"error": f"HTTP {resp.status_code}"}
    else:
        return {"error": "Geen response"}

    # Haal laatste commit SHA op
    resp = fetch_with_retry(
        f"{GITHUB_API}/repos/{repo_path}/commits?per_page=1",
        headers=github_headers(),
    )
    if resp and resp.status_code == 200:
        commits = resp.json()
        if commits:
            result["last_commit_sha"] = commits[0]["sha"]
            result["last_commit_date"] = commits[0]["commit"]["committer"]["date"]

    # Haal laatste tag op
    resp = fetch_with_retry(
        f"{GITHUB_API}/repos/{repo_path}/tags?per_page=1",
        headers=github_headers(),
    )
    if resp and resp.status_code == 200:
        tags = resp.json()
        if tags:
            result["latest_tag"] = tags[0]["name"]

    return result


def check_http_resource(url: str, hash_body: bool = True) -> dict:
    """Check HTTP resource via ETag/Last-Modified en optioneel body hash."""
    result: dict = {}

    resp = fetch_with_retry(url)
    if resp is None:
        return {"error": "Geen response"}
    if resp.status_code >= 400:
        return {"error": f"HTTP {resp.status_code}"}

    if "ETag" in resp.headers:
        result["etag"] = resp.headers["ETag"]
    if "Last-Modified" in resp.headers:
        result["last_modified"] = resp.headers["Last-Modified"]

    if hash_body and resp.text:
        visible_text = extract_visible_text(resp.text)
        result["body_sha256"] = hashlib.sha256(visible_text.encode()).hexdigest()

    return result


def check_url(entry: dict) -> dict:
    """Check een URL op basis van type."""
    url = entry["url"]
    url_type = entry["type"]

    if url_type == "github_repo":
        return check_github_repo(url)
    else:
        # Alle niet-GitHub URLs als HTTP resource checken
        return check_http_resource(url, hash_body=True)


def load_checksums(path: Path) -> dict:
    """Laad opgeslagen state uit checksums.json."""
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def save_checksums(path: Path, data: dict) -> None:
    """Sla state op naar checksums.json."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def detect_changes(
    url: str,
    current: dict,
    previous: dict | None,
) -> list[str]:
    """Vergelijk huidige staat met opgeslagen staat. Retourneert lijst van wijzigingen."""
    if previous is None:
        return []  # Eerste run = baseline, geen alerts

    changes = []

    # Check voor errors
    if "error" in current:
        return []  # Errors worden apart afgehandeld via failure counter

    prev_state = previous.get("state", {})

    # GitHub repo specifiek - alleen vergelijken als key ook in vorige state bestond
    if (
        "last_commit_sha" in current
        and "last_commit_sha" in prev_state
        and current["last_commit_sha"] != prev_state["last_commit_sha"]
    ):
        changes.append(
            f"Nieuwe commit: {current['last_commit_sha'][:7]} "
            f"({current.get('last_commit_date', 'onbekend')})"
        )
    if (
        "latest_tag" in current
        and "latest_tag" in prev_state
        and current["latest_tag"] != prev_state["latest_tag"]
    ):
        changes.append(
            f"Nieuwe tag: {current['latest_tag']} (was: {prev_state.get('latest_tag', 'geen')})"
        )
    if current.get("archived") and not prev_state.get("archived"):
        changes.append("Repository is gearchiveerd")

    # HTTP resources - alleen vergelijken als de key ook in de vorige state bestond
    body_hash_available = "body_sha256" in current and "body_sha256" in prev_state
    body_hash_changed = body_hash_available and current["body_sha256"] != prev_state["body_sha256"]

    if body_hash_changed:
        changes.append("Content is gewijzigd (body hash verschilt)")

    # ETag/Last-Modified alleen rapporteren als er GEEN body hash beschikbaar is
    # (als body hash wel beschikbaar is, is die leidend en zijn ETag/Last-Modified noise)
    if not body_hash_available:
        if "etag" in current and "etag" in prev_state and current["etag"] != prev_state["etag"]:
            changes.append("ETag gewijzigd")
        if (
            "last_modified" in current
            and "last_modified" in prev_state
            and current["last_modified"] != prev_state["last_modified"]
        ):
            changes.append("Last-Modified gewijzigd")

    return changes


def manage_issue(
    changes: list[dict],
    dry_run: bool = False,
) -> None:
    """Maak of update GitHub Issues voor gedetecteerde wijzigingen."""
    if not changes:
        return

    if dry_run:
        for change in changes:
            print(f"[DRY RUN] Issue: {change['title']}")
            print(f"  Body: {change['body'][:200]}...")
        return

    # Haal alle open monitoring issues op in één keer (vermijdt herhaalde API calls
    # en omzeilt het probleem dat --search faalt op speciale tekens in titels)
    result = subprocess.run(
        [
            "gh",
            "issue",
            "list",
            "--label",
            "monitoring,content-changed",
            "--state",
            "open",
            "--limit",
            "200",
            "--json",
            "number,title",
        ],
        capture_output=True,
        text=True,
    )
    existing_issues: list[dict] = []
    if result.returncode == 0 and result.stdout.strip():
        with contextlib.suppress(json.JSONDecodeError):
            existing_issues = json.loads(result.stdout)

    for change in changes:
        title = change["title"]
        body = change["body"]
        labels = change.get("labels", "monitoring,content-changed")

        # Zoek bestaand issue met exact dezelfde titel
        existing_number = ""
        for issue in existing_issues:
            if issue.get("title") == title:
                existing_number = str(issue["number"])
                break

        if existing_number:
            # Update bestaande issue met comment
            subprocess.run(
                ["gh", "issue", "comment", existing_number, "--body", body],
                capture_output=True,
            )
            print(f"  Updated issue #{existing_number}")
        else:
            # Maak nieuwe issue
            result = subprocess.run(
                [
                    "gh",
                    "issue",
                    "create",
                    "--title",
                    title,
                    "--body",
                    body,
                    "--label",
                    labels,
                ],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                # Voeg nieuw issue toe aan lijst zodat verdere duplicaten in dezelfde run
                # ook gevonden worden
                try:
                    url = result.stdout.strip()
                    number = url.rstrip("/").split("/")[-1]
                    existing_issues.append({"number": int(number), "title": title})
                except (ValueError, IndexError):
                    pass
            print(f"  Created issue: {result.stdout.strip()}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Monitor content-wijzigingen in Logius standaarden bronnen"
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        required=True,
        help="Pad naar JSON manifest (output van extract_urls.py --format json)",
    )
    parser.add_argument(
        "--checksums",
        type=Path,
        default=Path(".github/monitoring/checksums.json"),
        help="Pad naar checksums state file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Alleen wijzigingen detecteren, geen issues aanmaken",
    )
    parser.add_argument(
        "--type",
        choices=["github_repo", "published_doc", "draft_doc", "forum", "all"],
        default="all",
        help="Alleen URLs van dit type controleren",
    )
    args = parser.parse_args()

    # Laad manifest
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    entries = manifest["urls"]

    # Filter op type indien gewenst
    if args.type != "all":
        entries = [e for e in entries if e["type"] == args.type]

    # Laad opgeslagen state
    checksums = load_checksums(args.checksums)
    is_first_run = len(checksums) == 0

    issues_to_create: list[dict] = []
    new_checksums: dict = {}

    total = len(entries)
    for i, entry in enumerate(entries):
        url = entry["url"]
        url_type = entry["type"]
        skills = ", ".join(entry.get("skills", []))

        print(f"[{i + 1}/{total}] {url_type}: {url}")

        # Vertraging tussen requests om rate limits te voorkomen
        if i > 0:
            time.sleep(API_DELAY)

        current = check_url(entry)
        previous = checksums.get(url)

        # Error handling met 3-daagse drempel
        if "error" in current:
            fail_count = (previous or {}).get("consecutive_failures", 0) + 1
            new_checksums[url] = {
                "state": (previous or {}).get("state", {}),
                "consecutive_failures": fail_count,
                "last_error": current["error"],
                "last_checked": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }

            if fail_count >= CONSECUTIVE_FAILURE_THRESHOLD and not is_first_run:
                issues_to_create.append(
                    {
                        "title": f"[monitoring] Bron onbereikbaar: {url}",
                        "body": (
                            f"De bron **{url}** is al {fail_count} dagen onbereikbaar.\n\n"
                            f"- **Type:** {url_type}\n"
                            f"- **Skill(s):** {skills}\n"
                            f"- **Fout:** {current['error']}\n\n"
                            f"Controleer of de URL nog correct is."
                        ),
                        "labels": "monitoring,content-changed",
                    }
                )
            continue

        # Detecteer wijzigingen
        changes = detect_changes(url, current, previous)

        new_checksums[url] = {
            "state": current,
            "consecutive_failures": 0,
            "last_checked": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }

        if changes and not is_first_run:
            change_text = "\n".join(f"- {c}" for c in changes)
            # Gebruik de laatste 2-3 pad-segmenten voor een beschrijvende titel
            url_parts = url.rstrip("/").split("/")
            short_name = "/".join(url_parts[-min(3, len(url_parts)) :])
            issues_to_create.append(
                {
                    "title": f"[monitoring] Content gewijzigd: {short_name} ({skills})",
                    "body": (
                        f"Wijzigingen gedetecteerd voor **{url}**:\n\n"
                        f"{change_text}\n\n"
                        f"- **Type:** {url_type}\n"
                        f"- **Skill(s):** {skills}\n\n"
                        f"**Actie:** controleer of de bijbehorende skill-content nog actueel is."
                    ),
                    "labels": "monitoring,content-changed",
                }
            )

    # Sla state op (niet bij --dry-run, zodat dezelfde wijzigingen opnieuw gedetecteerd worden)
    if not args.dry_run:
        if args.type != "all":
            # Bij type-filter: merge met bestaande state i.p.v. overschrijven
            merged = dict(checksums)
            merged.update(new_checksums)
            save_checksums(args.checksums, merged)
        else:
            save_checksums(args.checksums, new_checksums)

    if is_first_run:
        print(f"\nEerste run: baseline opgeslagen voor {len(new_checksums)} URLs")
    else:
        print(f"\n{len(issues_to_create)} wijzigingen gedetecteerd")

    # Maak issues aan
    manage_issue(issues_to_create, dry_run=args.dry_run)

    # Output samenvatting
    errors = sum(1 for v in new_checksums.values() if v.get("last_error"))
    print(
        f"\nSamenvatting: {total} URLs gecontroleerd, {errors} fouten, "
        f"{len(issues_to_create)} issues"
    )


if __name__ == "__main__":
    main()
