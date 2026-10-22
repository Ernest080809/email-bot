# -*- coding: utf-8 -*-
# Leitfaden für die Fabrik-Calls (22.10.2026): Deutsch für Ernest, Fragen auf Englisch zum Vorlesen, Bewertungsbogen
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_HTML = os.path.join(HERE, "v19", "call_guide.html")

CSS = """
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;font-family:Helvetica,Arial,sans-serif;color:#1b2230;font-size:8.6pt;line-height:1.3}
.pg{width:210mm;height:297mm;padding:12mm 13mm 10mm;overflow:hidden;break-after:page;display:flex;flex-direction:column;gap:3mm}
.hd{display:flex;justify-content:space-between;align-items:baseline;border-bottom:0.4mm solid #1b2230;padding-bottom:2mm}
.hd b{font-size:8pt;letter-spacing:.12em;text-transform:uppercase}.hd span{font-size:8pt;color:#68707e}
h1{font-size:19pt;margin:0}h2{font-size:11.5pt;margin:1mm 0 0}p{margin:0}
.sub{color:#4a5262}
table{width:100%;border-collapse:collapse}
td,th{text-align:left;vertical-align:top;padding:0.8mm 1.4mm;border-bottom:0.25mm solid #e1e4ea}
th{background:#eef1f5;font-size:7.6pt;text-transform:uppercase;letter-spacing:.04em}
td.no{font-weight:700;width:6mm}
td.en{width:58%}
.en q{font-style:normal;quotes:none}
.note{background:#f3f5f8;border-radius:2mm;padding:2.5mm 3mm}
.warn{background:#fbf0e6;border-left:1mm solid #a8643a;border-radius:1mm;padding:2.5mm 3mm}
ul{margin:0;padding-left:5mm}li{margin-bottom:0.6mm}
.score td{height:9mm}
.score td.c{width:22mm;text-align:center;color:#9aa1ad}
.foot{margin-top:auto;font-size:7.3pt;color:#68707e;border-top:0.25mm solid #e1e4ea;padding-top:2mm}
"""

Q = [
    ("Stickerei", "Can you show me the embroidery machines on camera? Do you embroider the cut panels before sewing?",
     "Kuzgunlar: Name und Ort des Stick-Partners. DiZNEW: Liegt die Schwesterfirma auf demselben Gelände?"),
    ("Wäsche", "Can you show me the laundry? Do you have a laser for the honeycombs? Can you do our wash without sandblasting and without potassium permanganate spray?",
     "Laser zeigen lassen. Wer nur „no problem“ sagt, ohne Maschine, bekommt Punkte abgezogen."),
    ("Waschtest", "Before the proto, can you embroider a denim panel and wash it with our recipe? What does it cost?",
     "Das ist unser wichtigster Test: Hält die Stickerei die Wäsche aus?"),
    ("Schnitt", "Who makes the pattern? Can you send me the measurement sheet of the pattern before you cut the proto?",
     "Muss ja sein, sonst Minuspunkt."),
    ("Termine", "Can you ship the proto by 30 November and the pre-production sample by 4 January? When is your factory closed until May?",
     "Türkei: Ramadan Februar–März, Bayram. China: Neujahr 25.01.–20.02. Daten notieren."),
    ("Preis", "When can you send the quotation? Please include sample, digitizing and tooling for the button and the snaps.",
     "Angebot bis Di 27.10. Bei DiZNEW steht unser Zielpreis 30 $ FOB schon in der Mail. Nicht nachgeben im Call."),
    ("Zubehör", "Can you source a YKK metal zip, a custom shank button with an embossed star and ring-spring snaps, all nickel-free with a test report?",
     "Hersteller der Knöpfe notieren."),
    ("Zahlung", "What are your payment terms? We prefer 50 % deposit and 50 % after we approve the final inspection.",
     "100 % im Voraus heißt: rot."),
    ("Qualität", "Do you check every pair? Can you send a photo of every numbered pair before shipping?", ""),
    ("Versand", "Can you deliver DAP Berlin? How long does shipping take?",
     "Türkei: „Can you issue an ATR movement certificate?“"),
    ("Referenzen", "Do you produce for other small brands? Can I talk to one of them?", "Name und Kontakt notieren."),
    ("Kontakt", "Who will be my contact during production, and can we use WhatsApp?", "Name, Nummer, Englisch gut?"),
]
qrows = "".join(f'<tr><td class="no">{i}</td><td><b>{k}</b></td><td class="en"><q>{en}</q></td><td>{de}</td></tr>'
                for i, (k, en, de) in enumerate(Q, 1))
