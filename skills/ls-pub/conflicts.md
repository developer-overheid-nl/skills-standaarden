# Publicatie & Tooling - Bronconflicten

Geconstateerd: 2026-02-21

Dit document beschrijft bekende discrepanties en bewuste keuzes voor de Publicatie-skill.

## GitHub-tags vs. gepubliceerde versies

De publicatie-tooling repositories (respec, Automatisering, etc.) zijn tooling-repos, geen standaard-documenten. Ze hebben geen vastgestelde (DEF) versies op gitdocumentatie.logius.nl.

Er zijn geen bronconflicten geconstateerd. Tooling-versies worden via GitHub Releases beheerd, niet via gitdocumentatie.logius.nl.

## pubDomain `ftv` (Federatieve Toegang Verlening)

Geconstateerd: 2026-03-28

In maart 2026 is `ftv` als nieuw pubDomain toegevoegd aan `organisation-config.mjs` ([PR #65](https://github.com/logius-standaarden/publicatie/pull/65)). De authorization-decision-log is verhuisd van pubDomain `dk` (Digikoppeling) naar `ftv` met shortName `adl`. De oude `dk/authorization-decision-log/` directory is verwijderd uit de publicatie-repo.

Sinds april 2026 (commit 6422959) is de email-mapping in organisation-config.mjs herschreven van een dictionary-lookup naar expliciete if/else branches. `ftv` valt in de default-branch en krijgt `api@logius.nl` als contactadres en `"API"` als technisch overleg. Daarnaast voegt de config nu `emailForConsultation` en `technischOverleg` toe aan de ReSpec-configuratie voor gebruik bij het aanmaken van consultatie-READMEs.

## Keuze in SKILL.md

De skill beschrijft de publicatie-tooling en workflows zonder versieclaims voor de tooling zelf. Er zijn geen discrepanties tussen bronnen. Als er in de toekomst versiegebonden tooling-releases komen, moet dit document worden bijgewerkt.

## Licentie-status GitHub-repositories

Sommige repositories bevatten een W3C Software License (afkomstig van het ReSpec-template), terwijl de gepubliceerde standaarden CC-BY-4.0 vermelden via de ReSpec-configuratie. Andere repositories hebben geen expliciet `LICENSE`-bestand.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [publicatie](https://github.com/logius-standaarden/publicatie) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Publicatie-Preview](https://github.com/logius-standaarden/Publicatie-Preview) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [ReSpec-template](https://github.com/logius-standaarden/ReSpec-template) | W3C Software License | CC-BY-4.0 (ReSpec) | Discrepantie |
| [ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius) | W3C Software License | CC0-1.0 (ReSpec) | Afwijkend |
| [Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [respec](https://github.com/logius-standaarden/respec) | W3C Software License | N.v.t. (tooling) | OK |
| [automatisering-test](https://github.com/logius-standaarden/automatisering-test) | W3C Software License | N.v.t. (tooling) | OK |

### Aandachtspunt

De W3C Software License is afkomstig van het ReSpec-template en dekt de tooling-code. De gepubliceerde standaard-inhoud valt onder CC-BY-4.0 (vermeld in de ReSpec-configuratie). Voor repositories zonder LICENSE-bestand verdient het aanbeveling om expliciet een licentie toe te voegen, relevant voor artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- GitHub publicatie-tools: https://github.com/logius-standaarden/respec
- GitHub Automatisering: https://github.com/logius-standaarden/Automatisering
- Publicatie-overzicht: https://gitdocumentatie.logius.nl/publicatie/
