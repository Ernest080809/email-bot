# -*- coding: utf-8 -*-
"""Rev. 7 · Design-Phase: W7 Design-Suche, W8–W11 Design fertig (26.10.–29.11.2026)."""
from lib7 import O, T, N, DROP, DROPALL, week, LINKS

CAPTURE = "Für den Content-Vorrat (Marketing startet Mo 30.11.): "
TZ = "15:00 Istanbul = 14:00 Nikosia (Republik Zypern) = 13:00 Berlin"


def board(nr, name, bereich, was, frage):
    return T('G', f"Design-Suche {nr}/5: {name}", f"r7-suche-{bereich}", m=40, s=[
        f"Pinterest (oder Are.na) öffnen, geheimes Board „TT · {name}“ anlegen. Geheim, damit niemand deine Richtung vor dem Start sieht.",
        f"Suchen und pinnen: {was}",
        "8 bis 12 Pins. Zu jedem Pin ein Wort in die Beschreibung: warum er dir gefällt (Material, Schrift, Farbe, Gefühl).",
        "Dann 3 Pins markieren, die du NICHT willst, mit Grund. Das ist für Claude genauso wichtig wie das, was du willst.",
        f"Eine Frage für dich, schriftlich im Board: {frage}",
        "Board-Link oder Screenshots an Claude (Prompt unten). Claude macht daraus bis zur Designwoche zwei Entwürfe in deinem Stil.",
    ], f="das Board 8–12 Pins mit je einem Wort, 3 Nein-Pins und deine Antwort auf die Frage hat und bei Claude liegt.",
       p=f"Projekt Time Travel, Design-Suche „{name}“ (Docket Rev. 7, W7). Hier ist mein Board mit Pins und meinen Notizen: [Link oder Screenshots]. Meine Nein-Pins: [3 mit Grund]. Meine Antwort auf die Frage: [..]. Fasse in 5 Zeilen zusammen, was ich will (Material, Farben, Schrift, Gefühl) und was nicht. Gleiche das mit dem Time-Travel-Design ab (Kreuzstich-Raster, Knallrot, Naturweiß, Leinen, Antik-Kupfer, Sprachregel „das Muster ist das Subjekt“). Sag mir ehrlich, wo meine Wahl mit dem Rest bricht. Noch keine Entwürfe, die kommen in der Designwoche.",
       o=['pinterest', 'arena', 'claude'])


