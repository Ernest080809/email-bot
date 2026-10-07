# -*- coding: utf-8 -*-
# Video-Bibliothek Time Travel (Rev. 6). Daten fuer gen_content.py
# Felder: id, date (ISO oder None), time, slot, fmt, title, hook_en, hook_de, alt_en,
#         shots[], ort, dauer, ton, cap (Caption EN ohne CTA), cta, check[], docket, phase (nur Reserve)

W = "Wohnung · Schreibtisch, Draufsicht (Handy auf Stativ oder Bücherstapel), Fensterlicht von der Seite"
FENSTER = "Wohnung · Fensterbank, Tageslicht (Gold und Stoffstruktur brauchen Licht von der Seite)"
SPIEGEL = "Wohnung · Flurspiegel, Ganzkörper, Licht von vorn"
WAND = "Wohnung · weiße Wand oder Tür, Hose auf Bügel, Streiflicht vom Fenster"
MAC = "Mac · Bildschirmaufnahme (Cmd + Shift + 5), dazu Gesicht/Hände am Schreibtisch"
BODEN = "Wohnung · Boden-Flatlay auf hellem Laken, Draufsicht"
HOF = "Berlin · Hinterhof oder Treppenhaus mit Fensterlicht (keine Sowjet-/DDR-Monumentalkulisse, keine Flaggen im Bild)"
FELD = "Berlin · Tempelhofer Feld oder offene Wiese bei Sonnenuntergang (Öffnungszeiten vor Ort prüfen; Himmel orange/violett, nie Blau über Gelb)"
ARCHIV = "Archiv-Clips aus früheren Drehs (Ordner content/archiv)"
SHOOT = "Material vom Shoot Sa 20.02.2027 + Makros zu Hause (gedreht am Do 18.03. und Sa 20.03.)"

S_ASMR = "Originalton (Papier, Schere, Nadel, Stoff). Keine Musik oder sehr leise"
S_OTON = "O-Ton (deine Stimme) + Untertitel. Musik nur leise aus der Business-Bibliothek der jeweiligen App"
S_TREND = "Trend-Sound aus der TikTok Commercial Music Library (Creative Center, Region DE, „für Business freigegeben“). Instagram: Musik aus der Business-Bibliothek der App"
S_RUHIG = "Ruhiger Track aus der Business-Bibliothek der App, darunter Originalton"
S_KEINE = "kein Ton (Story-Sticker)"

E = []

def v(**k):
    E.append(k)

# ---------------- P1 PROZESS (bis 02.12.) ----------------
v(id="V001", date="2026-10-12", time="18:00", slot="BUILD", fmt="Video 9:16", title="Papier, bevor es Garn wird",
  hook_en="Before I spend €6,000, I tape paper to my jeans.",
  hook_de="Bevor ich 6.000 € ausgebe, klebe ich Papier auf meine Jeans.",
  alt_en="Day {day} of building a 100-pair jeans drop.",
  shots=["Zeitraffer von oben: Druckvorlage ausschneiden (Schere, Lineal, Malerkrepp)",
         "Hände kleben das Papierband an die rechte Vordertasche der Eightyfive",
         "Flurspiegel von vorn: einmal drehen, Hose mit allen Papierteilen",
         "Makro: Papierband an der Taschenkante, ein Finger fährt entlang",
         "Endkarte: „100 jeans. One pattern. 22.04.2027“"],
  ort="Wohnung · Schreibtisch + Flurspiegel. Material kommt vom Papiertest 3 am Do 08.10. (dort filmen, Shotliste in Abschnitt 4.1)",
  dauer="20–25 s", ton=S_ASMR,
  cap="Day {day}. Before a factory sews a single stitch, I test every embroidery as paper on my own jeans. 100 pairs, numbered. Drop 22.04.2027.",
  cta="LIST", check=["Spiegel nur von vorn oder hinten, nie seitlich mit Serp (B) und Ähren-Tasche (B2) im selben Bild"],
  docket="Rev 5.3 W5 Mo · BUILD „Papier, bevor es Garn wird“")

v(id="V002", date="2026-10-14", time="18:00", slot="ORIGIN", fmt="Video 9:16 (alternativ Karussell)", title="Jede Region stickt die Raute anders",
  hook_en="Every region stitches this diamond differently. The meaning stays.",
  hook_de="Jede Region stickt diese Raute anders. Die Bedeutung bleibt.",
  alt_en="This diamond means the same everywhere: a sown field.",
  shots=["Du am Schreibtisch, O-Ton: drei Sätze aus deiner Herkunftsgeschichte (Woche 2)",
         "Hand zeichnet die Raute Kästchen für Kästchen auf ausgedrucktes 1,33-mm-Raster",
         "Eigene Fotos von Familien-Textilien (Tischdecke, Handtuch), nur eigene Bilder",
         "Schnitt auf die Raute im Papierband an der Hose"],
  ort=W, dauer="25–40 s", ton=S_OTON,
  cap="The diamond is one of the oldest motifs in folk cross-stitch. Every region draws it a little differently. The meaning stays: a sown field. It is the first motif on my jeans.",
  cta="LIST", check=["Ersetzt den Hook „Älter als jede Grenze“ (kann wie „Grenzen sind künstlich“ klingen, zielgruppe.md 3.7, [Q25])", "Keine Landkarte, keine Länderliste im Bild"],
  docket="Rev 5.3 W5 Mi · ORIGIN „Älter als jede Grenze“ (Hook ersetzt)")

v(id="V003", date="2026-10-16", time="18:00", slot="REAL", fmt="Video 9:16", title="Die Zahlen",
  hook_en="My budget: €4,500. My plan costs €9,380.",
  hook_de="Mein Budget: 4.500 €. Mein Plan kostet 9.380 €.",
  alt_en="Here's exactly what 100 embroidered jeans cost me.",
  shots=["Hand schreibt mit Edding auf weißes Blatt: 100 jeans · €9,380 · €4,500",
         "Darunter: gap €4,880, Pfeil auf das Wort gap",
         "Schnitt auf Kalenderblatt „14.01.“",
         "Du in die Kamera: „Pre-orders close the gap. Or this drop doesn't happen.“"],
  ort=W, dauer="20–30 s", ton=S_OTON,
  cap="Building in public means showing the numbers. Making and launching 100 jeans costs €9,380. I have €4,500. Pre-orders from 14.01. close the gap.",
  cta="LIST", check=["Zahlen aus Plan Rev. 5.3. Vor dem Post mit Rev. 6 abgleichen"],
  docket="Rev 5.3 W5 Fr · REAL „Die Zahlen“")

v(id="V004", date="2026-10-19", time="18:00", slot="BUILD", fmt="Video 9:16", title="Der Bauplan (Tech Pack)",
  hook_en="This document decides if my jeans will exist.",
  hook_de="Dieses Dokument entscheidet, ob es meine Jeans geben wird.",
  alt_en="Day {day}: what a factory needs before it says yes.",
  shots=["Bildschirmaufnahme: Tech-Pack-PDF durchscrollen (Maßtabelle, technische Flachzeichnung)",
         "Zoom auf eine Zeile: „W32 = 81 cm“",
         "Ausgedruckte Seite mit Kugelschreiber-Notizen, Hand blättert",
         "Ordner „to factory“ auf dem Desktop"],
  ort=MAC, dauer="20–30 s", ton=S_OTON,
  cap="Day {day}. A tech pack is the blueprint a factory works from: measurements, fabric, wash, every stitch position. Mine: five sizes, five embroideries.",
  cta="LIST", check=["Nur technische Flachzeichnung, kein fotorealistisches Rendering", "Keine Fabriknamen"],
  docket="Rev 5.3 W6 Mo · BUILD „Der Bauplan“")

v(id="V005", date="2026-10-21", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Die Drei-von-vier-Regel",
  hook_en="A motif only gets in if three traditions share it.",
  hook_de="Ein Motiv kommt nur rein, wenn drei Traditionen es teilen.",
  alt_en="I have one rule for every stitch on these jeans.",
  shots=["Vier Stapel Notizkarten, beschriftet nur mit 1–4 (keine Flaggen, keine Karten)",
         "Hand legt die Rauten-Karte auf drei Stapel, Haken",
         "Eine Karte fliegt raus (Motiv nur in einer Tradition belegt), Kreuz",
         "Schnitt auf Papierband an der Hose"],
  ort=W, dauer="25–35 s", ton=S_OTON,
  cap="My rule: a motif goes on the jeans only if it appears with the same meaning in at least three of four textile traditions (Belarus, Poland, Russia, Ukraine). The diamond, the eight-point star and the zigzag passed. A lot didn't.",
  cta="LIST", check=["Länder nur in der Caption und alphabetisch", "Nur posten, wenn die Belegtabelle (Spec Teil 5) steht. Sonst Hook nicht behaupten"],
  docket="Rev 5.3 W6 Mi · ORIGIN „Die Raute“ (Thema getauscht, Raute lief in V002)")

v(id="V006", date="2026-10-23", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Feiner Kreuzstich",
  hook_en="One stitch is 1.33 millimeters. There are about 33,000.",
  hook_de="Ein Stich ist 1,33 Millimeter. Es sind etwa 33.000.",
  alt_en="Why my embroidery isn't pixelated anymore.",
  shots=["Makro: Lineal neben ausgedrucktem Raster von Band A (17 Stiche hoch)",
         "Altes 4-mm-Raster und neues 1,33-mm-Raster nebeneinander",
         "Du stickst fünf Kreuzstiche von Hand auf Stickstoff (Nadel-ASMR)",
         "Text: „~33,000 stitches per pair (estimate)“"],
  ort=W + ". Schreibtischlampe seitlich für Makro", dauer="12–20 s", ton=S_ASMR,
  cap="Version 1 used 4 mm squares and looked pixelated. Now one cross-stitch is 1.33 mm, a third of the size. About 33,000 stitches per pair, an estimate until the digitizer counts.",
  cta="LIST", check=["Stichzahl als Schätzung gekennzeichnet", "Handgestickte Übung ist Prozess, kein Produkt"],
  docket="Rev 5.3 W6 Fr · DETAIL „Feiner Kreuzstich“")

v(id="V007", date="2026-10-26", time="18:00", slot="BUILD", fmt="Video 9:16", title="8 Fabriken angeschrieben",
  hook_en="I emailed 8 factories. Here's who answered.",
  hook_de="Ich habe 8 Fabriken angeschrieben. Das sind die Antworten.",
  alt_en="Day {day}: finding a factory that embroiders denim.",
  shots=["Bildschirmaufnahme Postfach, Absender und Namen verpixelt",
         "Strichliste auf Papier: written 8 · answered X · panel embroidery in-house Y",
         "Du, ein Satz: „Denim AND embroidery on the cut panel, in-house.“",
         "Endkarte: „Calls this week“"],
  ort=MAC, dauer="20–30 s", ton=S_OTON,
  cap="Day {day}. The question that filters most factories out: can you embroider on the cut panel before sewing, in your own house? Big embroidery doesn't fit on a sewn leg. Answers so far: [X] of 8.",
  cta="LIST", check=["Fabriknamen, Logos, E-Mail-Adressen unkenntlich", "Nur echte Zahlen"],
  docket="Rev 5.3 W7 Mo · BUILD „8 Fabriken angeschrieben“")

v(id="V008", date="2026-10-28", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Die Goldfäden",
  hook_en="Nine gold threads leave the pocket. Here's why.",
  hook_de="Neun Goldfäden verlassen die Tasche. Darum.",
  alt_en="The one detail a machine can't do on my jeans.",
  shots=["Spule Goldgarn in der Hand (oder normales Stickgarn, falls das echte noch fehlt)",
         "Papiervorlage linke Gesäßtasche (B2) mit 9 aufgeklebten Fadenstücken",
         "Lineal misst 19, 25, 30 mm",
         "Hand schwingt die Papiertasche, die Fäden bewegen sich",
         "O-Ton: „Hand-set after the wash. Every pair.“"],
  ort=FENSTER, dauer="20–30 s", ton=S_OTON,
  cap="Under three wheat ears: nine gold threads, 18 to 30 mm, set by hand after the wash, because an industrial washer would eat them. It's the moment of the whole design.",
  cta="LIST", check=["Papier, kein fertiges Teil", "Immer drei Ähren, nie „fünf“ (zielgruppe.md 3.6, [Q26])"],
  docket="Rev 5.3 W7 Mi · ORIGIN „Die Goldfäden“")

v(id="V009", date="2026-10-30", time="18:00", slot="REAL", fmt="Video 9:16", title="Was eine Jeans kostet",
  hook_en="What one embroidered jeans costs me to make.",
  hook_de="Was mich eine bestickte Jeans in der Herstellung kostet.",
  alt_en="€169 sounds expensive. Here's the math.",
  shots=["Handschrift, Posten für Posten: base jeans ~€35 · embroidery ~€18 · patch ~€3 · gold threads ~€2 · handling ~€5",
         "Strich darunter: ~€63",
         "Du: „Estimate. The real number comes with the stitch count.“"],
  ort=W, dauer="25–35 s", ton=S_OTON,
  cap="My estimate per pair: about €63 to make. Base jeans ~€35, embroidery ~€18, patch ~€3, gold threads ~€2, handling ~€5. The real number comes when the digitizer counts the stitches.",
  cta="LIST", check=["Zahlen aus Spec 3.11, als Schätzung markiert", "Fabrikpreis öffentlich: deine Entscheidung"],
  docket="Rev 5.3 W7 Fr · REAL „Was eine Jeans kostet“")

v(id="V010", date="2026-11-02", time="18:00", slot="BUILD", fmt="Video 9:16", title="Die Fabrik steht",
  hook_en="Day {day}: I picked one factory out of eight.",
  hook_de="Tag {day}: Ich habe mich für eine von acht Fabriken entschieden.",
  alt_en="Three video calls. One factory. Here's how I chose.",
  shots=["Call-Screen: nur dein Gesicht, Fabrikfenster verpixelt (Name/Bild nur mit schriftlicher Erlaubnis)",
         "Bewertungsraster auf Papier: 5 Kriterien × 3 Fabriken, Punkte",
         "Land als Text, kein Name",
         "Du: „Next: samples.“"],
  ort=MAC, dauer="25–35 s", ton=S_OTON,
  cap="Day {day}. 8 requests, 3 calls, 1 factory. My criteria: denim and panel embroidery in-house, photos of past work, 50/50 payment, dates in writing. Name and photos once they say yes.",
  cta="LIST", check=["Fabrik-Bilder und -Namen nur mit schriftlicher Erlaubnis", "Wenn die Validierung vom 01.11. gut lief: echte Listen-Zahl nennen"],
  docket="Rev 5.3 W8 Mo · BUILD „Die Fabrik steht“")

