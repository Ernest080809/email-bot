# -*- coding: utf-8 -*-
# Referenz-Abschnitte für Docket Rev. 5 (HTML)
import html, datetime as dt

def e(s):
    return html.escape(s, quote=False)

def copybox(pid, label, text):
    return ('<div class="prompt"><div class="ph"><span class="eyebrow">%s</span>'
            '<button type="button" data-copy="%s">Kopieren</button></div>'
            '<pre class="code" id="%s">%s</pre></div>' % (e(label), pid, pid, e(text.strip("\n"))))

def table(head, rows, caption=None, num=()):
    h = '<div class="tablewrap"><table><thead><tr>'
    for i, c in enumerate(head):
        h += '<th%s>%s</th>' % (' class="num"' if i in num else '', c)
    h += '</tr></thead><tbody>'
    for r in rows:
        cls = ''
        if isinstance(r, tuple) and len(r) == 2 and isinstance(r[1], str) and r[1] in ("total", "sub"):
            r, cls = r
        h += '<tr%s>' % (' class="%s"' % cls if cls else '')
        for i, c in enumerate(r):
            h += '<td%s>%s</td>' % (' class="num"' if i in num else '', c)
        h += '</tr>'
    h += '</tbody>'
    if caption:
        h += '<caption>%s</caption>' % caption
    return h + '</table></div>'

def ref(id_, title, inner, pill=None):
    p = ' <span class="pill ok" style="font-size:9.5px">%s</span>' % pill if pill else ''
    return ('<details class="ref" id="%s"><summary><span class="chev"></span>%s%s</summary>'
            '<div class="inner">%s</div></details>' % (id_, title, p, inner))

# ======================================================================
# 1 · Zeitachse
# ======================================================================
ZEIT = [
 ("Do 01.10.", "W3", "Papiertest 1 an der echten Hose, erledigt → Design v1.5"),
 ("Mi 07.10.", "W4", "Deine Skizze → Design v1.6, abends v1.7 mit großem Serp"),
 ("Do 08.10.", "W4", "Papiertest 3 mit v1.7"),
 ("Fr 09.10.", "W4", "<b>Design-Freeze</b> · Tech Pack bestellt"),
 ("So 11.10.", "W4", "Tech Pack v1.0 freigegeben"),
 ("Mo 12.10.", "W5", "Anfrage an 8 Fabriken · erster Post"),
 ("Mo 26.10.", "W7", "<b>Eine Fabrik gewählt</b>, Nummer 2 als Reserve"),
 ("So 01.11.", "W7", "<b>VALIDIERUNG</b>: grün ab 150 Anmeldungen, gelb 50–149, rot unter 50"),
 ("Mo 02.11.", "W8", "Entwicklung bezahlt (Digitizing, Stickproben, Proto)"),
 ("Di 17.11.", "W10", "Stickproben und Garnfarben freigegeben"),
 ("Do 03.12.", "W12", "<b>Das Proto ist da</b> · Sa 05.12. Fit-Test"),
 ("Mo 07.12.", "W13", "PP-Sample bestellt, Versand spätestens 04.01."),
 ("Do 17.12.", "W14", "Label-Patch D in Serie bestellt (an die Fabrik bis 22.01.)"),
 ("Mo 04.01.", "W17", "<b>PP-Sample prüfen und freigeben</b>"),
 ("Do 14.01., 19:00", "W18", "<b>Vorbestellung öffnet</b>: 35 Paar zu 149 €, Warteliste ab 18:00"),
 ("Mo 01.02.", "W21", "<b>SCHWELLE</b>: mindestens 10 Vorbestellungen bis So 31.01. → Bestellung, Anzahlung bis Do 04.02."),
 ("Fr 05.02.", "W21", "Spiel: bauen oder streichen"),
 ("Mo 08.02.", "W22", "Produktionsstart"),
 ("Sa 20.02.", "W23", "Lookbook-Shoot"),
 ("Mo 08.–Do 11.03.", "W26", "Ramadan-Fest (Ramazan Bayramı): Fabrik in der Türkei zu"),
 ("Fr 19.03.", "W27", "Endkontrolle und <b>Restzahlung</b> (mindestens 32 Vorbestellungen)"),
 ("So 21.03., 20:00", "W27", "Vorbestellpreis endet"),
 ("~Mo 22.03.", "W28", "Versand der Ware"),
 ("Fr 26.–Mo 29.03.", "W28–29", "Ostern: kein Zoll, keine Zustellung"),
 ("Mo 29.03.", "W29", "<b>Countdown T−24</b> startet"),
 ("~Di 30.03.", "W29", "Die Ware kommt an, Prüfung bis Sa 03.04."),
 ("Di 06.–Mi 07.04.", "W30", "Vorbestellungen verschickt (Nummern 001 ff.)"),
 ("Do 15.04.", "—", "Spätester Ankunftstermin der Ware für den Drop am 22.04."),
 ("Sa 17.04.", "W31", "Letzte Testbestellung · Code-Freeze (Spiel)"),
 ("Do 22.04., 18:00 / 19:00", "W32", "<b>DROP</b>: Warteliste ab 18:00, öffentlich ab 19:00"),
 ("So 25.04.", "W32", "Auswertung nach 72 Stunden · Blanks für Zipper und Polo bestellt"),
]
REF_ZEIT = ref("zeit", "Zeitachse · alle Termine auf einen Blick",
    '<p class="intro">Die festen Punkte des Plans. Alles andere hängt an ihnen. Verschiebt sich einer, schreib es Claude, dann wird der Rest neu geschnitten.</p>'
    + table(["Datum", "Woche", "Was"], [(a, '<span class="mono">%s</span>' % b, c) for a, b, c in ZEIT],
            "Fett sind die Punkte, an denen etwas entschieden oder bezahlt wird. Die Reihenfolge ist fest: Design fertig → Sample kaufen und prüfen → erst dann das Produkt zeigen und verkaufen."),
    "Neu Rev. 5")

