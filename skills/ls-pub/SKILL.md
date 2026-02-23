---
name: ls-pub
description: "Gebruik deze skill wanneer de gebruiker vraagt over 'publicatie', 'ReSpec', 'documentatie tooling', 'GitHub Actions workflows', 'build workflow', 'check workflow', 'publish workflow', 'tech radar', 'WCAG check', 'markdownlint', 'markdown lint', 'kwaliteitscheck', 'Muffet', 'link validatie', 'automatisering', 'HTML generatie', 'PDF generatie', 'accessibility check', 'a11y'. Niet voor API linting (zie ls-api) of code linting."
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - Bash(gh issue list *)
  - Bash(gh pr list *)
  - Bash(gh search *)
  - Bash(curl -s *)
  - Bash(npx respec *)
  - Bash(npx markdownlint *)
  - Bash(npx @axe-core/cli *)
  - Bash(npx muffet *)
  - Bash(npx http-server *)
  - Bash(node *)
  - WebFetch(*)
---

# Publicatie & Tooling

**Agent-instructie:** Deze skill is de centrale plek voor publicatie-tooling en kwaliteitschecks van alle Logius standaarden. Gebruik deze skill wanneer de gebruiker een document wil bouwen, valideren (WCAG, markdown lint, link check), publiceren, of een nieuw ReSpec-document wil opzetten. Dit is de ENIGE skill met markdownlint, axe-core en muffet tools.

## Versiemodel van standaarden

De publicatie-tooling ondersteunt het versiemodel van Logius-standaarden via de `specStatus` configuratiewaarde in ReSpec:

| specStatus | Betekenis | Publicatiekanaal |
|-----------|-----------|-----------------|
| `WV` | Werkversie (draft) | `logius-standaarden.github.io` |
| `CV` | Consultatieversie | `logius-standaarden.github.io/Openbare-Consultaties/` (automatisch op `consultatie/*` branches) |
| `VV` | Versie ter vaststelling | `gitdocumentatie.logius.nl` |
| `DEF` | Vastgestelde versie | `gitdocumentatie.logius.nl` |

## Repositories

