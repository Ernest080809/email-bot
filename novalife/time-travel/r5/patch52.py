# -*- coding: utf-8 -*-
# Docket Rev. 5.2: Design v1.6 (Skizze 07.10.), Papiertest 3 am 08.10., Freeze am 09.10., Tech Pack bis 11.10., Zahlen zurück auf 10/31
import os
H = os.path.dirname(os.path.abspath(__file__))
def rd(f): return open(os.path.join(H, f), encoding="utf-8").read()
def wr(f, s): open(os.path.join(H, f), "w", encoding="utf-8").write(s)
def rep(s, a, b, cnt=1):
    assert s.count(a) == cnt, (a[:90], s.count(a))
    return s.replace(a, b)
def block(s, start, end, new):
    assert s.count(start) == 1, start[:70]
    i = s.index(start); j = s.index(end, i) + len(end)
    return s[:i] + new + s[j:]
TP_PROMPT = ("Bau mir das Tech Pack v1.0 für NVL-TT-01 als PDF auf Englisch, aus produkt-spec.md und der Freeze-Version des Designs: 1 Deckblatt, 2 Flachzeichnungen vorn und hinten mit Maßen, "
             "3 Maßtabelle W30–W38 mit Toleranzen, 4 BOM, 5 Stoff- und Waschspezifikation, 6 Stickspezifikation pro Element A–E mit Platzierung ab Naht, 7 Konstruktion, 8 Labels und Verpackung, 9 Prüfplan. Version 1.0, Datum heute.")

# ======================= r5_a.py =======================
A = rd("r5_a.py")
A = rep(A, "Zeitraffer vom Aufkleben (gefilmt am 02.10.)", "Zeitraffer vom Aufkleben (gefilmt beim Papiertest am 08.10.)")
A = block(A, ' [T("B", "Papiertest 2 mit Design v1.5", 60, [', 'Ist der Alatyr auf der rechten Tasche besser als auf der Passe?")],',
          ' [NOTE("ÜBERHOLT 07.10.: Statt Papiertest 2 hast du per Skizze entschieden: Serp und Garbe runter von der Tasche, drei Ähren auf einem einfach roten Band, dazu ein kleiner Serp im Stoppelfeld an der Seite. Claude hat daraus Design v1.6 gebaut. Papiertest 3 ist am Do 08.10.")],')
A = block(A, ' [T("D", "Design-Entscheidungen treffen", 30, [', 'Bau daraus die Freeze-Version und aktualisiere Canvas, Druckvorlage und Spec.")],',
          ' [NOTE("VERSCHOBEN: Die Entscheidungen triffst du am Do 08.10. zusammen mit Papiertest 3.")],')
A = block(A, ' [T("B", "Tech Pack v1 bei Claude bestellen", 5, [', 'Version 1.0, Datum heute."),\n  REVIEW(3)],',
          ' [NOTE("VERSCHOBEN: Das Tech Pack bestellst du am Fr 09.10. direkt nach dem Freeze."),\n  REVIEW(3)],')
# W4 Mo: Freeze -> Notiz
A = block(A, ' [T("D", "Design-Freeze abnehmen", 30, [', '], "Du hast „Freeze“ geschrieben."),',
          ' [NOTE("VERSCHOBEN auf Fr 09.10.: Du hast am 07.10. noch einmal geändert, Design v1.6. Erst Papiertest 3 am Donnerstag, dann Freeze."),')
