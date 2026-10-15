"""Erzeugt aus rewind_data.py die Docket-Aufgaben (extra.json) und die Tabelle für die Video-Bibel."""
import datetime as dt
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("d", HERE / "rewind_data.py")
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
V = sorted(d.V, key=lambda v: v["post"][0])
EXTRA = pathlib.Path(sys.argv[1])
WD = "Mo Di Mi Do Fr Sa So".split()


def de(iso):
    x = dt.date.fromisoformat(iso)
    return f"{WD[x.weekday()]} {x.day:02d}.{x.month:02d}."


def nr(v):
    return "#" + v["id"][1:]


LINKS = [{"n": "Video-Bibel", "u": d.BIBEL, "h": "Konzept, Trick, Sicherheit"},
         {"n": "CapCut", "u": d.CAPCUT, "h": "Rückwärts, Geschwindigkeit, Maske, Standbild"}]


def vblock(v, slot):
    return {"id": v["id"], "slot": slot, "dauer": v["dauer"], "plattform": "TikTok + Instagram Reels",
            "hook_en": v["hook_en"], "hook_de": v["hook_de"], "shots": v["shots"], "ort": v["ort"],
            "ton": v["ton"], "text": v["text"], "cta": "Warteliste: Link in der Bio, erster Kommentar angepinnt",
            "caption": v["caption"], "check": v["check"]}


def shoot_task(v):
    date, m = v["shoot"]
    steps = [f"Die Idee: {v['idee']}", f"Was du trägst: {v['kleidung']}."]
    steps += [f"Vorbereitung: {p}" for p in v["prep"]]
    steps += v["ablauf"]
    if v["safety"] != "—":
        steps.append(f"Sicherheit: {v['safety']}")
    if "edit" not in v:
        steps.append("Gleich danach schneiden: Signatur ans Ende (Rückspul-Geräusch, Hand gegen den Uhrzeigersinn, Endkarte TIME TRAVEL · 22.04.) und die 3 Frames mit dem Codewort.")
    t = {"c": "C", "t": f"Dreh · REWIND {nr(v)} „{v['name']}“ ({v['trick']})", "m": m, "s": steps,
         "f": "die Rohclips gesichert sind" + ("" if "edit" in v else " und der Schnitt fertig ist") + f" und der Check stimmt: {v['check']}.",
         "o": LINKS, "v": vblock(v, f"Post {de(v['post'][0])} {v['post'][1]}")}
    return date, t


def edit_task(v):
    date, m = v["edit"]
    return date, {"c": "C", "t": f"Schnitt · REWIND {nr(v)} „{v['name']}“", "m": m,
                  "s": ["Besten Take wählen, in CapCut: Clip → Rückwärts.", "Geschwindigkeit 1,5–2x, damit das Auto schnell wirkt. Prüfen: Wirkt nichts rückwärts (Passanten, Rauch, Haare)?",
                        "Hinweis „Reverse. Nobody was in danger.“ klein unten, Kennzeichen unscharf (Mosaik-Effekt mit Tracking).",
                        "Ton: Motor, Bass-Schlag auf dem Seitschritt. Signatur und 3 Frames Codewort ans Ende.",
                        "Einmal stumm und einmal mit 0,5x ansehen. Was dann auffällt, fällt auch Zuschauern auf.",
                        "Die Rohaufnahme behalten: Sie ist das Making-of."],
                  "f": "die Endfassung im Ordner liegt und der Check stimmt.", "o": LINKS}


def post_task(v):
    date, slot = v["post"]
    return date, {"c": "C", "t": f"{slot} · REWIND {nr(v)} „{v['name']}“ posten", "m": 15,
                  "s": ["Auf TikTok und als Reel posten, Caption aus dem Briefing.", "Ersten Kommentar anpinnen: Link zur Warteliste.",
                        "Wer das Codewort zuerst in die Kommentare schreibt, wird angepinnt." if v["id"] >= "R04" else "Kommentare mit „wie habt ihr das gemacht?“ sammeln, sie sind der Aufhänger fürs Making-of.",
                        "In den ersten 30 Minuten auf Kommentare antworten.", "Nach 48 Stunden Views, Anmeldungen und Codewort-Anmeldungen ins Blatt „Content“."],
                  "f": "das Video auf beiden Plattformen läuft und der Link-Kommentar angepinnt ist.",
                  "o": [LINKS[0]], "v": vblock(v, f"{de(date)} {slot}")}


