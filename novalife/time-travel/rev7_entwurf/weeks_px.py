# -*- coding: utf-8 -*-
"""Rev. 7 · W21–W41 (01.02.–27.06.2027): Vorbestellung, Bestellung, Produktion, Abi-Pause, Countdown, Drop.
Die Wochen übernehmen alle Nicht-Content-Aufgaben aus v35 am selben Tag. Content kommt aus dem Content-Plan."""
from lib7 import V35, OLD, O, T, N, DROP, week, LINKS
from mails import M


def is_content(t):
    if t.get('c') != 'C':
        return False
    if t.get('v'):
        return True
    s = t['t']
    return any(k in s for k in ("Variante", "Content-Batch", "Reserve-Post", "Countdown-Assets", "Feld"))


def carry_week(n, phase, goal, kpi, skip=(), over=None, add=None, drop=None):
    """Alle Nicht-Content-Aufgaben der v35-Woche n übernehmen. over: key -> dict für O(). add: Tag -> Liste neuer Aufgaben."""
    over = over or {}
    add = add or {}
    drop = drop or {}
    w = next(x for x in V35 if x['n'] == n)
    days = []
    for di, d in enumerate(w['days']):
        out = []
        for ti, t in enumerate(d):
            k = f"w{n}d{di}t{ti}"
            if k in drop:
                DROP(k, drop[k])
                continue
            if k in skip:
                continue
            if is_content(t) and k not in over:
                continue
            out.append(O(k, **over.get(k, {})))
        out += add.get(di, [])
        days.append(out)
    return week(n, w['start'], phase, goal, kpi, days)


def mail_task(eid, t, id, m=15, wann="", extra=()):
    e = M[eid]
    return T('C', t, id, m=m, s=[
        f"Text steht fertig unten ({eid}). Platzhalter mit echten Zahlen füllen.",
        "Shopify → Marketing → Kampagnen → Shopify Email: Entwurf öffnen oder neu anlegen, Betreff, Vorschau und Text einfügen.",
        f"Empfänger: {e['an']}.",
        f"Button-Links mit utm_source=email&utm_campaign={eid.lower()}.",
        "Testmail an dich, am Handy lesen, Links antippen.",
        f"Senden oder terminieren: {e['wann']}.",
        *extra,
    ], f=f"{eid} wie geplant raus oder terminiert ist und die Testmail gut aussah.", o=['shopify'])


def emb(task, eid):
    task['e'] = M[eid]
    return task


R_PO = [("PP-Freigabe vom 05.01.", "PP-Freigabe vom 15.01."), ("Stoff reserviert seit 06.01.", "Stoff reserviert seit 18.01."), ("(Toleranz Spec 1.1)", "(Toleranz Tech Pack Seite 6)")]


def w21():
    return carry_week(21, "M2", "Vorbestellung öffnet Mo 01.02., 19:00 (Liste 18:00), Mess-Abend 1 am Mi, erste Zahlen",
                      [("Warteliste", "1.100 bestätigt (Alarm 440)"), ("Vorbestellungen", "10 bezahlt (Alarm 6)"), ("Posts", "4 Kern + Stories")],
                      over={
                          'w21d0t0': dict(id='r7-launch', t="17:50 · VORBESTELLUNG: 18:00 Liste, 19:00 öffentlich, Live",
                                          v=None, vr='V235',
                                          rep=[("18:00 geht die geplante Mail „Die Liste kauft zuerst“ an die ganze Liste.", "18:00 geht die terminierte Mail E06 „Du bist drin“ an die ganze Liste."),
                                               ("V052 posten", "V235 posten"), ("V052 online", "V235 online")]),
                          'w21d4t0': dict(id='r7-creator-clips', rep=[("Umgewidmet von „Creator-Anproben terminieren“: Die Clips sind seit 14.02.–09.02. online, jetzt wird gezählt.", "Die Clips der Creator aus der Preview (Sa 30.01.) sind online. Jetzt wird gezählt.")]),
                          'w21d6t0': dict(id='r7-monat-jan', rep=[("(Korridor 1.500 auf der Liste)", "(Korridor 900 auf der Liste)"), ("Korridor 1.500", "Korridor 900")]),
                          'w21d6t2': dict(id='r7-gate-w21', t="Gate: Vorbestellungen ≥ 8 · Liste ≥ 1.100 · Stufe-2-Check",
                                          rep=[("Liste ≥ 1.500: weiter. Unter Alarm 600 (G1)", "Liste ≥ 1.100: weiter. Unter Alarm 440 (G1)")]),
                      })


