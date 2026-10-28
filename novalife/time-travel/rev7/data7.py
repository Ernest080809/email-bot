# -*- coding: utf-8 -*-
"""Docket Rev. 7, Teil 1: alle Wochen zusammensetzen, Content-Aufgaben aus dem Content-Plan erzeugen, Abdeckung prüfen."""
import copy, datetime, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib7
from lib7 import T
import clib
import c_w12_16, c_w17_21, c_w22_27, c_w35_41, c_rewind  # noqa: F401  (füllen clib.VIDS und clib.SCHED)
import mails
import weeks_d, weeks_m, weeks_px
import kpi7, inventur7
import enrich7
enrich7.apply()

D = datetime.date.fromisoformat

# ---------- Wochen ----------
ARCH = []
for w in lib7.V35:
    if w['n'] <= 6:
        a = copy.deepcopy(w)
        a['phase'] = 'A0'
        ARCH.append(a)
NEW = weeks_d.build() + weeks_m.build() + weeks_px.build()
WEEKS = ARCH + NEW
assert [w['n'] for w in WEEKS] == list(range(1, 42)), [w['n'] for w in WEEKS]
OLDSTART = {w['n']: w['start'] for w in lib7.V35}
for w in WEEKS:
    assert w['start'] == OLDSTART[w['n']], (w['n'], w['start'], OLDSTART[w['n']])
    assert len(w['days']) == 7

DAY = {}
for w in WEEKS:
    for di in range(7):
        DAY[(D(w['start']) + datetime.timedelta(days=di)).isoformat()] = (w, di)

# ---------- Nachträge: v35-Aufgaben, die in den Wochenmodulen noch fehlten ----------
lib7.DROPALL(['w8d1t2', 'w8d3t3', 'w8d5t2', 'w9d1t2', 'w9d3t0', 'w10d1t2', 'w10d3t1', 'w10d5t2', 'w11d1t0', 'w11d3t3'],
             "Design-Phase: Die Community-Runden starten mit dem Marketing am Mo 30.11. (r7-comm-…).")
for k, why in {
    'w8d1t0': "ersetzt durch r7-dateien-fabrik am Fr 06.11., nach der Fabrikwahl.",
    'w8d4t0': "ersetzt durch r7-patch-angebote am Do 12.11.",
    'w9d3t3': "ersetzt durch r7-techpack-zipper (gleicher Tag).",
    'w12d6t1': "ersetzt durch r7-review-w12 (gleicher Tag).",
    'w13d6t0': "ersetzt durch r7-review-w13 (gleicher Tag).",
    'w13d5t2': "ersetzt durch Story S24 „Bring 3“ (gleicher Tag).",
    'w14d3t2': "ersetzt durch r7-comm-1217 (gleicher Tag).",
    'w17d5t3': "ersetzt durch r7-schnitt-R11 (gleicher Tag).",
}.items():
    lib7.DROP(k, why)
# Läden-Runde bleibt als Grind+ am selben Tag; die Absender-Domain muss vor der ersten Mail (E01, Mo 30.11.) stehen.
DAY["2026-11-21"][0]['days'][DAY["2026-11-21"][1]].append(lib7.O('w10d5t3', id='r7-laeden-nudie', plus=True))
DAY["2026-11-24"][0]['days'][DAY["2026-11-24"][1]].append(lib7.O(
    'w18d0t1', id='r7-absender-domain', t="Absender-Domain in Shopify authentifizieren (vor der ersten Mail E01 am Mo 30.11.)",
    rep=[("(vor E-Mail 1 am Di 26.01.)", "(vor der ersten Mail E01 am Mo 30.11.)"), ("vor E-Mail 1 am Di 26.01.", "vor der ersten Mail E01 am Mo 30.11.")]))