v(id="V011", date="2026-11-04", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Der Achtstern",
  hook_en="This eight-point star stands for the sun.",
  hook_de="Dieser Achtstern steht für die Sonne.",
  alt_en="27 by 27 stitches. One star. Zero curves.",
  shots=["Zeitraffer: Hand zeichnet den Stern Kästchen für Kästchen (27 × 27)",
         "Makro auf die Mitte (ungerade Zahl = echte Mitte)",
         "Papierstück auf der rechten Gesäßtasche",
         "Text: „right back pocket“"],
  ort=W, dauer="15–25 s", ton=S_ASMR,
  cap="In many textile traditions the eight-point star stands for the sun. Mine is 27 × 27 cross-stitches, 36 mm, only straight lines and diagonals. Odd numbers, so it has a true centre.",
  cta="LIST", check=["Nach außen „eight-point star“, nicht „Alatyr“ (Vorschlag zielgruppe.md 3.5, [Q23], du entscheidest)", "Keine Haken- oder Drehformen (Spec 3.10)"],
  docket="Rev 5.3 W8 Mi · ORIGIN „Der achtstrahlige Stern“")

v(id="V012", date="2026-11-06", time="18:00", slot="REAL", fmt="Video 9:16", title="Ein einziges Thema",
  hook_en="I killed two of my three themes. Here's why.",
  hook_de="Ich habe zwei meiner drei Themen gestrichen. Darum.",
  alt_en="Three themes on one drop is three drops.",
  shots=["Drei Papierstapel auf dem Tisch, zwei wandern in eine Kiste mit Aufschrift „Drop 2“",
         "Du: „Three themes = triple content, triple research, same 100 pieces.“",
         "Ein Stapel bleibt liegen"],
  ort=W, dauer="20–30 s", ton=S_OTON,
  cap="In September I had three embroidery themes for one pair of jeans. Three themes on one drop are three drops on the same day. I kept one. The others are parked, not deleted.",
  cta="LIST", check=["Keine Bilder der geparkten Themen, keine Namen möglicher Partner (Gmail-Entwürfe bleiben unversendet)"],
  docket="Rev 5.3 W8 Fr · REAL „Ein einziges Teil“")

v(id="V013", date="2026-11-09", time="18:00", slot="BUILD", fmt="Video 9:16", title="Muster als Maschinen-Code",
  hook_en="My pattern just became machine code.",
  hook_de="Mein Muster ist gerade Maschinen-Code geworden.",
  alt_en="Day {day}: the real stitch count is in.",
  shots=["Bildschirmaufnahme der Digitizing-Vorschau (Stichsimulation auf weißem Grund, keine Hose)",
         "Echte Stichzahl groß einblenden",
         "Vergleich: estimate ~33,000 vs. real [ZAHL]",
         "Deine Reaktion, ein Satz"],
  ort=MAC, dauer="15–25 s", ton=S_OTON,
  cap="Day {day}. A digitizer turns a drawing into a stitch file: every needle point, every colour change. My estimate was ~33,000 stitches. The real count: [ZAHL].",
  cta="LIST", check=["Nur Stichsimulation, kein Garment-Mockup", "Datei nur mit Erlaubnis des Digitizers zeigen", "Echte Zahl"],
  docket="Rev 5.3 W9 Mo · BUILD „Muster als Maschinen-Code“")

v(id="V014", date="2026-11-11", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Der Lebensbaum",
  hook_en="Roots, trunk, crown: the patch on my waistband.",
  hook_de="Wurzeln, Stamm, Krone: der Patch an meinem Bund.",
  alt_en="Ten twisted strands make this tree's trunk.",
  shots=["Deine Referenz-Skizze des Baums auf dem Tisch (eigene Zeichnung)",
         "Finger fährt Wurzeln → Stamm → Krone nach",
         "Papierausschnitt 86 × 76 mm am Bund (Papiertest)",
         "Text: „natural linen · gold · brown · red“"],
  ort=W, dauer="15–25 s", ton=S_RUHIG,
  cap="The tree of life sits on the back waistband: 86 × 76 mm on natural linen, a trunk of ten twisted strands, roots in a circle. Made as a patch by a specialist.",
  cta="LIST", check=["Nie „Slavic tree of life“ (Spec 3.2)", "Patch-Muster kommen erst um den 13.11.: bis dahin nur Papier und Skizze"],
  docket="Rev 5.3 W9 Mi · ORIGIN „Der Lebensbaum“")

v(id="V015", date="2026-11-13", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Zickzack",
  hook_en="This zigzag means water. It runs along my pocket.",
  hook_de="Dieser Zickzack bedeutet Wasser. Er läuft an meiner Tasche entlang.",
  alt_en="17 stitches high. 23 millimeters. One pocket edge.",
  shots=["Makro Raster von Band A, Finger folgt dem Zickzack",
         "Papierband an der Kante der rechten Vordertasche",
         "Lineal: 23 mm"],
  ort=FENSTER, dauer="8–15 s", ton=S_ASMR,
  cap="Zigzag = water. It frames the cross-stitch band on the right front pocket: 23 mm, 17 stitches high. White next to red, so it reads from three metres.",
  cta="LIST", check=["Papier, kein fertiges Teil"],
  docket="Rev 5.3 W9 Fr · DETAIL „Zickzack“")

v(id="V016", date="2026-11-16", time="18:00", slot="BUILD", fmt="Video 9:16", title="Die erste Stickprobe",
  hook_en="First time my pattern exists in thread.",
  hook_de="Zum ersten Mal gibt es mein Muster in Garn.",
  alt_en="Day {day}: the first stitch-out arrived.",
  shots=["Umschlag öffnen (Paket-ASMR)",
         "Stickprobe auf Denim-Stück, Makro, Finger über die Stiche",
         "Rückseite der Probe mit Stabilisator",
         "Neben der Papiervorlage"],
  ort=FENSTER, dauer="15–25 s", ton=S_ASMR,
  cap="Day {day}. A stitch-out is a test patch: my pattern on a scrap of real denim. Tomorrow it goes in the wash. If it doesn't survive, no prototype gets sewn.",
  cta="LIST", check=["Stickprobe ist Prozess, kein fertiges Teil (Plan erlaubt Stickproben)"],
  docket="Rev 5.3 W10 Mo · BUILD „Die erste Stickprobe“")

v(id="V017", date="2026-11-18", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Der Teppich",
  hook_en="This carpet hung on so many walls. Remember it?",
  hook_de="Dieser Teppich hing an so vielen Wänden. Erinnerst du dich?",
  alt_en="Send this to someone whose grandma had one.",
  shots=["Familienfoto mit Teppich im Hintergrund (nur eigenes Foto, Gesichter nur mit Einverständnis)",
         "Wenn der echte Teppich erreichbar ist: langsamer Schwenk über Medaillon und Rahmen",
         "Hand zeichnet das Medaillon auf Rasterpapier ab",
         "Text: „It's going on the back of a zipper.“"],
  ort="Familie · Wohnung mit Teppich, oder dein Fotoalbum + Schreibtisch", dauer="20–35 s", ton=S_OTON,
  cap="Wall carpets hung in a lot of homes in the region: for warmth, against noise, and because they were precious. [Nur wenn wahr: Ours too.] Its medallion is becoming the back of the zipper.",
  cta="LIST", check=["Subjekt ist der Teppich", "Kein „sowjetisch“, kein CCCP, keine Sowjet-Deko im Bild (zielgruppe.md 3.6)", "Vom Mi 25.11. vorgezogen: in der Woche 23.–29.11. kein Ernte- oder Sichel-Post (Holodomor-Gedenktag Sa 28.11., [Q26])", "Familien-Aussagen nur, wenn sie stimmen"],
  docket="Rev 5.3 W11 Mi · ORIGIN „Der Teppich“ (auf W10 Mi vorgezogen)")

v(id="V018", date="2026-11-20", time="18:00", slot="REAL", fmt="Video 9:16", title="Was die Wäsche mit der Stickprobe macht",
  hook_en="What the wash did to my first stitch-out.",
  hook_de="Was die Wäsche mit meiner ersten Stickprobe gemacht hat.",
  alt_en="I'll show you my mistake before you buy anything.",
  shots=["Vorher und nachher nebeneinander",
         "Makro auf Wellen, Einzug, Fransen (falls da)",
         "Lineal: Einzug in mm",
         "Du: „What changes: [ein Satz].“"],
  ort=FENSTER, dauer="20–30 s", ton=S_OTON,
  cap="Washed vs. unwashed. [Befund in einem Satz]. That's why you test before making 100 pairs, not after.",
  cta="LIST", check=["Echtes Ergebnis, auch wenn es schlecht ist"],
  docket="Rev 5.3 W10 Fr · REAL „Was an der Stickprobe falsch war“")

v(id="V019", date="2026-11-23", time="18:00", slot="BUILD", fmt="Video 9:16", title="Drei Stoffe",
  hook_en="Three denims. Only one becomes my jeans.",
  hook_de="Drei Denims. Nur einer wird meine Jeans.",
  alt_en="Day {day}: 12 oz or 13 oz? Hear the difference.",
  shots=["Drei Stoffmuster nebeneinander",
         "Hand knüllt jedes Muster (Stoff-ASMR)",
         "Gegenlicht am Fenster: Dichte",
         "Lab Dips nebeneinander (Ziel, heller, dunkler)",
         "Finger tippt auf den Gewinner"],
  ort=FENSTER, dauer="15–25 s", ton=S_ASMR,
  cap="Day {day}. 100% cotton, rigid, no stretch. Three swatches, three wash tones. The dark one wins, because white thread needs contrast to read from three metres.",
  cta="LIST", check=["Woche 23.–29.11.: kein Ernte- oder Sichel-Motiv im Bild (zielgruppe.md 3.7)"],
  docket="Rev 5.3 W11 Mo · BUILD „Drei Stoffe“")

v(id="V020", date="2026-11-25", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Warum Panel-Stickerei",
  hook_en="Why you can't embroider a finished pair of jeans.",
  hook_de="Warum man eine fertige Jeans nicht groß besticken kann.",
  alt_en="The embroidery happens before the jeans exist.",
  shots=["Alte Jeans: Hand im Hosenbein zeigt die Röhre",
         "Papierschnitt eines Vorderteils flach auf dem Tisch",
         "Papiermotiv auf das flache Teil legen",
         "Text: „embroider flat → sew → wash“"],
  ort=BODEN, dauer="20–30 s", ton=S_OTON,
  cap="Large embroidery doesn't fit in the hoop on a sewn leg. It goes on the flat cut panel first, then the jeans get sewn and washed. That's why most factories said no.",
  cta="LIST", check=["Vom Mi 18.11. hierher getauscht: technisches Thema statt Teppich in der Woche vor dem 28.11."],
  docket="Rev 5.3 W10 Mi · ORIGIN „Warum Panel-Stickerei“ (auf W11 Mi verschoben)")

v(id="V021", date="2026-11-27", time="18:00", slot="REAL", fmt="Video 9:16", title="Warum 169 €",
  hook_en="Why my jeans cost €169, line by line.",
  hook_de="Warum meine Jeans 169 € kostet, Zeile für Zeile.",
  alt_en="€169 for jeans? Let me show you the math.",
  shots=["Papier: €169 → ~€63 to make (estimate)",
         "Darunter: payment fees, shipping, returns, next drop",
         "Text: „pre-order: €149“"],
  ort=W, dauer="25–35 s", ton=S_OTON,
  cap="€169. About €63 goes into making it (estimate). The rest pays fees, shipping, returns and the next drop. People on the list can pre-order at €149 from 14.01.",
  cta="LIST", check=["Keine fremden Marken im Preisvergleich", "Sa 28.11. (Holodomor-Gedenktag, [Q26]): kein Post"],
  docket="Rev 5.3 W11 Fr · REAL „Warum 169 €“")

v(id="V022", date="2026-11-30", time="18:00", slot="BUILD", fmt="Video 9:16", title="Sie ist unterwegs",
  hook_en="Day {day}: my first prototype is on its way.",
  hook_de="Tag {day}: Mein erster Prototyp ist unterwegs.",
  alt_en="Thursday I hold the first pair. Nervous.",
  shots=["Sendungsverfolgung am Handy, Nummer verpixelt",
         "Kalender, Do 03.12. umkringelt",
         "Leerer Platz auf dem Tisch, Maßband und Papiervorlagen daneben",
         "Du: „Thursday.“"],
  ort=W, dauer="10–15 s", ton=S_RUHIG,
  cap="Day {day}. No photos yet. My rule: I only show what exists. On Thursday it exists.",
  cta="LIST", check=["Kein Produktbild"],
  docket="Rev 5.3 W12 Mo · BUILD „Sie ist unterwegs“")

v(id="V023", date="2026-12-01", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Warum ein Sample",
  hook_en="I won't show you the jeans before I hold them.",
  hook_de="Ich zeige dir die Jeans nicht, bevor ich sie in der Hand halte.",
  alt_en="Design first. Sample second. Showing it third.",
  shots=["Du in die Kamera am Schreibtisch",
         "Drei Karten: „1 design ✓ · 2 sample … · 3 show“",
         "Schnitt auf einen Papiertest-Clip vom Oktober"],
  ort=W, dauer="15–25 s", ton=S_OTON,
  cap="My order of work: finish the design, buy a sample, only then show the product. No renders pretending to be real.",
  cta="LIST", check=["Kein Mockup"],
  docket="Rev 5.3 W12 Di · ORIGIN „Warum ein Sample“")

v(id="V024", date="2026-12-02", time="19:00", slot="REACH", fmt="Video 9:16", title="Donnerstag",
  hook_en="Tomorrow paper becomes thread.",
  hook_de="Morgen wird aus Papier Garn.",
  alt_en="Two months of paper. Tomorrow: the real thing.",
  shots=["Schnelle Schnitte über alle Papierteile (A, E, B, B2, C, D), je 0,5 s, B und B2 in getrennten Einstellungen",
         "Letzter Frame: „Thu.“"],
  ort=ARCHIV, dauer="6–10 s", ton=S_TREND,
  cap="Thursday.",
  cta="LIST", check=["Nur Papier"],
  docket="Rev 5.3 W12 Mi · REACH „Donnerstag“")

# ---------------- P2 AB PROTO (03.12.–13.01.) ----------------
v(id="V025", date="2026-12-03", time="19:00", slot="BUILD", fmt="Video 9:16", title="Unboxing des Prototyps (NEU)",
  hook_en="Two months of paper. This is the first real pair.",
  hook_de="Zwei Monate Papier. Das ist das erste echte Paar.",
  alt_en="Unboxing the prototype of my own jeans.",
  shots=["Paket auf dem Tisch, Cutter schneidet das Klebeband (ASMR)",
         "Hände ziehen die Jeans heraus, erst die Rückseite mit den Goldfäden",
         "Deine echte Reaktion, nicht gespielt, nicht wiederholt",
         "Makro Band A",
         "Endkarte: „fit test Saturday“"],
  ort=FENSTER, dauer="20–40 s", ton="Originalton, keine Musik (die echte Reaktion trägt)",
  cap="Prototype #1. Not perfect yet. Fit test on Saturday, then a list of fixes for the factory.",
  cta="LIST", check=["Ab jetzt erlaubt: echtes Teil", "Im Bild und Text klar „prototype“, nicht Endprodukt", "Fabrik nicht nennen ohne Erlaubnis", "Filme das Auspacken am 03.12. sofort, egal ob du postest"],
  docket="NEU · Do 03.12. 19:00 (zusätzlich zum Plan, der wichtigste Clip der Phase)")

