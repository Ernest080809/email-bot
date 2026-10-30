# -*- coding: utf-8 -*-
"""Docket Rev. 8 (30.10.2026): kompletter Neuplan nach Ernests Vorgaben.
Reihenfolge: erst Design und Fabrik bis zur Muster-Freigabe, dann Gewerbe, Recht und Shop parallel zum Marketing.
Öffentlich ab dem ersten Proto (Di 15.12.), Vorbestellung ab Mo 15.02., Abi-Pause 22.03.–09.05., Drop Do 24.06.2027 19:00.
Zeit: 3–5 Stunden pro Woche bis zum Abi (Ernests Angabe vom 30.10.)."""
from lib8 import Plan, LINKS
import content8, mails8

P = Plan()
A = P.add


def review(iso, n, extra=()):
    A(iso, 'A', f"Wochenreview W{n}", 15, id=f"r8-review-w{n}", tm="20:00", s=[
        "Abschnitt „Zahlen“: Follower (TikTok + Instagram zusammen), Warteliste (bestätigte Adressen in Shopify) und bezahlte Vorbestellungen eintragen.",
        "Was diese Woche liegen geblieben ist: nicht nachholen, sondern Claude kurz schreiben, dann schiebt er es in eine freie Woche.",
        *extra], f="die drei Zahlen eingetragen sind.")


# =====================================================================================
# Phase F · Fabrik und Design fertig (Fr 30.10. – So 13.12.)
# =====================================================================================
A('2026-10-30', 'B', "Maßblätter v1.1 und Farbcodes an Nargiza schicken", 20, id="r8-masse-senden", s=[
    "Maßblätter öffnen (Link unten) und Seite 1–4 kurz durchsehen: stimmen Bundweite 43, Innenbein 81 und die Größen W30–W38?",
    "Claude schreibt die Antwort an Nargiza im bestehenden Verlauf, mit zwei Anhängen: Maßblätter v1.1 und Farbcodes (PDF).",
    "Inhalt der Mail: neue Maßblätter in ihrem Format, alle Farbcodes, der Patch D wird jetzt auch von ihnen gestickt, Bitte um ihre Größenvorlage.",
    "Du sagst „senden“. Vorher geht nichts raus."], f="die Mail mit beiden PDFs raus ist.", o=['masse', 'farben', 'gmail'])
A('2026-10-30', 'B', "LOGIC und DiZNEW: Stand prüfen", 10, id="r8-andere-fabriken", s=[
    "Claude prüft Gmail: Hat LOGIC bis heute geantwortet? Hat DiZNEW einen Preis geschickt?",
    "Nichts absagen, bevor die Fabrik am Do 05.11. entschieden ist."], f="du weißt, ob es ein zweites Angebot gibt.", o=['gmail'])
A('2026-10-31', 'D', "Zwei Fragen an Claude beantworten: Alter und Berlin", 5, id="r8-fragen-alter", s=[
    "Bist du 18 oder älter? Unter 18 brauchst du für das Gewerbe die Zustimmung der Eltern und des Familiengerichts. Das dauert Wochen und muss dann schon im November starten.",
    "Ab wann bist du wieder in Berlin? Der Zipper-Papiertest am Sa 07.11. braucht deinen RL-Zipper."], f="Claude beide Antworten hat.")
review('2026-11-01', 1, ["Startwert Follower ist 170 (schon eingetragen). Warteliste: 0."])

# ---- W2 · 02.–08.11. ----
A('2026-11-02', 'B', "Kuzgunlar: schriftliches Angebot anfordern", 20, id="r8-angebot", s=[
    "Claude schreibt die Mail an Nargiza, du sagst „senden“.",
    "Gefragt wird: Preis pro Paar bei 50, 75 und 100 Stück, alles inklusive (Stoff, 4 Stickereien, Patch D, Wäsche, Knopf, Nieten, Druckknöpfe, Etikett, Goldfäden von Hand).",
    "Dazu: Mindestmenge, Musterkosten (Proto und PP), Preis für 2 zusätzliche Marketing-Paare, Werkzeugkosten Knopf, Lieferzeit Muster und Serie, Zahlung 50/50.",
    "Und der Versand: eine Sendung nach Berlin (DAP) und alternativ jedes Paar einzeln an Kunden in der EU (Preis pro Paket, wer verzollt).",
    "In der Türkei war am 29.10. Feiertag. Antwort bis Mi 04.11. ist realistisch."], f="die Anfrage raus ist.", o=['gmail', 'callbogen'])
A('2026-11-05', 'D', "Fabrik entscheiden", 30, id="r8-fabrik-wahl", s=[
    "Claude legt dir den Vergleich hin: Preis pro Paar, Muster, Stickerei im Haus, Wäsche im Haus, Eindruck aus dem Call (4,2 von 5).",
    "Ampel Preis pro Paar bei 100 Stück: bis 60 € grün, bis 63 € gelb, darüber rot.",
    "Ohne schriftlichen Preis keine Entscheidung: dann neuer Termin Mo 09.11.",
    "Danach schreibt Claude die Zusage an Kuzgunlar und kurze, freundliche Absagen an die anderen. Du sagst „senden“."],
  f="die Fabrik feststeht und die Zusage raus ist.", o=['callbogen', 'gmail'])
A('2026-11-06', 'A', "Proforma prüfen und Muster anzahlen", 20, id="r8-muster-zahlen", s=[
    "Erst wenn die Proforma von Kuzgunlar da ist. Claude prüft sie gegen das Angebot: Betrag, Leistungen, Bankdaten.",
    "Bankdaten nur aus der Proforma, nie aus einer späteren Mail mit „neuer Bankverbindung“. Im Zweifel bei Nargiza per WhatsApp nachfragen.",
    "Überweisen (Wise oder Bank), Beleg als PDF in den Ordner „TT Belege“."], f="die Anzahlung überwiesen ist und der Beleg abgelegt ist.")
