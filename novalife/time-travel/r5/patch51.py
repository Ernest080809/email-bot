# -*- coding: utf-8 -*-
# Docket Rev. 5.1: Design v1.5 (Papiertest 1 am 01.10.) und neue Zahlen (~40.000 Stiche, 66 €, 9.680 €, Schwellen 11/34)
import os
H = os.path.dirname(os.path.abspath(__file__))
def rd(f): return open(os.path.join(H, f), encoding="utf-8").read()
def wr(f, s): open(os.path.join(H, f), "w", encoding="utf-8").write(s)
def rep(s, a, b, cnt=1):
    assert s.count(a) == cnt, (a[:90], s.count(a))
    return s.replace(a, b)
def block(s, start, end, new):
    i = s.index(start); j = s.index(end, i) + len(end)
    assert s.count(start) == 1, start[:60]
    return s[:i] + new + s[j:]

# ======================= r5_a.py =======================
A = rd("r5_a.py")
A = rep(A, '"Mein Budget: 4.500 €. Mein Plan kostet 9.030 €."', '"Mein Budget: 4.500 €. Mein Plan kostet 9.680 €."')
A = rep(A, "100 Jeans, 9.030 € Plan, 4.500 € Budget, Lücke 4.530 €.", "100 Jeans, 9.680 € Plan, 4.500 € Budget, Lücke 5.180 €.")
A = rep(A, '"Acht Strahlen. Er sitzt hinten auf der Passe."', '"Acht Strahlen. Er sitzt hinten auf der rechten Tasche."')
A = rep(A, "bei ~5.900 € Ware rund 1.100 €.", "bei ~6.300 € Ware rund 1.200 €.")
# Do 01.10.: Druck bleibt (Ernest hakt selbst ab), Papiertest 1 als Notiz dahinter
A = rep(A, '"Fünf Teile sind ausgeschnitten, die Kontrolllinie misst 100 mm.")],',
        '"Fünf Teile sind ausgeschnitten, die Kontrolllinie misst 100 mm."),\n'
        '  NOTE("ERLEDIGT 01.10.: Papiertest 1 schon heute, einen Tag früher. Dein Urteil: Band schmaler, Münztasche größer, Tasche gut, Serp mit Garbe realistisch statt aufgeklebt, Goldfäden länger, Alatyr auf die andere Gesäßtasche. Claude hat daraus Design v1.5 gebaut: Canvas Version 12, Spec Rev. 11, Druckvorlage v1.5.")],')
# Fr 02.10.: Papiertest 2
A = block(A, ' [T("B", "Papiertest: aufkleben, anziehen, fotografieren", 60, [',
          '4) Was würdest du ändern, bevor das Design an die Fabrik geht?")],',
          ''' [T("B", "Papiertest 2 mit Design v1.5", 60, [
    "PDF „NVL_Druckvorlage_v15.pdf“ öffnen (im Chat vom 01.10.). Zwei Seiten, nur die geänderten Teile.",
    "Drucken wie beim ersten Mal: A4 Hochformat, Farbe, „Tatsächliche Größe“ bzw. „100 %“. Kontrolllinie messen, genau 100 mm.",
    "Ausschneiden: Seite 1 das Band A und die Münztasche E, Seite 2 die linke Gesäßtasche mit B. Die alten A, E und die alte Gesäßtasche weglegen. Alatyr C und Patch D vom ersten Ausdruck weiterverwenden.",
    "Goldfäden echt machen: 9 Stücke gelbes oder goldenes Garn (oder Wolle), 2–3 cm lang, unterschiedlich lang, direkt unter die rote Linie kleben.",
    "Handy aufs Regal und das Aufkleben im Zeitraffer filmen, falls es vom ersten Test kein Video gibt. Das ist dein erster Post am 12.10.",
    "Vorn: Band mit der Innenkante auf die Öffnung der rechten Vordertasche (vom Träger aus). Münztasche oben bündig an die Münztaschennaht, die untere rechte Ecke unter das Band.",
    "Hinten: Tasche mit B auf die linke Gesäßtasche, Oberkante an Oberkante. Alatyr C auf die rechte Gesäßtasche, waagerecht mittig, Mitte ca. 45 mm unter der Oberkante (in der Taschenmitte gemessen). Patch D wie beim ersten Test.",
    "Münztasche deiner Eightyfive messen: Breite oben und Höhe bis dahin, wo sie unter der Vordertasche verschwindet. Beide Zahlen gehen ins Tech Pack.",
    "Hose anziehen. Aus 3 m und aus 1 m je ein Foto von vorn, hinten und seitlich, also 6 Fotos. Dazu 10 Sekunden Video, in dem du dich einmal drehst. Alles mit dem Prompt unten an Claude.",
   ], "Claude hat 6 Fotos, das Video und die zwei Maße der Münztasche.",
   "Papiertest 2 mit Design v1.5. Hier sind 6 Fotos und das Video. Münztasche meiner Eightyfive: Breite … mm, Höhe … mm. Beurteile ehrlich: 1) Ist das Band mit 23 mm jetzt richtig? 2) Ist die Münztasche groß genug? 3) Wirkt Serp mit Garbe jetzt echt oder immer noch aufgeklebt? 4) Schauen die Goldfäden genug raus? 5) Ist der Alatyr auf der rechten Tasche besser als auf der Passe?")],''')
