<!-- markdownlint-disable MD052 MD034 MD013 MD038 -->
# Audit ls-logboek — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 7 | 18% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 15 | 38% |
| UNGROUNDED | 0 | 0% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 17 | 44% |

*Geverifieerd met sonnet, 5 calls, $0.4027.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (7)

### `ls-logboek-0002` — SKILL.md:37 *(§ Versiemodel)*

> Logboek Dataverwerkingen is nog niet opgenomen op de lijst van het Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen standaard status

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron vermeldt alleen dat de sectie werkingsgebied 'beoogde beschrijvingen voor opname op de lijst van Aanbevolen standaarden van Forum Standaardisatie' bevat, maar zegt niet expliciet dat de standaard er nog niet op staat.*

### `ls-logboek-0022` — SKILL.md:153 *(§ Protocol)*

> OTLP ondersteunt zowel gRPC als HTTP/protobuf als transportlaag; standaard OTLP-poorten zijn 4317 voor gRPC en 4318 voor HTTP.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen protocol / OTLP

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron noemt OTLP maar beschrijft geen transportlagen (gRPC vs HTTP/protobuf) of specifieke poorten (4317/4318). Dit is OTLP-interne specificatie die buiten scope van deze standaard valt.*

### `ls-logboek-0024` — SKILL.md:161 *(§ Object Extensie)*

