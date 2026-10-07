# -*- coding: utf-8 -*-
# Woche 1–8 · Design fertig, Fabrik finden
import json, os
from r5_common import *

HERE = os.path.dirname(os.path.abspath(__file__))
LIVE = json.load(open(os.path.join(HERE, "..", "live_weeks_r41.json")))

# ---------- Woche 1 und 2: bleiben als Verlauf ----------
def alt(n):
    w = LIVE[n - 1]
    return dict(n=n, phase=w["phase"], goal=w["goal"],
                days=[[DONE(t[0], t[1]) for t in d] for d in w["days"]])

W1 = alt(1)
W2 = alt(2)
W2["days"][5] = [NOTE("ERLEDIGT 26.09.: Design v1.0 und v1.1 mit Claude gebaut, statt den Vektor selbst nachzubauen. Canvas „Fit-Mockup NVL-TT-01“")]
W2["days"][6] = [NOTE("ERLEDIGT 27.09.: Design v1.2 und v1.3 mit Claude. Band 28 mm, Alatyr auf die Passe, Serp schneidet in die Garbe, realistischer Lebensbaum ohne NL")]

# ---------- Posts Woche 5–9 (werden im Batch davor gedreht) ----------
PW = {}
PW[5] = {
 0: P("BUILD", "Papier, bevor es Garn wird",
      "Bevor ich 6.000 € ausgebe, klebe ich Papier auf meine Jeans.",
      "Zeitraffer vom Aufkleben (gefilmt beim Papiertest am 08.10.), einmal drehen vor dem Spiegel, Nahaufnahme Papierband an der Tasche. Letzte Einblendung: „100 Jeans. Ein Muster. 22.04.2027“", "20–25 Sek."),
 2: P("ORIGIN", "Älter als jede Grenze",
      "Dieses Muster ist älter als jede Grenze.",
      "Du sprichst 3 Sätze aus deiner Herkunftsgeschichte (aus Woche 2) als O-Ton. Dazu Bilder: Raute, Zickzack, Lebensbaum aus deinen Referenzen, am Ende die Papierteile an der Hose. Sprachregel: Subjekt ist das Muster, nicht das Volk", "30–45 Sek."),
 4: P("REAL", "Die Zahlen",
      "Mein Budget: 4.500 €. Mein Plan kostet 9.380 €.",
      "Zahlen von Hand auf Papier schreiben und filmen: 100 Jeans, 9.380 € Plan, 4.500 € Budget, Lücke 4.880 €. Dann ein Satz: „Die Lücke schließen Vorbestellungen ab Januar.“", "20–30 Sek."),
}
PW[6] = {
 0: P("BUILD", "Der Bauplan",
      "So sieht der Bauplan meiner Jeans aus.",
      "Bildschirmaufnahme: durch das Tech-Pack-PDF scrollen, bei der Maßtabelle und bei der Stickspezifikation kurz stoppen, Zoom auf Element A", "15–20 Sek."),
 2: P("ORIGIN", "Die Raute",
      "Diese Raute bedeutet überall dasselbe: ein bestelltes Feld.",
      "Papier-Münztasche in Nahaufnahme, dein Finger zeigt auf eine Raute. Dazu 2–3 Referenzbilder von Rauten aus deiner Sammlung (Quelle klein einblenden)", "25–30 Sek."),
 4: P("DETAIL", "Feiner Kreuzstich",
      "1 Kästchen = 1 Kreuzstich = 1,33 mm.",
      "Makro auf das ausgedruckte Elementblatt (Seite 4 der Design-PDF): langsamer Schwenk über das Band, dann ein Lineal daneben", "15 Sek."),
}
PW[7] = {
 0: P("BUILD", "8 Fabriken angeschrieben",
      "8 Fabriken angeschrieben. So viele können das überhaupt.",
      "Tracking-Tabelle am Bildschirm, Fabriknamen unkenntlich gemacht. Spalte „Panel-Stickerei“ zeigen. Am Ende die Zahl, wie viele übrig bleiben", "15–20 Sek."),
 2: P("ORIGIN", "Die Goldfäden",
      "Die Ähren sind gestickt. Die Fäden darunter setzt eine Hand.",
      "Papier-Gesäßtasche mit den Ähren, dazu eine echte Spule goldenes Polyestergarn (Kurzwarenladen, ca. 3 €). Du ziehst einen Faden durch die Finger", "20–25 Sek."),
 4: P("REAL", "Was eine Jeans kostet",
      "So viel kostet eine bestickte Jeans in der Fabrik wirklich.",
      "Zahlen aus den Angeboten von Hand aufschreiben: Basis-Jeans, Stickerei pro 1.000 Stiche, Sample. Keine Fabriknamen. Am Ende: „Und so viel kostet sie bei mir: 169 €. Hier ist warum.“", "30 Sek."),
}
PW[8] = {
 0: P("BUILD", "Die Fabrik steht",
      "Diese Fabrik macht meine 100 Jeans.",
      "Fotos oder Video, das dir die Fabrik schickt (vorher fragen, ob du es zeigen darfst): Stickmaschinen, Wäscherei. Dazu Land und Stadt. Name nur, wenn die Fabrik zustimmt", "15–20 Sek."),
 2: P("ORIGIN", "Der achtstrahlige Stern",
      "Acht Strahlen. Er sitzt hinten auf der rechten Tasche.",
      "Papier-Alatyr auf der Hose, dann der Ausdruck im Kreuzstich-Raster in Nahaufnahme. Ein Satz: Sonnenzeichen in den Textilien von Russland, Belarus, Ukraine und Polen. Keine Mythologie, nur Textil", "20–25 Sek."),
 4: P("REAL", "Ein einziges Teil",
      "Ich bezahle heute X € für eine einzige Jeans.",
      "Bildschirm der Überweisung (Betrag sichtbar, Kontodaten geschwärzt). Ein Satz, warum: Bevor 100 Stück entstehen, muss eine perfekt sein", "15–20 Sek."),
}
PW[9] = {
 0: P("BUILD", "Muster als Maschinen-Code",
      "So sieht mein Muster aus, wenn eine Maschine es lesen muss.",
      "Digitizing-Vorschau der Fabrik am Bildschirm, langsamer Zoom, Stichzahl einblenden", "15–20 Sek."),
 2: P("ORIGIN", "Der Lebensbaum",
      "Dieser Patch kommt auf 100 Jeans.",
      "Papier-Patch am Bund, Zoom auf Stamm, Knoten und Wurzeln. Ein Satz: Der Lebensbaum steht in vielen Kulturen für Herkunft und Wachstum. Nicht „slawisch“ nennen (Sprachregel)", "20–25 Sek."),
 4: P("DETAIL", "Zickzack",
      "Zickzack heißt Wasser. Es läuft um meine Tasche.",
      "Makro auf das Papierband, dein Finger fährt die Zickzackkante entlang", "15 Sek."),
}

