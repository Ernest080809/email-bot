# -*- coding: utf-8 -*-
"""Content W35–W41 (10.05.–27.06.2027): Neustart nach dem Abi, Countdown, Drop."""
from clib import V, S, LICHT_ABEND

V("V260", "BUILD", "Fast fertig", ("2027-05-10", "18:00"), ("2027-05-09", 25), old=("V086",), cta='vor',
  ziel="Neustart nach sieben Wochen Pause: Fotos aus der Produktion, die Liste wieder wecken.", dauer="18–22 s",
  hook=("Seven weeks of exams. Meanwhile, this happened.", "Sieben Wochen Abi. In der Zeit ist das passiert."),
  alt=["Day 211: first photos from the production line.", "I'm back. So are the jeans."],
  beats=[["0–3 s", "Du in die Kamera, Lernzettel werden weggeschoben", "I'm back.", "Stimme liest den Hook"],
         ["3–14 s", "Fabrik-Fotos der fertigen Jeans: Stapel, Etiketten, Patches (nur freigegebene Fotos)", "100 pairs, almost done", "Stimme: „The factory finished while I wrote my exams.“"],
         ["14–19 s", "Kalender: 14.05. fertig, 24.06. Drop", "ready 14.05. · drop 24.06.", ""],
         ["19–22 s", "Endkarte", "pre-order €149 ends Sun 23.05., 20:00", ""]],
  dreh=["Selfie Augenhöhe, Fenster vor dir, 3 Takes.", "Fabrik-Fotos aus der Mail vom Mo 10.05., nur mit Freigabe, keine Gesichter."],
  ort="Schreibtisch", req="Lernzettel, Fabrik-Fotos, Kalender",
  schnitt=["Vorlage BUILD.", "Fotos mit leichtem Zoom.", "Untertitel Englisch."], cover="Stapel fertiger Jeans, Text „Almost done“",
  cap="Seven weeks of exams. Meanwhile the factory made the 100 pairs. Ready by 14.05., drop on 24.06. The €149 pre-order price ends Sun 23.05., 20:00.",
  de="Zurück. Die Jeans sind fast fertig.", kom="Missed me? 😄", story="Link-Sticker ?ref=st-v260.", tags="#buildinpublic #denim",
  check="Keine Gesichter von Arbeitern, kein Fabrikname.")

V("V261", "ORIGIN", "Für alle Neuen", ("2027-05-11", "18:00"), ("2027-05-09", 40), old=("V087",), cta='vor',
  plattform="Instagram-Karussell (anheften), TikTok Photo Mode", kind='karussell',
  ziel="Das angeheftete Erklär-Karussell für alle, die erst jetzt kommen.", dauer="8 Bilder",
  hook=("New here? 100 jeans, 4 embroideries, 1 patch, 24.06.", "Neu hier? 100 Jeans, 4 Stickereien, 1 Patch, 24.06."),
  alt=["Everything about Time Travel in 8 slides."],
  beats=[["Bild 1", "Shoot-Hauptbild", "New here? Start here.", ""], ["Bild 2", "Rückansicht", "100 numbered jeans", ""],
         ["Bild 3", "Band A + E", "right: the pattern", ""], ["Bild 4", "B2 mit Fäden", "left: the harvest", ""],
         ["Bild 5", "Patch D mit Gürtel", "the belt loop", ""], ["Bild 6", "Größen", "W30–W38 · label = real waist", ""],
         ["Bild 7", "Zipper", "zip hoodie: carpet front", ""], ["Bild 8", "Termine", "€149 until 23.05. · drop 24.06., 19:00", ""]],
  dreh=["Fotos aus Shoot und Mini-Shoots, 4:5."], ort="—", req="Fotos",
  schnitt=["Canva oder CapCut, 1080 × 1350, Schrift aus dem Content-Look.", "Nach dem Posten im Profil anheften (drei Punkte → Anheften)."], cover="Bild 1",
  cap="New here? Time Travel is 100 numbered jeans with four embroideries and a tree-of-life patch, plus a zip hoodie with a carpet on the front. Pre-order at €149 until Sun 23.05., 20:00. Drop 24.06., 19:00.",
  de="Neu hier? Alles in 8 Bildern.", kom="Questions? Ask here.", story="Link-Sticker ?ref=st-v261.", tags="#denim #embroidery #drop")