# ---------- Vorlage für Grind+-Aufgaben ----------
clib.VIDS['V299'] = dict(
    id='V299', saeule='Grind+ · Vorlage', titel='Antwort-Video oder Variante', slot='an jedem Grind+-Tag, 18:00', dauer='8–20 s',
    plattform='TikTok → Instagram Reel → YouTube Short',
    ziel='Optional. Ein schnelles Video aus dem, was gerade läuft: eine echte Frage aus den Kommentaren beantworten oder das beste Video der Woche in einer Variante nachdrehen.',
    hook_en='„[Kommentar wörtlich]“ – here is the answer.', hook_de='„[Kommentar]“ – hier ist die Antwort.',
    hook_alt=['Version 2 of my best video this week: [eine Sache anders].', 'You asked: [Frage]. 10 seconds.'],
    beats=[['0–2 s', 'TikTok: „Mit Video antworten“, der Kommentar steht als Sticker oben', 'Kommentar-Sticker', 'deine Stimme: die Frage einmal laut'],
           ['2–15 s', 'die Antwort am Teil zeigen: Makro, Hand, Papier oder Datei', 'eine Zeile mit der Antwort', 'Originalton'],
           ['letzte 1 s', 'Endkarte', 'TIME TRAVEL · 24.06.', 'Rückspul-Geräusch']],
    dreh=['Antwort: Kommentar mit einer echten Frage wählen (Größe, Preis, Stoff, Stickerei). Keine Fragen zu Politik oder Herkunft.',
          'Variante: das Video mit den meisten Shares der Woche nehmen und genau eine Sache ändern: Hook, erstes Bild, Länge, Ton oder Cover.',
          '3 Takes, der beste kommt rein. Nicht länger als 20 Minuten.'],
    ort='wo das Teil gerade liegt', req='Handy, das Teil oder die Datei, um die es geht',
    licht=clib.LICHT_TAG, kamera=clib.KAMERA, ton='Originalton und deine Stimme.',
    schnitt=['CapCut-Vorlage BUILD oder DETAIL.', 'Untertitel an, Endkarte wie immer.'],
    cover='der Kommentar groß oder das erste Bild der Variante',
    caption='[Antwort in einem Satz]. ' + clib.CTA['liste'][0] + ' ' + clib.TAG,
    de='[Antwort auf Deutsch in einem Satz].', kommentar='Ask me anything about the jeans. I answer with a video. 🧵',
    story='Optional: Video in die Story teilen.', cta=clib.CTA['liste'][0],
    check='Nur echte Fragen und echte Zahlen. ' + clib.REGELN,
    posten=clib.POST_VIDEO, messen=clib.MESSEN, varianten='Variante nur vom Video mit den meisten Shares, nie von einem schwachen.')

TEMPLATES = {'V299'}
COVER_FILM = {'V201', 'V202', 'V203', 'V204'}   # gedreht in den Content-Batches r7-batch-w12a/b (W11)
COVER_POST = {'V235'}                            # gepostet in r7-launch (Mo 01.02.)


def tkey(t):
    m = re.match(r'\s*(\d{1,2}):(\d{2})', t.get('t', ''))
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None


def put(iso, task, timed):
    assert iso in DAY, (iso, task['t'])
    w, di = DAY[iso]
    day = w['days'][di]
    if not timed:
        day.append(task)
        return
    k = tkey(task)
    pos = len(day)
    for i, t in enumerate(day):
        kk = tkey(t)
        if kk is not None and kk > k:
            pos = i
            break
    day.insert(pos, task)


def move(tid, iso, strip_time=False):
    """Aufgabe aus dem Wochenmodul auf einen anderen Tag legen (Tageslast)."""
    for w in NEW:
        for d in w['days']:
            for t in d:
                if t.get('id') == tid:
                    d.remove(t)
                    if strip_time:
                        t['t'] = re.sub(r'^\s*\d{1,2}:\d{2}\s*·\s*', '', t['t'])
                    put(iso, t, tkey(t) is not None)
                    return
    raise KeyError(tid)