| Repository | Beschrijving | Publicatie |
|-----------|-------------|-----------|
| [publicatie](https://github.com/logius-standaarden/publicatie) | Centrale publicatie-repo: alle vastgestelde standaarden | gitdocumentatie.logius.nl (geen directory listing) |
| [Publicatie-Preview](https://github.com/logius-standaarden/Publicatie-Preview) | Preview-omgeving voor documenten in ontwikkeling | [Lees online](https://logius-standaarden.github.io/Publicatie-Preview/) |
| [respec](https://github.com/logius-standaarden/respec) | Logius fork van W3C ReSpec documentatie-tool | - |
| [ReSpec-template](https://github.com/logius-standaarden/ReSpec-template) | Basis template voor nieuwe ReSpec documenten | [Lees online](https://logius-standaarden.github.io/ReSpec-template/) |
| [ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius) | Logius-specifiek ReSpec template met huisstijl | [Lees online](https://logius-standaarden.github.io/ReSpec-template-Logius/) |
| [Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties) | Gepubliceerde consultatieversies (CV) | [Lees online](https://logius-standaarden.github.io/Openbare-Consultaties/) |
| [Automatisering](https://github.com/logius-standaarden/Automatisering) | Herbruikbare GitHub Actions workflows | - |
| [automatisering-test](https://github.com/logius-standaarden/automatisering-test) | Testomgeving voor de automatiseringsworkflows | - |
| [tech-radar](https://github.com/logius-standaarden/tech-radar) | Technologie radar voor Logius standaarden | [Lees online](https://logius-standaarden.github.io/tech-radar/) |

## ReSpec Documentatie-systeem

ReSpec genereert technische specificaties als HTML en PDF vanuit Markdown. Logius gebruikt een eigen fork met aangepaste huisstijl.

### Hoe ReSpec werkt

Het hoofdbestand `index.html` laadt de ReSpec-engine en verwijst via `data-include` naar losse Markdown-bestanden per hoofdstuk:

```html
<section data-include-format="markdown" data-include="ch01.md"></section>
<section data-include-format="markdown" data-include="ch02.md"></section>
```

### ReSpec Configuratie (`js/config.mjs`)

Nieuwe documenten gebruiken ES-module formaat (`config.mjs`); oudere repos kunnen nog `config.js` bevatten.

```javascript
// js/config.mjs (nieuw, aanbevolen formaat)
import { loadRespecWithConfiguration } from
  "https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs";

loadRespecWithConfiguration({
  useLogo: true,
  useLabel: true,
  license: "cc-by",
  specStatus: "WV",        // WV=Werkversie, CV=Consultatieversie, VV=Versie ter vaststelling, DEF=Vastgestelde versie
  specType: "HR",           // HR=Handreiking, ST=Standaard, PR=Praktijkrichtlijn, IM=Informatiemodel
  pubDomain: "dk",
  shortName: "template",
  publishDate: "2023-06-21",
  publishVersion: "0.0.3",
  editors: [{ name: "Logius Standaarden", company: "Logius", companyURL: "https://logius.nl" }],
  authors: [{ name: "Logius Standaarden", company: "Logius", companyURL: "https://logius.nl" }],
  github: "https://github.com/logius-standaarden/ReSpec-template",
});
```

> **Let op:** Oudere repos gebruiken `config.js` met `var respecConfig = { ... }` syntax. Die bevat soms extra velden zoals `content`, `alternateFormats` en `postProcess` die niet in de `config.mjs`-variant voorkomen.

### Directory Structuur

```
.github/workflows/    # CI/CD workflows (verwijzen naar Automatisering repo)
js/config.mjs         # ReSpec configuratie (of config.js bij oudere repos)
media/                # Afbeeldingen, diagrammen
ch01.md, ch02.md      # Hoofdstukken
abstract.md           # Samenvatting
index.html            # ReSpec entry point
```

## GitHub Actions Workflows (Automatisering repo)

Alle standaarden-repos roepen centrale workflows aan uit de `Automatisering` repo.

### build.yml - Document Generatie

1. Branch-detectie: `consultatie/*` branches krijgen automatisch `specStatus: "cv"` (via sed op `config.mjs`)
2. HTML generatie: `npx respec --localhost --src index.html --out ~/static/index.html --haltonwarn`
3. PDF generatie via Puppeteer/headless Chrome (met `scripts/pdf.js`)
4. Cache opslag als GitHub Actions cache

### check.yml - Kwaliteitschecks (3 parallelle checks)

1. **WCAG check**: `npx @axe-core/cli http://localhost:8080/index.html --tags wcag2aa` (geautomatiseerde check; dekt ~30% van WCAG-criteria, handmatige toetsing blijft nodig). axe-core is een van meerdere tools die gestandaardiseerde [W3C ACT Rules](https://www.w3.org/WAI/standards-guidelines/act/rules/) implementeren; alternatieven zijn o.a. Alfa (Siteimprove) en Linter van het NL Design System.
2. **Markdown lint**: `npx markdownlint-cli sections/`
3. **Link validatie**: Muffet valideert alle hyperlinks

### publish.yml - Publicatie

Bevat meerdere jobs afhankelijk van de context:
- **Release** (push naar `main`/`master`): publiceert naar de centrale `publicatie` repo (gitdocumentatie.logius.nl)
- **Deploy develop** (push naar `develop`): publiceert naar GitHub Pages van de standaarden-repo zelf
- **Preview** (pull request): publiceert een preview naar de `Publicatie-Preview` repo
- **Consultatie** (`consultatie/*` branches): publiceert naar de `Openbare-Consultaties` repo

### link-checker.yml - Gepubliceerde Links Controleren

Controleert periodiek of de gepubliceerde versie op gitdocumentatie.logius.nl geen dode links bevat. Stuurt een e-mail bij gevonden fouten.

### Calling Workflow Voorbeeld

```yaml
# .github/workflows/build.yml in een standaarden-repo
name: Build document
on:
  push:
    branches: [main, 'consultatie/*']
  pull_request:
    branches: [main]

jobs:
  build:
    uses: logius-standaarden/Automatisering/.github/workflows/build.yml@main
    with:
      workflow_input_file_names: '["index.html"]'
```

## Nieuw Document Starten

1. **Fork het template**: Gebruik [ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius) als basis
2. **Configureer `js/config.mjs`**: Pas `specStatus`, `specType`, `pubDomain`, `shortName`, `title` aan
3. **Schrijf content**: Maak hoofdstukken als losse Markdown-bestanden
4. **Push naar GitHub**: CI/CD bouwt automatisch HTML en PDF

## Checks Lokaal Draaien

```bash
# ReSpec bouwen naar statische HTML
npx respec --src index.html --out output.html

# WCAG Accessibility check (wcag2aa niveau)
npx @axe-core/cli output.html --tags wcag2aa
# ⚠️ Let op: axe-core checkt automatisch ~30% van de WCAG-criteria.
# Een groene check betekent NIET dat je volledig voldoet aan EN 301 549 / WCAG 2.1 AA.
# Handmatige toetsing op alle 55 succescriteria in WCAG 2.1 AA blijft nodig.
# axe-core implementeert W3C ACT Rules (https://www.w3.org/WAI/standards-guidelines/act/rules/)
# Alternatieven: Alfa (Siteimprove), Linter van NL Design System

# Markdown linting
npx markdownlint-cli 'sections/**/*.md'

# Link validatie (start eerst een lokale server)
npx http-server -p 8080 . &
muffet http://localhost:8080/index.html
```

## Foutafhandeling

| Fout | Oorzaak | Oplossing |
|------|---------|----------|
| `ReSpec error: data-include file not found` | Markdown-bestand ontbreekt | Controleer `data-include` verwijzingen |
| `WCAG violation: Images must have alternate text` | Afbeelding zonder alt-tekst | Voeg alt-tekst toe: `![Beschrijving](media/img.svg)` |
| Geen WCAG violations gevonden | axe-core heeft geen fouten gedetecteerd | **Let op:** dit betekent niet dat het document volledig toegankelijk is. axe-core test ~30% van de WCAG 2.1 AA criteria. Toets handmatig op alle 55 succescriteria in WCAG 2.1 AA, waaronder toetsenbordnavigatie, leesbare kopstructuur en logische leesvolgorde. |
| `markdownlint MD013: Line length` | Regel te lang | Breek af op ~120 karakters |
| `muffet: 404 Not Found` | Dode link | Verwijder of update de link |
| `PDF generation failed` | Puppeteer crash | Controleer of document valid HTML genereert |

### Consultatie Branch Gedrag

Op `consultatie/*` branches wordt `specStatus` automatisch overschreven naar `"cv"`. Na merge naar `main` wordt `specStatus` uit `js/config.mjs` gebruikt.

## Achtergrondinfo

Zie [reference.md](reference.md) voor gedetailleerde info over tech radar, label-updates workflow, en workflow-configuratie.
Zie [conflicts.md](conflicts.md) voor bronconflicten en gemaakte keuzes.