# Sa 03.10.: Entscheidungen nach Papiertest 2
A = block(A, ' [T("D", "Design-Entscheidungen treffen", 30, [',
          'Bau daraus Design v1.5 als Freeze-Version und aktualisiere Canvas, Druckvorlage und Spec.")],',
          ''' [T("D", "Design-Entscheidungen treffen", 30, [
    "Claudes Einschätzung zu Papiertest 2 lesen.",
    "Vier Fragen beantworten: v1.5 so lassen oder noch etwas ändern? Patch D mit 86 × 76 mm so lassen oder kleiner? Taschenklappe hinten ja oder nein (Vorschlag: nein, die Tasche ohne Klappe war beim ersten Test gut)? Nackenlabel für Zipper und Polo als gewebtes Etikett mit vereinfachtem Baum, okay?",
    "Antworten mit dem Prompt unten an Claude. Claude baut daraus die Freeze-Version für die Fabrik.",
   ], "Claude hat deine vier Antworten.",
   "Meine Entscheidungen nach Papiertest 2: v1.5: passt / ändern: … / Patch: … / Taschenklappe: … / Nackenlabel: … Bau daraus die Freeze-Version und aktualisiere Canvas, Druckvorlage und Spec.")],''')
A = rep(A, "aus produkt-spec.md und Design v1.5:", "aus produkt-spec.md und der Freeze-Version des Designs:")
A = rep(A, 'T("D", "Design-Freeze v1.5 abnehmen", 30, [', 'T("D", "Design-Freeze abnehmen", 30, [')
A = rep(A, '"Canvas „Fit-Mockup NVL-TT-01“ öffnen und v1.5 ansehen.",',
        '"Canvas „Fit-Mockup NVL-TT-01“ öffnen und die Freeze-Version ansehen: v1.5, oder v1.6, falls Papiertest 2 noch etwas geändert hat.",')
wr("r5_a.py", A)

# ======================= r5_b.py =======================
B = rd("r5_b.py")
B = rep(B, '"Mit dem Prompt unten an Claude: Maße und Motive gegen das Elementblatt, Stichzahl gesamt nahe ~33.000, echter Kreuzstich oder feine Füllung bei A, C und E.",',
        '"Mit dem Prompt unten an Claude: Maße und Motive gegen das Elementblatt, Stichzahl gesamt nahe ~40.000 (Design v1.5), echter Kreuzstich oder feine Füllung bei A, C und E.",\n'
        '    "Liegt die Summe deutlich über 40.000: Claude rechnet Stückkosten, Anzahlung und die Schwellen 01.02. und 19.03. neu, bevor du freigibst.",')
B = rep(B, "Das ist Teil der Stückkosten von ~62 €", "Das ist Teil der Stückkosten von ~66 €")
wr("r5_b.py", B)

