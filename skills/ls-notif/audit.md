<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit ls-notif — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 13 | 46% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 1 | 4% |
| UNGROUNDED | 11 | 39% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 3 | 11% |

*Geverifieerd met sonnet, 10 calls, $0.7333.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (13)

### `ls-notif-0001` — SKILL.md:34 *(§ Versiemodel)*

> Het NL GOV profiel voor CloudEvents heeft een vastgestelde versie (v1.1 DEF).

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profiel voor CloudEvents

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *De aangeleverde brontekst bevat alleen een redirect-melding ('Redirecting to v1.1') en geen inhoudelijke tekst over versies of vaststellingen.*

### `ls-notif-0002` — SKILL.md:36 *(§ Versiemodel)*

> Op het Forum Standaardisatie staat CloudEvents v1.0 als verplicht ('pas-toe-of-leg-uit'), goedgekeurd OBDO 25-11-2025.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Forum Standaardisatie / NL GOV profiel voor CloudEvents

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding ('Redirecting to v0.0.1') en is verder leeg/onbruikbaar. Geen inhoud beschikbaar om deze claim te verifiëren.*

### `ls-notif-0003` — SKILL.md:36 *(§ Versiemodel)*

> Versie v1.1 is de meest recente DEF van Logius voor het NL GOV profiel voor CloudEvents.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profiel voor CloudEvents

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*

### `ls-notif-0004` — SKILL.md:47 *(§ Repositories)*

> Abonneren WV v0.0.1 is gepubliceerd op gitdocumentatie.logius.nl maar is nog niet vastgesteld als standaard.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Abonneren API-specificatie

