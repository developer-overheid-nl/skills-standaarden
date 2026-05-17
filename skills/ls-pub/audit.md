<!-- markdownlint-disable MD052 MD034 MD013 MD038 -->
# Audit ls-pub — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 2 | 6% |
| CONTRADICTED | 1 | 3% |
| PARTIALLY_GROUNDED | 6 | 17% |
| UNGROUNDED | 2 | 6% |
| NO_SOURCE | 21 | 60% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 1 | 3% |
| GROUNDED | 2 | 6% |

*Geverifieerd met sonnet, 9 calls, $0.4697.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (2)

### `ls-pub-0009` — SKILL.md:51 *(§ Repositories)*

> De `Openbare-Consultaties` repo bevat gepubliceerde consultatieversies (CV) en heeft licentie CC-BY-4.0.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius standaarden repositories

- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/logius-standaarden/Openbare-Consultaties/main/LICENSE](https://raw.githubusercontent.com/logius-standaarden/Openbare-Consultaties/main/LICENSE)
  - *Bron status: unreachable*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/logius-standaarden/Openbare-Consultaties/master/LICENSE](https://raw.githubusercontent.com/logius-standaarden/Openbare-Consultaties/master/LICENSE)
  - *Bron status: unreachable*
<details><summary>4x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  - *De bron vermeldt de Openbare-Consultaties repo niet en geeft geen informatie over consultatieversies of bijbehorende licenties.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  - *De brontekst bevat geen informatie over een 'Openbare-Consultaties' repo, consultatieversies of CC-BY-4.0 licentie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron behandelt de ReSpec-template repo; een 'Openbare-Consultaties' repo of consultatieversies (CV) worden niet genoemd.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De bron gaat over de ReSpec-template-Logius repo, niet over een 'Openbare-Consultaties' repo. Geen relevante informatie aanwezig.*
</details>

### `ls-pub-0010` — SKILL.md:54 *(§ Repositories)*

> De `tech-radar` repo heeft MIT-licentie en is gepubliceerd op logius-standaarden.github.io/tech-radar/.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius standaarden repositories

- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/logius-standaarden/tech-radar/main/LICENSE](https://raw.githubusercontent.com/logius-standaarden/tech-radar/main/LICENSE)
  - *Bron status: unreachable*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/logius-standaarden/tech-radar/master/LICENSE](https://raw.githubusercontent.com/logius-standaarden/tech-radar/master/LICENSE)
  - *Bron status: unreachable*
<details><summary>4x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  - *De bron vermeldt de tech-radar repo niet en geeft geen informatie over MIT-licentie of publicatie-URL.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  - *De brontekst bevat geen informatie over een 'tech-radar' repo, MIT-licentie of logius-standaarden.github.io/tech-radar/.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron behandelt de ReSpec-template repo; een 'tech-radar' repo, MIT-licentie of logius-standaarden.github.io/tech-radar/ worden niet vermeld.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De bron gaat over de ReSpec-template-Logius repo, niet over een 'tech-radar' repo. Geen informatie over MIT-licentie of publicatie-URL.*
</details>

## CONTRADICTED — bron spreekt de claim expliciet tegen (1)

### `ls-pub-0013` — SKILL.md:71 *(§ ReSpec Configuratie (`js/config.mjs`))*

> Nieuwe documenten gebruiken ES-module formaat (`config.mjs`); oudere repos kunnen nog `config.js` bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** ReSpec configuratie

- **CONTRADICTED** (medium) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  > "De configuratie files bevat informatie over de organisatie en over de status van het document. [...] De files zijn gesplitst in 2 files: een [config.js](js/config.js]"
  - *De bron verwijst expliciet naar config.js; ES-module formaat of config.mjs wordt niet genoemd. De bron suggereert dat config.js het huidige formaat is, zonder vermelding van een nieuwer ES-module formaat. Dit is een gedeeltelijke tegenspraak: de bron kent alleen config.js, niet config.mjs.*
- **PARTIALLY_SUPPORTED** (medium) — [https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs](https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs)
  > In `js/config.mjs` moet het volgende staan: ```js import { loadRespecWithConfiguration } from "https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs"; loadRespecWithConfiguration({ ... }); ```
  - *De bron bevestigt het ES-module formaat (config.mjs) als het huidige patroon. De claim over 'oudere repos kunnen nog config.js bevatten' wordt niet bevestigd noch tegengesproken in de bron.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (6)

### `ls-pub-0005` — SKILL.md:46 *(§ Repositories)*

> De centrale publicatie-repo `publicatie` bevat alle vastgestelde standaarden en heeft licentie CC-BY-4.0.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius standaarden repositories

- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/logius-standaarden/publicatie/main/LICENSE](https://raw.githubusercontent.com/logius-standaarden/publicatie/main/LICENSE)
  - *Bron status: unreachable*
- **SOURCE_UNAVAILABLE** (high) — [https://raw.githubusercontent.com/logius-standaarden/publicatie/master/LICENSE](https://raw.githubusercontent.com/logius-standaarden/publicatie/master/LICENSE)
  - *Bron status: unreachable*
- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  > De inhoud van deze repository wordt dagelijks gepubliceerd naar gitdocumentatie.logius.nl/publicatie.
  - *De bron bevestigt dat de repo standaarden bevat en publiceert, maar vermeldt geen licentie (CC-BY-4.0) en spreekt niet expliciet van 'alle vastgestelde standaarden'.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  - *De brontekst gaat over de Logius-standaarden/respec repository. Er is geen informatie over een centrale 'publicatie' repo, vastgestelde standaarden of CC-BY-4.0 licentie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron gaat over de ReSpec-template repo, niet over een centrale 'publicatie' repo. Er is geen informatie over een repo met die naam of bijbehorende licentie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst beschrijft de ReSpec-template-Logius repo, niet een centrale publicatie-repo genaamd 'publicatie'. Geen informatie over CC-BY-4.0 licentie van die repo.*
</details>

### `ls-pub-0006` — SKILL.md:46 *(§ Repositories)*

> De `publicatie` repo publiceert naar gitdocumentatie.logius.nl zonder directory listing.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius standaarden repositories

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  > De inhoud van deze repository wordt dagelijks gepubliceerd naar gitdocumentatie.logius.nl/publicatie.
  - *De bron bevestigt publicatie naar gitdocumentatie.logius.nl/publicatie, maar vermeldt niets over het al dan niet aanwezig zijn van een directory listing.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template-Logius](https://logius-standaarden.github.io/ReSpec-template-Logius)
  - *Bron status: unsupported*
<details><summary>4x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  - *De brontekst bevat geen informatie over een 'publicatie' repo of gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron behandelt de ReSpec-template repo; gitdocumentatie.logius.nl of een 'publicatie' repo wordt niet genoemd.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De bron gaat over de ReSpec-template-Logius repo en bevat geen informatie over publicatie naar gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties)
  - *De brontekst beschrijft de openbare consultaties repository van Logius. Er is geen enkele vermelding van een `publicatie` repo, gitdocumentatie.logius.nl, of directory listing.*
</details>

### `ls-pub-0007` — SKILL.md:48 *(§ Repositories)*

> De Logius `respec` repo is een fork van W3C ReSpec met aangepaste huisstijl en heeft W3C Software License.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius standaarden repositories

- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *Bron status: unsupported*
- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  > forked from speced/respec [...] ReSpec is a tool for writing W3C specifications and other technical documents.
  - *De bron bevestigt dat de Logius respec repo een fork is van speced/respec (de W3C ReSpec). Er is echter geen expliciete vermelding van 'aangepaste huisstijl' of 'W3C Software License'. De LICENSE link is aanwezig maar de inhoud ervan is niet weergegeven in de brontekst.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template-Logius](https://logius-standaarden.github.io/ReSpec-template-Logius)
  - *Bron status: unsupported*
<details><summary>4x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  - *De bron (de publicatie-repo) bevat een map 'respec' maar geeft geen informatie over de respec-repo zelf, de relatie tot W3C ReSpec, de huisstijl, of de licentie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron gaat over de ReSpec-template, niet over een 'respec' repo die een fork van W3C ReSpec zou zijn. W3C Software License wordt niet vermeld.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De bron beschrijft de ReSpec-template-Logius repo, niet de 'respec' repo als fork van W3C ReSpec. Geen informatie over W3C Software License.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties)
  - *De brontekst bevat geen informatie over een `respec` repository, W3C ReSpec forks, huisstijl-aanpassingen, of W3C Software License.*
