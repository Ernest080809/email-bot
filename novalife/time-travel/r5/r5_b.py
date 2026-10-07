# -*- coding: utf-8 -*-
# Woche 9–16 · Stickdatei, Stickproben, Proto, PP-Sample, Shop
from r5_common import *
from r5_a import PW

PW[10] = {
 0: P("BUILD", "Die erste Stickprobe",
      "Das ist kein Papier mehr.",
      "Fotos und Video der Stickproben, die dir die Fabrik schickt (vorher fragen, ob du sie zeigen darfst). Deine Reaktion beim ersten Ansehen, ungeschnitten", "15–20 Sek.", batch=False),
 2: P("ORIGIN", "Warum Panel-Stickerei",
      "Warum man ein fertiges Hosenbein nicht besticken kann.",
      "Zeichnung auf Papier: ein flacher Zuschnitt neben einem Hosenbein als Röhre. Ein Stickrahmen passt nur auf den flachen Zuschnitt. Deshalb wird gestickt, bevor genäht wird", "25–30 Sek."),
 4: P("REAL", "Was an der Stickprobe falsch war",
      "Die erste Stickprobe hatte Fehler. Das hier.",
      "Fotos der Stickproben mit roten Kreisen (Markup in der Fotos-App). Pro Fehler ein Satz, und was die Fabrik jetzt ändert", "20–25 Sek.", batch=False),
}
PW[11] = {
 0: P("BUILD", "Drei Stoffe",
      "Drei Stoffe. Einer wird 100 Jeans.",
      "Stoffmuster am Fenster, deine Hand reibt den Stoff, Licht von der Seite, damit man den Köper sieht. Zum Schluss legst du die gewählte Probe nach vorn", "15–20 Sek."),
 2: P("ORIGIN", "Der Teppich",
      "Dieser Teppich hing bei allen an der Wand.",
      "Teppich-Fotos aus deiner Familie (oder ähnliche Teppiche), dann die Medaillon-Zeichnung für den Zipper-Rücken. Ein Satz: Daraus wird der Rücken des Zippers", "25–30 Sek."),
 4: P("REAL", "Warum 169 €",
      "Warum meine Jeans 169 € kostet.",
      "Von Hand aufgeschrieben: Basis-Jeans ~35 €, Stickerei ~18 €, Patch ~3 €, Handarbeit Goldfäden ~2 €, Versand und Verpackung. Am Ende: „Vorbestellt 149 €. Ab 14. Januar.“", "25–30 Sek."),
}
PW[12] = {
 0: P("BUILD", "Sie ist unterwegs",
      "Meine erste echte Jeans ist unterwegs.",
      "Tracking-Screenshot (Sendungsnummer geschwärzt), die Papierteile auf dem Tisch, ein Kalender mit dem Ankunftstag", "15 Sek."),
 1: P("ORIGIN", "Warum ein Sample",
      "Warum ich für eine einzige Jeans so viel bezahle.",
      "Die Papierteile, dann ein Satz: Ein Sample zeigt die Fehler, bevor sie 100-mal passieren. Danach die Prüfliste, die du für Donnerstag ausgedruckt hast", "20–25 Sek."),
 2: P("REACH", "Donnerstag",
      "Donnerstag wird aus Papier Garn.",
      "Aktueller Trend-Sound aus der TikTok-Bibliothek, schnelle Schnitte über alle Papierteile, letzter Frame: „Do.“", "8–12 Sek."),
 4: P("DETAIL", "Echter Kreuzstich",
      "Das ist kein Papier mehr.",
      "Makro der echten Stickerei: erst Band A, dann Münztasche E. Langsam, Licht vom Fenster. Gedreht am Donnerstag beim Auspacken", "15 Sek.", batch=False),
 5: STORY("Was zuerst?", "Was willst du zuerst in echt sehen?", "„Band“, „Münztasche“, „Rückseite“"),
}
PW[13] = {
 0: P("BUILD", "Was nicht gepasst hat",
      "Das erste Sample ist da. Das hier stimmt noch nicht.",
      "Maßband an den 2–3 größten Abweichungen aus deiner Korrekturliste, je ein Satz dazu. Ehrlich, nicht dramatisch", "25 Sek."),
 1: P("ORIGIN", "Das Band in echt",
      "Rauten, Sterne, Zickzack. Jetzt in Garn.",
      "Makro auf Band A, deine Hand an der Tasche. Pro Motiv ein Satz: Raute = bestelltes Feld, Zickzack = Wasser, Stern = Sonne", "25–30 Sek."),
 2: P("REACH", "Älter als jede Grenze",
      "Dieses Muster ist älter als jede Grenze.",
      "Trend-Sound, 3 Clips vom Fit-Test am Samstag: gehen, drehen, Hand in die Tasche", "10–15 Sek."),
 4: P("DETAIL", "Die Goldfäden",
      "Diese Fäden setzt eine Hand. Bei jeder Jeans anders.",
      "Makro auf die Gesäßtasche, die Fäden bewegen sich (Hand oder Fön auf kleinster Stufe). Hat das Proto noch keine Fäden: stattdessen Münztasche E im Makro", "15 Sek."),
 5: STORY("Vorbestellen?", "Würdest du sie vorbestellen?", "„Ja“, „Vielleicht“, „Nein“"),
}
PW[14] = {
 0: P("BUILD", "Die Vorbestellseite",
      "Ab 14. Januar kannst du sie vorbestellen.",
      "Bildschirm der Vorbestellseite (Entwurf): Fotos, Preis 149 € statt 169 €, „35 Paar“", "15–20 Sek."),
 1: P("ORIGIN", "Ehrliche Größen",
      "Meine W32 ist wirklich 32 Zoll.",
      "Maßband um den Bund des Protos: 81 cm = 32 Zoll. Daneben eine gekaufte W32 aus deinem Schrank, die mehr misst. Ein Satz: Wir labeln nach dem echten Maß", "25–30 Sek."),
 2: P("REACH", "100 Stück",
      "100 Stück. Danach nie wieder genau so.",
      "Trend-Sound, Makro-Schnitte: Band, Münztasche, Fäden, Patch, Alatyr", "8–12 Sek."),
 4: P("DETAIL", "Die Rückseite",
      "Die Rückseite verrät, wie gut eine Stickerei ist.",
      "Hose auf links: Innenseite der Stickerei, sauber geschnittenes Vlies, keine losen Fäden", "15 Sek."),
 5: STORY("Größe", "Welche Größe trägst du?", "„W30“, „W32“, „W34“, „W36+“"),
}
PW[15] = {
 0: P("BUILD", "12 Wochen",
      "12 Wochen: von Papier zu Garn.",
      "Clips aus deinen bisherigen Videos aneinander: Papiertest, Tabelle, Stickprobe, Sample", "20–25 Sek."),
 2: P("REAL", "Was es bis jetzt gekostet hat",
      "So viel habe ich 2026 in eine Jeans gesteckt.",
      "Summe aus dem Blatt „Ausgaben“ von Hand aufgeschrieben, aufgeteilt in Sample, Shop, Material. Ein Satz: Ab Januar muss die Vorbestellung den Rest tragen", "20 Sek."),
 5: STORY("2027", "Was soll ich 2027 mehr zeigen?", "„Prozess“, „Fertige Teile“, „Herkunft“"),
}
PW[16] = {
 0: P("BUILD", "Was 2027 passiert",
      "14. Januar Vorbestellung. 22. April Drop.",
      "Kalender oder Notizbuch mit den zwei Daten, dazu Clips des Samples", "15 Sek."),
 2: P("REACH", "Die einzige ihrer Art",
      "Es gibt sie 100-mal. Danach nie wieder.",
      "Trend-Sound, das Sample in drei schnellen Einstellungen (vorn, hinten, Makro)", "8–12 Sek."),
 5: STORY("14.01.", "Bist du am 14.01. um 19 Uhr dabei?", "„Ja“, „Erinnere mich“"),
}
PW[17] = {
 0: P("BUILD", "Das finale Sample",
      "Das ist die Jeans, die 100-mal entsteht.",
      "PP-Sample auspacken (gefilmt am Montag), gleich anziehen, einmal drehen", "15–20 Sek.", batch=False),
 1: P("ORIGIN", "Warum vorbestellen",
      "Warum ich verkaufe, bevor ich produziere.",
      "Ein Satz ins Handy: Die Anzahlung an die Fabrik kommt aus den Vorbestellungen. Wer vorbestellt, bezahlt 149 € statt 169 € und bekommt seine Stücknummer zuerst", "25–30 Sek."),
 2: P("REACH", "Nächster Donnerstag",
      "Nächsten Donnerstag, 19 Uhr.",
      "Trend-Sound, Makro-Schnitte vom PP-Sample, letzter Frame: „14.01. · 19:00“", "8–12 Sek."),
 4: P("DETAIL", "Stücknummer",
      "Jede Jeans hat eine Nummer. 001 bis 100.",
      "Hangtag-Entwurf oder Labels am PP-Sample im Makro", "15 Sek."),
 5: STORY("Erinnerung", "Soll ich dich am Donnerstag erinnern?", "„Ja“, „Bin eh da“", extra=["Allen, die „Ja“ tippen, am Donnerstag um 18:55 eine DM schicken."]),
}

