# -*- coding: utf-8 -*-
"""Content W22–W34 (08.02.–09.05.2027): Vorbestellung, Bestellung, Produktion, Shoot, Autopilot."""
from clib import V, S

V("V237", "BUILD", "Zwischenstand", ("2027-02-08", "18:00"), ("2027-02-07", 20), old=("V055",), cta='vor',
  ziel="Echte Zahl nach einer Woche. Wer zögert, sieht: es bewegt sich.",
  dauer="12–15 s",
  hook=("Day 70: [X] of 35 pairs pre-ordered.", "Tag 70: [X] von 35 Paar vorbestellt."),
  alt=["One week of pre-order. The real number."],
  beats=[["0–3 s", "Papier mit Strichliste, Hand macht den letzten Strich", "[X] / 35", "Stimme liest den Hook"],
         ["3–9 s", "Stapel Innenetikett-Ausdrucke mit den vergebenen Nummern", "numbers taken: 001–0[X]", "Stimme: „Numbers one to [X] have owners.“"],
         ["9–13 s", "Endkarte", "[35−X] left at €149", ""]],
  dreh=["Papier von oben, echte Zahl aus Shopify."], ort="Tisch", req="Papier, Stift",
  schnitt=["Vorlage BUILD.", "Untertitel Englisch."], cover="„[X] / 35“",
  cap="One week of pre-order: [X] of 35 pairs at €149 are gone. [35−X] left at that price, then €169.",
  de="Eine Woche: [X] von 35.", kom="Thank you to the first [X]. 🙏",
  story="Link-Sticker ?ref=st-v237.", tags="#buildinpublic #preorder",
  check="Nur die echte Zahl aus Shopify. Unter 5: Post durch V239 ersetzen und die Zahl nicht zeigen.")

V("V238", "REAL", "Noch Y Paar", ("2027-02-09", "18:00"), ("2027-02-07", 15), old=("V060",), cta='vor',
  ziel="Knappheit mit echter Zahl.", dauer="8–10 s",
  hook=("[Y] pairs left at €149.", "Noch [Y] Paar zu 149 €."),
  alt=["After these, €169."],
  beats=[["0–3 s", "Innenetiketten, die freie Nummer nah", "[Y] left", "Beat"], ["3–8 s", "Gehen von hinten", "then €169", ""], ["8–10 s", "Endkarte", "link in bio", ""]],
  dreh=["Archiv-Clips plus ein neues Etikett-Bild."], ort="Tisch", req="—",
  ton="Titel aus der Commercial Music Library.", schnitt=["10 s."], cover="„[Y] left“",
  cap="[Y] pairs left at €149. After that, €169 until 06.06.", de="Noch [Y] Paar zu 149 €.",
  kom="Size questions? Ask below.", story="Link-Sticker ?ref=st-v238.", tags="#preorder #limitededition",
  check="Nur echte Zahl.")

S("S10", "Q&A zur Vorbestellung", ("2027-02-10", "12:00"), old=("V059",),
  ziel="Einwände am Tag des Mess-Abends 2 beantworten.",
  frames=[["Foto: du mit PP", "Frag mich alles zur Vorbestellung.", "Frage-Sticker"],
          ["Ab 17:00 Antworten: Frage als Bild, Antwort als 10-s-Clip", "", ""],
          ["Foto: Ort des Mess-Abends", "Heute 18:00–20:00: Mess-Abend. Probier deine Größe.", "Link-Sticker"]],
  folge="Fragen ins Blatt „Einwände“, FAQ ergänzen, wenn eine Frage zweimal kommt.")

V("V239", "ORIGIN", "Vor dem Nähen gestickt", ("2027-02-12", "18:00"), ("2027-02-07", 25), old=("V020", "W22-ORIGIN"), cta='vor',
  ziel="Handwerks-Erklärung: warum Panel-Stickerei. Für Denim-Käufer.",
  dauer="20–24 s",
  hook=("You can't embroider a finished pair of jeans. Here's why.", "Eine fertige Jeans kann man nicht besticken."),
  alt=["Why my jeans get embroidered before they're sewn."],
  beats=[["0–3 s", "Fertige Jeans, Hand versucht, sie in einen Stickrahmen zu legen", "a sewn leg doesn't fit", "Stimme liest den Hook"],
         ["3–12 s", "Skizze: Zuschnittteil flach, Stickerei, dann Nähen", "cut → embroider → sew → wash", "Stimme: „So the pattern goes on the flat panels first, then the jeans is sewn, then washed.“"],
         ["12–19 s", "Makro Band A an der Taschenkante", "that's why the band sits exactly on the edge", "Stimme"],
         ["19–22 s", "Endkarte", "pre-order open", ""]],
  dreh=["Stickrahmen (vom Stick-Abend) und Jeans.", "Skizze von Hand, von oben."], ort="Tisch", req="Stickrahmen, Jeans, Skizze",
  schnitt=["Vorlage BUILD.", "Untertitel Englisch."], cover="Rahmen und Jeans, Text „Why it can't work“",
  cap="A sewn leg doesn't fit under an embroidery machine. So the pattern goes on the flat cut panels first, then the jeans is sewn and washed. That's why the band sits exactly on the pocket edge.",
  de="Erst sticken, dann nähen, dann waschen.", kom="Did you know this?", story="Link-Sticker ?ref=st-v239.",
  tags="#denim #manufacturing #embroidery", check="")

