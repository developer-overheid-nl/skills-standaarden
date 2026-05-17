<!-- markdownlint-disable MD052 MD034 MD013 MD038 -->
# Audit ls-iam — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 12 | 16% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 11 | 15% |
| UNGROUNDED | 24 | 33% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 26 | 36% |

*Geverifieerd met sonnet, 24 calls, $2.7302.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (12)

### `ls-iam-0015` — SKILL.md:98 *(§ Betrouwbaarheidsniveaus (Levels of Assurance))*

> Het OIDC NL GOV profiel definieert drie betrouwbaarheidsniveaus conform de eIDAS-verordening: Laag (Low), Substantieel (Substantial), Hoog (High).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIDC NL GOV profiel - Betrouwbaarheidsniveaus

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron verwijst naar eIDAS LoA-waarden (substantial, high) maar definieert zelf geen drie niveaus (Low/Substantial/High) als eigen definitie. De spec verwijst naar [eIDAS.SAML] Section 3.2 voor de definitie. 'Laag' wordt niet als apart niveau in deze bron geïntroduceerd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over eIDAS-betrouwbaarheidsniveaus in OIDC NL GOV.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OIDC NL GOV profiel niet. eIDAS-betrouwbaarheidsniveaus worden niet gedefinieerd in deze bron.*
</details>

### `ls-iam-0027` — SKILL.md:143 *(§ Architectuurcomponenten)*

> Het AuthZEN NL GOV profiel specificeert een architectuur voor geëxternaliseerde autorisatie met PDP en PEP als kerncomponenten; PAP en PIP komen uit het XACML-referentiemodel.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** AuthZEN NL GOV - Architectuur

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron gaat over het OIDC NL GOV profiel. AuthZEN, PDP, PEP, PAP, PIP en het XACML-referentiemodel worden nergens in de bron genoemd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over AuthZEN NL GOV.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *AuthZEN NL GOV wordt niet behandeld in het OAuth NL profiel.*
</details>

### `ls-iam-0028` — SKILL.md:156 *(§ Evaluation endpoint)*

> Het AuthZEN NL GOV evaluation endpoint is POST /access/v1/evaluation met Content-Type application/json.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** AuthZEN NL GOV - Evaluation endpoint

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *AuthZEN en het evaluation endpoint POST /access/v1/evaluation worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over AuthZEN endpoints.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *AuthZEN evaluation endpoint wordt niet behandeld in het OAuth NL profiel.*
</details>

### `ls-iam-0029` — SKILL.md:163 *(§ Request formaat)*

> Een AuthZEN autorisatieverzoek bestaat uit vier elementen: subject, action, resource en context (optioneel).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** AuthZEN NL GOV - Request formaat

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *AuthZEN autorisatieverzoeken met subject, action, resource en context worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over AuthZEN request formaat.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *AuthZEN autorisatieverzoekformaat wordt niet behandeld in het OAuth NL profiel.*
</details>

### `ls-iam-0030` — SKILL.md:196 *(§ Response formaat)*

> Het PDP retourneert een `decision` (boolean): true voor toestaan, false voor weigeren; optioneel met `context` met aanvullende informatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** AuthZEN NL GOV - Response formaat

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *AuthZEN PDP response met decision (boolean) wordt niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over AuthZEN response formaat.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron gaat over het OAuth 2.0 NL GOV profiel. AuthZEN en PDP response-formaten worden niet behandeld.*
</details>

### `ls-iam-0031` — SKILL.md:223 *(§ Authorization Decision Log)*

> De ADL-werkversie volgt sinds april 2026 een OpenTelemetry-vorm op basis van het AuthZEN-informatiemodel.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Authorization Decision Log

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Authorization Decision Log en OpenTelemetry worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over Authorization Decision Log of OpenTelemetry.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Authorization Decision Log, OpenTelemetry en AuthZEN-informatiemodel worden niet behandeld in deze bron.*
</details>

### `ls-iam-0036` — SKILL.md:234 *(§ Record-velden)*

> Het ADL veld `status` kent drie waarden: `Unset` (default, ook bij denial), `Ok`, of `Error` (PDP kon geen beslissing produceren).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Authorization Decision Log - Record-velden

