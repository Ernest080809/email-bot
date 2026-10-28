# -*- coding: utf-8 -*-
"""Rev. 7 · Marketing, Recht, Muster, Website: W12–W20 (30.11.2026–31.01.2027). Content kommt aus dem Content-Plan."""
from lib7 import O, T, N, DROP, DROPALL, week, LINKS

G = [("Schema vom 10.10.", "Link-Schema vom Fr 27.11."), ("Spec Rev. 14", "Tech Pack v1.0")]


def comm(id, when="12:30"):
    return T('V', f"{when} · Community: 5 Kommentare mit Inhalt in deiner Nische, DMs, jedes „Ja“ ins Blatt", id, m=10, s=[
        "Bei 5 Accounts aus deiner Nische (Denim, Berliner Streetwear, Stickerei) einen echten Kommentar mit Inhalt, kein Emoji allein.",
        "Alle DMs beantworten. Wer nach Größe, Preis oder Datum fragt: freundlich antworten und mit Erlaubnis ins Blatt „Die ersten 35“, Spalte „Vielleicht“.",
        "Kritik sachlich beantworten, nie löschen. Z, V, Georgsband und Kriegsverherrlichung ausblenden.",
    ], f="5 Kommentare geschrieben und alle DMs beantwortet sind.", o=['insta', 'tiktok'])


def grind(id):
    return T('C', "18:00 · Grind+ · Antwort-Video auf einen Kommentar oder Variante des besten Videos", id, m=15, plus=True, vr='V299', s=[
        "Gab es diese Woche ein Video mit ≥ 2 × Median? Dann eine Variante davon (eine Sache anders). Sonst ein Antwort-Video auf den besten Kommentar der Woche.",
        "Briefing „Antwort-Video“ unten.",
    ], f="das Video online ist oder du bewusst ausgesetzt hast.")


def review(id, wk, date, extra=()):
    return T('A', f"10:00 · Wochenreview W{wk}: Liste nach Quellen-Tag, Content, Kasse, Cockpit", id, m=20, s=[
        "Warteliste: Shopify → Kunden → Segment „E-Mail-Abonnenten“, nur bestätigte. Zahl, Zuwachs, Verteilung nach Quellen-Tag (ref-, st-, rw-) ins Blatt „Warteliste“.",
        "Content: jedes Video der Woche mit Views, Wiedergabedauer, Saves, Shares, neuen Followern und Anmeldungen ins Blatt „Content“. Median der letzten 10 Videos neu rechnen.",
        "Kassencheck K − F − R ins Blatt „Kasse“.",
        "Cockpit im Docket: Liste, Follower gesamt, Zusagen (nur Spalte „Zusage“), bezahlte Jeans.",
        *extra,
        "Zeile an Claude (Prompt unten).",
    ], f="Blätter und Cockpit aktuell sind und die Zeile an Claude gesendet ist.",
       p=f"Projekt Time Travel, Docket Rev. 7, Review W{wk} ({date}). Liste [X] (+[Y]), Follower [F], Zusagen [Z], Videos: bestes [ID, Views], schwächstes [ID, Views], Median [M], Anmeldungen je 1.000 Views [Q], kritische Kommentare [K], Kasse [Ampel]. Offen: [..]. Sag mir, welches Gate greift und was ich nächste Woche anders mache.",
       o=['shopify', 'sheets', 'claude'])