V("V262", "REACH", "So kommt dein Paar an", ("2027-05-12", "19:00"), ("2027-05-09", 25), old=("V088",), cta='vor',
  ziel="Unboxing-Vorfreude, Vertrauen in die Lieferung.", dauer="12–15 s",
  hook=("How your pair will arrive.", "So kommt dein Paar an."),
  alt=["Packing test."],
  beats=[["0–3 s", "Karton mit Stempel", "how it arrives", "Beat"], ["3–10 s", "Probepaket öffnen: Seidenpapier, Karte, Jeans gedrittelt, Patch mit Seidenpapier", "", ""], ["10–14 s", "Dankeskarte nah", "", ""]],
  dreh=["Probepaket vom Mi 17.03., Ich-Perspektive."], ort="Tisch", req="Probepaket", ton="Titel aus der Commercial Music Library.",
  schnitt=["Vorlage DETAIL.", "14 s."], cover="Karton",
  cap="How your pair arrives: stamped box, tissue, the card, the jeans folded in three, the patch wrapped so the snaps leave no marks.",
  de="So kommt dein Paar an.", kom="Keep the box?", story="Link-Sticker ?ref=st-v262.", tags="#unboxing #packaging")

V("V263", "DETAIL", "Gold im Licht", ("2027-05-14", "18:00"), ("2027-05-09", 30), old=("V089",), cta='vor',
  ziel="Ästhetischer Detailpost, goldene Stunde.", dauer="10–12 s",
  hook=("Gold thread at golden hour.", "Goldfaden zur goldenen Stunde."),
  alt=["Watch the threads."],
  beats=[["0–3 s", "Gegenlicht, Fäden leuchten", "golden hour", "Beat"], ["3–9 s", "Gehen, Zeitlupe", "", ""], ["9–12 s", "Endkarte", "", ""]],
  dreh=["Abends 30 Min. vor Sonnenuntergang, Gegenlicht, 60 fps."], ort="Hof oder Straße ohne Menschen", req="PP",
  licht="Gegenlicht kurz vor Sonnenuntergang.", schnitt=["Zeitlupe 50 %.", "12 s."], cover="Fäden im Licht",
  cap="Gold thread at golden hour.", de="Goldfaden zur goldenen Stunde.", kom="✨", story="Link-Sticker ?ref=st-v263.", tags="#goldenhour #detail",
  check="Kein Weizenfeld unter blauem Himmel.")

S("S15", "Letzte Woche 149 €", ("2027-05-15", "12:00"), old=("V090",),
  ziel="Dringlichkeit vor dem Ende des Vorbestellpreises, Mess-Abend 3 heute.",
  frames=[["Foto: PP", "149 € endet So 23.05., 20:00.", "Countdown-Sticker auf So 23.05., 20:00"],
          ["Foto: Ort Mess-Abend", "Heute 18:00–20:00: Mess-Abend 3. Probier deine Größe.", "Link-Sticker"]],
  folge="Countdown-Erinnerungen zählen.")

V("V264", "BUILD", "Noch bis Sonntag", ("2027-05-17", "18:00"), ("2027-05-16", 20), old=("V091", "W27-BUILD"), cta='vor',
  ziel="Letzte Woche Vorbestellpreis.", dauer="12–15 s",
  hook=("Six days left at €149.", "Noch sechs Tage zu 149 €."),
  alt=["Last week."],
  beats=[["0–3 s", "Kalender, 23.05. eingekreist", "6 days", "Stimme liest den Hook"], ["3–11 s", "Proto/PP, Innenetikett", "then €169", "Stimme"], ["11–14 s", "Endkarte", "Sun 23.05., 20:00", ""]],
  dreh=["Kalender, PP."], ort="Tisch", req="Kalender", schnitt=["Vorlage BUILD."], cover="„6 days“",
  cap="Six days left at €149. Sunday 23.05., 20:00, it's €169.", de="Noch sechs Tage zu 149 €.", kom="⏰", story="Countdown-Sticker, Link ?ref=st-v264.", tags="#preorder")