<details><summary>8x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents](https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents)
  - *De bron behandelt de Abonneren API-specificatie of gitdocumentatie.logius.nl niet. De bron is de GitHub repository pagina voor NL-GOV-profile-for-CloudEvents.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/NL-GOV-profile-for-CloudEvents](https://logius-standaarden.github.io/NL-GOV-profile-for-CloudEvents)
  - *De bron behandelt het NL-GOV-profile-for-CloudEvents specificatie, niet de Abonneren API-specificatie of Abonneren WV v0.0.1. Er is geen vermelding van een Abonneren-standaard of versienummer in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/CloudEvents-NL-Guidelines](https://github.com/logius-standaarden/CloudEvents-NL-Guidelines)
  - *De brontekst betreft de CloudEvents-NL-Guidelines repository op GitHub. Er is geen informatie over de Abonneren API-specificatie of Abonneren WV v0.0.1 in de aangeleverde tekst.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/CloudEvents-NL-Guidelines](https://logius-standaarden.github.io/CloudEvents-NL-Guidelines)
  - *De brontekst behandelt de CloudEvents-NL-Guidelines handreiking, niet de Abonneren API-specificatie. Geen vermelding van 'Abonneren WV v0.0.1' of publicatiestatus daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Notificatieservices](https://github.com/logius-standaarden/Notificatieservices)
  - *De bron vermeldt een 'Concept API-specificatie voor geautomatiseerd abonneren' maar geeft geen versienummer (v0.0.1) of publicatielocatie (gitdocumentatie.logius.nl). Er staat ook niets over de vaststelling als standaard.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Abonneren](https://github.com/logius-standaarden/Abonneren)
  - *De brontekst betreft de GitHub-repository 'Abonneren' van Logius-standaarden. Er staat geen vermelding van een versienummer (v0.0.1), publicatie op gitdocumentatie.logius.nl, of de vaststelling als standaard.*
</details>

### `ls-notif-0011` — SKILL.md:70 *(§ Optionele attributen)*

> Het optionele attribuut `dataref` verwijst naar een externe locatie waar de volledige event payload beschikbaar is en implementeert het Claim Check Pattern voor grote payloads.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profiel voor CloudEvents - optionele attributen

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0013` — SKILL.md:76 *(§ Notificatieservices API)*

> De Notificatieservices API is gespecificeerd als OpenAPI 3.x en biedt een centraal endpoint voor het publiceren van events.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Notificatieservices API

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0015` — SKILL.md:108 *(§ Abonneren)*

> De huidige Notificatieservices OpenAPI-specificatie bevat alleen push-endpoints voor events (`POST /events`); er zijn geen pull/polling-endpoints voor het ophalen van events.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Notificatieservices API

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0019` — SKILL.md:308 *(§ Notificatieservice Error Responses)*

> Bij een HTTP 403-respons van de notificatieservice ontbreekt de scope `notifications.distribute`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Notificatieservices API - foutafhandeling

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0021` — reference.md:21 *(§ Kernconcepten)*

> CloudEvents is een CNCF standaard voor het beschrijven van events in een cloud-omgeving.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** CloudEvents kernstandaard

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0024` — reference.md:44 *(§ Niet aanbevolen technologieën)*

> WebSub wordt niet aanbevolen vanwege verouderde status, beperkte ondersteuning en community.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Aanbevolen technologieën voor notificatieservices

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0025` — reference.md:45 *(§ Niet aanbevolen technologieën)*

> MQTT wordt niet aanbevolen voor overheidsnotificaties omdat het primair gericht is op IoT-toepassingen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Aanbevolen technologieën voor notificatieservices

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0026` — reference.md:46 *(§ Niet aanbevolen technologieën)*

> GraphQL Subscriptions wordt niet aanbevolen vanwege te sterke koppeling aan specifieke API-implementaties.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Aanbevolen technologieën voor notificatieservices

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0028` — reference.md:25 *(§ Kernconcepten)*

> De event source wordt geïdentificeerd via OIN in URN-notatie (nld namespace).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profiel voor CloudEvents - kernconcepten

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (1)

### `ls-notif-0010` — SKILL.md:69 *(§ Optionele attributen)*

> Het optionele attribuut `time` bevat het tijdstip in RFC 3339 formaat. Dit is het tijdstip van logging/registratie van het event, niet noodzakelijk het moment van de werkelijke gebeurtenis.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profiel voor CloudEvents - optionele attributen

- **PARTIALLY_SUPPORTED** (medium) — [https://www.rfc-editor.org/rfc/rfc3339.txt](https://www.rfc-editor.org/rfc/rfc3339.txt)
  > date-time = full-date "T" full-time [...] The following profile of ISO 8601 [ISO8601] dates SHOULD be used in new protocols on the Internet.
  - *RFC 3339 definieert het datum/tijdformaat dat door het `time` attribuut gebruikt wordt. De bron bevestigt dat RFC 3339 een tijdstempelformaat definieert, maar de specifieke claim dat `time` het tijdstip van logging/registratie betreft (niet de werkelijke gebeurtenis) is een semantische beschrijving die niet in RFC 3339 voorkomt — RFC 3339 gaat uitsluitend over het formaat, niet over de betekenis van specifieke CloudEvents-attributen.*

## UNGROUNDED — geen bron ondersteunt de claim (11)

### `ls-notif-0005` — SKILL.md:57 *(§ Verplichte attributen)*

> Het `id` attribuut is verplicht: een unieke event-identifier; bij voorkeur een persistent domeinspecifiek ID, anders een UUID (v4). De combinatie `source` + `id` moet globaal uniek zijn.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profiel voor CloudEvents - verplichte attributen

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0006` — SKILL.md:58 *(§ Verplichte attributen)*

> Het `source` attribuut is verplicht en het NL GOV profiel schrijft URN-notatie voor met de `nld` namespace. Formaat: `urn:nld:oin:<OIN>:systeem:<systeemnaam>`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profiel voor CloudEvents - verplichte attributen

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0007` — SKILL.md:59 *(§ Verplichte attributen)*

> Het `specversion` attribuut is verplicht en moet de waarde `"1.0"` hebben.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profiel voor CloudEvents - verplichte attributen

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0008` — SKILL.md:60 *(§ Verplichte attributen)*

> Het `type` attribuut is verplicht en moet in Reverse Domain Name Notation worden opgegeven. Versioning gebeurt met een `v` prefix (bijv. `nl.brp.verhuizing.v2`). Types worden geregistreerd in een centraal register.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profiel voor CloudEvents - verplichte attributen

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0009` — SKILL.md:66 *(§ Optionele attributen)*

> Het optionele attribuut `datacontenttype` geeft het media type van de event data payload aan; JSON (`application/json`) wordt aanbevolen als standaardformaat.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NL GOV profiel voor CloudEvents - optionele attributen

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0012` — SKILL.md:71 *(§ Optionele attributen)*

> `sequence` en `sequencetype` zijn NL GOV extensie-attributen (niet in de CNCF-kernspec). `sequencetype` is verplicht als `sequence` wordt gebruikt.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profiel voor CloudEvents - optionele attributen

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0014` — SKILL.md:104 *(§ Abonneren)*

> Push-model (webhook) is het aanbevolen aflevermodel vanwege lage latency en efficiënter resourcegebruik.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Abonneren - aflevermodellen

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0016` — SKILL.md:122 *(§ Security & Privacy)*

> Context-attributen (zoals `source`, `type`, `subject`) mogen nooit persoonsgegevens of gevoelige informatie bevatten; gebruik hiervoor de versleutelde `data`-payload.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Security & Privacy - CloudEvents NL GOV profiel

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0017` — SKILL.md:123 *(§ Security & Privacy)*

> Wanneer de payload gevoelige gegevens bevat, moet deze versleuteld worden (end-to-end encryptie).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Security & Privacy - CloudEvents NL GOV profiel

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0018` — SKILL.md:124 *(§ Security & Privacy)*

> Alle communicatie tussen bronnen, notificatieservices en afnemers moet plaatsvinden over TLS (minimaal versie 1.2).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Security & Privacy - CloudEvents NL GOV profiel

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

### `ls-notif-0020` — reference.md:50 *(§ Authenticatie en autorisatie)*

> De Notificatieservices API maakt gebruik van JWT Bearer Tokens voor authenticatie. Publicerende systemen hebben een token nodig met de scope `notifications.distribute`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Notificatieservices API - authenticatie

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangeleverde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*

## GROUNDED — minstens één bron ondersteunt de claim (3)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-notif-0022` — reference.md:17 *(§ Type Systeem)*

> Het `time` attribuut gebruikt het Timestamp type conform RFC 3339.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** CloudEvents type systeem

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc3339.txt](https://www.rfc-editor.org/rfc/rfc3339.txt)
  > date-time = full-date "T" full-time [...] This document defines a date and time format for use in Internet protocols that is a profile of the ISO 8601 standard for representation of dates and times using the Gregorian calendar.
  - *RFC 3339 definieert het Timestamp-formaat (date-time) dat gebruikt wordt in Internet protocollen. De claim dat het `time` attribuut het Timestamp type conform RFC 3339 gebruikt is consistent met de inhoud van deze bron, die precies dat formaat specificeert.*

### `ls-notif-0023` — reference.md:16 *(§ Type Systeem)*

> URI-reference is een URI of relatieve referentie conform RFC 3986.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** CloudEvents type systeem

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc3986.txt](https://www.rfc-editor.org/rfc/rfc3986.txt)
  > URI-reference = URI / relative-ref ... A URI-reference is either a URI or a relative reference. If the URI-reference's prefix does not match the syntax of a scheme followed by its colon separator, then the URI-reference is a relative reference.

### `ls-notif-0027` — SKILL.md:42 *(§ Repositories)*

> Het NL GOV profiel voor CloudEvents is gepubliceerd onder CC-BY-4.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL-GOV-profile-for-CloudEvents repository

- **SUPPORTED** (high) — [https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents](https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents)
  > License CC-BY-4.0 license
  - *De GitHub repository pagina vermeldt expliciet 'CC-BY-4.0 license' als licentie voor het NL GOV profiel voor CloudEvents.*
- **SUPPORTED** (high) — [https://logius-standaarden.github.io/NL-GOV-profile-for-CloudEvents](https://logius-standaarden.github.io/NL-GOV-profile-for-CloudEvents)
  > This document is licensed under Creative Commons Attribution 4.0 International Public License
- **SUPPORTED** (high) — [https://logius-standaarden.github.io/CloudEvents-NL-Guidelines](https://logius-standaarden.github.io/CloudEvents-NL-Guidelines)
  > Dit document valt onder de volgende licentie: Creative Commons Attribution 4.0 International Public License
  - *De bron vermeldt expliciet CC BY 4.0, wat overeenkomt met CC-BY-4.0. De claim stelt 'NL GOV profiel voor CloudEvents' maar de bron is de bijbehorende Guidelines — beide vallen onder dezelfde licentie.*
<details><summary>5x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *Aangelevelde brontekst was leeg of onbruikbaar — alleen redirect-melding aanwezig.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De aangeleverde brontekst bevat alleen een redirect-melding en is verder leeg/onbruikbaar.*
- **NOT_FOUND** (medium) — [https://github.com/logius-standaarden/CloudEvents-NL-Guidelines](https://github.com/logius-standaarden/CloudEvents-NL-Guidelines)
  - *De repository heeft een LICENSE-bestand en verwijst naar een 'View license' link, maar de aangeleverde brontekst bevat geen expliciete tekst over de licentiesoort (CC-BY-4.0 of anders). De licentie-inhoud is niet weergegeven in de aangeleverde tekst.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Notificatieservices](https://github.com/logius-standaarden/Notificatieservices)
  - *De bron bevat geen informatie over licenties. De CC-BY-4.0 licentie wordt nergens vermeld in de aangeleverde tekst.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Abonneren](https://github.com/logius-standaarden/Abonneren)
  - *De brontekst gaat over de Abonneren-repository, niet over het NL GOV profiel voor CloudEvents. Er is geen vermelding van CloudEvents of een CC-BY-4.0 licentie in deze bron.*
</details>

</details>
