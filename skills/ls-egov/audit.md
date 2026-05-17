<!-- markdownlint-disable MD052 MD034 MD013 MD038 -->
# Audit ls-egov — 2026-05-17

> Automatisch gegenereerd door audit-tooling. Niet handmatig bewerken; wijzig SKILL.md / reference.md en regenereer.

## Samenvatting

| Status | Aantal | % |
|--------|--------|---|
| UNSUPPORTED_ASSERTION | 3 | 5% |
| CONTRADICTED | 0 | 0% |
| PARTIALLY_GROUNDED | 1 | 2% |
| UNGROUNDED | 1 | 2% |
| NO_SOURCE | 51 | 88% |
| UNVERIFIABLE | 0 | 0% |
| KNOWN_DISCREPANCY | 0 | 0% |
| GROUNDED | 2 | 3% |

*Geverifieerd met sonnet, 4 calls, $0.2186.*

## UNSUPPORTED_ASSERTION — stellige bewering zonder enige bronsteun (mogelijke hallucinatie) (3)

### `ls-egov-0023` — SKILL.md:107 *(§ Samenhang Standaarden)*

> Basisfactuur Rijk is gebaseerd op Peppol BIS Billing 3.0 en NLCIUS (NL-specifieke invulling EN 16931) en UBL-OHNL.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisfactuur Rijk - samenhang standaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis](https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis)
  - *De bron beschrijft Peppol BIS algemeen en noemt NLCIUS als gerelateerde standaard, maar geeft geen informatie over 'Basisfactuur Rijk' of de specifieke technische grondslag daarvan (Peppol BIS Billing 3.0, NLCIUS, UBL-OHNL).*

### `ls-egov-0024` — SKILL.md:111 *(§ Samenhang Standaarden)*

> Basisorder Rijk is gebaseerd op Peppol BIS Order 3.0 en UBL 2.1 Order.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisorder Rijk - samenhang standaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis](https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis)
  - *De bron bevat geen informatie over 'Basisorder Rijk' of de grondslag daarvan (Peppol BIS Order 3.0, UBL 2.1 Order).*

### `ls-egov-0027` — SKILL.md:115 *(§ Samenhang Standaarden)*

> De overige e-government standaarden (Digimelding, Terugmelding, e-procurement) staan niet op de lijst van Forum Standaardisatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Forum Standaardisatie - e-government standaarden

- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis](https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis)
  - *De bron behandelt uitsluitend Peppol BIS en geeft geen informatie over de lijststatus van Digimelding, Terugmelding of andere e-government standaarden.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/nlcius](https://www.forumstandaardisatie.nl/open-standaarden/nlcius)
  - *De bron gaat uitsluitend over NLCIUS. Digimelding, Terugmelding en e-procurement worden niet besproken.*

## PARTIALLY_GROUNDED — bron ondersteunt deel van de claim (1)

### `ls-egov-0040` — SKILL.md:266 *(§ Foutafhandeling)*

> De huidige operationele interface voor terugmelden is SOAP/WUS, beschreven in de Digimelding-Koppelvlakspecificatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding koppelvlak

- **PARTIALLY_SUPPORTED** (low) — [https://github.com/logius-standaarden/Digimelding-Koppelvlakspecificatie](https://github.com/logius-standaarden/Digimelding-Koppelvlakspecificatie)
  > Digimelding Koppelvlakspecificatie gepubliceerde versie: https://gitdocumentatie.logius.nl/publicatie/digimelding/koppelvlak/
  - *De brontekst is uitsluitend de GitHub-repositorypagina (README/navigatie). Deze bevestigt dat er een Digimelding-Koppelvlakspecificatie bestaat en gepubliceerd is, maar de aangeleverde tekst bevat geen inhoudelijke informatie over het gebruikte protocol (SOAP/WUS). Het bestaan van de spec wordt ondersteund; de claim dat SOAP/WUS de operationele interface is, kan op basis van deze brontekst niet worden bevestigd of ontkend.*

## UNGROUNDED — geen bron ondersteunt de claim (1)

### `ls-egov-0028` — SKILL.md:232 *(§ Foutafhandeling)*

> De Terugmelden-API gebruikt application/problem+json conform RFC 9457 voor foutresponses.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Terugmelden-API foutafhandeling

- **OUT_OF_SCOPE** (high) — [https://www.rfc-editor.org/rfc/rfc9457.txt](https://www.rfc-editor.org/rfc/rfc9457.txt)
  - *De bron is RFC 9457, die het algemene 'problem details' formaat definieert. De bron bevat geen informatie over de Terugmelden-API. De claim gaat over een specifieke Nederlandse overheids-API die RFC 9457 zou moeten gebruiken — dat valt buiten het bereik van deze specificatie.*

## NO_SOURCE — geen kandidaat-bron gevonden (51)

### `ls-egov-0001` — SKILL.md:34 *(§ Versiemodel)*

> De E-Government standaarden hebben momenteel alleen werkversies. Er zijn nog geen vastgestelde versies gepubliceerd.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** E-Government standaarden (Logius) versiemodel


### `ls-egov-0002` — SKILL.md:31 *(§ Versiemodel)*

> Vastgestelde versies (DEF) zijn officieel goedgekeurd en gepubliceerd op gitdocumentatie.logius.nl.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius standaarden publicatiekanalen


### `ls-egov-0003` — SKILL.md:32 *(§ Versiemodel)*

> Werkversies (draft) zijn werk-in-uitvoering en gepubliceerd op logius-standaarden.github.io.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Logius standaarden publicatiekanalen


### `ls-egov-0004` — SKILL.md:51 *(§ Terugmelden-API (in ontwikkeling))*

> De Terugmelden-API is een beoogde REST API voor het indienen en opvragen van terugmeldingen. De repository bevat nog geen uitgewerkte specificatie; de API is in conceptfase.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Terugmelden-API (in ontwikkeling)


### `ls-egov-0005` — SKILL.md:51 *(§ Terugmelden-API (in ontwikkeling))*

> De bestaande koppelvlakspecificatie voor terugmelden is de Digimelding-Koppelvlakspecificatie (SOAP/WUS).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding koppelvlak


### `ls-egov-0006` — SKILL.md:59 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> De Basisfactuur Rijk definieert de minimum data-eisen waaraan facturen aan de Rijksoverheid moeten voldoen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisfactuur Rijk


### `ls-egov-0007` — SKILL.md:59 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Facturen aan de Rijksoverheid die verplichte velden missen worden automatisch afgewezen.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk


### `ls-egov-0008` — SKILL.md:62 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet een uniek factuurnummer bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Factuuridentificatie


### `ls-egov-0009` — SKILL.md:63 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet een factuurdatum bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Factuuridentificatie


### `ls-egov-0010` — SKILL.md:64 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet een factuurtypeaanduiding (factuur, creditnota, etc.) bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Factuuridentificatie


### `ls-egov-0011` — SKILL.md:65 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet een valutacode bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Factuuridentificatie


### `ls-egov-0012` — SKILL.md:69 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet naam en adresgegevens van de leverancier bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Leverancieridentificatie


### `ls-egov-0013` — SKILL.md:70 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet een KvK-nummer of vergelijkbaar identificatienummer van de leverancier bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Leverancieridentificatie


### `ls-egov-0014` — SKILL.md:71 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet een BTW-identificatienummer van de leverancier bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Leverancieridentificatie


### `ls-egov-0015` — SKILL.md:72 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet bankgegevens van de leverancier (IBAN en eventueel BIC) bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Leverancieridentificatie


### `ls-egov-0016` — SKILL.md:75 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet het OIN (Overheids Identificatie Nummer) of vergelijkbaar van de ontvangende overheidsorganisatie bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Ontvanger


### `ls-egov-0017` — SKILL.md:79 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet per regelitem een omschrijving van het geleverde product of de dienst bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Regelitems


### `ls-egov-0018` — SKILL.md:80 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet per regelitem hoeveelheid en eenheid, prijs per eenheid, totaalbedrag, BTW-percentage en BTW-bedrag bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Regelitems


### `ls-egov-0019` — SKILL.md:86 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk moet een ordernummer (inkoopordernummer van de overheidsorganisatie) bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Order- en referentie-informatie


### `ls-egov-0020` — SKILL.md:96 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Een Basisfactuur Rijk mag maximaal 9 bijlagen bevatten.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Basisfactuur Rijk - Bijlagen


### `ls-egov-0021` — SKILL.md:97 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> De totale grootte van alle bijlagen bij een Basisfactuur Rijk mag niet groter zijn dan 20 MB.

**Type:** normative_requirement  ·  **Modaliteit:** MUST_NOT  ·  **Scope:** Basisfactuur Rijk - Bijlagen


### `ls-egov-0022` — SKILL.md:98 *(§ Basisfactuur Rijk: Verplichte Elementen)*

> Bijlagen bij de Basisfactuur Rijk moeten voldoen aan ondersteunde formaten conform Peppol-specificaties (PDF, afbeeldingen, etc.).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - Bijlagen


### `ls-egov-0029` — SKILL.md:246 *(§ Foutafhandeling)*

> HTTP 201 geeft aan dat een terugmelding succesvol is aangemaakt.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Terugmelden-API HTTP statuscodes


### `ls-egov-0030` — SKILL.md:247 *(§ Foutafhandeling)*

> HTTP 400 bij de Terugmelden-API betekent dat een verplicht veld ontbreekt of een ongeldige waarde is meegegeven.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Terugmelden-API HTTP statuscodes


### `ls-egov-0031` — SKILL.md:248 *(§ Foutafhandeling)*

> HTTP 401 bij de Terugmelden-API betekent dat authenticatie vereist is.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Terugmelden-API HTTP statuscodes


### `ls-egov-0032` — SKILL.md:249 *(§ Foutafhandeling)*

> HTTP 403 bij de Terugmelden-API betekent dat het OIN niet geautoriseerd is voor de betreffende registratie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Terugmelden-API HTTP statuscodes


### `ls-egov-0033` — SKILL.md:251 *(§ Foutafhandeling)*

> HTTP 422 bij de Terugmelden-API betekent een validatiefout (bijv. ongeldig BSN-formaat).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Terugmelden-API HTTP statuscodes


### `ls-egov-0034` — SKILL.md:256 *(§ Foutafhandeling)*

> Facturen worden automatisch afgewezen wanneer het ordernummer ontbreekt of onjuist is.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - afwijzingsredenen


### `ls-egov-0035` — SKILL.md:257 *(§ Foutafhandeling)*

> Facturen worden automatisch afgewezen wanneer een verplicht veld ontbreekt (KvK-nummer, BTW-ID, IBAN, of factuurdatum).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - afwijzingsredenen


### `ls-egov-0036` — SKILL.md:258 *(§ Foutafhandeling)*

> Facturen worden automatisch afgewezen wanneer de BTW-berekening inconsistent is (regeltotalen kloppen niet met factuurtotaal).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - afwijzingsredenen


### `ls-egov-0037` — SKILL.md:259 *(§ Foutafhandeling)*

> Facturen worden automatisch afgewezen wanneer bijlagen te groot zijn (maximaal 9 bijlagen, totaal max 20 MB).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - afwijzingsredenen


### `ls-egov-0038` — SKILL.md:260 *(§ Foutafhandeling)*

> Facturen worden automatisch afgewezen wanneer het UBL-formaat ongeldig is (XML voldoet niet aan NLCIUS-validatieschema).

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - afwijzingsredenen


### `ls-egov-0039` — SKILL.md:262 *(§ Foutafhandeling)*

> Bij afwijzing van een factuur ontvangt de leverancier een e-mail met de specifieke ontbrekende velden.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisfactuur Rijk - afwijzingsproces


### `ls-egov-0041` — SKILL.md:275 *(§ Foutafhandeling)*

> Het repo basisfactuur-rijk bevat een Schematron bestand met validatieregels en voorbeeld-XML's.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisfactuur Rijk - validatie


### `ls-egov-0042` — reference.md:11 *(§ Terugmelding & Digimelding)*

> Terugmelding is een melding dat gegevens in een basisregistratie mogelijk onjuist zijn. Burgers, bedrijven en overheidsorganisaties kunnen een terugmelding indienen.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Terugmelding - begrip


### `ls-egov-0043` — reference.md:23 *(§ Terugmelding & Digimelding)*

> Digimelding is de centrale voorziening waarmee terugmeldingen op basisregistraties worden ingediend en afgehandeld, en fungeert als koppelpunt tussen melder en bronhouder.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding - begrip


### `ls-egov-0044` — reference.md:29 *(§ Technische Architectuur: Annotatie-framework)*

> De berichtenarchitectuur van Digimelding is gebaseerd op een annotatie-framework dat terugmeldingen structureert als hiërarchische annotaties.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding - technische architectuur


### `ls-egov-0045` — reference.md:41 *(§ Technische Architectuur: Annotatie-framework)*

> Een root-annotatie is de initiële terugmelding aangemaakt door de melder en bevat het gegeven, de registratie en de motivatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding annotatie-framework


### `ls-egov-0046` — reference.md:42 *(§ Technische Architectuur: Annotatie-framework)*

> Leaf-annotaties zijn vervolgberichten die aan de root-annotatie worden gehangen en refereren terug naar het UUID van de root-annotatie.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding annotatie-framework


### `ls-egov-0047` — reference.md:43 *(§ Technische Architectuur: Annotatie-framework)*

> Elke annotatie (root of leaf) bevat een annotatiebasis met metadata zoals tijdstip, auteur, en berichttype.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Digimelding annotatie-framework


### `ls-egov-0048` — reference.md:63 *(§ Best Practices voor Leveranciers)*

> Voor basisfacturen aan de Rijksoverheid moet altijd het juiste inkoopordernummer worden gebruikt; een fout ordernummer leidt tot afwijzing.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - best practices leveranciers


### `ls-egov-0049` — reference.md:65 *(§ Best Practices voor Leveranciers)*

> Leveranciers dienen facturen aan de Rijksoverheid te leveren in UBL 2.1 XML-formaat voor optimale automatische verwerking.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Basisfactuur Rijk - best practices leveranciers


### `ls-egov-0050` — reference.md:66 *(§ Best Practices voor Leveranciers)*

> Leveranciers dienen de factuur te valideren tegen het NLCIUS-validatieschema voordat deze wordt ingediend.

**Type:** normative_requirement  ·  **Modaliteit:** SHOULD  ·  **Scope:** Basisfactuur Rijk - best practices leveranciers


### `ls-egov-0051` — reference.md:67 *(§ Best Practices voor Leveranciers)*

> BTW-bedragen op een Basisfactuur moeten consistent zijn op regel- en factuurniveau.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** Basisfactuur Rijk - best practices leveranciers


### `ls-egov-0052` — reference.md:77 *(§ Basisorder Rijk)*

> De Basisorder Rijk is gebaseerd op UBL 2.1 Order-berichttype en sluit aan op Peppol-orderberichten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Basisorder Rijk


### `ls-egov-0053` — reference.md:90 *(§ E-Procurement)*

> Elektronisch factureren (e-invoicing) is verplicht voor leveranciers aan de Rijksoverheid conform EU-richtlijn 2014/55/EU.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** E-Procurement - elektronisch factureren


### `ls-egov-0054` — reference.md:93 *(§ E-Procurement)*

> E-Procurement vereist naleving van de Europese norm EN 16931 voor elektronische facturering.

**Type:** normative_requirement  ·  **Modaliteit:** MUST  ·  **Scope:** E-Procurement - compliance


### `ls-egov-0055` — reference.md:97 *(§ E-Procurement)*

> De Basisfactuur Rijk dekt circa 90% van alle overheidsfacturen (standaard inkoop- en dienstverleningsfacturen).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** E-Procurement - bereik


### `ls-egov-0056` — reference.md:98 *(§ E-Procurement)*

> De resterende 10% van overheidsfacturen betreft uitzonderingsgevallen zoals creditnota's met afwijkende structuren of specifieke sectorvereisten.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** E-Procurement - bereik


### `ls-egov-0057` — reference.md:105 *(§ E-Procurement)*

> NLCIUS is de Nederlandse invulling (Core Invoice Usage Specification) van de Europese norm EN 16931.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** E-Procurement - ondersteunde standaarden


### `ls-egov-0058` — reference.md:104 *(§ E-Procurement)*

> Peppol BIS 3 is een Europese factuurstandaard via het Peppol-netwerk.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** E-Procurement - ondersteunde standaarden


## GROUNDED — minstens één bron ondersteunt de claim (2)

<details>
<summary>Klap uit voor alle GROUNDED claims</summary>

### `ls-egov-0025` — SKILL.md:115 *(§ Samenhang Standaarden)*

> NLCIUS heeft bij Forum Standaardisatie de status 'verplicht' (pas-toe-of-leg-uit).

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Forum Standaardisatie - NLCIUS

- **SUPPORTED** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/nlcius](https://www.forumstandaardisatie.nl/open-standaarden/nlcius)
  > Verplicht ('Pas toe leg uit')
  - *De status van NLCIUS wordt expliciet als 'Verplicht (Pas toe of leg uit)' vermeld op de pagina.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis](https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis)
  - *De bron gaat over Peppol BIS, niet over NLCIUS. De status van NLCIUS bij Forum Standaardisatie wordt niet behandeld.*

### `ls-egov-0026` — SKILL.md:115 *(§ Samenhang Standaarden)*

> Peppol BIS heeft bij Forum Standaardisatie de status 'aanbevolen', niet verplicht.

**Type:** factual_assertion  ·  **Modaliteit:** STATEMENT  ·  **Scope:** Forum Standaardisatie - Peppol BIS

- **SUPPORTED** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis](https://www.forumstandaardisatie.nl/open-standaarden/peppol-bis)
  > Aanbevolen [...] 'Aanbevolen' betekent dat dit een gangbare of opkomende standaard is waarvan het Forum Standaardisatie het gebruik aanbeveelt.
  - *De bron toont expliciet de status 'Aanbevolen' voor Peppol BIS, niet 'Verplicht (Pas toe of leg uit)'.*
- **NOT_FOUND** (high) — [https://www.forumstandaardisatie.nl/open-standaarden/nlcius](https://www.forumstandaardisatie.nl/open-standaarden/nlcius)
  - *De bron vermeldt Peppol BIS alleen als een gerelateerde standaard ('Relatie met andere standaarden Peppol BIS'), maar geeft geen informatie over de lijststatus van Peppol BIS bij Forum Standaardisatie.*

</details>
