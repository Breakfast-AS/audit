# SEO-audit for kunder

Månedlig, automatisert SEO-oppfølging av kundene i `clients.toml`, med dashboard i `dashboard/`.
Alle rapporter skrives på norsk (bokmål).

## Struktur

```
clients.toml                       kundeliste (slug, navn, url, key_pages, event_patterns)
clients/<slug>/<YYYY-MM>/
  metrics.json                     harde tall + score (fra collect.py) – kilden til alt i dashboardet
  pages.json                       per-side-data fra crawlen
  CHANGES.md                       automatisk diff mot forrige måned (compare.py)
  SUMMARY.md                       kort månedsrapport (skrives av Claude)
  ACTION-PLAN.md                   oppdatert handlingsplan (skrives av Claude)
  FULL-AUDIT-REPORT.md             full audit (kvartalsvis eller ved behov)
scripts/collect.py                 crawl + Lighthouse/PSI → metrics.json
scripts/compare.py                 metrics forrige vs nå → CHANGES.md
scripts/build_dashboard.py         alle metrics + rapporter → dashboard/data.js
dashboard/                         statisk frontend (index.html, app.js, styles.css, data.js)
```

Måneder med `"method": "manual"` i metrics.json er gamle skjønnsbaserte audits fra før automatiseringen.
De vises i dashboardet, men scoren er ikke direkte sammenlignbar med automatiske måneder.

## Månedlig rutine

Kjøres av skyrutinen den 1. hver måned, eller manuelt med «kjør månedlig SEO-audit».

1. `python3 scripts/collect.py --all`
   PageSpeed/CrUX brukes når `GOOGLE_API_KEY` er satt, eller når `SEO_USE_PSI=1` (i skyen legges nøkkelen på som network secret for `www.googleapis.com`). Hvis en kunde feiler, fortsett med resten og nevn det i oppsummeringen.
2. `python3 scripts/compare.py --all`
3. For hver kunde: les `metrics.json`, `CHANGES.md` og forrige måneds `ACTION-PLAN.md`. Skriv deretter:
   - `SUMMARY.md` (maks ~40 linjer) med:
     - score og endring
     - hva som er løst
     - hva som er nytt eller verre
     - de 3 viktigste tiltakene nå
     Tallene skal komme fra metrics.json, og du skal ikke gjette.
   - `ACTION-PLAN.md`: oppdater forrige plan. Marker tiltak som ✅ løst, 🔄 delvis eller ❌ gjenstår ut fra tallene. Legg til nye funn. Prioriter etter Kritisk, Høy, Middels og Lav.
   - I januar, april, juli og oktober skal du i tillegg skrive en `FULL-AUDIT-REPORT.md` for hver kunde. Den bygger på metrics/pages.json og stikkprøver av sidene.
4. `python3 scripts/build_dashboard.py`
5. Commit med meldingen `SEO-audit YYYY-MM` og push til `main`.

## Regler

- Scoren regnes ut av fast formel i `collect.py` (`score_and_issues`). Endrer du formelen, skal du øke `SCHEMA_VERSION` og notere det i commit-meldingen.
- Ikke start subagenter for den månedlige rutinen. Gjør alt i én sesjon for å holde kostnaden nede.
- Kunden legges til i `clients.toml`. Første kjøring gir baseline.
- Dashboardet skal ikke ha noe byggesteg. Avhengigheter hentes fra CDN med låst versjon.

## Lokalt

```
python3 scripts/collect.py --client moss --no-perf   # rask test uten ytelse
python3 scripts/build_dashboard.py
open dashboard/index.html                            # eller: python3 -m http.server -d dashboard
```