# ======================================================================
# 2 · Vorlagen
# ======================================================================
RFQ = """Subject: RFQ – 100 embroidered jeans with panel embroidery (NVL-TT-01)

Hello [NAME / TEAM OF FACTORY],

I'm Ernest, founder of Novalife, a denim brand from Berlin. For our next drop I'm looking for one factory to produce 100 jeans with embroidery on the cut panels before assembly. Tech pack v1.0 and the 1:1 element sheet are attached.

Key facts:
- Style NVL-TT-01, straight leg, sizes W30–W38 (honest sizing), 100 pcs in total
- 12 oz rigid denim, 100 % cotton, 3/1 twill, mid-dark indigo (L* 34–40), vintage wash with laser finishing
- 5 embroidery elements (A–E) on 5 cut-panel zones, one motif (approx. 53 × 49 mm) 10 mm from the outseam, approx. 33,000 stitches per pair, fine cross-stitch look on a 1.33 mm grid, up to 10 polyester thread colours (white, light grey, red, four golds, straw, two browns)
- 1 embroidered label patch (86 × 76 mm) sewn onto the back waistband before washing. I supply the patches
- After washing: raw hem cut to final length, then 9 gold polyester threads (three-ply, approx. 1 mm, 18–30 mm long) set by hand and knotted inside the left back pocket
- Timeline: digitizing and washed stitch-outs in November 2026, proto (W32) shipped by 30 November 2026, PP sample shipped by 4 January 2027, bulk production February–March 2027, delivery DDP Berlin by the end of March 2027

Could you please answer these questions:
1. Do you embroider in-house or outsource it?
2. Do you embroider on cut panels before assembly? Maximum hoop/embroidery area in cm?
3. Price per 1,000 stitches at 100 / 150 / 250 pcs?
4. Digitizing in-house? Cost per design? Could you send photos of shaded, multi-colour embroidery you have digitized (realistic motifs, 6–8 colours)?
5. How do you compensate the draw-in of the embroidery in the pattern?
6. Have you done embroider → assemble → wash before? What happens to the thread in the wash?
7. Price of the base jeans FOB and DDP Berlin at 100 / 150 / 250 pcs?
8. Is the denim in stock, or is there a minimum order at the mill?
9. Payment terms? Is 50/50 possible?
10. Two reference brands with embroidery that I may contact?
11. What happens in case of faulty production?
12. Laser finishing in-house? Which system, cost per piece?
13. Do you cut raw hems to final length after washing? Cost per piece?
14. Can you set thread elements by hand after finishing and secure them on the inside? Cost per piece?
15. Can you supply woven labels and an engraved shank button (17 mm, antique brass, "NOVALIFE")? MOQ and price?

Please also send me the costs and lead times for digitizing, washed stitch-outs and the proto.

Best regards,
Ernest Veskimäe
Novalife · Berlin
[WEBSITE]"""

NACH = """Subject: Re: RFQ – 100 embroidered jeans (NVL-TT-01)

Hello [NAME],

just following up on my request from [DATE]. I'm deciding on the factory on 26 October. Even a short answer to questions 1 and 2 (in-house embroidery on cut panels?) would help me a lot.

Thank you and best regards,
Ernest"""

CALL = """Subject: NVL-TT-01 – 30-minute call this week?

Hello [NAME],

thank you for your offer. You are on my shortlist of three factories. Could we do a 30-minute video call (WhatsApp, Zoom or Google Meet) between Wednesday and Friday? Times that work for me (Berlin time): [SLOT 1], [SLOT 2], [SLOT 3].

During the call I'd like to see your embroidery machines and the washing area on camera. Could you send me before the call:
- photos of a previous production with embroidery on cut panels
- two reference brands I may contact

Best regards,
Ernest"""

VERH = """Subject: NVL-TT-01 – next steps

Hello [NAME],

thank you for the call. I would like to work with you on NVL-TT-01. Before I pay for the development, I'd like to agree on these points in writing:

1. Payment 50 % deposit / 50 % before shipment (instead of 60/40).
2. Development costs (digitizing, stitch-outs, proto) are credited against the bulk order.
3. Digitizing of all 5 elements is included.
4. Dates: digitizing preview by [DATE], washed stitch-outs by [DATE], proto shipped by 30 Nov 2026, PP sample shipped by 4 Jan 2027.
5. Price DDP Berlin for 100 pcs, and for 75 pcs as a fallback.

Please send me a proforma invoice for the development: digitizing, washed stitch-outs, proto W32 fully embroidered and washed, express shipping.

Best regards,
Ernest"""

ABS = """Subject: NVL-TT-01 – thank you

Hello [NAME],

thank you very much for your time and your offer. For this first drop I have decided to work with another factory. I would like to keep your contact for future projects.

Best regards,
Ernest"""

REFC = """EN: Hi [NAME], I'm Ernest from Novalife, a denim brand from Berlin. [FACTORY] gave me your brand as a reference. May I ask you two quick questions? 1) Were quality and dates as agreed? 2) Would you produce with them again? Thanks a lot!

DE: Hi [NAME], ich bin Ernest von Novalife, Denim aus Berlin. [FABRIK] hat euch als Referenz genannt. Darf ich kurz zwei Fragen stellen? 1) Haben Qualität und Termine gestimmt? 2) Würdet ihr dort wieder produzieren? Danke dir!"""

STICK = """Betreff: Anfrage Stickerei auf Zip-Hoodie und Polo, ab 1 Stück

Hallo [NAME],

ich bin Ernest von Novalife, einer Denim-Marke aus Berlin. Für unseren Drop im April 2027 suche ich einen Betrieb in Berlin, der zwei Teile auf Bestellung bestickt:

1. Zip-Hoodie, Fleece 330–350 g/m²: zwei senkrechte Bänder, je 25 mm × ca. 25 cm, links und rechts der Zip-Leiste, im Kreuzstich-Look in Rot und Weiß. Dazu ein Medaillon auf dem Rücken (ca. 200 × 150 mm).
2. Piqué-Polo: zwei Bänder, je 20 mm × ca. 12 cm, links und rechts der Knopfleiste.

Die Motive kommen von uns als Datei. Digitizing durch euch oder als DST/EMB von uns.

Meine Fragen:
1. Stickt ihr auf fertigen Teilen? Wie groß ist euer größter Rahmen?
2. Könnt ihr auf Fleece 330–350 g/m² mit Topping sticken? Habt ihr Beispiele?
3. Könnt ihr auf Piqué sticken?
4. Nehmt ihr DST/EMB-Dateien von außen an, und was kostet das Digitizing bei euch?
5. Preis pro Teil bei 1 / 10 / 50 Stück für die Zipper-Bänder, das Rücken-Medaillon und die Polo-Bänder?
6. Wie lange dauert ein Auftrag?
7. Könnt ihr ein Musterteil besticken? Den Blank bringe ich mit. Was kostet das?

Viele Grüße
Ernest Veskimäe
Novalife · Berlin
[WEBSITE]"""

