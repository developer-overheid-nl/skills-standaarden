<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit ls-logboek — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 6 | 16% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 12 | 32% |
| UNGROUNDED | 0 | 0% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 19 | 51% |

*Geverifieerd met sonnet, 3 calls, $0.3082.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (6)

### `ls-logboek-0002` — SKILL.md:37 *(§ Versiemodel)*

> Logboek Dataverwerkingen is nog niet opgenomen op de lijst van het Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen status

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron vermeldt dat de standaard beoogd is voor opname op de lijst van Forum Standaardisatie (§1.1), maar bevestigt noch ontkent of opname al heeft plaatsgevonden.*

### `ls-logboek-0022` — SKILL.md:153 *(§ Protocol)*

> OTLP ondersteunt zowel gRPC als HTTP/protobuf als transportlaag met standaard poorten 4317 voor gRPC en 4318 voor HTTP, maar deze poorten zijn niet voorgeschreven door de Logboek-standaard zelf.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen protocol

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron noemt OTLP en verwijst naar OpenTelemetry, maar specificeert nergens poortnummers (4317/4318) of een onderscheid tussen gRPC en HTTP/protobuf als transportlagen van OTLP.*

### `ls-logboek-0023` — SKILL.md:173 *(§ NEN 7513 Extensie)*