def wochenposts(n):
    return list(PW[n].values())

# ---------- Woche 9 ----------
W9 = dict(n=9, phase="P2", goal="Stickdatei prüfen, Berliner Muster starten, Stoff anfragen", days=[
 [T("B", "Digitizing-Vorschau prüfen", 45, [
    "Die Fabrik schickt pro Element eine Vorschau (Bild oder PDF) und die Stichzahl.",
    "Mit dem Prompt unten an Claude: Maße und Motive gegen das Elementblatt, Stichzahl gesamt nahe ~33.000 (Design v1.7), echter Kreuzstich oder feine Füllung bei A, C und E.",
    "Liegt die Summe deutlich über 33.000: Claude rechnet Stückkosten, Anzahlung und die Schwellen 01.02. und 19.03. neu, bevor du freigibst.",
    "Abweichungen als nummerierte Liste mit Screenshot an die Fabrik.",
    "Kommt die Vorschau nicht bis heute: freundlich nachfragen und den Termin aus der Bestätigung zitieren.",
   ], "Die Korrekturliste oder ein „Passt“ ist an die Fabrik raus.",
   "Hier ist die Digitizing-Vorschau der Fabrik für A–E mit Stichzahlen: … Vergleiche mit Design v1.5 und der Spec: Maße, Motive, Stichart, Dichte. Gib mir eine nummerierte Korrekturliste auf Englisch."),
  PW[9][0]],
 [T("D", "Digitizing freigeben", 20, [
    "Wenn die Korrekturen drin sind, schriftlich: „Digitizing A–E approved for stitch-out.“",
    "Stichzahl pro Element ins Blatt „Fabriken“. Davon hängt der Endpreis ab.",
   ], "Die Freigabe ist per Mail raus."),
  T("B", "Blanks zu den Berliner Stickern", 20, [
    "Sind Zipper und Polo da? Dann zu den beiden ausgewählten Stickern bringen (oder beide zu einem, wenn nur einer beides kann).",
    "Termin für die Abholung notieren. Ziel: bis Woche 11 fertig.",
   ], "Die Teile sind beim Sticker.")],
 [T("B", "Stoffoptionen anfordern", 20, [
    "Die Fabrik um 2–3 Denim-Optionen bitten: 12 oz, 100 % Baumwolle, rigid, 3/1 Köper. Je ein Stück roh und ein Stück im Zielton gewaschen.",
    "Dazu ein Foto des gewaschenen Stücks neben einer Graukarte oder einem weißen Blatt, damit du den Ton beurteilen kannst.",
    "Fragen: Ist der Stoff Lagerware? Reicht er für 100 Paar (ca. 150 m) bis Februar?",
   ], "Die Anfrage ist raus."),
  PW[9][2]],
 [T("A", "Größenseite und FAQ für den Shop", 45, [
    "Text mit dem Prompt unten bei Claude holen.",
    "Shopify → Onlineshop → Seiten → „Größen“ und „FAQ“ anlegen, noch nicht im Menü verlinken.",
   ], "Beide Seiten sind als Entwurf angelegt.",
   "Schreib mir die Größenseite für Shopify: Tabelle W30–W38 aus der Spec (Bund, Hüfte, Innenbein), Anleitung „Miss deine Lieblingsjeans“ in 4 Schritten, Umrechnung „Eightyfive/Carhartt/Dickies W30 → Novalife W32“. Dazu 8 FAQ: Lieferzeit, Größe, Pflege, Goldfäden, Rückgabe, Versandkosten, Vorbestellung, Stücknummer.")],
 [T("B", "Muster des Label-Patches bestellen", 20, [
    "Bester Anbieter aus dem Blatt „Patches“: 3 Muster von Patch D (86 × 76 mm) bestellen, Lieferung an dich. Budget 80 €.",
    "Warum 3: eines wäschst du selbst, zwei gehen später an die Fabrik für das PP-Sample.",
    "Dem Anbieter schreiben: Der Patch wird auf die Jeans genäht und dann industriell gewaschen (Enzym-/Steinwäsche). Bitte vorgewaschenes Leinen und eine feste Kante.",
    "Chenille-Patch für den Zipper: nur Angebot, entschieden wird in Woche 14.",
   ], "3 Muster sind bestellt, der Liefertermin steht im Blatt „Patches“."),
  PW[9][4]],
 [T("A", "Puffer", 30, ["Liegengebliebenes erledigen.", "Kommentare und DMs beantworten."], "Aus Woche 9 ist nichts mehr offen.")],
 [REVIEW(9), BATCH([p for p in wochenposts(10) if p[-1].get("batch")], 10)],
])

