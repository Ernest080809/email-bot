# -*- coding: utf-8 -*-
"""Content Rev. 8: Auswahl aus den Rev.-7-Briefings, neue Termine ab dem ersten Proto, Stunts (REWIND) im Mittelpunkt.
Öffentlich ab Di 15.12.2026, bis zur Abi-Pause 2 Posts pro Woche, in der Pause 5 vorproduzierte Posts, danach 3 pro Woche und der Countdown."""
import copy, json, os, re
from lib8 import dl, D

HERE = os.path.dirname(os.path.abspath(__file__))
V7 = json.load(open(os.path.join(HERE, 'vids7_sel.json'), encoding='utf-8'))

AUTO = 'auto'
# (ID, Posttag, Uhrzeit, Dreh (Tag, Minuten) oder None = am Posttag, Optionen)
CP = [
    # ---- öffentlich ab dem Proto ----
    ('V201', '2026-12-15', '19:00', ('2026-11-28', 60), ''),
    ('V206', '2026-12-19', '12:00', ('2026-12-10', 30), ''),
    ('R01', '2026-12-26', '12:00', ('2026-12-21', 120), ''),
    ('R01M', '2026-12-29', '19:00', ('2026-12-28', 30), 'schnitt'),
    ('R08', '2027-01-02', '12:00', ('2026-12-30', 120), ''),
    ('V209', '2027-01-05', '19:00', ('2027-01-03', 30), ''),
    ('R09', '2027-01-09', '12:00', ('2027-01-03', 45), ''),
    ('V210', '2027-01-12', '19:00', ('2027-01-10', 30), ''),
    ('V223', '2027-01-16', '12:00', ('2027-01-13', 20), ''),
    ('V225', '2027-01-19', '19:00', ('2027-01-15', 20), ''),
    ('R07', '2027-01-23', '12:00', ('2027-01-17', 60), ''),
    ('V204', '2027-01-26', '19:00', ('2027-01-17', 30), ''),
    ('R03', '2027-01-30', '12:00', ('2027-01-24', 60), ''),
    ('V230', '2027-02-02', '19:00', ('2027-01-24', 25), ''),
    ('R12', '2027-02-06', '12:00', ('2027-01-31', 90), ''),
    ('V218', '2027-02-09', '19:00', ('2027-01-31', 30), ''),
    ('V232', '2027-02-13', '12:00', ('2027-02-06', 25), ''),
    ('R11', '2027-02-15', '19:00', ('2027-02-07', 120), ''),
    ('V236', '2027-02-20', '12:00', ('2027-02-18', 25), ''),
    ('R11M', '2027-02-23', '19:00', ('2027-02-21', 30), 'schnitt'),
    ('V238', '2027-02-27', '12:00', None, ''),
    ('V231', '2027-03-02', '19:00', ('2027-02-28', 25), ''),
    ('R05', '2027-03-06', '12:00', ('2027-02-28', 90), ''),
    ('V228', '2027-03-09', '19:00', ('2027-03-07', 25), ''),
    ('V240', '2027-03-13', '12:00', None, ''),
    ('V241', '2027-03-16', '19:00', None, ''),
    ('V259', '2027-03-20', '12:00', ('2027-03-14', 20), ''),
    # ---- Abi-Pause: vorproduziert, am So 21.03. eingeplant ----
    ('R13', '2027-03-27', '12:00', ('2027-03-07', 60), AUTO),
    ('V256', '2027-04-03', '12:00', ('2027-03-14', 30), AUTO),
    ('R10', '2027-04-17', '12:00', ('2027-03-13', 90), AUTO),
    ('V258', '2027-04-24', '12:00', ('2027-03-14', 25), AUTO),
    ('V244', '2027-05-08', '12:00', ('2027-03-21', 30), AUTO),
    # ---- Endspurt ----
    ('V260', '2027-05-11', '19:00', ('2027-05-10', 25), ''),
    ('R16', '2027-05-13', '19:00', ('2027-05-12', 100), ''),
    ('V262', '2027-05-15', '12:00', ('2027-05-14', 25), ''),
    ('V264', '2027-05-18', '19:00', ('2027-05-17', 20), ''),
    ('V265', '2027-05-20', '19:00', ('2027-05-17', 25), ''),
    ('V267', '2027-05-22', '12:00', ('2027-05-21', 20), ''),
    ('V268', '2027-05-25', '19:00', ('2027-05-24', 20), ''),
    ('R17', '2027-05-27', '19:00', ('2027-05-22', 120), ''),
    ('V269', '2027-05-29', '12:00', ('2027-05-26', 30), ''),
    ('V271', '2027-06-01', '19:00', ('2027-05-30', 25), ''),
    ('R18', '2027-06-03', '19:00', ('2027-05-30', 60), ''),
    ('V263', '2027-06-05', '12:00', ('2027-06-04', 30), ''),
    ('V261', '2027-06-08', '19:00', ('2027-06-06', 40), ''),
    ('R19', '2027-06-12', '12:00', ('2027-06-10', 100), ''),
] + [(f'CD-T{n:02d}', f'2027-06-{24 - n:02d}', '19:00', ('BATCH', 0), 'cd') for n in range(10, 0, -1)] + [
    ('V272', '2027-06-24', '18:00', None, 'live'),
    ('V273', '2027-06-24', '19:00', None, ''),
    ('R20', '2027-06-26', '12:00', ('2027-06-25', 30), ''),
    ('V277', '2027-06-27', '19:00', ('2027-06-27', 30), ''),
]
CD_BATCH = [('2027-06-13', 90, [f'CD-T{n:02d}' for n in range(10, 4, -1)]), ('2027-06-19', 60, [f'CD-T{n:02d}' for n in range(4, 0, -1)])]