PATCH = """Subject: Quote request – embroidered patch 86 × 76 mm and chenille patch 200 × 150 mm

Hello,

I'm Ernest from Novalife, a denim brand from Berlin. I would like a quote for two patches (artwork attached):

1. Embroidered patch, 86 × 76 mm, natural linen base, many shades (gold, ochre, three browns, red), fine lines down to 0.8 mm, folded and stitched edge. It will be sewn onto jeans and then go through an industrial enzyme/stone wash. Quantities: 3 samples, then 110 pcs.
2. Chenille patch, approx. 200 × 150 mm, on felt or twill, merrowed edge, colours bordeaux, beige, black and gold. It will be sewn onto a fleece zip hoodie. Quantities: 1 sample, then your minimum.

Questions:
- Price at 20 / 50 / 100 / 200 pcs?
- Sample cost and lead time?
- Production lead time?
- Minimum line width?
- Can the linen be pre-washed so the patch survives an industrial wash without shrinking?

Best regards,
Ernest Veskimäe
Novalife · Berlin"""

CREATOR = """Hey [NAME], ich bin Ernest von Novalife aus Berlin. Ich mache gerade 100 bestickte Jeans, Drop am 22.04. Dein [KONKRETES VIDEO ODER POST] hat mir gezeigt, dass das zu dir passen könnte.

Lust auf eine Anprobe des Samples in Berlin (30 Minuten)? Wenn sie dir gefällt: ein Clip mit Erwähnung, und du bekommst im April ein Paar aus der Serie in deiner Größe. Kein Muss, keine Vorgaben zum Text. Weil das Paar ein Geschenk ist, kennzeichnest du den Post als Werbung."""

LEIT = [
 ("5 Min.", "Rundgang per Kamera: Stickmaschinen (wie viele Köpfe, wie viele Nadeln?), Wäscherei, Laser."),
 ("5 Min.", "Eine Panel-Stickerei aus einer früheren Produktion zeigen lassen, als Foto oder als echtes Teil vor der Kamera."),
 ("5 Min.", "Einzug: „How do you compensate the draw-in?“ Eine gute Antwort nennt größeren Zuschnitt, gemessene Testpanels und Prozent pro Element. Wer die Frage nicht versteht, ist raus."),
 ("5 Min.", "Termine: Digitizing-Vorschau bis wann? Gewaschene Stickproben bis wann? Proto bis 30.11. möglich? PP bis 04.01.? Produktion Februar–März? Feiertage (Ramadan-Fest 08.–11.03.)?"),
 ("5 Min.", "Goldfäden von Hand nach der Wäsche: Wer macht es, wie wird gesichert? Saum nach der Wäsche auf Länge geschnitten?"),
 ("3 Min.", "Zahlung 50/50? Preis DDP Berlin? A.TR bei Türkei?"),
 ("2 Min.", "Wer ist dein Ansprechpartner, auf welchem Kanal (WhatsApp, E-Mail), wie schnell kommen Antworten?"),
]

REF_VORL = ref("vorlagen", "Vorlagen · Mails, DMs und Call-Leitfaden",
    '<p class="intro">Alles, worauf eine Aufgabe mit „Vorlage …“ verweist. Kopieren, die eckigen Klammern ersetzen, senden. Fabriken auf Englisch, Berlin auf Deutsch. <b>Pro Empfänger eine eigene Mail, nie mehrere in CC.</b></p>'
    + '<h3>Fabriken</h3>'
    + copybox("v_rfq", "RFQ Jeansfabrik · Woche 5", RFQ)
    + copybox("v_nach", "Nachfassen · Woche 5", NACH)
    + copybox("v_call", "Call anfragen · Woche 6", CALL)
    + '<h3>Call-Leitfaden · 30 Minuten, bei allen drei gleich</h3>'
    + '<ol class="steps">' + "".join('<li><span><b>%s</b> · %s</span></li>' % (a, e(b)) for a, b in LEIT) + '</ol>'
    + '<p class="intro" style="margin-top:12px">Direkt danach bewerten, je 1–5: Stickerei-Kompetenz, Kommunikation, Preis, Termine, Bauchgefühl. Ins Blatt „Fabriken“.</p>'
    + copybox("v_verh", "Verhandlung und Proforma · Woche 7", VERH)
    + copybox("v_abs", "Absage · Woche 7", ABS)
    + copybox("v_refc", "Referenz-Check · Woche 6", REFC)
    + '<h3>Berlin, Patches, Creator</h3>'
    + copybox("v_stick", "Anfrage Berliner Sticker · Woche 5", STICK)
    + copybox("v_patch", "Patch-Anfrage · Woche 7", PATCH)
    + copybox("v_creator", "Creator-DM · Woche 19", CREATOR),
    "Neu Rev. 5")