> De NEN 7513 extensie voegt verplichte attributen toe voor de zorgsector, zoals gebruikersidentificatie, patiëntidentificatie en de specifieke actie op het medisch dossier.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen NEN 7513 extensie

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/logboek-extensie-nen7513](https://github.com/logius-standaarden/logboek-extensie-nen7513)
  - *De aangeleverde brontekst bevat alleen de GitHub-repositorypagina met navigatie-UI, bestandsnamen en metadata. Er is geen inhoudelijke tekst over de NEN 7513 extensie, verplichte attributen, gebruikersidentificatie, patiëntidentificatie of medische dossiers. De specificatie-inhoud (specificatie.md, abstract.md) is niet meegeleverd.*

### `ls-logboek-0032` — reference.md:13 *(§ Architectuur - Kernprincipes)*

> Het Register beschrijft het wat en waarom van een verwerking; het Logboek beschrijft het wanneer en voor wie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen architectuur

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron beschrijft de functies van Register en Logboek afzonderlijk, maar formuleert nergens expliciet het onderscheid als 'Register = wat en waarom, Logboek = wanneer en voor wie'. Dit is een parafrase/synthese die niet letterlijk of als directe parafrase in de bron staat.*

### `ls-logboek-0035` — reference.md:33 *(§ Header formaat)*

> Het W3C Trace Context `traceparent` header formaat is: `<version>-<trace_id>-<span_id>-<trace_flags>` waarbij version altijd `00` is in de huidige specificatie.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context integratie

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron verwijst naar de W3C Trace Context standaard maar beschrijft het exacte header-formaat (<version>-<trace_id>-<span_id>-<trace_flags>) en de versie '00' niet.*

### `ls-logboek-0037` — reference.md:44 *(§ Header formaat)*

> In het W3C Trace Context header formaat geldt: `trace_flags` `01` = gesampled, `00` = niet gesampled.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context integratie

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron vermeldt niets over trace_flags of de semantiek van waarden 01 en 00 daarin. Dit is detail uit de W3C Trace Context specificatie zelf, niet uit deze bron.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (12)

### `ls-logboek-0003` — SKILL.md:37 *(§ Versiemodel)*

> De overige onderdelen van Logboek Dataverwerkingen (inleiding, juridisch-beleidskader, extensies) hebben nog alleen werkversies.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen publicatiekanalen

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De LDV Normatieve Standaard - Logboek dataverwerkingen (werkversie) [...] De Algemene Inleiding - De Algemene Inleiding (werkversie) [...] Het Juridische Beleidskader - Juridisch Beleidskader (werkversie) [...] LDV Extensie Guideline - Guideline voor het schrijven van een extensie voor LDV (werkversie)
  - *De tabel toont alle vier documenten met '(werkversie)' voor gepubliceerde versie, maar de bron zelf ís de vastgestelde versie van document 1. De claim dat de overige drie alleen werkversies hebben wordt ondersteund, maar voor document 1 is de vastgestelde versie juist deze bron zelf. De tabel is vermoedelijk niet volledig bijgewerkt na vaststelling.*

### `ls-logboek-0004` — SKILL.md:75 *(§ Log Record Structuur)*

> Het veld `trace_id` (16 bytes) is verplicht in elk log record en bevat een uniek trace ID over systemen heen conform W3C Trace Context.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > trace_id | 16 byte | verplicht [...] Unieke identificerende code van Trace die Dataverwerking volgt.
  - *De bron bevestigt trace_id als 16 byte en verplicht. De claim dat het 'conform W3C Trace Context' is, wordt niet expliciet zo gesteld voor trace_id zelf; W3C Trace Context wordt genoemd voor metadata-uitwisseling bij HTTP, niet als definitie van trace_id.*

### `ls-logboek-0009` — SKILL.md:80 *(§ Log Record Structuur)*

> Het veld `start_time` (uint64, starttijd in milliseconden sinds Unix Epoch) is verplicht in elk log record.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > start_time | uint64 | verplicht [...] Tijdstip waarop de Actie gestart is in milliseconden sinds Epoch.
  - *De bron bevestigt uint64, verplicht, en milliseconden sinds Epoch. De claim zegt 'Unix Epoch'; de bron zegt alleen 'Epoch' zonder 'Unix' te specificeren — inhoudelijk gelijkwaardig maar niet letterlijk identiek.*

### `ls-logboek-0010` — SKILL.md:81 *(§ Log Record Structuur)*

> Het veld `end_time` (uint64, eindtijd in milliseconden sinds Unix Epoch) is verplicht in elk log record.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > end_time | uint64 | verplicht [...] Tijdstip waarop de Actie beëindigd is in milliseconden sinds Epoch.
  - *Zelfde kanttekening als ls-logboek-0009: 'Epoch' vs 'Unix Epoch' — inhoudelijk gelijkwaardig, niet letterlijk identiek.*

### `ls-logboek-0013` — SKILL.md:99 *(§ Core Attributes (dpl.core namespace))*

> `dpl.core.processing_activity_id` (URI) is een verplicht attribuut dat verwijst naar de verwerkingsactiviteit in het Register conform AVG Art. 30.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > dpl.core.processing_activity_id | URI | Verwijzing naar een Register met meer informatie over de Verwerkingsactiviteit.
  - *De bron bevestigt het veld als URI en verwijzing naar een Register. De claim voegt 'conform AVG Art. 30' toe; de bron vermeldt AVG Art. 30 in de context van het Register van Verwerkingsactiviteiten maar koppelt dat niet expliciet aan dit attribuut als eis.*

### `ls-logboek-0016` — SKILL.md:101 *(§ Core Attributes (dpl.core namespace))*

> `dpl.core.data_subject_id_type` (string) is een verplicht attribuut. Mogelijke waarden zijn: BSN, personeelsnummer, URI, of een ander organisatiespecifiek type.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > dpl.core.data_subject_id_type | String | Type van de identificerende code, zoals BSN, personeelsnummer, of een URI naar een Register dat het type specificeert.
  - *De bron bevestigt het veld en noemt BSN, personeelsnummer en URI als voorbeelden. De claim voegt 'of een ander organisatiespecifiek type' toe, wat de bron niet expliciet noemt maar impliciet open laat. De kern (verplicht, string, genoemde voorbeelden) is ondersteund.*

### `ls-logboek-0017` — SKILL.md:102 *(§ Core Attributes (dpl.core namespace))*

> `dpl.core.foreign_operation.processor` (URL) is een optioneel attribuut met een link naar de externe applicatie of organisatie betrokken bij een cross-organisatie verwerking.

**Type:** factual_assertion  ·  **Modaliteit:** MAY  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > dpl.core.foreign_operation.processor | URL | Link naar externe applicatie
  - *De bron bevestigt het veld als URL en 'link naar externe applicatie'. De claim voegt 'of organisatie betrokken bij een cross-organisatie verwerking' toe; de bron zegt alleen 'externe applicatie', niet expliciet 'organisatie'.*

### `ls-logboek-0026` — SKILL.md:356 *(§ Verplichte Velden Validatie)*

> Een logregel MOET minimaal bevatten: trace_id, span_id, name, start_time, end_time, status, dpl.core.processing_activity_id, dpl.core.data_subject_id en dpl.core.data_subject_id_type.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen verplichte velden

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De interface MOET de volgende velden implementeren: trace_id [...] verplicht, span_id [...] verplicht, status [...] verplicht, name [...] verplicht, start_time [...] verplicht, end_time [...] verplicht [...] dpl.core.processing_activity_id [...] dpl.core.data_subject_id [...] dpl.core.data_subject_id_type
  - *De bron bevestigt al deze velden als verplicht. Echter: dpl.core.data_subject_id en dpl.core.data_subject_id_type zijn verplicht 'voor dataverwerkingen met persoonsdata' (§3.3.1.1); voor dataverwerkingen zonder persoonsdata geldt dit niet. De claim stelt dat een logregel ALTIJD alle negen velden moet bevatten, wat de bron niet onvoorwaardelijk zo stelt.*

### `ls-logboek-0027` — SKILL.md:366 *(§ Verplichte Velden Validatie)*

> Als een verplicht veld ontbreekt, MOET de software een standaardwaarde invullen om runtime-fouten te voorkomen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen verplichte velden

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Bijvoorbeeld als name leeg is, moet deze automatisch worden gevuld met een waarde zodat er in ieder geval op dit punt geen fout kan optreden.
  - *De bron noemt dit principe specifiek alleen voor het veld 'name', niet als algemene regel voor alle verplichte velden. De claim is breder dan wat de bron stelt.*

### `ls-logboek-0030` — reference.md:11 *(§ Architectuur - Kernprincipes)*

> Het Logboek verwijst naar het Register van Verwerkingsactiviteiten (AVG Art. 30) via `dpl.core.processing_activity_id`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen architectuur

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Iedere Dataverwerking van persoonsdata betreft een Verwerkingsactiviteit die in het Register van Verwerkingsactiviteiten moet zijn opgenomen. De Applicatie MOET in de Logregel een verwijzing naar de juiste Verwerkingsactiviteit in het Register van Verwerkingsactiviteiten opnemen in het veld dpl.core.processing_activity_id.
  - *De bron bevestigt de verwijzing via dpl.core.processing_activity_id en de relatie met het Register van Verwerkingsactiviteiten (AVG art. 30), maar de claim stelt dat het 'Logboek' verwijst naar het register, terwijl de bron stelt dat de 'Applicatie' de verwijzing opneemt in de Logregel. Dat is een nuanceverschil in architecturele attributie.*

### `ls-logboek-0033` — reference.md:21 *(§ Inkomende requests)*

> Bij inkomende requests moet de `traceparent` header worden geparsed, het ontvangen `trace_id` gebruikt voor de eigen logregel, en de ontvangen `span_id` opgeslagen als `parent_span_id` in het eigen log record.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context integratie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Als de Applicatie een verzoek van een andere Applicatie kan ontvangen, MOET de Applicatie metadata volgens de W3C Trace Context standaard kunnen verwerken en gebruiken in de eigen Trace(s). Metadata verkregen via W3C Trace Context MOET in attributes meegenomen worden als velden die beginnen met dpl.core.foreign_operation.
  - *De bron bevestigt verwerking van W3C Trace Context metadata bij inkomende requests en gebruik ervan in de eigen trace, maar specificeert niet expliciet het parsen van een 'traceparent' header, en stelt dat metadata wordt opgeslagen als dpl.core.foreign_operation-velden, niet letterlijk als parent_span_id. De claim is specifieker dan de bron.*

### `ls-logboek-0036` — reference.md:42 *(§ Header formaat)*

> In het W3C Trace Context header formaat is `trace_id` 32 hex karakters (16 bytes) uniek per verwerkingsketen, en `span_id` 16 hex karakters (8 bytes) uniek per actie.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context integratie

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > trace_id 16 byte verplicht ... span_id 8 byte verplicht
  - *De bron bevestigt de groottes (16 byte voor trace_id, 8 byte voor span_id), maar noemt niet het hex-formaat (32 resp. 16 hex karakters) en niet de context 'uniek per verwerkingsketen' / 'uniek per actie' in deze exacte bewoording.*

## GROUNDED — minstens één bron ondersteunt de claim (19)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-logboek-0001` — SKILL.md:37 *(§ Versiemodel)*

> De normatieve hoofdspecificatie logboek-dataverwerkingen heeft sinds 9 april 2026 een vastgestelde versie v1.0.0.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen hoofdspecificatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Logboek dataverwerkingen 1.0.0 Logius Standaard Vastgestelde versie 09 april 2026

### `ls-logboek-0005` — SKILL.md:76 *(§ Log Record Structuur)*

> Het veld `span_id` (8 bytes) is verplicht in elk log record en bevat een uniek action ID binnen een verwerking.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > span_id | 8 byte | verplicht [...] Unieke identificerende code van Actie binnen de Dataverwerking.

### `ls-logboek-0006` — SKILL.md:77 *(§ Log Record Structuur)*

> Het veld `parent_span_id` (8 bytes) is optioneel en bevat het ID van de aanroepende actie voor parent-child relaties.

**Type:** factual_assertion  ·  **Modaliteit:** MAY  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > parent_span_id | 8 byte | optioneel [...] Unieke identificerende code aanroepende Actie. Dit geldt voor zowel binnen de huidige applicatie als bij een aanroep van een andere applicatie.

### `ls-logboek-0007` — SKILL.md:78 *(§ Log Record Structuur)*

> Het veld `status` (enum: Unset, Ok, of Error) is verplicht in elk log record.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > status | enum | verplicht [...] Het veld status is een enumeratie die de volgende waarden kan bevatten: Unset [...] Ok [...] Error

### `ls-logboek-0008` — SKILL.md:79 *(§ Log Record Structuur)*

> Het veld `name` (string, mensleesbare actienaam) is verplicht in elk log record.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > name | string | verplicht [...] Naam van de specifieke Actie binnen de Dataverwerking. Dit is een tekstuele beschrijving bestemd voor mensen, niet voor machines.

### `ls-logboek-0011` — SKILL.md:82 *(§ Log Record Structuur)*

> Het veld `resource` (object, systeem- en applicatie-identificatie) is optioneel in elk log record.

**Type:** factual_assertion  ·  **Modaliteit:** MAY  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > resource | object | optioneel

### `ls-logboek-0012` — SKILL.md:83 *(§ Log Record Structuur)*

> Het veld `attributes` (object, verwerkingsmetadata in de `dpl` namespace) is verplicht in elk log record.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > attributes | object | verplicht [...] Het veld attributes is een object, opgebouwd uit velden in een namespace met prefix dpl (data processing log).

### `ls-logboek-0014` — SKILL.md:100 *(§ Core Attributes (dpl.core namespace))*

> `dpl.core.data_subject_id` (string) is een verplicht attribuut met de unieke, versleutelde identificerende code van de betrokkene.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > dpl.core.data_subject_id | String | Unieke, versleutelde identificerende code van de Betrokkene.

### `ls-logboek-0015` — SKILL.md:100 *(§ Core Attributes (dpl.core namespace))*

> De specificatie BEVEELT AAN (SHOULD) om `dpl.core.data_subject_id` te pseudonimiseren.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Het wordt AANBEVOLEN om de identificerende code te pseudonimiseren.
  - *AANBEVOLEN correspondeert met SHOULD conform BCP 14 / RFC 2119.*

### `ls-logboek-0018` — SKILL.md:115 *(§ Core Attributes (dpl.core namespace))*

> De specificatie schrijft geen specifiek pseudonimiseringsalgoritme voor `dpl.core.data_subject_id` voor.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Het wordt AANBEVOLEN om de identificerende code te pseudonimiseren.
  - *De bron beveelt pseudonimisering aan maar schrijft geen specifiek algoritme voor. De claim is een negatieve bewering (geen algoritme voorgeschreven) die consistent is met de brontekst.*

### `ls-logboek-0019` — SKILL.md:147 *(§ Protocol)*

> De standaard schrijft geen specifiek transportprotocol voor, maar beveelt OpenTelemetry Protocol (OTLP) aan als transportprotocol voor het aanleveren van logregels aan het Logboek.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Logboek Dataverwerkingen protocol

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De protocollen die worden gebruikt tussen applicatie en logboek [...] worden niet voorgeschreven in de standaard. [...] Het is AANBEVOLEN om het OpenTelemetry Protocol (OTLP) te gebruiken in de interactie tussen Applicatie en Logboek.

### `ls-logboek-0020` — SKILL.md:151 *(§ Protocol)*

> Het Logboek MOET TLS kunnen afdwingen (capability-eis aan de software); of TLS-connecties daadwerkelijk worden toegepast is een organisatie-keuze.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen protocol

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Het Logboek MOET TLS kunnen afdwingen. [...] Als er software wordt geschreven dat een Logboek component implementeert, dan moet dit TLS kunnen ondersteunen. Of TLS connecties daadwerkelijk worden toegepast door organisaties die de software gebruiken, is de keuze van de organisatie zelf.

### `ls-logboek-0021` — SKILL.md:152 *(§ Protocol)*

> Het Logboek MOET elke schrijfactie bevestigen met een bevestigingsbericht (acknowledgement).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen protocol

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Het Logboek MOET het wegschrijven van elke logregel bevestigen.

### `ls-logboek-0024` — SKILL.md:328 *(§ Status Waarden en Wanneer te Gebruiken)*

> Status `Unset` wordt gebruikt wanneer een verwerking is afgerond zonder systeemfout, ook als er geen resultaat is (bijv. persoon niet gevonden in BRP).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen foutafhandeling

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Unset: De standaardwaarde voor elke status is Unset. Dit betekent dat de dataverwerking is uitgevoerd zonder interne fout. Deze waarde wordt toegepast wanneer de dataverwerking technisch correct is afgerond, ook als er geen resultaat beschikbaar is of wanneer de invoer onvolledig was.

### `ls-logboek-0025` — SKILL.md:330 *(§ Status Waarden en Wanneer te Gebruiken)*

> Status `Error` wordt gebruikt bij een systeemfout tijdens verwerking (bijv. database timeout, API onbereikbaar). Een gebruikersannulering is GEEN error.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Logboek Dataverwerkingen foutafhandeling

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Error: De waarde Error wordt toegekend bij fouten die zijn ontstaan binnen het systeem dat de dataverwerking uitvoert, zoals interne fouten of mislukte uitvoeringen door technische oorzaken. [...] wanneer een gebruiker een verwerking bewust afbreekt, wordt dit niet als een fout beschouwd.
  - *De bron bevestigt beide onderdelen van de claim: Error voor systeemfouten, en gebruikersannulering is geen Error.*

### `ls-logboek-0028` — SKILL.md:366 *(§ Verplichte Velden Validatie)*

> Log sampling is NIET toegestaan bij Logboek Dataverwerkingen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Logboek Dataverwerkingen verplichte velden

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De Applicatie MAG NIET gebruik maken van Log Sampling.

### `ls-logboek-0029` — reference.md:9 *(§ Architectuur - Kernprincipes)*

> Elke verwerkingsverantwoordelijke beheert een eigen Logboek; een applicatie logt uitsluitend de eigen verwerkingsactiviteiten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen architectuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Belangrijk uitgangspunt is dat een Verantwoordelijke alleen Logregels bijhoudt voor Dataverwerkingen die onder eigen verantwoordelijkheid plaatsvinden.

### `ls-logboek-0031` — reference.md:12 *(§ Architectuur - Kernprincipes)*

> Er wordt geen inhoudelijke data gedeeld tussen organisaties; alleen Trace-metadata (trace_id, span_id) wordt meegegeven om verwerkingen over organisatiegrenzen te correleren.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Logboek Dataverwerkingen architectuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Er wordt met de standaard geen inhoudelijke informatie over Dataverwerkingen uitgewisseld tussen Verantwoordelijken. De informatie die wordt uitgewisseld is beperkt tot zogenaamde Trace-informatie waarmee Logregels van de ene Verantwoordelijke gerelateerd kunnen worden aan Logregels bij de andere Verantwoordelijke.

### `ls-logboek-0034` — reference.md:27 *(§ Uitgaande requests)*

> Bij uitgaande requests moet een `traceparent` header worden toegevoegd met het actieve `trace_id` en een nieuw gegenereerd `span_id`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context integratie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Als de Applicatie een verzoek aan een andere Applicatie kan versturen, MOET de Applicatie metadata volgens de W3C Trace Context standaard meegeven aan dit verzoek.
  - *De bron zegt dat W3C Trace Context metadata moet worden meegegeven bij uitgaande requests, maar specificeert niet het exacte header-formaat (traceparent) of dat er een nieuw span_id moet worden gegenereerd. De kern van de claim wordt ondersteund.*

</details>