# ---------- Woche 3 ----------
W3 = dict(n=3, phase="P0", goal="Design an der echten Hose testen und festlegen", days=[
 [],
 [NOTE("ERLEDIGT 29.09.: Design v1.4 mit Claude. Feiner Kreuzstich 1,33 mm statt 4-mm-Pixel, Goldfäden Variante 2 unter den Ähren"),
  NOTE("ERLEDIGT 29.09.: produkt-spec.md Rev. 10 mit allen Design-Entscheidungen (Claude)")],
 [],
 [T("B", "Druckvorlage 1:1 drucken und ausschneiden", 45, [
    "PDF „NVL_Druckvorlage_1zu1.pdf“ öffnen (im Chat vom 01.10.).",
    "Drucken: A4 Hochformat, Farbe, „Tatsächliche Größe“ bzw. „100 %“. Nicht „An Seite anpassen“.",
    "Kontrolllinie unten auf jeder Seite mit dem Lineal messen. Sind es nicht genau 100 mm: Einstellung korrigieren, neu drucken.",
    "Kein Drucker: PDF per Mail an einen Copyshop und ausdrücklich „100 %, nicht skalieren“ dazuschreiben.",
    "Ausschneiden entlang der gestrichelten Linien: Taschenband A, Münztasche E, Gesäßtasche mit B, Patch D, Alatyr C.",
   ], "Fünf Teile sind ausgeschnitten, die Kontrolllinie misst 100 mm."),
  NOTE("ERLEDIGT 01.10.: Papiertest 1 schon heute, einen Tag früher. Dein Urteil: Band schmaler, Münztasche größer, Tasche gut, Serp mit Garbe realistisch statt aufgeklebt, Goldfäden länger, Alatyr auf die andere Gesäßtasche. Claude hat daraus Design v1.5 gebaut: Canvas Version 12, Spec Rev. 11, Druckvorlage v1.5.")],
 [NOTE("ÜBERHOLT 07.10.: Statt Papiertest 2 hast du per Skizze entschieden: Serp und Garbe runter von der Tasche, drei Ähren auf einem einfach roten Band, dazu ein Serp im Stoppelfeld an der Seite. Claude hat daraus Design v1.7 gebaut. Papiertest 3 ist am Do 08.10.")],
 [NOTE("VERSCHOBEN: Die Entscheidungen triffst du am Do 08.10. zusammen mit Papiertest 3.")],
 [NOTE("VERSCHOBEN: Das Tech Pack bestellst du am Fr 09.10. direkt nach dem Freeze."),
  REVIEW(3)],
])

