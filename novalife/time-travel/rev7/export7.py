# -*- coding: utf-8 -*-
"""Docket Rev. 7 als Markdown für andere Chats: Tagesplan, Content-Plan, Mails, Design-Inventur, Cockpit."""
import datetime, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import data7 as DT
import lib7, clib, mails, kpi7, inventur7

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'export')
os.makedirs(OUT, exist_ok=True)
CAT = {'G': 'DESIGN', 'B': 'BUILD', 'C': 'CONTENT', 'D': 'ENTSCHEIDUNG', 'A': 'ADMIN', 'R': 'RECHT', 'W': 'WEBSITE', 'S': 'SPIEL', 'V': 'VERKAUF'}
PH = {"A0": "Bisher: Konzept, Freeze, Anfragen", "D1": "Design-Suche", "D2": "Design fertig", "M1": "Marketing, Recht, Muster",
      "M2": "Vorbestellung", "P": "Produktion, Shoot, Abi-Pause", "X": "Countdown und Drop"}
HEAD = "Stand: Docket Rev. 7, veröffentlicht Mi 28.10.2026 (https://claude.ai/artifact/RCciF8jMPSGhgdcQiHAQTm). Aus den Daten der Seite erzeugt."


def one(x):
    return str(x).replace('\n', ' ').strip()


def plan():
    L = [f"# Time Travel · Tagesplan Rev. 7 (W7–W41)\n\n{HEAD}\n",
         "Kategorien: DESIGN, BUILD (Produkt, Fabrik, Muster), CONTENT, ENTSCHEIDUNG, ADMIN, RECHT, WEBSITE, VERKAUF. „Grind+“ ist optional. "
         "Videos, Storys und Mails stehen mit vollem Text in `Content_Plan_Rev7.md` und `Mails_Rev7.md`, hier nur mit ihrer ID.\n"]
    for w in DT.WEEKS:
        if w['n'] < 7:
            continue
        st = DT.D(w['start'])
        L.append(f"\n## W{w['n']} · {PH[w['phase']]} · {st:%d.%m.}–{st + datetime.timedelta(days=6):%d.%m.%Y}\n\n**Wochenziel:** {w['goal']}")
        if w.get('kpi'):
            L.append("**Zahlen bis Sonntag:** " + " · ".join(f"{k['k']}: {k['ziel']}" for k in w['kpi']))
        for di, day in enumerate(w['days']):
            L.append(f"\n### {lib7.dlabel(DT.date_of(w, di))}\n")
            if not day:
                L.append("Frei.")
            for t in day:
                if t.get('c') == 'N':
                    L.append(f"- *Notiz:* {one(t['t'])}")
                    continue
                meta = [CAT.get(t['c'], t['c'])]
                if t.get('m'):
                    meta.append(f"{t['m']} Min.")
                if t.get('plus'):
                    meta.append("Grind+")
                refs = []
                if t.get('vr'):
                    refs.append(f"Briefing {t['vr']}")
                es = t.get('e')
                for e in ([es] if isinstance(es, str) else es or []):
                    refs.append(f"Mail {e}")
                L.append(f"- **{one(t['t'])}** ({', '.join(meta)}){' · ' + ', '.join(refs) if refs else ''} `{t.get('id', '')}`")
                for x in t.get('s', []):
                    L.append(f"  - {one(x)}")
                if t.get('f'):
                    L.append(f"  - *{one(t['f'])}*")
                for o in t.get('o', []) or []:
                    if isinstance(o, dict):
                        L.append(f"  - Link: {o.get('n', '')} {o.get('u', '')}".rstrip())
                if t.get('p'):
                    L.append("  - Prompt an Claude:\n\n    ```\n    " + t['p'].replace('\n', '\n    ') + "\n    ```")
    return "\n".join(L) + "\n"


LBL = [('ziel', 'Ziel'), ('hook_en', 'Hook (EN)'), ('hook_de', 'Hook (DE)'), ('hook_alt', 'Andere Hooks'), ('trick', 'Trick'), ('idee', 'Idee'),
       ('dreh', 'Dreh'), ('prep', 'Vorbereitung'), ('ablauf', 'Ablauf'), ('shots', 'Shots'), ('safety', 'Sicherheit'), ('ort', 'Ort'), ('req', 'Requisiten'),
       ('kleid', 'Kleidung'), ('licht', 'Licht'), ('kamera', 'Kamera'), ('ton', 'Ton'), ('text', 'Text im Bild'), ('schnitt', 'Schnitt'), ('cover', 'Cover'),
       ('caption', 'Caption'), ('de', 'Deutsche Zeile'), ('kommentar', 'Erster Kommentar'), ('story', 'Story'), ('folge', 'Danach'), ('cta', 'CTA'),
       ('posten', 'Posten'), ('messen', 'Messen'), ('varianten', 'Varianten'), ('check', 'Regel-Check')]