def w12():
    DROP('w8d0t1', 'neu geschrieben als E01 (r7-mail-e01): Werkstatt-Mail 1 „Ab heute öffentlich“, Validierung jetzt am So 20.12.')
    DROP('w12d0t1', 'entfällt: Zipper und Polo laufen nicht über den Berliner Sticker (23.10.).')
    DROP('w12d1t0', 'Notiz vom 23.10., steht in der Design-Inventur.')
    DROP('w12d2t0', 'Notiz vom 23.10., steht in der Design-Inventur.')
    DROP('w12d2t2', 'ersetzt durch E02 (r7-mail-e02), fertig geschrieben, Di 08.12.')
    DROP('w12d3t4', 'ersetzt durch E02 (r7-mail-e02).')
    mo = [
        T('C', "19:00 · Werkstatt-Mail E01 „Ab heute öffentlich“ senden", 'r7-mail-e01', m=20, s=[
            "Shopify-Admin → Marketing → Kampagnen → Kampagne erstellen → Shopify Email. Einfache Text-Vorlage, kein Banner.",
            "Betreff, Vorschau und Text aus der Mail unten. Ein Foto vom Papiertest einsetzen, kein fertiges Teil.",
            "Empfänger: Segment „E-Mail-Abonnenten“ (nur bestätigte).",
            "Link zur Startseite mit utm_source=email&utm_campaign=e01.",
            "Testmail an dich, am Handy lesen, dann für 19:00 terminieren.",
        ], f="E01 für 19:00 terminiert ist und die Testmail am Handy gut aussah.", o=['shopify'], vr=None),
        O('w12d0t2', id='r7-broadcast-start', t="17:00 · Broadcast starten: „Nächste Woche kommt das erste echte Paar“",
          rep=[("„Am Donnerstag kommt das erste echte Teil. Hier siehst du es zuerst.“", "„Nächste Woche kommt das erste echte Paar. Hier siehst du es zuerst.“"),
               ("(angelegt am So 29.11.)", "(angelegt am So 29.11.)"),
               ("Dazu das Foto vom Tracking-Screenshot (Nummer geschwärzt) oder vom leeren Tisch mit Maßband.", "Dazu ein Foto vom Papiertest an der Jeans.")]),
        O('w7d0t2', id='r7-papierabend-fotos', t="Nur falls der Papiertest-Abend stattfand: Fotos an die Gäste, Bitte um Story",
          rep=[("Ordner „W7 · Papierabend“", "Ordner „Papierabend“"), ("Nur Fotos aus der Auswahl vom So", "Nur ausgewählte Fotos")],
          add=["Fand der Abend nicht statt (Bestandsaufnahme W5/W6): abhaken, es gibt nichts zu tun."]),
        T('R', "IHK-Gründungsberatung buchen (Dezember)", 'r7-ihk', m=15, s=[
            "Am 13.10. angefragt, ab 01.11. möglich. Jetzt einen Termin im Dezember buchen, gern online.",
            "Deine Fragen mitnehmen (Claude schreibt sie dir): Gewerbe und Tätigkeitsbeschreibung, Kleinunternehmer ja oder nein bei 10.000 € Umsatz, Einfuhrumsatzsteuer aus der Türkei, Vorbestellung und Rechnungen, Verpackungsgesetz, GPSR-Herstellerangabe.",
            "Termin in den Kalender, Notizen später in den Ordner „03_Recht-Steuer“.",
        ], f="ein Termin gebucht ist und die Fragenliste bereitliegt.", o=['ihk', 'claude']),
    ]
    di = [
        O('w7d1t3', id='r7-gespraeche-1', t="Gespräche: die nächsten zwei à 20 Min. (Ziel bis Do: 10)",
          rep=[("Für Markenkriterium 3 brauchst du bis Do 5 Personen mit UA-, PL- oder BY-Hintergrund (Gespräche plus Tally).", "Für Markenkriterium 3 brauchst du 5 Personen mit UA-, PL- oder BY-Hintergrund (Gespräche plus Tally)."),
               ("(149 € im Januar vorbestellen?)", "(149 € am 01.02. vorbestellen?)"), ("Codes G8 und G9", "Codes G[n]")],
          add=["Wie viele Gespräche hast du schon (Bestandsaufnahme)? Nur so viele führen, bis 10 erreicht sind."]),
        comm('r7-comm-1201'),
    ]
    mi = [
        O('w7d3t2', id='r7-netz-runde', t="Netz-Runde: dein warmes Netz persönlich anschreiben",
          rep=[("„Hey [NAME], nur kurz: Am Sonntag schau ich, ob genug Leute dabei sind, damit ich das Sample bezahle. Wenn du magst: [LINK]?ref=netz. Wenn nicht, alles gut!“",
                "„Hey [NAME], ich mache gerade 100 nummerierte Jeans, nächste Woche kommt das erste echte Paar. Wenn du magst: [LINK]?ref=netz. Wenn nicht, alles gut!“"),
               ("Blatt „Netz“: alle, die auf N1 nicht reagiert haben und nicht eingetragen sind.", "Blatt „Netz“: alle, die noch nicht eingetragen sind. Lief Netz-Runde 1 im Oktober nicht: an alle 15–30 Namen.")]),
        O('w8d2t1', id='r7-hochschulen', rep=[("zwei offene Abende (Stick-Abend Fr 27.11., Mess-Abende im Februar)", "zwei offene Abende (Stick-Abend Fr 18.12., Mess-Abende im Februar)")]),
    ]
    do = [
        O('w7d3t4', id='r7-gespraeche-2', t="Gespräch: das letzte fehlende Segment, Runde abschließen"),
        O('w8d3t1', id='r7-ort-stickabend', t="Ort für den Stick-Abend Fr 18.12. anfragen",
          rep=[("Fr 27.11., ca. 19:00–21:00", "Fr 18.12., ca. 18:30–20:30"), ("Kein Ja bis Mi 11.11.: der Abend findet bei dir statt.", "Kein Ja bis Mo 07.12.: der Abend findet bei dir statt.")]),
    ]
    fr = [
        O('w12d0t0', id='r7-proto-versand', t="Versand des Protos verfolgen (Ziel: verschickt heute)",
          s=["Mail oder WhatsApp an die Fabrik: „Has the prototype shipped? Please send the tracking number.“",
             "Tracking ins Blatt „Proto“, voraussichtlicher Ankunftstag in den Kalender (Ziel Di 08.12.).",
             "Bei Türkei oder China: Zoll und Einfuhrsteuer für das Proto zahlst du bei der Zustellung. Bargeld oder Karte bereithalten, Beleg aufheben.",
             "Kein Versand bis heute: anrufen und ein schriftliches Datum holen. Dann rücken V206 und E02 mit."],
          f="Tracking und Ankunftstag im Blatt stehen oder ein neues Datum schriftlich vorliegt."),
        O('w10d2t2', id='r7-orte-vorab', rep=[("Docket W10, Mi 18.11.", "Docket Rev. 7, Fr 04.12."), ("Das Proto ist ab Do 03.12. da", "Das Proto ist ab Di 08.12. da"), ("Das Proto ist ab 03.12. da", "Das Proto ist ab 08.12. da"),
                                                ("gesendet am 18.11., Antwort offen. Nachfassen am Mi 25.11., wenn nichts kommt.", "gesendet am 04.12., Antwort offen. Nachfassen am Sa 12.12. persönlich mit dem Proto.")]),
        comm('r7-comm-1204'),
        O('w8d4t2', id='r7-medienstudie'),
    ]
    sa = [
        O('w8d5t1', id='r7-creator-1', t="11:00 · Creator-Longlist Runde 1: 10 Namen von Hand"),
        O('w10d5t0', id='r7-burg-schild', rep=[("Stick-Abend Fr 27.11. erwähnen", "Stick-Abend Fr 18.12. erwähnen")]),
        O('w11d5t1', id='r7-cank', t="Grind+ · Weihnachtsmärkte für Designer ansehen (als Besucher)",
          rep=[("Holy Shit Shopping im CANK, Karl-Marx-Straße, Neukölln, 28.–29.11. laut berlin.de. Datum, Öffnung und Eintritt auf der offiziellen Seite nachsehen.",
                "Holy Shit Shopping oder ein anderer Designer-Markt im Dezember: Datum, Ort, Öffnung und Eintritt auf der offiziellen Seite nachsehen. Liegt keiner auf diesem Wochenende, nimm den nächsten."),
               ("Keine Fotos für Posts heute, kein Post (Gedenktag). Notizen reichen.", "Notizen reichen, keine Fotos fremder Stände posten."),
               ("nach der Mail vom 18.11. fragen", "nach der Mail vom 04.12. fragen")]),
    ]
    so = [
        review('r7-review-w12', 12, "So 06.12.", extra=["Erste Woche Content: Welches der vier Videos hat die meisten Anmeldungen gebracht? Das wird dein Startwert für den Median."]),
        O('w12d6t2', id='r7-gate-w12', t="GATE W12: ≥ 60 neue Anmeldungen · Liste ≥ 100 · Proto unterwegs",
          rep=[("Neue Anmeldungen der Woche ≥ 80 und V025 ≥ 2 × Median nach 48 h? Sonst: Proto-Video in 3 Varianten bis So 13.12. (neuer Hook, neues erstes Bild, gleicher Kern).",
                "Neue Anmeldungen der Woche ≥ 60? Sonst: V201 in 2 Varianten bis So 13.12. (neuer Hook, neues erstes Bild, gleicher Kern)."),
               ("Liste ≥ 470? Unter 200 (Alarm, G1)", "Liste ≥ 100? Unter 40 (Alarm, G1)"), ("Zwischen 200 und 470 (G2)", "Zwischen 40 und 100 (G2)")]),
        T('R', "Gewerbe-Anmeldung vorbereiten", 'r7-gewerbe-prep', m=15, s=[
            "Bist du schon 18? Wenn nicht: sag es Claude heute. Dann brauchst du Eltern und Familiengericht, und das dauert Wochen. Der ganze Recht-Block rückt dann vor.",
            "Bereitlegen: Personalausweis, Meldeadresse, Bankkarte für die Gebühr. Tätigkeit: „Entwurf, Herstellenlassen und Online-Handel mit Bekleidung und Accessoires“.",
            "Was sagt die IHK-Beratung (falls schon gewesen)? Ihre Antwort gilt vor diesem Text.",
        ], f="die Unterlagen bereitliegen und die Altersfrage geklärt ist.", o=['gewerbe']),
    ]
    return week(12, "2026-11-30", "M1",
                "Marketing-Start: öffentlich ab heute, Netz und Gespräche, Proto unterwegs, Recht beginnt",
                [("Warteliste", "100 bestätigt (Alarm 40)"), ("Posts", "4 Kern + Story, Grind+ optional"), ("Gespräche", "10 von 10"),
                 ("Proto", "verschickt mit Tracking"), ("Recht", "IHK-Termin gebucht, Gewerbe vorbereitet")],
                [mo, di, mi, do, fr, sa, so])