V("V265", "ORIGIN", "Gold nur, wo etwas wächst", ("2027-05-18", "18:00"), ("2027-05-16", 25), old=("V092",), cta='vor',
  ziel="Design-Regel als Geschichte.", dauer="15–18 s",
  hook=("Gold only goes where something grows.", "Gold nur dort, wo etwas wächst."),
  alt=["My one rule for gold."],
  beats=[["0–4 s", "B2 Makro", "gold = growth", "Stimme liest den Hook"], ["4–12 s", "Ähren, Fäden, Patch-Baum", "ears · threads · tree", "Stimme: „Only the harvest and the tree get gold. Everything else is red and white.“"], ["12–15 s", "Endkarte", "", ""]],
  dreh=["Makros."], ort="Fenster", req="PP", schnitt=["Vorlage BUILD."], cover="Gold-Makro",
  cap="One rule: gold only goes where something grows. The ears, the threads, the tree. Everything else is red and white.", de="Gold nur, wo etwas wächst.",
  kom="Did you notice?", story="Link-Sticker ?ref=st-v265.", tags="#design #rules")

V("V266", "REACH", "Oktober Papier, Mai Garn", ("2027-05-19", "19:00"), ("2027-05-16", 20), old=("V093",), cta='vor',
  ziel="Match-Cut mit der fertigen Serienware.", dauer="6–8 s",
  hook=("October: paper. May: thread. Same pocket.", "Oktober Papier. Mai Garn."),
  alt=["7 months."],
  beats=[["0–3 s", "Papier-Clip aus dem Oktober", "October", ""], ["3–4 s", "Match-Cut auf Serienware", "May", "Schlag"], ["4–7 s", "Hand fährt weiter", "", ""]],
  dreh=["Gleicher Bildausschnitt wie V211."], ort="Fensterbank", req="Serienware oder PP", schnitt=["7 s."], cover="Split",
  cap="October: paper. May: thread.", de="Oktober Papier, Mai Garn.", kom="🧵", story="Link-Sticker ?ref=st-v266.", tags="#beforeandafter")

V("V267", "DETAIL", "Deine Nummer", ("2027-05-21", "18:00"), ("2027-05-16", 20), old=(), cta='vor',
  ziel="Innenetikett der Serie zeigen.", dauer="10–12 s",
  hook=("Every pair, its own number. Printed inside.", "Jedes Paar, seine Nummer."),
  alt=["001 to 100."],
  beats=[["0–3 s", "Bund umklappen, Etikett", "Nr. 0XX/100", "Stoff"], ["3–9 s", "Mehrere Etiketten nacheinander (Fabrik-Foto)", "001 · 002 · 003 …", ""], ["9–12 s", "Endkarte", "", ""]],
  dreh=["Fabrik-Fotos der Etiketten oder dein PP."], ort="Tisch", req="—", schnitt=["12 s."], cover="Etikett",
  cap="Every pair has its own number, printed on the inside label. Pre-orders got theirs by order date.", de="Jedes Paar hat seine Nummer.",
  kom="Which one is yours?", story="Link-Sticker ?ref=st-v267.", tags="#numbered #limitededition")

S("S16", "Letzter Tag 149 €", ("2027-05-22", "12:00"), old=("V095",),
  ziel="Letzte Erinnerung vor dem Preisende.",
  frames=[["Foto: PP", "Morgen 20:00 ist 149 € vorbei.", "Countdown-Sticker auf So 23.05., 20:00"]],
  folge="—")

V("V268", "BUILD", "Alles bezahlt", ("2027-05-24", "18:00"), ("2027-05-23", 20), old=("V096",), cta='stufe2',
  ziel="Restzahlung, Ware unterwegs.", dauer="12–15 s",
  hook=("Factory fully paid. The jeans are coming.", "Fabrik bezahlt. Die Jeans kommen."),
  alt=["Last payment."],
  beats=[["0–3 s", "Banking-App, Betrag unscharf", "paid", "Stimme liest den Hook"], ["3–10 s", "Tracking-Karte, Nummer geschwärzt", "on the way", ""], ["10–14 s", "Endkarte", "drop 24.06., 19:00", ""]],
  dreh=["Bildschirm."], ort="Mac", req="—", schnitt=["Vorlage BUILD."], cover="„Paid“",
  cap="Factory fully paid, the 100 pairs are on their way. Pre-order at €169 until Sun 06.06., delivery early June.", de="Alles bezahlt.",
  kom="🧵", story="Link-Sticker ?ref=st-v268.", tags="#buildinpublic", check="Keine Beträge, keine Trackingnummer.")

