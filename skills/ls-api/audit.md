<!-- markdownlint-disable MD052 MD034 MD013 MD038 -->
# Audit ls-api — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 9 | 16% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 14 | 25% |
| UNGROUNDED | 6 | 11% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 6 | 11% |
| GROUNDED | 20 | 36% |

*Geverifieerd met sonnet, 17 calls, $1.4480.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (9)

### `ls-api-0004` — SKILL.md:35 *(§ Versiemodel)*

> ADR-modules ontlenen hun vaststellingsstatus aan de standaard die ernaar verwijst, niet aan een eigen vaststellingsproces.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — versiemodel modules

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron beschrijft niet hoe modules hun vaststellingsstatus ontlenen. Dit onderwerp wordt niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron beschrijft het beheermodel van de ADR-standaard als geheel, maar bespreekt het vaststellingsproces van individuele modules niet. Het concept van modules met eigen of afgeleide vaststellingsstatus komt niet voor in de tekst.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron behandelt het vaststellingsproces van modules of de relatie tot de verwijzende standaard niet.*
</details>

### `ls-api-0029` — SKILL.md:103 *(§ Datum en tijd)*

> De Spectral linter bevat 4 regels voor datum/tijd: `date-time-ensure-timezone`, `specify-format-for-date-and-time`, `time-without-timezone`, `use-date-instead-of-datetime`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Spectral linter

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron vermeldt geen datum/tijd-specifieke Spectral-regels zoals `date-time-ensure-timezone` of `specify-format-for-date-and-time`.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst is het ADR Beheermodel en bevat geen informatie over Spectral linter regels voor datum/tijd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De Spectral linter en datum/tijd-regels worden niet behandeld in deze bron.*
</details>

### `ls-api-0046` — SKILL.md:148 *(§ Signing Module (JAdES) — draft)*

> De Signing module gebruikt JAdES detached signatures met RSASSA-PSS (PS256), minimaal 256 bits.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Signing module (draft)

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron vermeldt de Signing module alleen als een apart extensie-document en geeft geen details over JAdES, RSASSA-PSS of PS256.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. De Signing module wordt niet besproken.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron gaat over de Geospatial module, niet over een Signing module.*
</details>

### `ls-api-0047` — SKILL.md:148 *(§ Signing Module (JAdES) — draft)*

> Signing module: signatures worden geplaatst in `Payload-Signature` en `Message-Signature` HTTP headers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Signing module (draft)

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen inhoud over `Payload-Signature` of `Message-Signature` HTTP headers.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. HTTP headers voor signing worden niet besproken.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron behandelt geen Signing module of HTTP signature headers.*
</details>

### `ls-api-0048` — SKILL.md:148 *(§ Signing Module (JAdES) — draft)*

> Signing module: OpenAPI representatie gebruikt `format: jws-compact-detached`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Signing module (draft)

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen vermelding van `format: jws-compact-detached`.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. OpenAPI-representaties van signing worden niet besproken.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron gaat niet over Signing module of jws-compact-detached formaten.*
</details>

### `ls-api-0049` — SKILL.md:154 *(§ Encryption Module (JWE) — draft)*

> De Encryption module (JWE) is bedoeld voor end-to-end versleuteling van request/response payloads wanneer transport-level encryptie niet voldoende is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Encryption module (draft)

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron vermeldt alleen dat 'security controls for signing and encrypting of application level messages are part of separate extensions', zonder inhoudelijke details over JWE of end-to-end encryptie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. De Encryption module wordt niet besproken.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron behandelt geen Encryption module of JWE.*
</details>

### `ls-api-0050` — SKILL.md:237 *(§ Spectral Linter)*

> De DON-hosted Spectral ruleset bevat 11 regels; de GitHub-versie bevat 22 regels (11 extra t.o.v. DON).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Spectral linter

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen vergelijking tussen een DON-hosted versie (11 regels) en een GitHub-versie (22 regels) van de Spectral ruleset.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. Spectral ruleset-aantallen worden niet besproken.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen informatie over Spectral rulesets of het aantal regels daarin.*
</details>

### `ls-api-0054` — SKILL.md:271 *(§ Spectral Linter)*

