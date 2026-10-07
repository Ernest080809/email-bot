# -*- coding: utf-8 -*-
# Docket Rev. 5.3: Design v1.7 (großer Serp), Papiertest 3 mit zwei Seiten, Zahlen 63 € / 9.380 € / 10 und 32
import os
H = os.path.dirname(os.path.abspath(__file__))
def rd(f): return open(os.path.join(H, f), encoding="utf-8").read()
def wr(f, s): open(os.path.join(H, f), "w", encoding="utf-8").write(s)
def rep(s, a, b, cnt=1):
    assert s.count(a) == cnt, (a[:90], s.count(a))
    return s.replace(a, b)

A = rd("r5_a.py")
A = rep(A, '"Mein Budget: 4.500 €. Mein Plan kostet 9.230 €."', '"Mein Budget: 4.500 €. Mein Plan kostet 9.380 €."')
A = rep(A, "100 Jeans, 9.230 € Plan, 4.500 € Budget, Lücke 4.730 €.", "100 Jeans, 9.380 € Plan, 4.500 € Budget, Lücke 4.880 €.")
A = rep(A, "bei ~5.850 € Ware rund 1.100 €.", "bei ~6.000 € Ware rund 1.150 €.")
A = rep(A, "dazu ein kleiner Serp im Stoppelfeld an der Seite. Claude hat daraus Design v1.6 gebaut.", "dazu ein Serp im Stoppelfeld an der Seite. Claude hat daraus Design v1.7 gebaut.")
A = rep(A, "Du hast am 07.10. noch einmal geändert, Design v1.6.", "Du hast am 07.10. noch einmal geändert, Design v1.7.")
A = rep(A, 'T("B", "Papiertest 3 mit Design v1.6 und fünf Entscheidungen", 45, [', 'T("B", "Papiertest 3 mit Design v1.7 und vier Entscheidungen", 45, [')
A = rep(A, '"PDF „NVL_Druckvorlage_v16.pdf“ öffnen (im Chat vom 07.10.). Eine Seite.",', '"PDF „NVL_Druckvorlage_v17.pdf“ öffnen (im Chat vom 07.10., die neuere). Zwei Seiten.",')
A = rep(A, '"Ausschneiden: die linke Gesäßtasche und den kleinen Zettel mit dem Serp.",', '"Ausschneiden: Seite 1 die linke Gesäßtasche, Seite 2 den Zettel mit dem Serp.",')
A = rep(A, '"Claude hat 7 Fotos, die zwei Maße der Münztasche und deine fünf Antworten."', '"Claude hat 7 Fotos, die zwei Maße der Münztasche und deine vier Antworten."')
A = rep(A, "Papiertest 3 mit Design v1.6. Hier sind 7 Fotos. Münztasche meiner Eightyfive: Breite … mm, Höhe … mm. Meine Entscheidungen: Serp an der Seite: ja / nein, Höhe … cm unter dem Bund.",
        "Papiertest 3 mit Design v1.7. Hier sind 7 Fotos. Münztasche meiner Eightyfive: Breite … mm, Höhe … mm. Meine Entscheidungen: Serp an der Seite auf … cm unter dem Bund.")
wr("r5_a.py", A)

B = rd("r5_b.py")
B = rep(B, "Stichzahl gesamt nahe ~30.000 (Design v1.6)", "Stichzahl gesamt nahe ~33.000 (Design v1.7)")
B = rep(B, "Liegt die Summe deutlich über 30.000:", "Liegt die Summe deutlich über 33.000:")
B = rep(B, "Das ist Teil der Stückkosten von ~61,50 €", "Das ist Teil der Stückkosten von ~63 €")
wr("r5_b.py", B)

