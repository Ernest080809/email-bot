"""Baut die Referenz- und Analyse-Abschnitte des Docket Rev. 6 aus Strategie und Recherche.

Aufruf: python3 rev6/build/refs6.py
Schreibt rev6/ref/*.html, rev6/ref/order.json, rev6/build/zielgruppe.html, rev6/build/design.html.
Quelle der Wahrheit ist rev6/strategie.md; wo eine Recherche-Datei abweicht, steht ein Hinweis davor.
"""
import datetime as dt
import html
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R6 = ROOT / "rev6"
RS = R6 / "research"
REF = R6 / "ref"
BUILD = R6 / "build"
_pid = [0]
sys.path.insert(0, str(BUILD))
from build6 import human  # noqa: E402  (gleiche Verweis-Umschreibung wie im Tagesplan)


def read(p):
    return pathlib.Path(p).read_text(encoding="utf-8")


def secs(md, level=2):
    pat = re.compile(r"^(#{%d}) (\S+) · .*$" % level, re.M)
    hits = list(pat.finditer(md))
    out = {}
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(md)
        out[m.group(2)] = md[m.start():end].rstrip()
    return out


def pick(md, start, stop=None):
    """Textblock ab einer Zeile, die mit `start` beginnt, bis vor `stop`."""
    a = re.search(r"^" + re.escape(start), md, re.M)
    if not a:
        raise SystemExit(f"Abschnitt nicht gefunden: {start}")
    rest = md[a.start():]
    if stop:
        b = re.search(r"^" + re.escape(stop), rest[1:], re.M)
        if b:
            return rest[:b.start() + 1].rstrip()
    return rest.rstrip()


CLAUDE_NET = [
    (r"\s*\(ohne Netz: 4 weitere selbst suchen\)", ""),
    (r"So 11\.10\. \(60′, nur wenn Claude kein Netz hat\)", "So 11.10. (60′, nur wenn die Fabrikliste unter 8 bleibt)"),
    (r"\*\*Selbst geprüft in dieser Aufgabe: 0\.\*\*[^\n]*?Die folgenden Quellen",
     "**Prüfstand:** Die Recherche vom 07.10.2026 hat diese Quellen per Websuche gefunden, meist als Suchauszug. Vor jeder Ausgabe, jeder rechtlichen Umsetzung und jedem Besuch öffnest du die Quelle selbst. Angaben ohne Primärquelle sind im Docket als „ungeprüft“ markiert. Die folgenden Quellen"),
    (r"\((?:[A-Za-z-]*[Ss]eite )?(?:`[^`]*` )?am 07\.10\. (?:für content\.md )?gesperrt(?:, nicht geöffnet)?\)", "(ungeprüft)"),
    (r"\*\*Keine davon habe ich in dieser Runde geöffnet\*\* \(Proxy gesperrt\)\. Die Domains sind große, bekannte Anbieter\. Pfade unterhalb der Startseite gebe ich nur an, wenn ich sie versucht habe \(dann steht „gesperrt“ dabei\) oder eine andere Recherche von heute sie gesehen hat\.",
     "**Keine davon ist geprüft.** Die Domains sind große, bekannte Anbieter. Öffne die Seite selbst, bevor du Geld ausgibst."),
    (r"\s*\(Proxy gesperrt\)", ""),
    (r"Offizielle Website von hier gesperrt", "Offizielle Website selbst prüfen"),
    (r"konnte ich heute nicht sehen, die Seiten waren gesperrt\.", "sind nicht geprüft."),
    (r", Seite gesperrt", ""),
    (r"\(ascolour\.eu war gesperrt, Existenz nicht geprüft\)", "(Domain nicht geprüft)"),
    (r"Die offizielle Website des Fashion Council Germany war für mich gesperrt", "Die offizielle Website des Fashion Council Germany ist noch zu prüfen"),
    (r"Die Shopify-Hilfe dazu war in dieser Sitzung gesperrt\.", "Die Shopify-Hilfe dazu ist noch nicht geprüft."),
    (r"\[technisch zu prüfen, die Shopify-Dokumentation war heute gesperrt\]", "[technisch zu prüfen]"),
    (r"Die Seiten von BGH und Medienanstalten waren heute gesperrt\. ", ""),
    (r"Die Seiten selbst waren für mich gesperrt, das Datum steht dabei, wenn bekannt\.", "Vor jedem Besuch selbst prüfen. Das Datum steht dabei, wenn bekannt."),
]