> De GitHub-versie van de ruleset bevat `nlgov:problem-schema-members` die verplichte velden in problem+json schema (RFC 9457) controleert.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Spectral linter regels (GitHub-only)

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc9457.txt](https://www.rfc-editor.org/rfc/rfc9457.txt)
  - *De claim gaat over een specifieke Spectral linter ruleset (`nlgov:problem-schema-members`) in een GitHub-repository van de Nederlandse API Design Rules. RFC 9457 bevat geen informatie over Spectral rules, linters, of de Nederlandse API Design Rules GitHub-repo.*

### `ls-api-0055` — reference.md:50 *(§ Implementatievoorbeelden)*

> Referentie-implementaties voor de ADR zijn beschikbaar in ASP.NET en Quarkus.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — implementatievoorbeelden

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen vermelding van referentie-implementaties in ASP.NET of Quarkus.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. Referentie-implementaties in specifieke frameworks worden niet besproken.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron behandelt geen referentie-implementaties voor ADR in ASP.NET of Quarkus.*
</details>

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (14)

### `ls-api-0005` — SKILL.md:35 *(§ Versiemodel)*

> De Geospatial module v1.0.x is normatief onderdeel van ADR v2.1.0 en daarmee vastgesteld.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Geospatial module

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > The API Design Rules Module: Geospatial version 1.0.x MUST be applied when providing geospatial data or functionality.
  - *De bron bevestigt dat de Geospatial module v1.0.x normatief onderdeel is van ADR v2.1.0. Dat de module daarmee 'vastgesteld' is in een eigen vaststellingsproces wordt niet vermeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron beschrijft de ADR v1.0. ADR v2.1.0 en een Geospatial module worden niet vermeld.*

### `ls-api-0007` — SKILL.md:42 *(§ Repositories)*

> De ADR-Beheermodel repository is gearchiveerd en vervangen door API-Standaarden-Beheermodel.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — repositories

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel)
  > Dit beheermodel is verouderd en vervangen door het algemene API Standaarden beheermodel
  - *De bron bevestigt dat de ADR-Beheermodel repository gearchiveerd is en vervangen is door een algemeen API Standaarden beheermodel. De claim noemt specifiek 'API-Standaarden-Beheermodel' als naam van de vervangende repository — dat exacte detail staat niet in de bron.*
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/logius-standaarden/API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel)
  > Generiek beheermodel voor de verzameling van API standaarden [...] Overzicht van API standaarden Een overzicht van API standaarden waarvoor dit beheer model wordt opgezet: NLGov REST API Design Rules NLGov Profiel voor OAuth 2.0 NLGov OIDC profiel Cloudevents
  - *De bron bevestigt dat API-Standaarden-Beheermodel bestaat en de ADR beheert, wat de vervanging impliciet ondersteunt. Maar of de ADR-Beheermodel repository expliciet is 'gearchiveerd' staat niet in de brontekst.*
<details><summary>6x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron maakt geen melding van de ADR-Beheermodel repository of een opvolger. Dit onderwerp wordt niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron is juist de ADR-Beheermodel repository zelf (v1.0). Of deze gearchiveerd is en vervangen door een API-Standaarden-Beheermodel staat er niet in.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules)
  - *De brontekst (GitHub README van API-Design-Rules) vermeldt niets over een gearchiveerde ADR-Beheermodel repository of een vervangend API-Standaarden-Beheermodel. Er staat alleen een link naar https://gitdocumentatie.logius.nl/publicatie/api/beheermodel/ zonder verdere details over archivering.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules)
  - *De brontekst vermeldt het beheermodel alleen als externe referentie ('The Governance of this standard is described by the API-Standaarden beheermodel published by Logius'), maar bevat geen informatie over archivering van de ADR-Beheermodel repository of vervanging door API-Standaarden-Beheermodel.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Standaarden-Beheermodel](https://logius-standaarden.github.io/API-Standaarden-Beheermodel)
  - *De brontekst vermeldt dat beheermodellen van ADR en OAuth zijn samengevoegd met dit beheermodel en dat 'de kopieën zijn daarom nu gearchiveerd', maar zegt niets specifieks over een 'ADR-Beheermodel repository' die gearchiveerd is en vervangen door 'API-Standaarden-Beheermodel' als repositorynaam.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial)
  - *De brontekst gaat uitsluitend over de API-mod-geospatial repository. Er is geen informatie over ADR-Beheermodel of API-Standaarden-Beheermodel.*
</details>

### `ls-api-0008` — SKILL.md:44 *(§ Repositories)*

> De API-mod-geospatial module is normatief opgenomen in ADR v2.1.0; vastgestelde versie is v1.0.3.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Geospatial module

- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > The API Design Rules Module: Geospatial version 1.0.x MUST be applied when providing geospatial data or functionality.
  - *De bron bevestigt dat de Geospatial module v1.0.x normatief is opgenomen, maar noemt geen specifiek versienummer v1.0.3. De claim dat de vastgestelde versie v1.0.3 is wordt niet ondersteund.*