def w13():
    DROP('w13d3t2', 'Notiz zur Proto-Runde, steht jetzt in den Proto-Runde-Aufgaben.')
    mo = [
        O('w17d2t4', id='r7-gewerbe', c='R', t="Gewerbe anmelden",
          rep=[("Bist du noch keine 18: heute nicht anmelden, sondern Claude fragen. Dann brauchst du die Zustimmung deiner Eltern und des Familiengerichts, und das dauert Wochen.",
                "Bist du noch keine 18: heute nicht anmelden (siehe Vorbereitung vom So)."),
               ("Beginn heute", "Beginn heute (ab jetzt läuft alles über das Gewerbe: Rechnungen, Zahlungsanbieter, Shop)")]),
        O('w9d4t1', id='r7-einladung-stickabend', t="Einladung Stick-Abend Fr 18.12. (E2), 10 Plätze",
          rep=[("Ort steht fest? Antwort vom Kunstraum Heartspace (05.11.) oder Plan B bei dir.", "Ort steht fest? Antwort vom Kunstraum Heartspace (03.12.) oder Plan B bei dir."),
               ("an die Gäste vom Papiertest-Abend", "an die Gäste vom Papiertest-Abend (falls er stattfand)"),
               ("Hochschulen mit Zusage (H1 vom 04.11.)", "Hochschulen mit Zusage (H1 vom 02.12.)"),
               ("Docket W9, Fr 13.11.", "Docket Rev. 7, Mo 07.12."), ("zum Stick-Abend am Fr 27.11.", "zum Stick-Abend am Fr 18.12."),
               ("du siehst die ersten Stickproben", "du siehst das erste echte Paar")]),
        comm('r7-comm-1207'),
    ]
    di = [
        O('w12d3t0', id='r7-proto-da', t="PROTO DA: auspacken (filmen), 10 Messpunkte, Fotos",
          rep=[("Das ist V025.", "Das ist V206 (heute 19:00)."), ("Makros für V026 morgen gleich mit", "Makros für V207 und V208 gleich mit"),
               ("jedes Element A–E nah", "jedes Element (A, E, B2, C, Patch D) nah"), ("vorbereitet am So", "vorbereitet am Vorabend"),
               ("Proto bleibt bei dir (vereinbart am 27.10.). Es ist bis 13.12. dein einziges Vorzeigeteil", "Proto bleibt bei dir (in der Verhandlung am 04.11. festgehalten). Es ist bis zum PP dein einziges Vorzeigeteil")]),
        O('w12d3t1', id='r7-proto-runde', t="Proto-Runde starten: 20 Termine bis So 20.12.",
          rep=[("Ziel 20 Termine bis So 13.12.", "Ziel 20 Termine bis So 20.12."),
               ("Die Slots dieser Woche zuerst anbieten: Fr 04.12. (2 Calls), Mo 07.12. (2 Calls), Di 08.12. (2 Calls), Mi 09.12. und Do 10.12. (je 2–3 Treffen), Sa 12.12. (3 Treffen mit der A-Liste).",
                "Diese Slots zuerst anbieten: Mi 09.12. (2 Calls), Do 10.12. und Fr 11.12. (je 2–3 Treffen), Sa 12.12. (3 Treffen mit der A-Liste), Mo 14.12. (2 Calls), Mi 16.12. (2–3 Treffen)."),
               ("„Das Proto ist da.", "„Das erste echte Paar ist da.")]),
        O('w12d3t2', id='r7-broadcast-proto', t="18:00 · Broadcast: Proto 1 h vor dem Feed"),
        T('C', "19:00 · Werkstatt-Mail E02 „Das erste echte Paar ist da“ senden", 'r7-mail-e02', m=15, s=[
            "Nur wenn das Proto heute da ist. Sonst die Mail auf den Ankunftstag schieben.",
            "Shopify Email, Text aus der Mail unten, Button auf dein TikTok-Profil (Unboxing V206).",
            "Testmail, dann um 19:00 senden, gleichzeitig mit V206.",
        ], f="E02 um 19:00 raus ist.", o=['shopify']),
    ]
    mi = [
        O('w12d4t0', id='r7-proto-pruefen', rep=[("je Element A–E", "je Element (A, E, B2, C)"),
                                                  ("Farben von B2 gegen die Entscheidung vom Sa 07.11. prüfen (Spec Rev. 14).", "Farben von B2 gegen Tech Pack v1.0 prüfen: Gold, Dunkelgold, Rot, kein Weiß."),
                                                  ("Kritische Punkte gehen am So in die Korrekturliste.", "Kritische Punkte gehen am So 13.12. in die Korrekturliste.")]),
        O('w12d4t1', id='r7-proto-calls-1', t="Proto-Runde: 2 Video-Calls à 15′"),
    ]
    do = [
        O('w17d3t0', id='r7-elster', c='R', t="Fragebogen zur steuerlichen Erfassung in ELSTER senden"),
        O('w12d5t0', id='r7-fittest', t="18:00 · Fit-Test mit zwei Körpergrößen",
          rep=[("Oberschenkel: 30 cm statt 28 cm Halbmaß war Absicht für die Stickfläche. Beide sagen: zu weit, passt, zu eng? Hier entscheidet sich, ob er bleibt.",
                "Oberschenkel: Das Tech Pack sagt 29,0 cm Halbmaß bei W34. Beide sagen: zu weit, passt, zu eng?"),
               ("für Varianten und V030", "für Varianten"), ("Tageslicht.", "Abends: warmes Licht seitlich, Graukarte.")]),
        O('w13d3t1', id='r7-gate-proto-da', rep=[("Kommt es nach dem 17.12.: am Sa 19.12. entscheidest du über die Öffnung am Mo 15.02. (B-Zeitachse 1).", "Kommt es nach dem 17.12.: Die Vorbestellung bleibt 01.02., aber das Sample-Gate rückt. Claude plant mit dir um.")]),
        O('w13d1t1', id='r7-proto-calls-2', t="Proto-Runde: 2 Video-Calls à 15′"),
    ]
    fr = [
        O('w13d2t1', id='r7-proto-treffen-1', t="Proto-Runde: 2–3 Treffen", rep=[("(Kern, das Gate am 13.12. hängt daran)", "(das Gate am 20.12. hängt daran)")]),
        comm('r7-comm-1211'),
        O('w13d4t2', id=None, rep=[("Es ist bis 13.12. dein einziges Vorzeigeteil. Die Waschserie läuft mit dem PP ab Mo 04.01.", "Es ist bis zum PP dein einziges Vorzeigeteil. Die Waschserie läuft mit dem PP ab Mi 13.01.")]),
    ]
    sa = [
        O('w13d1t0', id='r7-minishoot-1', t="10:00 · Mini-Shoot 1 (Proto): Makros, Graukarte, On-Body",
          v=None, vr=None,
          rep=[("Beweis 4: Fahrt 3 m → 30 cm in einem Take. Das ist V030 morgen: im Hinterhof, Person mit Proto steht, geht langsam auf die Kamera zu, Kamera auf Hüfthöhe, endet im Makro Münztasche E. 3 Takes.",
                "Beweis 4: Fahrt 3 m → 30 cm in einem Take (Reserve, falls V207 nachgedreht werden soll). 3 Takes."),
               ("V124 gleich mit: Hose auf links, Makro der Stickerei-Rückseite mit Vlies, Finger zeigt. 3 Takes.", "Rückseite gleich mit: Hose auf links, Makro der Stickerei-Rückseite mit Vlies, Finger zeigt. 3 Takes."),
               ("Makro jedes Elements (A, E, B2, C, D)", "Makro jedes Elements (A, E, B2, C, Patch D)"),
               ("V030 schneiden: CapCut, Hook EN, 7–10 s, Export W13/final/V030. Musik nicht einbacken.", "Clips in den Ordner „TT Vorrat“.")],
          f="mindestens 12 scharfe Fotos im Ordner „Shop“ liegen und die Clips im Vorrat sind."),
        O('w13d5t1', id='r7-a-liste', rep=[("Wir hatten am 18.11. gesprochen.", "Ich hatte euch am 04.12. geschrieben.")]),
        O('w12d5t2', id='r7-gate-proto-fit', t="GATE Proto und Fit ok → PP am Mo 14.12. bestellen",
          rep=[("PP-Sample am Mo 07.12. bestellen", "PP-Sample am Mo 14.12. bestellen"),
               ("zweites Proto bestellen, Öffnung der Vorbestellung nach B-Zeitachse 1 auf Mo 15.02. (Referenz „Wochenziele, Gates“ 7.4). Claude schreiben: „Gate 05.12. rot, Grund: …, rechne B-Zeitachse 1.“",
                "zweites Proto bestellen. Die Vorbestellung bleibt am 01.02. mit Proto-Fotos, nur das Sample-Gate rückt. Claude schreiben: „Gate 12.12. rot, Grund: …, plan um.“")]),
    ]
    so = [
        O('w12d6t0', id='r7-korrekturliste', t="10:00 · Korrekturliste mit Claude",
          rep=[("Oberschenkel 28 oder 30 cm entscheiden und ins Blatt „Gates“.", "Oberschenkel: bleibt 29,0 cm Halbmaß (W34) oder ändern? Entscheiden und ins Blatt „Gates“."),
               ("Sie geht am Mo 07.12. mit der PP-Bestellung raus.", "Sie geht am Mo 14.12. mit der PP-Bestellung raus."),
               ("Docket W12, So 06.12.", "Docket Rev. 7, So 13.12."), ("je Element A–E", "je Element (A, E, B2, C, Patch D)"),
               ("Oberschenkel 28 oder 30 cm Halbmaß", "Oberschenkel 29,0 cm Halbmaß lassen oder ändern")]),
        O('w13d3t0', id='r7-onbody', t="11:30 · On-Body-Fotos: zwei Körper, mit Größe und Bundmaß"),
        review('r7-review-w13', 13, "So 13.12.", extra=["Proto-Runde: Termine vereinbart [n]/20, Zusagen mit Größe."]),
        O('w13d6t1', id='r7-gate-w13', t="GATE So 13.12.: Zusagen ≥ 5 · Liste ≥ 180 · PP-Termin",
          rep=[("Zusagen mit Größe ≥ 18 (nur Spalte „Zusage“)? Sonst: bis So 20.12. jeden Tag 3 persönliche Termine.", "Zusagen mit Größe ≥ 5 (nur Spalte „Zusage“)? Sonst: bis So 20.12. jeden Tag 3 persönliche Termine."),
               ("Zipper-Muster: Hat die Zipper-Fabrik ein Versanddatum vor Di 05.01. genannt? Sonst morgen nachfragen: Ohne Zipper-Muster kein Sample-Gate am Di 05.01.", "Zipper-Muster: Hat die Zipper-Fabrik ein Versanddatum bis Mo 11.01. genannt? Sonst morgen nachfragen: Ohne Zipper-Muster kein Sample-Gate am Fr 15.01."),
               ("Liste ≥ 550? Unter 230 (Alarm, G1)", "Liste ≥ 180? Unter 70 (Alarm, G1)"), ("Zwischen 230 und 550 (G2)", "Zwischen 70 und 180 (G2)"),
               ("(betrifft V035, V036)", "(betrifft V211, V212)"), ("Proto-Varianten aus dem Gate vom 06.12. erledigt?", "Varianten aus dem Gate vom 06.12. erledigt?")]),
        O('w13d6t2', id='r7-giggster'),
        O('w9d6t2', id='r7-creator-2', t="Creator-Longlist Runde 2 (10 Namen)"),
    ]
    return week(13, "2026-12-07", "M1",
                "Das erste echte Paar: Proto prüfen, zeigen, Proto-Runde, Fit-Test; Gewerbe und ELSTER",
                [("Warteliste", "180 bestätigt (Alarm 70)"), ("Proto", "da, gemessen, Fit-Test, Gate Sa"), ("Proto-Runde", "10 von 20 Terminen"),
                 ("Zusagen", "5 mit Größe"), ("Recht", "Gewerbe angemeldet, ELSTER gesendet")],
                [mo, di, mi, do, fr, sa, so])


