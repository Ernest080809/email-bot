"""Baut den Time Travel Drop Docket Rev. 6 aus den Daten in rev6/.

Ablauf: python3 rev6/build/build6.py  →  rev6/docket_rev6.html
Wochen 1–3 und W4 Mo–Mi kommen unverändert aus Rev. 5.3 (r5/weeks_r5.json),
damit die gespeicherten Häkchen (Schlüssel w{n}d{tag}t{index}) gültig bleiben.
Ab Do 08.10.2026 kommen die Tage aus rev6/weeks/w{n}.json.
"""
import datetime as dt
import html.parser
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R6 = ROOT / "rev6"
BUILD = R6 / "build"
CUTOVER = dt.date(2026, 10, 8)
W1 = dt.date(2026, 9, 14)
CATS = {"B", "C", "D", "A", "S", "V", "N"}
VOID = {"br", "img", "input", "meta", "link", "hr", "wbr", "source", "col"}

problems, warnings, FALLBACK = [], [], []
_extra = pathlib.Path(__file__).resolve().parent / "extra.json"
EXTRA = json.loads(_extra.read_text(encoding="utf-8")) if _extra.exists() else {}


def week_start(n):
    return W1 + dt.timedelta(days=7 * (n - 1))


def conv_old(t):
    c, title, m, steps, fertig, prompt, flag = (list(t) + [""] * 7)[:7]
    o = {"c": c, "t": title}
    if m:
        o["m"] = m
    if steps:
        o["s"] = steps
    if fertig:
        o["f"] = fertig
    if prompt:
        o["p"] = prompt
    if flag:
        o["x"] = flag
    return o


STRAT_SEC = {"2": "Strategie", "3": "Strategie", "5": "Strategie", "8": "Strategie", "6": "Wochenziele, Gates", "7": "Wochenziele, Gates",
             "9": "Content-System", "10": "Berlin", "11": "Warteliste, Netz, Creator, Presse", "13": "Website", "16": "Risiken", "18": "Quellen"}
FILE_REF = {"zielgruppe": "Abschnitt „Zielgruppe“", "design": "Abschnitt „Design“", "berlin": "Referenz „Berlin“",
            "community": "Referenz „Warteliste, Netz, Creator, Presse“", "content": "Referenz „Content-System“",
            "website": "Referenz „Website“", "tools": "Referenz „Tools“", "lieferanten": "Referenz „Fabriken und Lieferanten“",
            "markt": "Referenz „Markt“"}


def human(s):
    """Interne Dateiverweise → Abschnitte im Docket (nur für Text, den Ernest liest; Prompts bleiben unverändert)."""
    s = re.sub(r"`?rev6/research/design_varianten/NVL_Papiertest3_Varianten\.pdf`?", "NVL_Papiertest3_Varianten.pdf (von Claude am 07.10. im Chat geschickt)", s)

    def strat(m):
        sec = m.group(1)
        top = sec.split(".")[0] if sec else ""
        if top == "12":
            return f"Abschnitt „Design“ ({sec})"
        if top == "17":
            return "Abschnitt „Das Urteil“ → Entscheidungen"
        name = STRAT_SEC.get(top)
        return f"Referenz „{name}“ {sec}" if name else (f"Strategie {sec}" if sec else "Strategie")
    s = re.sub(r"`?strategie\.md`?(?:,? (?:Abschnitt )?(\d+(?:\.\d+)?))?", strat, s)

    def other(m):
        label = FILE_REF[m.group(1)]
        sec = m.group(2)
        return f"{label} {sec}" if sec else label
    s = re.sub(r"`?(" + "|".join(FILE_REF) + r")\.md`?(?:,? (?:Abschnitt )?(\d+(?:\.\d+)?))?", other, s)
    s = re.sub(r"`?produkt-spec(?:_rev13)?\.md`?", "produkt-spec.md (Projektdatei)", s)
    s = re.sub(r"`?time-travel-drop-plan\.md`?", "time-travel-drop-plan.md (Projektdatei)", s)
    return s