# Versandweg stand bisher nur in der Entscheidungstabelle (Do 29.10.); er gehört vor die Fabrikwahl
put('2026-11-02', T('D', "Versandweg entscheiden: einmal nach Deutschland oder direkt aus der Fabrik zu jedem Kunden?", 'r7-versand-weg', m=10, s=[
    "Claudes Rat: Die Ware kommt als eine Sendung nach Deutschland. Dann packst du selbst oder ein Fulfillment-Dienstleister in Deutschland.",
    "Warum: Direkt aus der Türkei oder China heißt Einfuhrumsatzsteuer und Abfertigung für jedes einzelne Paket, ab 150 € Warenwert auch Zoll, dazu längere Lieferzeit. Retouren brauchen trotzdem eine Adresse in Deutschland.",
    "Deine Entscheidung ins Blatt „Entscheidungen“ und als Bedingung in die Scorecard für morgen: Incoterm DAP Berlin, eine Sendung.",
], f="der Versandweg im Blatt „Entscheidungen“ steht und in der Scorecard für Di 03.11.", o=['sheets']), False)

# Tageslast: Samstag 05.12. (REWIND #01) und Donnerstag 10.12. (Fit-Test) entlasten, Drehs nach der Abi-Pause verteilen
move('r7-creator-1', '2026-12-04', strip_time=True)
move('r7-proto-calls-2', '2026-12-11')
for s in clib.SCHED:
    if s['id'] == 'V262':
        s['film'] = ('2027-05-11', s['film'][1])
    if s['id'] == 'V263':
        s['film'] = ('2027-05-13', s['film'][1])

GEN = []
for s in sorted(clib.SCHED, key=lambda x: (x['post'][0], x['post'][1])):
    vid, v, kind = s['id'], clib.VIDS[s['id']], s['kind']
    titel = v['titel']
    film, edit = s.get('film'), s.get('edit')
    name = titel if kind == 'rewind' else f"{vid}: {titel}"
    if film and film[1] > 0 and vid not in COVER_FILM:
        t = T('C', f"{name} drehen" if kind == 'rewind' else f"{vid} drehen: {titel}", f"r7-dreh-{vid}", m=film[1], vr=vid, plus=s['plus'], s=[
            "Briefing unten: Takte, Dreh, Ort, Requisiten, Kleidung, Licht und Kamera." if kind != 'rewind' else "Briefing unten: Trick, Vorbereitung, Ablauf, Shots und Sicherheit. Erst die Sicherheit lesen.",
            f"Rohmaterial ins Album „TT Roh / {vid}“." + ("" if edit else f" Schneiden nach dem Briefing, Datei „{vid}_final.mp4“ in den Ordner „TT Posts“, Caption als Notiz daneben."),
            f"Post: {v['slot']}.",
        ], f=f"{vid} " + ("im Kasten ist." if edit else "fertig geschnitten im Ordner liegt."))
        put(film[0], t, False)
        GEN.append(t)
    if edit:
        t = T('C', f"{name} schneiden", f"r7-schnitt-{vid}", m=edit[1], vr=vid, plus=s['plus'], s=[
            "Schnitt nach dem Briefing unten: Rückwärts, Geschwindigkeit, Codewort 3 Frames, Signatur am Ende.",
            f"Datei „{vid}_final.mp4“ in den Ordner „TT Posts“, Caption als Notiz daneben.",
            f"Post: {v['slot']}."], f=f"{vid} fertig geschnitten im Ordner liegt.")
        put(edit[0], t, False)
        GEN.append(t)
    if s['pm'] > 0 and vid not in COVER_POST:
        tm = s['post'][1]
        if kind == 'story':
            tt = f"{tm} · Story {vid}: {titel}"
            fw = "die Story online ist und die Antworten im Blatt „Die ersten 35“ oder „Content“ stehen."
        elif kind == 'live':
            tt = f"{tm} · LIVE {vid}: {titel}"
            fw = f"{vid} gelaufen ist und die Zahlen im Blatt „Content“ stehen."
        elif kind == 'rewind':
            tt = f"{tm} · {titel} posten"
            fw = f"{vid} auf allen drei Plattformen online ist und der erste Kommentar angepinnt ist."
        elif kind == 'karussell':
            tt = f"{tm} · Karussell {vid} posten: {titel}"
            fw = f"{vid} auf Instagram und TikTok online ist und der erste Kommentar angepinnt ist."
        elif not film:
            tt = f"{tm} · {vid} drehen und posten: {titel}"
            fw = f"{vid} online ist und der erste Kommentar angepinnt ist."
        else:
            tt = f"{tm} · {vid} posten: {titel}"
            fw = f"{vid} auf allen drei Plattformen online ist und der erste Kommentar angepinnt ist."
        t = T('C', tt, f"r7-post-{vid}", m=s['pm'], vr=vid, plus=s['plus'], f=fw)
        put(s['post'][0], t, True)
        GEN.append(t)