# ---------- Woche 10 ----------
W10 = dict(n=10, phase="P2", goal="Stickproben und Stoff bewerten, Farben festlegen", days=[
 [T("B", "Stickproben bewerten", 60, [
    "Die Fabrik schickt Fotos und ein Video jeder Stickprobe, ungewaschen und gewaschen. Physische Stücke per Post sind besser, wenn es zeitlich passt.",
    "Prüfliste: Referenz → Prüfplan Sample, Teil „Stickerei“. Wellen? Einzug? Konturen scharf? Farben? Rückseite? Nach der Wäsche ausgefranst oder stumpf?",
    "Mit dem Prompt unten an Claude.",
    "Video vom ersten Ansehen für den BUILD-Post heute Abend.",
   ], "Pro Element steht fest: passt oder Korrektur.",
   "Hier sind Fotos und Video der Stickproben (ungewaschen und gewaschen): … Bewerte jedes Element A–E gegen die Spec: Wellen, Einzug, Konturen, Farben, Rückseite, Waschergebnis. Gib mir pro Element „ok“ oder eine konkrete Korrektur auf Englisch."),
  PW[10][0]],
 [T("D", "Stickproben und Garnfarben freigeben", 30, [
    "Pro Element A–E: freigeben oder Korrektur mit Foto und Maß.",
    "Garnfarben entscheiden: Weiß, Rot, Gold, Braun. Nur auf echtem, gewaschenem Denim beurteilen, nie am Bildschirm.",
    "Freigabe schriftlich, Garnnummern ins Blatt „Fabriken“.",
   ], "Freigabe oder Korrekturliste ist raus.")],
 [T("B", "Stoffmuster bewerten", 45, [
    "Bei Tageslicht am Fenster ansehen. Neben deine Eightyfive legen: Ziel ist deutlich dunkler als die Eightyfive (Spec: L* 34–40).",
    "Gewicht in der Hand, Griff, ist der Köper sichtbar?",
    "Eine Option wählen und der Fabrik schriftlich bestätigen. Bitte um Reservierung für 100 Paar.",
   ], "Der Stoff ist gewählt und bestätigt."),
  PW[10][2]],
 [T("A", "Produktseite Jeans als Entwurf", 45, [
    "Shopify → Produkte → hinzufügen, Status „Entwurf“ (unsichtbar).",
    "Titel „Time Travel Jeans · NVL-TT-01“, Varianten W30, W32, W34, W36, W38. Preis 169 €.",
    "Text mit dem Prompt unten bei Claude holen und einsetzen. Bilder kommen in Woche 13.",
   ], "Die Produktseite existiert als Entwurf.",
   "Schreib mir den Produkttext für die Time Travel Jeans NVL-TT-01: 1 Satz Kern, 1 Absatz zum Muster (Raute, Zickzack, Stern, Lebensbaum, Ernte mit Goldfäden), 1 Absatz Material und Passform (12 oz, 100 % Baumwolle, rigid, Straight, ehrliche Größen), Pflege, Stücknummer 001–100. Sprachregel beachten, nie „authentisch“.")],
 [PW[10][4]],
 [T("A", "Puffer", 30, ["Liegengebliebenes erledigen.", "Kommentare und DMs beantworten."], "Aus Woche 10 ist nichts mehr offen.")],
 [REVIEW(10), BATCH(wochenposts(11), 11)],
])