V("V269", "ORIGIN", "Warum Time Travel", ("2027-05-25", "18:00"), ("2027-05-23", 30), old=("V097",), cta='stufe2',
  ziel="Der Name erklärt, persönlich.", dauer="20–25 s",
  hook=("Why I called this drop Time Travel.", "Warum dieser Drop Time Travel heißt."),
  alt=["Old patterns, new denim."],
  beats=[["0–4 s", "Du in die Kamera", "why Time Travel?", "Stimme liest den Hook"], ["4–16 s", "Teppich-Foto, Stickerei-Detail, Jeans", "old patterns · new jeans", "Stimme: zwei Sätze, was der Name für dich heißt"], ["16–22 s", "Endkarte", "24.06., 19:00", ""]],
  dreh=["Selfie, Archiv."], ort="Schreibtisch", req="—", schnitt=["Vorlage BUILD."], cover="Du",
  cap="Why Time Travel: patterns that hung on walls and tablecloths for generations, on jeans you wear today.", de="Warum Time Travel.",
  kom="What does the name mean to you?", story="Link-Sticker ?ref=st-v269.", tags="#story #brand",
  check="Keine Länder, keine Volksgruppen, das Muster ist das Subjekt.")

V("V270", "REACH", "Packstation", ("2027-05-26", "19:00"), ("2027-05-25", 30), old=("V098",), cta='stufe2',
  ziel="Zeitraffer der Packstation, Vorfreude.", dauer="8–10 s",
  hook=("My living room is now a packing station.", "Mein Wohnzimmer ist jetzt eine Packstation."),
  alt=["Ready."],
  beats=[["0–8 s", "Zeitraffer: Tisch, Kartons, Seidenpapier, Etiketten", "packing station", "Titel"], ["8–10 s", "Endkarte", "", ""]],
  dreh=["Zeitraffer beim Aufbau am Di 25.05. (Aufgabe Lager und Packstation)."], ort="Wohnzimmer", req="—", schnitt=["10 s."], cover="Packstation",
  cap="My living room is now a packing station.", de="Packstation steht.", kom="📦", story="Link-Sticker ?ref=st-v270.", tags="#smallbusiness #packing")

V("V271", "DETAIL", "Vier Stickereien, ein Patch", ("2027-05-28", "18:00"), ("2027-05-23", 25), old=("V099",), cta='stufe2',
  ziel="Alle Elemente in einer Sekunde je Element.", dauer="7–9 s",
  hook=("Four embroideries, one patch. One second each.", "Vier Stickereien, ein Patch. Je eine Sekunde."),
  alt=["All of it."],
  beats=[["0–1 s", "A", "A", "Schlag"], ["1–2 s", "E", "E", "Schlag"], ["2–3 s", "B2", "B2", "Schlag"], ["3–4 s", "C", "C", "Schlag"], ["4–5 s", "D", "D", "Schlag"], ["5–7 s", "Gehen, Fäden", "", ""], ["7–8 s", "Endkarte", "", ""]],
  dreh=["Makros aus dem Archiv, gleiche Größe im Bild."], ort="—", req="—", ton="Titel mit 5 Schlägen.", schnitt=["Schnitt auf jeden Schlag.", "8 s."], cover="Collage",
  cap="Four embroideries and a patch, one second each.", de="Alles in acht Sekunden.", kom="Favourite?", story="Link-Sticker ?ref=st-v271.", tags="#detail")

S("S17", "Welche Größe?", ("2027-05-29", "12:00"), old=("V100",),
  ziel="Größenfragen vor dem Drop klären.",
  frames=[["Foto: Größentabelle", "Unsicher bei der Größe? Frag mich.", "Frage-Sticker"]],
  folge="Jede Frage persönlich beantworten, häufige in die FAQ.")

V("V290", "BUILD", "Eine Stunde am Tag", ("2027-05-27", "18:00"), ("2027-05-23", 15), old=("V116",), plus=True, pm=10, cta='stufe2',
  ziel="Optional: Gründer-Alltag.", dauer="12–15 s",
  hook=("I built this drop in one hour a day.", "Diesen Drop habe ich in einer Stunde am Tag gebaut."),
  alt=["Next to school."],
  beats=[["0–4 s", "Uhr, Docket am Handy", "1 hour a day", "Stimme liest den Hook"], ["4–12 s", "Schnelle Folge aus 9 Monaten", "", ""], ["12–15 s", "Endkarte", "", ""]],
  dreh=["Archiv."], ort="—", req="—", schnitt=["15 s."], cover="Uhr",
  cap="Nine months, about one hour a day, next to school and exams.", de="Eine Stunde am Tag.", kom="How much time do you have for your side project?", story="Optional.",
  tags="#buildinpublic #student")

