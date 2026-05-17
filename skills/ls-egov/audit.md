<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit ls-egov — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 3 | 8% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 0 | 0% |
| UNGROUNDED | 1 | 3% |
| NO_SOURCE | 31 | 86% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 1 | 3% |

*Geverifieerd met sonnet, 2 calls, $0.1270.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (3)

### `ls-egov-0019` — SKILL.md:115 *(§ Samenhang Standaarden)*

> NLCIUS heeft de Forum Standaardisatie status 'verplicht' (pas-toe-of-leg-uit).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NLCIUS - Forum Standaardisatie

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis](https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis)
  - *De bron gaat over Peppol BIS, niet over NLCIUS. De status van NLCIUS staat niet in deze bron. NLCIUS wordt wel genoemd als gerelateerde standaard, maar zonder statusaanduiding.*

### `ls-egov-0021` — SKILL.md:107 *(§ Samenhang Standaarden)*

> De Basisfactuur Rijk is gebaseerd op Peppol BIS Billing 3.0, NLCIUS (NL-specifieke invulling EN 16931) en UBL-OHNL.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisfactuur Rijk - samenhang standaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis](https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis)
  - *De bron behandelt Peppol BIS als standaard in het algemeen. De Basisfactuur Rijk en de specifieke samenstelling daarvan (Peppol BIS Billing 3.0, NLCIUS, UBL-OHNL) worden niet in deze bron beschreven.*

### `ls-egov-0022` — SKILL.md:111 *(§ Samenhang Standaarden)*

> De Basisorder Rijk is gebaseerd op Peppol BIS Order 3.0 en UBL 2.1 Order.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisorder Rijk - samenhang standaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis](https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis)
  - *De Basisorder Rijk en de specifieke grondslag daarvan worden niet in deze bron behandeld.*

## UNGROUNDED — geen bron ondersteunt de claim (1)

### `ls-egov-0023` — SKILL.md:232 *(§ Foutafhandeling)*