# ---- CTA je Phase ----
CTA = {
    'liste': ("Link in bio: join the list. The list buys first, 35 pairs at the pre-order price.", "Link in Bio: Trag dich ein. Die Liste kauft zuerst, 35 Paar zum Vorbestellpreis.", "Waitlist: link in bio."),
    'vor': ("Pre-order is open: 35 pairs at €149, numbered. Link in bio.", "Vorbestellung offen: 35 Paar zu 149 €, nummeriert. Link in Bio.", "Pre-order open: link in bio."),
    'stufe2': ("Pre-order: €169 until Sun 06.06., delivery early June. Link in bio.", "Vorbestellen bis So 06.06.: 169 €, Lieferung Anfang Juni. Link in Bio.", "Pre-order €169 until 06.06.: link in bio."),
    'drop': ("Drop 24.06., 19:00. The list gets in at 18:00. Link in bio.", "Drop 24.06., 19:00. Die Liste kommt um 18:00 rein. Link in Bio.", "Drop 24.06., 19:00. Link in bio."),
}


def phase_cta(iso):
    if iso < '2027-02-15':
        return 'liste'
    if iso <= '2027-05-23':
        return 'vor'
    if iso <= '2027-06-06':
        return 'stufe2'
    return 'drop'


REP_ALL = [  # zuerst die Sonderfälle, dann das neue Startdatum der Vorbestellung
    ("If too few people pre-order by 15.02., everyone gets their money back in full.", "If the order does not happen, everyone gets their money back in full."),
    ("Papier: „If fewer than 10 by 15.02. → money back“", "Papier: „No order → money back“"),
    ("Pre-order in 14 days: Mon 01.02., 19:00", "Pre-order in 4 weeks: Mon 15.02., 19:00"),
    ("Mon 01.02.", "Mon 15.02."), ("Monday, 01.02.", "Monday, 15.02."), ("Monday 01.02.", "Monday 15.02."),
    ("01.02., 19:00", "15.02., 19:00"), ("· 01.02.", "· 15.02."), ("Mo 01.02.", "Mo 15.02."), ("auf 01.02.", "auf 15.02."),
    ("Aus dem Shoot (06.03.), den Mini-Shoots und der Serienware.", "Aus dem Material seit Dezember und den Marketing-Paaren."),
    ("aus dem Shoot", "aus den Drehs"), ("Fotos aus Shoot und Mini-Shoots, 4:5.", "Fotos aus den Drehs seit Dezember, 4:5."), ("Shoot-Hauptbild", "bestes Foto der Jeans"),
    ("nur Bleach-Teil", "Proto, Patch D im Bild"),
]
OVER = {
    'R01': dict(kleid="Proto der Time-Travel-Jeans, Gürtel durch Patch D",
                prep=["Bis Sa 21.11. mit deinem Vater Tag und Ort festmachen: Mo 21.12. (Ferien), Ausweichtag Di 22.12.",
                      "Kreide, Stativ, ein Freund als Aufpasser, Kennzeichen später unscharf machen. Proto sauber, Gürtel durch Patch D."],
                _shots={3: "Rücken nach der Drehung: Patch D mit Gürtel, B2 mit den Goldfäden"},
                _check=[("keine Time-Travel-Hose", "Patch D und Gürtel im letzten Bild")]),
    'R03': dict(kleid="Proto der Time-Travel-Jeans", _shots={2: "Ende: du bleibst stehen, drehst dich, Patch D und Gürtel im Bild"}),
    'R05': dict(kleid="geliehene Teile aus der Familie oder vom Second-Hand-Laden, zum Schluss das Time-Travel-Muster",
                prep=["Bis So 21.02. vier alte Jeans-Looks leihen oder für wenig Geld kaufen: Schlaghose, Stonewash, Baggy, Low-Rise."],
                _idee=[("dann dein Bleach-Teil", "dann das Time-Travel-Muster")]),
    'R11': dict(kleid="PP-Muster (freigegeben am 15.01.)", prep=["Mit deinem Vater den Termin bis So 31.01. festmachen. Ort und Ablauf wie bei #01.",
                                                                "Kreide, Stativ, Aufpasser, Kennzeichen später unscharf."]),
    'R20': dict(idee="Das Finale: Dein Vater fährt mit der G-Klasse ganz normal vorwärts. Er bringt das erste Paar zu einem Käufer in Berlin (nur mit dessen Ja) oder zur Post. Am Anfang 1 s aus REWIND #01 als Rückblende.",
                prep=["Am Do 24.06. einen Berliner Käufer fragen, ob ihr ihm am Fr 25.06. sein Paar bringen dürft, mit Kamera. Sonst: Paket zur Post."],
                _shots={2: "Übergabe oder Paket, keine Adresse und kein Gesicht ohne Ja"}),
    'V201': dict(_dreh=[("Papiertest Zipper am 02.11.): die Teppich-Drehung vom 02.11.", "Papiertest Zipper am Sa 07.11.): die Teppich-Drehung vom 07.11.")]),
    'V209': dict(_dreh=[("vom So 13.12.", "vom Sa 12.12.")]),
    'V232': dict(hook_de="Noch zwei Tage. So läuft der Montag genau ab."),
    'V259': dict(_dreh=[("Vorher gedreht am Mi 17.03.", "Vorher gedreht am So 14.03.")]),
    'V262': dict(_dreh=[("Probepaket vom Mi 17.03., Ich-Perspektive.", "Probepaket von Kuzgunlar (Versandweg wie am Fr 13.11. entschieden), Ich-Perspektive.")]),
    'V272': dict(ort="Schreibtisch, Handy auf Stativ, Shopify auf dem Laptop daneben"),
}