S("S11", "Montag entscheidet", ("2027-02-13", "12:00"), old=("V064",),
  ziel="Letzter Schub vor der Schwelle am Mo 15.02.",
  frames=[["Foto: Strichliste", "Montag entscheide ich, ob 100 Paar gemacht werden.", ""],
          ["Foto: PP", "Wer noch will: bis Sonntag zum Vorbestellpreis.", "Link-Sticker ?ref=st-s11"]],
  folge="Keine erfundene Dringlichkeit. Ist die Schwelle schon erreicht: Text ändern auf „Montag bestelle ich bei der Fabrik.“")

V("V240", "BUILD", "100 oder 75", ("2027-02-15", "18:00"), None, old=("V065",), pm=40, cta='vor',
  ziel="Die Schwellen-Entscheidung öffentlich und ehrlich.", dauer="20–25 s",
  hook=("100 pairs or 75? Today I decide.", "100 oder 75 Paar? Heute entscheide ich."),
  alt=["The threshold day."],
  beats=[["0–3 s", "Du am Tisch mit der Rechnung", "100 or 75?", "Stimme liest den Hook"],
         ["3–14 s", "Papier: ausgezahlte Vorbestellungen, Hochrechnung, Mengenformel", "the maths", "Stimme erklärt in 2 Sätzen"],
         ["14–20 s", "Du kreist die Entscheidung ein", "[100 / 75 / later]", "Stimme: die Entscheidung"],
         ["20–23 s", "Endkarte", "factory order: Wednesday", ""]],
  dreh=["Am Mo nach der Entscheidung um 10:30 drehen, um 18:00 posten."], ort="Tisch", req="Rechnung, Stift",
  schnitt=["Vorlage BUILD.", "Untertitel Englisch."], cover="„100 or 75?“",
  cap="Today was the threshold. [Result in one sentence]. The factory order goes out on Wednesday.",
  de="Schwellen-Tag: [Ergebnis].", kom="Thank you. Seriously.", story="Link-Sticker ?ref=st-v240.",
  tags="#buildinpublic #smallbusiness", check="Nur die echte Entscheidung.")

V("V241", "REACH", "Bestellt.", ("2027-02-17", "19:00"), None, old=("V066",), pm=30, cta='vor',
  ziel="Meilenstein, kurz und stark.", dauer="6–8 s",
  hook=("I just ordered [100] jeans.", "Gerade [100] Jeans bestellt."),
  alt=["Sent."],
  beats=[["0–3 s", "Finger über „Senden“", "", "Ticken"], ["3–5 s", "Klick", "Sent.", "Schlag"], ["5–8 s", "Text", "[100] pairs · ready 14.05.", ""]],
  dreh=["Bildschirmaufnahme, nur der Senden-Knopf, kein Empfänger."], ort="Mac", req="—",
  ton="Ticken plus Schlag.", schnitt=["8 s."], cover="„Sent.“",
  cap="I just sent the order for [100] pairs. Ready by 14.05.", de="Bestellt.", kom="🧵", story="Link-Sticker ?ref=st-v241.",
  tags="#buildinpublic", check="Kein Fabrikname, keine Summe.")

