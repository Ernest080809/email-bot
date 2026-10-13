"""Erzeugt kompakte Briefings für die Wochen-Autoren des Docket Rev. 6.

Aufruf: python3 rev6/build/brief6.py
Schreibt rev6/briefs/rules.md, rev6/briefs/links.md und rev6/briefs/w{n}.md (n = 4 … 32).
"""
import datetime as dt
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R6 = ROOT / "rev6"
OUT = R6 / "briefs"
W1 = dt.date(2026, 9, 14)
DN = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]


def sections(md, level=2):
    """{nummer: text} für Überschriften wie '## 9 · Content-System'."""
    pat = re.compile(r"^(#{%d}) (\d+(?:\.\d+)?) · .*$" % level, re.M)
    hits = list(pat.finditer(md))
    out = {}
    for i, m in enumerate(hits):
        end = len(md)
        for m2 in hits[i + 1:]:
            end = m2.start()
            break
        out[m.group(2)] = md[m.start():end].rstrip()
    return out


def strat():
    md = (R6 / "strategie.md").read_text(encoding="utf-8")
    return md, sections(md, 2)


def sub(md, start_pat, stop_pat):
    a = re.search(start_pat, md, re.M)
    if not a:
        return ""
    b = re.search(stop_pat, md[a.end():], re.M)
    return md[a.start(): a.end() + (b.start() if b else len(md) - a.end())].rstrip()


FORMAT = """
## Dateiformat · rev6/weeks/w{n}.json (UTF-8, valides JSON)

{
 "n": 5, "phase": "P1", "goal": "Wochenziel in einem Satz",
 "kpi": [{"k": "Warteliste", "ziel": "40 (Alarm 15)"}, {"k": "Posts", "ziel": "3 + 2 Grind+"}],
 "days": { "2026-10-12": [Aufgabe, …], … jedes Datum der Woche (W4 nur 2026-10-08 bis 2026-10-11) }
}

Aufgabe = {
 "c": "B" | "C" | "V" | "D" | "A" | "S" | "N",
      B BUILD Produkt/Fabrik/Sample · C CONTENT Videos/Posts/E-Mails · V VERKAUF Warteliste/Netz/Zusagen/Creator/Berlin/Presse/Abende
      D ENTSCHEIDUNG (jedes Gate) · A ADMIN Shop/Recht/Steuer/Versand · S SPIEL (nur bei „Spiel bauen“) · N Notiz (nur "c" und "t")
 "t": "Titel, aktiv, max. ~70 Zeichen, feste Uhrzeit vorn („18:00 · V001 posten“)",
 "m": 25,                      ganze Minuten, realistisch
 "plus": true,                 nur bei optionalen Grind+-Aufgaben
 "s": ["…", "…"],              3–8 konkrete Schritte: Klickpfad („Shopify → Kunden → Segmente“), Adresse, was sagen/schreiben, was mitnehmen, welche Datei
 "f": "Fertig, wenn … (prüfbar)",
 "p": "fertiger Prompt an Claude zum Kopieren (wenn Claude Texte, Auswertungen, Rechnungen, Zeichnungen liefert). Platzhalter in [eckigen Klammern]. Der Prompt beginnt mit einem Satz Kontext („Projekt Time Travel, Docket W5 …“), weil ihn Ernest in einen neuen Chat im Projekt „novalife time travel“ einfügt.",
 "o": [{"n": "Name", "u": "https://…", "a": "Adresse · Öffnungszeit", "h": "Hinweis, z. B. vor Ort prüfen"}],
 "v": {                        nur bei Aufgaben, die ein Video/Karussell/Story drehen oder posten
   "id": "V001", "slot": "BUILD", "dauer": "20–25 s", "plattform": "TikTok + Reels + Shorts",
   "hook_en": "…", "hook_de": "…", "shots": ["…"], "ort": "konkreter Drehort",
   "ton": "…", "text": "Text im Bild", "cta": "CTA der Phase (Tabelle unten)",
   "caption": "fertige Caption EN mit CTA und 4–6 Hashtags", "check": "Regel-Check in einem Satz"
 },
 "x": "s"                      nur bei Spiel-Aufgaben
}

Prüfen: python3 rev6/build/check_week.py N  → muss „0 Fehler“ melden.
"""