</details>

### `ls-pub-0014` — SKILL.md:84 *(§ ReSpec Configuratie (`js/config.mjs`))*

> `pubDomain` accepteert alleen de waarden: `api`, `bomos`, `dk`, `fsc`, `ftv`, `logboek` of `notificatieservices`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ReSpec configuratie pubDomain

- **PARTIALLY_SUPPORTED** (high) — [https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs](https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs)
  > const ACCEPTED_DOMAINS = ['api', 'bomos', 'dk', 'digimelding', 'fsc', 'ftv', 'logboek', 'notificatieservices'];
  - *De bron bevat 'digimelding' als geaccepteerd domein, maar de claim noemt dit niet. De claim mist dus één geldige waarde.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron verwijst voor configuratieopties naar de 'Logius ReSpec wiki' maar geeft geen details over pubDomain of toegestane waarden daarvoor.*

### `ls-pub-0016` — SKILL.md:94 *(§ ReSpec Configuratie (`js/config.mjs`))*

> Oudere repos gebruiken `config.js` met `var respecConfig = { ... }` syntax en kunnen extra velden bevatten zoals `content`, `alternateFormats` en `postProcess`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ReSpec configuratie legacy

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  > "De files zijn gesplitst in 2 files: een [config.js](js/config.js]" en "content: {"ch01": "informative", "mermaid": ""}, Deze code voegt 2 markdown files toe" en "alternateFormats" wordt indirect aangeduid: "Er wordt automatisch een PDF versie als alternatief format aangemaakt."
  - *De bron bevestigt config.js en het 'content' veld. 'alternateFormats' wordt niet expliciet als configuratieveld genoemd maar PDF als alternatief formaat wel. 'var respecConfig = { ... }' syntax en 'postProcess' worden niet vermeld in de bron.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs](https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs)
  - *De bron beschrijft alleen het huidige ES-module formaat (config.mjs). Informatie over legacy config.js syntax met 'var respecConfig', 'content', 'alternateFormats' als legacy-velden, of 'postProcess' als legacy-patroon staat niet in de bron.*