V("V242", "REAL", "Überwiesen", ("2027-02-19", "18:00"), ("2027-02-18", 30), old=("V067",), cta='vor',
  ziel="Ehrlichkeit über Geld: Anzahlung bezahlt, woher das Geld kommt.", dauer="18–22 s",
  hook=("I just paid the factory. Here's where the money came from.", "Gerade die Fabrik bezahlt. Daher kommt das Geld."),
  alt=["The deposit."],
  beats=[["0–3 s", "Banking-App, Betrag unscharf", "deposit paid", "Stimme liest den Hook"],
         ["3–12 s", "Papier: Kreis-Diagramm von Hand: mein Geld · Vorbestellungen", "my money · your pre-orders", "Stimme: „Half my savings, half your pre-orders.“"],
         ["12–19 s", "Proto in der Hand", "thank you", "Stimme: „Without the first [X], this wouldn't exist.“"],
         ["19–21 s", "Endkarte", "TIME TRAVEL", ""]],
  dreh=["Banking-App nur mit unscharfem Betrag."], ort="Tisch", req="Papier, Stift",
  schnitt=["Vorlage BUILD.", "Untertitel Englisch."], cover="Diagramm",
  cap="Deposit paid. Roughly half my own savings, half your pre-orders. Without the first [X], these 100 pairs wouldn't exist.",
  de="Anzahlung bezahlt.", kom="If you pre-ordered: you're in this video. 🙏", story="Link-Sticker ?ref=st-v242.",
  tags="#smallbusiness #buildinpublic", check="Keine Kontodaten, keine genaue Summe.")

V("V243", "BUILD", "In Produktion", ("2027-02-22", "18:00"), ("2027-02-21", 25), old=("V068",), cta='vor',
  ziel="Produktionsstart mit Fotos der Fabrik (nur mit Erlaubnis).", dauer="15–20 s",
  hook=("My jeans are in production.", "Meine Jeans sind in Produktion."),
  alt=["Day 84: cutting started."],
  beats=[["0–3 s", "Foto der Fabrik: Stoffballen (mit Erlaubnis, ohne Gesichter)", "in production", "Stimme liest den Hook"],
         ["3–12 s", "Fotos: Zuschnitt, bestickte Panels", "cut → embroider", "Stimme"],
         ["12–17 s", "Kalender: 14.05. eingekreist", "ready 14.05.", ""],
         ["17–19 s", "Endkarte", "pre-order open", ""]],
  dreh=["Nur Fotos, die die Fabrik freigibt."], ort="—", req="Fabrik-Fotos",
  schnitt=["Fotos mit leichtem Zoom.", "Untertitel Englisch."], cover="Stoffballen",
  cap="Production started: cutting first, then the flat panels get embroidered. Ready by 14.05.",
  de="In Produktion.", kom="What step do you want to see?", story="Link-Sticker ?ref=st-v243.",
  tags="#manufacturing #denim", check="Keine Gesichter von Arbeitern, kein Fabrikname, keine Logos.")

V("V244", "ORIGIN", "In 8 Schritten", ("2027-02-23", "18:00"), ("2027-02-21", 30), old=("V069",), cta='vor',
  plattform="Instagram-Karussell, TikTok Photo Mode", kind='karussell',
  ziel="Speicherbares Erklär-Karussell.", dauer="9 Bilder",
  hook=("How 100 embroidered jeans get made, in 8 steps.", "So entstehen 100 bestickte Jeans, in 8 Schritten."),
  alt=["Save this."],
  beats=[["Bild 1", "Proto", "8 steps", ""], ["Bild 2", "Stoff", "1 fabric", ""], ["Bild 3", "Zuschnitt", "2 cut", ""],
         ["Bild 4", "Stickerei", "3 embroider the flat panels", ""], ["Bild 5", "Nähen", "4 sew", ""], ["Bild 6", "Wäsche", "5 wash", ""],
         ["Bild 7", "Goldfäden", "6 nine threads by hand", ""], ["Bild 8", "Nieten, Knopf, Patch", "7 hardware + patch", ""],
         ["Bild 9", "Prüfung", "8 I check every pair", ""]],
  dreh=["Fotos 4:5, eigene oder freigegebene Fabrikfotos."], ort="—", req="Fotos",
  schnitt=["1080 × 1350, Schrift aus dem Content-Look."], cover="Bild 1",
  cap="How 100 embroidered jeans get made: fabric, cut, embroider the flat panels, sew, wash, nine gold threads by hand, hardware and patch, then I check every pair.",
  de="So entsteht Time Travel, in 8 Schritten.", kom="Save for later.", story="Link-Sticker ?ref=st-v244.",
  tags="#howitsmade #denim", check="")

V("V245", "REACH", "Diese Rolle", ("2027-02-25", "19:00"), None, old=("V070",), pm=15, cta='vor',
  ziel="Kurzer Loop zum Stoff.", dauer="6–8 s",
  hook=("This roll becomes [100] pairs.", "Aus dieser Rolle werden [100] Paar."),
  alt=["One roll."],
  beats=[["0–3 s", "Stoffrolle (Fabrikfoto oder -clip)", "This roll", "Beat"], ["3–6 s", "Schnitt auf die fertige Jeans", "becomes [100] pairs", ""], ["6–8 s", "Endkarte", "", ""]],
  dreh=["Clip der Fabrik oder Foto."], ort="—", req="—", ton="Titel mit Schlag.", schnitt=["8 s."], cover="Rolle",
  cap="This roll becomes [100] pairs.", de="Eine Rolle, [100] Paar.", kom="🧵", story="Link-Sticker ?ref=st-v245.", tags="#denim",
  check="Kein Post am Mi 24.02. (Jahrestag). Dieser Post läuft am Do.")