v(id="V026", date="2026-12-04", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Echter Kreuzstich",
  hook_en="Real cross-stitch on denim. Look closer.",
  hook_de="Echter Kreuzstich auf Denim. Schau genauer hin.",
  alt_en="I zoomed in until you can count the stitches.",
  shots=["Totale aus 3 m: Hose auf Bügel an der Tür",
         "Langsam auf 30 cm heranfahren",
         "Makro Band A, dann Münztasche E"],
  ort=WAND, dauer="8–15 s", ton=S_RUHIG,
  cap="Red and white cross-stitch along the pocket edge and on the coin pocket. 1.33 mm per stitch.",
  cta="LIST", check=["Nach außen „cross-stitch band“, nicht „Vyshyvanka“ (Vorschlag zielgruppe.md 3.5, [Q24])"],
  docket="Rev 5.3 W12 Fr · DETAIL „Echter Kreuzstich“")

v(id="V027", date="2026-12-05", time="12:00", slot="ASK", fmt="Story (3 Frames)", title="Was zuerst?",
  hook_en="Which detail should I film first?",
  hook_de="Welches Detail soll ich zuerst filmen?",
  alt_en="Pick one. I film it tomorrow.",
  shots=["Frame 1: Foto der Rückseite", "Frame 2: Umfrage-Sticker mit 4 Antworten: band · coin pocket · gold threads · star", "Frame 3 (abends): Ergebnis + „filming it Sunday“"],
  ort="Wohnung", dauer="3 Story-Frames", ton=S_KEINE,
  cap="(Story, keine Caption)", cta="STORY", check=["Umfrage-Sticker bis 4 Antworten (zielgruppe.md Q62)"],
  docket="Rev 5.3 W12 Sa · ASK „Was zuerst?“")

v(id="V028", date="2026-12-07", time="18:00", slot="BUILD", fmt="Video 9:16", title="Was nicht gepasst hat",
  hook_en="Day {day}: what's wrong with my prototype.",
  hook_de="Tag {day}: Was an meinem Prototyp nicht stimmt.",
  alt_en="I'll show you my mistakes before you buy.",
  shots=["Ganzkörper im Spiegel von vorn, Proto getragen",
         "Maßband am Oberschenkel (Entscheidung 28 oder 30 cm Halbmaß)",
         "Makro auf die Problemstelle",
         "Korrekturliste auf Papier „to factory“"],
  ort=SPIEGEL, dauer="25–35 s", ton=S_OTON,
  cap="Day {day}. Fit test done. What changes before the final sample: [Liste]. Better you see this now than get it in April.",
  cta="LIST", check=["Echte Befunde", "Spiegel nur von vorn: Serp und Ähren-Tasche nicht im selben Bild"],
  docket="Rev 5.3 W13 Mo · BUILD „Was nicht gepasst hat“")

v(id="V029", date="2026-12-08", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Das Band in echt",
  hook_en="This band was paper in October.",
  hook_de="Dieses Band war im Oktober aus Papier.",
  alt_en="Same pocket. Paper then, thread now.",
  shots=["Match-Cut: Papierband an der Tasche (Oktober-Clip), gleiche Einstellung mit echtem Band",
         "Makro",
         "Finger fährt das Band entlang"],
  ort="Gleiche Stelle und gleiches Licht wie beim Papiertest (Wohnung)", dauer="8–12 s", ton=S_TREND,
  cap="October: paper and tape. December: 23 mm of red and white cross-stitch on the pocket edge.",
  cta="LIST", check=["Nach außen „cross-stitch band“"],
  docket="Rev 5.3 W13 Di · ORIGIN „Das Band in echt“")

v(id="V030", date="2026-12-09", time="19:00", slot="REACH", fmt="Video 9:16", title="Uhrwerk",
  hook_en="From three metres: dots. From thirty centimetres: clockwork.",
  hook_de="Aus drei Metern: ein paar Punkte. Aus dreißig Zentimetern: ein Uhrwerk.",
  alt_en="Walk toward my jeans. Watch what happens.",
  shots=["Ein Take: Handy startet 3 m entfernt, Person mit Proto geht langsam auf die Kamera zu",
         "Endet im Makro auf der Münztasche E"],
  ort=HOF, dauer="7–10 s", ton=S_TREND,
  cap="The design rule: wearable from far away, a clock up close.",
  cta="LIST", check=["Ersetzt „Älter als jede Grenze“ (zielgruppe.md 3.7)"],
  docket="Rev 5.3 W13 Mi · REACH „Älter als jede Grenze“ (Hook ersetzt)")

v(id="V031", date="2026-12-11", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Die Goldfäden",
  hook_en="Nine threads. Set by hand. After the wash.",
  hook_de="Neun Fäden. Von Hand gesetzt. Nach der Wäsche.",
  alt_en="The only part of my jeans that moves.",
  shots=["Makro linke Gesäßtasche, Fäden hängen",
         "Fön auf kleinster Stufe oder Hand: Fäden schwingen",
         "Gehen, Rückansicht (nur hinten, kein Serp)"],
  ort=FENSTER + ". Gegenlicht, damit das Gold glänzt", dauer="8–12 s", ton=S_ASMR,
  cap="Gold polyester, triple-twisted, 18 to 30 mm, knotted inside the pocket. The care label says: don't cut them.",
  cta="LIST", check=["Drei Ähren, nie „fünf“"],
  docket="Rev 5.3 W13 Fr · DETAIL „Die Goldfäden“")

v(id="V032", date="2026-12-12", time="12:00", slot="ASK", fmt="Story (2 Frames)", title="Vorbestellen?",
  hook_en="Would you pre-order at €149 on 14.01.?",
  hook_de="Würdest du am 14.01. für 149 € vorbestellen?",
  alt_en="Pre-order at €149: yes, maybe, or no?",
  shots=["Frame 1: Makro Goldfäden", "Frame 2: Umfrage: yes · maybe · need my size first · no"],
  ort="Wohnung", dauer="2 Story-Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["Antworten zählen und im Sonntags-Review notieren"],
  docket="Rev 5.3 W13 Sa · ASK „Vorbestellen?“")

v(id="V033", date="2026-12-14", time="18:00", slot="BUILD", fmt="Video 9:16", title="Die Vorbestellseite",
  hook_en="Day {day}: building the page where you'll pre-order.",
  hook_de="Tag {day}: Ich baue die Seite, auf der du vorbestellst.",
  alt_en="Pre-orders open 14.01. Here's how it works.",
  shots=["Bildschirmaufnahme Shopify-Editor, Produktseite im Entwurf",
         "Größen-Buttons „W32 — 81 cm“",
         "Lieferfenster 22.–30.04.2027",
         "Handy-Vorschau der Seite"],
  ort=MAC, dauer="20–30 s", ton=S_OTON,
  cap="Day {day}. Pre-order opens 14.01., 19:00: 35 pairs at €149, delivery window 22.–30.04.2027. Every size button shows the real waist in cm.",
  cta="LIST", check=["Lieferfenster aus Plan Abschnitt 7"],
  docket="Rev 5.3 W14 Mo · BUILD „Die Vorbestellseite“")

v(id="V034", date="2026-12-15", time="18:00", slot="ORIGIN", fmt="Video 9:16 (zum Speichern)", title="Ehrliche Größen",
  hook_en="My W30 jeans measured 32 inches. So I label honestly.",
  hook_de="Meine W30 hat 32 Zoll gemessen. Deshalb label ich ehrlich.",
  alt_en="How to measure your jeans in 30 seconds.",
  shots=["Referenzjeans flach auf dem Boden, zugeknöpft",
         "Maßband quer über den Bund: 41 cm × 2 = 82 cm = 32 Zoll",
         "Text: „label says W30“",
         "Novalife-Tabelle: W32 = 81 cm"],
  ort=BODEN, dauer="20–30 s", ton=S_OTON,
  cap="My reference jeans say W30. Measured flat: 41 cm × 2 = 82 cm, that's 32 inches. Novalife sizes are the real waist: W32 = 81 cm. Measure your favourite pair before you order. Save this.",
  cta="LIST", check=["Fremdmarke nicht nennen (nur „my reference jeans“)", "Messwerte aus Spec 1.5"],
  docket="Rev 5.3 W14 Di · ORIGIN „Ehrliche Größen“")

v(id="V035", date="2026-12-16", time="19:00", slot="REACH", fmt="Video 9:16", title="100 Stück",
  hook_en="Only 100 will exist. Numbered 001 to 100.",
  hook_de="Es wird nur 100 geben. Nummeriert 001 bis 100.",
  alt_en="One of these could be number 001.",
  shots=["Hangtag-Entwurf auf Papier mit „001/100“", "Schnelle Detail-Schnitte vom Proto", "Endframe: „001–100“"],
  ort=W, dauer="7–10 s", ton=S_TREND,
  cap="100 pairs, each numbered on the hangtag. Pre-orders get the lowest numbers, in order.",
  cta="LIST", check=["Keine Aussage zu „kein Restock“, solange nicht entschieden", "Stückzahl 100 gilt bis zur Schwellen-Entscheidung am 01.02. (100 oder 75)"],
  docket="Rev 5.3 W14 Mi · REACH „100 Stück“")

v(id="V036", date="2026-12-18", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Die Rückseite",
  hook_en="Left pocket: harvest. Right pocket: pattern.",
  hook_de="Linke Tasche: Ernte. Rechte Tasche: Muster.",
  alt_en="The back of my jeans tells one story.",
  shots=["Rückansicht Totale, getragen, gehen", "Makro links: drei Ähren, Band, Fäden", "Makro rechts: Achtstern", "Patch am Bund"],
  ort=HOF, dauer="10–15 s", ton=S_RUHIG,
  cap="Right side: the pattern. Left side: the harvest. Three wheat ears with nine gold threads on the left, the eight-point star on the right, the tree of life on the waistband.",
  cta="LIST", check=["Serp (vorn links) nicht im Bild (B und B2 getrennt halten, zielgruppe.md 3.5)"],
  docket="Rev 5.3 W14 Fr · DETAIL „Die Rückseite“")

v(id="V037", date="2026-12-19", time="12:00", slot="ASK", fmt="Story (2 Frames)", title="Größe",
  hook_en="What's your real waist in cm?",
  hook_de="Was ist dein echter Bund in cm?",
  alt_en="Which size would you take?",
  shots=["Frame 1: Maßband am Bund", "Frame 2: Umfrage W30 · W32 · W34 · W36+"],
  ort="Wohnung", dauer="2 Story-Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["Ergebnis fließt in die Größenverteilung (Spec 1.3)"],
  docket="Rev 5.3 W14 Sa · ASK „Größe“")

v(id="V038", date="2026-12-21", time="18:00", slot="BUILD", fmt="Video 9:16", title="Was bis zum Drop fehlt",
  hook_en="Day {day}: everything left before the drop.",
  hook_de="Tag {day}: Alles, was bis zum Drop noch fehlt.",
  alt_en="17 weeks. Here's the whole plan on one page.",
  shots=["Zeitachse von Hand auf Papier: 04.01. final sample · 14.01. pre-order · Feb production · 20.02. shoot · 22.04. drop",
         "Du hakst ab, was erledigt ist"],
  ort=W, dauer="20–30 s", ton=S_OTON,
  cap="Day {day}. Next: final sample approval 04.01., pre-order 14.01., production from February, drop 22.04., 19:00.",
  cta="LIST", check=["Termine aus Plan Abschnitt 5"],
  docket="Rev 5.3 W15 Mo · BUILD „12 Wochen“ (Titel angepasst)")

v(id="V039", date="2026-12-23", time="18:00", slot="REAL", fmt="Video 9:16", title="Was es bis jetzt gekostet hat",
  hook_en="What this drop has cost me so far.",
  hook_de="Was mich dieser Drop bis jetzt gekostet hat.",
  alt_en="Every euro I spent before selling a single pair.",
  shots=["Belege und Liste auf Papier (Digitizing, Stickproben, Proto, Stoffe, Patches)", "Summe einkreisen", "„budget left: [X]“"],
  ort=W, dauer="20–30 s", ton=S_OTON,
  cap="Development so far: €[echte Summe]. Not a cent of the factory order yet. That one gets paid by pre-orders.",
  cta="LIST", check=["Echte Summen"],
  docket="Rev 5.3 W15 Mi · REAL „Was es bis jetzt gekostet hat“")

v(id="V040", date="2026-12-26", time="12:00", slot="ASK", fmt="Story (Countdown-Sticker)", title="Erinnerung 14.01.",
  hook_en="Tap remind me: pre-order opens 14.01.",
  hook_de="Tipp auf Erinnern: Vorbestellung öffnet am 14.01.",
  alt_en="Don't miss 14.01., 19:00.",
  shots=["Frame 1: Detailfoto", "Frame 2: Countdown-Sticker „Pre-order · 14.01. 19:00“"],
  ort="Wohnung", dauer="2 Story-Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["Countdown-Sticker schickt Erinnerung (markt.md Q49)"],
  docket="Rev 5.3 W15 Sa · ASK „2027“")

v(id="V041", date="2026-12-28", time="18:00", slot="BUILD", fmt="Video 9:16", title="Was 2027 passiert",
  hook_en="2027 plan: 100 jeans, one drop, 22 April.",
  hook_de="Plan 2027: 100 Jeans, ein Drop, 22. April.",
  alt_en="Day {day}: four dates that decide my year.",
  shots=["Kalender 2027 durchblättern", "Vier Daten markieren: 14.01. · 01.02. · 20.02. · 22.04.", "Du, ein Satz"],
  ort=W, dauer="15–20 s", ton=S_OTON,
  cap="Day {day}. Four dates: 14.01. pre-order, February production, 20.02. shoot, 22.04. drop at 19:00.",
  cta="LIST", check=["—"],
  docket="Rev 5.3 W16 Mo · BUILD „Was 2027 passiert“")

v(id="V042", date="2026-12-30", time="19:00", slot="REACH", fmt="Video 9:16", title="Die einzige ihrer Art",
  hook_en="Only one pair exists right now. This one.",
  hook_de="Gerade gibt es nur ein Paar. Dieses.",
  alt_en="The only pair in the world, for now.",
  shots=["Proto auf einem Stuhl mitten im Raum", "Handy kreist langsam drumherum", "Endframe: „prototype“"],
  ort="Wohnung · leerer Raum, Stuhl, Fensterlicht", dauer="7–10 s", ton=S_TREND,
  cap="Prototype. Until 22.04. it stays the only one.",
  cta="LIST", check=["Ehrlich als Prototyp bezeichnet"],
  docket="Rev 5.3 W16 Mi · REACH „Die einzige ihrer Art“")

v(id="V043", date="2027-01-02", time="12:00", slot="ASK", fmt="Story (Frage-Sticker)", title="Frag mich alles",
  hook_en="Pre-order opens in 12 days. Ask me anything.",
  hook_de="In 12 Tagen öffnet die Vorbestellung. Frag mich alles.",
  alt_en="Questions about sizes or delivery? Ask.",
  shots=["Frame 1: Proto-Detail + Frage-Sticker", "Frames 2–5: Antworten als eigene Story"],
  ort="Wohnung", dauer="1 + Antwort-Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["Gute Fragen werden V-Reserve-Videos (Antwort-Format V117)"],
  docket="Rev 5.3 W16 Sa · ASK „14.01.“")