def w14():
    DROP('w14d3t0', 'Notiz vom 23.10., steht in der Design-Inventur.')
    DROP('w14d5t2', 'Notiz vom 23.10.; Sample-Gate ist jetzt Fr 15.01.')
    DROP('w14d6t0', 'zusammengelegt mit der Validierung (r7-validierung, So 20.12.).')
    DROP('w12d2t1', 'Creator-Shortlist kommt nach Runde 3, jetzt Do 17.12. (r7-creator-short).')
    mo = [
        O('w13d0t0', id='r7-pp-bestellen', t="09:00 · Korrekturen per Foto und Maß senden, PP-Sample bestellen",
          rep=[("Das Proto bleibt bei dir (vereinbart am 27.10.).", "Das Proto bleibt bei dir."),
               ("Termin schriftlich: PP bei dir spätestens Mo 04.01.2027 (Waschserie ab 04.01., Gate „PP freigegeben“ Di 05.01.). Portugal hat zwischen den Jahren meist Pause, Feiertag 08.12. einrechnen (ungeprüft). Die Türkei nicht.",
                "Termin schriftlich: PP verschickt bis Fr 08.01.2027, bei dir bis Mi 13.01. (Waschserie ab 13.01., Sample-Gate Fr 15.01.). Polen hat am 24.–26.12. und 01.01. frei, die Türkei nur am 01.01."),
               ("Bitte um Bestätigung bis Mi 09.12. mit Versanddatum. Ins Blatt „Fabriken“: gesendet 07.12., Versanddatum PP, Bestätigung ja/nein.", "Bitte um Bestätigung bis Mi 16.12. mit Versanddatum. Ins Blatt „Fabriken“: gesendet 14.12., Versanddatum PP, Bestätigung ja/nein."),
               ("Korrekturen und PP-Bestellung raus sind und im Blatt „Fabriken“ das geforderte Datum 04.01. steht.", "Korrekturen und PP-Bestellung raus sind und im Blatt „Fabriken“ das geforderte Datum 08.01. steht."),
               ("Docket W13, Mo 07.12.", "Docket Rev. 7, Mo 14.12."), ("bis Mo 04.01.2027", "bis Mi 13.01.2027"), ("by 4 January 2027", "by 13 January 2027"), ("by Mon 4 January", "by Wed 13 January")]),
        O('w13d0t1', id='r7-patch-express'),
        O('w11d0t3', id='r7-stickabend-tn', t="Stick-Abend Fr 18.12.: Teilnehmer bestätigen, QR mit ?ref=stick bauen"),
        O('w13d0t2', id='r7-proto-calls-3', t="Proto-Runde: 2 Video-Calls à 15′"),
    ]
    di = [
        O('w14d1t0', id='r7-handheber'),
        O('w10d5t1', id='r7-stickabend-material', t="Material für den Stick-Abend kaufen: Denim, Garn, Nadeln, 10 Rahmen"),
        O('w17d3t2', id='r7-payments', c='R', t="Shopify Payments aktivieren, Support fragen: Reserve und Auszahlung"),
        O('w17d2t2', id='r7-bank', c='R', t="Bank: Tageslimit ≥ 3.100 €, Auslandsüberweisung, Kontoart prüfen"),
        O('w9d5t0', id='r7-presse-1', t="Presseliste Teil 1: 8 Medien, je 3 Artikel lesen"),
    ]
    mi = [
        O('w13d2t0', id='r7-pressemappe', t="PRESSE: Pressemappe v1 und Seite /pages/presse"),
        O('w13d3t3', id='r7-proto-treffen-2', t="Proto-Runde: 2–3 Treffen", rep=[("(Kern, das Gate am 13.12. hängt daran)", "(das Gate am 20.12. hängt daran)")]),
        O('w19d1t0', id='r7-web-groessen', c='W', t="Website: Größenseite und FAQ: „W34 — 86 cm“, Umrechnung, sechs Einwände",
          rep=[("„W32 — 81 cm“", "„W34 — 86 cm“")]),
    ]
    do = [
        O('w10d3t0', id='r7-presse-2', t="Presseliste Teil 2: Kontakte nur aus Impressum oder offizieller Seite"),
        O('w11d3t2', id='r7-creator-3', t="Creator-Longlist Runde 3: auf 30 Namen komplett"),
        T('V', "Creator-Shortlist 12: Engagement, Views, Brand-Safety", 'r7-creator-short', m=30, s=[
            "Aus den 30 Namen 12 wählen: echte Kommentare, Views pro Video im Verhältnis zu Followern, Stil passt, keine Politik oder Provokation im Feed.",
            "Ins Blatt „Creator“ Spalte „Shortlist“, Top 8 markieren. Morgen bekommen die Top 8 die erste DM.",
        ], f="12 Namen auf der Shortlist und die Top 8 markiert sind.", o=['sheets']),
        O('w17d3t3', id='r7-haftpflicht', c='R', t="Produkthaftpflicht: Preis bei 1–2 Versicherern anfragen"),
        comm('r7-comm-1217'),
    ]
    fr = [
        O('w13d4t0', id='r7-creator-dm', t="10:00 · CREATOR: Erst-DM C2 an die Top 8"),
        O('w11d4t1', id='r7-stickabend', t="18:30 · STICK-ABEND bis 20:30: Raute 7 × 7 in Rot/Weiß auf Denim",
          add=["REWIND #02 am Abend drehen (Briefing in der Content-Aufgabe heute): erst fragen, wer ins Video will."]),
        O('w11d4t2', id='r7-stickabend-plus'),
    ]
    sa = [
        O('w14d5t0', id='r7-vorbestellung-plan', rep=[("Gilt für Website-Raster (Sa 23.01.)", "Gilt für Website-Raster (Sa 23.01.)"), ("Docket W14, Sa 19.12.", "Docket Rev. 7, Sa 19.12.")]),
        O('w14d5t3', id='r7-orte-fest', rep=[("Antworten auf die Anfragen vom 12.12. prüfen.", "Antworten auf die Anfragen vom 04.12. und die Besuche vom 12.12. prüfen."),
                                              ("Orte an Claude für die Mails vom 26.01. und den Event-Tipp am 30.12.", "Orte an Claude für die Mails E04 (26.01.) und den Event-Tipp am 30.12.")]),
        O('w7d5t0', id='r7-validierung-zahlen', t="Zahlen für die Validierung sammeln: Anmeldungen, Views, Quote"),
        O('w7d5t1', id='r7-markenkriterien', t="Gespräche, Tally und Storys an Claude: Markenkriterien 1–3"),
        O('w8d5t3', id='r7-laden-runde', t="Grind+ · Laden-Runde Mitte-Nord (4 Läden) mit dem Proto"),
        O('w14d4t2', id='r7-a-liste-2', t="Grind+ · A-Liste Teil 2 mit Proto: Studio183 und Konk"),
    ]
    so = [
        O('w7d6t0', id='r7-validierung', t="10:00 · VALIDIERUNG + Wochenreview W14: Liste, Zusagen, Views, Kasse, Cockpit"),
        O('w7d6t1', id='r7-gate-validierung', t="Gate · VALIDIERUNG: grün ≥ 250 und ≥ 10 Zusagen · gelb 100–249 · rot < 100",
          s=["Grün (≥ 250 bestätigt und ≥ 10 Zusagen mit Größe): Patch-Serie am Mo bestellen, alles weiter wie geplant.",
             "Gelb (100–249): Patch-Serie trotzdem bestellen (sie wird für das PP gebraucht), aber bis 10.01. keine weiteren Ausgaben außer Plan. Bestes Video in 3 Varianten, Netz-Runde an alle Offenen.",
             "Rot (< 100): Ausgaben-Stopp bis auf die Patch-Serie. Prompt an Claude: Was ändern wir an Hooks, Kanälen und Abenden? Die Vorbestellung bleibt 01.02., aber das Ziel 35 ist dann wackelig.",
             "Ergebnis ins Blatt „Gates“ und in den Docket-Abschnitt Cockpit."],
          f="die Ampel im Blatt „Gates“ steht."),
        O('w11d6t1', id='r7-gate-reservierung', t="GATE Reservierung A/B entscheiden (gebaut wird im Januar)",
          rep=[("(gebaut wird nach dem Sample-Gate)", "(gebaut wird Mo 18.01.)")]),
        O('w14d6t1', id='r7-gate-w14', t="GATE 20.12.: Zusagen ≥ 10, Stufe 2, Patch, Zipper-Muster, Liste ≥ 260",
          rep=[("Zusagen mit Größe ≥ 15, nur Spalte „Zusage“. 10–14: jeden Tag bis Mi 3 persönliche DMs. Unter 10:", "Zusagen mit Größe ≥ 10, nur Spalte „Zusage“. 5–9: jeden Tag bis Mi 3 persönliche DMs. Unter 5:"),
               ("Zipper-Muster da oder mit Versanddatum vor Di 05.01.?", "Zipper-Muster mit Versanddatum bis Mo 11.01.?"),
               ("Liste ≥ 620 (Alarm 260)", "Liste ≥ 260 (Alarm 100)")]),
        T('D', "Sprache der Hooks und Liefergebiet entscheiden", 'r7-sprache', m=15, s=[
            "Drei Wochen Content: Haben englische oder deutsche Hooks mehr Anmeldungen je 1.000 Views gebracht? Zahlen aus dem Blatt „Content“.",
            "Englisch vorn: Versand EU vorbereiten (W17), englische Produktseite (W20). Deutsch vorn: nur Versand nach Deutschland bis zum Drop.",
            "Bildregel bleibt: keine Seitenansicht links mit B2 im Bild.",
        ], f="Sprache und Liefergebiet im Blatt „Entscheidungen“ stehen.", o=['sheets']),
    ]
    return week(14, "2026-12-14", "M1",
                "PP bestellt, Payments und Bank, Presse vorbereiten, Stick-Abend Fr 18.12., Validierung So 20.12.",
                [("Warteliste", "260 bestätigt (Alarm 100)"), ("Validierung", "grün ≥ 250 und ≥ 10 Zusagen"), ("PP", "bestellt, Versand bis 08.01. bestätigt"),
                 ("Stick-Abend", "Fr 18.12., 10 Gäste"), ("Recht", "Payments und Bank eingerichtet")],
                [mo, di, mi, do, fr, sa, so])


