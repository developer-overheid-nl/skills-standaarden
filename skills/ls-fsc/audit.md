<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit ls-fsc — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 31 | 70% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 0 | 0% |
| UNGROUNDED | 11 | 25% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 1 | 2% |
| GROUNDED | 1 | 2% |

*Geverifieerd met sonnet, 15 calls, $0.9454.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (31)

### `ls-fsc-0002` — SKILL.md:29 *(§ Versiemodel)*

> FSC kent twee publicatiekanalen: een vastgestelde versie (DEF) op gitdocumentatie.logius.nl en een werkversie (draft) op logius-standaarden.github.io.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - versiemodel

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0004` — SKILL.md:39 *(§ Repositories)*

> fsc-logging heeft een vastgestelde versie v1.1.0 gepubliceerd op gitdocumentatie.logius.nl/publicatie/fsc/logging/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** fsc-logging

- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/fsc-regulated-area](https://logius-standaarden.github.io/fsc-regulated-area)
  - *Bron status: unsupported*
<details><summary>15x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-core](https://github.com/logius-standaarden/fsc-core)
  - *De brontekst vermeldt 'https://gitdocumentatie.logius.nl/publicatie/fsc/logging/' als publicatielocatie, maar noemt geen versienummer (v1.1.0) of vaststellingsstatus.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-core](https://logius-standaarden.github.io/fsc-core)
  - *De bron is de FSC Core spec en behandelt fsc-logging niet als gepubliceerde standaard met versienummer. Er is alleen een verwijzing: 'It is RECOMMENDED to use FSC Core with the following extensions, each specified in a dedicated RFC: FSC Logging, keep a log of requests to Services.' Geen publicatie-URL of versienummer voor fsc-logging.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-logging](https://github.com/logius-standaarden/fsc-logging)
  - *De brontekst is de GitHub-repositorypagina van fsc-logging en bevat geen versie-informatie, geen release-tags, en geen verwijzingen naar gitdocumentatie.logius.nl/publicatie/fsc/logging/. Publicatie-metadata staat niet in de GitHub repo-indexpagina.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-logging](https://logius-standaarden.github.io/fsc-logging)
  - *De bron vermeldt wel 'Latest published version: https://gitdocumentatie.logius.nl/publicatie/fsc/logging/' maar noemt geen versienummer v1.1.0. Het document is een draft, niet een vastgestelde versie. Versienummer ontbreekt volledig in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-properties](https://github.com/logius-standaarden/fsc-properties)
  - *De bron vermeldt gitdocumentatie.logius.nl/publicatie/fsc/logging/ maar geeft geen versienummer. De claim over versie v1.1.0 kan niet worden geverifieerd.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-properties](https://logius-standaarden.github.io/fsc-properties)
  - *De brontekst gaat over de FSC Properties extension en bevat geen informatie over fsc-logging of enige versie daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-regulated-area](https://github.com/logius-standaarden/fsc-regulated-area)
  - *De brontekst vermeldt de URL https://gitdocumentatie.logius.nl/publicatie/fsc/logging/ maar geeft geen versienummer (v1.1.0) of publicatiedatum.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-external-contract](https://github.com/logius-standaarden/fsc-external-contract)
  - *De brontekst bevat geen informatie over fsc-logging of een versie v1.1.0 daarvan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-external-contract](https://logius-standaarden.github.io/fsc-external-contract)
  - *De bron verwijst naar de Transaction log extensie maar noemt geen versienummer of publicatie-URL voor fsc-logging.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-extensie-template](https://github.com/logius-standaarden/fsc-extensie-template)
  - *De brontekst bevat geen informatie over fsc-logging of versies daarvan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-extensie-template](https://logius-standaarden.github.io/fsc-extensie-template)
  - *De brontekst bevat geen informatie over fsc-logging of versie v1.1.0.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-test-suite](https://github.com/logius-standaarden/fsc-test-suite)
  - *De brontekst maakt geen melding van fsc-logging, een versienummer v1.1.0, of een publicatielocatie. De bron gaat uitsluitend over de FSC Test Suite.*
</details>

### `ls-fsc-0006` — SKILL.md:54 *(§ Stap 1: Contract aanmaken)*

> De consumer maakt een Contract aan met daarin een ServiceConnectionGrant, dat specificeert welke service de consumer wil afnemen en bij welke provider.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - contract flow

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0007` — SKILL.md:58 *(§ Stap 2: Contract ondertekenen door consumer)*