v(id="V044", date="2027-01-04", time="18:00", slot="BUILD", fmt="Video 9:16", title="Das finale Sample",
  hook_en="Day {day}: the final sample. Approve or not?",
  hook_de="Tag {day}: Das finale Sample. Freigeben oder nicht?",
  alt_en="This pair decides how all 100 look.",
  shots=["PP-Sample auspacken", "Prüfplan auf Papier abhaken: Maße, fünf Elemente, Fäden, Patch", "Vergleich Proto vs. PP: was korrigiert wurde", "Deine Entscheidung"],
  ort=FENSTER, dauer="25–35 s", ton=S_OTON,
  cap="Day {day}. The pre-production sample is exactly how the 100 will be. I check measurements, all five embroideries, the threads, the patch. Result: [Ergebnis].",
  cta="LIST", check=["Echtes Ergebnis"],
  docket="Rev 5.3 W17 Mo · BUILD „Das finale Sample“")

v(id="V045", date="2027-01-05", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Warum vorbestellen",
  hook_en="Why I'm asking you to pay before it exists.",
  hook_de="Warum ich dich bitte zu zahlen, bevor es sie gibt.",
  alt_en="35 pre-orders decide if this drop happens.",
  shots=["Du am Tisch, ruhig", "Papier: budget €4,500 · factory wants 50% upfront", "„35 pre-orders = 100 pairs happen“"],
  ort=W, dauer="25–35 s", ton=S_OTON,
  cap="A factory wants half upfront. My budget covers development, not 100 pairs. 35 pre-orders at €149 close the gap. You get €20 off, a low number, and delivery 22.–30.04.",
  cta="LIST", check=["Lieferfenster und Widerruf stehen auf der Vorbestellseite (Plan 7)"],
  docket="Rev 5.3 W17 Di · ORIGIN „Warum vorbestellen“")

v(id="V046", date="2027-01-06", time="19:00", slot="REACH", fmt="Video 9:16", title="Nächster Donnerstag",
  hook_en="Next Thursday, 19:00. 35 pairs.",
  hook_de="Nächsten Donnerstag, 19 Uhr. 35 Paar.",
  alt_en="8 days. 35 pairs. €149.",
  shots=["Schnelle Detail-Schnitte", "Endframe: „14.01. · 19:00“"],
  ort=ARCHIV, dauer="6–9 s", ton=S_TREND,
  cap="14.01., 19:00.", cta="LIST", check=["—"],
  docket="Rev 5.3 W17 Mi · REACH „Nächster Donnerstag“")

v(id="V047", date="2027-01-08", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Stücknummer",
  hook_en="Pre-order early, get a low number.",
  hook_de="Früh vorbestellen, niedrige Nummer bekommen.",
  alt_en="Number 001 goes to the first pre-order.",
  shots=["Hangtag-Muster mit 001 in der Hand", "Hand dreht den Hangtag um", "Stapel leerer Hangtags"],
  ort=W, dauer="8–12 s", ton=S_RUHIG,
  cap="Numbers go out in order of pre-order. 001 is the first.",
  cta="LIST", check=["Entspricht Entscheidung vom 01.10. (Stücknummern nach Bestelldatum)"],
  docket="Rev 5.3 W17 Fr · DETAIL „Stücknummer“")

v(id="V048", date="2027-01-09", time="12:00", slot="ASK", fmt="Story (Countdown-Sticker)", title="Erinnerung",
  hook_en="Tap remind me. Thursday, 19:00.",
  hook_de="Tipp auf Erinnern. Donnerstag, 19 Uhr.",
  alt_en="Five days. Set the reminder.",
  shots=["Frame 1: Countdown-Sticker auf 14.01. 19:00", "Frame 2: Link-Sticker Warteliste"],
  ort="Wohnung", dauer="2 Story-Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["—"],
  docket="Rev 5.3 W17 Sa · ASK „Erinnerung“")

v(id="V049", date="2027-01-11", time="18:00", slot="BUILD", fmt="Video 9:16", title="Donnerstag, 19 Uhr",
  hook_en="Day {day}: three days until pre-order. Here's the plan.",
  hook_de="Tag {day}: Drei Tage bis zur Vorbestellung. So läuft es.",
  alt_en="Thursday 19:00. Here's exactly what happens.",
  shots=["Ablauf auf Papier: 18:00 reminder email · 19:00 open · 19:00 live", "Handy mit Shop-Vorschau"],
  ort=W, dauer="20–25 s", ton=S_OTON,
  cap="Day {day}. Thursday: reminder email at 18:00, pre-order opens at 19:00, I go live and answer size questions.",
  cta="LIST", check=["Ablauf mit den Mail-Terminen aus Plan 10 abgleichen"],
  docket="Rev 5.3 W18 Mo · BUILD „Donnerstag, 19 Uhr“")

v(id="V050", date="2027-01-12", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Vom Wandteppich auf den Zipper",
  hook_en="From a wall carpet to the back of a zipper.",
  hook_de="Vom Wandteppich auf den Rücken eines Zippers.",
  alt_en="A carpet pattern, redrawn stitch by stitch.",
  shots=["Teppich-Foto", "Rasterzeichnung des Medaillons", "Zipper-Muster aus Berlin, Rücken", "Hand über das Medaillon"],
  ort=W, dauer="15–25 s", ton=S_OTON,
  cap="The medallion of a wall carpet, drawn on a grid, embroidered on the back of the zipper. The zipper is made to order in Berlin.",
  cta="LIST", check=["Zipper-Muster existiert seit November: ab Proto-Phase zeigbar", "Subjekt Teppich, kein „sowjetisch“"],
  docket="Rev 5.3 W18 Di · ORIGIN „Vom Teppich auf die Tasche“ (sachlich korrigiert: Medaillon sitzt auf dem Zipper)")

v(id="V051", date="2027-01-13", time="19:00", slot="REACH", fmt="Video 9:16", title="Morgen",
  hook_en="Tomorrow, 19:00. 35 pairs at €149.",
  hook_de="Morgen, 19 Uhr. 35 Paar zu 149 €.",
  alt_en="24 hours. 35 pairs.",
  shots=["Ein Makro, langsam", "Endframe: „tomorrow 19:00“"],
  ort=ARCHIV, dauer="6–9 s", ton=S_TREND,
  cap="Tomorrow, 19:00.", cta="LIST", check=["—"],
  docket="Rev 5.3 W18 Mi · REACH „Morgen“")

# ---------------- P3 VORBESTELLUNG (14.01.–07.02.) ----------------
v(id="V052", date="2027-01-14", time="19:00", slot="BUILD", fmt="Video 9:16 + Live 30 min", title="Jetzt offen",
  hook_en="Pre-order is open. 35 pairs. €149.",
  hook_de="Die Vorbestellung ist offen. 35 Paar. 149 €.",
  alt_en="It's live. 35 pairs at €149.",
  shots=["Handy zeigt den Shop live", "Du, ein Satz", "Fünf Sekunden Detail-Montage", "„link in bio“"],
  ort=W, dauer="10–15 s", ton=S_OTON,
  cap="Open now: 35 pairs at €149 instead of €169. Delivery 22.–30.04. Numbered in order.",
  cta="PRE", check=["Ab 19:05 Live auf Instagram oder TikTok, 30 Minuten, Größenfragen (markt.md Hebel 7)"],
  docket="Rev 5.3 W18 Do · LAUNCH „Jetzt offen“")

v(id="V053", date="2027-01-15", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Der Patch",
  hook_en="Three patch samples. One tree of life made it.",
  hook_de="Drei Patch-Muster. Ein Lebensbaum hat es geschafft.",
  alt_en="I washed these three times at 60°C.",
  shots=["Drei Patch-Muster nebeneinander", "Vorher/Nachher Waschtest 3 × 60 °C", "Gewinner am Bund, Makro"],
  ort=FENSTER, dauer="10–15 s", ton=S_ASMR,
  cap="I washed three patch samples three times at 60°C. [Ergebnis]. The winner sits on every waistband.",
  cta="PRE", check=["Echte Ergebnisse", "Nie „Slavic tree of life“"],
  docket="Rev 5.3 W18 Fr · DETAIL „Der Patch“")

v(id="V054", date="2027-01-16", time="12:00", slot="ASK", fmt="Story", title="Zwischenstand 48 h",
  hook_en="48 hours in: [X] of 35 pre-ordered.",
  hook_de="Nach 48 Stunden: [X] von 35 vorbestellt.",
  alt_en="[Y] pairs left at €149.",
  shots=["Frame 1: echte Zahl groß auf Indigo", "Frame 2: Link-Sticker Vorbestellung"],
  ort="Story-Vorlage", dauer="2 Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["Nur echte Zahl"],
  docket="Rev 5.3 W18 Sa · Zwischenstand-Story")

v(id="V055", date="2027-01-18", time="18:00", slot="BUILD", fmt="Video 9:16", title="Zwischenstand",
  hook_en="Day {day}: [X] of 35 pairs pre-ordered.",
  hook_de="Tag {day}: [X] von 35 Paar vorbestellt.",
  alt_en="Thank you. Here's where we are.",
  shots=["Hangtags auf dem Tisch, einer pro Vorbestellung (nur Nummern, keine Namen)", "Du sagst Danke, ein Satz", "Rest-Zahl groß"],
  ort=W, dauer="15–20 s", ton=S_OTON,
  cap="Day {day}. Real numbers: [X] pre-orders, [Y] left at €149.",
  cta="PRE", check=["Keine Kundennamen", "Echte Zahl"],
  docket="Rev 5.3 W19 Mo · BUILD „Zwischenstand“")

v(id="V056", date="2027-01-19", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Das Feld nach der Ernte",
  hook_en="Why the stubble on my jeans is already cut.",
  hook_de="Warum die Halme auf meiner Jeans schon geschnitten sind.",
  alt_en="The field after the harvest, on my left leg.",
  shots=["Makro: Serp an der Seitennaht im Streiflicht", "Finger zeigt auf die Halme", "Text: „after the harvest“"],
  ort=WAND, dauer="12–20 s", ton=S_OTON,
  cap="On the left leg, a harvest blade stands over cut stubble: the field after the harvest. On the back pocket: the ears that came from it.",
  cta="PRE", check=["Serp nie neben Stern, Hammer oder rotem Grund", "Ähren-Tasche nicht im selben Bild (Sichel + Ähren + rotes Band erinnern an Staatswappen, [Q28])", "Nur posten, wenn der Diaspora-Test bis 08.11. kein Warnsignal zum Serp ergab (zielgruppe.md 3.4)"],
  docket="Rev 5.3 W19 Di · ORIGIN „Geschnittener Weizen“")

v(id="V057", date="2027-01-20", time="19:00", slot="REACH", fmt="Video 9:16", title="Eine Hand",
  hook_en="Every gold thread is set by hand.",
  hook_de="Jeder Goldfaden wird von Hand gesetzt.",
  alt_en="No machine touches these nine threads.",
  shots=["Demonstration am PP-Sample: Nadel zieht einen Faden durch die Tasche", "Knoten innen in der Tasche", "Faden hängt"],
  ort=FENSTER, dauer="7–10 s", ton=S_ASMR,
  cap="Demonstration on the sample. In production, every thread is set by hand after the wash.",
  cta="PRE", check=["Als Demonstration kennzeichnen, wenn du es selbst machst"],
  docket="Rev 5.3 W19 Mi · REACH „Eine Hand“")

v(id="V058", date="2027-01-22", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Die Schnittkante",
  hook_en="Raw hem, cut after the wash. Look.",
  hook_de="Roher Saum, nach der Wäsche geschnitten. Schau.",
  alt_en="No turn-up. No stitch. Just a clean cut.",
  shots=["Makro Saum", "Finger fährt die Kante entlang", "Gehen, der Saum bewegt sich"],
  ort=HOF, dauer="8–12 s", ton=S_RUHIG,
  cap="No turn-up, no stitch. The hem is cut to length after the wash, so the edge is sharp and the frays come from wearing.",
  cta="PRE", check=["—"],
  docket="Rev 5.3 W19 Fr · DETAIL „Die Schnittkante“")

v(id="V059", date="2027-01-23", time="12:00", slot="ASK", fmt="Story (Frage-Sticker)", title="Q&A",
  hook_en="Ask me anything about the pre-order.",
  hook_de="Frag mich alles zur Vorbestellung.",
  alt_en="Size, delivery, returns: ask.",
  shots=["Frame 1: Frage-Sticker", "Antwort-Frames"],
  ort="Wohnung", dauer="1 + Antworten", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["Rechtliche Fragen (Widerruf) nur mit dem Text der Rechtsseite beantworten"],
  docket="Rev 5.3 W19 Sa · Story-Q&A")

v(id="V060", date="2027-01-25", time="18:00", slot="BUILD", fmt="Video 9:16", title="Noch X Paar",
  hook_en="Day {day}: [Y] pairs left at €149.",
  hook_de="Tag {day}: Noch [Y] Paar zu 149 €.",
  alt_en="[Y] pairs left. Then it's €169.",
  shots=["Hangtag-Stapel wird kleiner (Zeitraffer)", "Echte Zahl"],
  ort=W, dauer="10–15 s", ton=S_RUHIG,
  cap="Day {day}. [Y] of 35 left at the pre-order price.", cta="PRE", check=["Echte Zahl"],
  docket="Rev 5.3 W20 Mo · BUILD „Noch X Paar“")

v(id="V061", date="2027-01-26", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Warum 100",
  hook_en="Why 100 pairs, and not 1,000.",
  hook_de="Warum 100 Paar und nicht 1.000.",
  alt_en="100 is the minimum. And my maximum.",
  shots=["Du am Tisch", "Papier: „factory minimum per style: 100“", "Du: „And it's what I can pack and answer for, myself.“"],
  ort=W, dauer="15–25 s", ton=S_OTON,
  cap="100 is the factory minimum per style. It's also what I can sell, pack and answer for, myself.",
  cta="PRE", check=["MOQ 100 laut Plan"],
  docket="Rev 5.3 W20 Di · ORIGIN „Warum 100“")

v(id="V062", date="2027-01-27", time="19:00", slot="REACH", fmt="Video 9:16", title="POV",
  hook_en="POV: your jeans come with their own number.",
  hook_de="POV: Deine Jeans hat ihre eigene Nummer.",
  alt_en="POV: you own number 0XX of 100.",
  shots=["Hangtag-Makro", "Hand dreht den Hangtag", "Jeans gefaltet"],
  ort=W, dauer="6–9 s", ton=S_TREND,
  cap="001–100.", cta="PRE", check=["—"],
  docket="Rev 5.3 W20 Mi · REACH „POV“")

v(id="V063", date="2027-01-29", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Der Stern",
  hook_en="27 by 27 stitches. One star. Zero curves.",
  hook_de="27 mal 27 Stiche. Ein Stern. Null Rundungen.",
  alt_en="Count the stitches in this star.",
  shots=["Makro Achtstern", "Lineal: 36 mm", "Finger"],
  ort=FENSTER, dauer="8–12 s", ton=S_ASMR,
  cap="Eight-point star, right back pocket: 27 × 27 cross-stitches, 36 mm.", cta="PRE",
  check=["Nach außen „eight-point star“"],
  docket="Rev 5.3 W20 Fr · DETAIL „Der Stern“")

