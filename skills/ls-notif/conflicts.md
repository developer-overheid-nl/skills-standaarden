# Notificaties (CloudEvents) - Bronconflicten

Geconstateerd: 2026-02-21

Dit document beschrijft bekende discrepanties en bewuste keuzes voor de Notificaties-skill.

## GitHub-tags vs. gepubliceerde versies

| Repository | Gepubliceerde versie (DEF) | Laatste GitHub-tag | Discrepantie |
|-----------|---------------------------|-------------------|-------------|
| [NL-GOV-profile-for-CloudEvents](https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents) | [v1.1](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl/) | `1.1` | Geen discrepantie (tag komt overeen). Alle tags: `1.1`, `1.0`, `0.3`, `v0.1` |
| [Abonneren](https://github.com/logius-standaarden/Abonneren) | _(geen DEF)_ — [WV v0.0.1](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren/) | _(geen tags)_ | Werkversie op gitdocumentatie; nog geen vastgestelde versie |

### Observatie: reponaam

De juiste GitHub-reponaam is `NL-GOV-profile-for-CloudEvents`. De naam `CloudEvents-NL-profiel` (die soms in verwijzingen voorkomt) bestaat niet en geeft een 404.

## Forum Standaardisatie vs. Logius DEF-versie

| Bron | Versie | Status |
|------|--------|--------|
| [Forum Standaardisatie](https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-profile-cloudevents) | v1.0 | Verplicht (pas-toe-of-leg-uit) |
| [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl/) | v1.1 | Meest recente DEF bij Logius |

### Analyse

Het Forum Standaardisatie vermeldt v1.0 als de verplichte versie op de pas-toe-of-leg-uit lijst. Logius heeft inmiddels v1.1 als DEF vastgesteld. Dit is geen fout: het Forum werkt met vastgestelde lijstversies die periodiek worden bijgewerkt, terwijl Logius doorontwikkelt.

## Keuze in SKILL.md

De skill noemt beide versies: v1.0 als de Forum Standaardisatie-versie (verplicht) en v1.1 als de meest recente Logius DEF. Als het Forum de lijstversie bijwerkt naar v1.1, moet dit conflict opnieuw worden beoordeeld.

## Ontbrekende licentie in GitHub-repositories

De meeste Logius-standaarden repositories bevatten geen expliciet `LICENSE`-bestand in GitHub. De gepubliceerde standaarden op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl) en [logius-standaarden.github.io](https://logius-standaarden.github.io) vermelden echter CC-BY-4.0 als licentie via de ReSpec-configuratie.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [NL-GOV-profile-for-CloudEvents](https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [CloudEvents-NL-Guidelines](https://github.com/logius-standaarden/CloudEvents-NL-Guidelines) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Notificatieservices](https://github.com/logius-standaarden/Notificatieservices) | Geen | N.v.t. | Geen licentie |
| [Abonneren](https://github.com/logius-standaarden/Abonneren) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |

### Aandachtspunt

De licentie-informatie in de SKILL.md is gebaseerd op de gepubliceerde ReSpec-documenten. Het verdient aanbeveling dat de repositories expliciet een `LICENSE`-bestand toevoegen om juridische duidelijkheid te bieden, met name voor hergebruik onder artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- Publicatie CloudEvents NL GOV profiel: https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl/
- GitHub repo: https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents
- GitHub tags: https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents/tags
- Forum Standaardisatie: https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-profile-cloudevents
