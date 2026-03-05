# API Design Rules - Bronconflicten

Geconstateerd: 2026-02-21

Dit document beschrijft bekende discrepanties tussen GitHub-repository tags en de gepubliceerde versies op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl). De **gepubliceerde versie op gitdocumentatie.logius.nl is leidend** voor DEF-versies.

## Discrepanties

| Repository | Gepubliceerde versie (DEF) | Laatste GitHub-tag | Discrepantie |
|-----------|---------------------------|-------------------|-------------|
| [API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial) | [v1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3/) | `1.0.2` | Tag achter: publicatie v1.0.3 vs tag 1.0.2 |
| [ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel) | [v1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0/) | `10r4` | Tag-formaat afwijkend: publicatie v1.0 vs tag `10r4` |

### Details API-mod-geospatial

- **Alle bekende tags:** `1.0.2`, `1.0.1`, `1.0.0`
- **Geen GitHub Releases** aangemaakt
- De tag `1.0.2` bestaat op GitHub, maar de gepubliceerde versie op gitdocumentatie is `1.0.3`
- Er is geen tag `1.0.3` in de repository
- Dit wijst erop dat de publicatie v1.0.3 is doorgevoerd zonder een bijbehorende Git-tag aan te maken

### Details ADR-Beheermodel

- **Enige tag:** `10r4` — afwijkend formaat, geen semantic versioning
- De repository is **gearchiveerd** en vervangen door API-Standaarden-Beheermodel
- De gepubliceerde DEF-versie op gitdocumentatie is `v1.0`
- Het tag-formaat `10r4` komt waarschijnlijk uit een ouder versiebeheersysteem

## Transport Security module: dubbelzinnige status

De Transport Security module (API-mod-transport-security) heeft een dubbelzinnige status in ADR v2.1.0:

| Aspect | Status | Bron |
|--------|--------|------|
| GitHub-repository | **Gearchiveerd** | https://github.com/logius-standaarden/API-mod-transport-security |
| Inhoud in ADR v2.1.0 | **Ingebed** als sectie 3.8 met eigen regels (`/core/transport/*`) | https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0/ |
| Leeswijzer ADR v2.1.0 | Module v1.0 staat **normatief vermeld** | https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0/ |

### Analyse

De module-inhoud is feitelijk in de hoofdspecificatie opgenomen, maar de leeswijzer van v2.1.0 vermeldt de module v1.0 nog steeds als normatief. De repo is gearchiveerd, wat suggereert dat het Technisch Overleg de module als afgehandeld beschouwt. De vermelding in de leeswijzer is waarschijnlijk een redactioneel overblijfsel.

### Keuze in SKILL.md

De SKILL.md beschrijft de drieledige situatie: inhoud ingebed in v2.1.0, module nog normatief in leeswijzer, repo gearchiveerd. Als de leeswijzer wordt bijgewerkt, moet deze beschrijving opnieuw worden beoordeeld.

## ADR werkversie-nummering op draft-pagina

De draft-pagina op GitHub Pages ([logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules/)) toont in de ReSpec-configuratie nog versienummer '2.1.0', terwijl v2.1.0 ook de huidige DEF-versie is. De draft betreft echter werk-in-uitvoering richting de volgende release — het versienummer in ReSpec is simpelweg nog niet opgehoogd. Dit is een bekend patroon bij Logius-standaarden: de ReSpec `defined_in` configuratie wordt pas bijgewerkt wanneer de nieuwe versie wordt vastgesteld.

### Keuze in SKILL.md

De SKILL.md beschrijft de werkversie als "lopende ontwikkeling richting de volgende release" zonder een specifiek versienummer voor de draft. Als de ReSpec-configuratie wordt bijgewerkt naar een nieuw versienummer, moet deze beschrijving opnieuw worden beoordeeld.

## Keuze in SKILL.md

De skill gebruikt versienummers van gitdocumentatie.logius.nl als bron van waarheid voor vastgestelde (DEF) versies. De GitHub-tag van API-mod-geospatial loopt één patchversie achter; dit is hetzelfde patroon als bij andere Logius-standaarden repos (zie ook [ls-dk/conflicts.md](../ls-dk/conflicts.md)). ADR-Beheermodel heeft een afwijkend tag-formaat (`10r4` vs DEF v1.0). Transport Security wordt beschreven met de feitelijke drieledige status (ingebed, leeswijzer, gearchiveerd). Als tags worden bijgewerkt of de leeswijzer wordt aangepast, moeten deze conflicten opnieuw worden beoordeeld.

## Ontbrekende licentie in GitHub-repositories

De meeste Logius-standaarden repositories bevatten geen expliciet `LICENSE`-bestand in GitHub. De gepubliceerde standaarden op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl) en [logius-standaarden.github.io](https://logius-standaarden.github.io) vermelden echter CC-BY-4.0 als licentie via de ReSpec-configuratie.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [API-mod-signing](https://github.com/logius-standaarden/API-mod-signing) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [API-mod-encryption](https://github.com/logius-standaarden/API-mod-encryption) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |

### Aandachtspunt

De licentie-informatie in de SKILL.md is gebaseerd op de gepubliceerde ReSpec-documenten. Het verdient aanbeveling dat de repositories expliciet een `LICENSE`-bestand toevoegen om juridische duidelijkheid te bieden, met name voor hergebruik onder artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- Publicatie API-mod-geospatial: https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3/
- GitHub repo: https://github.com/logius-standaarden/API-mod-geospatial
- GitHub tags: https://github.com/logius-standaarden/API-mod-geospatial/tags
- Publicatie ADR-Beheermodel: https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0/
- GitHub ADR-Beheermodel: https://github.com/logius-standaarden/ADR-Beheermodel
- GitHub ADR-Beheermodel tags: https://github.com/logius-standaarden/ADR-Beheermodel/tags
- GitHub API-mod-transport-security: https://github.com/logius-standaarden/API-mod-transport-security
- Publicatie ADR v2.1.0: https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0/
- Forum Standaardisatie ADR: https://www.forumstandaardisatie.nl/open-standaarden/rest-api-design-rules