v(id="V064", date="2027-01-30", time="12:00", slot="ASK", fmt="Story", title="Montag entscheidet",
  hook_en="Monday decides if 100 pairs get made.",
  hook_de="Montag entscheidet, ob 100 Paar gemacht werden.",
  alt_en="[X] pre-orders. Monday is the deadline.",
  shots=["Frame 1: echte Zahl", "Frame 2: Link-Sticker"],
  ort="Story-Vorlage", dauer="2 Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["Nur, wenn die Schwelle (10) noch offen ist. Sonst: „[X] of 35“"],
  docket="Rev 5.3 W20 Sa · Zwischenstand-Story")

v(id="V065", date="2027-02-01", time="18:00", slot="BUILD", fmt="Video 9:16", title="100 oder 75",
  hook_en="Day {day}: 100 pairs or 75? Today I decide.",
  hook_de="Tag {day}: 100 Paar oder 75? Heute entscheide ich.",
  alt_en="The number that decides how many pairs exist.",
  shots=["Zahl der Vorbestellungen auf Papier", "Regel aus dem Plan daneben", "Deine Entscheidung"],
  ort=W, dauer="15–25 s", ton=S_OTON,
  cap="Day {day}. [X] pre-orders. Decision: [100/75] pairs.", cta="PRE", check=["Echtes Ergebnis"],
  docket="Rev 5.3 W21 Mo · BUILD „100 oder 75“")

v(id="V066", date="2027-02-03", time="19:00", slot="REACH", fmt="Video 9:16", title="Bestellt",
  hook_en="I just ordered [100] jeans from the factory.",
  hook_de="Ich habe gerade [100] Jeans bei der Fabrik bestellt.",
  alt_en="It's official. [100] pairs are ordered.",
  shots=["Bildschirm: Bestellbestätigung (Namen verpixelt)", "Deine Reaktion"],
  ort=MAC, dauer="6–10 s", ton=S_TREND,
  cap="Ordered.", cta="PRE", check=["Nur wenn wahr"],
  docket="Rev 5.3 W21 Mi · REACH „Bestellt“")

v(id="V067", date="2027-02-05", time="18:00", slot="REAL", fmt="Video 9:16", title="Überwiesen",
  hook_en="I just paid the factory [€3,000]. Here's why.",
  hook_de="Ich habe der Fabrik gerade [3.000 €] überwiesen. Darum.",
  alt_en="The deposit is paid. Production starts Monday.",
  shots=["Banking-App, Betrag sichtbar, Empfänger verpixelt", "Du erklärst 50/50 in einem Satz"],
  ort=W, dauer="15–25 s", ton=S_OTON,
  cap="Half upfront, half before shipping. This half came from you: [X] pre-orders.", cta="PRE",
  check=["Echter Betrag (50/50 oder 60/40)"],
  docket="Rev 5.3 W21 Fr · REAL „Überwiesen“")

# ---------------- P4 PRODUKTION (08.02.–28.03.) ----------------
v(id="V068", date="2027-02-08", time="18:00", slot="BUILD", fmt="Video 9:16", title="In Produktion",
  hook_en="Day {day}: my jeans are in production.",
  hook_de="Tag {day}: Meine Jeans sind in Produktion.",
  alt_en="[100] pairs are being cut right now.",
  shots=["Fotos/Clips der Fabrik (nur mit schriftlicher Erlaubnis)", "Sonst: Kalender bis Ende März, Tech Pack auf dem Tisch"],
  ort=W, dauer="15–20 s", ton=S_OTON,
  cap="Day {day}. Production started. Next update: first inline photos.", cta="PRE",
  check=["Fabrik-Bilder nur mit schriftlicher Erlaubnis"],
  docket="Rev 5.3 W22 Mo · BUILD „In Produktion“")

v(id="V069", date="2027-02-09", time="18:00", slot="ORIGIN", fmt="Karussell 8 Slides + Video", title="Wie eine Jeans entsteht",
  hook_en="How 100 embroidered jeans get made, in 8 steps.",
  hook_de="Wie 100 bestickte Jeans entstehen, in 8 Schritten.",
  alt_en="Cut, embroider, sew, wash, cut again.",
  shots=["Slide 1 Zuschnitt", "Slide 2 Sticken auf dem flachen Teil", "Slide 3 Nähen + Patch", "Slide 4 Wäsche", "Slide 5 Abrieb", "Slide 6 Saum schneiden + Goldfäden"],
  ort="Fabrik-Material mit Erlaubnis, sonst Papierkarten am Schreibtisch", dauer="8 Slides / 20–30 s", ton=S_RUHIG,
  cap="Embroider the flat panel, sew, patch, wash, abrade, cut the hem, set the gold threads by hand. Save this.",
  cta="PRE", check=["Prozesskette aus Spec 2.3"],
  docket="Rev 5.3 W22 Di · ORIGIN „Wie eine Jeans entsteht“")

v(id="V070", date="2027-02-10", time="19:00", slot="REACH", fmt="Video 9:16", title="Stoff",
  hook_en="This roll becomes [100] pairs.",
  hook_de="Aus dieser Rolle werden [100] Paar.",
  alt_en="It starts as one roll of denim.",
  shots=["Stoffrolle in der Fabrik (mit Erlaubnis) oder dein Stoffmuster in Großaufnahme"],
  ort="Fabrik-Material mit Erlaubnis / Fensterbank", dauer="6–9 s", ton=S_TREND,
  cap="Day one of production.", cta="PRE", check=["Fabrik-Bild nur mit Erlaubnis"],
  docket="Rev 5.3 W22 Mi · REACH „Stoff“")

v(id="V071", date="2027-02-12", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Der Hangtag",
  hook_en="001 to 100. Each number exists once.",
  hook_de="001 bis 100. Jede Nummer gibt es einmal.",
  alt_en="The tag tells you which pair is yours.",
  shots=["Hangtag-Makro auf Recyclingkarton", "Hand fächert 10 Hangtags auf", "Nummer 001 groß"],
  ort=W, dauer="8–12 s", ton=S_ASMR,
  cap="Recycled card, 300 g, one number per pair.", cta="PRE", check=["Material aus Spec 2.8"],
  docket="Rev 5.3 W22 Fr · DETAIL „Der Hangtag“")

v(id="V072", date="2027-02-13", time="12:00", slot="ASK", fmt="Story", title="Casting",
  hook_en="Shoot on 20.02. in Berlin. Want in?",
  hook_de="Shoot am 20.02. in Berlin. Bist du dabei?",
  alt_en="Looking for two people for my first shoot.",
  shots=["Frame 1: Moodboard", "Frame 2: Frage-Sticker „your size + why“"],
  ort="Story-Vorlage", dauer="2 Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["Bildrechte schriftlich vor dem Shoot klären"],
  docket="Rev 5.3 W22 Sa · Story „Casting“")

v(id="V073", date="2027-02-15", time="18:00", slot="BUILD", fmt="Video 9:16", title="Shoot am Samstag",
  hook_en="Day {day}: planning a shoot on €150.",
  hook_de="Tag {day}: Ich plane einen Shoot mit 150 €.",
  alt_en="My whole shoot plan on one sheet.",
  shots=["Moodboard auf dem Tisch (eigene Referenzen)", "Shotliste auf Papier", "Foto der Location"],
  ort=W, dauer="15–25 s", ton=S_OTON,
  cap="Day {day}. €150, one Saturday, one location at sunset.", cta="PRE",
  check=["Moodboard: Sonnenuntergang statt Blau über Gelb", "Keine Sowjet-Kulisse"],
  docket="Rev 5.3 W23 Mo · BUILD „Shoot am Samstag“")

v(id="V074", date="2027-02-16", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Der Zipper",
  hook_en="Why the zipper wears two bands at the front.",
  hook_de="Warum der Zipper vorn zwei Bänder trägt.",
  alt_en="Every product wears its pattern at its opening.",
  shots=["Zipper hängt an der Tür", "Makro Bänder links und rechts der Zip-Leiste", "Rücken mit Medaillon"],
  ort=WAND, dauer="15–25 s", ton=S_OTON,
  cap="Traditional embroidered shirts carry their ornament at the neck opening. A zipper has an opening too, so the bands sit left and right of the zip. €139, made to order in Berlin.",
  cta="PRE", check=["„Vyshyvanka“ nach außen vermeiden"],
  docket="Rev 5.3 W23 Di · ORIGIN „Der Zipper“")

v(id="V075", date="2027-02-17", time="19:00", slot="REACH", fmt="Video 9:16", title="Drei Teile",
  hook_en="Jeans, zipper, polo. One drop. 22.04.",
  hook_de="Jeans, Zipper, Polo. Ein Drop. 22.04.",
  alt_en="Three pieces. One pattern. 22.04., 19:00.",
  shots=["Drei schnelle Schnitte, je ein Teil", "Endframe „22.04.“"],
  ort=ARCHIV, dauer="6–9 s", ton=S_TREND,
  cap="22.04., 19:00.", cta="PRE", check=["—"],
  docket="Rev 5.3 W23 Mi · REACH „Drei Teile“")

v(id="V076", date="2027-02-19", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Der Polo",
  hook_en="Two bands at the placket. €79.",
  hook_de="Zwei Bänder an der Knopfleiste. 79 €.",
  alt_en="The lightest way into the drop.",
  shots=["Polo flach", "Makro Bänder an der Knopfleiste", "Getragen, Halbtotale"],
  ort=FENSTER, dauer="8–12 s", ton=S_RUHIG,
  cap="Piqué polo, two cross-stitch bands at the placket. €79, made to order in Berlin.", cta="PRE",
  check=["—"],
  docket="Rev 5.3 W23 Fr · DETAIL „Der Polo“")

v(id="V077", date="2027-02-22", time="18:00", slot="BUILD", fmt="Video 9:16", title="Hinter den Kulissen",
  hook_en="Day {day}: behind the scenes of my first shoot.",
  hook_de="Tag {day}: Hinter den Kulissen meines ersten Shoots.",
  alt_en="What €150 and one sunset get you.",
  shots=["BTS-Clips vom 20.02., schnell geschnitten", "Ein Fail (umgefallenes Stativ o. ä., wenn passiert)", "Ein fertiges Bild als Endframe"],
  ort=SHOOT, dauer="15–25 s", ton=S_TREND,
  cap="Day {day}. One Saturday, one location, one sunset.", cta="PRE", check=["Bildrechte der Models geklärt"],
  docket="Rev 5.3 W24 Mo · BUILD „Hinter den Kulissen“")

v(id="V078", date="2027-02-25", time="19:00", slot="REACH", fmt="Foto/Video", title="Das erste Bild",
  hook_en="The first real photo of Time Travel.",
  hook_de="Das erste echte Foto von Time Travel.",
  alt_en="Four months of work. One photo.",
  shots=["Hauptbild aus dem Shoot", "Langsamer Zoom"],
  ort=SHOOT, dauer="6–9 s", ton=S_RUHIG,
  cap="Time Travel. 22.04., 19:00.", cta="PRE",
  check=["Von Mi 24.02. auf Do 25.02. verschoben: 24.02.2027 ist der 5. Jahrestag des russischen Großangriffs, an dem Tag nichts Werbliches (zielgruppe.md 3.7)"],
  docket="Rev 5.3 W24 Mi · REACH „Das erste Bild“ (auf Do verschoben)")

v(id="V079", date="2027-02-26", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Kampagnenfilm",
  hook_en="Thirty seconds. Five embroideries. One field at sunset.",
  hook_de="Dreißig Sekunden. Fünf Stickereien. Ein Feld im Sonnenuntergang.",
  alt_en="The Time Travel film.",
  shots=["Kampagnenfilm, 30 s", "Fünf Stickereien in getrennten Einstellungen"],
  ort=SHOOT, dauer="30 s", ton="Track aus der Business-Bibliothek, für beide Plattformen getrennt gesetzt",
  cap="Time Travel. 100 pairs. 22.04., 19:00.", cta="PRE",
  check=["Sonnenuntergang, nie Blau über Gelb", "Serp und Ähren-Tasche nie im selben Frame"],
  docket="Rev 5.3 W24 Fr · DETAIL „Kampagnenfilm“")

v(id="V080", date="2027-02-27", time="12:00", slot="ASK", fmt="Story", title="Hauptbild",
  hook_en="Which photo should be the main image?",
  hook_de="Welches Foto soll das Hauptbild werden?",
  alt_en="A or B? You decide the shop photo.",
  shots=["Frame 1: zwei Bilder nebeneinander + Umfrage A/B"],
  ort="Story-Vorlage", dauer="1–2 Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["—"],
  docket="Rev 5.3 W24 Sa · ASK „Hauptbild“")

v(id="V081", date="2027-03-01", time="18:00", slot="BUILD", fmt="Video 9:16", title="Das ist Time Travel",
  hook_en="Day {day}: this is Time Travel. All of it.",
  hook_de="Tag {day}: Das ist Time Travel. Alles.",
  alt_en="From paper in October to this.",
  shots=["Zeitraffer: Papiertest → Stickprobe → Proto → Shoot-Bild"],
  ort=ARCHIV, dauer="15–20 s", ton=S_TREND,
  cap="Day {day}. Paper in October, thread in November, a prototype in December, production now.", cta="PRE",
  check=["—"],
  docket="Rev 5.3 W25 Mo · BUILD „Das ist Time Travel“")

v(id="V082", date="2027-03-02", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Rot und Weiß",
  hook_en="Why white sits next to red on my denim.",
  hook_de="Warum auf meinem Denim Weiß neben Rot sitzt.",
  alt_en="Red disappears on indigo. Here's the fix.",
  shots=["Rotes Garn auf Indigo aus 2 m: verschwindet", "Gleiches mit weißer Kante: liest sich", "Makro Band A"],
  ort=WAND, dauer="15–25 s", ton=S_OTON,
  cap="Deep red and indigo have almost the same brightness. From two metres, red alone disappears. So on the pattern side, white always sits next to red.",
  cta="PRE", check=["Farbregel aus Spec 3.4", "Keine Streifen in Weiß-Rot-Weiß (zielgruppe.md 3.6)"],
  docket="Rev 5.3 W25 Di · ORIGIN „Rot und Weiß“")

v(id="V083", date="2027-03-03", time="19:00", slot="REACH", fmt="Video 9:16", title="Nummer vergeben",
  hook_en="Pair [0XX] already has an owner.",
  hook_de="Paar [0XX] hat schon einen Besitzer.",
  alt_en="[X] numbers are taken. Yours?",
  shots=["Hangtag mit echter Nummer der letzten Vorbestellung", "Hand legt ihn auf den Stapel „taken“"],
  ort=W, dauer="6–9 s", ton=S_TREND,
  cap="Numbers go in order.", cta="PRE", check=["Echte Nummer (Rev. 5.3 nannte 047, das liegt über 35 Vorbestellungen)"],
  docket="Rev 5.3 W25 Mi · REACH „Nummer 047“ (Nummer an echte Zahl gekoppelt)")

v(id="V084", date="2027-03-05", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Fäden nicht abschneiden",
  hook_en="The care label says: don't cut the threads.",
  hook_de="Auf dem Pflegeetikett steht: Fäden nicht abschneiden.",
  alt_en="Wash inside out. Never cut these.",
  shots=["Makro Pflegeetikett", "Schnitt auf die Goldfäden", "Hose auf links gedreht"],
  ort=FENSTER, dauer="8–12 s", ton=S_ASMR,
  cap="Wash inside out. Don't cut the threads. They're the moment.", cta="PRE", check=["Text aus Spec 3.7"],
  docket="Rev 5.3 W25 Fr · DETAIL „Fäden nicht abschneiden“")