# W4 Do: Papiertest 3 anhängen
A = rep(A, 'Sprachregel: Subjekt ist das Muster, nicht das Volk.")],',
        'Sprachregel: Subjekt ist das Muster, nicht das Volk."),\n'
        '  T("B", "Papiertest 3 mit Design v1.6 und fünf Entscheidungen", 45, [\n'
        '    "PDF „NVL_Druckvorlage_v16.pdf“ öffnen (im Chat vom 07.10.). Eine Seite.",\n'
        '    "Drucken: A4 Hochformat, Farbe, „Tatsächliche Größe“ bzw. „100 %“. Kontrolllinie messen, genau 100 mm.",\n'
        '    "Ausschneiden: die linke Gesäßtasche und den kleinen Zettel mit dem Serp.",\n'
        '    "Goldfäden echt machen: 9 Stücke gelbes Garn, 2–3 cm, unterschiedlich lang, direkt unter das rote Band kleben.",\n'
        '    "Handy aufs Regal und das Aufkleben im Zeitraffer filmen. Das ist dein erster Post am 12.10.",\n'
        '    "Hinten: Tasche auf die linke Gesäßtasche, Oberkante an Oberkante. Alatyr C auf die rechte Tasche, auf Höhe des roten Bands. Patch D wie gehabt.",\n'
        '    "Seite: Hose flach hinlegen, Vorderseite oben. Den Serp-Zettel auf das linke Bein, die goldene Zettelkante genau auf die Seitennaht. Höhe 40–50 cm unter der Bundoberkante, am Körper ausprobieren.",\n'
        '    "Vorn: Band A und Münztasche E aus der Druckvorlage v1.5, falls sie noch nicht dran sind.",\n'
        '    "Münztasche deiner Eightyfive messen: Breite oben und Höhe bis dahin, wo sie unter der Vordertasche verschwindet.",\n'
        '    "Anziehen. Aus 3 m und 1 m je ein Foto von vorn, hinten und seitlich, dazu ein Foto von der Seite aus 30 cm. Alles mit dem Prompt unten an Claude.",\n'
        '   ], "Claude hat 7 Fotos, die zwei Maße der Münztasche und deine fünf Antworten.",\n'
        '   "Papiertest 3 mit Design v1.6. Hier sind 7 Fotos. Münztasche meiner Eightyfive: Breite … mm, Höhe … mm. Meine Entscheidungen: Serp an der Seite: ja / nein, Höhe … cm unter dem Bund. Patch D 86 × 76 mm: so lassen / kleiner. Taschenklappe: nein / ja. Nackenlabel für Zipper und Polo als gewebtes Etikett: okay / anders. Beurteile die Fotos und sag mir, ob das Design so in den Freeze kann.")],')
# W4 Fr: Tech-Pack-Prüfung wird zu Freeze + Tech Pack bestellen
A = block(A, ' [T("B", "Tech Pack v1 prüfen und freigeben", 60, [', '], "Tech Pack v1.0 ist freigegeben und liegt als PDF bei dir.")],',
          ' [T("D", "Design-Freeze abnehmen und Tech Pack bestellen", 25, [\n'
          '    "Canvas „Fit-Mockup NVL-TT-01“ öffnen und die Freeze-Version ansehen. Sind deine Antworten von gestern drin?",\n'
          '    "Wenn ja, schreib Claude „Freeze“. Ab jetzt ändert sich am Design nur noch etwas, wenn die Fabrik oder die Stickprobe einen Grund liefern.",\n'
          '    "Wenn nein: die Änderung einmal klar benennen, Claude korrigiert, dann Freeze. Nicht weiter schieben, am Montag gehen die Anfragen raus.",\n'
          '    "Direkt danach den Prompt unten an Claude schicken. Das Tech Pack prüfst du am Sonntag.",\n'
          '   ], "Du hast „Freeze“ geschrieben und das Tech Pack bestellt.",\n'
          f'   "{TP_PROMPT}")],')