# ======================= r5_c.py =======================
C = rd("r5_c.py")
C = rep(C, '"Makro auf den Alatyr auf der Passe"', '"Makro auf den Alatyr auf der rechten Gesäßtasche"')
C = rep(C, "reicht es für mindestens 10?", "reicht es für mindestens 11?")
C = rep(C, "Jedes geschenkte Paar kostet dich ~62 €", "Jedes geschenkte Paar kostet dich ~66 €")
C = rep(C, "Vorbestellungen gegen Minimum (10 bis heute).", "Vorbestellungen gegen Minimum (11 bis heute).")
C = rep(C, "Planwert: bei 50/50 ca. 2.950 €, bei 60/40 ca. 3.540 € (Fabrikpreis ~59 € pro Paar",
        "Planwert: bei 50/50 ca. 3.150 €, bei 60/40 ca. 3.780 € (Fabrikpreis ~63 € pro Paar")
C = rep(C, "brauchst du mindestens 31 Vorbestellungen.", "brauchst du mindestens 34 Vorbestellungen.")
C = rep(C, "Die Vorbestellung läuft (mindestens 10)", "Die Vorbestellung läuft (mindestens 11)")
wr("r5_c.py", C)

# ======================= r5_d.py =======================
Dd = rd("r5_d.py")
Dd = rep(Dd, '19: "Alatyr auf der Passe, die Kamera kommt von oben",', '19: "Alatyr auf der rechten Gesäßtasche, die Kamera kommt langsam näher",')
Dd = rep(Dd, "(Planwert bei 50/50 ca. 2.950 €)", "(Planwert bei 50/50 ca. 3.150 €)")
Dd = rep(Dd, "Hinten: B mit Ähren, Linie und 7–9 Goldfäden (sitzen sie fest?), Alatyr C, Patch D gerade.",
         "Hinten links: B mit Ähren, Linie und 9 Goldfäden (sitzen sie fest?). Hinten rechts: Alatyr C. Patch D gerade.")
Dd = rep(Dd, "Break-even (59 Paar)", "Break-even (62 Paar)")
wr("r5_d.py", Dd)

# ======================= ref5.py =======================
R = rd("ref5.py")
R = rep(R, ' ("Fr 02.10.", "W3", "Papiertest an der echten Hose"),\n ("Mo 05.10.", "W4", "<b>Design-Freeze v1.5</b>"),',
        ' ("Do 01.10.", "W3", "Papiertest 1 an der echten Hose, erledigt → Design v1.5"),\n ("Fr 02.10.", "W3", "Papiertest 2 mit v1.5"),\n ("Mo 05.10.", "W4", "<b>Design-Freeze</b>"),')
R = rep(R, "mindestens 10 Vorbestellungen bis So 31.01.", "mindestens 11 Vorbestellungen bis So 31.01.")
R = rep(R, "(mindestens 31 Vorbestellungen)", "(mindestens 34 Vorbestellungen)")
R = rep(R, "- 5 embroidery elements (A–E), approx. 33,000 stitches per pair, fine cross-stitch look on a 1.33 mm grid, polyester thread in white, red, gold and brown",
        "- 5 embroidery elements (A–E), approx. 40,000 stitches per pair, fine cross-stitch look on a 1.33 mm grid, 8 polyester thread colours (white, light grey, red, three golds, two browns)")
R = rep(R, "then 7–9 gold polyester threads set by hand and knotted inside the right back pocket",
        "then 9 gold polyester threads (three-ply, approx. 1 mm, 18–30 mm long) set by hand and knotted inside the left back pocket")
R = rep(R, '"Innenkante liegt auf der Taschenöffnung, 28 mm breit (±1),', '"Innenkante liegt auf der Taschenöffnung, 23 mm breit (±1),')
R = rep(R, '"Ganze Fläche bestickt, 49 × 49 mm (±1), Raster gerade zur Taschenkante, Tasche danach sauber angenäht."',
        '"Ganze Fläche bestickt, 60 × 60 mm (±1) auf 62-mm-Tasche, Raster gerade zur Taschenkante, untere rechte Ecke unter dem Band, Tasche danach sauber angenäht."')
R = rep(R, '"Mittig in der unteren Hälfte der rechten Gesäßtasche. Klinge weiß, Schneide rot, die Spitze schneidet in die Halme. Kein Stern, kein Hammer, kein roter Grund."',
        '"Mittig in der unteren Hälfte der linken Gesäßtasche. Klinge weiß, Schneide rot, sie liegt hinter den Halmen, zwei Halme sind durchtrennt. Ähren mit Grannen, Licht und Schatten sichtbar. Kein Stern, kein Hammer, kein roter Grund."')