- **NOT_FOUND** (high) — [https://www.w3.org/TR/trace-context](https://www.w3.org/TR/trace-context)
  - *De W3C Trace Context spec definieert geen statusvelden (Unset, Ok, Error). Dit is OpenTelemetry-terminologie, niet W3C Trace Context. Deze bron behandelt het onderwerp niet.*

### `ls-iam-0048` — reference.md:63 *(§ OIN Structuur)*

> Een OIN bestaat uit 20 cijfers; de eerste 8 identificeren de organisatie, de resterende cijfers zijn een volgnummer.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIN-stelsel - Structuur

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *OIN-structuur (20 cijfers, eerste 8 voor organisatie) wordt niet beschreven in deze bron. De bron vermeldt OIN alleen zijdelings als onderdeel van PKIoverheid certificaten.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over de structuur van een OIN.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *OIN-structuur (20 cijfers, eerste 8 identificeren de organisatie) wordt niet behandeld in deze bron.*
</details>

### `ls-iam-0049` — reference.md:69 *(§ OIN Structuur)*

> In PKIoverheid-certificaten wordt het OIN opgenomen in het `subject.serialNumber` veld.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIN-stelsel - PKIoverheid certificaten

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron vermeldt PKIoverheid certificaten in de context van publieke sleutels (JWK Set, x5c/x5u parameters), maar beschrijft niet dat het OIN in het subject.serialNumber veld wordt opgenomen.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over OIN in PKIoverheid-certificaten.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron vermeldt PKIoverheid certificaten met OIN maar specificeert niet dat het OIN in het subject.serialNumber veld wordt opgenomen.*
</details>

### `ls-iam-0055` — reference.md:163 *(§ Levels of detail)*

> De ADL-standaard definieert vier niveaus van replayability: (1) request+response, (2) + adl.core.policies, (3) + adl.core.information, (4) + adl.core.configuration.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Authorization Decision Log - Levels of detail

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL-standaard en replayability-niveaus worden niet behandeld in deze OIDC NL GOV specificatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over ADL niveaus van replayability.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL-standaard en niveaus van replayability worden niet behandeld in deze bron.*
</details>

### `ls-iam-0069` — SKILL.md:51 *(§ Repositories)*

> OIN-Stelsel vastgestelde versie is v3.0.0, gepubliceerd op gitdocumentatie.logius.nl/publicatie/dk/oin/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIN-Stelsel

<details><summary>7x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Het OIN-Stelsel en versienummers daarvan worden niet behandeld in deze OIDC NL GOV bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth-NL-profiel. Er is geen informatie over het OIN-Stelsel of de versie daarvan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OAuth-NL-profiel](https://logius-standaarden.github.io/OAuth-NL-profiel)
  - *De bron bevat geen informatie over het OIN-Stelsel, versienummers daarvan, of de publicatielocatie ervan.*
- **OUT_OF_SCOPE** (high) — [https://github.com/logius-standaarden/OAuth-NL-profiel](https://github.com/logius-standaarden/OAuth-NL-profiel)
  - *De bron gaat over het OAuth-NL-profiel. OIN-Stelsel is een andere standaard; geen informatie hierover in de brontekst.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/OIDC-NLGOV](https://github.com/logius-standaarden/OIDC-NLGOV)
  - *De bron gaat uitsluitend over OIDC-NLGOV. Het OIN-Stelsel wordt niet vermeld.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OIDC-NLGOV](https://logius-standaarden.github.io/OIDC-NLGOV)
  - *Het OIN-Stelsel wordt in de bron niet als referentie of onderwerp behandeld. De bron noemt OIN alleen in een afkortingenlijst als begrip, maar bevat geen informatie over het OIN-Stelsel als standaard of een vastgestelde versie ervan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/OAuth-Inleiding](https://github.com/logius-standaarden/OAuth-Inleiding)
  - *De brontekst bevat geen informatie over het OIN-Stelsel, versienummers of publicatie-URL's.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OAuth-Inleiding](https://logius-standaarden.github.io/OAuth-Inleiding)
  - *De aangeleverde brontekst bevat alleen navigatie-elementen zonder inhoudelijke tekst over versienummers of publicatie-URLs van het OIN-Stelsel.*
</details>

### `ls-iam-0070` — SKILL.md:47 *(§ Repositories)*

> OAuth-Beheermodel heeft een vastgestelde versie v1.0 maar is gearchiveerd.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth-Beheermodel

<details><summary>8x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Een OAuth-Beheermodel en de archiefstatus daarvan worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron bevat geen informatie over een OAuth-Beheermodel of de archiefstatus daarvan.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OAuth-NL-profiel](https://logius-standaarden.github.io/OAuth-NL-profiel)
  - *De bron vermeldt niets over een OAuth-Beheermodel, een versie v1.0 daarvan, of archivering ervan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/OAuth-NL-profiel](https://github.com/logius-standaarden/OAuth-NL-profiel)
  - *De bron verwijst naar een beheermodel via 'https://gitdocumentatie.logius.nl/publicatie/api/beheermodel/' maar geeft geen versienummer, geen vermelding van v1.0, en geen aanduiding dat het gearchiveerd is.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/OIDC-NLGOV](https://github.com/logius-standaarden/OIDC-NLGOV)
  - *De bron gaat uitsluitend over OIDC-NLGOV. Het OAuth-Beheermodel wordt niet vermeld.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OIDC-NLGOV](https://logius-standaarden.github.io/OIDC-NLGOV)
  - *Het OAuth-Beheermodel wordt in de bron niet genoemd. Er is geen verwijzing naar een beheermodel, een versie v1.0 daarvan, of archiefstatus ervan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/OAuth-Inleiding](https://github.com/logius-standaarden/OAuth-Inleiding)
  - *De brontekst bevat geen informatie over een OAuth-Beheermodel, versienummers of archiveringsstatus.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OAuth-Inleiding](https://logius-standaarden.github.io/OAuth-Inleiding)
  - *De aangeleverde brontekst bevat alleen navigatie-elementen zonder inhoudelijke tekst over het OAuth-Beheermodel of archiefstatus.*
</details>

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (11)

### `ls-iam-0002` — SKILL.md:36 *(§ Versiemodel)*

> Voor nieuwe implementaties wordt OIDC aanbevolen; bestaande SAML-koppelingen blijven ondersteund.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Forum Standaardisatie - Authenticatie-standaarden

- **PARTIALLY_SUPPORTED** (medium) — [https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden](https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden)
  > Deze gecombineerde verplichting van OpenID.NLGov (en de achterliggende internationale standaard OIDC) en SAML zet een transitie in gang met afbouw van SAML en opbouw naar OpenID.NLGov (en de achterliggende internationale standaard OIDC).
  - *De bron bevestigt dat er een transitie loopt van SAML naar OpenID.NLGov, en dat SAML blijft ondersteund. Maar de bron zegt niet expliciet dat OIDC 'aanbevolen' wordt voor nieuwe implementaties; het gaat om een gecombineerde verplichting waarbij serviceproviders mogen kiezen. De strekking klopt deels, maar de formulering 'voor nieuwe implementaties wordt OIDC aanbevolen' staat niet letterlijk in de bron.*
<details><summary>5x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20](https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20)
  - *De bron behandelt OAuth 2.0 en het NL GOV profiel daarvoor. OIDC als aanbeveling voor nieuwe implementaties en SAML-ondersteuning worden niet besproken.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11](https://www.forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11)
  - *OIDC als aanbeveling voor nieuwe implementaties en de status van bestaande SAML-koppelingen worden niet besproken in deze bron. De bron gaat over OAuth 2.0 en het NL Gov profiel daarop.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De spec spreekt niet over aanbevelingen voor nieuwe vs. bestaande implementaties ten opzichte van SAML. Dit is Forum Standaardisatie-beleid, niet de technische spec.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron gaat over het OAuth-NL beheermodel en doet geen uitspraken over aanbevelingen voor OIDC vs SAML voor nieuwe implementaties.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron betreft uitsluitend het OAuth NL profiel. SAML en aanbevelingen voor nieuwe implementaties versus bestaande SAML-koppelingen worden nergens behandeld.*
</details>

### `ls-iam-0004` — SKILL.md:38 *(§ Versiemodel)*

> OAuth-NL-profiel v1.1.0 is vastgesteld door Logius (DEF) maar staat bij het Forum in procedure (intake goedgekeurd 24-09-2025, verkort expertonderzoek loopt).

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth-NL-profiel

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > MIDO programmeringstafel 1.1.0 definitive approved version 03-12-2024
  - *De bron bevestigt dat v1.1.0 definitief is vastgesteld (03-12-2024). De claim over de Forum Standaardisatie-procedure (intake goedgekeurd 24-09-2025, verkort expertonderzoek loopt) staat niet in de bron; die datum ligt ook na de publicatiedatum van het document.*

### `ls-iam-0007` — SKILL.md:62 *(§ Verplichte beveiligingseisen)*

> Implicit grant en Resource Owner Password Credentials zijn expliciet verboden vanwege bekende beveiligingsrisico's.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** OAuth NL profiel - Grant types

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > The Implicit Flow and Hybrid Flow allow tokens to be obtained from the Authorization Endpoint... Therefore, the Implicit Flow and Hybrid flow MUST NOT be used.
  - *Implicit Flow is expliciet verboden (MUST NOT). Resource Owner Password Credentials wordt in deze bron niet genoemd — die claim is dus slechts gedeeltelijk ondersteund.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het beheermodel en bevat geen technische specificaties over verboden grant types.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron noemt de implicit grant in de discovery-voorbeeldresponse (response_types_supported: code, token) maar verbiedt implicit grant en ROPC niet expliciet. Er is geen MUST NOT voor deze grant types te vinden in de normatieve tekst.*

### `ls-iam-0012` — SKILL.md:75 *(§ Client authenticatie)*

> private_key_jwt is verplicht per het OAuth NL profiel als client authenticatiemethode bij het token endpoint.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OAuth NL profiel - Client authenticatie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > Confidential Clients, as defined in Section 4.1, MUST authenticate to the OpenID Provider using either: a JWT assertion as defined by... using only the private_key_jwt method... or mutually authenticated TLS, as specified in [RFC8705].
  - *De bron stelt dat confidential clients MUST authenticeren met private_key_jwt OF mTLS. private_key_jwt is dus niet de enige verplichte methode — mTLS is een gelijkwaardig alternatief. De claim dat private_key_jwt 'verplicht' is als enige methode is daarmee te absoluut.*
- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > Full clients, native clients with dynamically registered keys, and direct access clients as defined above MUST authenticate to the authorization server's token endpoint using a JWT assertion [...] using only the private_key_jwt method
  - *De bron bevestigt dat private_key_jwt verplicht is, maar voegt toe dat tls_client_auth MAY ook worden gebruikt als alternatief. De claim stelt dat private_key_jwt 'verplicht' is zonder alternatief te noemen, wat de bron nuanceert met een MAY voor mTLS.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het beheermodel en bevat geen technische specificaties over client authenticatiemethoden.*

### `ls-iam-0017` — SKILL.md:110 *(§ Verplichte claims in het ID Token)*

> Het ID Token moet minimaal de claims sub, iss, aud, exp, iat en nonce bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token claims

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > iss REQUIRED... aud REQUIRED... sub REQUIRED... nonce REQUIRED... exp, iat, nbf REQUIRED... jti REQUIRED.
  - *De bron bevestigt iss, aud, sub, exp, iat, nonce als verplicht. nbf is ook REQUIRED (niet in de claim). jti is ook REQUIRED (niet in de claim). De claim noemt de minimale set correct maar is niet volledig — de spec vereist ook jti en nbf.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen technische specificaties over verplichte ID Token claims.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron gaat over OAuth access tokens en JWT Bearer tokens, niet over OIDC ID Token claims. De minimale ID Token claim-set is niet in deze bron beschreven.*

### `ls-iam-0020` — SKILL.md:127 *(§ ID Token validatie)*

> Bij ID Token validatie MOET de `iss` claim exact overeenkomen met de `issuer` uit het discovery document.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > iss — The issuer Claim is the Uniform Resource Locater (URL) of the expected Issuer. Identical as in [OpenID.iGov].
  - *De bron bevestigt dat de iss claim de URL van de verwachte issuer moet zijn, maar specificeert niet expliciet dat dit exact moet overeenkomen met de issuer uit het discovery document. De claim is breder dan wat de bron letterlijk zegt.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over ID Token validatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ID Token iss-validatie valt buiten scope van het OAuth NL profiel.*

### `ls-iam-0026` — SKILL.md:133 *(§ ID Token validatie)*

> Bij ID Token validatie MOET `jti` uniek zijn (bewaar voldoende lang om hergebruik te detecteren).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > jti REQUIRED. A unique identifier for the token, which can be used to prevent reuse of the token. The value of jti MUST uniquely identify the ID Token between sender and receiver for at least 12 months.
  - *De bron bevestigt dat jti uniek moet zijn en voor minimaal 12 maanden uniek moet identificeren, maar zegt niets over de verplichting om jti-waarden bij te houden om hergebruik te detecteren (dat is een client-implementatieverplichting die niet expliciet in de bron staat).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over jti-validatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ID Token jti-uniekheid valt buiten scope van het OAuth NL profiel. De bron beschrijft wel jti-uniciteit voor access tokens en client assertions, maar niet voor ID Tokens.*

### `ls-iam-0033` — SKILL.md:229 *(§ Record-velden)*

> Het ADL veld `trace_id` is verplicht: 16 byte hex (32 chars), conform W3C Trace Context, cryptografisch random.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Record-velden

- **PARTIALLY_SUPPORTED** (high) — [https://www.w3.org/TR/trace-context](https://www.w3.org/TR/trace-context)
  > trace-id = 32 HEXDIGLC ; 16 bytes array identifier. All zeroes forbidden
  - *De bron bevestigt dat trace-id 16 byte hex (32 chars) is conform W3C Trace Context. De eis 'cryptografisch random' wordt slechts als aanbeveling beschreven: 'Randomly generated value of trace-id SHOULD be preferred', niet als MUST. De claim stelt het als verplicht vereiste, maar de spec zegt SHOULD. Verder is 'verplicht' in ADL-context (het ADL-veld zelf is verplicht) niet iets wat deze bron kan bevestigen.*

### `ls-iam-0034` — SKILL.md:230 *(§ Record-velden)*

> Het ADL veld `span_id` is verplicht: 8 byte hex (16 chars).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Record-velden

- **PARTIALLY_SUPPORTED** (high) — [https://www.w3.org/TR/trace-context](https://www.w3.org/TR/trace-context)
  > parent-id = 16 HEXDIGLC ; 8 bytes array identifier. All zeroes forbidden
  - *De bron bevestigt dat parent-id (span-id) 8 byte hex (16 chars) is. De claim dat het ADL-veld `span_id` verplicht is, kan deze technische spec niet bevestigen — dat is een ADL-specifieke eis buiten deze bron.*

### `ls-iam-0035` — SKILL.md:231 *(§ Record-velden)*

> Het ADL veld `parent_span_id` is conditioneel verplicht: verplicht bij upstream `traceparent`; alleen weglaatbaar bij root-span.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Record-velden

- **PARTIALLY_SUPPORTED** (medium) — [https://www.w3.org/TR/trace-context](https://www.w3.org/TR/trace-context)
  > If the value of the traceparent field wasn't changed before propagation, tracestate MUST NOT be modified as well.
  - *De bron beschrijft traceparent-propagatie en de rol van parent-id als 'ID of this request as known by the caller', wat het concept van een upstream traceparent en root-span ondersteunt. De specifieke ADL-regel dat parent_span_id verplicht is bij upstream traceparent en weglaatbaar bij root-span staat niet expliciet in deze bron; de bron bevestigt alleen de onderliggende W3C-structuur.*

### `ls-iam-0050` — reference.md:89 *(§ Toegangsbeheer en Scopes)*

> De authorization server MOET controleren of gevraagde scopes geldig zijn, de client geautoriseerd is om ze te vragen, en de resource owner akkoord gaat met de gevraagde scopes.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OAuth 2.0 - Scope-validatie

- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > "Authorization servers SHOULD define and document default scope values that will be used if an authorization request does not specify a requested set of scopes." en "Authorization servers MAY restrict certain scopes from use by dynamically registered systems or public clients."
  - *De bron beschrijft scope-beheer door de authorization server maar formuleert geen expliciete MUST-verplichting dat de server controleert of gevraagde scopes geldig zijn, de client geautoriseerd is, én de resource owner akkoord gaat. Sectie 4.1 zegt wel dat authorization servers alleen toegang mogen verlenen aan hogere scope-niveaus aan clients met toestemming, en dat verzoeken buiten toestemming worden geweigerd: "Client authorization requests containing scopes that are outside their permission MUST be rejected." Dit ondersteunt deels de claim maar dekt niet alle drie genoemde elementen expliciet.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt scope-validatie niet expliciet in de termen van de claim. Scope wordt wel als REQUIRED parameter genoemd maar de validatieplicht voor authorization servers zoals beschreven in de claim staat er niet in.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen technische specificaties over scope-validatie door de authorization server.*

## UNGROUNDED — geen bron ondersteunt de claim (24)

### `ls-iam-0010` — SKILL.md:67 *(§ Token specificaties)*

> Access tokens in JWT-formaat (RFC 9068) zijn verplicht (MUST) per het OAuth NL profiel.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OAuth NL profiel - Token specificaties

- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc9068.txt](https://www.rfc-editor.org/rfc/rfc9068.txt)
  - *RFC 9068 definieert een JWT-profiel voor access tokens, maar bevat geen verwijzing naar een 'OAuth NL profiel' of een verplichting vanuit dat profiel. De bron kan niet bevestigen dat het OAuth NL profiel JWT access tokens verplicht stelt; dat is een claim over het NL profiel zelf, niet over RFC 9068.*

### `ls-iam-0032` — SKILL.md:223 *(§ Authorization Decision Log)*

> Het ADL record-model is transport-onafhankelijk; OTLP wordt aanbevolen, maar elke transport is toegestaan zolang het record de gespecificeerde velden draagt.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Authorization Decision Log - Transport

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL record-model en OTLP transport worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over ADL transport.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL record-model en OTLP transport worden niet behandeld in deze bron.*
</details>

### `ls-iam-0037` — SKILL.md:239 *(§ Record-velden)*

> Een denial (decision: false) in ADL heeft status `Unset`, niet `Error`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Record-velden

- **NOT_FOUND** (high) — [https://www.w3.org/TR/trace-context](https://www.w3.org/TR/trace-context)
  - *De W3C Trace Context spec kent geen concept van 'status Unset bij denial'. Dit is ADL/OpenTelemetry-specifieke semantiek die niet in deze bron staat.*

### `ls-iam-0038` — SKILL.md:253 *(§ attributes.adl.core.*)*

> Source-referenties in ADL horen in `attributes`; een veld MOET in precies één van `attributes` of `body` staan.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - attributes.adl.core.*

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL attributes en body velden worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over ADL attributes.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL attributes/body structuur wordt niet behandeld in deze bron.*
</details>

### `ls-iam-0039` — SKILL.md:264 *(§ attributes.adl.core.*)*

> Aanvullende ADL attribute keys volgen `<vendor>.<area>.<name>`. Onbekende keys MOETEN door consumers worden genegeerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - attributes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL attribute key naamgeving conventies worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over ADL attribute keys.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL attribute key-naamgeving en consumer-gedrag worden niet behandeld in deze bron.*
</details>

### `ls-iam-0040` — SKILL.md:296 *(§ Trace context en ingestion)*

> Alle componenten (PEP, PDP, PIP, PAP) MOETEN W3C Trace Context propageren; trace_id blijft ongewijzigd over organisatiegrenzen, ook bij sampling=0.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Trace context

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron betreft het OIDC NL GOV profiel. W3C Trace Context, PEP/PDP/PIP/PAP componenten en ADL worden niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over W3C Trace Context.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *W3C Trace Context propagatie door PEP/PDP/PIP/PAP wordt niet behandeld in deze bron.*
</details>

### `ls-iam-0041` — SKILL.md:296 *(§ Trace context en ingestion)*

> ADL records worden altijd geproduceerd, ook bij sampling=0 (records worden altijd geproduceerd).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Trace context

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL records en sampling-gedrag vallen buiten de scope van deze OIDC-specificatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over ADL records bij sampling.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL records bij sampling=0 worden niet behandeld in deze bron.*
</details>

### `ls-iam-0042` — SKILL.md:296 *(§ Trace context en ingestion)*

> Ingestion van ADL log records MOET idempotent zijn met `(trace_id, span_id)` of content-hash als sleutel.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Ingestion

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Ingestion van ADL log records wordt niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over idempotente ingestion van ADL records.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Idempotente ingestion van ADL log records wordt niet behandeld in deze bron.*
</details>

### `ls-iam-0044` — reference.md:44 *(§ SAML Implementatiedetails)*

> SAML assertions MOETEN worden ondertekend door de Identity Provider.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** SAML - Security Requirements

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *SAML assertions en ondertekeningsvereisten door Identity Providers worden niet behandeld in deze OIDC-specificatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over SAML assertion signing.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *SAML assertions en ondertekening door de Identity Provider worden niet behandeld in deze bron.*
</details>

### `ls-iam-0045` — reference.md:45 *(§ SAML Implementatiedetails)*

> SAML assertions KUNNEN worden versleuteld voor de Service Provider.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** SAML - Security Requirements

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *SAML assertion-encryptie voor Service Providers valt buiten de scope van deze OIDC-specificatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over SAML assertion encryption.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Versleuteling van SAML assertions wordt niet behandeld in deze bron.*
</details>

### `ls-iam-0046` — reference.md:46 *(§ SAML Implementatiedetails)*

> TLS MOET worden gebruikt voor alle SAML communicatie.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** SAML - Security Requirements

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Hoewel de bron TLS vereist voor OIDC-communicatie, behandelt het geen TLS-vereisten specifiek voor SAML-communicatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over TLS voor SAML.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *TLS voor SAML communicatie specifiek wordt niet behandeld. De bron vereist wel TLS voor OAuth-communicatie, maar niet voor SAML.*
</details>

### `ls-iam-0047` — reference.md:47 *(§ SAML Implementatiedetails)*

> SAML Metadata MOET worden ondertekend en periodiek worden gevalideerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** SAML - Security Requirements

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *SAML Metadata ondertekening en validatie worden niet behandeld in deze OIDC-specificatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over SAML Metadata ondertekening.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *SAML Metadata ondertekening en validatie worden niet behandeld in deze bron.*
</details>

### `ls-iam-0051` — reference.md:96 *(§ Pushed Authorization Requests (PAR))*

> Pushed Authorization Requests (PAR) worden aanbevolen per RFC 9126 voor het OAuth NL profiel.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** OAuth NL profiel - PAR

- **NOT_FOUND** (medium) — [https://www.rfc-editor.org/rfc/rfc9126.txt](https://www.rfc-editor.org/rfc/rfc9126.txt)
  - *RFC 9126 definieert PAR en beschrijft de technische specificatie, maar bevat geen verwijzing naar een 'OAuth NL profiel' of een aanbeveling specifiek voor dat profiel. De claim gaat over een nationaal profiel dat buiten de scope van deze RFC valt.*

### `ls-iam-0053` — reference.md:151 *(§ Client Registratie)*

> Het OIDC NL GOV profiel beveelt dynamische client registratie (RFC 7591) aan ('Clients SHOULD use Dynamic Registration').

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** OIDC NL GOV profiel - Client registratie

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7591.txt](https://www.rfc-editor.org/rfc/rfc7591.txt)
  - *De bron is RFC 7591 zelf (de specificatie voor OAuth 2.0 Dynamic Client Registration). De claim gaat over het OIDC NL GOV profiel dat RFC 7591 aanbeveelt ('Clients SHOULD use Dynamic Registration'). RFC 7591 bevat geen uitspraken over het NL GOV profiel of aanbevelingen vanuit dat profiel — dat is een apart document. De bron is dus niet de juiste bron om deze claim te verifiëren.*

### `ls-iam-0056` — reference.md:176 *(§ Trace context propagatie)*

> Alle componenten (PEP, PDP, PIP, PAP) MOETEN W3C Trace Context propageren en trace-continuïteit over componentgrenzen behouden. De `trace_id` mag NIET binnen een lopende beslissingsflow opnieuw worden gealloceerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Trace context propagatie

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *W3C Trace Context propagatie over componentgrenzen (PEP/PDP/PIP/PAP) en trace_id-allocatieregels worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over W3C Trace Context propagatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *W3C Trace Context propagatie en trace-continuïteit over componentgrenzen worden niet behandeld in deze bron.*
</details>

### `ls-iam-0057` — reference.md:178 *(§ Trace context propagatie)*

> ADL-records zijn accountability records en MOETEN altijd worden geproduceerd, ongeacht sampling. ADL-emitters MOGEN het `sampled`-flag NIET wijzigen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Trace context propagatie

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron gaat over OIDC NL GOV profiel. ADL (Authorization Decision Log), trace context propagatie en sampling-flags worden nergens in de bron behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over ADL-records als accountability records.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL-records als accountability records en sampled-flag beheer worden niet behandeld in deze bron.*
</details>

### `ls-iam-0058` — reference.md:184 *(§ Idempotente ingestion)*

> Ingestion van ADL log records MOET idempotent zijn: re-submission van hetzelfde record MOET niet leiden tot een duplicate persisted record. De idempotency-sleutel is gangbaar `(trace_id, span_id)` of content-hash.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Idempotente ingestion

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Idempotente ingestion van ADL log records en idempotency-sleutels worden niet behandeld in deze OIDC NL GOV bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over idempotente ingestion van ADL records.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Idempotente ingestion van ADL log records wordt niet behandeld in deze bron.*
</details>

### `ls-iam-0059` — reference.md:188 *(§ Cached decisions)*

> Indien een gecachte autorisatiebeslissing toch wordt toegepast, MOET de toepassing een nieuw log record produceren met trace_id en parent_span_id van de nieuwe request en een vers gealloceerde span_id.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Cached decisions

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Gecachte autorisatiebeslissingen en ADL log records voor nieuwe requests komen niet voor in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over gecachte autorisatiebeslissingen.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Gecachte autorisatiebeslissingen en bijbehorende log record vereisten worden niet behandeld in deze bron.*
</details>

### `ls-iam-0060` — reference.md:214 *(§ Retention en Privacy)*

> ADL log records MOETEN minimaal 12 maanden worden bewaard voor audit doeleinden.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Retention

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Retentievereisten voor ADL log records worden niet behandeld in deze OIDC NL GOV bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over retentie van ADL log records.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Retentievereisten voor ADL log records worden niet behandeld in deze bron.*
</details>

### `ls-iam-0061` — reference.md:217 *(§ Retention en Privacy)*

> Persoonlijke identificeerbare informatie (PII) in ADL log records MOET worden beschermd en toegang tot logs MOET worden beperkt tot geautoriseerd personeel.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Privacy

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Hoewel de bron privacy-overwegingen bespreekt, gaat die niet over bescherming van PII in ADL log records of toegangsbeperking tot logs.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De brontekst beschrijft het beheermodel van de OAuth-NL standaard. Er is geen enkele vermelding van Authorization Decision Logs (ADL), PII-bescherming in logs, of toegangsbeperking tot logbestanden.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *PII-bescherming in ADL log records en toegangsbeperking tot logs worden niet behandeld in deze bron.*
</details>

### `ls-iam-0062` — reference.md:220 *(§ Retention en Privacy)*

> Bij het delen van ADL logs voor analyse MOETEN PII worden geanonimiseerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - Privacy

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Anonimisering van PII bij het delen van ADL logs wordt niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De brontekst bevat geen informatie over ADL logs, anonimisering van PII, of het delen van loggegevens voor analyse.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth 2.0 NL GOV profiel. Er is geen vermelding van Authorization Decision Log (ADL) of anonimisering van PII in logs.*
</details>

### `ls-iam-0063` — reference.md:235 *(§ Toegankelijkheidsvalidatie)*

> De IAM-specificaties MOETEN voldoen aan WCAG 2.1 niveau AA voor toegankelijkheid.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** IAM - Toegankelijkheidsvalidatie

- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OAuth-NL-profiel](https://logius-standaarden.github.io/OAuth-NL-profiel)
  - *De brontekst bevat geen enkele verwijzing naar WCAG, toegankelijkheid, of AA-niveaus.*

### `ls-iam-0064` — reference.md:248 *(§ Markdown Linting)*

> Markdown bestanden in IAM repositories MOETEN voldoen aan de markdownlint regels voor consistente opmaak.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** IAM - Markdown Linting

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Markdown linting vereisten voor IAM repositories worden niet behandeld in deze technische specificatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De brontekst gaat over het beheermodel van OAuth-NL en bevat geen vereisten over markdownlint of opmaakregels voor Markdown bestanden.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron bevat geen informatie over markdownlint regels of Markdown opmaak vereisten voor IAM repositories.*
</details>

### `ls-iam-0066` — reference.md:138 *(§ Userinfo Endpoint)*

> De OpenID Provider MOET gebruikers informeren over welke claims worden gedeeld en met welke Relying Parties.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV - Userinfo privacy

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt dataminimalisatie en privacy, maar een expliciete verplichting voor de OpenID Provider om gebruikers te informeren over welke claims worden gedeeld en met welke Relying Parties staat niet in de bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De brontekst bevat geen informatie over OpenID Provider verplichtingen rondom het informeren van gebruikers over gedeelde claims of Relying Parties.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt OAuth 2.0, niet OIDC NL GOV gebruikersinformatie-verplichtingen voor OpenID Providers over het informeren van gebruikers.*
</details>

## GROUNDED — minstens één bron ondersteunt de claim (26)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-iam-0001` — SKILL.md:36 *(§ Versiemodel)*

> OpenID.NLGov (v1.0.1) en SAML zijn beide verplicht ('pas-toe-of-leg-uit') sinds 21-09-2023.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Forum Standaardisatie - Authenticatie-standaarden

- **SUPPORTED** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden](https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden)
  > De Authenticatie-standaarden op de 'Pas toe of leg uit'-lijst van het Forum Standaardisatie bestaan uit: OpenID.NLGov, Nederlands overheidsprofiel op OpenID Connect, versie 1.0.1 SAML, versie 2.0 [...] Datum van besluit 21-09-2023
<details><summary>4x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20](https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20)
  - *De bron gaat uitsluitend over NL GOV Assurance profile for OAuth 2.0. OpenID.NLGov (v1.0.1) en SAML worden niet genoemd, en de datum 21-09-2023 komt niet voor in de bron.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11](https://www.forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11)
  - *De bron behandelt uitsluitend het intakeadvies voor NL Gov Assurance Profile for OAuth 2.0 versie 1.1. OpenID.NLGov (v1.0.1) en SAML worden niet genoemd, laat staan hun verplichtingstatus of de datum 21-09-2023.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron is de technische specificatie zelf (v1.0.1). Publicatie-metadata over 'pas-toe-of-leg-uit'-status of de datum 21-09-2023 staat niet in de spec.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De brontekst betreft het beheermodel van OAuth-NL. SAML en OpenID.NLGov v1.0.1 als gecombineerde vermelding per 21-09-2023 worden niet genoemd.*
</details>

### `ls-iam-0003` — SKILL.md:38 *(§ Versiemodel)*

> OAuth-NL-profiel v1.0 staat op het Forum Standaardisatie als verplicht ('pas-toe-of-leg-uit').

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Forum Standaardisatie - OAuth NL profiel

- **SUPPORTED** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20](https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20)
  > Verplicht ('Pas toe leg uit') [...] NL GOV Assurance Profile for OAuth 2.0 moet worden toegepast bij applicaties waarbij gebruikers of 'resource owners' impliciet of expliciet toestemming geven aan een dienst van een derde om namens deze toegang te krijgen tot gegevens via een REST API
  - *De bron bevestigt de verplichte ('pas-toe-of-leg-uit') status. De versie wordt in de detailinformatie als '15 juli 2019' / 'v1.0' aangeduid; het besluit viel op 09-07-2020.*
- **SUPPORTED** (medium) — [https://www.forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11](https://www.forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11)
  > NL Gov Assurance profile for OAuth 2.0 is 15 juli 2019 opgenomen op de 'Pas toe of leg uit'-lijst van het Forum Standaardisatie.
  - *De bron bevestigt dat het OAuth-NL-profiel op de 'Pas toe of leg uit'-lijst staat, maar noemt expliciet de opnamedatum 15 juli 2019 en verwijst naar v1.0 impliciet (de huidige aanmelding betreft v1.1 als nieuwe versie). De claim spreekt over 'v1.0' wat consistent is met de context, maar de bron specificeert het versienummer van de reeds geplaatste versie niet expliciet als '1.0'.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  > De actuele versie van de OAuth-NL is v1.0. [...] De status van de standaard is 'Verplicht (pas toe leg uit)'. Dit houdt kort gezegd in dat Nederlandse overheden en instellingen uit de (semi) publieke sector verplicht zijn deze standaard toe te passen
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden](https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden)
  - *De bron behandelt uitsluitend de Authenticatie-standaarden (OpenID.NLGov en SAML). Het OAuth-NL-profiel wordt in deze brontekst niet genoemd.*

### `ls-iam-0005` — SKILL.md:61 *(§ Verplichte beveiligingseisen)*

> PKCE is verplicht voor alle clients per het OIDC NL GOV profiel ('Clients MUST use PKCE to protect calls to the Token Endpoint'), inclusief confidential clients die private_key_jwt of mTLS gebruiken — er is geen vrijstelling.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - PKCE

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > Clients MUST use 'Proof Key for Code Exchange' [RFC7636] to protect calls to the Token Endpoint.
  - *De spec maakt geen uitzondering voor confidential clients die private_key_jwt of mTLS gebruiken. De MUST geldt voor alle clients universeel (sectie 4.1).*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het beheermodel van OAuth-NL, geen technische specificatie. PKCE-vereisten worden niet beschreven.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron is het OAuth NL profiel, niet het OIDC NL GOV profiel. PKCE-verplichtingen voor confidential clients in OIDC NL GOV context worden hier niet behandeld. Het OAuth NL profiel verplicht PKCE voor public/native clients en via section 3.1.7 voor de authorization server, maar de specifieke OIDC NL GOV formulering over geen vrijstelling voor confidential clients staat niet in deze bron.*

### `ls-iam-0006` — SKILL.md:62 *(§ Verplichte beveiligingseisen)*

> Grant type `authorization_code` is verplicht (MUST); `client_credentials` is toegestaan (MAY) voor machine-to-machine communicatie.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OAuth NL profiel - Grant types

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > grant_types_supported REQUIRED . JSON array containing the list of OAuth 2.0 grant_type values that the OpenID Provider supports. In the context of this profile, the value MUST be ['authorization_code'].
  - *authorization_code als MUST wordt ondersteund. Echter, client_credentials (MAY voor M2M) wordt in deze OIDC-spec niet vermeld — die scope valt onder de OAuth NL GOV spec. De bron is een OIDC-profiel, niet de OAuth NL profiel.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > The authorization server MUST support the authorization_code , and MAY support the client_credentials grant types as described in Section 2.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het beheermodel en bevat geen technische specificaties over grant types.*

### `ls-iam-0008` — SKILL.md:63 *(§ Verplichte beveiligingseisen)*

> Access tokens worden als HTTP Authorization header (Bearer scheme) meegegeven. Transport via query parameters is verboden (MUST NOT).

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** OAuth NL profiel - Token transport

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > A Protected Resource under this profile MUST NOT accept access tokens passed using the query parameter method.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron bevat geen expliciete bepaling over het verbod op transport van access tokens via query parameters. Dit is OAuth NL GOV profiel-materie, niet terug te vinden in deze OIDC-spec.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het beheermodel en bevat geen technische specificaties over token transport.*

### `ls-iam-0009` — SKILL.md:63 *(§ Verplichte beveiligingseisen)*

> Form-encoded body parameters (RFC 6750 Section 2.2) zijn toegestaan als methode om access tokens mee te sturen.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** OAuth NL profiel - Token transport

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc6750.txt](https://www.rfc-editor.org/rfc/rfc6750.txt)
  > Resource servers MAY support this method.
  - *RFC 6750 Section 2.2 beschrijft de form-encoded body parameter methode en stelt expliciet dat resource servers deze methode MAY ondersteunen, wat overeenkomt met de claim dat deze methode 'toegestaan' is.*

### `ls-iam-0011` — SKILL.md:68 *(§ Token specificaties)*

> Refresh tokens worden ondersteund (MAY) bij de authorization_code flow; refresh token rotation wordt aanbevolen.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** OAuth NL profiel - Refresh tokens

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > OpenID Providers MAY issue Refresh Tokens to Clients; when used, Refresh Tokens MUST be one-time-use or sender-constrained.
  - *MAY voor refresh tokens wordt bevestigd. Rotation wordt indirect ondersteund: 'with every Access Token refresh response the OpenID Provider can issue a new Refresh Token and MUST invalidate the previous Refresh Token'.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > Authorization Servers MAY issue refresh tokens to clients under the following context: [...] This client type MAY request and be issued a refresh token if the security parameters of the access request allow for it.
  - *Refresh token rotation wordt als 'Refresh tokens for public clients must either be sender-constrained or one-time use' aangestipt, wat gedeeltelijk overeenkomt met de aanbeveling voor rotation.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het beheermodel en bevat geen technische specificaties over refresh tokens.*

### `ls-iam-0013` — SKILL.md:76 *(§ Client authenticatie)*

> mTLS (Mutual TLS) is een gelijkwaardig alternatief per het OIDC NL GOV profiel voor client authenticatie bij het token endpoint (MAY per OAuth NL profiel).

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** OAuth NL profiel / OIDC NL GOV - Client authenticatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > Confidential Clients, as defined in Section 4.1, MUST authenticate to the OpenID Provider using either: a JWT assertion as defined by the 'JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants' [RFC7523] using only the private_key_jwt method... or mutually authenticated TLS, as specified in [RFC8705].
  - *mTLS wordt in deze OIDC NL GOV spec als gelijkwaardig alternatief voor private_key_jwt gepresenteerd (beide als MUST-opties). De kwalificatie 'MAY per OAuth NL profiel' kan niet vanuit deze bron worden geverifieerd.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > In addition to private_key_jwt , the client authentication method tls_client_auth [ rfc8705 ] MAY also be used.
  - *De claim verwijst ook naar OIDC NL GOV profiel, maar het OAuth NL profiel bevestigt de MAY-status van mTLS als alternatief voor client authenticatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het beheermodel en bevat geen technische specificaties over mTLS.*

### `ls-iam-0014` — SKILL.md:94 *(§ OpenID Connect NL GOV Profiel)*

> Het OIDC NL GOV profiel bouwt voort op OpenID Connect Core 1.0 en het iGov-profiel.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIDC NL GOV profiel

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > This profile builds on top of, and inherits all properties of, the NL GOV Assurance profile for OAuth 2.0 [OAuth2.NLGov]... This profile is based upon the 'International Government Assurance Profile (iGov) for OpenID Connect 1.0' [OpenID.iGov] as published by the OpenID Foundation. It should be considered a fork of this profile.
  - *Zowel OpenID Connect Core 1.0 (impliciet via iGov en OpenID.Core) als het iGov-profiel worden als basis vermeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron gaat over OAuth-NL beheermodel, niet over het OIDC NL GOV profiel. De relatie met OpenID Connect Core 1.0 en iGov-profiel voor OIDC wordt niet beschreven.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron is het OAuth NL profiel, niet het OIDC NL GOV profiel. Het OIDC NL GOV profiel en zijn relatie tot OpenID Connect Core 1.0 wordt in deze bron niet beschreven.*

### `ls-iam-0016` — SKILL.md:106 *(§ Betrouwbaarheidsniveaus (Levels of Assurance))*

> De `acr_values` parameter in het authentication request mapt naar eIDAS-niveaus. De OpenID Provider geeft het daadwerkelijk bereikte niveau terug in de `acr` claim van het ID Token.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIDC NL GOV profiel - acr_values

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > acr_values OPTIONAL. Lists the acceptable LoAs for this authentication... acr OPTIONAL. The LoA the End-User was authenticated at. MUST be at least the requested Level of Assurance value requested by the Client (either via the acr_values or claims parameters).
  - *Zowel het gebruik van acr_values in het request als het retourneren van het bereikte niveau in de acr claim van het ID Token worden expliciet beschreven.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over acr_values of ID Token claims.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt acr_values en eIDAS-niveaumapping niet.*

### `ls-iam-0018` — SKILL.md:120 *(§ Verplichte claims in het ID Token)*

> De `acr` claim in het ID Token is OPTIONAL per OIDC NL GOV; als gezet MOET de waarde minimaal het gevraagde betrouwbaarheidsniveau zijn.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token acr claim

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > acr OPTIONAL. The LoA the End-User was authenticated at. MUST be at least the requested Level of Assurance value requested by the Client (either via the acr_values or claims parameters) or - if none was requested - a Level of Assurance established through prior agreement.
  - *De bron bevestigt exact: acr is OPTIONAL in het ID Token, maar als gezet MOET de waarde minimaal het gevraagde niveau zijn.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over de acr claim in ID Tokens.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OIDC NL GOV profiel en ID Token acr claim niet.*

### `ls-iam-0019` — SKILL.md:126 *(§ ID Token validatie)*

> Bij ID Token validatie MOET de JWS handtekening worden geverifieerd met de publieke sleutel van de provider (via jwks_uri).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > All Clients MUST validate the signature of an ID Token before accepting it. Validation can be done using the public key of the issuing server, which is published in JSON Web Key (JWK) format... Clients MUST use the public keys obtained from the jwks endpoint to validate the signature on tokens.
  - *Beide vereisten worden expliciet bevestigd: handtekeningverificatie verplicht (MUST) en gebruik van jwks_uri voor de publieke sleutel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over ID Token validatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ID Token validatie valt buiten scope van het OAuth NL profiel dat in deze bron staat.*

### `ls-iam-0021` — SKILL.md:128 *(§ ID Token validatie)*

> Bij ID Token validatie MOET de `aud` claim de `client_id` van de relying party bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > aud — The audience Claim contains the Client ID of the Client. Identical as in [OpenID.iGov].
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over ID Token validatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ID Token aud-validatie valt buiten scope van het OAuth NL profiel.*

### `ls-iam-0022` — SKILL.md:129 *(§ ID Token validatie)*

> Bij ID Token validatie MOET de `nonce` exact overeenkomen met de nonce uit het authorization request.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > nonce — The nonce parameter in the ID Token MUST equal the nonce request parameter sent in the Authentication Request. This is in line with [OpenID.Core], Section 3.1.3.7.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over nonce-validatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ID Token nonce-validatie valt buiten scope van het OAuth NL profiel.*

### `ls-iam-0023` — SKILL.md:130 *(§ ID Token validatie)*

> Bij ID Token validatie MOET `exp` in de toekomst liggen (token niet verlopen).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > exp, iat, nbf — Values for iat and nbf MUST lie in the past and exp MUST lie in the future; the acceptable range for how far away iat is in the past is specific to the Client.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over exp-validatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ID Token exp-validatie valt buiten scope van het OAuth NL profiel.*

### `ls-iam-0024` — SKILL.md:131 *(§ ID Token validatie)*

> Bij ID Token validatie MOET `iat` in het verleden liggen; de acceptabele afstand is per Client te bepalen (OIDC NL GOV laat dit expliciet aan de Client).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > Values for iat and nbf MUST lie in the past and exp MUST lie in the future; the acceptable range for how far away iat is in the past is specific to the Client.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over iat-validatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ID Token iat-validatie valt buiten scope van het OAuth NL profiel.*

### `ls-iam-0025` — SKILL.md:132 *(§ ID Token validatie)*

> Bij ID Token validatie MOET de `acr` minimaal het gevraagde betrouwbaarheidsniveau bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > acr — The Level of Assurance received in the acr Claim is at least the Level of Assurance requested. See also Section 5.2.3. This is in line with [OpenID.Core], Section 3.1.3.7.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen informatie over acr-validatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ID Token acr-validatie valt buiten scope van het OAuth NL profiel.*

### `ls-iam-0043` — reference.md:9 *(§ SAML)*

> SAML is verplicht als onderdeel van de gecombineerde vermelding 'Authenticatie-standaarden (OpenID.NLGov en SAML)' op het Forum Standaardisatie (sinds 21-09-2023).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Forum Standaardisatie - SAML

- **SUPPORTED** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden](https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden)
  > De 'Pas toe of leg uit'-verplichting van de Authenticatie-standaarden bestaat eruit dat aanbieders van identitydiensten [...] zowel OpenID.NLGov [...] als SAML dienen te ondersteunen. [...] Datum van besluit 21-09-2023
<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron is de technische OIDC NL GOV specificatie zelf en bevat geen informatie over Forum Standaardisatie-vermeldingen of gecombineerde opname met SAML.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron vermeldt SAML niet. De bron gaat over het OAuth-NL beheermodel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Forum Standaardisatie-vermelding van SAML en gecombineerde authenticatiestandaarden worden niet behandeld in deze bron.*
</details>

### `ls-iam-0052` — reference.md:144 *(§ Client Registratie)*

> Redirect URI's bij client registratie moeten een exacte match zijn; wildcards zijn niet toegestaan voor beveiliging.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV - Client registratie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > "One of these registered Redirection URI values MUST exactly match the redirect_uri parameter value used in each Authorization Request." en "MUST exactly match one of the Redirection URI values for the Client pre-registered at the OpenID Provider"
  - *De bron bevestigt de exact-match eis. Wildcards worden niet expliciet verboden maar de exact-match eis sluit wildcards impliciet uit.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > "The Authorization Server MUST validate the redirect URI given by the client at the authorization endpoint using strict string comparison." en "Clients MUST NOT allow the redirecting to the local domain."
  - *De bron stelt expliciet dat exacte string-vergelijking vereist is voor redirect URIs. Wildcards worden niet vermeld als toegestaan, en strict string comparison sluit ze impliciet uit.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen technische specificaties over redirect URI matching.*

### `ls-iam-0054` — reference.md:151 *(§ Client Registratie)*

> Voor native clients met per-instance registratie is dynamische client registratie verplicht (MUST); voor web- en browser-applicaties blijft handmatige registratie toegestaan.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - Client registratie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > "In case a native Client is using per-instance registration, the Client MUST use Dynamic Registration." en "In other cases, particularly when dealing with Browser-based applications or Native Apps, Dynamic Registration SHOULD be supported"
  - *De bron bevestigt exact wat de claim stelt: MUST voor native clients met per-instance registratie, en SHOULD (niet verplicht) voor web/browser-applicaties.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > "Native clients MUST either: use dynamic client registration to obtain a separate client id for each instance, or act as a public client by using a common client id and use PKCE [RFC7636] to protect calls to the token endpoint."
  - *De bron stelt dat native clients dynamische registratie MOETEN gebruiken OF als public client met PKCE mogen opereren. De claim stelt dat dynamische registratie verplicht is voor native clients met per-instance registratie, wat klopt. Maar de claim zegt ook dat voor web- en browser-applicaties handmatige registratie toegestaan blijft — dit wordt niet expliciet zo gesteld in de bron; de bron behandelt registratie van web-clients niet als apart onderscheid.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron is het OAuth-NL beheermodel en bevat geen technische specificaties over dynamische client registratie voor native clients.*

### `ls-iam-0065` — reference.md:138 *(§ Userinfo Endpoint)*

> De Relying Party MOET alleen de claims vragen die strikt noodzakelijk zijn voor de dienstverlening (dataminimalisatie).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV - Userinfo privacy

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > All Clients MUST apply the concept of data minimization. As a result, a Client MUST NOT request any more identifiers, attributes or other Claims than strictly necessary.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De brontekst behandelt het beheermodel van OAuth-NL, niet de technische specificaties van OIDC NL GOV. Er is geen vermelding van Relying Party, claims, of dataminimalisatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron is het OAuth 2.0 NL GOV profiel, niet het OIDC NL GOV profiel. Er is geen bepaling over dataminimalisatie voor Relying Parties bij UserInfo claims.*

### `ls-iam-0067` — SKILL.md:45 *(§ Repositories)*

> OIDC-NLGOV vastgestelde versie is v1.0.1, gepubliceerd op gitdocumentatie.logius.nl/publicatie/api/oidc/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIDC-NLGOV

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > OpenID NLGov 1.0.1 Logius Standard Definitive version September 18, 2023 This version: https://gitdocumentatie.logius.nl/publicatie/api/oidc/1.0.1 Latest published version: https://gitdocumentatie.logius.nl/publicatie/api/oidc
- **SUPPORTED** (high) — [https://github.com/logius-standaarden/OIDC-NLGOV](https://github.com/logius-standaarden/OIDC-NLGOV)
  > Deze versie: https://gitdocumentatie.logius.nl/publicatie/api/oidc/1.0.1
<details><summary>6x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron is het OAuth-NL-profiel, niet het OIDC-NLGOV profiel. Er is geen informatie over de versie of publicatielocatie van OIDC-NLGOV.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OAuth-NL-profiel](https://logius-standaarden.github.io/OAuth-NL-profiel)
  - *De bron verwijst naar de NLGOV OpenID specificatie via een URL maar noemt geen versienummer v1.0.1 voor OIDC-NLGOV.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/OAuth-NL-profiel](https://github.com/logius-standaarden/OAuth-NL-profiel)
  - *De brontekst gaat over het OAuth-NL-profiel repository, niet over OIDC-NLGOV. Geen informatie over OIDC-NLGOV versie of publicatielocatie.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OIDC-NLGOV](https://logius-standaarden.github.io/OIDC-NLGOV)
  - *De bron vermeldt geen versienummer 'v1.0.1'. De brontekst verwijst naar de latest published version op gitdocumentatie.logius.nl/publicatie/api/oidc/ en noemt het originele concept als 'version 1.0 in February 2021', maar een vastgesteld versienummer v1.0.1 staat niet in de bron. Publicatie-metadata zoals versienummers staan zelden in de spec zelf.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/OAuth-Inleiding](https://github.com/logius-standaarden/OAuth-Inleiding)
  - *De brontekst is de GitHub-repositorypagina van OAuth-Inleiding en bevat geen informatie over versienummers of publicatie-URL's van OIDC-NLGOV.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OAuth-Inleiding](https://logius-standaarden.github.io/OAuth-Inleiding)
  - *De aangeleverde brontekst bevat alleen navigatie-elementen (Inleiding, Samenvatting, Use Cases, etc.) zonder inhoudelijke tekst over versienummers of publicatie-URLs van OIDC-NLGOV.*
</details>

### `ls-iam-0068` — SKILL.md:44 *(§ Repositories)*

> OAuth-NL-profiel vastgestelde versie is v1.1.0, gepubliceerd op gitdocumentatie.logius.nl/publicatie/api/oauth/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth-NL-profiel

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > NL GOV Assurance profile for OAuth 2.0 v1.1.0 Logius Standard Definitive version December 03, 2024 This version: https://gitdocumentatie.logius.nl/publicatie/api/oauth/v1.1.0/ Latest published version: https://gitdocumentatie.logius.nl/publicatie/api/oauth/
  - *De bron bevestigt expliciet versie v1.1.0 als vastgestelde versie, gepubliceerd op de genoemde URL.*
- **PARTIALLY_SUPPORTED** (medium) — [https://logius-standaarden.github.io/OAuth-NL-profiel](https://logius-standaarden.github.io/OAuth-NL-profiel)
  > Latest published version: https://gitdocumentatie.logius.nl/publicatie/api/oauth/ ... Previous version: https://gitdocumentatie.logius.nl/publicatie/api/oauth/v1.1.0/ ... MIDO programmeringstafel 1.1.0 definitive approved version 03-12-2024
  - *De bron bevestigt dat v1.1.0 een vastgestelde versie is en gepubliceerd op gitdocumentatie.logius.nl/publicatie/api/oauth/. De 'latest published version' URL zonder versienummer suggereert dat er mogelijk een nieuwere versie is dan v1.1.0, maar dat is niet expliciet bevestigd. De publicatielocatie klopt wel.*
- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/OAuth-NL-profiel](https://github.com/logius-standaarden/OAuth-NL-profiel)
  > Versie 1.1.0 - Client credentials Latest Dec 20, 2024
  - *De bron bevestigt dat versie 1.1.0 de laatste release is. De publicatielocatie gitdocumentatie.logius.nl/publicatie/api/oauth/ wordt ook genoemd: 'Bekijk hier de laatste vastgestelde versie van de standaard: https://gitdocumentatie.logius.nl/publicatie/api/oauth/' — daarmee is de claim volledig ondersteund. SUPPORTED zou hier passender zijn, maar de bron bevestigt de versie indirect via de releases-sectie en de URL expliciet.*
<details><summary>5x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron verwijst naar het OAuth NL GOV profiel ([OAuth2.NLGov]) maar noemt geen versienummer v1.1.0. De referentie geeft alleen 'july 2020' en de URL https://gitdocumentatie.logius.nl/publicatie/api/oauth/ zonder versieaanduiding.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/OIDC-NLGOV](https://github.com/logius-standaarden/OIDC-NLGOV)
  - *De bron gaat uitsluitend over OIDC-NLGOV. Het OAuth-NL-profiel wordt niet vermeld.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OIDC-NLGOV](https://logius-standaarden.github.io/OIDC-NLGOV)
  - *De bron verwijst naar het OAuth-NL-profiel via [OAuth2.NLgov] met URL https://gitdocumentatie.logius.nl/publicatie/api/oauth/ en vermeldt 'july 2020' als datum, maar noemt geen versienummer v1.1.0. Versie-informatie van een externe standaard staat niet in deze spec.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/OAuth-Inleiding](https://github.com/logius-standaarden/OAuth-Inleiding)
  - *De brontekst bevat geen informatie over versienummers of publicatie-URL's van het OAuth-NL-profiel.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OAuth-Inleiding](https://logius-standaarden.github.io/OAuth-Inleiding)
  - *De aangeleverde brontekst bevat alleen navigatie-elementen zonder inhoudelijke tekst over versienummers of publicatie-URLs van het OAuth-NL-profiel.*
</details>

### `ls-iam-0071` — reference.md:357 *(§ Aanvullende Bronnen)*

> RFC 7636 definieert PKCE (Proof Key for Code Exchange).

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth - PKCE

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7636.txt](https://www.rfc-editor.org/rfc/rfc7636.txt)
  > Proof Key for Code Exchange by OAuth Public Clients [...] This specification describes the attack as well as a technique to mitigate against the threat through the use of Proof Key for Code Exchange (PKCE, pronounced "pixy").

### `ls-iam-0072` — reference.md:358 *(§ Aanvullende Bronnen)*

> RFC 9068 definieert het JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth - JWT Access Tokens

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc9068.txt](https://www.rfc-editor.org/rfc/rfc9068.txt)
  > This specification defines a profile for issuing OAuth 2.0 access tokens in JSON Web Token (JWT) format.

### `ls-iam-0073` — reference.md:359 *(§ Aanvullende Bronnen)*

> RFC 9126 definieert OAuth 2.0 Pushed Authorization Requests.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth - PAR

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc9126.txt](https://www.rfc-editor.org/rfc/rfc9126.txt)
  > This document defines the pushed authorization request (PAR) endpoint, which allows clients to push the payload of an OAuth 2.0 authorization request to the authorization server via a direct request and provides them with a request URI that is used as reference to the data in a subsequent call to the authorization endpoint.

</details>
