"""Verschiebt den Docket auf Drop Do 24.06.2027: Aufholwochen W19/W22, Abi-Pause W28–W34.

Aufruf aus novalife/time-travel:  python3 -I warp.py rev6
"""
import copy
import datetime as dt
import json
import pathlib
import re
import sys

R6 = pathlib.Path(sys.argv[1])
W1 = dt.date(2026, 9, 14)
MAP = {**{n: n for n in range(5, 19)}, 19: 20, 20: 21, 21: 23, 22: 24, 23: 25, 24: 26, 25: 27, **{n: n + 9 for n in range(26, 33)}}
CATCH, PAUSE, NEWMAX = [19, 22], list(range(28, 35)), 41
OLD_END = dt.date(2027, 4, 25)
FIXED = {dt.date(2027, 2, 24)}  # Jahrestag, kalenderfest
DAY0 = dt.date(2026, 10, 11)
WD = "Mo Di Mi Do Fr Sa So".split()


def wstart(n):
    return W1 + dt.timedelta(days=7 * (n - 1))


def oldweek(d):
    return (d - W1).days // 7 + 1


def remap(d):
    if d in FIXED:
        return d
    if d == dt.date(2027, 4, 30):
        return dt.date(2027, 6, 30)
    if d < wstart(19):
        return d
    if d <= OLD_END:
        m = oldweek(d)
        return d + dt.timedelta(days=7 * (MAP[m] - m))
    if d <= dt.date(2027, 6, 30):
        return d + dt.timedelta(days=63)
    return d


SPECIAL = [
    ("mit Ostern (26.–29.03.)", "neben den mündlichen Prüfungen"),
    ("geplant Anfang April", "geplant Anfang Juni"), ("planned early April", "planned early June"),
    ("22. April 2027", "24. Juni 2027"), ("22. April", "24. Juni"), ("April 22", "June 24"),
    ("25. April", "27. Juni"),
]
DATE = re.compile(r"(?<![\d.])(?:(\d{1,2})\.\s?([–-])\s?)?(\d{2})\.(\d{2})\.(\d{4})?(?!\d)")
WREF = re.compile(r"((?:Docket|Wochenreview|Content-Batch|Batch|Gate|GATE|Offen aus|Offenes aus|Woche|Ordner „) ?W?)(\d{1,2})\b")
ISO = re.compile(r"\b(202[67])-(\d{2})-(\d{2})\b")


def infer(day, mon, year):
    y = int(year) if year else (2026 if mon >= 8 else 2027)
    return dt.date(y, mon, day)


def sub_date(m):
    d1, dash, dd, mm, yy = m.groups()
    try:
        day, mon = int(dd), int(mm)
        if not (1 <= day <= 31 and 1 <= mon <= 12):
            return m.group(0)
        end = infer(day, mon, yy)
        start = None
        if d1:
            s = int(d1)
            start = end.replace(day=s) if s <= day else (end.replace(day=1) - dt.timedelta(days=1)).replace(day=s)
    except ValueError:
        return m.group(0)
    ne = remap(end)
    ys = f"{ne.year}" if yy else ""
    if start is None:
        if ne == end:
            return m.group(0)
        return f"{ne.day:02d}.{ne.month:02d}.{ys}"
    ns = remap(start)
    if ns == start and ne == end:
        return m.group(0)
    if ns.month == ne.month:
        return f"{ns.day:02d}.{dash}{ne.day:02d}.{ne.month:02d}.{ys}"
    return f"{ns.day:02d}.{ns.month:02d}.{dash}{ne.day:02d}.{ne.month:02d}.{ys}"


def sub_wref(m):
    n = int(m.group(2))
    if 19 <= n <= 32:
        return m.group(1) + str(MAP[n])
    return m.group(0)


def sub_iso(m):
    try:
        d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return m.group(0)
    return remap(d).isoformat()


def text(s, iso=False):
    for a, b in SPECIAL:
        s = s.replace(a, b)
    s = DATE.sub(sub_date, s)
    s = WREF.sub(sub_wref, s)
    if iso:
        s = ISO.sub(sub_iso, s)
    return s


def walk(x, f):
    if isinstance(x, str):
        return f(x)
    if isinstance(x, list):
        return [walk(y, f) for y in x]
    if isinstance(x, dict):
        return {k: walk(v, f) for k, v in x.items()}
    return x


def dayfix(s, od, nd):
    if od == nd:
        return s
    o, n = (od - DAY0).days, (nd - DAY0).days
    return re.sub(rf"\bDay {o}\b", f"Day {n}", s)