FELD = dict(ort="Feld am Stadtrand (gefunden am Di 02.02.), immer derselbe Punkt, Markierung an einem Pfosten",
            req="Stativ, Markierung (Klebeband am Pfosten), PP oder Serienpaar")
for i, (d, m) in enumerate([("2027-05-30", 90), ("2027-06-06", 90), ("2027-06-13", 90), ("2027-06-20", 90)], 1):
    V(f"FELD{i}", "REACH", f"Das Feld wächst {i}/4", (d, "20:30"), (d, m), old=({1: "Reserve · Das Feld wächst 1", 2: "Feld-Dreh 2", 3: "Feld-Dreh 3", 4: "Das Feld wächst · Dreh 4"}[i],),
      plus=True, pm=10, cta='stufe2' if i == 1 else 'drop',
      ziel="Optional: Serie am selben Feld bis zum Drop. Zeigt Zeit vergehen.", dauer="8–12 s",
      hook=(f"Same field. Same spot. Week {i}.", f"Gleiches Feld, gleicher Punkt. Woche {i}."),
      alt=["Watch it grow until 24.06."],
      beats=[["0–3 s", "Totale vom markierten Punkt", f"week {i}", "Wind"], ["3–9 s", "Du gehst ins Bild, Rückansicht, Fäden", "", ""], ["9–11 s", "Endkarte", "24.06.", ""]],
      dreh=["Stativ genau auf der Markierung, gleiche Höhe (Klebeband am Stativbein), gleiche Uhrzeit 30 Min. vor Sonnenuntergang.",
            "1 Totale 10 s ohne dich, 1 Take mit dir." + (" Dazu Zeitraffer der vier Wochen nebeneinander." if i == 4 else "")],
      licht="30 Minuten vor Sonnenuntergang, Sonne seitlich, nie Weizen unter blauem Himmel im Bild.",
      schnitt=["Gleicher Schnitt wie Woche 1, nur Text ändert sich.", "11 s."], cover="Feld",
      cap=f"Same field, same spot, week {i}.", de=f"Das Feld wächst, Woche {i}.", kom="🌾", story="Optional.", tags="#timelapse", **FELD,
      check="Nur bei Sonnenuntergang, Himmel nicht blau im Bild, keine Sichel, keine Ähren in der Hand.")

