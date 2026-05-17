<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit ls-api — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 13 | 19% |
| CONTRADICTED | 1 | 1% |
| PARTIALLY_GROUNDED | 6 | 9% |
| UNGROUNDED | 15 | 22% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 2 | 3% |
| GROUNDED | 31 | 46% |

*Geverifieerd met sonnet, 25 calls, $2.0571.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (13)

### `ls-api-0004` — SKILL.md:35 *(§ Versiemodel)*

> ADR-modules hebben geen eigen vaststellingsproces; ze ontlenen hun status aan de standaard die ernaar verwijst.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — versiemodel modules

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron behandelt het vaststellingsproces van ADR-modules niet.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron beschrijft het beheermodel van de ADR-standaard zelf, maar behandelt niet het vaststellingsproces van modules of extensies afzonderlijk.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron beschrijft de inhoud van de Geospatial module maar zegt niets over het vaststellingsproces van modules of hun statusontlening aan een overkoepelende standaard.*
</details>

### `ls-api-0031` — SKILL.md:103 *(§ Datum en tijd)*

> De Spectral linter bevat 4 regels die datum/tijd vereisten afdwingen: `date-time-ensure-timezone`, `specify-format-for-date-and-time`, `time-without-timezone`, `use-date-instead-of-datetime`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter datum/tijd

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De linter configuratie in de bron bevat geen van de vier genoemde datum/tijd regels (`date-time-ensure-timezone`, `specify-format-for-date-and-time`, `time-without-timezone`, `use-date-instead-of-datetime`).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Spectral linter-regels worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Spectral linter regels voor datum/tijd worden niet vermeld in deze bron.*
</details>

### `ls-api-0052` — SKILL.md:146 *(§ Signing Module (JAdES) — draft)*

> De Signing module is nog in concept (draft) en is nog niet goedgekeurd door het Technisch Overleg.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Signing module

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron vermeldt Signing als aparte extensie maar geeft geen informatie over de draftstatus of goedkeuring door een Technisch Overleg.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De Signing module wordt niet vermeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De Signing module wordt niet behandeld in deze Geospatial module bron.*
</details>

### `ls-api-0053` — SKILL.md:148 *(§ Signing Module (JAdES) — draft)*

> De Signing module gebruikt JAdES detached signatures met RSASSA-PSS (PS256), minimaal 256 bits.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Signing module

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen inhoudelijke informatie over JAdES detached signatures of RSASSA-PSS algoritmes.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Technische details van de Signing module worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *JAdES detached signatures en RSASSA-PSS worden niet behandeld in deze bron.*
</details>

### `ls-api-0054` — SKILL.md:148 *(§ Signing Module (JAdES) — draft)*

> Signatures van de Signing module worden geplaatst in `Payload-Signature` en `Message-Signature` HTTP headers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Signing module

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen informatie over `Payload-Signature` of `Message-Signature` HTTP headers.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *HTTP headers voor signing worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Payload-Signature en Message-Signature HTTP headers worden niet behandeld in deze bron.*
</details>

### `ls-api-0055` — SKILL.md:148 *(§ Signing Module (JAdES) — draft)*

> De OpenAPI representatie voor signing gebruikt `format: jws-compact-detached`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Signing module

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen informatie over `format: jws-compact-detached` in OpenAPI representaties.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *OpenAPI-representatie voor signing wordt niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *OpenAPI representatie voor signing (format: jws-compact-detached) wordt niet behandeld in deze bron.*
</details>

### `ls-api-0056` — SKILL.md:152 *(§ Encryption Module (JWE) — draft)*

> De Encryption module is nog in concept (draft) en is nog niet goedgekeurd door het Technisch Overleg.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Encryption module

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron vermeldt Encryption als aparte extensie maar geeft geen informatie over de draftstatus of goedkeuring door een Technisch Overleg.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De Encryption module wordt niet vermeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De Encryption module wordt niet behandeld in deze Geospatial module bron.*
</details>

### `ls-api-0057` — SKILL.md:154 *(§ Encryption Module (JWE) — draft)*

> De Encryption module (JWE) is bedoeld voor end-to-end versleuteling van request/response payloads wanneer transport-level encryptie niet voldoende is, bijv. bij niet-vertrouwde intermediairs.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Encryption module

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen inhoudelijke informatie over JWE of end-to-end encryptie van payloads bij niet-vertrouwde intermediairs.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Technische details van de Encryption module worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *JWE end-to-end versleuteling van payloads wordt niet behandeld in deze bron.*
</details>

### `ls-api-0058` — SKILL.md:237 *(§ Spectral Linter)*

> De DON-hosted Spectral ruleset bevat 11 regels; de GitHub-versie bevat 22 regels (inclusief 11 extra checks voor datum/tijd, naamgeving en foutafhandeling).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat de Spectral linter configuratie maar geeft geen expliciete telling van het aantal regels (11 of 22). Het tellen van de regels in de bron levert ongeveer 12-13 named rules op, maar de claim over twee versies (DON-hosted vs GitHub) met specifieke aantallen is niet verifieerbaar vanuit deze tekst.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Aantallen Spectral-regels in de DON-hosted of GitHub-versie worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Spectral ruleset aantallen regels (11 DON-hosted vs. 22 GitHub) worden niet behandeld in deze bron.*
</details>

### `ls-api-0065` — SKILL.md:265 *(§ Spectral Linter)*

> De Spectral regel `nlgov:query-keys-camel-case` is alleen beschikbaar in de GitHub-versie en controleert camelCase query parameters.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter (GitHub-versie)

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De brontekst bevat de Spectral linter configuratie volledig, maar een regel `nlgov:query-keys-camel-case` of `query-keys-camel-case` ontbreekt daarin geheel. De bron bevat `schema-camel-case` en `property-casing`, maar niet een regel voor camelCase query parameters.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst bevat geen informatie over Spectral regels, GitHub-versies van linters, of `nlgov:query-keys-camel-case`.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron beschrijft de API Design Rules Module Geospatial. Er is geen vermelding van Spectral linter regels of `nlgov:query-keys-camel-case` in de brontekst.*
</details>

### `ls-api-0066` — SKILL.md:268 *(§ Spectral Linter)*

> De Spectral regel `nlgov:semver` is alleen beschikbaar in de GitHub-versie en controleert het semantic versioning formaat.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter (GitHub-versie)

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De brontekst bevat de volledige Spectral linter configuratie van ADR 2.1.0, maar een regel `nlgov:semver` of `semver` voor semantic versioning controle is daarin niet aanwezig. De standaard verwijst naar /core/semver als design rule, maar er is geen bijbehorende Spectral regel in de gepubliceerde configuratie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst bevat geen informatie over Spectral regels, GitHub-versies van linters, of `nlgov:semver`.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron beschrijft de API Design Rules Module Geospatial. Er is geen vermelding van Spectral linter regels of `nlgov:semver` in de brontekst.*
</details>

### `ls-api-0067` — SKILL.md:271 *(§ Spectral Linter)*

> De Spectral regel `nlgov:problem-schema-members` controleert verplichte velden in problem+json schema conform RFC 9457.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter (GitHub-versie)

- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc9457.txt](https://www.rfc-editor.org/rfc/rfc9457.txt)
  - *RFC 9457 bevat geen enkele verwijzing naar Spectral, linters, of de nlgov:problem-schema-members regel. Dit is een implementatiedetail van de Nederlandse API Design Rules tooling, niet van de RFC zelf.*

### `ls-api-0068` — reference.md:50 *(§ Implementatievoorbeelden)*

> Referentie-implementaties voor de ADR zijn beschikbaar in ASP.NET en Quarkus.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — implementatievoorbeelden

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De brontekst bevat geen verwijzing naar referentie-implementaties in ASP.NET of Quarkus. Dit onderwerp wordt in deze versie van de ADR spec niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst noemt geen referentie-implementaties in ASP.NET of Quarkus. Wel wordt validatie via API-test.nl en Developer.overheid.nl genoemd, maar dit zijn testtools, geen referentie-implementaties.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron beschrijft de API Design Rules Module Geospatial. Er is geen vermelding van referentie-implementaties in ASP.NET of Quarkus in de brontekst.*
</details>

## CONTRADICTED — bron spreekt de claim expliciet tegen (1)

### `ls-api-0036` — SKILL.md:111 *(§ Naamgeving)*

> Implementatiedetails zoals framework- of databasenamen MOGEN NIET in URIs worden verborgen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** ADR — naamgeving

- **CONTRADICTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > An API SHOULD not expose implementation details of the underlying application, development platforms/frameworks or database systems/persistence models.
  - *De claim stelt dat implementatiedetails NIET in URIs verborgen mogen worden (MUST NOT), maar de bron zegt dat een API implementatiedetails SHOULD NOT blootstellen — dit is een zwakkere norm dan MUST NOT. Bovendien gaat de regel over het niet blootstellen (niet verbergen) van implementatiedetails, wat de omgekeerde formulering is van de claim.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *URI-ontwerpregels over implementatiedetails worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Verbod op implementatiedetails in URIs wordt niet behandeld in deze bron.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (6)

### `ls-api-0005` — SKILL.md:35 *(§ Versiemodel)*

> De Geospatial module v1.0.x is normatief onderdeel van ADR v2.1.0 en daarmee vastgesteld.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR v2.1.0 — Geospatial module

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > functional /core/geospatial : Apply the geospatial module for geospatial data — The API Design Rules Module: Geospatial version 1.0.x MUST be applied when providing geospatial data or functionality.
  - *De bron bevestigt dat Geospatial module v1.0.x normatief vereist is (MUST), maar zegt niets over een eigen vaststellingsproces of dat de module daarmee 'vastgesteld' is in de formele zin.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron is het beheermodel ADR v1.0 uit 2021. ADR v2.1.0 en de Geospatial module worden niet vermeld.*

### `ls-api-0023` — SKILL.md:78 *(§ Versiebeheer)*

> Bij major version changes MOET een deprecation schedule gepubliceerd worden.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — versiebeheer

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > functional /core/deprecation-schedule : Include a deprecation schedule when deprecating features or versions — When deprecating features or versions, a deprecation schedule MUST be published.
  - *De bron vereist een deprecation schedule bij het deprecaten van features of versies in het algemeen, niet specifiek alleen bij major version changes. De claim koppelt het expliciet aan major version changes, wat een beperking is die de bron niet maakt.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen regels over deprecation schedules bij major version changes.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over deprecation schedules bij major version changes.*

### `ls-api-0025` — SKILL.md:83 *(§ Foutafhandeling)*

> Foutresponses MOETEN `application/problem+json` (RFC 9457) gebruiken.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — foutafhandeling

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc9457.txt](https://www.rfc-editor.org/rfc/rfc9457.txt)
  > The data model for problem details is a JSON [JSON] object; when serialized as a JSON document, it uses the "application/problem+json" media type.
  - *RFC 9457 definieert application/problem+json als het media type voor problem details en beschrijft het formaat uitgebreid, maar legt geen MUST-verplichting op aan API-implementors om dit te gebruiken. De spec zegt dat foutresponses dit formaat KAN gebruiken ('Problem details can be used with any HTTP status code'), niet dat het verplicht is. De MUST-claim is dus sterker dan wat de RFC zelf voorschrijft — die verplichting komt waarschijnlijk uit de ADR (API Design Rules), niet uit RFC 9457 zelf. De bron ondersteunt het gebruik van application/problem+json maar niet de MUST-modaliteit.*

### `ls-api-0033` — SKILL.md:108 *(§ Naamgeving)*

> Collecties MOETEN in meervoud worden benoemd: `/users`, `/orders`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — naamgeving

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Collection resources are referred to using plural nouns. [...] The path segment describing the name of the collection resource MUST be written in the plural form. Example collection resources: https://api.example.org/v1/gebouwen https://api.example.org/v1/vergunningen
  - *Bron bevestigt meervoud voor collecties maar gebruikt Nederlandse voorbeelden (`gebouwen`, `vergunningen`), niet de Engelstalige voorbeelden `/users` en `/orders` uit de claim.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Naamgevingsregels voor collecties zijn geen onderdeel van dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Naamgeving van collecties in meervoud wordt niet behandeld in deze bron.*

### `ls-api-0035` — SKILL.md:110 *(§ Naamgeving)*

> Interfaces MOETEN in het Nederlands worden gedefinieerd tenzij er een officieel Engelstalig begrippenkader bestaat.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — naamgeving

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Resources and the underlying attributes SHOULD be defined in the Dutch language unless there is an official English glossary available.
  - *De bron zegt SHOULD, niet MUST. De claim stelt MOETEN (MUST). Dit is een verzwakking van de norm.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Taalvereisten voor interface-definities worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Taalvereisten voor interface-definities (Nederlands tenzij officieel Engelstalig begrippenkader) worden niet behandeld in deze bron.*

### `ls-api-0050` — SKILL.md:142 *(§ Geospatial Module (v1.0.3 — vastgesteld))*

> De Geospatial module v1.0.3 is normatief onderdeel van ADR v2.1.0 en is verplicht bij geospatiale data.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — Geospatial module

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > The API Design Rules Module: Geospatial version 1.0.x MUST be applied when providing geospatial data or functionality.
  - *De bron bevestigt dat de Geospatial module verplicht is bij geospatiale data, maar vermeldt versie `1.0.x` (niet specifiek `v1.0.3`). De versieclaim `v1.0.3` is niet verifieerbaar vanuit deze bron.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > This document is part of the Nederlandse API Strategie. [...] Normative module GEO module v1.0 [...] This is the definitive version of this document.
  - *De bron bevestigt dat dit document een normatief onderdeel is van de Nederlandse API Strategie en dat het de definitieve versie is (1.0.3). De claim over 'ADR v2.1.0' specifiek en 'verplicht bij geospatiale data' als zodanig wordt niet letterlijk bevestigd; de bron noemt 'GEO module v1.0' als normatief zonder versienummer 1.0.3 in de statustabel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De Geospatial module en versienummers worden niet beschreven in dit beheermodel.*

## UNGROUNDED — geen bron ondersteunt de claim (15)

### `ls-api-0011` — SKILL.md:55 *(§ URI-ontwerp)*

> Padsegmenten MOETEN kebab-case gebruiken: `/mijn-documenten` (niet `/mijnDocumenten`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — URI-ontwerp

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat een linter-regel (paths-kebab-case) met severity 'warn', niet 'error', die kebab-case aanbeveelt. Er is geen normatieve MUST-regel voor kebab-case padsegmenten in de designrules-tekst zelf.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron is het beheermodel en bevat geen technische URI-ontwerpregels over kebab-case padsegmenten.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over kebab-case padsegmenten in URIs.*
</details>

### `ls-api-0012` — SKILL.md:56 *(§ URI-ontwerp)*

> Query-parameters MOETEN camelCase gebruiken: `?sortOrder=desc`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — URI-ontwerp

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen regel over camelCase query-parameters.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen technische URI-ontwerpregels over camelCase query-parameters.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over camelCase query-parameters.*
</details>

### `ls-api-0014` — SKILL.md:58 *(§ URI-ontwerp)*

> URIs mogen geen bestandsextensies bevatten; gebruik de Accept-header voor content negotiation.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** ADR — URI-ontwerp

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen regel over het verbod op bestandsextensies in URIs of het gebruik van de Accept-header voor content negotiation.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen regels over bestandsextensies in URIs of gebruik van Accept-headers.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over bestandsextensies in URIs of het gebruik van de Accept-header voor content negotiation in deze context.*
</details>

### `ls-api-0028` — SKILL.md:100 *(§ Datum en tijd)*

> Bij `date-time` velden MOET altijd een timezone worden gespecificeerd (bijv. `2026-04-11T10:30:00+02:00`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — datum en tijd

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron bevat geen regels over date-time velden of het verplicht opnemen van een timezone.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen technische regels over datum/tijd-velden of timezone-specificatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over `date-time` velden of timezone-specificatie.*
</details>

### `ls-api-0029` — SKILL.md:101 *(§ Datum en tijd)*

> Gebruik `format: date` wanneer alleen een datum nodig is (niet `date-time`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — datum en tijd

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De brontekst bevat geen regels over datum/tijd formatting of gebruik van `format: date` vs `format: date-time`.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen technische regels over het gebruik van `format: date` versus `date-time`.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over het gebruik van `format: date`.*
</details>

### `ls-api-0030` — SKILL.md:102 *(§ Datum en tijd)*

> Properties die datum of tijd bevatten MOETEN altijd een `format` specificeren.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — datum en tijd

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De brontekst bevat geen regels over verplicht specificeren van `format` voor datum/tijd properties.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron is het ADR Beheermodel (governance/beheer document), niet de technische ADR-specificatie zelf. Technische regels over datum/tijd-properties worden hier niet beschreven.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron gaat over de Geospatial module (GeoJSON, CRS, bounding box). Datum/tijd-properties en format-specificaties worden niet behandeld.*
</details>

### `ls-api-0034` — SKILL.md:109 *(§ Naamgeving)*

> Individuele resources MOETEN in enkelvoud worden benoemd: `/users/{id}`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — naamgeving

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron zegt dat enkelvoudige resources niet in een collectie staan MUST worden benoemd in enkelvoud, maar dit gaat over zelfstandige singular resources, niet over `/users/{id}` als patroon. De claim stelt dat individuele resources binnen een collectie enkelvoud MOETEN gebruiken, wat de bron niet expliciet stelt. De bron bespreekt `/gebouwen/3b9710c4-...` als patroon zonder de naam van het segment enkelvoud te noemen.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Naamgevingsregels voor individuele resources zijn geen onderdeel van dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Naamgeving van individuele resources in enkelvoud wordt niet behandeld in deze bron.*
</details>

### `ls-api-0042` — SKILL.md:126 *(§ Transport Security (TLS))*

> Alle verbindingen MOETEN TLS gebruiken (wettelijk verplicht). Volg de laatste NCSC-richtlijnen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — Transport Security

*Mogelijk relevant in conflicts.md (§ Transport Security module: dubbelzinnige status): conflicts.md § 'Transport Security module' beschrijft de gearchiveerde status van API-mod-transport-security en dat inhoud is ingebed in ADR v2.1.0. Maar specifieke TLS/NCSC-verplichtingen worden niet behandeld. Lage confidence: het onderwerp raakt dezelfde module, maar de concrete claim is niet gedocumenteerd.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De brontekst is alleen de GitHub-repositorypagina (README/navigatie). De inhoud van transport-security.md is niet meegeleverd, dus de TLS-verplichting kan niet worden geverifieerd.*

### `ls-api-0043` — SKILL.md:132 *(§ Transport Security (TLS))*

> De header `Cache-Control: no-store` is verplicht in alle API-responses om caching van gevoelige data te voorkomen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — Transport Security, security headers

*Mogelijk relevant in conflicts.md (§ Transport Security module: dubbelzinnige status): conflicts.md § 'Transport Security module' beschrijft dat de repo gearchiveerd is en content ingebed in ADR v2.1.0, maar de specifieke Cache-Control-verplichting wordt nergens behandeld. Lage confidence.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De inhoud van transport-security.md is niet meegeleverd in de brontekst.*

### `ls-api-0044` — SKILL.md:133 *(§ Transport Security (TLS))*

> De header `Content-Security-Policy: frame-ancestors 'none'` is verplicht in alle API-responses als clickjacking-bescherming.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — Transport Security, security headers

*Mogelijk relevant in conflicts.md (§ Transport Security module: dubbelzinnige status): conflicts.md § 'Transport Security module' behandelt de gearchiveerde repo en inbedding, maar niet de specifieke Content-Security-Policy-verplichting. Lage confidence.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De inhoud van transport-security.md is niet meegeleverd in de brontekst.*

### `ls-api-0045` — SKILL.md:134 *(§ Transport Security (TLS))*

> De header `Content-Type: application/json` is verplicht in alle API-responses.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — Transport Security, security headers

*Mogelijk relevant in conflicts.md (§ Transport Security module: dubbelzinnige status): conflicts.md § 'Transport Security module' raakt dezelfde module-context, maar de verplichting voor Content-Type-header in API-responses is niet als discrepantie gedocumenteerd. Lage confidence.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De inhoud van transport-security.md is niet meegeleverd in de brontekst.*

### `ls-api-0046` — SKILL.md:135 *(§ Transport Security (TLS))*

> De header `Strict-Transport-Security` is verplicht in alle API-responses om HTTPS te vereisen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — Transport Security, security headers

*Mogelijk relevant in conflicts.md (§ Transport Security module: dubbelzinnige status): conflicts.md § 'Transport Security module' beschrijft de module-status maar niet de specifieke Strict-Transport-Security-verplichting. Lage confidence.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De inhoud van transport-security.md is niet meegeleverd in de brontekst.*

### `ls-api-0047` — SKILL.md:136 *(§ Transport Security (TLS))*

> De header `X-Content-Type-Options: nosniff` is verplicht in alle API-responses om MIME sniffing te voorkomen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — Transport Security, security headers

*Mogelijk relevant in conflicts.md (§ Transport Security module: dubbelzinnige status): conflicts.md § 'Transport Security module' raakt de module-context, maar de X-Content-Type-Options-verplichting is niet specifiek gedocumenteerd als discrepantie. Lage confidence.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De inhoud van transport-security.md is niet meegeleverd in de brontekst.*

### `ls-api-0048` — SKILL.md:137 *(§ Transport Security (TLS))*

> De header `X-Frame-Options: DENY` is verplicht in alle API-responses als clickjacking-bescherming.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — Transport Security, security headers

*Mogelijk relevant in conflicts.md (§ Transport Security module: dubbelzinnige status): conflicts.md § 'Transport Security module' behandelt de gearchiveerde repo en inbedding, maar niet de specifieke X-Frame-Options-verplichting. Lage confidence.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De inhoud van transport-security.md is niet meegeleverd in de brontekst.*

### `ls-api-0049` — SKILL.md:138 *(§ Transport Security (TLS))*

> De header `Access-Control-Allow-Origin` is verplicht in alle API-responses voor het CORS-beleid.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — Transport Security, security headers

*Mogelijk relevant in conflicts.md (§ Transport Security module: dubbelzinnige status): conflicts.md § 'Transport Security module' raakt de module-context, maar de Access-Control-Allow-Origin-verplichting voor CORS is niet als discrepantie gedocumenteerd. Lage confidence.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De inhoud van transport-security.md is niet meegeleverd in de brontekst.*

## KNOWN_DISCREPANCY — gedocumenteerd in conflicts.md (2)

### `ls-api-0008` — SKILL.md:41 *(§ Repositories)*

> ADR v2.1.0 is de vastgestelde versie, gepubliceerd op https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — hoofdspecificatie

**Erkend in conflicts.md** *(§ ADR werkversie-nummering op draft-pagina)*: conflicts.md § 'ADR werkversie-nummering op draft-pagina': de draft-pagina (logius-standaarden.github.io/API-Design-Rules) toont nog versienummer '2.1.0' terwijl v2.1.0 ook de DEF-versie is. 'Het versienummer in ReSpec is simpelweg nog niet opgehoogd.' CONTRADICTED-verdict op GitHub Pages is dus gedocumenteerde keuze.

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > NLGov REST API Design Rules 2.1.0 Logius Standard Definitive version August 27, 2025 This version: https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0/
- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules)
  > Releases 8 v2.1.0 Latest Sep 29, 2025
  - *De bron bevestigt dat v2.1.0 de meest recente release is. De publicatie-URL https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0/ wordt niet expliciet vermeld in de brontekst.*
- **CONTRADICTED** (high) — [https://logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules)
  > Previous version: https://gitdocumentatie.logius.nl/publicatie/api/adr/2.0.2/
  - *De bron vermeldt v2.0.2 als de vorige versie en is zelf een draft zonder versienummer in de header dat overeenkomt met v2.1.0. Er is geen bevestiging dat v2.1.0 de vastgestelde versie is; de meest recente gepubliceerde versie die wordt genoemd is 2.0.2.*
- **PARTIALLY_SUPPORTED** (medium) — [https://logius-standaarden.github.io/API-Standaarden-Beheermodel](https://logius-standaarden.github.io/API-Standaarden-Beheermodel)
  > Formele standaard: NLGov API Design Rules (ADR) 2.1.0 — Gepubliceerde versie: 2.1.0
  - *De bron bevestigt dat ADR 2.1.0 de gepubliceerde versie is, maar de specifieke publicatie-URL https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0/ wordt niet vermeld in de bron.*
<details><summary>13x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron is het beheermodel uit 2021 en vermeldt alleen ADR v1.0 als vastgestelde versie. ADR v2.1.0 wordt niet vermeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron gaat over de Geospatial module v1.0.3, niet over ADR v2.1.0.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel)
  - *De bron bevat geen informatie over ADR versienummers of publicatie-URLs. Het is een GitHub repo-pagina van het beheermodel, niet de hoofdspecificatie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel)
  - *De bron vermeldt de NLGov REST API Design Rules als onderdeel van de API standaarden, maar noemt geen versienummer (v2.1.0) of publicatie-URL. Versie-metadata staat zelden in een beheermodel-README.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial)
  - *De brontekst bevat geen informatie over ADR v2.1.0 of de hoofdspecificatie. De bron gaat uitsluitend over de geospatial module.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-geospatial](https://logius-standaarden.github.io/API-mod-geospatial)
  - *De brontekst vermeldt de ADR hoofdspecificatie alleen als verwijzing in de tabel (normative, 'API Design Rules (ADR v2.0)'), maar bevat geen informatie over versie 2.1.0 of de bijbehorende publicatie-URL.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De brontekst is de README van de Transport Security module repository en bevat geen informatie over ADR v2.1.0 of de publicatie-URL.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-signing](https://github.com/logius-standaarden/API-mod-signing)
  - *De bron vermeldt geen versienummers van de ADR hoofdspecificatie. Er wordt alleen gelinkt naar 'Formele standaard', 'Gepubliceerde versie' en 'Werkversie' zonder specifieke versienummers.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-signing](https://logius-standaarden.github.io/API-mod-signing)
  - *De bron beschrijft de ADR Signing module (draft), niet de hoofdspecificatie ADR v2.1.0. Versienummers of publicatie-URLs van de hoofdspecificatie komen niet voor.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-encryption](https://github.com/logius-standaarden/API-mod-encryption)
  - *De brontekst vermeldt de ADR hoofdspecificatie wel als link ('NLGov API Design Rules (ADR)') maar geeft geen versienummer of publicatiedatum. De claim over v2.1.0 kan niet worden bevestigd of ontkracht.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-encryption](https://logius-standaarden.github.io/API-mod-encryption)
  - *De bron is de API-mod-encryption specificatie en bevat geen informatie over de ADR hoofdspecificatie of versienummers daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/api-linter-impactanalyse](https://github.com/logius-standaarden/api-linter-impactanalyse)
  - *De brontekst bevat geen informatie over ADR versies, publicaties of de URL gitdocumentatie.logius.nl. De repository gaat uitsluitend over een impactanalyse-tool voor de spectral linter.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/zaakgericht-werken-api](https://github.com/logius-standaarden/zaakgericht-werken-api)
  - *De brontekst bevat geen informatie over ADR v2.1.0 of publicatie-URLs. De bron gaat over een ReSpec template repository voor zaakgericht-werken-api.*
</details>

### `ls-api-0009` — SKILL.md:44 *(§ Repositories)*

> Geospatial module v1.0.3 is vastgesteld en gepubliceerd op https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Geospatial module

**Erkend in conflicts.md** *(§ Details API-mod-geospatial)*: conflicts.md § 'Details API-mod-geospatial': 'De tag 1.0.2 bestaat op GitHub, maar de gepubliceerde versie op gitdocumentatie is 1.0.3. Er is geen tag 1.0.3 in de repository.' CONTRADICTED-verdict op GitHub Pages (draft toont 1.0.2) is gedocumenteerde discrepantie; gitdocumentatie.logius.nl is leidend.

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > API Design Rules Module: Geospatial 1.0.3 Logius Guide Definitive version May 22, 2025 This version: https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3/
- **CONTRADICTED** (medium) — [https://logius-standaarden.github.io/API-mod-geospatial](https://logius-standaarden.github.io/API-mod-geospatial)
  > Previous version: https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.1/
  - *De bron noemt versie 1.0.1 als de vorige versie en het huidige document is een draft (geen vastgestelde versie). Versie 1.0.3 wordt nergens vermeld. De claim dat 1.0.3 vastgesteld is, wordt tegengesproken doordat de bron de huidige versie als draft aanduidt en de meest recente gepubliceerde versie 1.0.1 was. Echter: de bron vermeldt 1.0.3 expliciet niet, dus dit is ook deels NOT_FOUND; CONTRADICTED omdat de draft-status en de genoemde vorige versie 1.0.1 de claim van een vastgestelde 1.0.3 ondermijnen.*
<details><summary>15x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron noemt de Geospatial module maar niet het specifieke versienummer 1.0.3 of de specifieke publicatie-URL.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Geospatial module v1.0.3 en de bijbehorende publicatie-URL worden niet vermeld in deze bron.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules)
  - *De brontekst bevat geen informatie over een Geospatial module of versie v1.0.3.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules)
  - *De bron verwijst naar de Geospatial module via '[ADR-GEO] API Design Rules Module: Geospatial . ... March 07, 2024. URL: https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/' maar noemt geen specifiek versienummer 1.0.3.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel)
  - *De bron bevat geen informatie over de Geospatial module of versienummers daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel)
  - *De bron noemt geen Geospatial module, geen versienummer v1.0.3 en geen publicatie-URL. De normatieve modules van het Kennisplatform API's worden wel kort aangehaald maar zonder detail.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Standaarden-Beheermodel](https://logius-standaarden.github.io/API-Standaarden-Beheermodel)
  - *De bron vermeldt geen Geospatial module, versienummer v1.0.3 of de bijbehorende publicatie-URL.*
