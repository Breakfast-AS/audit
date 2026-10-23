#!/usr/bin/env python3
"""Samler alle clients/<slug>/<YYYY-MM>/metrics.json + rapporter til dashboard/data.json.

  python3 scripts/build_dashboard.py
"""
import datetime as dt, json, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = {"summary": "SUMMARY.md", "changes": "CHANGES.md", "report": "FULL-AUDIT-REPORT.md", "plan": "ACTION-PLAN.md"}


def main():
    clients = tomllib.loads((ROOT / "clients.toml").read_text())["client"]
    out = {"generated": dt.datetime.now().isoformat(timespec="minutes"), "clients": []}
    for c in clients:
        base = ROOT / "clients" / c["slug"]
        snaps = []
        for mf in sorted(base.glob("*/metrics.json")):
            m = json.loads(mf.read_text())
            snap = {k: m.get(k) for k in ("month", "date", "method", "note", "score", "categories",
                                          "kpis", "issues", "performance", "sampled", "schema_version")}
            if m.get("site"):
                s = m["site"]
                snap["site"] = {"security_headers": s["security_headers"], "robots": s["robots"],
                                "llms_txt": s["llms_txt"], "https_redirect": s["https_redirect"]}
            snap["reports"] = {k: (mf.parent / f).read_text() for k, f in REPORTS.items() if (mf.parent / f).exists()}
            snaps.append(snap)
        out["clients"].append({"slug": c["slug"], "name": c["name"], "url": c["url"], "snapshots": snaps})
    # data.js (ikke .json) slik at dashboardet også fungerer åpnet direkte fra disk (file://)
    p = ROOT / "dashboard" / "data.js"
    p.write_text("window.SEO_DATA = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
    print(f"{p.relative_to(ROOT)}: {len(out['clients'])} kunder, {p.stat().st_size // 1024} kB")


if __name__ == "__main__":
    main()
