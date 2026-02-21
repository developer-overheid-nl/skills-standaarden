# Publicatie & Tooling - Achtergrondinfo

## Tech Radar

De [Tech Radar](https://logius-standaarden.github.io/tech-radar/) is een visualisatie van technologiekeuzes binnen het Logius standaardenportfolio.

| Ring | Betekenis |
|------|-----------|
| **Adopt** | Bewezen technologie, actief aanbevolen voor gebruik |
| **Trial** | Veelbelovend, wordt actief getest in projecten |
| **Assess** | Interessant, wordt onderzocht en geëvalueerd |
| **Hold** | Niet aanbevolen voor nieuw gebruik, wordt uitgefaseerd |

```bash
# Tech radar inhoud bekijken
gh api repos/logius-standaarden/tech-radar/contents --jq '.[].name'
```

## label-updates.yml - Automatische PR-status Labels

Beheert automatisch labels op Pull Requests op basis van hun status.

```bash
gh api repos/logius-standaarden/Automatisering/contents/.github/workflows/label-updates.yml \
  -H "Accept: application/vnd.github.raw"
```

## Check en Publish Workflow Voorbeelden

```yaml
# .github/workflows/check.yml
name: Check document
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  check:
    needs: build
    uses: logius-standaarden/Automatisering/.github/workflows/check.yml@main
```

```yaml
# .github/workflows/publish.yml
name: Publish document
on:
  push:
    branches: [main]

jobs:
  publish:
    needs: [build, check]
    uses: logius-standaarden/Automatisering/.github/workflows/publish.yml@main
    secrets: inherit
```

## Handige Commando's

```bash
# Alle workflows in Automatisering repo bekijken
gh api repos/logius-standaarden/Automatisering/contents/.github/workflows --jq '.[].name'

# ReSpec configuratie van het Logius template ophalen
gh api repos/logius-standaarden/ReSpec-template-Logius/contents/js/config.js \
  -H "Accept: application/vnd.github.raw"

# Publicatie repo structuur bekijken
gh api repos/logius-standaarden/publicatie/contents --jq '.[].name'

# Laatste wijzigingen aan Automatisering
gh api repos/logius-standaarden/Automatisering/commits \
  --jq '.[:5] | .[] | "\(.commit.committer.date) \(.commit.message | split("\n")[0])"'

# Welke repos gebruiken de centrale workflows
gh search code "logius-standaarden/Automatisering" --owner logius-standaarden --filename "*.yml"
```

## Gerelateerde Skills

| Skill | Relatie |
|-------|---------|
| `/ls-api` | API Design Rules documentatie gebruikt ReSpec en de centrale workflows |
| `/ls-dk` | Digikoppeling documentatie gebruikt ReSpec en de centrale workflows |
| `/ls-fsc` | FSC documentatie gebruikt ReSpec en de centrale workflows |
| `/ls-bomos` | BOMOS documentatie gebruikt ReSpec en de centrale workflows |
| `/ls` | Overzicht alle standaarden |
