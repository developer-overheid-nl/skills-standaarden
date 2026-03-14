# Digikoppeling - Bronconflicten

Geconstateerd: 2026-02-21

Dit document beschrijft bekende discrepanties tussen GitHub-repository tags en de gepubliceerde versies op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl). De **gepubliceerde versie op gitdocumentatie.logius.nl is leidend** voor DEF-versies; GitHub-tags worden niet altijd bijgewerkt na publicatie.

## Patroon

Bij Digikoppeling-repositories worden versie-tags in GitHub aangemaakt bij het doorlopen van het release-proces. Na vaststelling (DEF) wordt de versie gepubliceerd op gitdocumentatie.logius.nl. Echter, de Git-tags worden niet altijd bijgewerkt wanneer er na de oorspronkelijke publicatie correcties of nieuwe versies worden vastgesteld. Dit betekent dat de laatste Git-tag vaak achterloopt op de gepubliceerde versie.

Daarnaast worden GitHub Releases (een apart mechanisme naast tags) niet consequent aangemaakt. Veel tags hebben geen bijbehorende GitHub Release.

## Discrepanties

| Repository | Gepubliceerde versie (DEF) | Laatste GitHub-tag | Discrepantie |
|-----------|---------------------------|-------------------|-------------|
| [Digikoppeling-Architectuur](https://github.com/logius-standaarden/Digikoppeling-Architectuur) | [v2.1.1](https://gitdocumentatie.logius.nl/publicatie/dk/architectuur/) | `2.0.2` | Tag achter: publicatie v2.1.1 vs tag 2.0.2 |
| [Digikoppeling-Koppelvlakstandaard-REST-API](https://github.com/logius-standaarden/Digikoppeling-Koppelvlakstandaard-REST-API) | [v3.0.1](https://gitdocumentatie.logius.nl/publicatie/dk/restapi/) | `3.0.0` | Tag achter: publicatie v3.0.1 vs tag 3.0.0 |
| [Digikoppeling-Koppelvlakstandaard-ebMS2](https://github.com/logius-standaarden/Digikoppeling-Koppelvlakstandaard-ebMS2) | [v3.3.2](https://gitdocumentatie.logius.nl/publicatie/dk/ebms/) | `3.3.2` | Geen discrepantie (tag komt overeen) |
| [Digikoppeling-Koppelvlakstandaard-WUS](https://github.com/logius-standaarden/Digikoppeling-Koppelvlakstandaard-WUS) | [v3.8.1](https://gitdocumentatie.logius.nl/publicatie/dk/wus/) | `3.8.1` | Geen discrepantie (tag komt overeen) |
| [Digikoppeling-Koppelvlakstandaard-GB](https://github.com/logius-standaarden/Digikoppeling-Koppelvlakstandaard-GB) | [v3.8.1](https://gitdocumentatie.logius.nl/publicatie/dk/gb/) | `3.8.1` | Geen discrepantie (tag komt overeen, al zijn er ook sub-releases `3.8.1-2`, `3.8.1-3`) |
| [Digikoppeling-Beveiligingsstandaarden-en-voorschriften](https://github.com/logius-standaarden/Digikoppeling-Beveiligingsstandaarden-en-voorschriften) | [v2.0.1](https://gitdocumentatie.logius.nl/publicatie/dk/beveilig/) | `2.0.0` | Tag achter: publicatie v2.0.1 vs tag 2.0.0 |
| [Digikoppeling-Identificatie-en-Authenticatie](https://github.com/logius-standaarden/Digikoppeling-Identificatie-en-Authenticatie) | [v1.5.0](https://gitdocumentatie.logius.nl/publicatie/dk/idauth/) | `1.4.2` | Tag achter: publicatie v1.5.0 vs tag 1.4.2 |
| [OIN-Stelsel](https://github.com/logius-standaarden/OIN-Stelsel) | [v2.2.2](https://gitdocumentatie.logius.nl/publicatie/dk/oin/) | `2.2.0` | Tag achter: publicatie v2.2.2 vs tag 2.2.0 (zie ook [ls-iam conflicts.md](../ls-iam/conflicts.md)) |
| [Digikoppeling-Beheermodel](https://github.com/logius-standaarden/Digikoppeling-Beheermodel) | [v1.8](https://gitdocumentatie.logius.nl/publicatie/dk/beheer/) | `1.6r` | Tag achter: publicatie v1.8 vs tag 1.6r |
| [Digikoppeling-Gebruik-en-achtergrond-certificaten](https://github.com/logius-standaarden/Digikoppeling-Gebruik-en-achtergrond-certificaten) | [v1.6.3](https://gitdocumentatie.logius.nl/publicatie/dk/gbachtcert/) | `1.6.2` | Tag achter: publicatie v1.6.3 vs tag 1.6.2 |
| [Digikoppeling-Best-Practices-ebMS2](https://github.com/logius-standaarden/Digikoppeling-Best-Practices-ebMS2) | [v3.2.2](https://gitdocumentatie.logius.nl/publicatie/dk/bpebms/) | `3.2.1` | Tag achter: publicatie v3.2.2 vs tag 3.2.1 |
| [Digikoppeling-Overzicht-Actuele-Documentatie-en-Compliance](https://github.com/logius-standaarden/Digikoppeling-Overzicht-Actuele-Documentatie-en-Compliance) | [v1.12.2](https://gitdocumentatie.logius.nl/publicatie/dk/actueel/) | `1.12.0` | Tag achter: publicatie v1.12.2 vs tag 1.12.0 |
| [Digikoppeling-Best-Practices-GB](https://github.com/logius-standaarden/Digikoppeling-Best-Practices-GB) | [v3.2.0](https://gitdocumentatie.logius.nl/publicatie/dk/bpgb/) | `3.1.1` | Tag achter: publicatie v3.2.0 vs tag 3.1.1. Overige tags: `3.1`, `3.1r`–`3.1r5` |
| [Digikoppeling-Best-Practices-WUS](https://github.com/logius-standaarden/Digikoppeling-Best-Practices-WUS) | [v1.10.2](https://gitdocumentatie.logius.nl/publicatie/dk/bpwus/) | `1.10.1` | Tag achter: publicatie v1.10.2 vs tag 1.10.1. Overige tags: `1.10`, `1.10r`–`1.10r3`. Let op: anomale tag `3.8` (verkeerd versienummerschema) |
| [Digikoppeling-Handreiking-Adressering-en-Routering](https://github.com/logius-standaarden/Digikoppeling-Handreiking-Adressering-en-Routering) | [v1.1.0](https://gitdocumentatie.logius.nl/publicatie/dk/bpadres/) | `1.1.0` | Geen discrepantie (tag komt overeen). Overige tags: `1.0`, `1.0.1` |
| [Digikoppeling-Wat-is-Digikoppeling](https://github.com/logius-standaarden/Digikoppeling-Wat-is-Digikoppeling) | [v1.1.2](https://gitdocumentatie.logius.nl/publicatie/dk/watisdk/) | `1.1.2` | Geen discrepantie (tag komt overeen). Overige tags: `1.1.1`, `1.1.1r`–`1.1.1r4` |
| [Digikoppeling-Algemeen](https://github.com/logius-standaarden/Digikoppeling-Algemeen) | [v2024-2025](https://gitdocumentatie.logius.nl/publicatie/dk/roadmap/) | _(geen tags)_ | Geen tags aanwezig; publicatie v2024-2025 is niet getagd |

## Overige observaties

- **Malformed tag:** `Digikoppeling-Beveiligingsstandaarden-en-voorschriften` bevat een tag `1,4r` met een komma i.p.v. een punt.
- **GitHub Releases:** Veel repos hebben een laatste GitHub Release die ouder is dan de laatste Git tag. Releases worden niet consequent aangemaakt.

## Keuze in SKILL.md

De skill gebruikt versienummers van gitdocumentatie.logius.nl als bron van waarheid voor vastgestelde (DEF) versies. GitHub-tags lopen achter maar dat is een beheerproces-kwestie. Als tags worden bijgewerkt, moet dit conflict opnieuw worden beoordeeld.

## Ontbrekende licentie in GitHub-repositories

De meeste Logius-standaarden repositories bevatten geen expliciet `LICENSE`-bestand in GitHub. De gepubliceerde standaarden op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl) en [logius-standaarden.github.io](https://logius-standaarden.github.io) vermelden echter CC-BY-4.0 als licentie via de ReSpec-configuratie.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [Digikoppeling-Architectuur](https://github.com/logius-standaarden/Digikoppeling-Architectuur) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Koppelvlakstandaard-REST-API](https://github.com/logius-standaarden/Digikoppeling-Koppelvlakstandaard-REST-API) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Koppelvlakstandaard-ebMS2](https://github.com/logius-standaarden/Digikoppeling-Koppelvlakstandaard-ebMS2) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Koppelvlakstandaard-WUS](https://github.com/logius-standaarden/Digikoppeling-Koppelvlakstandaard-WUS) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Koppelvlakstandaard-GB](https://github.com/logius-standaarden/Digikoppeling-Koppelvlakstandaard-GB) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Beveiligingsstandaarden-en-voorschriften](https://github.com/logius-standaarden/Digikoppeling-Beveiligingsstandaarden-en-voorschriften) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Identificatie-en-Authenticatie](https://github.com/logius-standaarden/Digikoppeling-Identificatie-en-Authenticatie) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [OIN-Stelsel](https://github.com/logius-standaarden/OIN-Stelsel) | [CC-BY-4.0](https://github.com/logius-standaarden/OIN-Stelsel/blob/main/LICENSE) | CC-BY-4.0 (ReSpec) | Opgelost |
| [Digikoppeling-Beheermodel](https://github.com/logius-standaarden/Digikoppeling-Beheermodel) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Gebruik-en-achtergrond-certificaten](https://github.com/logius-standaarden/Digikoppeling-Gebruik-en-achtergrond-certificaten) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Best-Practices-ebMS2](https://github.com/logius-standaarden/Digikoppeling-Best-Practices-ebMS2) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Overzicht-Actuele-Documentatie-en-Compliance](https://github.com/logius-standaarden/Digikoppeling-Overzicht-Actuele-Documentatie-en-Compliance) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Best-Practices-GB](https://github.com/logius-standaarden/Digikoppeling-Best-Practices-GB) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Best-Practices-WUS](https://github.com/logius-standaarden/Digikoppeling-Best-Practices-WUS) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Handreiking-Adressering-en-Routering](https://github.com/logius-standaarden/Digikoppeling-Handreiking-Adressering-en-Routering) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Wat-is-Digikoppeling](https://github.com/logius-standaarden/Digikoppeling-Wat-is-Digikoppeling) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Digikoppeling-Algemeen](https://github.com/logius-standaarden/Digikoppeling-Algemeen) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |

### Aandachtspunt

De licentie-informatie in de SKILL.md is gebaseerd op de gepubliceerde ReSpec-documenten. Het verdient aanbeveling dat de repositories expliciet een `LICENSE`-bestand toevoegen om juridische duidelijkheid te bieden, met name voor hergebruik onder artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- Gepubliceerde versies (overzicht): https://gitdocumentatie.logius.nl/publicatie/dk/actueel/
- GitHub organisatie: https://github.com/logius-standaarden/
- Forum Standaardisatie: https://www.forumstandaardisatie.nl/open-standaarden/digikoppeling
