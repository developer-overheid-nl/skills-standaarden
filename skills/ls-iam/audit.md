<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit ls-iam — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 8 | 12% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 10 | 15% |
| UNGROUNDED | 29 | 44% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 19 | 29% |

*Geverifieerd met sonnet, 16 calls, $2.1815.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (8)

### `ls-iam-0017` — SKILL.md:98 *(§ Betrouwbaarheidsniveaus (Levels of Assurance))*

> Het OIDC NL GOV profiel definieert drie betrouwbaarheidsniveaus (Laag, Substantieel, Hoog) conform de eIDAS-verordening.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIDC NL GOV profiel - betrouwbaarheidsniveaus

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron definieert geen drie betrouwbaarheidsniveaus (Laag, Substantieel, Hoog) zelf. Het profiel verwijst naar eIDAS LoA-waarden en gebruikt 'substantial' en 'high' als voorbeelden, maar definieert geen drie niveaus als eigen onderdeel van het profiel. De eIDAS-niveaus worden als extern gegeven behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Betrouwbaarheidsniveaus conform eIDAS worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel, niet het OIDC NL GOV profiel. Betrouwbaarheidsniveaus conform eIDAS worden niet gedefinieerd.*
</details>

### `ls-iam-0025` — SKILL.md:139 *(§ AuthZEN NL GOV)*

> Het AuthZEN NL GOV profiel specificeert een architectuur voor geëxternaliseerde autorisatie via een centraal PDP.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** AuthZEN NL GOV profiel

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De brontekst betreft het OIDC NL GOV profiel. AuthZEN wordt nergens in de bron genoemd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *AuthZEN NL GOV profiel wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. AuthZEN en geëxternaliseerde autorisatie via een PDP worden niet besproken.*
</details>

### `ls-iam-0026` — SKILL.md:156 *(§ Evaluation endpoint)*

> Het AuthZEN evaluation endpoint is POST /access/v1/evaluation met Content-Type application/json.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** AuthZEN NL GOV profiel - evaluation endpoint

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *AuthZEN en het evaluation endpoint komen niet voor in deze brontekst.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Het AuthZEN evaluation endpoint wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. Het AuthZEN evaluation endpoint wordt niet besproken.*
</details>

### `ls-iam-0027` — SKILL.md:163 *(§ Request formaat)*

> Een AuthZEN autorisatieverzoek bestaat uit vier elementen: subject, action, resource en context (optioneel).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** AuthZEN NL GOV profiel - request formaat

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *AuthZEN autorisatieverzoekformaat (subject, action, resource, context) wordt niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *AuthZEN autorisatieverzoek-elementen worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. AuthZEN autorisatieverzoeken worden niet besproken.*
</details>

### `ls-iam-0028` — SKILL.md:197 *(§ Response formaat)*

> Het PDP retourneert een `decision` (boolean: true voor toestaan, false voor weigeren) en optioneel een `context` met aanvullende informatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** AuthZEN NL GOV profiel - response formaat

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *PDP-responses en het AuthZEN decision-formaat komen niet voor in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *AuthZEN PDP response formaat wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. AuthZEN PDP responses worden niet besproken.*
</details>

### `ls-iam-0029` — SKILL.md:223 *(§ Authorization Decision Log)*

> De ADL-werkversie volgt sinds april 2026 een OpenTelemetry-vorm op basis van het AuthZEN-informatiemodel.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Authorization Decision Log

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL (Authorization Decision Log) en OpenTelemetry worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Authorization Decision Log en OpenTelemetry worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. De ADL-werkversie en OpenTelemetry worden niet besproken.*
</details>

### `ls-iam-0033` — SKILL.md:234 *(§ Record-velden)*

> Het ADL `status` veld kent drie waarden: `Unset` (default, ook bij denial), `Ok`, of `Error` (PDP kon geen beslissing produceren).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Authorization Decision Log - status