def humanize_task(t):
    for k in ("t", "f"):
        if isinstance(t.get(k), str):
            t[k] = human(t[k])
    if isinstance(t.get("s"), list):
        t["s"] = [human(x) for x in t["s"]]
    for o in t.get("o", []) or []:
        for k in ("n", "a", "h"):
            if isinstance(o.get(k), str):
                o[k] = human(o[k])
    v = t.get("v")
    if isinstance(v, dict):
        for k in ("ort", "check", "text", "ton"):
            if isinstance(v.get(k), str):
                v[k] = human(v[k])
    return t


def clean_task(t, where):
    if isinstance(t, dict) and not t.get("raw"):
        t = humanize_task(dict(t))
    if not isinstance(t, dict):
        problems.append(f"{where}: Aufgabe ist kein Objekt")
        return None
    c = t.get("c")
    if c not in CATS:
        problems.append(f"{where}: unbekannte Kategorie {c!r}")
        return None
    if not t.get("t"):
        problems.append(f"{where}: Titel fehlt")
    out = {"c": c, "t": str(t.get("t", "")).strip()}
    if c == "N":
        return out
    m = t.get("m", 0)
    try:
        m = int(m)
    except (TypeError, ValueError):
        problems.append(f"{where}: Minuten {m!r}")
        m = 0
    if m:
        out["m"] = m
    if t.get("plus"):
        out["plus"] = True
    for k in ("s",):
        if t.get(k):
            out[k] = [str(x) for x in t[k] if str(x).strip()]
    for k in ("f", "p", "x"):
        if t.get(k):
            out[k] = str(t[k])
    if t.get("o"):
        lst = []
        for i, x in enumerate(t["o"]):
            if not isinstance(x, dict) or not x.get("n"):
                problems.append(f"{where}: Ort/Link {i} ohne Namen")
                continue
            y = {"n": str(x["n"])}
            u = str(x.get("u") or "").strip()
            if u:
                if not u.startswith(("http://", "https://")):
                    problems.append(f"{where}: URL ohne http(s): {u}")
                else:
                    y["u"] = u
            for k in ("a", "h"):
                if x.get(k):
                    y[k] = str(x[k])
            lst.append(y)
        if lst:
            out["o"] = lst
    if t.get("v"):
        v = t["v"]
        if isinstance(v, dict) and (v.get("hook_en") or v.get("shots")):
            out["v"] = {k: v[k] for k in ("id", "slot", "dauer", "plattform", "hook_en", "hook_de", "shots", "ort", "ton", "text", "cta", "caption", "check") if v.get(k)}
        else:
            warnings.append(f"{where}: Video-Brief leer")
    return out


KEYWORDS = [
    ("D", r"\b(gate|freeze|entscheid|entscheidung|validierung|schwelle|freigeben|freigabe)\b"),
    ("C", r"\b(V\d{3}|CD-T\d{2}|post|posten|dreh|drehen|video|reel|story|karussell|caption|mail|newsletter|schnitt|schneiden)\b"),
    ("V", r"\b(netz|zusage|creator|presse|abend|warteliste|liste|laden|läden|markt|flohmarkt|dm|bring 3|broadcast|einladung|gäste)\b"),
    ("A", r"\b(shopify|steuer|gewerbe|lucid|recht|agb|widerruf|impressum|datenschutz|payments|eori|zoll|versand|etikett|kasse|konto)\b"),
    ("B", r"\b(fabrik|tech pack|proto|pp|stick|patch|digitiz|muster|stoff|sample|label|knopf|garn|naht)\b"),
]