# ---------- Woche 4 ----------
W4 = dict(n=4, phase="P0", goal="Design-Freeze, Warteliste online, Tech Pack fertig", days=[
 [NOTE("VERSCHOBEN auf Fr 09.10.: Du hast am 07.10. noch einmal geändert, Design v1.7. Erst Papiertest 3 am Donnerstag, dann Freeze."),
  T("A", "Tracking-Tabelle anlegen", 15, [
    "Google Sheets: neue Tabelle „Time Travel Tracking“.",
    "Blätter anlegen: Warteliste (Datum, Zahl) · Content (Datum, Slot, Titel, Views TikTok, Views IG, Saves, Shares, neue Follower) · Fabriken (Name, Land, Website, E-Mail, gesendet, Antwort, Stickerei im Haus, Panel-Stickerei, MOQ, Preis Basis, Preis pro 1.000 Stiche, Sample-Preis, Zahlung, Lieferzeit, Notizen) · Sticker · Patches · Ausgaben (Datum, Posten, Betrag, Beleg) · Pre-Order (später).",
    "Link als Lesezeichen aufs Handy.",
   ], "Die Tabelle hat alle Blätter.")],
 [T("A", "Shopify-Shop anlegen", 60, [
    "shopify.com/de → kostenlos testen. Stand Oktober 2026: 3 Tage gratis, danach 1 € pro Monat für 3 Monate im Basic-Tarif, danach 27 € pro Monat (19 € bei Jahreszahlung).",
    "Shopname Novalife, Land Deutschland, Währung EUR, Zeitzone Berlin.",
    "Plan wählen: Basic zum 1-€-Angebot. Ohne gewählten Plan lässt sich der Passwortschutz später nicht abschalten.",
    "Theme: Dawn (Standard, kostenlos) behalten.",
    "Domain: Hast du schon eine, unter Einstellungen → Domains verbinden. Sonst dort kaufen (ca. 10–20 € pro Jahr).",
    "Einstellungen → Kundendatenschutz: „Double-Opt-in für Marketing“ einschalten. Für Newsletter in Deutschland Pflicht.",
   ], "Shop existiert, Domain ist verbunden, Double-Opt-in ist an.")],
 [T("A", "Impressum und Datenschutzerklärung", 75, [
    "Impressum-Generator auf e-recht24.de (kostenlos): Name, ladungsfähige Adresse (kein Postfach), E-Mail, Telefon. USt-IdNr, falls du eine hast.",
    "Datenschutz-Generator auf e-recht24.de: Shopify als Shop-System, Newsletter mit Double-Opt-in, Cookies, Links zu Instagram und TikTok auswählen.",
    "Shopify: Onlineshop → Seiten → „Impressum“ und „Datenschutz“ anlegen, Texte einfügen.",
    "Onlineshop → Navigation → Footer-Menü: beide Seiten verlinken.",
    "AGB und Widerrufsbelehrung brauchst du erst ab dem Verkauf im Januar. Die kommen in Woche 11.",
   ], "Impressum und Datenschutz sind online und im Footer verlinkt.")],
 [T("A", "Startseite als Warteliste bauen", 60, [
    "Text mit dem Prompt unten bei Claude holen.",
    "Onlineshop → Themes → Dawn → Anpassen → Startseite: alle Demo-Abschnitte löschen.",
    "Drei Abschnitte: 1 Bild-Banner (Foto vom Papiertest), 2 Rich-Text mit Claudes Text, 3 „E-Mail-Anmeldung“.",
    "Onlineshop → Einstellungen → Passwortschutz ausschalten. Es sind keine Produkte sichtbar, also kann noch niemand kaufen.",
    "Test mit einer zweiten E-Mail-Adresse: anmelden, Bestätigungsmail kommt, bestätigen. Dann muss die Adresse unter Kunden mit „E-Mail-Marketing: abonniert“ stehen.",
   ], "Deine Testadresse steht in Shopify als abonniert.",
   "Schreib mir den Text für meine Wartelisten-Startseite in Shopify: Überschrift (max. 6 Wörter), zwei kurze Absätze, Button-Text. Fakten: Novalife Time Travel, 100 bestickte Jeans, ein Muster aus der slawischen Textiltradition, Drop 22.04.2027 um 19:00, Vorbestellung ab Januar zu 149 € statt 169 €, wer auf der Liste ist, kauft zuerst. Sprachregel: Subjekt ist das Muster, nicht das Volk."),
  T("B", "Papiertest 3 mit Design v1.7 und vier Entscheidungen", 45, [
    "PDF „NVL_Druckvorlage_v17.pdf“ öffnen (im Chat vom 07.10., die neuere). Zwei Seiten.",
    "Drucken: A4 Hochformat, Farbe, „Tatsächliche Größe“ bzw. „100 %“. Kontrolllinie messen, genau 100 mm.",
    "Ausschneiden: Seite 1 die linke Gesäßtasche, Seite 2 den Zettel mit dem Serp.",
    "Goldfäden echt machen: 9 Stücke gelbes Garn, 2–3 cm, unterschiedlich lang, direkt unter das rote Band kleben.",
    "Handy aufs Regal und das Aufkleben im Zeitraffer filmen. Das ist dein erster Post am 12.10.",
    "Hinten: Tasche auf die linke Gesäßtasche, Oberkante an Oberkante. Alatyr C auf die rechte Tasche, auf Höhe des roten Bands. Patch D wie gehabt.",
    "Seite: Hose flach hinlegen, Vorderseite oben. Den Serp-Zettel auf das linke Bein, die goldene Zettelkante genau auf die Seitennaht. Höhe 40–50 cm unter der Bundoberkante, am Körper ausprobieren.",
    "Vorn: Band A und Münztasche E aus der Druckvorlage v1.5, falls sie noch nicht dran sind.",
    "Münztasche deiner Eightyfive messen: Breite oben und Höhe bis dahin, wo sie unter der Vordertasche verschwindet.",
    "Anziehen. Aus 3 m und 1 m je ein Foto von vorn, hinten und seitlich, dazu ein Foto von der Seite aus 30 cm. Alles mit dem Prompt unten an Claude.",
   ], "Claude hat 7 Fotos, die zwei Maße der Münztasche und deine vier Antworten.",
   "Papiertest 3 mit Design v1.7. Hier sind 7 Fotos. Münztasche meiner Eightyfive: Breite … mm, Höhe … mm. Meine Entscheidungen: Serp an der Seite auf … cm unter dem Bund. Patch D 86 × 76 mm: so lassen / kleiner. Taschenklappe: nein / ja. Nackenlabel für Zipper und Polo als gewebtes Etikett: okay / anders. Beurteile die Fotos und sag mir, ob das Design so in den Freeze kann.")],
 [T("D", "Design-Freeze abnehmen und Tech Pack bestellen", 25, [
    "Canvas „Fit-Mockup NVL-TT-01“ öffnen und die Freeze-Version ansehen. Sind deine Antworten von gestern drin?",
    "Wenn ja, schreib Claude „Freeze“. Ab jetzt ändert sich am Design nur noch etwas, wenn die Fabrik oder die Stickprobe einen Grund liefern.",
    "Wenn nein: die Änderung einmal klar benennen, Claude korrigiert, dann Freeze. Nicht weiter schieben, am Montag gehen die Anfragen raus.",
    "Direkt danach den Prompt unten an Claude schicken. Das Tech Pack prüfst du am Sonntag.",
   ], "Du hast „Freeze“ geschrieben und das Tech Pack bestellt.",
   "Bau mir das Tech Pack v1.0 für NVL-TT-01 als PDF auf Englisch, aus produkt-spec.md und der Freeze-Version des Designs: 1 Deckblatt, 2 Flachzeichnungen vorn und hinten mit Maßen, 3 Maßtabelle W30–W38 mit Toleranzen, 4 BOM, 5 Stoff- und Waschspezifikation, 6 Stickspezifikation pro Element A–E mit Platzierung ab Naht, 7 Konstruktion, 8 Labels und Verpackung, 9 Prüfplan. Version 1.0, Datum heute.")],
 [T("C", "Profile vorbereiten", 20, [
    "Instagram und TikTok: Bio prüfen: „Time Travel — 100 bestickte Jeans. Drop 22.04.2027“.",
    "Link in beiden Bios: deine Shopify-Startseite.",
    "Instagram: Highlight „TIME TRAVEL“ anlegen.",
    "Alte Bleach-Posts bleiben stehen. Die neue Serie bekommt ab Montag die drei angehefteten Plätze.",
   ], "Der Link in beiden Bios führt zur Warteliste."),
  BATCH(list(PW[5].values()), 5)],
 [T("B", "Fabrikliste: Claude recherchiert 8 Fabriken", 30, [
    "Prompt unten an Claude.",
    "Liste prüfen: Hat jede Fabrik eine echte Website und eine E-Mail von dieser Website? Keine Adressen aus Verzeichnissen ohne Quelle.",
    "Die 8 Fabriken ins Blatt „Fabriken“ der Tracking-Tabelle.",
    "Warum 8, wenn du bei einer bestellst: Erfahrungsgemäß antwortet die Hälfte, und nur 2–3 können Stickerei auf dem Zuschnitt im eigenen Haus. Übrig bleibt eine.",
   ], "8 Fabriken mit geprüfter E-Mail stehen in der Tabelle.",
   "Recherchiere 8 Jeansfabriken in der Türkei und in Portugal für 100 Jeans mit Panel-Stickerei (Stickerei auf dem Zuschnitt vor dem Nähen, im eigenen Haus) und eigener Wäscherei. Startpunkte: Istanbul Clothing Manufacturers, Portugal Textile (Jeans Factory), Brosan Textile, White Cotton. Für jede: Website, offizielle E-Mail von der Website, Stadt, Hinweise auf Stickerei im Haus, MOQ falls öffentlich. Nur Angaben mit Quelle, nichts aus Scraper-Verzeichnissen."),
  REVIEW(4),
  T("B", "Tech Pack v1 prüfen und freigeben", 60, [
    "Claudes Tech-Pack-PDF öffnen.",
    "Seite für Seite gegen diese Liste: Stilnummer NVL-TT-01? Maße W30–W38 vollständig mit Toleranz? Alle Elemente A–E und B2 mit Maß und Position ab Naht? Garn Polyester? Reihenfolge sticken → nähen → waschen? Goldfäden nach der Wäsche von Hand?",
    "Was dir unklar ist, als Frage an Claude, nicht als Änderung.",
    "Wenn alles stimmt: „Tech Pack v1 freigegeben“ an Claude. Morgen geht es mit der Anfrage an die Fabriken raus.",
   ], "Tech Pack v1.0 ist freigegeben und liegt als PDF bei dir.")],
])

