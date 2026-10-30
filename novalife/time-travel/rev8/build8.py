# -*- coding: utf-8 -*-
"""Docket Rev. 8 als eine HTML-Seite: python3 build8.py <ausgabe.html>"""
import html, json, os, sys
import plan8 as P
from lib8 import dl

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'time_travel_docket_rev8.html')
E = html.escape
OLDDONE = json.load(open(os.path.join(HERE, 'old_done.json'), encoding='utf-8'))

NT = sum(1 for w in P.WEEKS for d in w['days'] for t in d if t['c'] != 'N')
NS = len(P.content8.STUNTS)
NPOST = len(P.content8.CPLAN)


def js(x):
    return json.dumps(x, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


PATH = [("Do 05.11.", "Fabrik entschieden", "schriftlicher Preis von Kuzgunlar"),
        ("Mo 09.11.", "Unterlagen bei Kuzgunlar", "Tech Pack, Maßblätter, Farbcodes, Patch D"),
        ("Di 24.11.", "Gate: gewaschene Stickprobe", "sonst wird das Proto später"),
        ("Do 10.12.", "Proto da", "erst dann wird öffentlich gepostet"),
        ("Di 15.12.", "Erster Post", "V201, dann zwei Posts pro Woche"),
        ("Mo 21.12.", "REWIND #01 · G-Klasse", "Dreh in den Ferien, Post Sa 26.12."),
        ("Fr 15.01.", "GATE Muster-Freigabe", "erst danach Gewerbe, Recht, Shop"),
        ("Mo 18.01.", "Gewerbe", "dann Steuer, Rechtstexte, Zahlung, LUCID"),
        ("Mo 15.02.", "Vorbestellung öffnet", "18:00 die Liste, 19:00 alle, mit REWIND #11"),
        ("So 14.03.", "GATE Bestellmenge", "100, 75 oder Notfall-Regel"),
        ("Mo 15.03.", "Serie bestellt", "50 % Anzahlung aus deinem Budget"),
        ("22.03.–09.05.", "Abi-Pause", "5 Posts laufen automatisch"),
        ("Fr 14.05.", "Endkontrolle und Restzahlung", "nie vor der Kontrolle zahlen"),
        ("Mi 26.05.", "Vorbestellungen unterwegs", "Versandweg vom 13.11."),
        ("Do 24.06., 19:00", "DROP", "Ziel: alle 100 Paare bis 31.08.")]
TIME = [("Fabrik und Design fertig", "30.10.–13.12.", "1,5–2,5 h", "Entscheidungen und Prüfungen, nichts posten"),
        ("Öffentlich mit dem Proto", "14.12.–17.01.", "2–4,5 h", "zwei Posts pro Woche, Stunts in den Ferien"),
        ("Gewerbe, Recht, Shop, Vorbestellung", "18.01.–21.03.", "3–5 h", "die vollste Phase, Claude schreibt alle Texte vor"),
        ("Abi-Pause", "22.03.–09.05.", "0 h", "optional 10 Minuten am Sonntag"),
        ("Endspurt und Drop", "10.05.–27.06.", "3–7 h", "drei Posts pro Woche, Countdown, Drop")]

head = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Time Travel Docket</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@400;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap">
<style>{open(os.path.join(HERE, 'docket8.css'), encoding='utf-8').read()}</style></head><body><div class="wrap">"""

top = f"""<header class="top"><span class="eyebrow">Drop Docket · Rev. 8 · 30.10.2026</span><h1>Time Travel</h1>
<p class="sub">100 nummerierte Jeans · Vorbestellung ab Mo 15.02.2027 · Drop Do 24.06.2027, 19:00</p>
<div class="cd"><div><div class="big" id="cdDays">–</div><div class="lbl">Tage bis zum Drop</div></div>
<div><div class="big" style="font-size:32px" id="weekOf">–</div><div class="lbl">{len(P.WEEKS)} Wochen, {NT} Aufgaben</div></div>
<div class="bar"><div class="tr"><div class="fl" id="megaBar"></div></div><div class="lbl mono"><span id="megaCount">–</span><span id="megaPct">–</span></div></div></div>
<div id="saveNote"></div></header>
<nav class="nav" aria-label="Abschnitte"><a href="#heute">Heute</a><a href="#plan">Plan</a><a href="#wochen">Wochen</a><a href="#stunts">Stunts</a><a href="#content">Content</a><a href="#mails">Mails</a><a href="#zahlen">Zahlen</a><a href="#erledigt">Erledigt</a><a href="#offen">Offen</a></nav>"""

legend = '<div class="legend">' + "".join(f'<span class="tg {k}">{v}</span>' for k, v in [("B", "FABRIK"), ("G", "DESIGN"), ("D", "ENTSCHEIDUNG"), ("S", "STUNT"), ("C", "CONTENT"), ("V", "VERKAUF"), ("R", "RECHT"), ("W", "SHOP"), ("A", "ADMIN")]) + '</div>'

heute = f"""<section id="heute"><div class="sechead"><span class="n">01</span><h2>Heute</h2><span class="note">Die nächsten drei Tage mit Aufgaben. Häkchen werden gespeichert und gelten überall auf der Seite.</span></div>
{legend}<div class="today" id="todayList"></div></section>"""

plan = f"""<section id="plan"><div class="sechead"><span class="n">02</span><h2>Der Plan</h2><span class="note">Neu aufgesetzt am Fr 30.10. nach deinen Antworten.</span></div>
<div class="callout"><span class="eyebrow">Was sich gegenüber Rev. 7 ändert</span><ul>
<li><b>Öffentlich erst mit dem echten Paar.</b> Der erste Post ist am Di 15.12., wenn das Proto da ist. Bis dahin baust du nur vor.</li>
<li><b>Erst Design und Fabrik, dann der Rest.</b> Gewerbe, Steuer, Rechtstexte und Shop starten am Mo 18.01., nach der Muster-Freigabe, so wie du es am 17.10. wolltest. Eine Ausnahme: Impressum und Datenschutz auf der Warteliste vor dem ersten Post, sonst droht eine Abmahnung.</li>
<li><b>Vorbestellung ab Mo 15.02.</b> statt 01.02. Der Drop bleibt Do 24.06., 19:00.</li>
<li><b>Für 3–5 Stunden pro Woche gebaut.</b> {NT} Aufgaben statt 824, {NPOST} Posts statt 164. Bis zur Abi-Pause zwei Posts pro Woche, jeder zweite ein Stunt.</li>
<li><b>{NS} Stunt-Videos (REWIND)</b> mit eigener Farbe, eigenem Abschnitt und vollem Briefing. Die G-Klasse ist #01 in den Weihnachtsferien und #11 zum Start der Vorbestellung.</li>
<li><b>Keine „Zusagen“ mehr.</b> Gezählt werden nur Follower, Warteliste und bezahlte Vorbestellungen, mit Zielen, die zu deinem Start bei 170 Followern passen.</li>
<li><b>September und Oktober</b> stehen nur noch unter „Erledigt“. Alle 43 Häkchen sind dort erhalten.</li></ul></div>
<div class="callout crit"><span class="eyebrow">Mein Urteil</span>
<p>Der Plan ist machbar. Aber nur, wenn zwei Dinge halten, die du nicht ganz in der Hand hast.</p><ul>
<li><b>Die Fabrik.</b> Alles hängt am Proto am Do 10.12. Kommt es drei Wochen später, rutschen Freigabe, Gewerbe und Vorbestellung mit. Darum fragt Claude bei jedem Schritt schriftlich nach Terminen.</li>
<li><b>Ein Stunt muss zünden.</b> Mit zwei Posts pro Woche kommst du nur auf 120 Leute auf der Liste, wenn mindestens ein Video das Doppelte deines Medians schafft. Darum stehen die stärksten Stunts (G-Klasse, 8 Handys, 20 kg) in den Ferien, wo du Zeit hast.</li>
<li><b>Geld.</b> Die Anzahlung der Serie (50 %) zahlst du aus deinen 4.500 €. Für die Restzahlung im Mai brauchst du etwa 22 bezahlte Vorbestellungen. Das ist ehrgeizig, aber realistisch. Reicht es nicht, gilt die Notfall-Regel unten.</li></ul></div>
<h3>Der kritische Pfad</h3><div class="tablewrap"><table><thead><tr><th>Wann</th><th>Was</th><th>Warum es zählt</th></tr></thead><tbody>
{"".join(f"<tr><td class='mono'>{E(a)}</td><td><b>{E(b)}</b></td><td>{E(c)}</td></tr>" for a, b, c in PATH)}</tbody></table></div>
<h3>Deine Zeit</h3><div class="tablewrap"><table><thead><tr><th>Phase</th><th>Wann</th><th>Pro Woche</th><th>Was du machst</th></tr></thead><tbody>
{"".join(f"<tr><td><b>{E(a)}</b></td><td class='mono'>{E(b)}</td><td class='mono'>{E(c)}</td><td>{E(d)}</td></tr>" for a, b, c, d in TIME)}</tbody></table></div>
<p>Kommentare beantworten, Storys und Mess-Abende sind nicht eingeplant. Wenn du Zeit übrig hast, sind sie das Beste, was du mit ihr machen kannst.</p>
<h3>Notfall-Regel</h3><div class="callout"><ul>
<li><b>Bestellmenge am So 14.03.:</b> 20 oder mehr bezahlte Vorbestellungen → 100 Paar. 10 bis 19 → 75 Paar. Unter 10 → du entscheidest mit Claude: 50 Paar aus eigenem Geld (wenn Kuzgunlar die Menge macht), oder der Drop rückt in den September und jeder Vorbesteller kann sein Geld zurück.</li>
<li><b>Restzahlung am Fr 14.05.:</b> Reicht das Geld nicht, in dieser Reihenfolge: Stufe 2 zu 169 € früher öffnen, Familie fragen, Teillieferung mit Kuzgunlar verhandeln.</li>
<li><b>Nie:</b> vor der Endkontrolle zahlen, den Vorbestellpreis über den 23.05. verlängern, „ausverkauft“ melden, wenn es nicht stimmt.</li></ul></div></section>"""

wochen = f"""<section id="wochen"><div class="sechead"><span class="n">03</span><h2>Woche für Woche</h2><span class="note">Die laufende Woche ist offen. „So geht’s“ zeigt Schritte, Links und das Video-Briefing.</span></div>
<div class="tools"><input type="search" id="wq" placeholder="Suchen: Kuzgunlar, G-Klasse, Gewerbe, V201 …" aria-label="Aufgaben durchsuchen"><label><input type="checkbox" id="wopen"> nur offene</label><span class="hits" id="whits"></span></div>
<div id="weekList"></div></section>"""

stunts = f"""<section id="stunts"><div class="sechead"><span class="n">04</span><h2>Stunt-Videos · REWIND</h2><span class="note">{NS} Videos aus deiner Idee vom 13.10. Jedes spielt mit der Zeit und endet auf der Jeans.</span></div>
<div class="callout crit"><span class="eyebrow">Sicherheit, für jeden Stunt</span><ul>
<li>Auto nur auf privatem, abgesperrtem Gelände mit Erlaubnis. Dein Vater fährt, nur rückwärts von dir weg, Schritttempo. Ein Aufpasser steht außerhalb der Strecke.</li>
<li>Im Bild steht „Reverse. Nobody was in danger.“, zu jedem großen Stunt kommt ein Making-of.</li>
<li>Keine Drehs in U-Bahn und S-Bahn ohne Erlaubnis, keine Drohne über der Innenstadt, Kennzeichen unscharf, fremde Gesichter nur mit Ja.</li></ul>
<p>Mehr dazu in der <a href="https://claude.ai/artifact/UEvQ2PrfHn8rwmujfURiTW" target="_blank" rel="noopener">Video-Bibel</a>.</p></div>
<div class="stunts" id="stuntList"></div></section>"""

content = f"""<section id="content"><div class="sechead"><span class="n">05</span><h2>Content-Plan</h2><span class="note">{NPOST} Posts von Di 15.12. bis So 27.06. Videos immer zuerst TikTok, dann Instagram Reel, dann YouTube Short, hochkant 1080 × 1920.</span></div>
<div class="tools"><input type="search" id="cpq" placeholder="Suchen: Hook, Titel, ID …" aria-label="Content durchsuchen"><select id="cpk" aria-label="Art"><option value="">Alle</option><option value="rewind">Stunts</option><option value="video">Videos</option><option value="karussell">Karussells</option><option value="auto">Autopilot (Abi-Pause)</option><option value="cd">Countdown</option><option value="live">Live</option></select><span class="hits" id="cphits"></span></div>
<div id="cplanList"></div></section>"""

mails = """<section id="mails"><div class="sechead"><span class="n">06</span><h2>Mails an die Liste</h2><span class="note">Aus Shopify Email, immer erst als Testmail an dich.</span></div><div id="mailList"></div></section>"""

zahlen = """<section id="zahlen"><div class="sechead"><span class="n">07</span><h2>Zahlen</h2><span class="note">Sonntags eintragen. Grün: Ziel erreicht. Gelb: zwischen Alarm und Ziel. Rot: unter Alarm.</span></div>
<div class="tablewrap"><table><thead><tr><th>Sonntag</th><th>Follower gesamt</th><th>Warteliste</th><th>Vorbestellt, bezahlt</th><th>Check</th></tr></thead><tbody id="kpiBody"></tbody></table></div>
<p>Die Ziele gehen von 170 Followern und null Posts heute aus. Sie sind bewusst vorsichtig. Schlägt ein Stunt ein, liegst du schnell darüber.</p></section>"""

erledigt = f"""<section id="erledigt"><div class="sechead"><span class="n">08</span><h2>Erledigt</h2><span class="note">Was seit September geschafft ist.</span></div>
<div class="tablewrap"><table><thead><tr><th>Wann</th><th>Ergebnis</th></tr></thead><tbody>{"".join(f"<tr><td class='mono'>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in P.DONE_STATIC)}</tbody></table></div>
<h3>Deine abgehakten Aufgaben aus dem alten Docket</h3><ul class="tasks donegrid" id="oldDone"></ul></section>"""

offen = f"""<section id="offen"><div class="sechead"><span class="n">09</span><h2>Offene Fragen</h2></div>
<div class="tablewrap"><table><thead><tr><th>Bis</th><th>Frage</th></tr></thead><tbody>{"".join(f"<tr><td class='mono'>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in P.OPEN_Q)}</tbody></table></div></section>
<footer>Novalife · Time Travel · Drop Docket Rev. 8 · gebaut am 30.10.2026 aus <code>novalife/time-travel/rev8</code></footer></div>"""

data = (f"<script>var WEEKS={js(P.WEEKS)};var VIDS={js(P.content8.VIDS)};var MAILS={js(P.mails8.MAILS)};var CPLAN={js(P.content8.CPLAN)};"
        f"var KPI={js(P.KPI)};var PH={js(P.PH)};var OLDDONE={js(OLDDONE)};var DROPTS=Date.UTC(2027,5,24,17,0,0);</script>")
script = f"<script>{open(os.path.join(HERE, 'docket8.js'), encoding='utf-8').read()}</script></body></html>"
page = head + top + heute + plan + wochen + stunts + content + mails + zahlen + erledigt + offen + data + script
open(OUT, 'w', encoding='utf-8').write(page)
print(OUT, f"{len(page.encode('utf-8')) / 1024:.0f} KB", NT, "Aufgaben", NPOST, "Posts", NS, "Stunts")