A('2026-11-07', 'G', "Zipper-Papiertest und RL-Kapuze abpausen", 60, id="r8-zipper-papier", s=[
    "Nur wenn du in Berlin bist. Sonst verschiebt Claude auf das nächste Wochenende in Berlin.",
    "PDF „Papiertest Zipper“ in 100 % drucken, Teppich in S, M und L ausschneiden, mit Malerkrepp auf deinen RL-Zipper.",
    "Vor dem Spiegel fotografieren: vorn, seitlich, mit offenem Reißverschluss. Clip mit einer Drehung für V201 filmen.",
    "Kapuze flach legen und den Umriss auf Papier abpausen (Rückendruck). Foto von oben mit Lineal daneben.",
    "Alle Fotos an Claude."], f="Claude die Fotos von Teppich und Kapuze hat.", o=['zipper_pt', 'zipper_v2'])
review('2026-11-08', 2)

# ---- W3 · 09.–15.11. ----
A('2026-11-09', 'B', "Unterlagen an Kuzgunlar: Startschuss fürs Muster", 20, id="r8-unterlagen", s=[
    "Claude stellt das Paket zusammen: Tech Pack v1.0, Maßblätter v1.1, Farbcodes, Artwork 1:1, Patch D als Stickerei in ihrem Auftrag.",
    "Gebeten wird um: Digitizing-Vorschau aller 5 Motive mit Stichzahl, Fotos der Garne neben den Pantone-Farben bei Tageslicht, gewaschene Stickprobe vor dem Proto.",
    "Du sagst „senden“."], f="das Paket raus ist und Nargiza den Eingang bestätigt hat.", o=['techpack', 'masse', 'farben', 'artwork'])
A('2026-11-11', 'G', "Innenetikett und Hangtag wählen", 30, id="r8-etikett-hangtag", s=[
    "Claude zeigt dir je zwei Entwürfe: Innenetikett (Nummer, Größe, Pflege, „Goldfäden nicht abschneiden“) und Hangtag mit Bedeutungskarte.",
    "Du wählst je einen, Claude macht die Druckdatei für Kuzgunlar.",
    "Weniger ist hier mehr: Das Etikett druckt die Fabrik, der Hangtag kommt in Phase 2 dazu."], f="beide Entwürfe gewählt sind.")
A('2026-11-13', 'D', "Versandweg entscheiden", 30, id="r8-versandweg", s=[
    "Claude legt dir zwei Wege nebeneinander: A · Kuzgunlar schickt jedes Paar direkt an den Kunden. B · Eine Sendung nach Berlin, du oder ein Fulfillment-Dienst verschickt.",
    "Was zählt: Zoll und Einfuhrumsatzsteuer pro Paket (ab 150 € Warenwert auch Zoll), wer sie zahlt, Lieferzeit, Retouren, Kosten pro Paket, Zeitaufwand für dich im Juni.",
    "Mein Rat kommt mit dem Vergleich. Für deine 3–5 Stunden pro Woche ist wichtig, dass du im Juni nicht 100 Pakete selbst packst.",
    "Die Entscheidung geht als Bedingung an Kuzgunlar."], f="der Versandweg feststeht und Kuzgunlar Bescheid weiß.", o=['gmail'])
A('2026-11-14', 'G', "Zipper: offene Punkte entscheiden", 30, id="r8-zipper-punkte", s=[
    "Teppichgröße S, M oder L aus dem Papiertest.",
    "Kordeln über dem Teppich: ja oder nein.",
    "Reißverschluss: Antik-Kupfer wie alle anderen Metallteile (mein Rat) oder dunkel.",
    "Rückendruck aus der abgepausten Kapuze: Claude zeigt dir die fertige Fassung, du gibst frei."], f="alle vier Punkte entschieden sind.", o=['zipper_v2'])
review('2026-11-15', 3)

# ---- W4 · 16.–22.11. ----
A('2026-11-16', 'B', "Digitizing-Vorschau und Garnfotos prüfen", 30, id="r8-digitizing", s=[
    "Sobald Kuzgunlar sie schickt. Claude prüft Stichzahl (Ziel unter 30.000 für alle Motive), Farbwechsel, Fadenschnitte und Größen.",
    "Du schaust nur auf die Garnfotos bei Tageslicht: Ist das Rot ein Knallrot? Ist das Weiß warm? Ist das Gold nicht metallisch?",
    "Freigabe schriftlich per Mail, Garnnummern ins Blatt „Fabrik“."], f="Digitizing und Garne schriftlich freigegeben sind.", o=['farben', 'gmail'])
A('2026-11-18', 'D', "Zipper und Polo: in diesem Drop oder im nächsten?", 20, id="r8-zipper-polo", s=[
    "Mein Rat: Polo kommt in den nächsten Drop. Deine 3–5 Stunden pro Woche reichen nicht für drei Produkte.",
    "Zipper nur, wenn Kuzgunlar ihn zu einem guten Preis macht und das Muster mit dem PP der Jeans kommt. Sonst auch nächster Drop.",
    "Entscheidung ins Blatt „Entscheidungen“. Bei Zipper „ja“ baut Claude bis Do 19.11. das Tech Pack."], f="für Zipper und Polo ein klares Ja oder Später steht.")