> De consumer ondertekent het contract cryptografisch met zijn eigen certificaat; de handtekening bevat de certificate thumbprint (SHA-256).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - contract ondertekening

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0008` — SKILL.md:62 *(§ Stap 3: Contract verzenden naar provider)*

> Het ondertekende contract wordt via de Manager API (POST /contracts) naar de Manager van de provider gestuurd.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - contract flow

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0009` — SKILL.md:66 *(§ Stap 4: Contract ondertekenen door provider)*

> De provider accepteert een contract via PUT /contracts/{hash}/accept; na ondertekening door provider is het contract geldig en hebben beide partijen een ondertekend exemplaar.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - contract flow

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0010` — SKILL.md:70 *(§ Stap 5: Access token verkrijgen)*

> De consumer vraagt een access token aan bij de Manager van de provider via het OAuth 2.0 Client Credentials grant (grant_type=client_credentials, scope=<GrantHash>, client_id=<PeerID>).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - token aanvraag

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0012` — SKILL.md:82 *(§ Stap 5: Access token verkrijgen)*

> De scope-parameter in de token-aanvraag bevat de hash van het specifieke Grant dat de consumer wil gebruiken.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - token aanvraag

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0013` — SKILL.md:83 *(§ Stap 5: Access token verkrijgen)*

> De client_id in de token-aanvraag is het PeerID van de consumer, afgeleid uit het certificaat.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - token aanvraag

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0014` — SKILL.md:85 *(§ Stap 5: Access token verkrijgen)*

> De Manager valideert de token-aanvraag, controleert of er een geldig contract bestaat met het opgegeven grant, en geeft een JWT access token terug.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Manager tokenuitgifte

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0016` — SKILL.md:101 *(§ Stap 7: Validatie en doorsturen door Inway)*

> De Inway extraheert het JWT uit de Fsc-Authorization header, valideert de handtekening, controleert de claims (aud, svc, gth, gid, cnf), en verifieert dat het certificaat van de verbinding overeenkomt met de cnf thumbprint.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Inway validatie

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0017` — SKILL.md:174 *(§ Access Token (JWT))*

> Het FSC access token bevat de claim sub (PeerID van de consumer), iss (PeerID van de provider), svc (servicenaam), aud (URL van de Inway), gth (Grant Hash), gid (Group ID), cnf (certificate thumbprint), exp en nbf.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - JWT access token claims

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0018` — SKILL.md:184 *(§ Access Token (JWT))*

> De cnf claim bindt het token aan het specifieke certificaat van de consumer via x5t#S256 (SHA-256 thumbprint), waardoor token-diefstal wordt voorkomen (certificate-bound tokens).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - JWT access token

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0019` — SKILL.md:244 *(§ Poorten)*

> FSC definieert poort 443 voor dataverkeer (service-aanroepen tussen Outway en Inway) en poort 8443 voor managementverkeer (contractbeheer, tokenuitgifte, peer-discovery).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - netwerkconfiguratie

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0024` — SKILL.md:260 *(§ Transactie-ID)*

> Elk FSC-verzoek krijgt een uniek transaction_id mee via de Fsc-Transaction-Id HTTP header, doorgegeven door alle componenten in de keten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - logging extensie

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0026` — SKILL.md:284 *(§ Logging per component)*