# W4 So: Tech-Pack-Prüfung anhängen (nach dem Wochenreview, damit keine Häkchen verrutschen)
i = A.index("W4 = dict("); j = A.index("W5 = dict(") if "W5 = dict(" in A else len(A)
w4 = A[i:j]
assert w4.count("REVIEW(4)") == 1, "REVIEW(4) nicht eindeutig"
k = w4.index("REVIEW(4)") + len("REVIEW(4)")
w4 = (w4[:k] + ',\n  T("B", "Tech Pack v1 prüfen und freigeben", 60, [\n'
      '    "Claudes Tech-Pack-PDF öffnen.",\n'
      '    "Seite für Seite gegen diese Liste: Stilnummer NVL-TT-01? Maße W30–W38 vollständig mit Toleranz? Alle Elemente A–E und B2 mit Maß und Position ab Naht? Garn Polyester? Reihenfolge sticken → nähen → waschen? Goldfäden nach der Wäsche von Hand?",\n'
      '    "Was dir unklar ist, als Frage an Claude, nicht als Änderung.",\n'
      '    "Wenn alles stimmt: „Tech Pack v1 freigegeben“ an Claude. Morgen geht es mit der Anfrage an die Fabriken raus.",\n'
      '   ], "Tech Pack v1.0 ist freigegeben und liegt als PDF bei dir.")' + w4[k:])
A = A[:i] + w4 + A[j:]
wr("r5_a.py", A)

# ======================= r5_b.py =======================
B = rd("r5_b.py")
B = rep(B, "Stichzahl gesamt nahe ~40.000 (Design v1.5)", "Stichzahl gesamt nahe ~30.000 (Design v1.6)")
B = rep(B, "Liegt die Summe deutlich über 40.000:", "Liegt die Summe deutlich über 30.000:")
B = rep(B, "Das ist Teil der Stückkosten von ~66 €", "Das ist Teil der Stückkosten von ~61,50 €")
wr("r5_b.py", B)

# ======================= r5_c.py =======================
C = rd("r5_c.py")
C = rep(C, "Makro auf die Gesäßtasche: Ähren, rote Linie, Fäden, darunter Garbe und Serp. Ein Satz: Ernte. Was geschnitten ist, hängt",
        "Makro auf die Gesäßtasche: drei Ähren, rotes Band, Fäden. Dann Schnitt auf die Seitennaht: der kleine Serp im Stoppelfeld. Ein Satz: Hinten die Ernte, an der Seite das Feld danach")
C = rep(C, "reicht es für mindestens 11?", "reicht es für mindestens 10?")
C = rep(C, "Jedes geschenkte Paar kostet dich ~66 €", "Jedes geschenkte Paar kostet dich ~61,50 €")
C = rep(C, "Vorbestellungen gegen Minimum (11 bis heute).", "Vorbestellungen gegen Minimum (10 bis heute).")
C = rep(C, "Planwert: bei 50/50 ca. 3.150 €, bei 60/40 ca. 3.780 € (Fabrikpreis ~63 € pro Paar",
        "Planwert: bei 50/50 ca. 2.925 €, bei 60/40 ca. 3.510 € (Fabrikpreis ~58,50 € pro Paar")
C = rep(C, "brauchst du mindestens 34 Vorbestellungen.", "brauchst du mindestens 31 Vorbestellungen.")
C = rep(C, "Die Vorbestellung läuft (mindestens 11)", "Die Vorbestellung läuft (mindestens 10)")
wr("r5_c.py", C)

# ======================= r5_d.py =======================
Dd = rd("r5_d.py")
Dd = rep(Dd, ' 21: "Gesäßtasche: Ähren, rote Linie, Garbe und Serp",', ' 21: "Gesäßtasche: drei Ähren, rotes Band, Goldfäden",')
Dd = rep(Dd, ' 6: "Köper des Denims im Seitenlicht",', ' 6: "Seitennaht im Streiflicht: der kleine Serp und die Stoppeln",')
Dd = rep(Dd, ' 3: "Papiertest vom 02.10., hart geschnitten auf das fertige Teil",', ' 3: "Papiertest aus dem Oktober, hart geschnitten auf das fertige Teil",')
Dd = rep(Dd, "der Papiertest-Clip vom 02.10.,", "der Papiertest-Clip aus dem Oktober,")
Dd = rep(Dd, "(Planwert bei 50/50 ca. 3.150 €)", "(Planwert bei 50/50 ca. 2.925 €)")
Dd = rep(Dd, "Hinten links: B mit Ähren, Linie und 9 Goldfäden (sitzen sie fest?). Hinten rechts: Alatyr C. Patch D gerade.",
         "Hinten links: B2 mit drei Ähren, rotem Band und 9 Goldfäden (sitzen sie fest?). Hinten rechts: Alatyr C. Patch D gerade. Linkes Bein: Serp B an der Seitennaht.")