# ---------- Woche 5 ----------
W5 = dict(n=5, phase="P1", goal="Anfragen an die Fabriken raus, der erste Post geht online", days=[
 [T("B", "Anfrage (RFQ) an 8 Fabriken senden", 60, [
    "Vorlage „RFQ Jeansfabrik“ kopieren (Referenz → Vorlagen).",
    "Pro Fabrik eine eigene Mail, nie alle in CC. Erste Zeile mit dem Namen der Fabrik.",
    "Anhänge: Tech Pack v1.0 (PDF) und das Elementblatt 1:1.",
    "Absender: deine Novalife-Adresse. Signatur: Name, Novalife, Berlin, Website.",
    "Im Blatt „Fabriken“ das Datum unter „gesendet“ eintragen.",
   ], "8 Mails sind raus, das Datum steht in der Tabelle."),
  PW[5][0]],
 [T("A", "Steuerstatus klären: Kleinunternehmer ja oder nein", 30, [
    "Umsatz 2025 nachsehen. Kleinunternehmer heißt: 2025 höchstens 25.000 € und 2026 voraussichtlich höchstens 100.000 €.",
    "Was daran hängt: Als Kleinunternehmer weist du keine Mehrwertsteuer aus, kannst aber auch keine Vorsteuer abziehen. Ware aus der Türkei kostet bei der Einfuhr 19 % Einfuhrumsatzsteuer. Für dich wäre das echter Aufwand, bei ~6.000 € Ware rund 1.150 €.",
    "30 Minuten mit einem Steuerberater (Erstgespräch) oder der IHK-Gründungsberatung klären: Lohnt der Verzicht auf die Kleinunternehmerregelung? Ist Portugal steuerlich dann günstiger? Ich bin kein Steuerberater.",
    "Ergebnis Claude schreiben, damit es in den Fabrikvergleich eingeht.",
   ], "Du weißt: Kleinunternehmer ja oder nein, und was Türkei gegen Portugal steuerlich kostet.")],
 [T("B", "Berliner Sticker anfragen (Zipper und Polo)", 45, [
    "Google Maps: „Stickerei Berlin“ und „Textilveredelung Berlin“. 3 Betriebe mit Website und guten Bewertungen auswählen.",
    "Vorlage „Anfrage Berliner Sticker“ (Referenz → Vorlagen) an alle drei.",
    "Die zwei entscheidenden Fragen stehen drin: Fleece 330–350 g/m² mit Topping? Piqué?",
    "Ins Blatt „Sticker“ eintragen.",
   ], "3 Anfragen sind raus."),
  PW[5][2]],
 [T("B", "Teppich-Fotos und Familienbilder", 45, [
    "Familie fragen: Gibt es den Wandteppich noch? Fotos davon? Alte Stickereien?",
    "Wenn ja: bei Tageslicht gerade von vorn fotografieren, ganz und in Ausschnitten (Medaillon in der Mitte, Rahmen, Ecken).",
    "Fotos an Claude: Daraus entsteht das Medaillon für den Zipper-Rücken.",
    "Gibt es ihn nicht mehr: Fotos ähnlicher Teppiche aus deinem Umfeld. Sonst baut Claude das Medaillon aus den Motiven der Grammatik.",
   ], "Die Fotos sind bei Claude, oder du weißt sicher, dass es keine gibt.")],
 [T("B", "Fabriken nachfassen", 20, [
    "Wer bis heute nicht geantwortet hat: Vorlage „Nachfassen“ als Antwort auf deine erste Mail (gleicher Mailverlauf).",
    "Alle Antworten ins Blatt „Fabriken“.",
   ], "Jede Fabrik ohne Antwort hat eine zweite Mail."),
  PW[5][4]],
 [T("A", "Puffer", 30, [
    "Was diese Woche liegen geblieben ist, jetzt erledigen.",
    "Kommentare und DMs der drei Posts beantworten.",
   ], "Aus Woche 5 ist nichts mehr offen.")],
 [REVIEW(5), BATCH(list(PW[6].values()), 6)],
])

