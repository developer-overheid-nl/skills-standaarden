# BOMOS - Bronconflicten

Geconstateerd: 2026-02-21

Dit document beschrijft bekende discrepanties tussen GitHub-repository tags en de gepubliceerde versies op [gitdocumentatie.logius.nl](https://gitdocumentatie.logius.nl). De **gepubliceerde versie op gitdocumentatie.logius.nl is leidend** voor DEF-versies.

## Discrepanties

| Repository | Gepubliceerde versie (DEF) | Laatste GitHub-tag | Discrepantie |
|-----------|---------------------------|-------------------|-------------|
| [BOMOS-Fundament](https://github.com/logius-standaarden/BOMOS-Fundament) | [v3.0.1](https://gitdocumentatie.logius.nl/publicatie/bomos/fundament/) | `0.2.1` | Volledig afwijkend versienummerschema |
| [BOMOS-Verdieping](https://github.com/logius-standaarden/BOMOS-Verdieping) | [v3.1.0](https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping/) | `0.2.1` | Volledig afwijkend versienummerschema |

### Details: Dubbel versienummerschema

Bij BOMOS is de discrepantie **fundamenteel anders** dan bij andere Logius-standaarden. Het gaat niet om een achterlopende tag, maar om **twee volledig verschillende versienummerschema's**:

- **Git-tags** (`0.2.1`, `0.2`, `0.1`): volgen het repo/tooling-versienummer. Dit nummert de technische revisies van de repository-structuur.
- **Documentversies** (`v3.0.1`, `v3.1.0`): volgen het documentversienummer zoals opgenomen in de ReSpec-configuratie van het document zelf. Dit is het versienummer dat op de voorpagina van het document staat.

De documentversie v3.0.1 resp. v3.1.0 is bevestigd via de ReSpec `localBiblio` configuratie in de repositories.

### Tags per repository

**BOMOS-Fundament:**
- Tags: `0.2.1`, `0.2`, `0.1`
- Geen GitHub Releases
- Documentversie (ReSpec): `3.0.1`

**BOMOS-Verdieping:**
- Tags: `0.2.1`, `0.2`, `0.1`
- Geen GitHub Releases
- Documentversie (ReSpec): `3.1.0`

## Keuze in SKILL.md

De skill gebruikt de documentversies (`v3.0.1` en `v3.1.0`) van gitdocumentatie.logius.nl, niet de Git-tags die een onafhankelijk versienummerschema voor de repo-structuur hanteren. Dit is een bijzonderheid van BOMOS. Als het versienummerschema wordt geharmoniseerd, moet dit conflict opnieuw worden beoordeeld.

## Licentie-status GitHub-repositories

Sommige repositories bevatten een W3C Software License (afkomstig van het ReSpec-template), terwijl de gepubliceerde standaarden CC-BY-4.0 vermelden via de ReSpec-configuratie. Andere repositories hebben geen expliciet `LICENSE`-bestand.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [BOMOS-Fundament](https://github.com/logius-standaarden/BOMOS-Fundament) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [BOMOS-Verdieping](https://github.com/logius-standaarden/BOMOS-Verdieping) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [BOMOS-Aanvullende-Modules](https://github.com/logius-standaarden/BOMOS-Aanvullende-Modules) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [BOMOS-LinkedData](https://github.com/logius-standaarden/BOMOS-LinkedData) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [BOMOS-OpenSource](https://github.com/logius-standaarden/BOMOS-OpenSource) | W3C Software License | CC0-1.0 (ReSpec) | Afwijkend |
| [BOMOS-Stelsels](https://github.com/logius-standaarden/BOMOS-Stelsels) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [BOMOS-Beheermodel](https://github.com/logius-standaarden/BOMOS-Beheermodel) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [BOMOS-voorbeeld-beheermodel](https://github.com/logius-standaarden/BOMOS-voorbeeld-beheermodel) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [BOMOS-Community](https://github.com/logius-standaarden/BOMOS-Community) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Logius-Beheermodel](https://github.com/logius-standaarden/Logius-Beheermodel) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |

### Aandachtspunt

De W3C Software License is afkomstig van het ReSpec-template en dekt de tooling-code. De gepubliceerde standaard-inhoud valt onder CC-BY-4.0 (vermeld in de ReSpec-configuratie). Voor repositories zonder LICENSE-bestand verdient het aanbeveling om expliciet een licentie toe te voegen, relevant voor artikel 15n Auteurswet (text and data mining exceptie).

## Referenties

- Publicatie BOMOS-Fundament: https://gitdocumentatie.logius.nl/publicatie/bomos/fundament/
- Publicatie BOMOS-Verdieping: https://gitdocumentatie.logius.nl/publicatie/bomos/verdieping/
- GitHub BOMOS-Fundament: https://github.com/logius-standaarden/BOMOS-Fundament
- GitHub BOMOS-Fundament tags: https://github.com/logius-standaarden/BOMOS-Fundament/tags
- GitHub BOMOS-Verdieping: https://github.com/logius-standaarden/BOMOS-Verdieping
- GitHub BOMOS-Verdieping tags: https://github.com/logius-standaarden/BOMOS-Verdieping/tags