v(id="V085", date="2027-03-06", time="12:00", slot="ASK", fmt="Story", title="Paket",
  hook_en="Which packaging should your pair arrive in?",
  hook_de="In welcher Verpackung soll dein Paar ankommen?",
  alt_en="Paper or fabric bag? Vote.",
  shots=["Frame 1: zwei Verpackungsmuster + Umfrage"],
  ort="Wohnung", dauer="1 Frame", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["—"],
  docket="Rev 5.3 W25 Sa · ASK „Paket“")

v(id="V086", date="2027-03-08", time="18:00", slot="BUILD", fmt="Video 9:16", title="Fast fertig",
  hook_en="Day {day}: first photos from the production line.",
  hook_de="Tag {day}: Erste Fotos aus der Produktion.",
  alt_en="They're being embroidered right now.",
  shots=["Inline-Fotos der Fabrik (mit Erlaubnis)", "Deine Prüf-Notizen daneben"],
  ort="Fabrik-Material mit Erlaubnis + Schreibtisch", dauer="15–20 s", ton=S_OTON,
  cap="Day {day}. Inline check: [Befund].", cta="PRE",
  check=["Fabrik-Bilder nur mit Erlaubnis", "Ramadan-Fest in der Türkei 08.–11.03.: keine Druck-Botschaft an die Fabrik"],
  docket="Rev 5.3 W26 Mo · BUILD „Fast fertig“")

v(id="V087", date="2027-03-09", time="18:00", slot="ORIGIN", fmt="Karussell 7 Slides (anheften)", title="Für alle Neuen",
  hook_en="New here? 100 jeans, 5 embroideries, 22.04.",
  hook_de="Neu hier? 100 Jeans, 5 Stickereien, 22.04.",
  alt_en="Start here: what Time Travel is.",
  shots=["Slide 1 Hook", "Slide 2 Das Teil", "Slide 3 Fünf Stickereien", "Slide 4 Goldfäden", "Slide 5 Ehrliche Größen", "Slide 6 Preis und Termine", "Slide 7 Warteliste"],
  ort=SHOOT, dauer="7 Slides", ton=S_RUHIG,
  cap="Start here. 100 numbered jeans, five embroideries, nine gold threads set by hand. Pre-order €149 until 21.03., 20:00. Drop 22.04., 19:00.",
  cta="PRE", check=["Im Profil anheften"],
  docket="Rev 5.3 W26 Di · ORIGIN „Für alle Neuen“")

v(id="V088", date="2027-03-10", time="19:00", slot="REACH", fmt="Video 9:16", title="So wird verpackt",
  hook_en="How your pair will arrive.",
  hook_de="So kommt dein Paar an.",
  alt_en="Packing test with the prototype.",
  shots=["Verpackung Schritt für Schritt (mit dem Proto)", "Hangtag, Karte, Paket zu"],
  ort=W, dauer="8–12 s", ton=S_ASMR,
  cap="Folded, tagged, numbered.", cta="PRE", check=["—"],
  docket="Rev 5.3 W26 Mi · REACH „So wird verpackt“")

v(id="V089", date="2027-03-12", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Gold im Licht",
  hook_en="Gold thread at golden hour.",
  hook_de="Goldfaden zur goldenen Stunde.",
  alt_en="Watch the threads catch the sun.",
  shots=["Gegenlicht Sonnenuntergang, Goldfäden schwingen", "Makro Ähren"],
  ort=FELD, dauer="6–10 s", ton=S_TREND,
  cap="Nine threads, one sunset.", cta="PRE", check=["Himmel orange/violett, nie Blau über Gelb"],
  docket="Rev 5.3 W26 Fr · DETAIL „Gold im Licht“")

v(id="V090", date="2027-03-13", time="12:00", slot="ASK", fmt="Story (Countdown-Sticker)", title="Letzte Woche Vorbestellpreis",
  hook_en="€149 ends Sunday 21.03., 20:00.",
  hook_de="149 € enden am Sonntag 21.03., 20:00.",
  alt_en="One week left at €149.",
  shots=["Frame 1: Countdown-Sticker auf 21.03. 20:00", "Frame 2: Link-Sticker"],
  ort="Story-Vorlage", dauer="2 Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["—"],
  docket="Rev 5.3 W26 Sa · ASK „Letzte Woche Vorbestellpreis“")

v(id="V091", date="2027-03-15", time="18:00", slot="BUILD", fmt="Video 9:16", title="Noch bis Sonntag",
  hook_en="Day {day}: six days left at €149.",
  hook_de="Tag {day}: Noch sechs Tage zu 149 €.",
  alt_en="Sunday 20:00 the price goes up.",
  shots=["Kalender, Sonntag umkringelt", "Echte Restzahl"],
  ort=W, dauer="10–15 s", ton=S_OTON,
  cap="Day {day}. Pre-order price ends Sunday 21.03., 20:00. [Y] of 35 left.", cta="PRE", check=["Echte Zahl"],
  docket="Rev 5.3 W27 Mo · BUILD „Noch bis Sonntag“")

v(id="V092", date="2027-03-16", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Gold nur, wo etwas wächst",
  hook_en="Gold only goes where something grows.",
  hook_de="Gold kommt nur dorthin, wo etwas wächst.",
  alt_en="My one rule for gold thread.",
  shots=["Makro Ähren (Gold)", "Makro Lebensbaum-Patch (Gold)", "Makro Band A (kein Gold)"],
  ort=FENSTER, dauer="12–18 s", ton=S_OTON,
  cap="Gold belongs to the wheat and the tree of life. Nowhere else on the jeans.", cta="PRE",
  check=["Farbregel 3 aus Spec 3.4"],
  docket="Rev 5.3 W27 Di · ORIGIN „Gold nur, wo etwas wächst“")

v(id="V093", date="2027-03-17", time="19:00", slot="REACH", fmt="Video 9:16", title="Papier zu Garn",
  hook_en="October: paper. March: thread. Same pocket.",
  hook_de="Oktober: Papier. März: Garn. Dieselbe Tasche.",
  alt_en="I taped paper on these in October.",
  shots=["Match-Cut Papiertest → fertiges Teil, gleiche Einstellung"],
  ort=ARCHIV, dauer="6–9 s", ton=S_TREND,
  cap="Paper → thread.", cta="PRE", check=["—"],
  docket="Rev 5.3 W27 Mi · REACH „Papier zu Garn“")

v(id="V094", date="2027-03-19", time="18:00", slot="DETAIL", fmt="Video 9:16", title="45 × 45",
  hook_en="The smallest pocket: 45 by 45 stitches.",
  hook_de="Die kleinste Tasche: 45 mal 45 Stiche.",
  alt_en="A coin pocket, completely embroidered.",
  shots=["Makro Münztasche E", "Lineal: 60 mm", "Finger"],
  ort=FENSTER, dauer="8–12 s", ton=S_ASMR,
  cap="Coin pocket, fully embroidered: 60 × 60 mm, 45 × 45 cross-stitches, red and white.", cta="PRE",
  check=["Rev. 5.3 nannte „37 mal 37“, das passt zu keinem Element (C = 27 × 27, E = 45 × 45). Korrigiert"],
  docket="Rev 5.3 W27 Fr · DETAIL „37 mal 37“ (korrigiert)")

v(id="V095", date="2027-03-20", time="12:00", slot="ASK", fmt="Story (Countdown-Sticker)", title="Letzter Tag",
  hook_en="Tomorrow 20:00 the €149 price is gone.",
  hook_de="Morgen um 20 Uhr ist der Preis von 149 € weg.",
  alt_en="Last 24 hours at €149.",
  shots=["Frame 1: Countdown-Sticker 21.03. 20:00", "Frame 2: Countdown-Sticker Drop 22.04. 19:00"],
  ort="Story-Vorlage", dauer="2 Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["—"],
  docket="Rev 5.3 W27 Sa · ASK „Countdown“")

v(id="V096", date="2027-03-22", time="18:00", slot="BUILD", fmt="Video 9:16", title="Alles bezahlt",
  hook_en="Day {day}: factory fully paid. The jeans are coming.",
  hook_de="Tag {day}: Fabrik komplett bezahlt. Die Jeans kommen.",
  alt_en="Paid. Shipped. Here's what's next.",
  shots=["Banking-App, Empfänger verpixelt", "Kalender: Ware ca. 30.03.", "Du, ein Satz"],
  ort=W, dauer="10–15 s", ton=S_OTON,
  cap="Day {day}. Fully paid. Arrival around 30.03., then I check every single pair.", cta="DROP",
  check=["Nur wenn wahr"],
  docket="Rev 5.3 W28 Mo · BUILD „Alles bezahlt“")

v(id="V097", date="2027-03-23", time="18:00", slot="ORIGIN", fmt="Video 9:16", title="Warum Time Travel",
  hook_en="Why I called this drop Time Travel.",
  hook_de="Warum dieser Drop Time Travel heißt.",
  alt_en="Old patterns. New denim. Here's the name.",
  shots=["Du in die Kamera", "Schnitt auf Teppich-Foto und fertiges Teil"],
  ort=W, dauer="20–30 s", ton=S_OTON,
  cap="[Deine Begründung in zwei Sätzen, Subjekt ist das Muster.]", cta="DROP",
  check=["Begründung muss von dir kommen, nicht erfunden", "Kein „älter als jede Grenze“"],
  docket="Rev 5.3 W28 Di · ORIGIN „Warum Time Travel“")

v(id="V098", date="2027-03-24", time="19:00", slot="REACH", fmt="Video 9:16", title="Packstation",
  hook_en="My living room is now a packing station.",
  hook_de="Mein Wohnzimmer ist jetzt eine Packstation.",
  alt_en="35 packages. One living room.",
  shots=["Zeitraffer: Wohnzimmer wird zur Packstraße", "Kartons, Hangtags, Klebeband"],
  ort="Wohnung · Wohnzimmer", dauer="6–10 s", ton=S_TREND,
  cap="Getting ready for 35 pre-orders.", cta="DROP", check=["—"],
  docket="Rev 5.3 W28 Mi · REACH „Packstation“")

v(id="V099", date="2027-03-26", time="18:00", slot="DETAIL", fmt="Video 9:16", title="Fünf Stickereien",
  hook_en="Five embroideries. One second each.",
  hook_de="Fünf Stickereien. Je eine Sekunde.",
  alt_en="Count the embroideries on these jeans.",
  shots=["Band A", "Münztasche E", "Serp B", "Ähren B2", "Achtstern C", "Patch D"],
  ort=SHOOT, dauer="6–8 s", ton=S_TREND,
  cap="Band, coin pocket, harvest, star, tree. Plus nine threads.", cta="DROP",
  check=["B und B2 in getrennten Einstellungen, nie im selben Frame"],
  docket="Rev 5.3 W28 Fr · DETAIL „Fünf Stickereien“")

v(id="V100", date="2027-03-27", time="12:00", slot="ASK", fmt="Story (Frage-Sticker)", title="Größe",
  hook_en="Not sure about your size? Ask me.",
  hook_de="Unsicher mit der Größe? Frag mich.",
  alt_en="Send me your waist in cm.",
  shots=["Frame 1: Größentabelle", "Frame 2: Frage-Sticker"],
  ort="Story-Vorlage", dauer="2 Frames", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["—"],
  docket="Rev 5.3 W28 Sa · ASK „Größe“")

# ---------------- P6 DROP (22.–25.04.) ----------------
v(id="V101", date="2027-04-22", time="18:00", slot="ASK", fmt="Story + Live 30 min", title="Die Liste kauft gerade",
  hook_en="The list is shopping right now.",
  hook_de="Die Warteliste kauft gerade.",
  alt_en="Early access is open. Check your email.",
  shots=["Story 18:00: Handy mit Shop", "Live 18:05–18:35: Größenfragen, Pakete im Hintergrund", "Story 18:50: „10 minutes“"],
  ort="Wohnung", dauer="Live 30 min + 2 Frames", ton=S_KEINE,
  cap="(Story)", cta="LIVE", check=["Ablauf „Drop-Tag Minute für Minute“ aus der Docket-Referenz"],
  docket="Rev 5.3 W32 Do · DROP 18:00")

v(id="V102", date="2027-04-22", time="19:00", slot="REACH", fmt="Video 9:16", title="Live",
  hook_en="Time Travel is live now.",
  hook_de="Time Travel ist jetzt live.",
  alt_en="19:00. Go.",
  shots=["Kampagnenfilm 15 s", "Endframe „live now“"],
  ort=SHOOT, dauer="15 s", ton="wie Kampagnenfilm",
  cap="Live now. Jeans €169, zipper €139, polo €79.", cta="LIVE",
  check=["Link in beiden Bios auf die Kollektion", "Werbekampagne 2 startet"],
  docket="Rev 5.3 W32 Do · DROP 19:00")

v(id="V103", date="2027-04-22", time="20:00", slot="ASK", fmt="Story", title="Restbestand",
  hook_en="[X] pairs left. Here are the sizes.",
  hook_de="Noch [X] Paar. Das sind die Größen.",
  alt_en="Sizes left right now:",
  shots=["Frame: Restbestand pro Größe, echte Zahlen"],
  ort="Story-Vorlage", dauer="1 Frame, um 19:15, 20:00, 22:00 aktualisieren", ton=S_KEINE,
  cap="(Story)", cta="LIVE", check=["Echte Zahlen"],
  docket="Rev 5.3 W32 Do · 19:15 / 20:00 / 22:00 Stories")

v(id="V104", date="2027-04-23", time="18:00", slot="BUILD", fmt="Video 9:16", title="24 Stunden",
  hook_en="24 hours: [X] of 100 found an owner.",
  hook_de="24 Stunden: [X] von 100 haben einen Besitzer.",
  alt_en="Day {day}: what happened last night.",
  shots=["Packtisch, Kartons", "Echte Zahl", "Danke, ein Satz"],
  ort="Wohnung · Packstation", dauer="10–15 s", ton=S_OTON,
  cap="Day {day}. Packing all weekend. Everything ordered Thursday and Friday ships by Saturday night.", cta="LIVE",
  check=["Echte Zahl"],
  docket="Rev 5.3 W32 Fr · Zwischenstand-Story")

v(id="V105", date="2027-04-24", time="12:00", slot="ASK", fmt="Story", title="Drop 2",
  hook_en="What should the next drop be?",
  hook_de="Was soll der nächste Drop werden?",
  alt_en="Drop 2: you choose the direction.",
  shots=["Frame: Frage-Sticker (keine geparkten Themen oder Partnernamen zeigen)"],
  ort="Story-Vorlage", dauer="1 Frame", ton=S_KEINE,
  cap="(Story)", cta="STORY", check=["Keine Namen möglicher Kollaborationspartner"],
  docket="Rev 5.3 W32 Sa · ASK „Drop 2“")