# ---------- Woche 11 ----------
W11 = dict(n=11, phase="P2", goal="Das Proto entsteht, der Shop wird rechtssicher", days=[
 [T("B", "Status Proto abfragen", 15, [
    "Die Fabrik um Fotos bitten: Zuschnitt, bestickte Panels, Montage.",
    "Versanddatum bestätigen lassen. Ziel: Versand bis Mo 30.11., Ankunft Do 03.12.",
   ], "Fotos und Versanddatum sind da."),
  PW[11][0]],
 [T("A", "AGB, Widerruf, Versand- und Zahlungsinfos", 60, [
    "Für den Verkauf ab Januar brauchst du rechtssichere AGB, eine Widerrufsbelehrung mit Muster-Widerrufsformular, Versand- und Zahlungsinformationen.",
    "Empfehlung: ein kostenpflichtiger Rechtstexte-Service mit Abmahnschutz (z. B. IT-Recht Kanzlei oder Händlerbund). Preise vergleichen, Kosten aus dem Puffer. Für einen Shop mit Vorkasse ist das die billigste Versicherung.",
    "Texte in Shopify unter Einstellungen → Richtlinien einsetzen, im Footer verlinken.",
   ], "Alle Rechtstexte sind im Shop und verlinkt.")],
 [T("A", "Zahlungsanbieter einrichten", 45, [
    "Shopify → Einstellungen → Zahlungen: Shopify Payments aktivieren. Ausweis und Bankkonto bereithalten.",
    "PayPal zusätzlich verbinden.",
    "Die Testbestellung kommt in Woche 16.",
   ], "Shopify Payments und PayPal sind aktiv."),
  PW[11][2]],
 [T("B", "Patch-Muster prüfen und waschen", 30, [
    "Sind die 3 Muster da? Wenn nicht: beim Anbieter nachfragen, Liefertermin ins Blatt „Patches“.",
    "Gegen das Elementblatt halten: 86 × 76 mm? Einrollungen und Knoten sauber, Linien nicht zugelaufen? Farben wie im Design?",
    "Waschtest mit einem Muster: dreimal bei 60 °C waschen. Schrumpft das Leinen, wellt sich der Patch oder franst die Kante, muss der Anbieter nachbessern, bevor du 110 Stück bestellst.",
    "Fotos vorher und nachher an Claude.",
   ], "Du weißt: Der Patch hält die Wäsche, oder der Anbieter hat eine Korrekturliste."),
  T("B", "Prüfung des Protos vorbereiten", 20, [
    "Referenz → Prüfplan Sample ausdrucken.",
    "Bereitlegen: Maßband 150 cm, Lineal, heller Tisch, Handy mit freiem Speicher.",
    "Zwei Freunde mit W32 für Samstag, 05.12., anfragen (Fit-Test, 30 Minuten).",
   ], "Prüfplan liegt ausgedruckt bereit, Fit-Termin steht.")],
 [PW[11][4]],
 [T("A", "Versand im Shop einrichten", 30, [
    "Shopify → Einstellungen → Versand: Zonen Deutschland und EU.",
    "Gewicht pro Paket 1,0 kg ansetzen (Jeans ca. 0,7 kg plus Karton).",
    "Kundenpreis: Empfehlung 4,90 € in Deutschland, EU nach DHL-Tarif aufgerundet. Echte Portokosten im DHL-Geschäftskundenportal nachsehen.",
   ], "Versandzonen und Preise stehen.")],
 [REVIEW(11, ["Monatsende November: Warteliste notieren. Ziel bis 31.12.: 700."]), BATCH(wochenposts(12), 12)],
])