- **NOT_FOUND** (medium) — [https://github.com/logius-standaarden/API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial)
  - *De brontekst vermeldt wel de publicatieversie-URL (https://gitdocumentatie.logius.nl/publicatie/api/mod-geo) en werkversie-URL, maar noemt geen specifiek versienummer zoals v1.0.3. Het versiebeheer of de vastgestelde versie wordt niet vermeld.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De brontekst bevat geen informatie over een Geospatial module.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-signing](https://github.com/logius-standaarden/API-mod-signing)
  - *De bron behandelt de Signing module, niet de Geospatial module. Er is geen informatie over mod-geo v1.0.3.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-signing](https://logius-standaarden.github.io/API-mod-signing)
  - *De bron noemt de GEO module v1.0 in de tabel van de Nederlandse API Strategie, maar geeft geen versienummer 1.0.3 of publicatie-URL voor die module.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-encryption](https://github.com/logius-standaarden/API-mod-encryption)
  - *De brontekst bevat geen informatie over de Geospatial module of enig versienummer daarvan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-encryption](https://logius-standaarden.github.io/API-mod-encryption)
  - *De bron vermeldt in de abstracttabel wel 'GEO module v1.0' als onderdeel van de Nederlandse API Strategie, maar geeft geen informatie over versie 1.0.3 of de publicatie-URL daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/api-linter-impactanalyse](https://github.com/logius-standaarden/api-linter-impactanalyse)
  - *De brontekst bevat geen informatie over de Geospatial module of enige versie daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/zaakgericht-werken-api](https://github.com/logius-standaarden/zaakgericht-werken-api)
  - *De brontekst bevat geen informatie over een Geospatial module of versienummers daarvan.*
</details>

## GROUNDED — minstens één bron ondersteunt de claim (31)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-api-0001` — SKILL.md:26 *(§ API Design Rules (NL GOV))*

> De API Design Rules zijn verplicht onder het 'pas-toe-of-leg-uit' regime van het Forum Standaardisatie.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** API Design Rules (ADR) — NL GOV

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > This version of the design rules has been submitted to Forum Standaardisatie for inclusion on the Comply or Explain list of mandatory standards in the Dutch Public Sector.
  - *De bron zegt dat de standaard is ingediend ('submitted') voor opname op de lijst, niet dat het al verplicht is onder het pas-toe-of-leg-uit regime. De claim stelt het als vaststaand feit.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  > De status van de ADR-standaard is 'Verplicht (pas toe leg uit)'. Dit houdt kort gezegd in dat Nederlandse overheden en instellingen uit de (semi) publieke sector verplicht zijn deze standaard toe te passen op het moment dat zij REST API's gaan gebruiken voor het ontsluiten van overheidsinformatie en/of functionaliteit.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron gaat over de Geospatial module van de ADR en vermeldt niets over het 'pas-toe-of-leg-uit' regime van het Forum Standaardisatie.*

### `ls-api-0002` — SKILL.md:32 *(§ Versiemodel)*

> De vastgestelde versie (DEF) van de ADR is gepubliceerd op `gitdocumentatie.logius.nl`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — versiemodel

- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > This version: https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3/ ... This is the definitive version of this document.
  - *De bron bevestigt dat vastgestelde (definitieve) versies op gitdocumentatie.logius.nl worden gepubliceerd, maar specifiek voor de Geospatial module, niet de ADR-hoofdspecificatie. De claim is algemeen over de ADR.*

### `ls-api-0003` — SKILL.md:33 *(§ Versiemodel)*

> De werkversie (draft) van de ADR is gepubliceerd op `logius-standaarden.github.io`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — versiemodel

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Latest editor's draft: https://logius-standaarden.github.io/API-Design-Rules/
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  > De laatste concept versie van de standard is gepubliceerd op: https://logius-standaarden.github.io/API-Design-Rules/
- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > Latest editor's draft: https://logius-standaarden.github.io/API-mod-geospatial/
  - *Bevestigd voor de Geospatial module; de claim is algemeen over de ADR-werkversie, maar het patroon klopt.*

### `ls-api-0006` — SKILL.md:35 *(§ Versiemodel)*

> Transport Security is in ADR v2.1.0 ingebed als sectie 3.8 met eigen regels (`/core/transport/*`).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR v2.1.0 — Transport Security

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > 3.8 Transport Security [...] technical /core/transport/tls [...] technical /core/transport/security-headers [...] technical /core/transport/cors

### `ls-api-0007` — SKILL.md:45 *(§ Repositories)*

> De API-mod-transport-security GitHub-repository is gearchiveerd.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Transport Security module

- **SUPPORTED** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  > This repository was archived by the owner on Aug 29, 2025. It is now read-only.
<details><summary>16x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron vermeldt niets over archivering van de API-mod-transport-security GitHub-repository.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron vermeldt de API-mod-transport-security repository of archivering daarvan niet.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron vermeldt de Transport Security module of de bijbehorende repository niet.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules)
  - *De brontekst bevat geen informatie over een API-mod-transport-security repository of de archiefstatus ervan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules)
  - *De brontekst vermeldt de Transport Security module als normatief onderdeel en verwijst naar een apart document, maar bevat geen informatie over de archiefstatus van de GitHub-repository.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel)
  - *De bron gaat over het ADR-Beheermodel repository, niet over de API-mod-transport-security repository. Geen informatie over archivering van die specifieke repo.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel)
  - *De brontekst is de README/overzichtspagina van het API-Standaarden-Beheermodel repository. Er wordt geen melding gemaakt van de API-mod-transport-security GitHub-repository of de archiefstatus ervan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Standaarden-Beheermodel](https://logius-standaarden.github.io/API-Standaarden-Beheermodel)
  - *De bron vermeldt geen GitHub-repository voor een Transport Security module, noch informatie over archivering daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial)
  - *De brontekst gaat over de API-mod-geospatial repository, niet over API-mod-transport-security. Geen informatie over archivering van transport-security repo.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-geospatial](https://logius-standaarden.github.io/API-mod-geospatial)
  - *De brontekst gaat over de Geospatial module en vermeldt niets over een Transport Security module of de status van een bijbehorende GitHub-repository.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-signing](https://github.com/logius-standaarden/API-mod-signing)
  - *De bron gaat over de API-mod-signing repository, niet over API-mod-transport-security. Er is geen informatie over archivering van transport-security.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-signing](https://logius-standaarden.github.io/API-mod-signing)
  - *De bron gaat over de API-mod-signing specificatie en maakt geen melding van een transport-security repository of de archiveringsstatus daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-encryption](https://github.com/logius-standaarden/API-mod-encryption)
  - *De brontekst gaat over de API-mod-encryption repository, niet over de API-mod-transport-security repository. Er is geen informatie over archivering van transport-security.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-encryption](https://logius-standaarden.github.io/API-mod-encryption)
  - *De bron behandelt alleen de Encryption module (JWE). Er is geen informatie over de Transport Security module of de archiefstatus van een gerelateerde GitHub-repository.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/api-linter-impactanalyse](https://github.com/logius-standaarden/api-linter-impactanalyse)
  - *De brontekst gaat over de api-linter-impactanalyse repository en bevat geen informatie over de API-mod-transport-security GitHub-repository of de archiefstatus daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/zaakgericht-werken-api](https://github.com/logius-standaarden/zaakgericht-werken-api)
  - *De brontekst gaat over de zaakgericht-werken-api repository (een ReSpec template). Er is geen informatie over de API-mod-transport-security repository of archiveringsstatus daarvan.*
</details>

### `ls-api-0010` — SKILL.md:42 *(§ Repositories)*

> ADR-Beheermodel v1.0 is gearchiveerd en vervangen door het API-Standaarden-Beheermodel.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — beheermodel

- **SUPPORTED** (high) — [https://github.com/logius-standaarden/ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel)
  > Dit beheermodel is verouderd en vervangen door het algemene API Standaarden beheermodel
  - *De bron bevestigt expliciet dat het ADR-Beheermodel vervangen is door het API Standaarden beheermodel. De archivering wordt ook bevestigd: 'This repository was archived by the owner on Jul 15, 2025. It is now read-only.' De versieaanduiding 'v1.0' staat niet letterlijk in de brontekst, maar de releases sectie toont '1.0 (rerelease) Latest Jan 7, 2022', wat v1.0 ondersteunt.*
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/logius-standaarden/API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel)
  > "Generiek beheermodel voor de verzameling van API standaarden" en "Generated from Logius-standaarden/Logius-Beheermodel"
  - *De bron bevestigt dat het API-Standaarden-Beheermodel bestaat als opvolger/generiek kader, gegenereerd vanuit het Logius-Beheermodel. Dat impliceert dat er een voorganger was, maar de bron benoemt het ADR-Beheermodel v1.0 noch de archiefstatus ervan expliciet. PARTIALLY_SUPPORTED omdat de vervanging indirect blijkt maar de archiefstatus en versieaanduiding ontbreken.*
- **SUPPORTED** (high) — [https://logius-standaarden.github.io/API-Standaarden-Beheermodel](https://logius-standaarden.github.io/API-Standaarden-Beheermodel)
  > Met het indienen van versie 2.0 van de ADR standaard zijn tevens de beheermodelen van ADR en OAuth (die hadden een apart beheermodel) samengevoegd met dit beheermodel. Ook deze samenvoeging is goedgekeurd en de kopieën zijn daarom nu gearchiveerd.
  - *De bron bevestigt expliciet dat het aparte ADR-beheermodel is samengevoegd met het API-Standaarden-Beheermodel en gearchiveerd. De claim over 'v1.0' als specifiek versienummer wordt niet vermeld, maar dat is een klein detail dat de kern van de claim niet weerspreekt.*
<details><summary>14x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  - *De bron vermeldt niets over het ADR-Beheermodel v1.0 of archivering ervan.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron is het beheermodel zelf en vermeldt niets over archivering of vervanging ervan door een API-Standaarden-Beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron vermeldt het ADR-Beheermodel of het API-Standaarden-Beheermodel niet.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules)
  - *De brontekst vermeldt wel een beheermodel-URL (https://gitdocumentatie.logius.nl/publicatie/api/beheermodel/) maar zegt niets over archiefstatus van ADR-Beheermodel v1.0 of vervanging door een API-Standaarden-Beheermodel.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-Design-Rules](https://logius-standaarden.github.io/API-Design-Rules)
  - *De bron vermeldt dat het beheermodel van de standaard wordt beschreven door 'het API-Standaarden beheermodel gepubliceerd door Logius', maar bevat geen informatie over archivering van een ADR-Beheermodel v1.0 of vervanging ervan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial)
  - *De brontekst bevat geen informatie over het ADR-Beheermodel of het API-Standaarden-Beheermodel.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-geospatial](https://logius-standaarden.github.io/API-mod-geospatial)
  - *De brontekst bevat geen informatie over het ADR-Beheermodel of een vervangend API-Standaarden-Beheermodel.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security)
  - *De brontekst bevat geen informatie over het ADR-Beheermodel.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-signing](https://github.com/logius-standaarden/API-mod-signing)
  - *De bron vermeldt wel het beheermodel via de URL https://gitdocumentatie.logius.nl/publicatie/api/beheermodel/, maar geeft geen informatie over archivering van ADR-Beheermodel v1.0 of vervanging door een API-Standaarden-Beheermodel.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-signing](https://logius-standaarden.github.io/API-mod-signing)
  - *Het ADR-Beheermodel of de archiveringsstatus daarvan wordt in deze bron niet besproken.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/API-mod-encryption](https://github.com/logius-standaarden/API-mod-encryption)
  - *De brontekst verwijst naar het beheermodel via een URL ('https://gitdocumentatie.logius.nl/publicatie/api/beheermodel/') maar zegt niets over archivering van ADR-Beheermodel v1.0 of een opvolger.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/API-mod-encryption](https://logius-standaarden.github.io/API-mod-encryption)
  - *De bron bevat geen informatie over het ADR-Beheermodel of een opvolger daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/api-linter-impactanalyse](https://github.com/logius-standaarden/api-linter-impactanalyse)
  - *De brontekst bevat geen informatie over het ADR-Beheermodel of het API-Standaarden-Beheermodel.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/zaakgericht-werken-api](https://github.com/logius-standaarden/zaakgericht-werken-api)
  - *De brontekst bevat geen informatie over het ADR-Beheermodel of een API-Standaarden-Beheermodel.*
</details>

### `ls-api-0013` — SKILL.md:57 *(§ URI-ontwerp)*

> URIs mogen geen trailing slashes bevatten: `/api/v1/users` (niet `/api/v1/users/`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** ADR — URI-ontwerp

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > technical /core/no-trailing-slash : Leave off trailing slashes from URIs — A URI MUST never contain a trailing slash. When requesting a resource including a trailing slash, this MUST result in a 404 (not found) error response and not a redirect.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen regels over trailing slashes in URIs.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over trailing slashes in URIs.*

### `ls-api-0015` — SKILL.md:59 *(§ URI-ontwerp)*

> De major versie MOET in de URI staan (`/v1/resources`); in de OAS moet dit op serverniveau worden gespecificeerd, niet in individuele paden.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — URI-ontwerp en versiebeheer

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > technical /core/uri-version : Include the major version number in the URI — The URI of an API (base path) MUST include the major version number, prefixed by the letter v [...] An example of an openapi.yaml for an API with a base path https://api.example.org/v1 [...] servers: - description: test environment url: https://api.test.example.org/v1
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen technische regels over versiebeheer in URIs of OAS-serverniveau specificatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over het opnemen van de major versie in de URI of OAS-configuratie op serverniveau.*

### `ls-api-0016` — SKILL.md:60 *(§ URI-ontwerp)*

> Operaties als sub-resources: het laatste padsegment mag starten met `_` (bijv. `/_search`).

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** ADR — URI-ontwerp

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > In exceptional cases [...] Use the imperative mood of a verb, maybe even prefix it with a underscore to distinguish these resources from regular resources. For example: /search or /_search .
- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > In case of a global query /api/v1/_search , results should be placed in the relevant geometric context
  - *De bron gebruikt het patroon `/_search` als voorbeeld en de bijbehorende regel /geo/geometric-context, wat consistent is met de claim dat het laatste padsegment mag starten met `_`.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen regels over operaties als sub-resources of het gebruik van `_` als prefix.*

### `ls-api-0017` — SKILL.md:61 *(§ URI-ontwerp)*

> Gevoelige informatie MAG NIET in URIs worden opgenomen omdat URIs niet door TLS beschermd zijn.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** ADR — URI-ontwerp

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > functional /core/transport/no-sensitive-uris : No sensitive information in URIs — Even when using TLS connections, information in URIs is not secured. URIs can be cached and logged outside of the servers controlled by clients and servers. [...] MUST NOT contain any sensitive information.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen regels over gevoelige informatie in URIs en TLS-bescherming.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over het opnemen van gevoelige informatie in URIs of TLS-bescherming.*

### `ls-api-0018` — SKILL.md:67 *(§ HTTP-methoden)*

> De GET-methode is veilig en idempotent en mag de resource nooit wijzigen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** ADR — HTTP-methoden

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Method Safe Idempotent GET Yes Yes [...] Request methods are considered safe if their defined semantics are essentially read-only; i.e., the client does not request, and does not expect, any state change on the origin server as a result of applying a safe method to a target resource.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen technische regels over HTTP-methoden zoals GET.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen expliciete regels over de veiligheid of idempotentie van de GET-methode.*

### `ls-api-0019` — SKILL.md:69 *(§ HTTP-methoden)*

> De PUT-methode is idempotent en wordt gebruikt voor het aanmaken of volledig vervangen van een resource.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — HTTP-methoden

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > PUT Create/update Create a resource with the given URI or replace (full update) a resource when the resource already exists. [...] Method Safe Idempotent [...] PUT No Yes
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen technische regels over de PUT-methode.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over de PUT-methode.*

### `ls-api-0020` — SKILL.md:75 *(§ Versiebeheer)*

> De major versie MOET in het URI-pad staan: `/v1`, `/v2`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — versiebeheer

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > technical /core/uri-version : Include the major version number in the URI — The URI of an API (base path) MUST include the major version number, prefixed by the letter v .
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen technische versiebeheerregels over major versie in het URI-pad.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen expliciete regel dat de major versie in het URI-pad moet staan.*

### `ls-api-0021` — SKILL.md:76 *(§ Versiebeheer)*

> De volledige versie MOET in de `API-Version` response header worden opgenomen: `1.2.3`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — versiebeheer

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > technical /core/version-header : Return the full version number in a response header — The version number MUST be returned in an HTTP response header named API-Version (case-insensitive) [...] An example of an API version response header: API-Version: 1.0.2
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron vermeldt de `API-Version` response header niet.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over de `API-Version` response header.*

### `ls-api-0022` — SKILL.md:77 *(§ Versiebeheer)*

> Semantic versioning (major.minor.patch) MOET worden gebruikt in `info.version`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — versiebeheer

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > technical /core/semver : Adhere to the Semantic Versioning model when releasing API changes — Version numbering MUST follow the Semantic Versioning [SemVer] model [...] Release versions are formatted using the major.minor.patch template
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron vermeldt semantic versioning in `info.version` niet.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over semantic versioning of `info.version`.*

### `ls-api-0024` — SKILL.md:79 *(§ Versiebeheer)*

> Er MOET een vaste transitieperiode tussen major versies worden gehanteerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — versiebeheer

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > functional /core/transition-period : Schedule a fixed transition period for a new major API version — When releasing a new major API version, the old version MUST remain available for a limited and fixed deprecation period.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen regels over een transitieperiode tussen major versies.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over transitieperiodes tussen major versies.*

### `ls-api-0026` — SKILL.md:95 *(§ Foutafhandeling)*

> Foutmeldingen MOGEN GEEN technische details bevatten zoals stack traces of interne hints.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** ADR — foutafhandeling

- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > In case of an error, the server SHOULD NOT pass technical details (e.g. call stacks or other internal hints) to the client. The error message SHOULD be generic to avoid revealing additional details and expose internal information which can be used with malicious intent.
  - *De bron gebruikt SHOULD NOT, niet MUST NOT. De claim gebruikt MOGEN NIET (MUST NOT). Dit is een potentieel verschil in normatieve sterkte, maar de strekking is gelijk en de bron ondersteunt de claim in de geest.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De bron bevat geen regels over de inhoud van foutmeldingen of het weglaten van technische details.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron bevat geen regels over foutmeldingen of het uitsluiten van technische details daarin.*

### `ls-api-0027` — SKILL.md:99 *(§ Datum en tijd)*

> Datum/tijd waarden MOETEN RFC 3339 formaat gebruiken.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — datum en tijd

- **SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc3339.txt](https://www.rfc-editor.org/rfc/rfc3339.txt)
  > The following profile of ISO 8601 [ISO8601] dates SHOULD be used in new protocols on the Internet. [...] date-time = full-date "T" full-time
  - *RFC 3339 definieert het formaat dat de claim beschrijft. De bron zegt echter SHOULD (aanbevolen) voor gebruik in nieuwe protocollen, niet MUST. De claim stelt MOETEN (MUST). De bron definieert het RFC 3339 formaat zelf volledig, maar legt het gebruik als SHOULD op, niet MUST. Toch is de claim dat datum/tijd waarden RFC 3339 formaat MOETEN gebruiken plausibel als een API-standaard RFC 3339 als verplicht aanwijst — de bron bevestigt het formaat zelf volledig. Omdat de claim gaat over een ADR-regel die RFC 3339 verplicht stelt (niet over RFC 3339 zelf die dat verplicht stelt), en de bron het formaat volledig beschrijft, is SUPPORTED hier de juiste keuze: de bron definieert het formaat waaraan voldaan moet worden.*

### `ls-api-0032` — SKILL.md:107 *(§ Naamgeving)*

> Resources MOETEN als zelfstandige naamwoorden worden benoemd (niet werkwoorden).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — naamgeving

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Resources are referred to using nouns (instead of verbs) that represent entities meaningful to the API consumer.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Naamgevingsregels voor resources zijn geen onderdeel van dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Naamgevingsregels voor resources (zelfstandige naamwoorden vs. werkwoorden) komen niet voor in deze bron.*

### `ls-api-0037` — SKILL.md:115 *(§ OpenAPI Documentatie)*

> Een OpenAPI 3.0+ specificatie is VERPLICHT.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — OpenAPI documentatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > API documentation MUST be provided in the form of an OpenAPI definition document which conforms to the OpenAPI Specification (from v3 onwards).
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De verplichting van een OpenAPI 3.0+ specificatie staat niet in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *OpenAPI 3.0+ verplichting wordt niet behandeld in deze Geospatial module bron.*

### `ls-api-0038` — SKILL.md:116 *(§ OpenAPI Documentatie)*

> De OpenAPI JSON-spec MOET gepubliceerd worden op standaardlocatie `/openapi.json` (VERPLICHT); YAML op `/openapi.yaml` is OPTIONEEL.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — OpenAPI documentatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > The standard location for the OAS document is a URI called openapi.json or openapi.yaml within the base path of the API. [...] At least the JSON format MUST be supported. [...] the same OAS document MAY be provided in YAML format: https://api.example.org/v1/openapi.yaml
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Publicatielocaties voor OpenAPI-specificaties worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Publicatielocatie van OpenAPI specificatie wordt niet behandeld in deze bron.*

### `ls-api-0039` — SKILL.md:117 *(§ OpenAPI Documentatie)*

> Contactinformatie (`info.contact` met `name`, `email`, `url`) wordt sterk aanbevolen voor publieke APIs (ADR `/core/doc-openapi-contact`: SHOULD).

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** ADR — OpenAPI documentatie, publieke APIs

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > OpenAPI definition document SHOULD include the info.contact object for publicly available APIs. Contact information SHOULD NOT be a generic contact address for the whole organisation. [...] { "name": "Gebouwen API beheerder", "url": "...", "email": "teamgebouwen@ministerie.nl" }
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Aanbevelingen voor contactinformatie in OpenAPI-specs worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Contactinformatie in OpenAPI (info.contact) wordt niet behandeld in deze bron.*

### `ls-api-0040` — SKILL.md:117 *(§ OpenAPI Documentatie)*

> De Spectral linter dwingt contactinformatie-velden af als error voor publieke APIs.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter, OpenAPI documentatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > #/core/doc-openapi-contact # This rule exists in the base oas spectral linter set info-contact: error info-contact-fields-exist: severity: error given: - "$.info.contact" then: function: schema functionOptions: schema: required: - email - name - url
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Spectral linter-gedrag voor contactinformatie wordt niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Spectral linter afdwinging van contactinformatie-velden wordt niet behandeld in deze bron.*

### `ls-api-0041` — SKILL.md:118 *(§ OpenAPI Documentatie)*

> CORS MOET ondersteund worden voor documentatie-toegang.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ADR — OpenAPI documentatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > Clients (such as Swagger UI or ReDoc) MUST be able to retrieve the document without having to authenticate. Furthermore, the CORS policy for this URI MUST allow external domains to read the documentation from a browser environment.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *CORS-vereisten worden niet behandeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *CORS-vereisten voor documentatietoegang worden niet behandeld in deze bron.*

### `ls-api-0051` — SKILL.md:142 *(§ Geospatial Module (v1.0.3 — vastgesteld))*

> De Geospatial module regelt GeoJSON encodering, bounding box filtering en coördinaatsystemen (CRS).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Geospatial module

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  > The Geospatial Module provides rules for the structuring of geospatial payloads and for functions in APIs to handle geospatial data. [...] how to encode geometries in APIs how to supply a spatial filter in the call (request) how to return results of a spatial search
  - *De bron bevestigt dat de Geospatial module GeoJSON encodering, bounding box filtering (bbox query parameter) en coördinaatsystemen (CRS, heel hoofdstuk 3) regelt.*

### `ls-api-0059` — SKILL.md:241 *(§ Spectral Linter)*

> De publieke DON-hosted ruleset is beschikbaar op `https://static.developer.overheid.nl/adr/ruleset.yaml`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > curl -L https://static.developer.overheid.nl/adr/ruleset.yaml > .spectral.yml
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De URL van de DON-hosted Spectral ruleset wordt niet vermeld in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De DON-hosted Spectral ruleset URL wordt niet vermeld in deze bron.*

### `ls-api-0060` — SKILL.md:257 *(§ Spectral Linter)*

> Spectral regel `include-major-version-in-uri` / `nlgov:include-major-version-in-uri` controleert de aanwezigheid van de major versie in de server URL.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter, URI-ontwerp

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > #/core/uri-version include-major-version-in-uri: severity: error given: - "$.servers[*]" then: function: pattern functionOptions: match: "\/v[\d+]" field: url message: "/core/uri-version: Include the major version number in the URI"
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Specifieke Spectral-regelnamen worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Spectral regel include-major-version-in-uri wordt niet behandeld in deze bron.*

### `ls-api-0061` — SKILL.md:258 *(§ Spectral Linter)*

> Spectral regel `paths-no-trailing-slash` / `nlgov:paths-no-trailing-slash` controleert dat paden geen trailing slashes hebben.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > #/core/no-trailing-slash paths-no-trailing-slash: severity: error given: - "$.paths" then: function: pattern functionOptions: notMatch: ".+ \/$" field: "@key" message: "/core/no-trailing-slash: Leave off trailing slashes from URIs"
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Specifieke Spectral-regelnamen worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Spectral regel paths-no-trailing-slash wordt niet behandeld in deze bron.*

### `ls-api-0062` — SKILL.md:259 *(§ Spectral Linter)*

> Spectral regel `paths-kebab-case` / `nlgov:paths-kebab-case` controleert dat padsegmenten kebab-case gebruiken.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > paths-kebab-case: severity: warn message: " {{property}} is not kebab-case." given: $.paths[?(@property && !@property.match(/ \/openapi\.json/))]~
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Specifieke Spectral-regelnamen worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *Spectral regel paths-kebab-case wordt niet behandeld in deze bron.*

### `ls-api-0063` — SKILL.md:261 *(§ Spectral Linter)*

> Spectral regel `missing-version-header` / `nlgov:missing-version-header` controleert de aanwezigheid van de version header in 2xx/3xx responses.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > #/core/version-header missing-version-header: severity: error given: $..[responses][?(@property && @property.match(/(2|3)\d\d/))][headers] then: function: or functionOptions: properties: - API-Version - Api-Version - Api-version - api-version - API-version message: "Return the full version number in a response header"
  - *De regel heet `missing-version-header` (zonder `nlgov:`-prefix) en controleert 2xx/3xx responses op aanwezigheid van de version header.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *Specifieke Spectral-regelnamen worden niet beschreven in dit beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron beschrijft de API Design Rules Module Geospatial. Er is geen vermelding van Spectral linter regels of `missing-version-header` in de brontekst.*

### `ls-api-0064` — SKILL.md:262 *(§ Spectral Linter)*

> Spectral regel `use-problem-schema` / `nlgov:use-problem-schema` controleert het gebruik van problem+json voor foutresponses.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ADR — Spectral linter

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0)
  > use-problem-schema: severity: warn message: "The content type of an error response should be application/problem+json or application/problem+xml to match RFC 9457." given: $..[responses][?(@property && @property.match(/(4|5)\d\d/))].content then: function: schema functionOptions: schema: anyOf: - required: [ "application/problem+json" ] - required: [ "application/problem+xml" ]
  - *De regel heet `use-problem-schema` (zonder `nlgov:`-prefix) in de gepubliceerde versie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0)
  - *De brontekst gaat over het beheermodel van de ADR-standaard. Er is geen vermelding van Spectral, linters, of specifieke regels zoals `use-problem-schema`.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3)
  - *De bron beschrijft de API Design Rules Module Geospatial. Er is geen vermelding van Spectral linter regels of `use-problem-schema` in de brontekst.*

</details>
