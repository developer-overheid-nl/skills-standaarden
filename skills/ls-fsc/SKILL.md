---
name: ls-fsc
description: "Gebruik deze skill wanneer de gebruiker vraagt over 'FSC', 'Federated Service Connectivity', 'federatieve dienstverlening', 'inway', 'outway', 'service directory', 'regulated area', 'external contract', 'fsc-core', 'NLX', 'peer', 'PeerID', 'Manager API'."
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - Bash(gh issue list *)
  - Bash(gh pr list *)
  - Bash(gh search *)
  - Bash(curl -s *)
  - WebFetch(*)
---

> **Let op:** De beschrijvingen in deze skill zijn informatieve samenvattingen — niet de officiële standaarden zelf. De definities op [forumstandaardisatie.nl](https://www.forumstandaardisatie.nl/open-standaarden) en [Logius](https://www.logius.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Rijksbrede beleidskader voor generatieve AI](https://www.government.nl/documents/policy-notes/2025/01/31/government-wide-position-on-the-use-of-generative-ai). Zie [DISCLAIMER.md](../../DISCLAIMER.md).

# Federated Service Connectivity (FSC)

**Agent-instructie:** Deze skill helpt bij het implementeren van FSC (Federated Service Connectivity) voor federatieve dienstverlening. FSC gebruikt mTLS, OAuth 2.0 client_credentials en cryptografisch ondertekende contracten. Vereist bij Digikoppeling REST-API (v3.0.1+); geen afzonderlijke vermelding op het Forum Standaardisatie.

## Versiemodel

Net als andere Logius-standaarden kent FSC twee publicatiekanalen (vergelijkbaar met W3C):

- **Vastgestelde versie (DEF)**: officieel goedgekeurd, gepubliceerd op `gitdocumentatie.logius.nl`
- **Werkversie (draft)**: werk-in-uitvoering, gepubliceerd op `logius-standaarden.github.io`

FSC heeft **vastgestelde versies** voor fsc-core en fsc-logging. De overige modules hebben alleen werkversies; fsc-external-contract heeft een consultatieversie (CV). Modulestatus hangt samen met de core-specificatie maar wordt apart vastgesteld.

## Repositories

| Repository | Beschrijving | Vastgesteld | Draft |
|-----------|-------------|------------|-------|
| [fsc-core](https://github.com/logius-standaarden/fsc-core) | Core specificatie: architectuur, protocol, componenten | [v1.1.2](https://gitdocumentatie.logius.nl/publicatie/fsc/core/) | [Draft](https://logius-standaarden.github.io/fsc-core/) |
| [fsc-logging](https://github.com/logius-standaarden/fsc-logging) | Module: logging specificatie voor FSC transacties | [v1.0.0](https://gitdocumentatie.logius.nl/publicatie/fsc/logging/) | [Draft](https://logius-standaarden.github.io/fsc-logging/) |
| [fsc-properties](https://github.com/logius-standaarden/fsc-properties) | Module: metadata-properties voor FSC services | - | [Draft](https://logius-standaarden.github.io/fsc-properties/) |
| [fsc-regulated-area](https://github.com/logius-standaarden/fsc-regulated-area) | Module: Regulated Area specificatie (governance zones) | - | [Draft](https://logius-standaarden.github.io/fsc-regulated-area/) |
| [fsc-external-contract](https://github.com/logius-standaarden/fsc-external-contract) | Module: External Contract specificatie (afspraken tussen partijen) | [CV v1.0.0](https://gitdocumentatie.logius.nl/publicatie/fsc/ext/)¹ | [Draft](https://logius-standaarden.github.io/fsc-external-contract/) |
| [fsc-extensie-template](https://github.com/logius-standaarden/fsc-extensie-template) | Richtlijn voor nieuwe FSC extensies | - | [Draft](https://logius-standaarden.github.io/fsc-extensie-template/) |
| [fsc-test-suite](https://github.com/logius-standaarden/fsc-test-suite) | Integratietests en componenttests | - | - |

¹ CV = consultatieversie, nog niet definitief vastgesteld.

## Service Connectivity Flow

Het proces waarmee een consumer-organisatie een service van een provider-organisatie afneemt verloopt in de volgende stappen:

### Stap 1: Contract aanmaken

De consumer maakt een Contract aan met daarin een **ServiceConnectionGrant**. Dit grant specificeert welke service de consumer wil afnemen en bij welke provider.

### Stap 2: Contract ondertekenen door consumer

De consumer ondertekent het contract cryptografisch met zijn eigen certificaat. De handtekening bevat de certificate thumbprint (SHA-256).

### Stap 3: Contract verzenden naar provider

Het ondertekende contract wordt via de Manager API (`POST /contracts`) naar de Manager van de provider gestuurd.

### Stap 4: Contract ondertekenen door provider

De provider beoordeelt het contract en ondertekent het bij akkoord (`PUT /contracts/{hash}/accept`). Het contract is nu geldig en beide partijen hebben een ondertekend exemplaar.

### Stap 5: Access token verkrijgen

De consumer (via de Outway) vraagt een access token aan bij de Manager van de provider via het **OAuth 2.0 Client Credentials** grant:

```
POST /token HTTP/1.1
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&scope=<GrantHash>
&client_id=<PeerID>
```

- `grant_type`: altijd `client_credentials`
- `scope`: de hash van het specifieke Grant dat de consumer wil gebruiken
- `client_id`: het PeerID van de consumer (afgeleid uit het certificaat)

De Manager valideert de aanvraag, controleert of er een geldig contract bestaat met het opgegeven grant, en geeft een JWT access token terug.

### Stap 6: Verzoek via Outway naar Inway

De Outway van de consumer stuurt het HTTP-verzoek naar de Inway van de provider. Het access token wordt meegegeven in de `Fsc-Authorization` header:

```
GET /service/endpoint HTTP/1.1
Host: inway.provider.example.nl
Fsc-Authorization: Bearer <JWT-token>
```

### Stap 7: Validatie en doorsturen door Inway

De Inway van de provider:

1. Extraheert het JWT uit de `Fsc-Authorization` header
2. Valideert de handtekening van het token
3. Controleert de claims (`aud`, `svc`, `gth`, `gid`, `cnf`)
4. Verifieert dat het certificaat van de verbinding overeenkomt met de `cnf` thumbprint
5. Stuurt het verzoek door naar de achterliggende service
6. Retourneert de response aan de Outway

## Contract & Grant Types

### Contract JSON-structuur

Een contract heeft de volgende structuur (conform fsc-core specificatie):

```json
{
  "content": {
    "fsc_version": "1.0.0",
    "iv": "06338364-8305-7b74-8000-de4963503139",
    "group_id": "nl-overheid-productie",
    "validity": {
      "not_before": 1672527600,
      "not_after": 1704063600
    },
    "grants": [
      {
        "data": {
          "type": "GRANT_TYPE_SERVICE_CONNECTION",
          "service": {
            "type": "SERVICE_TYPE_SERVICE",
            "peer_id": "00000000000000000001",
            "name": "mijn-service"
          },
          "outway": {
            "peer_id": "00000000000000000002",
            "identification": {
              "type": "OUTWAY_IDENTIFICATION_TYPE_PUBLIC_KEY_THUMBPRINT",
              "public_key_thumbprint": "3a56f2e9269ac63f0d4394c46b96539da1625b6a985d38029ff89f34e490960c"
            }
          }
        }
      }
    ],
    "hash_algorithm": "HASH_ALGORITHM_SHA3_512",
    "created_at": 1672527600
  },
  "signatures": {
    "accept": {
      "00000000000000000001": "eyJhbGciOiJSUzUxMiIsIng1dCNTMjU2Ijo...  <JWS compact serialization>",
      "00000000000000000002": "eyJhbGciOiJFUzI1NiIsIng1dCNTMjU2Ijo...  <JWS compact serialization>"
    },
    "reject": {},
    "revoke": {}
  }
}
```

> **Polymorfe velden:** `service` kan ook `SERVICE_TYPE_DELEGATED_SERVICE` zijn (extra veld `delegator`). `outway.identification` kan ook `OUTWAY_IDENTIFICATION_TYPE_DOMAIN_NAME` zijn (veld `domain_name`). Grants kunnen optioneel een `properties`-object bevatten. Zie de [fsc-core OpenAPI spec](https://github.com/logius-standaarden/fsc-core/blob/develop/media/specs/manager.yaml) voor het volledige schema.

### Grant Types

| Grant Type | Gebruik | Partijen |
|-----------|---------|----------|
| **ServicePublicationGrant** | Service publiceren in Directory | Provider + Directory |
| **DelegatedServicePublicationGrant** | Service publiceren namens andere Peer | Gemachtigde + Eigenaar + Directory |
| **ServiceConnectionGrant** | Toegang tot service (meest gebruikt) | Consumer + Provider |
| **DelegatedServiceConnectionGrant** | Toegang namens andere consumer | Gemachtigde + Consumer + Provider |

## Access Token (JWT)

Het access token is een JSON Web Token (JWT) dat wordt uitgegeven door de Manager van de provider. Het token bevat de volgende claims:

| Claim | Beschrijving |
|-------|-------------|
| `sub` | Subject: het PeerID van de consumer die de service afneemt |
| `iss` | Issuer: het PeerID van de provider die het token uitgeeft |
| `svc` | Service: de naam van de service waarvoor het token geldig is |
| `aud` | Audience: de URL van de Inway van de provider |
| `gth` | Grant Hash: de hash van het specifieke grant in het contract |
| `gid` | Group ID: identifier van de Group waarbinnen het token geldig is |
| `cnf` | Confirmation: object met `x5t#S256` (SHA-256 thumbprint van het client-certificaat) |
| `exp` | Expiration: verloopdatum van het token |
| `nbf` | Not Before: tijdstip vanaf wanneer het token geldig is |

De `cnf` claim bindt het token aan het specifieke certificaat van de consumer, waardoor token-diefstal wordt voorkomen (certificate-bound tokens).

```json
{
  "sub": "PeerID-consumer",
  "iss": "PeerID-provider",
  "svc": "mijn-service",
  "aud": "https://inway.provider.example.nl",
  "gth": "sha256-hash-van-grant",
  "gid": "nl-overheid-productie",
  "cnf": {
    "x5t#S256": "sha256-thumbprint-van-client-certificaat"
  },
  "exp": 1735689600,
  "nbf": 1735686000
}
```

## Manager API Endpoints

De Manager biedt de volgende REST API endpoints:

### Peer-beheer

| Methode | Endpoint | Beschrijving |
|---------|----------|-------------|
| `PUT` | `/announce` | Registreer of update een Peer in het netwerk. Bevat informatie over de Peer zoals naam, Inway-adres en beschikbare services. |
| `GET` | `/peer` | Haal informatie op over de eigen Peer (self-discovery). |
| `GET` | `/peers` | Lijst van alle bekende Peers in het netwerk. |

### Contract-beheer

| Methode | Endpoint | Beschrijving |
|---------|----------|-------------|
| `POST` | `/contracts` | Dien een nieuw (ondertekend) contract in bij de tegenpartij. |
| `GET` | `/contracts` | Haal alle contracten op (met optionele filters). |
| `PUT` | `/contracts/{hash}/accept` | Accepteer een contract door het te ondertekenen. |
| `PUT` | `/contracts/{hash}/reject` | Wijs een contract af. |
| `PUT` | `/contracts/{hash}/revoke` | Trek een eerder geaccepteerd contract in. |

### Token-uitgifte

| Methode | Endpoint | Beschrijving |
|---------|----------|-------------|
| `POST` | `/token` | Vraag een access token aan via OAuth 2.0 Client Credentials. Vereist `grant_type`, `scope` (GrantHash) en `client_id` (PeerID). |

### Service-discovery

| Methode | Endpoint | Beschrijving |
|---------|----------|-------------|
| `GET` | `/services` | Lijst van alle gepubliceerde services (beschikbaar op de Directory). |

## Netwerkconfiguratie

### Poorten

FSC definieert twee poorten voor verschillende typen verkeer:

| Poort | Gebruik | Beschrijving |
|-------|---------|-------------|
| **443** | Dataverkeer | Standaardpoort voor service-aanroepen tussen Outway en Inway. Draagt de eigenlijke API-verzoeken en responses. |
| **8443** | Managementverkeer | Poort voor communicatie tussen Managers onderling en tussen Outways en Managers. Gebruikt voor contractbeheer, tokenuitgifte en peer-discovery. |

### HTTP-vereisten

- **HTTP/1.1** is verplicht als minimale versie voor alle FSC-verbindingen
- **HTTP/2** is optioneel en mag worden ondersteund als aanvulling
- **TLS** is verplicht; de minimale TLS-versie wordt bepaald door de Group Rules (in de praktijk minimaal TLS 1.2)
- **mTLS** is verplicht: zowel client als server presenteren een certificaat

## Logging Extensie

De FSC Logging extensie (`fsc-logging`) beschrijft hoe transactielogs worden vastgelegd voor audit- en verantwoordingsdoeleinden.

### Transactie-ID

Elk verzoek krijgt een uniek **transaction_id** mee via de `Fsc-Transaction-Id` HTTP header. Dit ID wordt door alle componenten in de keten doorgegeven, zodat een volledig pad van consumer naar provider en terug traceerbaar is.

```
GET /service/endpoint HTTP/1.1
Fsc-Authorization: Bearer <JWT-token>
Fsc-Transaction-Id: 550e8400-e29b-41d4-a716-446655440000
```

### Logvelden

Elk transactielog bevat minimaal de volgende velden:

| Veld | Beschrijving |
|------|-------------|
| `transaction_id` | Uniek ID van de transactie (UUID), corresponderend met de `Fsc-Transaction-Id` header |
| `direction` | Richting van het verzoek: `in` (ontvangen) of `out` (verzonden) |
| `grant_hash` | Hash van het grant dat is gebruikt voor autorisatie |
| `source` | PeerID van de verzendende partij |
| `destination` | PeerID van de ontvangende partij |
| `timestamp` | Tijdstip van het logmoment |
| `service` | Naam van de aangeroepen service |

### Logging per component

- **Outway**: logt uitgaande verzoeken met `direction: out`, het gebruikte grant en de bestemming
- **Inway**: logt inkomende verzoeken met `direction: in`, het gevalideerde grant en de bron
- Beide componenten loggen dezelfde `transaction_id`, waardoor correlatie mogelijk is

## Implementatievoorbeelden

### Outway Proxy (Python/FastAPI)

```python
from fastapi import FastAPI, Request, Response
import requests, jwt, time, uuid

app = FastAPI(title="FSC Outway Proxy")

MANAGER_URL = "https://manager.example.com:8443"
MTLS_CERT = ("pkio_cert.pem", "pkio_key.pem")
CA_BUNDLE = "pkio_ca_chain.pem"

# Token cache per grant_hash
token_cache: dict[str, dict] = {}

def get_access_token(grant_hash: str, peer_id: str) -> str:
    """Haal access token op van de Manager (OAuth 2.0 Client Credentials)."""
    cached = token_cache.get(grant_hash)
    if cached and cached["exp"] > time.time():
        return cached["token"]

    response = requests.post(
        f"{MANAGER_URL}/token",
        data={
            "grant_type": "client_credentials",
            "scope": grant_hash,
            "client_id": peer_id,
        },
        cert=MTLS_CERT,
        verify=CA_BUNDLE,
    )
    response.raise_for_status()
    token_data = response.json()
    token_cache[grant_hash] = {
        "token": token_data["access_token"],
        "exp": jwt.decode(token_data["access_token"], options={"verify_signature": False})["exp"]
    }
    return token_data["access_token"]

@app.api_route("/{service_name}/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def proxy_request(service_name: str, path: str, request: Request):
    """Proxy verzoeken naar een service via FSC Inway."""
    grant_hash = resolve_grant_hash(service_name)  # uit lokale contracten
    inway_url = resolve_inway_url(service_name)     # uit directory

    access_token = get_access_token(grant_hash, "mijn-oin")

    # Forward request naar Inway met Fsc-Authorization header
    response = requests.request(
        method=request.method,
        url=f"{inway_url}/{service_name}/{path}",
        headers={
            "Fsc-Authorization": f"Bearer {access_token}",
            "Fsc-Transaction-Id": str(uuid.uuid4()),  # Uniek per request
            **{k: v for k, v in request.headers.items()
               if k.lower() not in ("host", "fsc-authorization")},
        },
        data=await request.body(),
        cert=MTLS_CERT,
        verify=CA_BUNDLE,
    )

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers),
    )
```

### Inway Token Validatie (Python)

```python
import jwt
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives.hashes import SHA256
import base64

def base64url_encode(data: bytes) -> str:
    """Encode bytes als base64url (zonder padding)."""
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('ascii')

def validate_fsc_token(token: str, client_cert_pem: bytes, group_id: str, manager_public_key) -> dict:
    """Valideer een FSC access token op de Inway."""
    # 1. Decode token (signature verificatie met Manager's publieke sleutel)
    payload = jwt.decode(token, manager_public_key, algorithms=["RS256", "PS256"])

    # 2. Controleer group_id
    if payload["gid"] != group_id:
        raise ValueError(f"Verkeerde group_id: {payload['gid']}")

    # 3. Controleer certificate binding (RFC 8705)
    cert = load_pem_x509_certificate(client_cert_pem)
    cert_thumbprint = base64url_encode(cert.fingerprint(SHA256()))
    if payload["cnf"]["x5t#S256"] != cert_thumbprint:
        raise ValueError("Certificate thumbprint komt niet overeen met token")

    # 4. Controleer service bestaat
    registered_services = ["service1", "service2"]  # uit configuratie
    if payload["svc"] not in registered_services:
        raise ValueError(f"Service niet gevonden: {payload['svc']}")

    # 5. Controleer expiratie (standaard JWT)
    # jwt.decode doet dit automatisch met verify_exp=True

    return payload
```

### Contract Aanmaken en Ondertekenen (curl)

De Manager API (`POST /contracts`) verwacht `content` (verplicht) en `signature` (JWS string). De Manager berekent en valideert de signature op basis van het certificaat waarmee de mTLS-verbinding is opgezet.

```bash
# Stap 1: Contract indienen door consumer bij eigen Manager
# De Manager genereert de JWS-signature op basis van het mTLS-certificaat
curl -X POST https://consumer-manager.example.com:8443/v1/contracts \
  --cert pkio_cert.pem --key pkio_key.pem --cacert pkio_ca_chain.pem \
  -H "Content-Type: application/json" \
  -H "Fsc-Manager-Address: https://consumer-manager.example.com:8443" \
  -d '{
    "content": {
      "fsc_version": "1.0.0",
      "iv": "06338364-8305-7b74-8000-de4963503139",
      "group_id": "nl-overheid-productie",
      "validity": {
        "not_before": 1704067200,
        "not_after": 1735689600
      },
      "grants": [{
        "data": {
          "type": "GRANT_TYPE_SERVICE_CONNECTION",
          "service": {
            "type": "SERVICE_TYPE_SERVICE",
            "peer_id": "00000001234567890000",
            "name": "brp-bevraging"
          },
          "outway": {
            "peer_id": "00000001823288444000",
            "identification": {
              "type": "OUTWAY_IDENTIFICATION_TYPE_PUBLIC_KEY_THUMBPRINT",
              "public_key_thumbprint": "3a56f2e9269ac63f0d4394c46b96539da1625b6a985d38029ff89f34e490960c"
            }
          }
        }
      }],
      "hash_algorithm": "HASH_ALGORITHM_SHA3_512",
      "created_at": 1704067200
    },
    "signature": "eyJhbGciOiJSUzUxMiIsIng1dCNTMjU2Ijo..."
  }'
# Response: 201 Created

# Stap 2: Contract accepteren door provider via zijn Manager
# De accept endpoint vereist zowel content als signature (signatureRequest schema)
CONTRACT_HASH="<hash uit stap 1 response>"
curl -X PUT "https://provider-manager.example.com:8443/v1/contracts/${CONTRACT_HASH}/accept" \
  --cert pkio_cert.pem --key pkio_key.pem --cacert pkio_ca_chain.pem \
  -H "Content-Type: application/json" \
  -H "Fsc-Manager-Address: https://provider-manager.example.com:8443" \
  -d '{
    "content": { <dezelfde contract content als in stap 1> },
    "signature": "eyJhbGciOiJSUzUxMiIsIng1dCNTMjU2Ijo..."
  }'
# Response: 201 Signature created
```

> **Let op:** De `signature`-waarden zijn JWS tokens (RFC7515) die een hash van de contract-content bevatten, ondertekend met het PKIoverheid-certificaat. De JWS payload bevat `contract_content_hash`, `type` ("accept"/"reject"/"revoke") en `signed_at`. Het volledige algoritme staat in de [fsc-core specificatie](https://gitdocumentatie.logius.nl/publicatie/fsc/core/), sectie Signatures.

### Service Discovery via Directory (curl)

```bash
# Beschikbare services ophalen
curl -s https://directory.example.com:8443/services \
  --cert pkio_cert.pem --key pkio_key.pem --cacert pkio_ca_chain.pem | jq

# Peers in de groep ophalen
curl -s https://directory.example.com:8443/peers \
  --cert pkio_cert.pem --key pkio_key.pem --cacert pkio_ca_chain.pem | jq

# Specifieke service details
curl -s "https://directory.example.com:8443/services?name=brp-bevraging" \
  --cert pkio_cert.pem --key pkio_key.pem --cacert pkio_ca_chain.pem | jq
```

## Foutafhandeling

### Inway Error Codes

| HTTP Status | Fsc-Error-Code | Beschrijving | Actie |
|------------|---------------|-------------|-------|
| 401 | `ERROR_CODE_ACCESS_TOKEN_MISSING` | Geen Fsc-Authorization header | Voeg token toe via Outway |
| 401 | `ERROR_CODE_ACCESS_TOKEN_INVALID` | Token handtekening ongeldig | Nieuw token ophalen |
| 401 | `ERROR_CODE_ACCESS_TOKEN_EXPIRED` | Token verlopen | Nieuw token ophalen |
| 403 | `ERROR_CODE_WRONG_GROUP_ID_IN_TOKEN` | Group ID in token matcht niet | Controleer groepsconfiguratie |
| 404 | `ERROR_CODE_SERVICE_NOT_FOUND` | Service niet geregistreerd | Controleer servicenaam in contract |
| 502 | `ERROR_CODE_SERVICE_UNREACHABLE` | Achterliggende service onbereikbaar | Probeer later opnieuw |

### Error Response Formaat

```json
{
  "code": "ERROR_CODE_ACCESS_TOKEN_EXPIRED",
  "domain": "ERROR_DOMAIN_INWAY",
  "message": "Token expired at 2024-01-15T10:30:00Z"
}
```

De `Fsc-Error-Code` header wordt altijd meegegeven bij foutresponses, naast de HTTP status code.

### Outway Error Code

| HTTP Status | Fsc-Error-Code | Beschrijving |
|------------|---------------|-------------|
| 405 | `ERROR_CODE_METHOD_UNSUPPORTED` | CONNECT methode niet ondersteund |

## Achtergrondinfo

Zie [reference.md](reference.md) voor componentarchitectuur, trust model, retry-strategie (exponential backoff), en protocoldocumentatie. Zie [conflicts.md](conflicts.md) voor bronconflicten.