R = rep(R, '"Ähren über der roten Linie. 7–9 Goldfäden, 9–16 mm lang, ungleich verteilt,',
        '"Ähren über der roten Linie. 9 Goldfäden, 18–30 mm lang, dreifach gezwirnt, ungleich verteilt,')
R = rep(R, '"36 × 36 mm (±1), mittig zwischen den zwei linken Gürtelschlaufen auf der Passe."',
        '"36 × 36 mm (±1), rechte Gesäßtasche, waagerecht mittig, auf Höhe der roten Linie links."')
R = rep(R, "echter Aufwand: rund 1.100 € auf die Lieferung.", "echter Aufwand: rund 1.200 € auf die Lieferung.")
R = rep(R, '("Stickerei ~33.000 Stiche", "18,00", "~0,55 € pro 1.000 Stiche"),', '("Stickerei ~40.000 Stiche", "22,00", "~0,55 € pro 1.000 Stiche, Design v1.5"),')
R = rep(R, '"Vorderteil, Münztasche, Gesäßtasche, Passe"', '"Vorderteil, Münztasche, beide Gesäßtaschen"')
R = rep(R, '"nach der Wäsche, 7–9 Fäden"', '"nach der Wäsche, 9 Fäden"')
R = rep(R, '(("<b>Stückkosten</b>", "<b>62,00</b>", "Spec Rev. 10"), "total"),', '(("<b>Stückkosten</b>", "<b>66,00</b>", "Spec Rev. 11"), "total"),')
R = rep(R, '("", "Anzahlung 50 % (100 × ~59 € Fabrikpreis)", "2.950 €", "Feb 27"),', '("", "Anzahlung 50 % (100 × ~63 € Fabrikpreis)", "3.150 €", "Feb 27"),')
R = rep(R, '("", "Restzahlung 50 %", "2.950 €", "Mär 27"),', '("", "Restzahlung 50 %", "3.150 €", "Mär 27"),')
R = rep(R, '"<b>9.280 €</b>"', '"<b>9.680 €</b>"')
R = rep(R, '"<b>4.780 €</b>"', '"<b>5.180 €</b>"')
R = rep(R, "Bei 60/40 statt 50/50 steigt die Anzahlung auf ~3.540 €.", "Bei 60/40 statt 50/50 steigt die Anzahlung auf ~3.780 €. Gegenüber Design v1.4 sind es +400 € (100 × 4 € mehr Stickerei).")
R = rep(R, '("Mo 01.02. Schwelle", "Anzahlung 2.950 €", "~1.990 €", "~960 €", "<b>mindestens 10</b>"),',
        '("Mo 01.02. Schwelle", "Anzahlung 3.150 €", "~1.990 €", "~1.160 €", "<b>mindestens 11</b>"),')
R = rep(R, '("Fr 19.03. Restzahlung", "Rest 2.950 €, Shoot, Verpackung, Versandmaterial, Werbung", "0 €", "~4.400–4.550 €", "<b>mindestens 31</b>"),',
        '("Fr 19.03. Restzahlung", "Rest 3.150 €, Shoot, Verpackung, Versandmaterial, Werbung", "0 €", "~4.800–4.950 €", "<b>mindestens 34</b>"),')
R = rep(R, "Zwischen 31 und 35 liegen nur 4 Paar Puffer.", "Zwischen 34 und 35 liegt nur 1 Paar Puffer (vor Design v1.5 waren es 4).")
R = rep(R, '("<b>Break-even</b>", "35 → 5.215 €", "25 → 4.225 €", "60", "<b>9.440 €</b>"),',
        '("<b>Break-even</b>", "35 → 5.215 €", "27 → 4.563 €", "62", "<b>9.778 €</b>"),')
R = rep(R, "'<h3>Stückkosten Jeans · ~62 €</h3>'", "'<h3>Stückkosten Jeans · ~66 €</h3>'")
R = rep(R, '("Goldfäden", "Polyester Gold, nicht metallisiert, von Hand gesetzt", "7–9 Fäden"),',
        '("Goldfäden", "Polyester Gold, nicht metallisiert, dreifach gezwirnt, von Hand gesetzt", "9 Fäden, 18–30 mm"),')
