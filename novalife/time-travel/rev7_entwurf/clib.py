# -*- coding: utf-8 -*-
"""Content-Bausteine Rev. 7: Briefings (VIDS) und Termine (SCHED)."""
import datetime

VIDS = {}
SCHED = []      # dict(id, post=(iso, 'HH:MM'), film=(iso, min) | None, pm=min, plus=bool, kind)
OLDMAP = {}     # alte Video-ID (v35) -> neue ID

TAG = "#novalifetimetravel"
CTA = {
    'liste': ("Link in bio: join the list. The list buys first, 35 pairs at the pre-order price.",
              "Link in Bio: Trag dich ein. Die Liste kauft zuerst, 35 Paar zum Vorbestellpreis."),
    'vor': ("Pre-order is open: 35 pairs at €149, numbered. Link in bio.",
            "Vorbestellung offen: 35 Paar zu 149 €, nummeriert. Link in Bio."),
    'stufe2': ("Pre-order: €169 until Sun 06.06., delivery early June. Link in bio.",
               "Vorbestellen bis So 06.06.: 169 €, Lieferung Anfang Juni. Link in Bio."),
    'drop': ("Drop 24.06., 19:00. The list gets in at 18:00. Link in bio.",
             "Drop 24.06., 19:00. Die Liste kommt um 18:00 rein. Link in Bio."),
    'live': ("Live now. Link in bio.", "Jetzt live. Link in Bio."),
}

KAMERA = "Handy-Hauptkamera 1×, 4K 30 fps (für Zeitlupe 60 fps), Raster an, Linse putzen, Belichtung und Fokus sperren (lange auf das Motiv tippen)."
LICHT_TAG = "Tageslicht vom Fenster seitlich, Deckenlicht aus. Wolkiger Tag ist besser als pralle Sonne."
LICHT_ABEND = "Eine warme Lampe seitlich, Deckenlicht aus, ein weißes A4-Blatt auf der Schattenseite als Aufheller."

REGELN = "Subjekt ist das Muster, nie „wir“ als Volk. Nie „authentisch“, nie „slawisch“ für den Lebensbaum, nach außen „Achtstern“ und „Kreuzstich-Band“. Keine Länder als Herkunft. Kein roter Hintergrund, kein Weizen unter blauem Himmel, keine Sichel. Nur echte Zahlen."

POST_VIDEO = [
    "T−10 Min.: Video mit Ton am Handy ansehen. Untertitel richtig? Kein Fabrikname, keine Adresse, keine Bestell- oder Trackingnummer lesbar?",
    "TikTok (Business-Konto): hochladen, Cover-Bild wählen, Caption einfügen. Musik nur aus der Commercial Music Library und leise unter dem O-Ton. Zur Uhrzeit posten.",
    "Direkt danach: Instagram Reel mit derselben Datei, gleichem Cover, Caption plus deutscher Zeile, „Auch im Feed teilen“ an. Dann YouTube Short, Titel = Hook auf Englisch.",
    "Ersten Kommentar auf allen drei Plattformen posten und anpinnen (Text unten).",
    "Instagram-Story: das Reel teilen, Link-Sticker zur Startseite mit dem Quellen-Tag aus der Story-Zeile unten.",
    "15 Minuten bleiben und jeden Kommentar beantworten. Z, V, Georgsband und Kriegsverherrlichung sofort ausblenden. Kritik nie löschen, sachlich antworten.",
]
POST_STORY = [
    "Instagram → Story → Foto oder Clip aus der Bildspalte unten. Text und Sticker genau wie angegeben.",
    "Sticker immer im mittleren Drittel, nicht vom Profilbild oder der Antwortleiste verdeckt.",
    "Ab 18:00 die Antworten lesen. Jede Antwort mit Größe oder „Ja“ ins Blatt „Die ersten 35“ (nur mit Erlaubnis zum Anschreiben).",
]
MESSEN = ("Nach 24 h ins Blatt „Content“: Views, durchschnittliche Wiedergabedauer, Anteil ganz gesehen, Saves, Shares, neue Follower, "
          "Anmeldungen mit dem Quellen-Tag dieses Videos. Nach 72 h nur noch die Views. Maßstab ist der Median deiner letzten 10 Videos: "
          "gut ab 2 × Median, schwach unter 0,5 × Median.")
