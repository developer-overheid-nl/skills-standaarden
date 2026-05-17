<!-- markdownlint-disable MD052 MD034 MD013 MD038 -->
# Audit ls-fsc — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 4 | 11% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 11 | 29% |
| UNGROUNDED | 2 | 5% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 2 | 5% |
| GROUNDED | 19 | 50% |

*Geverifieerd met sonnet, 10 calls, $0.9168.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (4)

### `ls-fsc-0008` — SKILL.md:42 *(§ Repositories)*

> fsc-external-contract heeft een consultatieversie CV v1.0.0 op gitdocumentatie.logius.nl/publicatie/fsc/ext/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** fsc-external-contract

<details><summary>8x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *fsc-external-contract wordt niet vermeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *De bron behandelt fsc-external-contract niet.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-core](https://github.com/logius-standaarden/fsc-core)
  - *fsc-external-contract wordt in de brontekst niet genoemd. De FSC-repositories en publicaties die worden opgesomd zijn: fsc-core, fsc-logging, fsc-properties, fsc-regulated-area en fsc-test-suite. Geen verwijzing naar een 'ext'-publicatie of consultatieversie.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-core](https://logius-standaarden.github.io/fsc-core)
  - *De bron maakt geen enkele melding van fsc-external-contract, een consultatieversie CV v1.0.0, of de URL gitdocumentatie.logius.nl/publicatie/fsc/ext/.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-logging](https://github.com/logius-standaarden/fsc-logging)
  - *De aangeleverde brontekst bevat geen informatie over fsc-external-contract of een consultatieversie CV v1.0.0.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-logging](https://logius-standaarden.github.io/fsc-logging)
  - *De bron behandelt FSC Logging en verwijst niet naar fsc-external-contract of een consultatieversie daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-properties](https://github.com/logius-standaarden/fsc-properties)
  - *fsc-external-contract wordt in deze brontekst (fsc-properties repository) niet vermeld. Er is geen verwijzing naar een consultatieversie of de URL gitdocumentatie.logius.nl/publicatie/fsc/ext/.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-properties](https://logius-standaarden.github.io/fsc-properties)
  - *De brontekst betreft de FSC Properties extension. Er is geen vermelding van fsc-external-contract, een consultatieversie CV v1.0.0, of de bijbehorende publicatie-URL.*
</details>

### `ls-fsc-0011` — SKILL.md:62 *(§ Stap 3: Contract verzenden naar provider)*

> Het ondertekende contract wordt via de Manager API (POST /contracts) naar de Manager van de provider gestuurd.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC Service Connectivity Flow

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *De bron beschrijft het mechanisme van contractuitwisseling via de Manager maar specificeert het endpoint 'POST /contracts' niet expliciet bij naam. De OpenAPI Specification wordt wel gerefereerd maar niet afgedrukt in de brontekst.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *Manager API POST /contracts is een FSC Core-onderwerp; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *De specifieke Manager API endpoint POST /contracts wordt niet vermeld in deze bron. De bron beschrijft wel contracttransmissie maar noemt geen specifieke endpoints.*
</details>

### `ls-fsc-0012` — SKILL.md:66 *(§ Stap 4: Contract ondertekenen door provider)*

> De provider accepteert het contract via PUT /contracts/{hash}/accept; na ondertekening door beide partijen is het contract geldig.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC Service Connectivity Flow

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *De bron beschrijft het acceptatieproces conceptueel (accept signatures, contract states) maar het specifieke endpoint 'PUT /contracts/{hash}/accept' wordt niet bij naam genoemd in de aangeleverde tekst.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *PUT /contracts/{hash}/accept is een FSC Core-onderwerp; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *De specifieke PUT /contracts/{hash}/accept endpoint wordt niet vermeld in deze bron.*
</details>

### `ls-fsc-0025` — SKILL.md:284 *(§ Logging per component)*

> De Outway logt uitgaande verzoeken met direction: out; de Inway logt inkomende verzoeken met direction: in. Beide gebruiken dezelfde transaction_id voor correlatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC Logging Extensie / logging per component

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Direction-velden (out/in) voor Outway en Inway logging vallen buiten het bereik van fsc-core.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *De bron beschrijft dat zowel Outway als Inway schrijven naar de TransactionLog en dezelfde TransactionID gebruiken, maar de specifieke direction-waarden 'out' en 'in' worden niet vermeld in de brontekst.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *Direction 'out' voor Outway en 'in' voor Inway worden niet beschreven in deze bron. De bron toont alleen DIRECTION_INCOMING in het voorbeeld.*
</details>

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (11)

### `ls-fsc-0003` — SKILL.md:27 *(§ Versiemodel)*

> FSC kent twee publicatiekanalen: een vastgestelde versie (DEF) op gitdocumentatie.logius.nl en een werkversie (draft) op logius-standaarden.github.io.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC versiemodel

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > This is the definitive version of this document. [...] Latest editor's draft: https://logius-standaarden.github.io/fsc-core/
  - *De bron bevestigt het onderscheid definitieve versie (gitdocumentatie.logius.nl) en werkversie (logius-standaarden.github.io). De aanduiding 'DEF' als label wordt niet expliciet gebruikt; de claim over twee kanalen wordt wel ondersteund.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  > This version: https://gitdocumentatie.logius.nl/publicatie/fsc/logging/1.1.0/ Latest published version: https://gitdocumentatie.logius.nl/publicatie/fsc/logging/ Latest editor's draft: https://logius-standaarden.github.io/fsc-logging/
  - *De bron bevestigt indirect het bestaan van beide kanalen (gitdocumentatie.logius.nl voor vastgestelde versie, logius-standaarden.github.io voor werkversie) via de URL-vermeldingen, maar maakt de claim over 'twee publicatiekanalen als DEF/draft' niet expliciet.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > This version: https://gitdocumentatie.logius.nl/publicatie/fsc/ext/1.0.0/ Latest published version: https://gitdocumentatie.logius.nl/publicatie/fsc/ext/ Latest editor's draft: https://logius-standaarden.github.io/fsc-external-contract/
  - *De bron bevestigt de twee URL-patronen (gitdocumentatie.logius.nl voor gepubliceerde versie, logius-standaarden.github.io voor werkversie), maar de termen 'DEF' en 'draft' worden niet expliciet gebruikt. De claim gaat over het algemene FSC versiemodel; deze bron toont het patroon alleen voor fsc-ext.*

### `ls-fsc-0004` — SKILL.md:32 *(§ Versiemodel)*

> FSC heeft vastgestelde versies voor fsc-core en fsc-logging.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC versiemodel

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > FSC - Core 2.0.0 Logius Standard Definitive version April 21, 2026 [...] It is RECOMMENDED to use FSC Core with the following extensions, each specified in a dedicated RFC: FSC Logging, keep a log of requests to Services.
  - *De bron bevestigt een vastgestelde versie voor fsc-core (v2.0.0). Voor fsc-logging vermeldt de bron alleen dat het een extensie is in een 'dedicated RFC', maar geeft geen versiestatus of publicatielocatie van fsc-logging.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  > FSC - Logging 1.1.0 Logius Standard Definitive version April 21, 2026
  - *De bron bevestigt dat fsc-logging een vastgestelde versie heeft (v1.1.0). De claim over fsc-core met een vastgestelde versie wordt niet bevestigd in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *Deze bron gaat over fsc-external-contract, niet over fsc-core of fsc-logging. Er is geen informatie over vastgestelde versies van die modules.*

### `ls-fsc-0015` — SKILL.md:101 *(§ Stap 7: Validatie en doorsturen door Inway)*

> De Inway extraheert het JWT uit de `Fsc-Authorization` header, valideert de handtekening, controleert claims (aud, svc, gth, gid, cnf), verifieert het certificaat via de cnf-thumbprint, en stuurt het verzoek door.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC Inway validatieproces

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > The request MUST be authorized if the access token meets the following conditions: The access token is signed by the same Peer that owns Inway. The access token is used by an Outway that uses the X.509 certificate to which the access token is bound [...] The Service specified in the access token is known to the Inway. The Group ID specified in the claim gid of the access token matches the Group...
  - *De bron bevestigt validatie van handtekening, cnf-thumbprint, svc en gid. De claim noemt ook 'aud' en 'gth' als gevalideerde claims, maar de bron vermeldt deze niet expliciet als validatiecriteria in de Inway-sectie. Gedeeltelijk ondersteund.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *JWT-validatie door de Inway inclusief claims als aud, svc, gth, gid, cnf is een FSC Core-onderwerp.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *Het Inway validatieproces (JWT extractie, claims controle aud/svc/gth/gid/cnf) wordt niet beschreven in deze bron.*

### `ls-fsc-0018` — SKILL.md:244 *(§ Poorten)*

> FSC definieert poort 443 voor dataverkeer (service-aanroepen tussen Outway en Inway) en poort 8443 voor managementverkeer (communicatie tussen Managers en tussen Outways en Managers).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC netwerkconfiguratie

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > The ports used by FSC components MUST be 443 or 8443. Port 443 is RECOMMENDED for data traffic i.e. HTTP requests to a Service. Port 8443 is RECOMMENDED for management traffic i.e. submitting/signing Contracts.
  - *De bron bevestigt poort 443 voor dataverkeer en 8443 voor managementverkeer. De claim zegt 8443 is voor 'communicatie tussen Managers en tussen Outways en Managers', terwijl de bron zegt 'management traffic: Directory, Manager' — Outways worden niet expliciet bij 8443 vermeld. Licht onduidelijk voor het Outway-deel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *Poortconfiguratie (443 en 8443) is een FSC Core-onderwerp; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *Poorten 443 en 8443 worden niet vermeld in deze bron.*

### `ls-fsc-0019` — SKILL.md:249 *(§ HTTP-vereisten)*

> HTTP/1.1 is verplicht als minimale versie voor alle FSC-verbindingen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC netwerkconfiguratie / HTTP-vereisten

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > The Manager MUST support HTTP/1.1[RFC9112]. The Manager MAY support HTTP/2[RFC9113]. The protocol used between the Inway and Outway can be either HTTP/1.1[RFC9112] or HTTP/2[RFC9113].
  - *HTTP/1.1 is verplicht voor de Manager. Voor Inway/Outway kan het HTTP/1.1 of HTTP/2 zijn — MUST voor HTTP/1.1 geldt alleen voor de Manager, niet voor alle FSC-verbindingen als zodanig. De claim zegt 'alle FSC-verbindingen', wat te breed is.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *HTTP/1.1 als minimale versie is een FSC Core-vereiste; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *HTTP/1.1 als minimale versie wordt niet vermeld in deze bron.*

### `ls-fsc-0020` — SKILL.md:250 *(§ HTTP-vereisten)*

> HTTP/2 is optioneel en mag worden ondersteund als aanvulling op HTTP/1.1 in FSC-verbindingen.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** FSC netwerkconfiguratie / HTTP-vereisten

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > The Manager MAY support HTTP/2[RFC9113]. The protocol used between the Inway and Outway can be either HTTP/1.1[RFC9112] or HTTP/2[RFC9113].
  - *Voor de Manager is HTTP/2 optioneel (MAY). Voor Inway/Outway is HTTP/2 een gelijkwaardige optie naast HTTP/1.1. De claim zegt 'als aanvulling op HTTP/1.1', maar de bron presenteert het als alternatief voor Inway/Outway, niet puur als aanvulling.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *HTTP/2 ondersteuning is een FSC Core-onderwerp; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *HTTP/2 wordt niet vermeld in deze bron.*

### `ls-fsc-0021` — SKILL.md:251 *(§ HTTP-vereisten)*

> TLS is verplicht voor alle FSC-verbindingen; de minimale TLS-versie wordt bepaald door de Group Rules (in de praktijk minimaal TLS 1.2).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC netwerkconfiguratie / HTTP-vereisten

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > The TLS versions used between Peers in a Group MUST be defined in the additional Group Rules & Restrictions.
  - *TLS is verplicht en de versie wordt bepaald door Group Rules — dit klopt. De toevoeging 'in de praktijk minimaal TLS 1.2' staat niet in de bron; de bron laat dit open aan de Group.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *TLS-versievereisten zijn een FSC Core-onderwerp; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *TLS-vereisten en minimale TLS-versie worden niet vermeld in deze bron.*

### `ls-fsc-0024` — SKILL.md:270 *(§ Logvelden)*

> Elk FSC transactielog bevat minimaal: transaction_id, direction, grant_hash, source, destination, timestamp en service.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC Logging Extensie

- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  > The fields that a log record MUST contain are described in the OpenAPI Specification
  - *De bron stelt dat de verplichte velden in de OpenAPI Specification staan, maar somt ze niet op in de tekstuele bron. De velden grant_hash, source, destination en service_name worden wel indirect vermeld via de access token mapping (3.1.1), maar timestamp en direction worden niet expliciet als verplichte log record velden benoemd in de tekst.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > "transaction_id" : "019a7dea-9048-7c4d-9e66-4d3f75a18f58" , "direction" : "DIRECTION_INCOMING" , "grant_hash" : "$1$4$+PQI7we01qIfEwq4O5UioLKzjGBgRva6F5+bUfDlKxUjcY5yX1MRsn6NKquDbL8VcklhYO9sk18rHD6La3w/mg" , "source" : {...} , "destination" : {...} , "service_name" : "random_service_name" , "created_at" : 1672527600
  - *Het transactielog voorbeeld toont transaction_id, direction, grant_hash, source, destination, service_name en created_at. De claim noemt 'timestamp' (gedekt door created_at) en 'service' (gedekt door service_name). Alle genoemde velden zijn aanwezig, maar dit is de extensie-spec; de claim stelt dat dit de minimale vereisten zijn in de Logging Extensie zelf (buiten scope van deze bron).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Logging-velden zoals transaction_id, direction, grant_hash, source, destination worden niet beschreven in fsc-core.*

### `ls-fsc-0027` — SKILL.md:455 *(§ Contract Aanmaken en Ondertekenen (curl))*

> JWS signature-waarden (RFC7515) bevatten een hash van de contract-content, ondertekend met het PKIoverheid-certificaat; de JWS payload bevat contract_content_hash, type (accept/reject/revoke) en signed_at.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC contract signatures

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "The JWS Payload as defined in section 2 of [RFC7515], MUST contain a hash of the contract.content as described in the section Content Hash, one of the signature types described in the signature type section and a Unix timestamp of the sign date. JWS Payload example: { "contract_content_hash": "--------", "type": "accept", "signed_at": 1672527600 }"
  - *De bron bevestigt dat de JWS payload contract_content_hash, type (accept/reject/revoke) en signed_at bevat, en dat JWS gebaseerd is op RFC7515. De claim vermeldt echter specifiek 'PKIoverheid-certificaat', terwijl de bron alleen spreekt van X.509-certificaten uitgegeven door de Trust Anchor van de Group — PKIoverheid wordt nergens expliciet genoemd.*

### `ls-fsc-0031` — reference.md:15 *(§ Group)*

> Een Group is een logisch systeem van een Peer, bestaande uit een combinatie van Inways, Outways en een Manager. Een Peer kan meerdere Groups hebben.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC architectuur / Group

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "Group: System of Peers using Inways, Outways and Managers that confirm to the FSC specification to make use of each other's Services." en "Organizations can participate in multiple Groups at the same time."
  - *De bron beschrijft een Group als een systeem van meerdere Peers (niet één Peer), en bevestigt dat een organisatie in meerdere Groups kan participeren. De claim stelt echter dat een Group bestaat uit 'een combinatie van Inways, Outways en een Manager' van één Peer — dat is een onjuiste weergave. Een Group omvat meerdere Peers, elk met eigen componenten. De claim 'Een Peer kan meerdere Groups hebben' is correct ondersteund.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *De definitie van een Group is een FSC Core-onderwerp; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *Het concept Group (combinatie van Inways, Outways en Manager) wordt niet gedefinieerd in deze bron, al wordt 'gid' (Group ID) wel gebruikt in het JWT voorbeeld.*

### `ls-fsc-0038` — reference.md:78 *(§ Certificate Thumbprints)*

> Contracten bevatten Certificate Thumbprints (SHA-256 hashes van DER-encoded certificaten) van de ondertekenaars; de thumbprint wordt ook opgenomen in access tokens via de `cnf` claim.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC trust model / Certificate Thumbprints

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "Public Key thumbprints are used in FSC contracts [...] Certificate thumbprints are used in the certificate-bound access tokens section 3 of [RFC8705]. [...] The cnf.x5t#S256 claim MUST contain the certificate thumbprint of the X.509 certificate provided by the client requesting the token"
  - *De bron bevestigt dat access tokens certificate thumbprints bevatten via de cnf claim (x5t#S256). Echter: de claim stelt dat contracten 'Certificate Thumbprints (SHA-256 hashes van DER-encoded certificaten)' bevatten — dit is onjuist. De bron stelt expliciet dat contracten Public Key Thumbprints gebruiken (niet Certificate Thumbprints), zodat certificaatvernieuwing zonder sleutelrotatie het contract niet ongeldig maakt. Dit is een gedeeltelijke tegenstelling voor het contract-gedeelte van de claim.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > "cnf" : { "x5t#S256" : "06QekfpQ2IkYWhXyZqz3T1llvPEqDYYO0UyETSr7QdU" }
  - *De bron bevestigt dat de cnf claim met x5t#S256 thumbprint in access tokens wordt opgenomen. Het deel over Certificate Thumbprints in contracten zelf (SHA-256 hashes van DER-encoded certificaten van ondertekenaars) wordt niet beschreven in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *Certificate Thumbprints in contracten en de cnf-claim in access tokens zijn FSC Core-onderwerpen. De Logging-bron vermeldt accessToken.gth als grant_hash mapping maar behandelt thumbprints in contracten of cnf-claim niet.*

## UNGROUNDED — geen bron ondersteunt de claim (2)

### `ls-fsc-0002` — SKILL.md:23 *(§ Federated Service Connectivity (FSC))*

> FSC is vereist bij Digikoppeling REST-API (v3.0.1+; huidige publicatie v4.0.0).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Digikoppeling REST-API / FSC

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Deze bron is de FSC Core spec zelf; zij bevat geen verwijzingen naar Digikoppeling REST-API of versievereisten daarbinnen.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *De bron beschrijft FSC Logging; Digikoppeling REST-API vereisten staan hier niet in.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *Digikoppeling REST-API wordt niet genoemd in deze bron.*
</details>

### `ls-fsc-0026` — SKILL.md:399 *(§ Contract Aanmaken en Ondertekenen (curl))*

> De Manager API POST /contracts verwacht `content` (verplicht) en `signature` (JWS string); de Manager berekent en valideert de signature op basis van het certificaat waarmee de mTLS-verbinding is opgezet.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC Manager API / contract aanmaken

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *De bron beschrijft de werking van de Manager API op conceptueel niveau en vermeldt validatieregels voor Contracts en signatures, maar specificeert niet de exacte request body parameters (content + signature) van POST /contracts. De claim dat de Manager de signature valideert op basis van het mTLS-certificaat is deels aantoonbaar (zie signature validatie sectie 4.4.1.3), maar de specifieke API-parameterstructuur staat niet in de brontekst.*

## KNOWN_DISCREPANCY — gedocumenteerd in conflicts.md (2)

### `ls-fsc-0005` — SKILL.md:32 *(§ Versiemodel)*

> fsc-external-contract heeft een consultatieversie (CV); de overige modules (fsc-properties, fsc-regulated-area, fsc-extensie-template) hebben alleen werkversies.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC versiemodel

**Erkend in conflicts.md** *(§ Details fsc-external-contract)*: conflicts.md stelt expliciet: 'Dit is een CV (Consultatieversie), geen DEF-versie — het document is nog niet definitief vastgesteld.' De CONTRADICTED-verdict op de ext-publicatie is dus een gedocumenteerde keuze.

- **CONTRADICTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > This is the definitive version of this document. Edits resulting from consultations have been applied.
  - *De claim stelt dat fsc-external-contract een consultatieversie (CV) heeft, maar de bron is expliciet een 'definitive version' (vastgestelde versie), niet een consultatieversie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *De bron behandelt fsc-external-contract, fsc-properties, fsc-regulated-area en fsc-extensie-template niet.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *De bron behandelt fsc-external-contract, fsc-properties, fsc-regulated-area en fsc-extensie-template niet.*

### `ls-fsc-0006` — SKILL.md:38 *(§ Repositories)*

> fsc-core vastgestelde versie is v2.0.0, gepubliceerd op gitdocumentatie.logius.nl/publicatie/fsc/core/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** fsc-core

**Erkend in conflicts.md** *(§ Details fsc-core)*: conflicts.md: 'Enige tag: 1.1.0-rc ... terwijl de gepubliceerde versie inmiddels v2.0.0 is.' En: 'De gepubliceerde versie op gitdocumentatie.logius.nl is leidend voor DEF-versies.' De CONTRADICTED van logius-standaarden.github.io is hiermee verklaard.

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > FSC - Core 2.0.0 Logius Standard Definitive version April 21, 2026 This version: https://gitdocumentatie.logius.nl/publicatie/fsc/core/2.0.0/ Latest published version: https://gitdocumentatie.logius.nl/publicatie/fsc/core/
- **CONTRADICTED** (high) — [https://logius-standaarden.github.io/fsc-core](https://logius-standaarden.github.io/fsc-core)
  > Previous version: https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.1.0/
  - *De bron vermeldt de vorige gepubliceerde versie als 1.1.0, niet als v2.0.0. De huidige versie in de bron is een draft zonder versienummer. Er is geen aanwijzing dat v2.0.0 bestaat of gepubliceerd is.*
<details><summary>6x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *De bron gaat over fsc-logging, niet over fsc-core. Versie-informatie van fsc-core staat hier niet in.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-core](https://github.com/logius-standaarden/fsc-core)
  - *De brontekst is de GitHub repository-pagina van fsc-core. Er staat geen versienummer (v2.0.0) vermeld. Alleen de publicatie-URL wordt genoemd: 'https://gitdocumentatie.logius.nl/publicatie/fsc/core/' — zonder versieaanduiding.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-logging](https://github.com/logius-standaarden/fsc-logging)
  - *De aangeleverde brontekst betreft de GitHub-repo fsc-logging (CC-BY-4.0 licentietekst en repo-metadata). Er staat geen informatie over fsc-core versienummers of publicatie-URLs.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-logging](https://logius-standaarden.github.io/fsc-logging)
  - *De bron behandelt FSC Logging, niet FSC Core. Er wordt geen versienummer of publicatiestatus van fsc-core vermeld.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-properties](https://github.com/logius-standaarden/fsc-properties)
  - *De brontekst (GitHub repository pagina van fsc-properties) vermeldt de publicatie URL gitdocumentatie.logius.nl/publicatie/fsc/core/ maar geeft geen versienummer. Versie-metadata zoals 'v2.0.0' staat niet in deze bron.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-properties](https://logius-standaarden.github.io/fsc-properties)
  - *De brontekst betreft de FSC Properties extension specificatie. Er wordt nergens gerefereerd aan een versienummer van fsc-core (v2.0.0) of de publicatie-URL van fsc-core.*
</details>

## GROUNDED — minstens één bron ondersteunt de claim (19)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-fsc-0001` — SKILL.md:23 *(§ Federated Service Connectivity (FSC))*

> FSC gebruikt mTLS, OAuth 2.0 client_credentials en cryptografisch ondertekende contracten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC algemeen

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > All connections between Peers leverage mTLS and contracts are cryptographically signed. [...] Access tokens are obtained using the Client Credentials flow section 4,4 of [RFC6749].
  - *De bron bevestigt mTLS, cryptografisch ondertekende contracten én OAuth 2.0 client_credentials flow expliciet.*
- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *Deze bron beschrijft de FSC Logging extensie, niet FSC Core. mTLS, OAuth 2.0 client_credentials en cryptografisch ondertekende contracten zijn FSC Core-onderwerpen die hier niet worden behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *De brontekst (fsc-external-contract extensie) beschrijft delegatie via externe contractreferenties. mTLS, OAuth 2.0 client_credentials en cryptografisch ondertekende contracten worden niet in deze bron behandeld.*

### `ls-fsc-0007` — SKILL.md:39 *(§ Repositories)*

> fsc-logging vastgestelde versie is v1.1.0, gepubliceerd op gitdocumentatie.logius.nl/publicatie/fsc/logging/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** fsc-logging

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  > FSC - Logging 1.1.0 Logius Standard Definitive version April 21, 2026 This version: https://gitdocumentatie.logius.nl/publicatie/fsc/logging/1.1.0/
<details><summary>7x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *De bron vermeldt fsc-logging alleen als aanbevolen extensie, zonder versienummer of publicatielocatie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-core](https://github.com/logius-standaarden/fsc-core)
  - *De brontekst vermeldt wel de publicatie-URL voor fsc-logging ('https://gitdocumentatie.logius.nl/publicatie/fsc/logging/'), maar geen versienummer (v1.1.0).*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-core](https://logius-standaarden.github.io/fsc-core)
  - *De bron behandelt alleen FSC Core. FSC Logging wordt enkel kort vermeld als aanbevolen extensie ('FSC Logging, keep a log of requests to Services'), maar er is geen informatie over versienummers of publicatie-URL's van fsc-logging.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-logging](https://github.com/logius-standaarden/fsc-logging)
  - *De aangeleverde brontekst bevat alleen de GitHub-repo pagina van fsc-logging met licentietekst en algemene repo-metadata. Versienummers of publicatie-URLs voor fsc-logging staan niet in de aangeleverde tekst.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-logging](https://logius-standaarden.github.io/fsc-logging)
  - *De bron vermeldt wel de URL gitdocumentatie.logius.nl/publicatie/fsc/logging/ als 'Latest published version', maar noemt geen versienummer (v1.1.0). Publicatiemetadata met specifieke versienummers staat niet in de spec zelf.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-properties](https://github.com/logius-standaarden/fsc-properties)
  - *De brontekst vermeldt de publicatie URL gitdocumentatie.logius.nl/publicatie/fsc/logging/ maar geeft geen versienummer. Versie 'v1.1.0' wordt nergens in de bron genoemd.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-properties](https://logius-standaarden.github.io/fsc-properties)
  - *De brontekst betreft de FSC Properties extension. Er is geen vermelding van fsc-logging, versie v1.1.0, of een publicatie-URL voor logging.*
</details>

### `ls-fsc-0009` — SKILL.md:54 *(§ Stap 1: Contract aanmaken)*

> De consumer maakt een Contract aan met daarin een ServiceConnectionGrant dat specificeert welke service de consumer wil afnemen en bij welke provider.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC Service Connectivity Flow

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > The Service consumer creates a Contract with a Service Connection Grant. This Grant contains the details of the Service and the consumer.
- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > The Manager of the API consumer creates a ServiceConnectionGrant containing the Property delegation.connection.external_contract_reference ... Contract Transmission : The Manager of the API consumer creates a Contract containing the ServiceConnectionGrant and transmits it to the Manager of the API provider.
  - *De bron beschrijft de ServiceConnectionGrant in de context van de External Contract extensie. De kern van de claim (consumer maakt Contract met ServiceConnectionGrant aan) wordt bevestigd, al is dit de delegatie-variant.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *Contracts en ServiceConnectionGrants zijn FSC Core-onderwerpen; de Logging-extensiebron behandelt dit niet.*

### `ls-fsc-0010` — SKILL.md:58 *(§ Stap 2: Contract ondertekenen door consumer)*

> De consumer ondertekent het contract cryptografisch met zijn eigen certificaat; de handtekening bevat de certificate thumbprint (SHA-256).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC Service Connectivity Flow

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > The JWS MUST specify the certificate thumbprint of the keypair used to create the digital signature using the x5t#S256 section 4.1.8 of [RFC7515] field of the JOSE Header [...] Within FSC both Certificate thumbprints and Public Key thumbprints uses the sha256 thumbprint.
- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > "cnf" : { "x5t#S256" : "06QekfpQ2IkYWhXyZqz3T1llvPEqDYYO0UyETSr7QdU" }
  - *De bron toont de cnf/x5t#S256 thumbprint in het access token voorbeeld, maar beschrijft niet expliciet dat de consumer het contract cryptografisch ondertekent met zijn certificaat. De signing van het contract zelf wordt niet beschreven in deze extensie-spec.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *Cryptografisch ondertekenen van contracten met certificate thumbprint is een FSC Core-onderwerp.*

### `ls-fsc-0013` — SKILL.md:70 *(§ Stap 5: Access token verkrijgen)*

> De consumer vraagt een access token aan bij de Manager van de provider via OAuth 2.0 Client Credentials grant (grant_type=client_credentials, scope=<GrantHash>, client_id=<PeerID>).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC Service Connectivity Flow / token aanvraag

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > Access tokens are obtained using the Client Credentials flow section 4,4 of [RFC6749]. [...] GrantHash of a Service Connection grant or Delegated Service Connection grant provided in the scope field. PeerID of the Peer making the request in the client_id field client_credentials in the grant_type field.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *OAuth 2.0 Client Credentials token-aanvraag bij de Manager is een FSC Core-onderwerp.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *OAuth 2.0 Client Credentials grant, grant_type=client_credentials, scope=<GrantHash>, client_id=<PeerID> worden niet beschreven in deze bron.*

### `ls-fsc-0014` — SKILL.md:89 *(§ Stap 6: Verzoek via Outway naar Inway)*

> Het access token wordt meegegeven in de `Fsc-Authorization` header bij verzoeken van de Outway naar de Inway.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC Service Connectivity Flow

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > The Outway MUST include an access token in the HTTP header Fsc-Authorization when proxying the HTTP request to the Inway.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *De `Fsc-Authorization` header is een FSC Core-onderwerp. De Logging-bron vermeldt alleen de `Fsc-Transaction-Id` header.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *De `Fsc-Authorization` header wordt niet genoemd in deze bron.*

### `ls-fsc-0016` — SKILL.md:170 *(§ Access Token (JWT))*

> Het JWT access token bevat de claims: sub (PeerID consumer), iss (PeerID provider), svc (servicenaam), aud (URL Inway), gth (Grant Hash), gid (Group ID), cnf (x5t#S256 thumbprint), exp en nbf.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC access token (JWT)

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > gth(string): The hash of the Grant [...] gid(string): The ID of the Group sub(string): [...] iss(string): [...] svc(string): Name of the Service aud(string): [...] URI of the Inway providing the Service [...] exp(int): Expiration time [...] nbf(int): Not before [...] cnf(object): x5t#S256(string): The thumbprint of the certificate
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  > accessToken.gth --> logRecord.grant_hash accessToken.sub --> logRecord.source.outway_peer_id accessToken.iss --> logRecord.destination.service_peer_id accessToken.svc --> logRecord.service_name
  - *De bron bevestigt indirect de claims sub, iss, svc en gth door ze als velden uit het access token te benoemen in de logging-mapping. Claims aud, gid, cnf, exp en nbf worden in deze bron niet vermeld.*
- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > "gid" : "fsc.group.example.id" , "gth" : "$1$3$n4kellB6p2..." , "sub" : "12345678901234567890" , "iss" : "12345678901234567891" , "svc" : "test" , "aud" : "https://inway.organization-b.open-fsc.localhost:443" , "exp" : 1493726400 , "nbf" : 1493722800 , "cnf" : { "x5t#S256" : "06QekfpQ2IkYWhXyZqz3T1llvPEqDYYO0UyETSr7QdU" }
  - *Het JWT voorbeeld in de bron bevat alle genoemde claims (sub, iss, svc, aud, gth, gid, cnf, exp, nbf). Echter bevat het ook de prp claim die de claim niet noemt. De claim is inhoudelijk correct voor de genoemde claims.*

### `ls-fsc-0017` — SKILL.md:184 *(§ Access Token (JWT))*

> De `cnf` claim bindt het token aan het specifieke certificaat van de consumer, waardoor token-diefstal wordt voorkomen (certificate-bound tokens).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC access token / certificate binding

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > The access token is a certificate-bound access token as specified in section 3 of [RFC8705] [...] cnf(object): x5t#S256(string): The thumbprint of the certificate that is allowed to use the access token.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *Certificate-bound tokens via de cnf-claim zijn een FSC Core-onderwerp; de Logging-bron behandelt dit niet inhoudelijk.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *De bron toont de cnf claim in het JWT voorbeeld maar beschrijft niet expliciet het doel van certificate binding of het voorkomen van token-diefstal.*

### `ls-fsc-0022` — SKILL.md:252 *(§ HTTP-vereisten)*

> mTLS is verplicht: zowel client als server presenteren een certificaat bij FSC-verbindingen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC netwerkconfiguratie / HTTP-vereisten

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > Connections between Inways, Outways, Managers of a Group are mTLS connections based on X.509 certificates [...] The Outway MUST use mTLS when connecting to Inways [...] The Inway MUST only accept connections from Outways using mTLS [...] The Manager MUST only accept mTLS connections from other external Managers
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *mTLS-verplichting is een FSC Core-onderwerp; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *mTLS als verplichting wordt niet beschreven in deze bron.*

### `ls-fsc-0023` — SKILL.md:260 *(§ Transactie-ID)*

> Elk FSC-verzoek krijgt een uniek transaction_id mee via de `Fsc-Transaction-Id` HTTP header, dat door alle componenten wordt doorgegeven.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC Logging Extensie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  > The Outway will generate a unique ID for the Transaction and write a record to the TransactionLog before proxying the request to the Inway. [...] The Outway proxies the request to the Inway and includes the TransactionID in the HTTP header Fsc-Transaction-Id. The Inway reads the unique ID from the request.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *De FSC Logging extensie en Fsc-Transaction-Id header worden niet beschreven in deze brontekst (fsc-core). De bron verwijst alleen naar FSC Logging als aanbevolen extensie zonder details.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *De `Fsc-Transaction-Id` header wordt niet vermeld in deze bron.*

### `ls-fsc-0028` — SKILL.md:496 *(§ Foutafhandeling)*

> De `Fsc-Error-Code` header wordt altijd meegegeven bij foutresponses van de Inway, naast de HTTP status code.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC Inway foutafhandeling

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "In case of an error within the scope of FSC these components MUST return the HTTP header Fsc-Error-Code which MUST contain the code specifying the error."
  - *De bron vermeldt dit voor Inway en Outway (beide hebben een 'single endpoint which proxies HTTP requests'). Sectie 4.7.2.2 bevestigt specifiek voor de Inway de verplichting tot het foutafhandelingsformaat.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *De bron introduceert foutcodes voor Inway (TRANSACTION_LOG_WRITE_ERROR, INVALID_LOG_RECORD_ID, MISSING_LOG_RECORD_ID) maar vermeldt de `Fsc-Error-Code` header niet expliciet als verplichte header bij foutresponses.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *De `Fsc-Error-Code` header wordt niet vermeld in deze bron.*

### `ls-fsc-0029` — SKILL.md:496 *(§ Foutafhandeling)*

> De Outway geeft HTTP 405 met ERROR_CODE_METHOD_UNSUPPORTED bij een niet-ondersteunde CONNECT methode.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC Outway foutafhandeling

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "ERROR_CODE_METHOD_UNSUPPORTED 405 The Outway received a request with an HTTP Method that is not supported. The CONNECT method is not supported."
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *HTTP 405 met ERROR_CODE_METHOD_UNSUPPORTED is een FSC Core-foutcode voor de Outway; de Logging-bron introduceert andere Outway-foutcodes maar niet deze.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *HTTP 405 en ERROR_CODE_METHOD_UNSUPPORTED worden niet vermeld in deze bron.*

### `ls-fsc-0030` — reference.md:11 *(§ Peer)*

> Een Peer wordt uniek geïdentificeerd door een PeerID, afgeleid uit het subject van het X.509-certificaat dat de Peer gebruikt voor mTLS-verbindingen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC architectuur / Peer

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "Each Peer MUST have a unique identifier within the Group, this identifier is called the PeerID. The PeerID is determined by at least one element from the subject field section 4.1.2.6 of [RFC5280] of an X.509 certificate."
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *PeerID en X.509-certificaat-afleiding zijn FSC Core-onderwerpen; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *PeerID en de afleiding ervan uit het X.509-certificaat subject worden niet beschreven in deze bron.*

### `ls-fsc-0032` — reference.md:19 *(§ Inway)*

> De Inway is een reverse proxy die inkomende verbindingen van andere Peers afhandelt, het Fsc-Authorization JWT valideert, en bij succesvolle validatie het verzoek doorstuurt naar de achterliggende service.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC architectuur / Inway

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "The Inway is used by Peers to offer a Service to other Peers. The Inway is a Reverse proxy that handles incoming connections from Outways and routes the request to the correct Service. [...] The Inway MUST validate the access token provided in the HTTP Fsc-Authorization. [...] The Inway MUST proxy the HTTP request to the Service specified in the field svc of the access token."
- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  > The Inway also writes a log record containing the unique ID to its own TransactionLog before proxying the request to the Service.
  - *De bron bevestigt dat de Inway proxying doet naar de service. JWT-validatie en Fsc-Authorization worden niet in deze Logging-bron behandeld; die zijn FSC Core-onderwerpen.*
- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > The Inway MUST include External Contract Reference properties in the Transaction Log records as additional_data when the Logging extension is used.
  - *De bron noemt de Inway alleen in de context van transaction logging. De beschrijving van Inway als reverse proxy die JWT valideert staat niet in deze bron; die is in FSC Core.*

### `ls-fsc-0033` — reference.md:29 *(§ Outway)*

> De Outway is een forward proxy die uitgaande verbindingen beheert: verwerft een access token via OAuth 2.0 Client Credentials bij de Manager van de aanbieder, voegt het toe als Fsc-Authorization header, en stuurt via mTLS naar de Inway.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC architectuur / Outway

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "The Outway is used by Peers to connect to a Service. The Outway functions as a forwarding proxy [...] Access tokens are obtained using the Client Credentials flow section 4,4 of [RFC6749]. [...] The Outway MUST include an access token in the HTTP header Fsc-Authorization when proxying the HTTP request to the Inway. [...] The Outway MUST use mTLS when connecting to Inways with an X.509 certific...
- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  > The Outway will generate a unique ID for the Transaction and write a record to the TransactionLog before proxying the request to the Inway.
  - *De bron bevestigt dat de Outway verzoeken proxiet naar de Inway, maar OAuth 2.0 Client Credentials token-aanvraag en Fsc-Authorization header zijn FSC Core-onderwerpen die hier niet worden behandeld.*
- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > The Outway MUST include External Contract Reference properties in the Transaction Log records as additional_data when the Logging extension is used.
  - *De bron noemt de Outway alleen voor transaction logging. De beschrijving van Outway als forward proxy met OAuth 2.0 token acquisitie staat niet in deze bron.*

### `ls-fsc-0034` — reference.md:39 *(§ Manager)*

> De Manager fungeert als OAuth 2.0 Authorization Server voor het uitgeven van access tokens en beheert het aanmaken, ondertekenen, accepteren en intrekken van Contracts.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC architectuur / Manager

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "The Manager is responsible for: [...] Providing access tokens [...] Receiving Contracts [...] Validating Contracts [...] Receiving Contract signatures (accept, reject, revoke) [...] Validating Contract signatures"
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  > A Peer can request the records of the TransactionLog through the Manager of a Peer. The Manager returns only logs records that involve the Peer requesting the log records.
  - *De bron bevestigt de Manager-rol voor het verstrekken van TransactionLog-records. De OAuth 2.0 Authorization Server-rol en contractbeheer zijn FSC Core-onderwerpen die hier niet worden behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *De Manager als OAuth 2.0 Authorization Server wordt niet beschreven in deze bron. De Manager wordt wel genoemd als component dat Contracts aanmaakt en verzendt.*

### `ls-fsc-0035` — reference.md:49 *(§ Directory)*

> De Directory is een speciale Manager die fungeert als centraal register voor service- en peer-discovery; Peers publiceren hun services via een ServicePublicationGrant in een contract.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC architectuur / Directory

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "The Directory is a Manager chosen by the Group to act as a Directory. The Directory is used by Peers to: Discover Services, Discover Peers, Publish Services, Register themselves" en "Service publication is accomplished by offering a Contract to the Directory which contains one or more (Delegated)ServicePublicationGrants"
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  > The Contract is received by the Peer acting as Directory... Grant Creation : The Manager of the API provider creates a ServicePublicationGrant... Service Publication : The Service is now published in the Directory on behalf of the delegator organization
  - *De bron bevestigt dat de Directory services registreert via ServicePublicationGrants in contracten. De omschrijving van Directory als 'speciale Manager voor service- en peer-discovery' staat niet expliciet in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *De Directory als centraal register en ServicePublicationGrants zijn FSC Core-onderwerpen; niet behandeld in deze Logging-bron.*

### `ls-fsc-0036` — reference.md:66 *(§ mTLS met X.509-certificaten)*

> Alle verbindingen tussen FSC-componenten worden beveiligd met mutual TLS (mTLS); beide partijen presenteren een X.509-certificaat en valideren het certificaat van de tegenpartij.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC trust model / mTLS

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "Connections between Managers, Inways, Outways use Mutual Transport Layer Security (mTLS) with X.509 certificates." en "The Inway MUST only accept connections from Outways using mTLS with an X.509 certificate signed by the chosen TA of the Group."
  - *De bron bevestigt mTLS voor alle componenten. Dat beide partijen het certificaat van de tegenpartij valideren, volgt direct uit de definitie van mTLS en wordt impliciet bevestigd door de eis dat certificaten door de TA ondertekend moeten zijn.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *mTLS-verplichting voor alle verbindingen is een FSC Core-onderwerp; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *mTLS als verplichting voor alle verbindingen tussen FSC-componenten wordt niet beschreven in deze bron.*

### `ls-fsc-0037` — reference.md:70 *(§ Trust Anchors)*

> Alle Peers moeten certificaten gebruiken die zijn uitgegeven onder een gedeelde Trust Anchor.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC trust model / Trust Anchors

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  > "Every Peer in a Group MUST accept the same TA(s) that are defined in the Trust Anchor List defined by the Group." en "Components in the Group are configured to accept the same (Sub-) Certificate Authorities (CA) as defined in the Trust Anchors list (TA)."
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *Trust Anchors en gedeelde CA-vereisten zijn FSC Core-onderwerpen; niet behandeld in deze Logging-bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *Trust Anchors en de verplichting om certificaten onder een gedeelde Trust Anchor te gebruiken worden niet vermeld in deze bron.*

</details>