- **NOT_FOUND** (high) — [https://www.w3.org/TR/trace-context](https://www.w3.org/TR/trace-context)
  - *De W3C Trace Context spec behandelt geen statuswaarden zoals `Unset`, `Ok` of `Error`. Dit zijn OpenTelemetry-concepten voor span-status, niet gedefinieerd in deze specificatie.*

### `ls-iam-0046` — reference.md:63 *(§ OIN Structuur)*

> Een OIN bestaat uit 20 cijfers waarbij de eerste 8 cijfers de organisatie identificeren en de resterende cijfers een volgnummer zijn.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIN-stelsel - structuur

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron vermeldt OIN niet als afkorting in de glossary, maar geeft geen structuurbeschrijving (20 cijfers, eerste 8 voor organisatie-ID). De OIN-structuur wordt niet behandeld in deze spec.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *OIN-structuur (20 cijfers) wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De structuur van een OIN (20 cijfers, eerste 8 voor organisatie, rest volgnummer) wordt niet beschreven in deze bron.*
</details>

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (10)

### `ls-iam-0008` — SKILL.md:62 *(§ Verplichte beveiligingseisen)*

> Implicit grant en Resource Owner Password Credentials zijn expliciet verboden vanwege bekende beveiligingsrisico's.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** OAuth-NL-profiel - grant types

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > Therefore, the Implicit Flow and Hybrid Flow MUST NOT be used. Also, the IETF OAuth Working Group is removing support for the Implicit Flow from the OAuth 2.1 specification [OAuth2.1] for the same reasons.
  - *De bron verbiedt expliciet de Implicit Flow (MUST NOT). Resource Owner Password Credentials wordt niet expliciet vermeld in de bron. Alleen het Implicit Flow verbod is gedekt.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Implicit grant en Resource Owner Password Credentials worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron noemt implicit grant wel in de discovery response ('response_types_supported': ['code', 'token']) en in de grant_types_supported lijst, maar verbiedt deze grant types niet expliciet. Resource Owner Password Credentials wordt nergens vermeld. Er is geen MUST NOT voor deze grant types.*

### `ls-iam-0015` — SKILL.md:76 *(§ Client authenticatie)*

> mTLS is toegestaan (MAY) per het OAuth NL profiel als gelijkwaardig alternatief voor client authenticatie per het OIDC NL GOV profiel, bij voorkeur met PKIoverheid-certificaat.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** OAuth-NL-profiel / OIDC NL GOV - client authenticatie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > Confidential Clients, as defined in Section 4.1, MUST authenticate to the OpenID Provider using either: a JWT assertion [...] using only the private_key_jwt method [...]; or mutually authenticated TLS, as specified in [RFC8705]. [...] In case PKIoverheid certificates are used, the certificate and entire certificate chain up until the root certificate MUST be included
  - *De bron bevestigt mTLS als toegestaan alternatief (MAY in de zin van een van beide opties). De verwijzing naar PKIoverheid-certificaten staat in de context van public keys/JWK, niet specifiek als voorkeur voor mTLS client authenticatie. 'Bij voorkeur met PKIoverheid-certificaat' voor mTLS client auth is niet expliciet gesteld in de bron.*
- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > In addition to private_key_jwt , the client authentication method tls_client_auth [rfc8705] MAY also be used. [...] In case the Authorization Server, Resource Server and client are not operated under responsibility of the same organisation, each party MUST use PKIoverheid certificates with OIN.
  - *De bron bevestigt dat mTLS (tls_client_auth) MAY worden gebruikt als alternatief, en dat PKIoverheid-certificaten verplicht zijn tussen verschillende organisaties. De claim stelt echter 'bij voorkeur met PKIoverheid-certificaat' als een SHOULD/voorkeur, terwijl de bron PKIoverheid MUST stelt voor cross-organisatie situaties. Bovendien is de gelijkwaardigheid met het OIDC NL GOV profiel niet in deze bron bevestigd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *mTLS als alternatief voor client authenticatie wordt niet besproken in dit beheermodeldocument.*

### `ls-iam-0016` — SKILL.md:94 *(§ OpenID Connect NL GOV Profiel)*

> Het OIDC NL GOV profiel bouwt voort op OpenID Connect Core 1.0 en het iGov-profiel.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIDC NL GOV profiel

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > This profile is based upon the 'International Government Assurance Profile (iGov) for OpenID Connect 1.0' [OpenID.iGov] as published by the OpenID Foundation. It should be considered a fork of this profile [...] This profile builds on top of, and inherits all properties of, the NL GOV Assurance profile for OAuth 2.0 [OAuth2.NLGov].
  - *De bron bevestigt dat het profiel voortbouwt op iGov en op OAuth2.NLGov. OpenID Connect Core 1.0 wordt als basis gebruikt maar de bron zegt het profiel bouwt 'op' het iGov-profiel en OAuth2.NLGov, niet expliciet 'op OpenID Connect Core 1.0' direct. Indirect klopt het wel — iGov zelf bouwt op Core. De claim is grotendeels gedekt.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron beschrijft het OAuth-NL beheermodel, niet het OIDC NL GOV profiel of diens relatie met OpenID Connect Core 1.0 of het iGov-profiel.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron is het OAuth NL profiel. Het OIDC NL GOV profiel en zijn relatie met OpenID Connect Core 1.0 worden hier niet beschreven.*

### `ls-iam-0019` — SKILL.md:110 *(§ Verplichte claims in het ID Token)*

> Het ID Token MOET minimaal de claims sub, iss, aud, exp, iat en nonce bevatten per het OIDC NL GOV profiel.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token claims

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > iss REQUIRED [...] aud REQUIRED [...] sub REQUIRED [...] nonce REQUIRED [...] exp, iat, nbf REQUIRED. The expiration, issued at, and not before timestamps indicate when the token expires, was issued and becomes valid
  - *De bron bevestigt sub, iss, aud, exp, iat en nonce als REQUIRED in het ID Token (sectie 5.2.2). nbf is ook REQUIRED. De claim stelt 'minimaal sub, iss, aud, exp, iat en nonce', wat klopt — al mist de claim nbf en jti (ook REQUIRED per de bron). De genoemde claims zijn allemaal gedekt; de claim is correct maar niet volledig ten opzichte van wat de bron vereist.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *ID Token claims worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. ID Token claims per het OIDC NL GOV profiel komen niet aan bod.*

### `ls-iam-0021` — SKILL.md:124 *(§ ID Token validatie)*

> Bij het valideren van een OIDC ID Token MOETEN de JWS handtekening, iss, aud, nonce, exp, iat, acr en jti worden geverifieerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > All Clients MUST validate the signature of an ID Token before accepting it. Clients MUST verify the following in received ID tokens: iss [...] aud [...] nonce [...] exp, iat, nbf [...] acr [...] represents
  - *De bron bevestigt JWS handtekening, iss, aud, nonce, exp/iat, en acr als te valideren velden. De claim noemt ook 'jti', maar de bron schrijft jti-validatie niet expliciet voor als verificatieplicht voor clients — jti is een REQUIRED veld in het ID Token (voor de OP), maar niet expliciet als client-validatieverplichting opgesomd. nbf wordt wel genoemd maar de claim heeft 'exp, iat' zonder nbf. De claim noemt niet 'represents' terwijl de bron dat wel verplicht stelt.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *ID Token validatie wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. ID Token validatie per OIDC NL GOV profiel wordt niet beschreven.*

### `ls-iam-0024` — SKILL.md:133 *(§ ID Token validatie)*

> De `jti` claim MOET uniek zijn; bewaar voldoende lang om hergebruik te detecteren.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > jti REQUIRED . A unique identifier for the token, which can be used to prevent reuse of the token. The value of jti MUST uniquely identify the ID Token between sender and receiver for at least 12 months.
  - *De bron bevestigt dat jti uniek MOET zijn (minimaal 12 maanden). De claim dat clients jti voldoende lang moeten bewaren om hergebruik te detecteren is impliciet aanwezig maar niet als expliciete client-verplichting geformuleerd — de bron formuleert jti als OP-verplichting bij het aanmaken van het token.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > jti a unique identifier generated by the client for this authentication. This identifier MUST contain at least 128 bits of entropy and MUST NOT be re-used by any subsequent authentication token.
  - *De bron bevestigt de uniciteit van jti en het verbod op hergebruik, maar dit betreft client assertion JWTs (token endpoint), niet ID Token validatie. De claim stelt 'bewaar voldoende lang om hergebruik te detecteren', wat niet expliciet in de bron staat.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *jti claim uniciteit wordt niet besproken in dit beheermodeldocument.*

### `ls-iam-0031` — SKILL.md:229 *(§ Record-velden)*

> Het ADL veld `trace_id` is verplicht en bestaat uit 16 byte hex (32 chars) conform W3C Trace Context, cryptografisch random.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - record-velden

- **PARTIALLY_SUPPORTED** (medium) — [https://www.w3.org/TR/trace-context](https://www.w3.org/TR/trace-context)
  > trace-id = 32 HEXDIGLC ; 16 bytes array identifier. All zeroes forbidden
  - *De bron bevestigt dat trace-id 16 bytes (32 hex chars) is conform W3C Trace Context. De eis van 'cryptografisch random' wordt ondersteund door sectie 8.2: 'Randomly generated value of trace-id SHOULD be preferred', maar dat is een SHOULD, geen MUST. Het ADL-specifieke veld `trace_id` en de verplichting ervan zijn niet in deze bron te vinden — dat is IAM/ADL-specificatie, niet W3C Trace Context.*

### `ls-iam-0045` — reference.md:55 *(§ OIN (Organisatie Identificatie Nummer))*

> Het OIN is opgenomen in het `subject.serialNumber` veld van PKIoverheid-certificaten voor server- en client-authenticatie (mTLS).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIN-stelsel - PKIoverheid-certificaten

- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > In case PKIoverheid certificates are used, the certificate and entire certificate chain up until the root certificate MUST be included as either an x5c or as x5u parameter, according to [RFC7517] Sections 4.6 and 4.7.
  - *De bron vermeldt PKIoverheid-certificaten in de context van JWK-sets voor OIDC, maar zegt niets specifieks over het OIN in het subject.serialNumber veld voor mTLS. Dat is een aanvullende bewering over PKIoverheid-certificaatstructuur die buiten de scope van deze spec valt.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > In case the Authorization Server, Resource Server and client are not operated under responsibility of the same organisation, each party MUST use PKIoverheid certificates with OIN.
  - *De bron bevestigt dat OIN wordt gebruikt in PKIoverheid-certificaten, maar beschrijft niet specifiek dat het OIN in het `subject.serialNumber` veld staat.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *OIN in PKIoverheid-certificaten wordt niet besproken in dit beheermodeldocument.*

### `ls-iam-0047` — reference.md:89 *(§ Toegangsbeheer en Scopes)*

> De authorization server MOET controleren of gevraagde scopes geldig zijn, de client geautoriseerd is, en de resource owner akkoord gaat.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OAuth-NL-profiel - scope-validatie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > Authorization servers MAY restrict certain scopes from use by dynamically registered systems or public clients. [...] Client authorization requests containing scopes that are outside their permission MUST be rejected.
  - *De bron bevestigt dat de authorization server scopes kan beperken en verzoeken buiten de scope-rechten moet afwijzen, maar bevat geen expliciete drieledige controle (geldigheid, client-autorisatie én resource owner akkoord) als één gecombineerde MUST-vereiste.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt scope in de context van OIDC-verzoeken (scope MUST contain at least openid), maar bevat geen expliciete normering dat de authorization server MUST controleren of gevraagde scopes geldig zijn, de client geautoriseerd is, en de resource owner akkoord gaat als gecombineerde verplichting. Dit is een OAuth-profiel-vereiste die in de NL GOV OAuth-spec thuis hoort.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Scope-validatie door de authorization server wordt niet besproken in dit beheermodeldocument.*

### `ls-iam-0053` — reference.md:151 *(§ Client Registratie)*

> Voor native clients met per-instance registratie is dynamische client registratie verplicht (MUST); voor web- en browser-applicaties blijft handmatige registratie toegestaan.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - client registratie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > In case a native Client is using per-instance registration, the Client MUST use Dynamic Registration. [...] Clients SHOULD use Dynamic Registration as per [RFC7591] to reduce manual labor and the risks of configuration errors.
  - *De bron ondersteunt dat native clients met per-instance registratie MUST Dynamic Registration gebruiken. Voor web- en browser-applicaties zegt de bron SHOULD (niet dat handmatige registratie expliciet toegestaan blijft). De claim dat 'handmatige registratie toegestaan blijft' voor web/browser is een inferentie die de bron niet expliciet bevestigt.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > Native clients MUST either: use dynamic client registration to obtain a separate client id for each instance, or act as a public client by using a common client id and use PKCE [RFC7636] to protect calls to the token endpoint.
  - *De bron bevestigt dat native clients met per-instance registratie dynamische client registratie MUST gebruiken, maar de claim stelt ook dat voor web- en browser-applicaties handmatige registratie toegestaan blijft — dit wordt niet expliciet zo geformuleerd in de bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Dynamische client registratie voor native clients wordt niet besproken in dit beheermodeldocument.*

## UNGROUNDED — geen bron ondersteunt de claim (29)

### `ls-iam-0001` — SKILL.md:36 *(§ Versiemodel)*

> OpenID.NLGov (v1.0.1) en SAML zijn beide verplicht ('pas-toe-of-leg-uit') sinds 21-09-2023.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Forum Standaardisatie - Authenticatie-standaarden

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron is de technische specificatie van OpenID NLGov 1.0.1 zelf. Informatie over 'pas-toe-of-leg-uit'-status bij Forum Standaardisatie of de datum 21-09-2023 staat niet in deze bron. De bron vermeldt wel 'September 18, 2023' als publicatiedatum, maar niet de verplichtstellingsstatus door Forum Standaardisatie.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De brontekst gaat over het beheermodel van het OAuth-NL profiel. OpenID.NLGov en SAML worden niet besproken; de datum 21-09-2023 wordt nergens genoemd.*

### `ls-iam-0002` — SKILL.md:36 *(§ Versiemodel)*

> Voor nieuwe implementaties wordt OIDC aanbevolen; bestaande SAML-koppelingen blijven ondersteund.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Authenticatie-standaarden NL overheid

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron bevat geen aanbeveling over migratie van SAML naar OIDC of het ondersteunen van bestaande SAML-koppelingen. Dit is beleid van Forum Standaardisatie, niet inhoud van de technische spec.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron behandelt het beheermodel van OAuth-NL, niet de aanbeveling van OIDC versus SAML voor nieuwe implementaties.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt uitsluitend het OAuth NL profiel. OIDC versus SAML-aanbevelingen voor nieuwe implementaties komen niet voor in deze tekst.*
</details>

### `ls-iam-0011` — SKILL.md:67 *(§ Token specificaties)*

> Access tokens MOETEN het JWT-formaat (RFC 9068) hebben per het OAuth NL profiel.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OAuth-NL-profiel - access tokens

- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc9068.txt](https://www.rfc-editor.org/rfc/rfc9068.txt)
  - *RFC 9068 definieert het JWT-profiel voor OAuth 2.0 access tokens als standaard, maar bevat geen verwijzing naar een 'OAuth NL profiel' of enige verplichting dat dit NL profiel JWT-formaat MOET gebruiken. De bron beschrijft de RFC zelf, niet een nationaal profiel dat daarnaar verwijst.*

### `ls-iam-0030` — SKILL.md:223 *(§ Authorization Decision Log)*

> Het ADL record-model is transport-onafhankelijk; OTLP wordt aanbevolen, maar elke transport is toegestaan zolang het record de gespecificeerde velden draagt.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Authorization Decision Log - transport

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL transport-onafhankelijkheid en OTLP worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *ADL record-model en OTLP transport worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. ADL (Authorization Decision Log), OTLP en transport-onafhankelijkheid komen niet voor in deze bron.*
</details>

### `ls-iam-0032` — SKILL.md:231 *(§ Record-velden)*

> Het ADL veld `parent_span_id` is conditioneel verplicht: verplicht bij upstream `traceparent`, alleen weglaatbaar bij root-span.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - record-velden

- **NOT_FOUND** (high) — [https://www.w3.org/TR/trace-context](https://www.w3.org/TR/trace-context)
  - *De W3C Trace Context spec definieert parent-id als veld in de traceparent header, maar bevat geen uitspraken over een ADL-veld `parent_span_id` of conditionele verplichtingen daaromtrent. Dit is ADL-specifieke logica buiten scope van deze bron.*

### `ls-iam-0034` — SKILL.md:239 *(§ Record-velden)*

> Een denial (decision: false) heeft status `Unset`, niet `Error` in het ADL.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - status

- **NOT_FOUND** (high) — [https://www.w3.org/TR/trace-context](https://www.w3.org/TR/trace-context)
  - *De W3C Trace Context spec bevat geen informatie over ADL-statusvelden of de relatie tussen een authorization denial en een `Unset`-status. Dit valt buiten het onderwerp van deze bron.*

### `ls-iam-0035` — SKILL.md:253 *(§ `attributes.adl.core.*`)*

> Een ADL-veld MOET in precies één van de twee locaties staan: `attributes` (source-referenties) of `body` (raw data).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - attributes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL attributes/body-velden worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *ADL-velden en hun locaties worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL record-model met attributes/body-velden komt niet voor in deze bron.*
</details>

### `ls-iam-0036` — SKILL.md:264 *(§ `attributes.adl.core.*`)*

> Aanvullende ADL attribute keys volgen het patroon `<vendor>.<area>.<name>`. Onbekende keys MOETEN door consumers worden genegeerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - attributes

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL attribute key-patronen worden niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *ADL attribute key patronen worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL attribute key patronen komen niet voor in deze bron.*
</details>

### `ls-iam-0037` — SKILL.md:296 *(§ Trace context en ingestion)*

> Alle ADL-componenten (PEP, PDP, PIP, PAP) MOETEN W3C Trace Context propageren; `trace_id` blijft ongewijzigd over organisatiegrenzen, ook bij sampling=0.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - trace context

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *W3C Trace Context propagatie in ADL-context wordt niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *W3C Trace Context propagatie in ADL-componenten wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *W3C Trace Context propagatie voor ADL-componenten (PEP, PDP, PIP, PAP) komt niet voor in deze bron.*
</details>

### `ls-iam-0038` — SKILL.md:296 *(§ Trace context en ingestion)*

> ADL-records worden altijd geproduceerd ongeacht het sampled-bit in traceparent (sampling=0 geeft geen vrijstelling van logging).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - trace context

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *ADL-logging ongeacht sampled-bit wordt niet behandeld in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *ADL-records en het sampled-bit worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL-records en sampled-bit/sampling vrijstelling komen niet voor in deze bron.*
</details>

### `ls-iam-0039` — SKILL.md:296 *(§ Trace context en ingestion)*

> Ingestion van ADL log records MOET idempotent zijn met `(trace_id, span_id)` of content-hash als sleutel.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - ingestion

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron gaat over OpenID Connect NL GOV profiel. ADL (Authorization Decision Log) ingestion en idempotentie worden niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Idempotente ingestion van ADL log records wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Idempotente ingestion van ADL log records komt niet voor in deze bron.*
</details>

### `ls-iam-0040` — reference.md:9 *(§ SAML)*

> SAML is samen met OpenID.NLGov (v1.0.1) verplicht als onderdeel van de gecombineerde vermelding 'Authenticatie-standaarden' op het Forum Standaardisatie (sinds 21-09-2023).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Forum Standaardisatie - Authenticatie-standaarden

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron beschrijft de OIDC NL GOV standaard zelf, maar bevat geen informatie over de gecombineerde vermelding met SAML op het Forum Standaardisatie-lijst of de datum 21-09-2023.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De gecombineerde vermelding 'Authenticatie-standaarden' met SAML en OpenID.NLGov per 21-09-2023 wordt niet besproken in dit beheermodeldocument, dat alleen over OAuth-NL gaat.*

### `ls-iam-0041` — reference.md:44 *(§ SAML Implementatiedetails)*

> SAML assertions MOETEN worden ondertekend door de Identity Provider.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** SAML - security requirements

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt OpenID Connect, niet SAML. SAML-ondertekeningsvereisten voor assertions staan niet in deze spec.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *SAML assertion signing wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *SAML assertions en ondertekening door de Identity Provider worden niet behandeld in deze OAuth-NL-profiel bron.*
</details>

### `ls-iam-0042` — reference.md:45 *(§ SAML Implementatiedetails)*

> SAML assertions KUNNEN worden versleuteld voor de Service Provider.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** SAML - security requirements

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt OpenID Connect, niet SAML. SAML assertion-encryptie wordt niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *SAML assertion encryptie wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *SAML assertion versleuteling voor de Service Provider komt niet voor in deze bron.*
</details>

### `ls-iam-0043` — reference.md:46 *(§ SAML Implementatiedetails)*

> TLS MOET worden gebruikt voor alle SAML communicatie.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** SAML - security requirements

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt OpenID Connect, niet SAML. TLS-vereisten voor SAML-communicatie staan niet in deze spec.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *TLS-vereisten voor SAML communicatie worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Hoewel de bron TLS vereist voor OAuth-communicatie, behandelt zij geen SAML-specifieke TLS-vereisten.*
</details>

### `ls-iam-0044` — reference.md:47 *(§ SAML Implementatiedetails)*

> SAML Metadata MOET worden ondertekend en periodiek worden gevalideerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** SAML - security requirements

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt OpenID Connect, niet SAML. SAML Metadata-ondertekening en -validatie worden niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *SAML Metadata ondertekening en validatie worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *SAML Metadata ondertekening en periodieke validatie komen niet voor in deze bron.*
</details>

### `ls-iam-0048` — reference.md:96 *(§ Pushed Authorization Requests (PAR))*

> Pushed Authorization Requests (PAR) worden aanbevolen (RFC 9126) per het OAuth NL profiel.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** OAuth-NL-profiel - PAR

- **NOT_FOUND** (high) — [https://www.rfc-editor.org/rfc/rfc9126.txt](https://www.rfc-editor.org/rfc/rfc9126.txt)
  - *De bron is RFC 9126 zelf. De bron beschrijft de PAR-specificatie maar maakt geen melding van een 'OAuth NL profiel' of een Nederlandse aanbeveling. De claim gaat over het NL-profiel dat PAR aanbeveelt, wat buiten de scope van deze bron valt.*

### `ls-iam-0050` — reference.md:138 *(§ Userinfo Endpoint)*

> De OpenID Provider MOET gebruikers informeren over welke claims worden gedeeld en met welke Relying Parties.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - privacy

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron bevat geen verplichting dat de OpenID Provider gebruikers moet informeren over welke claims worden gedeeld en met welke Relying Parties. Privacy-overwegingen richten zich op dataminimalisatie, pairwise identifiers en encryptie, niet op een informatieplicht richting gebruikers.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Informatieplicht van de OpenID Provider richting gebruikers wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Informatieplicht van de OpenID Provider aan gebruikers over gedeelde claims en Relying Parties komt niet voor in deze bron.*
</details>

### `ls-iam-0052` — reference.md:151 *(§ Client Registratie)*

> Het OIDC NL GOV profiel beveelt dynamische client registratie (RFC 7591) aan ('Clients SHOULD use Dynamic Registration').

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** OIDC NL GOV profiel - client registratie

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc7591.txt](https://www.rfc-editor.org/rfc/rfc7591.txt)
  - *De brontekst is RFC 7591 zelf (de specificatie voor OAuth 2.0 Dynamic Client Registration). De claim gaat over wat het OIDC NL GOV profiel aanbeveelt ('Clients SHOULD use Dynamic Registration'). RFC 7591 bevat geen tekst over het NL GOV profiel of aanbevelingen daarin; die uitspraak staat in het NL GOV profiel-document, niet in RFC 7591.*

### `ls-iam-0054` — reference.md:176 *(§ Trace context propagatie)*

> Alle ADL-componenten MOETEN W3C Trace Context propageren en trace-continuïteit over componentgrenzen behouden. Een nieuwe `trace_id` MAG NIET worden gealloceerd binnen een lopende beslissingsflow.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Authorization Decision Log - trace context propagatie

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt OpenID Connect NL GOV. ADL (Authorization Decision Log) en W3C Trace Context worden niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *W3C Trace Context propagatie en verbod op nieuwe trace_id allocatie worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *W3C Trace Context propagatie en verbod op nieuwe trace_id allocatie binnen ADL-flows komen niet voor in deze bron.*
</details>

### `ls-iam-0055` — reference.md:178 *(§ Trace context propagatie)*

> ADL-records zijn accountability records en MOETEN altijd worden geproduceerd, ongeacht sampling. ADL-emitters MOGEN het `sampled`-flag NIET wijzigen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - sampling

<details><summary>2x NOT_FOUND + 1x OUT_OF_SCOPE (klap uit)</summary>

- **OUT_OF_SCOPE** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt OpenID Connect NL GOV. ADL-records, accountability records en sampling-flags worden niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *ADL-records als accountability records en sampling-vereisten worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *ADL-records als accountability records en het sampled-flag komen niet voor in deze bron.*
</details>

### `ls-iam-0056` — reference.md:184 *(§ Idempotente ingestion)*

> Ingestion van ADL log records MOET idempotent zijn; re-submission MOET niet leiden tot een duplicate persisted record. De idempotency-sleutel is `(trace_id, span_id)` of een content-hash.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - idempotente ingestion

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron gaat over OpenID Connect NL GOV profiel. Er is geen sprake van een Authorization Decision Log, idempotente ingestion, trace_id, span_id of content-hash.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Idempotente ingestion van ADL log records wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Idempotente ingestion van ADL log records met (trace_id, span_id) als sleutel komt niet voor in deze bron.*
</details>

### `ls-iam-0057` — reference.md:188 *(§ Cached decisions)*

> Caching van autorisatiebeslissingen wordt afgeraden. Indien toch toegepast, MOET de toepassing van een gecachte beslissing een nieuw log record produceren met de `trace_id` en `parent_span_id` van de nieuwe request en een vers gealloceerde `span_id`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - cached decisions

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron behandelt caching van Discovery-documenten en JWK-sets, niet het cachen van autorisatiebeslissingen of een Authorization Decision Log.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Caching van autorisatiebeslissingen en bijbehorende ADL-vereisten worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Caching van autorisatiebeslissingen en bijbehorende logging-vereisten komen niet voor in deze bron.*
</details>

### `ls-iam-0058` — reference.md:214 *(§ Retention en Privacy)*

> ADL log records MOETEN minimaal 12 maanden worden bewaard voor audit doeleinden.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - retention

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Geen vermelding van ADL log records, retentieperiodes of audit-bewaarplicht in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Minimale bewaarperiode van ADL log records wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Bewaarplicht van 12 maanden voor ADL log records komt niet voor in deze bron.*
</details>

### `ls-iam-0059` — reference.md:217 *(§ Retention en Privacy)*

> Persoonlijke identificeerbare informatie (PII) in ADL log records MOET worden beschermd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - privacy

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron bevat privacy-overwegingen over pairwise identifiers en data minimization, maar niets over PII-bescherming in ADL log records.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *PII-bescherming in ADL log records wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Bescherming van PII in ADL log records komt niet voor in deze bron.*
</details>

### `ls-iam-0060` — reference.md:218 *(§ Retention en Privacy)*

> Toegang tot ADL logs MOET worden beperkt tot geautoriseerd personeel.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - privacy

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Geen vermelding van toegangsbeperking tot ADL logs in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron gaat over het beheermodel van de OAuth-NL standaard. Er wordt nergens gesproken over een Authorization Decision Log (ADL) of toegangsbeperking tot logbestanden.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Toegangsbeperking tot ADL logs voor geautoriseerd personeel komt niet voor in deze bron.*
</details>

### `ls-iam-0061` — reference.md:220 *(§ Retention en Privacy)*

> Bij het delen van ADL logs voor analyse MOETEN PII worden geanonimiseerd.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Authorization Decision Log - privacy

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *Geen vermelding van het delen of anonimiseren van ADL logs voor analyse in deze bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron bevat geen informatie over Authorization Decision Logs, het delen van logs voor analyse, of het anonimiseren van PII in logbestanden.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Anonimisering van PII bij delen van ADL logs voor analyse komt niet voor in deze bron.*
</details>

### `ls-iam-0062` — reference.md:235 *(§ Toegankelijkheidsvalidatie)*

> IAM-specificaties MOETEN voldoen aan WCAG 2.1 niveau AA voor toegankelijkheid.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** IAM repositories - toegankelijkheid

- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/OAuth-NL-profiel](https://logius-standaarden.github.io/OAuth-NL-profiel)
  - *De brontekst bevat geen enkele verwijzing naar WCAG, toegankelijkheid (accessibility), of soortgelijke vereisten. De specificatie richt zich uitsluitend op OAuth 2.0 autorisatie- en authenticatieprofielen.*

### `ls-iam-0063` — reference.md:248 *(§ Markdown Linting)*

> Markdown bestanden MOETEN voldoen aan de markdownlint regels voor consistente opmaak.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** IAM repositories - markdown linting

<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron bevat geen vereisten over markdown linting of markdownlint regels.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron beschrijft het beheermodel van OAuth-NL en noemt wel dat pre-commit hooks worden gebruikt in het generieke beheermodel, maar bevat geen specifieke vereisten over markdownlint regels voor markdown bestanden.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De brontekst is de NL GOV Assurance profile for OAuth 2.0 specificatie. Deze bevat geen informatie over markdownlint regels of opmaakconventies voor Markdown bestanden in repositories. Dit is een technische OAuth-specificatie, geen repository-stijlgids.*
</details>

## GROUNDED — minstens één bron ondersteunt de claim (19)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-iam-0003` — SKILL.md:38 *(§ Versiemodel)*

> Het OAuth-NL-profiel v1.0 staat op het Forum Standaardisatie als verplicht ('pas-toe-of-leg-uit').

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Forum Standaardisatie - OAuth NL profiel

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  > De status van de standaard is 'Verplicht (pas toe leg uit)'. Dit houdt kort gezegd in dat Nederlandse overheden en instellingen uit de (semi) publieke sector verplicht zijn deze standaard toe te passen op het moment dat zij REST API's gaan gebruiken voor het ontsluiten van overheidsinformatie

### `ls-iam-0004` — SKILL.md:38 *(§ Versiemodel)*

> OAuth-NL-profiel versie v1.1.0 is vastgesteld door Logius (DEF) en gepubliceerd op gitdocumentatie.logius.nl.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth-NL-profiel

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > NL GOV Assurance profile for OAuth 2.0 v1.1.0 Logius Standard Definitive version December 03, 2024 [...] MIDO programmeringstafel 1.1.0 definitive approved version 03-12-2024

### `ls-iam-0005` — SKILL.md:61 *(§ Verplichte beveiligingseisen)*

> PKCE is verplicht voor alle clients per het OIDC NL GOV profiel, inclusief confidential clients die private_key_jwt of mTLS gebruiken; er is geen vrijstelling.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - PKCE

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > Clients MUST use 'Proof Key for Code Exchange' [RFC7636] to protect calls to the Token Endpoint. [...] OpenID Providers MUST support and require the use of 'Proof Key for Code Exchange' ([RFC7636]) using only the S256 verification method
  - *De MUST geldt voor alle clients zonder vrijstelling. Sectie 4.1 stelt dit als algemene vereiste voor alle client types, en sectie 5 vereist dat providers dit afdwingen.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De bron beschrijft het beheermodel, niet de technische inhoud van het OIDC NL GOV profiel. PKCE-vereisten worden niet besproken.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron is het OAuth NL profiel, niet het OIDC NL GOV profiel. PKCE-vereisten voor confidential clients die private_key_jwt of mTLS gebruiken worden in deze bron niet behandeld. De bron vereist PKCE voor public clients en native clients, maar spreekt niet van een vrijstellingsloze verplichting voor alle clients inclusief confidential clients.*

### `ls-iam-0006` — SKILL.md:62 *(§ Verplichte beveiligingseisen)*

> De grant type 'authorization_code' is verplicht (MUST) per het OAuth NL profiel.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OAuth-NL-profiel - grant types

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > grant_type REQUIRED . MUST contain the value authorization_code . Identical as in [OAuth2.NLGov].
  - *De bron bevestigt dat authorization_code verplicht is in het token request, en verwijst naar OAuth2.NLGov. De claim stelt dit als vereiste 'per het OAuth NL profiel', maar de bron zelf is het OIDC NL GOV profiel dat verwijst naar OAuth2.NLGov. De inhoud klopt, maar de directe bron voor de claim is het OAuth NL profiel dat hier niet beschikbaar is.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > The authorization server MUST support the authorization_code , and MAY support the client_credentials grant types as described in Section 2.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Grant types worden in dit beheermodeldocument niet technisch gespecificeerd.*

### `ls-iam-0007` — SKILL.md:62 *(§ Verplichte beveiligingseisen)*

> De grant type 'client_credentials' is toegestaan (MAY) voor machine-to-machine communicatie per het OAuth NL profiel.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** OAuth-NL-profiel - grant types

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > The authorization server MUST support the authorization_code , and MAY support the client_credentials grant types as described in Section 2. [...] These clients use the client credentials flow of OAuth 2 by sending a request to the token endpoint with the client's credentials and obtaining an access token in the response.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron vermeldt client_credentials grant type niet. In de discovery document sectie staat grant_types_supported MUST be ['authorization_code']. client_credentials wordt niet behandeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Client credentials grant type wordt niet besproken in dit beheermodeldocument.*

### `ls-iam-0009` — SKILL.md:63 *(§ Verplichte beveiligingseisen)*

> Access tokens worden als HTTP Authorization header (Bearer scheme) meegegeven. Transport via query parameters is verboden (MUST NOT).

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** OAuth-NL-profiel - token transport

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > Clients SHOULD send bearer tokens passed in the Authentication header as defined by [rfc6750]. [...] A Protected Resource under this profile MUST NOT accept access tokens passed using the query parameter method.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  - *De bron bevat geen expliciete bepaling over het verbod op het meegeven van access tokens als query parameter. Het Bearer scheme wordt getoond in een voorbeeld (Authorization: Bearer ...) maar een MUST NOT voor query parameters staat er niet in.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Token transport en Authorization header-vereisten worden niet besproken in dit beheermodeldocument.*

### `ls-iam-0010` — SKILL.md:63 *(§ Verplichte beveiligingseisen)*

> Form-encoded body parameters (RFC 6750 Section 2.2) zijn toegestaan voor het meegeven van access tokens.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** OAuth-NL-profiel - token transport

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc6750.txt](https://www.rfc-editor.org/rfc/rfc6750.txt)
  > Resource servers MAY support this method.
  - *RFC 6750 Section 2.2 beschrijft de form-encoded body parameter methode en stelt dat resource servers deze MAY ondersteunen. De claim gebruikt 'toegestaan' (MAY), wat overeenkomt met de tekst in de bron.*

### `ls-iam-0012` — SKILL.md:68 *(§ Token specificaties)*

> Refresh tokens worden ondersteund (MAY) bij de authorization_code flow en maken het mogelijk nieuwe access tokens te verkrijgen zonder hernieuwde gebruikersinteractie.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** OAuth-NL-profiel - refresh tokens

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > OpenID Providers MAY issue Refresh Tokens to Clients; when used, Refresh Tokens MUST be one-time-use or sender-constrained.
  - *De bron bevestigt dat refresh tokens MAY worden uitgegeven. De koppeling aan specifiek de authorization_code flow staat niet expliciet vermeld maar is impliciet (dit profiel gebruikt alleen authorization_code).*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > This client type MAY request and be issued a refresh token if the security parameters of the access request allow for it. [...] Under this profile, refresh tokens are supported.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Refresh tokens worden niet besproken in dit beheermodeldocument.*

### `ls-iam-0013` — SKILL.md:68 *(§ Token specificaties)*

> Refresh token rotation wordt aanbevolen per het OAuth NL profiel.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** OAuth-NL-profiel - refresh tokens

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > For security reasons, Refresh Tokens that are not sender-constrained MUST be one-time-use, i.e. with every Access Token refresh response the OpenID Provider can issue a new Refresh Token and MUST invalidate the previous Refresh Token
  - *Refresh token rotation wordt vereist (MUST) voor niet-sender-constrained tokens, wat de aanbeveling (SHOULD) in de claim ondersteunt. De bron stelt het als vereiste, wat sterker is dan de claim suggereert.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Refresh token rotation wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron vermeldt dat refresh tokens voor public clients sender-constrained of one-time use MOETEN zijn, maar een expliciete SHOULD-aanbeveling voor 'refresh token rotation' als algemeen concept ontbreekt.*

### `ls-iam-0014` — SKILL.md:75 *(§ Client authenticatie)*

> private_key_jwt is verplicht per het OAuth NL profiel voor client authenticatie bij het token endpoint.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OAuth-NL-profiel - client authenticatie

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > Confidential Clients, as defined in Section 4.1, MUST authenticate to the OpenID Provider using either: a JWT assertion as defined by the 'JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants' [RFC7523] using only the private_key_jwt method defined in [OpenID.Core]; or mutually authenticated TLS, as specified in [RFC8705].
  - *De bron vereist private_key_jwt ÓÓOF mTLS voor confidential clients — het is dus geen absolute verplichting van private_key_jwt alleen. De claim stelt private_key_jwt als enige verplichte methode, maar de bron geeft mTLS als gelijkwaardig alternatief. Bovendien is de claim dat dit 'per het OAuth NL profiel' is, terwijl deze bron het OIDC NL GOV profiel is.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > Full clients, native clients with dynamically registered keys, and direct access clients as defined above MUST authenticate to the authorization server's token endpoint using a JWT assertion as defined by the [JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants] using only the private_key_jwt method defined in [OpenID Connect Core].
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *private_key_jwt als verplicht authenticatiemechanisme bij het token endpoint wordt niet besproken in dit beheermodeldocument.*

### `ls-iam-0018` — SKILL.md:106 *(§ Betrouwbaarheidsniveaus (Levels of Assurance))*

> De `acr_values` parameter in het authentication request mapt naar eIDAS-betrouwbaarheidsniveaus. De OpenID Provider geeft het bereikte niveau terug in de `acr` claim van het ID Token.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OIDC NL GOV profiel - acr_values

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > acr_values OPTIONAL. Lists the acceptable LoAs for this authentication. [...] OpenID Providers SHOULD use eIDAS Level of Assurance (LoA) values for the acr Claim [...] acr OPTIONAL. The LoA the End-User was authenticated at. MUST be at least the requested Level of Assurance value requested by the Client (either via the acr_values or claims parameters)
  - *De bron bevestigt dat acr_values in het authentication request verwijst naar LoA-niveaus en dat de provider het bereikte niveau teruggeeft in de acr claim van het ID Token, gerelateerd aan eIDAS.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De acr_values parameter en mapping naar eIDAS-niveaus worden niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. acr_values-parameter en ID Token acr claim worden niet besproken.*

### `ls-iam-0020` — SKILL.md:120 *(§ Verplichte claims in het ID Token)*

> De `acr` claim is OPTIONAL per OIDC NL GOV; als gezet MOET de waarde minimaal het gevraagde betrouwbaarheidsniveau zijn.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token acr claim

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > acr OPTIONAL . The LoA the End-User was authenticated at. MUST be at least the requested Level of Assurance value requested by the Client (either via the acr_values or claims parameters) or - if none was requested - a Level of Assurance established through prior agreement.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *De acr claim in ID Tokens wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. De acr claim in ID Tokens is geen onderdeel van deze specificatie.*

### `ls-iam-0022` — SKILL.md:127 *(§ ID Token validatie)*

> De `iss` claim MOET exact overeenkomen met de `issuer` uit het discovery document bij ID Token validatie.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > iss The issuer Claim is the Uniform Resource Locater (URL) of the expected Issuer. Identical as in [OpenID.iGov].
  - *De bron stelt dat iss de URL van de verwachte issuer moet zijn. De expliciete formulering 'exact overeenkomen met de issuer uit het discovery document' staat niet letterlijk zo in de bron, maar dit is de directe strekking van de verificatieverplichting.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *iss claim validatie wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. ID Token iss-validatie per OIDC NL GOV profiel wordt niet besproken.*

### `ls-iam-0023` — SKILL.md:128 *(§ ID Token validatie)*

> De `aud` claim MOET de `client_id` van de relying party bevatten bij ID Token validatie.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - ID Token validatie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > aud The audience Claim contains the Client ID of the Client. Identical as in [OpenID.iGov].
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *aud claim validatie wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *De bron behandelt het OAuth NL profiel. aud-validatie van ID Tokens per OIDC NL GOV profiel wordt niet besproken.*

### `ls-iam-0049` — reference.md:138 *(§ Userinfo Endpoint)*

> De Relying Party MOET alleen de claims vragen die strikt noodzakelijk zijn voor de dienstverlening (dataminimalisatie).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** OIDC NL GOV profiel - privacy

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > All Clients MUST apply the concept of data minimization. As a result, a Client MUST NOT request any more identifiers, attributes or other Claims than strictly necessary.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Dataminimalisatie voor Relying Parties wordt niet besproken in dit beheermodeldocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  - *Dataminimalisatie als MUST-verplichting voor de Relying Party in het OIDC NL GOV profiel komt niet voor in deze OAuth-NL-profiel bron.*

### `ls-iam-0051` — reference.md:144 *(§ Client Registratie)*

> Redirect URI's bij client registratie vereisen een exacte match; wildcards zijn niet toegestaan voor beveiliging.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** OIDC NL GOV profiel - client registratie

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oidc](https://gitdocumentatie.logius.nl/publicatie/api/oidc)
  > One of these registered Redirection URI values MUST exactly match the redirect_uri parameter value used in each Authorization Request.
  - *De bron stelt expliciet dat exact matching vereist is. Wildcards worden niet vermeld als optie, en de exacte-match eis sluit wildcard-gebruik uit.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth](https://gitdocumentatie.logius.nl/publicatie/api/oauth)
  > The Authorization Server MUST compare a client's registered redirect URIs with the redirect URI presented during an authorization request using an exact string match.
  - *De bron bevestigt exact string matching voor redirect URIs. Wildcards worden niet expliciet verboden, maar exact string match sluit ze impliciet uit.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer)
  - *Redirect URI exacte match en verbod op wildcards worden niet besproken in dit beheermodeldocument.*

### `ls-iam-0064` — reference.md:357 *(§ Aanvullende Bronnen)*

> RFC 7636 definieert PKCE (Proof Key for Code Exchange).

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth - PKCE

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc7636.txt](https://www.rfc-editor.org/rfc/rfc7636.txt)
  > Proof Key for Code Exchange by OAuth Public Clients [...] This specification describes the attack as well as a technique to mitigate against the threat through the use of Proof Key for Code Exchange (PKCE, pronounced "pixy").

### `ls-iam-0065` — reference.md:358 *(§ Aanvullende Bronnen)*

> RFC 9068 definieert het JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth - JWT access tokens

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc9068.txt](https://www.rfc-editor.org/rfc/rfc9068.txt)
  > This specification defines a profile for issuing OAuth 2.0 access tokens in JSON Web Token (JWT) format.

### `ls-iam-0066` — reference.md:359 *(§ Aanvullende Bronnen)*

> RFC 9126 definieert OAuth 2.0 Pushed Authorization Requests.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** OAuth - PAR

- **SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc9126.txt](https://www.rfc-editor.org/rfc/rfc9126.txt)
  > This document defines the pushed authorization request (PAR) endpoint, which allows clients to push the payload of an OAuth 2.0 authorization request to the authorization server via a direct request and provides them with a request URI that is used as reference to the data in a subsequent call to the authorization endpoint.

</details>