def from_skeleton(line):
    """Macht aus einer Skelett-Zeile eine einfache Aufgabe (Rückfall, solange die Woche nicht ausgearbeitet ist)."""
    text = line.strip()
    plus = False
    m = 0
    if text.lower().startswith("info"):
        return {"c": "N", "t": re.sub(r"^info\s*·\s*", "", text, flags=re.I)}
    mm = re.match(r"^(grind\+\s*)?(ausnahme\s*)?(\d+)\s*[′']\s*·\s*(.*)$", text, re.I)
    gate = False
    if mm:
        plus = bool(mm.group(1))
        m = int(mm.group(3))
        text = mm.group(4)
    elif text.lower().startswith("gate"):
        gate = True
        text = re.sub(r"^gate\s*·\s*", "", text, flags=re.I)
        m = 10
    c = "D" if gate else "B"
    if not gate:
        low = text.lower()
        for cat, pat in KEYWORDS:
            if re.search(pat, low, re.I):
                c = cat
                break
    title = re.split(r"\s\(|:\s|;\s|\s·\s", text, maxsplit=1)[0].strip()
    if len(title) > 90:
        title = title[:87].rsplit(" ", 1)[0] + " …"
    t = {"c": c, "t": title or text[:80], "m": m or 15, "s": [text], "f": "Erledigt wie beschrieben."}
    if plus:
        t["plus"] = True
    return t


def skeleton_week(n):
    for w in json.loads((R6 / "skeleton.json").read_text(encoding="utf-8")):
        if w["n"] == n:
            days = {d: [from_skeleton(x) for x in lines if x.strip() and x.strip().lower() != "frei"] for d, lines in w["tage"].items()}
            first = min(days)
            days[first].insert(0, {"c": "N", "t": "Diese Woche steht noch im Kurzformat aus dem Tagesskelett: Termine, Dauer und Inhalt stimmen. Die ausgearbeitete Fassung mit Schritten, Links und Video-Briefing kommt vor Wochenbeginn."})
            return {"n": n, "phase": w["phase"], "goal": w.get("goal", ""), "kpi": w.get("kpi", []), "days": days}
    return None


def load_weeks():
    r5 = json.loads((ROOT / "r5" / "weeks_r5.json").read_text(encoding="utf-8"))
    weeks = []
    for w in r5:
        n = w["n"]
        if n > 4:
            break
        days = [[conv_old(t) for t in d] for d in w["days"]]
        weeks.append({"n": n, "phase": w["phase"], "goal": w["goal"], "start": w["start"], "days": days})
    # W4: Mo–Mi aus Rev. 5, Do–So neu
    for n in range(4, 33):
        f = R6 / "weeks" / f"w{n}.json"
        data = None
        if f.exists():
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                problems.append(f"W{n}: JSON-Fehler {e}")
        if data is None:
            data = skeleton_week(n)
            FALLBACK.append(n)
            if data is None:
                problems.append(f"W{n}: weder Datei noch Skelett")
                continue
        start = week_start(n)
        if n == 4:
            wk = weeks[3]
            wk["goal"] = data.get("goal") or wk["goal"]
        else:
            wk = {"n": n, "phase": data.get("phase"), "goal": data.get("goal", ""), "start": start.isoformat(), "days": [[] for _ in range(7)]}
            weeks.append(wk)
        if data.get("kpi"):
            wk["kpi"] = [{"k": str(k.get("k", "")), "ziel": str(k.get("ziel", ""))} for k in data["kpi"] if k.get("k")]
        if wk["phase"] not in {"P0", "P1", "P2", "P3", "P4", "P5"}:
            problems.append(f"W{n}: Phase {wk['phase']!r}")
        days = data.get("days", {})
        for di in range(7):
            d = start + dt.timedelta(days=di)
            if d < CUTOVER:
                continue
            key = d.isoformat()
            if key not in days:
                problems.append(f"W{n}: Tag {key} fehlt")
                wk["days"][di] = []
                continue
            tasks = [clean_task(t, f"W{n} {key} #{i}") for i, t in enumerate(days[key])]
            tasks = [t for t in tasks if t]
            ex = EXTRA.get(key, {})
            pre = [clean_task(t, f"extra {key}") for t in ex.get("prepend", [])]
            post = [clean_task(t, f"extra {key}") for t in ex.get("append", [])]
            wk["days"][di] = [t for t in pre if t] + tasks + [t for t in post if t]
        extra = set(days) - {(start + dt.timedelta(days=i)).isoformat() for i in range(7)}
        if extra:
            problems.append(f"W{n}: Tage außerhalb der Woche {sorted(extra)}")
    return weeks


