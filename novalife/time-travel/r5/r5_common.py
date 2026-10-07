# -*- coding: utf-8 -*-
# Docket Rev. 5 · gemeinsame Bausteine
# Aufgabe = [Typ, Titel, Minuten, [Schritte], "Fertig, wenn", "Prompt an Claude" oder ""]
# Typen: B Build/Produktion · C Content · D Entscheidung · A Admin/Shop · S Spiel

def T(typ, titel, minuten=0, schritte=None, fertig="", claude=""):
    return [typ, titel, minuten, list(schritte or []), fertig, claude]

def DONE(typ, text):
    """Vergangene Aufgabe ohne Anleitung (Woche 1–3)."""
    return [typ, text, 0, [], "", ""]

CTA = "Schluss und Caption: „Link in Bio: Trag dich ein. Wer auf der Liste ist, kauft zuerst und zum Vorbestellpreis.“"

# ---------- Posts ----------
# Ein Post wird am Sonntag davor im Content-Batch gedreht und geschnitten.
# Am Posttag ist er nur noch Veröffentlichen + Kommentare (15 Min.).
SLOT_ZEIT = {"BUILD": "18:00", "ORIGIN": "18:00", "REACH": "19:00", "REAL": "18:00", "DETAIL": "18:00", "ASK": "12:00", "LAUNCH": "19:00", "COUNTDOWN": "18:00"}

def P(slot, titel, hook, bilder, laenge="20–30 Sek.", batch=True, cta=CTA, extra=None):
    """Reel/TikTok-Post. bilder = was im Video zu sehen ist."""
    zeit = SLOT_ZEIT[slot]
    schritte = []
    if batch:
        schritte.append("Video liegt fertig im Ordner der Woche (gedreht im Content-Batch am Sonntag).")
    schritte += [
        "Hook als Text in den ersten 2 Sekunden: „%s“" % hook,
        "Im Bild: %s" % bilder,
        "Länge %s, 9:16, Untertitel an." % laenge,
        cta,
        "Um %s auf TikTok und als Instagram Reel posten. Danach 15 Minuten lang jeden Kommentar beantworten." % zeit,
    ]
    if extra:
        schritte += extra
    t = T("C", "%s %s · %s" % (slot, zeit, titel), 15 if batch else 45, schritte,
          "Der Post ist auf beiden Plattformen online und die ersten Kommentare sind beantwortet.")
    t.append({"post": True, "slot": slot, "titel": titel, "hook": hook, "bilder": bilder, "batch": batch})
    return t

def STORY(titel, frage, optionen, extra=None):
    """Instagram-Story mit Umfrage. Kein Dreh nötig."""
    schritte = [
        "Instagram-Story: ein Foto aus der Woche als Hintergrund.",
        "Umfrage-Sticker mit der Frage „%s“ und den Antworten %s." % (frage, optionen),
        "Link-Sticker zur Startseite (Warteliste) dazu.",
        "Ergebnis am Abend notieren (Tracking-Tabelle, Blatt „Content“).",
    ]
    if extra:
        schritte += extra
    t = T("C", "ASK 12:00 · %s" % titel, 10, schritte, "Story ist online, das Ergebnis steht am Abend in der Tabelle.")
    t.append({"post": False})
    return t

def BATCH(naechste_woche_posts, wn, minuten=None, label=None):
    """Sonntags: die Videos der nächsten Woche drehen und schneiden."""
    videos = [p for p in naechste_woche_posts if p[-1].get("post") and p[-1].get("batch")]
    if not videos:
        return None
    m = minuten or (25 * len(videos))
    schritte = [
        "Ordner „W%d“ in deiner Handy-Galerie oder Cloud anlegen." % wn,
    ]
    for i, p in enumerate(videos, 1):
        meta = p[-1]
        schritte.append("Video %d · %s „%s“: %s" % (i, meta["slot"], meta["titel"], meta["bilder"]))
    schritte += [
        "Schneiden in CapCut oder Edits: Hook als Text in die ersten 2 Sekunden, Untertitel automatisch, Länge prüfen.",
        ("Das Video in den Ordner „W%d“ exportieren. Am Posttag wird nichts mehr gedreht." % wn) if len(videos) == 1 else ("Alle Videos in den Ordner „W%d“ exportieren. Am Posttag wird nichts mehr gedreht." % wn),
    ]
    k = len(videos)
    t = T("C", "Content-Batch: %s für %s drehen und schneiden" % ("1 Video" if k == 1 else "%d Videos" % k, label or ("Woche %d" % wn)), m, schritte,
          ("1 fertiges Video liegt im Ordner „W%d“." % wn) if k == 1 else ("%d fertige Videos liegen im Ordner „W%d“." % (k, wn)))
    t.append({"post": False})
    return t

REVIEW_BASIS = [
    "Alles abhaken, was erledigt ist. Was offen ist, Claude schreiben: „Offen aus Woche X: …“. Claude schiebt es sinnvoll in die nächste Woche.",
    "Warteliste: Shopify → Kunden → Filter „E-Mail-Marketing: abonniert“. Zahl in die Tracking-Tabelle, Blatt „Warteliste“.",
    "Content: pro Post Views, Saves, Shares und neue Follower (TikTok und Instagram) ins Blatt „Content“.",
    "Geld: alle Ausgaben der Woche mit Beleg ins Blatt „Ausgaben“.",
]

def REVIEW(wn, extra=None, minuten=20):
    schritte = list(REVIEW_BASIS)
    if wn < 5:
        schritte = [schritte[0]]
    if extra:
        schritte += extra
    t = T("A", "Wochenreview W%d" % wn, minuten, schritte,
          "Tabelle ist aktuell, Offenes ist an Claude gemeldet.")
    t.append({"post": False})
    return t

def strip(task):
    """Metadaten entfernen, bevor es ins JSON geht."""
    return task[:6]

def STATUS(titel, schritte, minuten=10):
    """Story ohne Umfrage (Zwischenstand, Q&A)."""
    t = T("C", titel, minuten, schritte, "Die Story ist online.")
    t.append({"post": False})
    return t

def NOTE(text):
    """Erledigt-Vermerk ohne Checkbox, zählt nicht zum Fortschritt."""
    return ["N", text, 0, [], "", ""]

def CD(n, datum, motiv, live=None):
    """Countdown-Post. Asset vorproduziert in Woche 27, an echten Tagen ersetzt ein Live-Clip das Asset."""
    if live:
        erster = ("Heute ersetzt ein echter Clip das Asset: %s Mit derselben T−%d-Vorlage in CapCut schneiden, 6–10 Sek. "
                  "Passiert es heute doch nicht, nimm das Asset „T−%d“ (%s)." % (live, n, n, motiv))
    else:
        erster = "Asset „T−%d“ aus dem Ordner „Countdown“ (vorproduziert in Woche 27). Motiv: %s." % (n, motiv)
    t = T("C", "Countdown T−%d · %s" % (n, datum), 30 if live else 10, [
        erster,
        "18:00 auf TikTok und als Instagram Reel posten. Caption: „T−%d. Time Travel · 22.04. · 19:00. Link in Bio.“" % n,
        "Dieselbe Datei als Instagram-Story mit Countdown-Sticker (22.04., 19:00) und Link-Sticker zur Startseite. Wer im Sticker auf „Erinnern“ tippt, bekommt um 19:00 eine Nachricht von Instagram.",
        "10 Minuten Kommentare und DMs beantworten.",
    ], "T−%d ist auf TikTok, als Reel und als Story online." % n)
    t.append({"post": False})
    return t
