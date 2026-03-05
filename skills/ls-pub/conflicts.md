# Publicatie & Tooling - Bronconflicten

Geconstateerd: 2026-02-21

Dit document beschrijft bekende discrepanties en bewuste keuzes voor de Publicatie-skill.

## GitHub-tags vs. gepubliceerde versies

De publicatie-tooling repositories (respec, Automatisering, etc.) zijn tooling-repos, geen standaard-documenten. Ze hebben geen vastgestelde (DEF) versies op gitdocumentatie.logius.nl.

Er zijn geen bronconflicten geconstateerd. Tooling-versies worden via GitHub Releases beheerd, niet via gitdocumentatie.logius.nl.

## Keuze in SKILL.md

De skill beschrijft de publicatie-tooling en workflows zonder versieclaims voor de tooling zelf. Er zijn geen discrepanties tussen bronnen. Als er in de toekomst versiegebonden tooling-releases komen, moet dit document worden bijgewerkt.

## Ontbrekende licentie in GitHub-repositories

De meeste Logius-standaarden repositories bevatten geen expliciet `LICENSE`-bestand in GitHub. De gepubliceerde standaarden op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl) en [logius-standaarden.github.io](https://logius-standaarden.github.io) vermelden echter CC-BY-4.0 als licentie via de ReSpec-configuratie.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [publicatie](https://github.com/logius-standaarden/publicatie) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Publicatie-Preview](https://github.com/logius-standaarden/Publicatie-Preview) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [ReSpec-template](https://github.com/logius-standaarden/ReSpec-template) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |

### Aandachtspunt

De licentie-informatie in de SKILL.md is gebaseerd op de gepubliceerde ReSpec-documenten. Het verdient aanbeveling dat de repositories expliciet een `LICENSE`-bestand toevoegen om juridische duidelijkheid te bieden, met name voor hergebruik onder artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- GitHub publicatie-tools: https://github.com/logius-standaarden/respec
- GitHub Automatisering: https://github.com/logius-standaarden/Automatisering
- Publicatie-overzicht: https://gitdocumentatie.logius.nl/publicatie/