def w22():
    return carry_week(22, "M2", "Vorbestellung am Laufen halten, Mess-Abend 2 am Mi, Hochrechnung vor der Schwelle",
                      [("Warteliste", "1.250 bestätigt (Alarm 500)"), ("Vorbestellungen", "16 bezahlt (Alarm 10)"), ("Posts", "4 Kern + Stories")],
                      drop={'w22d0t0': 'ersetzt durch E07, fertig geschrieben (r7-mail-e07).', 'w22d1t1': 'ersetzt durch E08, fertig geschrieben (r7-mail-e08).'},
                      add={0: [emb(mail_task('E07', "E-Mail E07 „Noch Y Paar“ mit echter Zahl planen (Versand 18:00)", 'r7-mail-e07'), 'E07')],
                           1: [emb(mail_task('E08', "E-Mail E08 „Eine Frage an dich“ an Abonnenten ohne Kauf (18:00)", 'r7-mail-e08'), 'E08')]},
                      over={'w22d6t1': dict(id='r7-gate-w22')})


def w23():
    return carry_week(23, "M2", "Schwelle nach der Mengenformel, Bestellung mit Endkontroll-Nachweis, Anzahlung, Spiel entscheiden",
                      [("Warteliste", "1.400 bestätigt (Alarm 560)"), ("Vorbestellungen", "18 bezahlt (Alarm 12)"), ("Schwelle", "Mo 15.02. entschieden")],
                      drop={'w23d3t2': 'ersetzt durch E09, fertig geschrieben (r7-mail-e09).'},
                      add={3: [emb(mail_task('E09', "14:00 · Werkstatt-Mail E09 „Bestellt.“ planen (19:00)", 'r7-mail-e09'), 'E09')]},
                      over={'w23d2t0': dict(id='r7-po', rep=R_PO)})


def w24():
    return carry_week(24, "P", "Produktion läuft, Hangtags in Druck, Helfer suchen; Mi 24.02. kein Post",
                      [("Warteliste", "1.550 bestätigt (Alarm 620)"), ("Vorbestellungen", "20 bezahlt (Alarm 14)"), ("Posts", "4 Kern")],
                      drop={'w24d1t1': 'alte Notiz aus Rev. 5.3, erledigt.', 'w24d2t1': 'alte Notiz aus Rev. 5.3, erledigt.'},
                      over={'w24d4t0': dict(id='r7-hangtags-druck', rep=[
                          ("Nur falls noch offen: Nackenlabels für Zipper und Polo (Datei aus W8) bei einem Webetiketten-Anbieter in kleinster Menge bestellen. Vorher den Berliner Sticker fragen, ob er sie beim Besticken einnäht und was das kostet.",
                           "Nackenlabel Zipper macht die Zipper-Fabrik (Tech Pack). Ein Polo-Nackenlabel nur, falls das Polo als Blank mit Berliner Sticker kommt: dann bei einem Webetiketten-Anbieter in kleinster Menge bestellen."),
                          ("Druckdatei öffnen (von Claude, Ordner „Hangtag“).", "Druckdatei öffnen (gewählt am Mo 09.11., Ordner „TT Design final / Hangtag“).")])})


def w25():
    return carry_week(25, "P", "Lookbook-Shoot „Die Hütte“ am Sa 06.03.",
                      [("Warteliste", "1.700 bestätigt (Alarm 680)"), ("Vorbestellungen", "22 bezahlt (Alarm 16)"), ("Shoot", "Sa 06.03., alle Motive")],
                      over={'w25d5t0': dict(id='r7-shoot', v=None, rep=[("Makros später zu Hause am 18. und 22.05.", "Makros später zu Hause am 20. und 22.05."),
                                                                         ("Set Jeans + Zipper + Polo in den 3 Gruppenbildern.", "Set Jeans + Zipper (+ Polo, falls es ein Muster gibt) in den 3 Gruppenbildern.")])})


