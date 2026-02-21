# Changelog

Alle noemenswaardige wijzigingen aan deze plugin worden hier gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.1.0/)
en dit project volgt [Semantic Versioning](https://semver.org/lang/nl/).

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

- Marketplace gescheiden van plugin: marketplace.json is verplaatst naar [MinBZK/overheid-claude-plugins](https://github.com/MinBZK/overheid-claude-plugins)
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