C = rd("r5_c.py")
C = rep(C, "Jedes geschenkte Paar kostet dich ~61,50 €", "Jedes geschenkte Paar kostet dich ~63 €")
C = rep(C, "Planwert: bei 50/50 ca. 2.925 €, bei 60/40 ca. 3.510 € (Fabrikpreis ~58,50 € pro Paar",
        "Planwert: bei 50/50 ca. 3.000 €, bei 60/40 ca. 3.600 € (Fabrikpreis ~60 € pro Paar")
C = rep(C, "brauchst du mindestens 31 Vorbestellungen.", "brauchst du mindestens 32 Vorbestellungen.")
C = rep(C, "Dann Schnitt auf die Seitennaht: der kleine Serp im Stoppelfeld.", "Dann Schnitt auf die Seitennaht: der Serp im Stoppelfeld.")
wr("r5_c.py", C)

Dd = rd("r5_d.py")
Dd = rep(Dd, ' 6: "Seitennaht im Streiflicht: der kleine Serp und die Stoppeln",', ' 6: "Seitennaht im Streiflicht: der Serp über den Stoppeln",')
Dd = rep(Dd, "(Planwert bei 50/50 ca. 2.925 €)", "(Planwert bei 50/50 ca. 3.000 €)")
Dd = rep(Dd, "Break-even (59 Paar)", "Break-even (60 Paar)")
wr("r5_d.py", Dd)

R = rd("ref5.py")
R = rep(R, ' ("Mi 07.10.", "W4", "Deine Skizze → Design v1.6"),\n ("Do 08.10.", "W4", "Papiertest 3 mit v1.6"),',
        ' ("Mi 07.10.", "W4", "Deine Skizze → Design v1.6, abends v1.7 mit großem Serp"),\n ("Do 08.10.", "W4", "Papiertest 3 mit v1.7"),')
R = rep(R, "(mindestens 31 Vorbestellungen)", "(mindestens 32 Vorbestellungen)")
R = rep(R, "- 5 embroidery elements (A–E) on 5 cut-panel zones, one small motif 10 mm from the outseam, approx. 30,000 stitches per pair, fine cross-stitch look on a 1.33 mm grid, 8 polyester thread colours (white, light grey, red, gold, dark gold, straw, two browns)",
        "- 5 embroidery elements (A–E) on 5 cut-panel zones, one motif (approx. 53 × 49 mm) 10 mm from the outseam, approx. 33,000 stitches per pair, fine cross-stitch look on a 1.33 mm grid, up to 10 polyester thread colours (white, light grey, red, four golds, straw, two browns)")
R = rep(R, '("B · Serp im Stoppelfeld", "Linkes Bein vorn, 10 mm (±2) neben der Seitennaht, Höhe laut Tech Pack. Klinge weiß, kein Rot. Die Halme als feine Striche sichtbar, nicht zu Punkten verlaufen. Kein Stern, kein Hammer, kein roter Grund."),',
        '("B · Serp im Stoppelfeld", "Linkes Bein vorn, 10 mm (±2) neben der Seitennaht, Höhe laut Tech Pack, ca. 53 × 49 mm. Klinge weiß, Schneide rot, Griff braun. Die Halme einzeln lesbar, Schnittkanten hell. Kein Stern, kein Hammer, kein roter Grund."),')