def w15():
    mo = [
        O('w14d3t1', id='r7-patch-serie', t="Patch D in Serie: 110 Stück direkt an die Fabrik bis 29.01.",
          rep=[("Nur wenn der Waschtest aus W11 bestanden ist.", "Nur wenn der Waschtest vom 26.11. bestanden ist und die Validierung grün oder gelb ist."),
               ("Patch-Vorlage aus Docket → Referenz → Vorlagen nutzen, 110 Stück", "110 Stück"),
               ("Zahlung (ca. 330 €, Rev. 5.3) ins Blatt „Ausgaben“.", "Zahlung (Angebot vom 12.11.) ins Blatt „Ausgaben“."),
               ("Klappt es heute nicht: Bestellung spätestens Mo 21.12., Fabrik über die neue Patch-Frist Fr 05.02. informieren (Gate So).", "Klappt es heute nicht: spätestens Mo 28.12., und die Fabrik über die neue Patch-Frist Fr 05.02. informieren.")]),
    ]
    di = [O('w15d1t0', id='r7-belege'), O('w15d1t1', id='r7-comm-1222')]
    mi = [O('w15d2t1', id='r7-broadcast-feiertage')]
    do = [O('w15d3t0', id=None)]
    fr = [O('w15d4t0', id=None)]
    sa = []
    so = [O('w15d6t0', id='r7-proto-bilder', rep=[("seit 03.12.", "seit 08.12."), ("Rest für die Mails vom 26.01. und 01.02.", "Rest für die Mails E04 und E06")]),
          O('w15d6t1', id='r7-review-w15', t="Wochenreview W15 + Cockpit + Zeile an Claude")]
    return week(15, "2026-12-21", "M1",
                "Feiertage: wenig, aber sauber. Patch-Serie bestellt, Belege sortiert, Proto-Bilder ausgewählt",
                [("Warteliste", "320 bestätigt (Alarm 120)"), ("Posts", "2 Kern + Story"), ("Patch D", "110 Stück bestellt")],
                [mo, di, mi, do, fr, sa, so])