# ---------- Woche 6 ----------
W6 = dict(n=6, phase="P1", goal="Angebote vergleichen und mit den besten drei sprechen", days=[
 [T("B", "Angebote in den Vergleich", 45, [
    "Alle Antworten (Mails, PDFs) mit dem Prompt unten an Claude.",
    "Claude baut die Vergleichstabelle und markiert Ausschlüsse.",
    "Sofort raus: Wer keine Stickerei im eigenen Haus hat oder nicht auf dem Zuschnitt stickt.",
   ], "Die Vergleichstabelle steht, die Top 3 sind markiert.",
   "Hier sind die Antworten der Fabriken auf meine RFQ: … Bau die Vergleichstabelle mit den 14 Fragen als Spalten, markiere Ausschlüsse (keine Panel-Stickerei im eigenen Haus) und gib mir die Top 3 mit Begründung. Berücksichtige meinen Steuerstatus: …"),
  PW[6][0]],
 [T("B", "Calls mit den Top 3 anfragen", 20, [
    "Vorlage „Call anfragen“ an die Top 3.",
    "30 Minuten per Video (WhatsApp, Zoom oder Google Meet), Mittwoch bis Freitag.",
    "In derselben Mail: 2 Referenzmarken mit Stickerei und Fotos einer früheren Panel-Stickerei.",
   ], "3 Termine stehen im Kalender."),
  T("D", "Farbe für Zipper und Polo festlegen", 10, [
    "Empfehlung: Navy. Dieselbe Logik wie das Indigo der Jeans: Weiß und Rot brauchen einen dunklen Grund.",
    "Alternative: Schwarz.",
    "Entscheidung ins Blatt „Sticker“.",
   ], "Die Farbe steht fest."),
  T("B", "Bänder und Medaillon bei Claude bestellen", 5, [
    "Prompt unten an Claude.",
   ], "Der Prompt ist abgeschickt.",
   "Zeichne die Bänder für den Zipper (2 × 25 mm × ca. 25 cm, gespiegelt an der Zip-Leiste) und den Polo (2 × 20 mm × ca. 12 cm an der Knopfleiste) im selben 1,33-mm-Kreuzstichraster wie Band A, dazu das Teppich-Medaillon für den Zipper-Rücken aus meinen Teppich-Fotos. Liefere SVG und ein Druckblatt 1:1.")],
 [T("B", "Call 1", 45, [
    "Leitfaden öffnen (Referenz → Vorlagen → Call-Leitfaden) und ausdrucken.",
    "Im Call: Stickmaschinen und Wäscherei per Kamera zeigen lassen.",
    "Die Frage nach der Einzug-Kompensation stellen. Wer sie nicht versteht, ist raus.",
    "Notizen direkt nach dem Call ins Blatt „Fabriken“.",
   ], "Notizen von Call 1 stehen in der Tabelle."),
  PW[6][2]],
 [T("B", "Call 2", 45, [
    "Gleicher Leitfaden, gleiche Reihenfolge, damit du vergleichen kannst.",
    "Notizen direkt danach in die Tabelle.",
   ], "Notizen von Call 2 stehen in der Tabelle."),
  T("B", "Blanks bestellen: 1 Zipper, 1 Polo", 20, [
    "Zip-Hoodie 330–350 g/m² und Piqué-Polo in deiner Größe, in der Farbe von Dienstag.",
    "Anbieter: AS Colour (Europa-Onlineshop) oder Stanley/Stella über einen Händler. Auf Grammatur und Material achten.",
    "Je 1 Stück. Beide gehen später als Musterteil zum Berliner Sticker.",
   ], "Bestellung ist bestätigt.")],
 [T("B", "Call 3", 45, [
    "Gleicher Leitfaden.",
    "Notizen direkt danach in die Tabelle.",
   ], "Notizen von Call 3 stehen in der Tabelle."),
  PW[6][4]],
 [T("B", "Referenzen der Top 3 prüfen", 30, [
    "Je 2 Marken pro Fabrik: Vorlage „Referenz-Check“ als DM oder Mail.",
    "Antworten ins Blatt „Fabriken“, Spalte Notizen.",
   ], "6 Nachrichten sind raus.")],
 [REVIEW(6), BATCH(list(PW[7].values()), 7)],
])