V("V246", "DETAIL", "Hangtag und Karte", ("2027-02-26", "18:00"), ("2027-02-26", 30), old=("V071",), cta='vor',
  ziel="Die Bedeutungskarte zeigen (V6): die Erklärung, die man bei sich trägt.", dauer="15–18 s",
  hook=("The inside tells the story.", "Die Geschichte steckt im Etikett."),
  alt=["Every pair comes with a map."],
  beats=[["0–3 s", "Hangtag an der Jeans, Hand klappt die Karte auf", "the inside tells the story", "Stimme liest den Hook"],
         ["3–12 s", "Karte innen: Zeichnung mit A, E, B2, C, D", "A · E · B2 · C · D", "Stimme liest zwei Sätze der Karte"],
         ["12–16 s", "Innenetikett „Nr. 0__/100“", "and your number", ""],
         ["16–18 s", "Endkarte", "", ""]],
  dreh=["Gedruckte Karte (Druck heute), Tageslicht."], ort="Tisch", req="Hangtag, Karte, PP",
  schnitt=["Vorlage DETAIL.", "Untertitel Englisch."], cover="Karte offen",
  cap="Every pair comes with a folded card: a drawing of the jeans and one line for each embroidery. The explanation you carry with you.",
  de="Die Karte zur Jeans.", kom="Would you keep the card?", story="Link-Sticker ?ref=st-v246.", tags="#packaging #detail",
  check="Nur Bedeutungen mit Beleg. Die Nummer steht auf dem Innenetikett, nicht auf dem Hangtag.")

S("S12", "Casting für den Shoot", ("2027-02-27", "12:00"), old=("V072",),
  ziel="Leute für den Shoot am Sa 06.03. finden (Größen W30, W34, W36/38).",
  frames=[["Foto: PP", "Shoot am Sa 06.03. in Berlin. Willst du dabei sein?", "Umfrage: Ja · Nein"],
          ["Text", "Gesucht: Bundweite 76, 86 oder 91–96 cm. Kein Modelvertrag, ein Nachmittag, ein Paar als Dank.", "Frage-Sticker „Deine Bundweite“"]],
  folge="Antworten mit passender Größe persönlich anschreiben. Einwilligung schriftlich vor dem Shoot (Aufgabe Do 04.03.).",
  check="Unter 18: nur mit Einwilligung der Eltern.")

V("V247", "BUILD", "Ein Shoot mit 150 €", ("2027-03-01", "18:00"), ("2027-02-28", 25), old=("V073",), cta='vor',
  ziel="Shoot ankündigen, Budget ehrlich.", dauer="15–18 s",
  hook=("Planning a shoot on €150.", "Einen Shoot mit 150 € planen."),
  alt=["Saturday: the first real photos."],
  beats=[["0–3 s", "Moodboard am Bildschirm", "€150 shoot", "Stimme liest den Hook"],
         ["3–12 s", "Packliste auf Papier: Teppich, Trockenweizen, Graukarte, 3 Paar", "the list", "Stimme"],
         ["12–16 s", "Kalender 06.03.", "Saturday", ""]],
  dreh=["Moodboard, Packliste."], ort="Schreibtisch", req="Moodboard, Packliste",
  schnitt=["Vorlage BUILD."], cover="„€150 shoot“",
  cap="Saturday is the first real shoot. Budget: €150. One room with a carpet, then golden hour.",
  de="Samstag: der erste echte Shoot.", kom="Guess the location.", story="Link-Sticker ?ref=st-v247.", tags="#photoshoot #buildinpublic",
  check="Kein Weizen unter blauem Himmel, keine Sichel, kein roter Hintergrund.")

