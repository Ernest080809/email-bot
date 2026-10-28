# -*- coding: utf-8 -*-
"""Bausteine für Docket Rev. 7: alte Aufgaben aus v35 übernehmen, neue anlegen, stabile IDs."""
import copy, datetime, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
V35 = json.load(open(os.path.join(HERE, 'weeks_v35.json'), encoding='utf-8'))
OLD = {}
for w in V35:
    for di, d in enumerate(w['days']):
        for ti, t in enumerate(d):
            OLD[f"w{w['n']}d{di}t{ti}"] = t

USED = {}       # alter Schlüssel -> neue ID (übernommen)
DROPPED = {}    # alter Schlüssel -> Grund
IDS = set()

LINKS = {
    'sheets': {"n": "Tracking-Tabelle", "u": "https://sheets.google.com"},
    'gmail': {"n": "Gmail", "u": "https://mail.google.com"},
    'claude': {"n": "Claude · Projekt „novalife time travel“", "u": "https://claude.ai"},
    'capcut': {"n": "CapCut", "u": "https://www.capcut.com", "h": "Schnitt, Untertitel, Rückwärts, Geschwindigkeit"},
    'tiktok': {"n": "TikTok", "u": "https://www.tiktok.com", "h": "Business-Konto"},
    'insta': {"n": "Instagram", "u": "https://www.instagram.com", "h": "Reel, Story, Broadcast-Kanal"},
    'yt': {"n": "YouTube Studio", "u": "https://studio.youtube.com", "h": "Shorts"},
    'shopify': {"n": "Shopify Admin", "u": "https://admin.shopify.com"},
    'pinterest': {"n": "Pinterest", "u": "https://www.pinterest.com", "h": "geheimes Board anlegen"},
    'arena': {"n": "Are.na", "u": "https://www.are.na", "h": "Alternative zu Pinterest, ohne Werbung"},
    'docket': {"n": "Docket · Abschnitt Design-Inventur", "u": "#inventur"},
    'repo': {"n": "GitHub · email-bot / novalife/time-travel", "u": "https://github.com/ernest080809/email-bot"},
    'messbogen': {"n": "Messbogen RL-Zipper", "u": "https://claude.ai/artifact/HtgJUNUmfucqHemECDTTPS"},
    'bibel': {"n": "REWIND · Video-Bibel", "u": "https://claude.ai/code/artifact/dc9851e3-9c08-43fc-b95f-f7047cc86775", "h": "Konzept, Trick, Sicherheit"},
    'tiktokmusic': {"n": "TikTok Commercial Music Library", "u": "https://ads.tiktok.com/business/creativecenter/music/pc/en", "h": "nur Titel mit „für Business freigegeben“"},
    'elster': {"n": "ELSTER", "u": "https://www.elster.de"},
    'gewerbe': {"n": "Service-Portal Berlin · Gewerbeanmeldung", "u": "https://service.berlin.de/dienstleistung/121921/"},
    'ihk': {"n": "IHK Berlin · Gründung", "u": "https://www.ihk.de/berlin"},
    'lucid': {"n": "LUCID Verpackungsregister", "u": "https://lucid.verpackungsregister.org"},
    'dpma': {"n": "DPMAregister · Markensuche", "u": "https://register.dpma.de"},
}


def _check_id(i):
    assert i not in IDS, f"doppelte ID {i}"
    IDS.add(i)
    return i


def _rep(x, reps):
    if not reps:
        return x
    if isinstance(x, str):
        for a, b in reps:
            x = x.replace(a, b)
        return x
    if isinstance(x, list):
        return [_rep(y, reps) for y in x]
    if isinstance(x, dict):
        return {k: _rep(v, reps) for k, v in x.items()}
    return x


def O(key, id=None, rep=None, add=None, **over):
    """Alte Aufgabe übernehmen. rep: Ersetzungen in allen Texten, add: Schritte anhängen, over: Felder überschreiben."""
    assert key in OLD, key
    assert key not in USED, f"{key} schon übernommen als {USED[key]}"
    t = copy.deepcopy(OLD[key])
    t = _rep(t, rep)
    for k, v in over.items():
        if v is None:
            t.pop(k, None)
        else:
            t[k] = v
    if add:
        t['s'] = list(t.get('s', [])) + list(add)
    if t.get('c') != 'N':
        t['id'] = _check_id(id or f"v35-{key}")
    USED[key] = t.get('id', 'note')
    return t


def DROP(key, why):
    assert key in OLD, key
    assert key not in USED and key not in DROPPED, key
    DROPPED[key] = why


def DROPALL(keys, why):
    for k in keys:
        DROP(k, why)


def T(c, t, id, m=None, s=None, f=None, p=None, o=None, v=None, vr=None, plus=False, x=None):
    """Neue Aufgabe mit stabiler ID."""
    assert c in 'GBCVDARWS', c
    d = {"c": c, "t": t, "id": _check_id(id)}
    if m: d['m'] = m
    if s: d['s'] = s
    if f: d['f'] = f if f.startswith('Fertig, wenn') else 'Fertig, wenn ' + f
    if p: d['p'] = p
    if o: d['o'] = [LINKS[k] if isinstance(k, str) else k for k in o]
    if v: d['v'] = v
    if vr: d['vr'] = vr
    if plus: d['plus'] = True
    if x: d['x'] = x
    return d


def N(t):
    return {"c": "N", "t": t}


DAYS = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']


def week(n, start, phase, goal, kpi, days):
    assert len(days) == 7, n
    return {"n": n, "phase": phase, "start": start, "goal": goal, "kpi": [{"k": a, "ziel": b} for a, b in kpi], "days": days}


def dlabel(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{DAYS[d.weekday()]} {d.day:02d}.{d.month:02d}."