# ======================================================================
# 3 · Prüfplan
# ======================================================================
POM = [
 ("Bund, flach (½)", "40,6", "±0,3", "Bund geschlossen, von Kante zu Kante oben"),
 ("Hüfte, 20 cm unter Bund (½)", "50,0", "±0,5", "von der Bundoberkante 20 cm abmessen"),
 ("Vordere Leibhöhe", "28,0", "±0,3", "Schrittnaht bis Bundoberkante vorn"),
 ("Hintere Leibhöhe", "40,0", "±0,3", "Schrittnaht bis Bundoberkante hinten"),
 ("Oberschenkel, 2,5 cm unter Schritt (½)", "30,0", "±0,5", "quer über das Bein"),
 ("Knie, 33 cm unter Schritt (½)", "24,0", "±0,5", "quer über das Bein"),
 ("Beinöffnung (½)", "22,0", "±0,5", "am Saum, quer"),
 ("Innenbeinlänge", "80,5", "±0,5", "Schritt bis Saumkante, an der Innennaht"),
 ("Außenlänge", "106,0", "±0,5", "Bundoberkante bis Saumkante, an der Seitennaht"),
 ("Bundbreite", "4,0", "±0,2", "Höhe des Bundes"),
]
STICK_P = [
 ("A · Band", "Innenkante liegt auf der Taschenöffnung, 23 mm breit (±1), Rapport ohne Sprung, keine Wellen, Kanten scharf."),
 ("E · Münztasche", "Ganze Fläche bestickt, 60 × 60 mm (±1) auf 62-mm-Tasche, Raster gerade zur Taschenkante, untere rechte Ecke unter dem Band, Tasche danach sauber angenäht."),
 ("B · Serp im Stoppelfeld", "Linkes Bein vorn, 10 mm (±2) neben der Seitennaht, Höhe laut Tech Pack, ca. 53 × 49 mm. Klinge weiß, Schneide rot, Griff braun. Die Halme einzeln lesbar, Schnittkanten hell. Kein Stern, kein Hammer, kein roter Grund."),
 ("B2 · Ähren und Fäden", "Drei Ähren über dem roten Band, Band 48 mm (±1), einfach rot, Kanten sauber. 9 Goldfäden, 18–30 mm lang, dreifach gezwirnt, ungleich verteilt, innen in der Tasche verknotet. Zugtest: sanft ziehen, nichts löst sich."),
 ("C · Alatyr", "36 × 36 mm (±1), rechte Gesäßtasche, waagerecht mittig, auf Höhe des roten Bands links."),
 ("D · Patch", "86 × 76 mm, gerade (höchstens 2 mm schief), zwischen den mittleren Schlaufen, Kante fest. Nach der Wäsche nicht geschrumpft, nicht gewellt."),
 ("Alle", "Platzierung ±3 mm. Farben wie freigegeben. Rückseite: Vlies sauber geschnitten, keine losen Fäden über 5 mm. Nach der Wäsche nichts ausgefranst, nichts stumpf."),
]
VERARB = [
 "Nähte gerade, Riegel an allen Taschen, Nieten fest, Knopf fest, Reißverschluss läuft ohne Haken.",
 "Saum roh, gerade geschnitten, beide Beine gleich lang (höchstens 5 mm Unterschied).",
 "Waschton im Zielbereich L* 34–40: bei Tageslicht neben dem freigegebenen Lab Dip. Kein Kantenabrieb an der Tasche mit Band A.",
 "Labels: Hauptlabel innen hinten am Bund, Größenlabel mit der richtigen Größe, Pflegeetikett mit „100 % Baumwolle“, Herkunftsland und „Auf links waschen, Fäden nicht abschneiden“.",
]
FEHLER = [
 ("Kritisch", "crit", "Nicht verkaufen, reklamieren", "Loch, bleibender Fleck, Stickerei fehlt oder sitzt mehr als 5 mm falsch, Maß außerhalb der Toleranz, Reißverschluss defekt, Patch fehlt."),
 ("Hauptfehler", "warn", "Selbst nacharbeiten, wenn unter 5 Minuten", "Lose Fäden über 1 cm, weniger als 7 Goldfäden, Patch 2–5 mm schief, Saumunterschied 5–10 mm."),
 ("Nebenfehler", "ok", "Verkaufen", "Kurze Fadenenden, kleine Schwankung im Waschton innerhalb L* ±2."),
]
REF_PRUEF = ref("pruefplan", "Prüfplan · Sample und Wareneingang",
    '<p class="intro">Derselbe Plan für jedes Teil, das du in die Hand bekommst: Proto (Woche 12), PP-Sample (Woche 17), Inline-Fotos (Woche 23 und 25), Endkontrolle (Woche 27) und die Ware (Woche 29). Ausdrucken, abhaken, Ergebnisse in die Tabelle.</p>'
    + '<h3>1 · Zehn Messpunkte · Größe W32</h3>'
    + table(["Messpunkt", "Soll (cm)", "Toleranz", "Wie"], [(a, b, c, d) for a, b, c, d in POM],
            "Flach hinlegen, glattstreichen, nicht ziehen. Jeden Punkt zweimal messen und den Mittelwert eintragen. Werte für die anderen Größen stehen unter Sizing.", num=(1, 2))
    + '<h3>2 · Stickerei, Element für Element</h3>'
    + table(["Element", "Prüfen"], STICK_P)
    + '<h3>3 · Verarbeitung, Waschung, Labels</h3>'
    + '<ol class="steps">' + "".join('<li><span>%s</span></li>' % e(x) for x in VERARB) + '</ol>'
    + '<h3>4 · Wareneingang · Fehlerklassen</h3>'
    + "".join('<div class="risk%s"><div class="rh"><span class="rt">%s</span><span class="pill %s">%s</span></div><p>%s</p></div>'
              % ("" if c == "crit" else " med", a, c, e(b), e(d)) for a, c, b, d in FEHLER)
    + '<div class="callout plain"><span class="eyebrow">So läuft die Prüfung der 100 Jeans</span>'
      '<p><b>Sichtprüfung bei allen</b>, je 2 Minuten, verteilt auf zwei Abende (31.03. und 01.04.). <b>Maße bei 15 Stück</b>, drei pro Größe (02.04.). Grüner Punkt aufs Größenlabel heißt geprüft, roter Punkt heißt Fehler mit Foto und Eintrag ins Blatt „QC“. Reklamationsfrist 14 Tage ab Ankunft, mit der Fabrik in Woche 26 schriftlich vereinbart. Teile mit rotem Punkt gehen nicht in den Drop.</p></div>',
    "Neu Rev. 5")

