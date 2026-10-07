# -*- coding: utf-8 -*-
import datetime as dt, json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_data import E, CD

OUT = "/home/user/email-bot/novalife/time-travel/rev6/research/content.md"
OUTJ = "/home/user/email-bot/novalife/time-travel/rev6/research/content_library.json"
DAY1 = dt.date(2026, 10, 12)
WD = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
W1 = dt.date(2026, 9, 14)

CTA = {
    "LIST": ("Link in bio: join the list. The list buys first, at the pre-order price.",
             "Link in Bio: Trag dich ein. Wer auf der Liste ist, kauft zuerst und zum Vorbestellpreis."),
    "PRE": ("Pre-order in bio: €149 instead of €169. [Y] of 35 left.",
            "Vorbestellen über den Link in Bio: 149 € statt 169 €. Noch [Y] von 35."),
    "DROP": ("Drop 22.04., 19:00. The list gets in at 18:00. Link in bio.",
             "Drop 22.04., 19:00. Die Liste kommt um 18:00 rein. Link in Bio."),
    "LIVE": ("Live now. Link in bio.", "Jetzt live. Link in Bio."),
    "STORY": ("Link-Sticker auf die Warteliste (ab 14.01. auf die Vorbestellung, ab 22.04. auf die Kollektion)",
              "Link-Sticker auf die Warteliste (ab 14.01. auf die Vorbestellung, ab 22.04. auf die Kollektion)"),
}
TAGS = {
    "BUILD": "#buildinpublic #clothingbrand #denim #novalifetimetravel",
    "ORIGIN": "#crossstitch #folkembroidery #embroidery #novalifetimetravel",
    "REAL": "#buildinpublic #smallbusiness #denim #novalifetimetravel",
    "DETAIL": "#embroidereddenim #crossstitch #denim #novalifetimetravel",
    "REACH": "#embroidereddenim #berlinfashion #denim #novalifetimetravel",
    "ASK": "",
}

def phase_of(d):
    if d < dt.date(2026, 12, 3): return "P1 Prozess (vor Proto: nur Papier, Datei, Zahl, Prozess)"
    if d < dt.date(2027, 1, 14): return "P2 Ab Proto"
    if d < dt.date(2027, 2, 8): return "P3 Vorbestellung"
    if d < dt.date(2027, 3, 29): return "P4 Produktion und Kampagne"
    if d < dt.date(2027, 4, 22): return "P5 Countdown"
    return "P6 Drop"

def week_of(d):
    return (d - W1).days // 7 + 1

BAN_EN = ["authentic", "slavic", "soviet", "ussr", "one people", "brother", "border", "five ears", "vyshyvanka", "alatyr", "we are"]
BAN_DE = ["authentisch", "slawisch", "sowjet", "grenze", "ein volk", "brudervölker", "fünf ähren"]
problems = []

def fill(s, day):
    return s.replace("{day}", str(day)) if s else s

def words(s):
    s2 = re.sub(r"\[[^\]]*\]", "X", s)  # Platzhalter zählt als ein Wort
    return len([w for w in s2.split() if w.strip()])

recs = []
for e in E:
    d = dt.date.fromisoformat(e["date"]) if e.get("date") else None
    day = (d - DAY1).days + 1 if d else "X"
    rec = dict(e)
    for k in ("hook_en", "hook_de", "alt_en", "cap"):
        rec[k] = fill(e.get(k, ""), day)
    rec["phase"] = phase_of(d) if d else e.get("phase", "Reserve")
    rec["date_label"] = (WD[d.weekday()] + " " + d.strftime("%d.%m.%Y")) if d else "frei (Reserve)"
    rec["week"] = week_of(d) if d else None
    rec["tags"] = TAGS[e["slot"]]
    rec["cta_en"], rec["cta_de"] = CTA[e["cta"]]
    chk = []
    if d and d < dt.date(2026, 12, 3):
        chk.append("Vor Proto: nur Papier, Datei, Zahl, Prozess. Kein fertiges Teil, kein Mockup ✓")
    chk.append("Sprachregel: Subjekt ist das Muster, kein „wir“, kein „authentisch“ ✓")
    chk += [x for x in e.get("check", []) if x != "—"]
    rec["checks"] = chk
    # Prüfungen
    if words(rec["hook_en"]) > 10:
        problems.append(f"{e['id']}: Hook EN hat {words(rec['hook_en'])} Wörter")
    for k in ("hook_en", "alt_en", "cap"):
        low = rec[k].lower()
        for b in BAN_EN:
            if b in low: problems.append(f"{e['id']}: verbotenes Wort „{b}“ in {k}")
    low = rec["hook_de"].lower()
    for b in BAN_DE:
        if b in low: problems.append(f"{e['id']}: verbotenes Wort „{b}“ in hook_de")
    if not (3 <= len(e["shots"]) <= 6) and not e["fmt"].startswith("Story") and "Live" not in e["fmt"] and "Foto" not in e["fmt"] and "Video-Antwort" not in e["fmt"]:
        problems.append(f"{e['id']}: {len(e['shots'])} Shots")
    recs.append(rec)

