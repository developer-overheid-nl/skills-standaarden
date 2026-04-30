---
name: ls-iam
description: "Gebruik deze skill wanneer de gebruiker vraagt over 'OAuth', 'OpenID Connect', 'OIDC', 'authenticatie', 'autorisatie', 'AuthZEN', 'SAML', 'identity management', 'toegangsbeheer', 'OAuth NL profiel', 'OIDC NL GOV', 'NL GOV profiel', 'authorization decision', 'OIN authenticatie', 'token endpoint', 'JWT', 'private_key_jwt', 'client credentials', 'authorization_code', 'PKCE'."
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - Bash(gh issue list *)
  - Bash(gh pr list *)
  - Bash(gh search *)
  - Bash(curl -s *)
  - WebFetch(*)
metadata:
  created-with-ai: "true"
  created-with-model: claude-opus-4-20250514
  created-date: "2025-02-12"
  status: concept
---

> **CONCEPT — Let op:** Deze skill is geen officieel product van Logius. De beschrijvingen zijn informatieve samenvattingen — niet de officiële standaarden zelf. De definities op [forumstandaardisatie.nl](https://www.forumstandaardisatie.nl/open-standaarden) en [Logius](https://www.logius.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Overheidsbreed standpunt voor de inzet van generatieve AI](https://open.overheid.nl/documenten/bc03ce31-0cf1-4946-9c94-e934a62ebe73/file). Zie [DISCLAIMER.md](../../DISCLAIMER.md) en onze [verantwoording](https://github.com/developer-overheid-nl/skills-marketplace/blob/main/docs/verantwoording.md).

# Identity & Access Management (IAM)

**Agent-instructie:** Deze skill helpt bij het implementeren van authenticatie en autorisatie voor overheids-APIs. Gebruik de OAuth 2.0 NL en OIDC NL GOV profielen voor nieuwe implementaties. AuthZEN voor geëxternaliseerde autorisatie.

De IAM-standaarden van Logius definiëren profielen voor authenticatie en autorisatie bij Nederlandse overheids-APIs. Dit omvat OAuth 2.0, OpenID Connect, AuthZEN en aanvullende profielen specifiek voor de Nederlandse overheid. Deze standaarden waarborgen een consistent en veilig identiteits- en toegangsbeheer binnen het publieke domein.

## Versiemodel

Net als andere Logius-standaarden kennen deze standaarden twee publicatiekanalen (vergelijkbaar met W3C):

- **Vastgestelde versie (DEF)**: officieel goedgekeurd, gepubliceerd op `gitdocumentatie.logius.nl`
- **Werkversie (draft)**: werk-in-uitvoering, gepubliceerd op `logius-standaarden.github.io`

De IAM-standaarden OAuth-NL-profiel, OIDC-NLGOV en OIN-Stelsel hebben **vastgestelde versies** op gitdocumentatie.logius.nl. OAuth-Beheermodel heeft eveneens een vastgestelde versie maar is **gearchiveerd**. De overige standaarden (AuthZEN, Authorization Decision Log, OAuth-Inleiding) hebben momenteel alleen werkversies.

OpenID.NLGov (v1.0.1) en SAML zijn beide **verplicht** (['pas-toe-of-leg-uit'](https://www.forumstandaardisatie.nl/open-standaarden/authenticatie-standaarden), sinds 21-09-2023). Voor **nieuwe implementaties** wordt OIDC aanbevolen; bestaande SAML-koppelingen blijven ondersteund. SAML-details staan in [reference.md](reference.md).

Op het Forum Standaardisatie staat het OAuth-NL-profiel **v1.0** als verplicht (['pas-toe-of-leg-uit'](https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-assurance-profile-oauth-20)). Versie v1.1.0 is vastgesteld door Logius (DEF) maar is op het Forum [in procedure genomen](https://www.forumstandaardisatie.nl/intakeadvies-nl-gov-assurance-profile-oauth-20-versie-11) (intake goedgekeurd 24-09-2025, verkort expertonderzoek loopt).

## Repositories

| Repository | Beschrijving | Licentie | Vastgesteld | Draft |
|-----------|-------------|--------|------------|-------|
| [OAuth-NL-profiel](https://github.com/logius-standaarden/OAuth-NL-profiel) | Nederlands profiel voor OAuth 2.0 | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) | [v1.1.0](https://gitdocumentatie.logius.nl/publicatie/api/oauth/) | [Draft](https://logius-standaarden.github.io/OAuth-NL-profiel/) |
| [OIDC-NLGOV](https://github.com/logius-standaarden/OIDC-NLGOV) | OpenID Connect profiel voor NL overheid | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) | [v1.0.1](https://gitdocumentatie.logius.nl/publicatie/api/oidc/) | [Draft](https://logius-standaarden.github.io/OIDC-NLGOV/) |
| [OAuth-Inleiding](https://github.com/logius-standaarden/OAuth-Inleiding) | Introductie en achtergrond OAuth | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) | - | [Draft](https://logius-standaarden.github.io/OAuth-Inleiding/) |
| [OAuth-Beheermodel](https://github.com/logius-standaarden/OAuth-Beheermodel) | Beheermodel voor OAuth standaarden — **gearchiveerd** | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) | [v1.0](https://gitdocumentatie.logius.nl/publicatie/api/oauth-beheer/) | - |
| [authzen-nlgov](https://github.com/logius-standaarden/authzen-nlgov) | AuthZEN NL GOV profiel (autorisatiebeslissingen) | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) | - | [Draft](https://logius-standaarden.github.io/authzen-nlgov/) |
| [authorization-decision-log](https://github.com/logius-standaarden/authorization-decision-log) | Logging van autorisatiebeslissingen | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) | - | [Draft](https://logius-standaarden.github.io/authorization-decision-log/) |
| [st-saml-spec](https://github.com/logius-standaarden/st-saml-spec) | SAML specificatie — onderdeel van verplichte "Authenticatie-standaarden"; voor nieuwe implementaties wordt OIDC aanbevolen | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) | - | [Draft](https://logius-standaarden.github.io/st-saml-spec/) |
| [OIN-Stelsel](https://github.com/logius-standaarden/OIN-Stelsel) | Organisatie Identificatie Nummer (ook in `/ls-dk`) | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) | [v2.2.2](https://gitdocumentatie.logius.nl/publicatie/dk/oin/) | [Draft](https://logius-standaarden.github.io/OIN-Stelsel/) |

---

## OAuth 2.0 NL Profiel

Het Nederlandse OAuth 2.0 profiel scherpt de basisspecificatie (RFC 6749) aan met strikte beveiligingseisen voor gebruik binnen de overheid. Doel is het voorkomen van veelvoorkomende kwetsbaarheden en het garanderen van interoperabiliteit.

### Verplichte beveiligingseisen

- **PKCE (Proof Key for Code Exchange)** is verplicht voor public clients. Confidential clients die zich authenticeren met `private_key_jwt` of mTLS zijn vrijgesteld. Dit voorkomt authorization code interception aanvallen. Clients genereren een `code_verifier` en sturen een `code_challenge` mee in het authorization request.
- **Grant types**: `authorization_code` is verplicht (MUST); `client_credentials` is toegestaan (MAY) voor machine-to-machine communicatie. Implicit grant en Resource Owner Password Credentials zijn expliciet verboden vanwege bekende beveiligingsrisico's.
- **Tokens als HTTP headers**: access tokens worden als HTTP `Authorization` header (Bearer scheme) meegegeven. Transport via query parameters is verboden (MUST NOT). Form-encoded body parameters (RFC 6750 Section 2.2) zijn wel toegestaan.

### Token specificaties

- **Access tokens**: JWT-formaat (RFC 9068) is verplicht (MUST). Dit maakt lokale validatie mogelijk zonder een introspection endpoint aan te roepen, wat de prestaties verbetert.
- **Refresh tokens**: worden ondersteund (MAY) bij de `authorization_code` flow. Hiermee kunnen clients nieuwe access tokens verkrijgen zonder hernieuwde gebruikersinteractie. Refresh token rotation wordt aanbevolen.
- **Token levensduur**: access tokens hebben een korte levensduur. De exacte duur wordt bepaald door de authorization server, maar korte TTL's (minuten) verdienen de voorkeur.

### Client authenticatie

Het token endpoint vereist sterke client authenticatie:

- **private_key_jwt** (VERPLICHT per OAuth NL profiel): de client ondertekent een JWT-assertion met zijn private key en stuurt deze mee als client authenticatie. De authorization server valideert met de geregistreerde public key.
- **mTLS (Mutual TLS)** (MAY per OAuth NL profiel, gelijkwaardig alternatief per OIDC NL GOV profiel): de client presenteert een TLS-certificaat (bij voorkeur PKIoverheid) bij het aanroepen van het token endpoint. Dit biedt sterke cryptografische binding.

### Keuzematrix: grant type en client authenticatie

```
Menselijke eindgebruiker betrokken?
  JA  → authorization_code + PKCE
  NEE → client_credentials (machine-to-machine)

Client authenticatie bij token endpoint:
  → private_key_jwt (standaard, verplicht per OAuth NL profiel)
  → mTLS (gelijkwaardig alternatief per OIDC NL GOV profiel, bij PKIoverheid certificaat)
```

---

## OpenID Connect NL GOV Profiel

Het OIDC NL GOV profiel bouwt voort op OpenID Connect Core 1.0 en het iGov-profiel, en specificeert eisen voor authenticatie binnen de Nederlandse overheid. Het profiel legt de nadruk op betrouwbaarheidsniveaus en gestructureerde identiteitsinformatie.

### Betrouwbaarheidsniveaus (Levels of Assurance)

Het profiel definieert drie betrouwbaarheidsniveaus conform de eIDAS-verordening:

| Niveau | eIDAS Level | Toepassing |
|--------|-------------|------------|
| **Laag** | Low | Zelfregistratie, beperkte toegang |
| **Substantieel** | Substantial | DigiD Midden/Hoog, eHerkenning EH3 |
| **Hoog** | High | eHerkenning EH4, face-to-face verificatie |

De `acr_values` parameter in het authentication request mapt naar deze eIDAS-niveaus. De OpenID Provider geeft het daadwerkelijk bereikte niveau terug in de `acr` claim van het ID Token.

### Verplichte claims in het ID Token

Het ID Token moet minimaal de volgende claims bevatten:

| Claim | Beschrijving |
|-------|-------------|
| `sub` | Unieke identifier van de gebruiker (subject) |
| `iss` | Identifier van de OpenID Provider (issuer) |
| `aud` | Identifier van de Relying Party (audience) |
| `exp` | Verloopdatum van het token (expiration) |
| `iat` | Tijdstip van uitgifte (issued at) |
| `nonce` | Waarde uit het authorization request (voorkomt replay attacks) |
| `acr` | Betrouwbaarheidsniveau (SHOULD — aanbevolen, niet verplicht) |

### ID Token validatie

Bij het valideren van een OIDC ID Token MOETEN de volgende stappen worden doorlopen:

1. **Signature** - Verifieer de JWS handtekening met de publieke sleutel van de provider (via `jwks_uri`)
2. **iss** - MOET exact overeenkomen met de `issuer` uit het discovery document
3. **aud** - MOET de `client_id` van de relying party bevatten
4. **nonce** - MOET exact overeenkomen met de nonce uit het authorization request
5. **exp** - MOET in de toekomst liggen (token niet verlopen)
6. **iat** - MAG niet te ver in het verleden liggen (max 5 minuten aanbevolen)
7. **acr** - MOET minimaal het gevraagde betrouwbaarheidsniveau bevatten
8. **jti** - MOET uniek zijn (bewaar voldoende lang om hergebruik te detecteren)

---

## AuthZEN NL GOV

Het AuthZEN NL GOV profiel specificeert een architectuur voor geëxternaliseerde autorisatie. In plaats van autorisatielogica in applicaties te bouwen, worden autorisatiebeslissingen gedelegeerd aan een centraal beslispunt. Dit bevordert consistentie, herbruikbaarheid en auditeerbaarheid.

### Architectuurcomponenten

Het profiel definieert PDP en PEP als kerncomponenten. PAP en PIP komen uit het XACML-referentiemodel en worden in de praktijk vaak samen ingezet:

| Component | Rol | Beschrijving |
|-----------|-----|-------------|
| **PDP** | Policy Decision Point | Evalueert autorisatieverzoeken tegen het beleid en neemt een beslissing (permit/deny) |
| **PEP** | Policy Enforcement Point | Onderschept verzoeken en handhaaft de beslissing van het PDP |
| **PAP** | Policy Administration Point | Beheert autorisatiebeleid: aanmaken, wijzigen, verwijderen van policies |
| **PIP** | Policy Information Point | Levert aanvullende attributen en contextinformatie aan het PDP voor besluitvorming |

### Evaluation endpoint

Het PDP biedt een gestandaardiseerd evaluation endpoint:

```
POST /access/v1/evaluation
Content-Type: application/json
```

### Request formaat

Een autorisatieverzoek bestaat uit vier elementen:

- **subject**: de entiteit die toegang vraagt (gebruiker, systeem)
- **action**: de gevraagde actie
- **resource**: het object waarop de actie wordt uitgevoerd
- **context**: aanvullende omstandigheden (optioneel)

Voorbeeld van een autorisatieverzoek:

```json
{
  "subject": {
    "type": "user",
    "id": "alice"
  },
  "action": {
    "name": "approve"
  },
  "resource": {
    "type": "holiday-request",
    "id": "446epbc8y7",
    "properties": {
      "employee": "bob"
    }
  }
}
```

In dit voorbeeld vraagt gebruiker Alice toestemming om een verlofaanvraag van Bob goed te keuren. Het PDP evalueert of Alice de juiste rol en bevoegdheid heeft om deze actie uit te voeren.

### Response formaat

Het PDP retourneert een beslissing:

- **decision** (boolean): `true` voor toestaan, `false` voor weigeren
- **context** (optioneel): aanvullende informatie, zoals de reden van weigering of referenties naar de toegepaste beleidsregels

```json
{
  "decision": true
}
```

Bij een weigering kan het PDP een reden meegeven:

```json
{
  "decision": false,
  "context": {
    "reason": {
      "48": "No signing authority"
    }
  }
}
```

---

## Authorization Decision Log

De Authorization Decision Log standaard definieert een gestructureerd formaat voor het vastleggen van autorisatiebeslissingen. Dit is essentieel voor audit, verantwoording en het reproduceren van historische beslissingen.

De werkversie volgt sinds april 2026 een **OpenTelemetry-vorm** op basis van de AuthZEN-informatiemodel. Het record-model is transport-onafhankelijk; OTLP wordt aanbevolen, maar elke transport (REST, gRPC, messaging) is toegestaan zolang het record de gespecificeerde velden draagt.

### Verplichte velden

| Veld | Type | Beschrijving |
|------|------|-------------|
| `trace_id` | 16 byte hex (32 chars) | Trace-identifier conform [W3C Trace Context](https://www.w3.org/TR/trace-context/), MUST cryptografisch random gegenereerd worden |
| `span_id` | 8 byte hex (16 chars) | Span-identifier voor deze beslissing |
| `event_name` | string | Type beslissing — een van vijf vaste waarden (zie hieronder) |
| `timestamp` | uint64 | Aantal milliseconden sinds Unix epoch |
| `status` | enum | `Unset`, `Ok` of `Error` |

### Conditioneel verplicht

| Veld | Beschrijving |
|------|-------------|
| `parent_span_id` | Verplicht wanneer een upstream `traceparent` aanwezig is; alleen weglaatbaar bij root-span |

### Optionele velden

| Veld | Beschrijving |
|------|-------------|
| `attributes` | Source-referenties en metadata (`adl.core.*` keys) |
| `resource` | OpenTelemetry resource-object (component-context) |
| `body` | Raw payload (`adl.core.request`, `adl.core.response`, etc.) |

### `event_name` waarden

Elk record correspondeert met één van de vijf AuthZEN APIs:

| AuthZEN API | `event_name` |
|-------------|--------------|
| Access Evaluation API | `adl.access_evaluation` |
| Access Evaluations API | `adl.access_evaluations` |
| Subject Search API | `adl.search_subject` |
| Action Search API | `adl.search_action` |
| Resource Search API | `adl.search_resource` |

### `status` waarden

- `Unset` (default) — PDP heeft geëvalueerd zonder fout. Een denial (`decision: false`) is `Unset`, niet `Error`.
- `Ok` — optionele expliciete markering van succesvolle evaluatie, functioneel gelijk aan `Unset`.
- `Error` — PDP kon geen beslissing produceren (engine fault, missende attributen, downstream timeout).

### `attributes.adl.core.*`

Source-referenties (geen raw data — die hoort in `body`). Een veld MOET in precies één van beide locaties staan.

| Attribute | Beschrijving |
|-----------|-------------|
| `adl.core.request` | Source-referentie naar de input van de beslissing (AuthZEN-formaat) |
| `adl.core.response` | Source-referentie naar de output (verplicht retrieveerbaar bij `status: Unset`/`Ok`) |
| `adl.core.policies` | Object met per policy-source een versie-identifier (timestamp, hash, semver) |
| `adl.core.information` | Referenties naar PIP-data die voor de beslissing is gebruikt |
| `adl.core.configuration` | Configuratie van PDP/PIP/PAP ten tijde van de beslissing |
| `adl.fsc.transaction_id` | FSC transaction-id voor correlatie met FSC logs |

Aanvullende keys buiten `adl.*` mogen worden opgenomen volgens `<vendor>.<area>.<name>`-conventie. Onbekende keys MOETEN zonder fout worden genegeerd door consumers.

### Levels of detail

Vier niveaus van replayability, oplopend in detail:

| Niveau | Bevat | Doel |
|--------|-------|------|
| 1 | Request + response | Basis-accountability |
| 2 | + `adl.core.policies` | Policy-versie reproduceerbaar |
| 3 | + `adl.core.information` | PIP-data reconstrueerbaar (full replayability bij deterministische engine) |
| 4 | + `adl.core.configuration` | Volledige replayability inclusief engine-configuratie |

### Voorbeeld log record (Level 1)

```json
{
  "trace_id": "28dbeec32e77635cc19bc3204ec56c41",
  "span_id": "5e3c8a4f9b2d1e07",
  "parent_span_id": "893e1b2ac52d712f",
  "event_name": "adl.access_evaluation",
  "timestamp": 1757240058042,
  "status": "Unset",
  "attributes": {},
  "body": {
    "adl.core.request": {
      "subject": { "type": "user", "id": "alice" },
      "action": { "name": "approve" },
      "resource": {
        "type": "holiday-request",
        "id": "446epbc8y7",
        "properties": { "employee": "bob" }
      },
      "context": {
        "traceparent": "00-28dbeec32e77635cc19bc3204ec56c41-dec5220770f8f4f4-01"
      }
    },
    "adl.core.response": {
      "decision": false,
      "context": { "reason": { "48": "No signing authority" } }
    }
  }
}
```

### Trace context propagatie

Alle componenten in een autorisatie-evaluatie (PEP, PDP, PIP, PAP) MOETEN W3C Trace Context propageren. De `trace_id` blijft ongewijzigd over organisatiegrenzen heen — een nieuwe `trace_id` mag NIET binnen een lopende beslissingsflow worden gealloceerd. Logging is onafhankelijk van het `sampled`-bit in `traceparent`: ADL-records MOETEN altijd worden geproduceerd, ongeacht sampling.

### Idempotente ingestion

Re-submission van hetzelfde log record (bijvoorbeeld door queue-redelivery in een write-ahead-log patroon) MOET niet leiden tot duplicate records. De idempotency-sleutel is implementatie-specifiek; gangbare keuzes zijn `(trace_id, span_id)` of een content-hash van het record.

---

## Implementatievoorbeelden

### OAuth 2.0 Authorization Code Flow met PKCE (Python)

```python
# Complete example using requests library
import hashlib, base64, secrets, requests

# 1. PKCE code_verifier en code_challenge genereren
code_verifier = secrets.token_urlsafe(64)  # min 43, max 128 chars
code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode()).digest()
).rstrip(b'=').decode()

# 2. Authorization request (redirect user to this URL)
auth_url = "https://auth.example.com/authorize"
params = {
    "client_id": "my-client-id",
    "response_type": "code",
    "scope": "openid profile",
    "redirect_uri": "https://myapp.example.com/callback",
    "state": secrets.token_urlsafe(32),  # min 128 bits entropy
    "code_challenge": code_challenge,
    "code_challenge_method": "S256",
    "acr_values": "http://eidas.europa.eu/LoA/substantial",  # eIDAS level
}
# redirect_url = f"{auth_url}?{'&'.join(f'{k}={v}' for k, v in params.items())}"

# 3. Token request (after receiving authorization code)
token_response = requests.post("https://auth.example.com/token", data={
    "grant_type": "authorization_code",
    "code": "received_auth_code",
    "redirect_uri": "https://myapp.example.com/callback",
    "client_id": "my-client-id",
    "code_verifier": code_verifier,  # PKCE proof
})
tokens = token_response.json()
# tokens = {"access_token": "eyJ...", "token_type": "Bearer", "id_token": "eyJ...", "expires_in": 3600}
```

### Client Credentials Flow met private_key_jwt (Python)

```python
import jwt, time, uuid, requests

# JWT client assertion aanmaken (private_key_jwt authenticatie)
private_key = open("client_private_key.pem").read()

now = int(time.time())
client_assertion = jwt.encode({
    "iss": "my-client-id",
    "sub": "my-client-id",
    "aud": "https://auth.example.com/token",
    "jti": str(uuid.uuid4()),  # uniek per request
    "iat": now,
    "exp": now + 300,  # max 5 minuten geldig
}, private_key, algorithm="PS256", headers={"kid": "my-key-id"})

# Token request met client assertion
response = requests.post("https://auth.example.com/token", data={
    "grant_type": "client_credentials",
    "scope": "api.read api.write",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_assertion": client_assertion,
})
access_token = response.json()["access_token"]
```

### JWT Access Token Validatie (Python)

```python
import jwt, requests

# JWKS ophalen van de authorization server
jwks_url = "https://auth.example.com/.well-known/jwks.json"
jwks = requests.get(jwks_url).json()

# Access token valideren
try:
    payload = jwt.decode(
        access_token,
        jwt.PyJWKClient(jwks_url).get_signing_key_from_jwt(access_token),
        algorithms=["RS256", "PS256"],
        audience="https://api.example.com",  # verwachte audience
        issuer="https://auth.example.com",   # verwachte issuer
        options={
            "verify_exp": True,
            "verify_iat": True,
            "require": ["iss", "sub", "aud", "exp", "jti", "client_id"],
        }
    )
    # Verplichte claims per NL GOV profiel
    assert "client_id" in payload
    assert "jti" in payload  # uniek, niet herbruikbaar
except jwt.ExpiredSignatureError:
    # Token verlopen - nieuwe token ophalen
    pass
except jwt.InvalidTokenError as e:
    # Token ongeldig - toegang weigeren
    pass
```

### OIDC Discovery Endpoint Ophalen (curl)

```bash
# Discovery document ophalen
curl -s https://auth.example.com/.well-known/openid-configuration | jq '{
  issuer,
  authorization_endpoint,
  token_endpoint,
  jwks_uri,
  scopes_supported,
  response_types_supported,
  grant_types_supported,
  acr_values_supported,
  subject_types_supported,
  token_endpoint_auth_methods_supported
}'
```

### FastAPI Resource Server met Token Validatie

```python
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt, requests

app = FastAPI(title="NL GOV Protected Resource", version="1.0.0")
security = HTTPBearer()

JWKS_URL = "https://auth.example.com/.well-known/jwks.json"
ISSUER = "https://auth.example.com"
AUDIENCE = "https://api.example.com"

jwks_client = jwt.PyJWKClient(JWKS_URL)

async def validate_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Valideer OAuth 2.0 NL GOV access token."""
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(credentials.credentials)
        payload = jwt.decode(
            credentials.credentials,
            signing_key,
            algorithms=["RS256", "PS256"],
            audience=AUDIENCE,
            issuer=ISSUER,
        )
        return payload
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

@app.get("/v1/resources")
async def get_resources(token: dict = Depends(validate_token)):
    """Beschermd endpoint - vereist geldig NL GOV OAuth token."""
    return {
        "client_id": token.get("client_id"),
        "sub": token.get("sub"),
        "scope": token.get("scope"),
        "data": [{"id": 1, "name": "Resource"}]
    }
```

## Foutafhandeling

### OAuth 2.0 Error Responses

Het NL GOV profiel volgt RFC 6749 voor error responses:

```json
{
  "error": "invalid_grant",
  "error_description": "The authorization code has expired"
}
```

| Error Code | HTTP Status | Beschrijving |
|-----------|-------------|-------------|
| `invalid_request` | 400 | Verplichte parameter ontbreekt of ongeldig |
| `invalid_client` | 401 | Client authenticatie mislukt (verkeerde client_assertion) |
| `invalid_grant` | 400 | Authorization code verlopen of al gebruikt |
| `unauthorized_client` | 400 | Client niet geautoriseerd voor dit grant type |
| `unsupported_grant_type` | 400 | Grant type niet ondersteund |
| `invalid_scope` | 400 | Scope ongeldig of niet beschikbaar |

### Token Introspection Response

```bash
# Token introspection (voor resource servers die tokens niet zelf kunnen valideren)
curl -X POST https://auth.example.com/introspect \
  -H "Authorization: Bearer $RESOURCE_SERVER_TOKEN" \
  -d "token=$ACCESS_TOKEN" | jq

# Response bij geldig token:
# {"active": true, "scope": "api.read", "client_id": "...", "sub": "...", "exp": 1234567890}
# Response bij ongeldig token:
# {"active": false}
```

## Achtergrondinfo

Zie [reference.md](reference.md) voor SAML-details, OIN-stelsel, en gedetailleerde protocoldocumentatie. Zie [conflicts.md](conflicts.md) voor bekende bronconflicten (GitHub-tags vs. publicatie, Forum Standaardisatie tegenstrijdigheden).