- **PARTIALLY_SUPPORTED** (medium) — [https://logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules)
  > Normative module GEO module v1.0 [...] /core/modules/geospatial : Apply the geospatial module for geospatial data [...] The API Design Rules Module: Geospatial version 1.0.x MUST be applied when providing geospatial data or functionality.
  - *De bron bevestigt dat de Geospatial module normatief is opgenomen (via /core/modules/geospatial), en verwijst naar versie 1.0.x. De claim dat het specifiek om ADR v2.1.0 gaat en dat de vastgestelde versie v1.0.3 is, wordt niet bevestigd — de bron is een draft zonder versienummer in de titel, en noemt alleen '1.0.x'.*
<details><summary>6x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *API-mod-geospatial en ADR v2.1.0 worden niet vermeld in deze bron.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules)
  - *De brontekst bevat geen informatie over een API-mod-geospatial module, noch over normatieve opname in ADR v2.1.0 of een versienummer v1.0.3. De README noemt alleen ADR, OAuth en OIDC als standaarden.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel)
  - *De bron (GitHub-landingspagina van ADR-Beheermodel) bevat geen informatie over de geospatial module, ADR v2.1.0 of versienummers.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel)
  - *De brontekst noemt geen modules, geen versienummers, en geen geospatial specificaties.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Standaarden-Beheermodel](https://logius-standaarden.github.io/API-Standaarden-Beheermodel)
  - *De brontekst noemt de API-mod-geospatial module niet. Er is geen informatie over normatieve opname in ADR v2.1.0 of een vastgestelde versie v1.0.3.*
- **NOT_FOUND** (medium) — [https://github.com/logius-standaarden/API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial)
  - *De bron bevestigt dat API-mod-geospatial bestaat als module, maar vermeldt niets over normatieve opname in ADR v2.1.0 of een vastgestelde versie v1.0.3. Er zijn wel '3 tags' vermeld, maar geen versienummers.*
</details>

### `ls-api-0009` — SKILL.md:45 *(§ Repositories)*

> De API-mod-transport-security repository is gearchiveerd; de inhoud is ingebed in ADR v2.1.0.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Transport Security module

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > 3.8 Transport Security ... The scope of this section is limited to generic security controls that directly influence the visible parts of an API.
  - *De bron bevestigt dat Transport Security is ingebed in ADR v2.1.0 als sectie 3.8. Dat de repository gearchiveerd is wordt niet vermeld in de bron.*
- **PARTIALLY_SUPPORTED** (medium) — [https://logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules)
  > Normative Transport Security module v1.0 [...] 2.11 Transport Security [...] Note: security controls for signing and encrypting of application level messages are part of separate extensions: Signing and Encryption.
  - *De bron bevestigt dat Transport Security als module bestaat en normatief is opgenomen (sectie 2.11 is geheel gewijd aan Transport Security, en de leeswijzer noemt 'Transport Security module v1.0'). De claim dat de repository gearchiveerd is en de inhoud ingebed is in ADR v2.1.0 wordt niet expliciet bevestigd — de bron is een draft zonder versienummer.*
<details><summary>6x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *API-mod-transport-security en ADR v2.1.0 worden niet vermeld in deze bron.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules)
  - *De brontekst vermeldt niets over een API-mod-transport-security repository, archivering daarvan, of inbedding in ADR v2.1.0.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel)
  - *De bron bevat geen informatie over de API-mod-transport-security repository of de inhoud ervan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel)
  - *De brontekst bevat geen informatie over API-mod-transport-security of archivering daarvan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Standaarden-Beheermodel](https://logius-standaarden.github.io/API-Standaarden-Beheermodel)
  - *De brontekst noemt de API-mod-transport-security repository niet. Er is geen informatie over archivering of inbedding in ADR v2.1.0.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial)
  - *De brontekst behandelt de API-mod-transport-security repository niet.*
</details>

### `ls-api-0010` — SKILL.md:46 *(§ Repositories)*

> De API-mod-signing module (HTTP Message Signing) heeft nog geen vastgestelde versie en is een draft.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Signing module

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Note: security controls for signing and encrypting of application level messages are part of separate extensions: Signing and Encryption.
  - *De bron bevestigt dat Signing een aparte extensie is, maar zegt niets over de vaststellingsstatus (draft of vastgesteld).*
<details><summary>7x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Een signing module of HTTP Message Signing wordt niet vermeld in deze bron.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules)
  - *De brontekst bevat geen informatie over een API-mod-signing module of de draftstatus daarvan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules)
  - *De bron vermeldt de Signing module normatief (/core/modules/signing) en verwijst naar 'API Design Rules Module: Signing version 1.0.x', maar bevat geen informatie over de versie-status (draft vs. vastgesteld). De claim dat er nog geen vastgestelde versie is, kan niet worden getoetst aan deze bron.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel)
  - *De bron bevat geen informatie over de API-mod-signing module of HTTP Message Signing.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel)
  - *De brontekst noemt geen signing module, HTTP Message Signing, of draftstatus van modules.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Standaarden-Beheermodel](https://logius-standaarden.github.io/API-Standaarden-Beheermodel)
  - *De brontekst noemt de API-mod-signing module noch HTTP Message Signing. Er is geen informatie over de status (draft of vastgesteld).*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial)
  - *De brontekst behandelt de API-mod-signing repository niet.*
</details>

### `ls-api-0011` — SKILL.md:47 *(§ Repositories)*

> De API-mod-encryption module (JWE) heeft nog geen vastgestelde versie en is een draft.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Encryption module

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Note: security controls for signing and encrypting of application level messages are part of separate extensions: Signing and Encryption.
  - *De bron bevestigt dat Encryption een aparte extensie is, maar zegt niets over de vaststellingsstatus (draft of vastgesteld).*
<details><summary>7x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Een encryption module (JWE) wordt niet vermeld in deze bron.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules)
  - *De brontekst bevat geen informatie over een API-mod-encryption module of de draftstatus daarvan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules)
  - *De bron vermeldt de Encryption module normatief (/core/modules/encryption) en verwijst naar 'API Design Rules Module: Encryption version 1.0.x', maar bevat geen informatie over de versie-status (draft vs. vastgesteld). De claim dat er nog geen vastgestelde versie is, kan niet worden getoetst aan deze bron.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel)
  - *De bron bevat geen informatie over de API-mod-encryption module of JWE.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel)
  - *De brontekst noemt geen encryption module, JWE, of draftstatus van modules.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Standaarden-Beheermodel](https://logius-standaarden.github.io/API-Standaarden-Beheermodel)
  - *De brontekst noemt de API-mod-encryption module noch JWE. Er is geen informatie over de status (draft of vastgesteld).*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial)
  - *De brontekst behandelt de API-mod-encryption repository niet.*
</details>

### `ls-api-0012` — SKILL.md:55 *(§ URI-ontwerp)*