# ---------- Woche 12 ----------
W12 = dict(n=12, phase="P2", goal="Das erste echte Teil kommt an", days=[
 [T("B", "Versand des Protos verfolgen", 10, [
    "Tracking-Nummer von der Fabrik.",
    "Bei Versand aus der Türkei meldet sich der Paketdienst wegen Einfuhrumsatzsteuer (19 %) und einer Gebühr. EORI-Nummer und Rechnung der Fabrik als PDF bereithalten.",
    "Kommt es später als Donnerstag, verschiebt sich der Rest dieser Woche um die Tage.",
   ], "Du kennst den Ankunftstag."),
  PW[12][0]],
 [PW[12][1]],
 [PW[12][2]],
 [T("B", "SAMPLE DA: auspacken und messen", 75, [
    "Erst filmen, dann denken. Das Auspacken komplett filmen, ungeschnitten. Deine echte Reaktion ist einer der stärksten Posts des ganzen Drops.",
    "Alle 10 Messpunkte messen (Referenz → Prüfplan Sample): flach hinlegen, glattstreichen, nicht ziehen, jeden Punkt zweimal.",
    "Ist-Wert gegen W32-Soll und Toleranz ins Blatt „Proto“ (neues Blatt).",
    "Fotos: vorn, hinten, jedes Element A–E nah, Innenseite, Rückseite der Stickerei. Makros für den DETAIL-Post morgen gleich mit.",
   ], "10 Messwerte und mindestens 12 Fotos sind in der Tabelle.")],
 [T("B", "Stickerei und Verarbeitung prüfen", 45, [
    "Prüfplan Teil „Stickerei“ und Teil „Verarbeitung“ Punkt für Punkt.",
    "Jede Abweichung mit Foto-Nummer ins Blatt „Proto“.",
   ], "Alle Punkte des Prüfplans haben ein Ergebnis."),
  PW[12][4]],
 [T("B", "Fit-Test mit zwei Personen", 60, [
    "Beide ziehen das Proto an.",
    "Pro Person 4 Fotos: vorn, seitlich, hinten, sitzend.",
    "Fragen: Wo drückt es? Bund, Schritt, Oberschenkel, Knie? Länge?",
    "Notizen ins Blatt „Proto“. Der Oberschenkel mit 30 cm statt 28 cm war Absicht für die Stickfläche. Hier wird entschieden, ob er bleibt.",
    "3 kurze Clips (gehen, drehen, Hand in die Tasche) für den REACH-Post am Mittwoch.",
   ], "Fotos und Notizen beider Personen sind in der Tabelle."),
  PW[12][5]],
 [T("B", "Korrekturliste mit Claude", 45, [
    "Messwerte, Fotos und Fit-Notizen mit dem Prompt unten an Claude.",
    "Liste lesen und prüfen, ob alles stimmt, was du gesehen hast.",
   ], "Die Korrekturliste auf Englisch ist fertig.",
   "Hier sind die Messwerte, Fotos und Fit-Notizen vom Proto: … Schreib mir die Korrekturliste für die Fabrik auf Englisch (Messpunkt, Ist, Soll, Änderung in cm, Foto-Nummer), dazu die Stickerei-Korrekturen, und gib mir eine Empfehlung: Oberschenkel 28 oder 30 cm."),
  REVIEW(12), BATCH(wochenposts(13), 13, 80)],
])

