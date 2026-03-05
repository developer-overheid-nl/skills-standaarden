# FSC - Bronconflicten

Geconstateerd: 2026-02-21

Dit document beschrijft bekende discrepanties tussen GitHub-repository tags en de gepubliceerde versies op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl). De **gepubliceerde versie op gitdocumentatie.logius.nl is leidend** voor DEF-versies.

## Discrepanties

| Repository | Gepubliceerde versie (DEF) | Laatste GitHub-tag | Discrepantie |
|-----------|---------------------------|-------------------|-------------|
| [fsc-core](https://github.com/logius-standaarden/fsc-core) | [v1.1.2](https://gitdocumentatie.logius.nl/publicatie/fsc/core/) | `1.1.0-rc` | Tag ver achter: publicatie v1.1.2 vs tag 1.1.0-rc (release candidate) |
| [fsc-logging](https://github.com/logius-standaarden/fsc-logging) | [v1.0.0](https://gitdocumentatie.logius.nl/publicatie/fsc/logging/) | _(geen tags)_ | Geen tags: publicatie v1.0.0 bestaat maar de repo heeft nul Git-tags |
| [fsc-external-contract](https://github.com/logius-standaarden/fsc-external-contract) | [CV v1.0.0](https://gitdocumentatie.logius.nl/publicatie/fsc/ext/) | _(geen tags)_ | Geen tags: publicatie CV v1.0.0 bestaat maar de repo heeft nul Git-tags |

### Details fsc-core

- **Enige tag:** `1.1.0-rc` (gepubliceerd als GitHub Release op 2025-08-07)
- De tag is een **release candidate** (`-rc`), terwijl de gepubliceerde versie `v1.1.2` al twee patchversies verder is
- Er zijn geen tags voor `1.1.0`, `1.1.1` of `1.1.2`
- Dit wijst erop dat het volledige release-proces (v1.1.0 -> v1.1.1 -> v1.1.2) heeft plaatsgevonden zonder nieuwe Git-tags

### Details fsc-logging

- De repository heeft **nul Git-tags** en **nul GitHub Releases**
- Desondanks bestaat er een gepubliceerde versie [v1.0.0 op gitdocumentatie](https://gitdocumentatie.logius.nl/publicatie/fsc/logging/)
- Het publicatieproces heeft hier volledig buiten Git-tagging om plaatsgevonden

### Details fsc-external-contract

- De repository heeft **nul Git-tags** en **nul GitHub Releases**
- Op gitdocumentatie bestaat een gepubliceerde versie [CV v1.0.0](https://gitdocumentatie.logius.nl/publicatie/fsc/ext/)
- **Let op:** Dit is een **CV** (Consultatieversie), geen DEF-versie — het document is nog niet definitief vastgesteld
- Het publicatieproces heeft hier volledig buiten Git-tagging om plaatsgevonden

## Keuze in SKILL.md

De skill gebruikt versienummers van gitdocumentatie.logius.nl als bron van waarheid voor vastgestelde (DEF) versies. De GitHub-tags lopen significant achter (fsc-core) of ontbreken geheel (fsc-logging, fsc-external-contract). Als tags worden bijgewerkt of aangemaakt, moet dit conflict opnieuw worden beoordeeld.

## Ontbrekende licentie in GitHub-repositories

De meeste Logius-standaarden repositories bevatten geen expliciet `LICENSE`-bestand in GitHub. De gepubliceerde standaarden op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl) en [logius-standaarden.github.io](https://logius-standaarden.github.io) vermelden echter CC-BY-4.0 als licentie via de ReSpec-configuratie.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [fsc-core](https://github.com/logius-standaarden/fsc-core) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [fsc-logging](https://github.com/logius-standaarden/fsc-logging) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [fsc-properties](https://github.com/logius-standaarden/fsc-properties) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [fsc-regulated-area](https://github.com/logius-standaarden/fsc-regulated-area) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [fsc-external-contract](https://github.com/logius-standaarden/fsc-external-contract) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [fsc-extensie-template](https://github.com/logius-standaarden/fsc-extensie-template) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [fsc-test-suite](https://github.com/logius-standaarden/fsc-test-suite) | Geen | N.v.t. | Geen licentie |

### Aandachtspunt

De licentie-informatie in de SKILL.md is gebaseerd op de gepubliceerde ReSpec-documenten. Het verdient aanbeveling dat de repositories expliciet een `LICENSE`-bestand toevoegen om juridische duidelijkheid te bieden, met name voor hergebruik onder artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- Publicatie fsc-core: https://gitdocumentatie.logius.nl/publicatie/fsc/core/
- Publicatie fsc-logging: https://gitdocumentatie.logius.nl/publicatie/fsc/logging/
- GitHub fsc-core: https://github.com/logius-standaarden/fsc-core
- GitHub fsc-core tags: https://github.com/logius-standaarden/fsc-core/tags
- GitHub fsc-logging: https://github.com/logius-standaarden/fsc-logging
- GitHub fsc-logging tags: https://github.com/logius-standaarden/fsc-logging/tags
- Publicatie fsc-external-contract: https://gitdocumentatie.logius.nl/publicatie/fsc/ext/
- GitHub fsc-external-contract: https://github.com/logius-standaarden/fsc-external-contract
- GitHub fsc-external-contract tags: https://github.com/logius-standaarden/fsc-external-contract/tags