> URI-padsegmenten MOETEN kebab-case gebruiken: `/mijn-documenten` (niet `/mijnDocumenten`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — URI-ontwerp

- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > paths-kebab-case: severity: warn message: " {{property}} is not kebab-case."
  - *De linter configuratie in de bron suggereert kebab-case voor paden, maar dit is een warn (niet error) en staat in een non-normatieve sectie (Appendix A). Er is geen normatieve MUST-regel voor kebab-case in de kern van de spec.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron beschrijft het beheermodel, niet de inhoudelijke technische regels van de ADR. Kebab-case voor URI-padsegmenten staat er niet in.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron gaat over geospatiale regels; kebab-case voor URI-padsegmenten wordt niet behandeld.*

### `ls-api-0016` — SKILL.md:59 *(§ URI-ontwerp)*

> De major versie MOET in de URI zijn opgenomen: `/v1/resources`; in OAS op serverniveau, niet in individuele paden.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — URI-ontwerp en versiebeheer

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > The URI of an API (base path) MUST include the major version number, prefixed by the letter v ... An example of an openapi.yaml for an API with a base path https://api.example.org/v1
  - *De bron bevestigt dat de major versie in de URI moet staan. De specificatie dat dit 'op serverniveau, niet in individuele paden' moet worden gedaan wordt geïmpliceerd door het voorbeeld maar niet expliciet als regel gesteld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Versie-opname in de URI en OAS-serverniveau worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Versie in de URI wordt niet behandeld in deze bron.*

### `ls-api-0025` — SKILL.md:99 *(§ Datum en tijd)*

> Datum/tijd-waarden MOETEN het RFC 3339 formaat gebruiken.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — datum en tijd

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc3339.txt](https://www.rfc-editor.org/rfc/rfc3339.txt)
  > The following profile of ISO 8601 [ISO8601] dates SHOULD be used in new protocols on the Internet.
  - *RFC 3339 definieert het formaat als SHOULD (aanbevolen), niet als MUST (verplicht). De claim stelt dat het formaat MOET worden gebruikt, maar de bron zegt 'SHOULD be used'. Dit is een verzwakking ten opzichte van de claim, maar de bron bevestigt wel dat RFC 3339 het relevante formaat is voor datum/tijd-waarden op internet. De claim kan dus grotendeels worden onderbouwd door de bron, maar het normatieve niveau (MUST vs SHOULD) klopt niet exact.*

### `ls-api-0031` — SKILL.md:108 *(§ Naamgeving)*

> Collecties MOETEN in meervoud worden aangeduid: `/users`, `/orders`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — naamgeving

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Collection resources are referred to using plural nouns. [...] The path segment describing the name of the collection resource MUST be written in the plural form. Example collection resources: https://api.example.org/v1/gebouwen https://api.example.org/v1/vergunningen
  - *De bron bevestigt het meervoud-MUST, maar de voorbeelden zijn `/gebouwen` en `/vergunningen`, niet `/users` of `/orders` zoals de claim stelt. De eis zelf is correct, maar de specifieke voorbeeldpaden in de claim worden niet bevestigd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel, niet de inhoudelijke naamgevingsregels van de ADR.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Meervoud voor collecties wordt niet als expliciete regel behandeld. De bron gebruikt wel meervoud in voorbeelden (e.g. /collections/gebouwen) maar formuleert geen MUST-regel hierover.*

### `ls-api-0032` — SKILL.md:110 *(§ Naamgeving)*

> Interfaces MOETEN in het Nederlands worden gedefinieerd tenzij er een officieel Engelstalig begrippenkader bestaat.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — naamgeving

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Resources and the underlying attributes SHOULD be defined in the Dutch language unless there is an official English glossary available.
  - *De bron zegt SHOULD, niet MUST zoals de claim stelt. De claim gebruikt 'MOETEN' (MUST), maar de spec gebruikt SHOULD — dit is een verschil in normativiteit.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel, niet de inhoudelijke naamgevingsregels van de ADR.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Taalkeuze (Nederlands/Engels) voor interface-definities wordt niet behandeld.*

### `ls-api-0033` — SKILL.md:111 *(§ Naamgeving)*

> Een API SHOULD geen framework-, platform- of databasenamen blootleggen in resource-paden (ADR).

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD_NOT  ·  **Scope:** API Design Rules — naamgeving

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > The API SHOULD not expose information about the technical components being used, such as development platforms/frameworks or database systems.
  - *De bron bevestigt dat platforms/frameworks en databasesystemen niet blootgelegd mogen worden (SHOULD NOT), maar spreekt specifiek over implementatiedetails in het algemeen, niet uitsluitend over 'resource-paden'. De strekking klopt, de locatie-specificiteit (resource-paden) wordt niet expliciet vermeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel, niet de inhoudelijke API-ontwerpregels.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Het niet blootleggen van framework- of databasenamen in resource-paden wordt niet behandeld.*

### `ls-api-0036` — SKILL.md:117 *(§ OpenAPI Documentatie)*

> Contactinformatie (`info.contact` met `name`, `email`, `url`) wordt sterk aanbevolen voor publieke APIs (ADR `/core/doc-openapi-contact`: SHOULD).

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** API Design Rules — OpenAPI documentatie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > OpenAPI definition document SHOULD include the info.contact object for publicly available APIs. Contact information SHOULD NOT be a generic contact address for the whole organisation. [...] Relevant contact information can include an email address and issue tracker.
  - *De bron bevestigt SHOULD en vermeldt name, url en email als velden in het voorbeeld. De claim stelt dat name, email en url 'sterk aanbevolen' zijn, wat klopt. Echter, de bron zegt alleen dat relevante contactinfo 'can include' email en issue tracker — de drie velden worden alleen als voorbeeld in de JSON getoond, niet expliciet als vereiste velden benoemd in de normatieve tekst.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel, niet de inhoudelijke ADR-regels over contactinformatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron behandelt geen OpenAPI contactinformatie of info.contact velden.*

### `ls-api-0045` — SKILL.md:142 *(§ Geospatial Module (v1.0.3 — vastgesteld))*

> De Geospatial module (v1.0.3, vastgesteld) is verplicht bij geospatiale data en regelt GeoJSON encodering, bounding box filtering en coördinaatsystemen (CRS).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — Geospatial module

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > This document describes the Geospatial module, containing rules for geospatial content and functions in APIs. [...] This is the definitive version of this document.
  - *De bron bevestigt dat het om versie 1.0.3 (definitief/vastgesteld) gaat en behandelt GeoJSON encodering, bounding box filtering en CRS. De bron zegt echter nergens expliciet dat de module 'verplicht' is bij geospatiale data; de normatieve status impliceert dat, maar de claim van 'verplicht' staat niet letterlijk in de bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. De Geospatial module wordt niet besproken.*

## UNGROUNDED — geen bron ondersteunt de claim (6)

### `ls-api-0013` — SKILL.md:56 *(§ URI-ontwerp)*

> Query-parameters MOETEN camelCase gebruiken: `?sortOrder=desc`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — URI-ontwerp

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen regel over camelCase voor query-parameters. Dit onderwerp wordt niet normatief behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *camelCase voor query-parameters wordt niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *CamelCase voor query-parameters wordt niet behandeld in deze bron.*
</details>

### `ls-api-0015` — SKILL.md:58 *(§ URI-ontwerp)*

> URIs mogen geen bestandsextensies bevatten; gebruik Accept-header voor content negotiation.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** API Design Rules — URI-ontwerp

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen regel over bestandsextensies in URIs of het gebruik van Accept-header voor content negotiation in dit verband.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Bestandsextensies in URIs en content negotiation via Accept-header worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Bestandsextensies in URIs en content negotiation via Accept-header worden niet behandeld.*
</details>

### `ls-api-0023` — SKILL.md:83 *(§ Foutafhandeling)*

> Foutresponses MOETEN het mediatype `application/problem+json` (RFC 9457) gebruiken.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — foutafhandeling

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc9457.txt](https://www.rfc-editor.org/rfc/rfc9457.txt)
  - *De bron is RFC 9457 zelf, die het application/problem+json formaat definieert. De claim gaat over een verplichting in de Nederlandse API Design Rules om dit mediatype te gebruiken. RFC 9457 legt geen verplichting op aan API Design Rules of vergelijkbare nationale standaarden — dat is een externe beleidskeuze. De bron is dus niet de juiste bron om deze claim te verifiëren.*

### `ls-api-0026` — SKILL.md:100 *(§ Datum en tijd)*

> Bij `date-time` velden MOET altijd een timezone worden gespecificeerd (bijv. `2026-04-11T10:30:00+02:00`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — datum en tijd

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen regels over date-time velden of timezone specificatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *date-time velden en timezone-specificatie worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Timezone in date-time velden wordt niet behandeld in deze bron.*
</details>

### `ls-api-0027` — SKILL.md:101 *(§ Datum en tijd)*

> Wanneer alleen een datum nodig is, MOET `format: date` worden gebruikt in plaats van `date-time`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — datum en tijd

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen regels over het gebruik van format: date versus format: date-time.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *format: date versus date-time wordt niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Gebruik van format: date wordt niet behandeld.*
</details>

### `ls-api-0028` — SKILL.md:102 *(§ Datum en tijd)*

> Voor properties die datum of tijd bevatten MOET altijd een `format` worden gespecificeerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — datum en tijd

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen regels of vermeldingen over het specificeren van een `format` voor datum/tijd-properties.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Format-specificatie voor datum/tijd properties wordt niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Format-specificatie voor datum/tijd properties wordt niet behandeld.*
</details>

## KNOWN_DISCREPANCY — gedocumenteerd in conflicts.md (6)

### `ls-api-0039` — SKILL.md:126 *(§ Transport Security (TLS))*

> Alle verbindingen MOETEN TLS gebruiken (wettelijk verplicht). Volg de laatste NCSC-richtlijnen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — Transport Security

**Erkend in conflicts.md** *(§ Transport Security module: dubbelzinnige status)*: conflicts.md §'Transport Security module': repo is gearchiveerd, inhoud ingebed als sectie 3.8 in ADR v2.1.0, module v1.0 nog normatief in leeswijzer. NOT_FOUND in gearchiveerde repo is verwacht; claim kan via ADR v2.1.0 worden geverifieerd.

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De aangeleverde brontekst bevat alleen de GitHub-repositorypagina met navigatie, metadata en een korte beschrijving. De inhoud van transport-security.md is niet meegeleverd. Er is geen inhoudelijke tekst over TLS of NCSC-richtlijnen.*

### `ls-api-0040` — SKILL.md:132 *(§ Transport Security (TLS))*

> De header `Cache-Control: no-store` is verplicht in alle API-responses.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — Transport Security verplichte headers

**Erkend in conflicts.md** *(§ Transport Security module: dubbelzinnige status)*: conflicts.md §'Transport Security module': repo is gearchiveerd, inhoud ingebed in ADR v2.1.0 sectie 3.8. NOT_FOUND in gearchiveerde repo is verwacht; verificatie loopt via ADR v2.1.0.

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De aangeleverde brontekst bevat geen inhoud van de specificatie. Alleen GitHub UI-tekst en bestandslijsten zijn zichtbaar.*

### `ls-api-0041` — SKILL.md:133 *(§ Transport Security (TLS))*

> De header `Content-Security-Policy: frame-ancestors 'none'` is verplicht in alle API-responses.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — Transport Security verplichte headers

**Erkend in conflicts.md** *(§ Transport Security module: dubbelzinnige status)*: conflicts.md §'Transport Security module': repo is gearchiveerd, inhoud ingebed in ADR v2.1.0 sectie 3.8. NOT_FOUND in gearchiveerde repo is verwacht; verificatie loopt via ADR v2.1.0.

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De aangeleverde brontekst bevat geen inhoud van de specificatie. Alleen GitHub UI-tekst en bestandslijsten zijn zichtbaar.*

### `ls-api-0042` — SKILL.md:135 *(§ Transport Security (TLS))*

> De header `Strict-Transport-Security` is verplicht in alle API-responses.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — Transport Security verplichte headers

**Erkend in conflicts.md** *(§ Transport Security module: dubbelzinnige status)*: conflicts.md §'Transport Security module': repo is gearchiveerd, inhoud ingebed in ADR v2.1.0 sectie 3.8. NOT_FOUND in gearchiveerde repo is verwacht; verificatie loopt via ADR v2.1.0.

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De aangeleverde brontekst bevat geen inhoud van de specificatie. Alleen GitHub UI-tekst en bestandslijsten zijn zichtbaar.*

### `ls-api-0043` — SKILL.md:136 *(§ Transport Security (TLS))*

> De header `X-Content-Type-Options: nosniff` is verplicht in alle API-responses.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — Transport Security verplichte headers

**Erkend in conflicts.md** *(§ Transport Security module: dubbelzinnige status)*: conflicts.md §'Transport Security module': repo is gearchiveerd, inhoud ingebed in ADR v2.1.0 sectie 3.8. NOT_FOUND in gearchiveerde repo is verwacht; verificatie loopt via ADR v2.1.0.

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De aangeleverde brontekst bevat geen inhoud van de specificatie. Alleen GitHub UI-tekst en bestandslijsten zijn zichtbaar.*

### `ls-api-0044` — SKILL.md:137 *(§ Transport Security (TLS))*

> De header `X-Frame-Options: DENY` is verplicht in alle API-responses.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — Transport Security verplichte headers

**Erkend in conflicts.md** *(§ Transport Security module: dubbelzinnige status)*: conflicts.md §'Transport Security module': repo is gearchiveerd, inhoud ingebed in ADR v2.1.0 sectie 3.8. NOT_FOUND in gearchiveerde repo is verwacht; verificatie loopt via ADR v2.1.0.

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De aangeleverde brontekst bevat geen inhoud van de specificatie. Alleen GitHub UI-tekst en bestandslijsten zijn zichtbaar.*

## GROUNDED — minstens één bron ondersteunt de claim (20)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-api-0001` — SKILL.md:24 *(§ API Design Rules (NL GOV))*

> De API Design Rules zijn verplicht onder het 'pas-toe-of-leg-uit' regime van het Forum Standaardisatie.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules (ADR) — NL GOV

- **SUPPORTED** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/rest-api-design-rules](https://www.forumstandaardisatie.nl/open-standaarden/rest-api-design-rules)
  > Lijst status Verplicht ('Pas toe leg uit') [...] De standaard NLGov REST API Design Rules moet worden toegepast bij het aanbieden van REST API's ten behoeve van het ontsluiten van overheidsinformatie en/of functionaliteit.
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > This version of the design rules has been submitted to Forum Standaardisatie for inclusion on the Comply or Explain list of mandatory standards in the Dutch Public Sector.
  - *De bron zegt dat de standaard is 'ingediend voor opname' op de lijst, niet dat deze er al verplicht op staat. De claim stelt dat de ADR 'verplicht' is onder het pas-toe-of-leg-uit regime, maar de bron bevestigt alleen de indiening.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  > De status van de ADR-standaard is 'Verplicht (pas toe leg uit)'. Dit houdt kort gezegd in dat Nederlandse overheden en instellingen uit de (semi) publieke sector verplicht zijn deze standaard toe te passen op het moment dat zij REST API's gaan gebruiken voor het ontsluiten van overheidsinformatie en/of functionaliteit.
- **NOT_FOUND** (low) — [https://www.forumstandaardisatie.nl/open-standaarden](https://www.forumstandaardisatie.nl/open-standaarden)
  - *De brontekst vermeldt slechts de navigatiestructuur en paginatitels van de Forum Standaardisatie website, zonder een specifieke lijst van standaarden die onder het 'pas toe of leg uit'-regime vallen. De API Design Rules worden nergens expliciet genoemd. De tekst bevestigt wél dat er een 'pas toe of leg uit'-lijst bestaat, maar welke standaarden daarop staan is niet uit deze brontekst op te maken.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron beschrijft de technische inhoud van de Geospatial Module (ADR mod-geo). Forum Standaardisatie en het 'pas-toe-of-leg-uit' regime worden niet behandeld.*

### `ls-api-0002` — SKILL.md:32 *(§ Versiemodel)*

> De vastgestelde ADR-versie (DEF) wordt gepubliceerd op `gitdocumentatie.logius.nl`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — versiemodel

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > This version: https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0/
  - *De vastgestelde versie wordt gepubliceerd op gitdocumentatie.logius.nl, zoals de bron zelf laat zien.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  > Versie 1.0 van de ADR is gepubliceerd op: https://gitdocumentatie.logius.nl/publicatie/api/adr/1.0 De laatste versie van de ADR is gepubliceerd op: https://gitdocumentatie.logius.nl/publicatie/api/adr/
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > This version: https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3/
  - *De bron bevestigt dat de definitieve (vastgestelde) versie wordt gepubliceerd op gitdocumentatie.logius.nl, maar dan voor de Geospatial Module, niet voor de ADR zelf. De claim gaat over ADR in het algemeen.*

### `ls-api-0003` — SKILL.md:33 *(§ Versiemodel)*

> De ADR werkversie (draft) wordt gepubliceerd op `logius-standaarden.github.io`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — versiemodel

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Latest editor's draft: https://logius-standaarden.github.io/API-Design-Rules/
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  > De laatste concept versie van de standard is gepubliceerd op: https://logius-standaarden.github.io/API-Design-Rules/
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > Latest editor's draft: https://logius-standaarden.github.io/API-mod-geospatial/
  - *De bron bevestigt dat de editor's draft op logius-standaarden.github.io staat, maar dit geldt voor de Geospatial Module, niet expliciet voor de ADR zelf.*

### `ls-api-0006` — SKILL.md:35 *(§ Versiemodel)*

> De inhoud van Transport Security is in ADR v2.1.0 ingebed als sectie 3.8 met eigen regels (`/core/transport/*`).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Transport Security module

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > 3.8 Transport Security ... technical /core/transport/tls ... technical /core/transport/security-headers ... technical /core/transport/cors
  - *Sectie 3.8 met eigen /core/transport/* regels is duidelijk aanwezig in de bron.*

### `ls-api-0014` — SKILL.md:57 *(§ URI-ontwerp)*

> URIs mogen geen trailing slashes bevatten: `/api/v1/users` (niet `/api/v1/users/`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** API Design Rules — URI-ontwerp

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > A URI MUST never contain a trailing slash. When requesting a resource including a trailing slash, this MUST result in a 404 (not found) error response and not a redirect.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Trailing slashes in URIs worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Trailing slashes in URIs worden niet behandeld in deze bron.*

### `ls-api-0017` — SKILL.md:60 *(§ URI-ontwerp)*

> Operaties als sub-resources: het laatste padsegment mag starten met `_` (bijv. `/_search`).

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** API Design Rules — URI-ontwerp

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Use the imperative mood of a verb, maybe even prefix it with a underscore to distinguish these resources from regular resources. For example: /search or /_search.
- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > /geo/geometric-context : Place results of a global spatial query in the relevant geometric context In case of a global query /api/v1/_search
  - *De bron gebruikt het patroon `_search` als voorbeeld van een sub-resource met underscore-prefix, wat de claim ondersteunt. De regel zelf is echter niet expliciet als MAY geformuleerd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Sub-resources met underscore-prefix worden niet behandeld in dit beheermodel.*

### `ls-api-0018` — SKILL.md:61 *(§ URI-ontwerp)*

> Gevoelige informatie MAG NIET in URIs worden opgenomen (niet beschermd door TLS).

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** API Design Rules — URI-ontwerp

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Do not put any sensitive information in URIs ... URIs can be cached and logged outside of the servers controlled by clients and servers ... MUST NOT contain any sensitive information. This includes client secrets used for authentication, privacy sensitive information suchs as BSNs
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Gevoelige informatie in URIs wordt niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Gevoelige informatie in URIs wordt niet behandeld in deze bron.*

### `ls-api-0019` — SKILL.md:67 *(§ HTTP-methoden)*

> De HTTP GET-methode is veilig en idempotent en mag een resource NOOIT wijzigen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** API Design Rules — HTTP-methoden

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Method Safe Idempotent GET Yes Yes ... GET Read Retrieve a resource representation for the given URI. Data is only retrieved and never modified.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *HTTP GET-methode en veiligheid/idempotentie worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *HTTP GET veiligheid en idempotentie worden niet behandeld in deze bron.*

### `ls-api-0020` — SKILL.md:76 *(§ Versiebeheer)*

> De volledige versie MOET worden opgenomen in de `API-Version` response header: bijv. `1.2.3`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — versiebeheer

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > The version number MUST be returned in an HTTP response header named API-Version (case-insensitive) and SHOULD not be prefixed. An example of an API version response header: API-Version: 1.0.2
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *API-Version response header wordt niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De API-Version response header wordt niet behandeld in deze bron.*

### `ls-api-0021` — SKILL.md:77 *(§ Versiebeheer)*

> Semantic versioning (major.minor.patch) MOET worden gebruikt in `info.version` van de OpenAPI spec.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — versiebeheer

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Version numbering MUST follow the Semantic Versioning [SemVer] model to prevent breaking changes when releasing new API versions. Release versions are formatted using the major.minor.patch template
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Semantic versioning in info.version van OpenAPI spec wordt niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Semantic versioning in info.version van OpenAPI wordt niet behandeld.*

### `ls-api-0022` — SKILL.md:78 *(§ Versiebeheer)*

> Bij major version changes MOET een deprecation schedule worden gepubliceerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — versiebeheer

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > When deprecating features or versions, a deprecation schedule MUST be published.
  - *De bron stelt dit breder dan alleen bij major version changes (ook bij het deprecaten van features), maar de kern van de claim wordt ondersteund.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Deprecation schedules bij major version changes worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Deprecation schedule bij major version changes wordt niet behandeld.*

### `ls-api-0024` — SKILL.md:95 *(§ Foutafhandeling)*

> Foutmeldingen MOGEN GEEN technische details bevatten zoals stack traces of interne hints.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** API Design Rules — foutafhandeling

- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > In case of an error, the server SHOULD NOT pass technical details (e.g. call stacks or other internal hints) to the client. The error message SHOULD be generic to avoid revealing additional details
  - *De bron gebruikt SHOULD NOT, niet MUST NOT. De claim gebruikt MOGEN GEEN (MUST NOT). Dit is een subtiel verschil in modaliteit maar de strekking is gelijk.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Inhoudelijke regels over foutmeldingen en stack traces worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Foutmeldingen en het vermijden van technische details worden niet behandeld.*

### `ls-api-0030` — SKILL.md:107 *(§ Naamgeving)*

> Resources MOETEN als zelfstandige naamwoorden worden benoemd, niet als werkwoorden.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — naamgeving

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Resources are referred to using nouns (instead of verbs) that represent entities meaningful to the API consumer. [...] This is different than RPC-style APIs, where verbs are often used to perform certain actions
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel, niet de inhoudelijke naamgevingsregels van de ADR.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Naamgeving van resources als zelfstandige naamwoorden wordt niet behandeld.*

### `ls-api-0034` — SKILL.md:115 *(§ OpenAPI Documentatie)*

> Een OpenAPI 3.0+ specificatie is verplicht.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — OpenAPI documentatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > API documentation MUST be provided in the form of an OpenAPI definition document which conforms to the OpenAPI Specification (from v3 onwards).
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel, niet de inhoudelijke vereisten van de ADR.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De verplichting van een OpenAPI 3.0+ specificatie wordt niet behandeld in deze bron.*

### `ls-api-0035` — SKILL.md:116 *(§ OpenAPI Documentatie)*

> De OpenAPI spec in JSON MOET op de standaardlocatie `/openapi.json` worden gepubliceerd (VERPLICHT); YAML (`/openapi.yaml`) is OPTIONEEL.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — OpenAPI documentatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > The standard location for the OAS document is a URI called openapi.json or openapi.yaml within the base path of the API. [...] At least the JSON format MUST be supported. [...] Optionally, the same OAS document MAY be provided in YAML format
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel, niet de inhoudelijke vereisten over OpenAPI-locaties.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron gaat over de Geospatial module. Niets over OpenAPI spec locaties (/openapi.json, /openapi.yaml) staat in deze bron.*

### `ls-api-0037` — SKILL.md:117 *(§ OpenAPI Documentatie)*

> De Spectral linter dwingt contactvelden af als error voor publieke APIs.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Spectral linter

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > info-contact: error [...] info-contact-fields-exist: severity: error given: - "$.info.contact" then: function: schema functionOptions: schema: required: - email - name - url message: "Missing fields in `info.contact` field. Must specify email, name and url."
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst bevat geen informatie over Spectral linter gedrag of error-niveaus.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen informatie over Spectral linter regels of contactvelden.*

### `ls-api-0038` — SKILL.md:118 *(§ OpenAPI Documentatie)*

> CORS MOET worden ondersteund voor documentatie-toegang.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules — OpenAPI documentatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Clients (such as Swagger UI or ReDoc) MUST be able to retrieve the document without having to authenticate. Furthermore, the CORS policy for this URI MUST allow external domains to read the documentation from a browser environment.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel, niet de inhoudelijke CORS-vereisten.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *CORS wordt niet behandeld in deze Geospatial module bron.*

### `ls-api-0051` — SKILL.md:241 *(§ Spectral Linter)*

> De publieke DON-hosted ruleset is beschikbaar op `https://static.developer.overheid.nl/adr/ruleset.yaml`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Spectral linter

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > curl -L https://static.developer.overheid.nl/adr/ruleset.yaml > .spectral.yml
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. De URL van de DON-hosted ruleset wordt niet vermeld.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen verwijzing naar static.developer.overheid.nl of Spectral rulesets.*

### `ls-api-0052` — SKILL.md:257 *(§ Spectral Linter)*

> Spectral regel `include-major-version-in-uri` / `nlgov:include-major-version-in-uri` controleert of de major versie in het URI-pad aanwezig is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Spectral linter regels

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > include-major-version-in-uri: severity: error given: - "$.servers[*]" then: function: pattern functionOptions: match: "\/v[\d+]" field: url message: "/core/uri-version: Include the major version number in the URI"
  - *De claim noemt ook `nlgov:include-major-version-in-uri` als alternatieve naam; de bron gebruikt alleen `include-major-version-in-uri`. Het bestaan van de regel wordt bevestigd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. Specifieke Spectral regelnames worden niet besproken.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron behandelt geen Spectral linter regels over URI versioning.*

### `ls-api-0053` — SKILL.md:262 *(§ Spectral Linter)*

> Spectral regel `use-problem-schema` / `nlgov:use-problem-schema` controleert gebruik van problem+json voor foutresponses.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** API Design Rules — Spectral linter regels

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > use-problem-schema: severity: warn message: "The content type of an error response should be application/problem+json or application/problem+xml to match RFC 9457." given: $..[responses][?(@property && @property.match(/(4|5)\d\d/))].content
  - *De claim noemt ook `nlgov:use-problem-schema`; de bron gebruikt alleen `use-problem-schema`. De kern van de claim wordt bevestigd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst beschrijft het beheermodel voor de ADR. Specifieke Spectral regelnames worden niet besproken.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen Spectral regels over problem+json foutresponses.*

</details>
