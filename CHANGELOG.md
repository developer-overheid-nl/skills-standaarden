# Changelog

Alle noemenswaardige wijzigingen aan deze plugin worden hier gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.1.0/)
en dit project volgt [Semantic Versioning](https://semver.org/lang/nl/).

## [1.3.5](https://github.com/developer-overheid-nl/standaarden-plugin/compare/v1.3.4...v1.3.5) (2026-02-26)


### Opgelost

* corrigeer feitelijke onjuistheden in skills na grondige verificatie ([#55](https://github.com/developer-overheid-nl/standaarden-plugin/issues/55)) ([fa41c9c](https://github.com/developer-overheid-nl/standaarden-plugin/commit/fa41c9cb4fa4b68cf59d9b247f0da945e2bab3d9))
* voeg disclaimer toe dat axe-core WCAG check beperkt is ([#57](https://github.com/developer-overheid-nl/standaarden-plugin/issues/57)) ([27c2af3](https://github.com/developer-overheid-nl/standaarden-plugin/commit/27c2af38d7ea767acc5e6d6f7add96390983bbc2))

## [1.3.4](https://github.com/developer-overheid-nl/standaarden-plugin/compare/v1.3.3...v1.3.4) (2026-02-22)


### Opgelost

* verbeter bruikbaarheid en correctheid van skills ([#53](https://github.com/developer-overheid-nl/standaarden-plugin/issues/53)) ([b68942f](https://github.com/developer-overheid-nl/standaarden-plugin/commit/b68942fe185f45afc97bc29898e1a6ca5be70d5f))

## [1.3.3](https://github.com/developer-overheid-nl/standaarden-plugin/compare/v1.3.2...v1.3.3) (2026-02-22)


### Opgelost

* vervang /publicatie/dk/ (403) door /publicatie/dk/actueel/ ([#46](https://github.com/developer-overheid-nl/standaarden-plugin/issues/46)) ([66d405e](https://github.com/developer-overheid-nl/standaarden-plugin/commit/66d405e32b870c0b7d3d38d99f00089083aee2eb))

## [1.3.2](https://github.com/developer-overheid-nl/standaarden-plugin/compare/v1.3.1...v1.3.2) (2026-02-22)


### Opgelost

* elimineer monitoring false positives ([#45](https://github.com/developer-overheid-nl/standaarden-plugin/issues/45)) ([13434d5](https://github.com/developer-overheid-nl/standaarden-plugin/commit/13434d5ca452ab5c6457ad1e2a8c80600ffdacff))
* gebruik Actions cache voor monitoring checksums i.p.v. git push ([#40](https://github.com/developer-overheid-nl/standaarden-plugin/issues/40)) ([c0b2f5e](https://github.com/developer-overheid-nl/standaarden-plugin/commit/c0b2f5e3b2b8a1e1eb6ce09e0cff69836222b92e))

## [1.3.1](https://github.com/developer-overheid-nl/standaarden-plugin/compare/v1.3.0...v1.3.1) (2026-02-21)


### Opgelost

* gebruik dynamische shields.io badge voor versienummer ([#27](https://github.com/developer-overheid-nl/standaarden-plugin/issues/27)) ([08344df](https://github.com/developer-overheid-nl/standaarden-plugin/commit/08344df969b3e410dfe93fadafdf29a6c2be392d))
* negeer ETag/Last-Modified false positives in monitoring ([#29](https://github.com/developer-overheid-nl/standaarden-plugin/issues/29)) ([ae64994](https://github.com/developer-overheid-nl/standaarden-plugin/commit/ae649941af21c9a9068ae70ba1dc2b948bc15655))

## [1.3.0](https://github.com/developer-overheid-nl/standaarden-plugin/compare/v1.2.0...v1.3.0) (2026-02-21)


### Toegevoegd

* Automatische releases met release-please ([#17](https://github.com/developer-overheid-nl/standaarden-plugin/issues/17)) ([08ead1a](https://github.com/developer-overheid-nl/standaarden-plugin/commit/08ead1a7a85d1252c297406483fd320559fb3c49))
* Python linting met ruff ([#15](https://github.com/developer-overheid-nl/standaarden-plugin/issues/15)) ([741a1f1](https://github.com/developer-overheid-nl/standaarden-plugin/commit/741a1f1c9907635832c5f7257a4ecc39f50105bb))
* Tests toevoegen met pytest ([#19](https://github.com/developer-overheid-nl/standaarden-plugin/issues/19)) ([f0d81dc](https://github.com/developer-overheid-nl/standaarden-plugin/commit/f0d81dc7f971fb272efa40a84ef95489e5ce53c1))


### Opgelost

* markdownlint regels compatibel met release-please CHANGELOG ([#25](https://github.com/developer-overheid-nl/standaarden-plugin/issues/25)) ([40879cd](https://github.com/developer-overheid-nl/standaarden-plugin/commit/40879cdc9eedd643b5e6ea393485e5a3950103ca))
* versie-badge in README automatisch bijwerken bij release ([#26](https://github.com/developer-overheid-nl/standaarden-plugin/issues/26)) ([08edcce](https://github.com/developer-overheid-nl/standaarden-plugin/commit/08edcce71d213ca5b340bbb5e37247265ca9a9e1))

## [1.2.0] - 2026-02-21

### Toegevoegd

- Versiemodel en publicatiekanalen gedocumenteerd in meta-skill `/ls` en alle domein-skills
- `conflicts.md` per domein: bronconflicten en bewuste keuzes gedocumenteerd (9 bestanden)
- Forum Standaardisatie status toegevoegd aan meta-skill `/ls`
- Ontbrekende vastgestelde versie-links toegevoegd in ls-dk (6 documenten met gitdocumentatie URLs)
- Digikoppeling-Algemeen beschrijving en links toegevoegd (Roadmap)
- CI-check voor `model` in skill frontmatter en reference.md voor ls-pub
- `conflicts.md` patroon gedocumenteerd in CLAUDE.md

### Gewijzigd

- Repo-telling gecorrigeerd: 88→77 unieke repos (gearchiveerde, meta/test en duplicaten uitgefilterd)
- Gearchiveerde repos gemarkeerd in ls-api, ls-bomos en ls-iam (ADR-Beheermodel, BOMOS-Aanvullende-Modules, BOMOS-OpenSource, OAuth-Beheermodel)
- Dode links gefixt in ls-notif (Notificatieservices 404, Abonneren 404), ls-egov (Terugmelden-API 404) en ls-pub (gitdocumentatie root 403)
- Verkeerde status-labels gecorrigeerd: NL-GOV-profile-for-CloudEvents (Draft→DEF v1.1), BOMOS-Verdieping (Draft→DEF), fsc-external-contract (Draft→CV)
- ADR werkversie-omschrijving verduidelijkt: draft is werk-in-uitvoering richting volgende release (n.a.v. reviewer feedback)
- README, publiccode.yml en plugin.json bijgewerkt met gecorrigeerde tellingen en beschrijvingen

## [1.1.0] - 2026-02-16

### Gewijzigd

- Marketplace gescheiden van plugin: marketplace.json is verplaatst naar [developer-overheid-nl/overheid-claude-plugins](https://github.com/developer-overheid-nl/overheid-claude-plugins)
- Installatie-instructies bijgewerkt naar de nieuwe overheid-plugins marketplace

### Verwijderd

- `.claude-plugin/marketplace.json` - leeft voortaan in de marketplace-repo
- Marketplace validatiestap uit CI workflow

## [1.0.0] - 2026-02-12

### Toegevoegd

- 10 skills voor 9 domeinen en 77 Logius standaarden repositories
  - `/ls` - Meta-skill: overzicht en routing naar het juiste domein
  - `/ls-api` - API Design Rules (9 repos): NL GOV API-standaard, Spectral linter, referentie-implementaties
  - `/ls-dk` - Digikoppeling (17 repos): REST, ebMS2, WUS, Grote Berichten, OIN
  - `/ls-iam` - Identity & Access Management (8 repos): OAuth 2.0 NL, OpenID Connect, AuthZEN, SAML
  - `/ls-fsc` - Federated Service Connectivity (7 repos): core protocol, inway/outway, service directory
  - `/ls-logboek` - Logboek Dataverwerkingen (8 repos): REST API, juridisch kader, Docker demo
  - `/ls-notif` - CloudEvents & Notificaties (4 repos): NL GOV CloudEvents profiel, pub/sub
  - `/ls-bomos` - BOMOS Governance (10 repos): Beheer- en Ontwikkelmodel voor Open Standaarden
  - `/ls-egov` - E-Government Services (6 repos): Terugmelding, Digimelding, e-procurement
  - `/ls-pub` - Publicatie & Tooling (9 repos): ReSpec, GitHub Actions workflows, tech radar
- Implementatievoorbeelden in Python, JavaScript, curl, XML en YAML
- Foutafhandeling met error codes en retry patronen
- Validatie-integraties (Spectral, markdownlint, axe-core)
- Marketplace metadata voor plugin distributie
- Upstream tracking metadata in plugin.json