# ======================================================================
# 4 · Content-Regeln und Countdown
# ======================================================================
def ref_content(MOTIV, tag):
    phasen = [
     ("bis 11.10.", "0", "Profile vorbereiten, erster Content-Batch am 10.10."),
     ("12.10.–29.11.", "3 pro Woche", "Mo BUILD 18:00 · Mi ORIGIN 18:00 · Fr REAL oder DETAIL 18:00. Papiertest, Bauplan, Zahlen, Fabriksuche, Referenzen, Stickproben, Stoffe, Teppich. <b>Kein fertiges Teil.</b>"),
     ("ab 30.11. (Proto)", "5 pro Woche", "Mo BUILD 18:00 · Di ORIGIN 18:00 · Mi REACH 19:00 · Fr DETAIL 18:00 · Sa ASK 12:00 (Story). Ab jetzt gibt es ein echtes Teil."),
     ("21.12.–03.01.", "2–3 pro Woche", "Feiertage. Rückblick und Ausblick, nichts Neues drehen."),
     ("04.01.–07.02.", "4–5 pro Woche", "Vorbestellung: echte Zahlen „X von 35“, Zwischenstand-Storys, Q&A."),
     ("08.02.–28.03.", "4 pro Woche + Story", "Produktion, Shoot, Kampagne, Verpackung."),
     ("29.03.–21.04.", "täglich 18:00", "Countdown T−24 bis T−1. An echten Tagen (Ware da, Pakete raus) ersetzt ein Live-Clip das Asset."),
     ("22.04.", "18:00 und 19:00", "Warteliste zuerst, dann öffentlich. Siehe „Drop-Tag · Minute für Minute“."),
    ]
    regeln = [
     "<b>Gezeigt wird nur, was es gibt.</b> Bis das Proto am 03.12. da ist: Papier, Dateien, Zahlen, Mails, Referenzen. Kein Rendering und kein Mockup, das wie ein fertiges Produkt aussieht.",
     "<b>Subjekt ist das Muster, nicht das Volk.</b> „Dieses Muster ist älter als jede Grenze“ geht. „Wir sind ein Volk“ geht nicht. Keine Landkarten, keine Flaggenfarben.",
     "<b>Nie hellblauer Himmel über gelbem Weizen.</b> Weizen-Bilder im Sonnenuntergang: Orange, Bordeaux, Dämmerungsviolett.",
     "<b>Nie „authentisch“.</b> Den Lebensbaum nie „slawisch“ nennen.",
     "<b>Fabrik-Bilder und -Namen nur mit Erlaubnis.</b> Vorher fragen, schriftlich.",
     "<b>Nur echte Zahlen.</b> Vorbestellungen, Bestand, Kosten: so, wie sie sind.",
     "<b>Jeder Post endet mit dem Aufruf zur Warteliste:</b> „Link in Bio: Trag dich ein. Wer auf der Liste ist, kauft zuerst und zum Vorbestellpreis.“",
     "<b>Gedreht wird sonntags im Batch.</b> Am Posttag nur posten und 15 Minuten lang Kommentare beantworten.",
     "<b>Geschenkt heißt Werbung.</b> Creator, die ein Paar bekommen, kennzeichnen ihren Post als Werbung.",
    ]
    korr = [
     ("31.12.2026", "700", "Hooks überarbeiten: Claude die drei besten und drei schwächsten Posts geben"),
     ("31.01.2027", "1.500", "Vorteil der Liste deutlicher sagen: zuerst kaufen, 20 € günstiger"),
     ("28.02.2027", "2.400", "Creator-Anproben verdoppeln, Werbung früher starten"),
     ("22.04.2027", "3.000", "—"),
    ]
    drop = [
     ("ab 17:00", "Frei. Nichts anderes einplanen."),
     ("17:30", "Shop am Handy öffnen (mit Spiel: das Feld). Preise und Bestände ein letztes Mal."),
     ("18:00", "Produkte gehen automatisch live. E-Mail T−1h an die Warteliste mit dem Link zur Kollektion (mit Spiel: Schlüssel-Link). 18:01 den Link selbst im privaten Fenster testen."),
     ("18:00–19:00", "Erste Bestellungen, DMs beantworten. Story: „Die Warteliste kauft gerade.“"),
     ("18:50", "Story „10 Minuten“."),
     ("19:00", "<b>Öffentlich.</b> Ohne Spiel das Theme „Drop 22.04.“ veröffentlichen. E-Mail LIVE geht raus. Kampagnenfilm auf TikTok und als Reel. Story mit Link, Link in beiden Bios auf die Kollektion. Werbekampagne 2 startet."),
     ("19:15", "Erster Zwischenstand in der Story, echte Zahl."),
     ("20:00", "Restbestand pro Größe in die Story."),
     ("22:00", "Danke und Zwischenstand. Bis 23:00 jede Nachricht beantworten."),
     ("Fr–Sa", "Packen. Bis Samstagabend sind alle Bestellungen von Donnerstag und Freitag raus."),
     ("So 25.04.", "Auswertung nach 72 Stunden. Blanks für Zipper und Polo bestellen."),
    ]
    cdrows = [("T−%d" % n, tag(n), e(MOTIV[n])) for n in range(24, 0, -1)]
    return ref("content", "Content-Regeln, Countdown und Drop-Tag",
        '<p class="intro">Feste Slots, damit du nie überlegen musst, was heute kommt. Die Themen stehen im Tagesplan, Hook und Bildideen in jeder Post-Aufgabe.</p>'
        + table(["Zeitraum", "Posts", "Was"], phasen)
        + '<h3>Neun Regeln</h3><ol class="steps">' + "".join('<li><span>%s</span></li>' % r for r in regeln) + '</ol>'
        + '<h3>Countdown · 24 Videos, vorproduziert am 18. und 20.03.</h3>'
        + table(["Tag", "Datum", "Motiv"], cdrows,
                "Eine Vorlage in CapCut: 9:16, dunkler Indigo-Grund, oben groß T−n, unten „22.04. · 19:00“, in der Mitte ein Clip von 4–6 Sekunden. Gepostet um 18:00 auf TikTok, als Reel und als Story mit Countdown-Sticker. Wer im Sticker „Erinnern“ tippt, bekommt von Instagram eine Nachricht, wenn es losgeht.")
        + '<h3>Warteliste · Zielkorridor</h3>'
        + table(["Stichtag", "Anmeldungen", "Wenn du drunter liegst"], korr,
                "Die Zahl steht jeden Sonntag im Review in der Tabelle. 3.000 Adressen bei 2–3 % Kaufquote sind 60–90 Käufe, das ist dein Drop.", num=(1,))
        + '<h3>Drop-Tag · Minute für Minute</h3>'
        + table(["Zeit", "Was passiert"], drop))

