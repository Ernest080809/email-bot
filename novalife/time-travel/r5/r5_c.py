# -*- coding: utf-8 -*-
# Woche 17–24 · PP-Freigabe, Vorbestellung, Bestellung, Produktion, Shoot, Spiel
from r5_common import *
from r5_a import PW
import r5_b  # füllt PW[10..17]

def wp(n, nur_batch=False):
    l = list(PW[n].values())
    return [p for p in l if p[-1].get("batch")] if nur_batch else l

SPIEL = "Nur wenn in Woche 21 „Spiel bauen“ entschieden wurde. "

PW[18] = {
 0: P("BUILD", "Donnerstag, 19 Uhr",
      "Donnerstag, 19 Uhr. 35 Paar.",
      "PP-Sample am Körper, einmal drehen, dann Bildschirm der Vorbestellseite (Entwurf) mit 149 €", "15 Sek."),
 1: P("ORIGIN", "Vom Teppich auf die Tasche",
      "Ein Muster, das bei allen an der Wand hing.",
      "Teppich-Foto, dann Medaillon-Zeichnung, dann Münztasche E im Makro. Ein Satz pro Bild", "25 Sek."),
 2: P("REACH", "Morgen",
      "Morgen, 19 Uhr.",
      "Trend-Sound, Makro-Schnitte vom PP-Sample, letzter Frame „Morgen 19:00“", "8 Sek."),
 3: P("LAUNCH", "Jetzt offen",
      "Jetzt offen: 35 Paar zu 149 €.",
      "Der beste On-Body-Clip, dann die Vorbestellseite am Handy, dann „Link in Bio“", "10–15 Sek.",
      cta="Caption: „Vorbestellung offen. 35 Paar zu 149 € statt 169 €. Versand 22.–30. April. Link in Bio.“"),
 4: P("DETAIL", "Der Patch",
      "86 × 76 mm. Gestickt auf Leinen.",
      "Makro auf das Muster des Lebensbaum-Patches, langsamer Schwenk vom Stamm zu den Wurzeln", "15 Sek."),
}
PW[19] = {
 0: P("BUILD", "Zwischenstand",
      "X von 35 vorbestellt.",
      "Echte Zahl groß ins Bild, dazu ein kurzer Clip vom PP-Sample. Am Sonntag mit der echten Zahl nachschneiden", "10 Sek."),
 1: P("ORIGIN", "Geschnittener Weizen",
      "Geschnittener Weizen. Deshalb hängen da Fäden.",
      "Makro auf die Gesäßtasche: drei Ähren, rotes Band, Fäden. Dann Schnitt auf die Seitennaht: der Serp im Stoppelfeld. Ein Satz: Hinten die Ernte, an der Seite das Feld danach", "20–25 Sek."),
 2: P("REACH", "Eine Hand",
      "Jede Jeans hat Fäden, die eine Hand gesetzt hat.",
      "Trend-Sound, Fäden in Bewegung, dann Ganzkörper", "8–10 Sek."),
 4: P("DETAIL", "Die Schnittkante",
      "Roh, aber auf Länge geschnitten.",
      "Makro des Saums: rohe, gerade Schnittkante. Ein Satz: Ausgefranst wird sie durchs Tragen, nicht in der Waschmaschine", "15 Sek."),
}
PW[20] = {
 0: P("BUILD", "Noch X Paar",
      "Noch X Paar zum Vorbestellpreis.",
      "Echte Zahl, Clip vom PP-Sample, Kalender mit dem 22.04.", "10 Sek."),
 1: P("ORIGIN", "Warum 100",
      "Warum es nur 100 gibt.",
      "Ein Satz ins Handy: Eine Fabrik, eine Bestellung, nummeriert 001 bis 100. Danach kommt das nächste Muster, nicht dieselbe Jeans nochmal", "20 Sek."),
 2: P("REACH", "POV",
      "POV: Du trägst Nummer 001.",
      "Trend-Sound, Hangtag mit Nummer, dann On-Body", "8 Sek."),
 4: P("DETAIL", "Der Stern",
      "Acht Strahlen, 36 mm, im Kreuzstich.",
      "Makro auf den Alatyr auf der rechten Gesäßtasche", "15 Sek."),
}
PW[21] = {
 0: P("BUILD", "100 oder 75",
      "Diese Woche entscheide ich: 100 Jeans oder 75.",
      "Die Rechnung von Hand: Vorbestellungen × 149 € plus Budget gegen Anzahlung. Ehrlich, ohne Drama", "20 Sek."),
 2: P("REACH", "Bestellt",
      "Gerade 100 Jeans bestellt.",
      "Trend-Sound, Bildschirm mit der gesendeten Bestellung (Namen geschwärzt)", "8 Sek.", batch=False),
 4: P("REAL", "Überwiesen",
      "Gerade die Anzahlung überwiesen. Die Ware gibt es noch nicht.",
      "Überweisung am Bildschirm, Betrag sichtbar, Kontodaten geschwärzt. Ein Satz, wie sich das anfühlt", "15 Sek.", batch=False),
}
PW[22] = {
 0: P("BUILD", "In Produktion",
      "100 Jeans. Ab heute in Produktion.",
      "Fotos aus der Fabrik (Zuschnitt, Stoffballen), dazu der Produktionsplan als Liste", "15 Sek.", batch=False),
 1: P("ORIGIN", "Wie eine Jeans entsteht",
      "Zuschnitt, sticken, nähen, waschen. In dieser Reihenfolge.",
      "Vier Zeichnungen auf Papier, je eine pro Schritt, mit einem Satz. Warum gestickt wird, bevor genäht wird", "25–30 Sek."),
 2: P("REACH", "Stoff",
      "150 Meter Stoff für 100 Jeans.",
      "Trend-Sound, Foto des Stoffs aus der Fabrik, dein Stoffmuster in der Hand", "8 Sek."),
 4: P("DETAIL", "Der Hangtag",
      "Nummer 001 bis 100.",
      "Hangtag-Druckdatei am Bildschirm oder die frisch gedruckten Hangtags", "15 Sek.", batch=False),
}
PW[23] = {
 0: P("BUILD", "Shoot am Samstag",
      "Samstag Shoot. Mit Leuten aus der Community.",
      "Moodboard am Bildschirm, Shotlist auf Papier, das PP-Sample auf dem Bügel", "15 Sek."),
 1: P("ORIGIN", "Der Zipper",
      "Vorn zwei Bänder, hinten der Teppich.",
      "Zipper-Muster vom Berliner Sticker: vorn die Bänder an der Zip-Leiste, hinten das Medaillon (Zeichnung oder Patch-Muster)", "20 Sek."),
 2: P("REACH", "Drei Teile",
      "Jeans, Zipper, Polo. Ein Muster.",
      "Trend-Sound, die drei Muster nebeneinander auf dem Boden", "8 Sek."),
 4: P("DETAIL", "Der Polo",
      "Zwei Bänder an der Knopfleiste.",
      "Makro vom Polo-Muster", "15 Sek."),
}
PW[24] = {
 0: P("BUILD", "Hinter den Kulissen",
      "So sah der Shoot wirklich aus.",
      "Behind-the-scenes-Clips vom Samstag, schnell geschnitten", "15–20 Sek."),
 2: P("REACH", "Das erste Bild",
      "Das erste Bild aus dem Shoot.",
      "Trend-Sound, das stärkste Shoot-Bild, langsam reingezoomt", "8 Sek."),
 4: P("DETAIL", "Kampagnenfilm",
      "Time Travel. 22. April, 19 Uhr.",
      "Der Kampagnenfilm, 30–45 Sekunden, ein Sound, kaum Text (geschnitten am Donnerstag)", "30–45 Sek.", batch=False),
}

