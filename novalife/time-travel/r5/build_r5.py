# -*- coding: utf-8 -*-
# Baut weeks_r5.json aus r5_a..r5_d und prüft alles
import json, os, sys, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from r5_a import WEEKS_A
from r5_b import WEEKS_B
from r5_c import WEEKS_C
from r5_d import WEEKS_D
from r5_common import strip
from r5_c import SPIEL

START = dt.date(2026, 9, 14)
WEEKS = WEEKS_A + WEEKS_B + WEEKS_C + WEEKS_D
assert [w["n"] for w in WEEKS] == list(range(1, 33)), [w["n"] for w in WEEKS]

PHASE_OK = {**{n: "P0" for n in range(1, 5)}, **{n: "P1" for n in range(5, 9)}, **{n: "P2" for n in range(9, 15)},
            **{n: "P3" for n in range(15, 22)}, **{n: "P4" for n in range(22, 29)}, **{n: "P5" for n in range(29, 33)}}

out, problems = [], []
WT = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
total = 0; total_min = 0; heavy = []
for w in WEEKS:
    n = w["n"]
    if w["phase"] != PHASE_OK[n]:
        problems.append("W%d Phase %s statt %s" % (n, w["phase"], PHASE_OK[n]))
    if len(w["days"]) != 7:
        problems.append("W%d hat %d Tage" % (n, len(w["days"])))
    start = START + dt.timedelta(weeks=n - 1)
    days = []
    for di, d in enumerate(w["days"]):
        tasks = []
        for t in d:
            if t is None:
                problems.append("W%d %s: None-Eintrag" % (n, WT[di])); continue
            t = strip(t)
            if len(t) != 6 or t[0] not in "BCDASN" or not isinstance(t[2], int) or not isinstance(t[3], list):
                problems.append("W%d %s: kaputte Aufgabe %r" % (n, WT[di], t[:2]))
            if n >= 3 and t[0] != "N" and (t[2] <= 0 or not t[3] or not t[4]):
                problems.append("W%d %s: Aufgabe ohne Minuten/Schritte/Fertig: %s" % (n, WT[di], t[1]))
            flag = ""
            if t[0] == "S" and t[3] and t[3][0].startswith(SPIEL):
                t = list(t); t[3] = list(t[3]); t[3][0] = t[3][0][len(SPIEL):]; flag = "s"
            t = list(t) + [flag]
            tasks.append(t)
        mins = sum(t[2] for t in tasks if t[0] != "N")
        mins_ns = sum(t[2] for t in tasks if t[0] not in "NS")
        total += sum(1 for t in tasks if t[0] != "N")
        total_min += mins
        dd = start + dt.timedelta(days=di)
        if n >= 3 and (mins_ns > 150):
            heavy.append("W%d %s %s: %d Min. ohne Spiel (%d mit)" % (n, WT[di], dd.strftime("%d.%m."), mins_ns, mins))
        days.append(tasks)
    out.append({"n": n, "phase": w["phase"], "goal": w["goal"], "start": start.isoformat(), "days": days})

json.dump(out, open(os.path.join(HERE, "weeks_r5.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("Aufgaben:", total, "· Minuten gesamt:", total_min, "· Stunden:", round(total_min / 60, 1))
print("Probleme:", len(problems))
for p in problems: print("  ", p)
print("Schwere Tage (>150 Min. ohne Spiel):")
for h in heavy: print("  ", h)
# Wochenübersicht
for w in out:
    if w["n"] < 3: continue
    per = []
    for di, d in enumerate(w["days"]):
        m = sum(t[2] for t in d if t[0] not in "NS"); s = sum(t[2] for t in d if t[0] == "S")
        per.append("%s %3d%s" % (WT[di], m, ("+%d" % s) if s else ""))
    print("W%-2d %s | %s" % (w["n"], w["phase"], " ".join(per)))
print("Bytes JSON:", os.path.getsize(os.path.join(HERE, "weeks_r5.json")))