v(id="V106", date="2027-04-25", time="18:00", slot="REAL", fmt="Video 9:16", title="Was der Drop gebracht hat",
  hook_en="Day {day}: the real numbers of my first drop.",
  hook_de="Tag {day}: Die echten Zahlen meines ersten Drops.",
  alt_en="What 193 days of building turned into.",
  shots=["Handschrift: verkauft, Umsatz, Kosten", "Du, ehrlich, zwei Sätze"],
  ort=W, dauer="20–30 s", ton=S_OTON,
  cap="Day {day}. Sold: [X]. Revenue: [€]. What I'd do differently: [ein Satz].", cta="LIVE",
  check=["Nur echte Zahlen"],
  docket="Rev 5.3 W32 So · Auswertung (NEU als Post)")

v(id="V107", date="2027-04-22", time="21:00", slot="ASK", fmt="Live 30 min (optional)", title="Drop-Live vom Packtisch",
  hook_en="Live from my packing table. Ask about sizes.",
  hook_de="Live von meinem Packtisch. Frag nach Größen.",
  alt_en="Drop night, live. Questions welcome.",
  shots=["Handy auf Stativ über dem Packtisch", "Größentabelle griffbereit"],
  ort="Wohnung · Packstation", dauer="30 min", ton="Live-Ton",
  cap="(Live)", cta="LIVE", check=["Keine Kundennamen oder Adressen im Bild"],
  docket="NEU · Drop-Abend")

# ---------------- RESERVE (ohne festes Datum) ----------------
def r(**k):
    k.setdefault("date", None); k.setdefault("time", "frei"); E.append(k)

r(id="V108", phase="ab P1", slot="ORIGIN", fmt="Karussell / Photo Mode 5 Slides", title="Ornament in 15 Sekunden: Raute",
  hook_en="This diamond means one thing: a sown field.",
  hook_de="Diese Raute bedeutet eine Sache: ein bestelltes Feld.",
  alt_en="Save this: what the diamond means in cross-stitch.",
  shots=["Slide 1 Hook auf Indigo", "Slide 2 Raute gezeichnet", "Slide 3 Raute mit Punkt in der Mitte", "Slide 4 Raute im Papierband", "Slide 5 Warteliste"],
  ort=W, dauer="5 Slides", ton=S_RUHIG,
  cap="The diamond with a dot: a sown field. One of the motifs that made it onto my jeans. Save it.",
  cta="LIST", check=["Vor Proto nur Papier"], docket="Reserve · für Extra-Tage oder als Ersatz schwacher Posts")

r(id="V109", phase="ab P1", slot="ORIGIN", fmt="Karussell / Photo Mode 4 Slides", title="Ornament in 15 Sekunden: Zickzack",
  hook_en="Zigzag in cross-stitch means water. Save this.",
  hook_de="Zickzack im Kreuzstich bedeutet Wasser. Speicher dir das.",
  alt_en="One line, one meaning: water.",
  shots=["Slide 1 Hook", "Slide 2 Zickzack gezeichnet", "Slide 3 Zickzack am Band", "Slide 4 Warteliste"],
  ort=W, dauer="4 Slides", ton=S_RUHIG,
  cap="Zigzag = water. It frames the band on my right front pocket.", cta="LIST", check=["—"],
  docket="Reserve")

r(id="V110", phase="ab P1", slot="ORIGIN", fmt="Karussell / Photo Mode 4 Slides", title="Ornament in 15 Sekunden: Achtstern",
  hook_en="Eight points, one sun. Save this.",
  hook_de="Acht Zacken, eine Sonne. Speicher dir das.",
  alt_en="How to draw an eight-point star on a grid.",
  shots=["Slide 1 Hook", "Slide 2 Raster 27 × 27 leer", "Slide 3 Stern halb gezeichnet", "Slide 4 Stern fertig + Warteliste"],
  ort=W, dauer="4 Slides", ton=S_RUHIG,
  cap="The eight-point star stands for the sun. Mine: 27 × 27 stitches.", cta="LIST",
  check=["Nicht „Alatyr“", "Keine Haken- oder Drehformen"], docket="Reserve")

r(id="V111", phase="ab P1 (nicht 23.–29.11.2026)", slot="ORIGIN", fmt="Karussell / Photo Mode 4 Slides", title="Ornament in 15 Sekunden: drei Ähren",
  hook_en="Three wheat ears, nine gold threads. Here's why.",
  hook_de="Drei Ähren, neun Goldfäden. Darum.",
  alt_en="Why my back pocket has a harvest on it.",
  shots=["Slide 1 Hook", "Slide 2 drei Ähren gezeichnet", "Slide 3 Fäden", "Slide 4 Warteliste"],
  ort=W, dauer="4 Slides", ton=S_RUHIG,
  cap="Three ears on a red band, nine gold threads below. The harvest sits on the left.", cta="LIST",
  check=["Nie „fünf Ähren“", "Nicht in der Woche 23.–29.11.2026", "Nie Ähren und Serp zusammen auf Rot"], docket="Reserve")

r(id="V112", phase="ab P1", slot="ORIGIN", fmt="Karussell / Photo Mode 4 Slides", title="Ornament in 15 Sekunden: Lebensbaum",
  hook_en="Roots, trunk, crown. The tree on my waistband.",
  hook_de="Wurzeln, Stamm, Krone. Der Baum an meinem Bund.",
  alt_en="Why a tree sits where the label usually is.",
  shots=["Slide 1 Hook", "Slide 2 Skizze", "Slide 3 Größe 86 × 76 mm", "Slide 4 Warteliste"],
  ort=W, dauer="4 Slides", ton=S_RUHIG,
  cap="The tree of life takes the place of a leather label.", cta="LIST", check=["Nie „Slavic tree of life“"], docket="Reserve")

r(id="V113", phase="ab P1", slot="REAL", fmt="Video 9:16", title="Mein Fehler: die realistische Szene",
  hook_en="I designed this for a week. Then I scrapped it.",
  hook_de="Ich habe eine Woche daran gezeichnet. Dann habe ich es gestrichen.",
  alt_en="I'll show you my mistake: too many stitches.",
  shots=["Ausdruck der verworfenen Szene (Flachzeichnung auf Papier)", "Du streichst sie mit Edding durch", "Daneben die drei Ähren", "Du: „Too many colours for embroidery.“"],
  ort=W, dauer="20–30 s", ton=S_OTON,
  cap="Version 1.5 had a realistic harvest scene. Beautiful on screen, too many colours and stitches for embroidery. I went back to three ears. Simpler, and it saves money.",
  cta="LIST", check=["Nur Papier-Ausdruck einer Flachzeichnung, kein Garment-Mockup", "Keine Sichel neben Ähren auf rotem Grund im Bild"],
  docket="Reserve · Format „Ich zeige dir meinen Fehler“")

r(id="V114", phase="ab P1", slot="REAL", fmt="Video 9:16", title="Mein Fehler: Deadline verpasst",
  hook_en="I missed my own design deadline. Here's the cost.",
  hook_de="Ich habe meine eigene Design-Deadline verpasst. Das hat es gekostet.",
  alt_en="Day {day}: my plan slipped. Here's how I fixed it.",
  shots=["Kalender: 05.10. durchgestrichen, 09.10. eingekreist", "Du, ehrlich, was sich verschoben hat", "Neue Regel auf Papier"],
  ort=W, dauer="20–30 s", ton=S_OTON,
  cap="Design freeze was 05.10. It happened on 09.10. Four days don't sound like much. They push everything after it.",
  cta="LIST", check=["Nur posten, wenn der Freeze am 09.10. wirklich gehalten hat"], docket="Reserve · Format „Fehler“")

r(id="V115", phase="ab P1", slot="DETAIL", fmt="Video 9:16 (zum Speichern)", title="Miss deine Lieblingsjeans",
  hook_en="Measure your favourite jeans in 60 seconds.",
  hook_de="Miss deine Lieblingsjeans in 60 Sekunden.",
  alt_en="Save this before you buy jeans online.",
  shots=["Jeans flach, zugeknöpft", "Bund quer, Zahl × 2", "Innenbein vom Schrittpunkt", "Zahl notieren", "Text: „your real size“"],
  ort=BODEN, dauer="30–45 s", ton=S_OTON,
  cap="Lay them flat, button them, measure straight across the top of the waistband, double it. That's your real waist. Save this.",
  cta="LIST", check=["Messregeln aus Spec 1.4"], docket="Reserve · Spar-Format, gut gegen Retouren")

r(id="V116", phase="ab P1", slot="BUILD", fmt="Video 9:16", title="Eine Stunde am Tag",
  hook_en="I build this brand in one hour a day.",
  hook_de="Ich baue diese Marke in einer Stunde am Tag.",
  alt_en="Day {day}: what one focused hour looks like.",
  shots=["Timer 60:00 startet", "Zeitraffer am Schreibtisch", "Was erledigt ist, auf Papier", "Timer 00:00"],
  ort=W, dauer="15–25 s", ton=S_TREND,
  cap="One to two hours a day. That's what I have for this drop. Here's today's hour.", cta="LIST",
  check=["Nur echte Aufgaben zeigen"], docket="Reserve · Build in Public")

r(id="V117", phase="ab P1", slot="REACH", fmt="Video-Antwort auf Kommentar", title="Antwort auf Kommentar",
  hook_en="Replying to: [Kommentar, max. 8 Wörter]",
  hook_de="Antwort auf: [Kommentar]",
  alt_en="Good question. Here's the honest answer.",
  shots=["Kommentar als Sticker (TikTok „mit Video antworten“, Instagram Kommentar-Sticker)", "Du antwortest in einem Take", "Ein Beweisbild (Papier, Maßband, Detail)"],
  ort=W, dauer="15–30 s", ton=S_OTON,
  cap="You asked, here's the answer.", cta="LIST",
  check=["Bei „Ist das russisch?“: ruhige Standardantwort aus zielgruppe.md 3.8, nie diskutieren"],
  docket="Reserve · jede Woche aus dem besten Kommentar")

r(id="V118", phase="ab P1", slot="DETAIL", fmt="Video 9:16", title="Stickmaschine ASMR",
  hook_en="Turn the sound on. This is 1,000 stitches.",
  hook_de="Ton an. Das sind 1.000 Stiche.",
  alt_en="The sound of my pattern being made.",
  shots=["Makro Stickkopf auf Stoffstück (beim Berliner Sticker, Woche 10, nur mit Erlaubnis)", "Garnwechsel", "Ergebnis auf dem Stoffstück"],
  ort="Berliner Sticker bei der Blank-Bemusterung (nur mit Erlaubnis), sonst Stickprobe zu Hause", dauer="10–20 s", ton="Maschinenton, keine Musik",
  cap="Sound on.", cta="LIST",
  check=["Vor dem 03.12.: nur Stoffstück, kein fertiger Zipper oder Polo im Bild", "Zahl 1.000 nur, wenn der Sticker sie für den Clip bestätigt"],
  docket="Reserve · Prozess-ASMR")

r(id="V119", phase="ab P1", slot="BUILD", fmt="Video 9:16", title="Wie ich die Höhe gefunden habe",
  hook_en="40 or 50 cm? How I placed one embroidery.",
  hook_de="40 oder 50 cm? Wie ich eine Stickerei platziert habe.",
  alt_en="10 centimetres changed the whole design.",
  shots=["Papiertest-Clip: Papier bei 40, 45, 50 cm", "Spiegel von vorn", "Entscheidung mit Lineal"],
  ort=SPIEGEL, dauer="15–25 s", ton=S_OTON,
  cap="I taped the same paper at three heights and walked. [Ergebnis] won.", cta="LIST",
  check=["Material vom Papiertest 3 (08.10.)", "Nur Papier"], docket="Reserve")

r(id="V120", phase="ab P1", slot="BUILD", fmt="Video 9:16", title="Die eine Frage an Fabriken",
  hook_en="One question filters most denim factories out.",
  hook_de="Eine Frage siebt die meisten Denim-Fabriken aus.",
  alt_en="Can you embroider before you sew?",
  shots=["Du am Tisch", "Frage auf Papier: „panel embroidery in-house?“", "Strichliste ja/nein"],
  ort=W, dauer="15–20 s", ton=S_OTON,
  cap="If they can't embroider the flat panel in-house, I can't work with them.", cta="LIST",
  check=["Echte Strichliste"], docket="Reserve · Fabriksuche")

r(id="V121", phase="ab P1", slot="REAL", fmt="Video 9:16", title="Warteliste-Stand",
  hook_en="[X] people on my list. Goal: 3,000.",
  hook_de="[X] Leute auf meiner Liste. Ziel: 3.000.",
  alt_en="Day {day}: is anyone actually signing up?",
  shots=["Shopify-Kundenzahl auf dem Bildschirm (ohne Namen)", "Ziel auf Papier", "Du: warum die Liste zählt"],
  ort=MAC, dauer="15–20 s", ton=S_OTON,
  cap="The list buys first and at the pre-order price. Right now: [X].", cta="LIST",
  check=["Keine Namen oder E-Mail-Adressen sichtbar", "Echte Zahl"], docket="Reserve · Zahlen offenlegen")

r(id="V122", phase="ab P1", slot="ASK", fmt="Story (Frage-Sticker) + spätere Collage", title="Schick mir deinen Teppich",
  hook_en="Send me a photo of your family's wall carpet.",
  hook_de="Schick mir ein Foto vom Teppich deiner Familie.",
  alt_en="Did your grandma have one of these?",
  shots=["Frame 1: dein Teppich-Foto + Frage-Sticker", "Später: Collage der Einsendungen (nur mit ausdrücklicher Erlaubnis)"],
  ort="Story-Vorlage", dauer="1 Frame", ton=S_KEINE,
  cap="(Story)", cta="STORY",
  check=["Einsendungen nur mit schriftlicher Erlaubnis zeigen", "Keine Sowjet-Deko in der Auswahl"], docket="Reserve · Teppich-Story (zielgruppe.md 5.2: Do 15.10.)")

r(id="V123", phase="ab P2", slot="REACH", fmt="Video 9:16", title="Straßenfrage",
  hook_en="Which pocket would you wear? Asking Berlin.",
  hook_de="Welche Tasche würdest du tragen? Ich frage Berlin.",
  alt_en="I showed strangers my jeans. Honest reactions.",
  shots=["Du zeigst zwei Details auf der Straße", "Antworten in einem Satz (nur mit Einwilligung vor der Kamera)", "Zählung am Ende"],
  ort="Berlin · Mauerpark-Flohmarkt sonntags (Sekundärquelle, vor Ort prüfen) oder vor Overkill, Köpenicker Straße 195A, Kreuzberg (Adresse aus Sekundärquelle, vor Ort prüfen). Im Laden nur mit Erlaubnis",
  dauer="20–35 s", ton="Originalton, Untertitel",
  cap="Two details, [X] strangers, one answer: [Ergebnis].", cta="LIST",
  check=["Personen nur mit Einwilligung zeigen", "Erst ab Proto (echtes Teil)"], docket="Reserve · ab Dezember")

r(id="V124", phase="ab P2", slot="DETAIL", fmt="Video 9:16", title="Auf links",
  hook_en="The inside of my embroidery. Turn it over.",
  hook_de="Die Innenseite meiner Stickerei. Dreh sie um.",
  alt_en="Good embroidery is clean on both sides.",
  shots=["Hose auf links", "Makro Rückseite mit Stabilisator", "Finger"],
  ort=FENSTER, dauer="8–12 s", ton=S_ASMR,
  cap="Inside out: cut-away stabiliser behind every embroidery so the denim doesn't pucker.", cta="LIST",
  check=["Ab Proto"], docket="Reserve")