# ---------- Woche 17 ----------
W17 = dict(n=17, phase="P3", goal="PP-Sample freigeben, Vorbestellung ankündigen", days=[
 [T("B", "PP-Sample prüfen", 75, [
    "Auspacken filmen (für den BUILD-Post heute).",
    "Prüfplan komplett: 10 Messpunkte, alle Stick-Elemente, Goldfäden (Zugtest: sanft ziehen, nichts darf sich lösen), Labels, Knopf, Nieten, Saum.",
    "Liegen alle Korrekturen aus Woche 13 vor? Jede einzelne abhaken.",
    "Ergebnisse ins Blatt „Proto“, Spalte „PP“.",
   ], "Jeder Punkt des Prüfplans hat ein Ergebnis."),
  PW[17][0]],
 [T("D", "PP-Sample freigeben", 30, [
    "Alles in Toleranz, alle Korrekturen drin: schriftlich „PP sample approved“ mit Fotos und Maßprotokoll.",
    "Kleine Abweichungen: „approved with comments“ und die Liste dazu.",
    "Große Abweichungen: dritte Runde. Kostet 2–3 Wochen. Dann mit Claude den Zeitplan neu schneiden, bevor die Vorbestellung öffnet.",
   ], "Die Freigabe (oder die dritte Runde) ist schriftlich raus."),
  PW[17][1]],
 [T("B", "Bestellkonditionen festzurren", 30, [
    "Schriftlich anfordern: Preis bei 100 Stück (und bei 75 als Plan B), Zahlung 50/50, Liefertermin ab Anzahlung, Stoff für 100 Paar reserviert.",
    "Ramadan-Fest: in der Türkei offiziell 8. März ab mittags bis 11. März 2027. Viele Fabriken machen länger zu. Fragen: Wann genau seid ihr zu?",
    "DDP-Preis bestätigen lassen (Lieferung bis Berlin, Zoll und Einfuhr erledigt). Bei der ersten Bestellung ist das am einfachsten.",
   ], "Preis, Zahlung, Termin und Feiertage stehen schriftlich."),
  PW[17][2]],
 [T("A", "Vorbestellseite final, E-Mail 1 senden", 45, [
    "PP-Fotos rein, Texte lesen, Größenseite verlinkt, Lieferfenster 22.–30.04. steht oben.",
    "18:00 E-Mail 1 („Nächsten Donnerstag öffnet die Vorbestellung“) an alle Abonnenten.",
   ], "Seite ist fertig (Status Entwurf), E-Mail 1 ist raus.")],
 [T("B", "Zipper-Rücken bis zum Shoot fertig machen", 20, [
    "Gestickt (Entscheidung Woche 14): Zipper-Muster zum Berliner Sticker bringen, Medaillon auf den Rücken (Datei von Claude). Abholen spätestens Fr 12.02., der Shoot ist am 20.02.",
    "Chenille: Ist der Muster-Patch da? Vom Sticker oder einer Schneiderei annähen lassen, nicht aufbügeln. Dahinter ein Stabilisatorstreifen.",
    "Abholtermin in den Kalender.",
   ], "Der Zipper ist beim Sticker oder beim Schneider, der Abholtermin steht."),
  PW[17][4]],
 [PW[17][5]],
 [REVIEW(17), BATCH(wp(18, True), 18, 100)],
])

