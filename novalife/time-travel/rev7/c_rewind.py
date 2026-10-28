# -*- coding: utf-8 -*-
"""REWIND-Serie in Rev. 7: Daten aus rev6/build/rewind_data.py, neue Termine."""
import copy, os, sys
for _p in (os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rev6', 'build'), '/home/user/email-bot/novalife/time-travel/rev6/build'):
    if os.path.isdir(_p):
        sys.path.insert(0, _p)
        break
import rewind_data as RD
from clib import VIDS, SCHED, OLDMAP, dl, REGELN, POST_VIDEO, MESSEN, VARIANTEN, TAG

# id: (Dreh (iso, min), Schnitt (iso, min) oder None, Post (iso, Zeit), Making-of iso oder None, Autopilot?)
NEU = {
    'R01': (("2026-12-05", 90), ("2026-12-06", 45), ("2026-12-10", "19:00"), "2026-12-13", False),
    'R03': (("2026-12-12", 60), None, ("2026-12-17", "19:00"), None, False),
    'R02': (("2026-12-18", 15), None, ("2027-01-03", "19:00"), None, False),
    'R08': (("2026-12-26", 120), None, ("2027-03-11", "19:00"), "2027-03-13", False),
    'R09': (("2026-12-27", 45), None, ("2027-04-01", "18:00"), None, True),
    'R10': (("2026-12-30", 90), None, ("2027-04-15", "18:00"), None, True),
    'R11': (("2027-01-08", 120), ("2027-01-09", 45), ("2027-02-01", "20:30"), "2027-02-08", False),
    'R04': (("2027-01-10", 60), None, ("2027-01-14", "19:00"), None, False),
    'R05': (("2027-01-23", 90), None, ("2027-01-28", "19:00"), None, False),
    'R06': (("2027-02-06", 90), None, ("2027-02-11", "19:00"), None, False),
    'R12': (("2027-02-04", 90), None, ("2027-02-16", "19:00"), None, False),
    'R13': (("2027-02-18", 60), None, ("2027-03-02", "19:00"), None, False),
    'R07': (("2027-02-20", 60), None, ("2027-04-29", "18:00"), None, True),
    'R14': (("2027-02-25", 90), None, ("2027-03-16", "19:00"), None, False),
    'R15': (("2027-03-04", 90), None, ("2027-05-20", "19:00"), None, False),
    'R16': (("2027-05-12", 100), None, ("2027-05-13", "19:00"), None, False),
    'R18': (("2027-05-27", 60), None, ("2027-06-05", "12:00"), None, False),
    'R17': (("2027-05-29", 120), None, ("2027-06-01", "19:00"), None, False),
    'R19': (("2027-06-12", 100), None, ("2027-06-15", "19:00"), None, False),
    'R20': (("2027-06-25", 30), None, ("2027-06-26", "19:00"), None, False),
}

FIX = {
    'R11': dict(kleidung="Proto (oder PP, falls es schon da ist)",
                idee="Die Fortsetzung von #01, jetzt mit der echten Jeans. Gleicher Ablauf, gleicher Seitschritt. Nach der Drehung siehst du Patch D, der Gürtel läuft durch. Dann die Endkarte zur Vorbestellung."),
    'R06': dict(idee="Die Fahrstuhltür schließt sich, beim Öffnen trägst du jedes Mal ein anderes Jahrzehnt. Beim letzten Mal geht die Tür auf und es ist dunkel, nur ein Satz leuchtet: „Vorbestellung läuft. 35 Paar zu 149 €.“",
                text="„35 × 149 €“ in der letzten Öffnung · 3 Frames „RW06“ · Endkarte"),
    'R02': dict(ort="Stick-Abend am Fr 18.12., alle Gäste mit Stickrahmen oder Papier auf ihren eigenen Jeans",
                idee="Am Stick-Abend klatschst du, alle Gäste frieren mitten in der Bewegung ein. Du gehst durch den Raum und rückst einem Gast den Stickrahmen zurecht. Du klatschst, alle bewegen sich wieder."),
}


def cta_for(iso):
    if iso < "2027-02-01":
        return "Waitlist: link in bio."
    if iso <= "2027-05-23":
        return "Pre-order open: link in bio."
    if iso <= "2027-06-06":
        return "Pre-order €169 until 06.06.: link in bio."
    return "Drop 24.06., 19:00. Link in bio."


for src in RD.V:
    r = copy.deepcopy(src)
    rid = r['id']
    film, edit, post, mo, auto = NEU[rid]
    r.update(FIX.get(rid, {}))
    cap = r['caption']
    for a in ("Time Travel · 24.06.2027 · waitlist in bio", "Time Travel · 24.06.2027"):
        cap = cap.replace(a, "")
    cap = f"{cap.strip()} {cta_for(post[0])} Time Travel · 24.06.2027 {TAG} #rewind #transition".replace("  ", " ")
    posten = (["Vorproduziert vor der Abi-Pause. In Instagram und TikTok auf " + dl(post[0], post[1]) + " einplanen.", "Kommentare am Sonntag beantworten."]
              if auto else POST_VIDEO + [f"Codewort RW{rid[1:]} steht 3 Frames lang im Video. Wer es im Wartelisten-Formular einträgt, zählt für dieses Video."])
    v = dict(id=rid, saeule="REWIND", titel=f"REWIND #{rid[1:]} · {r['name']}", slot=dl(post[0], post[1]), dauer=r['dauer'],
             plattform="TikTok → Instagram Reel → YouTube Short", trick=r['trick'], idee=r['idee'],
             ziel="Reichweite über einen Trick, der zum Namen Time Travel passt. Jedes REWIND endet mit derselben Signatur: Rückspul-Geräusch, Hand gegen den Uhrzeigersinn, Endkarte TIME TRAVEL · 24.06.",
             hook_en=r['hook_en'], hook_de=r['hook_de'], shots=r['shots'], ort=r['ort'], kleid=r.get('kleidung', ''),
             ton=r['ton'], text=r['text'], prep=r.get('prep', []), ablauf=r.get('ablauf', []), safety=r.get('safety', ''),
             caption=cap, cta=cta_for(post[0]), check=r['check'] + " · " + REGELN,
             posten=posten, messen=MESSEN + " Dazu: Wie viele Einträge mit dem Codewort RW" + rid[1:] + "?", varianten=VARIANTEN,
             kommentar="Reverse. Nobody was in danger. Find the code in the video. 👀")
    VIDS[rid] = v
    SCHED.append(dict(id=rid, post=post, film=film, edit=edit, pm=0 if auto else 15, plus=False, kind='rewind', auto=auto))
    OLDMAP.setdefault(rid, rid)
    if mo:
        mid = rid + "M"
        VIDS[mid] = dict(id=mid, saeule="REWIND · Making-of", titel=f"Making-of REWIND #{rid[1:]}", slot=dl(mo, "18:00"), dauer="15 s",
                         plattform="TikTok + Instagram Reels",
                         ziel="Optional: zeigen, wie der Trick entstand. Beruhigt, wo es nach Gefahr aussah, und bringt eine zweite Welle Views.",
                         hook_en="How we did it. Nobody was in danger.", hook_de="So haben wir's gemacht. Niemand war in Gefahr.",
                         beats=[["0–1 s", "Text auf Schwarz", "RAW vs FINAL", ""], ["1–13 s", "Geteiltes Bild: oben Rohaufnahme, unten Endfassung, gleich lang", "RAW · FINAL", "Originalton der Rohaufnahme, leiser Beat"], ["13–15 s", "Endkarte", "TIME TRAVEL · 24.06.", ""]],
                         dreh=["Kein neuer Dreh: Rohaufnahme und Endfassung aus dem Ordner."],
                         schnitt=["CapCut: Leinwand 9:16, zwei Ebenen übereinander, je 50 % Höhe.", "Beide Clips gleich lang, synchron starten.", "Text „RAW“ oben, „FINAL“ unten."],
                         caption=f"Behind Rewind #{rid[1:]}. Nobody was in danger. {cta_for(mo)} {TAG} #behindthescenes",
                         kommentar="Ask me how any trick works. 🎬", story="Optional.", check="Rohaufnahme zeigt klar, dass niemand in Gefahr war.",
                         posten=POST_VIDEO, messen=MESSEN, varianten=VARIANTEN)
        SCHED.append(dict(id=mid, post=(mo, "18:00" if mid != 'R11M' else "20:00"), film=None, pm=20, plus=True, kind='video'))
        OLDMAP.setdefault(mid, mid)
