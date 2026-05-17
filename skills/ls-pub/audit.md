<!-- markdownlint-disable MD052 MD034 MD013 -->
# Audit ls-pub — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 2 | 5% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 9 | 24% |
| UNGROUNDED | 2 | 5% |
| NO_SOURCE | 22 | 58% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 3 | 8% |

*Geverifieerd met sonnet, 12 calls, $0.6263.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (2)

### `ls-pub-0008` — SKILL.md:50 *(§ Repositories)*

> ReSpec-template-Logius valt onder CC0-1.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius ReSpec-template-Logius repository

- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template-Logius](https://logius-standaarden.github.io/ReSpec-template-Logius)
  - *Bron status: unsupported*
<details><summary>11x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  - *De bron bevat geen informatie over een ReSpec-template-Logius repository of de CC0-1.0 licentie.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen 'Loading...')*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  - *De bron gaat over de ReSpec-repo, niet over ReSpec-template-Logius. CC0-1.0 wordt nergens vermeld.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron gaat over de ReSpec-template repository, niet over een 'ReSpec-template-Logius' repository. CC0-1.0 wordt niet genoemd.*
- **NOT_FOUND** (medium) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst vermeldt wel dat de repository een LICENSE-bestand heeft ('View license'), maar de inhoud van die licentie wordt niet weergegeven. Er staat enkel 'View license' zonder de naam CC0-1.0 te noemen.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties)
  - *De brontekst bevat geen informatie over ReSpec-template-Logius of CC0-1.0 licentie.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Openbare-Consultaties](https://logius-standaarden.github.io/Openbare-Consultaties)
  - *De brontekst bevat geen informatie over ReSpec-template-Logius of CC0-1.0 licentie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Automatisering](https://github.com/logius-standaarden/Automatisering)
  - *De brontekst bevat geen informatie over ReSpec-template-Logius of een CC0-1.0 licentie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/automatisering-test](https://github.com/logius-standaarden/automatisering-test)
  - *De brontekst vermeldt geen CC0-1.0 licentie of ReSpec-template-Logius repository. De pagina verwijst wel naar een ReSpec-template als bronrepository ('Generated from Logius-standaarden/ReSpec-template'), maar licentie-informatie ontbreekt.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/tech-radar](https://github.com/logius-standaarden/tech-radar)
  - *De brontekst bevat geen informatie over ReSpec-template-Logius of CC0-1.0 licentie.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/tech-radar](https://logius-standaarden.github.io/tech-radar)
  - *De brontekst bevat geen informatie over ReSpec-template-Logius of CC0-1.0 licentie.*
</details>

### `ls-pub-0034` — SKILL.md:159 *(§ Nieuw Document Starten)*

> Na push naar GitHub bouwt CI/CD automatisch HTML en PDF.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius ReSpec CI/CD pipeline

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst toont wel een .github-map wat op CI/CD wijst, maar er is geen informatie over automatisch bouwen van HTML en PDF na een push.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (9)

### `ls-pub-0005` — SKILL.md:46 *(§ Repositories)*

> De centrale publicatie-repo bevat alle vastgestelde standaarden en publiceert naar gitdocumentatie.logius.nl zonder directory listing.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie repository

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  > De inhoud van deze repository wordt dagelijks gepubliceerd naar gitdocumentatie.logius.nl/publicatie.
  - *De bron bevestigt publicatie naar gitdocumentatie.logius.nl, maar niet specifiek naar gitdocumentatie.logius.nl zonder directory listing. Ook wordt niet expliciet gesteld dat alle vastgestelde standaarden zijn opgenomen; de repo bevat wel een uitgebreide lijst van standaarden (ADR, OAuth, Digikoppeling, FSC, etc.).*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template-Logius](https://logius-standaarden.github.io/ReSpec-template-Logius)
  - *Bron status: unsupported*
<details><summary>10x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen 'Loading...')*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  - *De bron is de GitHub-pagina van de Logius ReSpec-repo. Er staat niets over een centrale publicatie-repo, vastgestelde standaarden of gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron beschrijft de ReSpec-template repository. Er staat niets over een centrale publicatie-repo, gitdocumentatie.logius.nl, of directory listing.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst beschrijft alleen de ReSpec-template-Logius repository. Er is geen informatie over een centrale publicatie-repo of gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties)
  - *De brontekst betreft de Openbare-Consultaties repository van Logius. Er is geen informatie over een centrale publicatie-repo die naar gitdocumentatie.logius.nl publiceert of over directory listing.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Openbare-Consultaties](https://logius-standaarden.github.io/Openbare-Consultaties)
  - *De brontekst gaat over openbare consultaties van Logius. Er is geen informatie over een centrale publicatie-repo, gitdocumentatie.logius.nl of directory listing.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Automatisering](https://github.com/logius-standaarden/Automatisering)
  - *De brontekst beschrijft de Automatisering-repo en noemt publicatie naar logius.nl, maar geeft geen informatie over directory listing of de centrale publicatie-repo met vastgestelde standaarden op gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/automatisering-test](https://github.com/logius-standaarden/automatisering-test)
  - *De brontekst beschrijft een test-repository voor automatisering-verificatie. Er staat niets over een centrale publicatie-repo, vastgestelde standaarden, of gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/tech-radar](https://github.com/logius-standaarden/tech-radar)
  - *De brontekst gaat over de tech-radar repository van Logius, niet over een centrale publicatie-repo of gitdocumentatie.logius.nl.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/tech-radar](https://logius-standaarden.github.io/tech-radar)
  - *De brontekst gaat over de Tech Radar en beschrijft de vier ringen en het doel ervan. Er is geen informatie over een centrale publicatie-repo, vastgestelde standaarden, of gitdocumentatie.logius.nl.*
</details>

### `ls-pub-0006` — SKILL.md:46 *(§ Repositories)*

> De publicatie-repo en Publicatie-Preview-repo vallen onder CC-BY-4.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie repositories licenties

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  > License CC-BY-4.0 license
  - *De bron bevestigt dat de ReSpec-template repo onder CC-BY-4.0 valt. Er is geen informatie over een aparte 'Publicatie-Preview-repo' of een centrale publicatie-repo met dezelfde licentie.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template-Logius](https://logius-standaarden.github.io/ReSpec-template-Logius)
  - *Bron status: unsupported*
<details><summary>10x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  - *De brontekst (GitHub README en paginalijst) bevat geen informatie over licenties van de publicatie-repo of een Publicatie-Preview-repo.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen 'Loading...')*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  - *De bron vermeldt geen licentie-informatie over publicatie-repo's. De ReSpec-repo zelf toont een eigen licentie (via 'View license'), maar CC-BY-4.0 wordt nergens genoemd.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst vermeldt geen licentie-informatie voor publicatie-repo of Publicatie-Preview-repo.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties)
  - *De brontekst bevat geen informatie over licenties van publicatie-repos. De Openbare-Consultaties repo vermeldt geen CC-BY-4.0 licentie.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Openbare-Consultaties](https://logius-standaarden.github.io/Openbare-Consultaties)
  - *De brontekst bevat geen informatie over licenties van publicatie-repos.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Automatisering](https://github.com/logius-standaarden/Automatisering)
  - *De brontekst bevat geen informatie over licenties van de publicatie-repo of Publicatie-Preview-repo.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/automatisering-test](https://github.com/logius-standaarden/automatisering-test)
  - *De brontekst vermeldt geen CC-BY-4.0 licentie voor publicatie-repo's. De repository heeft wel een LICENSE-bestand maar de inhoud daarvan is niet weergegeven in de aangeleverde tekst.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/tech-radar](https://github.com/logius-standaarden/tech-radar)
  - *De brontekst bevat geen informatie over CC-BY-4.0 licenties voor publicatie-repos.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/tech-radar](https://logius-standaarden.github.io/tech-radar)
  - *De brontekst bevat geen informatie over licenties van publicatie-repos.*
</details>

### `ls-pub-0007` — SKILL.md:48 *(§ Repositories)*

> De Logius ReSpec-repo is een fork van de W3C ReSpec documentatie-tool en valt onder de W3C Software License.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius ReSpec repository

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  > Logius-standaarden / respec Public forked from speced/respec
  - *De bron bevestigt dat de Logius ReSpec-repo een fork is van speced/respec (de W3C ReSpec tool). De W3C Software License wordt echter niet expliciet vermeld in de aangeleverde brontekst; alleen 'View license' staat er zonder verdere details.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template-Logius](https://logius-standaarden.github.io/ReSpec-template-Logius)
  - *Bron status: unsupported*
<details><summary>10x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  - *De bron gaat over de publicatie-repository van Logius-standaarden. Er is geen informatie over een ReSpec-repo, een fork van W3C ReSpec, of de W3C Software License.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen 'Loading...')*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron beschrijft de ReSpec-template, niet de Logius ReSpec-repo zelf. Er staat niets over een fork van W3C ReSpec of de W3C Software License.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst bevat geen informatie over de Logius ReSpec-repo als fork van W3C ReSpec of over de W3C Software License.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties)
  - *De brontekst bevat geen informatie over een ReSpec-repo, een fork van W3C ReSpec, of de W3C Software License.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Openbare-Consultaties](https://logius-standaarden.github.io/Openbare-Consultaties)
  - *De brontekst bevat geen informatie over een Logius ReSpec-repo of de W3C ReSpec tool.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Automatisering](https://github.com/logius-standaarden/Automatisering)
  - *De brontekst maakt geen melding van de Logius ReSpec-repo, een fork van W3C ReSpec, of de W3C Software License.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/automatisering-test](https://github.com/logius-standaarden/automatisering-test)
  - *De brontekst gaat over de automatisering-test repository, niet over de Logius ReSpec-repo of een fork van W3C ReSpec. Geen vermelding van W3C Software License.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/tech-radar](https://github.com/logius-standaarden/tech-radar)
  - *De brontekst gaat over de tech-radar repository, niet over een ReSpec-repo of W3C Software License.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/tech-radar](https://logius-standaarden.github.io/tech-radar)
  - *De brontekst maakt geen melding van ReSpec, W3C, of licenties.*
</details>

### `ls-pub-0012` — SKILL.md:71 *(§ ReSpec Configuratie (js/config.mjs))*

> Nieuwe ReSpec-documenten gebruiken ES-module formaat (config.mjs); oudere repos kunnen nog config.js bevatten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius ReSpec configuratie

- **PARTIALLY_SUPPORTED** (medium) — [https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs](https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs)
  > In `js/config.mjs` moet het volgende staan: `import { loadRespecWithConfiguration } from "https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs";`
  - *De bron bevestigt dat nieuwe documenten config.mjs gebruiken, maar zegt niets over oudere repos met config.js. Alleen het nieuwe formaat is gedocumenteerd.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron noemt config.js als configuratiebestand maar vermeldt geen ES-module formaat, config.mjs, of onderscheid tussen nieuwe en oudere repos.*

### `ls-pub-0015` — SKILL.md:85 *(§ ReSpec Configuratie (js/config.mjs))*

> De ReSpec configuratieparameter shortName moet in kebab-case zijn: alleen kleine letters, gescheiden door streepjes.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logius ReSpec configuratie

- **PARTIALLY_SUPPORTED** (high) — [https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs](https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs)
  > if (!/^[a-z][a-z0-9]*(-[a-z0-9]+)*$/.test(config.shortName)) { utils.showError(`Invalid shortName. Must be in kebab-case (only lowercase letters and potentially separated by dashes), but was "${config.shortName}"`); }
  - *De bron bevestigt kebab-case en kleine letters. De claim zegt 'gescheiden door streepjes' maar laat cijfers weg; de bron staat ook cijfers toe ([a-z0-9]+). Deels ondersteund: de kern klopt, maar cijfers in shortName worden door de claim niet vermeld.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron noemt geen shortName parameter of vereisten omtrent kebab-case naamgeving.*

### `ls-pub-0016` — SKILL.md:94 *(§ ReSpec Configuratie (js/config.mjs))*

> Oudere ReSpec-repos gebruiken config.js met 'var respecConfig = { ... }' syntax en bevatten soms extra velden zoals content, alternateFormats en postProcess.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius ReSpec configuratie oudere repos

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  > De files zijn gesplitst in 2 files: een [config.js](js/config.js] en een organisation config. [...] content: {"ch01": "informative", "mermaid": ""}, [...] Er wordt automatisch een PDF versie als alternatief format aangemaakt.
  - *De bron bevestigt het gebruik van config.js en toont het content-veld. Het veld alternateFormats wordt indirect bevestigd via de PDF-generatie. De exacte 'var respecConfig = { ... }' syntax en het postProcess-veld worden niet expliciet vermeld.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs](https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs)
  - *De bron is de organisation-config.mjs zelf en beschrijft uitsluitend het nieuwe ES-module formaat. Over oudere repos met config.js, 'var respecConfig = { ... }' syntax, of extra velden zoals content en postProcess staat niets in deze bron.*