def w07():
    DROP('w7d0t0', 'überholt: Die Fabrikwahl ist jetzt Di 03.11. (Rev. 7).')
    DROP('w7d0t5', 'erledigt 24.–26.10.: Teppich in zwei Farben, Papiertest-PDF.')
    DROPALL(['w7d1t0', 'w7d1t1'], 'überholt: Konditionen und Absagen stehen jetzt Mi 04.11.')
    DROPALL(['w7d3t0', 'w7d3t1'], 'Notizen vom 23.10.; der Weg des Polos ist jetzt eine eigene Entscheidung am Di 17.11.')
    DROP('w7d5t3', 'gilt weiter, steht in Referenz „Wochenziele, Gates“ 7.4.')
    DROP('w7d6t2', 'Markt am 01.11. fällt in die Design-Suche; Märkte kommen ab Dezember als Grind+.')
    DROPALL(['w7d1t4', 'w7d3t5', 'w7d5t2'], 'Community-Runde läuft ab Mo 30.11. mit dem Marketing.')

    mo = [
        N("ERLEDIGT 26.10. (Claude, mit deinem Ja): Die Erinnerung an Kuzgunlar und die Anfrage an LOGIC (Łódź) sind raus. Gebaut: Maßtabelle Zipper S–XL, Rückendruck B (Band A oben am Hals) und das Papiertest-PDF mit 11 Seiten."),
    ]
    di = [
        N("ERLEDIGT 27.10.: Emirhan (Kuzgunlar) will telefonieren. Deine Zeiten sind raus (Istanbuler Zeit): Mi 28.10. ab 15:00, Fr 30.10. 10:00–13:00 oder Sa 31.10. tagsüber. Er soll vorher eine grobe Schätzung mailen."),
        N("27.10.: Du hast den Docket komplett neu bestellt. Ab heute gilt diese Reihenfolge: zuerst die Design-Suche, dann Design fertig bis So 29.11., danach Marketing und Recht ab Mo 30.11. Die Website läuft parallel."),
        O('w7d1t6', id='w7d1t6'),
    ]
    mi = [
        T('B', f"Kuzgunlar-Call, falls Emirhan Mi ab 15:00 Istanbul bestätigt ({TZ})", 'r7-call-kuzgunlar', m=45, s=[
            "Um 12:00 in Gmail nachsehen: Hat Emirhan einen der drei Termine bestätigt? Nein: nichts tun, die Aufgabe rückt auf Fr 30.10. (10:00–13:00 Istanbul) oder Sa 31.10.",
            "Vorbereiten, 10 Minuten: Call-Leitfaden öffnen (pdf/NVL_Leitfaden_Fabrik-Calls.pdf). Der Satz „I'll decide on 29 October“ gilt nicht mehr. Sag stattdessen: „I'll decide early next week.“",
            "Anruf per WhatsApp an Emirhans Handy (Nummer aus seiner Mail-Signatur). Ruhiger Ort, Kopfhörer, Notizzettel. Ist das Netz in Zypern schlecht: vorher eine kurze Nachricht „calling in 5 minutes“.",
            "Diese 9 Punkte fragst du, in dieser Reihenfolge: 1) Price per pair at 100 and 75 pcs, EXW and DAP Berlin. 2) Development cost: digitizing, washed stitch-outs, proto (200 € + shipping?), tooling for button and rivets. 3) Who embroiders: name of the partner, on cut panels before sewing? Photos of earlier panel work. 4) Who washes, and can the wash keep seams and embroidery free of wash effects? 5) Dates: proto shipped by early December, PP by early January, production mid-February to 14 May. 6) Payment: 50/50, balance after the final inspection video. 7) A.TR on every shipment. 8) Ramadan 2027 and Kurban Bayramı: how many working days are lost? 9) Can you also make our zip hoodie (French Terry 380–450 g/m², printed velvet patch, screen print, embroidered rib)?",
            "Nichts zusagen. Am Ende: „Thank you. Please send the estimate in writing, I'll decide early next week.“",
            "Direkt danach 10 Minuten: Antworten ins Blatt „Fabriken“, Zeile Kuzgunlar. Notizen und Gefühl in drei Sätzen an Claude (Prompt unten).",
        ], f="der Call geführt ist und die 9 Antworten im Blatt „Fabriken“ stehen, oder klar ist, an welchem Tag er stattfindet.",
           p="Projekt Time Travel, Docket Rev. 7, W7: Ich habe mit Emirhan von Kuzgunlar telefoniert. Meine Notizen zu den 9 Punkten: [1–9]. Mein Gefühl: [3 Sätze]. Bewerte das gegen die Scorecard (Panel-Stickerei vor dem Nähen nachgewiesen, Preis ≤ 60 € grün, 61–63 € gelb, > 63 € rot, Termine, 50/50, A.TR). Was fehlt mir noch schriftlich, bevor ich am Di 03.11. entscheide? Schreib mir eine kurze Nachfass-Mail auf Englisch mit genau diesen offenen Punkten.",
           o=['gmail', 'sheets', {"n": "Call-Leitfaden (PDF im Repo)", "u": "https://github.com/ernest080809/email-bot/tree/main/novalife/time-travel/pdf", "h": "NVL_Leitfaden_Fabrik-Calls.pdf"}]),
        T('G', "Design-Inventur lesen: Stimmt jeder Status?", 'r7-inventur-lesen', m=30, s=[
            "Docket → Abschnitt „Design-Inventur“ öffnen. Dort steht jedes Design aller drei Teile: was entschieden ist, welche Datei gilt, was offen ist und wann es dran ist.",
            "Zeile für Zeile lesen. Bei jeder Zeile fragen: Stimmt der Status? Fehlt ein Teil, an das ich denke, zum Beispiel ein Sticker, eine Tüte, eine Karte im Paket, ein Profilbild?",
            "Alles, was falsch ist oder fehlt, als Liste an Claude (Prompt unten). Claude korrigiert die Inventur und hängt fehlende Teile in die Designwochen.",
        ], f="Claude deine Korrekturliste hat oder du „stimmt so“ geschrieben hast.",
           p="Projekt Time Travel, Design-Inventur (Docket Rev. 7). Korrekturen: [Zeile → was stimmt nicht]. Was fehlt: [..]. Bau die Inventur neu und sag mir, in welche Designwoche jedes neue Teil kommt, ohne dass das Design-Gate am So 29.11. rutscht.",
           o=['docket', 'claude']),
        T('D', "Bestandsaufnahme: Was aus W5 und W6 ist schon passiert?", 'r7-bestand-w5w6', m=15, s=[
            "Im alten Plan standen für 12.–25.10. viele Marketing-Aufgaben. Abgehakt hast du dort nichts, auch nicht das RL-Messen, das du gemacht hast. Ich weiß deshalb nicht, was wirklich passiert ist.",
            "Beantworte im Prompt unten jede Zeile mit ja, nein oder teilweise. Ehrlich, auch wenn es nein ist. Daraus baut Claude die Nachhol-Aufgaben vor dem Marketing-Start.",
        ], f="Claude die 14 Antworten hat.",
           p="Projekt Time Travel, Bestandsaufnahme W5/W6 (Docket Rev. 7). Je Zeile ja/nein/teilweise: 1) V001–V006 gepostet? Welche? 2) REWIND #01 (G-Klasse) gedreht oder gepostet? 3) Papiertest-Abend am 24.10.? 4) Steuerberater oder IHK: die 11 Fragen geklärt? 5) Datenschutzerklärung für Tally und „Bring 3“ ergänzt? 6) Tally-Umfrage angelegt? 7) „Bring 3 Freunde“ eingebaut? 8) Blätter „Netz“ und „Die ersten 35“ angelegt, wie viele Namen? 9) Netz-Runde 1 (15 Nachrichten) raus? 10) Gespräche geführt, wie viele? 11) Startseite als Warteliste live, wie viele bestätigte Adressen? 12) MEK-Besuch und Belegtabelle? 13) Bio und Highlight aktualisiert? 14) Follower TikTok und Instagram heute. Bau mir daraus die Nachhol-Aufgaben für W8–W11, nur was vor dem Marketing-Start am Mo 30.11. wirklich nötig ist.",
           o=['claude']),
    ]
    do = [
        N("Türkei: Nationalfeiertag (Cumhuriyet Bayramı). Kuzgunlar antwortet heute nicht."),
        T('D', "Patch D: Woher stammt das Baum-Bild?", 'r7-baum-herkunft', m=10, s=[
            "Seit 20.10. offen, und die Patch-Anfrage am Fr 06.11. hängt daran.",
            "Frage: Hast du das Baum-Bild selbst gezeichnet, aus einer KI, aus Canva oder von einer fremden Seite (Pinterest, Etsy, Stockfoto)?",
            "Eigenes Bild oder KI ohne fremde Vorlage: ok, der Patch geht so in die Anfrage.",
            "Fremde Vorlage oder unklar: Claude zeichnet bis Mi 04.11. eine eigene Fassung (Kreis, Stamm, Knotenfelder, „NL“, höchstens 4 Garnfarben). Eine Kopie auf 110 Patches kann ein Urheberrechtsproblem sein (keine Rechtsberatung).",
            "Antwort in einem Satz an Claude.",
        ], f="Claude weiß, woher das Bild stammt, und ob eine eigene Fassung nötig ist.", o=['claude']),
        board(1, "Etiketten", 'etiketten',
              "gedruckte Innenetiketten an Jeans (Nummer, Größe), gewebte Nackenlabels mit kleinem Symbol statt Schrift, Pflegeetiketten mit gutem Layout, Labels in Naturweiß mit Rot oder Kupfer.",
              "Soll das Nackenlabel von Zipper und Polo nur den vereinfachten Baum zeigen, oder Baum plus kleines „NL“?"),
    ]
    fr = [
        T('B', "Fabriken: LOGIC-Frist heute, DiZNEW abschließen", 'r7-fabrik-fristen', m=20, s=[
            "LOGIC (Łódź): Antwortfrist ist heute. In Gmail nachsehen. Antwort da: Prompt unten mit der Mail an Claude. Prüfpunkte vor jeder Zahlung: echte Fotos oder ein Video aus der Halle, ein Videocall, Firmenregister (CEIDG oder KRS) zur Adresse ul. Komunalna 15, Muster vor Anzahlung. Keine Antwort: einmal kurz nachfassen, Frist Di 03.11. 09:00.",
            "DiZNEW: Die Frist vom 27.10. ist ohne Preis verstrichen. Eine letzte Mail: „Please send sample cost and estimated bulk price by Monday 2 November, otherwise I will continue with other factories.“ Claude schreibt sie dir, wenn du willst.",
            "Kuzgunlar: Hat Emirhan auf Fr 10:00–13:00 Istanbul gelegt, führst du den Call heute (Aufgabe vom Mi).",
            "Stand aller drei ins Blatt „Fabriken“.",
        ], f="für LOGIC, DiZNEW und Kuzgunlar ein Stand mit Datum im Blatt „Fabriken“ steht.",
           p="Projekt Time Travel, Fabrikwahl Di 03.11. Hier ist die Antwort von LOGIC: [Mail]. Prüfe sie gegen unsere 5 Fragen (Stickerei-Partner, Wäscherei, Menge und Termin, Preis, Call) und die Prüfpunkte (Fotos, Videocall, Register CEIDG/KRS ul. Komunalna 15, Muster vor Anzahlung). Was ist belegt, was nur behauptet? Schreib mir die Antwort auf Englisch mit allem, was ich bis Mo 02.11. noch brauche.",
           o=['gmail', 'sheets', 'claude']),
        T('B', "Claude: Sweat-Fabriken Portugal und Druckereien für Baumwollsamt suchen lassen", 'r7-suche-lieferanten', m=10, s=[
            "Diese Recherche war für den 26.10. geplant und ist noch offen. Prompt unten an Claude, in einem Chat mit Websuche.",
            "Claude liefert bis So 01.11.: 4–6 Sweat-Hersteller in Portugal mit kleiner Mindestmenge, 3–5 Druckereien für bedruckten Baumwollsamt (Muster A4) und 2 Quellen für einen fertigen Achtstern-Anhänger aus Metall.",
            "Die Liste brauchst du am Do 05.11. (Zipper-Anfrage) und am Mo 09.11. (Samtprobe).",
        ], f="Claude die Suche hat.",
           p="Projekt Time Travel, Zipper NVL-TT-02 (Briefing rev6/research/zipper_briefing.md). Such mit Websuche: 1) 4–6 Hersteller in Portugal für Zip-Hoodies aus schwerem French Terry 380–450 g/m², eigener Schnitt, Mindestmenge 30–100, mit Kontaktseite. 2) 3–5 Druckereien in der EU, die Baumwollsamt (matt) digital bedrucken und ein A4-Muster verkaufen. 3) 2 Quellen für einen fertigen Achtstern-Anhänger aus Metall, etwa 25 mm, Antik-Kupfer, kleine Mengen. Je Treffer: Name, Website, Ort, Mindestmenge, was belegt ist und was nicht. Keine Adressen aus Verzeichnissen kopieren, nur von der eigenen Seite des Anbieters.",
           o=['claude']),
        board(2, "Hangtag, Karte und Verpackung", 'hangtag',
              "Hangtags aus dickem Recyclingkarton (300 g), gefaltete Karten mit Bedeutung oder Zeichnung innen, Versandkartons mit Stempel statt Druck, Seidenpapier, Aufkleber zum Verschließen, Dankeskarten. Gern Denim-Marken (Kapital, Story mfg., Evisu), aber auch kleine Labels.",
              "Kommt die Bedeutung der Muster auf eine gefaltete Karte am Hangtag oder auf eine lose Karte im Paket?"),
    ]
    sa = [
        board(3, "Polo", 'polo',
              "weiße Piqué-Polos mit kleinem gesticktem Brustlogo (Ralph Lauren, Lacoste, aber auch kleine Marken), Muster unter dem Kragen, bestickte oder gewebte Bänder an Bündchen und Kragen, Details hinten am Kragen.",
              "Willst du das Muster unter dem Kragen und an den Bündchen wirklich, oder reicht das Brustlogo, damit das Polo leicht bleibt?"),
        board(4, "Website und Content-Look", 'website',
              "Shop-Startseiten kleiner Modemarken, die du gut findest; Produktseiten mit großen Nahaufnahmen; Video-Cover und Untertitel-Stile auf TikTok und Reels, die du gern ansiehst; Schriften für „TIME TRAVEL“.",
              "Soll die Seite eher wie ein Archiv wirken (ruhig, hell, Papier) oder wie ein Film (dunkel, groß, bewegt)?"),
    ]
    so = [
        board(5, "Zipper-Zubehör und Marke", 'zubehoer',
              "Zipper-Anhänger aus Metall, Kordelenden und Ösen in Antik-Kupfer, Reißverschlüsse in Dunkel oder Antik, dazu dein Novalife-Schriftzug in allen Varianten, die es schon gibt (Bleach-Linie, Instagram, alte Etiketten).",
              "Welcher Novalife-Schriftzug ist der echte? Schick ein Foto oder eine Datei."),
        T('D', "Design-Suche abschließen: Lücken-Liste an Claude", 'r7-suche-abschluss', m=20, s=[
            "Prüfen: 5 Boards fertig, Baum-Herkunft geklärt, Bestandsaufnahme W5/W6 geschickt, Inventur gelesen.",
            "Prompt unten an Claude. Claude baut daraus bis Mo 02.11. den Plan der Designwochen: wer wann welchen Entwurf liefert.",
            "Zurück in Berlin? Dann heute Abend 15 Minuten: Kapuze abpausen (Anleitung Seite 1 des Papiertest-PDF) und auf dem Etikett des RL-Zippers Material und Gewicht nachsehen. Sonst am Mo 02.11. mit dem Papiertest.",
        ], f="Claude alle fünf Boards, die Baum-Antwort und die Bestandsaufnahme hat.",
           p="Projekt Time Travel, Ende der Design-Suche (Docket Rev. 7, So 01.11.). Boards: [5 Links oder Screenshots]. Baum-Herkunft: [..]. Bestandsaufnahme W5/W6: [..]. Was in der Inventur noch fehlt: [..]. Plane mir die Designwochen W8–W11 so, dass bis So 29.11. alles final ist: Etiketten, Hangtag und Karte, Verpackung, Polo, Website-Look, Content-Look, Zipper-Zubehör, Knopf-Prägung, Patch D. Für jeden Entwurf: wann du lieferst, wann ich wähle, wann es an Fabrik oder Lieferant geht.",
           o=['claude']),
        T('A', "Wochenreview W7: Design-Suche und Fabrik-Stand", 'r7-review-w7', m=15, s=[
            "Drei Zeilen an Claude: Was ist diese Woche fertig geworden? Was ist liegen geblieben? Wann bist du zurück in Berlin?",
            "Fabrik: Hat Kuzgunlar geschätzt? Hat LOGIC geantwortet? Kein Preis bis Mo 02.11. 18:00: Die Fabrikwahl rückt auf Fr 06.11., alles Weitere um drei Tage.",
        ], f="Claude die drei Zeilen und den Fabrik-Stand hat.", o=['claude']),
    ]
    return week(7, "2026-10-26", "D1",
                "Design-Suche: jedes Design finden, das noch fehlt, Fabrik-Call führen, Stand aus W5/W6 klären",
                [("Design-Suche", "5 Boards mit je 8–12 Referenzen"), ("Fabrik", "Call Kuzgunlar geführt, LOGIC und DiZNEW mit Stand"),
                 ("Patch D", "Herkunft des Baum-Bildes geklärt"), ("Bestand", "W5/W6 an Claude")],
                [mo, di, mi, do, fr, sa, so])