V("V248", "REACH", "Drei Teile, ein Drop", ("2027-03-03", "19:00"), ("2027-02-28", 20), old=("V075",), cta='vor',
  ziel="Das Set zeigen: Jeans, Zipper, Polo (Polo nur, wenn entschieden).", dauer="7–9 s",
  hook=("Jeans, zip hoodie, polo. One drop. 24.06.", "Jeans, Zipper, Polo. Ein Drop."),
  alt=["The full set."],
  beats=[["0–2 s", "Jeans", "jeans", "Schlag"], ["2–4 s", "Zipper", "zip hoodie", "Schlag"], ["4–6 s", "Polo (oder Polo-Skizze)", "polo", "Schlag"], ["6–8 s", "Endkarte", "24.06., 19:00", ""]],
  dreh=["Drei Teile nacheinander am Bügel, gleiche Wand."], ort="helle Wand", req="PP, Zipper-Muster, Polo-Muster",
  ton="Titel mit drei Schlägen.", schnitt=["8 s, Schnitt auf jeden Schlag."], cover="Drei Teile",
  cap="Jeans, zip hoodie, polo. One drop on 24.06.", de="Drei Teile, ein Drop.", kom="Which one first?", story="Umfrage Jeans/Zipper/Polo, Link ?ref=st-v248.",
  tags="#drop #fashion", check="Polo nur zeigen, wenn es ein Muster gibt; sonst nur Jeans und Zipper.")

V("V249", "DETAIL", "Der Zipper vorn", ("2027-03-05", "18:00"), ("2027-02-28", 25), old=("V074", "V076"), cta='vor',
  ziel="Zipper-Detail für die Drop-Zielgruppe.", dauer="15–18 s",
  hook=("A wall carpet on the front. A pattern under the hood.", "Ein Wandteppich vorn. Ein Muster unter der Kapuze."),
  alt=["The zip hoodie, every detail."],
  beats=[["0–3 s", "Zipper vorn, Teppich", "carpet front", "Stimme liest den Hook"],
         ["3–9 s", "Fransen, gestickte Kante, Reißverschluss mit Achtstern-Anhänger", "fringes · stitched edge · star pull", ""],
         ["9–14 s", "Kapuze hoch, Rückendruck", "hood up", ""],
         ["14–17 s", "Stern auf der Saumrippe", "star on the rib", ""]],
  dreh=["Zipper-Muster, Makros, Tageslicht."], ort="Spiegel und Tisch", req="Zipper-Muster",
  schnitt=["Vorlage DETAIL.", "Untertitel Englisch."], cover="Teppich nah",
  cap="The zip hoodie: carpet front on cotton velvet, fringes, a stitched edge, the eight-point star on the pull and on the rib, and the coin-pocket pattern under the hood.",
  de="Der Zipper im Detail.", kom="Hood up or down?", story="Link-Sticker ?ref=st-v249.", tags="#zipper #hoodie #detail")

V("V250", "BUILD", "Hinter den Kulissen", ("2027-03-08", "18:00"), ("2027-03-07", 30), old=("V077",), cta='vor',
  ziel="Shoot-Making-of, Nähe.", dauer="20–25 s",
  hook=("Behind the scenes of my first shoot.", "Hinter den Kulissen meines ersten Shoots."),
  alt=["€150 shoot, here's how it went."],
  beats=[["0–3 s", "Aufbau, Teppich an der Wand", "behind the scenes", "Stimme liest den Hook"],
         ["3–15 s", "Schnelle Folge: Licht, Graukarte, Model probiert, du fotografierst", "", "Originalton"],
         ["15–21 s", "Goldene Stunde draußen", "golden hour", ""],
         ["21–24 s", "Endkarte", "", ""]],
  dreh=["Am Shoot-Tag nebenbei mit dem zweiten Handy (Freund), nur Leute mit Einwilligung."], ort="Shoot-Ort", req="—",
  schnitt=["Vorlage BUILD."], cover="Aufbau", cap="Behind the scenes of the first Time Travel shoot: one room, one carpet, then golden hour.",
  de="Hinter den Kulissen.", kom="Photos drop this week.", story="Link-Sticker ?ref=st-v250.", tags="#behindthescenes #photoshoot",
  check="Nur Personen mit schriftlicher Einwilligung.")

V("V251", "REACH", "Das erste Bild", ("2027-03-10", "19:00"), ("2027-03-07", 15), old=("V078",), cta='vor',
  ziel="Das stärkste Shoot-Bild als Loop.", dauer="6–8 s",
  hook=("The first real photo of Time Travel.", "Das erste echte Foto von Time Travel."),
  alt=["This is it."],
  beats=[["0–6 s", "Langsamer Zoom in das beste Shoot-Foto", "The first real photo.", "Beat"], ["6–8 s", "Endkarte", "", ""]],
  dreh=["Aus der Auswahl vom So 07.03."], ort="—", req="—", schnitt=["8 s."], cover="Das Foto",
  cap="The first real photo of Time Travel.", de="Das erste echte Foto.", kom="Main image?", story="Link-Sticker ?ref=st-v251.", tags="#photography")