### `ls-pub-0017` — SKILL.md:109 *(§ GitHub Actions Workflows (Automatisering repo))*

> Alle standaarden-repos roepen centrale workflows aan uit de Automatisering repo (logius-standaarden/Automatisering).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius GitHub Actions workflows

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/Automatisering](https://github.com/logius-standaarden/Automatisering)
  > In de repository van iedere ReSpec-publicatie is een script te vinden dat de volgende handelingen uitvoert: Genereer statische HTML-pagina Controleer op WCAG-criteria Genereer PDF-bestand Publiceer naar logius.nl via Logius-standaarden/publicatie
  - *De bron bevestigt dat standaarden-repos gebruik maken van de Automatisering-repo (logius-standaarden/Automatisering) via centrale publicatiescripts. De claim spreekt specifiek van 'centrale workflows aanroepen' (GitHub Actions), wat impliciet wordt ondersteund door de beschrijving van gedeelde scripts, maar de bron specificeert niet expliciet dat het om GitHub Actions workflows gaat die centraal worden aangeroepen.*
- **NOT_FOUND** (medium) — [https://github.com/logius-standaarden/automatisering-test](https://github.com/logius-standaarden/automatisering-test)
  - *De brontekst beschrijft GitHub Actions workflows voor WCAG-checks en link-checks in de automatisering-test repo zelf, maar vermeldt nergens dat standaarden-repos centrale workflows aanroepen uit een Automatisering-repo. De workflows draaien 'zodra er een aanpassing gedaan wordt aan de main branch', maar er staat niets over een centrale Automatisering-repo als bron.*

### `ls-pub-0031` — SKILL.md:156 *(§ Nieuw Document Starten)*

> Voor een nieuw document moet ReSpec-template-Logius als basis worden gebruikt.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Logius nieuw ReSpec document starten

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  > "ReSpec template Logius - Template voor Afdeling Standaarden."
  - *De bron bevestigt dat de repository een template is voor Logius Afdeling Standaarden, wat de claim ondersteunt dat het als basis dient voor nieuwe documenten. De normatieve SHOULD-formulering ('moet worden gebruikt') wordt niet expliciet bevestigd.*

### `ls-pub-0038` — reference.md:9 *(§ Tech Radar)*

> De Tech Radar gebruikt vier ringen: Adopt (bewezen, actief aanbevolen), Trial (veelbelovend, actief getest), Assess (interessant, onderzocht), Hold (niet aanbevolen voor nieuw gebruik, wordt uitgefaseerd).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius Tech Radar

- **PARTIALLY_SUPPORTED** (medium) — [https://logius-standaarden.github.io/tech-radar](https://logius-standaarden.github.io/tech-radar)
  > ADOPT — Technologies we have high confidence in to serve our purpose [...] recommended to be widely used. TRIAL — Technologies that we have seen work with success [...] ASSESS — Technologies that are promising and have clear potential value-add [...] HOLD — Technologies not recommended to be used for new projects.
  - *De vier ringen en hun globale betekenis worden bevestigd. De claim dat Hold-technologieën 'worden uitgefaseerd' wordt echter niet ondersteund: de bron zegt expliciet 'usually can be continued for existing projects', wat eerder 'niet aanbevolen voor nieuw gebruik maar niet actief uitgefaseerd' impliceert.*

## UNGROUNDED — geen bron ondersteunt de claim (2)

### `ls-pub-0032` — SKILL.md:157 *(§ Nieuw Document Starten)*

> pubDomain accepteert alleen de waarden: api, bomos, dk, fsc, ftv, logboek of notificatieservices.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logius ReSpec configuratie pubDomain

*Mogelijk relevant in conflicts.md (§ pubDomain `ftv` (Federatieve Toegang Verlening)): conflicts.md vermeldt dat 'ftv' in maart 2026 als nieuw pubDomain is toegevoegd, wat de lijst beïnvloedt. De volledige geaccepteerde waardelijst wordt niet beschreven; alleen 'ftv' als toevoeging en 'dk' als context worden genoemd.*

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst bevat geen ReSpec-configuratieopties of toegestane waarden voor pubDomain.*

### `ls-pub-0033` — SKILL.md:157 *(§ Nieuw Document Starten)*

> shortName moet in kebab-case zijn: alleen kleine letters, gescheiden door streepjes (bijv. rest-api).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logius ReSpec configuratie shortName

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst bevat geen informatie over de shortName-configuratie of kebab-case vereisten.*

## NO_SOURCE — geen kandidaat-bron gevonden (22)

### `ls-pub-0001` — SKILL.md:37 *(§ Versiemodel van standaarden)*

> specStatus 'WV' (Werkversie/draft) publiceert naar logius-standaarden.github.io.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie-tooling versiemodel


### `ls-pub-0002` — SKILL.md:38 *(§ Versiemodel van standaarden)*

> specStatus 'CV' (Consultatieversie) publiceert naar logius-standaarden.github.io/Openbare-Consultaties/ en wordt automatisch ingesteld op consultatie/* branches.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie-tooling versiemodel


### `ls-pub-0003` — SKILL.md:39 *(§ Versiemodel van standaarden)*

> specStatus 'VV' (Versie ter vaststelling) publiceert naar gitdocumentatie.logius.nl.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie-tooling versiemodel


### `ls-pub-0004` — SKILL.md:40 *(§ Versiemodel van standaarden)*

> specStatus 'DEF' (Vastgestelde versie) publiceert naar gitdocumentatie.logius.nl.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publicatie-tooling versiemodel


### `ls-pub-0010` — SKILL.md:58 *(§ ReSpec Documentatie-systeem)*

> ReSpec genereert technische specificaties als HTML en PDF vanuit Markdown. Logius gebruikt een eigen fork met aangepaste huisstijl.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius ReSpec documentatie-systeem


### `ls-pub-0011` — SKILL.md:62 *(§ Hoe ReSpec werkt)*

> Het ReSpec hoofdbestand index.html laadt de ReSpec-engine en verwijst via data-include naar losse Markdown-bestanden per hoofdstuk.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius ReSpec documentatie-systeem


### `ls-pub-0018` — SKILL.md:113 *(§ build.yml - Document Generatie)*

> build.yml detecteert consultatie/* branches en overschrijft automatisch specStatus naar 'cv' via sed op config.mjs.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius build.yml workflow


### `ls-pub-0019` — SKILL.md:114 *(§ build.yml - Document Generatie)*

> HTML generatie in build.yml gebruikt het commando: npx respec --localhost --src index.html --out ~/static/index.html --haltonwarn.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius build.yml workflow


### `ls-pub-0020` — SKILL.md:115 *(§ build.yml - Document Generatie)*

> PDF generatie in build.yml verloopt via Puppeteer/headless Chrome met scripts/pdf.js.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius build.yml workflow


### `ls-pub-0021` — SKILL.md:118 *(§ check.yml - Kwaliteitschecks (3 parallelle checks))*

> check.yml voert drie parallelle checks uit: WCAG check, markdown lint en link validatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius check.yml workflow


### `ls-pub-0022` — SKILL.md:120 *(§ check.yml - Kwaliteitschecks (3 parallelle checks))*

> WCAG check in check.yml gebruikt: npx @axe-core/cli http://localhost:8080/index.html --tags wcag2aa.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius check.yml WCAG check


### `ls-pub-0023` — SKILL.md:120 *(§ check.yml - Kwaliteitschecks (3 parallelle checks))*

> axe-core dekt geautomatiseerd circa 30% van de WCAG-criteria; handmatige toetsing blijft nodig.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius WCAG check met axe-core


### `ls-pub-0024` — SKILL.md:120 *(§ check.yml - Kwaliteitschecks (3 parallelle checks))*

> axe-core implementeert gestandaardiseerde W3C ACT Rules; alternatieven zijn Alfa (Siteimprove) en QualWeb.

**Type:** reference_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius WCAG tooling


### `ls-pub-0025` — SKILL.md:121 *(§ check.yml - Kwaliteitschecks (3 parallelle checks))*

> Markdown lint in check.yml gebruikt: npx markdownlint-cli sections/.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius check.yml markdown lint


### `ls-pub-0026` — SKILL.md:127 *(§ publish.yml - Publicatie)*

> publish.yml publiceert bij push naar main/master naar de centrale publicatie-repo (gitdocumentatie.logius.nl).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publish.yml workflow


### `ls-pub-0027` — SKILL.md:128 *(§ publish.yml - Publicatie)*

> publish.yml publiceert bij push naar develop naar GitHub Pages van de standaarden-repo zelf.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publish.yml workflow


### `ls-pub-0028` — SKILL.md:129 *(§ publish.yml - Publicatie)*

> publish.yml publiceert bij een pull request een preview naar de Publicatie-Preview repo.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publish.yml workflow


### `ls-pub-0029` — SKILL.md:130 *(§ publish.yml - Publicatie)*

> publish.yml publiceert bij consultatie/* branches naar de Openbare-Consultaties repo.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius publish.yml workflow


### `ls-pub-0030` — SKILL.md:134 *(§ link-checker.yml - Gepubliceerde Links Controleren)*

> link-checker.yml controleert periodiek of de gepubliceerde versie op gitdocumentatie.logius.nl geen dode links bevat en stuurt een e-mail bij gevonden fouten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius link-checker.yml workflow


### `ls-pub-0035` — SKILL.md:169 *(§ Checks Lokaal Draaien)*

> axe-core test automatisch circa 30% van de WCAG 2.1 AA criteria; een groene check betekent niet dat het document volledig voldoet aan EN 301 549 / WCAG 2.1 AA.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Logius WCAG check interpretatie


### `ls-pub-0036` — SKILL.md:171 *(§ Checks Lokaal Draaien)*

> Handmatige toetsing op alle 55 succescriteria in WCAG 2.1 AA blijft nodig, ook na een groene axe-core check.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logius WCAG handmatige toetsing


### `ls-pub-0037` — SKILL.md:196 *(§ Consultatie Branch Gedrag)*

> Op consultatie/* branches wordt specStatus automatisch overschreven naar 'cv'; na merge naar main wordt specStatus uit js/config.mjs gebruikt.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius consultatie branch gedrag


## GROUNDED — minstens één bron ondersteunt de claim (3)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-pub-0009` — SKILL.md:54 *(§ Repositories)*

> De tech-radar repository valt onder de MIT licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius tech-radar repository

- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template](https://logius-standaarden.github.io/ReSpec-template)
  - *Bron status: unsupported*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/ReSpec-template-Logius](https://logius-standaarden.github.io/ReSpec-template-Logius)
  - *Bron status: unsupported*
- **SUPPORTED** (high) — [https://github.com/logius-standaarden/tech-radar](https://github.com/logius-standaarden/tech-radar)
  > MIT license ... License MIT license
  - *De brontekst vermeldt expliciet dat de tech-radar repository onder de MIT licentie valt.*
<details><summary>10x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/publicatie](https://github.com/logius-standaarden/publicatie)
  - *De bron bevat geen informatie over een tech-radar repository of de MIT licentie.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Publicatie-Preview](https://logius-standaarden.github.io/Publicatie-Preview)
  - *aangeleverde brontekst was leeg of onbruikbaar (alleen 'Loading...')*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/respec](https://github.com/logius-standaarden/respec)
  - *De bron gaat over de ReSpec-repo. De tech-radar repository en MIT-licentie worden niet vermeld.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron behandelt de ReSpec-template repository. Er is geen vermelding van een tech-radar repository of MIT licentie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template-Logius](https://github.com/logius-standaarden/ReSpec-template-Logius)
  - *De brontekst behandelt de ReSpec-template-Logius repository, niet de tech-radar repository.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Openbare-Consultaties](https://github.com/logius-standaarden/Openbare-Consultaties)
  - *De brontekst bevat geen informatie over een tech-radar repository of MIT licentie.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/Openbare-Consultaties](https://logius-standaarden.github.io/Openbare-Consultaties)
  - *De brontekst bevat geen informatie over een tech-radar repository of MIT licentie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/Automatisering](https://github.com/logius-standaarden/Automatisering)
  - *De brontekst bevat geen informatie over een tech-radar repository of MIT licentie.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/automatisering-test](https://github.com/logius-standaarden/automatisering-test)
  - *De brontekst gaat niet over een tech-radar repository of MIT licentie.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/tech-radar](https://logius-standaarden.github.io/tech-radar)
  - *De brontekst bevat geen informatie over de licentie van de tech-radar repository zelf.*
</details>

### `ls-pub-0013` — SKILL.md:75 *(§ ReSpec Configuratie (js/config.mjs))*

> De ReSpec config.mjs laadt ReSpec via https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius ReSpec configuratie

- **SUPPORTED** (high) — [https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs](https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs)
  > import { loadRespecWithConfiguration } from "https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs";
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron vermeldt dat er een organisation config bestaat die 'centraal gepubliceerd' staat en automatisch wordt ingeladen, maar noemt geen specifieke URL zoals https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs.*

### `ls-pub-0014` — SKILL.md:84 *(§ ReSpec Configuratie (js/config.mjs))*

> De ReSpec configuratieparameter pubDomain accepteert alleen de waarden: api, bomos, dk, fsc, ftv, logboek of notificatieservices.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Logius ReSpec configuratie

- **SUPPORTED** (high) — [https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs](https://logius-standaarden.github.io/publicatie/respec/organisation-config.mjs)
  > const ACCEPTED_DOMAINS = ['api', 'bomos', 'dk', 'digimelding', 'fsc', 'ftv', 'logboek', 'notificatieservices']; if (!ACCEPTED_DOMAINS.includes(config.pubDomain)) { utils.showError(`Invalid pubDomain. Must be one of ${ACCEPTED_DOMAINS}, but was "${config.pubDomain}"`); }
  - *De bron bevat ook 'digimelding' in de lijst, wat de claim niet noemt. De claim is dus iets onvolledig, maar niet onjuist — SUPPORTED omdat de genoemde waarden kloppen en de validatie duidelijk is.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/ReSpec-template](https://github.com/logius-standaarden/ReSpec-template)
  - *De bron noemt de configuratie van ReSpec documenten en verwijst naar de Logius ReSpec wiki voor meer informatie, maar bespreekt de parameter pubDomain of toegestane waarden niet.*

</details>