# ---------- Mails: nur die ID in der Aufgabe, der Text steht einmal in MAILS ----------
for w in NEW:
    for d in w['days']:
        for t in d:
            if 'e' in t:
                e = t['e']
                t['e'] = e['id'] if isinstance(e, dict) else e
            if t.get('id') == 'r7-mail-e19-20':
                t['e'] = ['E19', 'E20']
                t['s'] = [x for x in t['s'] if not x.startswith('E20 steht')]

# ---------- Abdeckung: jede v35-Aufgabe ab W7 ----------
CONTENT_DROP = {}
NOTE_DROP = []
UNCOVERED = []
for k, t in lib7.OLD.items():
    n = int(k[1:k.index('d')])
    if n < 7 or k in lib7.USED or k in lib7.DROPPED:
        continue
    if t.get('c') == 'N':
        NOTE_DROP.append(k)
        continue
    if weeks_px.is_content(t):
        vid = (t.get('v') or {}).get('id')
        CONTENT_DROP[k] = clib.OLDMAP.get(vid) if vid else None
        continue
    UNCOVERED.append(k)

ALL = [(w, di, t) for w in WEEKS for di, d in enumerate(w['days']) for t in d]
IDX = {t['id']: (w, di, t) for w, di, t in ALL if t.get('id')}


def date_of(w, di):
    return (D(w['start']) + datetime.timedelta(days=di)).isoformat()


import fix7  # noqa: E402
fix7.apply(ALL, IDX, date_of)


def check():
    errs = []
    if UNCOVERED:
        errs.append(f"nicht abgedeckt: {UNCOVERED}")
    ids = [t['id'] for _, _, t in ALL if t.get('id')]
    if len(ids) != len(set(ids)):
        errs.append("doppelte IDs")
    for w, di, t in ALL:
        if w['n'] >= 7 and t.get('c') != 'N' and not t.get('id'):
            errs.append(f"ohne ID: W{w['n']} {t['t'][:60]}")
        if t.get('vr') and t['vr'] not in clib.VIDS:
            errs.append(f"vr fehlt: {t['vr']}")
        for e in ([t['e']] if isinstance(t.get('e'), str) else t.get('e', [])):
            if e not in mails.M:
                errs.append(f"Mail fehlt: {e}")
        if w['n'] >= 7 and t.get('v'):
            errs.append(f"altes Inline-Video in W{w['n']}: {t.get('id')} {t['v'].get('id')}")
    # Abi-Pause: keine Pflichtaufgaben außer Sonntag
    for w, di, t in ALL:
        iso = date_of(w, di)
        if "2027-03-22" <= iso <= "2027-05-09" and t.get('c') != 'N' and not t.get('plus') and di != 6:
            errs.append(f"Abi-Pause {iso}: {t['t'][:60]}")
    return errs


if __name__ == '__main__':
    print("Wochen", len(WEEKS), "· Aufgaben", sum(1 for _, _, t in ALL if t.get('c') != 'N'),
          "· davon ab W7", sum(1 for w, _, t in ALL if t.get('c') != 'N' and w['n'] >= 7),
          "· erzeugt aus dem Content-Plan", len(GEN))
    print("übernommen", len(lib7.USED), "· gestrichen mit Grund", len(lib7.DROPPED), "· Content ersetzt", len(CONTENT_DROP), "· alte Notizen", len(NOTE_DROP))
    for e in check():
        print("FEHLER", e)
