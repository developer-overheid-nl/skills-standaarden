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

## DEF v1.1 vs. werkversie (develop)

Geconstateerd: 2026-10-29

Op `develop` is het profiel in oktober 2026 gesynchroniseerd met CNCF CloudEvents v1.0.2 ([PR #46](https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents/pull/46), 2026-10-21). DEF v1.1 is nog gebaseerd op CloudEvents v1.0.1. Inhoudelijke verschillen in de werkversie:

| Onderdeel | DEF v1.1 | Werkversie (okt 2026) |
|-----------|----------|------------------------|
| Basis | CNCF CloudEvents v1.0.1 | CNCF CloudEvents v1.0.2 |
| `dataref` | Optioneel attribuut in het profiel, met NLgov-toelichting (informatiearm notificeren) | Niet meer in het profiel beschreven; alleen nog een verwijzing naar de [CNCF dataref-extensie](https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/dataref.md) |
| `sequence` / `sequencetype` | Optionele attributen in het profiel (Sequence-extensie overgenomen) | Niet meer in het profiel beschreven; vallen onder de algemene regels voor extensie-attributen |
| `specversion` | `"1.0"` | `"1.0"`, met een expliciete noot ([PR #62](https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents/pull/62)) dat de profielversie losstaat van `specversion` |

## Keuze in SKILL.md

De skill noemt beide versies: v1.0 als de Forum Standaardisatie-versie (verplicht) en v1.1 als de meest recente Logius DEF. Als het Forum de lijstversie bijwerkt naar v1.1, moet dit conflict opnieuw worden beoordeeld.

De attributentabel volgt DEF v1.1, dus `dataref`, `sequence` en `sequencetype` blijven als optionele profielattributen staan. De skill meldt bij die attributen dat de werkversie ze uit het profiel haalt. Wordt een nieuwe DEF gepubliceerd met de v1.0.2-synchronisatie, dan moeten de tabel en het voorbeeld met `dataref` (Claim Check Pattern) opnieuw worden beoordeeld.

## Licentie-status GitHub-repositories

Sommige repositories bevatten een W3C Software License (afkomstig van het ReSpec-template), terwijl de gepubliceerde standaarden CC-BY-4.0 vermelden via de ReSpec-configuratie. Andere repositories hebben geen expliciet `LICENSE`-bestand.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [NL-GOV-profile-for-CloudEvents](https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [CloudEvents-NL-Guidelines](https://github.com/logius-standaarden/CloudEvents-NL-Guidelines) | W3C Software License | CC-BY-4.0 (ReSpec) | Afwijkend |
| [Notificatieservices](https://github.com/logius-standaarden/Notificatieservices) | Geen | N.v.t. | Geen licentie |
| [Abonneren](https://github.com/logius-standaarden/Abonneren) | W3C Software License | CC-BY-4.0 (ReSpec) | Afwijkend |

### Aandachtspunt

De W3C Software License is afkomstig van het ReSpec-template en dekt de tooling-code. De gepubliceerde standaard-inhoud valt onder CC-BY-4.0 (vermeld in de ReSpec-configuratie). Voor repositories zonder LICENSE-bestand verdient het aanbeveling om expliciet een licentie toe te voegen, relevant voor artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- Publicatie CloudEvents NL GOV profiel: https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl/
- GitHub repo: https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents
- GitHub tags: https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents/tags
- Forum Standaardisatie: https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-profile-cloudevents