V("V252", "DETAIL", "Kampagnenfilm", ("2027-03-12", "18:00"), ("2027-03-11", 60), old=("V079",), cta='vor',
  ziel="Der 30-s-Kampagnenfilm (Schnitt am Do 11.03.).", dauer="30 s",
  hook=("Thirty seconds. Four embroideries, one patch.", "Dreißig Sekunden. Vier Stickereien, ein Patch."),
  alt=["Time Travel, the film."],
  beats=[["0–5 s", "Totale im Raum mit Teppich", "", "Musik"], ["5–20 s", "Details A, E, B2, C, D", "", ""], ["20–27 s", "Goldene Stunde, Gehen, Fäden", "", ""], ["27–30 s", "Endkarte", "24.06.2027", ""]],
  dreh=["Aus dem Shoot-Material."], ort="—", req="—", schnitt=["Siehe Aufgabe „Kampagnenfilm schneiden“."], cover="Shoot-Bild",
  cap="Time Travel. 100 numbered jeans. 24.06.2027.", de="Der Kampagnenfilm.", kom="🧵", story="Link-Sticker ?ref=st-v252.", tags="#campaign #denim",
  ton="Musik nur aus der Commercial Music Library oder lizenzfrei mit Nachweis.")

S("S13", "Welches ist das Hauptbild?", ("2027-03-13", "12:00"), old=("V080",),
  ziel="Zielgruppe wählt das Hauptbild der Produktseite.",
  frames=[["Zwei Shoot-Fotos", "Welches wird das Hauptbild?", "Umfrage: Links · Rechts"]],
  folge="Gewinner ist ab Di 16.03. das erste Bild der Produktseite.")

V("V253", "BUILD", "Das ist Time Travel", ("2027-03-15", "18:00"), ("2027-03-14", 30), old=("V081", "W25-BUILD"), cta='vor',
  ziel="Zusammenfassung vor der Abi-Pause: alles in einem Video.", dauer="25–30 s",
  hook=("This is Time Travel. All of it.", "Das ist Time Travel. Alles."),
  alt=["Five months in 30 seconds."],
  beats=[["0–5 s", "Papiertest Oktober", "October", ""], ["5–10 s", "Proto Dezember", "December", ""], ["10–15 s", "PP Januar", "January", ""],
         ["15–20 s", "Vorbestellung Februar", "February", ""], ["20–26 s", "Shoot März", "March", ""], ["26–30 s", "Endkarte", "24.06.2027", ""]],
  dreh=["Archiv."], ort="—", req="—", schnitt=["30 s, Schnitt auf Takt."], cover="Shoot-Bild",
  cap="From paper in October to the shoot in March. Now I write my exams; the factory makes the 100 pairs. See you in May.",
  de="Von Papier bis zum Shoot. Bis Mai.", kom="See you in May. 🧵", story="Link-Sticker ?ref=st-v253.", tags="#buildinpublic #journey")

V("V254", "REACH", "Nummer vergeben", ("2027-03-17", "19:00"), ("2027-03-14", 15), old=("V083",), cta='vor',
  ziel="Knappheit kurz.", dauer="6–8 s",
  hook=("Pair [0XX] already has an owner.", "Paar [0XX] hat schon einen Besitzer."),
  alt=["Taken."],
  beats=[["0–4 s", "Innenetikett mit vergebener Nummer, Stempel „taken“ (Animation)", "[0XX] · taken", "Beat"], ["4–8 s", "Endkarte", "[Y] left", ""]],
  dreh=["Etikett-Ausdruck."], ort="Tisch", req="—", schnitt=["8 s."], cover="„taken“",
  cap="Pair [0XX] already has an owner.", de="Paar [0XX] ist vergeben.", kom="Which number is still free? Ask me.", story="Link-Sticker ?ref=st-v254.", tags="#limitededition")

V("V255", "DETAIL", "Fäden nicht abschneiden", ("2027-03-19", "18:00"), ("2027-03-14", 20), old=("V084",), cta='vor',
  ziel="Pflege und Humor, speicherbar.", dauer="10–12 s",
  hook=("The care label says: don't cut the threads.", "Auf dem Pflegeetikett steht: Fäden nicht abschneiden."),
  alt=["Rule one."],
  beats=[["0–3 s", "Schere nähert sich den Goldfäden", "", "Spannung"], ["3–6 s", "Schnitt aufs Pflegeetikett", "DON'T CUT THE THREADS", "Schlag"], ["6–11 s", "Fäden schwingen", "", ""]],
  dreh=["Schere nur nah dran, nie schneiden."], ort="Tisch", req="PP, Schere", schnitt=["12 s."], cover="Schere und Fäden",
  cap="Rule one of Time Travel: don't cut the threads.", de="Regel eins: Fäden nicht abschneiden.", kom="😅", story="Link-Sticker ?ref=st-v255.", tags="#care #denim")