def brief_md(v, film=None):
    L = [f"\n## {v['id']} · {v.get('titel', '')}\n", f"{v.get('saeule', '')} · {v.get('slot', '')} · {v.get('dauer', '')} · {v.get('plattform', '')}" + (f" · Dreh: {film}" if film else "")]
    if v.get('beats'):
        L.append("\n| Zeit | Bild | Text im Bild | Ton und Stimme |\n|---|---|---|---|")
        for b in v['beats']:
            L.append("| " + " | ".join(one(c).replace('|', '/') for c in b) + " |")
    if v.get('frames'):
        L.append("\n| # | Bild | Text | Sticker |\n|---|---|---|---|")
        for i, f in enumerate(v['frames'], 1):
            L.append(f"| {i} | " + " | ".join(one(c).replace('|', '/') for c in f) + " |")
    L.append("")
    for k, lab in LBL:
        x = v.get(k)
        if not x or x == "—":
            continue
        if isinstance(x, list):
            L.append(f"**{lab}:**")
            L += [f"{i}. {one(y)}" for i, y in enumerate(x, 1)]
        else:
            L.append(f"**{lab}:** {one(x)}")
    return "\n".join(L)


def content():
    L = [f"# Time Travel · Content-Plan Rev. 7\n\n{HEAD}\n", "Alle Videos, Storys, REWIND-Folgen und Countdown-Tage mit vollem Briefing, nach Posttermin sortiert. Vom 26.10. bis 29.11. wird nichts gepostet.\n"]
    for s in sorted(clib.SCHED, key=lambda x: (x['post'][0], x['post'][1])):
        film = None
        if s.get('film') and s['film'][1] > 0:
            film = lib7.dlabel(s['film'][0])
        L.append(brief_md(clib.VIDS[s['id']], film) + (" \n\n*Grind+, optional.*" if s.get('plus') else "") + (" \n\n*Autopilot: vorproduziert und eingeplant.*" if s.get('auto') else ""))
    L.append("\n# Vorlage für Grind+-Aufgaben\n" + brief_md(clib.VIDS['V299']))
    return "\n".join(L) + "\n"


def mails_md():
    L = [f"# Time Travel · E-Mails an die Liste (Rev. 7)\n\n{HEAD}\n", "Platzhalter in [eckigen Klammern] vor dem Senden mit echten Zahlen füllen. Gesendet wird aus Shopify Email, immer erst als Testmail.\n"]
    for k in sorted(mails.M):
        m = mails.M[k]
        L.append(f"\n## {k} · {m['betreff']}\n\n**Wann:** {m['wann']}  \n**An:** {m['an']}  \n**Vorschau:** {m['vorschau']}  \n**Andere Betreffs:** {' · '.join(m.get('alt', []))}\n\n```\n{m['text']}\n```\n\n**Vor dem Senden:** {m['check']}")
    return "\n".join(L) + "\n"


def inventur_md():
    L = [f"# Time Travel · Design-Inventur (Stand Di 27.10.2026)\n\n{HEAD}\n"]
    for prod, intro, rows in inventur7.INV:
        L.append(f"\n## {prod}\n\n{intro}\n\n| Element | Status | Was gilt | Datei | Offen | Wann |\n|---|---|---|---|---|---|")
        for name, st, was, datei, offen, wann in rows:
            L.append("| " + " | ".join(one(c).replace('|', '/') for c in (name, inventur7.ST[st][1], was, datei, offen, wann)) + " |")
    return "\n".join(L) + "\n"


def cockpit_md():
    L = [f"# Time Travel · Zahlen-Cockpit Rev. 7\n\n{HEAD}\n", "Sonntagswerte. Liste und Follower zählen ab dem Startwert vom So 29.11. In Klammern der Alarmwert.\n",
         "| Sonntag | W | Warteliste | Follower neu | Zusagen | Jeans bezahlt | Prüfpunkt | Wenn nicht |\n|---|---|---|---|---|---|---|---|"]
    for k in kpi7.kpi():
        def z(a, b=None):
            if k[a] is None:
                return "—"
            return f"{k[a]:,}".replace(',', '.') + (f" ({k[b]:,})".replace(',', '.') if b and k.get(b) is not None else "")
        L.append(f"| {lib7.dlabel(k['d'])} | {k['w']} | {z('wl', 'wl_a')} | {z('fo')} | {z('zu')} | {z('pre', 'pre_a')} | {one(k['gate'] or '').replace('|', '/')} | {' · '.join(one(m) for m in k['mass']).replace('|', '/')} |")
    return "\n".join(L) + "\n"


for name, fn in (('Docket_Rev7_Tagesplan.md', plan), ('Content_Plan_Rev7.md', content), ('Mails_Rev7.md', mails_md),
                 ('Design_Inventur.md', inventur_md), ('Cockpit_Rev7.md', cockpit_md)):
    txt = fn()
    open(os.path.join(OUT, name), 'w', encoding='utf-8').write(txt)
    print(f"{name}: {len(txt.encode('utf-8')) / 1024:.0f} KB")