# ---------- Woche 13 ----------
W13 = dict(n=13, phase="P2", goal="Korrekturen raus, PP-Sample bestellen, Fotos für die Vorbestellung", days=[
 [T("B", "Korrekturen senden und PP-Sample bestellen", 45, [
    "Korrekturliste mit Fotos an die Fabrik.",
    "PP-Sample bestellen: W32 mit allen Korrekturen, bestickt, genäht, gewaschen, Goldfäden gesetzt, Labels dran. Fehlt eines davon, ist es kein PP-Sample.",
    "Termin schriftlich: Versand spätestens Mo 04.01.2027. Portugal hat zwischen den Jahren meist Pause, die Türkei nicht.",
    "Die 2 übrigen Patch-Muster per Expressversand an die Fabrik. Einer kommt aufs PP-Sample, der zweite geht als Waschtest durch das echte Waschrezept der Fabrik. Foto vom Ergebnis anfordern.",
   ], "Das PP-Sample ist bestellt, das Versanddatum steht schriftlich fest, die Patches sind unterwegs."),
  PW[13][0]],
 [T("B", "Mini-Shoot 1: Produktfotos vom Proto", 60, [
    "Tageslicht, weiße Wand oder heller Boden.",
    "Liegend vorn und hinten, von oben fotografiert (Handy über dem Kopf, gerade halten).",
    "Makros: A, E, B mit den Fäden, C, D. Ruhig, scharf, kein Filter.",
    "Diese Bilder kommen auf die Vorbestellseite. Dort steht dazu: „Abgebildet ist das Sample. Das Serienteil kann minimal abweichen.“",
   ], "Mindestens 12 gute Fotos liegen im Ordner „Shop“."),
  PW[13][1]],
 [PW[13][2]],
 [T("B", "On-Body-Fotos", 60, [
    "Du oder ein Freund mit W32.",
    "Ruhiger Hintergrund (Hof, Wand, leere Straße), Tageslicht.",
    "Ganzkörper vorn, hinten, seitlich, beim Gehen. Detail: Hand an der Tasche.",
    "Dazu 3 Clips à 5 Sekunden für Reels.",
   ], "Mindestens 8 On-Body-Fotos und 3 Clips im Ordner „Shop“.")],
 [PW[13][4]],
 [T("A", "Produktseite mit echten Bildern", 45, [
    "Die besten Fotos in die Produktseite (Entwurf): 1 Ganzkörper vorn, 1 hinten, 4 Makros, 1 liegend.",
    "Dateien vorher sauber benennen, z. B. „time-travel-jeans-vorn.jpg“.",
    "Größenseite verlinken.",
   ], "Die Produktseite sieht in der Vorschau fertig aus."),
  PW[13][5]],
 [REVIEW(13), BATCH(wochenposts(14), 14)],
])