> De Object Extensie definieert aanvullende attributes in de `dpl.objects` namespace voor het vastleggen van objectgegevens bij verwerkingen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen Object Extensie

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/logboek-extensie-object](https://github.com/logius-standaarden/logboek-extensie-object)
  - *De brontekst is de GitHub repository README van logboek-extensie-object. Deze bevat alleen een projectbeschrijving, inleiding, doel en verwijzingstabel. Er is geen technische inhoud over de `dpl.objects` namespace of aanvullende attributes voor objectgegevens. De claim kan niet worden bevestigd of weersproken op basis van deze brontekst.*

### `ls-logboek-0026` — SKILL.md:173 *(§ NEN 7513 Extensie)*

> De NEN 7513 Extensie voegt verplichte attributen toe voor de zorgsector, zoals gebruikersidentificatie, patiëntidentificatie en de specifieke actie op het medisch dossier.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen NEN 7513 Extensie

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/logboek-extensie-nen7513](https://github.com/logius-standaarden/logboek-extensie-nen7513)
  - *De aangeleverde brontekst bevat alleen de GitHub-repositorypagina met metadata (bestandslijst, contributeurs, licentie, etc.). De inhoud van specificatie.md of abstract.md is niet meegeleverd. Er is geen informatie over verplichte attributen, gebruikersidentificatie, patiëntidentificatie of acties op medische dossiers.*

### `ls-logboek-0034` — reference.md:13 *(§ Architectuur - Kernprincipes)*

> Het Register beschrijft het wat en waarom; het Logboek beschrijft het wanneer en voor wie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen architectuur

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron beschrijft de rollen van Register en Logboek afzonderlijk, maar formuleert nergens expliciet de samenvatting 'het Register beschrijft het wat en waarom; het Logboek beschrijft het wanneer en voor wie'. Dit onderscheid staat niet als zodanig in de brontekst.*

### `ls-logboek-0037` — reference.md:41 *(§ Header formaat)*

> Het traceparent header formaat is `<version>-<trace_id>-<span_id>-<trace_flags>`, waarbij `version` altijd `00` is in de huidige specificatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context header formaat

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron verwijst naar de W3C Trace Context specificatie maar beschrijft het traceparent header formaat (<version>-<trace_id>-<span_id>-<trace_flags> met version=00) niet in de brontekst zelf.*

### `ls-logboek-0039` — reference.md:44 *(§ Header formaat)*

> In het traceparent header betekent `trace_flags` waarde `01` dat de trace gesampled is; `00` betekent niet gesampled.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context header formaat

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  - *De bron beschrijft de trace_flags waarden (01=gesampled, 00=niet gesampled) niet. Dit is detail uit de W3C Trace Context specificatie, niet uit de brontekst.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (15)

### `ls-logboek-0003` — SKILL.md:37 *(§ Versiemodel)*

> De overige onderdelen van Logboek Dataverwerkingen (inleiding, juridisch-beleidskader, extensies) hebben nog alleen werkversies.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen publicatiekanalen

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De LDV Normatieve Standaard - Logboek dataverwerkingen (werkversie) logboek-dataverwerkingen / De Algemene Inleiding - De Algemene Inleiding (werkversie) / Het Juridische Beleidskader - Juridisch Beleidskader (werkversie) / LDV Extensie Guideline - Guideline voor het schrijven van een extensie voor LDV (werkversie)
  - *De bron bevestigt dat inleiding, juridisch beleidskader en extensie guideline werkversies hebben, maar geeft geen expliciete 'gepubliceerde versie' kolom-waarden voor die drie — de kolom 'Gepubliceerde versie' lijkt leeg voor die documenten. De claim is daarmee grotendeels ondersteund maar niet volledig aantoonbaar uit de tabel.*

### `ls-logboek-0004` — SKILL.md:27 *(§ Logboek Dataverwerkingen)*

> Logboek Dataverwerkingen is gebaseerd op OpenTelemetry en W3C Trace Context, waardoor verwerkingen over organisatiegrenzen heen traceerbaar zijn.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen architectuur

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Het is AANBEVOLEN om het OpenTelemetry Protocol (OTLP) te gebruiken in de interactie tussen Applicatie en Logboek. ... Als gebruik wordt gemaakt van HTTP/1.1 of HTTP/2 voor het uitvoeren van dataverwerkingen in meerdere applicaties MOET gebruik worden gemaakt van de Trace Context specificatie voor het uitwisselen van metadata over Traces.
  - *De bron bevestigt OTLP (aanbevolen) en W3C Trace Context (verplicht bij HTTP), en bevestigt dat verwerkingen over organisatiegrenzen heen traceerbaar zijn. Echter: OTLP is aanbevolen, niet verplicht, dus 'gebaseerd op OpenTelemetry' is enigszins sterker gesteld dan de bron rechtvaardigt.*

### `ls-logboek-0005` — SKILL.md:75 *(§ Log Record Structuur)*

> Het log record veld `trace_id` (16 bytes) is verplicht en vormt een uniek trace ID over systemen heen conform W3C Trace Context.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > trace_id | 16 byte | verplicht ... Unieke identificerende code van Trace die Dataverwerking volgt. Als er meerdere applicaties dataverwerkingen uitvoeren ten behoeve van 1 originele dataverwerking, dan is de trace code identiek voor al deze dataverwerkingen
  - *De bron bevestigt dat trace_id 16 bytes en verplicht is, en dat het over meerdere applicaties wordt gedeeld. De claim stelt 'conform W3C Trace Context' — de bron vermeldt W3C Trace Context voor HTTP-verkeer, maar koppelt dit niet expliciet aan de trace_id definitie zelf.*

### `ls-logboek-0010` — SKILL.md:80 *(§ Log Record Structuur)*

> Het log record veld `start_time` (uint64) is verplicht en bevat de starttijd in milliseconden sinds Unix Epoch.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > start_time | uint64 | verplicht ... Tijdstip waarop de Actie gestart is in milliseconden sinds Epoch.
  - *De bron zegt 'milliseconden sinds Epoch', de claim zegt 'milliseconden sinds Unix Epoch'. Dit is inhoudelijk hetzelfde, maar de bron gebruikt niet het woord 'Unix'. Verder volledig ondersteund.*

### `ls-logboek-0011` — SKILL.md:81 *(§ Log Record Structuur)*

> Het log record veld `end_time` (uint64) is verplicht en bevat de eindtijd in milliseconden sinds Unix Epoch.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > end_time | uint64 | verplicht ... Tijdstip waarop de Actie beëindigd is in milliseconden sinds Epoch.
  - *Zelfde nuance als ls-logboek-0010: 'Epoch' vs 'Unix Epoch'. Inhoudelijk gelijkwaardig.*

### `ls-logboek-0014` — SKILL.md:99 *(§ Core Attributes (dpl.core namespace))*

> `dpl.core.processing_activity_id` is een verplicht URI-attribuut dat verwijst naar de verwerkingsactiviteit in het Register (AVG Art. 30).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > dpl.core.processing_activity_id | URI | Verwijzing naar een Register met meer informatie over de Verwerkingsactiviteit.
  - *De bron bevestigt dat het een verplicht URI-attribuut is dat verwijst naar het Register. De claim voegt '(AVG Art. 30)' toe als specificatie van het Register — de bron vermeldt AVG art. 30 elders in de context van het Register van Verwerkingsactiviteiten, maar koppelt dit niet expliciet aan dpl.core.processing_activity_id in de attribuut-definitie zelf.*

### `ls-logboek-0016` — SKILL.md:101 *(§ Core Attributes (dpl.core namespace))*

> `dpl.core.data_subject_id_type` is een verplicht string-attribuut met mogelijke waarden `BSN`, `personeelsnummer`, `URI`, of een ander organisatiespecifiek type.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > dpl.core.data_subject_id_type | String | Type van de identificerende code, zoals BSN, personeelsnummer, of een URI naar een Register dat het type specificeert.
  - *De bron bevestigt dat het veld verplicht is en noemt BSN, personeelsnummer en URI als voorbeelden. De claim noemt ook 'ander organisatiespecifiek type' — dat staat impliciet in de voorbeeldopsomming maar niet letterlijk zo geformuleerd.*

### `ls-logboek-0025` — SKILL.md:167 *(§ Lees Extensie)*

> De basisstandaard definieert alleen het schrijven van logregels; de Lees Extensie voegt leesoperaties toe en ondersteunt filteren op trace_id, tijdsbereik en betrokkene.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen Lees Extensie

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/logboek-extensie-lezen](https://github.com/logius-standaarden/logboek-extensie-lezen)
  > De extensie lezen breid deze uit met de mogelijkheid te kunnen lezen: De logs van een (interne) bron te lezen, Logs lezen bij de(externe) bron(loggende organisatie), Gerelateerde logs bij meerdere bronnen op te vragen
  - *De bron bevestigt dat de basisstandaard gericht is op schrijven (wegschrijven, relateren van logs) en dat de Lees Extensie leesoperaties toevoegt. Echter, de specifieke filtermogelijkheden op trace_id, tijdsbereik en betrokkene worden nergens in de brontekst vermeld. Die details staan vermoedelijk in de inhoud van de standaard zelf, niet in de README.*

### `ls-logboek-0027` — SKILL.md:356 *(§ Verplichte Velden Validatie)*

> Een logregel MOET minimaal `trace_id` (16 bytes), `span_id` (8 bytes), `name`, `start_time`, `end_time`, `status`, `dpl.core.processing_activity_id`, `dpl.core.data_subject_id` en `dpl.core.data_subject_id_type` bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen verplichte velden

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De interface MOET de volgende velden implementeren: trace_id 16 byte verplicht / span_id 8 byte verplicht / status enum verplicht / name string verplicht / start_time uint64 verplicht / end_time uint64 verplicht / attributes object verplicht ... dpl.core.processing_activity_id URI ... dpl.core.data_subject_id String ... dpl.core.data_subject_id_type String
  - *De bron bevestigt alle genoemde velden als verplicht. Echter: dpl.core.processing_activity_id, dpl.core.data_subject_id en dpl.core.data_subject_id_type zijn verplicht specifiek voor dataverwerkingen met persoonsdata (sectie 3.3.1.1). Voor verwerkingen zonder persoonsdata is dpl.core.processing_activity_id slechts aanbevolen (AANBEVOLEN). De claim stelt een absolute minimumverplichting zonder deze nuance.*

### `ls-logboek-0028` — SKILL.md:366 *(§ Verplichte Velden Validatie)*

> Als een verplicht veld ontbreekt, MOET de software een standaardwaarde invullen om runtime-fouten te voorkomen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen verplichte velden validatie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De software van de applicatie die de registratie van de logdata registreert, moet er voor zorgen dat er geen fout optreedt in 'run-time'. Bijvoorbeeld als name leeg is, moet deze automatisch worden gevuld met een waarde zodat er in ieder geval op dit punt geen fout kan optreden.
  - *De bron beschrijft dit als uitgangspunt voor foutregistratie (sectie 3.3.2.1), niet als een normatieve MOET-eis geformuleerd met het RFC2119-trefwoord MUST/MOET. De strekking klopt, maar de formulering als harde MUST-verplichting is sterker dan de bron ondersteunt.*

### `ls-logboek-0030` — reference.md:9 *(§ Architectuur - Kernprincipes)*

> Elke verwerkingsverantwoordelijke beheert een eigen Logboek.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen architectuur

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Iedere Verantwoordelijke kan een veelheid aan Applicaties, Logboeken en Registers gebruiken. Iedere Verantwoordelijke houdt alleen Logregels bij over eigen Dataverwerkingen.
  - *De bron bevestigt dat iedere Verantwoordelijke eigen logregels bijhoudt, maar stelt niet expliciet dat elke verwerkingsverantwoordelijke een 'eigen Logboek beheert' als verplichting. Meerdere Logboeken per Verantwoordelijke zijn mogelijk; het is geen 1-op-1 relatie.*

### `ls-logboek-0032` — reference.md:11 *(§ Architectuur - Kernprincipes)*

> Het Logboek verwijst naar het Register van Verwerkingsactiviteiten (AVG Art. 30) via `dpl.core.processing_activity_id`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen architectuur

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Iedere Dataverwerking van persoonsdata betreft een Verwerkingsactiviteit die in het Register van Verwerkingsactiviteiten moet zijn opgenomen. De Applicatie MOET in de Logregel een verwijzing naar de juiste Verwerkingsactiviteit in het Register van Verwerkingsactiviteiten opnemen in het veld dpl.core.processing_activity_id .
  - *De bron bevestigt de koppeling via dpl.core.processing_activity_id naar het Register van Verwerkingsactiviteiten (AVG art. 30). De claim stelt echter dat 'het Logboek verwijst naar het Register', terwijl de bron specificeert dat de Applicatie (niet het Logboek zelf) de verwijzing in de logregel opneemt. Bovendien geldt de verplichting in de bron primair voor persoonsdata; voor dataverwerkingen zonder persoonsdata is het slechts aanbevolen.*

### `ls-logboek-0035` — reference.md:21 *(§ Inkomende requests)*

> Bij inkomende requests moet de `traceparent` header geparsed worden en het ontvangen `trace_id` gebruikt worden voor de eigen logregel; de ontvangen `span_id` wordt opgeslagen als `parent_span_id`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context integratie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Als de Applicatie een verzoek van een andere Applicatie kan ontvangen, MOET de Applicatie metadata volgens de W3C Trace Context standaard kunnen verwerken en gebruiken in de eigen Trace(s). Metadata verkregen via W3C Trace Context MOET in attributes meegenomen worden als velden die beginnen met dpl.core.foreign_operation .
  - *De bron bevestigt dat inkomende W3C Trace Context metadata verwerkt en gebruikt moet worden. De claim spreekt specifiek over de 'traceparent header', het parsen ervan, en dat de ontvangen span_id wordt opgeslagen als parent_span_id. De bron verwijst naar parent_span_id en foreign_operation attributen maar specificeert de 'traceparent header' niet bij naam in de normatieve tekst — dat detail staat in de gerefereerde W3C Trace Context specificatie, niet in de brontekst zelf.*

### `ls-logboek-0036` — reference.md:27 *(§ Uitgaande requests)*

> Bij uitgaande requests moet een `traceparent` header worden toegevoegd met het actieve `trace_id` en een nieuw gegenereerd `span_id`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context integratie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Als de Applicatie een verzoek aan een andere Applicatie kan versturen, MOET de Applicatie metadata volgens de W3C Trace Context standaard meegeven aan dit verzoek.
  - *De bron bevestigt de verplichting om W3C Trace Context metadata mee te geven bij uitgaande requests. De claim specificeert 'traceparent header met actieve trace_id en nieuw gegenereerd span_id'; de bron verwijst hiervoor naar de W3C Trace Context standaard zonder de header of het nieuwe span_id expliciet te noemen.*

### `ls-logboek-0038` — reference.md:42 *(§ Header formaat)*

> Het `trace_id` in het traceparent header bestaat uit 32 hex karakters (16 bytes) en is uniek per verwerkingsketen; het `span_id` bestaat uit 16 hex karakters (8 bytes) en is uniek per actie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen W3C Trace Context header formaat

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > trace_id 16 byte verplicht [...] span_id 8 byte verplicht
  - *De bron bevestigt dat trace_id 16 bytes is en span_id 8 bytes, en dat trace_id dataverwerkingen groepeert (uniek per verwerkingsketen) en span_id uniek is per actie. De claim voegt '32 hex karakters' en '16 hex karakters' toe als representatie; dit klopt rekenkundig maar staat niet letterlijk in de bron. Het traceparent header formaat staat ook niet in de bron.*

## GROUNDED — minstens één bron ondersteunt de claim (17)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-logboek-0001` — SKILL.md:37 *(§ Versiemodel)*

> De normatieve hoofdspecificatie logboek-dataverwerkingen heeft sinds 9 april 2026 een vastgestelde versie v1.0.0.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen hoofdspecificatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Logboek dataverwerkingen 1.0.0 Logius Standaard Vastgestelde versie 09 april 2026

### `ls-logboek-0006` — SKILL.md:76 *(§ Log Record Structuur)*

> Het log record veld `span_id` (8 bytes) is verplicht en vormt een uniek action ID binnen een verwerking.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > span_id | 8 byte | verplicht ... Unieke identificerende code van Actie binnen de Dataverwerking. Een applicatie kan meerdere span_id voor dezelfde trace_id hebben.

### `ls-logboek-0007` — SKILL.md:77 *(§ Log Record Structuur)*

> Het log record veld `parent_span_id` (8 bytes) is optioneel en bevat het ID van de aanroepende actie voor parent-child relaties.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > parent_span_id | 8 byte | optioneel ... Unieke identificerende code aanroepende Actie. Dit geldt voor zowel binnen de huidige applicatie als bij een aanroep van een andere applicatie.

### `ls-logboek-0008` — SKILL.md:78 *(§ Log Record Structuur)*

> Het log record veld `status` (enum) is verplicht en heeft waarden `Unset`, `Ok`, of `Error`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > status | enum | verplicht ... Het veld status is een enumeratie die de volgende waarden kan bevatten: Unset ... Ok ... Error

### `ls-logboek-0009` — SKILL.md:79 *(§ Log Record Structuur)*

> Het log record veld `name` (string) is verplicht en bevat een mensleesbare actienaam.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > name | string | verplicht ... Naam van de specifieke Actie binnen de Dataverwerking. Dit is een tekstuele beschrijving bestemd voor mensen, niet voor machines.

### `ls-logboek-0012` — SKILL.md:82 *(§ Log Record Structuur)*

> Het log record veld `resource` (object) is optioneel en bevat systeem- en applicatie-identificatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > resource | object | optioneel ... Het veld resource is een object, opgebouwd uit de volgende velden: attributes Any Een object met velden dat gebruikt wordt om een systeem, applicatie of component aan te duiden op een manier die binnen de organisatie gebruikelijk is.

### `ls-logboek-0013` — SKILL.md:83 *(§ Log Record Structuur)*

> Het log record veld `attributes` (object) is verplicht en bevat verwerkingsmetadata in de `dpl` namespace.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen log record structuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > attributes | object | verplicht ... Het veld attributes is een object, opgebouwd uit velden in een namespace met prefix dpl (data processing log).

### `ls-logboek-0015` — SKILL.md:100 *(§ Core Attributes (dpl.core namespace))*

> `dpl.core.data_subject_id` is een verplicht string-attribuut met de unieke, versleutelde identificerende code van de betrokkene. De specificatie BEVEELT AAN om deze te pseudonimiseren.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > dpl.core.data_subject_id | String | Unieke, versleutelde identificerende code van de Betrokkene. ... Het wordt AANBEVOLEN om de identificerende code te pseudonimiseren.
  - *De bron bevestigt zowel dat het veld verplicht en versleuteld is, als dat pseudonimisering wordt aanbevolen (SHOULD).*

### `ls-logboek-0017` — SKILL.md:102 *(§ Core Attributes (dpl.core namespace))*

> `dpl.core.foreign_operation.processor` is een optioneel URL-attribuut met een link naar de externe applicatie of organisatie bij een cross-organisatie verwerking.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > dpl.core.foreign_operation.processor | URL | Link naar externe applicatie ... Als dpl.core.foreign_operation.processor aanwezig is (zie attributes), dan is het een aanroep van een andere applicatie.
  - *De bron bevestigt het als optioneel URL-attribuut voor cross-applicatie aanroepen. De claim zegt 'externe applicatie of organisatie' — de bron spreekt over 'externe applicatie', niet expliciet over organisatie, maar de context (over organisatiegrenzen) sluit aan.*

### `ls-logboek-0018` — SKILL.md:115 *(§ Core Attributes (dpl.core namespace))*

> De specificatie schrijft geen specifiek pseudonimiseringsalgoritme voor voor `dpl.core.data_subject_id`.

**Type:** normative_requirement  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen dpl.core namespace

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Het wordt AANBEVOLEN om de identificerende code te pseudonimiseren.
  - *De bron beveelt pseudonimisering aan maar schrijft geen specifiek algoritme voor. Dit ondersteunt de claim dat geen specifiek algoritme is voorgeschreven.*

### `ls-logboek-0019` — SKILL.md:147 *(§ Protocol)*

> De standaard schrijft geen specifiek transportprotocol voor, maar beveelt OpenTelemetry Protocol (OTLP) aan als transportprotocol voor het aanleveren van logregels aan het Logboek.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Logboek Dataverwerkingen protocol

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De protocollen die worden gebruikt tussen applicatie en logboek en voor het uitvoeren van transacties tussen applicaties worden niet voorgeschreven in de standaard. ... Het is AANBEVOLEN om het OpenTelemetry Protocol (OTLP) te gebruiken in de interactie tussen Applicatie en Logboek.

### `ls-logboek-0020` — SKILL.md:151 *(§ Protocol)*

> Het Logboek MOET TLS kunnen afdwingen (capability-eis aan de software); of TLS-connecties daadwerkelijk worden toegepast is een organisatiekeuze.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen protocol

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Het Logboek MOET TLS kunnen afdwingen. Noot: Hiermee wordt niet bedoeld dat TLS verplicht is. Als er software wordt geschreven dat een Logboek component implementeert, dan moet dit TLS kunnen ondersteunen. Of TLS connecties daadwerkelijk worden toegepast door organisaties die de software gebruiken, is de keuze van de organisatie zelf.

### `ls-logboek-0021` — SKILL.md:152 *(§ Protocol)*

> Het Logboek MOET elke schrijfactie bevestigen met een bevestigingsbericht (acknowledgement).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen protocol

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Het Logboek MOET het wegschrijven van elke logregel bevestigen.

### `ls-logboek-0023` — SKILL.md:153 *(§ Protocol)*

> De standaard OTLP-poorten (4317 voor gRPC, 4318 voor HTTP) zijn niet voorgeschreven door de Logboek-standaard zelf.

**Type:** normative_requirement  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logboek Dataverwerkingen protocol

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De protocollen die worden gebruikt tussen applicatie en logboek en voor het uitvoeren van transacties tussen applicaties worden niet voorgeschreven in de standaard.
  - *De bron schrijft geen poorten voor; de claim dat standaard OTLP-poorten niet door de Logboek-standaard zijn voorgeschreven is consistent met de algemene vrijheid die de standaard laat voor transportprotocollen.*

### `ls-logboek-0029` — SKILL.md:366 *(§ Verplichte Velden Validatie)*

> Log sampling is NIET toegestaan.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Logboek Dataverwerkingen implementatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > De Applicatie MAG NIET gebruik maken van Log Sampling .

### `ls-logboek-0031` — reference.md:10 *(§ Architectuur - Kernprincipes)*

> Een applicatie logt uitsluitend de eigen verwerkingsactiviteiten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logboek Dataverwerkingen architectuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Belangrijk uitgangspunt is dat een Verantwoordelijke alleen Logregels bijhoudt voor Dataverwerkingen die onder eigen verantwoordelijkheid plaatsvinden.

### `ls-logboek-0033` — reference.md:12 *(§ Architectuur - Kernprincipes)*

> Er wordt geen inhoudelijke data gedeeld tussen organisaties; alleen Trace-metadata (trace_id, span_id) wordt meegegeven om verwerkingen over organisatiegrenzen te correleren.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Logboek Dataverwerkingen cross-organisatie architectuur

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0](https://gitdocumentatie.logius.nl/publicatie/logboek/dataverwerkingen/1.0.0)
  > Er wordt met de standaard geen inhoudelijke informatie over Dataverwerkingen uitgewisseld tussen Verantwoordelijken. [...] De informatie die wordt uitgewisseld is beperkt tot zogenaamde Trace -informatie waarmee Logregels van de ene Verantwoordelijke gerelateerd kunnen worden aan Logregels bij de andere Verantwoordelijke.
  - *De bron noemt trace-informatie (niet expliciet 'trace_id en span_id' maar dit vloeit voort uit de Trace Context specificatie die de standaard gebruikt).*

</details>