> De Outway logt uitgaande verzoeken met direction: out; de Inway logt inkomende verzoeken met direction: in. Beide componenten loggen dezelfde transaction_id voor correlatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - logging per component

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0028` — SKILL.md:479 *(§ Inway Error Codes)*

> De Inway retourneert HTTP 401 met ERROR_CODE_ACCESS_TOKEN_MISSING als de Fsc-Authorization header ontbreekt.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Inway error codes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0029` — SKILL.md:480 *(§ Inway Error Codes)*

> De Inway retourneert HTTP 401 met ERROR_CODE_ACCESS_TOKEN_INVALID als de token handtekening ongeldig is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Inway error codes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0030` — SKILL.md:481 *(§ Inway Error Codes)*

> De Inway retourneert HTTP 401 met ERROR_CODE_ACCESS_TOKEN_EXPIRED als het token verlopen is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Inway error codes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0031` — SKILL.md:482 *(§ Inway Error Codes)*

> De Inway retourneert HTTP 403 met ERROR_CODE_WRONG_GROUP_ID_IN_TOKEN als de Group ID in het token niet overeenkomt.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Inway error codes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0032` — SKILL.md:483 *(§ Inway Error Codes)*

> De Inway retourneert HTTP 404 met ERROR_CODE_SERVICE_NOT_FOUND als de service niet geregistreerd is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Inway error codes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0033` — SKILL.md:484 *(§ Inway Error Codes)*

> De Inway retourneert HTTP 502 met ERROR_CODE_SERVICE_UNREACHABLE als de achterliggende service onbereikbaar is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Inway error codes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0034` — SKILL.md:496 *(§ Foutafhandeling)*

> De Outway geeft 405 ERROR_CODE_METHOD_UNSUPPORTED bij een niet-ondersteunde CONNECT methode.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Outway error codes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0035` — SKILL.md:455 *(§ Contract Aanmaken en Ondertekenen (curl))*

> De contract-signatures zijn JWS tokens (RFC7515) die een hash van de contract-content bevatten, ondertekend met het PKIoverheid-certificaat. De JWS payload bevat contract_content_hash, type en signed_at.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - contract ondertekening

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*

### `ls-fsc-0036` — reference.md:11 *(§ Peer)*

> Een Peer is een actor (organisatie) die deelneemt aan het FSC-netwerk en wordt uniek geïdentificeerd door een PeerID, afgeleid uit het subject van het X.509-certificaat.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - architectuur

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0037` — reference.md:15 *(§ Group)*

> Een Group is een logisch systeem van een Peer, bestaande uit een combinatie van Inways, Outways en een Manager. Een Peer kan meerdere Groups hebben voor verschillende omgevingen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - architectuur

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0038` — reference.md:19 *(§ Inway)*

> De Inway is een reverse proxy die inkomende verbindingen van andere Peers afhandelt en het Fsc-Authorization JWT access token valideert voor doorsturen naar de achterliggende service.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Inway component

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0039` — reference.md:29 *(§ Outway)*

> De Outway is een forward proxy die een access token verkrijgt bij de Manager van de aanbieder via OAuth 2.0 Client Credentials en het token toevoegt als Fsc-Authorization header.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Outway component

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0040` — reference.md:39 *(§ Manager)*

> De Manager fungeert als OAuth 2.0 Authorization Server voor het uitgeven van access tokens en beheert contracten (aanmaken, ondertekenen, accepteren, intrekken).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Manager component

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0041` — reference.md:49 *(§ Directory)*

> De Directory is een speciale Manager die als centraal register voor service- en peer-discovery fungeert. Peers publiceren services via een ServicePublicationGrant in een contract.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - Directory component

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0044` — reference.md:78 *(§ Certificate Thumbprints)*

> Contracten bevatten Certificate Thumbprints (SHA-256 hashes van de DER-encoded certificaten) van de ondertekenaars. De thumbprint wordt ook opgenomen in access tokens via de cnf claim.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** FSC - trust model

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

## UNGROUNDED — geen bron ondersteunt de claim (11)

### `ls-fsc-0001` — SKILL.md:23 *(§ Federated Service Connectivity (FSC))*