A('2026-11-19', 'G', "Zipper Tech Pack durchgehen und senden", 45, id="r8-zipper-techpack", s=[
    "Nur bei Zipper „ja“. Claude baut es nach dem Muster der Jeans: Maße S–XL, Teppich, Rückendruck, Stern C, Kordeln, Reißverschluss, Etiketten.",
    "Du gehst es Seite für Seite durch und markierst, was nicht stimmt.",
    "Danach Anfrage an Kuzgunlar: Preis, Muster mit dem PP der Jeans. Du sagst „senden“."], f="das Zipper Tech Pack bei Kuzgunlar ist oder der Zipper auf „später“ steht.", o=['zipper_v2', 'messbogen_z'])
A('2026-11-21', 'S', "Stunt-Drehs organisieren: Vater, Gelände, Freunde", 30, id="r8-stunt-orga", s=[
    "G-Klasse für REWIND #01: Dein Vater sagt zu für Mo 21.12. (Ausweich Di 22.12.).",
    "Gelände: privat, abgesperrt, 30 m gerade, mit Erlaubnis des Eigentümers. Keine öffentliche Straße. Eigentümer schriftlich (WhatsApp reicht) fragen.",
    "REWIND #08 „8 Handys“: 7 Freunde mit Handy für Mi 30.12., 2 Stunden. Termin in eine WhatsApp-Gruppe.",
    "Alles ins Blatt „Drehs“: Datum, Ort, wer kommt."], f="Vater, Gelände und Freunde zugesagt haben.", o=['bibel'])
review('2026-11-22', 4)

# ---- W5 · 23.–29.11. ----
A('2026-11-24', 'B', "Gate: gewaschene Stickprobe freigeben", 30, id="r8-strikeoff", s=[
    "Kuzgunlar schickt Fotos und ein kurzes Video der gestickten Proben nach der Wäsche. Claude prüft mit dir.",
    "Bestanden, wenn: kein Rot im Weiß, keine Wellen, Größe nach der Wäsche wie im Maßblatt (± 1 mm), Weiß gut lesbar, Kupfer-Gold ohne Indigo.",
    "Nicht bestanden: Korrektur schriftlich, neue Probe. Das Proto verschiebt sich dann, und Claude verschiebt den Start der Posts mit."],
  f="die Stickprobe schriftlich freigegeben ist oder die Korrektur raus ist.", o=['masse'])
A('2026-11-26', 'B', "Patch D: Stickprobe auf Leinen prüfen", 20, id="r8-patch-probe", s=[
    "Fotos von Kuzgunlar: Leinen, 4 Farben (Dunkelbraun 19-1432, Kupfer-Gold 17-1340, Gold 14-0952, Rot 18-1662), Einlage, Raster der Druckknöpfe 66 × 46 mm.",
    "Druckknöpfe versteckt hinter der Rückwand, glatte Kappen ohne Buchstaben. Ein Gürtel bis 4 cm muss durchpassen."], f="der Patch schriftlich freigegeben ist.", o=['masse', 'farben'])
review('2026-11-29', 5, ["Profil vorbereiten: Bio „Time Travel · 100 nummerierte Jeans · Drop 24.06.2027“, Link zur Warteliste, noch keine Posts."])

# ---- W6 · 30.11.–06.12. ----
A('2026-11-30', 'B', "Proto: Versandtermin und Sendungsnummer", 10, id="r8-proto-termin", s=[
    "Claude fragt bei Nargiza nach: Wann geht das Proto raus, mit welcher Sendungsnummer?",
    "Kommt es später als Do 10.12., schiebt Claude den ersten Post. Öffentlich wird erst mit dem echten Paar."], f="der Versandtermin bekannt ist.", o=['gmail'])
A('2026-12-02', 'C', "CapCut-Vorlagen anlegen", 45, id="r8-capcut", s=[
    "Vorlage REWIND: Rückspul-Geräusch, Hand gegen den Uhrzeigersinn, Endkarte „TIME TRAVEL · 24.06.“, Hinweis „Reverse. Nobody was in danger.“",
    "Vorlage BUILD und DETAIL: Schrift, Untertitel-Stil, Endkarte.",
    "Export 1080 × 1920, 30 fps. Ein Testvideo exportieren und am Handy ansehen."], f="die Vorlagen gespeichert sind und das Testvideo passt.", o=['capcut', 'bibel'])
A('2026-12-05', 'V', "Warteliste testen", 15, id="r8-warteliste-test", s=[
    "Mit zwei eigenen Adressen auf der Startseite eintragen. Kommt die Bestätigung? Kommt die Willkommens-Mail E00?",
    "In Shopify prüfen, ob beide Adressen als Abonnenten erscheinen."], f="beide Testadressen bestätigt angekommen sind.", o=['shopify'])
review('2026-12-06', 6)

# ---- W7 · 07.–13.12. ----
A('2026-12-12', 'B', "Fit-Test und Korrekturliste", 60, id="r8-fittest", s=[
    "Proto anziehen, sitzen, gehen, Treppe. Fotos vorn, seitlich, hinten im Spiegel.",
    "Alle 20 Maße flach messen wie im Maßblatt, Werte an Claude.",
    "Druckknopf-Test: Gürtel 20-mal durch Patch D, Patch 50-mal ab und an.",
    "Goldfäden: halten sie beim Hinsetzen? Claude schreibt aus allem die Korrekturliste für das PP."], f="Claude Maße, Fotos und Testergebnis hat.", o=['masse'])
A('2026-12-12', 'A', "Impressum und Datenschutz auf die Warteliste", 30, id="r8-impressum", s=[
    "Die eine Ausnahme von „Recht erst nach dem Muster“: Ab dem ersten Post tragen sich Leute ein. Ohne Impressum und Datenschutzerklärung riskierst du eine Abmahnung.",
    "Claude schreibt beide Texte für die Warteliste (ohne Shop), du fügst sie in Shopify ein: Einstellungen → Richtlinien, Links in den Footer.",
    "Willkommens-Mail E00: Datum der Vorbestellung auf Mo 15.02. ändern."], f="Impressum und Datenschutz im Footer verlinkt sind und E00 das neue Datum hat.", o=['shopify'], e='E00')