RULES_HEAD = """# Regeln für die Wochen-Autoren · Docket Rev. 6

Du schreibst Tage des „Time Travel Drop Docket“ für Ernest Veskimäe (Novalife, Denim, Berlin). Drop Do 24.06.2027, 19:00.
Ziel 10.000 € Umsatz (64 Jeans netto, 72 brutto). Heute ist Mi 07.10.2026. Ernest liest jeden Tag oben „Heute“ und arbeitet die Aufgaben ab.
Er will es so detailliert, dass er nie nachdenken muss: was er tut, wohin er geht, welches Video er dreht, mit Links.

## Harte Regeln
- Das Skelett deines Briefings ist verbindlich: Jeder Stichpunkt wird zu einer Aufgabe. Info-Zeilen → "N". Gate-Zeilen → "D" mit den Gegenmaßnahmen als Schritte. „Grind+“-Zeilen → plus:true. Nichts fallen lassen. Kleinigkeiten darfst du zusammenlegen, die Reihenfolge am Tag ordnest du nach Uhrzeit und Dringlichkeit.
- Kern (ohne plus, ohne Spiel) höchstens 120 Min. pro Tag. Ausnahmen nur 08.–11.10., 16.01., 20.02., 30.03.–02.04., 06.–07.04., 22.–25.04.
- Fakten: Keine neuen URLs, Adressen, Preise, Termine erfinden. Nur aus dem Briefing, rev6/briefs/links.md (mit grep durchsuchen), strategie.md, den Recherche-Dateien oder Rev. 5.3. Vorbehalte übernehmen („vor Ort prüfen“, „ungeprüft“, „Schätzung“).
- Keine Aufgabe über Claudes Netzwerk, Sandbox, Proxy oder „Netz freischalten“. Was ungeprüft ist, prüft Ernest selbst („Link öffnen und prüfen“) oder er lässt es Claude per Prompt in einem normalen Chat mit Websuche prüfen.
- Keine Politik. Subjekt ist das Muster, nicht das Volk. Nie „authentisch“. Den Lebensbaum nie „slawisch“ nennen. Wortliste nach außen (9.3). Bildregeln (9.3). Bis zum Proto am Do 03.12.2026: kein fertiges Teil und kein Mockup, das wie eins aussieht. Sperrtermine: 23.–29.11. kein Ernte- und kein Serp-Bild, Sa 28.11. kein Post; Mi 24.02.2027 nichts Werbliches; Teilsperre am 22.04. (9.2).
- Keine Adressen scrapen. Die Gmail-Entwürfe an Hidrock und Lapiztola gehen nie raus. Ernest sendet und postet selbst.
- Stil: Deutsch, Du-Form, kurze klare Sätze, keine Floskeln, keine Gedankenstriche als Stilmittel. Hooks und Captions englisch (Hook zusätzlich deutsch), außer die Strategie verlangt Deutsch.
- Vorlagen (RFQ, Nachfassen, Call, Verhandlung, Absage, Referenz-Check, Berliner Sticker, Patch, Creator-DM) stehen im Docket unter „Referenz → Vorlagen“: nicht abschreiben, darauf verweisen. Neue Texte schreibst du direkt in die Schritte oder als Prompt an Claude.

## Standard-Bausteine
- Drehtag (meist Sonntag-Batch): Video-Briefing komplett ("v" mit Shots, Ort, Ton, Text im Bild), Drehreihenfolge nach Orten, Kamera 9:16, Licht von vorn, je Shot 3 Takes.
- Posttag: "v" mit Caption + Schritte: 17:55 Video in TikTok hochladen (Business-Konto, Musik nur aus der Commercial Music Library), Caption einfügen, 18:00 posten · gleich danach als Reel auf Instagram und als Short auf YouTube · Reel in die Story mit Link-Sticker · 15 Min. Kommentare beantworten (Regeln 9.3 Punkt 9).
- Jeder Sonntag: Wochenreview mit den Gates aus 7.1 (als Schritte: welche Zahl prüfen, was tun wenn darunter), „Zahlen ins Cockpit eintragen“ (bestätigte Warteliste aus Shopify → Kunden → Segment „E-Mail-Abonnenten“, Follower TikTok + Instagram gesamt, bezahlte Vorbestellungen; Docket-Abschnitt „Zahlen-Cockpit“), die Zeile an Claude aus 9.4 als Prompt.
- Orte und Websites gehören immer in "o" (Shopify-Admin https://admin.shopify.com, TikTok, Instagram, CapCut, Google Sheets, Läden, Märkte, Ämter mit Adresse).
"""