S("S14", "Welches Paket?", ("2027-03-20", "12:00"), old=("V085",),
  ziel="Verpackung mit der Community abstimmen.",
  frames=[["Zwei Verpackungsvarianten", "In welchem Paket soll dein Paar ankommen?", "Umfrage: A · B"]],
  folge="Ergebnis vor der Bestellung der Verpackung nur, wenn noch nicht bestellt (09.03.). Sonst als Bestätigung nutzen.")

# Autopilot W28–W34: vorproduziert in W27, eingeplant für Do 18:00
V("V256", "ORIGIN", "Rot und Weiß", ("2027-03-25", "18:00"), ("2027-03-16", 30), old=("V082",), cta='vor', pm=0,
  ziel="Autopilot 1/7 (Abi-Pause). Evergreen: warum Weiß neben Rot sitzt.", dauer="15–18 s",
  hook=("Why white sits next to red on my denim.", "Warum Weiß neben Rot sitzt."),
  alt=["Red alone disappears on indigo."],
  beats=[["0–4 s", "Makro: nur Rot auf Indigo (Stickprobe)", "red alone", "Stimme liest den Hook"],
         ["4–10 s", "Makro Band A, Rot mit Weiß", "red + white", "Stimme: „Red alone disappears on dark denim from two metres. White makes it readable.“"],
         ["10–15 s", "Totale aus 3 m", "readable from 3 m", ""]],
  dreh=["Stickprobe und PP."], ort="Fenster", req="Stickprobe, PP", schnitt=["Vorlage DETAIL."], cover="Rot/Weiß",
  cap="Red alone disappears on dark indigo from two metres. White next to it makes the pattern readable. That's the rule for every embroidery on these jeans.",
  de="Rot allein verschwindet auf Indigo.", kom="Save for later.", story="Link-Sticker ?ref=st-v256.", tags="#design #denim",
  posten=["Vorproduziert in W27. In Instagram (Meta Business Suite) und TikTok (Planen im Web) auf Do 25.03., 18:00 einplanen.",
          "Ersten Kommentar beim Einplanen mit eingeben, falls möglich, sonst weglassen.",
          "Während der Abi-Pause nicht reinschauen müssen: Kommentare beantwortest du am So in 10 Minuten."])

V("V257", "ORIGIN", "Zickzack", ("2027-04-08", "18:00"), ("2027-03-16", 25), old=("V015", "V109"), cta='vor', pm=0,
  ziel="Autopilot 3/7. Evergreen zum Zickzack am Band.", dauer="12–15 s",
  hook=("This zigzag runs along my pocket.", "Dieser Zickzack läuft an meiner Tasche entlang."),
  alt=["One line, two colours."],
  beats=[["0–4 s", "Makro Zickzack in Band A", "zigzag", "Stimme liest den Hook"], ["4–12 s", "Fahrt entlang des Bands", "17 rows", ""], ["12–15 s", "Endkarte", "", ""]],
  dreh=["Makro, Streiflicht."], ort="Fenster", req="PP", schnitt=["Vorlage DETAIL."], cover="Zickzack",
  cap="The zigzag runs along the pocket edge, 17 rows of red and white cross-stitch.", de="Der Zickzack am Band.",
  kom="🧵", story="Link-Sticker ?ref=st-v257.", tags="#embroidery", check="Bedeutung („Wasser“) nur mit Beleg.",
  posten=["Vorproduziert in W27, eingeplant auf Do 08.04., 18:00.", "Kommentare am So beantworten."])

V("V258", "ORIGIN", "Der Lebensbaum", ("2027-04-22", "18:00"), ("2027-03-16", 25), old=("V014", "V112"), cta='vor', pm=0,
  ziel="Autopilot 5/7. Evergreen zum Patch D.", dauer="12–15 s",
  hook=("Roots, trunk, crown: the patch on my waistband.", "Wurzeln, Stamm, Krone: der Patch am Bund."),
  alt=["A tree where the label usually is."],
  beats=[["0–4 s", "Makro Patch D", "roots · trunk · crown", "Stimme liest den Hook"], ["4–12 s", "Gürtel läuft durch", "the belt loop", ""], ["12–15 s", "Endkarte", "", ""]],
  dreh=["Makro, Tageslicht."], ort="Tisch", req="PP", schnitt=["Vorlage DETAIL."], cover="Patch",
  cap="Where a leather label usually sits: a tree of life on linen. It's also the back belt loop.", de="Der Lebensbaum am Bund.",
  kom="🌳", story="Link-Sticker ?ref=st-v258.", tags="#design #denim", check="Lebensbaum nie „slawisch“.",
  posten=["Vorproduziert in W27, eingeplant auf Do 22.04., 18:00.", "Kommentare am So beantworten."])