ids = [r["id"] for r in recs]
assert len(ids) == len(set(ids)), "doppelte IDs"

cds = []
for c in CD:
    d = dt.date.fromisoformat(c["date"])
    assert (dt.date(2027, 4, 22) - d).days == c["n"], c["id"]
    rec = dict(c)
    rec["date_label"] = WD[d.weekday()] + " " + d.strftime("%d.%m.%Y")
    rec["week"] = week_of(d)
    if words(c["hook_en"]) > 10: problems.append(f"{c['id']}: Hook zu lang")
    for b in BAN_EN:
        if b in (c["hook_en"] + c["cap"]).lower(): problems.append(f"{c['id']}: {b}")
    cds.append(rec)

if problems:
    print("PROBLEME:"); print("\n".join(problems)); sys.exit(1)

# ---------- Statistik ----------
from collections import Counter
pc = Counter(r["phase"].split(" (")[0] for r in recs)
sc = Counter(r["slot"] for r in recs)
n_dated = sum(1 for r in recs if r.get("date"))
n_res = len(recs) - n_dated

# ---------- Markdown-Bausteine ----------
def block(r):
    L = []
    when = r["date_label"] + (" " + r["time"] if r.get("date") else "")
    L.append(f"#### {r['id']} · {when} · {r['slot']} · {r['title']}")
    wk = f" · **Docket-Woche:** W{r['week']}" if r.get("week") else ""
    L.append(f"- **Phase:** {r['phase']} · **Format:** {r['fmt']} · **Dauer:** {r['dauer']}{wk}")
    L.append(f"- **Docket:** {r['docket']}")
    L.append(f"- **Hook EN (Slide 1 / erster Satz):** „{r['hook_en']}“")
    L.append(f"- **Hook DE:** „{r['hook_de']}“")
    L.append(f"- **Test-Hook B:** „{r['alt_en']}“")
    L.append("- **Shots:** " + " · ".join(f"{i+1}) {s}" for i, s in enumerate(r["shots"])))
    L.append(f"- **Drehort:** {r['ort']}")
    L.append(f"- **Ton:** {r['ton']}")
    cap = r["cap"]
    if r["cta"] != "STORY" and not cap.startswith("("):
        cap = f"{cap} {r['cta_en']} {r['tags']}".strip()
    L.append(f"- **Caption EN:** {cap}")
    L.append(f"- **CTA:** {r['cta_en']}" + ("" if r["cta"] == "STORY" else f" (DE: {r['cta_de']})"))
    L.append("- **Regel-Check:** " + " · ".join(r["checks"]))
    return "\n".join(L)