def build_rules(md, sec):
    parts = [RULES_HEAD, FORMAT]
    for k in ("9", "7", "14", "17"):
        if k == "7":
            parts.append(sub(md, r"^### 7\.1 ", r"^### 7\.2 "))
            parts.append(sub(md, r"^### 7\.2 ", r"^### 7\.3 "))
            parts.append(sub(md, r"^### 7\.3 ", r"^### 7\.4 "))
        else:
            parts.append(sec.get(k, ""))
    (OUT / "rules.md").write_text("\n\n".join(p for p in parts if p), encoding="utf-8")


def build_links():
    files = ["strategie.md", "research/berlin.md", "research/tools.md", "research/lieferanten.md",
             "research/community.md", "research/website.md", "research/content.md", "research/zielgruppe.md",
             "research/markt.md", "research/design.md"]
    rows = []
    for f in files:
        p = R6 / f
        head = ""
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("#"):
                head = line.lstrip("# ").strip()[:60]
                continue
            if "http" in line:
                txt = re.sub(r"\s+", " ", line.strip())
                rows.append(f"[{f.replace('research/', '')} · {head}] {txt[:600]}")
    plan = ROOT / "docs" / "time-travel-drop-plan.md"
    for line in plan.read_text(encoding="utf-8").splitlines():
        if "http" in line:
            rows.append(f"[plan] {line.strip()[:600]}")
    (OUT / "links.md").write_text(
        "# Link-Register (nur durchsuchen, z. B. grep -i 'mauerpark' rev6/briefs/links.md)\n\n" + "\n".join(rows) + "\n",
        encoding="utf-8")
    return len(rows)


def fmt_r5_task(t):
    c, title, m, steps, fertig, prompt, flag = (list(t) + [""] * 7)[:7]
    if c == "N":
        return f"- [Notiz] {title}"
    s = f"- [{c}] {title} ({m}′)"
    if steps:
        s += "\n  Schritte: " + " | ".join(steps)
    if fertig:
        s += f"\n  Fertig, wenn: {fertig}"
    if prompt:
        s += f"\n  Prompt: {prompt}"
    if flag:
        s += f"\n  Flag: {flag}"
    return s


OVERRIDES = {
    "2026-10-10": "ÄNDERUNG gegenüber dem Skelett: Die Zeile „Netzwerkzugang … freischalten“ entfällt. Stattdessen eine Aufgabe (A, 15′): „Claude prüft Fabriken und offene Regeln“ mit einem Prompt für einen normalen Claude-Chat mit Websuche: die 4 bekannten Fabriken nach der Prüfliste lieferanten.md 1.5 prüfen, 4 weitere Kandidaten nach den Suchbegriffen 1.4 vorschlagen (nur offizielle Websites, keine Verzeichnisse) und die Punkte der Prüfliste aus strategie.md 19 gegen die Primärquelle prüfen (Tabelle 19 in den Prompt übernehmen). Ernest liest das Ergebnis am So 11.10.",
    "2026-10-11": "ÄNDERUNG gegenüber dem Skelett: Die Zeile „Nur wenn Claude bis heute kein Netz hat …“ wird zu: „Fabrikliste freigeben: Hat Claudes Prüfung vom Sa 10.10. weniger als 8 brauchbare Fabriken ergeben, suchst du selbst die fehlenden (Suchbegriffe lieferanten.md 1.4, keine Verzeichnisse, keine Scraper) und prüfst sie nach 1.5“ (Kern 30′, +30′ Grind+ falls selbst suchen).",
}


