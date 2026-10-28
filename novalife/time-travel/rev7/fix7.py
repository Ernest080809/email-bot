# -*- coding: utf-8 -*-
"""Docket Rev. 7: alte Termine und Verweise in übernommenen Aufgaben korrigieren. Jede Ersetzung muss treffen."""
import re

import clib
import lib7

FIX = [
    # Mockup-Regel: das Proto kommt jetzt am Di 08.12., danach gibt es echte Fotos
    ('r7-web-3', "(kein Mockup bis 03.12., nie „authentisch“)", "(keine Mockups, nur echte Fotos; nie „authentisch“)"),
    ('r7-web-6', "Kein fertiges Teil, kein Mockup bis 03.12.", "Keine Mockups, nur echte Fotos (Papier, Proto, Stickproben)."),
    ('r7-web-6', "„kein Mockup bis 03.12.“", "„keine Mockups, nur echte Fotos“"),
    ('r7-batch-w12b', "REWIND #01 (G-Klasse): Ist er schon gedreht (Bestandsaufnahme)? Ja: Schnitt prüfen, Post am Do 03.12. Nein: Dreh am Sa 05.12. vormittags mit deinem Vater planen, Post rückt auf Do 10.12.",
     "REWIND #01 (G-Klasse): Dreh am Sa 05.12. vormittags mit deinem Vater festmachen, Post Do 10.12. Ist er schon gedreht (Bestandsaufnahme), prüfst du am Sa nur den Schnitt."),
    ('r7-stickabend', "17:45 aufbauen am Ort vom 05.11.", "17:45 aufbauen am Ort aus der Einladung vom 07.12."),
    ('r7-stickabend', "Erzählen: am 03.12. kommt das Proto.", "Erzählen: Das Proto ist da, das finale Muster kommt im Januar."),
    ('r7-creator-dm', "Das Proto ist seit 03.12. da", "Das Proto ist seit Di 08.12. da"),
    ('r7-pp-bestellen', "Ich brauche das PP spätestens am Mo 04.01.2027 in Berlin und bitte um schriftliche Bestätigung mit Versanddatum bis Mi 09.12.",
     "Ich brauche das PP spätestens am Mi 13.01.2027 in Berlin (Versand bis Fr 08.01.) und bitte um schriftliche Bestätigung mit Versanddatum bis Mi 16.12."),
    ('r7-pp-bestellen', "Betriebspause bis 04.01.", "Betriebspause bis 13.01."),
    # Validierung jetzt So 20.12. mit den Werten aus Rev. 7
    ('r7-validierung-zahlen', "Je Post seit 12.10. (V001–V009 und Grind+)", "Je Post seit Mo 30.11. (V201 bis heute und Grind+; falls im Oktober schon gepostet, V001–V009 dazu)"),
    ('r7-validierung-zahlen', "Neue Follower TikTok + Instagram seit 12.10. ÷ Anmeldungen", "Neue Follower TikTok + Instagram seit dem Startwert vom So 29.11. ÷ Anmeldungen seit Mo 30.11."),
    ('r7-markenkriterien', "Zeile „Validierung 01.11.“", "Zeile „Validierung 20.12.“"),
    ('r7-validierung', "neu seit 25.10.", "neu seit So 13.12."),
    ('r7-validierung', "unter Alarm 50 → G1 · unter Soll 150 → G2", "unter Alarm 100 → G1 · unter Soll 260 → G2"),
    ('r7-validierung', "Maßnahmen wie am 25.10.", "Maßnahmen wie in strategie.md 7.1."),
    ('r7-validierung', "Projekt Time Travel, Docket W7, Validierung und Wochenreview So 01.11.: W7:", "Projekt Time Travel, Docket Rev. 7, W14, Validierung und Wochenreview So 20.12.: W14:"),
    ('r7-validierung', "Offen aus W7:", "Offen aus W14:"),
    ('r7-validierung', "Prüf die Validierung (grün ≥ 150, gelb 50–149, rot unter 50, dazu ≥ 10 Zusagen, 50/50 schriftlich, Markenkriterien)",
     "Prüf die Validierung (grün ab 250 auf der Liste und mindestens 10 Zusagen, gelb 100–249, rot unter 100, dazu 50/50 schriftlich und die Markenkriterien)"),
    ('r7-validierung', "Sag mir die Ampel, was ich Mo 02.11. zahle oder nicht, und schieb das Offene in W8.",
     "Sag mir die Ampel, welche Ausgaben bis So 10.01. laufen dürfen, und schieb das Offene in W15."),
    ('r7-gate-validierung', "Docket W7, So 01.11.:", "Docket Rev. 7, W14, So 20.12.:"),
    ('r7-gate-reservierung', "Nur entscheiden, nicht bauen: Shop, Zahlungen und Rechtstexte kommen erst nach dem Sample-Gate am Di 05.01.",
     "Nur entscheiden, nicht bauen: Zahlungen richtest du am Di 15.12. ein, die Rechtstexte kommen am Di 05.01., die Reservierung baust du im Januar."),
    # Website Stufe 1 geht an Silvester live
    ('r7-web-7', "Live geht die Seite am Mo 18.01.", "Live geht die Seite morgen, Do 31.12."),
    ('r7-presse-nachfassen', "Im Blatt „Presse“: nachgefasst am 05.01.", "Im Blatt „Presse“: nachgefasst am 12.01."),
    # Sample-Gate Fr 15.01.: Recht und Website sind dann schon erledigt
    ('r7-sample-gate', "Ja: Ab morgen läuft der Shop-Block. Gewerbe, Steuer, Zahlungen, Website und Rechtstexte bis So 31.01., die Vorbestellung öffnet Mo 01.02., 19:00.",
     "Ja: Das Muster ist der Standard für alle 100 Paar. Produktseiten (ab Mo 18.01.), Reservierung (ab Mi 20.01.) und Vorbestellung (Mo 01.02., 19:00) laufen wie geplant."),
    ('r7-sample-gate', "Nein: Erst das Muster korrigieren, dann der Shop-Block. Jeans- oder Zipper-Fabrik um ein korrigiertes Muster mit Versanddatum bitten. Jede Woche Verzug schiebt die Vorbestellung um eine Woche, höchstens auf Mo 15.02. (B-Zeitachse 1).",
     "Nein: Erst das Muster korrigieren. Jeans- oder Zipper-Fabrik um ein korrigiertes Muster mit Versanddatum bitten. Die Vorbestellung bleibt am Mo 01.02. mit Proto-Fotos, die Bestellung (PO) am Mi 17.02. braucht das freigegebene PP."),
    ('r7-sample-gate', "Projekt Time Travel, Docket W17, Fr 15.01.", "Projekt Time Travel, Docket Rev. 7, W18, Fr 15.01."),
    ('r7-sample-gate', "Schneide mir den Shop-Block (W17 bis W20) und die Vorbestellung nach B-Zeitachse 1 neu: Was verschiebt sich, was sage ich Creatorn und Zusagen, und wie wandern Schwelle 1 (Mo 15.02.) und die Produktion?",
     "Sag mir, was sich verschiebt (Produktseiten ab Mo 18.01., Vorbestellung Mo 01.02., Bestellung Mi 17.02.), was ich Creatorn und Zusagen sage und wie Schwelle 1 (Mo 15.02.) und die Produktion wandern."),
    ('r7-review-w18', "Shop-Block: welche Schritte fertig, welche offen?", "Shop-Aufgaben: welche Schritte fertig, welche offen?"),
    ('r7-review-w18', "der Stand des Shop-Blocks", "der Stand der Shop-Aufgaben"),
    ('r7-review-w18', "Shop-Block: Gewerbe [ja/nein], Fragebogen [ja/nein], Payments [verifiziert ja/nein],", "Shop: Payments [verifiziert ja/nein], Rechtstexte [live ja/nein],"),
    ('r7-gate-w19', "Gate: Stufe 1 live · Vorbestellung als Entwurf · Testbestellung läuft", "Gate: Produktseiten · Reservierung offen · Vorbestellung als Entwurf · Testbestellung läuft"),
    ('r7-gate-w19', "Stufe 1 live und PLAN B gesichert? Vorbestellung als Entwurf mit Liefertext?",
     "Produktseiten Jeans und Zipper mit echten Bildern? Reservierung offen seit Mi 20.01.? Vorbestellung als Entwurf mit Liefertext?"),
    ('r7-gate-w19', "Fehlt etwas: Der Shop-Block hat bis So 31.01. Vorrang vor allen Grind+-Aufgaben.", "Fehlt etwas: Die Shop-Aufgaben haben bis So 31.01. Vorrang vor allen Grind+-Aufgaben."),
    ('r7-gate-w19', "Liste ≥ 1.000 (Alarm 450)", "Liste ≥ 750 (Alarm 300)"),
    ('r7-review-w19', "Shop-Block: Stufe 1 live? Vorbestellung als Entwurf? Testbestellung gemacht?", "Shop: Produktseiten fertig? Reservierung offen? Vorbestellung als Entwurf? Testbestellung gemacht?"),
    ('r7-gate-w17', "Liste ≥ 850: weiter. Unter Alarm 380 (G1)", "Liste ≥ 480: weiter. Unter Alarm 190 (G1)"),
    ('r7-gate-w17', "Zwischen 380 und 850 (G2)", "Zwischen 190 und 480 (G2)"),
    ('r7-gate-w18', "Liste ≥ 1.000: weiter. Unter Alarm 450 (G1)", "Liste ≥ 600: weiter. Unter Alarm 240 (G1)"),
    ('v35-w26d6t2', "Liste ≥ 850, Kontingent", "Liste ≥ 760, Kontingent"),
    ('v35-w26d6t2', "Liste ≥ 850 (Alarm)?", "Liste ≥ 760 (Alarm)?"),
    ('v35-w38d6t2', "Liste ≥ 2.720 (Alarm 1.170)?", "Liste ≥ 2.700 (Alarm 1.170)?"),
    ('v35-w38d6t2', "· Liste ≥ 2.720", "· Liste ≥ 2.700"),
    ('r7-paypal', "Shopify Payments ist seit Do 07.01. aktiv.", "Shopify Payments ist seit Di 15.12. aktiv."),
    ('r7-web-produkt-zipper', "(Zahlen vom 09.11.)", "(Zahlen vom Mo 16.11.)"),
    ('r7-web-produkt-zipper', "(Sample-Gate 05.01.)", "(Sample-Gate Fr 15.01.)"),
    ('v35-w23d0t3', "Schwelle vom 09.11. erreicht", "Schwelle vom 16.11. erreicht"),
    ('r7-rechtstexte', "8 der Preissatz in V021 („Pre-order price €149 from 01.02. until 23.05.“).", "8 der Preissatz in den Captions ab Februar („Pre-order price €149 from 01.02. until 23.05.“)."),
    ('r7-rechtstexte', "8 Preissatz V021: [..]", "8 Preissatz Captions: [..]"),
    ('r7-rechtstexte', "ob V021 am Fr so raus darf, was das für die Reservierung am So 29.11. heißt",
     "ob der Preissatz so in die Captions ab Februar darf, was das für die Reservierung (Bau Mo 18.01.) heißt"),
    ('r7-po', "reserviert seit 06.01.", "reserviert seit 18.01."),
    ('v35-w24d6t1', "(reserviert seit 06.01.)", "(reserviert seit 18.01.)"),
    ('r7-minishoot-2', "Das ist Ersatzmaterial für V047 am Fr.", "Das ist Material für die Produktseite und den Countdown."),
    ('r7-waschserie', "Das ist Material für V058 „Neun Längen“.", "Das ist Material für V231 „Neun Fäden nach fünf Wäschen“."),
    ('v35-w27d2t0', "V088 „So wird verpackt“ (Mi 12.05.)", "V262 „So kommt dein Paar an“ (Mi 12.05.)"),
    ('v35-w36d1t0', "auf den Drop-Preis vom 09.11. umstellen", "auf den Drop-Preis vom 16.11. umstellen"),
    ('v35-w38d4t0', "Soll laut Spec Rev. 14", "Soll laut Tech Pack v1.0"),
]

