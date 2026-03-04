---
name: ls-api
description: "Gebruik deze skill wanneer de gebruiker vraagt over 'API Design Rules', 'ADR', 'REST API standaard', 'API richtlijnen', 'NL GOV API', 'Spectral linter', 'API linter', 'OpenAPI validatie', 'API design', 'REST API naming', 'transport security', 'API signing', 'API encryption', 'geospatial API', 'api-linter', 'problem+json', 'error response format'."
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - Bash(gh issue list *)
  - Bash(gh pr list *)
  - Bash(gh search *)
  - Bash(curl -s *)
  - Bash(npx @stoplight/spectral-cli *)
  - WebFetch(*)
---

> **Let op:** De beschrijvingen in deze skill zijn informatieve samenvattingen — niet de officiële standaarden zelf. De definities op [forumstandaardisatie.nl](https://www.forumstandaardisatie.nl/open-standaarden) en [Logius](https://www.logius.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Rijksbrede beleidskader voor generatieve AI](https://www.government.nl/documents/policy-notes/2025/01/31/government-wide-position-on-the-use-of-generative-ai). Zie [DISCLAIMER.md](../../DISCLAIMER.md).

# API Design Rules (NL GOV)

**Agent-instructie:** Deze skill helpt bij het implementeren van APIs conform de NL GOV API Design Rules. Gebruik de Spectral linter om OpenAPI specs te valideren. De regels zijn verplicht onder ['pas-toe-of-leg-uit'](https://www.forumstandaardisatie.nl/open-standaarden/rest-api-design-rules) van het Forum Standaardisatie.

De API Design Rules (ADR) zijn de Nederlandse standaard voor het ontwerpen van RESTful APIs bij de overheid. Ze zijn verplicht onder het "pas-toe-of-leg-uit" regime van het Forum Standaardisatie. De standaard bevat concrete, toetsbare regels voor URI-ontwerp, HTTP-methoden, versiebeheer, beveiliging, foutafhandeling en meer.

## Versiemodel

De ADR kent twee publicatiekanalen (vergelijkbaar met W3C-standaarden):

- **Vastgestelde versie (DEF)**: de officieel goedgekeurde versie, gepubliceerd op `gitdocumentatie.logius.nl`
- **Werkversie (draft)**: de ontwikkeling richting de volgende release, gepubliceerd op `logius-standaarden.github.io`. De werkversie op GitHub Pages is de lopende ontwikkeling richting de volgende release. De ReSpec-configuratie toont daar nog '2.1.0' maar dit betreft werk-in-uitvoering.

Modules hebben geen eigen vaststellingsproces — ze ontlenen hun status aan de standaard die ernaar verwijst. Als de ADR in een vastgestelde versie normatief naar een module verwijst, is die module daarmee ook vastgesteld. Zo is de Geospatial module v1.0.x normatief onderdeel van ADR v2.1.0 en daarmee vastgesteld. De inhoud van Transport Security is in ADR v2.1.0 ingebed als sectie 3.8 met eigen regels (`/core/transport/*`). De module v1.0 staat nog normatief vermeld in de leeswijzer van v2.1.0, maar de GitHub-repository is gearchiveerd.

## Repositories

| Repository | Beschrijving | Vastgesteld | Draft |
|-----------|-------------|------------|-------|
| [API-Design-Rules](https://github.com/logius-standaarden/API-Design-Rules) | Hoofdspecificatie (ADR) | [v2.1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr/2.1.0/) | [Draft](https://logius-standaarden.github.io/API-Design-Rules/) |
| [ADR-Beheermodel](https://github.com/logius-standaarden/ADR-Beheermodel) | Beheermodel voor de ADR standaard — **gearchiveerd**, vervangen door API-Standaarden-Beheermodel | [v1.0](https://gitdocumentatie.logius.nl/publicatie/api/adr-beheer/1.0/) | - |
| [API-Standaarden-Beheermodel](https://github.com/logius-standaarden/API-Standaarden-Beheermodel) | Overkoepelend beheermodel API-standaarden | - | [Draft](https://logius-standaarden.github.io/API-Standaarden-Beheermodel/) |
| [API-mod-geospatial](https://github.com/logius-standaarden/API-mod-geospatial) | Module: Geospatial (GeoJSON, CRS) — normatief in ADR v2.1.0 | [v1.0.3](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3/) | [Draft](https://logius-standaarden.github.io/API-mod-geospatial/) |
| [API-mod-transport-security](https://github.com/logius-standaarden/API-mod-transport-security) | Module: Transport Security — **gearchiveerd**; inhoud ingebed in ADR v2.1.0; normatief vermeld in leeswijzer; repo gearchiveerd | - | - |
| [API-mod-signing](https://github.com/logius-standaarden/API-mod-signing) | Module: HTTP Message Signing — draft | - | [Draft](https://logius-standaarden.github.io/API-mod-signing/) |
| [API-mod-encryption](https://github.com/logius-standaarden/API-mod-encryption) | Module: Encryption (JWE) — draft | - | [Draft](https://logius-standaarden.github.io/API-mod-encryption/) |
| [api-linter-impactanalyse](https://github.com/logius-standaarden/api-linter-impactanalyse) | Python tool: test Spectral regels tegen echte OpenAPI specs uit het API-register | - | - |
| [zaakgericht-werken-api](https://github.com/logius-standaarden/zaakgericht-werken-api) | API-specificatie voor zaakgericht werken | - | - |

## Technische Regels

### URI-ontwerp

- Gebruik **kebab-case** voor padsegmenten: `/mijn-documenten` (niet `/mijnDocumenten`)
- Gebruik **camelCase** voor query-parameters: `?sortOrder=desc`
- Geen trailing slashes: `/api/v1/users` (niet `/api/v1/users/`)
- Geen bestandsextensies (gebruik Accept-header voor content negotiation)
- Major versie in URI: `/v1/resources`
- Operaties als sub-resources: laatste padsegment mag starten met `_` (bijv. `/_search`)
- Geen gevoelige informatie in URIs (niet beschermd door TLS)

### HTTP-methoden

| Methode | Gebruik | Veilig | Idempotent |
|---------|--------|--------|------------|
| GET | Resource ophalen, nooit wijzigen | Ja | Ja |
| POST | Subresource aanmaken in collectie | Nee | Nee |
| PUT | Resource aanmaken of volledig vervangen | Nee | Ja |
| PATCH | Gedeeltelijke update | Nee | Nee |
| DELETE | Resource verwijderen | Nee | Ja |

### Versiebeheer

- Major versie in URI-pad: `/v1`, `/v2`
- Volledige versie in `API-Version` response header: `1.2.3`
- Semantic versioning (major.minor.patch) in `info.version`
- Deprecation schedule publiceren bij major version changes
- Vaste transitieperiode tussen major versies

### Foutafhandeling

Gebruik `application/problem+json` (RFC 9457) voor foutresponses:

```json
{
  "type": "https://example.com/errors/insufficient-funds",
  "title": "Insufficient Funds",
  "status": 422,
  "detail": "Your current balance is 30, but that costs 50.",
  "instance": "/account/12345/transactions/abc"
}
```

Geen technische details (stack traces, interne hints) in foutmeldingen.

### Naamgeving

- Resources als **zelfstandige naamwoorden** (niet werkwoorden)
- **Meervoud** voor collecties: `/users`, `/orders`
- **Enkelvoud** voor individuele resources: `/users/{id}`
- Definieer interfaces in het **Nederlands** tenzij er een officieel Engelstalig begrippenkader bestaat
- Verberg implementatiedetails (geen framework- of databasenamen)

### OpenAPI Documentatie

- OpenAPI 3.0+ specificatie verplicht
- Publiceer JSON op standaardlocatie: `/openapi.json` (VERPLICHT); YAML (`/openapi.yaml`) is OPTIONEEL
- Contactinformatie verplicht (name, email, url)
- CORS ondersteunen voor documentatie-toegang

## Modules

### Transport Security (TLS)

> **Let op:** De Transport Security module werd als aparte module normatief verwezen door ADR v2.0.0. Vanaf ADR v2.1.0 zijn de transport-security-eisen **ingebed in de hoofdspecificatie** (sectie 3.8, regels `/core/transport/*`) en is de [repository gearchiveerd](https://github.com/logius-standaarden/API-mod-transport-security). De module v1.0 staat nog normatief vermeld in de leeswijzer van ADR v2.1.0.

Alle verbindingen MOETEN TLS gebruiken (wettelijk verplicht). Volg de laatste NCSC-richtlijnen.

Verplichte security headers in alle API-responses:

| Header | Doel |
|--------|------|
| `Cache-Control: no-store` | Voorkom caching van gevoelige data |
| `Content-Security-Policy: frame-ancestors 'none'` | Clickjacking bescherming |
| `Content-Type: application/json` | Specificeer content type |
| `Strict-Transport-Security` | Vereis HTTPS |
| `X-Content-Type-Options: nosniff` | Voorkom MIME sniffing |
| `X-Frame-Options: DENY` | Clickjacking bescherming |
| `Access-Control-Allow-Origin` | CORS beleid |

### Geospatial Module (v1.0.3 — vastgesteld)

Normatief onderdeel van ADR v2.1.0. Verplicht bij geospatiale data. Regelt GeoJSON encodering, bounding box filtering, en coördinaatsystemen (CRS). Zie de [vastgestelde versie](https://gitdocumentatie.logius.nl/publicatie/api/mod-geo/1.0.3/).

### Signing Module (JAdES) — draft

> **Let op:** Deze module is nog in **concept** (draft) en is nog niet goedgekeurd door het Technisch Overleg. De inhoud kan nog wijzigen.

Voor end-to-end berichtintegriteit en authenticiteit. Gebruikt JAdES detached signatures met RSASSA-PSS (PS256), minimaal 256 bits. Signatures in `Payload-Signature` en `Message-Signature` HTTP headers. OpenAPI representatie met `format: jws-compact-detached`.

### Encryption Module (JWE) — draft

> **Let op:** Deze module is nog in **concept** (draft) en is nog niet goedgekeurd door het Technisch Overleg. De inhoud kan nog wijzigen.

Voor end-to-end versleuteling van request/response payloads wanneer transport-level encryptie niet voldoende is (bijv. bij niet-vertrouwde intermediairs).

## Implementatievoorbeeld

### Python/FastAPI

```python
from fastapi import FastAPI, Query, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import date

app = FastAPI(
    openapi_url="/v1/openapi.json",
    title="Zaakgericht Werken API",
    version="1.2.0",
    contact={"name": "API Team", "url": "https://example.com/support", "email": "api@example.com"},
    servers=[{"url": "https://api.example.com"}],
)

class Zaak(BaseModel):
    id: str
    zaaktype: str
    omschrijving: str
    startdatum: date
    status: str

@app.middleware("http")
async def add_adr_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["API-Version"] = "1.2.0"
    response.headers["Content-Type"] = "application/json"
    response.headers["Cache-Control"] = "no-store"
    response.headers["Strict-Transport-Security"] = "max-age=31536000"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "frame-ancestors 'none'"
    return response

@app.get("/v1/zaken", response_model=list[Zaak])
async def list_zaken(
    status: str | None = Query(None, description="Filter op status"),
    startdatum__gte: date | None = Query(None, alias="startdatumGte", description="Vanaf datum"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100, alias="pageSize"),
):
    """Haal zaken op met paginering en filtering (ADR-compliant)."""
    # Paginering met standaard page_size=20, max 100
    offset = (page - 1) * page_size
    return db.query_zaken(status=status, since=startdatum__gte, offset=offset, limit=page_size)

@app.exception_handler(HTTPException)
async def problem_json_handler(request: Request, exc: HTTPException):
    """RFC 9457 problem+json (verplicht per ADR)."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "type": f"https://api.example.com/errors/{exc.status_code}",
            "title": exc.detail if isinstance(exc.detail, str) else "Error",
            "status": exc.status_code,
            "instance": str(request.url),
        },
        media_type="application/problem+json",
    )
```

## Implementatie Checklist

- [ ] OpenAPI 3.0+ spec op `/openapi.json` (VERPLICHT); `/openapi.yaml` is optioneel
- [ ] Contactinformatie in spec
- [ ] Major versie in URI-pad (`/v1`)
- [ ] Volledige versie in `API-Version` response header
- [ ] Semantic versioning in `info.version`
- [ ] Kebab-case paden, camelCase query-parameters
- [ ] Geen trailing slashes
- [ ] Verplichte security headers
- [ ] TLS op alle verbindingen
- [ ] `application/problem+json` voor foutresponses
- [ ] Geen gevoelige data in URIs
- [ ] CORS geconfigureerd

## Spectral Linter

De Spectral linter valideert OpenAPI specs tegen ADR regels. De DON-hosted ruleset bevat 11 regels; de GitHub-versie bevat 17 regels (inclusief extra checks zoals `query-keys-camel-case`, `semver` en `info-contact`).

```bash
# Optie 1: Publieke DON-hosted ruleset (geen GitHub auth nodig, aanbevolen)
npx @stoplight/spectral-cli lint <jouw-spec.yaml> \
  --ruleset https://static.developer.overheid.nl/adr/ruleset.yaml

# Optie 2: Ruleset ophalen via GitHub API
gh api repos/logius-standaarden/API-Design-Rules/contents/media/linter.yaml \
  -H "Accept: application/vnd.github.raw" > /tmp/adr-linter.yaml
npx @stoplight/spectral-cli lint <jouw-spec.yaml> --ruleset /tmp/adr-linter.yaml

# Bekijk beschikbare regels (DON-versie)
curl -s https://static.developer.overheid.nl/adr/ruleset.yaml | grep -oE "^\s{2}\S+:" | sed 's/^\s*//;s/:$//'

# Linter testcases bekijken
gh api repos/logius-standaarden/API-Design-Rules/contents/linter/testcases --jq '.[].name'
```

Belangrijke Spectral regels (DON-naam / GitHub-naam):
- `include-major-version-in-uri` / `nlgov:include-major-version-in-uri` - Major versie in URI pad
- `paths-no-trailing-slash` / `nlgov:paths-no-trailing-slash` - Geen trailing slashes
- `paths-kebab-case` / `nlgov:paths-kebab-case` - Kebab-case padsegmenten
- `http-methods` / `nlgov:http-methods` - Alleen standaard HTTP methoden
- `missing-version-header` / `nlgov:missing-version-header` - Version header in 2xx/3xx responses
- `use-problem-schema` / `nlgov:use-problem-schema` - Problem+json voor fouten

Alleen in de GitHub-versie (17 regels totaal, 6 extra t.o.v. DON):
- `nlgov:query-keys-camel-case` - camelCase query parameters
- `nlgov:info-contact-fields-exist` - Contactinformatie velden aanwezig
- `info-contact` - Contactobject aanwezig (zonder `nlgov:` prefix)
- `nlgov:semver` - Semantic versioning formaat
- `nlgov:openapi-root-exists` - OpenAPI root object aanwezig
- `oas3-api-servers` - Servers array aanwezig (built-in regel op error gezet)

## Achtergrondinfo

Zie [reference.md](reference.md) voor Express.js/Go voorbeelden, impact analyse tool, en repo-exploratie commando's. Zie [conflicts.md](conflicts.md) voor bekende discrepanties tussen GitHub-tags en gepubliceerde versies.