def mo_task(v):
    date = v["mo"]
    return date, {"c": "C", "t": f"18:00 · Making-of REWIND {nr(v)} posten: Rohaufnahme neben Endfassung", "m": 20,
                  "s": ["Geteiltes Bild: oben die Rohaufnahme, unten die Endfassung, gleich lang.", "Text: „How we did it. Nobody was in danger.“",
                        "Auf die besten Fragen aus den Kommentaren antworten, eine davon als Video-Antwort."],
                  "f": "das Making-of läuft und auf das Original verweist.", "o": [LINKS[1]],
                  "v": {"id": v["id"] + "M", "slot": f"{de(date)} 18:00", "dauer": "15 s", "plattform": "TikTok + Instagram Reels",
                        "hook_en": "How we did it. Nobody was in danger.", "hook_de": "So haben wir's gemacht. Niemand war in Gefahr.",
                        "shots": ["Rohaufnahme oben", "Endfassung unten", "Endkarte"], "ort": "Schnitt, kein neuer Dreh",
                        "ton": "Originalton der Rohaufnahme, leiser Beat", "text": "„RAW“ oben, „FINAL“ unten",
                        "cta": "Original-Video verlinken", "caption": f"Behind Rewind {nr(v)}. The car only drove backwards." if v["id"] in ("R01", "R11") else f"Behind Rewind {nr(v)}.",
                        "check": "Rohaufnahme zeigt klar, dass niemand in Gefahr war"}}