def md2html(md, shift=1, key="x"):
    for a, b in CLAUDE_NET:
        md = re.sub(a, b, md)
    md = human(md)
    out = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"], input=md, capture_output=True, text=True, check=True).stdout
    out = re.sub(r'<(h[1-6]) id="[^"]*"', r"<\1", out)

    def hshift(m):
        lvl = min(6, int(m.group(2)) + shift)
        return f"<{m.group(1)}h{lvl}"
    out = re.sub(r"<(/?)h([1-6])", hshift, out)
    out = re.sub(r"<colgroup>.*?</colgroup>", "", out, flags=re.S)
    out = re.sub(r'<tr class="[^"]*">', "<tr>", out)
    out = re.sub(r'<(td|th) style="text-align: (?:left|center)[^"]*;?">', r"<\1>", out)
    out = re.sub(r'<(td|th) style="text-align: right;?">', r'<\1 class="num">', out)
    out = re.sub(r"<table>", '<div class="tablewrap"><table>', out)
    out = re.sub(r"</table>", "</table></div>", out)
    out = re.sub(r'<a href="(https?://[^"]+)"', r'<a class="lnk" href="\1" target="_blank" rel="noopener"', out)

    def pre(m):
        _pid[0] += 1
        pid = f"{key}_c{_pid[0]}"
        body = m.group(2)
        return (f'<div class="prompt"><div class="ph"><span class="eyebrow">Zum Kopieren</span>'
                f'<button type="button" data-copy="{pid}">Kopieren</button></div>'
                f'<pre class="code" id="{pid}">{body}</pre></div>')
    out = re.sub(r'<pre(?: class="[^"]*")?><code(?: class="[^"]*")?>(\s*)(.*?)</code></pre>', lambda m: pre(m), out, flags=re.S)
    return out


def block(rid, title, inner, pill="Neu Rev. 6"):
    p = f' <span class="pill ok" style="font-size:9.5px">{pill}</span>' if pill else ""
    return (f'<details class="ref" id="{rid}"><summary><span class="chev"></span>{html.escape(title)}{p}</summary>'
            f'<div class="inner">{inner}</div></details>')


def callout(eyebrow, text, kind=""):
    k = f" {kind}" if kind else ""
    return f'<div class="callout{k}"><span class="eyebrow">{html.escape(eyebrow)}</span><p>{text}</p></div>'


MARKERS = callout("So liest du die Kürzel", "[P] Plan Rev. 5.3 · [S] Spec Rev. 13 · [Ü] Übergabe · [M-Q…] Markt-Recherche · [Z-Q…] Zielgruppe · [B-…] Berlin · [C] Creator/Community · [K] Content · [W] Website · [T] Tools · [L] Lieferanten · [D] Design · [R] eigene Rechnung. <b>Schätzung</b> = Annahme · <b>vor Ort prüfen</b> = selbst nachsehen · <b>ungeprüft</b> = noch ohne Primärquelle. Alle Quellen stehen im Abschnitt „Quellen“.", "plain")


