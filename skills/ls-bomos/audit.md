<!-- markdownlint-disable MD052 MD034 MD013 MD038 -->
# Audit ls-bomos — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 3 | 9% |
| CONTRADICTED | 1 | 3% |
| PARTIALLY_GROUNDED | 13 | 37% |
| UNGROUNDED | 0 | 0% |
| NO_SOURCE | 0 | 0% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 1 | 3% |
| GROUNDED | 17 | 49% |

*Geverifieerd met sonnet, 20 calls, $1.9940.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (3)

### `ls-bomos-0010` — SKILL.md:80 *(§ Wijzigingsbeheer Workflow)*

> Het RFC-proces binnen BOMOS verloopt via de stappen: RFC indienen → Community review → Expert beoordeling → Autorisator besluit → Implementatie → Publicatie nieuwe versie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS RFC-procedure

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  - *De specifieke RFC-processtappen zoals beschreven in de claim worden nergens in de bron vermeld.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron beschrijft stappen in het wijzigingsproces (verzamelen wensen, voorbereiden veranderingsvoorstellen, beoordeling en besluitvorming) maar niet in de exacte volgorde of terminologie zoals in de claim: 'RFC indienen → Community review → Expert beoordeling → Autorisator besluit → Implementatie → Publicatie nieuwe versie'.*

### `ls-bomos-0031` — reference.md:107 *(§ Pressure Cooker Model)*

> Het Pressure Cooker Model is geschikt voor standaarden waar urgentie en breed draagvlak samenkomen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS Pressure Cooker Model

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  - *De bron vermeldt de pressure cooker alleen als een methode om 'sneller en goedkoper standaarden te ontwikkelen', maar zegt niets over toepassingscriteria zoals urgentie en breed draagvlak.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron beschrijft het pressure cooker model als efficiënt middel, maar koppelt het niet expliciet aan 'urgentie en breed draagvlak' als voorwaarden voor geschiktheid. De kwaliteit wordt gerelateerd aan de werkgroepleden, niet aan urgentie/draagvlak als vereiste combinatie.*

### `ls-bomos-0034` — reference.md:121 *(§ Linked Data Module)*

> De BOMOS Linked Data module behandelt URI-strategie, versiebeheer van ontologieën, en publicatie als Linked Data.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS Linked Data module