R = rep(R, "Kapitalbedarf <b>9.280 €</b>, Budget 4.500 €, Lücke <b>4.780 €</b>.", "Kapitalbedarf <b>9.680 €</b>, Budget 4.500 €, Lücke <b>5.180 €</b>.")
R = rep(R, "Mindestens 10 bis zur Schwelle am 01.02., mindestens 31 bis zur Restzahlung am 19.03. Das Kontingent ist 35, der Puffer also 4 Paar.",
        "Mindestens 11 bis zur Schwelle am 01.02., mindestens 34 bis zur Restzahlung am 19.03. Das Kontingent ist 35, der Puffer also nur 1 Paar. Design v1.5 kostet ~400 € mehr als v1.4.")
R = rep(R, "Schwelle am 01.02.: unter 10 keine Anzahlung,", "Schwelle am 01.02.: unter 11 keine Anzahlung,")
R = rep(R, "Restzahlung gegen Versandnachweis oder Teilzahlung (Woche 26).\"),",
        "Restzahlung gegen Versandnachweis oder Teilzahlung (Woche 26). Vorschlag, offen: Kontingent von Anfang an 40 statt 35, entscheiden beim Bau der Vorbestellung (Woche 14). Keine neue Stickerei ohne Gegenrechnung.\"),")
R = rep(R, "auf rund 5.900 € Ware echter Aufwand, etwa 1.100 €. Das sind 7–8 Vorbestellungen", "auf rund 6.300 € Ware echter Aufwand, etwa 1.200 €. Das sind 8–9 Vorbestellungen")
wr("ref5.py", R)

# ======================= gen5.py =======================
G = rd("gen5.py")
G = rep(G, "Projekt Slavic · Rev. 5 · 01.10.2026", "Projekt Slavic · Rev. 5.1 · 01.10.2026")
G = rep(G, '<span class="k">Stückkosten</span><div class="v">~62 €</div>', '<span class="k">Stückkosten</span><div class="v">~66 €</div>')
G = rep(G, '<div class="v">60</div><div class="s">Jeans: 35 vorbestellt + 25 im Drop</div>', '<div class="v">62</div><div class="s">Jeans: 35 vorbestellt + 27 im Drop</div>')
G = rep(G, '<div class="v">9.280 €</div><div class="s">Budget 4.500 € → Lücke 4.780 €</div>', '<div class="v">9.680 €</div><div class="s">Budget 4.500 € → Lücke 5.180 €</div>')
G = rep(G, '<div class="v">10 / 31</div>', '<div class="v">11 / 34</div>')
G = rep(G, "Kapitalbedarf <b>9.280 €</b> gegen 4.500 € Budget. Die Lücke von <b>4.780 €</b>", "Kapitalbedarf <b>9.680 €</b> gegen 4.500 € Budget. Die Lücke von <b>5.180 €</b>")
G = rep(G, "Mindestens <b>10 bis zur Schwelle am 01.02.</b>", "Mindestens <b>11 bis zur Schwelle am 01.02.</b>")
G = rep(G, "mindestens <b>31 bis zur Restzahlung am 19.03.</b>", "mindestens <b>34 bis zur Restzahlung am 19.03.</b>")
G = rep(G, "<p>Zwischen 31 und 35 liegen 4 Paar Puffer. Das ist dünn.", "<p>Zwischen 34 und 35 liegt seit Design v1.5 nur noch 1 Paar Puffer, vorher waren es 4. Das ist zu dünn: keine neue Stickerei ohne Gegenrechnung.")
G = rep(G, "kommen rund 1.100 € Einfuhrumsatzsteuer dazu.", "kommen rund 1.200 € Einfuhrumsatzsteuer dazu.")
G = rep(G, "Unter 10 Vorbestellungen keine Anzahlung", "Unter 11 Vorbestellungen keine Anzahlung")
G = rep(G, '<h2>Das Design · v1.4</h2><span class="note">Freeze als v1.5 am 05.10., nach dem Papiertest.</span>',
        '<h2>Das Design · v1.5</h2><span class="note">Nach Papiertest 1 am 01.10. Papiertest 2 am 02.10., Freeze am 05.10.</span>')