def build_week(n, skel, r5, lib, prev_w, next_w):
    start = W1 + dt.timedelta(days=7 * (n - 1))
    end = start + dt.timedelta(days=6)
    L = [f"# Briefing Woche {n} · {start:%d.%m.}–{end:%d.%m.%Y} · {skel['phase']}",
         f"Ziel (Skelett): {skel.get('goal', '')}", ""]
    L.append("## KPI dieser Woche (Skelett)")
    for k in skel.get("kpi", []):
        L.append(f"- {k.get('k')}: {k.get('ziel')}")
    L.append("\n## Feste Termine (Skelett)")
    L += [f"- {x}" for x in skel.get("fix", [])]
    if skel.get("abhaengig"):
        L.append("\n## Setzt voraus (aus früheren Wochen)")
        L += [f"- {x}" for x in skel["abhaengig"]]
    if skel.get("neu_ggue_rev5"):
        L.append("\n## Neu gegenüber Rev. 5.3")
        L += [f"- {x}" for x in skel["neu_ggue_rev5"]]
    L.append("\n## SKELETT JE TAG (verbindlich, jeder Stichpunkt wird eine Aufgabe)")
    ids = set()
    for d, lines in sorted(skel["tage"].items()):
        dd = dt.date.fromisoformat(d)
        L.append(f"\n### {d} ({DN[dd.weekday()]})")
        if d in OVERRIDES:
            L.append(f"> {OVERRIDES[d]}")
        for x in lines:
            L.append(f"- {x}")
            ids.update(re.findall(r"\b(?:V\d{3}|CD-T\d{2})\b", x))
    if prev_w:
        L.append(f"\n## Vorwoche W{prev_w['n']} (nur Zusammenhang): {prev_w.get('goal', '')}")
        last = sorted(prev_w["tage"].items())[-1]
        L.append(f"Letzter Tag {last[0]}: " + " | ".join(last[1])[:900])
    if next_w:
        L.append(f"\n## Folgewoche W{next_w['n']} (nur Zusammenhang): {next_w.get('goal', '')}")
        L += [f"- {x}" for x in next_w.get("fix", [])]
    if r5:
        L.append("\n## Rev. 5.3 · alte Aufgaben dieser Woche (Material: gute Schritte und Prompts übernehmen und verbessern, Termine aus dem Skelett gelten)")
        for di, day in enumerate(r5["days"]):
            d = start + dt.timedelta(days=di)
            if d < dt.date(2026, 10, 8) or not day:
                continue
            L.append(f"\n### {d.isoformat()} ({DN[di]})")
            L += [fmt_r5_task(t) for t in day]
    vids = {v["id"]: v for v in lib.get("videos", [])}
    cds = {v.get("id"): v for v in lib.get("countdown", [])}
    hits = [vids.get(i) or cds.get(i) for i in sorted(ids)]
    hits = [h for h in hits if h]
    if hits:
        L.append("\n## Video-Konzepte dieser Woche (aus content_library.json; Korrekturen aus rules.md 9.3 gelten vor diesen Einträgen)")
        for h in hits:
            keep = {k: v for k, v in h.items() if k not in ("docket", "date_label")}
            L.append("```json\n" + json.dumps(keep, ensure_ascii=False, indent=1) + "\n```")
    missing = sorted(i for i in ids if not (vids.get(i) or cds.get(i)))
    if missing:
        L.append("\nNicht in der Bibliothek gefunden (in research/content.md mit grep suchen): " + ", ".join(missing))
    (OUT / f"w{n}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return len("\n".join(L))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    md, sec = strat()
    build_rules(md, sec)
    nlinks = build_links()
    skel = {w["n"]: w for w in json.loads((R6 / "skeleton.json").read_text(encoding="utf-8"))}
    r5 = {w["n"]: w for w in json.loads((ROOT / "r5" / "weeks_r5.json").read_text(encoding="utf-8"))}
    lib = json.loads((R6 / "research" / "content_library.json").read_text(encoding="utf-8"))
    sizes = {}
    for n in range(4, 33):
        sizes[n] = build_week(n, skel[n], r5.get(n), lib, skel.get(n - 1), skel.get(n + 1))
    print(f"rules.md {len((OUT / 'rules.md').read_text(encoding='utf-8'))} Zeichen · links.md {nlinks} Zeilen")
    print("Briefings:", " ".join(f"W{n}:{s // 1000}k" for n, s in sizes.items()))


if __name__ == "__main__":
    main()