# ---------- Woche 7 ----------
W7 = dict(n=7, phase="P1", goal="Eine Fabrik wählen, Sample verhandeln, Zahlen prüfen", days=[
 [T("D", "Fabrik entscheiden", 45, [
    "Call-Notizen und Antworten der Referenzen mit dem Prompt unten an Claude.",
    "Claude macht die Scorecard. Pflicht: Panel-Stickerei im eigenen Haus, nachgewiesen mit Fotos einer früheren Produktion.",
    "Du entscheidest dich für eine Fabrik. Nummer 2 bleibt als Reserve, ihr wird nicht abgesagt.",
   ], "Eine Fabrik ist gewählt, Nummer 2 ist notiert.",
   "Hier sind meine Call-Notizen und die Antworten der Referenzen: … Mach mir eine Scorecard für die Top 3 (Panel-Stickerei nachgewiesen, Preis gesamt bei 100 Stück inklusive Stickerei, Sample-Zeit, Zahlung, Kommunikation, Steuer und Zoll nach meinem Status) und sag mir ehrlich, welche du nehmen würdest."),
  PW[7][0]],
 [T("B", "Konditionen verhandeln, Proforma anfordern", 30, [
    "Vorlage „Verhandlung“ an die gewählte Fabrik.",
    "Kernpunkte: 50/50 statt 60/40, Entwicklungskosten werden bei der Bestellung verrechnet, Digitizing inklusive, Termine schriftlich, DDP-Preis bis Berlin.",
    "Proforma-Rechnung für die Entwicklung anfordern: Digitizing, gewaschene Stickproben, Proto W32 komplett bestickt und gewaschen, Expressversand.",
   ], "Die Mail ist raus."),
  T("B", "Absagen an die anderen", 15, [
    "Vorlage „Absage“ an alle Fabriken außer Nummer 1 und 2.",
   ], "Jede Fabrik hat eine Antwort.")],
 [T("B", "Patch-Hersteller anfragen", 45, [
    "Zwei Patches: D Lebensbaum 86 × 76 mm (Stickpatch auf Naturleinen, viele Farbtöne, feine Linien) und Chenille-Patch 200 × 150 mm für den Zipper-Rücken.",
    "Suchen: „custom embroidered patches low minimum Europe“, „Aufnäher sticken lassen Kleinauflage“, „custom chenille patches“. Nur Anbieter mit Fotos von fein gestickten Patches.",
    "Vorlage „Patch-Anfrage“ an 3 Anbieter. Anhänge: Elementblatt mit D und der Medaillon-Entwurf.",
    "Ins Blatt „Patches“.",
   ], "3 Anfragen sind raus."),
  PW[7][2]],
 [T("B", "Berliner Sticker auswählen", 30, [
    "Antworten im Blatt „Sticker“ ansehen. Wer kann Fleece mit Topping UND Piqué?",
    "Die 2 besten auswählen. Ihnen Claudes Band-Dateien schicken und je ein Musterteil anfragen (Budget 180 € für beide).",
    "Die Blanks bringst du, sobald sie da sind.",
   ], "2 Sticker sind ausgewählt und haben die Dateien.")],
 [T("A", "EORI-Nummer beantragen", 30, [
    "Nur nötig, wenn deine Fabrik in der Türkei sitzt. Ohne EORI kann ein Gewerbe keine Ware einführen.",
    "zoll.de → EORI-Nummer beantragen (online, kostenlos). Dauer meist 1–2 Wochen.",
    "Nummer ins Blatt „Ausgaben“ oben als Notiz, du brauchst sie für Sample und Lieferung.",
   ], "Der Antrag ist gestellt."),
  PW[7][4]],
 [T("A", "Zahlen für die Validierung sammeln", 30, [
    "Warteliste seit 12.10.: Shopify → Kunden → „E-Mail-Marketing: abonniert“.",
    "Pro Post: Views, Saves, Shares, neue Follower auf TikTok und Instagram.",
    "Alles ins Blatt „Content“.",
   ], "Alle Zahlen stehen in der Tabelle.")],
 [T("D", "VALIDIERUNG: weiter, anpassen oder bremsen", 30, [
    "Grün: 150 oder mehr Anmeldungen seit 12.10. → Montag das Sample bezahlen.",
    "Gelb: 50 bis 149 → Sample bezahlen, aber den Content mit Claude überarbeiten (Prompt unten).",
    "Rot: unter 50 → Sample-Zahlung eine Woche schieben. Mit Claude die 9 Posts analysieren, 6 neue nach neuem Muster drehen, in 7 Tagen neu entscheiden.",
    "Das ist der letzte Punkt, an dem Anhalten fast nichts kostet. Ab Montag fließt Geld.",
   ], "Die Ampel steht fest und ist in der Tabelle notiert.",
   "Hier sind meine Zahlen der ersten 3 Content-Wochen: … Analysiere, welche Hooks funktioniert haben und welche nicht, und schlag mir 6 bessere Posts für die nächsten 2 Wochen vor."),
  REVIEW(7), BATCH(list(PW[8].values()), 8)],
])