def w08():
    DROP('w7d0t1', 'neu geschrieben als r7-eori (jetzt Di 03.11., auch bei China).')
    DROP('w7d4t0', 'neu geschrieben als r7-eori-check (Fr 06.11.).')
    DROP('w7d4t1', 'neu geschrieben als r7-gate-proforma (Fr 06.11.).')
    DROP('w7d3t8', 'neu geschrieben als r7-fabrik-wahl (Di 03.11., ohne Calls vom 21.–23.10., die es nicht gab).')
    DROP('w8d0t0', 'neu geschrieben als r7-entwicklung-zahlen (Do 05.11., Validierung entfällt vor dem Marketing).')
    DROP('w7d2t0', 'neu geschrieben als r7-patch-anfrage (Fr 06.11., ohne Chenille, mit eigenem Baum).')
    DROP('w8d6t0', 'ersetzt durch r7-review-w8 (Design-Review).')
    DROP('w8d6t1', 'ersetzt durch r7-gate-w8 (Design-Gate der Woche).')
    DROP('w8d5t0', 'B2-Band (ohne Weiß, 22.10.) und Namen nach außen sind entschieden; Sprache und Liefergebiet entscheidest du im Marketing (r7-sprache, W14).')

    mo = [
        O('w7d2t2', id='r7-papiertest-zipper', t="Papiertest Zipper auf dem RL und Kapuze abpausen", m=75,
          s=["Noch in Zypern? Dann rückt diese Aufgabe auf deinen ersten Abend in Berlin. Alles andere in W8 geht auch von unterwegs.",
             "Papiertest-PDF (pdf/NVL-TT-02_Papiertest_Zipper.pdf, 11 Seiten) im Copyshop mit 100 % drucken, nicht „an Seite anpassen“. Das Quadrat auf Seite 1 muss genau 5 × 5 cm messen.",
             "Teppich A in S (21 cm), M (25 cm) und L (29 cm) ausschneiden. Die Hälften links und rechts direkt an den Reißverschluss legen, Oberkante 6 cm unter dem Anfang des Reißverschlusses, mit Malerkrepp fixieren.",
             "Je Größe zwei Fotos: von vorn aus 2 m und angezogen im Spiegel.",
             "Rückendruck B in fein und doppelt an der Mittellinie zusammenkleben, Oberkante 2 cm unter der Kapuzennaht. Erst die Kapuze darüberklappen: Es darf nichts vorschauen. Dann Kapuze hoch, Foto.",
             "Stern C ausschneiden und hinten links auf die Saumrippe legen, Mitte 20 cm von der hinteren Mitte. Foto.",
             "Abdruck: zwei A4-Blätter zusammenkleben, oben auf den Rücken legen, Kapuze glatt darüber, mit Bleistift an der Kante der Kapuze entlangfahren. Blatt flach fotografieren, das 5-cm-Quadrat daneben.",
             "Etikett des RL-Zippers: Material und, falls angegeben, Gewicht in den Messbogen (Feld 22 und Material).",
             CAPTURE + "Zeitraffer von oben beim Ausschneiden (Handy auf Bücherstapel), 5 s Hände beim Kleben am Reißverschluss, Spiegel-Drehung mit Teppich M, Kapuze hoch mit Papier darunter. Alles ins Album „TT Vorrat“. Daraus wird V201.",
             "Fotos, Abdruck und deine Wahl an Claude: Teppichgröße S, M oder L, Rückendruck fein oder doppelt, Stern so oder anders."],
          f="Fotos, Abdruck und deine drei Wahlen bei Claude sind und die Clips im Album „TT Vorrat“ liegen.",
          o=[LINKS['messbogen'], LINKS['claude']]),
        T('R', "Steuer vor der Fabrikwahl: Was ändert Türkei, Polen oder China?", 'r7-steuer-fabrik', m=20, s=[
            "Nur falls die Steuerfragen aus W5/W6 noch offen sind (Bestandsaufnahme). Sonst abhaken.",
            "Kern: Bist du Kleinunternehmer? Aus der Türkei und aus China kommt bei der Einfuhr Einfuhrumsatzsteuer dazu, rund 19 % auf Ware plus Fracht. Als Kleinunternehmer bekommst du sie nicht zurück. Aus Polen kommt keine Einfuhrsteuer (EU).",
            "Prompt unten an Claude: Claude rechnet die drei Fälle für 100 Paar durch, damit die Scorecard morgen die echte Zahl hat. Keine Steuerberatung, im Zweifel bestätigt die IHK-Beratung.",
        ], f="Claude den Stand hat und die Steuer-Spalte für die Scorecard steht.",
           p="Projekt Time Travel, Fabrikwahl Di 03.11. Mein Steuerstand: Kleinunternehmer [ja/nein/weiß nicht], Gewerbe [nein], Steuerberater [Antworten oder „keine“]. Rechne für 100 Jeans je Fall Türkei (DAP Berlin, Zollunion mit A.TR), Polen (EU) und China (Zoll 12 % plus Einfuhrumsatzsteuer): was ich zusätzlich zahle, wann und an wen, und was das für die Schwellen bedeutet. Markiere klar, was belegt ist und was du annimmst.",
           o=['claude']),
    ]
    di = [
        T('D', "FABRIK WÄHLEN: Scorecard mit Preis, Stickerei, Steuer und Zahlung", 'r7-fabrik-wahl', m=45, s=[
            "Kein schriftlicher Preis bis heute 09:00 von Kuzgunlar oder LOGIC: heute nicht wählen. Die Wahl rückt auf Fr 06.11., alle Folgeaufgaben um drei Tage. Claude hängt sie um.",
            "Alles in einen Chat mit dem Prompt unten: Antworten von Kuzgunlar (Call und Schätzung), LOGIC, DiZNEW, Steuerstand von gestern.",
            "K.-o. vor jedem Preis: Stickerei auf den Zuschnitten vor dem Nähen, belegt mit Fotos früherer Arbeit. Kein Vermittler ohne genannte Fabrik. Bei LOGIC zusätzlich: echte Fotos oder Video aus der Halle und Registereintrag.",
            "Scorecard: Preis je Paar bei 100 und 75 inklusive Stickerei, ohne Patch D (≤ 60 € grün, 61–63 € gelb, > 63 € rot). Termine Proto bis Anfang Dezember, PP bis Anfang Januar. Zahlung 50/50. Steuer und Zoll aus der Rechnung von gestern. Kommunikation. Ramadan und Feiertage bis Mitte Mai.",
            "Nr. 1 wählen, Nr. 2 als Reserve. Nr. 2 bekommt keine Absage: Sie ist dein Weg, falls die Stickproben am Di 24.11. durchfallen.",
            "Entscheidung ins Blatt „Fabriken“: Nr. 1, Nr. 2, Datum, Grund in einem Satz. Danach Zusage an Nr. 1 in zwei Sätzen: „We'd like to work with you. Our terms follow tomorrow.“",
            CAPTURE + "Bildschirmaufnahme der Scorecard (Namen und Preise schwärzen), 10 s. Wird Teil von V205.",
        ], f="Nr. 1 und Nr. 2 im Blatt „Fabriken“ stehen und Nr. 1 die Zusage hat, oder die Wahl mit Grund auf Fr 06.11. verschoben ist.",
           p="Projekt Time Travel, Docket Rev. 7, Di 03.11.: Ich wähle heute meine Jeansfabrik. Anbei: Kuzgunlar (Call-Notizen und Schätzung), LOGIC (Antwort), DiZNEW (Stand), meine Steuerrechnung von gestern: [ANHÄNGE]. Mach eine Scorecard: K.-o. Panel-Stickerei vor dem Nähen nachgewiesen und kein Vermittler; dann Preis je Paar inkl. Stickerei ohne Patch D bei 100 und 75 mit Ampel (≤ 60 € grün, 61–63 € gelb, > 63 € rot), Termine (Proto Anfang Dezember, PP Anfang Januar, fertig bis 14.05.2027), Zahlung 50/50, Steuer und Zoll, Kommunikation, Ramadan und Feiertage, A.TR. Sag mir ehrlich, welche du nehmen würdest, welche Nr. 2 sein soll und was ich morgen in der Verhandlung schriftlich brauche.",
           o=['sheets', 'gmail', 'claude']),
        T('A', "EORI-Nummer beantragen, nur bei Türkei oder China", 'r7-eori', m=30, s=[
            "Polen gewählt: entfällt (EU). Notiz „EORI entfällt (PL)“ oben ins Blatt „Ausgaben“.",
            "Türkei oder China: zoll.de öffnen, Seite „EORI-Nummer beantragen“. Laut Recherche online und kostenlos, Dauer meist 1–2 Wochen (ungeprüft).",
            "Noch kein Gewerbe: Beim Antrag fragt der Zoll danach. Ob es als Privatperson für Muster reicht, klärst du in der Zoll-Auskunft (Telefon auf zoll.de). Reicht es nicht: Die Fabrik schickt Muster DDP (sie verzollt selbst).",
            "Die Nummer brauchst du für das Proto Anfang Dezember, das PP und die Lieferung. Bestätigung als Notiz ins Blatt „Ausgaben“.",
        ], f="der Antrag gestellt ist oder „entfällt“ im Blatt „Ausgaben“ steht.",
           o=[{"n": "Zoll · EORI-Nummer", "u": "https://www.zoll.de", "h": "Seite „EORI-Nummer beantragen“ suchen"}, 'sheets']),
    ]
    mi = [
        O('w7d4t4', id='r7-konditionen', t="Konditionen verhandeln, Proforma für die Entwicklung anfordern",
          rep=[("Docket W7, Fr 30.10.", "Docket Rev. 7, Mi 04.11."), ("Bei Türkei bis Mo 02.11.", "Ziel: Proforma bis Do 05.11."),
               ("bei Türkei spätestens 12:00 selbst senden", "bis 12:00 selbst senden"),
               ("Proto bis 30.11., PP bis 04.01.", "Proto verschickt bis Fr 04.12., PP verschickt bis Fr 08.01."),
               ("proto shipped by 30 Nov 2026, PP shipped by 4 Jan 2027", "proto shipped by 4 Dec 2026, PP shipped by 8 Jan 2027"),
               ("Digitizing aller 5 Elemente inklusive", "Digitizing aller 4 Stickzonen inklusive"),
               ("digitizing of all 5 elements included", "digitizing of all 4 embroidery zones (A, E, B2, C) included"),
               ("at the latest 24 March 2027", "at the latest 26 May 2027"),
               ("[BEI PORTUGAL: delivered to Berlin]", "[BEI POLEN: delivered to Berlin]"),
               ("Rest „nach Freigabe des Endkontroll-Videos, spätestens 26.05.“", "Rest nach Freigabe des Endkontroll-Videos, spätestens 26.05."),
               ("Preis 75/100 schriftlich bis 15.02.", "Preis 75/100 schriftlich, gültig bis 15.02."),
               ("valid until 1 February 2027", "valid until 15 February 2027"),
               ("[NUR TÜRKEI: every shipment", "[NUR TÜRKEI ODER CHINA: every shipment"),
               ("Bei Türkei: jede Sendung mit A.TR", "Bei Türkei: jede Sendung mit A.TR")]),
        O('w7d4t5', id='r7-absagen', rep=[("May I come back to you by 17 November?", "May I come back to you by 24 November?"), ("„Reserve bis 17.11.“", "„Reserve bis 24.11.“")]),
        T('G', "Zipper: Teppichgröße, Mustergröße und Rückendruck festlegen", 'r7-zipper-papier-wahl', m=20, s=[
            "Claude hat bis heute aus deinen Fotos und dem Abdruck den echten Umriss gebaut und den Rückendruck B neu gezeichnet. Du bekommst ein PDF mit Ansicht in 1:1.",
            "Prüfen: Liegt der Druck rundum 2 cm in der Kapuze? Endet die Spitze sauber? Passt Band A oben am Hals?",
            "Entscheiden und Claude schreiben: Teppich S, M oder L · Rückendruck fein oder doppelt · Stern bleibt bei 20 cm.",
            "Offen seit 24.10.: Dürfen die Kordeln über dem Teppich hängen? Ja oder nein.",
        ], f="Teppichgröße, Mustergröße, Stern und Kordel-Antwort bei Claude sind.",
           p="Projekt Time Travel, Zipper NVL-TT-02: Meine Wahl nach dem Papiertest: Teppich [S/M/L], Rückendruck B [fein/doppelt], Stern [so/anders: ..], Kordeln über dem Teppich [ja/nein]. Trag das ins Briefing ein, bau die Druckdateien für Teppich und Rückendruck in Originalgröße und sag mir, was davon ins Tech Pack Zipper muss.",
           o=['claude']),
    ]
    do = [
        T('B', "Proforma prüfen und Entwicklung bezahlen", 'r7-entwicklung-zahlen', m=30, s=[
            "Kassen-Check zuerst: Budget 4.500 €. Steht die Entwicklung im Blatt „Kasse“? Zahlst du sie, bleiben mindestens 300 € Puffer? Sonst erst mit Claude rechnen.",
            "Proforma Zeile für Zeile: Digitizing, gewaschene Stickproben, Proto W34 komplett, Expressversand. Abweichung über 10 % gegen die Zahl im Call: erst nachfragen, dann zahlen.",
            "Bankdaten-Regel: Gezahlt wird nur auf das Konto der ersten Proforma. Kommt per Mail ein neues Konto, zahlst du nicht und rufst die Fabrik an (Nummer aus dem Blatt, nie aus der neuen Mail).",
            "Banking-App → Überweisung (Ausland in EUR). Verwendungszweck: Proforma-Nummer + „Novalife NVL-TT-01 development“.",
            "Die Überweisung ist dein Test fürs Ausland: Betrag, Gebühr, Datum ins Blatt „Kasse“. Spalte „Gutschrift“ füllst du, wenn die Fabrik den Eingang bestätigt.",
            "Beleg als PDF an die Fabrik: „Payment for proforma [no.] sent today. Please confirm receipt.“",
        ], f="die Entwicklung auf das Konto der ersten Proforma bezahlt ist, der Beleg bei der Fabrik liegt und Gebühr und Datum im Blatt „Kasse“ stehen.",
           o=['sheets', 'gmail']),
        O('w7d4t6', id='r7-zipper-anfrage', t="Zipper-Anfrage prüfen und senden: gewählte Jeansfabrik und Portugal",
          s=["Claude legt die Mails als Entwürfe in Gmail an, auf Englisch, mit Briefing, Maßtabelle S–XL, Papiertest-Fotos und den Druckdateien von gestern. Nichts geht ohne dein Ja raus.",
             "Empfänger: deine gewählte Jeansfabrik (zusammen mit den Konditionen) und 3–4 Sweat-Hersteller aus Claudes Portugal-Liste vom So 01.11.",
             "Gefragt wird: Preis bei 30, 50 und 100 Stück, Muster bis Mitte Dezember, eigener Schnitt nach unserer Maßtabelle, schwerer French Terry 380–450 g/m² in Ecru, dunkler Metall-Reißverschluss mit Kinnschutz, Samt-Teppich aufnähen vor dem Reißverschluss, Siebdruck unter der Kapuze, Stern auf der Saumrippe, Kordeln mit Antik-Kupfer.",
             "Antwortfrist in der Mail: Do 12.11. Die Wahl ist Mo 16.11.",
             "Entwürfe lesen. Passt alles: in Gmail selbst senden oder Claude im Chat „senden“ schreiben.",
             "Ins Blatt „Fabriken“, Abschnitt Zipper: wer angefragt ist und wann."]),
    ]
    fr = [
        T('B', "Dateien an die Fabrik, Shade Card und 3 Lab Dips anfordern", 'r7-dateien-fabrik', m=45, s=[
            "Paket: Tech Pack v1.0 (oder v1.1, falls Claude die Call-Antworten eingearbeitet hat), Druckvorlage 1:1 v1.9, SVG der vier Stickzonen, Wash Reference Sheet, Knopf-Datei (siehe nächste Aufgabe).",
            "Fehlt die Fassung mit den Call-Antworten: Prompt unten an Claude, dann erst senden.",
            "Mail an die Fabrik, eine Mail, Anhänge als ZIP über 20 MB: Proto W34, Garnfarben entscheiden wir an den Stickproben, bitte jedes Element in den vorgeschlagenen Farben sticken und die Garnnummern nennen.",
            "Anfordern: Shade Card des Stoffs und 3 Lab Dips (Ziel, heller, dunkler) mit L*-Werten der Fabrik. Ziel L* 34–40 ±2.",
            "Termine schriftlich bestätigen lassen: Digitizing-Vorschau bis Do 12.11., Fotos der gewaschenen Stickproben bis Fr 20.11., Proto verschickt bis Fr 04.12.",
            "Fragen, ob du die Digitizing-Vorschau und Fotos aus der Halle im Video zeigen darfst (für den Content ab Dezember).",
            "Sendedatum und Uhrzeit ins Blatt „Fabriken“.",
        ], f="die Fabrik alle Dateien hat, Shade Card und Lab Dips angefordert sind und die Termine schriftlich bestätigt werden.",
           p="Projekt Time Travel, Docket Rev. 7, Fr 06.11. Mach mir aus Tech Pack v1.0 die nächste Fassung mit diesen Antworten aus Call und Verhandlung: [Antworten]. Ergänze Lab Dips (Ziel, heller, dunkler, L* 34–40 ±2), Shade Card, Termine (Digitizing-Vorschau 12.11., Stickproben-Fotos 20.11., Proto verschickt 04.12., PP verschickt 08.01.). Exportiere die Elemente als SVG in Originalgröße und schreib mir die Begleitmail auf Englisch, höchstens 150 Wörter.",
           o=['gmail', 'sheets', 'claude']),
        T('G', "Knopf 20 mm: Achtstern-Prägung freigeben", 'r7-knopf', m=15, s=[
            "Claude zeichnet die Prägung: Achtstern aus 8 Rauten wie C, für einen 20-mm-Knopf in Antik-Kupfer, Vorder- und Seitenansicht mit Maßen.",
            "Prüfen: Liest sich der Stern auf 20 mm noch? Linien nicht dünner als 0,5 mm (Prägung, Schätzung).",
            "Freigeben und mit den Dateien an die Fabrik. Fragen: Werkzeugkosten, Mindestmenge, Muster des Knopfs vor dem Proto?",
        ], f="die Knopf-Datei freigegeben bei der Fabrik liegt und die Frage nach Werkzeug und Mindestmenge gestellt ist.",
           p="Projekt Time Travel: Zeichne die Prägung für den Jeans-Knopf NVL-TT-01: 20 mm, Antik-Kupfer, nickelfrei, Achtstern aus 8 Rauten wie Element C (Fugen proportional), druckfertig als SVG und PDF mit Vorder- und Seitenansicht und Maßen. Sag mir die kleinste Linienstärke und ob der Stern auf 20 mm lesbar bleibt.",
           o=['claude']),
        T('B', "Patch-Hersteller anfragen: 3 Anbieter für Patch D", 'r7-patch-anfrage', m=45, s=[
            "Stand: Patch D ist 80 × 71 mm, zwei Lagen mit Rückwand, 4 versteckte Druckknöpfe (die setzt die Jeansfabrik), abnehmbar, wird nicht mitgewaschen. Keine Lasche. Kein Chenille mehr, der Zipper-Teppich ist bedruckter Samt.",
            "Baum-Datei: dein eigenes Bild oder Claudes eigene Fassung (Antwort vom Do 29.10.). Nie eine fremde Vorlage.",
            "Fragt deine Jeansfabrik den Patch selbst an (Call-Antwort)? Trotzdem 3 Angebote als Vergleich.",
            "Suchen: „Aufnäher sticken lassen ab 50 Stück“, „gestickte Patches Kleinauflage“, „custom embroidered patches low minimum Europe“. Nur Anbieter mit Nahaufnahmen fein gestickter Mehrton-Patches auf der eigenen Website. Kontakt nur von dort.",
            "Prompt unten an Claude, dann an 3 Anbieter senden. Anhang: Druckvorlage v1.9 Seite 5.",
            "Ins Blatt „Patches“: Anbieter, Website, Kontaktweg, Datum. Antwortfrist Do 12.11.",
        ], f="3 Patch-Anfragen raus sind und im Blatt „Patches“ stehen.",
           p="Projekt Time Travel, Docket Rev. 7, Fr 06.11.: Schreib mir eine Patch-Anfrage auf Englisch, in die ich nur den Anbieternamen eintrage. Patch D Lebensbaum, 80 × 71 mm (Seiten 60 mm, oben und unten je 5,5 mm gewölbt), vorgeschrumpftes Naturleinen, Kante umgeschlagen und gesteppt, feste Einlage, höchstens 4 Garnfarben (Gold, Kupfer, Dunkelbraun, Rot), Linien mindestens 0,8 mm, Einrollungen mindestens 2,5 mm. Dazu eine Rückwand gleicher Größe, nur oben und unten in der Mitte auf 30 mm mit dem Vorderteil verbunden, seitlich offen. Die Jeansfabrik setzt 4 Druckknöpfe in die Rückwand, sie muss sie halten. Der Patch wird separat von Hand bei 30 °C gewaschen. Mengen: 3 Muster, dann 110 Stück. Fragen: Preis bei 50/110/200, Musterpreis und -zeit, Produktionszeit, minimale Linienstärke, vorgeschrumpftes Leinen ja/nein. Kurz.",
           o=['sheets', 'gmail', 'claude']),
        T('A', "EORI-Stand und Proforma-Gate", 'r7-gate-proforma', m=10, s=[
            "EORI (nur Türkei oder China): Ist der Antrag vom Di eingegangen? Stand mit Datum ins Blatt „Ausgaben“.",
            "Proforma da und 50/50 steht drin? Konto notiert? Ohne Proforma keine Zahlung.",
        ], f="EORI-Stand und Proforma-Stand mit Datum in den Blättern stehen.", o=['sheets']),
    ]
    sa = [
        T('G', "Etiketten: Claudes Entwürfe ansehen und wählen", 'r7-etiketten-wahl', m=30, s=[
            "Claude liefert aus deinem Board 1 zwei Entwürfe je Etikett: Innenetikett Jeans (gedruckt: NOVALIFE · NVL-TT-01 · Größe · Nr. 0XX/100, Rückseite Pflege), Nackenlabel Zipper und Polo (gewebt, vereinfachter Baum), Pflegeetikett Zipper (Material, Pflege, Größe mit Brustweite, Nummer, Herstellerangabe).",
            "Je Etikett einen Entwurf wählen oder sagen, was anders sein soll.",
            "Text prüfen: „100 % Baumwolle“, Pflegesymbole in der Reihenfolge Waschen, Bleichen, Trocknen, Bügeln, Reinigung; „Vor dem ersten Tragen separat und auf links waschen. Patch vor dem Waschen abnehmen. Goldfäden nicht abschneiden.“ Herstellerangabe bleibt bis Januar ein Platzhalter.",
        ], f="je Etikett ein Entwurf gewählt ist oder Claude deine Änderungen hat.",
           p="Projekt Time Travel: Entwirf mir aus Board 1 („TT · Etiketten“) je zwei Entwürfe für: 1) Innenetikett Jeans, gedruckt, laut Tech Pack v1.0 Seite 12; 2) Nackenlabel Zipper und Polo, gewebt, vereinfachter Baum (Kreis, Stamm, 5–7 Äste, keine Knoten), etwa 40 × 20 mm; 3) Pflegeetikett Zipper laut Briefing (Material, Pflege, Größe mit Brustweite, Nummer, Herstellerangabe). Regeln: nie „authentisch“, „entworfen in Berlin“, Knallrot, Naturweiß, Antik-Kupfer. PDF und SVG mit Maßen.",
           o=['claude']),
        T('G', "Polo-Fragerunde 1: Weg, Schnitt, Farbe", 'r7-polo-1', m=30, s=[
            "Im Chat „Polo klären, Runde 1“ schreiben. Claude fragt, du antwortest kurz, so wie beim Zipper am 23.10.",
            "Runde 1: Eigener Schnitt aus der Zipper-Fabrik oder Blank plus Berliner Sticker? Weiß oder Naturweiß? Passform? Vorbestellbar ab 01.02. oder erst im Drop?",
            "Deinen Canva-Entwurf 2 (Kreuzstich-Baum) und Board 3 mitschicken.",
        ], f="Runde 1 beantwortet ist.", o=['claude']),
    ]
    so = [
        T('A', "Wochenreview W8: Design und Fabrik", 'r7-review-w8', m=20, s=[
            "Drei Zeilen an Claude: Was ist fertig? Was hängt? Was brauchst du von Claude?",
            "Blatt „Kasse“: Entwicklung bezahlt, was bleibt bis zur Anzahlung im Februar?",
        ], f="Claude die drei Zeilen hat.", o=['claude', 'sheets']),
        T('D', "Gate W8: Fabrik gewählt · Entwicklung bezahlt · Papiertest durch · Etiketten gewählt", 'r7-gate-w8', m=10, s=[
            "Grün: Alle vier stehen. Weiter wie geplant.",
            "Fabrik noch nicht gewählt: Die Wahl ist spätestens Fr 06.11. gefallen, sonst sagt Claude dir, was am Proto-Termin rutscht.",
            "Papiertest noch nicht gemacht (noch nicht in Berlin): Er ist Pflicht vor dem Tech Pack Zipper am Do 12.11.",
            "Ergebnis ins Blatt „Gates“.",
        ], f="das Ergebnis im Blatt „Gates“ steht.", o=['sheets']),
    ]
    return week(8, "2026-11-02", "D2",
                "Design fertig, Teil 1: Zipper-Papiertest, Jeansfabrik wählen und bezahlen, Etiketten, Knopf, Patch-Anfrage",
                [("Fabrik", "gewählt Di 03.11. (spätestens Fr 06.11.)"), ("Entwicklung", "bezahlt aufs Konto der ersten Proforma"),
                 ("Zipper", "Papiertest, Abdruck, Größe gewählt"), ("Etiketten", "je ein Entwurf gewählt")],
                [mo, di, mi, do, fr, sa, so])