> De Terugmelden-API gebruikt application/problem+json conform RFC 9457 voor foutresponses.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Terugmelden-API - foutafhandeling

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc9457.txt](https://www.rfc-editor.org/rfc/rfc9457.txt)
  - *De bron is RFC 9457 (Problem Details for HTTP APIs), een generieke IETF-specificatie. De Terugmelden-API wordt nergens in deze bron genoemd. De bron beschrijft wát application/problem+json is en hoe het werkt, maar kan niet bevestigen of ontkennen dat de Terugmelden-API dit formaat gebruikt.*

## NO_SOURCE — geen kandidaat-bron gevonden (31)

### `ls-egov-0001` — SKILL.md:34 *(§ Versiemodel)*

> De E-Government standaarden hebben momenteel alleen werkversies. Er zijn nog geen vastgestelde versies gepubliceerd.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** E-Government standaarden (Logius) versiemodel


### `ls-egov-0002` — SKILL.md:31 *(§ Versiemodel)*

> Vastgestelde versies (DEF) worden gepubliceerd op gitdocumentatie.logius.nl; werkversies (draft) worden gepubliceerd op logius-standaarden.github.io.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius standaarden publicatiekanalen


### `ls-egov-0003` — SKILL.md:51 *(§ Terugmelden-API (in ontwikkeling))*

> De Terugmelden-API is een beoogde REST API voor het indienen en opvragen van terugmeldingen; de repository bevat nog geen uitgewerkte specificatie en de API is in conceptfase.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Terugmelden-API


### `ls-egov-0004` — SKILL.md:51 *(§ Terugmelden-API (in ontwikkeling))*

> De bestaande koppelvlakspecificatie voor terugmelden is de Digimelding-Koppelvlakspecificatie (SOAP/WUS).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding / Terugmelden


### `ls-egov-0005` — SKILL.md:59 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Facturen aan de Rijksoverheid die de verplichte velden missen worden automatisch afgewezen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk


### `ls-egov-0006` — SKILL.md:63 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet een uniek factuurnummer bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Factuuridentificatie


### `ls-egov-0007` — SKILL.md:64 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet een factuurdatum bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Factuuridentificatie


### `ls-egov-0008` — SKILL.md:65 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet een factuurtypeaanduiding (factuur, creditnota, etc.) bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Factuuridentificatie


### `ls-egov-0009` — SKILL.md:66 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet een valutacode bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Factuuridentificatie


### `ls-egov-0010` — SKILL.md:70 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet naam en adresgegevens van de leverancier bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Leverancieridentificatie


### `ls-egov-0011` — SKILL.md:71 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet een KvK-nummer of vergelijkbaar identificatienummer van de leverancier bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Leverancieridentificatie


### `ls-egov-0012` — SKILL.md:72 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet een BTW-identificatienummer van de leverancier bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Leverancieridentificatie


### `ls-egov-0013` — SKILL.md:73 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet bankgegevens (IBAN en eventueel BIC) van de leverancier bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Leverancieridentificatie


### `ls-egov-0014` — SKILL.md:76 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet het OIN (Overheids Identificatie Nummer) of vergelijkbaar identificatienummer van de ontvangende organisatie bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Ontvanger


### `ls-egov-0015` — SKILL.md:80 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet per regelitem een omschrijving van het geleverde product of dienst, hoeveelheid en eenheid, prijs per eenheid, totaalbedrag per regel, BTW-percentage en BTW-bedrag bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Regelitems


### `ls-egov-0016` — SKILL.md:87 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een basisfactuur Rijk moet een ordernummer (inkoopordernummer van de overheidsorganisatie) bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Order- en referentie-informatie


### `ls-egov-0017` — SKILL.md:97 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Bijlagen bij de basisfactuur Rijk zijn gemaximeerd op 9 bijlagen per factuur.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Basisfactuur Rijk - Bijlagen


### `ls-egov-0018` — SKILL.md:98 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> De totale grootte van alle bijlagen bij de basisfactuur Rijk mag niet groter zijn dan 20 MB.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Basisfactuur Rijk - Bijlagen


### `ls-egov-0024` — SKILL.md:262 *(§ Foutafhandeling)*

> Bij afwijzing van een basisfactuur ontvangt de leverancier een e-mail met de specifieke ontbrekende velden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisfactuur Rijk - foutafhandeling


### `ls-egov-0025` — SKILL.md:275 *(§ Basisfactuur Validatie (Schematron))*

> Het repo basisfactuur-rijk bevat een Schematron bestand met validatieregels en voorbeeld-XML's.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisfactuur Rijk - validatie


### `ls-egov-0026` — reference.md:23 *(§ Terugmelding & Digimelding)*

> Digimelding is de centrale voorziening waarmee terugmeldingen op basisregistraties worden ingediend en afgehandeld, en fungeert als koppelpunt tussen melder en bronhouder.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding


### `ls-egov-0027` — reference.md:29 *(§ Technische Architectuur: Annotatie-framework)*

> De berichtenarchitectuur van Digimelding is gebaseerd op een annotatie-framework dat terugmeldingen structureert als hiërarchische annotaties.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding - technische architectuur


### `ls-egov-0028` — reference.md:42 *(§ Technische Architectuur: Annotatie-framework)*

> Elke leaf-annotatie in het Digimelding annotatie-framework refereert terug naar het UUID van de root-annotatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding - annotatie-framework


### `ls-egov-0029` — reference.md:90 *(§ E-Procurement)*

> Elektronisch factureren (e-invoicing) is verplicht voor leveranciers aan de Rijksoverheid conform EU-richtlijn 2014/55/EU.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** E-Procurement - e-invoicing


### `ls-egov-0030` — reference.md:92 *(§ E-Procurement)*

> E-Procurement gebruikt het Peppol-netwerk als transportlaag voor berichten tussen overheid en leveranciers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** E-Procurement - infrastructuur


### `ls-egov-0031` — reference.md:97 *(§ E-Procurement)*

> E-Procurement dekt circa 90% van alle overheidsfacturen (standaard inkoop- en dienstverleningsfacturen).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** E-Procurement - bereik


### `ls-egov-0032` — reference.md:105 *(§ E-Procurement)*

> NLCIUS is de Nederlandse invulling (Core Invoice Usage Specification) van de Europese norm EN 16931.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NLCIUS


### `ls-egov-0033` — reference.md:77 *(§ Basisorder Rijk)*

> De Basisorder Rijk is gebaseerd op UBL 2.1 Order-berichttype en sluit aan op Peppol-orderberichten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisorder Rijk


### `ls-egov-0034` — reference.md:66 *(§ Best Practices voor Leveranciers)*

> Leveranciers dienen facturen te valideren tegen het NLCIUS-validatieschema voordat deze worden ingediend.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Basisfactuur Rijk - best practices leveranciers


### `ls-egov-0035` — reference.md:65 *(§ Best Practices voor Leveranciers)*

> Facturen voor de Rijksoverheid dienen te worden aangeleverd in UBL 2.1 XML-formaat voor optimale automatische verwerking.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Basisfactuur Rijk - best practices leveranciers


### `ls-egov-0036` — reference.md:93 *(§ E-Procurement)*

> E-Procurement vereist naleving van de Europese norm EN 16931 voor elektronische facturering.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** E-Procurement - compliance


## GROUNDED — minstens één bron ondersteunt de claim (1)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-egov-0020` — SKILL.md:115 *(§ Samenhang Standaarden)*

> Peppol BIS heeft de Forum Standaardisatie status 'aanbevolen', niet verplicht.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Peppol BIS - Forum Standaardisatie

- **SUPPORTED** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis](https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis)
  > Aanbevolen [...] Status 'Aanbevolen' betekent dat dit een gangbare of opkomende standaard is waarvan het Forum Standaardisatie het gebruik aanbeveelt.
  - *De bron vermeldt expliciet 'Aanbevolen' als status van Peppol BIS, niet 'Verplicht (Pas toe of leg uit)'.*

</details>