review('2026-12-13', 7)

# =====================================================================================
# Phase O · Öffentlich mit dem Proto (Mo 14.12. – So 17.01.)
# =====================================================================================
A('2026-12-14', 'D', "PP-Muster bestellen", 20, id="r8-pp-bestellen", s=[
    "Claude schickt Nargiza die Korrekturliste vom Fit-Test. Du sagst „senden“.",
    "Dazu: 2 Marketing-Paare (W32 und W36), wenn der Preis aus dem Angebot passt. Damit drehst du später, ohne das PP zu riskieren.",
    "Liefertermin des PP schriftlich: Ziel Mi 13.01."], f="das PP bestellt ist und der Liefertermin schriftlich steht.", o=['gmail'])
A('2026-12-16', 'V', "Netz: 15 persönliche Nachrichten", 30, id="r8-netz-1", s=[
    "15 Leute, die dich kennen und Jeans tragen. Persönlich, kein Kopiertext: „Ich mache meine erste Jeans, 100 Stück, nummeriert. Gestern ging das erste Video raus. Wenn du magst, trag dich ein: [Link]“",
    "Wer antwortet, bekommt eine echte Antwort. Niemanden zweimal anschreiben."], f="15 Nachrichten raus sind.", o=['insta'])
review('2026-12-20', 8, ["Erste Woche öffentlich: Welches Video hatte mehr Views? Ein Satz an Claude."])
review('2026-12-27', 9)
review('2027-01-03', 10, ["Nach 5 Posts der erste ehrliche Check: Hat ein Video mindestens das Doppelte deines Medians? Wenn nicht, macht Claude 3 neue Hooks für die nächsten Stunts."])
A('2027-01-06', 'B', "PP: Versandtermin prüfen", 10, id="r8-pp-termin", s=["Claude fragt nach der Sendungsnummer. Verspätung heißt: Freigabe und Gewerbe rutschen mit, nicht die Vorbestellung zuerst."],
  f="die Sendungsnummer da ist.", o=['gmail'])
review('2027-01-10', 11)
A('2027-01-13', 'B', "PP-Muster prüfen", 60, id="r8-pp-pruefen", s=[
    "Auspacken filmen (V223), dann wie beim Proto: anziehen, 20 Maße, Fotos, Druckknopf-Test.",
    "Jede Korrektur vom Proto abhaken: umgesetzt oder nicht?",
    "Waschserie starten: das PP 5-mal auf links bei 30 °C waschen bis Ende Februar (für V231), Goldfäden nach jeder Wäsche fotografieren."], f="Claude Maße, Fotos und die abgehakte Korrekturliste hat.", o=['masse'])
A('2027-01-15', 'D', "GATE · Muster-Freigabe", 30, id="r8-freigabe", s=[
    "Freigabe nur, wenn: Maße in der Toleranz, alle Stickereien wie freigegeben, Patch hält, Goldfäden halten, Wäsche wie der Standard.",
    "Ja: Claude schreibt die schriftliche Freigabe an Kuzgunlar („sealed sample“), du sagst „senden“. Ab Montag starten Gewerbe, Recht und Shop.",
    "Nein: Claude schreibt die Korrektur, neues PP. Dann verschiebt sich der Start der Vorbestellung um die gleiche Zeit."],
  f="die Freigabe schriftlich bei Kuzgunlar ist.", o=['gmail'])
review('2027-01-17', 12)

# =====================================================================================
# Phase R · Gewerbe, Recht, Shop und Vorbestellung (Mo 18.01. – So 21.03.)
# =====================================================================================
A('2027-01-18', 'R', "Gewerbe anmelden", 30, id="r8-gewerbe", s=[
    "Service-Portal Berlin → Gewerbeanmeldung online. Tätigkeit: „Online-Handel mit Bekleidung, Entwurf von Bekleidung“. Beginn: heute.",
    "Unter 18? Dann gilt der Weg aus der Frage vom 31.10., Claude hat ihn dann schon im November gestartet.",
    "Gebühr online zahlen. Den Gewerbeschein als PDF in „TT Belege“."], f="die Anmeldung abgeschickt ist.", o=['gewerbe'])
A('2027-01-21', 'B', "Serie vorbereiten: Termine und Nummern", 20, id="r8-serie-vorbereiten", s=[
    "Claude klärt mit Kuzgunlar: Produktionszeit ab Bestellung, Ziel fertig bis Fr 14.05., Endkontrolle mit Foto pro Paar, Etiketten mit Nummern 001–100.",
    "Die Bestellung selbst kommt erst am Mo 15.03., wenn die Menge feststeht."], f="Produktionszeit und Ablauf schriftlich da sind.", o=['gmail'])
review('2027-01-24', 13)
A('2027-01-25', 'R', "Fragebogen zur steuerlichen Erfassung", 45, id="r8-elster", s=[
    "Kommt ein paar Tage nach dem Gewerbe. ELSTER → Formulare → Fragebogen zur steuerlichen Erfassung (Einzelunternehmen).",
    "Kleinunternehmerregelung ja oder nein: Claude erklärt dir vorher in 5 Sätzen, was das für 149 € und die Einfuhrumsatzsteuer bedeutet. Bei Unsicherheit: Steuerberater oder IHK fragen.",
    "Steuernummer notieren, sobald sie da ist."], f="der Fragebogen abgeschickt ist.", o=['elster'])