def check_minutes(weeks):
    for w in weeks:
        start = dt.date.fromisoformat(w["start"])
        for di, day in enumerate(w["days"]):
            d = start + dt.timedelta(days=di)
            if d < CUTOVER:
                continue
            core = sum(t.get("m", 0) for t in day if t["c"] not in ("N", "S") and not t.get("plus") and t.get("x") != "s")
            if core > 150:
                warnings.append(f"W{w['n']} {d}: Kern {core} Min.")


class TagCheck(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errs = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errs.append(f"</{tag}> erwartet </{self.stack[-1] if self.stack else '-'}> (Zeile {self.getpos()[0]})")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()


def check_html(name, frag):
    p = TagCheck()
    p.feed(frag)
    p.close()
    for e in p.errs[:5]:
        problems.append(f"{name}: {e}")
    if p.stack:
        problems.append(f"{name}: nicht geschlossen {p.stack[-5:]}")


def read(name, default=""):
    f = BUILD / name
    return f.read_text(encoding="utf-8") if f.exists() else default


def main():
    weeks = load_weeks()
    check_minutes(weeks)
    kpi = json.loads((R6 / "kpi.json").read_text(encoding="utf-8")) if (R6 / "kpi.json").exists() else []
    if not kpi:
        problems.append("kpi.json fehlt oder leer")
    order = json.loads((R6 / "ref" / "order.json").read_text(encoding="utf-8")) if (R6 / "ref" / "order.json").exists() else []
    refs = []
    for name in order:
        f = R6 / "ref" / name
        if not f.exists():
            f = BUILD / name
        if not f.exists():
            problems.append(f"Referenz {name} fehlt")
            continue
        frag = f.read_text(encoding="utf-8")
        check_html(name, frag)
        refs.append(frag)
    parts = {k: read(f) for k, f in {"URTEIL": "urteil.html", "ZIELGRUPPE": "zielgruppe.html", "DESIGN": "design.html", "KPI_TILES": "kpi_tiles.html", "FOOTER": "footer.html"}.items()}
    for k, v in parts.items():
        if not v.strip():
            problems.append(f"Abschnitt {k} leer")
        check_html(k, v)
    css = read("r5_style.css") + "\n" + read("rev6_extra.css")
    js = read("app.js")
    tasks = sum(1 for w in weeks for d in w["days"] for t in d if t["c"] != "N")

    def jdump(x):
        return json.dumps(x, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    out = read("template.html")
    repl = {
        "CSS": css, "REVDATE": "08.10.2026", "TASKCOUNT": str(tasks),
        "SUBLINE": "Eine Kultur, eine Fabrik, 100 bestickte Jeans. Ziel: 10.000 € Umsatz am 25. April. Jeder Tag bis zum Drop steht hier: was du tust, wohin du gehst, welches Video du drehst, mit Links, Prompts und einem „Fertig, wenn“.",
        "PLANNOTE": f"{len(weeks)} Wochen, {tasks} Aufgaben. Die laufende Woche ist offen. „So geht’s“ zeigt Schritte, Orte, Links und Video-Briefing.",
        "WEEKS_JSON": jdump(weeks), "KPI_JSON": jdump(kpi), "APPJS": js, "REFS": "\n".join(refs),
    }
    repl.update(parts)
    missing = sorted(set(re.findall(r"\{\{([A-Z_]+)\}\}", out)) - set(repl))
    if missing:
        problems.append("Platzhalter ohne Inhalt: " + ", ".join(missing))
    # ein Durchgang über die Vorlage: eingesetzter Inhalt (z. B. Liquid-Code) wird nie erneut ersetzt
    out = re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: repl.get(m.group(1), m.group(0)), out)
    (R6 / "docket_rev6.html").write_text(out, encoding="utf-8")
    print(f"Wochen: {len(weeks)} · Aufgaben: {tasks} · Bytes: {len(out.encode())}")
    if FALLBACK:
        print("Aus dem Skelett (noch nicht ausgearbeitet):", ", ".join(f"W{n}" for n in FALLBACK))
    for w in warnings[:40]:
        print("Warnung:", w)
    print(f"Warnungen: {len(warnings)}")
    for p in problems[:80]:
        print("Problem:", p)
    print(f"Probleme: {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