Dd = rep(Dd, "Break-even (62 Paar)", "Break-even (59 Paar)")
wr("r5_d.py", Dd)

# ======================= ref5.py =======================
R = rd("ref5.py")
R = rep(R, ' ("Fr 02.10.", "W3", "Papiertest 2 mit v1.5"),\n ("Mo 05.10.", "W4", "<b>Design-Freeze</b>"),\n ("Fr 09.10.", "W4", "Tech Pack v1.0 freigegeben"),',
        ' ("Mi 07.10.", "W4", "Deine Skizze → Design v1.6"),\n ("Do 08.10.", "W4", "Papiertest 3 mit v1.6"),\n ("Fr 09.10.", "W4", "<b>Design-Freeze</b> · Tech Pack bestellt"),\n ("So 11.10.", "W4", "Tech Pack v1.0 freigegeben"),')
R = rep(R, "mindestens 11 Vorbestellungen bis So 31.01.", "mindestens 10 Vorbestellungen bis So 31.01.")
R = rep(R, "(mindestens 34 Vorbestellungen)", "(mindestens 31 Vorbestellungen)")
R = rep(R, "- 5 embroidery elements (A–E), approx. 40,000 stitches per pair, fine cross-stitch look on a 1.33 mm grid, 8 polyester thread colours (white, light grey, red, three golds, two browns)",
        "- 5 embroidery elements (A–E) on 5 cut-panel zones, one small motif 10 mm from the outseam, approx. 30,000 stitches per pair, fine cross-stitch look on a 1.33 mm grid, 8 polyester thread colours (white, light grey, red, gold, dark gold, straw, two browns)")
R = rep(R, '("B · Serp und Garbe", "Mittig in der unteren Hälfte der linken Gesäßtasche. Klinge weiß, Schneide rot, sie liegt hinter den Halmen, zwei Halme sind durchtrennt. Ähren mit Grannen, Licht und Schatten sichtbar. Kein Stern, kein Hammer, kein roter Grund."),',
        '("B · Serp im Stoppelfeld", "Linkes Bein vorn, 10 mm (±2) neben der Seitennaht, Höhe laut Tech Pack. Klinge weiß, kein Rot. Die Halme als feine Striche sichtbar, nicht zu Punkten verlaufen. Kein Stern, kein Hammer, kein roter Grund."),')
R = rep(R, '("B2 · Ähren und Fäden", "Ähren über der roten Linie. 9 Goldfäden, 18–30 mm lang, dreifach gezwirnt, ungleich verteilt,',
        '("B2 · Ähren und Fäden", "Drei Ähren über dem roten Band, Band 48 mm (±1), einfach rot, Kanten sauber. 9 Goldfäden, 18–30 mm lang, dreifach gezwirnt, ungleich verteilt,')
