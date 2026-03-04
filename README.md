# Logius Standaarden - Claude Code Plugin

[![EUPL-1.2](https://img.shields.io/badge/licentie-EUPL--1.2-blue.svg)](LICENSE)
[![versie](https://img.shields.io/github/v/tag/developer-overheid-nl/skills-standaarden?label=versie&color=green)](CHANGELOG.md)

Claude Code plugin voor het werken met 77 van de 88 GitHub repositories van [Logius standaarden](https://github.com/logius-standaarden) voor Nederlandse overheidsinteroperabiliteit.

## Installatie

### Globaal installeren (aanbevolen)

Voeg de [overheid-plugins marketplace](https://github.com/developer-overheid-nl/skills-marketplace) toe en installeer de plugin. De skills zijn daarna beschikbaar in elke Claude Code sessie.

```bash
claude plugin marketplace add developer-overheid-nl/skills-marketplace
claude plugin install logius-standaarden@overheid-plugins
```

### Per sessie laden

Alternatief: laad de plugin alleen voor de huidige sessie via `--plugin-dir`:

```bash
git clone https://github.com/developer-overheid-nl/skills-standaarden.git
claude --plugin-dir ./skills-standaarden
```

## Wat doet deze plugin?

De plugin biedt 10 skills die een AI-agent helpen bij:

- **Implementeren** van standaard-conforme code (OAuth, Digikoppeling, CloudEvents, etc.)
- **Navigeren** door 77 repositories, gegroepeerd in 9 domeinen
- **Ophalen** van actuele content via `gh api` en `WebFetch`
- **Valideren** met Spectral linter, WCAG checks, markdown linting (via `/ls-pub`)
- **Kiezen** van het juiste profiel of protocol via beslisbomen en keuzematrices

### Instructie-gedreven aanpak

Skills zijn geschreven als **agent-instructies**, niet als encyclopedie. Elke SKILL.md bevat:

1. Wanneer de skill gebruikt moet worden
2. Repository-overzicht
3. Beslisbomen en keuzematrices
4. Werkende implementatievoorbeelden
5. Domein-specifieke foutafhandeling

Achtergrondkennis (architectuur, protocollen, concepten) staat in `reference.md` bestanden die de agent kan raadplegen wanneer nodig.

## Skills

| Skill | Domein | Repos | Beschrijving |
|-------|--------|-------|-------------|
| `/ls` | Overzicht | - | Meta-skill: routeert naar het juiste domein |
| `/ls-dk` | Digikoppeling | 17 | Beveiligde gegevensuitwisseling (REST, ebMS2, WUS, GB), OIN |
| `/ls-api` | API Design Rules | 9 | NL GOV API-standaard, Spectral linter, referentie-implementaties |
| `/ls-iam` | Identity & Access Management | 8 | OAuth 2.0 NL, OpenID Connect, AuthZEN, SAML |
| `/ls-fsc` | Federated Service Connectivity | 7 | Federatief netwerk: inway/outway, contracten, service directory |
| `/ls-logboek` | Logboek Dataverwerkingen | 8 | AVG-logging, OpenTelemetry, W3C Trace Context |
| `/ls-notif` | CloudEvents & Notificaties | 4 | NL GOV CloudEvents profiel, pub/sub |
| `/ls-bomos` | BOMOS Governance | 10 | Beheer- en Ontwikkelmodel voor Open Standaarden |
| `/ls-egov` | E-Government Services | 6 | Terugmelding, Digimelding, e-procurement |
| `/ls-pub` | Publicatie & Tooling | 9 | ReSpec, GitHub Actions, WCAG checks, markdown lint |

## Voorbeeldvragen

```
Welke Logius standaarden zijn er?
Wat zijn de API Design Rules?
Toon de laatste wijzigingen aan de Digikoppeling architectuur
Run de Spectral linter op mijn OpenAPI spec
Hoe implementeer ik OAuth 2.0 NL profiel?
Wat is het verschil tussen ebMS2 en REST koppelvlak?
Hoe stel ik een BOMOS beheermodel op?
Run een WCAG check op mijn document
```

## Structuur

```
.claude-plugin/
  plugin.json              # Plugin manifest
skills/
  ls/SKILL.md              # Meta/overzicht skill
  ls-api/
    SKILL.md               # Agent-instructies en implementatievoorbeelden
    reference.md           # Achtergrondkennis en repo-exploratie
    conflicts.md           # Bronconflicten en gemaakte keuzes
  ls-dk/
    SKILL.md
    reference.md
    conflicts.md
  ...                      # Idem voor alle 9 domein-skills
```

## Content strategie

Skills bevatten compacte agent-instructies, beslisbomen en implementatievoorbeelden. Encyclopedische achtergrondkennis staat in `reference.md`. Bronconflicten en bewuste keuzes (bijv. discrepanties tussen GitHub-tags en gepubliceerde versies) zijn gedocumenteerd in `conflicts.md`. Actuele content wordt on-demand opgehaald via `gh api` en `WebFetch` - de GitHub repos zelf zijn de bron van waarheid.

## Versioning

De hele plugin wordt als 1 eenheid geversioned (semver):

- **Patch** (`0.3.1`): Typos, broken links, kleine correcties
- **Minor** (`0.4.0`): Content sync met upstream standaard-wijzigingen, nieuwe voorbeelden
- **Major** (`1.0.0`): Stabiele release, breaking changes in structuur

## Vereisten

- [Claude Code](https://code.claude.com/docs) CLI
- [GitHub CLI](https://cli.github.com/) (`gh`) - voor het ophalen van repo-content
- Node.js - voor ReSpec, Spectral en andere npm-tools (optioneel, voor validatie)

## Disclaimer

Dit is een experimenteel project om te leren hoe generatieve AI gestuurd kan worden om te werken volgens de kaders, richtlijnen en standaarden van de overheid. De skills in deze plugin zijn informatieve samenvattingen — **niet** de officiële standaarden zelf. De definities op [Forum Standaardisatie](https://www.forumstandaardisatie.nl/open-standaarden) en [Logius](https://www.logius.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Rijksbrede beleidskader voor generatieve AI](https://www.government.nl/documents/policy-notes/2025/01/31/government-wide-position-on-the-use-of-generative-ai). Zie [DISCLAIMER.md](DISCLAIMER.md) voor de volledige disclaimer.

## Licentie

[EUPL-1.2](LICENSE) - European Union Public Licence