def w26():
    return carry_week(26, "P", "Kampagnenmaterial fertig, Verpackung und Lizenz, Pressemappe v2",
                      [("Warteliste", "1.900 bestätigt (Alarm 760)"), ("Vorbestellungen", "24 bezahlt (Alarm 18)"), ("Posts", "4 Kern + Story")],
                      drop={'w26d0t1': 'ersetzt durch E10, fertig geschrieben (r7-mail-e10).',
                            'w26d2t0': 'ersetzt durch r7-drop-mails: Die sieben Drop-Mails stehen fertig im Docket (E15–E21).'},
                      add={0: [emb(mail_task('E10', "19:00 · Werkstatt-Mail E10 „Die ersten echten Fotos“ senden", 'r7-mail-e10'), 'E10')],
                           2: [T('C', "Drop-Mails E15–E21 als Entwürfe in Shopify anlegen (nichts terminieren)", 'r7-drop-mails', m=30, s=[
                               "Die sieben Texte stehen fertig im Docket (E15 T−14, E16 T−7, E17 T−3, E18 T−24h, E19 Liste 18:00, E20 LIVE 19:00, E21 Nicht-Öffner).",
                               "Shopify → Marketing → Kampagnen → Shopify Email: sieben Entwürfe, Namen „TT E15 …“ bis „TT E21 …“. Nichts terminieren.",
                               "E19 bekommt den Schlüssel-Link (Website Schritt 15/21), bis dahin Platzhalter.",
                               "Bilder: Hero am 24.06. ist die Totale oder der Patch mit Gürtel. Keine Ernte-Hooks am Drop-Tag.",
                               "Preise für Zipper und Polo erst eintragen, wenn sie feststehen.",
                           ], f="sieben Entwürfe in Shopify Email liegen, keiner terminiert.", o=['shopify'])]},
                      over={'w26d5t2': dict(id='r7-web-14', c='W'), 'w26d1t2': dict(id='r7-verpackungslizenz', c='R')})


def w27():
    return carry_week(27, "P", "Fertige Panels prüfen, Versand aufbauen, Autopilot für die Abi-Pause, Presse-Welle 2",
                      [("Warteliste", "2.050 bestätigt (Alarm 820)"), ("Vorbestellungen", "26 bezahlt (Alarm 21)"), ("Autopilot", "7 Posts eingeplant")],
                      over={
                          'w27d1t3': dict(id='r7-autopilot-1', t="Autopilot für die Abi-Pause (1/2): 4 Posts einplanen",
                                          s=["Fertig geschnitten sind (Content-Aufgaben dieser Woche): V256, R09, V257, R10.",
                                             "In der Meta Business Suite und auf TikTok (Planen im Web) einplanen: V256 Do 25.03. · R09 Do 01.04. · V257 Do 08.04. · R10 Do 15.04., jeweils 18:00.",
                                             "Caption und ersten Kommentar beim Einplanen eingeben."]),
                          'w27d2t2': dict(id='r7-autopilot-2', t="Autopilot für die Abi-Pause (2/2): 3 Posts einplanen, einer davon ehrlich",
                                          s=["V258 Do 22.04. · R07 Do 29.04. · V259 Do 06.05. (der ehrliche), jeweils 18:00.",
                                             "Willkommens-Mail E00 prüfen: Drop-Termin 24.06., Vorbestellung läuft noch bis 23.05. zu 149 €.",
                                             "Story-Highlight „FAQ“ aktualisieren: Lieferung Anfang Juni, Drop 24.06."],
                                          f="7 Posts eingeplant sind, einer pro Woche bis zum 06.05."),
                          'w27d4t3': dict(id='r7-web-15', c='W'), 'w27d5t2': dict(id='r7-web-16', c='W'),
                      })


