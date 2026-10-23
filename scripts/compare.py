#!/usr/bin/env python3
"""Sammenligner en kundes måned med forrige måned og skriver clients/<slug>/<YYYY-MM>/CHANGES.md.

  python3 scripts/compare.py --client moss                # siste måned mot forrige
  python3 scripts/compare.py --client moss --month 2026-11
  python3 scripts/compare.py --all
"""
import argparse, json, sys, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT_LABELS = {"technical": "Teknisk", "content": "Innhold", "onpage": "On-page", "schema": "Schema",
              "performance": "Ytelse", "ai": "AI-søk", "images": "Bilder"}
# (nøkkel, etikett, True = høyere er bedre)
KPIS = [("pages_ok", "Sider (200)", None), ("thin_pages", "Tynne sider", False),
        ("median_unique_words", "Median unike ord", True), ("repeated_brand_titles", "Titler m/ gjentatt segment", False),
        ("duplicate_titles", "Dupliserte titler", False), ("missing_h1", "Mangler H1", False),
        ("missing_meta_description", "Mangler meta description", False), ("missing_og_image", "Mangler og:image", False),
        ("orphan_pages", "Sider uten interne lenker", False), ("event_pages_with_schema", "Arrangementer m/ Event-schema", True),
        ("security_headers_ok", "Sikkerhetsheadere OK", True), ("img_alt_coverage", "Alt-tekst-dekning", True),
        ("img_lazy_coverage", "Lazy-loading-dekning", True), ("perf_score", "Lighthouse ytelse", True),
        ("lcp_ms", "LCP (ms, verste nøkkelside)", False), ("cls", "CLS (verste nøkkelside)", False)]


def months(slug):
    d = ROOT / "clients" / slug
    return sorted(p.parent.name for p in d.glob("*/metrics.json"))


def load(slug, month):
    return json.loads((ROOT / "clients" / slug / month / "metrics.json").read_text())


def fmt(v):
    if v is None:
        return "–"
    if isinstance(v, bool):
        return "ja" if v else "nei"
    if isinstance(v, float) and v <= 1:
        return f"{v * 100:.0f} %"
    return f"{v:g}" if isinstance(v, float) else str(v)


def arrow(old, new, higher_better):
    if old is None or new is None or old == new or higher_better is None:
        return ""
    better = (new > old) == higher_better
    return " ✅" if better else " ⚠️"


def compare(slug, month=None):
    ms = months(slug)
    if not ms:
        return None
    month = month or ms[-1]
    prev = [m for m in ms if m < month]
    cur = load(slug, month)
    lines = [f"# Endringer — {slug} {month}", ""]
    if not prev:
        lines.append("Første måling, ingenting å sammenligne med.")
    else:
        old = load(slug, prev[-1])
        manual = old.get("method") == "manual"
        lines += [f"Sammenlignet med **{prev[-1]}**" + (" (manuell audit, skjønnsbasert score — tolk forsiktig)" if manual else ""), "",
                  "## Score", "", "| | Forrige | Nå | Endring |", "|---|---|---|---|",
                  f"| **Total** | {old['score']} | {cur['score']} | {cur['score'] - old['score']:+d} |"]
        for k, lbl in CAT_LABELS.items():
            o, n = old["categories"].get(k), cur["categories"].get(k)
            d = f"{n - o:+d}" if o is not None and n is not None else "–"
            lines.append(f"| {lbl} | {fmt(o)} | {fmt(n)} | {d} |")
        if not manual and old.get("schema_version") != cur.get("schema_version"):
            lines += ["", "> ⚠️ Scoreformelen er endret mellom målingene (schema_version). Sammenlign KPI-ene, ikke scoren."]
        ok, ck = old.get("kpis", {}), cur.get("kpis", {})
        if ok:
            lines += ["", "## Nøkkeltall", "", "| | Forrige | Nå |", "|---|---|---|"]
            for k, lbl, hb in KPIS:
                if k in ok or k in ck:
                    lines.append(f"| {lbl} | {fmt(ok.get(k))} | {fmt(ck.get(k))}{arrow(ok.get(k), ck.get(k), hb)} |")
            oi = {i["id"]: i for i in old.get("issues", [])}
            ci = {i["id"]: i for i in cur.get("issues", [])}
            resolved = [oi[k] for k in oi if k not in ci]
            new = [ci[k] for k in ci if k not in oi]
            changed = [(oi[k], ci[k]) for k in ci if k in oi and oi[k]["count"] != ci[k]["count"]]
            lines += ["", "## Problemer", ""]
            lines += [f"- ✅ **Løst:** {i['title']} (var {i['count']})" for i in resolved]
            lines += [f"- 🆕 **Nytt ({i['severity']}):** {i['title']} ({i['count']})" for i in new]
            lines += [f"- {'⬇️' if b['count'] < a['count'] else '⬆️'} {b['title']}: {a['count']} → {b['count']}" for a, b in changed]
            if not (resolved or new or changed):
                lines.append("Ingen endringer i problemlisten.")
    out = ROOT / "clients" / slug / month / "CHANGES.md"
    out.write_text("\n".join(lines) + "\n")
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--client")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--month")
    a = ap.parse_args()
    slugs = [a.client] if a.client else [c["slug"] for c in tomllib.loads((ROOT / "clients.toml").read_text())["client"]]
    for s in slugs:
        p = compare(s, a.month)
        print(p.relative_to(ROOT) if p else f"{s}: ingen målinger", file=sys.stderr)


if __name__ == "__main__":
    main()