- **NOT_FOUND** (medium) — [https://github.com/logius-standaarden/BOMOS-LinkedData](https://github.com/logius-standaarden/BOMOS-LinkedData)
  - *De brontekst beschrijft alleen de repository-pagina van BOMOS-LinkedData op GitHub (README, bestandslijst, metadata). De inhoud van de module zelf (URI-strategie, versiebeheer van ontologieën, publicatie als Linked Data) is niet aanwezig in de aangeleverde tekst. De titel suggereert dat de module over linked data gaat, maar de specifieke onderwerpsclaims kunnen niet worden bevestigd op basis van de aangeleverde brontekst.*

## CONTRADICTED — bron spreekt de claim expliciet tegen (1)

### `ls-bomos-0007` — SKILL.md:47 *(§ Repositories)*

> BOMOS-Aanvullende-Modules is gearchiveerd en heeft geen actieve publicatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS aanvullende modules

- **SUPPORTED** (high) — [https://github.com/logius-standaarden/BOMOS-Aanvullende-Modules](https://github.com/logius-standaarden/BOMOS-Aanvullende-Modules)
  > This repository was archived by the owner on May 1, 2025. It is now read-only.
  - *De bron bevestigt expliciet dat de repository gearchiveerd is en read-only. Geen actieve publicatie is daarmee bevestigd.*
- **CONTRADICTED** (medium) — [https://logius-standaarden.github.io/BOMOS-LinkedData](https://logius-standaarden.github.io/BOMOS-LinkedData)
  > Deze versie: https://logius-standaarden.github.io/BOMOS-LinkedData/ Laatst gepubliceerde versie: https://gitdocumentatie.logius.nl/publicatie/bomos/linkeddata/ ... Status van dit document: Dit is een werkversie die op elk moment kan worden gewijzigd, verwijderd of vervangen door andere documenten.
  - *De bron toont een actieve werkversie van een BOMOS aanvullende module (Linked Data), gedateerd 09 maart 2026. Dit weerspreekt de claim dat BOMOS aanvullende modules gearchiveerd zijn zonder actieve publicatie. Wel is dit een werkversie (niet formeel vastgesteld), maar van archivering is geen sprake. De claim spreekt over 'BOMOS-Aanvullende-Modules' generiek; deze bron dekt slechts één module (Linked Data), dus het verdict is gebaseerd op wat de bron laat zien.*
- **CONTRADICTED** (high) — [https://logius-standaarden.github.io/BOMOS-Stelsels](https://logius-standaarden.github.io/BOMOS-Stelsels)
  > Werkversie 09 maart 2026 ... Status van dit document: Dit is een werkversie die op elk moment kan worden gewijzigd, verwijderd of vervangen door andere documenten.
  - *De bron is een actieve werkversie gedateerd 09 maart 2026 met een live URL en redacteurs. Er is geen sprake van archivering; de module is actief gepubliceerd en wordt bijgehouden (zie documentbeheer: laatste wijziging 15/06/2025).*
<details><summary>5x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/BOMOS-LinkedData](https://github.com/logius-standaarden/BOMOS-LinkedData)
  - *De brontekst gaat over de BOMOS-LinkedData repository en noemt BOMOS-Aanvullende-Modules niet.*
- **NOT_FOUND** (medium) — [https://github.com/logius-standaarden/BOMOS-OpenSource](https://github.com/logius-standaarden/BOMOS-OpenSource)
  - *De brontekst gaat over BOMOS-OpenSource, niet over een module genaamd 'BOMOS-Aanvullende-Modules'. Of die specifieke module gearchiveerd is en geen actieve publicatie heeft, blijkt niet uit deze bron.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/BOMOS-OpenSource](https://logius-standaarden.github.io/BOMOS-OpenSource)
  - *De bron gaat over BOMOSS (BOMOS voor Open Source Software) en vermeldt niets over 'BOMOS-Aanvullende-Modules' of de archiefstatus daarvan.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/BOMOS-Stelsels](https://github.com/logius-standaarden/BOMOS-Stelsels)
  - *De brontekst is de README van BOMOS-Stelsels. Er wordt geen melding gemaakt van een repository genaamd 'BOMOS-Aanvullende-Modules' of de status daarvan (gearchiveerd of niet). De vermelde BOMOS-documenten zijn: Fundament, Verdieping, Stelsels, Linked Data en Beheermodel.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/BOMOS-Beheermodel](https://github.com/logius-standaarden/BOMOS-Beheermodel)
  - *De brontekst is de README van de BOMOS-Beheermodel repository. Er worden wel aanvullende modules genoemd (BOMOS Stelsels, BOMOS Linked Data), maar er staat niets over archivering of het ontbreken van een actieve publicatie van aanvullende modules.*
</details>

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (13)

### `ls-bomos-0001` — SKILL.md:32 *(§ Versiemodel)*

> BOMOS is geen interoperabiliteitsstandaard en staat niet op de 'pas-toe-of-leg-uit'-lijst van het Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS - Beheer- en Ontwikkelmodel voor Open Standaarden

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Overigens, als de beheerorganisatie conform BOMOS werkt, dan wil dat niet automatisch zeggen dat de standaard daarmee ook voldoet aan de criteria voor de pas-toe of leg-uit lijst van standaarden van de overheid. Echter het is wel te prefereren dat aangemelde standaarden conform BOMOS werken
  - *De bron bevestigt dat BOMOS-conformiteit niet automatisch leidt tot plaatsing op de pas-toe-of-leg-uit-lijst, maar zegt niet expliciet dat BOMOS zelf niet op die lijst staat. De claim dat BOMOS 'geen interoperabiliteitsstandaard' is wordt ook niet letterlijk bevestigd; BOMOS wordt een 'standaard voor standaarden' genoemd.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron noemt de 'pas-toe-of-leg-uit'-lijst van het Forum Standaardisatie meerdere keren in de context van andere standaarden, maar zegt nergens expliciet dat BOMOS zelf niet op die lijst staat of geen interoperabiliteitsstandaard is.*

### `ls-bomos-0009` — SKILL.md:58 *(§ Wijzigingsbeheer Workflow)*

> De RFC-procedure (Request for Change) is het kernproces voor wijzigingsbeheer binnen BOMOS.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS wijzigingsbeheer

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Op een moment dat de indiener dit aangeeft dient de wens of eis opgenomen te worden als request for change of wijzigingsverzoek.
  - *De bron noemt het RFC/wijzigingsverzoek-concept maar beschrijft het niet expliciet als 'het kernproces voor wijzigingsbeheer binnen BOMOS'. De procedure wordt beschreven als onderdeel van het operationele beheerproces, maar de centrale/kern-status wordt niet zo benoemd.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  - *De bron beschrijft het wijzigingsproces via wensen en eisen, maintenance requests, etc., maar noemt de term 'RFC-procedure' of 'Request for Change' niet als kernproces.*

### `ls-bomos-0012` — SKILL.md:181 *(§ BOMOS Conformiteit Checklist)*

> Een organisatie werkt conform BOMOS wanneer voor elke activiteit een bewuste beschrijving is opgenomen, ook als die beschrijving is: 'deze activiteit vullen wij (nog) niet in.'

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** BOMOS conformiteit

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > De beheerorganisatie werkt conform BOMOS als er een beheerdocument is gepubliceerd waarin de invulling van alle onderdelen uit het BOMOS Activiteitendiagram (het Beheer- en Ontwikkelmodel) zijn beschreven.
  - *De bron stelt dat alle onderdelen beschreven moeten zijn, maar zegt niet expliciet dat 'niet invullen' ook als bewuste beschrijving volstaat. De claim is specifieker dan de bron op dit punt.*
- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron beschrijft het BOMOS-model uitgebreid maar formuleert nergens een conformiteitseis zoals beschreven in de claim, namelijk dat elke activiteit bewust beschreven moet zijn, ook met 'deze activiteit vullen wij (nog) niet in'.*

### `ls-bomos-0014` — reference.md:13 *(§ Het BOMOS Activiteitenmodel)*

> De strategielaag van BOMOS bevat de activiteiten Governance, Visie, en Financiering, met de rollen Houder en Financier.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS strategielaag

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Strategie: Richtinggevende activiteiten gerelateerd aan de strategische (lange) termijn: Governance [...] Visie [...] Financiën [...] Activiteit Primair verantwoordelijke rol: Strategie - Eigenaar, financier
  - *De bron bevestigt Governance, Visie en Financiën als strategieactiviteiten, en Financier als rol. Maar de claim noemt 'Houder'; de bron gebruikt de term 'Eigenaar', niet 'Houder'. Dat is een terminologisch verschil.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Houder: Governance, Visie, Rechtenbeleid, Adoptie en erkenning (beleid) [...] Financier: Financiën
  - *De bron bevestigt Governance en Visie als activiteiten in de strategielaag, en de rollen Houder en Financier. Maar 'Financiering' als activiteitsnaam wordt in de bron aangeduid als 'Financiën' (sectie 2.2). De claim noemt 'Financiering', de bron noemt 'Financiën'.*

### `ls-bomos-0015` — reference.md:23 *(§ Het BOMOS Activiteitenmodel)*

> De tactieklaag van BOMOS bevat de activiteiten Architectuur, Specificatiebeheer, Wijzigingsbeheer, Adoptiestrategie, Kwaliteitsbeleid, Rechtenmanagement, en Community, met de rol Autorisator.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS tactieklaag

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Tactiek: Activiteiten die op middellang termijn voor stabiliteit zorgen: Adoptie & erkenning [...] Architectuur [...] Community [...] Kwaliteitsbeleid benchmarking [...] Rechtenbeleid [...] Autorisator
  - *De bron bevestigt Architectuur, Community, Kwaliteitsbeleid, Rechtenbeleid, Adoptie & erkenning en de rol Autorisator. Maar 'Specificatiebeheer' en 'Wijzigingsbeheer' als aparte activiteiten worden niet vermeld. De claim noemt meer activiteiten dan de bron beschrijft.*
- **NOT_FOUND** (low) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron beschrijft tactische activiteiten (Community, Architectuur, Adoptie & Erkenning, Kwaliteitsbeleid) en noemt de rol Autorisator, maar de volledige lijst uit de claim (Specificatiebeheer, Wijzigingsbeheer, Rechtenmanagement) wordt niet als zodanig als tactische laag-activiteiten benoemd in deze brontekst.*

### `ls-bomos-0016` — reference.md:37 *(§ Het BOMOS Activiteitenmodel)*

> De operationele laag van BOMOS bevat de activiteiten Initiatie, Wensen en eisen verzamelen, Ontwikkeling, Uitvoering, Documentatie, en Klachtenafhandeling, met de rollen Functioneel Beheerder en Technisch Beheerder.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS operationele laag

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Operationeel: De uitvoerende activiteiten die leiden tot nieuwe versies van standaarden, waaronder: Initiatie [...] Wensen en eisen [...] Ontwikkeling [...] Uitvoeren [...] Documentatie [...] Functioneel beheerder, Technisch beheerder
  - *De bron bevestigt Initiatie, Wensen en eisen, Ontwikkeling, Uitvoeren, Documentatie en de rollen Functioneel Beheerder en Technisch Beheerder. Maar 'Klachtenafhandeling' staat in de bron onder de Communicatielaag, niet onder Operationeel.*
- **NOT_FOUND** (low) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron behandelt operationele activiteiten zoals wensen/eisen verzamelen, wijzigingsvoorstellen, besluitvorming, en noemt rollen Functioneel Beheerder en Technisch Beheerder, maar de volledige en exacte opsomming van de operationele laag zoals in de claim wordt niet als zodanig gepresenteerd in deze brontekst.*

### `ls-bomos-0017` — reference.md:50 *(§ Het BOMOS Activiteitenmodel)*

> De implementatieondersteuningslaag van BOMOS bevat de activiteiten Helpdesk, Opleidingen, Open source modules, Pilots, en Validatie en certificatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS implementatieondersteuning

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Implementatie-ondersteuning, ondersteunende activiteiten gericht op het bevorderen van implementaties van de standaard, waaronder: Opleiding [...] Helpdesk [...] Module-ontwikkeling [...] Pilot [...] Validatie & Certificatie
  - *De bron bevestigt Helpdesk, Opleiding, Module-ontwikkeling (niet 'Open source modules'), Pilots en Validatie & Certificatie. De claim gebruikt 'Open source modules' waar de bron 'Module-ontwikkeling' zegt.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Een helpdesk functionaliteit is minimaal voor een beheerorganisatie. [...] Met het bieden van opleidingen [...] open source modules te ontwikkelen. [...] Laag drempeliger is het om pilots te organiseren. [...] Vooral een lichtere vorm van certificatie, validatie is een goede vorm van implementatie-ondersteuning.
  - *De bron bevestigt helpdesk, opleidingen, open source modules, pilots en validatie/certificatie als vormen van implementatieondersteuning. Echter ze worden niet expliciet als een formele lijst van vijf activiteiten van een 'implementatieondersteuningslaag' gepresenteerd.*

### `ls-bomos-0019` — reference.md:51 *(§ Het BOMOS Activiteitenmodel)*

> Opleidingen binnen BOMOS-implementatieondersteuning mogen niet concurreren met de markt; ze worden alleen aangeboden waar de markt niet voorziet.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD_NOT  ·  **Scope:** BOMOS implementatieondersteuning - Opleidingen

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Met het bieden van opleidingen kom je als beheerorganisatie al sneller in het vaarwater van anderen. Toch kan het in een beginstadium wel essentieel zijn om het aan te bieden, vooral ook om de kwaliteit van de implementaties te verhogen, en implementaties laagdrempeliger maken.
  - *De bron stelt dat opleidingen aanbieden je 'in het vaarwater van anderen' brengt en dat het alleen in beginstadium essentieel kan zijn. Dit ondersteunt de gedachte dat concurrentie vermeden moet worden, maar de expliciete formulering 'alleen waar de markt niet voorziet' staat niet letterlijk in de bron.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  - *De bron beschrijft opleidingen als activiteit maar stelt nergens dat ze niet mogen concurreren met de markt of alleen aangeboden mogen worden waar de markt niet voorziet.*

### `ls-bomos-0021` — reference.md:60 *(§ Het BOMOS Activiteitenmodel)*

> De communicatielaag van BOMOS bevat de activiteiten Promotie en Publicatie, met de rol Distributeur.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS communicatielaag

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Communicatie, ondersteunende activiteiten gericht op het creëren van draagvlak voor de standaard, waaronder: Promotie [...] Publicatie [...] Klachtenafhandeling [...] Distributeur
  - *De bron bevestigt Promotie, Publicatie en de rol Distributeur. Maar de claim vermeldt alleen Promotie en Publicatie; de bron noemt ook Klachtenafhandeling als communicatieactiviteit, wat de claim weglaat. Geen tegenspraak, wel onvolledigheid in de claim.*
- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Distributeur: Promotie, Publicatie
  - *De tabel met rollen en BOMOS-activiteiten bevestigt dat de Distributeur de activiteiten Promotie en Publicatie heeft. Echter de claim stelt dit als onderdeel van een 'communicatielaag' — de bron vermeldt wel een hoofdstuk Communicatie (6) maar koppelt Promotie/Publicatie in de tabel primair aan de rol Distributeur, niet expliciet als 'communicatielaag'. Deels ondersteund.*

### `ls-bomos-0023` — reference.md:80 *(§ Rollen en Verantwoordelijkheden)*

> Binnen BOMOS kan een persoon meerdere rollen vervullen, en een rol kan door meerdere personen worden ingevuld.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS rollenmodel

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Van bovenstaande rollen kunnen de financier-rol, de expert-rol, de gebruikers-rol en de eindgebruikers-rol meervoudig worden ingevuld: meer dan één persoon of organisatie kan de rol van financier, expert, gebruiker of eindgebruiker vervullen. De overige rollen zijn enkelvoudig
  - *De bron stelt dat sommige rollen meervoudig zijn en andere enkelvoudig. De claim dat 'een persoon meerdere rollen kan vervullen' wordt niet expliciet bevestigd; wel dat meerdere personen dezelfde rol kunnen invullen (meervoudig). De claim combineert twee dingen die de bron niet volledig zo stelt.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron beschrijft de rollen en hun activiteiten, maar bevat geen expliciete uitspraak dat één persoon meerdere rollen kan vervullen of dat één rol door meerdere personen kan worden ingevuld.*

### `ls-bomos-0027` — reference.md:96 *(§ Conformiteit)*

> Het BOMOS beheerdocument hoeft niet voor elk onderdeel uitgebreid te zijn; bij sommige activiteiten volstaat een bewuste keuze om deze (nog) niet in te vullen.

**Type:** normative_requirement  ·  **Modaliteit:** MAY  ·  **Scope:** BOMOS conformiteit

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > De invulling van de ontwikkel- en beheeronderwerpen zijn situationeel afhankelijk [...] Het is dus zeker niet zo dat elk onderwerp moet worden geïmplementeerd.
  - *De bron bevestigt dat niet elk onderwerp geïmplementeerd hoeft te worden, maar zegt niet expliciet dat een bewuste keuze om iets 'niet in te vullen' volstaat als beschrijving in het beheerdocument.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron bevat geen uitspraken over minimale vereisten voor BOMOS-conformiteit of dat bij sommige activiteiten een bewuste keuze om ze niet in te vullen volstaat.*

### `ls-bomos-0033` — reference.md:117 *(§ Praktijkvoorbeelden)*

> TOOI (Thesaurus en Ontologie voor OverheidsInformatie) gebruikt BOMOS als basis voor hun beheerplan en beschrijft per BOMOS-activiteit hoe deze wordt ingevuld.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS praktijkvoorbeelden - TOOI

- **PARTIALLY_SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Het beheerplan TOOI is opgezet volgens de principes uit BOMOS. De invulling van de 5 thema's uit BOMOS (Strategie, Tactiek, Operationeel, Implementatieondersteuning en Communicatie) zijn uitgebreid beschreven op de website.
  - *De bron bevestigt dat TOOI BOMOS als basis gebruikt en de thema's beschrijft, maar spreekt van 'thema's' beschreven op de website, niet expliciet van 'per BOMOS-activiteit'. De strekking klopt grotendeels maar de precisering 'per activiteit' staat er niet letterlijk.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *TOOI (Thesaurus en Ontologie voor OverheidsInformatie) wordt in de aangeleverde brontekst niet vermeld.*

### `ls-bomos-0035` — reference.md:127 *(§ Open Source Module)*

> De BOMOS Open Source module beschrijft governance voor open source componenten, inclusief licentiekeuze, contributor agreements, en beheer van referentie-implementaties.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS Open Source module

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/BOMOS-OpenSource](https://github.com/logius-standaarden/BOMOS-OpenSource)
  > Deze handreiking probeert een kader te geven waarmee open source code open beheerd kan worden. Het Beheer- en ontwikkelmodel Open Standaarden is ontwikkeld als een handreiking voor het beheer van standaarden. Deze handreiking beoogt ondersteuning aan het beheer van open source code te geven vanuit de BOMOS bril.
  - *De bron bevestigt dat de module governance voor open source code beschrijft. Licentiekeuze, contributor agreements en beheer van referentie-implementaties worden echter niet expliciet als onderwerpen genoemd in de brontekst; die details zijn niet te verifiëren op basis van de aangeleverde README-tekst alleen.*

## KNOWN_DISCREPANCY — gedocumenteerd in conflicts.md (1)

### `ls-bomos-0008` — SKILL.md:49 *(§ Repositories)*

> BOMOS-OpenSource is gearchiveerd en heeft een bevroren draft publicatie, gepubliceerd onder de W3C Software and Document License.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS-OpenSource module

**Erkend in conflicts.md** *(§ Licentie-status GitHub-repositories)*: conflicts.md beschrijft expliciet: 'BOMOS-OpenSource | W3C Software License | CC0-1.0 (ReSpec) | Afwijkend'. De discrepantie tussen de GitHub LICENSE (W3C Software License) en de gepubliceerde licentie is gedocumenteerd. Archivering wordt niet vermeld, maar de licentieconflicten zijn de kern van de CONTRADICTED-verdicts.

- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/BOMOS-OpenSource](https://github.com/logius-standaarden/BOMOS-OpenSource)
  > This repository was archived by the owner on Aug 28, 2025. It is now read-only.
  - *De bron bevestigt dat BOMOS-OpenSource gearchiveerd is. De claim over 'bevroren draft publicatie' is niet verifieerbaar uit de brontekst. De licentie is vermeld als 'View license' maar de W3C Software and Document License wordt nergens expliciet bij naam genoemd; de repo verwijst naar een LICENSE bestand zonder de inhoud te tonen.*
- **CONTRADICTED** (high) — [https://logius-standaarden.github.io/BOMOS-OpenSource](https://logius-standaarden.github.io/BOMOS-OpenSource)
  > Dit document valt onder de volgende licentie: Creative Commons 0 Public Domain Dedication
  - *De claim stelt dat het document gepubliceerd is onder de W3C Software and Document License, maar de bron vermeldt expliciet Creative Commons 0 Public Domain Dedication als licentie. Bovendien is het document een actieve werkversie ('Werkversie 25 augustus 2025'), niet een bevroren draft. Over archivering wordt niets vermeld.*
- **PARTIALLY_SUPPORTED** (medium) — [https://raw.githubusercontent.com/logius-standaarden/BOMOS-OpenSource/main/LICENSE](https://raw.githubusercontent.com/logius-standaarden/BOMOS-OpenSource/main/LICENSE)
  > The W3C SOFTWARE NOTICE AND LICENSE (W3C) https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document ... Permission to copy, modify, and distribute this work, with or without modification, for any purpose and without fee or royalty is hereby granted
  - *De bron bevestigt dat het werk gepubliceerd is onder de W3C Software and Document License. De claim dat BOMOS-OpenSource 'gearchiveerd is en een bevroren draft publicatie heeft' wordt niet ondersteund noch weersproken door deze licentietekst — die informatie staat niet in de LICENSE-file zelf.*
- **PARTIALLY_SUPPORTED** (medium) — [https://raw.githubusercontent.com/logius-standaarden/BOMOS-OpenSource/master/LICENSE](https://raw.githubusercontent.com/logius-standaarden/BOMOS-OpenSource/master/LICENSE)
  > The W3C SOFTWARE NOTICE AND LICENSE (W3C) https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document [...] Permission to copy, modify, and distribute this work, with or without modification, for any purpose and without fee or royalty is hereby granted
  - *De bron bevestigt dat de W3C Software and Document License van toepassing is op dit werk, wat het licentiedeel van de claim ondersteunt. De claim dat het werk 'gearchiveerd' is en een 'bevroren draft publicatie' heeft, wordt niet bevestigd noch tegengesproken door deze licensetekst — dat is publicatie-metadata die niet in een LICENSE-bestand staat.*
<details><summary>4x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/BOMOS-Aanvullende-Modules](https://github.com/logius-standaarden/BOMOS-Aanvullende-Modules)
  - *De brontekst gaat over BOMOS-Aanvullende-Modules, niet over een aparte BOMOS-OpenSource repository. Er is geen informatie over een W3C Software and Document License of een bevroren draft publicatie voor een OpenSource module.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/BOMOS-LinkedData](https://github.com/logius-standaarden/BOMOS-LinkedData)
  - *De brontekst gaat over de BOMOS-LinkedData repository en noemt BOMOS-OpenSource niet.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/BOMOS-LinkedData](https://logius-standaarden.github.io/BOMOS-LinkedData)
  - *De bron gaat uitsluitend over de BOMOS Linked Data module. BOMOS-OpenSource, archiveringsstatus daarvan, of een W3C Software and Document License worden nergens in de tekst vermeld.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/BOMOS-Stelsels](https://github.com/logius-standaarden/BOMOS-Stelsels)
  - *De brontekst bevat geen verwijzing naar een 'BOMOS-OpenSource' module, de archiefstatus ervan, of de W3C Software and Document License. Dit valt buiten de scope van de aangeleverde BOMOS-Stelsels README.*
</details>

## GROUNDED — minstens één bron ondersteunt de claim (17)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-bomos-0002` — SKILL.md:32 *(§ Versiemodel)*

> BOMOS is een raamwerk voor het beheren van open standaarden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS - Beheer- en Ontwikkelmodel voor Open Standaarden

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > BOMOS (Beheer- en OntwikkelModel voor Open Standaarden) is een hulpmiddel van en voor de standaardisatiewereld.
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Het doel van deze publicatie is organisaties te helpen bij het opzetten van het beheer van standaarden en de verbetering daarvan.
  - *De bron beschrijft BOMOS consistent als een Beheer- en OntwikkelModel voor Open Standaarden, een raamwerk gericht op het beheren van open standaarden.*

### `ls-bomos-0003` — SKILL.md:29 *(§ Versiemodel)*

> BOMOS kent twee publicatiekanalen: een vastgestelde versie (DEF) gepubliceerd op gitdocumentatie.logius.nl, en een werkversie (draft) gepubliceerd op logius-standaarden.github.io.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS versiemodel

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Deze versie: https://gitdocumentatie.logius.nl/publicatie/bomos/fundament/3.0.2/ [...] Laatste werkversie: https://logius-standaarden.github.io/BOMOS-Fundament/
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Deze versie: https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping/3.1.0/ [...] Laatste werkversie: https://logius-standaarden.github.io/BOMOS-Verdieping/
  - *De bron toont beide publicatiekanalen in de header: gitdocumentatie.logius.nl voor de vastgestelde versie en logius-standaarden.github.io voor de werkversie.*

### `ls-bomos-0004` — SKILL.md:40 *(§ Repositories)*

> BOMOS-Fundament v3.0.2 is de vastgestelde versie, gepubliceerd op gitdocumentatie.logius.nl/publicatie/bomos/fundament/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS-Fundament

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > BOMOS, het fundament 3.0.2 Logius Handreiking Vastgestelde versie 02 november 2023 Deze versie: https://gitdocumentatie.logius.nl/publicatie/bomos/fundament/3.0.2/
- **PARTIALLY_SUPPORTED** (low) — [https://github.com/logius-standaarden/BOMOS-Fundament](https://github.com/logius-standaarden/BOMOS-Fundament)
  > Vastgestelde versie 07 juni 2022
  - *De bron bevestigt dat er een vastgestelde versie bestaat (gepubliceerd op 07 juni 2022), maar vermeldt geen versienummer v3.0.2 en noemt de URL gitdocumentatie.logius.nl/publicatie/bomos/fundament/ niet. De gepubliceerde versie-URL ontbreekt in de aangeleverde tekst.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/BOMOS-Fundament](https://logius-standaarden.github.io/BOMOS-Fundament)
  - *Bron status: unsupported*
<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron (BOMOS Verdieping) verwijst naar het Fundament als apart document maar noemt geen specifiek versienummer v3.0.2 voor het Fundament.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/BOMOS-Verdieping](https://github.com/logius-standaarden/BOMOS-Verdieping)
  - *De brontekst vermeldt versienummers noch een publicatie-URL voor BOMOS-Fundament. Alleen de naam 'BOMOS Fundament' wordt genoemd als onderdeel van de documentatieset.*
- **NOT_FOUND** (high) — [https://logius-standaarden.github.io/BOMOS-Verdieping](https://logius-standaarden.github.io/BOMOS-Verdieping)
  - *De bron is BOMOS-Verdieping en bevat geen informatie over de BOMOS-Fundament versie of publicatielocatie. Dit document gaat uitsluitend over BOMOS Deel 2: De Verdieping.*
</details>

### `ls-bomos-0005` — SKILL.md:41 *(§ Repositories)*

> BOMOS-Verdieping v3.1.0 is de vastgestelde versie, gepubliceerd op gitdocumentatie.logius.nl/publicatie/bomos/verdieping/.

**Type:** version_claim  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS-Verdieping

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > BOMOS Deel 2: de verdieping 3.1.0 Logius Handreiking Vastgestelde versie 19 september 2025 Deze versie: https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping/3.1.0/
  - *De brontekst bevestigt expliciet dat v3.1.0 de vastgestelde versie is, gepubliceerd op gitdocumentatie.logius.nl.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/BOMOS-Fundament](https://logius-standaarden.github.io/BOMOS-Fundament)
  - *Bron status: unsupported*
- **SUPPORTED** (high) — [https://logius-standaarden.github.io/BOMOS-Verdieping](https://logius-standaarden.github.io/BOMOS-Verdieping)
  > BOMOS Deel 2: de verdieping 3.1.0 Logius Handreiking Vastgestelde versie 19 september 2025 Deze versie: https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping/3.1.0/ Laatst gepubliceerde versie: https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping/
  - *De bron bevestigt zowel versienummer 3.1.0 als de publicatielocatie op gitdocumentatie.logius.nl/publicatie/bomos/verdieping/.*
<details><summary>3x NOT_FOUND (klap uit)</summary>

- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  - *De bron gaat over BOMOS-Fundament. De versie van BOMOS-Verdieping (v3.1.0) wordt nergens in deze tekst vermeld.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/BOMOS-Fundament](https://github.com/logius-standaarden/BOMOS-Fundament)
  - *De bron vermeldt BOMOS-Verdieping als apart document maar geeft geen versienummer (v3.1.0) en geen URL voor de vastgestelde versie. Deze claim gaat over een apart repository en valt buiten wat deze brontekst behandelt.*
- **NOT_FOUND** (high) — [https://github.com/logius-standaarden/BOMOS-Verdieping](https://github.com/logius-standaarden/BOMOS-Verdieping)
  - *De brontekst noemt geen versienummer voor BOMOS-Verdieping en geen publicatie-URL op gitdocumentatie.logius.nl. Wel staat er een link naar een 'Vastgestelde versie 07 juni 2022' maar zonder versienummer v3.1.0.*
</details>

### `ls-bomos-0006` — SKILL.md:40 *(§ Repositories)*

> BOMOS-Fundament en BOMOS-Verdieping zijn gepubliceerd onder de CC-BY-4.0 licentie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS kerndocumenten

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Dit document valt onder de volgende licentie: Creative Commons Attribution 4.0 International Public License
  - *Geldt voor het Fundament-document. De bron bevestigt de CC-BY-4.0 licentie voor dit document; de Verdieping wordt niet behandeld in deze bron.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Dit document valt onder de volgende licentie: Creative Commons Attribution 4.0 International Public License
  - *CC BY 4.0 is de gangbare aanduiding voor Creative Commons Attribution 4.0 International Public License. De bron bevestigt dit voor de Verdieping; de claim spreekt over beide kerndocumenten, maar de bron dekt alleen de Verdieping.*
- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/BOMOS-Fundament](https://github.com/logius-standaarden/BOMOS-Fundament)
  > CC-BY-4.0 license
  - *De bron bevestigt de CC-BY-4.0 licentie voor BOMOS-Fundament. BOMOS-Verdieping wordt wel vermeld als apart document, maar de licentie daarvan is niet bevestigd in deze brontekst. De claim stelt dat beide documenten onder CC-BY-4.0 vallen; voor Verdieping ontbreekt bevestiging.*
- **SOURCE_UNAVAILABLE** (high) — [https://logius-standaarden.github.io/BOMOS-Fundament](https://logius-standaarden.github.io/BOMOS-Fundament)
  - *Bron status: unsupported*
- **PARTIALLY_SUPPORTED** (medium) — [https://github.com/logius-standaarden/BOMOS-Verdieping](https://github.com/logius-standaarden/BOMOS-Verdieping)
  > CC-BY-4.0 license (vermeld onder 'License' in de repository-metadata van BOMOS-Verdieping)
  - *De bron bevestigt CC-BY-4.0 voor BOMOS-Verdieping. De bron vermeldt niets over de licentie van BOMOS-Fundament, dus de claim dat beide documenten onder CC-BY-4.0 vallen is slechts gedeeltelijk onderbouwd.*
- **PARTIALLY_SUPPORTED** (high) — [https://logius-standaarden.github.io/BOMOS-Verdieping](https://logius-standaarden.github.io/BOMOS-Verdieping)
  > Dit document valt onder de volgende licentie: Creative Commons Attribution 4.0 International Public License
  - *De bron bevestigt CC-BY-4.0 voor BOMOS-Verdieping. De claim stelt dat ook BOMOS-Fundament onder deze licentie valt, maar de bron bevat geen informatie over de licentie van het Fundament.*
- **PARTIALLY_SUPPORTED** (medium) — [https://raw.githubusercontent.com/logius-standaarden/BOMOS-Fundament/main/LICENSE](https://raw.githubusercontent.com/logius-standaarden/BOMOS-Fundament/main/LICENSE)
  > Attribution 4.0 International [...] Creative Commons Attribution 4.0 International Public License
  - *De bron is het LICENSE-bestand van de BOMOS-Fundament repository en bevestigt dat CC-BY-4.0 de licentie is voor dit document. De claim stelt dat zowel BOMOS-Fundament als BOMOS-Verdieping onder CC-BY-4.0 zijn gepubliceerd. De bron bevestigt alleen BOMOS-Fundament; over BOMOS-Verdieping staat niets in deze brontekst.*
- **PARTIALLY_SUPPORTED** (medium) — [https://raw.githubusercontent.com/logius-standaarden/BOMOS-Fundament/master/LICENSE](https://raw.githubusercontent.com/logius-standaarden/BOMOS-Fundament/master/LICENSE)
  > Attribution 4.0 International [...] Creative Commons Attribution 4.0 International Public License
  - *De brontekst is de volledige tekst van de CC-BY-4.0 licentie, afkomstig uit de LICENSE-file van de BOMOS-Fundament repository. Dit bevestigt dat BOMOS-Fundament onder CC-BY-4.0 is gepubliceerd. De claim stelt echter ook dat BOMOS-Verdieping onder dezelfde licentie valt, maar de bron bevat geen informatie over BOMOS-Verdieping — dat valt buiten het bereik van dit document.*

### `ls-bomos-0011` — SKILL.md:84 *(§ Beheermodel Template)*

> Een BOMOS-conform beheermodel bevat minimaal de secties: Strategie, Tactiek, Operationeel, Implementatieondersteuning, en Communicatie.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** BOMOS beheermodel template

- **SUPPORTED** (high) — [https://github.com/logius-standaarden/BOMOS-voorbeeld-beheermodel](https://github.com/logius-standaarden/BOMOS-voorbeeld-beheermodel)
  > ch02_Strategie.md ch03_Tactiek.md ch04_Operationeel.md ch05_Implementatieondersteuning.md ch06_Communicatie.md
  - *De repository bevat expliciet de bestanden ch02_Strategie.md, ch03_Tactiek.md, ch04_Operationeel.md, ch05_Implementatieondersteuning.md en ch06_Communicatie.md, wat direct overeenkomt met de vijf genoemde secties in de claim.*

### `ls-bomos-0013` — reference.md:7 *(§ Het BOMOS Activiteitenmodel)*

> Het BOMOS activiteitenmodel beschrijft vijf hoofdlagen: Strategie, Tactiek, Operationeel, Implementatieondersteuning, en Communicatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS activiteitenmodel

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > De structuur bestaat uit een aantal elementen: Drie hoofdlagen: strategie, tactiek en operationeel. Twee ondersteunende lagen: implementatieondersteuning en communicatie.
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Naast de lagen operationeel, tactisch en strategisch worden implementatie ondersteuning en communicatie besproken.
  - *De bron bevestigt de vijf hoofdlagen expliciet in de introductie en werkt ze uit in aparte hoofdstukken.*

### `ls-bomos-0018` — reference.md:48 *(§ Het BOMOS Activiteitenmodel)*

> Bij implementatieondersteuning is het cruciaal om een balans te vinden tussen activiteiten van de beheerorganisatie en die van commerciële partijen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** BOMOS implementatieondersteuning

- **PARTIALLY_SUPPORTED** (low) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Module-ontwikkeling en Certificatie zijn riskante activiteiten, waarmee er actief ingegrepen wordt in de markt. De uitvoering daarvan dient zorgvuldig te gebeuren en zoveel mogelijk buiten de eigen organisatie.
  - *De bron waarschuwt voor riskante ingrepen in de markt maar formuleert dit niet als een must-vereiste over een 'balans'. De strekking overlapt gedeeltelijk maar de claim is specifieker dan wat de bron zegt.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Met name omdat er een balans gevonden moet worden wat de beheer-organisatie invult, en wat overgelaten wordt aan consultancy door commerciële ondernemingen. Als beheerorganisatie is het ongewenst om te concurreren.
  - *De bron ondersteunt de claim volledig: het belang van een balans tussen de beheerorganisatie en commerciële partijen bij implementatieondersteuning wordt expliciet beschreven.*

### `ls-bomos-0020` — reference.md:52 *(§ Het BOMOS Activiteitenmodel)*

> Open source modules (referentie-implementaties) worden binnen BOMOS alleen ingezet bij geconstateerde implementatieproblemen.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** BOMOS implementatieondersteuning - Open source modules

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Module-ontwikkeling is dan ook een activiteit die zeer zorgvuldig aangepakt moet worden, en pas in het vizier moet komen als er een probleem rond implementaties is ontstaan.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  - *De bron beschrijft module-ontwikkeling en noemt dat de markt gestimuleerd kan worden, maar stelt niet dat open source modules alleen ingezet mogen worden bij geconstateerde implementatieproblemen.*

### `ls-bomos-0022` — reference.md:67 *(§ Rollen en Verantwoordelijkheden)*

> BOMOS definieert de rollen: Houder, Financier, Autorisator, Functioneel Beheerder, Technisch Beheerder, Distributeur, Expert, en Gebruiker.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS rollenmodel

- **PARTIALLY_SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Eigenaar [...] Financier [...] Autorisator [...] Functioneel beheerder [...] Technisch beheerder [...] Distributeur [...] Expert [...] Gebruiker
  - *De bron beschrijft exact deze rollen, maar gebruikt 'Eigenaar' waar de claim 'Houder' zegt. Dat is een terminologisch verschil dat de claim gedeeltelijk tegenspreekt.*
- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Rol BOMOS activiteit: Houder [...] Financier [...] Autorisator [...] Expert [...] Functioneel beheerder [...] Technisch beheerder [...] Distributeur [...] Gebruiker [...]

### `ls-bomos-0024` — reference.md:86 *(§ Levensfasen van een Standaard)*

> BOMOS onderscheidt vijf levensfasen voor een standaard: Creatie/Ontwikkeling, Introductie, Implementatie/Groei, Volwassenheid, en Uitfasering.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS levensfasen

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Figuur 3 Levensfases van een standaard 1. Creatie / ontwikkeling 2. Introductiefase van de standaard 3. Implementatie / groei van de standaard 4. Volwaardige toepassing / volwassenheid van de standaard 5. Uitfaseren / overgang naar een andere (versie van de) standaard
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron vermeldt nergens een onderverdeling in vijf levensfasen (Creatie/Ontwikkeling, Introductie, Implementatie/Groei, Volwassenheid, Uitfasering). Levenscyclus van standaarden wordt wel kort aangestipt maar de vijf genoemde fasen worden niet als zodanig benoemd.*

### `ls-bomos-0025` — reference.md:92 *(§ Levensfasen van een Standaard)*

> De beheerorganisatie moet de activiteiten uit het activiteitenmodel aanpassen aan de huidige levensfase van de standaard.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** BOMOS levensfasen

- **SUPPORTED** (medium) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > Het is dan ook als vuistregel verstandig om bij iedere overgang een controle (op basis van het Beheer- en Ontwikkelmodel) uit te voeren om te bepalen of uw beheerinrichting nog voldoet.
  - *De bron formuleert dit als 'vuistregel' (aanbeveling), niet als harde must-vereiste. De claim gebruikt MUST, wat strenger is dan wat de bron zegt.*
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron bespreekt levenscyclus van standaarden en beheeractiviteiten, maar bevat geen expliciete MUST-norm dat activiteiten aangepast moeten worden aan de huidige levensfase.*

### `ls-bomos-0026` — reference.md:96 *(§ Conformiteit)*

> Een beheerorganisatie werkt conform BOMOS wanneer een beheerdocument is gepubliceerd dat alle componenten uit het BOMOS Activiteitendiagram beschrijft.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** BOMOS conformiteit

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > De beheerorganisatie werkt conform BOMOS als er een beheerdocument is gepubliceerd waarin de invulling van alle onderdelen uit het BOMOS Activiteitendiagram (het Beheer- en Ontwikkelmodel) zijn beschreven.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron beschrijft wel wat een beheerdocument kan inhouden (o.a. Geonovum voorbeeld), maar bevat geen expliciete conformiteitseis dat een beheerorganisatie 'conform BOMOS werkt' wanneer een beheerdocument alle componenten beschrijft.*

### `ls-bomos-0028` — reference.md:107 *(§ Pressure Cooker Model)*

> Het BOMOS Pressure Cooker Model beschrijft een versneld ontwikkelproces met een totale doorlooptijd van circa 2 maanden van initiatie tot governance.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS Pressure Cooker Model

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Na een werkgroepweek, met gemiddeld 15 deelnemers van zowel de afvalverwerkers en de leveranciers, waarin de standaarden stuk voor stuk zijn doorlopen, volgt twee weken van uitwerking door een externe begeleider, en vervolgens een twee weken review periode door de werkgroep voordat de standaard is opgeleverd aan de stuurgroep. Geteld vanaf de start van de werkgroep ligt er dan binnen 2 maanden ...
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  - *Het 'Pressure Cooker Model' wordt niet beschreven in BOMOS-Fundament. Het wordt alleen kort in vogelvlucht aangestipt als onderdeel van Deel 2 (De Verdieping), zonder details over doorlooptijd.*

### `ls-bomos-0029` — reference.md:102 *(§ Pressure Cooker Model)*

> De intensieve workshop in het BOMOS Pressure Cooker Model duurt 1 week en heeft gemiddeld 15 deelnemers.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS Pressure Cooker Model

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > Na een werkgroepweek, met gemiddeld 15 deelnemers van zowel de afvalverwerkers en de leveranciers, waarin de standaarden stuk voor stuk zijn doorlopen
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  - *De bron noemt het concept van de 'pressure cooker' kort in de context van snellere standaardiseringmethoden, maar geeft geen details over duur (1 week) of gemiddeld aantal deelnemers (15).*

### `ls-bomos-0030` — reference.md:103 *(§ Pressure Cooker Model)*

> In het BOMOS Pressure Cooker Model volgen na de intensieve workshop een expert-verfijningsfase van 2 weken en een community review van 2 weken.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS Pressure Cooker Model

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  > volgt twee weken van uitwerking door een externe begeleider, en vervolgens een twee weken review periode door de werkgroep voordat de standaard is opgeleverd aan de stuurgroep.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  - *De bron noemt de pressure cooker methode maar beschrijft geen fasen, tijdlijnen of een expert-verfijningsfase en community review van elk 2 weken.*

### `ls-bomos-0032` — reference.md:113 *(§ Praktijkvoorbeelden)*

> Geonovum ontving in 2014 het predicaat 'uitstekend beheer' voor de manier waarop zij standaarden conform BOMOS beheren.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** BOMOS praktijkvoorbeelden - Geonovum

- **SUPPORTED** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/fundament](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament)
  > De geo-standaarden zijn opgenomen in de pas-toe-of-leg-uit-lijst van het Forum Standaardisatie, waarvoor wij in 2014 het predicaat uitstekend beheer ontvingen, mede omdat wij de geo-standaarden beheren conform BOMOS.
- **NOT_FOUND** (high) — [https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping)
  - *De bron vermeldt Geonovum meerdere keren als voorbeeld, maar bevat geen verwijzing naar een predicaat 'uitstekend beheer' in 2014.*

</details>