def abi(n):
    return carry_week(n, "P", "Abi-Pause. Die Fabrik produziert, du schreibst Prüfungen.", [("Abi", "keine Aufgaben, nur 10 Minuten am Sonntag")],
                      over={f'w{n}d6t0': dict(id=f'r7-abi-mails-w{n}')} | ({'w34d6t1': dict(id='r7-neustart')} if n == 34 else {}))


def w35():
    return carry_week(35, "P", "Neustart: Fabrik vor dem Fest, Restzahlung vorbereiten, Mess-Abend 3 am Sa",
                      [("Warteliste", "2.350 bestätigt (Alarm 940)"), ("Vorbestellungen", "29 bezahlt (Alarm 25)"), ("Posts", "4 Kern + Story")],
                      drop={'w35d4t0': 'ersetzt durch E11, fertig geschrieben (r7-mail-e11).'},
                      add={4: [emb(mail_task('E11', "09:00 · E-Mail E11 „149 € endet am Sonntag“ für Mo 17.05., 18:00 planen", 'r7-mail-e11'), 'E11')]},
                      over={'w35d0t2': dict(id='r7-web-17', c='W')})


def w36():
    return carry_week(36, "P", "Restzahlung nach bestandener Endkontrolle, Vorbestellpreis endet So 20:00, Countdown-Assets fertig",
                      [("Warteliste", "2.450 bestätigt (Alarm 980)"), ("Vorbestellungen", "35 bezahlt (Alarm 32 ausgezahlt bis 18.05.)"), ("Countdown", "24 Assets fertig")],
                      drop={'w36d5t2': 'ersetzt durch E12, fertig geschrieben (r7-mail-e12).'},
                      add={5: [emb(mail_task('E12', "E-Mail E12 „Heute 20:00 endet der Vorbestellpreis“ auf So 12:00 terminieren", 'r7-mail-e12'), 'E12')]},
                      over={'w36d2t1': dict(id='r7-web-18', c='W'),
                            'w36d3t0': dict(id='r7-cd-assets-1', v=None, t="Countdown-Assets Teil 1: CD-T24 bis CD-T13 bauen und exportieren",
                                            add=["Briefings je Tag stehen im Content-Plan (CD-T24 … CD-T13). Vorlage „Countdown“ in CapCut, 1 s Zahl, 6 s Bild, 1 s Endkarte."]),
                            'w36d5t0': dict(id='r7-cd-assets-2', v=None, t="Countdown-Assets Teil 2: CD-T12 bis CD-T01 bauen und exportieren",
                                            add=["Briefings je Tag stehen im Content-Plan (CD-T12 … CD-T01)."])})


def w37():
    return carry_week(37, "P", "Ware unterwegs, Lager und Packstation, Support und Werbung stehen, Countdown startet Mo 31.05.",
                      [("Warteliste", "2.560 bestätigt (Alarm 1.050)"), ("Vorbestellungen", "37 bezahlt (Alarm 35)"), ("Ware", "mit Tracking unterwegs")],
                      drop={'w37d0t3': 'ersetzt durch E13, fertig geschrieben (r7-mail-e13).',
                            'w37d2t1': 'ersetzt durch E14, fertig geschrieben (r7-mail-e14).'},
                      add={0: [emb(mail_task('E13', "E-Mail E13 „Bis So 06.06. vorbestellen“ an alle ohne Kauf (18:00)", 'r7-mail-e13'), 'E13')],
                           2: [emb(mail_task('E14', "Vorbesteller informieren: E14 „Deine Time Travel kommt Anfang Juni“ (18:00)", 'r7-mail-e14', m=25), 'E14')]},
                      over={'w37d0t2': dict(id='r7-web-19', c='W'), 'w37d1t0': dict(id='r7-packstation', rep=[("Zeitraffer für V098 filmen", "Zeitraffer für V270 filmen"), ("V098", "V270")]),
                            'w37d3t1': dict(id='r7-helfer', c='R')})