G = rep(G, 'zum Ausdrucken in <span class="mono">NVL_Druckvorlage_1zu1.pdf</span>.',
        'zum Ausdrucken in <span class="mono">NVL_Druckvorlage_v15.pdf</span> (geänderte Teile) und <span class="mono">NVL_Druckvorlage_1zu1.pdf</span> (C und D).')
G = rep(G, "<td>28 mm × ca. 20,4 cm · 21 Stiche hoch, Rapport 16</td>", "<td>23 mm × ca. 20 cm · 17 Stiche hoch, Rapport 16</td>")
G = rep(G, "<td>Münztasche rechts vorn, ganze Fläche</td><td>49 × 49 mm · 37 × 37 Stiche</td>",
        "<td>Münztasche rechts vorn, ganze Fläche. Untere rechte Ecke unter dem Band</td><td>60 × 60 mm auf 62-mm-Tasche · 45 × 45 Stiche</td>")
G = rep(G, "<td><b>Serp mit Garbe</b></td><td>Rechte Gesäßtasche, untere Hälfte. Die Klingenspitze schneidet in die Halme</td><td>ca. 48 × 76 mm</td><td>Gold, Weiß, Rot, Braun</td>",
        "<td><b>Serp schneidet in die Garbe</b></td><td>Linke Gesäßtasche, untere Hälfte. Realistisch: Die Klinge liegt hinter den Halmen, zwei Halme sind durchtrennt</td><td>ca. 44 × 75 mm</td><td>Gold in drei Tönen, zwei Brauntöne, Weiß, Grauweiß, Rot</td>")
G = rep(G, "<td>Rechte Gesäßtasche oben. Fäden hängen unter den Ähren (Variante 2)</td><td>50 × 26 mm · mit Fäden 50 × 43 mm</td>",
        "<td>Linke Gesäßtasche oben. Neun Fäden hängen unter der Linie bis in die Ähren der Garbe</td><td>49 × 25 mm · mit Fäden 49 × 57 mm</td>")
G = rep(G, "<td>Passe hinten links, zwischen den zwei linken Gürtelschlaufen</td><td>36 × 36 mm · 27 × 27 Stiche</td>",
        "<td>Rechte Gesäßtasche, waagerecht mittig, auf Höhe der roten Linie links</td><td>36 × 36 mm · 27 × 27 Stiche</td>")
G = rep(G, "Rund 33.000 Stiche am Teil. Die Goldfäden: 7–9 Stück, 9–16 mm, Polyester, nicht metallisiert,",
        "Rund 40.000 Stiche am Teil. Die Goldfäden: 9 Stück, 18–30 mm, dreifach gezwirnt, Polyester, nicht metallisiert,")
G = rep(G, "<dt>Do 01.10.</dt><dd>Druckvorlage 1:1 drucken, Kontrolllinie auf 100 mm prüfen, fünf Teile ausschneiden.</dd>",
        "<dt>Do 01.10.</dt><dd>Erledigt: gedruckt und Papiertest 1 gemacht, einen Tag früher. Daraus ist Design v1.5 entstanden.</dd>")
G = rep(G, "<dt>Fr 02.10.</dt><dd>Mit Malerkrepp auf deine Jeans, anziehen, 6 Fotos und ein Video an Claude. Das Aufkleben im Zeitraffer ist dein erster Post.</dd>",
        "<dt>Fr 02.10.</dt><dd>Papiertest 2 mit v1.5: nur die geänderten Teile drucken, echte Garnfäden ankleben, 6 Fotos und ein Video an Claude. Das Aufkleben im Zeitraffer ist dein erster Post.</dd>")
G = rep(G, "<dt>Sa 03.10.</dt><dd>Vier Entscheidungen: Band, Patch-Größe, Taschenklappe, Nackenlabel. Claude baut daraus v1.5.</dd>",
        "<dt>Sa 03.10.</dt><dd>Vier Entscheidungen: v1.5 so lassen, Patch-Größe, Taschenklappe, Nackenlabel. Claude baut daraus die Freeze-Version.</dd>")
G = rep(G, "Straight, ehrliche Größen W30–W38. Stückkosten ~62 €.", "Straight, ehrliche Größen W30–W38. Stückkosten ~66 €.")
wr("gen5.py", G)
print("patch51 ok")