A('2027-01-28', 'R', "Rechtstexte für den Shop", 45, id="r8-rechtstexte", s=[
    "Claude schreibt die Entwürfe: Impressum, Datenschutz, AGB, Widerrufsbelehrung, Versand und Zahlung, Hinweis zur Vorbestellung (Lieferung bis 30.06.2027).",
    "Einfügen in Shopify → Einstellungen → Richtlinien. Keine Rechtsberatung: Für eine Prüfung gibt es günstige Pakete bei Händlerbund oder IT-Recht Kanzlei.",
    "Herstellerangabe für das Etikett (GPSR): deine Adresse oder ein Postfach. Claude schickt sie an Kuzgunlar."], f="alle Texte im Shop stehen und im Footer verlinkt sind.", o=['shopify'])
review('2027-01-31', 14)
A('2027-02-01', 'W', "Produktseite und Vorbestellung bauen", 60, id="r8-produktseite", s=[
    "Shopify → Produkte → hinzufügen: Time Travel Jeans NVL-TT-01, Größen W30–W38, Preis 149 €, Bestand 35, danach Stufe 2 zu 169 € (Nr. 036–060).",
    "Text: Claude schreibt ihn, mit Lieferung „spätestens 30.06.2027, geplant Anfang Juni“ und der Größentabelle (ehrliche Größen).",
    "Fotos: Proto und PP aus deinen Drehs, keine Fabrik, keine Adressen.",
    "Startseite bleibt bis Mo 15.02. die Warteliste. Produkt nur mit Passwort-Link sichtbar."], f="die Produktseite fertig, aber noch nicht öffentlich ist.", o=['shopify'])
A('2027-02-04', 'R', "Zahlung, Konto und Testbestellung", 30, id="r8-zahlung", s=[
    "Shopify Payments mit Gewerbe und Steuernummer aktivieren, Auszahlung auf ein eigenes Konto (am besten ein getrenntes Geschäftskonto).",
    "Testbestellung mit 1 € Testprodukt: Bezahlen, Bestätigung, Stornieren, Erstattung prüfen."], f="eine Testbestellung durchgelaufen und erstattet ist.", o=['shopify'])
A('2027-02-11', 'R', "LUCID: Verpackung registrieren", 20, id="r8-lucid", s=[
    "Wer verpackte Ware an Kunden in Deutschland schickt, muss im Verpackungsregister LUCID stehen und ein System beteiligen.",
    "Registrieren (kostenlos), dann ein kleines Lizenzpaket für Versandverpackung buchen. Claude hilft bei der Menge."], f="die LUCID-Nummer da ist.", o=['lucid'])
review('2027-02-07', 15)
A('2027-02-08', 'V', "Netz-Runde 2: Vorbestellung ankündigen", 30, id="r8-netz-2", s=[
    "20 persönliche Nachrichten an alle, die geantwortet oder kommentiert haben: „Montag, 15.02., 19:00 geht die Vorbestellung auf. 35 Paar zu 149 €, die Liste ist um 18:00 dran.“",
    "Wer eine Größe nennt, ins Blatt „Netz“ (nur Vorname und Größe)."], f="20 Nachrichten raus sind.", o=['insta'])
A('2027-02-10', 'W', "Generalprobe Vorbestellung", 45, id="r8-generalprobe", s=[
    "Mit Passwort-Link die ganze Bestellung einmal echt durchspielen: Größe wählen, zahlen, Bestätigungsmail, Nummer im Blatt notieren.",
    "Am Handy im Instagram-Browser testen.",
    "Was hakt, an Claude. Danach Testbestellung erstatten."], f="eine echte Bestellung am Handy durchgelaufen ist.", o=['shopify'])
A('2027-02-14', 'V', "Vorbestellung für Montag scharf schalten", 20, id="r8-scharf", tm="18:30", s=[
    "Shopify: Produkt auf „aktiv“ für Mo 15.02., 18:00 planen (oder Mo 17:55 von Hand). Startseite ab 19:00 mit dem Produkt.",
    "Mail E06 ist für Mo 18:00 terminiert (Aufgabe davor). R11 liegt fertig im Ordner."], f="Produkt und Mail für Montag geplant sind.", o=['shopify'])
review('2027-02-14', 16)
A('2027-02-15', 'V', "VORBESTELLUNG ÖFFNET", 45, id="r8-vorbestellung-auf", tm="18:00", s=[
    "18:00: Liste bekommt E06. Prüfen, ob der Link geht.",
    "19:00: R11 posten (Aufgabe unten), Story mit Link-Sticker.",
    "Bis 20:00 bleiben: DMs und Kommentare beantworten, jede Bestellung im Blatt mit Nummer."], f="die ersten Bestellungen da sind und alle Fragen beantwortet sind.", o=['shopify', 'insta'])
A('2027-02-16', 'V', "Danke an die ersten Vorbesteller", 20, id="r8-danke", s=[
    "Jedem der ersten Vorbesteller eine kurze persönliche Mail oder DM: Danke, deine Nummer, Lieferung Anfang Juni.",
    "Keine Namen öffentlich ohne Erlaubnis."], f="alle ersten Vorbesteller eine Nachricht haben.", o=['shopify'])
review('2027-02-21', 17, ["Bezahlte Vorbestellungen eintragen. Ziel bis heute: 6."])
review('2027-02-28', 18)
review('2027-03-07', 19)
A('2027-03-12', 'B', "Bestellmenge vorbereiten", 20, id="r8-menge-vorbereiten", s=[
    "Claude rechnet mit dir: bezahlte Vorbestellungen, Geld auf dem Konto, Anzahlung 50 % für 50, 75 oder 100 Paar.",
    "Die Regel steht im Abschnitt „Zahlen“. Am So 14.03. entscheidest du."], f="die drei Varianten mit Betrag vor dir liegen.")
