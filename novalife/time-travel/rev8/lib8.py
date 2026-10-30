# -*- coding: utf-8 -*-
"""Bausteine für Docket Rev. 8: Tage, Aufgaben, Links."""
import datetime

START = datetime.date(2026, 10, 26)          # Montag der ersten Woche (Rev. 8 beginnt Fr 30.10.)
DROP = datetime.date(2027, 6, 24)
END = datetime.date(2027, 6, 27)
WD = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']
GH = "https://github.com/Ernest080809/email-bot/blob/claude/time-travel-drop-docket-i92rvk/novalife/time-travel/"


def D(iso):
    return datetime.date.fromisoformat(iso)


def dl(iso, t=None):
    d = D(iso) if isinstance(iso, str) else iso
    return f"{WD[d.weekday()]} {d.day:02d}.{d.month:02d}." + (f" {t}" if t else "")


def week_of(iso):
    return (D(iso) - START).days // 7 + 1


LINKS = {
    'gmail': {"n": "Gmail", "u": "https://mail.google.com"},
    'sheets': {"n": "Tracking-Tabelle", "u": "https://sheets.google.com"},
    'claude': {"n": "Claude", "u": "https://claude.ai"},
    'capcut': {"n": "CapCut", "u": "https://www.capcut.com", "h": "Schnitt, Untertitel, Rückwärts, Geschwindigkeit"},
    'tiktok': {"n": "TikTok", "u": "https://www.tiktok.com"},
    'insta': {"n": "Instagram", "u": "https://www.instagram.com"},
    'meta': {"n": "Meta Business Suite", "u": "https://business.facebook.com", "h": "Reels und Posts im Voraus planen"},
    'shopify': {"n": "Shopify Admin", "u": "https://admin.shopify.com"},
    'gewerbe': {"n": "Service-Portal Berlin · Gewerbeanmeldung", "u": "https://service.berlin.de/dienstleistung/121921/"},
    'elster': {"n": "ELSTER", "u": "https://www.elster.de"},
    'lucid': {"n": "LUCID Verpackungsregister", "u": "https://lucid.verpackungsregister.org"},
    'techpack': {"n": "Tech Pack NVL-TT-01 v1.0 (PDF)", "u": GH + "pdf/NVL-TT-01_TechPack_v1.0.pdf"},
    'masse': {"n": "Maßblätter v1.1 im Kuzgunlar-Format (PDF)", "u": GH + "pdf/NVL-TT-01_Measurements_v1.1.pdf"},
    'artwork': {"n": "Artwork 1:1 v1.9 (PDF)", "u": GH + "pdf/NVL-TT-01_Artwork_1to1_v1.9.pdf"},
    'farben': {"n": "Farbcodes NVL-TT-01 (Dokument)", "u": "https://claude.ai/artifact/2u91Rqmfzc5GiTN5u8kwnv"},
    'callbogen': {"n": "Call-Bogen Kuzgunlar", "u": "https://claude.ai/artifact/JFM6VAsGqryEvVBSSDbPXz#kuzgunlar"},
    'zipper_pt': {"n": "Papiertest Zipper (PDF)", "u": GH + "pdf/NVL-TT-02_Papiertest_Zipper.pdf"},
    'zipper_v2': {"n": "Zipper Designvorschlag v0.2 (PDF)", "u": GH + "pdf/NVL-TT-02_Zipper_Designvorschlag_v0.2.pdf"},
    'messbogen_z': {"n": "Messbogen RL-Zipper", "u": "https://claude.ai/artifact/HtgJUNUmfucqHemECDTTPS"},
    'bibel': {"n": "Video-Bibel (Stunts)", "u": "https://claude.ai/artifact/UEvQ2PrfHn8rwmujfURiTW", "h": "Prinzip, Trick, Sicherheit"},
    'musik': {"n": "TikTok Commercial Music Library", "u": "https://ads.tiktok.com/business/creativecenter/music/pc/en", "h": "nur Titel, die für Business freigegeben sind"},
}


class Plan:
    def __init__(self):
        self.tasks = {}          # iso -> [task]
        self.ids = set()

    def add(self, iso, c, t, m=0, s=(), f=None, o=(), id=None, plus=False, vr=None, e=None, p=None, tm=None, who=None):
        assert id and id not in self.ids, f"ID fehlt oder doppelt: {id}"
        assert START <= D(iso) <= END, (iso, t)
        self.ids.add(id)
        task = dict(id=id, c=c, t=(f"{tm} · " if tm else "") + t, m=m)
        if s: task['s'] = list(s)
        if f: task['f'] = f
        if o: task['o'] = [LINKS[x] if isinstance(x, str) else x for x in o]
        if plus: task['plus'] = True
        if vr: task['vr'] = vr
        if e: task['e'] = e
        if p: task['p'] = p
        if who: task['who'] = who
        task['_tm'] = tm or "99:99"
        self.tasks.setdefault(iso, []).append(task)
        return task

    def note(self, iso, t):
        self.tasks.setdefault(iso, []).append(dict(c='N', t=t, _tm="00:00"))

    def weeks(self, meta):
        """meta: {n: (phase, goal)} -> Liste der Wochen mit Tagen."""
        out = []
        n = 1
        d = START
        while d <= END:
            days = []
            for i in range(7):
                iso = (d + datetime.timedelta(days=i)).isoformat()
                ts = sorted(self.tasks.get(iso, []), key=lambda t: (t['c'] != 'N', t['_tm']))
                days.append([{k: v for k, v in t.items() if k != '_tm'} for t in ts])
            ph, goal = meta[n]
            out.append(dict(n=n, start=d.isoformat(), phase=ph, goal=goal, days=days))
            n += 1
            d += datetime.timedelta(days=7)
        return out