def w09():
    DROP('w8d0t3', 'neu geschrieben als r7-samtprobe (Mo 09.11., mit Claudes Druckerei-Liste).')
    DROP('w8d2t0', 'neu geschrieben: Etiketten (r7-etiketten-wahl), Hangtag und Karte (r7-hangtag), Patch-Datei (r7-patch-anfrage). Nummer steht seit 23.10. auf dem Innenetikett, nicht auf dem Hangtag.')
    DROP('w8d3t0', 'neu geschrieben als r7-etiketten-fabrik (Mi 11.11.): Knopf ist 20 mm Achtstern in Antik-Kupfer, nicht „NOVALIFE“ 17 mm Messing; Polo und Zipper laufen nicht mehr über den Berliner Sticker.')
    DROP('w9d6t0', 'ersetzt durch r7-review-w9.')
    DROP('w9d6t1', 'ersetzt durch r7-gate-w9.')

    mo = [
        T('B', "Samtprobe bestellen: bedruckter Baumwollsamt, etwa A4", 'r7-samtprobe', m=20, s=[
            "Druckerei aus Claudes Liste vom So 01.11. nehmen. Druckfertige Datei: Teppich A in deiner Größe vom Mi 04.11. (kommt von Claude, im Maßstab 1:1).",
            "Baumwollsamt, matt, ein Stück etwa A4. Preis, Lieferzeit, Farbtreue (Muster vorher als Proof?) notieren.",
            "Beleg ins Blatt „Ausgaben“. Wenn die Probe da ist: Farben bei Tageslicht, Flor, mit dem Daumen reiben, einmal bei 30 °C waschen, Fotos an Claude.",
            CAPTURE + "Auspacken der Probe filmen, wenn sie kommt: Hand fährt über den Flor, Makro, Gegenlicht.",
        ], f="die Probe bestellt ist und der Beleg im Blatt „Ausgaben“ liegt.", o=['sheets', 'claude']),
        T('G', "Hangtag und Bedeutungskarte: Claudes Entwürfe wählen", 'r7-hangtag', m=30, s=[
            "Claude liefert aus Board 2 zwei Entwürfe: Hangtag (Recyclingkarton 300 g, Kordel, ohne Nummer, die Nummer steht auf dem Innenetikett) und gefaltete Karte „Bedeutung innen“ (V6).",
            "Auf der Karte: kleine Zeichnung der Jeans mit A, E, B2, C und D, je ein Satz. Nur Motive mit Beleg bekommen eine Bedeutung. „Aus drei Metern ein paar Punkte. Aus dreißig Zentimetern ein Uhrwerk.“ Sprachregel: Das Muster ist das Subjekt, nie „authentisch“, nie „slawisch“, nach außen „Kreuzstich-Band“ und „Achtstern“.",
            "Pflicht auf dem Hangtag: „Patch separat von Hand waschen, 30 °C, nicht auswringen, flach trocknen, erst trocken wieder anknöpfen.“",
            "Einen Entwurf wählen oder Änderungen an Claude. Gedruckt wird im Februar (W24), du druckst selbst.",
        ], f="Hangtag und Karte gewählt sind oder Claude deine Änderungen hat.",
           p="Projekt Time Travel: Entwirf aus Board 2 („TT · Hangtag, Karte und Verpackung“) zwei Entwürfe für Hangtag und Bedeutungskarte der Jeans NVL-TT-01 (V6 aus dem Design-Review). Hangtag ohne Nummer, mit Patch-Pflegetext. Karte gefaltet, außen „TIME TRAVEL · NVL-TT-01“, innen die Jeans als Linienzeichnung mit A, E, B2, C, D und je einem Satz, Bedeutungen nur für Motive mit Beleg in der Belegtabelle [Motive mit Beleg oder „keine Tabelle“]. Sprachregeln wie im Docket. Maße, Papier, Druckweg (Copyshop oder Online-Druckerei), PDF druckfertig mit Beschnitt.",
           o=['claude']),
    ]
    di = [
        T('G', "Polo-Fragerunde 2: Logo, Kragen, Bündchen, Knöpfe", 'r7-polo-2', m=30, s=[
            "Im selben Chat weiter. Runde 2: Größe und Lage des Kreuzstich-Baums (Claude zeichnet ihn neu, nicht deinen Anhänger kopieren), Muster unter dem Kragen ja oder nein, Webband oder Stickerei, Bündchen, Ähren hinten am Kragen ja oder nein, Knöpfe normal oder mit Achtstern.",
            "Ehrlicher Hinweis von Claude: Jedes Extra kostet Geld oder Mindestmenge. Das Polo soll das leichte Einstiegsteil bleiben.",
        ], f="Runde 2 beantwortet ist.", o=['claude']),
        O('w9d2t0', id='r7-stoffoptionen', rep=[("angefragt am 11.11.", "angefragt am 10.11."), ("Bewertung mit den Stickproben in W10.", "Bewertung am Mi 25.11. mit den Lab Dips.")]),
    ]
    mi = [
        T('B', "Etiketten freigeben und an die Fabrik", 'r7-etiketten-fabrik', m=30, s=[
            "Gewählte Entwürfe vom Sa 07.11. in der Endfassung von Claude prüfen: Text, Pflegesymbole, Größe, Nummernfeld „Nr. ___/100“.",
            "An die Jeansfabrik: Innenetikett (gedruckt) mit Bitte um Preis und Muster vor dem Proto. Die Nummernliste je Größe schickst du mit der Bestellung im Februar.",
            "An die Zipper-Anfrage nachreichen: Nackenlabel und Pflegeetikett Zipper.",
            "Antworten und Preise ins Blatt „Fabriken“.",
        ], f="die Fabrik die Etiketten-Dateien hat und die Preisfrage gestellt ist.", o=['gmail', 'sheets']),
        T('W', "Website: Bestandsaufnahme Shopify", 'r7-web-bestand', m=20, s=[
            "Shopify Admin öffnen. Notieren: Tarif und nächste Abbuchung, Domain verbunden ja oder nein, welches Theme, ist die Startseite als Warteliste live, wie viele Kunden mit „E-Mail-Marketing: abonniert“, Double-Opt-in an oder aus, Quellen-Tags (?ref=) vorhanden.",
            "Screenshot von Startseite und Formular an Claude. Claude sagt dir, was davon bis zum Marketing-Start am Mo 30.11. fehlt.",
        ], f="Claude die 7 Punkte und die Screenshots hat.", o=['shopify', 'claude']),
    ]
    do = [
        O('w9d0t0', id='r7-digitizing', t="Digitizing-Vorschau prüfen: Stichzahl, Fadenschnitte, Farbwechsel",
          rep=[("Docket W9, Mo 09.11.", "Docket Rev. 7, Do 12.11."), ("Spec Rev. 14", "Tech Pack v1.0"),
               ("Farben des B2-Bands wie am 07.11. entschieden", "B2 ohne Weiß, Rot ist Knallrot (22.10.)"),
               ("Darfst du die Vorschau zeigen (Antwort vom 03.11.)? Ja: jetzt Bildschirmaufnahme für V013 (Cmd + Shift + 5, 3 Takes, langsamer Zoom).", CAPTURE + "Darfst du die Vorschau zeigen (Antwort vom 06.11.)? Ja: jetzt Bildschirmaufnahme (Cmd + Shift + 5, 3 Takes, langsamer Zoom auf ein Motiv). Wird Teil von V205."),
               ("Kommt die Vorschau nicht bis heute", "Kommt die Vorschau nicht bis heute")]),
        T('B', "Tech Pack Zipper mit Claude durchgehen", 'r7-techpack-zipper', m=60, s=[
            "Claudes Entwurf v0.9 Seite für Seite: Deckblatt, Designübersicht, technische Zeichnungen vorn und hinten, Teppich (Größe, Lage, Fransen, Kante, aufnähen vor dem Reißverschluss), Rückendruck B (Siebdruck, Lage 2 cm in der Kapuze), Stern auf der Saumrippe, Maßtabelle S–XL mit Messpunkten, Material und Zutaten, Etiketten, Verpackung, Qualitätskontrolle.",
            "Alles, was nicht stimmt oder fehlt, an Claude. Claude baut v1.0 bis So 15.11.",
            "Offene Felder, die erst die Angebote füllen: Preis, Menge, Muster-Termin.",
        ], f="Claude deine Korrekturen hat und v1.0 bis So 15.11. zugesagt ist.",
           p="Projekt Time Travel: Bau mir das Tech Pack Zipper NVL-TT-02 v0.9 nach dem Muster des Jeans-Tech-Packs v1.0, zweisprachig Deutsch und Englisch, aus Briefing (rev6/research/zipper_briefing.md), Maßtabelle S–XL, Papiertest-Ergebnis, Abdruck und meinen Antworten vom Mi 04.11. Seiten: Deckblatt, Designübersicht, technische Zeichnungen, Teppich, Rückendruck, Stern, Messpunkte, Größen, Materialliste, Verarbeitung, Ablauf und Freigaben, Etiketten und Verpackung, Qualitätskontrolle. Markiere alles, was noch von Angeboten abhängt.",
           o=['claude']),
        T('B', "Patch-Angebote eintragen, Favorit wählen", 'r7-patch-angebote', m=20, s=[
            "Antworten der 3 Patch-Anbieter öffnen.",
            "Ins Blatt „Patches“: Preis bei 50/110/200, Musterkosten, Lieferzeit, Mindestlinienbreite, Leinen vorgeschrumpft ja oder nein, Kante.",
            "Wer keine feinen Arbeiten zeigen kann, fliegt raus. Favorit markieren, morgen bestellst du dort 3 Muster.",
            "Fehlt eine Antwort: kurz nachfassen.",
        ], f="alle Angebote im Blatt stehen und ein Favorit markiert ist.", o=['sheets', 'gmail']),
    ]
    fr = [
        O('w9d1t0', id='r7-gate-digitizing', t="Gate: Digitizing freigeben (≤ 28.000 Stiche)",
          rep=[("Docket W9, Di 10.11.", "Docket Rev. 7, Fr 13.11."), ("Schwellen 15.02. und 21.05.", "Schwellen 15.02. und 21.05."), ("Korrekturen von gestern drin?", "Korrekturen von gestern drin?"), ("Schwellen Mo 15.02. und Fr 21.05.", "Schwellen Mo 15.02. und Fr 21.05.")]),
        T('B', "Muster von Patch D bestellen (3 Stück)", 'r7-patch-muster', m=20, s=[
            "Beim Favoriten von gestern 3 Muster von Patch D bestellen (80 × 71 mm, zwei Lagen mit Rückwand, Datei aus der Anfrage vom 06.11.), Lieferung an dich. Budget 80 €.",
            "Warum 3: Eins wäschst du selbst, zwei gehen per Express an die Fabrik für das PP.",
            "Dem Anbieter schreiben: Der Patch wird nicht mitgewaschen, der Kunde wäscht ihn separat von Hand bei 30 °C. Bitte vorgeschrumpftes Leinen, eine feste Kante und eine Rückwand, die 4 Druckknöpfe hält.",
            "Liefertermin und Betrag ins Blatt „Patches“ und „Ausgaben“.",
        ], f="3 Muster bestellt sind und Liefertermin und Betrag in den Blättern stehen.", o=['sheets']),
    ]
    DROP('w9d4t0', 'neu geschrieben als r7-patch-muster (Fr 13.11., ohne Chenille-Angebot).')
    sa = [
        T('G', "Verpackung: Entwurf wählen", 'r7-verpackung', m=30, s=[
            "Claude liefert aus Board 2 einen Verpackungs-Plan: Versandkarton unbedruckt mit Stempel, Seidenpapier, Aufkleber zum Verschließen, Dankeskarte. Polybeutel und Falten macht die Fabrik (Tech Pack Seite 12).",
            "Entscheiden: Stempel-Motiv (Achtstern oder Schriftzug), Farbe des Seidenpapiers, Aufkleber ja oder nein, Text der Dankeskarte.",
            "Budget-Rahmen: 240 € für 110 Pakete (Plan). Claude rechnet mit.",
            "Bestellt wird im März (W26), LUCID und Verpackungslizenz im Recht-Block.",
        ], f="der Verpackungs-Plan gewählt ist.",
           p="Projekt Time Travel: Mach mir aus Board 2 einen Verpackungs-Plan für 110 Jeans und die Zipper: Versandkarton (Maß für eine gefaltete Jeans), Stempel-Motiv, Seidenpapier, Aufkleber, Dankeskarte mit Text (Deutsch, eine Zeile Englisch). Je Teil zwei Varianten mit Kosten bei 110 Stück, Gesamtbudget 240 €. Keine Plastik-Extras.",
           o=['claude']),
        O('w18d0t0', id='r7-web-1', c='W', t="Website Schritt 1: Werkzeuge auf dem Mac",
          rep=[("Website Schritt 1 (Docket W18, Mo 11.01.)", "Website Schritt 1 (Docket Rev. 7, Sa 14.11.)")]),
    ]
    so = [
        T('A', "Wochenreview W9", 'r7-review-w9', m=20, s=[
            "Drei Zeilen an Claude: fertig, hängt, brauchst du.",
            "Polo: Steht der Weg nach zwei Runden fest? Wenn nicht, sagt Claude dir, welche eine Frage noch fehlt.",
        ], f="Claude die drei Zeilen hat.", o=['claude']),
        T('D', "Gate W9: Digitizing ≤ 28.000 · Tech Pack Zipper v1.0 zugesagt · Hangtag gewählt · Patch-Muster bestellt", 'r7-gate-w9', m=10, s=[
            "Grün: alle vier.",
            "Digitizing über 28.000: Gegenrechnung aus der Aufgabe vom Fr gilt, Entscheidung spätestens Mo.",
            "Ergebnis ins Blatt „Gates“.",
        ], f="das Ergebnis im Blatt „Gates“ steht.", o=['sheets']),
    ]
    return week(9, "2026-11-09", "D2",
                "Design fertig, Teil 2: Digitizing freigeben, Tech Pack Zipper, Hangtag, Verpackung, Polo-Runden",
                [("Stiche", "≤ 28.000 freigegeben"), ("Tech Pack Zipper", "durchgegangen, v1.0 bis So"), ("Hangtag + Karte", "gewählt"), ("Patch D", "3 Muster bestellt")],
                [mo, di, mi, do, fr, sa, so])


