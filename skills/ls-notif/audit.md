<!-- markdownlint-disable MD052 MD034 MD013 MD038 -->
# Audit ls-notif — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 5 | 20% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 10 | 40% |
| UNGROUNDED | 2 | 8% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 8 | 32% |

*Geverifieerd met sonnet, 11 calls, $0.8515.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (5)

### `ls-notif-0009` — SKILL.md:69 *(§ Optionele attributen)*

> Het `time` attribuut is het tijdstip van logging/registratie van het event in RFC 3339 formaat, niet noodzakelijk het moment van de werkelijke gebeurtenis.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profile for CloudEvents - optionele attributen

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc3339.txt](https://www.rfc-editor.org/rfc/rfc3339.txt)
  - *De bron is RFC 3339 zelf, die het datum/tijdformaat definieert. De claim gaat over hoe CloudEvents het `time` attribuut semantisch invult (logging/registratie vs. werkelijke gebeurtenis). RFC 3339 bevat geen informatie over CloudEvents of de betekenis van specifieke attributen daarin.*

### `ls-notif-0013` — SKILL.md:76 *(§ Notificatieservices API)*

> De Notificatieservices API is gespecificeerd als OpenAPI 3.x en biedt een centraal endpoint voor het publiceren van events.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Notificatieservices API

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *De bron bevat geen informatie over een Notificatieservices API, OpenAPI 3.x specificatie of een centraal endpoint voor het publiceren van events.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bespreekt technologieën en aanbevelingen, maar bevat geen specificatie van een Notificatieservices API als OpenAPI 3.x met een centraal endpoint.*

### `ls-notif-0015` — SKILL.md:108 *(§ Abonneren)*

> De huidige Notificatieservices OpenAPI-specificatie bevat alleen push-endpoints voor events (`POST /events`); er zijn geen pull/polling-endpoints voor het ophalen van events.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Notificatieservices API

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *De bron bevat geen informatie over een OpenAPI-specificatie met endpoints zoals POST /events of pull/polling-endpoints.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen beschrijving van een OpenAPI-specificatie met specifieke endpoints zoals `POST /events` of het ontbreken van pull/polling-endpoints.*

### `ls-notif-0020` — reference.md:50 *(§ Authenticatie en autorisatie)*

> De Notificatieservices API maakt gebruik van JWT Bearer Tokens voor authenticatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Notificatieservices API - authenticatie

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *De bron bevat geen informatie over JWT Bearer Tokens of authenticatiemechanismen voor de Notificatieservices API.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron noemt OAuth/OIDC in algemene zin als onderdeel van security-aandachtspunten, maar bevat geen specificatie dat de Notificatieservices API JWT Bearer Tokens gebruikt voor authenticatie.*

### `ls-notif-0023` — reference.md:17 *(§ Type Systeem)*

> CloudEvents definieert het Timestamp type als datum en tijd conform RFC 3339.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** CloudEvents type systeem

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc3339.txt](https://www.rfc-editor.org/rfc/rfc3339.txt)
  - *De bron is RFC 3339 zelf. De claim gaat over hoe CloudEvents het Timestamp type definieert en welke standaard het daarvoor gebruikt. RFC 3339 bevat geen informatie over CloudEvents of de typedefinities daarin.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (10)

### `ls-notif-0001` — SKILL.md:34 *(§ Versiemodel)*

> Het NL GOV profiel voor CloudEvents heeft een vastgestelde versie (v1.1 DEF).

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profile for CloudEvents

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > NL GOV profile for CloudEvents 1.1 Notificatieservices Logius Standard Definitive version March 17, 2026
  - *De bron bevestigt een definitieve versie 1.1, maar de claim zegt 'v1.1 DEF' als aanduiding. De versie en definitieve status kloppen, de exacte afkorting 'DEF' staat er niet in maar is een redelijke parafrase.*

### `ls-notif-0002` — SKILL.md:36 *(§ Versiemodel)*

> Op het Forum Standaardisatie staat CloudEvents v1.0 als verplicht ('pas-toe-of-leg-uit'), goedgekeurd OBDO 25-11-2025.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Forum Standaardisatie / NL GOV profile for CloudEvents

- **PARTIALLY_SUPPORTED** (medium) — [https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-profile-cloudevents](https://www.forumstandaardisatie.nl/open-standaarden/nl-gov-profile-cloudevents)
  > Verplicht ('Pas toe leg uit') [...] Versie 1.1 [...] Specificatiedocument NL GOV profile for CloudEvents 1.0
  - *De bron bevestigt dat de standaard op de 'Pas toe of leg uit'-lijst staat (verplicht), wat de status-claim ondersteunt. Echter: de versie in de registratie is 1.1 (niet 1.0), al verwijst het specificatiedocument naar versie 1.0. De datum van OBDO-goedkeuring (25-11-2025) staat niet in de brontekst; de Forumadvies-datum suggereert 20250924 (september 2025), maar een expliciete OBDO-datum ontbreekt volledig. De claim is dus deels ondersteund (verplicht-status) maar de specifieke versie en OBDO-datum kunnen niet worden bevestigd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *De bron bevat geen informatie over Forum Standaardisatie, pas-toe-of-leg-uit status, OBDO of goedkeuringsdatum 25-11-2025.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De brontekst vermeldt CloudEvents en het NL GOV-profiel, maar bevat geen informatie over Forum Standaardisatie, de 'pas-toe-of-leg-uit' status, of een OBDO-goedkeuring op 25-11-2025.*

### `ls-notif-0003` — SKILL.md:47 *(§ Repositories)*

> Abonneren WV v0.0.1 is gepubliceerd op gitdocumentatie.logius.nl maar is nog niet vastgesteld.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Abonneren standaard

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  > Dit is een werkversie die op elk moment kan worden gewijzigd, verwijderd of vervangen door andere documenten. Het is geen door het TO goedgekeurde consultatieversie.
  - *De bron bevestigt dat het document een werkversie is op gitdocumentatie.logius.nl en niet is vastgesteld. Het versienummer v0.0.1 wordt echter niet expliciet vermeld in de brontekst.*
<details><summary>7x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *De bron bevat geen informatie over 'Abonneren WV v0.0.1' of publicatiestatus daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents](https://github.com/logius-standaarden/NL-GOV-profile-for-CloudEvents)
  - *De brontekst betreft de GitHub-repository van het NL-GOV-profile-for-CloudEvents. Er wordt geen melding gemaakt van een 'Abonneren' standaard, werkversie v0.0.1, of gitdocumentatie.logius.nl. De enige release die wordt vermeld is 'Release 1.1' van het CloudEvents profiel zelf.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/NL-GOV-profile-for-CloudEvents](https://logius-standaarden.github.io/NL-GOV-profile-for-CloudEvents)
  - *De brontekst behandelt uitsluitend het NLgov profile for CloudEvents. Er is geen vermelding van 'Abonneren WV v0.0.1' of een abonneer-standaard op gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/CloudEvents-NL-Guidelines](https://github.com/logius-standaarden/CloudEvents-NL-Guidelines)
  - *De aangeleverde brontekst betreft de GitHub-pagina van CloudEvents-NL-Guidelines. Er is geen vermelding van 'Abonneren WV v0.0.1', gitdocumentatie.logius.nl, of de vaststellingsstatus van een Abonneren-standaard.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/CloudEvents-NL-Guidelines](https://logius-standaarden.github.io/CloudEvents-NL-Guidelines)
  - *De brontekst gaat over de CloudEvents NL Guidelines (HTTP Protocol Binding, JSON Event Format, Webhook pattern). Er is geen informatie over een 'Abonneren' werkversie v0.0.1 of de publicatiestatus daarvan op gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Notificatieservices](https://github.com/logius-standaarden/Notificatieservices)
  - *De brontekst vermeldt een 'Concept API-specificatie voor geautomatiseerd abonneren' maar bevat geen informatie over 'Abonneren WV v0.0.1', publicatie op gitdocumentatie.logius.nl, of de vaststellingsstatus daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Abonneren](https://github.com/logius-standaarden/Abonneren)
  - *De aangeleverde brontekst is de GitHub-repositorypagina van Logius-standaarden/Abonneren. Er staat geen informatie over een versienummer (v0.0.1), een publicatie op gitdocumentatie.logius.nl, of een vaststellingsstatus. De tekst beschrijft alleen de repository-inhoud en de README-samenvatting.*
</details>

### `ls-notif-0005` — SKILL.md:58 *(§ Verplichte attributen)*

> Het `source` attribuut in het NL GOV profiel schrijft URN-notatie voor met de `nld` namespace. Formaat: `urn:nld:oin:<OIN>:systeem:<systeemnaam>`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profile for CloudEvents - verplichte attributen

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > SHOULD be a URN notation with 'nld' as namespace identifier. SHOULD contain consecutive a unique identifier of: the organization that publishes the event the source system that publishes the event. [...] Examples: urn:nld:oin:00000001823288444000:systeem:BRP-component
  - *De bron ondersteunt URN-notatie met 'nld' namespace en geeft het voorbeeld-formaat urn:nld:oin:<OIN>:systeem:<systeemnaam>. Echter: de bron gebruikt SHOULD, niet MUST voor deze URN-notatie. De claim stelt 'schrijft voor' wat de indruk wekt van een harde verplichting.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron noemt het NL GOV-profiel voor CloudEvents in het kader van Digilevering/Solace, maar bevat geen specificaties over URN-notatie, de `nld` namespace of het formaat van het `source` attribuut.*

### `ls-notif-0007` — SKILL.md:60 *(§ Verplichte attributen)*

> Het `type` attribuut gebruikt Reverse Domain Name Notation. Versioning gebeurt met een `v` prefix: `nl.brp.verhuizing.v2`. Types worden geregistreerd in een centraal register.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profile for CloudEvents - verplichte attributen

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > MUST be Reverse domain name notation [...] If versioning is used, the type attribute MUST only include a single version number, prefixed by the letter v
  - *Reverse DNS notatie en 'v' prefix voor versioning worden bevestigd. Het voorbeeld 'nl.brp.verhuizing.v2' past bij de spec. Maar een 'centraal register' voor types wordt nergens in de bron vermeld.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen normtekst over het `type` attribuut, Reverse Domain Name Notation, versioning met een `v` prefix, of een centraal register voor types.*

### `ls-notif-0011` — SKILL.md:71 *(§ Optionele attributen)*

> Het `sequence` attribuut is een CloudEvents extensie-attribuut (CNCF Sequence-extensie, niet in de kernspec) dat het NL GOV profiel overneemt.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profile for CloudEvents - optionele attributen

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > Two of the extension attributes included by CloudEvents ('dataref' and 'sequence') are included as optional attributes in the CloudEvents-NL profile because it is foreseen that there is often a need to use these attributes.
  - *De bron bevestigt dat 'sequence' een extensie-attribuut is dat het NL GOV profiel overneemt. De claim noemt specifiek 'CNCF Sequence-extensie, niet in de kernspec' — de bron zegt het is een extensie maar noemt niet expliciet 'CNCF Sequence-extensie' als naam.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen informatie over het `sequence` attribuut als CloudEvents extensie-attribuut.*

### `ls-notif-0016` — SKILL.md:122 *(§ Security & Privacy)*

> Context-attributen (zoals `source`, `type`, `subject`) mogen nooit persoonsgegevens of gevoelige informatie bevatten; gebruik hiervoor de versleutelde `data`-payload.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Security & Privacy - notificaties

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > Sensitive information SHOULD NOT be carried or represented in context attributes. CloudEvent producers, consumers, and intermediaries MAY introspect and log context attributes.
  - *De bron zegt SHOULD NOT voor gevoelige informatie in context-attributen, niet MUST NOT zoals de claim stelt. Dit is een relevant verschil in modaliteit. De verwijzing naar versleutelde data-payload komt ook voor ('Domain specific event data SHOULD be encrypted') maar is niet direct gekoppeld als vereiste tegenhanger.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen normtekst over het verbod op persoonsgegevens in context-attributen zoals `source`, `type` of `subject`.*

### `ls-notif-0017` — SKILL.md:123 *(§ Security & Privacy)*

> Wanneer de payload gevoelige gegevens bevat, moet deze versleuteld worden (end-to-end encryptie).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Security & Privacy - notificaties

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > Domain specific event data SHOULD be encrypted to restrict visibility to trusted parties. The mechanism employed for such encryption is an agreement between producers and consumers and thus outside the scope of this specification.
  - *De bron zegt SHOULD be encrypted, niet MUST. De claim stelt MUST. Bovendien spreekt de bron niet specifiek van 'end-to-end encryptie' als term.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen normtekst over verplichte end-to-end encryptie van gevoelige payloads.*

### `ls-notif-0018` — SKILL.md:124 *(§ Security & Privacy)*

> Alle communicatie tussen bronnen, notificatieservices en afnemers moet plaatsvinden over TLS (minimaal versie 1.2).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Security & Privacy - notificaties

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > Protocol level security SHOULD be employed to ensure the trusted and secure exchange of CloudEvents.
  - *De bron beveelt protocol-level security aan (SHOULD) maar noemt TLS noch een minimale versie (1.2). De claim stelt MUST en specificeert TLS minimaal 1.2, wat de bron niet bevestigt.*
- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  > Integration with federated identity and authorization frameworks (e.g., OAuth 2.0 / OIDC for authentication, fine-grained RBAC/ABAC policies) is crucial to govern who can subscribe and consume what data.
  - *De bron noemt beveiligingsmechanismen en verwijst naar mutual TLS in de context van AMQP ('mutual TLS, SASL-authenticatie'), maar bevat geen expliciete eis dat alle communicatie over TLS minimaal versie 1.2 moet plaatsvinden.*

### `ls-notif-0024` — reference.md:15 *(§ Type Systeem)*

> CloudEvents URI type is een absolute URI conform RFC 3986; URI-reference is een URI of relatieve referentie conform RFC 3986.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** CloudEvents type systeem

- **PARTIALLY_SUPPORTED** (high) — [https://www.rfc-editor.org/rfc/rfc3986.txt](https://www.rfc-editor.org/rfc/rfc3986.txt)
  > A URI is an identifier consisting of a sequence of characters matching the syntax rule named <URI> in Section 3. [...] URI-reference = URI / relative-ref [...] A URI-reference is either a URI or a relative reference.
  - *De bron ondersteunt volledig dat een URI een absolute URI is conform RFC 3986 en dat URI-reference een URI of relatieve referentie is. Wat de bron NIET bevestigt is het CloudEvents-specifieke deel: dat het 'type' attribuut in CloudEvents een absolute URI moet zijn. De bron definieert alleen de algemene URI-syntaxis, niet hoe CloudEvents dit toepast. Het deel over URI-reference als 'URI of relatieve referentie' is letterlijk ondersteund; het deel over CloudEvents URI type als absolute URI vereist kennis van de CloudEvents-specificatie zelf.*

## UNGROUNDED — geen bron ondersteunt de claim (2)

### `ls-notif-0019` — SKILL.md:308 *(§ Foutafhandeling)*

> De scope `notifications.distribute` is vereist voor publicerende systemen om events te publiceren via de Notificatieservices API.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Notificatieservices API - autorisatie

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *De bron bevat geen informatie over OAuth scopes, autorisatie of de scope 'notifications.distribute'.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen informatie over een OAuth scope `notifications.distribute` of autorisatievereisten voor de Notificatieservices API.*

### `ls-notif-0021` — reference.md:50 *(§ Authenticatie en autorisatie)*

> Publicerende systemen hebben een JWT token nodig met de scope `notifications.distribute`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Notificatieservices API - authenticatie

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *De bron bevat geen informatie over JWT tokens of de scope 'notifications.distribute'.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen normtekst over een JWT token vereiste met scope `notifications.distribute` voor publicerende systemen.*

## GROUNDED — minstens één bron ondersteunt de claim (8)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-notif-0004` — SKILL.md:57 *(§ Verplichte attributen)*

> Het `id` attribuut moet een unieke event-identifier zijn; de combinatie `source` + `id` moet globaal uniek zijn.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profile for CloudEvents - verplichte attributen

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > Identifies the event. Producers MUST ensure that source + id is unique for each distinct event. [...] MUST be a non-empty string MUST be unique within the scope of the producer
  - *De bron spreekt van 'unique within the scope of the producer' en 'source + id is unique for each distinct event'. De claim zegt 'globaal uniek' wat iets sterker is, maar de combinatie source+id dekt dit af.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bespreekt CloudEvents en CNCF CloudEvents + Subscription API als technologie, maar bevat geen normtekst over het `id` attribuut of de gecombineerde uniciteit van `source` + `id`.*

### `ls-notif-0006` — SKILL.md:59 *(§ Verplichte attributen)*

> Het `specversion` attribuut moet `"1.0"` zijn.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profile for CloudEvents - verplichte attributen

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > Compliant event producers MUST use a value of 1.0 when referring to this version of the specification.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen normtekst over het `specversion` attribuut.*

### `ls-notif-0008` — SKILL.md:66 *(§ Optionele attributen)*

> JSON (`application/json`) wordt aanbevolen als standaardformaat voor het `datacontenttype` attribuut.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NL GOV profile for CloudEvents - optionele attributen

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > JSON-format SHOULD be used (see API Design Rules ). Part of this is the intention to name JSON as the primary representation format for APIs. Because APIs play an important role in communicating events (e.g., when using the webhook pattern) the JSON format is preferred to use for payload data.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen normtekst over het `datacontenttype` attribuut of een aanbeveling voor JSON.*

### `ls-notif-0010` — SKILL.md:70 *(§ Optionele attributen)*

> Het `dataref` attribuut implementeert het Claim Check Pattern voor grote payloads die niet in het event zelf passen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profile for CloudEvents - optionele attributen

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > A reference to a location where the event payload is stored. [...] Known as the 'Claim Check Pattern', this attribute MAY be used for a variety of purposes, including: If the Data is too large to be included in the message, the data is not present, and the consumer can retrieve it using this attribute.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen informatie over het `dataref` attribuut of het Claim Check Pattern.*

### `ls-notif-0012` — SKILL.md:72 *(§ Optionele attributen)*

> Het `sequencetype` attribuut: indien aanwezig MOET het een niet-lege string zijn.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** NL GOV profile for CloudEvents - optionele attributen

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > sequencetype Type: String [...] Constraints: OPTIONAL If present, MUST be a non-empty string
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen normtekst over het `sequencetype` attribuut.*

### `ls-notif-0014` — SKILL.md:104 *(§ Abonneren)*

> Push-model (webhook) is het aanbevolen aflevermodel vanwege lage latency en efficiënter resourcegebruik.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Abonneren - aflevermodellen

- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  > Push-model Directe notificaties bij verandering; geen onnodige polling nodig [...] Asynchroon Ontkoppeling van systemen in tijd (Niet wachten op polling-cycli of batchjobs)
  - *De bron ondersteunt het push-model als voordelig vanwege directe notificaties en geen polling, wat aansluit bij de claim. De expliciete kwalificatie 'aanbevolen aflevermodel' of de specifieke termen 'lage latency' en 'efficiënter resourcegebruik' staan echter niet letterlijk in de bron. De strekking is wel consistent.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  - *De bron bespreekt het publish-subscribe patroon en webhook in appendix A, maar doet geen aanbeveling over push vs. pull als aflevermodel op basis van latency of resourcegebruik.*

### `ls-notif-0022` — SKILL.md:57 *(§ Verplichte attributen)*

> Het `id` attribuut heeft bij voorkeur een persistent (domeinspecifiek) ID; wanneer geen persistent ID beschikbaar is, gebruik een UUID (v4).

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** NL GOV profile for CloudEvents - verplichte attributen

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > If an ID is available that can persistently identify the event, producers MUST use that ID. [...] If no ID is available that can persistently identify the event producers SHOULD use a random ID: SHOULD use a UUID.
  - *De bron bevestigt de voorkeur voor persistent ID en UUID als fallback. De claim noemt 'UUID (v4)' specifiek, de bron zegt alleen 'UUID' zonder versieaanduiding — klein verschil maar de strekking klopt.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  - *De bron bevat geen normtekst over het `id` attribuut, persistent IDs of het gebruik van UUID v4 als fallback.*

### `ls-notif-0025` — SKILL.md:25 *(§ CloudEvents & Notificaties)*

> Het NL GOV profiel voor CloudEvents is gebaseerd op de internationale CNCF CloudEvents specificatie v1.0.1.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** NL GOV profile for CloudEvents

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/cloudevents-nl)
  > This profile is based on CloudEvents - Version 1.0.1 as published by the Serverless Working Group of the Cloud Native Computing Foundation.
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren](https://gitdocumentatie.logius.nl/publicatie/notificatieservices/abonneren)
  > CNCF CloudEvents + Subscription API Gestandaardiseerde eventstructuur + abonnementsbeheer, bevordert interoperabiliteit en leveranciersonafhankelijke, cloud-native eventafhandeling.
  - *De bron bevestigt dat CloudEvents een CNCF-standaard is en verwijst naar interoperabiliteit, maar vermeldt het specifieke versienummer v1.0.1 niet. De claim dat het NL GOV profiel hierop gebaseerd is, wordt ook niet expliciet bevestigd — de bron noemt het NL GOV-profiel alleen in de context van Solace/Digilevering.*

</details>
