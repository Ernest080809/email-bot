# -*- coding: utf-8 -*-
"""Cockpit Rev. 7: Sonntagswerte. Liste und Follower zählen ab dem Marketing-Start (Startwert So 29.11.)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OLDK = {k['d']: k for k in json.load(open(os.path.join(HERE, 'kpi_v35.json'), encoding='utf-8'))}

STD = ["Warteliste unter Soll: bestes Video der Woche in 2 Varianten nachdrehen, Kommentar-Zeit auf 15′, nichts streichen",
       "Warteliste unter Alarm: (a) Netz-Runde an alle Offenen bis Mi · (b) „Bring 3“-Story + DM an alle mit 1–2 Freunden · (c) einen Abend in den nächsten 14 Tagen festmachen · (d) Claude die 3 schwächsten Videos zeigen."]

# d, w, wl, wl_a, fo, zu, pre, pre_a, gate, mass
ROWS = [
 ("2026-11-01", 7, None, None, None, None, None, None, "So 01.11.: 5 Boards der Design-Suche, Baum-Herkunft geklärt, Bestandsaufnahme W5/W6 bei Claude, Kuzgunlar-Call geführt.",
  ["Nicht erfüllt → fehlende Boards bis Mi 04.11. nachholen; ohne schriftlichen Preis wird die Fabrikwahl am Di 03.11. auf Fr 06.11. geschoben."]),
 ("2026-11-08", 8, None, None, None, None, None, None, "Di 03.11.: Fabrik gewählt (spätestens Fr 06.11.) · Do 05.11.: Entwicklung bezahlt · Mo 02.11.: Zipper-Papiertest · Sa 07.11.: Etiketten gewählt.",
  ["Fabrik nicht gewählt → Claude rechnet, was am Proto-Termin rutscht; Papiertest fehlt → Pflicht vor dem Tech Pack Zipper am Do 12.11."]),
 ("2026-11-15", 9, None, None, None, None, None, None, "Fr 13.11.: Digitizing ≤ 28.000 Stiche freigegeben · Do 12.11.: Tech Pack Zipper durchgegangen · Mo 09.11.: Hangtag gewählt · Fr 13.11.: Patch-Muster bestellt.",
  ["Stiche über 28.000 → Gegenrechnung: Füllung statt echtem Kreuzstich, Münztasche offen oder Mehrkosten tragen."]),
 ("2026-11-22", 10, None, None, None, None, None, None, "Mo 16.11.: Zipper-Fabrik, Menge, Preis, Schwelle · Tech Pack Zipper bei der Fabrik · Di 17.11.: Polo-Weg · Mi 18.11.: Website- und Content-Look.",
  ["Zipper-Angebote zu teuer oder zu spät → Plan B: Zipper erst im Drop, nicht in der Vorbestellung."]),
 ("2026-11-29", 11, None, None, None, None, None, None, "Di 24.11.: Gate Stickproben · Mi 25.11.: Waschstandard · So 29.11.: DESIGN-GATE · Startwerte im Cockpit.",
  ["Stickproben rot → benannter Fehler an die Fabrik (neue Probe) oder Fabrik 2 · Design-Gate rot → Claude plant um, Marketing startet trotzdem am Mo 30.11."]),
 ("2026-12-06", 12, 100, 40, 300, None, None, None, "Erste Woche Content: ≥ 60 neue Anmeldungen · Proto verschickt.", STD),
 ("2026-12-13", 13, 180, 70, 540, 5, None, None, "Sa 12.12.: Proto und Fit ok → PP am Mo 14.12. · So 13.12.: Zusagen ≥ 5.",
  ["Proto oder Fit rot → zweites Proto, Vorbestellung bleibt 01.02. mit Proto-Fotos, Sample-Gate rückt."] + STD),
 ("2026-12-20", 14, 260, 100, 780, 10, None, None, "So 20.12.: VALIDIERUNG grün ≥ 250 und ≥ 10 Zusagen · Reservierung A/B · Sprache und Liefergebiet.",
  ["Gelb (100–249) → bis 10.01. nur Ausgaben nach Plan, bestes Video in 3 Varianten · Rot (< 100) → Ausgaben-Stopp außer Patch-Serie, Claude ändert Hooks, Kanäle und Abende."] + STD),
 ("2026-12-27", 15, 320, 120, 960, 12, None, None, "Feiertage: Patch-Serie bestellt, Belege sortiert.", STD),
 ("2027-01-03", 16, 380, 150, 1140, 14, None, None, "So 03.01.: Website Stufe 1 live · PP-Versand bis 08.01. schriftlich · Brücke ja/nein.", STD),
 ("2027-01-10", 17, 480, 190, 1440, 18, None, None, "So 10.01.: Rechtstexte live · LUCID · Zusagen ≥ 18.", STD),
 ("2027-01-17", 18, 600, 240, 1800, 22, None, None, "Fr 15.01.: SAMPLE-GATE (Jeans-PP und Zipper-Muster freigegeben).",
  ["Sample-Gate rot → erst das Muster korrigieren; die Vorbestellung bleibt am 01.02. mit Proto-Fotos, die Bestellung (PO) am 17.02. braucht das freigegebene PP."] + STD),
 ("2027-01-24", 19, 750, 300, 2250, 25, None, None, OLDK["2027-01-24"]['gate'], OLDK["2027-01-24"]['mass']),
 ("2027-01-31", 20, 900, 360, 2700, 28, None, None, OLDK["2027-01-31"]['gate'], OLDK["2027-01-31"]['mass']),
 ("2027-02-07", 21, 1100, 440, 3300, None, 10, 6, OLDK["2027-02-07"]['gate'], OLDK["2027-02-07"]['mass']),
 ("2027-02-14", 22, 1250, 500, 3750, None, 16, 10, OLDK["2027-02-14"]['gate'], OLDK["2027-02-14"]['mass']),
 ("2027-02-21", 23, 1400, 560, 4200, None, 18, 12, OLDK["2027-02-21"]['gate'], OLDK["2027-02-21"]['mass']),
 ("2027-02-28", 24, 1550, 620, 4650, None, 20, 14, "So 28.02.: Stoff da (reserviert seit 18.01.)", OLDK["2027-02-28"]['mass']),
 ("2027-03-07", 25, 1700, 680, 5100, None, 22, 16, OLDK["2027-03-07"]['gate'], OLDK["2027-03-07"]['mass']),
 ("2027-03-14", 26, 1900, 760, 5700, None, 24, 18, "So 14.03.: ≥ 18 Vorbestellungen, Liste ≥ 1.900, Shopify-Email-Kontingent", OLDK["2027-03-14"]['mass']),
 ("2027-03-21", 27, 2050, 820, 6150, None, 26, 21, OLDK["2027-03-21"]['gate'], OLDK["2027-03-21"]['mass']),
]
for i, d in enumerate(["2027-03-28", "2027-04-04", "2027-04-11", "2027-04-18", "2027-04-25", "2027-05-02", "2027-05-09"]):
    ROWS.append((d, 28 + i, 2075 + 25 * i, 830, 6225 + 75 * i, None, 26, 21, "Abi-Pause: keine Gates, Zahlen nur eintragen, wenn du magst", []))
ROWS += [
 ("2027-05-16", 35, 2350, 940, 7050, None, 29, 25, OLDK["2027-05-16"]['gate'], OLDK["2027-05-16"]['mass']),
 ("2027-05-23", 36, 2450, 980, 7350, None, 35, 32, OLDK["2027-05-23"]['gate'], OLDK["2027-05-23"]['mass']),
 ("2027-05-30", 37, 2560, 1050, 7680, None, 37, 35, OLDK["2027-05-30"]['gate'], OLDK["2027-05-30"]['mass']),
 ("2027-06-06", 38, 2700, 1170, 8100, None, 43, None, OLDK["2027-06-06"]['gate'], OLDK["2027-06-06"]['mass']),
 ("2027-06-13", 39, 2820, 1290, 8460, None, None, None, OLDK["2027-06-13"]['gate'], OLDK["2027-06-13"]['mass']),
 ("2027-06-20", 40, 2920, 1400, 8760, None, None, None, OLDK["2027-06-20"]['gate'], OLDK["2027-06-20"]['mass']),
 ("2027-06-27", 41, 3000, 1515, 9000, None, 72, 64, OLDK["2027-06-27"]['gate'], OLDK["2027-06-27"]['mass']),
]


def kpi():
    out = []
    for d, w, wl, wla, fo, zu, pre, prea, gate, mass in ROWS:
        out.append(dict(d=d, w=w, wl=wl, wl_a=wla, fo=fo, zu=zu, pre=pre, pre_a=prea, gate=gate, mass=mass))
    return out