# Countdown
CD = {
 24: ("24 days. 100 numbered jeans.", "Ganzkörper vorn aus dem Shoot, langsamer Zoom auf die rechte Vordertasche", "T−24 · 24.06. · 19:00", "T−24. The countdown starts. 100 numbered pairs."),
 23: ("23 days. They're here.", "Kartons im Flur, Hand öffnet den ersten, erster Griff: gefaltete Jeans, Band A sichtbar (live gedreht)", "T−23 · They're here.", "T−23. They're here. Every pair gets checked this week."),
 22: ("22 days. The smallest pocket, fully stitched.", "Makro Münztasche E, Lineal daneben", "T−22 · 62 × 62 mm", "T−22. The coin pocket: 62 by 62 mm, 45 by 45 squares."),
 21: ("21 days. Three ears, nine threads.", "Makro linke Gesäßtasche, Fäden hängen still", "T−21", "T−21. The harvest sits on the left: three ears, nine gold threads."),
 20: ("20 days. The only part that moves.", "Fäden schwingen beim Gehen, Gegenlicht", "T−20", "T−20. Nine threads, set by hand after the wash."),
 19: ("19 days. One star, eight diamonds.", "Kamera fährt an die rechte Gesäßtasche, Achtstern C", "T−19 · Story: pre-order ends tomorrow 20:00", "T−19. The eight-point star: eight diamonds, 1 mm apart."),
 18: ("18 days. A tree where the label usually is.", "Zoom auf den Lebensbaum-Patch, Gürtel läuft durch", "T−18 · Story: pre-order ends tonight 20:00", "T−18. Tree of life on linen, 80 by 71 mm, and it's the belt loop. Pre-order ends tonight, 20:00."),
 17: ("17 days. One drop.", "Gruppenbild aus dem Shoot: Jeans, Zipper (Polo, falls im Drop)", "T−17", "T−17. Jeans and zip hoodie, one drop."),
 16: ("16 days. A wall carpet, on the front.", "Zipper vorn, Schwenk über den Teppich, Reißverschluss geht zu", "T−16", "T−16. A small wall carpet on the front of the zip hoodie."),
 15: ("15 days. Pre-orders shipping.", "Packtisch-Zeitraffer, Karton zu, Stempel", "T−15", "T−15. Pre-orders are shipping."),
 14: ("Two weeks. Number 001 has shipped.", "Innenetikett „Nr. 001/100“ in der Hand, dann Karton zu", "T−14 · 2 weeks", "T−14. Two weeks. Number 001 is on its way."),
 13: ("13 days. How this shoot was made.", "BTS vom Shoot, 0,5 s je Clip", "T−13", "T−13. One Saturday, one sunset."),
 12: ("12 days. Nine threads, nine lengths.", "Finger fährt an den Goldfäden entlang", "T−12", "T−12. 19, 25, 22, 30, 27, 21, 29, 18, 24 mm."),
 11: ("11 days. The line around the band.", "Makro Zickzack am Band A", "T−11", "T−11. The zigzag frames the band. Or: photos from pre-order customers (only with their OK)."),
 10: ("10 days. From the wall to the zipper.", "Familienteppich 1 s, harter Schnitt auf das Medaillon am Zipper", "T−10", "T−10. The carpet, remembered. Its medallion now sits on the zip hoodie."),
 9: ("9 days. Turn it inside out.", "Jeans auf links, Makro der Rückseite der Stickerei", "T−9 · Clean on both sides.", "T−9. Clean on both sides."),
 8: ("8 days. Watch the back.", "Gehen, Rückansicht aus dem Shoot, Fäden schwingen", "T−8", "T−8. Watch the back. The threads move when you walk."),
 7: ("One week. 24.06., 19:00.", "Ganzkörper hinten aus dem Shoot", "T−7 · 1 week", "T−7. One week."),
 6: ("From three metres: dots. From thirty centimetres: clockwork.", "Fahrt aus 3 m auf Band A und E (V203/V207, jetzt mit Serienware)", "T−6", "T−6. From three metres: dots. From thirty centimetres: clockwork."),
 5: ("5 days. Rule one: don't cut the threads.", "Makro Pflegeetikett „Goldfäden nicht abschneiden“", "T−5 · wash inside out", "T−5. Rule one: don't cut the threads. Wash inside out."),
 4: ("4 days. Hands in pockets.", "Hand gleitet in die rechte Vordertasche, Band A im Fokus", "T−4", "T−4. The band sits on the pocket edge."),
 3: ("3 days. This was paper in October.", "Papiertest-Clip 1,5 s, harter Schnitt auf die Serienware, gleiche Einstellung", "T−3 · October → June", "T−3. October: paper on my jeans. June: this."),
 2: ("2 days. Four embroideries and a patch.", "A, E, C, D, B2, Goldfäden, je 1 s", "T−2", "T−2. Band, coin pocket, star, tree, harvest, gold threads."),
 1: ("Tomorrow, 19:00. The list gets in at 18:00.", "Kampagnenfilm auf 10 s gekürzt", "T−1 · tomorrow 19:00", "T−1. Tomorrow."),
}
import datetime as _dt
_start = _dt.date(2027, 5, 31)
for n in range(24, 0, -1):
    d = (_start + _dt.timedelta(days=24 - n)).isoformat()
    hook, bild, txt, cap = CD[n]
    film = ("2027-05-20", 0) if n >= 13 else ("2027-05-22", 0)
    if n in (23, 15, 14):
        film = None
    cta = 'stufe2' if n >= 18 else 'drop'
    V(f"CD-T{n:02d}", "COUNTDOWN", f"T−{n}", (d, "18:00"), film, old=(f"CD-T{n:02d}",) + (("V125",) if n == 6 else ()), pm=10, cta=cta,
      ziel=f"Countdown Tag {n}: jeden Tag zur gleichen Zeit, gleiche Form, ein Detail. Wiedererkennung und tägliche Erinnerung.",
      dauer="6–9 s",
      hook=(hook, f"Noch {n} Tage." if n > 1 else "Morgen, 19 Uhr. Die Liste um 18 Uhr."),
      alt=[f"T−{n}."],
      beats=[["0–1 s", "Zahl groß auf Schwarz", f"T−{n}", "Schlag"],
             ["1–7 s", bild, txt, "Titel aus der Countdown-Reihe, immer derselbe"],
             ["7–8 s", "Endkarte", "24.06. · 19:00", ""]],
      dreh=["Aus dem Shoot (06.03.), den Mini-Shoots und der Serienware. Neu gedreht nur, wo die Bildspalte „live“ sagt." if film else "Live am Tag gedreht, Bildausschnitt wie die anderen Countdown-Clips.",
            "Alle 24 Clips haben dasselbe Format: 1 s Zahl, 6 s Bild, 1 s Endkarte, gleicher Titel, gleiche Schrift."],
      ort="Archiv oder live", req="Countdown-Vorlage in CapCut",
      ton="Ein Titel aus der Commercial Music Library für die ganze Reihe, jeden Tag gleich.",
      schnitt=["CapCut-Vorlage „Countdown“: Zahl tauschen, Clip tauschen, Text tauschen, Export.", "Dateiname CD-T%02d.mp4, Caption in die Notiz daneben." % n],
      cover=f"Zahl „T−{n}“",
      cap=cap, de=f"Noch {n} Tage bis zum Drop." if n > 1 else "Morgen, 19 Uhr.",
      kom="⏰ 24.06., 19:00",
      story=f"Reel teilen, Countdown-Sticker auf 24.06., 19:00, Link-Sticker ?ref=st-cd{n:02d}.",
      tags="#countdown #denim",
      posten=["Vorproduziert (Countdown-Assets). Am Vortag in TikTok und Instagram auf 18:00 einplanen oder um 18:00 von Hand posten.",
              "Story mit Countdown-Sticker.", "5 Minuten Kommentare."],
      check="Nur echte Zahlen.")