A('2027-03-14', 'D', "GATE · Bestellmenge", 20, id="r8-menge", tm="18:00", s=[
    "Bezahlte Vorbestellungen bis heute 18:00 zählen.",
    "20 oder mehr: 100 Paar. 10 bis 19: 75 Paar (wenn Kuzgunlar die Menge macht). Unter 10: Notfall-Regel im Abschnitt „Zahlen“, du entscheidest mit Claude.",
    "Entscheidung ins Blatt „Entscheidungen“. V240 erzählt sie."], f="die Menge feststeht.")
review('2027-03-14', 20)
A('2027-03-15', 'B', "Serie bestellen und anzahlen", 30, id="r8-serie-bestellen", s=[
    "Claude schreibt die Bestellung: Menge, Größenverteilung aus den Vorbestellungen plus Schätzung, Nummernliste, Liefertermin Fr 14.05., Versandweg.",
    "Du sagst „senden“. Proforma prüfen wie beim Muster, 50 % anzahlen, Beleg ablegen.",
    "Kurz filmen, wie du auf „senden“ drückst (für V241)."], f="die Bestellung bestätigt und die Anzahlung raus ist.", o=['gmail'])
A('2027-03-21', 'C', "Autopilot für die Abi-Pause einplanen", 60, id="r8-autopilot", s=[
    "5 Posts terminieren: R13 (Sa 27.03.), V256 (Sa 03.04.), R10 (Sa 17.04.), V258 (Sa 24.04.), V244 (Sa 08.05.), jeweils 12:00.",
    "Instagram: Meta Business Suite → Planen. TikTok: Desktop → Hochladen → Planen. YouTube: Planen.",
    "Karussell V244 aus den Fotos seit Oktober bauen (8 Bilder).",
    "Bio: „Prüfungen bis 09.05. · Vorbestellung läuft · Drop 24.06.“. Automatische Antwort in den DMs: „Bin in den Prüfungen, antworte ab 10.05.“"],
  f="alle 5 Posts terminiert sind und die Auto-Antwort an ist.", o=['meta', 'tiktok', 'capcut'])
review('2027-03-21', 21, ["Ab morgen Abi-Pause. Nur noch sonntags 10 Minuten, wenn du willst."])

# =====================================================================================
# Phase A · Abi-Pause (Mo 22.03. – So 09.05.)
# =====================================================================================
for n, iso in zip(range(22, 29), ['2027-03-28', '2027-04-04', '2027-04-11', '2027-04-18', '2027-04-25', '2027-05-02', '2027-05-09']):
    A(iso, 'A', "Kurz-Check: Postfach und Shop", 10, id=f"r8-pause-w{n}", plus=True, s=[
        "Nur wenn du Zeit hast. Gmail: Hat Kuzgunlar etwas gefragt? Shopify: neue Bestellungen, Kundenfragen.",
        "Fragen der Fabrik beantwortet Claude mit dir in 5 Minuten. Alles andere wartet bis 10.05."], f="nichts Dringendes offen ist.", o=['gmail', 'shopify'])
P.note('2027-03-22', "Abi-Pause bis So 09.05. Die Fabrik produziert, 5 Posts laufen automatisch. Viel Erfolg in den Prüfungen.")
P.note('2027-04-17', "Mitte der Produktion: Kuzgunlar schickt Fotos. Anschauen nur, wenn du magst.")

# =====================================================================================
# Phase E · Endspurt und Drop (Mo 10.05. – So 27.06.)
# =====================================================================================
P.note('2027-05-10', "Nach den schriftlichen Prüfungen. Der Plan rechnet ab jetzt mit 6–8 Stunden pro Woche. Hast du weniger, sag es Claude, dann fällt zuerst Grind+ weg.")
A('2027-05-10', 'B', "Endkontrolle: Fotos und Video je Paar prüfen", 60, id="r8-endkontrolle", s=[
    "Kuzgunlar schickt pro nummeriertem Paar ein Foto (vorn, hinten, Etikett) und ein Video der Kontrolle.",
    "Claude prüft mit dir stichprobenweise: Stickereien, Patch, Goldfäden, Nummern ohne Lücke und doppelt.",
    "Fehler: Reservepaar mit gleicher Nummer, neues Etikett."], f="die Endkontrolle schriftlich bestanden ist.", o=['gmail'])
A('2027-05-14', 'A', "Restzahlung nach bestandener Endkontrolle", 20, id="r8-restzahlung", s=[
    "Erst nach der Endkontrolle, nie vorher. Betrag gegen die Proforma prüfen.",
    "Reicht das Geld nicht: Notfall-Regel im Abschnitt „Zahlen“ (Stufe 2 früher, Familie, Teillieferung)."], f="die Restzahlung raus ist.")
review('2027-05-16', 29)
A('2027-05-23', 'V', "149 € endet heute 20:00, Stufe 2 an", 15, id="r8-stufe2", tm="20:00", s=[
    "20:00: Preis im Shop auf 169 € (Stufe 2, Nr. 036–060), Text „Vorbestellen bis So 06.06., Lieferung Anfang Juni“.",
    "Nie verlängern, auch wenn noch Paare zu 149 € übrig sind."], f="der Shop um 20:05 169 € zeigt.", o=['shopify'])
