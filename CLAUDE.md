# Logius Standaarden Plugin - Werkinstructies

## Taal

Alle content in deze repo is in het **Nederlands**: skill descriptions, body tekst, commit messages, en documentatie. Gebruik Nederlands tenzij de gebruiker expliciet in het Engels communiceert.

## Repo structuur

- `.claude-plugin/plugin.json` - Plugin manifest (versie wordt automatisch gebumpt door release-please)
- `skills/ls/SKILL.md` - Meta-skill (overzicht, routing)
- `skills/ls-<domein>/SKILL.md` - Domein-skills (9 stuks)
- `skills/ls-<domein>/reference.md` - Achtergrondinfo per domein (optioneel)
- `skills/ls-<domein>/conflicts.md` - Bronconflicten en gemaakte keuzes per domein
- `scripts/extract_urls.py` - Extraheert monitorbare URLs uit skill-bestanden
- `scripts/monitor_content.py` - Detecteert content-wijzigingen (GitHub API + HTTP checks)
- `tests/` - Pytest tests voor de scripts
- `.github/workflows/ci.yml` - CI: structuurvalidatie, ruff, markdownlint, pytest
- `.github/workflows/release-please.yml` - Automatische releases via conventional commits
- `.github/workflows/monitoring-content.yml` - Dagelijkse content monitoring (07:00 UTC)
- `.github/workflows/monitoring-links.yml` - Dagelijkse link checks met lychee (06:00 UTC)
- `.github/workflows/labeler.yml` - Automatische PR-labels op basis van gewijzigde bestanden

## Conventies voor skills

### SKILL.md opbouw
1. YAML frontmatter met `name`, `description`, `model: sonnet`, `allowed-tools`
2. Agent-instructie (2-3 zinnen, vetgedrukt: wanneer wordt deze skill gebruikt, wat moet de agent doen)
3. Korte intro (wat is dit domein, link naar Forum Standaardisatie)
4. Versiemodel (altijd: WV/CV/VV/DEF kanalen uitleggen + Forum Standaardisatie status)
5. Repository tabel(len) — gescheiden in Kernspecificaties en Aanvullende documenten
6. Beslisboom / keuzematrix (waar relevant)
7. Implementatievoorbeelden - realistische code in Python, JavaScript, curl, XML/JSON
8. Foutafhandeling - domein-specifieke error responses, status codes
9. Achtergrondinfo (verwijzing naar reference.md en conflicts.md)

Elke skill moet genoeg bevatten zodat een agent standaard-conforme code kan genereren zonder externe bronnen op te halen. Encyclopedische uitleg hoort in `reference.md`, niet in `SKILL.md`.

### Repository tabel format

```markdown
| Repository | Beschrijving | Vastgesteld (DEF) | Draft (WV) |
|-----------|-------------|-----------------|-----------|
| [Naam](https://github.com/logius-standaarden/REPO) | Omschrijving | [vX.Y.Z](https://gitdocumentatie.logius.nl/publicatie/domein/slug/) | [Draft](https://logius-standaarden.github.io/REPO/) |
```

- Versies altijd als link: `[vX.Y.Z](gitdocumentatie-url)`
- Geen vastgestelde versie beschikbaar: gebruik `—` (em-dash)
- Gearchiveerde repos in aparte tabel onderaan met markering

### Versies en bronnen van waarheid

- **gitdocumentatie.logius.nl** is de bron van waarheid voor vastgestelde (DEF) versies
- GitHub-tags lopen vaak achter op gepubliceerde versies — dit is een bekend beheerproces-issue
- Versieformat: semantic versioning `vX.Y.Z` (uitzonderingen documenteren in conflicts.md)
- Versienummers in SKILL.md moeten overeenkomen met wat er op gitdocumentatie staat
- Bij een monitoring issue over een nieuwe tag/commit: controleer of de versie in SKILL.md nog klopt

### reference.md patroon
Achtergrondkennis die niet direct nodig is voor code-generatie wordt verplaatst naar `reference.md` in dezelfde skill-directory. Denk aan:
- Architectuurbeschrijvingen en conceptuele uitleg
- Historische context en levensfasen
- Praktijkvoorbeelden en case studies
- Gedetailleerde protocol-uitleg
- Handige commando's voor repo-exploratie

De `SKILL.md` verwijst onderaan naar `reference.md` met een korte zin.

### conflicts.md patroon
Elk domein heeft een `conflicts.md` met vaste structuur:
1. Header met datum: `Geconstateerd: YYYY-MM-DD`
2. Patroon-beschrijving (welk type discrepantie)
3. Discrepanties tabel: Repository | Gepubliceerde versie (DEF) | Laatste GitHub-tag | Discrepantie
4. Details per repo (alleen bij afwijkingen)
5. **"Keuze in SKILL.md"** sectie (altijd): welke bron leidend is en wanneer herbeoordeling nodig is

De `SKILL.md` verwijst naar `conflicts.md` in de Achtergrondinfo-sectie.

### Description triggers
Descriptions bevatten zowel Nederlandse als technische Engelse triggerwoorden zodat de skill bij relevante vragen wordt geactiveerd.

### Allowed tools
Pas per skill aan. Niet elke skill heeft alle tools nodig. Standaard set:
- `Bash(gh api *)`, `Bash(gh issue list *)`, `Bash(gh pr list *)`, `Bash(gh search *)`
- `Bash(curl -s *)`, `WebFetch(*)`