def video_table(lib):
    rows = []
    for v in lib["videos"]:
        d = v.get("date") or ""
        dl = dt.date.fromisoformat(d).strftime("%d.%m.%y") if d else "Reserve"
        rows.append((v["id"], dl, v.get("slot", ""), v.get("hook_en", ""), v.get("hook_de", ""), v.get("ort", "")))
    for v in lib["countdown"]:
        d = v.get("date") or ""
        dl = dt.date.fromisoformat(d).strftime("%d.%m.%y") if d else ""
        rows.append((v["id"], dl, "COUNTDOWN", v.get("hook_en", ""), v.get("hook_de", ""), v.get("ort", "")))
    h = ['<div class="tablewrap"><table><thead><tr><th>ID</th><th>Datum</th><th>Slot</th><th>Hook (EN)</th><th>Hook (DE)</th><th>Drehort</th></tr></thead><tbody>']
    for r in rows:
        h.append("<tr>" + "".join(f"<td>{html.escape(str(x))}</td>" for x in r) + "</tr>")
    h.append(f'</tbody><caption>{len(rows)} Konzepte. Das vollständige Briefing (Shots, Ton, Caption) steht im Tagesplan am Dreh- und am Posttag. Suche oben im Tagesplan nach der ID. Die Korrekturen aus den Content-Regeln (Wortliste, CTA, Bildregeln, Sperrtermine) gelten vor der Bibliothek.</caption></table></div>')
    return "".join(h)


def zeitachse():
    skel = json.loads(read(R6 / "skeleton.json"))
    h = ['<p class="intro">Die festen Termine je Woche aus dem Tagesplan. Verschiebt sich einer, schreib es Claude, dann wird der Rest neu geschnitten.</p>',
         '<div class="tablewrap"><table><thead><tr><th>Woche</th><th>Zeitraum</th><th>Feste Termine und Gates</th></tr></thead><tbody>']
    for w in skel:
        s = dt.date.fromisoformat(w["start"])
        e = s + dt.timedelta(days=6)
        fx = "<br>".join(html.escape(x) for x in w.get("fix", []))
        h.append(f'<tr><td class="mono">W{w["n"]} · {w["phase"]}</td><td class="mono">{s:%d.%m.}–{e:%d.%m.%y}</td><td>{fx}</td></tr>')
    h.append("</tbody></table></div>")
    return "".join(h)


R5_NOTE = {
    "vorlagen": "Die Vorlage „RFQ Jeansfabrik“ ist auf den Freeze vom 11.10. umgestellt (Serp gestrichen, 4 Stickzonen, ~28.000 Stiche, Patch D als Gürtelschlaufe). In Rev. 6 gilt zusätzlich: nach außen „Kreuzstich-Band“ statt „Vyshyvanka“, „Achtstern“ statt „Alatyr“, „Time Travel“ statt „Projekt Slavic“. Lieferzeile überall: „Lieferung bis spätestens 30.04.2027, geplant Anfang April“. CTA je Phase aus den Content-Regeln. Neue Vorlagen für Netz, Abende, Creator und Presse stehen im Abschnitt „Warteliste, Netz, Creator, Presse“.",
    "pruefplan": "Stand Rev. 5.3. In Rev. 6 kommen dazu: Weiß nach der Wäsche L* ≥ 80, Patch D 76 × 67 mm als Gürtelschlaufe mit Zugtest, Goldfäden-Test am PP (anziehen, sitzen, fünf Wäschen auf links).",
    "kalk": "Stand Rev. 5.3. In Rev. 6 gilt: Stufe 2 (Nr. 036–060 zu 169 €) statt Kontingent 45. Bei Türkei und Kleinunternehmer ~1.150 € Einfuhrumsatzsteuer: Schwelle 2b = 40 ausgezahlte Vorbestellungen bis Mi 24.03. Details im Abschnitt „Strategie“.",
    "techpack": "Stand Rev. 5.3. Zusätze aus Rev. 6 (falls beim Freeze angenommen): 2 mm Denim zwischen Band A und Kante · Weiß nach der Wäsche L* ≥ 80 · Anti-Backstaining-Frage · Schlaufen ≥ 8 mm vom Patch · GPSR-Herstellerangabe aufs Pflegeetikett · Verschleißkarte mit Freihaltezonen · Wash Reference Sheet · Stichdeckel 33.000, Füllung als Standard · REACH-Bestätigung für Knopf, Nieten und Farbstoffe.",
}