review('2027-05-23', 30)
A('2027-05-26', 'B', "Versand der Vorbestellungen starten", 30, id="r8-versand-vor", s=[
    "Je nach Versandweg vom 13.11.: Kuzgunlar schickt jedes Paar direkt, oder die Sendung kommt in Berlin an und wird verschickt.",
    "Sendungsnummern in Shopify eintragen, damit jeder Käufer die Versandmail bekommt.",
    "3 Paare bleiben bei dir: Nr. 001 für REWIND #19 und die beiden Marketing-Paare."], f="alle Vorbestellungen unterwegs sind.", o=['shopify', 'gmail'])
review('2027-05-30', 31)
A('2027-06-02', 'V', "Kundenservice: Lieferungen, Größen, Umtausch", 30, id="r8-service", s=[
    "Jede Frage in 24 Stunden beantworten. Größe passt nicht: Umtausch, solange eine Größe frei ist.",
    "Fotos von Käufern nur mit Erlaubnis teilen."], f="keine Frage älter als 24 Stunden ist.", o=['gmail', 'shopify'])
A('2027-06-06', 'V', "Stufe 2 endet 20:00", 10, id="r8-stufe2-ende", tm="20:00", s=[
    "Produkt auf „Drop 24.06., 19:00“ umstellen: nicht mehr kaufbar bis zum Drop.", "Restbestand je Größe ins Blatt."], f="der Shop den Drop-Termin zeigt.", o=['shopify'])
review('2027-06-06', 32)
review('2027-06-13', 33)
A('2027-06-18', 'W', "Drop-Generalprobe und Code-Freeze", 45, id="r8-drop-probe", s=[
    "Produkt für Do 24.06., 18:00 (Liste, Passwort) und 19:00 (alle) planen, Preis 169 €, Bestand je Größe.",
    "Eine Testbestellung am Handy. Danach ändert niemand mehr etwas am Shop (Code-Freeze ab Sa)."], f="der Drop geplant ist und die Testbestellung lief.", o=['shopify'])
review('2027-06-20', 34)
A('2027-06-24', 'V', "DROP-ABEND", 60, id="r8-drop", tm="19:00", s=[
    "18:00 Liste rein (E19), 19:00 alle (E20, V273). Live V272 von 18:00 bis 18:30.",
    "Bis 21:00: Fragen beantworten, Bestellungen an den Versandweg übergeben.",
    "21:00: Zahl der Käufe ins Blatt. Unter 15: E21 morgen um 10:00 senden."], f="alle Bestellungen übergeben sind und die Zahl im Blatt steht.", o=['shopify', 'insta'])
A('2027-06-27', 'D', "Auswertung und nächster Schritt", 60, id="r8-auswertung", s=[
    "Mit Claude: Was hat verkauft, welches Video hat Anmeldungen gebracht, was hat Zeit gekostet?",
    "Ziel bis 31.08.: alle 100 Paare verkauft. Plan für den Rest: Restgrößen, Zipper, nächster Drop."], f="die Auswertung im Blatt steht.")
review('2027-06-27', 35)

content8.gen_tasks(P)
mails8.gen_tasks(P)

PH = {
    'F': ("Fabrik und Design fertig", "30. Okt – 13. Dez 2026"),
    'O': ("Öffentlich mit dem Proto", "14. Dez 2026 – 17. Jan 2027"),
    'R': ("Gewerbe, Recht, Shop, Vorbestellung", "18. Jan – 21. Mär 2027"),
    'A': ("Abi-Pause", "22. Mär – 9. Mai 2027"),
    'E': ("Endspurt und Drop", "10. Mai – 27. Jun 2027"),
}
GOALS = {
    1: ('F', "Maßblätter und Farbcodes bei Nargiza, die anderen Fabriken im Blick"),
    2: ('F', "Schriftliches Angebot, Fabrik entschieden, Muster angezahlt, Zipper-Papiertest"),
    3: ('F', "Unterlagen bei Kuzgunlar, Etikett und Hangtag gewählt, Versandweg entschieden"),
    4: ('F', "Digitizing freigegeben, Zipper und Polo entschieden, Stunt-Drehs organisiert"),
    5: ('F', "Gate gewaschene Stickprobe, Patch-Probe, Material für das erste Video"),
    6: ('F', "Ruhige Woche: CapCut-Vorlagen, Warteliste testen, Puffer für die Fabrik"),
    7: ('F', "Das Proto ist da: auspacken filmen, Fit-Test, Impressum vor dem ersten Post"),
    8: ('O', "PP bestellt, die ersten zwei Posts öffentlich, 15 Nachrichten ans Netz"),
    9: ('O', "Ferien: REWIND #01 mit der G-Klasse drehen und posten"),
    10: ('O', "Making-of #01, REWIND #08 mit 8 Handys, Material für Januar"),
    11: ('O', "Zwei Posts, PP unterwegs"),
    12: ('O', "PP prüfen, GATE Muster-Freigabe am Fr 15.01."),
    13: ('R', "Gewerbe angemeldet, Serie vorbereitet, REWIND #07"),
    14: ('R', "Steuerliche Erfassung, Rechtstexte, REWIND #03"),
    15: ('R', "Produktseite, Zahlung, LUCID, REWIND #12"),
    16: ('R', "Netz-Runde 2, Generalprobe, alles für Montag scharf"),
    17: ('R', "Vorbestellung öffnet Mo 15.02. mit REWIND #11 · G-Klasse II"),
    18: ('R', "Vorbestellung am Laufen halten, Making-of #11"),
    19: ('R', "Zwei Posts, REWIND #05, Waschserie fertig"),
    20: ('R', "GATE Bestellmenge am So 14.03., Material für die Pause drehen"),
    21: ('R', "Serie bestellt, Autopilot eingeplant, ab Montag Abi"),
    22: ('A', "Abi-Pause"), 23: ('A', "Abi-Pause"), 24: ('A', "Abi-Pause"), 25: ('A', "Abi-Pause"),
    26: ('A', "Abi-Pause"), 27: ('A', "Abi-Pause"), 28: ('A', "Abi-Pause"),
    29: ('E', "Endkontrolle, Restzahlung, drei Posts, REWIND #16"),
    30: ('E', "Der Vorbestellpreis 149 € endet So 23.05., 20:00"),
    31: ('E', "Vorbestellungen gehen raus, REWIND #17 mit Freunden"),
    32: ('E', "Kundenservice, REWIND #18, Stufe 2 endet So 06.06."),
    33: ('E', "REWIND #19 mit Paar 001, Countdown gedreht"),
    34: ('E', "Countdown T−10 bis T−4, Drop-Generalprobe"),
    35: ('E', "Drop Do 24.06., 19:00, Finale REWIND #20, Auswertung"),
}
WEEKS = P.weeks(GOALS)