> FSC is vereist bij Digikoppeling REST-API (v3.0.1+; huidige publicatie v4.0.0); geen afzonderlijke vermelding op het Forum Standaardisatie.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - toepassingsgebied

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *De aangeleverde brontekst bevat alleen een redirect-melding ('Redirecting to v2.0.0'). Inhoudelijke verificatie is niet mogelijk.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0011` — SKILL.md:81 *(§ Stap 5: Access token verkrijgen)*

> De parameter grant_type in de token-aanvraag is altijd client_credentials.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - token aanvraag

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0015` — SKILL.md:89 *(§ Stap 6: Verzoek via Outway naar Inway)*

> Het access token wordt meegegeven in de Fsc-Authorization header als Bearer token bij het HTTP-verzoek van de Outway naar de Inway.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - Outway naar Inway

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0020` — SKILL.md:249 *(§ HTTP-vereisten)*

> HTTP/1.1 is verplicht als minimale versie voor alle FSC-verbindingen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - HTTP-vereisten

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0021` — SKILL.md:250 *(§ HTTP-vereisten)*

> HTTP/2 is optioneel en mag worden ondersteund als aanvulling op HTTP/1.1 bij FSC-verbindingen.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** FSC - HTTP-vereisten

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0022` — SKILL.md:251 *(§ HTTP-vereisten)*

> TLS is verplicht voor FSC-verbindingen; de minimale TLS-versie wordt bepaald door de Group Rules (in de praktijk minimaal TLS 1.2).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - HTTP-vereisten

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0023` — SKILL.md:252 *(§ HTTP-vereisten)*

> mTLS is verplicht voor FSC-verbindingen: zowel client als server presenteren een certificaat.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - HTTP-vereisten

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0025` — SKILL.md:270 *(§ Logvelden)*

> Elk FSC transactielog bevat minimaal de velden transaction_id, direction, grant_hash, source, destination, timestamp en service.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - logging extensie

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0027` — SKILL.md:496 *(§ Foutafhandeling)*