R = rep(R, "echter Aufwand: rund 1.100 € auf die Lieferung.", "echter Aufwand: rund 1.150 € auf die Lieferung.")
R = rep(R, '("Stickerei ~30.000 Stiche", "16,50", "~0,55 € pro 1.000 Stiche, Design v1.6"),', '("Stickerei ~33.000 Stiche", "18,00", "~0,55 € pro 1.000 Stiche, Design v1.7"),')
R = rep(R, '(("<b>Stückkosten</b>", "<b>61,50</b>", "Spec Rev. 12"), "total"),', '(("<b>Stückkosten</b>", "<b>63,00</b>", "Spec Rev. 13"), "total"),')
R = rep(R, '("", "Anzahlung 50 % (100 × ~58,50 € Fabrikpreis)", "2.925 €", "Feb 27"),', '("", "Anzahlung 50 % (100 × ~60 € Fabrikpreis)", "3.000 €", "Feb 27"),')
R = rep(R, '("", "Restzahlung 50 %", "2.925 €", "Mär 27"),', '("", "Restzahlung 50 %", "3.000 €", "Mär 27"),')
R = rep(R, '"<b>9.230 €</b>"', '"<b>9.380 €</b>"')
R = rep(R, '"<b>4.730 €</b>"', '"<b>4.880 €</b>"')
R = rep(R, "Bei 60/40 statt 50/50 steigt die Anzahlung auf ~3.510 €. Gegenüber Design v1.5 sind es −450 €.", "Bei 60/40 statt 50/50 steigt die Anzahlung auf ~3.600 €. Gegenüber Design v1.5 sind es −300 €.")
R = rep(R, '("Mo 01.02. Schwelle", "Anzahlung 2.925 €", "~1.990 €", "~935 €", "<b>mindestens 10</b>"),', '("Mo 01.02. Schwelle", "Anzahlung 3.000 €", "~1.990 €", "~1.010 €", "<b>mindestens 10</b>"),')
R = rep(R, '("Fr 19.03. Restzahlung", "Rest 2.925 €, Shoot, Verpackung, Versandmaterial, Werbung", "0 €", "~4.350–4.500 €", "<b>mindestens 31</b>"),',
        '("Fr 19.03. Restzahlung", "Rest 3.000 €, Shoot, Verpackung, Versandmaterial, Werbung", "0 €", "~4.500–4.650 €", "<b>mindestens 32</b>"),')
R = rep(R, "Zwischen 31 und 35 liegen 4 Paar Puffer.", "Zwischen 32 und 35 liegen 3 Paar Puffer.")
R = rep(R, '("<b>Break-even</b>", "35 → 5.215 €", "24 → 4.056 €", "59", "<b>9.271 €</b>"),', '("<b>Break-even</b>", "35 → 5.215 €", "25 → 4.225 €", "60", "<b>9.440 €</b>"),')
R = rep(R, '("abzüglich Stückkosten", "−61,50", "Spec Rev. 12"),', '("abzüglich Stückkosten", "−63,00", "Spec Rev. 13"),')
R = rep(R, '(("<b>Deckungsbeitrag</b>", "<b>70,17</b>", "als Kleinunternehmer 97,15 €, dafür ist die Einfuhrumsatzsteuer Aufwand"), "total"),',
        '(("<b>Deckungsbeitrag</b>", "<b>68,67</b>", "als Kleinunternehmer 95,65 €, dafür ist die Einfuhrumsatzsteuer Aufwand"), "total"),')
R = rep(R, "'<h3>Stückkosten Jeans · ~61,50 €</h3>'", "'<h3>Stückkosten Jeans · ~63 €</h3>'")
R = rep(R, "Kapitalbedarf <b>9.230 €</b>, Budget 4.500 €, Lücke <b>4.730 €</b>.", "Kapitalbedarf <b>9.380 €</b>, Budget 4.500 €, Lücke <b>4.880 €</b>.")
R = rep(R, "mindestens 31 bis zur Restzahlung am 19.03. Das Kontingent ist 35, der Puffer also 4 Paar.", "mindestens 32 bis zur Restzahlung am 19.03. Das Kontingent ist 35, der Puffer also 3 Paar.")
R = rep(R, "auf rund 5.850 € Ware echter Aufwand, etwa 1.100 €. Das sind 7–8 Vorbestellungen", "auf rund 6.000 € Ware echter Aufwand, etwa 1.150 €. Das sind rund 8 Vorbestellungen")
wr("ref5.py", R)