# ======================================================================
# 5 · Fabriken
# ======================================================================
FAB = [
 ("Istanbul Clothing Manufacturers", "TR", "Startpunkt", "Öffentlich: MOQ 100 pro Modell, Sample 7–10 Tage, Produktion 4–5 Wochen bei Lagerstoff, 60/40. Stickerei im Haus ist ungeklärt, das ist die erste Frage.", "istanbulclothingmanufacturers.com"),
 ("Portugal Textile · Jeans Factory", "PT", "Startpunkt", "Denim mit eigener Wäscherei, Tech-Pack-Unterstützung, 20-Punkte-QC. Teurer als die Türkei, dafür EU: keine Einfuhrumsatzsteuer, kurze Wege.", "portugaltextile.com"),
 ("Brosan Textile", "TR", "Vergleich", "Denim- und Jeanshersteller. Als Vergleich, ob dein Preis marktgerecht ist.", "brosantextile.com"),
 ("White Cotton", "PT", "Plan B", "MOQ ab 50. Rückfallebene, falls die Schwelle nur 75 Stück erlaubt.", "whitecotton.pt"),
]
def ref_fabriken():
    h = ('<div class="callout"><span class="eyebrow">Eine Fabrik. Deshalb 8 Anfragen, nicht 15.</span>'
         '<p>Du bestellst bei genau einer Fabrik. Von 8 Anfragen antwortet erfahrungsgemäß die Hälfte, und nur 2–3 können <b>Stickerei auf dem Zuschnitt im eigenen Haus</b>. Mit diesen drei sprichst du (Woche 6), eine nimmst du (26.10.), die zweite bleibt als Reserve. Den anderen wird abgesagt.</p>'
         '<p><b>Pflicht:</b> Panel-Stickerei im eigenen Haus, nachgewiesen mit Fotos einer früheren Produktion. Wird extern gestickt, wandern deine Zuschnitte zwischen zwei Betrieben, und jeder Fehler landet zwischen den Stühlen.</p></div>'
         '<p class="intro">Startpunkte für die Recherche in Woche 4. Angaben aus öffentlichen Quellen, nicht geprüft. Die 8 Fabriken mit geprüfter E-Mail von der eigenen Website recherchiert Claude am 11.10.</p>')
    for nm, cc, rank, txt, url in FAB:
        h += ('<div class="fac"><div class="top"><span class="nm">%s</span><span class="cc">%s</span><span class="rank">%s</span></div>'
              '<p>%s</p><div class="dl"><div><span>Website</span>%s</div></div></div>' % (e(nm), cc, rank, e(txt), url))
    h += '<h3>Scorecard · Woche 7</h3>'
    h += table(["Kriterium", "Gewicht", "Woran du es misst"], [
        ("Panel-Stickerei im Haus, nachgewiesen", "Pflicht", "Fotos einer früheren Produktion, im Call gezeigt"),
        ("Preis bei 100 Stück inkl. Stickerei, DDP Berlin", "hoch", "Angebot, umgerechnet auf ein Paar"),
        ("Termine: Proto bis 30.11., PP bis 04.01.", "hoch", "schriftlich im Angebot oder nach dem Call"),
        ("Einzug-Kompensation verstanden", "hoch", "Antwort im Call"),
        ("Zahlung 50/50", "mittel", "schriftlich"),
        ("Kommunikation", "mittel", "Antwortzeit, Klarheit, Englisch"),
        ("Steuer und Zoll nach deinem Status", "mittel", "Türkei: Einfuhrumsatzsteuer. Portugal: keine"),
    ])
    h += ('<div class="callout plain"><span class="eyebrow">Warum Türkei oder Portugal, nicht Asien</span>'
          '<p>Aus China killt dich bei 100 Stück der Import: MOQ meist 300+, 12 % Zoll, 19 % Einfuhrumsatzsteuer, 5 Wochen Seefracht. Die Türkei ist in der Zollunion mit der EU: <b>kein Zoll mit A.TR-Bescheinigung</b>, LKW 3–7 Tage. Die Einfuhrumsatzsteuer von 19 % bleibt. Portugal ist EU: weder Zoll noch Einfuhrumsatzsteuer.</p></div>'
          '<div class="callout bad"><span class="eyebrow">Steuer · klären in Woche 5</span>'
          '<p>Als <b>Kleinunternehmer</b> (Umsatz im Vorjahr höchstens 25.000 €, im laufenden Jahr höchstens 100.000 €) weist du keine Umsatzsteuer aus, kannst aber auch <b>keine Vorsteuer abziehen</b>. Die Einfuhrumsatzsteuer auf Ware aus der Türkei ist dann echter Aufwand: rund 1.150 € auf die Lieferung. Ob sich der Verzicht auf die Kleinunternehmerregelung lohnt oder Portugal günstiger ist, klärst du mit einem Steuerberater. Ich bin kein Steuerberater.</p></div>'
          '<h3>Berliner Sticker · Zipper und Polo</h3>'
          '<p class="intro">Drei Anfragen (Woche 5), zwei Musterteile (Woche 7–14, Budget 180 €), einer wird gewählt (17.12.). Pflichtfragen: Fleece 330–350 g/m² mit Topping? Piqué? Externe DST/EMB-Dateien? Preis bei 1 / 10 / 50 Stück und Lieferzeit pro Auftrag. Die Vorlage steht unter Vorlagen.</p>')
    return ref("fabriken", "Fabriken · Auswahl, Scorecard, Steuer", h)