def _rep(x, reps):
    if isinstance(x, str):
        for a, b in reps:
            x = x.replace(a, b)
        return x
    if isinstance(x, list):
        return [_rep(y, reps) for y in x]
    return x


def fix_cta(v, iso):
    k = phase_cta(iso)
    en, de, short = CTA[k]
    for kk, (e2, d2, s2) in CTA.items():
        if kk == k:
            continue
        for f in ('caption', 'cta', 'de'):
            if isinstance(v.get(f), str):
                v[f] = v[f].replace(e2, en).replace(d2, de).replace(s2, short)
    return v


VIDS, CPLAN = {}, []
for vid, iso, tm, film, opt in CP:
    v = copy.deepcopy(V7[vid])
    v = {k: _rep(x, REP_ALL) for k, x in v.items()}
    for k, x in OVER.get(vid, {}).items():
        if k == '_shots':
            for i, s in x.items():
                v['shots'][i] = s
        elif k == '_check':
            v['check'] = _rep(v['check'], x)
        elif k in ('_idee', '_dreh'):
            f = k[1:]
            v[f] = _rep(v[f], x)
        else:
            v[k] = x
    v = fix_cta(v, iso)
    v['slot'] = dl(iso, tm)
    if opt == AUTO:
        v['posten'] = ["Am So 21.03. in der Meta Business Suite (Instagram) und im TikTok-Planer terminiert. Am Posttag nichts zu tun.",
                       "Kommentare liest du erst nach den Prüfungen, außer du hast 5 Minuten übrig."]
    VIDS[vid] = v
    kind = 'rewind' if vid.startswith('R') and not vid.endswith('M') else ('karussell' if vid in ('V244', 'V261') else ('live' if opt == 'live' else 'video'))
    CPLAN.append(dict(id=vid, post=[iso, tm], film=list(film) if film else None, kind=kind, auto=opt == AUTO, cd=opt == 'cd', schnitt=opt == 'schnitt'))