# ---------- Woche 18 ----------
W18 = dict(n=18, phase="P3", goal="Die Vorbestellung öffnet am Donnerstag", days=[
 [T("A", "Generalprobe Vorbestellung", 30, [
    "Vorbestell-Produkt kurz auf „Aktiv“ stellen, aber nirgends verlinken.",
    "Ein Freund kauft am Handy W32. Du erstattest sofort.",
    "Prüfen: 149 €, Lieferfenster sichtbar, Größenseite verlinkt, Bestätigungsmail nennt das Lieferfenster.",
    "Bestand um das Testpaar korrigieren, Produkt zurück auf „Entwurf“.",
   ], "Der Testkauf hat geklappt, Bestand stimmt wieder."),
  PW[18][0]],
 [PW[18][1]],
 [T("A", "E-Mail 2 „Morgen 19 Uhr“", 10, [
    "Shopify Email: Entwurf 2 an alle Abonnenten, Versand heute 18:00.",
   ], "E-Mail 2 ist geplant."),
  PW[18][2]],
 [T("C", "19:00 VORBESTELLUNG ÖFFNET", 120, [
    "17:55 Produkt auf „Aktiv“ stellen, Bestand 35 prüfen.",
    "18:00 E-Mail 3 an die Warteliste: eine Stunde früher.",
    "19:00 Launch-Post (unten) und Story mit Link-Sticker.",
    "Bis 21:00 jede Frage innerhalb von 30 Minuten beantworten.",
    "21:00 Zwischenstand in die Story: „X von 35“. Nur echte Zahlen.",
   ], "Die Vorbestellung ist offen, die ersten Bestellungen sind da."),
  PW[18][3]],
 [T("A", "Bestellungen ins Blatt „Pre-Order“", 15, [
    "Pro Bestellung: Datum, Größe, Betrag, Land.",
    "Summe und Stand „X von 35“ oben ins Blatt.",
   ], "Alle Bestellungen stehen in der Tabelle."),
  PW[18][4]],
 [STATUS("Zwischenstand-Story", ["Echte Zahl „X von 35“ als Story, dazu ein Foto vom PP-Sample.", "Link-Sticker zur Vorbestellung."])],
 [REVIEW(18, ["Tempo: Bestellungen pro Tag seit Donnerstag. Hochrechnung bis So 31.01.: reicht es für mindestens 10?"]), BATCH(wp(19, True), 19)],
])

# ---------- Woche 19 ----------
W19 = dict(n=19, phase="P3", goal="Die Vorbestellung am Laufen halten", days=[
 [T("A", "E-Mail 4 „Noch X Paar“", 10, [
    "Shopify Email: Entwurf 4 mit der echten Zahl an alle, die noch nicht gekauft haben.",
    "Versand 18:00.",
   ], "E-Mail 4 ist geplant."),
  PW[19][0]],
 [T("D", "Tempo bewerten", 20, [
    "Unter 10 Bestellungen nach 5 Tagen: jetzt handeln. 100 € aus dem Puffer auf das Video mit der höchsten Haltequote, 7 Tage, nur Deutschland, Ziel: Besuche der Vorbestellseite.",
    "10 oder mehr: weiter so, kein Geld ausgeben.",
    "Entscheidung ins Blatt „Pre-Order“.",
   ], "Die Entscheidung steht in der Tabelle."),
  PW[19][1]],
 [T("C", "5 Creator anfragen", 45, [
    "5 Micro-Creator auswählen: 2.000–20.000 Follower, Denim, Vintage oder Streetwear, Berlin oder deutschsprachig.",
    "Vorlage „Creator-DM“ (Referenz → Vorlagen). Angebot: Anprobe des PP-Samples in Berlin, Clip gegen Nennung, ein Paar aus der Serie im April.",
    "Jedes geschenkte Paar kostet dich ~63 € und ein Verkaufsstück. Höchstens 5.",
    "Ins Blatt „Creator“ (neu).",
   ], "5 DMs sind raus."),
  PW[19][2]],
 [T("A", "Rückgabe festlegen", 30, [
    "Rücksendeadresse, Frist (14 Tage Widerruf), Zustand (ungetragen, Hangtag dran), Rücksendekosten: Empfehlung, die trägt der Kunde.",
    "Als eigene Seite „Rückgabe“ im Shop und in den FAQ verlinken.",
   ], "Die Seite „Rückgabe“ ist online.")],
 [PW[19][4]],
 [STATUS("Story-Q&A", ["Fragen-Sticker: „Frag mich alles zum Drop“.", "30 Minuten lang alle Fragen beantworten, danach als Highlight „DROP INFO“ sichern."], 30)],
 [REVIEW(19), BATCH(wp(20, True), 20)],
])

# ---------- Woche 20 ----------
W20 = dict(n=20, phase="P3", goal="Endspurt bis zur Schwelle am 1. Februar", days=[
 [T("C", "Creator-Anproben terminieren", 30, [
    "Mit allen, die zugesagt haben, einen Termin in Berlin (je 30 Minuten) für diese oder nächste Woche.",
    "PP-Sample mitbringen. Sie filmen, du filmst Behind the Scenes.",
   ], "Termine stehen im Kalender."),
  PW[20][0]],
 [T("C", "E-Mail an Abonnenten ohne Kauf", 20, [
    "Shopify → Kunden: Segment „abonniert, keine Bestellung“.",
    "Kurze E-Mail: noch X Paar zum Vorbestellpreis, ein Bild, ein Button. Text bei Claude holen.",
   ], "Die E-Mail ist geplant."),
  PW[20][1]],
 [T("C", "Persönliche DMs", 45, [
    "Alle, die je kommentiert oder auf die Story geantwortet haben, aber nicht bestellt haben.",
    "Einzeln, nicht kopiert, ein Satz mit Bezug auf ihren Kommentar. 20–40 Nachrichten.",
   ], "Mindestens 20 persönliche DMs sind raus."),
  PW[20][2]],
 [T("A", "Hochrechnung Cash-Schwelle", 20, [
    "Kontostand plus Vorbestellungen gegen die Anzahlung laut Proforma. Planwert: bei 50/50 ca. 3.000 €, bei 60/40 ca. 3.600 € (Fabrikpreis ~60 € pro Paar, der Patch ist schon bezahlt).",
    "Ergebnis: reicht, knapp oder fehlt. Bei „fehlt“: Claude fragen, ob 75 Stück oder 2 Wochen schieben besser ist.",
   ], "Du weißt, ob die Anzahlung am Montag gedeckt ist.")],
 [PW[20][4]],
 [STATUS("Zwischenstand-Story", ["Echte Zahl „X von 35“.", "Link-Sticker zur Vorbestellung."])],
 [T("A", "Monatsabschluss Januar", 15, [
    "Warteliste gegen Ziel 1.500. Vorbestellungen gegen Minimum (10 bis heute). Morgen ist die Schwelle.",
   ], "Beide Zahlen stehen in der Tabelle."),
  REVIEW(20), BATCH(wp(21, True), 21)],
])

# ---------- Woche 21 ----------
W21 = dict(n=21, phase="P3", goal="Schwelle prüfen, bestellen, anzahlen", days=[
 [T("D", "SCHWELLE: 100, 75 oder schieben", 30, [
    "Rechnung: Budget übrig laut Blatt „Ausgaben“ (Plan: ca. 1.990 €) plus eingenommene Vorbestellungen, gegen die Anzahlung und den Shoot (150 €).",
    "Reicht es für die Anzahlung: 100 Stück.",
    "Knapp darunter: 75 Stück. Vorher die Fabrik nach dem Preis bei 75 fragen, er steigt pro Stück.",
    "Weit darunter: Anzahlung 2 Wochen schieben, Vorbestellung läuft weiter. Liefertermin mit der Fabrik neu prüfen.",
    "Für die Restzahlung am 19.03. brauchst du mindestens 32 Vorbestellungen. Sind bis heute schon mehr als 25 verkauft: Kontingent von 35 auf 45 erhöhen. Jede weitere Vorbestellung bringt 20 € weniger, aber das Geld kommt vor der Restzahlung.",
    "Entscheidung Claude schreiben.",
   ], "Die Menge steht fest."),
  PW[21][0]],
 [T("B", "Größensplit aus den Vorbestellungen", 30, [
    "Blatt „Pre-Order“ mit dem Prompt unten an Claude.",
    "Den Split einmal gegenlesen: Gibt es eine Größe mit 0 Vorbestellungen? Dann trotzdem mindestens 5 Stück.",
   ], "Der Split pro Größe steht.",
   "Hier sind meine Vorbestellungen nach Größe: … Rechne den Split für 100 (bzw. 75) Paar hoch. Basis ist die Startannahme 14/30/30/18/8, gewichtet mit den echten Daten.")],
 [T("B", "Bestellung (PO) senden", 30, [
    "PO mit dem Prompt unten bei Claude holen.",
    "An die Fabrik mit der Bitte um schriftliche Bestätigung: Mengen, Preis, Liefertermin.",
    "In derselben Mail fragen: Sind die 110 Label-Patches angekommen und gezählt? Sonst beim Patch-Anbieter nachhaken, heute noch.",
   ], "Die PO ist raus.",
   "Schreib mir die Purchase Order auf Englisch: Style NVL-TT-01, Mengen pro Größe …, Stückpreis …, Zahlung 50/50, Liefertermin spätestens …, Grundlage Tech Pack v1.x und PP-Freigabe vom …, Prüfplan als Anhang, Labels eingenäht (Haupt-, Größen-, Pflegeetikett), Hangtags bringe ich selbst an, 110 Label-Patches D liegen bei euch, DDP Berlin."),
  PW[21][2]],
 [T("B", "Anzahlung überweisen", 15, [
    "Erst wenn die Fabrik die PO schriftlich bestätigt hat.",
    "Überweisung, Beleg ins Blatt „Ausgaben“.",
   ], "Die Anzahlung ist überwiesen, der Beleg ist gespeichert.")],
 [T("B", "Produktionsplan schriftlich", 15, [
    "Von der Fabrik: Termine für Zuschnitt, Stickerei, Nähen, Waschen, Versand.",
    "Alle Termine in deinen Kalender.",
   ], "Der Produktionsplan steht im Kalender."),
  T("D", "Spiel: bauen oder streichen", 20, [
    "Bauen nur, wenn beides stimmt: Die Vorbestellung läuft (mindestens 10), und du kannst 6 Wochen lang 3 Abende à 60–90 Minuten zusätzlich geben.",
    "Sonst streichen: Die Startseite bleibt die Warteliste mit einem Countdown-Text. Early Access am 22.04. per Link aus der E-Mail.",
    "Mein Rat bei 1–2 Stunden pro Tag: streichen oder die Silhouetten-Version. Die Kampagne verkauft, das Spiel ist Kür.",
    "Entscheidung Claude schreiben. Alle Aufgaben mit dem Etikett SPIEL gelten nur bei „bauen“.",
   ], "Die Entscheidung steht."),
  PW[21][4]],
 [T("A", "Shoot planen", 30, [
    "Termin: Samstag, 20.02. Ort: Berlin, neutral (Hof, Industrie oder helle Wand).",
    "Leute: 2–3 aus der Community oder den Creator-Anproben, die W32 tragen.",
    "Fotograf: ein Freund mit guter Kamera oder du mit dem Handy auf Stativ. Budget 150 € (Plan).",
   ], "Termin, Ort und Leute sind angefragt.")],
 [REVIEW(21), BATCH(wp(22, True), 22)],
])

# ---------- Woche 22 ----------
W22 = dict(n=22, phase="P4", goal="Die Produktion startet", days=[
 [T("B", "Produktionsplan im Blick", 15, [
    "Fotos vom Zuschnitt anfordern.",
    "Stimmt der Plan noch? Abweichungen sofort klären.",
   ], "Fotos sind da, Plan bestätigt."),
  PW[22][0]],
 [T("S", "Werkzeuge für das Spiel installieren", 60, [
    SPIEL + "Ein Abend.",
    "Node.js LTS, Git, Shopify CLI, Claude Code installieren.",
    "In Shopify das Live-Theme duplizieren, die Kopie „Time Travel · Feld“ nennen. Gebaut wird nur an der Kopie.",
   ], "Alle Werkzeuge laufen, die Kopie existiert."),
  PW[22][1]],
 [T("S", "Theme-Kopie holen, Git anlegen", 45, [
    SPIEL + "Befehle stehen unter Referenz → Das Spiel · Bauplan.",
    "Kopie mit shopify theme pull in einen Ordner holen, git init, privates GitHub-Repo anlegen.",
    "Erster Commit, bevor Claude Code etwas anfasst.",
   ], "Der erste Commit ist auf GitHub."),
  PW[22][2]],
 [T("S", "Prompt 1: Graubox", 60, [
    SPIEL + "Prompt 1 aus dem Bauplan an Claude Code.",
    "Mit shopify theme dev auf dem eigenen Handy öffnen. Ein Rechteck läuft durch ein Feld, Tippen = hinlaufen.",
   ], "Die Graubox läuft auf deinem Handy.")],
 [T("A", "Hangtags in Druck geben", 45, [
    "Druckdatei von Claude (Stücknummern 001–100, je eine Datei oder Seriendruck).",
    "Online-Druckerei, 300 g Recyclingkarton, mit Loch, 100 Stück plus 10 Reserve.",
    "Faden oder Schlaufen dazu bestellen.",
    "Nackenlabels für Zipper und Polo (Datei von Claude aus Woche 8) bei einem Webetiketten-Anbieter bestellen, kleinste Menge (meist 50–100 Stück). Den Berliner Sticker vorher fragen, ob er sie beim Besticken einnäht und was das kostet.",
   ], "Hangtags und Nackenlabels sind bestellt."),
  PW[22][4]],
 [STATUS("Story: Casting", ["Story: „Wer will beim Shoot am 20.02. in Berlin dabei sein? Du trägst W32? Schreib mir.“", "Antworten sammeln, 2–3 auswählen."])],
 [T("S", "Spiel-Check: Steuerung", 20, [
    SPIEL + "Fühlt sich das Laufen mit dem Daumen gut an? Wenn nein, erst das reparieren. Es wird nichts gezeichnet, bevor das Laufen stimmt.",
   ], "Die Steuerung fühlt sich gut an."),
  REVIEW(22), BATCH(wp(23, True), 23)],
])

# ---------- Woche 23 ----------
W23 = dict(n=23, phase="P4", goal="Lookbook-Shoot am Samstag", days=[
 [T("S", "Spiel-Palette festlegen", 20, [
    SPIEL + "Sechs Farben aus dem Teppich plus Sonnenuntergang: Orange, Bordeaux, Dämmerungsviolett.",
    "Nie hellblauer Himmel über gelbem Weizen.",
   ], "Die Palette ist als Datei gespeichert."),
  PW[23][0]],
 [T("B", "Inline-Kontrolle 1: bestickte Panels", 20, [
    "Fabrik um Fotos bitten: jedes Element auf 5 zufälligen Panels, vor dem Nähen.",
    "Gegen den Prüfplan: Position, Größe, Farben, Wellen. Fehler sofort melden. Nach dem Nähen ist es zu spät.",
   ], "Fotos geprüft, Rückmeldung an die Fabrik ist raus."),
  PW[23][1]],
 [T("A", "Shotlist schreiben", 30, [
    "Pro Person: Ganzkörper vorn, hinten, seitlich, gehend, Detail Tasche, Detail Rücken. Dazu 3 Gruppenbilder mit Jeans, Zipper und Polo.",
    "Behind the Scenes filmt jemand mit dem Handy, den ganzen Tag.",
   ], "Die Shotlist ist ausgedruckt."),
  PW[23][2]],
 [T("S", "Pixel-Art Teil 1", 90, [
    SPIEL + "Figur (Stehen 2 Frames, Laufen 6 Frames, nur nach rechts), Himmel, Hügel.",
    "Aus Aseprite als PNG + JSON exportieren, Maße laut Bauplan.",
   ], "Drei Dateien sind exportiert.")],
 [T("A", "Shoot vorbereiten", 45, [
    "PP-Sample und Zipper/Polo-Muster gebügelt, Ersatzklammern zum Anpassen, Akkus, Speicher, Getränke.",
    "Wetter prüfen, Plan B drinnen.",
   ], "Alles liegt gepackt bereit."),
  PW[23][4]],
 [T("A", "SHOOT", 180, [
    "Shotlist abarbeiten und abhaken.",
    "Behind the Scenes läuft die ganze Zeit. Das ist mehr Content als die Fotos selbst.",
    "Story live vom Set.",
   ], "Alle Motive der Shotlist sind im Kasten.")],
 [T("A", "Shoot sichten", 60, [
    "Pro Person die 6 besten Bilder, dazu die 3 besten Gruppenbilder.",
    "Retusche nur dezent. Die Stickerei nie glätten.",
    "Behind-the-Scenes-Clips in den Ordner „W24“.",
   ], "Die Auswahl liegt im Ordner „Shop“."),
  REVIEW(23, ["Monatsabschluss bald: Warteliste gegen Ziel 2.400 bis 28.02."]), BATCH(wp(24, True), 24, 40)],
])