FIELDS = ('t', 's', 'f', 'p')
KEEP_OLD_IDS = {'r7-bestand-w5w6'}   # fragt nach den Posts aus W5/W6, die alten Nummern sind dort richtig
RX_OLDVID = re.compile(r'\bV(0\d\d|1[0-2]\d)\b')
RX_HEAD = re.compile(r'Docket (?:Rev\. 7, )?W\d+(?:, (?:Mo|Di|Mi|Do|Fr|Sa|So) \d{2}\.\d{2}\.)?')
RX_REVIEW = re.compile(r'(Docket Rev\. 7, W(\d+), (?:Mo|Di|Mi|Do|Fr|Sa|So) \d{2}\.\d{2}\.)(\s*)W\d+:')


def _map(t, fn, fields=FIELDS):
    for fld in fields:
        v = t.get(fld)
        if isinstance(v, list):
            t[fld] = [fn(x) for x in v]
        elif isinstance(v, str):
            t[fld] = fn(v)


def apply(ALL, IDX, date_of):
    for i, a, b in FIX:
        t = IDX[i][2]
        hit = []
        _map(t, lambda x: (hit.append(1), x.replace(a, b))[1] if a in x else x)
        assert hit, f"FIX trifft nicht: {i}: {a[:60]}"
    for w, di, t in ALL:
        if w['n'] < 7 or t.get('c') == 'N':
            continue
        if t.get('id') not in KEEP_OLD_IDS:
            _map(t, lambda x: RX_OLDVID.sub(lambda m: clib.OLDMAP.get(m.group(0), m.group(0)), x))
        label = f"W{w['n']}, {lib7.dlabel(date_of(w, di))}"
        _map(t, lambda x: RX_REVIEW.sub(lambda m: m.group(1) + m.group(3) + f"W{m.group(2)}:", RX_HEAD.sub(f"Docket Rev. 7, {label}", x)), ('p',))
        _map(t, lambda x: x.replace('V0xx', 'V2xx'))