def weeks():
    old = {n: json.loads((R6 / "weeks" / f"w{n}.json").read_text(encoding="utf-8")) for n in range(5, 33)}
    new = {}
    for n, data in old.items():
        nn = MAP[n]
        delta = dt.timedelta(days=7 * (nn - n))
        out = {k: walk(v, text) for k, v in data.items() if k != "days"}
        out["n"] = nn
        out["days"] = {}
        for key, tasks in data["days"].items():
            od = dt.date.fromisoformat(key)
            nd = od + delta
            out["days"][nd.isoformat()] = [walk(walk(t, text), lambda s: dayfix(s, od, nd)) for t in tasks]
        new[nn] = out
    # Jahrestag 24.02.: Hinweis an den echten Tag, Post auf Do
    w24 = new[24]["days"]
    posts = [t for t in w24["2027-02-24"] if t.get("c") == "C" and "posten" in t.get("t", "")]
    w24["2027-02-24"] = [{"c": "N", "t": "Info: Heute nichts Werbliches, kein Post und keine Story (5. Jahrestag des russischen Großangriffs). Der Post von heute läuft morgen."}] + [t for t in w24["2027-02-24"] if t not in posts]
    w24["2027-02-25"] += posts
    for key in new[26]["days"]:
        new[26]["days"][key] = [t for t in new[26]["days"][key] if not (t.get("c") == "N" and "Jahrestag" in t.get("t", ""))]
    for n in CATCH:
        prev = new[n - 1]
        days = {(wstart(n) + dt.timedelta(days=i)).isoformat(): [] for i in range(7)}
        k = list(days)
        days[k[0]] = [{"c": "A", "t": "Aufholwoche: Offenes der letzten zwei Wochen nachholen", "m": 60,
                       "s": ["Im Docket die letzten zwei Wochen durchgehen: Was ist nicht abgehakt?",
                             "Nach Wirkung sortieren: zuerst alles, was Geld, Fabrik oder Vorbestellungen betrifft, dann Content.",
                             "Was nach zwei Wochen immer noch offen ist und nichts bewegt: streichen und Claude Bescheid sagen.",
                             "Diese Woche kommen keine neuen Aufgaben dazu. Wenn nichts offen ist: frei."],
                       "f": "nichts Wichtiges aus den letzten zwei Wochen mehr offen ist."}]
        days[k[2]] = [{"c": "C", "t": "18:00 · Reserve-Post oder Variante deines besten Videos", "m": 20,
                       "s": ["Aus dem Reserve-Ordner posten (V110, V113, V119) oder das beste Video der letzten 14 Tage mit neuem Hook neu schneiden.", "Ersten Kommentar mit dem Link anpinnen, 15 Minuten auf Kommentare antworten."],
                       "f": "ein Post läuft."}]
        days[k[3]] = [{"c": "V", "t": "Vorbestellungen und DMs: Fragen beantworten, Zusagen ohne Kauf freundlich nachfassen", "m": 20,
                       "s": ["Shopify-Mails und DMs durchgehen.", "Jede Zusage aus „Die ersten 35“ ohne Bestellung einmal persönlich anschreiben, nie drängen."],
                       "f": "keine Kundenfrage älter als 48 Stunden ist."}]
        days[k[5]] = [{"c": "C", "t": "12:00 · Reserve-Post oder Story-Serie", "m": 15,
                       "s": ["Zweiter Reserve-Post der Woche oder 3 Storys mit Proto-Details."], "f": "der Post oder die Storys laufen."}]
        days[k[6]] = [{"c": "A", "t": "Wochenreview (kurz): Zahlen ins Cockpit", "m": 20,
                       "s": ["Warteliste, Follower, Zusagen und Vorbestellungen ins Cockpit.", "Eine Zeile an Claude: Was ist liegen geblieben, was hat gewirkt?"],
                       "f": "die Zahlen im Cockpit stehen."}]
        new[n] = {"n": n, "phase": prev["phase"], "goal": "Aufholwoche: keine neuen Aufgaben. Offenes nachholen, sonst frei.",
                  "kpi": prev.get("kpi", []), "days": days}
    for i, n in enumerate(PAUSE):
        days = {(wstart(n) + dt.timedelta(days=j)).isoformat(): [] for j in range(7)}
        k = list(days)
        days[k[0]] = [{"c": "N", "t": f"Abi-Pause, Woche {i + 1} von {len(PAUSE)}: keine Aufgaben. Automatisch laufen ein eingeplanter Post pro Woche und die Produktion in der Fabrik. Viel Erfolg!"}]
        days[k[6]] = [{"c": "A", "t": "10 Minuten: Mails von Kunden und Fabrik", "m": 10,
                       "s": ["Shopify-Mails und das Fabrik-Postfach öffnen. Nur antworten, was nicht warten kann.", "Alles andere: „Ich melde mich ab dem 10.05.“"],
                       "f": "keine dringende Mail offen ist."}]
        if n == 34:
            days[k[6]].append({"c": "A", "t": "Neustart vorbereiten: Docket W35 lesen, Fabrik nach dem Liefertermin fragen", "m": 20,
                               "s": ["Die Aufgaben von W35 und W36 lesen, nichts abarbeiten.", "Fabrik per Mail: Ist die Ware fertig? Bleibt Lieferung ab Werk bis Fr 21.05.?", "Cockpit: Zahlen vom Ende der Pause eintragen."],
                               "f": "du weißt, wann die Ware kommt."})
        new[n] = {"n": n, "phase": new[27]["phase"], "goal": "Abi-Pause. Die Fabrik produziert, du schreibst Prüfungen.", "kpi": [], "days": days}
    # vor der Pause: Autopilot und Fabrik informieren
    d27 = new[27]["days"]
    d27["2027-03-15"].append({"c": "B", "t": "Fabrik informieren: Abi-Pause, Liefertermin ab Werk bis Fr 21.05.", "m": 15,
                              "s": ["Mail an die Fabrik: Vom 22.03. bis 09.05. antworte ich nur sonntags.",
                                    "Liefertermin bestätigen lassen: Ware ab Werk bis Fr 21.05., Restzahlung nach den Fotos der fertigen Ware.",
                                    "Fragen, ob sie früher fertig sind und die Ware bis dahin lagern."],
                              "f": "die Fabrik den Termin schriftlich bestätigt hat."})
    d27["2027-03-20"].append({"c": "C", "t": "Autopilot für die Abi-Pause: 7 Posts vorproduzieren und einplanen", "m": 90,
                              "s": ["7 Posts für die 7 Pausenwochen, je einer pro Woche: Reserve-Videos, Making-ofs, Proto-Details.",
                                    "Einer davon ist ehrlich: „Ich schreibe Abi. Der Drop ist am 24.06. Bis dahin baue ich weiter.“",
                                    "In der Meta Business Suite und auf TikTok mit Datum und Uhrzeit einplanen, Link-Kommentar vorbereiten.",
                                    "Willkommens-Mail der Warteliste prüfen: Drop-Termin 24.06."],
                              "f": "7 Posts eingeplant sind, einer pro Woche bis zum 09.05."})
    for n in range(5, NEWMAX + 1):
        (R6 / "weeks" / f"w{n}.json").write_text(json.dumps(new[n], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def kpi():
    p = R6 / "kpi.json"
    old = {e["w"]: e for e in json.loads(p.read_text(encoding="utf-8"))}
    out = {}
    for w, e in old.items():
        nn = MAP.get(w, w)
        e = walk(copy.deepcopy(e), text)
        e["w"], e["d"] = nn, (wstart(nn) + dt.timedelta(days=6)).isoformat()
        out[nn] = e
    for n in CATCH + PAUSE:
        e = copy.deepcopy(out[n - 1])
        e["w"], e["d"] = n, (wstart(n) + dt.timedelta(days=6)).isoformat()
        e["gate"] = "Aufholwoche: keine neuen Gates" if n in CATCH else "Abi-Pause: keine Gates, Zahlen nur eintragen, wenn du magst"
        e["mass"] = []
        out[n] = e
    p.write_text(json.dumps([out[k] for k in sorted(out)], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def files():
    pats = ["strategie.md", "research/*.md", "build/r5_ref_*.html", "build/urteil_head.html", "build/entscheidung_1110.html",
            "build/footer.html", "build/refs6.py", "build/tracking6.py", "build/rewind_data.py", "build/check_week.py"]
    for pat in pats:
        for f in sorted(R6.glob(pat)):
            s = f.read_text(encoding="utf-8")
            iso = f.suffix == ".py"
            t = text(s, iso=iso)
            if t != s:
                f.write_text(t, encoding="utf-8")
                print("angepasst:", f.relative_to(R6))


weeks()
kpi()
files()