R = rep(R, "rechte Gesäßtasche, waagerecht mittig, auf Höhe der roten Linie links.", "rechte Gesäßtasche, waagerecht mittig, auf Höhe des roten Bands links.")
R = rep(R, "echter Aufwand: rund 1.200 € auf die Lieferung.", "echter Aufwand: rund 1.100 € auf die Lieferung.")
R = rep(R, '("Stickerei ~40.000 Stiche", "22,00", "~0,55 € pro 1.000 Stiche, Design v1.5"),', '("Stickerei ~30.000 Stiche", "16,50", "~0,55 € pro 1.000 Stiche, Design v1.6"),')
R = rep(R, '("Panel-Handling, 4 Zonen", "4,00", "Vorderteil, Münztasche, beide Gesäßtaschen"),', '("Panel-Handling, 5 Zonen", "5,00", "Vorderteil rechts, Münztasche, beide Gesäßtaschen, Vorderteil links"),')
R = rep(R, '(("<b>Stückkosten</b>", "<b>66,00</b>", "Spec Rev. 11"), "total"),', '(("<b>Stückkosten</b>", "<b>61,50</b>", "Spec Rev. 12"), "total"),')
R = rep(R, '("", "Anzahlung 50 % (100 × ~63 € Fabrikpreis)", "3.150 €", "Feb 27"),', '("", "Anzahlung 50 % (100 × ~58,50 € Fabrikpreis)", "2.925 €", "Feb 27"),')
R = rep(R, '("", "Restzahlung 50 %", "3.150 €", "Mär 27"),', '("", "Restzahlung 50 %", "2.925 €", "Mär 27"),')
R = rep(R, '"<b>9.680 €</b>"', '"<b>9.230 €</b>"')
R = rep(R, '"<b>5.180 €</b>"', '"<b>4.730 €</b>"')
R = rep(R, "Bei 60/40 statt 50/50 steigt die Anzahlung auf ~3.780 €. Gegenüber Design v1.4 sind es +400 € (100 × 4 € mehr Stickerei).",
        "Bei 60/40 statt 50/50 steigt die Anzahlung auf ~3.510 €. Gegenüber Design v1.5 sind es −450 €.")
R = rep(R, '("Mo 01.02. Schwelle", "Anzahlung 3.150 €", "~1.990 €", "~1.160 €", "<b>mindestens 11</b>"),', '("Mo 01.02. Schwelle", "Anzahlung 2.925 €", "~1.990 €", "~935 €", "<b>mindestens 10</b>"),')
R = rep(R, '("Fr 19.03. Restzahlung", "Rest 3.150 €, Shoot, Verpackung, Versandmaterial, Werbung", "0 €", "~4.800–4.950 €", "<b>mindestens 34</b>"),',
        '("Fr 19.03. Restzahlung", "Rest 2.925 €, Shoot, Verpackung, Versandmaterial, Werbung", "0 €", "~4.350–4.500 €", "<b>mindestens 31</b>"),')
R = rep(R, "Zwischen 34 und 35 liegt nur 1 Paar Puffer (vor Design v1.5 waren es 4).", "Zwischen 31 und 35 liegen 4 Paar Puffer.")
R = rep(R, '("<b>Break-even</b>", "35 → 5.215 €", "27 → 4.563 €", "62", "<b>9.778 €</b>"),', '("<b>Break-even</b>", "35 → 5.215 €", "24 → 4.056 €", "59", "<b>9.271 €</b>"),')
R = rep(R, '("abzüglich Stückkosten", "−66,00", "Spec Rev. 11"),', '("abzüglich Stückkosten", "−61,50", "Spec Rev. 12"),')
R = rep(R, '(("<b>Deckungsbeitrag</b>", "<b>65,67</b>", "als Kleinunternehmer 92,65 €, dafür ist die Einfuhrumsatzsteuer Aufwand"), "total"),',
        '(("<b>Deckungsbeitrag</b>", "<b>70,17</b>", "als Kleinunternehmer 97,15 €, dafür ist die Einfuhrumsatzsteuer Aufwand"), "total"),')
R = rep(R, "'<h3>Stückkosten Jeans · ~66 €</h3>'", "'<h3>Stückkosten Jeans · ~61,50 €</h3>'")
R = rep(R, "Kapitalbedarf <b>9.680 €</b>, Budget 4.500 €, Lücke <b>5.180 €</b>.", "Kapitalbedarf <b>9.230 €</b>, Budget 4.500 €, Lücke <b>4.730 €</b>.")
R = rep(R, "Mindestens 11 bis zur Schwelle am 01.02., mindestens 34 bis zur Restzahlung am 19.03. Das Kontingent ist 35, der Puffer also nur 1 Paar. Design v1.5 kostet ~400 € mehr als v1.4.",
        "Mindestens 10 bis zur Schwelle am 01.02., mindestens 31 bis zur Restzahlung am 19.03. Das Kontingent ist 35, der Puffer also 4 Paar.")