def w10():
    DROP('w10d1t5', 'neu geschrieben als Polo-Runden 1–3 (r7-polo-1/2/3) ab Sa 07.11.')
    DROP('w10d6t0', 'ersetzt durch r7-review-w10.')
    DROP('w10d6t1', 'ersetzt durch r7-gate-w10.')
    mo = [
        O('w9d0t2', id='r7-zipper-wahl', t="ENTSCHEIDUNG Zipper: Fabrik, Menge, Preis und Zipper-Schwelle",
          rep=[("Antworten auf die Zipper-Anfrage vom 30.10.", "Antworten auf die Zipper-Anfrage vom Do 05.11."),
               ("Der Muster-Termin muss vor Di 05.01. liegen.", "Der Muster-Termin muss vor dem Sample-Gate (Ziel Fr 15.01.) liegen.")]),
        O('w10d0t2', id='r7-techpack-zipper-fabrik', t="Tech Pack Zipper v1.0 an die Fabrik, Muster bestellen",
          rep=[("Der Muster-Termin muss vor Di 05.01. liegen, sonst wackelt das Sample-Gate.", "Der Muster-Termin muss bis Mo 11.01. liegen, sonst wackelt das Sample-Gate am Fr 15.01.")]),
    ]
    di = [
        T('G', "Polo-Runde 3 und Entscheidung: Polo-Weg", 'r7-polo-3', m=40, s=[
            "Claude legt aus Runde 1 und 2 eine Polo-Spezifikation vor: Grundteil, Logo (neu gezeichneter Kreuzstich-Baum, Größe, Lage), Kragen, Bündchen, Knöpfe, Etiketten, Größen, Preis 79 € (Plan), Muster-Termin.",
            "Entscheiden: eigener Schnitt aus der Zipper-Fabrik, oder Blank plus Berliner Sticker (MOQ 1, Liste in Referenz „Fabriken“ 2). Claude rechnet beide Wege: Stückkosten, Muster, Zeit.",
            "Gehört das Polo zur Vorbestellung am 01.02. oder erst in den Drop am 24.06.? Claudes Rat: erst in den Drop, damit Januar nicht voll läuft. Du entscheidest.",
        ], f="der Polo-Weg und der Zeitpunkt (Vorbestellung oder Drop) entschieden sind.",
           p="Projekt Time Travel, Polo NVL-TT-03: Meine Antworten aus Runde 1 und 2: [..]. Leg mir die Spezifikation vor und rechne zwei Wege: A eigener Schnitt aus der Zipper-Fabrik [Name], B Blank (Stanley/Stella oder AS Colour) plus Berliner Sticker. Je Weg: Stückkosten, Musterkosten, Muster-Termin, Mindestmenge, Risiko. Und: Polo in die Vorbestellung am 01.02. oder erst in den Drop? Sag mir ehrlich, was du tun würdest.",
           o=['claude']),
        O('w18d1t0', id='r7-web-2', c='W', t="Website Schritt 2: Theme-Kopie, Git, GitHub",
          rep=[("Docket W18, Di 12.01.", "Docket Rev. 7, Di 17.11.")]),
        O('w18d1t1', id='r7-web-3', c='W', t="Website Schritt 3: CLAUDE.md mit deinen Regeln"),
    ]
    mi = [
        T('G', "Website-Look: Claudes Stil-Kachel wählen", 'r7-web-look', m=30, s=[
            "Claude baut aus Board 4 zwei Stil-Kacheln als Bild: Startseite oben, Produktkarte, Schrift für „TIME TRAVEL“, Farben, Knöpfe, Fotostil.",
            "Eine wählen oder mischen („Schrift von A, Farben von B“).",
            "Die gewählte Kachel wird die Vorgabe für Website Schritt 4–6 und die Produktseiten.",
        ], f="eine Stil-Kachel gewählt ist.",
           p="Projekt Time Travel: Bau mir aus Board 4 zwei Stil-Kacheln für die Shopify-Seite: A „Archiv“ (ruhig, hell, Papier) und B „Film“ (dunkel, groß, bewegt), je mit Startseite oben, Produktkarte, Schrift, Farben (Knallrot, Naturweiß, Indigo, Antik-Kupfer), Knöpfen und Fotostil. Als Bild, damit ich am Handy wählen kann.",
           o=['claude']),
        T('G', "Content-Look: Cover, Untertitel, Endkarte festlegen", 'r7-content-look', m=30, s=[
            "Claude liefert aus Board 4: Cover-Vorlage für Reels und TikTok (Textlage, Schrift, Größe), Untertitel-Stil (CapCut: Schrift, Größe, Farbe, Position im sicheren Bereich), Endkarte „TIME TRAVEL · 24.06.“ und Signatur der REWIND-Serie.",
            "Wählen. Danach legst du in CapCut 3 Vorlagen an: BUILD, DETAIL, REWIND (am Fr 27.11.).",
        ], f="Cover, Untertitel und Endkarte gewählt sind.",
           p="Projekt Time Travel: Leg mir den Content-Look fest: Cover-Vorlage 9:16 (Text oben im sicheren Bereich, max. 5 Wörter), Untertitel-Stil für CapCut (Schrift, Größe, Farbe, Rand, Position), Endkarte „TIME TRAVEL · 24.06.“ (1 s) und die REWIND-Signatur (Rückspul-Geräusch, Hand gegen den Uhrzeigersinn). Zwei Varianten, als Bild.",
           o=['claude', 'capcut']),
    ]
    do = [
        O('w18d2t0', id='r7-web-4', c='W', t="Website Schritt 4: Zeit-Modul und Countdown",
          rep=[("Docket W18, Mi 13.01.", "Docket Rev. 7, Do 19.11.")]),
        T('G', "Polo: Logo-Datei Kreuzstich-Baum freigeben", 'r7-polo-logo', m=15, s=[
            "Claude zeichnet den Kreuzstich-Baum neu: Raute oben, Äste statt Arme, einfarbig Knallrot, Zelle 1,33 mm wie an der Jeans, ohne Buchstaben. Nicht dein Anhänger und keine Berehynia-Figur.",
            "Prüfen in 1:1 auf Papier an deinem Polo (oder einem T-Shirt): Größe, Lage, liest es sich aus 2 m?",
            "Freigeben.",
        ], f="die Logo-Datei freigegeben ist.", o=['claude']),
    ]
    fr = [
        T('B', "Stickproben: Fotos der gewaschenen Proben anfordern", 'r7-stickproben-status', m=10, s=[
            "Heute ist der zugesagte Termin für die Fotos der gewaschenen Stickproben. Da: weiter am Mo 23.11. Nicht da: Mail „Please send photos and a short video of each washed stitch-out today, flat, daylight, with a grey card.“",
            "Bei Polen: Die Probe kann physisch kommen. Bei Türkei oder China zuerst Fotos, die Proben reisen mit dem Proto.",
        ], f="die Fotos da sind oder angemahnt.", o=['gmail']),
        T('G', "Zipper-Zubehör: Anhänger, Kordelenden, Reißverschluss festlegen", 'r7-zipper-zubehoer', m=20, s=[
            "Aus Board 5 und Claudes Lieferanten-Liste: Achtstern-Anhänger (etwa 25 mm, Antik-Kupfer), Kordelenden und Ösen, Reißverschluss dunkel oder antik mit Kinnschutz.",
            "Wählen und an die Zipper-Fabrik: Liefert sie das Zubehör, oder kaufst du den Anhänger selbst?",
            "Ins Tech Pack Zipper (Claude ergänzt).",
        ], f="Anhänger, Kordelenden und Reißverschluss gewählt und mit der Fabrik geklärt sind.", o=['claude', 'gmail']),
    ]
    sa = [
        O('w18d3t0', id='r7-web-5', c='W', t="Website Schritt 5: Warteliste mit Größen- und Quellen-Tags",
          rep=[("Docket W18, Do 14.01.", "Docket Rev. 7, Sa 21.11.")]),
        O('w18d3t2', id='r7-web-codewort', c='W'),
    ]
    so = [
        T('A', "Wochenreview W10", 'r7-review-w10', m=20, s=[
            "Drei Zeilen an Claude: fertig, hängt, brauchst du.",
            "Was fehlt noch bis zum Design-Gate am So 29.11.? Claude schickt dir die Liste.",
        ], f="Claude die drei Zeilen hat.", o=['claude']),
        T('D', "Gate W10: Zipper-Fabrik gewählt · Tech Pack Zipper bei der Fabrik · Polo-Weg entschieden · Website- und Content-Look gewählt", 'r7-gate-w10', m=10, s=[
            "Grün: alle vier.",
            "Zipper-Angebote zu teuer oder zu spät: Claude rechnet mit dir Plan B (Zipper erst im Drop, nicht in der Vorbestellung).",
            "Ergebnis ins Blatt „Gates“.",
        ], f="das Ergebnis im Blatt „Gates“ steht.", o=['sheets']),
    ]
    return week(10, "2026-11-16", "D2",
                "Design fertig, Teil 3: Zipper an die Fabrik, Polo entschieden, Website- und Content-Look, Website Schritte 2–5",
                [("Zipper", "Fabrik gewählt, Tech Pack v1.0 verschickt, Muster bestellt"), ("Polo", "Weg und Zeitpunkt entschieden"),
                 ("Look", "Website und Content gewählt"), ("Website", "Schritte 2–5")],
                [mo, di, mi, do, fr, sa, so])