CRIT = [("Stickerei", "im Haus oder fester Partner gezeigt, Panels vor dem Nähen", 25),
        ("Wäsche", "eigene Wäscherei oder fester Partner, Laser, ohne PP-Spray", 20),
        ("Kommunikation", "versteht Fragen, antwortet konkret, gutes Englisch", 15),
        ("Preis", "Preis pro Paar, Musterkosten, Werkzeug", 15),
        ("Termine", "Proto 30.11., PP 04.01., Pausen passen", 15),
        ("Vertrauen", "Referenzen, zeigt alles offen, Zahlung 50/50", 10)]
crows = "".join(f'<tr><td><b>{k}</b><br><span class="sub">{d}</span></td><td class="c">{w} %</td><td class="c">1 2 3 4 5</td><td class="c">1 2 3 4 5</td></tr>'
                for k, d, w in CRIT)


def page(n, total, body):
    return (f'<section class="pg"><div class="hd"><b>Novalife · Leitfaden Fabrik-Calls</b><span>22.10.2026 · Seite {n} von {total}</span></div>{body}'
            '<div class="foot">Nach dem Call: Notizen und Punkte an Claude schicken. Daraus entsteht der Vergleich für die Wahl am Do 29.10.</div></section>')


p1 = page(1, 2, f"""
<div><h1>Fabrik-Call · 30 Minuten</h1><p class="sub">Immer gleiche Fragen in gleicher Reihenfolge, damit die Calls vergleichbar sind. Die englischen Sätze kannst du so vorlesen.</p></div>
<div class="note"><b>Vorher (5 Min.):</b> Quote Pack und Mockup offen haben. Ton und Kamera testen. Zeit: 17:30 Istanbul ist in Zypern ebenfalls 17:30. Stift und Seite 2 bereit.<br>
<b>Start:</b> <q>Hi, I'm Ernest from Novalife in Berlin. Thank you for your time. I'd like to see your production and ask twelve short questions. Is that okay?</q></div>
<h2>Rundgang mit Kamera (10 Min.)</h2>
<p><b>Stickmaschinen</b> in Betrieb, möglichst mit Denim · <b>Wäscherei</b> mit Laser oder Handschleifplätzen · <b>Nähhalle</b>: wie viele Leute, ordentlich? · <b>Endkontrolle</b>: eigener Platz?</p>
<p class="sub">Sagt jemand „wir zeigen das später“ oder zeigt nur Büros, ist das ein Warnsignal.</p>
<h2>12 Fragen (15 Min.)</h2>
<table><tr><th></th><th>Thema</th><th>Auf Englisch</th><th>Worauf du achtest</th></tr>{qrows}</table>
<div class="note"><b>Ende (2 Min.):</b> <q>Thank you. I'll decide on 29 October. If we work together, you get our full tech pack the next day.</q><br>Nichts zusagen, keinen Preis nennen, nichts unterschreiben.</div>""")

p2 = page(2, 2, f"""
<h2>Bewertung direkt nach dem Call</h2>
<p class="sub">1 = schlecht, 5 = sehr gut. Kreise die Zahl ein. Die Gewichtung rechne ich aus.</p>
<table class="score"><tr><th>Kriterium</th><th>Gewicht</th><th>Kuzgunlar</th><th>DiZNEW</th></tr>{crows}
<tr><td><b>Bauchgefühl</b><br><span class="sub">Würdest du diesen Leuten 3.000 € überweisen?</span></td><td class="c">–</td><td class="c">ja / nein</td><td class="c">ja / nein</td></tr></table>
<div class="warn"><b>K.-o.-Gründe, dann raus, egal wie billig:</b>
<ul><li>zeigt keine Stickmaschinen und keine Wäscherei, auch nicht beim Partner</li><li>will 100 % Vorkasse</li><li>kann nicht vor dem Nähen sticken</li><li>keine schriftlichen Antworten nach dem Call</li></ul></div>
<h2>Notizen</h2>
<table><tr><th style="width:50%">Kuzgunlar</th><th>DiZNEW</th></tr><tr><td style="height:70mm"></td><td></td></tr></table>""")

open(OUT_HTML, "w").write(f'<!doctype html><html><head><meta charset="utf-8"><title>Leitfaden Fabrik-Calls</title><style>{CSS}</style></head><body>{p1}{p2}</body></html>')
print("ok")