R = rep(R, "Schwelle am 01.02.: unter 11 keine Anzahlung,", "Schwelle am 01.02.: unter 10 keine Anzahlung,")
R = rep(R, " Vorschlag, offen: Kontingent von Anfang an 40 statt 35, entscheiden beim Bau der Vorbestellung (Woche 14). Keine neue Stickerei ohne Gegenrechnung.", " Keine neue Stickerei ohne Gegenrechnung.")
R = rep(R, "auf rund 6.300 € Ware echter Aufwand, etwa 1.200 €. Das sind 8–9 Vorbestellungen", "auf rund 5.850 € Ware echter Aufwand, etwa 1.100 €. Das sind 7–8 Vorbestellungen")
wr("ref5.py", R)

# ======================= gen5.py =======================
G = rd("gen5.py")
G = rep(G, "Projekt Slavic · Rev. 5.1 · 01.10.2026", "Projekt Slavic · Rev. 5.2 · 07.10.2026")
G = rep(G, '<span class="k">Stückkosten</span><div class="v">~66 €</div>', '<span class="k">Stückkosten</span><div class="v">~61,50 €</div>')
G = rep(G, '<div class="v">62</div><div class="s">Jeans: 35 vorbestellt + 27 im Drop</div>', '<div class="v">59</div><div class="s">Jeans: 35 vorbestellt + 24 im Drop</div>')
G = rep(G, '<div class="v">9.680 €</div><div class="s">Budget 4.500 € → Lücke 5.180 €</div>', '<div class="v">9.230 €</div><div class="s">Budget 4.500 € → Lücke 4.730 €</div>')
G = rep(G, '<div class="v">11 / 34</div>', '<div class="v">10 / 31</div>')
G = rep(G, "Kapitalbedarf <b>9.680 €</b> gegen 4.500 € Budget. Die Lücke von <b>5.180 €</b>", "Kapitalbedarf <b>9.230 €</b> gegen 4.500 € Budget. Die Lücke von <b>4.730 €</b>")
G = rep(G, "Mindestens <b>11 bis zur Schwelle am 01.02.</b>", "Mindestens <b>10 bis zur Schwelle am 01.02.</b>")
G = rep(G, "mindestens <b>34 bis zur Restzahlung am 19.03.</b>", "mindestens <b>31 bis zur Restzahlung am 19.03.</b>")
G = rep(G, "<p>Zwischen 34 und 35 liegt seit Design v1.5 nur noch 1 Paar Puffer, vorher waren es 4. Das ist zu dünn: keine neue Stickerei ohne Gegenrechnung.",
        "<p>Zwischen 31 und 35 liegen 4 Paar Puffer. Das ist dünn, deshalb gilt: keine neue Stickerei ohne Gegenrechnung.")
G = rep(G, "kommen rund 1.200 € Einfuhrumsatzsteuer dazu.", "kommen rund 1.100 € Einfuhrumsatzsteuer dazu.")
G = rep(G, "Unter 11 Vorbestellungen keine Anzahlung", "Unter 10 Vorbestellungen keine Anzahlung")
G = rep(G, '<h2>Das Design · v1.5</h2><span class="note">Nach Papiertest 1 am 01.10. Papiertest 2 am 02.10., Freeze am 05.10.</span>',
        '<h2>Das Design · v1.6</h2><span class="note">Nach deiner Skizze vom 07.10. Papiertest 3 am 08.10., Freeze am 09.10.</span>')
G = rep(G, 'zum Ausdrucken in <span class="mono">NVL_Druckvorlage_v15.pdf</span> (geänderte Teile) und <span class="mono">NVL_Druckvorlage_1zu1.pdf</span> (C und D).',
        'zum Ausdrucken in <span class="mono">NVL_Druckvorlage_v16.pdf</span> (B2 und B), <span class="mono">NVL_Druckvorlage_v15.pdf</span> (A und E) und <span class="mono">NVL_Druckvorlage_1zu1.pdf</span> (C und D).')