def w11():
    DROP('w11d6t0', 'ersetzt durch r7-review-w11; die Reservierung A/B entscheidest du jetzt im Marketing (So 20.12.).')
    mo = [
        N("Sperrwoche 23.–29.11.: Falls du schon etwas postest, kein Ernte-Post und kein Ernte-Bild in Stories (Holodomor-Gedenktag Sa 28.11.)."),
        O('w10d0t0', id='r7-stickproben-bewerten', t="Stickproben bewerten: gewaschen, aus 3 m, Rot auf Indigo, Weiß",
          rep=[("Handy für V016 auf das Stativ: dein erstes Ansehen läuft mit (siehe nächste Aufgabe).", CAPTURE + "Handy aufs Stativ, dein erstes Ansehen läuft mit. Wird V205/V208."),
               ("Je Element A–E prüfen", "Je Zone A, E, B2 und C prüfen"),
               ("„W10_Stickprobe_[Element]_[gewaschen|ungewaschen]“", "„W11_Stickprobe_[Element]_[gewaschen|ungewaschen]“"),
               ("Docket W10, Mo 16.11.", "Docket Rev. 7, Mo 23.11."),
               ("Bewerte jedes Element A–E gegen die Spec (Freeze vom 09.10.)", "Bewerte jede Zone A, E, B2 und C gegen Tech Pack v1.0"),
               ("Gib mir je Element „ok“", "Gib mir je Zone „ok“"),
               ("für jedes Element A–E im Blatt", "für jede Zone A, E, B2 und C im Blatt")]),
        O('w11d0t1', id='r7-proto-status', rep=[("Our target: shipped by Mon 30.11., arriving Thu 03.12.", "Our target: shipped by Fri 04.12., arriving Tue 08.12."),
                                                  ("Bei Portugal: auf die Feiertage 01.12. und 08.12. hinweisen (Allgemeinwissen, ungeprüft) und um Versand vor dem 01.12. bitten.", "Bei Polen: auf die Feiertage am 24.–26.12. hinweisen, für das PP später wichtig."),
                                                  ("bis Do 03.12. zeigst du kein fertiges Teil", "bis zum Proto zeigst du kein fertiges Teil"),
                                                  ("(Gate So 22.11. nachtragen, falls es dort noch fehlte)", "")]),
    ]
    di = [
        O('w10d1t0', id='r7-stickproben-freigabe', rep=[("Je Element A–E", "Je Zone A, E, B2 und C"), ("Garnfarben entscheiden: Weiß, Rot, Gold, Braun.", "Garnfarben entscheiden: Weiß, Knallrot, Gold, Dunkelgold."),
                                                          ("Ziel Versand bis Mo 30.11.", "Ziel Versand bis Fr 04.12."), ("Docket W10, Di 17.11.", "Docket Rev. 7, Di 24.11."),
                                                          ("A [ok/Korrektur], B2 [..], C [..], D [..], E [..]", "A [ok/Korrektur], E [..], B2 [..], C [..]"),
                                                          ("Weiß [Nr.], Rot [Nr.], Gold [Nr.], Braun [Nr.]", "Weiß [Nr.], Knallrot [Nr.], Gold [Nr.], Dunkelgold [Nr.]"),
                                                          ("bis spätestens Mo 30.11.", "bis spätestens Fr 04.12.")]),
        O('w10d1t1', id='r7-gate-stickproben', rep=[("Öffnung rückt dann höchstens auf Mo 15.02.", "Die Vorbestellung bleibt am 01.02., das Proto rückt um die Dauer der neuen Probe."),
                                                      ("Docket W10, Di 17.11.", "Docket Rev. 7, Di 24.11."), ("Plane mir die Wochen 10–13", "Plane mir die Wochen 11–14"),
                                                      ("für den 17.11.", "für den 24.11."), ("(nichts Fertiges vor dem Proto)", "(nichts Fertiges vor dem Proto)")]),
    ]
    mi = [
        O('w10d2t0', id='r7-labdips', rep=[("freigegeben 18.11.2026", "freigegeben 25.11.2026"), ("Stoffmuster und Lab Dips aufheben: Sie sind die Requisiten für V019 am So 22.11.", "Stoffmuster und Lab Dips aufheben: Sie sind Requisiten für den Content ab Dezember.")]),
        O('w6d4t4', id='r7-datenschutz-warteliste', c='R', t="Datenschutz vor dem ersten Post: Warteliste, Tally und „Bring 3“",
          add=["Nur, falls noch offen (Bestandsaufnahme W5/W6). Ab Mo 30.11. sammelt das Marketing Adressen, vorher muss das stehen."]),
    ]
    do = [
        O('w11d3t0', id='r7-patch-waschtest', rep=[("Patch-Muster vom 13.11.", "Patch-Muster vom 13.11."), ("Docket W11, Do 26.11.", "Docket Rev. 7, Do 26.11.")]),
        O('w11d3t1', id='r7-proto-pruefung-vorbereiten',
          rep=[("Waschstandard-Lappen vom 18.11.", "Waschstandard-Lappen vom 25.11."), ("(Unboxing V025 wird am 03.12. sofort gefilmt)", "(das Unboxing wird sofort gefilmt, V206)"),
               ("für Sa 05.12. anfragen", "für Do 10.12. abends oder Sa 12.12. anfragen"), ("Hast du Sa 05.12. eine halbe Stunde?", "Hast du Do 10.12. abends oder Sa 12.12. eine halbe Stunde?"),
               ("zwei W34-Termine für Sa 05.12. bestätigt", "zwei W34-Termine für 10. oder 12.12. bestätigt")]),
    ]
    fr = [
        T('G', "Design-Gate vorbereiten: alle Dateien in einen Ordner", 'r7-design-ordner', m=30, s=[
            "Ordner „TT Design final“ (Drive oder Mac) mit Unterordnern Jeans, Zipper, Polo, Etiketten, Hangtag, Verpackung, Website, Content.",
            "Je Ordner die gültige Datei und eine Zeile „gilt seit, ersetzt“. Alte Fassungen in „_alt“.",
            "Liste an Claude: Was fehlt noch für das Gate am So?",
        ], f="der Ordner steht und Claude die Liste hat.", o=['claude']),
        T('C', "Marketing-Start vorbereiten: Profile, Bio, Link, CapCut-Vorlagen", 'r7-profile', m=40, s=[
            "TikTok, Instagram, YouTube: Profilbild (Achtstern oder dein Gesicht, auf allen gleich), Name „Novalife · Time Travel“.",
            "Bio, auf allen gleich: „100 bestickte Jeans, nummeriert. Berlin. Drop 24.06.2027 · Liste kauft zuerst ↓“ (Englisch: „100 embroidered jeans, numbered. Berlin. Drop 24.06.2027 · list buys first ↓“). Kein „22.04.“ mehr.",
            "Link: Startseite mit ?ref=bio-tt, ?ref=bio-ig, ?ref=bio-yt. Teste jeden Link am Handy bis zur Bestätigungsmail.",
            "Instagram-Highlights: „TIME TRAVEL“, „ZIPPER“, „FAQ“ mit Covern aus dem Content-Look.",
            "CapCut: 3 Vorlagen nach dem Content-Look anlegen (BUILD, DETAIL, REWIND) mit Untertitel-Stil und Endkarte.",
            "Startwerte notieren: Follower TikTok, Instagram, YouTube, bestätigte Liste. Ins Cockpit unter „Startwert“.",
        ], f="Bio und Links auf allen drei Plattformen getestet sind, die drei CapCut-Vorlagen stehen und die Startwerte im Cockpit sind.",
           o=['tiktok', 'insta', 'yt', 'capcut']),
    ]
    sa = [
        O('w11d5t0', id=None),
        T('C', "Content-Batch W12 (1/2): V201 und V203 drehen", 'r7-batch-w12a', m=60, s=[
            "Kein Post heute (Holodomor-Gedenktag). Gedreht wird trotzdem, gepostet ab Montag.",
            "V201 und V203 nach den Briefings unten drehen und schneiden. Material aus dem Album „TT Vorrat“ (Papiertest vom 02.11.) dazunehmen.",
            "Fertige Videos in den Ordner „TT Posts / W12“, Dateiname „V201_final.mp4“. Caption als Notiz daneben.",
        ], f="V201 und V203 fertig geschnitten im Ordner liegen.", vr='V201', o=['capcut']),
    ]
    so = [
        T('D', "DESIGN-GATE: Alles final, bevor das Marketing startet", 'r7-design-gate', m=30, s=[
            "Ordner „TT Design final“ öffnen und jede Zeile prüfen: Jeans (Tech Pack v1.0/1.1, Druckvorlage v1.9, Knopf, Etiketten, Patch D) · Zipper (Tech Pack v1.0 bei der Fabrik, Teppich, Rückendruck, Zubehör) · Polo (Spezifikation, Logo, Weg) · Hangtag und Karte · Verpackung · Website-Look · Content-Look.",
            "Grün: Alles hat eine gültige Datei. Ab morgen gilt: Am Design ändert sich nur etwas, wenn Fabrik, Stickprobe oder Muster einen Grund liefern. Neue Ideen kommen in eine Liste „Drop 2“.",
            "Gelb: Höchstens zwei Teile fehlen, und keins davon geht vor Januar an eine Fabrik (z. B. Verpackung). Dann starten Marketing und Recht trotzdem, und das Teil bekommt einen festen Tag.",
            "Rot: Zipper-Tech-Pack nicht bei der Fabrik oder Stickproben nicht freigegeben. Dann Prompt unten an Claude.",
            "Ergebnis ins Blatt „Gates“ und an Claude.",
        ], f="das Gate im Blatt „Gates“ steht und Claude das Ergebnis hat.",
           p="Projekt Time Travel, Design-Gate So 29.11. (Docket Rev. 7). Stand: [Liste aus dem Ordner]. Ergebnis: [grün/gelb/rot]. Bei gelb: [fehlende Teile]. Bei rot: [was fehlt]. Sag mir, was das für Proto, Sample-Gate (Ziel Fr 15.01.) und die Vorbestellung am 01.02. heißt, und was ich nächste Woche zuerst tue.",
           o=['sheets', 'claude']),
        T('A', "Wochenreview W11 und Startwerte", 'r7-review-w11', m=20, s=[
            "Drei Zeilen an Claude: fertig, hängt, brauchst du.",
            "Startwerte im Cockpit eingetragen? Ab nächstem Sonntag trägst du dort jede Woche Liste, Follower, Zusagen ein.",
        ], f="Claude die drei Zeilen hat und die Startwerte im Cockpit stehen.", o=['claude']),
        O('w11d6t2', id='r7-broadcast-kanal', rep=[("„Hier zeige ich zuerst, was passiert. Das Proto kommt am Do 03.12. Ihr seht es hier vor allen anderen.“", "„Hier zeige ich zuerst, was passiert. Das erste echte Paar kommt nächste Woche. Ihr seht es hier vor allen anderen.“")]),
        T('C', "Content-Batch W12 (2/2): V202 und V204 drehen", 'r7-batch-w12b', m=50, s=[
            "V202 und V204 nach den Briefings drehen und schneiden.",
            "REWIND #01 (G-Klasse): Ist er schon gedreht (Bestandsaufnahme)? Ja: Schnitt prüfen, Post am Do 03.12. Nein: Dreh am Sa 05.12. vormittags mit deinem Vater planen, Post rückt auf Do 10.12.",
        ], f="V202 und V204 fertig geschnitten im Ordner liegen und R01 einen Termin hat.", vr='V202', o=['capcut', 'bibel']),
    ]
    return week(11, "2026-11-23", "D2",
                "Design-Gate So 29.11.: Stickproben frei, Lab Dip als Waschstandard, alles final; Marketing-Start vorbereiten",
                [("Stickproben", "Gate Di 24.11. grün"), ("Waschstandard", "Lab Dip freigegeben"), ("Design-Gate", "So 29.11. grün oder gelb"),
                 ("Marketing-Start", "Profile, Bio, Vorlagen, 4 Videos fertig")],
                [mo, di, mi, do, fr, sa, so])


def build():
    return [w07(), w08(), w09(), w10(), w11()]
