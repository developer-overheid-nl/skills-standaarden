---
name: ls-bomos
description: "Gebruik deze skill wanneer de gebruiker vraagt over 'BOMOS', 'Beheer- en Ontwikkelmodel', 'open standaarden beheer', 'standaardisatie governance', 'beheermodel', 'community management standaarden', 'open source governance', 'stelselstandaarden', 'RFC proces', 'wijzigingsproces standaard', 'change management standaarden'."
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - Bash(gh issue list *)
  - Bash(gh pr list *)
  - Bash(gh search *)
  - Bash(curl -s *)
  - WebFetch(*)
---

# BOMOS - Beheer- en Ontwikkelmodel voor Open Standaarden

**Agent-instructie:** Deze skill helpt bij het opzetten en beoordelen van beheermodellen voor open standaarden conform BOMOS. Gebruik het template en de checklist om een beheermodel op te stellen. Gebruik gh commando's om actuele content op te halen uit de BOMOS repos.

## Versiemodel

Net als andere Logius-standaarden kent BOMOS twee publicatiekanalen:

- **Vastgestelde versie (DEF)**: officieel goedgekeurd, gepubliceerd op `gitdocumentatie.logius.nl`
- **Werkversie (draft)**: werk-in-uitvoering, gepubliceerd op `logius-standaarden.github.io`

BOMOS is geen interoperabiliteitsstandaard en staat niet op de 'pas-toe-of-leg-uit'-lijst van het Forum Standaardisatie. Het is een raamwerk voor het beheren van open standaarden.

## Repositories

### Kerndocumenten (met vastgestelde versies)