G = rep(G, "<td><b>Serp schneidet in die Garbe</b></td><td>Linke Gesäßtasche, untere Hälfte. Realistisch: Die Klinge liegt hinter den Halmen, zwei Halme sind durchtrennt</td><td>ca. 44 × 75 mm</td><td>Gold in drei Tönen, zwei Brauntöne, Weiß, Grauweiß, Rot</td>",
        "<td><b>Serp im Stoppelfeld</b></td><td>Linkes Bein vorn, 10 mm neben der Seitennaht, Mitte ca. 45 cm unter dem Bund. Kleiner Serp über abgeschnittenen Halmen (Vorschlag, Entscheidung beim Freeze)</td><td>ca. 22 × 35 mm</td><td>Weiß, Grauweiß, zwei Brauntöne, Stroh. Kein Rot</td>")
G = rep(G, "<td><b>Ähren, rote Linie, Goldfäden</b></td>", "<td><b>Drei Ähren, rotes Band, Goldfäden</b></td>")
G = rep(G, "<td>Linke Gesäßtasche oben. Neun Fäden hängen unter der Linie bis in die Ähren der Garbe</td><td>49 × 25 mm · mit Fäden 49 × 57 mm</td><td>Gold, Rot, Weiß</td>",
        "<td>Linke Gesäßtasche, das Band auf Höhe des Alatyr. Neun Fäden hängen unter dem Band</td><td>Band 48 mm · mit Fäden ca. 51 × 56 mm</td><td>Gold, Dunkelgold, Rot</td>")
G = rep(G, "<td>Rechte Gesäßtasche, waagerecht mittig, auf Höhe der roten Linie links</td>", "<td>Rechte Gesäßtasche, waagerecht mittig, auf Höhe des roten Bands links</td>")
G = rep(G, "Rund 40.000 Stiche am Teil.", "Rund 30.000 Stiche am Teil. Rechts das Muster, links die Ernte.")
G = rep(G, '<span class="era">01.–05.10.</span>', '<span class="era">01.–09.10.</span>')
G = rep(G, "<dt>Fr 02.10.</dt><dd>Papiertest 2 mit v1.5: nur die geänderten Teile drucken, echte Garnfäden ankleben, 6 Fotos und ein Video an Claude. Das Aufkleben im Zeitraffer ist dein erster Post.</dd>",
        "<dt>Mi 07.10.</dt><dd>Deine Skizze: Serp und Garbe runter von der Tasche, drei Ähren auf einem roten Band, ein kleiner Serp an der Seite. Claude baut v1.6.</dd>")
G = rep(G, "<dt>Sa 03.10.</dt><dd>Vier Entscheidungen: v1.5 so lassen, Patch-Größe, Taschenklappe, Nackenlabel. Claude baut daraus die Freeze-Version.</dd>",
        "<dt>Do 08.10.</dt><dd>Papiertest 3: eine Seite drucken, echte Garnfäden ankleben, Fotos an Claude, fünf Entscheidungen. Das Aufkleben im Zeitraffer ist dein erster Post.</dd>")
G = rep(G, "<dt>Mo 05.10.</dt><dd>„Freeze“. Danach ändert sich das Design nur noch, wenn Fabrik oder Stickprobe einen Grund liefern.</dd>",
        "<dt>Fr 09.10.</dt><dd>„Freeze“ und Tech Pack bestellen. Danach ändert sich das Design nur noch, wenn Fabrik oder Stickprobe einen Grund liefern.</dd>")
G = rep(G, "Straight, ehrliche Größen W30–W38. Stückkosten ~66 €.", "Straight, ehrliche Größen W30–W38. Stückkosten ~61,50 €.")
wr("gen5.py", G)
print("patch52 ok")