G = rd("gen5.py")
G = rep(G, "Projekt Slavic · Rev. 5.2 · 07.10.2026", "Projekt Slavic · Rev. 5.3 · 07.10.2026")
G = rep(G, '<span class="k">Stückkosten</span><div class="v">~61,50 €</div>', '<span class="k">Stückkosten</span><div class="v">~63 €</div>')
G = rep(G, '<div class="v">59</div><div class="s">Jeans: 35 vorbestellt + 24 im Drop</div>', '<div class="v">60</div><div class="s">Jeans: 35 vorbestellt + 25 im Drop</div>')
G = rep(G, '<div class="v">9.230 €</div><div class="s">Budget 4.500 € → Lücke 4.730 €</div>', '<div class="v">9.380 €</div><div class="s">Budget 4.500 € → Lücke 4.880 €</div>')
G = rep(G, '<div class="v">10 / 31</div>', '<div class="v">10 / 32</div>')
G = rep(G, "Kapitalbedarf <b>9.230 €</b> gegen 4.500 € Budget. Die Lücke von <b>4.730 €</b>", "Kapitalbedarf <b>9.380 €</b> gegen 4.500 € Budget. Die Lücke von <b>4.880 €</b>")
G = rep(G, "mindestens <b>31 bis zur Restzahlung am 19.03.</b>", "mindestens <b>32 bis zur Restzahlung am 19.03.</b>")
G = rep(G, "<p>Zwischen 31 und 35 liegen 4 Paar Puffer. Das ist dünn,", "<p>Zwischen 32 und 35 liegen 3 Paar Puffer. Das ist dünn,")
G = rep(G, "kommen rund 1.100 € Einfuhrumsatzsteuer dazu.", "kommen rund 1.150 € Einfuhrumsatzsteuer dazu.")
G = rep(G, '<h2>Das Design · v1.6</h2><span class="note">Nach deiner Skizze vom 07.10. Papiertest 3 am 08.10., Freeze am 09.10.</span>',
        '<h2>Das Design · v1.7</h2><span class="note">Nach deiner Skizze vom 07.10., mit großem Serp. Papiertest 3 am 08.10., Freeze am 09.10.</span>')
G = rep(G, '<span class="mono">NVL_Druckvorlage_v16.pdf</span> (B2 und B)', '<span class="mono">NVL_Druckvorlage_v17.pdf</span> (B2 und B)')
G = rep(G, "<td>Linkes Bein vorn, 10 mm neben der Seitennaht, Mitte ca. 45 cm unter dem Bund. Kleiner Serp über abgeschnittenen Halmen (Vorschlag, Entscheidung beim Freeze)</td><td>ca. 22 × 35 mm</td><td>Weiß, Grauweiß, zwei Brauntöne, Stroh. Kein Rot</td>",
        "<td>Linkes Bein vorn, 10 mm neben der Seitennaht, Mitte ca. 45 cm unter dem Bund. Der Serp wie in v1.5 über goldenen, abgeschnittenen Halmen</td><td>ca. 53 × 49 mm</td><td>Weiß, Rot, Grauweiß, zwei Brauntöne, Gold</td>")
G = rep(G, "Rund 30.000 Stiche am Teil.", "Rund 33.000 Stiche am Teil.")
G = rep(G, "drei Ähren auf einem roten Band, ein kleiner Serp an der Seite. Claude baut v1.6.</dd>", "drei Ähren auf einem roten Band, ein Serp an der Seite. Claude baut v1.6, abends v1.7 mit großem Serp.</dd>")
G = rep(G, "<dd>Papiertest 3: eine Seite drucken, echte Garnfäden ankleben, Fotos an Claude, fünf Entscheidungen.", "<dd>Papiertest 3: zwei Seiten drucken, echte Garnfäden ankleben, Fotos an Claude, vier Entscheidungen.")
G = rep(G, "Straight, ehrliche Größen W30–W38. Stückkosten ~61,50 €.", "Straight, ehrliche Größen W30–W38. Stückkosten ~63 €.")
wr("gen5.py", G)
print("patch53 ok")