# ---------- Woche 8 ----------
W8 = dict(n=8, phase="P1", goal="Sample beauftragen und alle Dateien an die Fabrik", days=[
 [T("B", "Proforma prüfen und Entwicklung bezahlen", 30, [
    "Nur bei Ampel grün oder gelb.",
    "Proforma prüfen: Digitizing, gewaschene Stickproben, Proto W32 komplett, Expressversand. Summe gegen den Plan (Digitizing 320 €, Stickproben 150 €, Proto 180 €).",
    "Per Banküberweisung zahlen, Verwendungszweck mit der Proforma-Nummer.",
    "Beleg ins Blatt „Ausgaben“.",
   ], "Bezahlt, der Beleg ist gespeichert."),
  PW[8][0]],
 [T("B", "Dateien an die Fabrik", 45, [
    "Tech Pack v1.1 bei Claude holen (Prompt unten), mit allen Antworten aus den Calls.",
    "Paket an die Fabrik: Tech Pack v1.1, Elementblatt 1:1, SVG-Dateien A–E, Druckvorlage.",
    "Dazuschreiben: Proto in W32. Garnfarben werden an den Stickproben entschieden. Bitte jedes Element in den vorgeschlagenen Farben sticken und die Garnnummern nennen.",
    "Termine schriftlich bestätigen lassen: Digitizing-Vorschau bis …, Fotos der Stickproben bis …, Versand Proto bis …",
   ], "Die Fabrik hat die Dateien bestätigt und Termine genannt.",
   "Mach mir aus Tech Pack v1.0 die v1.1 mit diesen Antworten aus den Fabrik-Calls: … Exportiere dazu die Elemente A–E als SVG in Originalgröße.")],
 [T("A", "Labels und Hangtag bei Claude bestellen", 15, [
    "Prompt unten an Claude.",
   ], "Der Prompt ist abgeschickt.",
   "Entwirf für NVL-TT-01: gewebtes Hauptlabel (Bund innen hinten), Größenlabel, EU-Pflegeetikett (100 % Baumwolle; 30 °C, auf links, nicht in den Trockner, Fäden nicht abschneiden; Herkunftsland), Hangtag mit Stücknummer 001–100 und Nackenlabel für Zipper und Polo. Liefere Druckdateien mit Maßen."),
  PW[8][2]],
 [T("A", "Labels freigeben und an die Fabrik", 30, [
    "Claudes Entwürfe prüfen: Materialangabe und Pflegesymbole richtig? Stücknummer auf dem Hangtag?",
    "An die Fabrik: Hauptlabel, Größenlabel, Pflegeetikett. Fragen: Macht ihr die Labels selbst, und zu welchem Preis? Gravierter Knopf „NOVALIFE“ 17 mm Antik-Messing: MOQ und Preis?",
    "Die Hangtags druckst du selbst in Woche 22.",
   ], "Die Fabrik hat die Label-Dateien.")],
 [T("B", "Patch-Angebote eintragen", 20, [
    "Antworten der 3 Patch-Anbieter ins Blatt „Patches“: Preis bei 50 / 100 / 200, Musterkosten, Lieferzeit, Mindestlinienbreite.",
    "Wer keine feinen Arbeiten zeigen kann, fliegt raus.",
   ], "Die Angebote stehen in der Tabelle."),
  PW[8][4]],
 [T("A", "Puffer", 30, [
    "Liegengebliebenes erledigen.",
    "Kommentare und DMs beantworten.",
   ], "Aus Woche 8 ist nichts mehr offen.")],
 [REVIEW(8), BATCH(list(PW[9].values()), 9)],
])

WEEKS_A = [W1, W2, W3, W4, W5, W6, W7, W8]