# ======================================================================
# 6 · Kalkulation
# ======================================================================
def ref_kalk():
    stk = table(["Position", "€ / Paar", "Grundlage"], [
        ("Basis-Jeans, Zuschnitt und Nähen", "35,00", "12 oz, 100 % Baumwolle, Waschung, Hardware, Labels"),
        ("Stickerei ~33.000 Stiche", "18,00", "~0,55 € pro 1.000 Stiche, Design v1.7"),
        ("Panel-Handling, 5 Zonen", "5,00", "Vorderteil rechts, Münztasche, beide Gesäßtaschen, Vorderteil links"),
        ("Label-Patch D, zugekauft", "3,00", "86 × 76 mm, MOQ 100"),
        ("Goldfäden, Handarbeit", "2,00", "nach der Wäsche, 9 Fäden"),
        (("<b>Stückkosten</b>", "<b>63,00</b>", "Spec Rev. 13"), "total"),
    ], "Echter Kreuzstich statt feiner Füllung kann 5.000–10.000 Stiche mehr bedeuten, also +3 bis +5 € je Paar. Die echte Stichzahl kommt mit der Digitizing-Vorschau (Woche 9).", num=(1,))
    bud = table(["Phase", "Posten", "Betrag", "Fällig"], [
        ("Entwicklung", "Schnitt und Gradierung W30–W38", "300 €", "Nov 26"),
        ("", "Digitizing Jeans, 5 Elemente", "320 €", "Nov 26"),
        ("", "Digitizing Zipper- und Polo-Bänder, Medaillon", "240 €", "Nov 26"),
        ("", "Stickproben, gewaschen", "150 €", "Nov 26"),
        ("", "Proto W32", "180 €", "Nov 26"),
        ("", "PP-Sample", "220 €", "Dez 26"),
        ("", "Stoffmuster, Lab Dips, Waschtests", "90 €", "Nov 26"),
        ("", "Labels, Hangtags, Knopf-Gravur (Setup)", "150 €", "Dez 26"),
        ("", "Label-Patch D, 3 Muster", "80 €", "Nov 26"),
        ("", "Blank-Muster Berlin (Zipper und Polo)", "180 €", "Nov 26"),
        ("", "Chenille-Muster (nur falls gewählt)", "120 €", "Jan 27"),
        ("", "Shopify bis April und Domain", "150 €", "Okt 26–Apr 27"),
        ("", "Lookbook-Shoot", "150 €", "Feb 27"),
        (("", "<b>Zwischensumme</b>", "<b>2.330 €</b>", ""), "sub"),
        ("Produktion", "Label-Patch D, 110 Stück", "~330 €", "Dez 26"),
        ("", "Anzahlung 50 % (100 × ~60 € Fabrikpreis)", "3.000 €", "Feb 27"),
        ("", "Restzahlung 50 %", "3.000 €", "Mär 27"),
        ("Launch", "Verpackung inkl. Hangtags", "240 €", "Feb 27"),
        ("", "Versandmaterial", "80 €", "Mär 27"),
        ("", "Werbung, 2 Kampagnen", "300 €", "Mär–Apr 27"),
        ("", "Puffer (Aseprite, Rechtstexte, Kleinkram)", "100 €", "—"),
        (("", "<b>Kapitalbedarf gesamt</b>", "<b>9.380 €</b>", ""), "total"),
        (("", "Eigenbudget", "4.500 €", ""), "total"),
        (("", "<b>Lücke, nur aus Vorbestellungen</b>", "<b>4.880 €</b>", "Feb–Mär 27"), "total"),
    ], "Bei 60/40 statt 50/50 steigt die Anzahlung auf ~3.600 €. Gegenüber Design v1.5 sind es −300 €. Blanks für Zipper und Polo tauchen nicht auf, sie werden erst nach bezahlter Bestellung gekauft.", num=(2,))
    cash = table(["Zeitpunkt", "Fällig", "Budget übrig vorher", "Aus Vorbestellungen nötig", "Vorbestellungen à 149 €"], [
        ("Mo 01.02. Schwelle", "Anzahlung 3.000 €", "~1.990 €", "~1.010 €", "<b>mindestens 10</b>"),
        ("Fr 19.03. Restzahlung", "Rest 3.000 €, Shoot, Verpackung, Versandmaterial, Werbung", "0 €", "~4.500–4.650 €", "<b>mindestens 32</b>"),
        ("Do 22.04. Drop", "—", "—", "—", "ab hier trägt der Drop"),
    ], "Rechnung mit ~146 € netto pro Vorbestellung nach Zahlungsgebühr. Zwischen 32 und 35 liegen 3 Paar Puffer. Deshalb die Regel in Woche 21: Mehr als 25 Vorbestellungen bis zur Schwelle, dann Kontingent auf 45.", num=(4,))
    ums = table(["Szenario", "Vorbestellung × 149 €", "Drop × 169 €", "Verkauft", "Umsatz"], [
        ("<b>Ausverkauf</b>", "35 → 5.215 €", "58 → 9.802 €", "93", "<b>15.017 €</b>"),
        ("<b>Ziel</b>", "35 → 5.215 €", "29 → 4.901 €", "64", "<b>10.116 €</b>"),
        ("<b>Break-even</b>", "35 → 5.215 €", "25 → 4.225 €", "60", "<b>9.440 €</b>"),
    ], "93 verkäufliche Paar: 100 minus 5 Creator-Paare minus 2 Reserve. Zahlungsgebühren (Shopify Payments im Basic-Tarif 2,1 % + 0,30 € pro Zahlung), Versandzuschuss und Retouren sind nicht abgezogen, real liegst du 3–5 % darunter.", num=(1, 2, 3, 4))
    marge = table(["Position", "€", "Kommentar"], [
        ("Verkaufspreis", "169,00", "brutto"),
        ("abzüglich Umsatzsteuer 19 %", "−26,98", "entfällt als Kleinunternehmer"),
        ("abzüglich Stückkosten", "−63,00", "Spec Rev. 13"),
        ("abzüglich Zahlungsgebühr", "−3,85", "Shopify Payments, Basic: 2,1 % + 0,30 €"),
        ("abzüglich Verpackung und Versandanteil", "−6,50", "Kunde zahlt 4,90 € in DE"),
        (("<b>Deckungsbeitrag</b>", "<b>68,67</b>", "als Kleinunternehmer 95,65 €, dafür ist die Einfuhrumsatzsteuer Aufwand"), "total"),
    ], num=(1,))
    zp = table(["Produkt", "Kosten", "Preis", "Marge", "Kapital"], [
        ("Zipper", "~45 €", "139 €", "~82 €", "keins, Blank nach Bestellung"),
        ("Polo", "~19 €", "79 €", "~50 €", "keins, Blank nach Bestellung"),
    ], "Zipper und Polo bringen Gewinn nach dem Drop. Zur Finanzierung vor dem Drop tragen sie nichts bei.")
    return ref("kalk", "Kalkulation · Stückkosten, Budget, Cash",
        '<h3>Stückkosten Jeans · ~63 €</h3>' + stk
        + '<h3>Budget · was wann rausgeht</h3>' + bud
        + '<h3>Cash · wann die Vorbestellungen da sein müssen</h3>' + cash
        + '<h3>Umsatz Jeans · drei Szenarien</h3>' + ums
        + '<h3>Marge pro Paar</h3>' + marge
        + '<h3>Zipper und Polo</h3>' + zp)

# ======================================================================
# 7 · Tech Pack
# ======================================================================
def ref_techpack():
    sek = [
     "<b>Deckblatt</b> · Novalife, NVL-TT-01, eine Variante, Farbcode, Version und Datum.",
     "<b>Flachzeichnungen</b> · vorn und hinten, alle fünf Elemente mit Maß und Position ab Naht, Sicht des Trägers.",
     "<b>Maßtabelle</b> · W30–W38 mit Toleranzen (siehe Sizing).",
     "<b>Stückliste (BOM)</b> · jedes Bauteil mit Material, Maß, Farbe, Lieferant.",
     "<b>Stoff und Waschung</b> · 12 oz, rigid, Grundton L* 34–40 (±2), lokaler Abrieb, Laser, kein Kantenabrieb an der Tasche mit Band A.",
     "<b>Stickspezifikation</b> · pro Element A–E: Maß, Stichzahl, Garnfarben, Stichart (Kreuzstich-Look, Raster 1,33 mm), Platzierung ab Naht, Cut-away-Vlies.",
     "<b>Konstruktion</b> · Reihenfolge sticken → nähen → Patch D aufnähen → waschen → Saum auf Länge schneiden → Goldfäden von Hand.",
     "<b>Labels und Verpackung</b> · Haupt-, Größen-, Pflegeetikett, Hangtags bringt Novalife selbst an.",
     "<b>Prüfplan</b> · Messpunkte, Stickkriterien, Fehlerklassen (siehe Prüfplan).",
    ]
    bom = [
     ("Oberstoff", "12 oz Denim, 100 % Baumwolle, rigid, 3/1 Köper", "1,5 lfm"),
     ("Stickgarn Weiß", "Polyester, L* 85–88, Pflichtfarbe in jedem Element", "alle"),
     ("Stickgarn Rot", "Polyester, tiefes Rot", "A, B, B2, C, E"),
     ("Stickgarn Gold", "Polyester, nicht metallisiert", "B, B2"),
     ("Stickgarn Braun", "Polyester, mittelbraun", "B"),
     ("Goldfäden", "Polyester Gold, nicht metallisiert, dreifach gezwirnt, von Hand gesetzt", "9 Fäden, 18–30 mm"),
     ("Label-Patch D", "Stickpatch 86 × 76 mm auf Naturleinen, zugekauft, liefert Novalife", "1"),
     ("Stabilisator", "Cut-away, mittelschwer", "—"),
     ("Hauptgarn / Steppgarn", "Poly-Core Tex 40 / Tex 60 Goldgelb", "—"),
     ("Knopf", "Shank Button 17 mm, Antik-Messing, graviert „NOVALIFE“", "1"),
     ("Nieten", "9 mm Antik-Messing", "6"),
     ("Reißverschluss", "YKK 4,5 Metall, Antik-Messing", "1"),
     ("Labels", "Hauptlabel Bund hinten, Größenlabel, Pflegeetikett (EU-Pflicht, Materialangabe)", "je 1"),
     ("Hangtag", "Recyclingkarton 300 g/m², Stücknummer 001–100, bringt Novalife an", "1"),
    ]
    return ref("techpack", "Tech Pack · 9 Abschnitte und Stückliste",
        '<p class="intro">Das Tech Pack ist kein Designdokument, es ist ein Vertrag. Was nicht drinsteht, entscheidet die Fabrik, und zwar so, wie es für sie am billigsten ist. v1.0 baut Claude am 04.10., du gibst es am 09.10. frei, v1.1 mit den Antworten aus den Calls geht am 03.11. an die Fabrik.</p>'
        + '<ol class="steps">' + "".join('<li><span>%s</span></li>' % x for x in sek) + '</ol>'
        + '<div class="callout"><span class="eyebrow">Die drei Punkte, an denen Stickerei scheitert</span>'
          '<p><b>Panel-Stickerei.</b> Ein Hosenbein ist eine geschlossene Röhre, die Stickerei passt nur auf den flachen Zuschnitt vor dem Nähen.</p>'
          '<p><b>Einzug.</b> Stickerei zieht den Stoff zusammen, der bestickte Zuschnitt wird kleiner. Der Schnitt muss das ausgleichen, sonst sitzt die Hose enger als die Maßtabelle.</p>'
          '<p><b>Garn.</b> Polyester, nicht Rayon. Rayon zerlegt sich in der Steinwäsche.</p></div>'
        + '<h3>Stückliste</h3>' + table(["Bauteil", "Spezifikation", "Menge"], bom))