V("V259", "REAL", "Ehrlich: Prüfungen", ("2027-05-06", "18:00"), ("2027-03-17", 20), old=("V116",), cta='vor', pm=0,
  ziel="Autopilot 7/7. Der ehrliche Post: warum es gerade ruhig ist.", dauer="12–15 s",
  hook=("Why it's quiet here: I'm writing my final exams.", "Warum es ruhig ist: Ich schreibe gerade Abi."),
  alt=["The factory works, I study."],
  beats=[["0–4 s", "Schreibtisch mit Lernzetteln (keine Schule erkennbar)", "exams", "Stimme liest den Hook"], ["4–11 s", "Proto am Stuhl", "the factory is making your pairs", "Stimme"], ["11–15 s", "Endkarte", "back on 10.05.", ""]],
  dreh=["Vorher gedreht am Mi 17.03."], ort="Schreibtisch", req="—", schnitt=["15 s."], cover="Schreibtisch",
  cap="Why it's quiet here: I'm writing my final exams, the factory is making the 100 pairs. Back on 10.05.", de="Ich schreibe Abi, die Fabrik näht.",
  kom="Wish me luck. 🍀", story="Link-Sticker ?ref=st-v259.", tags="#student #smallbusiness", check="Keine Schule, kein Ort nennen.",
  posten=["Vorproduziert in W27, eingeplant auf Do 06.05., 18:00.", "Kommentare am So beantworten."])

# Grind+ W22–W27
V("V287", "BUILD", "Mein Fehler: Deadline verpasst", ("2027-02-18", "18:00"), ("2027-02-14", 15), old=("V114",), plus=True, pm=10, cta='vor',
  ziel="Optional: Ehrlichkeit über eine verpasste Frist.", dauer="12–15 s",
  hook=("I missed my own deadline. Here's what it cost.", "Meine eigene Frist verpasst."), alt=["Honest update."],
  beats=[["0–4 s", "Kalender mit durchgestrichenem Datum", "missed", "Stimme liest den Hook"], ["4–12 s", "Neues Datum", "what it cost", "Stimme"], ["12–15 s", "Endkarte", "", ""]],
  dreh=["Kalender."], ort="Tisch", req="—", schnitt=["15 s."], cover="Kalender",
  cap="I missed one of my own deadlines. Here's what it cost and what I changed.", de="Frist verpasst, ehrlich.", kom="Ever happened to you?", story="Optional.",
  tags="#buildinpublic", check="Nur eine echte verpasste Frist.")

V("V288", "DETAIL", "Stickmaschine ASMR", ("2027-03-04", "18:00"), None, old=("V118",), plus=True, pm=10, cta='vor',
  ziel="Optional: Clip der Fabrik, nur mit Erlaubnis.", dauer="10–15 s",
  hook=("Turn the sound on. This is 1,000 stitches.", "Ton an. Das sind 1.000 Stiche."), alt=["ASMR."],
  beats=[["0–15 s", "Stickmaschine stickt Band A (Fabrik-Clip)", "1,000 stitches", "Originalton"]],
  dreh=["Clip von der Fabrik anfragen."], ort="—", req="—", schnitt=["15 s, kein Text außer Hook."], cover="Maschine",
  cap="Sound on. One thousand stitches of the cross-stitch band.", de="Ton an.", kom="🔊", story="Optional.", tags="#asmr #embroidery",
  check="Nur mit schriftlicher Erlaubnis der Fabrik, keine Gesichter.")

V("V289", "ORIGIN", "Karussell Lebensbaum", ("2027-03-18", "18:00"), ("2027-03-14", 20), old=(), plus=True, pm=10, cta='vor',
  plattform="Instagram-Karussell", kind='karussell',
  ziel="Optional: Karussell zum Patch.", dauer="5 Bilder",
  hook=("Roots, trunk, crown. Save this.", "Wurzeln, Stamm, Krone."), alt=[],
  beats=[["Bild 1", "Patch", "the tree", ""], ["Bild 2", "Knotenfelder nah", "knot fields", ""], ["Bild 3", "Druckknöpfe", "4 hidden snaps", ""], ["Bild 4", "Gürtel", "belt loop", ""], ["Bild 5", "Endkarte", "", ""]],
  dreh=["Fotos 4:5."], ort="Tisch", req="PP", schnitt=["1080 × 1350."], cover="Bild 1",
  cap="The tree of life patch: linen, knot fields, four hidden snaps, and it's the back belt loop.", de="Der Patch im Detail.",
  kom="Save.", story="Optional.", tags="#design", check="Lebensbaum nie „slawisch“.")
