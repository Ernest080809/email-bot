# -*- coding: utf-8 -*-
"""Mails an die Liste, Rev. 8: Texte aus Rev. 7, neue Termine (Vorbestellung ab Mo 15.02.)."""
import copy, json, os
from content8 import _rep

HERE = os.path.dirname(os.path.abspath(__file__))
M7 = json.load(open(os.path.join(HERE, 'mails7.json'), encoding='utf-8'))

# ID: (Aufgabentag, Uhrzeit, „wann“-Text)
SCHED = {
    'E00': (None, None, "automatisch nach der Bestätigung · Text am Sa 12.12. auf 15.02. ändern"),
    'E02': ('2026-12-19', '13:00', "Sa 19.12., 13:00 (nach dem Post V206)"),
    'E03': ('2027-01-19', '19:30', "Di 19.01., 19:30 (nach der Freigabe)"),
    'E04': ('2027-02-09', '19:30', "Di 09.02., 19:30"),
    'E05': ('2027-02-14', '18:00', "So 14.02., 18:00"),
    'E06': ('2027-02-14', '18:10', "Mo 15.02., 18:00 (am So terminiert)"),
    'E07': ('2027-02-22', '18:00', "Mo 22.02., 18:00"),
    'E09': ('2027-03-16', '19:30', "Di 16.03., 19:30"),
    'E11': ('2027-05-17', '18:00', "Mo 17.05., 18:00"),
    'E12': ('2027-05-22', '20:00', "So 23.05., 12:00 (am Sa terminiert)"),
    'E13': ('2027-05-24', '18:00', "Mo 24.05., 18:00"),
    'E14': ('2027-05-26', '18:00', "Mi 26.05., 18:00, nur an Vorbesteller"),
    'E15': ('2027-06-10', '18:00', "Do 10.06., 18:00"),
    'E16': ('2027-06-17', '18:00', "Do 17.06., 18:00"),
    'E17': ('2027-06-21', '18:00', "Mo 21.06., 18:00"),
    'E18': ('2027-06-23', '18:00', "Mi 23.06., 18:00"),
    'E19': ('2027-06-23', '18:10', "Do 24.06., 18:00 (am Mi terminiert)"),
    'E20': ('2027-06-23', '18:15', "Do 24.06., 19:00 (am Mi terminiert)"),
    'E21': ('2027-06-25', '10:00', "Fr 25.06., 10:00, nur wenn Do 21:00 unter 15 Käufe"),
}
REP = [
    ("Unsicher bei der Größe? Mittwoch, 10.02., 18:00–20:00 ist Mess-Abend 2 in [ORT]. Komm vorbei und probier.",
     "Unsicher bei der Größe? Miss deine Lieblingsjeans flach am Bund und vergleiche mit der Tabelle auf der Produktseite. Oder antworte mir, ich helfe dir."),
    ("Unter 5 verkauft: Betreff „Mess-Abend am Mittwoch“, ohne Zahl.", "Unter 5 verkauft: Betreff „Welche Größe passt dir?“, ohne Zahl."),
    ("· Produktion ab Mitte Februar\n· im März ein Shoot in Berlin\n", "· Produktion ab Mitte März\n"),
    ("Samstag, 15.05., war Mess-Abend 3 [oder: ist Mess-Abend 3, wenn die Mail vorher rausgeht].", ""),
    (" Mess-Abend-Satz an das Datum anpassen.", ""),
    ("Die 100 Paar sind fertig und unterwegs zu mir. Ich prüfe jedes Paar selbst, dann packe ich.",
     "Die [100] Paar sind fertig und einzeln geprüft. [Versandweg A: Unsere Werkstatt schickt dein Paar direkt zu dir. / Versandweg B: Sie kommen nach Berlin, von dort geht dein Paar los.]"),
    ("15.02. nicht genug Vorbestellungen", "14.03. nicht genug Vorbestellungen"),
    ("01.02.2027 um 19:00", "15.02.2027 um 19:00"), ("01.02.", "15.02."), ("31.01.", "14.02."),
    ("08.02.", "22.02."), ("10.02.", "24.02."), ("18.02.", "16.03."), ("20.01.", "19.01."),
    ("Montag, 01", "Montag, 15"),
]
MAILS = {}
for k, (iso, tm, wann) in SCHED.items():
    m = copy.deepcopy(M7[k])
    m = {f: _rep(x, REP) for f, x in m.items()}
    m['wann'] = wann
    if k == 'E14':
        m['check'] = (m.get('check', '') + " Den Satz zum Packen an den Versandweg vom 13.11. anpassen: Schickt Kuzgunlar direkt, schreib „verschickt unsere Werkstatt“.").strip()
    MAILS[k] = m


def gen_tasks(P):
    for k, (iso, tm, wann) in SCHED.items():
        if not iso:
            continue
        m = MAILS[k]
        terminiert = "terminiert" in wann
        P.add(iso, 'V', f"Mail {k} {'terminieren' if terminiert else 'senden'}: {m['betreff']}", 15, id=f"r8-mail-{k}", e=k, tm=tm, s=[
            "Shopify → Marketing → Kampagne erstellen → Shopify Email. Betreff und Text aus dem Kasten unten kopieren, Platzhalter in [eckigen Klammern] mit echten Zahlen füllen.",
            "Erst eine Testmail an dich selbst: Links klicken, Handy-Ansicht prüfen.",
            ("Versand planen auf: " + wann.split(' (')[0] + "." if terminiert else "Senden an: " + m['an'] + "."),
        ], f=f"{k} {'terminiert' if terminiert else 'gesendet'} ist und die Testmail gestimmt hat.", o=['shopify'])