# ---------- Woche 14 ----------
W14 = dict(n=14, phase="P2", goal="Vorbestellung bauen, Berliner Muster entscheiden", days=[
 [T("A", "Vorbestellung in Shopify anlegen", 60, [
    "Neues Produkt „Time Travel Jeans · Vorbestellung“, Preis 149 €, Varianten W30–W38.",
    "Bestand gesamt 35 nach der Startannahme verteilen: W30 5, W32 10, W34 10, W36 7, W38 3.",
    "Bei jeder Variante „Weiterverkaufen, wenn nicht vorrätig“ AUS. Sonst verkaufst du mehr, als es gibt.",
    "Oben in den Text, fett: „Vorbestellung. Versand zwischen 22. und 30. April 2027.“ Ein konkretes Lieferfenster ist Pflicht.",
    "Darunter: „Vorbestellpreis 149 € bis Sonntag, 21.03.2027, 20:00 oder solange die 35 Paar reichen. Ab dem Drop 169 €.“",
    "Status bleibt „Entwurf“ bis zum 14.01.",
   ], "Das Vorbestell-Produkt ist komplett angelegt, Status Entwurf."),
  PW[14][0]],
 [T("A", "Vorbestellung rechtlich sauber", 30, [
    "Lieferfenster überall gleich: 22.–30.04.2027. Nie nur „voraussichtlich“.",
    "Widerrufsrecht gilt auch bei Vorbestellungen: 14 Tage ab Erhalt der Ware.",
    "FAQ ergänzen: Was passiert, wenn sich die Produktion verzögert? Antwort: Du bekommst sofort eine Mail und auf Wunsch dein Geld zurück.",
   ], "Lieferfenster und FAQ sind überall gleich."),
  PW[14][1]],
 [T("A", "E-Mails für den Vorbestell-Start", 45, [
    "Texte mit dem Prompt unten bei Claude holen.",
    "Shopify → Marketing → Shopify Email: vier Entwürfe anlegen, noch nicht senden.",
   ], "Vier E-Mail-Entwürfe liegen in Shopify.",
   "Schreib mir 4 E-Mails für Shopify Email: 1) Do 07.01. „Nächsten Donnerstag öffnet die Vorbestellung“ 2) Mi 13.01. „Morgen 19 Uhr“ 3) Do 14.01. 18:00 Early Access „Für dich eine Stunde früher: 35 Paar zu 149 €“ 4) Mo 18.01. „Noch X Paar“. Je Betreff, Vorschautext, 80–120 Wörter, ein Button. Sprachregel beachten."),
  PW[14][2]],
 [T("B", "Berliner Muster abholen und entscheiden", 45, [
    "Zipper und Polo abholen. Bei Tageslicht prüfen: Stichbild, Verzug im Fleece und im Piqué, Rückseite, Reste vom Topping.",
    "Einmal waschen (30 °C, auf links) und nochmal prüfen.",
    "Einen Sticker wählen. Preis pro Teil bei 1 / 10 / 50 Stück und die Lieferzeit pro Auftrag schriftlich bestätigen lassen.",
    "Gleich mitfragen: Was kostet das Teppich-Medaillon direkt auf den Zipper-Rücken gestickt (statt Chenille-Patch), bei 1 / 10 / 50 Stück? Die Antwort brauchst du am Samstag.",
   ], "Der Sticker ist gewählt, Preis und Lieferzeit stehen schriftlich."),
  T("B", "Patch D in Serie bestellen", 30, [
    "Nur wenn der Waschtest aus Woche 11 bestanden ist.",
    "110 Stück (100 plus 10 Reserve) beim gewählten Anbieter. Lieferung direkt an die Fabrik, spätestens Fr 22.01.2027. Die Fabrik näht den Patch vor der Wäsche an.",
    "Lieferadresse und Ansprechpartner vorher bei der Fabrik erfragen. Auf den Karton: „NVL-TT-01 · Label patch D · 110 pcs“.",
    "Zahlung (ca. 330 €) ins Blatt „Ausgaben“. Das ist Teil der Stückkosten von ~63 €, wird aber jetzt fällig, nicht im Februar.",
   ], "Die Bestellung ist bestätigt, Liefertermin und Adresse stehen schriftlich.")],
 [PW[14][4]],
 [T("D", "Vorbestellung: Kontingent und Start festlegen", 15, [
    "Empfehlung: 35 Paar zum Vorbestellpreis. Das rechnerische Minimum liegt bei 31, deshalb nicht 30.",
    "Start Do 14.01.2027, 19:00. Die Warteliste bekommt den Link um 18:00, eine Stunde früher.",
    "Entscheidung Claude schreiben, damit Plan und E-Mails stimmen.",
   ], "Kontingent und Startzeit stehen fest."),
  T("D", "Zipper-Rücken: gestickt oder Chenille", 15, [
    "Chenille-Patches haben beim Hersteller meist 50–100 Stück Mindestmenge, bei ~6 € also 300–600 €, bezahlt vor dem Drop. Das passt nicht zu „Zipper auf Bestellung, ohne Kapital“.",
    "Gestickt beim Berliner Sticker: Mindestmenge 1, Preis pro Teil laut Angebot vom Donnerstag.",
    "Meine Empfehlung: gestickt. Chenille nur, wenn ein Anbieter 20 Stück oder weniger macht. Echter Teppich-Flor kommt in Drop 2 mit den Tufting-Artists.",
    "Entscheidung Claude schreiben. Bei Chenille bestellst du jetzt ein Muster (Budget 120 €).",
   ], "Die Entscheidung steht und ist an Claude gemeldet."),
  PW[14][5]],
 [REVIEW(14), BATCH(wochenposts(15) + wochenposts(16), 15, 100, "Woche 15 und 16")],
])