OTHER = [
    ("2026-10-19", {"c": "B", "t": "Knopf mit Achtstern: Preis und Mindestmenge bei den Fabriken erfragen (Skizze 15.10.)", "m": 10,
                    "s": ["In die Rückfragen zu den Angeboten von heute diesen Satz aufnehmen (Englisch):",
                          "„Can you supply a custom jeans shank button with our own embossed eight-pointed star (artwork follows), same metal finish as the rivets? Please quote MOQ, price per piece and the one-time die cost.“",
                          "Antworten in den Vergleich: Mindestmenge, Stückpreis, Werkzeugkosten. Bis 100 Stück und unter 1 € pro Paar plus Werkzeug: ja."],
                    "f": "die Frage an alle Fabriken mit Angebot raus ist.",
                    "o": [{"n": "Gmail", "u": "https://mail.google.com"}]}),
    ("2026-10-20", {"c": "D", "t": "Fragen zu deinen Skizzen vom 15.10. entscheiden", "m": 15,
                    "s": ["Jeans: Was sind die Punkte vorn am linken Bein? Sind es Stoppeln vom alten Serp, sind sie am 11.10. mitgestrichen.",
                          "Jeans: Patch D rechts neben der Mittelnaht, wie auf der Skizze? Und „NL“ auf dem Patch: ja oder nein?",
                          "Zipper-Anhänger: Achtstern-Anhänger zum Einhaken am normalen Zipper (Rat), eigener Metall-Zipper erst ab Drop 2.",
                          "Zipper im Juni: am Drop mitverkaufen oder als Herbst-Drop im September? Rat: zeigen und vorbestellen lassen, die Hauptsaison ist der Herbst.",
                          "Polo: Was ist das kleine Brustmotiv? Kragen und Bündchen gestickt oder als eigenes Webband (Rat: zuerst am Muster sticken, Webband nur bei Mindestmenge bis 100 m)?",
                          "Alles in einer Zeile an Claude, dann Blatt „Entscheidungen“."],
                    "f": "alle fünf Fragen beantwortet im Blatt „Entscheidungen“ stehen.",
                    "o": [{"n": "Google Sheets · „Time Travel Tracking“", "u": "https://sheets.google.com", "h": "Blatt „Entscheidungen“"}]}),
    ("2026-10-23", {"c": "A", "t": "Datenschutzerklärung ergänzen: Tally und „Bring 3“ (verschoben vom 13. und 15.10.)", "m": 20,
                    "s": ["e-recht24-Generator öffnen, Tally als Dienst ergänzen. Fehlt Tally dort, nimmst du Claudes Absatz vom 13.10.",
                          "Claudes Satz zu Quellen-Tags und Empfehlungs-Code (Chat R1 vom 14.10.) dazu.",
                          "Shopify → Onlineshop → Seiten → Datenschutz: beide Absätze einfügen, speichern.",
                          "Erst jetzt freischalten: Tally-Link als zweiten Link in die Instagram-Bio, „Bring 3“-Link in die Willkommens-Mail."],
                    "f": "beide Absätze online sind, der Tally-Link in der Bio steht und „Bring 3“ in der Willkommens-Mail ist.",
                    "o": [{"n": "Shopify-Admin", "u": "https://admin.shopify.com", "h": "Onlineshop → Seiten → Datenschutz"},
                          {"n": "e-recht24 Datenschutz-Generator", "u": "https://www.e-recht24.de", "h": "Generator für die Datenschutzerklärung"}]}),
    ("2026-11-11", {"c": "A", "t": "Feld „Codewort aus dem Video“ ins Wartelisten-Formular", "m": 10,
                    "s": ["Im selben Formular wie die Größen- und Quellen-Tags ein freiwilliges Feld „Codewort aus dem Video“ ergänzen. Claude schreibt dir den Code-Schnipsel.",
                          "Gespeichert wird es als Tag „rw-[Codewort]“, z. B. „rw-rw04“.",
                          "Test mit einer Testadresse, Tag beim Kunden prüfen.",
                          "Ab REWIND #04 (Di 17.11.) zählt jedes Codewort im Cockpit für sein Video."],
                    "f": "der Test-Kunde den Tag „rw-test“ hat.",
                    "p": "Projekt Time Travel, Docket W9, Mi 11.11. Ich habe heute das Wartelisten-Formular mit Größen- und Quellen-Tags gebaut. Schreib mir den kleinsten Code-Schnipsel für ein freiwilliges Feld „Codewort aus dem Video“, das als Kunden-Tag „rw-[Wort in Kleinbuchstaben]“ gespeichert wird. Mit Testschritten.",
                    "o": [{"n": "Shopify-Admin", "u": "https://admin.shopify.com", "h": "Onlineshop → Themes → Code bearbeiten"}]}),
]


def main():
    extra = json.loads(EXTRA.read_text(encoding="utf-8"))
    for k in list(extra):
        extra[k].pop("append", None)
        if not extra[k]:
            del extra[k]
    items = []
    for v in V:
        items.append(shoot_task(v))
        if "edit" in v:
            items.append(edit_task(v))
        items.append(post_task(v))
        if "mo" in v:
            items.append(mo_task(v))
    items += OTHER
    for date, t in items:
        extra.setdefault(date, {}).setdefault("append", []).append(t)
    EXTRA.write_text(json.dumps(dict(sorted(extra.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(len(items), "Aufgaben in", len({x for x, _ in items}), "Tagen")

    rows = ["| # | Video | Trick | Was passiert | Hook | Dreh | Post |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for v in V:
        name = f"**{v['name']}**" if v["top"] else v["name"]
        mo = f" · Making-of {de(v['mo'])}" if "mo" in v else ""
        rows.append(f"| {v['id'][1:]} | {name} | {v['trick']} | {v['idee']} Du trägst: {v['kleidung']}. | {v['hook_en']} | {de(v['shoot'][0])} | {de(v['post'][0])} {v['post'][1]}{mo} |")
    (HERE / "s5_table.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    json.dump([{"key": v["id"], "name": v["name"], "post": v["post"][0], "phase": v["phase"], "top": v["top"]} for v in V],
              open(HERE / "timeline.json", "w", encoding="utf-8"), ensure_ascii=False)


main()