def w38():
    return carry_week(38, "X", "Countdown läuft, Ware annehmen und jede Jeans prüfen, Stufe 2 am So 20:00 schließen",
                      [("Warteliste", "2.700 bestätigt (Alarm 1.170)"), ("Posts", "7 Countdown + REWIND"), ("Ware", "geprüft, Steuer bezahlt")],
                      over={'w38d0t3': dict(id='r7-web-feld', c='W')})


def w39():
    return carry_week(39, "X", "Vorbestellungen raus, Presse-Welle 3, Creator-Pakete, Produktfotos an echten Körpern",
                      [("Warteliste", "2.820 bestätigt (Alarm 1.290)"), ("Versand", "alle Vorbestellungen bis Mi 09.06."), ("Posts", "7 Countdown + REWIND")],
                      drop={'w39d3t0': 'ersetzt durch E15, fertig geschrieben (r7-mail-e15).'},
                      add={3: [emb(mail_task('E15', "10:00 · E-Mail E15 T−14 für heute 18:00 terminieren", 'r7-mail-e15', m=10), 'E15')]},
                      over={'w39d4t1': dict(id='r7-web-20', c='W')})


def w40():
    return carry_week(40, "X", "Letzte Woche vor dem Drop: alles terminieren, alles testen, Sa Code-Freeze",
                      [("Warteliste", "2.920 bestätigt (Alarm 1.400)"), ("Ware", "spätestens Do 17.06. da"), ("Shop", "Bestand aufs Stück, Code-Freeze Sa")],
                      drop={'w40d3t1': 'ersetzt durch E16, fertig geschrieben (r7-mail-e16).', 'w40d0t2': 'Notiz vom 23.10.; Zipper ist Ware aus der Fabrik, Polo nach Polo-Weg.'},
                      add={3: [emb(mail_task('E16', "09:15 · E-Mail E16 T−7 für heute 18:00 terminieren", 'r7-mail-e16', m=10), 'E16')]},
                      over={'w40d2t1': dict(id='r7-drop-startseite', c='W'), 'w40d3t3': dict(id='r7-web-21', c='W')})


def w41():
    return carry_week(41, "X", "Drop-Woche: Do 24.06. 18:00 Liste, 19:00 Drop, packen mit Helfern, Drop-Abend, Auswertung nach 72 Stunden",
                      [("Drop", "37 Käufe brutto bis So 27.06. (Alarm < 29 netto)"), ("Do 21:00", "≥ 15"), ("Fr 19:00", "≥ 26")],
                      drop={'w41d0t0': 'ersetzt durch E17 (r7-mail-e17).', 'w41d2t1': 'ersetzt durch E19 und E20 (r7-mail-e19-20).',
                            'w41d2t2': 'ersetzt durch E18 (r7-mail-e18).', 'w41d4t0': 'ersetzt durch E21 (r7-mail-e21).', 'w41d6t1': 'Notiz vom 23.10., überholt.'},
                      add={0: [emb(mail_task('E17', "09:00 · E-Mail E17 T−3 für heute 18:00 terminieren", 'r7-mail-e17', m=10), 'E17')],
                           2: [emb(mail_task('E18', "09:35 · E-Mail E18 T−24h für heute 18:00 terminieren, dazu Broadcast", 'r7-mail-e18', m=10), 'E18'),
                               emb(mail_task('E19', "09:20 · E19 (Do 18:00, Liste) und E20 (Do 19:00, alle) terminieren", 'r7-mail-e19-20', m=15,
                                             extra=["E20 steht als zweite Mail unten in dieser Aufgabe nicht; Text im Abschnitt E-Mails unter E20."]), 'E19')],
                           4: [emb(mail_task('E21', "10:00 · Nur wenn Do 21:00 unter 15: E21 an die Nicht-Öffner", 'r7-mail-e21', m=10), 'E21')]},
                      over={'w41d3t3': dict(id='r7-drop', rep=[("V101", "V272"), ("V102", "V273"), ("V103", "V274"), ("V107", "V275")])})


def build():
    return [w21(), w22(), w23(), w24(), w25(), w26(), w27()] + [abi(n) for n in range(28, 35)] + [w35(), w36(), w37(), w38(), w39(), w40(), w41()]
