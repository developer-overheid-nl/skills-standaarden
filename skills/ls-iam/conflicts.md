# IAM - Bronconflicten

Geconstateerd: 2026-02-21

Dit document beschrijft bekende discrepanties in bronnen die relevant zijn voor de IAM-skill.

---

## 1. GitHub-tag vs. gepubliceerde versie: OIN-Stelsel

De **gepubliceerde versie op gitdocumentatie.logius.nl is leidend** voor DEF-versies.

| Repository | Gepubliceerde versie (DEF) | Laatste GitHub-tag | Discrepantie |
|-----------|---------------------------|-------------------|-------------|
| [OIN-Stelsel](https://github.com/logius-standaarden/OIN-Stelsel) | [v2.2.1](https://gitdocumentatie.logius.nl/publicatie/dk/oin/) | `2.2.0` | Tag achter: publicatie v2.2.1 vs tag 2.2.0 |

### Details OIN-Stelsel

- **Bekende tags:** `2.2.0`, `2.0.3`, `2.0.2`, `2.0.2r`, `2.0.1`
- **Laatste GitHub Release:** `2.0.3` (gepubliceerd 2022-11-29) — ver achter op de laatste tag `2.2.0`
- De tag `2.2.0` bestaat, maar de gepubliceerde versie op gitdocumentatie is `v2.2.1` — één patchversie verder
- Er is geen tag `2.2.1` in de repository

**Let op:** OIN-Stelsel wordt ook gerefereerd vanuit `/ls-dk` (Digikoppeling). Dezelfde discrepantie is gedocumenteerd in [ls-dk/conflicts.md](../ls-dk/conflicts.md).

---

## 1b. GitHub-tags vs. gepubliceerde versies: OAuth-NL, OIDC-NLGOV en OAuth-Beheermodel

Voor compleetheid worden hier ook de IAM-repositories vermeld waar tags en publicatieversies wél overeenkomen, en het gearchiveerde OAuth-Beheermodel.

| Repository | Gepubliceerde versie (DEF) | Laatste GitHub-tag | Discrepantie |
|-----------|---------------------------|-------------------|-------------|
| [OAuth-NL-profiel](https://github.com/logius-standaarden/OAuth-NL-profiel) | [v1.1.0](https://gitdocumentatie.logius.nl/publicatie/api/oauth/) | `v1.1.0` | Geen discrepantie (tag komt overeen). Alle tags: `v1.1.0`, `v1.1.0-rc.2`, `v1.1.0-rc.1`, `v1.0`, `1.0r`, `1.0r2` |
| [OIDC-NLGOV](https://github.com/logius-standaarden/OIDC-NLGOV) | [v1.0.1](https://gitdocumentatie.logius.nl/publicatie/api/oidc/) | `v1.0.1` | Geen discrepantie (tag komt overeen) |
| [OAuth-Beheermodel](https://github.com/logius-standaarden/OAuth-Beheermodel) | [v1.0](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer/) | `0.2` | Tag-formaat afwijkend: publicatie v1.0 vs tag `0.2` |

### Details OAuth-Beheermodel

- **Tags:** `0.1`, `0.2`
- De repository is **gearchiveerd**
- De gepubliceerde DEF-versie op gitdocumentatie is `v1.0`
- De tag `0.2` is een conceptversie; de definitieve versie v1.0 is gepubliceerd zonder bijbehorende Git-tag

---

## 2. Forum Standaardisatie bronconflict: OAuth v1.1 expertonderzoek type

Het Forum Standaardisatie bevat **tegenstrijdige informatie** over het type expertonderzoek voor OAuth NL profiel v1.1:

| Bron | URL | Vermelding |
|------|-----|-----------|
| **Hoofdpagina** OAuth 2.0 NL | [forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20](https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20) | "Een **volledig** expertonderzoek is aangewezen" |
| **Intakeadvies** OAuth v1.1 | [forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11](https://www.forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11) | "Een **verkort** expertonderzoek is aangewezen om de nieuwe versie van de standaard te toetsen aan de criteria voor opname op de lijst." |

### Analyse

- Het intakeadvies-document is het **meer specifieke en autoritatieve** bron: het is de daadwerkelijke aanbeveling van de stuurgroep op basis van de intake op 14-08-2025
- De stuurgroep adviseert "verkort" omdat het een beperkte/incrementele versie-update betreft die backward compatible is met v1.0
- De hoofdpagina is waarschijnlijk niet bijgewerkt na het intakeadvies

### Keuze in SKILL.md

De skill gebruikt **"verkort expertonderzoek"**, conform het intakeadvies-document. Als de hoofdpagina van het Forum wordt bijgewerkt, moet dit conflict opnieuw worden beoordeeld.

---

## Keuze in SKILL.md

De skill gebruikt versienummers van gitdocumentatie.logius.nl als bron van waarheid voor vastgestelde (DEF) versies (OIN-Stelsel v2.2.1, OAuth-Beheermodel v1.0). Voor het expertonderzoek-type van OAuth v1.1 volgt de skill het intakeadvies-document ("verkort"). OAuth-Beheermodel heeft een afwijkende tag (`0.2` vs DEF v1.0) maar is gearchiveerd. Als de GitHub-tags of de Forum-hoofdpagina worden bijgewerkt, moet dit conflict opnieuw worden beoordeeld.

## Licentie-status GitHub-repositories

Sommige repositories bevatten een W3C Software License (afkomstig van het ReSpec-template), terwijl de gepubliceerde standaarden CC-BY-4.0 vermelden via de ReSpec-configuratie. Andere repositories hebben geen expliciet `LICENSE`-bestand.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [OAuth-NL-profiel](https://github.com/logius-standaarden/OAuth-NL-profiel) | Geen | CC-BY-4.0 (gepubliceerde versie); develop-branch ReSpec config bevat `cc-by-nd` | Discrepantie (develop wijkt af van publicatie) |
| [OIDC-NLGOV](https://github.com/logius-standaarden/OIDC-NLGOV) | W3C Software License | CC-BY-4.0 (ReSpec) | Afwijkend |
| [OAuth-Inleiding](https://github.com/logius-standaarden/OAuth-Inleiding) | W3C Software License | CC-BY-4.0 (ReSpec) | Afwijkend |
| [OAuth-Beheermodel](https://github.com/logius-standaarden/OAuth-Beheermodel) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [authzen-nlgov](https://github.com/logius-standaarden/authzen-nlgov) | W3C Software License | CC-BY-4.0 (ReSpec) | Afwijkend |
| [authorization-decision-log](https://github.com/logius-standaarden/authorization-decision-log) | W3C Software License | CC-BY-4.0 (ReSpec) | Afwijkend |
| [st-saml-spec](https://github.com/logius-standaarden/st-saml-spec) | W3C Software License | CC-BY-4.0 (ReSpec) | Afwijkend |
| [OIN-Stelsel](https://github.com/logius-standaarden/OIN-Stelsel) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |

### Aandachtspunt

De W3C Software License is afkomstig van het ReSpec-template en dekt de tooling-code. De gepubliceerde standaard-inhoud valt onder CC-BY-4.0 (vermeld in de ReSpec-configuratie). Voor repositories zonder LICENSE-bestand verdient het aanbeveling om expliciet een licentie toe te voegen, relevant voor artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- Publicatie OIN-Stelsel: https://gitdocumentatie.logius.nl/publicatie/dk/oin/
- GitHub OIN-Stelsel: https://github.com/logius-standaarden/OIN-Stelsel
- GitHub OIN-Stelsel tags: https://github.com/logius-standaarden/OIN-Stelsel/tags
- Forum Standaardisatie OAuth 2.0 NL: https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20
- Intakeadvies OAuth v1.1: https://www.forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11
- Publicatie OAuth-Beheermodel: https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer/
- GitHub OAuth-Beheermodel: https://github.com/logius-standaarden/OAuth-Beheermodel
- GitHub OAuth-Beheermodel tags: https://github.com/logius-standaarden/OAuth-Beheermodel/tags
- Forum Standaardisatie Authenticatie-standaarden: https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden
