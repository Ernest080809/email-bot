# -*- coding: utf-8 -*-
# Woche 25–32 · Fertigstellung, Versand, Countdown, Drop
import datetime as dt
from r5_common import *
from r5_a import PW
import r5_b  # füllt PW[10..17]
from r5_c import W24, SPIEL, wp

WT = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
DROP = dt.date(2027, 4, 22)

def tag(n):
    d = DROP - dt.timedelta(days=n)
    return "%s %02d.%02d." % (WT[d.weekday()], d.day, d.month)

# ---------- Countdown: 24 Motive, vorproduziert in Woche 27 ----------
MOTIV = {
 24: "Ganzkörper vorn aus dem Shoot, langsamer Zoom auf die Tasche",
 23: "Band A im Makro, langsamer Schwenk entlang der Tasche",
 22: "Münztasche E im Makro, Lineal daneben",
 21: "Gesäßtasche: drei Ähren, rotes Band, Goldfäden",
 20: "Goldfäden in Bewegung (Hand oder Fön auf kleinster Stufe)",
 19: "Alatyr auf der rechten Gesäßtasche, die Kamera kommt langsam näher",
 18: "Lebensbaum-Patch, Zoom auf Knoten und Wurzeln",
 17: "Gruppenbild aus dem Shoot: Jeans, Zipper, Polo",
 16: "Zipper-Rücken mit dem Medaillon",
 15: "Polo, Bänder an der Knopfleiste",
 14: "Hangtag mit Nummer 001 in der Hand, Text „Noch 2 Wochen“",
 13: "Behind the Scenes vom Shoot, schnell geschnitten",
 12: "Rohe Schnittkante am Saum, ein Finger fährt entlang",
 11: "Zickzack am Band",
 10: "Teppich-Foto, harter Schnitt auf das Medaillon",
 9: "Innenseite der Stickerei, Hose auf links",
 8: "Gehen, Rückansicht aus dem Shoot",
 7: "Ganzkörper hinten, Text „Noch 1 Woche“",
 6: "Seitennaht im Streiflicht: der Serp über den Stoppeln",
 5: "Pflegeetikett „Fäden nicht abschneiden“",
 4: "Hand in der Tasche, Detail aus dem Shoot",
 3: "Papiertest aus dem Oktober, hart geschnitten auf das fertige Teil",
 2: "Alle fünf Stickereien, je 1 Sekunde",
 1: "Kampagnenfilm auf 10 Sekunden gekürzt, Text „Morgen 19:00“",
}
def cd(n, live=None):
    return CD(n, tag(n), MOTIV[n], live)

def liste(von, bis):
    return ["%s · %s: %s" % ("T−%d" % n, tag(n), MOTIV[n]) for n in range(von, bis - 1, -1)]

# ---------- Posts Woche 25–28 ----------
PW[25] = {
 0: P("BUILD", "Das ist Time Travel",
      "Das ist Time Travel.",
      "Die 6 stärksten Shoot-Bilder, je 0,8 Sekunden auf den Beat. Letzter Frame: „100 Jeans · 22.04. · 19:00“", "10–12 Sek."),
 1: P("ORIGIN", "Rot und Weiß",
      "Warum meine Stickerei nur rot und weiß ist.",
      "Ein Referenzbild mit rotem Kreuzstich auf weißem Leinen (aus deiner Sammlung, Quelle klein einblenden), dann Band A im Makro. Ein Satz: Auf Leinen war der Grund hell, auf der Jeans ist er dunkel, deshalb trägt hier Weiß das Muster", "20–25 Sek."),
 2: P("REACH", "Nummer 047",
      "Nur eine Person hat Nummer 047.",
      "Trend-Sound, Hangtag-Makro mit einer Nummer, harter Schnitt auf einen Shoot-Clip", "8 Sek."),
 4: P("DETAIL", "Fäden nicht abschneiden",
      "Auf meinem Pflegeetikett steht: Fäden nicht abschneiden.",
      "Makro auf das Pflegeetikett am PP-Sample, dann Schwenk auf die Goldfäden", "10–15 Sek."),
 5: STORY("Paket", "Was willst du im Paket finden?", "„Handgeschriebene Karte“, „Sticker“, „Nur die Jeans“",
          extra=["Die Antwort mit den meisten Stimmen setzt du um, wenn sie unter 1 € pro Paket kostet."]),
}
PW[26] = {
 0: P("BUILD", "Fast fertig",
      "So sehen 100 Jeans aus, kurz bevor sie fertig sind.",
      "Fotos und Clips der Inline-Kontrolle 2 aus der Fabrik (vorher fragen, ob du sie zeigen darfst). Ein Satz: Diese Woche ist die Fabrik wegen des Ramadan-Fests zu, eingeplant seit Januar. Bei einer Fabrik in Portugal fällt der Satz weg", "15 Sek."),
 1: P("ORIGIN", "Für alle Neuen",
      "Für alle, die neu hier sind: Was ist Time Travel?",
      "Ein Clip pro Satz: Papiertest (Oktober), Stickprobe, Sample, Shoot. Vier Sätze: Ein Muster. Eine Fabrik. 100 Stück. 22. April", "25–30 Sek."),
 2: P("REACH", "So wird verpackt",
      "So wird deine Jeans verpackt.",
      "Trend-Sound, Zeitraffer vom Probepaket am 03.03.: Hangtag, Karte, Seidenpapier, Karton", "10 Sek."),
 4: P("DETAIL", "Gold im Licht",
      "Gold sieht man erst, wenn Licht drauf fällt.",
      "Makro der Ähren im Halbdunkel, die Handylampe wandert langsam darüber", "10–15 Sek."),
 5: STORY("Letzte Woche Vorbestellpreis", "Vorbestellpreis endet am Sonntag, 21.03. Schon dabei?", "„Hab schon“, „Mach ich noch“, „Ich warte auf den Drop“",
          extra=["Nur wenn noch Vorbestell-Paare frei sind. Sonst: „Vorbestellung ausverkauft. Drop am 22.04.“ mit Countdown-Sticker."]),
}
PW[27] = {
 0: P("BUILD", "Noch bis Sonntag",
      "Noch bis Sonntag: 149 € statt 169 €.",
      "PP-Sample am Körper, darüber die echte Zahl „X von 35 vorbestellt“ (am Sonntag davor einsetzen), letzter Frame „So 21.03.“. Sind die 35 schon weg, dreh stattdessen „Vorbestellung ausverkauft. Drop am 22.04.“", "10 Sek.",
      cta="Caption: „Vorbestellpreis 149 € nur bis Sonntag, 21.03., 20:00. Danach 169 €. Link in Bio.“"),
 1: P("ORIGIN", "Gold nur, wo etwas wächst",
      "Gold gibt es nur an zwei Stellen.",
      "Makro der Ähren mit den Fäden, dann Makro des Lebensbaum-Patches. Ein Satz: Gold nur an dem, was wächst", "15–20 Sek."),
 2: P("REACH", "Papier zu Garn",
      "Oktober: Papier. März: Garn.",
      "Trend-Sound, der Papiertest-Clip aus dem Oktober, hart geschnitten auf denselben Ausschnitt am PP-Sample", "8 Sek."),
 4: P("DETAIL", "37 mal 37",
      "37 mal 37 Kästchen. Auf einer Münztasche.",
      "Makro auf Münztasche E, Lineal daneben, langsamer Schwenk", "15 Sek."),
 5: STORY("Countdown", "Ab Montag, 29.03., zählen wir runter. Bist du am 22.04. dabei?", "„Ja“, „Erinnere mich“",
          extra=["Dazu den Countdown-Sticker auf 22.04., 19:00. Wer „Erinnern“ tippt, bekommt von Instagram eine Nachricht, wenn es losgeht."]),
}
PW[28] = {
 0: P("BUILD", "Alles bezahlt",
      "Alles bezahlt. Jetzt muss sie nur noch ankommen.",
      "Überweisung der Restzahlung (Betrag sichtbar, Kontodaten geschwärzt), dann die Fotos der Endkontrolle aus der Fabrik", "15 Sek."),
 1: P("ORIGIN", "Warum Time Travel",
      "Warum diese Jeans Time Travel heißt.",
      "Ein Satz ins Handy: Ein Muster, das Generationen alt ist, auf einer Jeans von 2027. Dazu ein Referenzbild, Band A und du im Shoot", "20 Sek."),
 2: P("REACH", "Packstation",
      "Hier werden 100 Jeans verpackt.",
      "Trend-Sound, Zeitraffer vom Aufbau der Packstation am Dienstag", "8 Sek.", batch=False),
 4: P("DETAIL", "Fünf Stickereien",
      "Fünf Stickereien. Findest du alle?",
      "Shoot-Bild von hinten, dann nacheinander Zoom auf C, D und B, dann vorn auf A und E", "15 Sek."),
 5: STORY("Größe", "Welche Größe holst du dir am 22.04.?", "„W30“, „W32“, „W34“, „W36+“",
          extra=["Ergebnis neben die Verteilung im Blatt „Bestand“ schreiben. Fehlt eine Größe, ist das eine Info für Drop 2, nicht für jetzt."]),
}

# Batch für Woche 25 am Sonntag, 28.02. (Woche 24)
W24["days"][6].append(BATCH(wp(25, True), 25, 75))

# ---------- Woche 25 ----------
W25 = dict(n=25, phase="P4", goal="Fertig genähte Jeans prüfen, Versand und Verpackung aufbauen", days=[
 [T("B", "Inline-Kontrolle 2: genäht und gewaschen", 30, [
    "Die Fabrik um Fotos und ein kurzes Video bitten: 5 zufällige, fertig gewaschene Jeans, je vorn, hinten und jedes Element A–E nah. Dazu ein Maßband an Bund und Innenbein im Bild.",
    "Gegen den Prüfplan (Referenz → Prüfplan Sample): Position, Farben, Wellen, Waschton, Saum.",
    "Fragen: Wann werden die Goldfäden gesetzt? Wann ist die Endkontrolle? Bleibt der Versandtermin?",
    "Fehler sofort mit Foto melden. Jetzt kostet eine Korrektur Tage, nach dem Versand kostet sie Wochen.",
   ], "Die Fotos sind geprüft, die Rückmeldung ist raus, der Versandtermin ist bestätigt."),
  PW[25][0]],
 [T("A", "Versandweg wählen und einrichten", 45, [
    "Drei Wege vergleichen: 1) DHL Online-Frankierung zu Privatkundenpreisen, 2) Versandsoftware mit eigenem DHL-Tarif und Shopify-Anbindung (z. B. Sendcloud), 3) eigener DHL-Geschäftskundenvertrag. Seit Juli 2025 kostet ein DHL-Geschäftskundenvertrag eine Monatspauschale ab 7,95 €, bei rund 150 Paketen im Jahr lohnt er sich selten.",
    "Kriterien: Preis pro Paket bis 1 kg in Deutschland und in die EU, Monatsgebühr, Bestellungen aus Shopify importieren, Label mit einem Klick, Tracking automatisch zurück an den Kunden.",
    "Den Prompt unten an Claude, dann einen Weg wählen und das Konto anlegen.",
    "Ein Testlabel erzeugen und auf normalem A4-Papier drucken. Ein Etikettendrucker ist nicht nötig.",
    "Stimmt dein Versandpreis im Shop aus Woche 11 noch? Sonst jetzt anpassen.",
   ], "Der Versandweg steht, ein Testlabel ist gedruckt, die Versandpreise im Shop stimmen.",
   "Vergleiche für mich die aktuellen Preise für Pakete bis 1 kg (Deutschland und EU) bei DHL Online-Frankierung, Sendcloud mit DHL und einem DHL-Geschäftskundenvertrag mit Monatspauschale. Ich verschicke etwa 150 Pakete, fast alle zwischen 06.04. und 30.04.2027, aus einem Shopify-Shop. Was ist am günstigsten und am einfachsten?"),
  T("S", "Prompt 4: Tür mit drei Zuständen", 60, [
    SPIEL + "Prompt 4 aus dem Bauplan an Claude Code.",
    "Mit dem Testmodus alle drei Zustände am Handy durchspielen: FELD, SCHLÜSSEL (mit ?key=…), OFFEN.",
    "Funktioniert alles: committen.",
   ], "Alle drei Zustände laufen auf dem Handy, der Commit ist gemacht."),
  PW[25][1]],
 [T("A", "Probepaket packen und Zeit stoppen", 40, [
    "Ist die Verpackung da? Wenn nicht: beim Händler nachhaken, Liefertermin notieren.",
    "Das PP-Sample packen wie eine echte Bestellung: Jeans falten, Hangtag dran, Karte mit Nummer und einem Danke-Satz, Seidenpapier, Karton, Stempel, Label in die Lieferscheintasche.",
    "Zeit stoppen. Ziel: unter 4 Minuten pro Paket. 100 Pakete sind dann knapp 7 Stunden.",
    "Paket wiegen. Liegt es unter 1 kg, stimmt die Preisstufe.",
    "Den ganzen Ablauf im Zeitraffer filmen. Das ist der REACH-Post nächste Woche.",
   ], "Ein fertiges Probepaket steht da, Zeit und Gewicht sind notiert."),
  T("S", "Button „Direkt zum Shop“ prüfen", 20, [
    SPIEL + "Auf jedem Bildschirm sichtbar, ohne Laufen erreichbar, ein echter Link.",
    "Vor der Öffnung zeigt er die Restzeit, ab der Öffnung führt er zur Kollektion. Mit dem Testmodus beide Zustände prüfen.",
    "Wer kaufen will, darf nie durchs Feld müssen.",
   ], "Der Button funktioniert in beiden Zuständen."),
  PW[25][2]],
 [T("B", "Fabrik: Plan rund um das Ramadan-Fest", 15, [
    "Nur bei einer Fabrik in der Türkei. Das Fest beginnt Mo 08.03. am Nachmittag (in der Türkei ab 13:00, bei uns 11:00) und geht bis Do 11.03.",
    "Schriftlich fragen: Was ist vor dem Fest fertig? Ab wann arbeitet ihr wieder, Fr 12.03. oder Mo 15.03.? Wann setzt ihr die Goldfäden, wann ist die Endkontrolle, wann der Versand?",
    "Die Antworten in den Kalender.",
    "Fabrik in Portugal: Das Fest entfällt, den Versandtermin trotzdem schriftlich bestätigen lassen.",
   ], "Du kennst Endkontrolle und Versandtermin schriftlich."),
  T("A", "Textbausteine für Kundenfragen", 30, [
    "Den Prompt unten an Claude.",
    "Jeden Baustein lesen und in deinem Ton anpassen.",
    "Auf dem Handy als Textersetzung speichern. iPhone: Einstellungen → Allgemein → Tastatur → Textersetzung. Android (Gboard): Einstellungen → Wörterbuch → Mein Wörterbuch. Kürzel wie „#gr“ für Größe.",
   ], "Alle 10 Bausteine sind als Kürzel auf dem Handy.",
   "Schreib mir 10 kurze Antwort-Textbausteine in Du-Form für Instagram-DMs und E-Mails zum Drop: 1) Welche Größe? (ehrliche Größen, W32 = 81 cm Bund, Umrechnung von Eightyfive, Carhartt und Dickies) 2) Wann wird verschickt? 3) Versandkosten 4) Rückgabe 5) Was ist die Stücknummer? 6) In meiner Größe ausverkauft 7) Vorbestellung: Wann kommt meine? 8) Zipper und Polo: Lieferzeit 9) Pflege und Goldfäden 10) Zahlung hat nicht geklappt. Je 2–3 Sätze.")],
 [T("A", "Freie Tage und Hilfe planen", 15, [
    "Die Woche, in der die Ware ankommt (voraussichtlich Di 30.03. bis Sa 03.04.), braucht zwei freie Tage zum Prüfen.",
    "Die Drop-Woche braucht Do 22.04. ab 17:00, dazu Fr 23.04. und Sa 24.04. ganz zum Packen.",
    "Jetzt Urlaub beantragen oder Schichten tauschen.",
    "Eine Person fragen, die am Fr 23.04. und Sa 24.04. je 3 Stunden beim Packen hilft. Bezahlung oder Gegenleistung vorher klar absprechen.",
   ], "Die freien Tage sind beantragt, die Hilfe hat zugesagt."),
  T("S", "Gewicht und Ladezeit messen", 20, [
    SPIEL + "Alle Dateien zusammen unter 1,5 MB, das erste Bild unter 2 Sekunden, mit WLAN aus.",
    "Liegt es drüber: Claude Code Bilder und Code verkleinern lassen, dann committen.",
   ], "Unter 1,5 MB und unter 2 Sekunden."),
  PW[25][4]],
 [PW[25][5]],
 [REVIEW(25), BATCH(wp(26, True), 26, 80)],
])

# ---------- Woche 26 ----------
W26 = dict(n=26, phase="P4", goal="Die Fabrik macht Pause: Werbung, Restzahlung und Warenannahme vorbereiten", days=[
 [T("B", "Fabrik-Status vor dem Fest", 15, [
    "Nur Türkei: bis 10:00 unserer Zeit den letzten Stand anfordern. Fotos vom aktuellen Stand, was fehlt noch, Versanddatum.",
    "Danach bis Do 11.03. keine Antworten erwarten.",
   ], "Du hast den Stand vor dem Fest schriftlich."),
  T("S", "Gerätetest und Prompt 5", 60, [
    SPIEL + "iPhone Safari, Android Chrome und vor allem der Instagram-In-App-Browser.",
    "Den Vorschau-Link per Instagram-DM an einen Freund schicken und in der App öffnen.",
    "Danach Prompt 5 aus dem Bauplan an Claude Code. Die ersten fünf Probleme reparieren lassen, committen.",
   ], "Das Spiel läuft auf allen drei Browsern."),
  PW[26][0]],
 [T("A", "Werbung vorbereiten: Pixel und Zielgruppen", 45, [
    "Shopify-App „Facebook & Instagram“ (von Meta) installieren und mit deinem Instagram-Konto verbinden. Damit misst der Meta-Pixel im Shop.",
    "Shopify → Einstellungen → Kundendatenschutz: Cookie-Banner für die EU einschalten. Ohne Einwilligung misst der Pixel nicht, das ist richtig so.",
    "Datenschutzerklärung um den Meta-Pixel ergänzen: Generator von e-recht24 aus Woche 4 neu durchlaufen, die Seite im Shop ersetzen.",
    "Im Werbeanzeigenmanager drei Zielgruppen anlegen: Shop-Besucher der letzten 30 Tage, Instagram-Interaktionen der letzten 90 Tage, Video-Zuschauer ab 50 Prozent.",
    "Keine E-Mail-Listen zu Meta hochladen. Ohne passende Einwilligung ist das datenschutzrechtlich heikel.",
   ], "Pixel läuft, Cookie-Banner ist an, drei Zielgruppen sind angelegt."),
  PW[26][1]],
 [T("B", "Restzahlung vorbereiten", 20, [
    "Kontostand plus Vorbestellungen (Blatt „Pre-Order“) gegen die Restzahlung laut Proforma (Planwert bei 50/50 ca. 3.000 €) plus Verpackung, Versand und Werbung.",
    "Reicht es: Restzahlung für Fr 19.03. einplanen, nach der Endkontrolle.",
    "Reicht es nicht: Prompt unten an Claude. Mögliche Lösungen sind Zahlung gegen Versandnachweis, Teilzahlung oder ein kurzes Zahlungsziel.",
   ], "Du weißt, ob die Restzahlung am 19.03. gedeckt ist.",
   "Mir fehlen für die Restzahlung … €. Kontostand …, Vorbestellungen …, Restzahlung laut Proforma …, Versand geplant am …. Schreib mir eine höfliche Mail auf Englisch an die Fabrik mit einem Vorschlag und sag mir ehrlich, welche Lösung das kleinste Risiko hat."),
  PW[26][2]],
 [T("B", "Versandpapiere klären", 20, [
    "Türkei: die Fabrik bitten, die Warenverkehrsbescheinigung A.TR mitzuschicken. Mit A.TR fällt kein Zoll an, nur die Einfuhrumsatzsteuer.",
    "Handelsrechnung (Commercial Invoice) und Packliste vorab als PDF: Stück pro Größe, Warenwert, Zolltarifnummer.",
    "DDP heißt: Fabrik oder Spediteur verzollen. Trotzdem fragen, ob deine EORI-Nummer gebraucht wird, und sie bereithalten.",
    "Portugal: nur Rechnung und Packliste.",
   ], "Rechnung und Packliste liegen als PDF vor, A.TR ist zugesagt (Türkei)."),
  T("B", "Warenannahme und Prüfung vorbereiten", 30, [
    "Prüfplan Teil „Wareneingang“ lesen (Referenz → Prüfplan Sample).",
    "Mit der Fabrik schriftlich vereinbaren: Fehlerklassen wie im Prüfplan, Reklamationsfrist 14 Tage ab Ankunft, Gutschrift oder Ersatz bei kritischen Fehlern.",
    "Platz für 6–8 Kartons freiräumen, trocken, nicht direkt auf dem Boden.",
    "Bereitlegen: Maßband, Prüfliste ausgedruckt, Klebepunkte in Grün und Rot.",
   ], "Fehlerklassen und Frist sind schriftlich vereinbart, der Platz ist frei.")],
 [T("A", "E-Mail „Vorbestellpreis endet“ planen", 15, [
    "Nur wenn noch Vorbestell-Paare frei sind.",
    "Text mit dem Prompt unten bei Claude holen.",
    "Shopify Email: an das Segment „abonniert, keine Bestellung“ aus Woche 20, Versand Mo 15.03., 18:00.",
   ], "Die E-Mail ist für Montag geplant.",
   "Schreib mir eine kurze E-Mail: Der Vorbestellpreis von 149 € endet am Sonntag, 21.03., um 20:00. Danach kostet die Jeans im Drop am 22.04. 169 €. Noch X von 35 Paar frei. Die Vorbestellungen werden im April verschickt. Betreff, Vorschautext, 60–90 Wörter, ein Button. Sprachregel beachten."),
  PW[26][4]],
 [PW[26][5],
  T("S", "Playtest mit 5 Leuten", 60, [
    SPIEL + "Das Handy in die Hand geben, nichts erklären, nur zuschauen und notieren, wo sie hängen bleiben.",
    "Wer den Shop-Button nicht in 5 Sekunden findet, zeigt dir einen Fehler.",
    "Bildschirmaufnahmen vom Laufen durchs Feld sichern. Das ist dein Launch-Content.",
   ], "Die Notizen von 5 Testern liegen vor.")],
 [REVIEW(26), BATCH(wp(27, True), 27, 80)],
])

# ---------- Woche 27 ----------
W27 = dict(n=27, phase="P4", goal="Restzahlung, Shop für den Drop fertig, Countdown vorproduzieren", days=[
 [T("B", "Fabrik-Status nach dem Fest", 15, [
    "Arbeitet die Fabrik wieder? Termin der Endkontrolle und des Versands bestätigen lassen.",
    "Verschiebt sich etwas um mehr als 3 Tage: Claude schreiben.",
   ], "Endkontrolle und Versanddatum sind schriftlich bestätigt."),
  T("S", "Playtest-Probleme beheben", 60, [
    SPIEL + "Die drei häufigsten Probleme aus dem Playtest an Claude Code, den Rest streichen.",
    "Am Handy prüfen, committen.",
   ], "Die drei Probleme sind behoben."),
  PW[27][0]],
 [T("A", "Drop-Produkte fertig machen", 60, [
    "Jeans: Produkt „Time Travel Jeans · NVL-TT-01“ (Entwurf seit Woche 10), Preis 169 €. Bestand vorläufig: Liefermenge minus Vorbestellungen minus 5 Creator-Paare minus 2 Reserve, nach der Startannahme auf die Größen verteilt. Den echten Bestand setzt du am Sa 03.04. nach der Prüfung.",
    "Bei jeder Variante „Weiterverkaufen, wenn nicht vorrätig“ AUS.",
    "Zipper (139 €, S–XL) und Polo (79 €, S–XL) neu anlegen, Status Entwurf, Texte mit dem Prompt unten.",
    "Oben in beide Texte: „Wird nach deiner Bestellung in Berlin bestickt. Versand innerhalb von 3 Wochen.“ Die 3 Wochen sind die Lieferzeit des Stickers (Woche 14) plus eine Woche für die Blanks. Ist das zusammen weniger, schreib die kürzere Zeit.",
    "Den Sticker fragen, wie viele Teile er in 2 Wochen schafft. Mehr verkaufst du nicht: Bestand von Zipper und Polo auf diese Zahl setzen.",
    "Kollektion „Time Travel“ anlegen, alle drei Produkte rein. Der Link zur Kollektion steht am Drop-Tag in der E-Mail.",
   ], "Alle drei Produkte und die Kollektion sind fertig, Status Entwurf.",
   "Schreib mir die Produkttexte für Shopify: Time Travel Zipper NVL-TT-02 (139 €, Fleece 330–350 g/m², vorn zwei gestickte Bänder an der Zip-Leiste, hinten das Teppich-Medaillon) und Time Travel Polo NVL-TT-03 (79 €, Piqué, zwei Bänder an der Knopfleiste). Je ein Satz Kern, ein Absatz zum Muster, ein Absatz Material und Pflege, dazu der Hinweis „wird nach deiner Bestellung in Berlin bestickt“. Sprachregel beachten, nie „authentisch“."),
  PW[27][1]],
 [T("A", "Shop-Durchlauf mit echter Karte", 30, [
    "Testprodukt für 1 € anlegen, Status Aktiv, aber in keinem Menü und keiner Kollektion.",
    "Am Handy mit deiner echten Karte kaufen.",
    "Prüfen: Bestellbestätigung, Rechnung mit Kleinunternehmer-Hinweis oder ausgewiesener Steuer, Label in deiner Versandlösung erzeugen (nicht drucken), Versandbestätigung mit Tracking.",
    "Bestellung erstatten, Label stornieren, Testprodukt löschen.",
   ], "Kauf, Rechnung und Label haben funktioniert, alles ist erstattet."),
  T("S", "PLAN B anlegen und üben", 20, [
    SPIEL + "Das bisherige Theme unverändert lassen und „PLAN B“ nennen.",
    "Das Zurückschalten einmal üben und die Zeit stoppen. Ziel: unter einer Minute.",
   ], "PLAN B existiert, das Umschalten dauert unter einer Minute."),
  PW[27][2]],
 [T("C", "Countdown-Assets Teil 1: T−24 bis T−13", 60, [
    "Vorlage in CapCut einmal bauen: 9:16, dunkler Indigo-Grund, oben groß „T−24“, unten „22.04. · 19:00“, in der Mitte ein Clip von 4–6 Sekunden. Danach tauschst du nur Zahl und Clip.",
    ] + liste(24, 13) + [
    "Export in den Ordner „Countdown“, Dateinamen „T-24“, „T-23“ und so weiter.",
   ], "12 Countdown-Videos liegen im Ordner.")],
 [T("B", "Endkontrolle und Restzahlung", 45, [
    "Die Fabrik schickt das Endkontroll-Paket: Video aller gepackten Kartons, 5 zufällige Jeans gemessen (Bund, Innenbein), Makros von A–E und den Goldfäden, Packliste mit Stück pro Größe.",
    "Prüfen: Stimmen die Mengen pro Größe mit der Bestellung? Sind die Goldfäden gesetzt, die Säume geschnitten, die Patches gerade?",
    "Stimmt alles: Restzahlung überweisen, Verwendungszweck mit der Rechnungsnummer. Beleg ins Blatt „Ausgaben“. Screenshot für den BUILD-Post.",
    "Schriftlich anfordern: Versanddatum, Spediteur, Tracking-Nummer, A.TR (Türkei).",
    "Stimmt etwas nicht: nicht zahlen. Fotos und Liste an die Fabrik, Claude dazuholen.",
   ], "Die Restzahlung ist raus, das Versanddatum steht schriftlich."),
  PW[27][4]],
 [T("C", "Countdown-Assets Teil 2: T−12 bis T−1", 60, [
    "Dieselbe Vorlage wie am Donnerstag.",
    ] + liste(12, 1) + [
    "Export in den Ordner „Countdown“. Danach liegen 24 Videos dort.",
   ], "Alle 24 Countdown-Videos liegen im Ordner."),
  PW[27][5]],
 [T("A", "Vorbestellung schließen, Bestand rechnen", 20, [
    "Um 20:00 das Vorbestell-Produkt auf „Entwurf“ stellen. Ab jetzt gibt es nur noch den Drop.",
    "Vorbestellungen pro Größe zählen (Blatt „Pre-Order“).",
    "Neues Blatt „Bestand“: Liefermenge pro Größe minus Vorbestellungen minus 5 Creator-Paare minus 2 Reserve = Drop-Bestand.",
    "Story: „Vorbestellung geschlossen. Danke an X Leute. Der Rest kommt am 22.04.“",
   ], "Die Vorbestellung ist geschlossen, das Blatt „Bestand“ steht."),
  T("S", "Letzter Stand vor dem Launch", 15, [
    SPIEL + "Commit, Push auf GitHub, shopify theme push auf die Kopie.",
    "Ab jetzt wird nicht mehr gebaut, nur noch repariert.",
   ], "Der letzte Stand ist auf GitHub und auf der Theme-Kopie."),
  REVIEW(27), BATCH(wp(28, True), 28, 60)],
])

# ---------- Woche 28 ----------
W28 = dict(n=28, phase="P4", goal="Die Ware ist unterwegs, Lager und Werbung stehen, Montag startet der Countdown", days=[
 [T("B", "Sendung verfolgen", 15, [
    "Tracking-Nummer von der Fabrik, voraussichtlichen Ankunftstag in den Kalender.",
    "Ostern: Karfreitag 26.03. und Ostermontag 29.03. sind Feiertage, kein Zoll und meist keine Zustellung. Kommt die Ware nicht bis Do 25.03., dann frühestens Di 30.03.",
    "Spätester Ankunftstermin für den Drop am 22.04. ist Do 15.04., denn die Prüfung braucht drei Abende. Wird es später, sofort Claude schreiben: Dann entscheidest du zwischen Drop eine Woche später (29.04.) und Drop am 22.04. mit Versand ab Ankunft, offen angekündigt.",
    "Das Lieferfenster der Vorbesteller (22.–30.04.) wackelt erst, wenn die Ware nach dem 26.04. ankommt.",
   ], "Der Ankunftstag steht im Kalender."),
  T("S", "STILLER LAUNCH: Feld veröffentlichen", 30, [
    SPIEL + "Theme „Time Travel · Feld“ veröffentlichen, ohne Ankündigung.",
    "48 Stunden mit echten Besuchern finden die Fehler, bevor jemand danach sucht.",
    "Einmal selbst von Instagram aus öffnen.",
   ], "Das Feld ist live, du hast es aus Instagram heraus getestet."),
  PW[28][0]],
 [T("A", "Lager und Packstation aufbauen", 45, [
    "Regal oder Kisten: ein Fach pro Größe W30, W32, W34, W36, W38, beschriftet.",
    "Packstation an einem festen Tisch: Waage, Drucker, Kartons, Seidenpapier, Karten, Hangtags in Nummernreihenfolge, Faden, Klebeband, Stempel, Stift.",
    "Material für 100 Pakete zählen. Was fehlt, heute bestellen.",
    "Den Aufbau im Zeitraffer filmen. Das ist der REACH-Post morgen.",
   ], "Die Packstation steht, das Material reicht für 100 Pakete."),
  PW[28][1]],
 [T("A", "Vorbesteller informieren", 20, [
    "Shopify → Kunden: Segment „hat das Produkt Time Travel Jeans · Vorbestellung gekauft“.",
    "Kurze E-Mail mit dem Prompt unten. Nichts Früheres versprechen, als du halten kannst.",
   ], "Die E-Mail an alle Vorbesteller ist raus.",
   "Schreib mir eine kurze, persönliche E-Mail an meine X Vorbesteller: Die 100 Jeans sind unterwegs nach Berlin. Ich prüfe jede einzeln und verschicke deine, sobald sie geprüft ist, spätestens im versprochenen Fenster 22.–30.04. Deine Stücknummer bekommst du mit dem Paket, Vorbesteller haben die ersten Nummern. Danke, dass du früh dabei warst. 60–90 Wörter."),
  T("S", "Feld-Check nach 48 Stunden", 15, [
    SPIEL + "Shopify → Kunden: Anmeldungen mit dem Tag tt-feld zählen.",
    "Null heißt: Das Formular ist kaputt oder die Hütte liegt zu weit weg. Dann die Hütte näher an den Start.",
   ], "Mindestens eine echte Anmeldung mit tt-feld."),
  PW[28][2]],
 [T("A", "Support festlegen", 30, [
    "Ein Postfach für alle E-Mails: die Shop-Adresse. Instagram-DMs beantwortest du selbst.",
    "Antwortzeit: normal 24 Stunden, am Drop-Abend 30 Minuten.",
    "Jeden Textbaustein aus Woche 25 einmal tippen und prüfen.",
    "Eine Person als Backup für den Drop-Abend einweisen. Sie beantwortet Größenfragen mit den Bausteinen, du machst den Rest.",
   ], "Postfach, Antwortzeit und Backup stehen.")],
 [T("A", "Werbung aufsetzen (Karfreitag)", 45, [
    "Kampagne 1 „Warteliste“: Ziel Traffic auf die Startseite. Zielgruppen aus Woche 26 plus eine ähnliche Zielgruppe (Lookalike 1 %, Deutschland) aus den Instagram-Interaktionen. Laufzeit Mo 29.03. bis Mi 21.04., Budget 150 € gesamt.",
    "Kampagne 2 „Drop“: Ziel Käufe, nur Retargeting (Shop-Besucher 30 Tage, Instagram-Interaktionen). Laufzeit Do 22.04., 19:00, bis So 25.04., Budget 150 € gesamt.",
    "Anzeigen: Kampagnenfilm, dein bestes organisches Video (meiste Views im Blatt „Content“), Karussell mit 5 Makros A–E.",
    "Beide Kampagnen heute einreichen. Die Prüfung durch Meta kann bis zu 24 Stunden dauern.",
   ], "Beide Kampagnen sind eingereicht, mit Laufzeit und Budget."),
  T("S", "Launch-Clip schneiden", 45, [
    SPIEL + "15 Sekunden durchs Feld bis zur verschlossenen Tür, aus den Bildschirmaufnahmen vom Playtest.",
    "Hook: „Diese Tür öffnet sich am 22. April um 19:00.“",
   ], "Der Launch-Clip ist exportiert."),
  PW[28][4]],
 [PW[28][5],
  T("A", "Alle Termine bis zum Drop in den Kalender", 20, [
    "Mit Erinnerung: 24 Countdown-Posts um 18:00, E-Mails T−14 (Do 08.04.), T−7 (Do 15.04.), T−3 (Mo 19.04.), T−24h (Mi 21.04.), T−1h (Do 22.04., 18:00), LIVE (19:00), freie Tage, Packtage.",
    "Heute Nacht werden die Uhren umgestellt. Shopify → Einstellungen → Allgemein: Steht die Zeitzone auf Berlin, stimmen alle geplanten Zeiten automatisch.",
   ], "Alle Termine stehen im Kalender, die Zeitzone ist Berlin.")],
 [T("C", "Countdown-Start vorbereiten", 15, [
    "Ordner „Countdown“: Sind T−24 bis T−1 alle da und richtig benannt?",
    "Die Caption für jeden Tag in die Notizen-App, damit du nur noch einfügst.",
   ], "Alle 24 Videos und Captions sind bereit."),
  REVIEW(28)],
])

# ---------- Woche 29 ----------
W29 = dict(n=29, phase="P5", goal="Countdown läuft. Ware annehmen und jede Jeans prüfen", days=[
 [cd(24),
  T("S", "DAS FELD IST OFFEN", 30, [
    SPIEL + "Statt des Countdown-Assets heute den Launch-Clip posten (TikTok und Reel, 18:00).",
    "Link in beide Bios, Story mit Bildschirmaufnahme vom Feld.",
   ], "Das Feld ist angekündigt, der Link steht in beiden Bios."),
  T("A", "Werbung: Freigabe prüfen", 10, [
    "Werbeanzeigenmanager: Ist Kampagne 1 aktiv? Abgelehnte Anzeigen sofort korrigieren und neu einreichen.",
   ], "Kampagne 1 läuft.")],
 [cd(23, "Die Ware ist da: Kartons im Flur, der erste Griff in den Karton."),
  T("B", "WARENANNAHME", 45, [
    "Kommt die Ware an einem anderen Tag, tauschst du diese Aufgabe mit dem Tag der Ankunft.",
    "Kartons zählen, bevor du unterschreibst. Außenschäden fotografieren und auf dem Lieferschein „unter Vorbehalt“ vermerken.",
    "Einen Karton öffnen und kurz filmen (Countdown-Clip heute).",
    "Kartons mit der Packliste abgleichen: Stück pro Größe.",
    "Trocken lagern, nicht auf dem Boden.",
   ], "Alle Kartons sind gezählt und mit der Packliste abgeglichen.")],
 [cd(22),
  T("B", "Prüfung Teil 1: Sichtprüfung der ersten 50", 100, [
    "Die erste Hälfte der Kartons, ca. 50 Jeans. Pro Jeans 2 Minuten, Prüfliste „Wareneingang“ (Referenz → Prüfplan Sample).",
    "Vorn: Band A, Münztasche E. Hinten links: B2 mit drei Ähren, rotem Band und 9 Goldfäden (sitzen sie fest?). Hinten rechts: Alatyr C. Patch D gerade. Linkes Bein: Serp B an der Seitennaht. Dazu Nähte, Knopf, Reißverschluss, Saum, Flecken, Größenlabel.",
    "In Ordnung: grüner Punkt auf das Größenlabel. Fehler: roter Punkt, Foto, Eintrag ins Blatt „QC“ (Karton, Größe, Fehler, Foto-Nummer).",
    "Noch keine Hangtags. Die Nummern vergibst du beim Packen.",
   ], "50 Jeans haben einen grünen oder roten Punkt.")],
 [cd(21),
  T("B", "Prüfung Teil 2: Sichtprüfung der zweiten 50", 100, [
    "Gleiche Prüfliste, gleiche Punkte, die zweite Hälfte.",
    "Am Ende: Zahl grün und Zahl rot ins Blatt „QC“.",
   ], "Alle Jeans haben einen grünen oder roten Punkt.")],
 [cd(20),
  T("B", "Prüfung Teil 3: Maße", 60, [
    "15 Jeans messen, 3 pro Größe, alle 10 Messpunkte (Prüfplan). Ins Blatt „QC“.",
    "Liegt eine Größe außerhalb der Toleranz, Claude sofort schreiben.",
   ], "15 Messprotokolle stehen in der Tabelle."),
  T("B", "Fehler sortieren und reklamieren", 30, [
    "Alle roten Punkte nach Fehlerklasse sortieren: kritisch, Hauptfehler, Nebenfehler (Prüfplan).",
    "Kritische Fehler: Fotos und Liste mit dem Prompt unten an die Fabrik, Gutschrift oder Ersatz fordern. Frist 14 Tage ab Ankunft.",
    "Hauptfehler wie lose Fäden oder ein fehlender Goldfaden: selbst nacharbeiten, wenn es unter 5 Minuten dauert.",
   ], "Die Reklamation ist raus oder es gibt nichts zu reklamieren.",
   "Hier ist meine Fehlerliste aus der Wareneingangsprüfung: … Schreib mir die Reklamation auf Englisch an die Fabrik, mit Foto-Nummern, Fehlerklasse und Forderung (Gutschrift pro kritischem Teil), mit Bezug auf die vereinbarte Frist von 14 Tagen.")],
 [cd(19),
  T("A", "Bestand einsortieren und im Shop setzen", 45, [
    "Nur Jeans mit grünem Punkt kommen ins Regal, sortiert nach Größe. Rote Teile in eine eigene Kiste „B-Ware“. Die werden nicht im Drop verkauft.",
    "Drop-Bestand pro Größe = geprüfte Jeans minus Vorbestellungen minus 5 Creator-Paare minus 2 Reserve. Ins Blatt „Bestand“.",
    "In Shopify beim Jeans-Produkt den Bestand pro Größe eintragen. „Weiterverkaufen, wenn nicht vorrätig“ bleibt AUS.",
   ], "Der Shop-Bestand stimmt mit dem Regal überein.")],
 [cd(18, "Das Prüfergebnis: „X von 100 geprüft und bestanden“, Stapel und Maßband im Bild. Nur echte Zahlen."),
  T("A", "Monatsabschluss März", 15, [
    "Warteliste gegen Ziel (zwischen 2.400 und 3.000). Ausgaben gegen Plan.",
   ], "Beide Zahlen stehen in der Tabelle."),
  T("S", "Feld-Zahlen der ersten Woche", 10, [
    SPIEL + "Anmeldungen mit Tag tt-feld gegen alle neuen Anmeldungen der Woche. Daran siehst du, ob das Spiel Adressen bringt oder nur Likes.",
   ], "Die Zahl steht im Blatt „Content“."),
  REVIEW(29)],
])

# ---------- Woche 30 ----------
W30 = dict(n=30, phase="P5", goal="Echte Produktfotos, Vorbestellungen und Creator-Pakete raus", days=[
 [cd(17),
  T("A", "Produktfotos der Serienware", 60, [
    "Tageslicht, weiße Wand. Eine W32 reicht.",
    "Vorn, hinten, liegend, dazu 4 Makros: A, E, B mit den Fäden, D.",
    "Die Shoot-Bilder bleiben vorn. Die Detailbilder kommen jetzt aus der Serie und ersetzen die Sample-Fotos. Der Hinweis „Abgebildet ist das Sample“ fliegt raus.",
   ], "Die Produktseite zeigt die echte Serienware.")],
 [cd(16),
  T("A", "Vorbestellungen packen, Teil 1", 90, [
    "Bestellungen im Blatt „Pre-Order“ nach Bestelldatum sortieren. Die erste Vorbestellung bekommt Nummer 001, die zweite 002 und so weiter.",
    "Pro Paket: Größe aus dem Regal, Hangtag mit der Nummer, Karte von Hand mit Vorname und Nummer („Nr. 007 · Danke, dass du früh dabei warst“), Seidenpapier, Karton, Stempel.",
    "Label in der Versandlösung erzeugen, Bestellung in Shopify als versendet markieren. Shopify schickt die Versandbestätigung mit Tracking.",
    "Nummer, Bestellnummer und Größe ins Blatt „Bestand“.",
    "Heute die erste Hälfte.",
   ], "Die erste Hälfte der Vorbestellungen ist gepackt und markiert.")],
 [cd(15, "Die ersten Pakete sind raus: Stapel Pakete, eine handgeschriebene Karte im Makro."),
  T("A", "Vorbestellungen packen, Teil 2 und abgeben", 75, [
    "Die zweite Hälfte wie gestern.",
    "Alle Pakete zur Filiale oder Abholung bestellen. Einlieferungsbeleg fotografieren.",
    "Blatt „Bestand“: Sind alle Vorbestellungen als versendet markiert?",
   ], "Alle Vorbestellungen sind unterwegs.")],
 [cd(14),
  T("A", "E-Mail T−14 senden", 10, [
    "Entwurf aus Woche 24 in Shopify Email öffnen, Zahlen prüfen (Stückzahl, Preise, Größen).",
    "Versand heute 18:00 an alle Abonnenten.",
   ], "E-Mail T−14 ist geplant."),
  T("C", "Creator-Pakete verschicken", 45, [
    "5 Pakete an die Creator aus Woche 19 und 20. Ihre Nummern kommen direkt nach den Vorbestellungen.",
    "Karte im Paket: „Danke! Wenn sie dir gefällt: ein Post oder eine Story zwischen 17. und 21. April, mit Markierung. Keine Vorgaben zum Text.“",
    "Dazuschreiben: Weil sie die Jeans geschenkt bekommen, müssen sie den Post als Werbung kennzeichnen (z. B. „Anzeige“). Freundlich, aber klar.",
    "Tracking-Nummern ins Blatt „Creator“.",
   ], "5 Creator-Pakete sind unterwegs.")],
 [cd(13),
  T("S", "Generalprobe auf einer zweiten Theme-Kopie", 45, [
    SPIEL + "Testprodukt zu 1 €, die Drop-Zeit in den Section-Einstellungen auf heute in 30 Minuten.",
    "Einmal alles durch: Feld, Schlüssel-Link, Tür, Produkt, Kauf, Erstattung.",
   ], "Die Generalprobe lief einmal komplett durch."),
  T("A", "Werbung: Zwischenstand", 10, [
    "Kampagne 1: Kosten pro Klick und neue Anmeldungen seit 29.03. Läuft eine Anzeige deutlich schlechter, pausieren.",
   ], "Die schwächste Anzeige ist pausiert oder alle laufen gut.")],
 [cd(12),
  T("C", "Fotos von Vorbestellern einsammeln", 30, [
    "Allen Vorbestellern eine kurze Nachricht (Prompt unten), per E-Mail oder DM.",
    "Reposten nur mit ausdrücklichem Ja.",
   ], "Alle Vorbesteller haben die Nachricht.",
   "Schreib mir eine kurze, persönliche Nachricht an Vorbesteller, deren Jeans gerade angekommen ist: Danke, ich hoffe, sie passt. Würdest du mir ein Foto oder Video in der Jeans schicken? Darf ich es in meiner Story zeigen? 40–60 Wörter, Du-Form.")],
 [cd(11, "Erste Fotos von Vorbestellern (nur mit Erlaubnis), schnell geschnitten."),
  REVIEW(30)],
])

# ---------- Woche 31 ----------
W31 = dict(n=31, phase="P5", goal="Letzte Woche vor dem Drop: alles terminieren, alles testen", days=[
 [cd(10),
  T("A", "Bestand ein letztes Mal zählen", 30, [
    "Regal pro Größe zählen und mit dem Shop vergleichen. Überverkauf in der Drop-Stunde ist der teuerste Fehler.",
    "Abweichungen klären, bevor du weitermachst.",
   ], "Regal und Shop stimmen überein.")],
 [cd(9),
  T("A", "Veröffentlichung auf Do 22.04., 18:00 planen", 30, [
    "Shopify → Einstellungen → Allgemein: Zeitzone Berlin?",
    "Jeans, Zipper und Polo auf Status „Aktiv“. Auf der Produktseite im Bereich „Veröffentlichung“ beim Onlineshop über das Kalender-Symbol den Termin setzen: 22.04.2027, 18:00. Hilfe dazu im Shopify Help Center unter „Future publishing“.",
    "Die Kollektion „Time Travel“ genauso auf 22.04., 18:00.",
    "Kontrolle im privaten Browserfenster: Die Produkt-URL muss heute noch „Seite nicht gefunden“ zeigen.",
   ], "Alle drei Produkte und die Kollektion sind auf 22.04., 18:00 geplant und heute unsichtbar.")],
 [cd(8),
  T("A", "Packstation für den Drop fertig machen", 30, [
    "Material für alle Drop-Pakete abgezählt, Kartons vorgefaltet.",
    "Karten mit Danke-Text vorgeschrieben. Name und Nummer kommen beim Packen dazu.",
   ], "Alles für den Drop liegt gepackt bereit."),
  T("A", "Drop-Startseite vorbereiten", 45, [
    "Ohne Spiel: Theme duplizieren, „Drop 22.04.“ nennen. Startseite: Bild-Banner mit dem Hauptbild aus der Abstimmung in Woche 24, Abschnitt „Ausgewählte Kollektion“ mit „Time Travel“, Link zur Größenseite. Nicht veröffentlichen. Das machst du am 22.04. um 19:00.",
    "Mit Spiel: nicht nötig. Die Tür öffnet um 19:00 von selbst, der Shop-Button führt zur Kollektion.",
   ], "Das Theme „Drop 22.04.“ ist fertig und unveröffentlicht (oder das Spiel übernimmt).")],
 [cd(7),
  T("A", "E-Mail T−7 senden", 10, [
    "Entwurf aus Woche 24, Zahlen prüfen, Versand heute 18:00.",
   ], "E-Mail T−7 ist geplant."),
  T("C", "Creator erinnern", 10, [
    "Kurze DM an alle 5: Post bitte zwischen Sa 17.04. und Mi 21.04., Kennzeichnung als Werbung nicht vergessen.",
   ], "Alle 5 sind erinnert."),
  T("S", "Schlüssel-Link testen", 20, [
    SPIEL + "Den Schlüssel-Link (?key=…) in den Entwurf der E-Mail T−1h einsetzen.",
    "Aus einem privaten Fenster testen. Drop-Zeit, Schlüssel und Produktlinks in den Section-Einstellungen ein letztes Mal lesen.",
   ], "Der Schlüssel-Link steht in der E-Mail und funktioniert im Testmodus.")],
 [cd(6),
  T("A", "Drop-Ablauf durchplanen", 30, [
    "Referenz → Drop-Tag Minute für Minute ausdrucken und mit deinen Zeiten ergänzen.",
    "Wer hilft wann? Ladegeräte, Laptop, zweiter Bildschirm.",
    "Prüfen: Liegt der Link zur Kollektion im Entwurf der E-Mail T−1h (ohne Spiel)?",
   ], "Der Ablauf liegt ausgedruckt neben dem Laptop.")],
 [cd(5),
  T("A", "Letzte Testbestellung", 30, [
    "Testprodukt 1 €, einmal am Handy, einmal am Laptop: Kasse, Bestätigungsmail, Label erzeugen.",
    "Erstatten, Label stornieren, Testprodukt löschen.",
   ], "Beide Testkäufe haben funktioniert."),
  T("S", "CODE-FREEZE", 5, [
    SPIEL + "Ab heute wird am Spiel nichts mehr geändert, auch keine Kleinigkeit.",
    "Jede Änderung in der Drop-Woche ist ein Risiko ohne Nutzen.",
   ], "Du hast den Code nicht mehr angefasst."),
  STATUS("Story-Q&A zum Drop", [
    "Fragen-Sticker: „Frag mich alles zum Drop“.",
    "30 Minuten lang alle Fragen beantworten, danach als Highlight „DROP INFO“ sichern.",
   ], 30)],
 [cd(4),
  REVIEW(31, ["Warteliste gegen Ziel 3.000.", "Alles getestet: Veröffentlichung geplant, Bestand gezählt, E-Mails geplant, Werbung bereit?"])],
])

# ---------- Woche 32 ----------
W32 = dict(n=32, phase="P5", goal="Drop-Woche", days=[
 [cd(3),
  T("A", "E-Mail T−3 senden", 10, [
    "Entwurf aus Woche 24: Größenhilfe und Ablauf des Drop-Tags. Versand heute 18:00.",
   ], "E-Mail T−3 ist geplant."),
  T("A", "Textbausteine griffbereit", 15, [
    "Alle Kürzel einmal testen. Dazu ein Baustein „In deiner Größe ausverkauft“ mit dem Hinweis auf Zipper und Polo.",
   ], "Alle Bausteine funktionieren.")],
 [cd(2),
  T("A", "Helfer briefen", 20, [
    "Ablauf vom Donnerstag mit der Backup-Person durchgehen: Wer beantwortet was?",
    "Packtage Fr und Sa: Uhrzeit, Ablauf, wer packt, wer etikettiert.",
   ], "Alle wissen, was sie am Do, Fr und Sa tun.")],
 [cd(1),
  T("A", "E-Mail T−24h senden", 10, [
    "Entwurf aus Woche 24, Versand heute 19:00.",
   ], "E-Mail T−24h ist geplant."),
  T("A", "Letzter Check", 20, [
    "Veröffentlichung 22.04., 18:00 bei allen drei Produkten und der Kollektion?",
    "Preise 169 / 139 / 79 €? Bestand pro Größe? Versandpreise? Zahlungsarten aktiv?",
    "E-Mails T−1h (18:00) und LIVE (19:00) geplant, mit den richtigen Links? Werbekampagne 2 eingeplant?",
    "Handy und Laptop laden.",
   ], "Alles geprüft, nichts ist offen.")],
 [T("C", "DROP · 22. April · 19:00", 180, [
    "Ab 17:00 frei. Nichts anderes einplanen.",
    "17:30 Shop am Handy öffnen (mit Spiel: das Feld). Preise und Bestände ein letztes Mal.",
    "18:00 Die Produkte gehen automatisch live. Die E-Mail T−1h geht an die Warteliste, mit dem Link zur Kollektion (mit Spiel: der Schlüssel-Link). Um 18:01 den Link selbst im privaten Fenster testen.",
    "18:00–19:00 Erste Bestellungen, DMs beantworten. Story: „Die Warteliste kauft gerade.“",
    "18:50 Story „10 Minuten“.",
    "19:00 Öffentlich: ohne Spiel das Theme „Drop 22.04.“ veröffentlichen. Die E-Mail LIVE geht raus. Kampagnenfilm als Post auf TikTok und Reel, Caption: „Time Travel ist live. 100 nummerierte Jeans, Zipper und Polo. Link in Bio.“ Story mit Link-Sticker, Link in beiden Bios auf die Kollektion.",
    "19:15 erster Zwischenstand in der Story, echte Zahl. 20:00 Restbestand pro Größe. 22:00 Danke und Zwischenstand.",
    "Bis 23:00 jede Nachricht beantworten. Bestand nie von Hand hochsetzen.",
   ], "Der Drop ist live, alle Nachrichten bis 23:00 sind beantwortet."),
  T("S", "Spiel am Drop-Tag", 10, [
    SPIEL + "17:30 Feld am Handy prüfen. 17:50 Schlüssel-Link im privaten Fenster: Die Tür ist noch zu.",
    "18:00 Geht die Tür mit Schlüssel auf? 19:00 Ist sie für alle offen?",
    "Hängt etwas: PLAN B veröffentlichen, geübt in unter einer Minute. Nicht debuggen.",
   ], "Die Tür war um 18:00 und 19:00 offen, oder PLAN B läuft.")],
 [T("A", "Packen, Tag 1", 180, [
    "Bestellungen in Shopify nach Eingang sortieren. Die Nummern laufen weiter nach den Creator-Paaren.",
    "Erst prüfen: Ist die Zahlung durch? Ist die Adresse vollständig? Unklare Adressen per E-Mail nachfragen (Textbaustein).",
    "Packen wie bei den Vorbestellungen: Hangtag, Karte, Seidenpapier, Karton, Label, als versendet markieren.",
    "Zipper und Polo nur zählen, nicht packen. Die werden ab Montag gefertigt.",
    "Ziel: Bis Samstagabend sind alle Bestellungen von Donnerstag und Freitag raus.",
   ], "Die erste Hälfte der Bestellungen ist unterwegs."),
  STATUS("Zwischenstand-Story", ["Echte Zahlen: verkauft und Restbestand pro Größe.", "Erste Fotos von Käufern reposten, nur mit Erlaubnis."])],
 [T("A", "Packen, Tag 2", 180, [
    "Alle restlichen Bestellungen wie gestern.",
    "Pakete abgeben oder Abholung, Einlieferungsbelege fotografieren.",
    "Blatt „Bestand“: Jede verkaufte Nummer hat eine Bestellnummer.",
   ], "Alle Jeans-Bestellungen bis Freitagabend sind unterwegs."),
  STORY("Drop 2", "Was soll Drop 2 werden?", "„Denim-Jacke“, „Teppich-Patch“, „Neues Muster“")],
 [T("B", "Blanks für Zipper und Polo bestellen", 30, [
    "Alle Zipper- und Polo-Bestellungen nach Größe und Farbe zählen.",
    "Blanks beim Anbieter aus Woche 6 bestellen, Lieferung zu dir oder direkt zum Sticker.",
    "Termin beim Sticker für Abgabe und Fertigstellung in den Kalender. Die Kunden haben „Versand innerhalb von 3 Wochen“ gelesen. Das ist deine Frist.",
   ], "Die Blanks sind bestellt, der Termin beim Sticker steht."),
  T("D", "Auswertung nach 72 Stunden", 45, [
    "Jeans verkauft, gesamt und pro Größe. Zipper und Polo. Umsatz gegen Break-even (60 Paar) und Ziel (64 Paar, 10.000 €).",
    "Werbung: Was hat eine Bestellung gekostet? Kampagne 2 endet heute von selbst.",
    "Ab jetzt jede Rücksendung mit Grund ins neue Blatt „Retouren“: zu klein, zu groß, gefällt nicht.",
    "Alles mit dem Prompt unten an Claude.",
   ], "Die Zahlen stehen in der Tabelle und sind bei Claude.",
   "Hier sind meine Drop-Zahlen nach 72 Stunden: … Werte sie aus und plane mit mir die nächsten 4 Wochen: Restbestand verkaufen, Zipper und Polo ausliefern, und was ich für Drop 2 anders mache."),
  T("S", "Feld behalten oder zurück", 10, [
    SPIEL + "Nach Zahlen entscheiden: Feld als Startseite behalten, bis ausverkauft, oder zurück aufs normale Theme.",
    "Das Spiel bleibt als Seite erhalten. Es ist das Gerüst für Drop 2.",
   ], "Die Entscheidung steht."),
  REVIEW(32)],
])

WEEKS_D = [W25, W26, W27, W28, W29, W30, W31, W32]