def w16():
    DROP('w16d0t0', 'neu als r7-pp-status (Mo 28.12.) und r7-pp-versand (Fr 08.01.).')
    mo = [T('B', "PP-Status abfragen: Fotos und Versanddatum", 'r7-pp-status', m=10, s=[
        "Mail an die Fabrik: „How is the PP sample going? Please send photos and confirm shipping by Fri 8 January.“",
        "Antwort ins Blatt „Proto“. Kein Versanddatum bis Mi: anrufen.",
    ], f="ein Versanddatum schriftlich vorliegt.", o=['gmail']),
          N("Zwischen den Jahren: Website Stufe 1 bauen und live schalten (Di bis Do). Dafür hast du jetzt mehr Zeit als im Januar.")]
    di = [O('w18d5t0', id='r7-web-6', c='W', t="Website Schritt 6: Startseite Stufe 1 „Prozess“"),
          O('w16d1t0', id='r7-comm-1229')]
    mi = [O('w16d2t0', id='r7-eventtipp', rep=[("Orte aus dem Blatt „Abende“ (fest seit 19.12.)", "Orte aus dem Blatt „Abende“ (fest seit 19.12.)")]),
          O('w18d6t0', id='r7-web-7', c='W', t="Website Schritt 7: Prüfen (Theme Check, Handy, Instagram-Browser)")]
    do = [O('w16d3t0', id='r7-monat-dez', rep=[("(Korridor: 700 auf der Liste)", "(Korridor: 380 auf der Liste)"), ("Zahl gegen den Korridor 700.", "Zahl gegen den Korridor 380."), ("(Korridor 700)", "(Korridor 380)")]),
          O('w16d3t1', id='r7-bruecke'),
          O('w19d0t0', id='r7-web-8', c='W', t="Website Schritt 8: Stufe 1 live, altes Theme wird PLAN B, Test ?ref=test"),
          O('w16d3t2', id='r7-comm-1231')]
    fr = [O('w16d4t0', id=None)]
    sa = [O('w16d5t0', id=None)]
    so = [O('w16d6t0', id='r7-review-w16', t="Wochenreview W16 + Cockpit + Zeile an Claude"),
          O('w16d6t1', id='r7-gate-w16', t="GATE 03.01.: Liste ≥ 380, PP-Versanddatum, Brücke ja/nein, Website Stufe 1 live",
            rep=[("Liste ≥ 740 (Alarm 300)?", "Liste ≥ 380 (Alarm 150)?"), ("PP-Sample unterwegs mit Tracking (Mo 28.12.)? Sonst morgen die Fabrik anrufen: Das Sample-Gate am Di 05.01. hängt daran.", "PP-Versanddatum bis Fr 08.01. schriftlich? Sonst morgen die Fabrik anrufen: Das Sample-Gate am Fr 15.01. hängt daran."),
                 ("Zipper und Polo frei oder das zweite Muster da? Sonst heute beim Sticker nachfragen.", "Zipper-Muster mit Versanddatum? Website Stufe 1 live?")]),
          O('w16d6t3', id='r7-whatsapp-kanal')]
    return week(16, "2026-12-28", "M1",
                "Zwischen den Jahren: Website Stufe 1 live, PP in Arbeit, Brücke klären, Event-Tipp planen",
                [("Warteliste", "380 bestätigt (Alarm 150)"), ("Website", "Stufe 1 live"), ("PP", "Versand bis 08.01. bestätigt"), ("Brücke", "ja oder nein")],
                [mo, di, mi, do, fr, sa, so])