> De Fsc-Error-Code header wordt altijd meegegeven bij foutresponses van de Inway, naast de HTTP status code.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - foutafhandeling

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0042` — reference.md:66 *(§ mTLS met X.509-certificaten)*

> Alle verbindingen tussen FSC-componenten worden beveiligd met mutual TLS (mTLS); beide partijen presenteren een X.509-certificaat en valideren het certificaat van de tegenpartij.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - trust model

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

### `ls-fsc-0043` — reference.md:70 *(§ Trust Anchors)*

> Alle Peers moeten certificaten gebruiken die zijn uitgegeven onder een gedeelde Trust Anchor (root- of intermediate-certificaat).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** FSC - trust model

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
</details>

## KNOWN_DISCREPANCY — gedocumenteerd in conflicts.md (1)

### `ls-fsc-0003` — SKILL.md:38 *(§ Repositories)*

> fsc-core heeft een vastgestelde versie v2.0.0 gepubliceerd op gitdocumentatie.logius.nl/publicatie/fsc/core/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** fsc-core

**Erkend in conflicts.md** *(§ Discrepanties)*: conflicts.md: 'fsc-core: gepubliceerde versie v2.0.0 vs tag 1.1.0-rc'. GitHub-bronnen (logius-standaarden.github.io) tonen een oudere versie; gitdocumentatie.logius.nl is leidend. 'De skill gebruikt versienummers van gitdocumentatie.logius.nl als bron van waarheid voor vastgestelde (DEF) versies.'

- **CONTRADICTED** (high) — [https://logius-standaarden.github.io/fsc-core](https://logius-standaarden.github.io/fsc-core)
  > Latest published version: https://gitdocumentatie.logius.nl/publicatie/fsc/core/ Previous version: https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.1.0/
  - *De bron vermeldt als vorige versie '1.1.0', niet v2.0.0. Er is geen aanwijzing dat v2.0.0 bestaat of gepubliceerd is. De huidige versie in de bron is een draft zonder versienummer, en de enige genoemde gepubliceerde versie is 1.1.0.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/fsc-regulated-area](https://logius-standaarden.github.io/fsc-regulated-area)
  - *Bron status: unsupported*
<details><summary>14x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-core](https://github.com/logius-standaarden/fsc-core)
  - *De brontekst vermeldt alleen de URL 'https://gitdocumentatie.logius.nl/publicatie/fsc/core/' als publicatielocatie, maar geeft geen versienummer (v2.0.0) of vaststellingsstatus. Versie-metadata staat niet in de GitHub-repo-pagina.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-logging](https://github.com/logius-standaarden/fsc-logging)
  - *De aangeleverde brontekst is de GitHub-repositorypagina van fsc-logging, niet fsc-core. Er is geen informatie over fsc-core v2.0.0 of gitdocumentatie.logius.nl/publicatie/fsc/core/ in deze bron.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-logging](https://logius-standaarden.github.io/fsc-logging)
  - *De bron gaat over FSC Logging, niet over FSC Core. Versie-informatie over fsc-core v2.0.0 staat niet in deze tekst.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-properties](https://github.com/logius-standaarden/fsc-properties)
  - *De bron (fsc-properties repo) vermeldt de publicatie-URL gitdocumentatie.logius.nl/publicatie/fsc/core/ maar geeft geen versienummer. De claim over versie v2.0.0 is niet te verifiëren uit deze brontekst.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-properties](https://logius-standaarden.github.io/fsc-properties)
  - *De brontekst gaat over de FSC Properties extension en bevat geen informatie over versies of publicaties van fsc-core.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-regulated-area](https://github.com/logius-standaarden/fsc-regulated-area)
  - *De brontekst vermeldt de URL https://gitdocumentatie.logius.nl/publicatie/fsc/core/ maar geeft geen versienummer (v2.0.0) of publicatiedatum. De bron is de GitHub-repository van fsc-regulated-area, niet van fsc-core zelf.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-external-contract](https://github.com/logius-standaarden/fsc-external-contract)
  - *De brontekst is de GitHub-repositorypagina van fsc-external-contract. Er staat geen informatie over fsc-core of een versie v2.0.0 daarvan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-external-contract](https://logius-standaarden.github.io/fsc-external-contract)
  - *De bron beschrijft FSC External Contract Reference en verwijst naar FSC Core als normatieve basis, maar noemt geen versienummer van FSC Core en bevat geen URL naar gitdocumentatie.logius.nl/publicatie/fsc/core/.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-extensie-template](https://github.com/logius-standaarden/fsc-extensie-template)
  - *De brontekst (GitHub repo fsc-extensie-template) bevat geen informatie over versies van fsc-core of publicaties op gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-extensie-template](https://logius-standaarden.github.io/fsc-extensie-template)
  - *De brontekst behandelt uitsluitend richtlijnen voor het schrijven van FSC-extensies. Er is geen vermelding van fsc-core versienummers of publicatie-URLs.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-test-suite](https://github.com/logius-standaarden/fsc-test-suite)
  - *De brontekst (de FSC Test Suite README op GitHub) vermeldt nergens een versienummer van fsc-core, laat staan een gepubliceerde v2.0.0 op gitdocumentatie.logius.nl. De bron beschrijft alleen de test suite zelf.*
</details>

## GROUNDED — minstens één bron ondersteunt de claim (1)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-fsc-0005` — SKILL.md:42 *(§ Repositories)*

> fsc-external-contract heeft een consultatieversie (CV v1.0.0) gepubliceerd op gitdocumentatie.logius.nl/publicatie/fsc/ext/; nog niet definitief vastgesteld.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** fsc-external-contract

- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/fsc-regulated-area](https://logius-standaarden.github.io/fsc-regulated-area)
  - *Bron status: unsupported*
- **SUPPORTED** (high) — [https://logius-standaarden.github.io/fsc-external-contract](https://logius-standaarden.github.io/fsc-external-contract)
  > FSC - External Contract Reference 1.0.0 Logius Standard Consultation version January 19, 2026 This version: https://gitdocumentatie.logius.nl/publicatie/fsc/ext/1.0.0/ Latest published version: https://gitdocumentatie.logius.nl/publicatie/fsc/ext/
  - *De bron bevestigt dat het om versie 1.0.0 gaat met de status 'Consultation version' (consultatieversie), gepubliceerd op gitdocumentatie.logius.nl/publicatie/fsc/ext/. De statusomschrijving 'This is a proposed recommendation approved by TO' bevestigt dat het nog geen definitief vastgestelde standaard is.*
<details><summary>14x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/core](https://gitdocumentatie.logius.nl/publicatie/fsc/core)
  - *Aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/logging](https://gitdocumentatie.logius.nl/publicatie/fsc/logging)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/fsc/ext](https://gitdocumentatie.logius.nl/publicatie/fsc/ext)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen redirect-melding)*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-core](https://github.com/logius-standaarden/fsc-core)
  - *De brontekst noemt geen 'fsc-external-contract' repository of publicatie. Er is geen verwijzing naar gitdocumentatie.logius.nl/publicatie/fsc/ext/ of een consultatieversie. De vermelde FSC-repositories en publicaties in de bron bevatten dit onderdeel niet.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-core](https://logius-standaarden.github.io/fsc-core)
  - *De bron maakt geen melding van fsc-external-contract, een consultatieversie daarvan, of een publicatie op gitdocumentatie.logius.nl/publicatie/fsc/ext/.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-logging](https://github.com/logius-standaarden/fsc-logging)
  - *De brontekst betreft fsc-logging, niet fsc-external-contract. Er is geen informatie over een consultatieversie of gitdocumentatie.logius.nl/publicatie/fsc/ext/ in deze bron.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-logging](https://logius-standaarden.github.io/fsc-logging)
  - *FSC External Contract wordt niet genoemd in deze brontekst over FSC Logging.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-properties](https://github.com/logius-standaarden/fsc-properties)
  - *De bron vermeldt fsc-external-contract noch de URL gitdocumentatie.logius.nl/publicatie/fsc/ext/ — dit repo behandelt uitsluitend fsc-properties.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-properties](https://logius-standaarden.github.io/fsc-properties)
  - *De brontekst gaat over de FSC Properties extension en bevat geen informatie over fsc-external-contract of enige versie daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-regulated-area](https://github.com/logius-standaarden/fsc-regulated-area)
  - *fsc-external-contract wordt niet genoemd in de brontekst. De FSC-repositories en publicaties die worden opgesomd zijn: fsc-core, fsc-logging, fsc-properties, fsc-regulated-area en fsc-test-suite. Geen verwijzing naar een external-contract extensie of bijbehorende publicatie-URL.*
- **NOT_FOUND** (medium) — [https://github.com/logius-standaarden/fsc-external-contract](https://github.com/logius-standaarden/fsc-external-contract)
  - *De brontekst is de GitHub-repositorypagina van fsc-external-contract en vermeldt 'No releases published'. Er staat geen informatie over een consultatieversie CV v1.0.0 of publicatie op gitdocumentatie.logius.nl. Het ontbreken van releases is consistent met 'nog niet definitief vastgesteld', maar bevestigt de specifieke claim over CV v1.0.0 en de publicatie-URL niet.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-extensie-template](https://github.com/logius-standaarden/fsc-extensie-template)
  - *De brontekst bevat geen informatie over fsc-external-contract of consultatieversies.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/fsc-extensie-template](https://logius-standaarden.github.io/fsc-extensie-template)
  - *De brontekst bevat geen informatie over fsc-external-contract of een consultatieversie CV v1.0.0.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/fsc-test-suite](https://github.com/logius-standaarden/fsc-test-suite)
  - *De brontekst maakt geen melding van fsc-external-contract, een consultatieversie, of een publicatielocatie op gitdocumentatie.logius.nl. De bron gaat uitsluitend over de FSC Test Suite.*
</details>

</details>