STUNTS = [c['id'] for c in CPLAN if c['id'].startswith('R')]


def gen_tasks(P):
    """Dreh- und Post-Aufgaben aus dem Content-Plan."""
    for c in CPLAN:
        vid, v = c['id'], VIDS[c['id']]
        name = v['titel']
        stunt = c['kind'] == 'rewind'
        if c['film'] and c['film'][0] != 'BATCH':
            iso, mins = c['film']
            if c['schnitt']:
                P.add(iso, 'C', f"{name} schneiden", mins, id=f"r8-schnitt-{vid}", vr=vid, s=[
                    "Rohaufnahme und Endfassung aus dem Stunt nebeneinander, Schnitt nach dem Briefing unten.",
                    f"Datei „{vid}_final.mp4“ in den Ordner „TT Posts“, Caption als Notiz daneben.", f"Post: {v['slot']}."],
                      f=f"{vid} fertig geschnitten im Ordner liegt.", o=['capcut'])
            else:
                P.add(iso, 'S' if stunt else 'C', f"{name} drehen" if stunt else f"{vid} drehen: {name}", mins, id=f"r8-dreh-{vid}", vr=vid, s=[
                    ("Erst „Sicherheit“ im Briefing lesen, dann Vorbereitung, Ablauf und Shots." if stunt else "Briefing unten: Takte, Dreh, Ort, Requisiten, Kleidung, Licht und Kamera."),
                    f"Rohmaterial ins Album „TT Roh / {vid}“, am selben Tag schneiden: Datei „{vid}_final.mp4“ in den Ordner „TT Posts“, Caption als Notiz daneben.",
                    f"Post: {v['slot']}" + (" (läuft automatisch in der Abi-Pause)." if c['auto'] else ".")],
                      f=f"{vid} fertig geschnitten im Ordner liegt.", o=(['capcut', 'bibel'] if stunt else ['capcut']))
        if c['auto']:
            continue
        iso, tm = c['post']
        if c['kind'] == 'live':
            P.add(iso, 'V', f"LIVE {vid}: {name}", 35, id=f"r8-post-{vid}", vr=vid, tm=tm, f=f"{vid} gelaufen ist und die Zahlen im Blatt „Content“ stehen.", o=['insta', 'tiktok'])
        elif not c['film']:
            P.add(iso, 'C', f"{vid} drehen und posten: {name}", 30, id=f"r8-post-{vid}", vr=vid, tm=tm,
                  f=f"{vid} online ist und der erste Kommentar angepinnt ist.", o=['tiktok', 'insta'])
        else:
            pm = 10 if c['cd'] else 20
            P.add(iso, 'S' if stunt else 'C', f"{name} posten" if stunt else f"{vid} posten: {name}", pm, id=f"r8-post-{vid}", vr=vid, tm=tm,
                  f=f"{vid} auf TikTok, Instagram und YouTube online ist und der erste Kommentar angepinnt ist.", o=['tiktok', 'insta'])
    for iso, mins, ids in CD_BATCH:
        P.add(iso, 'C', f"Countdown drehen: {ids[0]} bis {ids[-1]}", mins, id=f"r8-dreh-cd-{ids[0]}", s=[
            "Jedes Countdown-Video ist 6–9 s lang. Die Briefings stehen im Abschnitt „Content“ unter den IDs.",
            "Neu drehen nur, was im Material seit Dezember fehlt. Alles in einem Durchgang, Reihenfolge nach Ort.",
            f"Alle fertig geschnitten in „TT Posts“: {', '.join(ids)}."], f="alle Countdown-Videos dieser Gruppe fertig im Ordner liegen.", o=['capcut'])
