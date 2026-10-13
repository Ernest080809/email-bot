"""Erzeugt rev6/kpi.json (Zielwerte und Gegenmaßnahmen je Sonntag) aus strategie.md 6, 7.1 und 7.2.

Aufruf: python3 rev6/build/kpi6.py
"""
import datetime as dt
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R6 = ROOT / "rev6"


def table(md, start):
    a = md.index(start)
    rows = []
    for line in md[a:].splitlines()[1:]:
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            rows.append(cells)
        elif rows:
            break
    return rows


def plain(s):
    return re.sub(r"\*\*|`", "", s).strip()


def num(s):
    m = re.search(r"\d[\d.]*", plain(s).replace("~", ""))
    return int(m.group(0).replace(".", "")) if m else None


def alarm(s):
    m = re.search(r"\((?:Alarm\s*<?\s*)?(\d[\d.]*)", plain(s))
    return int(m.group(1).replace(".", "")) if m else None


def first_date(s):
    m = re.search(r"(\d{1,2})\.(\d{1,2})\.", s)
    if not m:
        return None
    d, mo = int(m.group(1)), int(m.group(2))
    return dt.date(2026 if mo >= 9 else 2027, mo, d)


def main():
    md = (R6 / "strategie.md").read_text(encoding="utf-8")
    wk = table(md, "| W | KW-Sonntag |")
    gates72 = table(md, "| Datum | Gate | grün → | sonst → |")
    g71 = {r[0]: (plain(r[1]), plain(r[2])) for r in table(md, "| # | Wenn am Sonntag … | dann … |")}
    out = []
    for r in wk:
        n = int(r[0])
        if n < 5:
            continue
        sunday = dt.date(2026, 9, 14) + dt.timedelta(days=7 * (n - 1) + 6)
        monday = sunday - dt.timedelta(days=6)
        e = {"d": sunday.isoformat(), "w": n,
             "wl": num(r[2]), "wl_a": alarm(r[2]),
             "fo": num(r[4]),
             "zu": num(r[7]) if num(r[7]) is not None and "zählen" not in r[7] else None,
             "pre": num(r[6]) if num(r[6]) is not None else None, "pre_a": alarm(r[6])}
        if "Gate ≥" in r[7]:
            e["zu_a"] = int(re.search(r"Gate ≥ (\d+)", r[7]).group(1))
        if n == 32:
            e["pre"], e["pre_a"] = 72, 64
        gates, mass = [], []
        for g in gates72:
            d = first_date(g[0])
            if d and monday <= d <= sunday:
                gates.append(f"{plain(g[0])}: {plain(g[1])}")
                mass.append(f"{plain(g[0])} nicht erfüllt → {plain(g[3])}")
        mass.append(f"Warteliste unter Soll: {g71['G2'][1]}")
        mass.append(f"Warteliste unter Alarm: {g71['G1'][1]}")
        if n >= 18:
            mass.append(f"Vorbestellungen unter Alarm: {g71['G10'][1]}")
        e["gate"] = " · ".join(gates) if gates else "Sonntags-Check: Warteliste, Follower, Zusagen bzw. Vorbestellungen gegen das Soll, dazu Kassen-Ampel und Anmeldungen je 1.000 Views (Abschnitt Gates)."
        e["mass"] = mass
        out.append(e)
    (R6 / "kpi.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(out), "Sonntage ·", out[0]["d"], "bis", out[-1]["d"])
    for e in out[:3] + out[13:16] + out[-2:]:
        print(e["w"], e["d"], e["wl"], e["wl_a"], e["fo"], e["zu"], e["pre"], e["pre_a"], "|", e["gate"][:90])


if __name__ == "__main__":
    main()