r(id="V125", phase="ab P2", slot="REACH", fmt="Video 9:16", title="Aus drei Metern",
  hook_en="Can you spot the embroidery from here?",
  hook_de="Siehst du die Stickerei von hier?",
  alt_en="Walk closer. Then count the stitches.",
  shots=["Totale 3 m, Person steht still", "Ein Schritt pro Sekunde näher", "Makro"],
  ort=HOF, dauer="6–10 s", ton=S_TREND,
  cap="Wearable from far. A clock up close.", cta="LIST", check=["Ab Proto"], docket="Reserve · Variante zu V030")


# ---------------- COUNTDOWN T-24 ... T-1 (29.03.-21.04.2027) ----------------
CD = []
def c(n, date, motiv, hook_en, hook_de, shots, ort, cap, real=None, check=None):
    CD.append(dict(id="CD-T%02d" % n, n=n, date=date, motiv=motiv, hook_en=hook_en, hook_de=hook_de,
                   shots=shots, ort=ort, cap=cap, real=real, check=check or []))

c(24, "2027-03-29", "Ganzkörper vorn, langsamer Zoom auf die Tasche", "24 days. 100 numbered jeans. 22.04., 19:00.", "24 Tage. 100 nummerierte Jeans. 22.04., 19 Uhr.",
  ["Ganzkörper vorn aus dem Shoot", "Langsamer Zoom auf die rechte Vordertasche"], SHOOT, "The countdown starts. 100 numbered pairs.")
c(23, "2027-03-30", "Band A im Makro, Schwenk entlang der Tasche", "23 days. The cross-stitch band, up close.", "23 Tage. Das Kreuzstich-Band, ganz nah.",
  ["Makro-Schwenk entlang Band A"], SHOOT, "23 mm, 17 stitches high.",
  real="Ware ca. 30.03.: Kommt die Lieferung, ersetzt ein Live-Clip „They're here.“ das Asset")
c(22, "2027-03-31", "Münztasche E, Lineal daneben", "22 days. The smallest pocket, fully stitched.", "22 Tage. Die kleinste Tasche, voll bestickt.",
  ["Makro Münztasche", "Lineal 60 mm"], SHOOT, "60 × 60 mm, 45 × 45 stitches.",
  real="Prüfung 31.03.–02.04.: Clip „Checking 100 pairs, one by one.“ ersetzt das Asset")
c(21, "2027-04-01", "Linke Gesäßtasche: drei Ähren, rotes Band, Goldfäden", "21 days. Three ears, nine threads.", "21 Tage. Drei Ähren, neun Fäden.",
  ["Makro linke Gesäßtasche", "Fäden hängen still"], SHOOT, "The harvest sits on the left.", check=["Kein Serp im Bild", "Nie „fünf“"])
c(20, "2027-04-02", "Goldfäden in Bewegung", "20 days. The only part that moves.", "20 Tage. Das Einzige, was sich bewegt.",
  ["Fön kleinste Stufe oder Gehen, Fäden schwingen, Gegenlicht"], SHOOT, "Set by hand after the wash.")
c(19, "2027-04-03", "Achtstern auf der rechten Gesäßtasche, Kamera kommt näher", "19 days. One star, 27 by 27 stitches.", "19 Tage. Ein Stern, 27 mal 27 Stiche.",
  ["Kamera fährt langsam an die rechte Gesäßtasche"], SHOOT, "The eight-point star stands for the sun.", check=["Nicht „Alatyr“"])
c(18, "2027-04-04", "Lebensbaum-Patch, Zoom auf Knoten und Wurzeln", "18 days. A tree where the label usually is.", "18 Tage. Ein Baum, wo sonst das Label sitzt.",
  ["Zoom auf Knoten und Wurzeln des Patches"], SHOOT, "Tree of life, natural linen, 86 × 76 mm.", check=["Nie „Slavic tree of life“"])
c(17, "2027-04-05", "Gruppenbild Jeans, Zipper, Polo", "17 days. Three pieces, one drop.", "17 Tage. Drei Teile, ein Drop.",
  ["Gruppenbild aus dem Shoot"], SHOOT, "Jeans €169, zipper €139, polo €79.")
c(16, "2027-04-06", "Zipper-Rücken mit dem Medaillon", "16 days. A wall carpet, on your back.", "16 Tage. Ein Wandteppich, auf deinem Rücken.",
  ["Zipper-Rücken, langsamer Schwenk"], SHOOT, "The medallion of a wall carpet.",
  real="Vorbestellungen gehen raus (06.–07.04.): Clip „Pre-orders shipping today.“ ersetzt das Asset")
c(15, "2027-04-07", "Polo, Bänder an der Knopfleiste", "15 days. Two bands at the placket.", "15 Tage. Zwei Bänder an der Knopfleiste.",
  ["Makro Knopfleiste"], SHOOT, "Polo €79, made to order.",
  real="Letzte Vorbestellungen raus: Clip vom Packtisch ersetzt das Asset")
c(14, "2027-04-08", "Hangtag mit Nummer 001 in der Hand", "Two weeks. Number 001 has already shipped.", "Zwei Wochen. Nummer 001 ist schon unterwegs.",
  ["Hangtag 001 in der Hand", "Text „2 weeks“"], SHOOT, "Two weeks. The list gets in at 18:00.", check=["Nur wenn wahr: Vorbestellungen gehen laut Plan am 06.–07.04. raus"])
c(13, "2027-04-09", "Behind the Scenes vom Shoot, schnell geschnitten", "13 days. How we shot this.", "13 Tage. So haben wir das gedreht.",
  ["BTS-Schnitte, 0,5 s je Clip"], SHOOT, "One Saturday, one sunset.")
c(12, "2027-04-10", "Rohe Schnittkante am Saum", "12 days. Raw hem, cut after the wash.", "12 Tage. Roher Saum, nach der Wäsche geschnitten.",
  ["Finger fährt die Saumkante entlang"], SHOOT, "No turn-up. No stitch.",
  real="Wenn Vorbesteller Fotos mit Erlaubnis geschickt haben: ein Foto ersetzt das Asset")
c(11, "2027-04-11", "Zickzack am Band", "11 days. Zigzag means water.", "11 Tage. Zickzack bedeutet Wasser.",
  ["Makro Zickzack"], SHOOT, "The line that frames the band.")
c(10, "2027-04-12", "Teppich-Foto, harter Schnitt auf das Medaillon", "10 days. From the wall to the zipper.", "10 Tage. Von der Wand auf den Zipper.",
  ["Teppich-Foto 1 s", "Harter Schnitt auf das Medaillon"], SHOOT + " + Familienfoto", "The carpet, remembered.", check=["Keine Sowjet-Deko im Bild"])
c(9, "2027-04-13", "Innenseite der Stickerei, Hose auf links", "9 days. Turn it inside out.", "9 Tage. Dreh sie auf links.",
  ["Hose auf links, Makro Rückseite"], SHOOT, "Clean on both sides.")
c(8, "2027-04-14", "Gehen, Rückansicht", "8 days. Watch the back.", "8 Tage. Schau auf die Rückseite.",
  ["Gehen, Rückansicht, Fäden schwingen"], SHOOT, "Left: harvest. Right: pattern.", check=["Serp nicht im Bild"])
c(7, "2027-04-15", "Ganzkörper hinten, Text „Noch 1 Woche“", "One week. 22.04., 19:00.", "Noch eine Woche. 22.04., 19 Uhr.",
  ["Ganzkörper hinten", "Text „1 week“"], SHOOT, "One week. The list gets in at 18:00.")
c(6, "2027-04-16", "Seitennaht im Streiflicht: der Serp über den Stoppeln", "6 days. The field after the harvest.", "6 Tage. Das Feld nach der Ernte.",
  ["Streiflicht über die Seitennaht links"], SHOOT, "Harvest blade over cut stubble.", check=["Kein Stern, Hammer, roter Grund", "Ähren-Tasche nicht im Bild"])
c(5, "2027-04-17", "Pflegeetikett „Fäden nicht abschneiden“", "5 days. Rule one: don't cut the threads.", "5 Tage. Regel eins: Fäden nicht abschneiden.",
  ["Makro Pflegeetikett"], SHOOT, "Wash inside out.")
c(4, "2027-04-18", "Hand in der Tasche, Detail", "4 days. Hands in pockets.", "4 Tage. Hände in die Taschen.",
  ["Hand gleitet in die rechte Vordertasche, Band im Fokus"], SHOOT, "The band sits on the pocket edge.")
c(3, "2027-04-19", "Papiertest aus dem Oktober, harter Schnitt auf das fertige Teil", "3 days. This was paper in October.", "3 Tage. Das war im Oktober Papier.",
  ["Papiertest-Clip 1,5 s", "Harter Schnitt auf das fertige Teil, gleiche Einstellung"], ARCHIV + " + " + SHOOT, "October → April.")
c(2, "2027-04-20", "Alle fünf Stickereien, je 1 Sekunde", "2 days. Five embroideries, one second each.", "2 Tage. Fünf Stickereien, je eine Sekunde.",
  ["A", "E", "B", "B2", "C", "D"], SHOOT, "Band, pocket, harvest, star, tree.", check=["B und B2 in getrennten Einstellungen"])
c(1, "2027-04-21", "Kampagnenfilm auf 10 Sekunden, Text „Morgen 19:00“", "Tomorrow, 19:00. The list gets in at 18:00.", "Morgen, 19 Uhr. Die Liste kommt um 18 Uhr rein.",
  ["Kampagnenfilm, 10 s", "Endframe „tomorrow 19:00“"], SHOOT, "Tomorrow.")


# ---------- Shot-Ergänzungen (jedes Konzept 3–6 Einstellungen) ----------
SHOTS_FIX = {
 "V024": ["Papierband A an der Tasche, 0,5 s", "Münztasche E aus Papier, 0,5 s", "Serp-Papier B am Bein (eigene Einstellung), 0,5 s", "Ähren-Papier B2 an der Gesäßtasche (eigene Einstellung), 0,5 s", "Achtstern C und Patch D, je 0,5 s", "Letzter Frame: „Thu.“"],
 "V030": ["Ein Take: Handy startet 3 m entfernt, Person mit Proto steht im Hinterhof", "Person geht langsam auf die Kamera zu, Kamera bleibt auf Hüfthöhe", "Endet im Makro auf der Münztasche E, Finger tippt drauf"],
 "V038": ["Zeitachse von Hand auf Papier schreiben (Draufsicht, Zeitraffer)", "Termine: 04.01. final sample · 14.01. pre-order · Feb production · 20.02. shoot · 22.04. drop", "Du hakst mit rotem Stift ab, was erledigt ist", "Finger auf „22.04.“"],
 "V046": ["Makro Band A, 1 s", "Makro Goldfäden, 1 s", "Makro Achtstern, 1 s", "Endframe: „14.01. · 19:00“"],
 "V049": ["Ablauf auf Papier schreiben: 18:00 reminder email · 19:00 open · 19:05 live", "Handy mit Shop-Vorschau (Entwurf)", "Du in die Kamera, ein Satz: „See you Thursday.“"],
 "V051": ["Makro Goldfäden, langsam", "Hangtag 001 in der Hand", "Endframe: „tomorrow 19:00“"],
 "V060": ["Hangtag-Stapel auf dem Tisch", "Zeitraffer: Hand nimmt für jede Vorbestellung einen Hangtag weg", "Echte Restzahl groß", "Endframe: „€149 until 21.03.“"],
 "V066": ["Bildschirm: Bestellbestätigung an die Fabrik (Namen verpixelt)", "Deine Reaktion, ein Atemzug", "Text: „[100] pairs ordered“"],
 "V067": ["Banking-App, Betrag sichtbar, Empfänger verpixelt", "Du erklärst 50/50 in einem Satz", "Papier: „paid by [X] pre-orders“", "Endframe: „production starts Monday“"],
 "V068": ["Fotos oder Clips der Fabrik (nur mit schriftlicher Erlaubnis)", "Ohne Erlaubnis: Tech Pack auf dem Tisch, Kalender bis Ende März", "Du, ein Satz: „Next update: first inline photos.“"],
 "V070": ["Stoffrolle in der Fabrik (mit Erlaubnis) oder dein Stoffmuster in Großaufnahme", "Hand fährt über den Stoff", "Text: „[100] pairs“"],
 "V075": ["Jeans auf Bügel, 1 s", "Zipper-Rücken, 1 s", "Polo-Knopfleiste, 1 s", "Endframe: „22.04.“"],
 "V079": ["Kampagnenfilm, 30 s, aus dem Shoot", "Fünf Stickereien in getrennten Einstellungen", "Sonnenuntergang als letzte Einstellung", "Endframe: „22.04. · 19:00“"],
 "V081": ["Papiertest-Clip vom Oktober", "Stickprobe November", "Proto-Unboxing Dezember", "Shoot-Bild Februar", "Endframe: „22.04.“"],
 "V083": ["Hangtag mit der echten Nummer der letzten Vorbestellung", "Hand legt ihn auf den Stapel „taken“", "Freie Nummern daneben"],
 "V086": ["Inline-Fotos der Fabrik (nur mit Erlaubnis)", "Deine Prüf-Notizen daneben", "Du, ein Satz zum Befund"],
 "V087": ["Slide 1 Hook", "Slide 2 Das Teil + fünf Stickereien", "Slide 3 Goldfäden", "Slide 4 Ehrliche Größen", "Slide 5 Preis und Termine", "Slide 6 Warteliste und Vorbestellung"],
 "V088": ["Proto gefaltet auf dem Tisch", "Hangtag dran, Karte rein", "Paket zu, Klebeband (ASMR)"],
 "V089": ["Gegenlicht im Sonnenuntergang, Goldfäden schwingen", "Makro Ähren", "Person geht aus dem Bild"],
 "V091": ["Kalender, Sonntag 21.03. rot umkringelt", "Echte Restzahl auf Papier", "Du, ein Satz: „Sunday 20:00, then it's €169.“"],
 "V093": ["Papiertest-Clip vom Oktober (gleiche Kameraposition, Klebeband-Markierung am Boden)", "Harter Schnitt auf das fertige Teil, gleiche Einstellung", "Makro auf dieselbe Tasche"],
 "V097": ["Du in die Kamera", "Teppich-Foto", "Fertiges Teil, Makro", "Endframe: „22.04.“"],
 "V098": ["Zeitraffer: Wohnzimmer wird zur Packstraße", "Kartons, Hangtags, Klebeband", "Erster gepackter Karton"],
 "V102": ["Kampagnenfilm, 15 s", "Handy zeigt den Shop live", "Endframe: „live now“"],
 "V106": ["Handschrift: verkauft, Umsatz, Kosten", "Du, ehrlich, zwei Sätze", "Was du anders machst, ein Satz auf Papier"],
}
for _e in E:
    if _e["id"] in SHOTS_FIX:
        _e["shots"] = SHOTS_FIX[_e["id"]]
    if _e["id"] == "V055":
        _e["alt_en"] = "Thank you. Here's the real number."