# ---- Zahlen: realistische Ziele (Sonntag), Alarm etwa 60 % ----
# fo = Follower gesamt (TikTok + Instagram), wl = Warteliste bestätigt, pre = bezahlte Vorbestellungen
KPI = [
    dict(d='2026-11-01', fo=170, wl=0, pre=None, gate="Startwerte: 170 Follower, Warteliste 0. Bis zum Proto wird nichts gepostet."),
    dict(d='2026-12-20', fo=250, wl=15, pre=None, gate="Erste Woche öffentlich. Noch kein Urteil, nur messen."),
    dict(d='2027-01-03', fo=400, wl=40, pre=None, gate="Nach REWIND #01 und #08: Hat einer das Doppelte deines Medians? Sonst 3 neue Hooks von Claude."),
    dict(d='2027-01-17', fo=500, wl=60, pre=None, gate="Muster freigegeben? Dann ab Mo Gewerbe."),
    dict(d='2027-01-31', fo=650, wl=90, pre=None, gate="Warteliste unter 55: Netz-Runde 2 vorziehen, REWIND #12 mit stärkerem Hook."),
    dict(d='2027-02-14', fo=800, wl=120, pre=None, gate="Vorbestellung morgen. Unter 70 auf der Liste: trotzdem öffnen, aber Ziel bis 14.03. halbieren."),
    dict(d='2027-02-21', fo=850, wl=125, pre=6, gate="Erste Woche Vorbestellung. Unter 4: persönliche Nachricht an alle, die sich die Größe notiert haben."),
    dict(d='2027-02-28', fo=900, wl=130, pre=10, gate=None),
    dict(d='2027-03-07', fo=950, wl=135, pre=13, gate=None),
    dict(d='2027-03-14', fo=1000, wl=140, pre=15, gate="GATE Bestellmenge: 20+ → 100 Paar · 10–19 → 75 Paar · unter 10 → Notfall-Regel."),
    dict(d='2027-05-09', fo=1050, wl=150, pre=22, gate="Restzahlung am Fr 14.05.: Geld reicht? Sonst Notfall-Regel."),
    dict(d='2027-05-23', fo=1200, wl=170, pre=28, gate="149 € endet heute 20:00."),
    dict(d='2027-06-06', fo=1400, wl=200, pre=32, gate="Stufe 2 endet heute 20:00."),
    dict(d='2027-06-20', fo=1600, wl=250, pre=35, gate="Drop am Donnerstag."),
    dict(d='2027-06-27', fo=1800, wl=280, pre=35, gate="Drop-Wochenende: 15 Käufe im Drop sind ein guter Start. Ziel: alle 100 bis 31.08."),
]
for k in KPI:
    for f in ('fo', 'wl', 'pre'):
        k[f + '_a'] = None if k[f] is None else int(round(k[f] * 0.6))

DONE_STATIC = [
    ("Sep–Okt", "Konzept „Time Travel“, Thema, Herkunftsgeschichte, Ornament-Grammatik"),
    ("Okt", "Design der Jeans eingefroren: Band A, Münztasche E, B2 mit Goldfäden, Stern C, Patch D"),
    ("17.–22.10.", "Papiertests an der Eightyfive, Druckvorlage 1:1 v1.9, Mockup"),
    ("17.10.", "Fabrik-Recherche, Anfragen an 6 Fabriken"),
    ("20.10.", "Quote Pack v0.9 an die Fabriken"),
    ("23.10.", "Tech Pack v1.0 (Englisch und Deutsch), Leitfaden für die Fabrik-Calls"),
    ("24.–26.10.", "Zipper: Briefing, Designvorschlag v0.2, Teppich „wie bei Oma“, Maße S–XL"),
    ("28.10.", "Call mit Kuzgunlar (Nargiza): Stickerei und Wäsche im Haus, Muster in ein paar Wochen, 50/50"),
    ("28.10.", "Farbcodes aller Garne, Patch D wird von Kuzgunlar gestickt"),
    ("30.10.", "Maßblätter v1.1 im Format von Kuzgunlar"),
    ("Okt", "Shopify-Shop angelegt, Warteliste als Startseite mit Willkommens-Mail"),
]
OPEN_Q = [
    ("Sa 31.10.", "Bist du 18 oder älter? (Gewerbe)"),
    ("Sa 31.10.", "Ab wann bist du wieder in Berlin? (Zipper-Papiertest, Proto)"),
    ("Mi 04.11.", "Schriftlicher Preis von Kuzgunlar, Mindestmenge, Versand an Endkunden"),
    ("Mi 18.11.", "Zipper und Polo in diesem Drop oder im nächsten"),
    ("Mo 10.05.", "Hast du nach den schriftlichen Prüfungen wirklich mehr Zeit? (Plan rechnet mit 6–8 Stunden pro Woche)"),
]