def cd_block(c):
    L = []
    L.append(f"#### {c['id']} · {c['date_label']} 18:00 · COUNTDOWN · {c['motiv']}")
    L.append(f"- **Phase:** P5 Countdown · **Format:** Video 9:16, Countdown-Vorlage · **Dauer:** 6–10 s · **Docket-Woche:** W{c['week']}")
    L.append(f"- **Hook EN (oben im Bild):** „{c['hook_en']}“")
    L.append(f"- **Hook DE:** „{c['hook_de']}“")
    sh = ["Einstieg: Vorlage T4, oben groß „T−%d“ auf Indigo (0,5 s)" % c["n"]] + c["shots"] + ["Endframe: „22.04. · 19:00“ (1 s)"]
    L.append("- **Shots:** " + " · ".join(f"{i+1}) {s}" for i, s in enumerate(sh)))
    L.append(f"- **Drehort:** {c['ort']}")
    L.append("- **Ton:** ein fester Countdown-Sound für alle 24 (Business-Bibliothek der App), damit die Serie wiedererkannt wird")
    L.append(f"- **Caption EN:** {c['cap']} {CTA['DROP'][0]} #novalifetimetravel #embroidereddenim #denim")
    L.append(f"- **CTA:** {CTA['DROP'][0]} · Story mit Countdown-Sticker auf 22.04. 19:00")
    chk = ["Sprachregel ✓", "Gezeigt wird nur, was existiert ✓"] + c["check"]
    L.append("- **Regel-Check:** " + " · ".join(chk))
    if c.get("real"):
        L.append(f"- **Echter Tag:** {c['real']}")
    return "\n".join(L)

sections = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static_md.py"), encoding="utf-8").read(), sections)

lib = []
order = ["P1 Prozess", "P2 Ab Proto", "P3 Vorbestellung", "P4 Produktion und Kampagne", "P6 Drop"]
heads = {
    "P1 Prozess": "### 3.1 · P1 Prozess · Mo 12.10.–Mi 02.12.2026 · 3 Posts pro Woche · kein fertiges Teil",
    "P2 Ab Proto": "### 3.2 · P2 Ab Proto · Do 03.12.2026–Mi 13.01.2027 · 5 Posts pro Woche (Feiertage 2–3)",
    "P3 Vorbestellung": "### 3.3 · P3 Vorbestellung · Do 14.01.–So 07.02.2027 · 4–5 Posts pro Woche",
    "P4 Produktion und Kampagne": "### 3.4 · P4 Produktion und Kampagne · Mo 08.02.–So 28.03.2027 · 4 Posts pro Woche + Story",
    "P6 Drop": "### 3.6 · P6 Drop · Do 22.–So 25.04.2027",
}
for ph in order:
    lib.append(heads[ph])
    for r in recs:
        if r.get("date") and r["phase"].startswith(ph):
            lib.append(block(r))
    if ph == "P4 Produktion und Kampagne":
        lib.append("### 3.5 · P5 Countdown T−24 bis T−1 · Mo 29.03.–Mi 21.04.2027 · täglich 18:00")
        lib.append(sections["COUNTDOWN_INTRO"])
        for c in sorted(cds, key=lambda x: -x["n"]):
            lib.append(cd_block(c))
lib.append("### 3.7 · Reserve V108–V125 · ohne festes Datum")
lib.append(sections["RESERVE_INTRO"])
for r in recs:
    if not r.get("date"):
        lib.append(block(r))

overview = sections["LIB_INTRO"].format(
    n_total=len(recs), n_dated=n_dated, n_res=n_res, n_cd=len(cds),
    p1=pc.get("P1 Prozess", 0), p2=pc.get("P2 Ab Proto", 0), p3=pc.get("P3 Vorbestellung", 0),
    p4=pc.get("P4 Produktion und Kampagne", 0), p6=pc.get("P6 Drop", 0),
    b=sc["BUILD"], o=sc["ORIGIN"], re_=sc["REAL"], de=sc["DETAIL"], rh=sc["REACH"], a=sc["ASK"])

md = "\n\n".join([sections["HEAD"], sections["KURZ"], sections["S0"], sections["S1"], sections["S2"],
                  overview, "\n\n".join(lib), sections["S4"], sections["S5"], sections["S6"], sections["S7"]]) + "\n"
open(OUT, "w", encoding="utf-8").write(md)

js = dict(stand="2026-10-07", quelle="content.md", videos=[{k: v for k, v in r.items() if k not in ("check",)} for r in recs], countdown=cds)
json.dump(js, open(OUTJ, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

kurz = sections["KURZ"]
kw = len(re.sub(r"[#*`>|\-]", " ", kurz).split())
print("OK", len(recs), "Videos,", len(cds), "Countdown,", n_dated, "mit Datum,", n_res, "Reserve")
print("Phasen", dict(pc)); print("Slots", dict(sc)); print("Kurzfassung Wörter:", kw)
print("Datei", OUT, os.path.getsize(OUT), "Bytes")