def r5_block(rid):
    b = read(BUILD / f"r5_ref_{rid}.html")
    note = callout("Hinweis Rev. 6", html.escape(R5_NOTE[rid]))
    return b.replace('<div class="inner">', '<div class="inner">' + note, 1)


def main():
    REF.mkdir(exist_ok=True)
    st = read(R6 / "strategie.md")
    S = secs(st, 2)
    lib = json.loads(read(RS / "content_library.json"))
    zg, ds, be, to, li, co, we, ct, mk = (read(RS / f"{n}.md") for n in ("zielgruppe", "design", "berlin", "tools", "lieferanten", "community", "website", "content", "markt"))
    ZG, DS, BE, TO, LI, CO, WE, CT, MK = (secs(x) for x in (zg, ds, be, to, li, co, we, ct, mk))

    def jn(*parts):
        return "\n\n".join(parts)

    refs = []
    refs.append(("zeit.html", block("zeit", "Zeitachse · feste Termine je Woche", zeitachse())))
    refs.append(("strategie.html", block("strategie", "Strategie · Kernthese, Funnel, Hebel", MARKERS + md2html(jn(S["2"], S["3"], S["5"], S["8"]), key="st"))))
    refs.append(("gates.html", block("gates", "Wochenziele, Gates, Notfall-Leiter", md2html(jn(S["6"], S["7"]), key="ga"))))
    refs.append(("content.html", block("content", "Content-System und Video-Bibliothek",
                 md2html(S["9"], key="co") + "<h3>Plattform, Formate, Workflow, Messen (Recherche)</h3>" +
                 md2html(jn(CT["1"], CT["2"], CT["4"], CT["5"]), shift=2, key="ct") +
                 "<h3>Video-Bibliothek</h3>" + video_table(lib))))
    refs.append(("berlin.html", block("berlin", "Berlin · Orte, Märkte, Abende, Drehorte",
                 md2html(S["10"], key="be1") + "<h3>Alle Orte aus der Recherche</h3>" +
                 callout("Vor jedem Besuch", "Adressen, Öffnungszeiten und Preise stammen aus Suchtreffern vom 07.10.2026. Vor jedem Besuch die Website oder Google Maps selbst öffnen.", "plain") +
                 md2html(jn(*(BE[k] for k in ("0", "1", "2", "3", "4", "5", "6", "7"))), shift=2, key="be"))))
    refs.append(("creator.html", block("creator", "Warteliste, Netz, Creator, Presse, Abende",
                 md2html(S["11"], key="cr1") + "<h3>Details aus der Recherche</h3>" +
                 md2html(jn(pick(co, "### 1.2", "## 2"), *(CO[k] for k in ("2", "3", "4", "5", "6", "7"))), shift=2, key="cr"))))
    refs.append(("website.html", block("website", "Website · Scroll-Story und Pixel-Spiel, kompletter Bauplan",
                 callout("Erst lesen", "Die Korrekturen aus der Strategie (Abschnitt 13, direkt hier drunter) gelten vor dem Bauplan der Recherche. Vor allem: „Stufe 2“ heißt die Preisstufe zu 169 €, und das Kontingent 45 gibt es nicht mehr.") +
                 md2html(S["13"], key="we1") + "<h3>Der komplette Bauplan</h3>" +
                 md2html(jn(*(WE[k] for k in ("2", "3", "4", "5", "6", "7", "8", "9"))), shift=2, key="we"))))
    refs.append(("tools.html", block("tools", "Tools, Websites, Recht, Steuer, Versand",
                 md2html(jn(*(TO[k] for k in ("0", "1", "2", "3", "4", "5", "6"))), key="to"))))
    refs.append(("fabriken.html", block("fabriken", "Fabriken und Lieferanten",
                 callout("Nichts davon ist geprüft", "Fähigkeiten, MOQ und Kontaktwege stammen aus Suchtreffern. Vor jeder Anfrage öffnest du die Website der Fabrik selbst und prüfst sie nach der Prüfliste (1.5). Kontakt nur über die offizielle Seite.", "bad") +
                 md2html(jn(*(LI[k] for k in ("1", "2", "3", "4", "6"))), key="li"))))
    refs.append(("markt.html", block("markt", "Markt, Wettbewerb, Benchmarks",
                 md2html(jn(*(MK[k] for k in ("1", "2", "4", "5"))), key="mk"))))
    for rid in ("vorlagen", "pruefplan", "kalk", "techpack"):
        refs.append((f"{rid}.html", r5_block(rid)))
    refs.append(("risiken.html", block("risiken", "Risiken und Gegenmaßnahmen", md2html(S["16"], key="ri"))))
    refs.append(("aenderungen.html", block("aenderungen", "Was sich gegenüber Rev. 5.3 ändert", md2html(pick(st, "## 15 ·", "### 15.1"), key="ae"))))
    refs.append(("quellen.html", block("quellen", "Quellen", md2html(S["18"], key="qu"), pill="")))
    for name, frag in refs:
        (REF / name).write_text(frag, encoding="utf-8")
    (REF / "order.json").write_text(json.dumps([n for n, _ in refs], ensure_ascii=False), encoding="utf-8")

    # Zielgruppe (oben im Docket)
    zg_main = md2html(jn(S["4"]), key="zs")
    zg_main += "<h3>Wer die ersten 35 kauft</h3>" + md2html(ZG["4"], shift=2, key="zp")
    zg_main += "<h3>Die Personas</h3>" + md2html(ZG["2"], shift=2, key="zq")
    zg_main += "<h3>Was verbindet, was trennt · Do und Don't</h3>" + md2html(jn(pick(zg, "### 3.2", "### 3.4"), pick(zg, "### 3.6", "### 3.7")), shift=1, key="zd")
    zg_more = md2html(jn(ZG["0"], ZG["1"], pick(zg, "### 3.1", "### 3.2"), pick(zg, "### 3.4", "### 3.6"), pick(zg, "### 3.7", "## 4"), ZG["5"]), key="zm")
    zg_main += block("zielgruppe-voll", "Die ganze Zielgruppenanalyse · Segmente, Zahlen, Symbol-Check, Tests", zg_more, pill="")
    (BUILD / "zielgruppe.html").write_text(zg_main, encoding="utf-8")

    # Design (oben im Docket)
    d_main = read(BUILD / "entscheidung_1110.html") + md2html(S["12"], key="ds1")
    d_main += "<h3>Papiertest 3 · Do 08.10. · Protokoll</h3>" + md2html(DS["4"], shift=1, key="dp")
    d_more = md2html(jn(DS["1"], DS["2"], DS["3"], DS["5"], DS["6"]), key="dm")
    d_main += block("design-voll", "Das ganze Design-Review · Stärken, Risiken, sechs Vorschläge, Lookbook", d_more, pill="")
    (BUILD / "design.html").write_text(d_main, encoding="utf-8")

    # Urteil (oben im Docket): handgeschriebener Kopf + Entscheidungen aus Strategie 17
    dec = re.sub(r"^## 17 · .*\n", "", S["17"])
    urteil = read(BUILD / "entscheidung_1110.html") + read(BUILD / "urteil_head.html") + "<h3 style=\"font-family:'Anton',sans-serif;font-weight:400;text-transform:uppercase;font-size:20px;margin:28px 0 10px\">Deine Entscheidungen mit Datum</h3>" + md2html(dec, key="ur")
    (BUILD / "urteil.html").write_text(urteil, encoding="utf-8")

    sizes = {n: len(f) for n, f in refs}
    print("Referenzen:", ", ".join(f"{n} {s // 1000}k" for n, s in sizes.items()))
    print("Zielgruppe", len(zg_main) // 1000, "k · Design", len(d_main) // 1000, "k")


if __name__ == "__main__":
    main()