Extra tools alleen waar relevant:
- `Bash(npx @stoplight/spectral-cli *)` alleen voor `/ls-api`
- `Bash(npx markdownlint *)`, `Bash(npx @axe-core/cli *)`, `Bash(npx muffet *)` alleen voor `/ls-pub`

### Maximale omvang
SKILL.md bestanden mogen maximaal **500 regels** bevatten. Grotere content hoort in `reference.md`.

## Content strategie

**On-demand ophalen, niet opslaan.** De GitHub repos van logius-standaarden zijn de bron van waarheid. Skills bevatten samenvattingen en structuur; actuele content wordt live opgehaald via `gh api` of `WebFetch`.

## GitHub organisatie

Alle repos staan onder: `https://github.com/logius-standaarden/`
Publicaties op: `https://logius-standaarden.github.io/<repo>/`
Vastgestelde publicaties op: `https://gitdocumentatie.logius.nl/publicatie/`

**Let op:** `gitdocumentatie.logius.nl/publicatie/<prefix>/` (directory-niveau) geeft 403 — gebruik altijd de volledige sub-pad URLs (bijv. `/publicatie/dk/architectuur/`, niet `/publicatie/dk/`).

## Development

### Vereisten

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) als package manager
- `uv sync` om dependencies te installeren

### Linting en tests

```bash
uv run ruff check scripts/ tests/       # Linting
uv run ruff format --check scripts/ tests/  # Format check
uv run pytest -v                         # Tests
```

Pre-commit hooks draaien automatisch ruff + markdownlint bij elke commit.

### CI/CD

**Branch protection** is actief op `main` met verplichte status checks: `validate`, `lint-python`, `lint-markdown`, `test-python`. Directe pushes naar main zijn geblokkeerd — alle wijzigingen gaan via PRs.

**Releases** worden automatisch beheerd door [release-please](https://github.com/googleapis/release-please):
1. Gebruik [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `chore:`, `docs:`
2. release-please maakt automatisch een Release PR aan met gebumpte versies en CHANGELOG
3. Bij merge van Release PR: GitHub Release + git tag + versie gebumpt in `plugin.json`, `pyproject.toml`, `publiccode.yml`

**Belangrijk:** Release PRs van release-please hebben geen CI checks (GITHUB_TOKEN pushes triggeren geen workflows). Push een lege commit om CI te triggeren:
```bash
gh pr checkout <nr> && git commit --allow-empty -m "chore: trigger CI" && git push && git checkout main
```

**Strict branch protection** vereist dat branches up-to-date zijn. Na merges van andere PRs: `gh pr update-branch <nr>` voordat je kunt mergen.

### Monitoring

**Content monitoring** (`scripts/monitor_content.py`) draait dagelijks om 07:00 UTC:
- Checkt GitHub repos via API (commit SHA, tags, archived status)
- Checkt HTTP resources via ETag/Last-Modified + SHA256 body hash
- Body hash is leidend — ETag/Last-Modified wijzigingen worden genegeerd als body hash ongewijzigd is
- `normalize_html()` filtert dynamische content: timestamps, nonces, cache-busters, Drupal CMS hashes
- Checksums state wordt opgeslagen in GitHub Actions cache (niet in de repo)
- Maakt GitHub Issues aan bij gedetecteerde wijzigingen (na 3 opeenvolgende failures voor errors)

**Link monitoring** (`monitoring-links.yml`) draait dagelijks om 06:00 UTC met lychee.

### Monitoring issues afhandelen

Wanneer de monitoring een GitHub Issue aanmaakt, volg dit proces:

**Content gewijzigd (body hash verschilt / nieuwe commit / nieuwe tag):**
1. Bekijk de wijziging: wat is er veranderd in de bron?
2. Controleer of versienummers in `SKILL.md` nog kloppen met gitdocumentatie.logius.nl
3. Update `SKILL.md` repository tabel als er een nieuwe versie is
4. Update `conflicts.md` als de discrepantie tussen tag en publicatie is veranderd
5. Sluit het issue met een verwijzing naar de PR

**Bron onbereikbaar (HTTP error na 3 dagen):**
1. Controleer of de URL nog correct is (typo? verhuisd? directory-niveau 403?)
2. Als de URL is verhuisd: update in de skill-bestanden
3. Als de bron tijdelijk down is: wacht en sluit het issue als het weer werkt
4. Als de bron permanent weg is: verwijder of vervang de URL in de skill-bestanden

**False positive (dynamische content, geen echte wijziging):**
1. Identificeer de oorzaak (CMS cache rebuild, nonce rotatie, timestamp, etc.)
2. Voeg een normalisatieregel toe aan `normalize_html()` in `scripts/monitor_content.py`
3. Voeg tests toe in `tests/test_monitor_content.py`
4. Als een hele URL niet gemonitord hoeft te worden: voeg een exclude-patroon toe aan `EXCLUDE_PATTERNS` in `scripts/extract_urls.py`
5. Sluit het false positive issue

## Plugin testen

Verificatievragen:
- "Welke Logius standaarden zijn er?" -> moet `/ls` triggeren
- "Wat zijn de API Design Rules?" -> moet `/ls-api` triggeren
- "Toon de laatste wijzigingen aan Digikoppeling" -> moet `/ls-dk` triggeren
- "Hoe stel ik een beheermodel op?" -> moet `/ls-bomos` triggeren
- "Run een WCAG check" -> moet `/ls-pub` triggeren (niet ls-dk of ls-api!)