def w17():
    DROP('w17d2t3', 'ersetzt durch den Content-Plan (V219 am Mi 06.01.).')
    mo = [
        O('w14d4t0', id='r7-creator-c3', t="CREATOR nachfassen (C3); unter 5 Zusagen: Nr. 9–12 anschreiben"),
        O('w18d3t1', id='r7-lucid', c='R', t="LUCID: Verpackungsregister registrieren"),
        O('w17d0t2', id='r7-creator-karte'),
    ]
    di = [
        O('w14d1t1', id='r7-presse-welle-1', t="PRESSE-WELLE 1 „Vorbestellung ab 01.02.“ an 7 Medien",
          rep=[("gesendet 15.12.", "gesendet 05.01."), ("Nachfassen nur einmal, am Di 05.01.", "Nachfassen nur einmal, am Di 12.01."), ("Docket W14, Di 15.12.", "Docket Rev. 7, Di 05.01."),
               ("ab 24.06. 169 €", "danach 169 €"), ("3 echte Proto-Fotos (kein Mockup)", "3 echte Proto-Fotos (kein Mockup)")]),
        O('w18d4t0', id='r7-rechtstexte', c='R', t="Rechtstexte: AGB, Widerruf, Versand, Zahlung mit Abmahnschutz + Hotline"),
    ]
    mi = [O('w18d4t1', id='r7-datenschutz-ende', c='R')]
    do = [O('w18d2t1', id='r7-versand-shop', c='W', t="Shop: Versand einrichten (Deutschland, EU nur bei englischen Hooks)"),
          O('w17d3t1', id='r7-comm-0107')]
    fr = [T('B', "Versand des PP-Samples bestätigen, Tracking holen", 'r7-pp-versand', m=10, s=[
        "Mail an die Fabrik: „Please confirm the PP sample has shipped and send the tracking number. We need it in Berlin by Wed 13.01.“",
        "Tracking ins Blatt „Proto“, Ankunftstag notieren.",
        "Kein Tracking bis heute Abend: Sample-Gate rückt, Claude plant um. Die Vorbestellung bleibt am 01.02. mit Proto-Fotos.",
    ], f="Tracking und Ankunftstag im Blatt stehen.", o=['gmail'])]
    sa = [O('w17d5t1', id='r7-mess-zusagen'), O('w17d5t2', id='r7-fotograf')]
    so = [O('w17d6t0', id='r7-review-w17', t="Wochenreview W17, Zahlen ins Cockpit, Zeile an Claude"),
          O('w17d6t1', id='r7-gate-w17', t="Gate: Zusagen ≥ 18 · Liste ≥ 480 · Rechtstexte live · LUCID",
            rep=[("Zusagen ≥ 25 · Liste ≥ 850 · Sample-Gate durch · Gewerbe angemeldet", "Zusagen ≥ 18 · Liste ≥ 480 · Rechtstexte live · LUCID")])]
    return week(17, "2027-01-04", "M1",
                "Recht: LUCID, Rechtstexte, Datenschutz; Presse-Welle 1; PP unterwegs; Creator nachfassen",
                [("Warteliste", "480 bestätigt (Alarm 190)"), ("Zusagen", "18"), ("Recht", "LUCID und Rechtstexte live"), ("PP", "unterwegs mit Tracking")],
                [mo, di, mi, do, fr, sa, so])


def w18():
    mo = [O('w17d1t2', id='r7-creator-c4'),
          O('w19d1t1', id='r7-web-produkt-jeans', c='W', t="Produktseite Jeans als Entwurf + Vertrauens-Checkliste (9 Punkte)")]
    di = [O('w17d1t3', id='r7-presse-nachfassen', t="PRESSE: Welle 1 einmal nachfassen (P4)"),
          O('w19d2t1', id='r7-web-9', c='W', t="Website Schritt 9: Stufe 2 „Das Muster“ mit Proto-Fotos")]
    mi = [O('w17d0t0', id='r7-pp-pruefen', t="PP-Sample prüfen: 10 Maße, Fäden, Patch, Knopf, Nieten, Labels"),
          O('w17d0t3', id='r7-waschserie', rep=[("bis Fr täglich 1× auf links", "bis Mo 18.01. täglich 1× auf links (5 Wäschen, für V231)")]),
          O('w14d2t0', id='r7-mails-entwurf', t="Mails E04–E07 zum Vorbestell-Start als Entwurf in Shopify anlegen", p=None,
            s=["Die Texte stehen fertig im Docket (E04, E05, E06, E07). Lesen, Zahlen und Orte prüfen.",
               "Shopify → Marketing → Kampagnen → Kampagne erstellen → Shopify Email. Vier Entwürfe: „TT E04 Vorbestellung“, „TT E05 Morgen“, „TT E06 Du bist drin“, „TT E07 Noch X Paar“.",
               "Empfänger: E04 und E05 die ganze Liste, E06 die ganze Liste (18:00), E07 Liste ohne Kauf.",
               "Buttons mit utm_source=email&utm_campaign=e04 … e07.",
               "Nichts terminieren. Geplant wird laut Plan."],
            f="vier Entwürfe mit Betreff, Vorschautext und Button in Shopify Email liegen.")]
    do = [T('B', "Zipper-Muster prüfen", 'r7-zipper-muster', m=60, s=[
              "Zipper-Muster gegen Tech Pack Zipper v1.0: alle Messpunkte der Maßtabelle (Größe M), Teppich (Größe, Lage, Versatz am Reißverschluss, Fransen, Kante), Rückendruck (Lage 2 cm in der Kapuze, Kapuze unten nichts sichtbar), Stern auf der Saumrippe (verzogen?), Kordeln, Reißverschluss, Anhänger, Etiketten.",
              "Anziehen, Spiegel, Fotos vorn, hinten, Kapuze hoch und runter. Graukarte im ersten Bild.",
              "Befunde ins Blatt „Proto“, Bereich Zipper. Korrekturliste mit Claude (Prompt unten).",
              CAPTURE_Z,
          ], f="jeder Punkt des Tech Packs ein Ergebnis hat und die Korrekturliste bei Claude liegt.",
             p="Projekt Time Travel, Zipper-Muster NVL-TT-02: Befunde gegen Tech Pack v1.0: [Tabelle], Fotos: [..]. Schreib mir eine Korrekturliste auf Englisch und sag mir ehrlich: Freigabe am Fr 15.01. mit Korrekturen für die Serie, oder braucht es ein zweites Muster?",
             o=['claude']),
          O('w19d4t2', id='r7-vorbestellung-recht', c='R', t="Vorbestellung rechtlich sauber machen + Geld-zurück-Regel")]
    fr = [O('w17d1t0', id='r7-pp-freigabe', t="PP-Sample schriftlich freigeben"),
          O('w17d1t1', id='r7-sample-gate', t="SAMPLE-GATE: Jeans-PP und Zipper-Muster freigegeben?",
            rep=[("Di 05.01.", "Fr 15.01.")])]
    sa = [O('w17d2t1', id='r7-minishoot-2', t="10:00 · Mini-Shoot 2 mit dem PP: Goldfäden, Innenetikett, Makros für die Produktseite",
            rep=[("N°", "Innenetikett")]),
          O('w19d3t0', id='r7-web-bilder', c='W', t="Produktseite mit echten Bildern (Proto und PP)")]
    so = [O('w18d6t0', id='r7-review-w18', t="Wochenreview W18, Zahlen ins Cockpit, Zeile an Claude"),
          O('w18d6t1', id='r7-gate-w18', t="Gate: Sample-Gate durch · Payments verifiziert · Liste ≥ 600",
            rep=[("Payments verifiziert · Rechtstexte live · LUCID · Liste ≥ 1.000", "Sample-Gate durch · Payments verifiziert · Liste ≥ 600")])]
    return week(18, "2027-01-11", "M1",
                "SAMPLE-GATE Fr 15.01.: PP und Zipper-Muster prüfen und freigeben; Produktseite mit echten Bildern",
                [("Warteliste", "600 bestätigt (Alarm 240)"), ("Zusagen", "22"), ("Sample-Gate", "Fr 15.01. grün"), ("Website", "Stufe 2 und Produktseite Jeans als Entwurf")],
                [mo, di, mi, do, fr, sa, so])