# ======================================================================
# 8 · Risiken
# ======================================================================
RISK = [
 ("1 · Die Finanzierung", "crit", "Kritisch",
  "Kapitalbedarf <b>9.380 €</b>, Budget 4.500 €, Lücke <b>4.880 €</b>. Sie kommt aus genau einer Quelle: den Vorbestellungen ab 14.01. Mindestens 10 bis zur Schwelle am 01.02., mindestens 32 bis zur Restzahlung am 19.03. Das Kontingent ist 35, der Puffer also 3 Paar.",
  "50/50 statt 60/40 verhandeln (Woche 7). Schwelle am 01.02.: unter 10 keine Anzahlung, dann 75 Stück oder 2 Wochen schieben. Mehr als 25 Vorbestellungen bis zur Schwelle: Kontingent auf 45. Reicht es im März trotzdem nicht: Restzahlung gegen Versandnachweis oder Teilzahlung (Woche 26). Keine neue Stickerei ohne Gegenrechnung."),
 ("2 · Einfuhrumsatzsteuer", "warn", "Hoch · neu",
  "Als Kleinunternehmer kannst du keine Vorsteuer abziehen. Bei einer Fabrik in der Türkei sind 19 % Einfuhrumsatzsteuer auf rund 6.000 € Ware echter Aufwand, etwa 1.150 €. Das sind rund 8 Vorbestellungen, die es im Plan nicht gibt.",
  "Steuerstatus am 13.10. mit einem Steuerberater klären. Ergebnis geht in den Fabrikvergleich: Portugal kann trotz höherem Preis günstiger sein."),
 ("3 · Die Stickerei geht schief", "crit", "Kritisch",
  "Der Stoff wellt sich, der Zuschnitt zieht sich zusammen, die Wäsche zerlegt das Garn oder schrumpft den Leinen-Patch. Jeder Fehler sitzt 100-mal.",
  "Gewaschene Stickproben (17.11.) vor dem Proto. Patch-Waschtest (26.11.). Proto mit Fit-Test (03.–05.12.). PP-Sample komplett (04.01.). Inline-Fotos zweimal (16.02., 01.03.). Endkontrolle vor der Restzahlung (19.03.)."),
 ("4 · Ein Design, kein Fallback", "crit", "Kritisch",
  "Alle 100 Teile hängen an einem Ornament. Wenn es nicht ankommt, kommt nichts an.",
  "Validierung am 01.11. aus echten Content-Zahlen, bevor die Entwicklung bezahlt wird. Das ist der billigste Ausstieg im ganzen Plan."),
 ("5 · Die Warteliste ist zu klein", "crit", "Kritisch",
  "100 Paar verkaufen ist eine Marketingleistung. Ohne rund 3.000 Adressen bleibst du bei 30–40 Paar.",
  "Zielkorridor 700 / 1.500 / 2.400 / 3.000 jeden Sonntag prüfen. Ab Dezember jede Woche ein Post mit echter Zahl. Creator-Anproben im Januar."),
 ("6 · Deine Zeit", "warn", "Hoch · neu",
  "1–2 Stunden pro Tag, rund 200 Stunden bis zum Drop. Fünf Tage sind länger: Shoot 20.02., Prüfung der Ware 31.03.–02.04., Drop und Packen 22.–24.04.",
  "Freie Tage jetzt schon einplanen (Aufgabe 05.03.), Packhilfe für den 23. und 24.04. Das Spiel nur bauen, wenn am 05.02. beides stimmt: Vorbestellung läuft und 3 Abende pro Woche sind frei."),
 ("7 · Termine der Fabrik", "warn", "Hoch · neu",
  "Ramadan-Fest 08.–11.03. (Türkei), Ostern 26.–29.03. ohne Zoll und Zustellung. Ein Engpass im März schiebt die Ankunft hinter den Drop.",
  "Termine rund um das Fest am 04.03. schriftlich. Spätester Ankunftstermin für den Drop: 15.04. Später: Drop um eine Woche schieben oder mit Versand ab Ankunft, offen angekündigt."),
 ("8 · Kommunikation", "ok", "Gesteuert",
  "Ein Herkunftsthema ohne Regel erzeugt politische Kommentarspalten statt Verkäufe.",
  "Subjekt ist das Muster, nicht das Volk. Keine Flaggenfarben. Nie „authentisch“. Gilt für jeden Post, jede E-Mail, jede Produktseite."),
 ("9 · Das Spiel bremst den Kauf", "warn", "Mittel",
  "Eine Startseite, durch die man erst laufen muss, kostet am Drop-Tag Verkäufe.",
  "Nur bei „bauen“. Button „Direkt zum Shop“ immer sichtbar, ab 19:00 Start direkt vor der offenen Tür, PLAN B in unter einer Minute, Code-Freeze 17.04."),
]
def ref_risiken():
    h = ""
    for t, c, pill, a, b in RISK:
        h += ('<div class="risk%s"><div class="rh"><span class="rt">%s</span><span class="pill %s">%s</span></div>'
              '<p>%s</p><p><b>Gegenmaßnahme:</b> %s</p></div>' % ("" if c == "crit" else " med", e(t), c, pill, a, b))
    return ref("risiken", "Risiken", h)