V("V272", "DROP", "Die Liste kauft gerade", ("2027-06-24", "18:00"), None, old=("V101",), pm=35, cta='live',
  ziel="18:00: nur die Liste ist drin. Live, Stimmung, Restgrößen.", dauer="Live 30 Min.",
  plattform="Instagram Live + Story", kind='live',
  hook=("The list is shopping right now.", "Die Liste kauft gerade."),
  alt=["18:00. Only the list."],
  beats=[["18:00", "Live starten, du am Tisch mit dem Shop am Laptop", "the list is in", "Begrüßung, wer ist da"],
         ["18:05–18:25", "Größen erklären, Fragen beantworten, echte Zahl verkaufter Paare", "[X] sold", ""],
         ["18:25–18:30", "Hinweis: 19:00 für alle", "19:00: everyone", ""]],
  dreh=["Handy auf Stativ, Laptop daneben, Ladekabel, WLAN geprüft."], ort="Packstation", req="Laptop, Handy, Stativ",
  schnitt=["Live, kein Schnitt."], cover="—",
  cap="The list is shopping right now. 19:00: everyone.", de="Die Liste kauft gerade.", kom="—",
  story="Story 18:00: „Die Liste ist drin“ mit Link für die Liste. Kein öffentlicher Link vor 19:00.", tags="",
  check="Keine Ernte-Hooks heute. Nur echte Zahlen.")

V("V273", "DROP", "Live", ("2027-06-24", "19:00"), None, old=("V102",), pm=15, cta='live',
  ziel="19:00 öffentlich.", dauer="7–9 s",
  hook=("Time Travel is live.", "Time Travel ist live."), alt=["Now."],
  beats=[["0–3 s", "Gehen von hinten, Fäden", "LIVE", "Schlag"], ["3–7 s", "Makro Band A", "100 numbered jeans", ""], ["7–9 s", "Endkarte", "link in bio", ""]],
  dreh=["Vorproduziert."], ort="—", req="—", schnitt=["9 s."], cover="„LIVE“",
  cap="Time Travel is live. 100 numbered jeans. Link in bio.", de="Jetzt live.", kom="Link in bio. 🧵", story="Link-Sticker ?ref=st-live.", tags="#drop")

V("V274", "DROP", "Restbestand", ("2027-06-24", "20:00"), None, old=("V103",), pm=10, cta='live', kind='story',
  plattform="Story-Updates 19:15, 20:00, 22:00",
  ziel="Ehrliche Restgrößen, keine falsche Knappheit.", dauer="3 Story-Updates",
  hook=("[X] pairs left. Here are the sizes.", "Noch [X] Paar. Diese Größen."), alt=[],
  beats=[["19:15", "Foto Bestandsliste", "[X] left: W30 [a] · W32 [b] · …", ""], ["20:00", "Update", "", ""], ["22:00", "Update", "", ""]],
  dreh=["Screenshot aus Shopify, nur Zahlen."], ort="—", req="—", schnitt=["—"], cover="—",
  cap="—", de="—", kom="—", story="Drei Updates mit Link-Sticker.", tags="", check="Nur echte Zahlen.")