| Repository | Beschrijving | Vastgesteld | Draft |
|-----------|-------------|------------|-------|
| [BOMOS-Fundament](https://github.com/logius-standaarden/BOMOS-Fundament) | Kernmodel: activiteiten, rollen, structuur | [v3.0.1](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament/) | [Draft](https://logius-standaarden.github.io/BOMOS-Fundament/) |
| [BOMOS-Verdieping](https://github.com/logius-standaarden/BOMOS-Verdieping) | Verdiepende beschrijving van BOMOS activiteiten | [v3.1.0](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping/) | [Draft](https://logius-standaarden.github.io/BOMOS-Verdieping/) |

### Aanvullende modules en documenten (alleen werkversies)

| Repository | Beschrijving | Publicatie |
|-----------|-------------|-----------|
| [BOMOS-Aanvullende-Modules](https://github.com/logius-standaarden/BOMOS-Aanvullende-Modules) | Aanvullende modules voor specifieke aspecten — **gearchiveerd** | - |
| [BOMOS-LinkedData](https://github.com/logius-standaarden/BOMOS-LinkedData) | Module: beheer van Linked Data standaarden | [Draft](https://logius-standaarden.github.io/BOMOS-LinkedData/) |
| [BOMOS-OpenSource](https://github.com/logius-standaarden/BOMOS-OpenSource) | Module: open source governance — **gearchiveerd** | [Draft (bevroren)](https://logius-standaarden.github.io/BOMOS-OpenSource/) |
| [BOMOS-Stelsels](https://github.com/logius-standaarden/BOMOS-Stelsels) | Module: beheer van stelsels van standaarden | [Draft](https://logius-standaarden.github.io/BOMOS-Stelsels/) |
| [BOMOS-Beheermodel](https://github.com/logius-standaarden/BOMOS-Beheermodel) | Beheermodel voor BOMOS zelf | [Draft](https://logius-standaarden.github.io/BOMOS-Beheermodel/) |
| [BOMOS-voorbeeld-beheermodel](https://github.com/logius-standaarden/BOMOS-voorbeeld-beheermodel) | Voorbeelddocument voor een beheermodel | [Draft](https://logius-standaarden.github.io/BOMOS-voorbeeld-beheermodel/) |
| [BOMOS-Community](https://github.com/logius-standaarden/BOMOS-Community) | Community-aspecten van standaardenbeheer | [Draft](https://logius-standaarden.github.io/BOMOS-Community/) |
| [Logius-Beheermodel](https://github.com/logius-standaarden/Logius-Beheermodel) | Overkoepelend beheermodel van Logius | [Draft](https://logius-standaarden.github.io/Logius-Beheermodel/) |

## Wijzigingsbeheer Workflow

De RFC-procedure (Request for Change) is het kernproces voor wijzigingsbeheer. Gebruik GitHub issues om wijzigingsverzoeken in te dienen en te volgen.

```bash
# Open RFC's bekijken
gh issue list --repo logius-standaarden/[STANDAARD] --label RFC

# Nieuwe RFC indienen
gh issue create --repo logius-standaarden/[STANDAARD] \
  --title "RFC: [korte omschrijving]" \
  --label RFC \
  --body "## Probleem\n[beschrijving]\n\n## Voorstel\n[oplossing]\n\n## Impact\n[gevolgen voor implementaties]"

# RFC status opvragen
gh issue view [NUMMER] --repo logius-standaarden/[STANDAARD]

# RFC's op prioriteit sorteren
gh issue list --repo logius-standaarden/[STANDAARD] --label RFC --json number,title,labels,updatedAt

# Zoeken naar goedgekeurde RFC's
gh issue list --repo logius-standaarden/[STANDAARD] --label RFC --label accepted --state closed
```

**Proces:** RFC indienen → Community review → Expert beoordeling → Autorisator besluit → Implementatie → Publicatie nieuwe versie

## Beheermodel Template

Een BOMOS-conform beheermodel bevat minimaal de volgende secties. Gebruik het [BOMOS-voorbeeld-beheermodel](https://github.com/logius-standaarden/BOMOS-voorbeeld-beheermodel) als startpunt.

### Document Structuur

```markdown
# Beheermodel [Naam Standaard]

## 1. Strategie
### 1.1 Governance
- Besluitvormingsstructuur (wie beslist over wijzigingen?)
- Samenstelling gremia (technisch overleg, stuurgroep)
- Vergaderfrequentie en besluitvormingsprocedure

### 1.2 Visie
- Doelgroep en toepassingsgebied
- Langetermijnvisie (3-5 jaar)
- Gewenste marktpositie en adoptiegraad

### 1.3 Financiering
- Begrotingsmodel en financieringsbronnen
- Kostenverantwoording

## 2. Tactiek
### 2.1 Architectuur
- Technische en functionele keuzes
- Samenhang met andere standaarden

### 2.2 Specificatiebeheer
- Versiebeheer (semantic versioning)
- Onderhoud van specificatiedocumenten

### 2.3 Wijzigingsbeheer
- RFC-procedure (Request for Change)
- Indienen, beoordelen en doorvoeren van wijzigingen
- GitHub issue workflow

### 2.4 Adoptiestrategie
- Forum Standaardisatie "pas-toe-of-leg-uit"
- Promotie en outreach

### 2.5 Kwaliteitsbeleid
- Kwaliteitscriteria voor de standaard
- Review- en testprocessen

### 2.6 Rechtenmanagement
- Licentiemodel (bijv. CC0, CC-BY)
- Intellectueel eigendom

## 3. Operationeel
### 3.1 Ontwikkelproces
- GitHub-based workflow
- Branch strategie en PR-reviews

### 3.2 Documentatie
- ReSpec publicatie
- Release notes bij elke versie

## 4. Implementatieondersteuning
### 4.1 Helpdesk
- Contactkanalen (GitHub issues, email)
- Responstijden

### 4.2 Referentie-implementaties
- Beschikbare tooling en voorbeelden

### 4.3 Validatie
- Beschikbare testtools en linters

## 5. Communicatie
### 5.1 Publicatie
- Website en GitHub Pages
- Verspreiding via Forum Standaardisatie

### 5.2 Community
- Werkgroepen en bijeenkomsten
- Bijdragerichtlijnen
```

### BOMOS Conformiteit Checklist

- [ ] **Governance** - Besluitvormingsstructuur beschreven
- [ ] **Visie** - Doelgroep en toepassingsgebied vastgelegd
- [ ] **Financiering** - Begrotingsmodel aanwezig
- [ ] **Architectuur** - Technische keuzes en samenhang beschreven
- [ ] **Specificatiebeheer** - Versiebeleid vastgelegd
- [ ] **Wijzigingsbeheer** - RFC-procedure beschreven
- [ ] **Adoptiestrategie** - Plan voor adoptiebevordering
- [ ] **Kwaliteitsbeleid** - Criteria en reviewproces beschreven
- [ ] **Rechtenmanagement** - Licentie en IP-beleid vastgelegd
- [ ] **Ontwikkelproces** - Werkwijze beschreven
- [ ] **Documentatie** - Publicatie- en versieproces vastgelegd
- [ ] **Helpdesk** - Contactkanalen en responstijden
- [ ] **Referentie-implementaties** - Beschikbare tooling beschreven
- [ ] **Validatie** - Testtools en conformiteitstests
- [ ] **Publicatie** - Distributiekanalen beschreven
- [ ] **Community** - Participatiemodel beschreven

Een organisatie werkt conform BOMOS wanneer voor **elke** activiteit een bewuste beschrijving is opgenomen, ook als die beschrijving is: "deze activiteit vullen wij (nog) niet in."

## Achtergrondinfo

Zie [reference.md](reference.md) voor het activiteitenmodel, rollen, levensfasen, pressure cooker model, en praktijkvoorbeelden. Zie [conflicts.md](conflicts.md) voor bekende discrepanties tussen GitHub-tags en gepubliceerde versies.