VARIANTEN = ("Gut (≥ 2 × Median und Shares über deinem Median): in den nächsten 14 Tagen 5 Varianten, je nur eine Sache anders "
             "(Hook, erstes Bild, Länge, Ton, Cover). Schwach (< 0,5 × Median): nicht nachdrehen, Hook in die Hook-Bank als „schwach“ eintragen.")
STORY_MESSEN = "Am Abend ins Blatt „Content“: Aufrufe der ersten Story, Antworten oder Stimmen, Link-Klicks. Gut: mehr als 10 % der Aufrufe antworten oder stimmen ab."


def dl(iso, t=None):
    d = datetime.date.fromisoformat(iso)
    s = f"{['Mo','Di','Mi','Do','Fr','Sa','So'][d.weekday()]} {d.day:02d}.{d.month:02d}."
    return s + (f" {t}" if t else "")


def V(id, saeule, titel, post, film, *, ziel, hook, alt, beats, dreh, ort, req, schnitt, cover, cap, de, kom, story,
      dauer, kleid=None, licht=None, kamera=None, ton=None, check=None, cta='liste', old=(), plus=False, pm=20,
      messen=None, varianten=None, posten=None, plattform="TikTok → Instagram Reel → YouTube Short", tags="", kind='video'):
    """Video-Briefing. post=(iso, 'HH:MM'), film=(iso, Minuten) oder None (Dreh am Posttag)."""
    assert id not in VIDS, id
    en, deu = CTA[cta] if cta in CTA else (cta, '')
    v = dict(id=id, saeule=saeule, titel=titel, slot=dl(post[0], post[1]), dauer=dauer, plattform=plattform,
             ziel=ziel, hook_en=hook[0], hook_de=hook[1], hook_alt=list(alt), beats=[list(b) for b in beats], dreh=list(dreh),
             ort=ort, req=req, kleid=kleid or "", licht=licht or LICHT_TAG, kamera=kamera or KAMERA,
             ton=ton or "Originalton und deine Stimme. Musik nur aus der Commercial Music Library, sehr leise.",
             schnitt=list(schnitt), cover=cover,
             caption=f"{cap} {en} {TAG} {tags}".strip(), de=f"{de} {deu}".strip(), kommentar=kom, story=story,
             cta=en, check=(check + " " if check else "") + REGELN,
             posten=posten or POST_VIDEO, messen=messen or MESSEN, varianten=varianten or VARIANTEN)
    VIDS[id] = v
    SCHED.append(dict(id=id, post=post, film=film, pm=pm, plus=plus, kind=kind))
    for o in old:
        OLDMAP.setdefault(o, id)
    return v


def S(id, titel, post, *, ziel, frames, folge, old=(), plus=False, pm=10, check=None):
    """Story-Briefing (ASK). frames: [Bild, Text, Sticker]."""
    assert id not in VIDS, id
    v = dict(id=id, saeule='ASK · Story', titel=titel, slot=dl(post[0], post[1]), dauer=f"{len(frames)} Story-Bilder",
             plattform="Instagram-Story (TikTok-Story optional)", ziel=ziel,
             frames=[list(f) for f in frames], folge=folge, posten=POST_STORY, messen=STORY_MESSEN,
             check=(check + " " if check else "") + REGELN)
    VIDS[id] = v
    SCHED.append(dict(id=id, post=post, film=None, pm=pm, plus=plus, kind='story'))
    for o in old:
        OLDMAP.setdefault(o, id)
    return v