V("V275", "DROP", "Live vom Packtisch", ("2027-06-24", "21:00"), None, old=("V107",), pm=30, cta='live',
  plattform="Instagram Live", kind='live',
  ziel="Nach der ersten Welle: Nähe, Fragen, Restgrößen.", dauer="Live 30 Min.",
  hook=("Live from my packing table. Ask about sizes.", "Live vom Packtisch."), alt=[],
  beats=[["21:00", "Live am Packtisch, Helfer im Hintergrund (nur mit Einwilligung)", "", "Fragen beantworten"]],
  dreh=["Stativ am Packtisch."], ort="Packstation", req="—", schnitt=["Live."], cover="—",
  cap="Live from the packing table.", de="Live vom Packtisch.", kom="—", story="Hinweis 20:50.", tags="")

V("V276", "BUILD", "24 Stunden", ("2027-06-25", "18:00"), ("2027-06-25", 20), old=("V104",), pm=20, cta='live',
  ziel="Ehrlicher Stand nach 24 h.", dauer="12–15 s",
  hook=("24 hours: [X] of 100 found an owner.", "24 Stunden: [X] von 100 haben einen Besitzer."), alt=["Day 1 after the drop."],
  beats=[["0–3 s", "Packtisch, Stapel Pakete", "[X] / 100", "Stimme liest den Hook"], ["3–11 s", "Hände packen", "thank you", ""], ["11–14 s", "Endkarte", "[Y] left · link in bio", ""]],
  dreh=["Packtisch heute."], ort="Packstation", req="—", schnitt=["Vorlage BUILD."], cover="Pakete",
  cap="24 hours: [X] of 100 pairs found an owner. [Y] left, sizes in my story.", de="24 Stunden nach dem Drop.", kom="Thank you. 🙏",
  story="Link-Sticker ?ref=st-v276.", tags="#drop #smallbusiness", check="Nur echte Zahlen.")

S("S19", "Drop 2?", ("2027-06-26", "12:00"), old=("V105",),
  ziel="Nachfrage für den nächsten Drop messen.",
  frames=[["Foto: Serienware", "Was soll der nächste Drop sein?", "Frage-Sticker"], ["Foto", "Mehr Jeans · Zipper · Polo · etwas Neues", "Umfrage"]],
  folge="Antworten in die Liste „Drop 2“.")

V("V277", "REAL", "Was der Drop gebracht hat", ("2027-06-27", "18:00"), ("2027-06-27", 30), old=("V106",), pm=20, cta='live',
  ziel="Ehrliche Bilanz.", dauer="25–30 s",
  hook=("The real numbers of my first drop.", "Die echten Zahlen meines ersten Drops."), alt=["What went right, what didn't."],
  beats=[["0–3 s", "Du in die Kamera", "the real numbers", "Stimme liest den Hook"], ["3–20 s", "Papier: Liste, Vorbestellungen, Drop-Verkäufe, Retouren, was übrig ist", "", "Stimme"], ["20–27 s", "Was du anders machen würdest", "next time", ""], ["27–30 s", "Endkarte", "", ""]],
  dreh=["Papier mit Zahlen aus der Auswertung nach 72 h."], ort="Schreibtisch", req="Zahlen", schnitt=["Vorlage BUILD."], cover="Zahlen",
  cap="The real numbers of my first drop: what worked, what didn't, what I'd change.", de="Die echten Zahlen.", kom="Ask me anything.",
  story="Link-Sticker.", tags="#buildinpublic #results", check="Nur echte Zahlen, keine Umsätze, die du nicht zeigen willst.")

S("S18", "Q&A zum Drop", ("2027-06-19", "12:00"), old=("ASK-Q&A",),
  ziel="Letzte Fragen vor dem Drop.",
  frames=[["Foto", "Frag mich alles zum Drop am Do.", "Frage-Sticker"], ["Antworten als Clips", "", ""]],
  folge="Häufige Fragen in die FAQ.")

S("S25", "Bring 3: letzte Woche 149 €", ("2027-05-15", "13:00"), old=("Bring3-W26",), plus=True,
  ziel="Optional: Empfehlungen vor dem Preisende.",
  frames=[["Foto", "Bring 3 Leute, bevor 149 € endet.", "Link-Sticker ?ref=bring3"]], folge="—")