### `ls-pub-0035` — reference.md:9 *(§ Tech Radar)*

> De Tech Radar heeft vier ringen: Adopt (bewezen, aanbevolen), Trial (actief getest), Assess (wordt onderzocht), Hold (niet aanbevolen, wordt uitgefaseerd).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Tech Radar Logius standaarden

- **PARTIALLY_SUPPORTED** (medium) — [https://logius-standaarden.github.io/tech-radar](https://logius-standaarden.github.io/tech-radar)
  > We use four rings with the following semantics: ADOPT — Technologies we have high confidence in to serve our purpose [...] TRIAL — Technologies that we have seen work with success in project work [...] ASSESS — Technologies that are promising and have clear potential value-add [...] HOLD — Technologies not recommended to be used for new projects.
  - *De vier ringen bestaan en de beschrijvingen van Adopt, Trial en Assess kloppen grotendeels. Echter: de claim zegt Hold betekent 'wordt uitgefaseerd', maar de bron zegt expliciet 'usually can be continued for existing projects' — Hold betekent niet per se uitfasering, alleen geen nieuwe projecten. Dat is een nuanceverschil maar geen directe tegenspraak. Verder: de omschrijvingen in de bron gaan over 'Zalando production environment' (kopie van de Zalando-tekst), wat niet klopt met de Logius-context, maar dat is een bronkwestie, niet een claim-verificatiekwestie.*

## UNGROUNDED — geen bron ondersteunt de claim (2)

### `ls-pub-0030` — SKILL.md:157 *(§ Nieuw Document Starten)*

> `pubDomain` accepteert alleen `api`, `bomos`, `dk`, `fsc`, `ftv`, `logboek` of `notificatieservices`.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Nieuw ReSpec document opstarten

*Mogelijk relevant in conflicts.md (§ pubDomain `ftv` (Federatieve Toegang Verlening)): conflicts.md noemt de toevoeging van pubDomain 'ftv' in maart 2026 en beschrijft de verhuizing van 'authorization-decision-log' van 'dk' naar 'ftv'. Dat raakt het onderwerp pubDomains, maar geeft geen exhaustieve lijst van toegestane waarden en bevestigt/weerspreekt de claim over de volledige set niet.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst bevat geen configuratie-details over `pubDomain` of de toegestane waarden ervan. De inhoud van index.html of andere configuratiebestanden is niet weergegeven.*

### `ls-pub-0031` — SKILL.md:157 *(§ Nieuw Document Starten)*

> `shortName` moet in kebab-case zijn (alleen kleine letters, gescheiden door streepjes, bijv. `rest-api`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Nieuw ReSpec document opstarten

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst bevat geen informatie over `shortName` of vereisten voor kebab-case notatie. De inhoud van configuratiebestanden is niet weergegeven.*

## NO_SOURCE — geen kandidaat-bron gevonden (21)

### `ls-pub-0001` — SKILL.md:37 *(§ Versiemodel van standaarden)*

> specStatus `WV` (Werkversie/draft) wordt gepubliceerd op `logius-standaarden.github.io`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie-tooling versiemodel


### `ls-pub-0002` — SKILL.md:38 *(§ Versiemodel van standaarden)*

> specStatus `CV` (Consultatieversie) wordt gepubliceerd op `logius-standaarden.github.io/Openbare-Consultaties/`, automatisch op `consultatie/*` branches.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie-tooling versiemodel


### `ls-pub-0003` — SKILL.md:39 *(§ Versiemodel van standaarden)*

> specStatus `VV` (Versie ter vaststelling) wordt gepubliceerd op `gitdocumentatie.logius.nl`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie-tooling versiemodel


### `ls-pub-0004` — SKILL.md:40 *(§ Versiemodel van standaarden)*

> specStatus `DEF` (Vastgestelde versie) wordt gepubliceerd op `gitdocumentatie.logius.nl`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie-tooling versiemodel


### `ls-pub-0011` — SKILL.md:58 *(§ ReSpec Documentatie-systeem)*

> ReSpec genereert technische specificaties als HTML en PDF vanuit Markdown.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ReSpec documentatie-systeem


### `ls-pub-0012` — SKILL.md:62 *(§ Hoe ReSpec werkt)*

> Het hoofdbestand `index.html` laadt de ReSpec-engine en verwijst via `data-include` naar losse Markdown-bestanden per hoofdstuk.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** ReSpec documentatie-systeem


### `ls-pub-0017` — SKILL.md:113 *(§ build.yml - Document Generatie)*

> Op `consultatie/*` branches wordt `specStatus` automatisch overschreven naar `"cv"` via sed op `config.mjs` in de build.yml workflow.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions build.yml workflow


### `ls-pub-0018` — SKILL.md:114 *(§ build.yml - Document Generatie)*

> HTML generatie in build.yml gebruikt `npx respec --localhost --src index.html --out ~/static/index.html --haltonwarn`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions build.yml workflow


### `ls-pub-0019` — SKILL.md:115 *(§ build.yml - Document Generatie)*

> PDF generatie in build.yml gebeurt via Puppeteer/headless Chrome met `scripts/pdf.js`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions build.yml workflow


### `ls-pub-0020` — SKILL.md:120 *(§ check.yml - Kwaliteitschecks (3 parallelle checks))*

> De WCAG check in check.yml gebruikt `npx @axe-core/cli http://localhost:8080/index.html --tags wcag2aa`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions check.yml workflow


### `ls-pub-0021` — SKILL.md:120 *(§ check.yml - Kwaliteitschecks (3 parallelle checks))*

> axe-core dekt automatisch ~30% van WCAG-criteria; handmatige toetsing blijft nodig voor volledige WCAG-conformiteit.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** WCAG accessibility check


### `ls-pub-0022` — SKILL.md:120 *(§ check.yml - Kwaliteitschecks (3 parallelle checks))*

> axe-core implementeert gestandaardiseerde W3C ACT Rules; alternatieven zijn Alfa (Siteimprove) en QualWeb.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** WCAG accessibility tooling


### `ls-pub-0023` — SKILL.md:121 *(§ check.yml - Kwaliteitschecks (3 parallelle checks))*

> Markdown lint in check.yml gebruikt `npx markdownlint-cli sections/`.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions check.yml workflow


### `ls-pub-0024` — SKILL.md:127 *(§ publish.yml - Publicatie)*

> publish.yml publiceert bij push naar `main`/`master` naar de centrale `publicatie` repo (gitdocumentatie.logius.nl).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions publish.yml workflow


### `ls-pub-0025` — SKILL.md:128 *(§ publish.yml - Publicatie)*

> publish.yml publiceert bij push naar `develop` naar GitHub Pages van de standaarden-repo zelf.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions publish.yml workflow


### `ls-pub-0026` — SKILL.md:129 *(§ publish.yml - Publicatie)*

> publish.yml publiceert bij pull requests een preview naar de `Publicatie-Preview` repo.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions publish.yml workflow


### `ls-pub-0027` — SKILL.md:130 *(§ publish.yml - Publicatie)*

> publish.yml publiceert `consultatie/*` branches naar de `Openbare-Consultaties` repo.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions publish.yml workflow


### `ls-pub-0028` — SKILL.md:134 *(§ link-checker.yml - Gepubliceerde Links Controleren)*

> link-checker.yml controleert periodiek of de gepubliceerde versie op gitdocumentatie.logius.nl geen dode links bevat en stuurt een e-mail bij gevonden fouten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** GitHub Actions link-checker.yml workflow


### `ls-pub-0032` — SKILL.md:169 *(§ Checks Lokaal Draaien)*

> axe-core checkt automatisch ~30% van de WCAG-criteria; een groene check betekent NIET volledige conformiteit aan EN 301 549 / WCAG 2.1 AA.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Lokale WCAG accessibility check


### `ls-pub-0033` — SKILL.md:171 *(§ Checks Lokaal Draaien)*

> Handmatige toetsing op alle 55 succescriteria in WCAG 2.1 AA blijft nodig, ook na een groene axe-core check.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** WCAG 2.1 AA conformiteit


### `ls-pub-0034` — SKILL.md:196 *(§ Consultatie Branch Gedrag)*

> Na merge van een `consultatie/*` branch naar `main` wordt `specStatus` uit `js/config.mjs` gebruikt.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Consultatie Branch Gedrag


## KNOWN_DISCREPANCY — gedocumenteerd in conflicts.md (1)

### `ls-pub-0008` — SKILL.md:50 *(§ Repositories)*

> De `ReSpec-template-Logius` repo heeft licentie CC0-1.0.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius standaarden repositories

**Erkend in conflicts.md** *(§ Licentie-status GitHub-repositories)*: conflicts.md tabel 'Licentie-status GitHub-repositories' documenteert expliciet: ReSpec-template-Logius heeft GitHub LICENSE 'W3C Software License' en gepubliceerde licentie 'CC0-1.0 (ReSpec)', status 'Afwijkend'. De claim beschrijft de gepubliceerde licentie; de discrepantie met de GitHub LICENSE is gedocumenteerd.

- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *Bron status: unsupported*
- **CONTRADICTED** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  > CC-BY-4.0 license (vermeld in de repository header en footer van de bron: 'License CC-BY-4.0 license')
  - *De claim stelt CC0-1.0, maar de bron toont expliciet CC-BY-4.0 als licentie van deze ReSpec-template repo. De repo heet overigens 'ReSpec-template', niet 'ReSpec-template-Logius', maar dit is de meest overeenkomstige repo in de bron.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **CONTRADICTED** (high) — [https://raw.githubusercontent.com/logius-standaarden/respec/main/LICENSE](https://raw.githubusercontent.com/logius-standaarden/respec/main/LICENSE)
  > The W3C SOFTWARE NOTICE AND LICENSE (W3C) https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document ... Permission to copy, modify, and distribute this work, with or without modification, for any purpose and without fee or royalty is hereby granted, provided that you include the following on ALL copies of the work
  - *De bron toont de W3C Software Notice and License, niet CC0-1.0. CC0-1.0 is een publiek domein-verklaring zonder voorwaarden, terwijl deze licentie expliciet attribuutverplichtingen oplegt (o.a. volledige tekst meenemen, copyright-statement bij wijzigingen). Dit is een directe tegenstelling met de claim dat de licentie CC0-1.0 is.*
- **CONTRADICTED** (high) — [https://raw.githubusercontent.com/logius-standaarden/respec/master/LICENSE](https://raw.githubusercontent.com/logius-standaarden/respec/master/LICENSE)
  > The W3C SOFTWARE NOTICE AND LICENSE (W3C) https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document ... Permission to copy, modify, and distribute this work, with or without modification, for any purpose and without fee or royalty is hereby granted, provided that you include the following on ALL copies of the work...
  - *De bron toont een W3C Software and Document License, niet CC0-1.0. CC0-1.0 is een publiek domein-verklaring zonder enige voorwaarden, terwijl deze licentie expliciete naamsvermelding- en meldingsverplichtingen oplegt. De claim dat de repo CC0-1.0 heeft wordt direct tegengesproken door de aanwezigheid van deze W3C-licentie.*
<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  - *De bron vermeldt de ReSpec-template-Logius repo noch enige licentie-informatie daarvoor.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  - *De brontekst gaat over de respec repository, niet over 'ReSpec-template-Logius'. Geen informatie over CC0-1.0 licentie.*
- **NOT_FOUND** (medium) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst vermeldt dat er een LICENSE-bestand aanwezig is, maar de inhoud van dat bestand wordt niet weergegeven. 'View license' is een link maar de tekst ervan is niet opgenomen in de bron. Er kan niet worden vastgesteld of het CC0-1.0 is.*
</details>

## GROUNDED — minstens één bron ondersteunt de claim (2)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-pub-0015` — SKILL.md:85 *(§ ReSpec Configuratie (`js/config.mjs`))*

> `shortName` moet kebab-case zijn: alleen kleine letters, gescheiden door streepjes (bijv. `rest-api`).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** ReSpec configuratie shortName

- **SUPPORTED** (high) — [https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs](https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs)
  > if (!/^[a-z][a-z0-9]*(-[a-z0-9]+)*$/.test(config.shortName)) { utils.showError(`Invalid shortName. Must be in kebab-case (only lowercase letters and potentially separated by dashes), but was "${config.shortName}"`); }
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *shortName of kebab-case vereisten worden niet besproken in de bron.*

### `ls-pub-0029` — SKILL.md:156 *(§ Nieuw Document Starten)*

> Voor een nieuw document moet `ReSpec-template-Logius` als basis worden gebruikt.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Nieuw ReSpec document opstarten

- **SUPPORTED** (medium) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  > "ReSpec template Logius Template voor Afdeling Standaarden." en "Generated from Logius-standaarden/ReSpec-template"
  - *De repo presenteert zichzelf expliciet als template voor Afdeling Standaarden en is als GitHub template repository aangemerkt ('Public template'), wat het gebruik als basis voor nieuwe documenten ondersteunt.*

</details>