# ---------- Woche 24 ----------
W24 = dict(n=24, phase="P4", goal="Kampagnenmaterial fertig, Drop-E-Mails schreiben", days=[
 [T("S", "Pixel-Art Teil 2 und Prompt 2", 90, [
    SPIEL + "Weizen hinten und vorn mit 3 Frames Wiegen, Hütte von außen.",
    "Prompt 2 an Claude Code: Grafik und Parallax einbauen. Auf dem Handy prüfen, committen.",
   ], "Grafik läuft auf dem Handy, Commit ist gemacht."),
  PW[24][0]],
 [T("A", "Shop-Bilder aufbereiten", 45, [
    "2000 px lange Seite, Formate 1:1 und 4:5, sauber benannt, Alt-Texte.",
    "Jeans-Bilder ins Produkt „Time Travel Jeans · NVL-TT-01“ (Entwurf seit Woche 10) hochladen. Bilder von Zipper und Polo in den Ordner „Shop“, die beiden Produkte legst du in Woche 27 an.",
   ], "Die Jeans-Bilder sind im Shop, Zipper und Polo liegen im Ordner „Shop“."),
  T("A", "Verpackung bestellen", 30, [
    "Die PP-Jeans falten wie fürs Paket und messen. Danach richtet sich die Kartongröße (ungefähr 35 × 25 × 8 cm).",
    "110 unbedruckte Versandkartons bei einem Verpackungshändler (z. B. Ratioform oder Raja), dazu Seidenpapier, 110 Karten A6 für die handgeschriebene Nachricht, Klebeband, Lieferscheintaschen.",
    "Statt bedruckter Kartons: ein Stempel mit Logo (ca. 20–30 €). Bedruckte Kartons nur, wenn alles zusammen mit den Hangtags unter 240 € bleibt.",
    "Lieferung bis spätestens Mi 03.03. Am 03.03. packst du das Probepaket.",
   ], "Die Verpackung ist bestellt, Liefertermin vor dem 03.03.")],
 [T("A", "Drop-E-Mails schreiben lassen", 30, [
    "Prompt unten an Claude.",
    "In Shopify Email als Entwürfe anlegen.",
   ], "6 Entwürfe liegen in Shopify.",
   "Schreib mir 6 E-Mails zum Drop am 22.04.2027 um 19:00: T−14 (Do 08.04.), T−7 (Do 15.04.), T−3 (Mo 19.04.), T−24h (Mi 21.04.), T−1h mit Early-Access-Link (Do 22.04., 18:00), LIVE (Do 22.04., 19:00). Je Betreff, Vorschautext, 60–120 Wörter, ein Button. Jeans 169 €, Zipper 139 €, Polo 79 €, 100 nummerierte Jeans. Sprachregel beachten."),
  PW[24][2]],
 [T("C", "Kampagnenfilm schneiden", 60, [
    "30–45 Sekunden aus Shoot und Behind the Scenes, ein Sound, kaum Text.",
    "Letzter Frame: „Time Travel · 22.04. · 19:00“.",
   ], "Der Film ist exportiert."),
  T("S", "Pixel-Art Teil 3 und Prompt 3", 90, [
    SPIEL + "Jeans an der Vogelscheuche, Zipper am Zaun, Polo auf der Wäscheleine, Hüttentür offen, Innenraum mit dem Teppich.",
    "Prompt 3 an Claude Code: Stationen mit Karten und das Formular „Hol dir den Schlüssel“.",
   ], "Stationen und Formular laufen auf dem Handy.")],
 [PW[24][4]],
 [STORY("Hauptbild", "Welches soll das Hauptbild werden?", "„A“, „B“, „C“ (drei Shoot-Bilder)")],
 [T("S", "Formular-Test", 15, [
    SPIEL + "Mit deiner eigenen Adresse anmelden. Steht sie in Shopify unter Kunden mit dem Tag tt-feld?",
   ], "Die Testanmeldung steht mit Tag in Shopify."),
  T("A", "Monatsabschluss Februar", 15, [
    "Warteliste gegen Ziel 2.400. Vorbestellungen gegen Ziel 28 bis Mitte März. Ausgaben gegen Plan.",
   ], "Alle Zahlen stehen in der Tabelle."),
  REVIEW(24)],
])

WEEKS_C = [W17, W18, W19, W20, W21, W22, W23, W24]