CAPTURE_Z = "Für den Content: Auspacken filmen (wie beim Proto), Kapuze hoch und runter vor dem Spiegel, Makro Samt und Fransen. Daraus werden V224 und V233."


def w19():
    DROP('w19d5t1', 'ersetzt durch den Content-Plan.')
    mo = [O('w17d2t0', id='r7-konditionen-po', t="Bestellkonditionen festzurren, Stoff für 100 Paar reservieren"),
          T('R', "GPSR: Herstellerangabe für das Innenetikett an die Fabrik", 'r7-gpsr', m=15, s=[
              "Laut Tech Pack Seite 12 schickst du im Januar den endgültigen Text: Novalife · Postanschrift · E-Mail. Modellnummer NVL-TT-01, Seriennummer = Stücknummer.",
              "Welche Adresse? Gewerbeadresse vom 07.12. Keine private Freemail-Adresse, wenn es eine Novalife-Adresse gibt.",
              "Text an Fabrik (Jeans) und Zipper-Fabrik, Bestätigung ins Blatt „Fabriken“.",
          ], f="beide Fabriken den Herstellertext bestätigt haben.", o=['gmail']),
          O('w19d0t2', id='r7-reservierung-bauen', c='W'),
          O('w19d0t1', id='r7-paypal', c='R', t="Zahlungsanbieter: PayPal verbinden, Auszahlungspläne notieren")]
    di = [O('w19d1t3', id='r7-web-produkt-zipper', c='W'), O('w19d1t2', id='r7-comm-0119')]
    mi = [O('w19d2t0', id='r7-reservierung-offen')]
    do = [O('w19d3t1', id='r7-vorbestellung-shopify', c='W'), O('w19d3t2', id='r7-comm-0121')]
    fr = [O('w19d4t0', id='r7-stufe2-entwurf', c='W'), O('w19d4t1', id='r7-bestaetigung-vorlage', c='W'), O('w19d4t3', id='r7-testbestellung', c='W')]
    sa = [O('w19d5t0', id='r7-web-10', c='W', t="Website Schritt 10: Nummern-Raster 001–100 als Kreuzstich"),
          O('w19d5t2', id='r7-spiel-stiltest')]
    so = [O('w19d6t0', id='r7-review-w19', t="Wochenreview W19, Zahlen ins Cockpit, Zeile an Claude"),
          O('w19d6t1', id='r7-gate-w19')]
    return week(19, "2027-01-18", "M1",
                "Shop-Bau: Reservierung offen, Vorbestellung und Stufe 2 als Entwurf, Testbestellung; GPSR-Text an die Fabriken",
                [("Warteliste", "750 bestätigt (Alarm 300)"), ("Zusagen", "25"), ("Reservierung", "offen seit Mi 20.01."), ("Shop", "Vorbestellung als Entwurf, Testbestellung läuft")],
                [mo, di, mi, do, fr, sa, so])


def w20():
    DROP('w20d2t1', 'ersetzt durch den Content-Plan.')
    mo = [O('w20d0t1', id='r7-web-11', c='W'),
          O('w20d0t2', id='r7-web-englisch', c='W', rep=[("Nur bei englischen Hooks (07.11.)", "Nur bei englischen Hooks (Entscheidung So 20.12.)")])]
    di = [O('w20d1t0', id='r7-vorbestellseite-final', c='W', t="Vorbestellseite final (Checkliste 9 von 9), E04 senden und Broadcast",
            add=["E04 ist fertig geschrieben (im Docket). Um 18:00 senden."]),
          O('w20d1t1', id='r7-web-12', c='W'), O('w20d1t2', id='r7-comm-0126'), O('w20d1t3', id='r7-zipper-vorbestellung', c='W')]
    mi = [O('w20d2t0', id='r7-creator-welle-2')]
    do = [O('w20d3t0', id='r7-kaufgrund', c='W'), O('w20d3t1', id='r7-rueckgabe', c='R'), O('w20d3t2', id='r7-comm-0128')]
    fr = [O('w20d4t0', id='r7-generalprobe', c='W'), O('w20d4t1', id='r7-30s-test', c='W'), O('w20d4t2', id='r7-patch-ankunft'),
          O('w20d4t3', id='r7-countdown-sticker')]
    sa = [O('w20d5t1', id='r7-creator-preview')]
    so = [O('w20d6t0', id='r7-review-w20', t="Wochenreview W20, Zahlen ins Cockpit, Zeile an Claude"),
          O('w20d6t1', id='r7-mail-e05', t="E-Mail E05 „Morgen: 18:00 für dich, 19:00 für alle“ senden (18:00)", p=None,
            s=["Text steht fertig im Docket (E05). Entwurf vom Mi 13.01. öffnen, prüfen, um 18:00 senden.", "E06 für Mo 01.02., 18:00 terminieren (Schlüssel-Link testen)."],
            f="E05 raus ist und E06 für Mo 18:00 terminiert ist."),
          O('w20d6t2', id='r7-nachricht-zusagen'), O('w20d6t3', id='r7-gate-start'), O('w20d6t4', id=None)]
    return week(20, "2027-01-25", "M1",
                "Letzte Woche vor dem Start: Seite final, Generalprobe am Fr, Creator-Preview am Sa",
                [("Warteliste", "900 bestätigt (Alarm 360)"), ("Zusagen", "28"), ("Seite", "9 von 9, Testauszahlung da"), ("Handheber", "≥ 40")],
                [mo, di, mi, do, fr, sa, so])


def build():
    return [w12(), w13(), w14(), w15(), w16(), w17(), w18(), w19(), w20()]
