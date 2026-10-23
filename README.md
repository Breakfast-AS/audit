# audit

Månedlig SEO-audit for Breakfast-kunder, med dashboard.

- **Dashboard:** `dashboard/` (statisk, hostes på Vercel)
- **Kunder:** `clients.toml`
- **Rutine og struktur:** se [`CLAUDE.md`](CLAUDE.md)

```
python3 scripts/collect.py --all        # måling (sett GOOGLE_API_KEY for PageSpeed/CrUX)
python3 scripts/compare.py --all        # diff mot forrige måned
python3 scripts/build_dashboard.py      # oppdater dashboard/data.js
```
