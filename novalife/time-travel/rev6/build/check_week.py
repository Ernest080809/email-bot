"""Prüft eine Wochen-Datei des Docket Rev. 6.

Aufruf: python3 rev6/build/check_week.py 5      (prüft rev6/weeks/w5.json)
        python3 rev6/build/check_week.py index  (kompakte Übersicht aller Wochen)
"""
import datetime as dt
import json
import pathlib
import re
import sys

R6 = pathlib.Path(__file__).resolve().parents[1]
W1 = dt.date(2026, 9, 14)
CUTOVER = dt.date(2026, 10, 8)
CATS = {"B", "C", "D", "A", "S", "V", "N"}
LONG_DAYS = {"2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11", "2027-01-16", "2027-03-06",
             "2027-06-01", "2027-06-02", "2027-06-03", "2027-06-04", "2027-06-08", "2027-06-09",
             "2027-06-24", "2027-06-25", "2027-06-26", "2027-06-27"}
VKEYS = {"id", "slot", "dauer", "plattform", "hook_en", "hook_de", "shots", "ort", "ton", "text", "cta", "caption", "check"}
TKEYS = {"c", "t", "m", "plus", "s", "f", "p", "o", "v", "x"}
BANNED = [r"\bauthentisch", r"slawische[rn]? lebensbaum", r"\bvyshyvanka\b(?!-band)", r"projekt slavic"]


def dates(n):
    s = W1 + dt.timedelta(days=7 * (n - 1))
    return [(s + dt.timedelta(days=i)) for i in range(7) if s + dt.timedelta(days=i) >= CUTOVER]


def check(n):
    errs, warns = [], []
    f = R6 / "weeks" / f"w{n}.json"
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"FEHLER: {f} nicht lesbar: {e}")
        return 1
    if data.get("n") != n:
        errs.append(f"n ist {data.get('n')} statt {n}")
    if data.get("phase") not in {"P0", "P1", "P2", "P3", "P4", "P5"}:
        errs.append(f"phase {data.get('phase')!r}")
    if not data.get("goal"):
        errs.append("goal fehlt")
    days = data.get("days")
    if not isinstance(days, dict):
        errs.append("days muss ein Objekt {Datum: [Aufgaben]} sein")
        days = {}
    want = [d.isoformat() for d in dates(n)]
    for d in want:
        if d not in days:
            errs.append(f"Tag {d} fehlt")
    for d in days:
        if d not in want:
            errs.append(f"Tag {d} gehört nicht in W{n}")
    ntask = nvid = nlink = 0
    for d, tasks in days.items():
        if not isinstance(tasks, list):
            errs.append(f"{d}: keine Liste")
            continue
        core = plus = 0
        for i, t in enumerate(tasks):
            w = f"{d} #{i}"
            if not isinstance(t, dict):
                errs.append(f"{w}: kein Objekt")
                continue
            extra = set(t) - TKEYS
            if extra:
                errs.append(f"{w}: unbekannte Felder {sorted(extra)}")
            c = t.get("c")
            if c not in CATS:
                errs.append(f"{w}: Kategorie {c!r}")
                continue
            if not t.get("t"):
                errs.append(f"{w}: Titel fehlt")
            if c == "N":
                continue
            ntask += 1
            m = t.get("m")
            if not isinstance(m, int) or m <= 0:
                errs.append(f"{w}: Minuten {m!r} (ganze Zahl > 0)")
                m = 0
            if t.get("plus"):
                plus += m
            elif c != "S" and t.get("x") != "s":
                core += m
            s = t.get("s", [])
            if not isinstance(s, list) or not s:
                errs.append(f"{w}: Schritte fehlen")
            elif len(s) < 2 and m >= 20:
                warns.append(f"{w}: nur {len(s)} Schritt bei {m} Min.")
            if not t.get("f"):
                errs.append(f"{w}: „Fertig, wenn“ fehlt")
            for j, o in enumerate(t.get("o", []) or []):
                if not isinstance(o, dict) or not o.get("n"):
                    errs.append(f"{w}: o[{j}] ohne n")
                    continue
                nlink += 1
                u = o.get("u")
                if u and not re.match(r"^https?://[^\s]+\.[^\s]+", u):
                    errs.append(f"{w}: URL {u!r}")
            v = t.get("v")
            if v is not None:
                if not isinstance(v, dict):
                    errs.append(f"{w}: v kein Objekt")
                else:
                    nvid += 1
                    extra = set(v) - VKEYS
                    if extra:
                        errs.append(f"{w}: v unbekannte Felder {sorted(extra)}")
                    for k in ("hook_en", "shots", "ort", "caption"):
                        if not v.get(k):
                            errs.append(f"{w}: Video ohne {k}")
            text = json.dumps(t, ensure_ascii=False).lower()
            for b in BANNED:
                if re.search(b, text) and "nie „authentisch" not in text and "nicht „authentisch" not in text:
                    warns.append(f"{w}: Wort prüfen ({b})")
        if core > 120 and d not in LONG_DAYS:
            errs.append(f"{d}: Kern {core} Min. > 120")
        elif core > 150:
            warns.append(f"{d}: Kern {core} Min. (Ausnahmetag)")
    for e in errs:
        print("FEHLER:", e)
    for w_ in warns:
        print("Hinweis:", w_)
    print(f"W{n}: {ntask} Aufgaben, {nvid} Video-Briefings, {nlink} Orte/Links, {len(errs)} Fehler, {len(warns)} Hinweise")
    return 1 if errs else 0


def index():
    for f in sorted((R6 / "weeks").glob("w*.json"), key=lambda p: int(p.stem[1:])):
        data = json.loads(f.read_text(encoding="utf-8"))
        print(f"== W{data.get('n')} {data.get('phase')} · {data.get('goal')}")
        for d, tasks in data.get("days", {}).items():
            for t in tasks:
                vid = f" [{t['v'].get('id')}]" if isinstance(t.get("v"), dict) and t["v"].get("id") else ""
                pl = " +" if t.get("plus") else ""
                print(f"{d} {t.get('c')}{pl} {t.get('m', 0):>3} {t.get('t')}{vid}")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "index":
        index()
        sys.exit(0)
    sys.exit(check(int(arg)))