# ---------- Woche 15 ----------
W15 = dict(n=15, phase="P3", goal="Feiertage: wenig, aber sauber", days=[
 [PW[15][0]],
 [T("A", "Belege 2026 sortieren", 30, [
    "Alle Rechnungen und Belege 2026 in einen Ordner (digital), Dateiname mit Datum.",
    "Summe pro Monat ins Blatt „Ausgaben“. Du brauchst das für die Steuer.",
   ], "Alle Belege 2026 liegen sortiert vor.")],
 [PW[15][2]],
 [],
 [],
 [PW[15][5]],
 [T("S", "Spiel-Stiltest", 150, [
    "Aseprite kaufen (ca. 20 €, aus dem Puffer).",
    "Eine Figur 16 × 32 px in zwei Laufposen zeichnen und eine Weizen-Kachel im Sonnenuntergang.",
    "Die ehrliche Frage an dich: Schaffst du das in dieser Qualität zehnmal?",
    "Wenn nein: Silhouettenstil (siehe Referenz → Das Spiel · Bauplan). Halb so viel Arbeit.",
   ], "Du weißt: Pixel oder Silhouette."),
  REVIEW(15, minuten=15)],
])

# ---------- Woche 16 ----------
W16 = dict(n=16, phase="P3", goal="PP-Sample unterwegs, Shop-Generalprobe", days=[
 [T("B", "Versand des PP-Samples bestätigen", 10, [
    "Tracking-Nummer anfordern. Ankunft bis spätestens Mi 06.01. einplanen.",
   ], "Du kennst den Ankunftstag."),
  PW[16][0]],
 [T("A", "Testbestellung im Shop", 30, [
    "Ein Testprodukt für 1 € anlegen und mit deiner echten Karte kaufen.",
    "Prüfen: Bestellbestätigung, Rechnung, Steuer- oder Kleinunternehmer-Hinweis, Absender, Logo.",
    "Bestellung erstatten, Testprodukt löschen.",
   ], "Der Kauf hat geklappt und ist erstattet.")],
 [PW[16][2]],
 [T("A", "Monatsabschluss Dezember", 15, [
    "Warteliste gegen Ziel 700. Darunter: Claude fragen, welche Posts die meisten Anmeldungen gebracht haben, und davon im Januar mehr.",
    "Ausgaben Dezember gegen Plan (700 €).",
   ], "Beide Zahlen stehen in der Tabelle.")],
 [],
 [PW[16][5]],
 [REVIEW(16), BATCH([p for p in wochenposts(17) if p[-1].get("batch")], 17)],
])

WEEKS_B = [W9, W10, W11, W12, W13, W14, W15, W16]
