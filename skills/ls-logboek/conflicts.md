# Logboek Dataverwerkingen - Bronconflicten

Geconstateerd: 2026-02-21

Dit document beschrijft bekende discrepanties en bewuste keuzes voor de Logboek-skill.

## GitHub-tags vs. gepubliceerde versies

Er zijn geen vastgestelde (DEF) versies voor Logboek Dataverwerkingen. De publicatie-URL `gitdocumentatie.logius.nl/publicatie/logboek/logging/` geeft een 404. De GitHub-repositories hebben geen tags.

| Repository | Gepubliceerde versie (DEF) | Laatste GitHub-tag | Discrepantie |
|-----------|---------------------------|-------------------|-------------|
| [logboek-dataverwerkingen](https://github.com/logius-standaarden/logboek-dataverwerkingen) | _(geen DEF)_ | _(geen tags)_ | N.v.t. — alleen werkversies |
| [logboek-extensie-lezen](https://github.com/logius-standaarden/logboek-extensie-lezen) | _(geen DEF)_ | _(geen tags)_ | N.v.t. — alleen werkversies |
| [logboek-extensie-nen7513](https://github.com/logius-standaarden/logboek-extensie-nen7513) | _(geen DEF)_ | _(geen tags)_ | N.v.t. — alleen werkversies |
| [logboek-extensie-object](https://github.com/logius-standaarden/logboek-extensie-object) | _(geen DEF)_ | _(geen tags)_ | N.v.t. — alleen werkversies |
| [logboek-extensie-template](https://github.com/logius-standaarden/logboek-extensie-template) | _(geen DEF)_ | _(geen tags)_ | N.v.t. — alleen werkversies |
| [logboek-dataverwerkingen-inleiding](https://github.com/logius-standaarden/logboek-dataverwerkingen-inleiding) | _(geen DEF)_ | _(geen tags)_ | N.v.t. — alleen werkversies |
| [logboek-dataverwerkingen-juridisch-beleidskader](https://github.com/logius-standaarden/logboek-dataverwerkingen-juridisch-beleidskader) | _(geen DEF)_ | _(geen tags)_ | N.v.t. — alleen werkversies |
| [logboek-dataverwerkingen-demo](https://github.com/logius-standaarden/logboek-dataverwerkingen-demo) | _(geen DEF)_ | _(geen tags)_ | N.v.t. — demo/referentie-implementatie |

## Keuze in SKILL.md

Alle repositories hebben alleen werkversies; er zijn geen bronconflicten. Als er een DEF-versie wordt vastgesteld, moet dit document worden bijgewerkt met de versie-informatie.

## Ontbrekende licentie in GitHub-repositories

De meeste Logius-standaarden repositories bevatten geen expliciet `LICENSE`-bestand in GitHub. De gepubliceerde standaarden op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl) en [logius-standaarden.github.io](https://logius-standaarden.github.io) vermelden echter CC-BY-4.0 als licentie via de ReSpec-configuratie.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [logboek-dataverwerkingen](https://github.com/logius-standaarden/logboek-dataverwerkingen) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [logboek-extensie-lezen](https://github.com/logius-standaarden/logboek-extensie-lezen) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [logboek-extensie-nen7513](https://github.com/logius-standaarden/logboek-extensie-nen7513) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [logboek-extensie-object](https://github.com/logius-standaarden/logboek-extensie-object) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [logboek-extensie-template](https://github.com/logius-standaarden/logboek-extensie-template) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [logboek-dataverwerkingen-inleiding](https://github.com/logius-standaarden/logboek-dataverwerkingen-inleiding) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [logboek-dataverwerkingen-juridisch-beleidskader](https://github.com/logius-standaarden/logboek-dataverwerkingen-juridisch-beleidskader) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |

**Opmerking:** [logboek-dataverwerkingen-demo](https://github.com/logius-standaarden/logboek-dataverwerkingen-demo) heeft wél een expliciete EUPL-1.2 licentie in GitHub en is een demo/referentie-implementatie (geen ReSpec-document), en is daarom niet opgenomen in bovenstaande tabel.

### Aandachtspunt

De licentie-informatie in de SKILL.md is gebaseerd op de gepubliceerde ReSpec-documenten. Het verdient aanbeveling dat de repositories expliciet een `LICENSE`-bestand toevoegen om juridische duidelijkheid te bieden, met name voor hergebruik onder artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- GitHub repo: https://github.com/logius-standaarden/logboek-dataverwerkingen
- GitHub extensies: https://github.com/logius-standaarden?q=logboek-extensie
- Werkversie: https://logius-standaarden.github.io/logboek-dataverwerkingen/
