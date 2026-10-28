# -*- coding: utf-8 -*-
"""Alle E-Mails an die Liste, fertig geschrieben. [Platzhalter] vor dem Senden mit echten Zahlen füllen."""

SIG = "Ernest\nNovalife · Berlin\n\nDu bekommst diese Mail, weil du dich für Time Travel eingetragen hast. Abmelden: Link unten."

M = {}


def mail(id, wann, an, betreff, alt, vorschau, text, check=""):
    M[id] = dict(id=id, wann=wann, an=an, betreff=betreff, alt=alt, vorschau=vorschau, text=text.strip() + "\n\n" + SIG,
                 check=("Platzhalter in [eckigen Klammern] durch echte Zahlen ersetzen. Testmail an dich, am Handy lesen, Links antippen. " + check).strip())


mail("E00", "automatisch nach der Bestätigung", "jede neue Anmeldung (Willkommens-Mail in Shopify)",
     "Du bist auf der Liste. Die Liste kauft zuerst.", ["Willkommen bei Time Travel", "Danke. Du bist drin."],
     "100 nummerierte Jeans, und du bist eine Stunde früher dran.",
     """
Hey,

danke, dass du dabei bist. Time Travel sind 100 nummerierte Jeans mit vier Stickereien und einem Patch, dazu ein Zipper mit einem kleinen Wandteppich vorn.

Was die Liste dir bringt:
· Die Vorbestellung öffnet am Mo 01.02.2027 um 19:00. Du bekommst den Link schon um 18:00.
· Die ersten 35 Paar kosten 149 € statt 169 € und bekommen die kleinsten Nummern.
· Ich schreibe dir nur, wenn etwas passiert: das erste echte Paar, das finale Muster, der Start.

Kennst du jemanden, der Jeans liebt? Dein eigener Link: [BRING-3-LINK]

Bis bald,""",
     "Bring-3-Link nur, wenn „Bring 3 Freunde“ eingebaut ist und der Datenschutz-Absatz online steht.")

mail("E01", "Mo 30.11., 19:00", "Segment „E-Mail-Abonnenten“ (nur bestätigte)",
     "Ab heute öffentlich: 10 Wochen Papier", ["Tag 1: Ich zeige jetzt alles", "Die Jeans ist fertig gezeichnet"],
     "Was in zehn Wochen entstanden ist, und was als Nächstes kommt.",
     """
Hey,

zehn Wochen lang habe ich an einer einzigen Jeans gezeichnet. Jede Stickerei habe ich zuerst als Papier auf meine eigene Hose geklebt, bevor sie in eine Stickdatei durfte. Seit gestern ist das Design fertig. Ab heute zeige ich alles öffentlich.

Was feststeht:
· 100 Paar, nummeriert, aus einer Fabrik
· vier Stickereien: ein Kreuzstich-Band an der Tasche, eine bestickte Münztasche, drei Ähren mit neun Goldfäden, ein Achtstern
· ein Lebensbaum-Patch aus Leinen, der zugleich die hintere Gürtelschlaufe ist

Was als Nächstes kommt: Nächste Woche kommt das erste echte Paar, der Prototyp. Du siehst ihn hier zuerst.

[FOTO: Papiertest an der Jeans]

Die Liste kauft zuerst: 35 Paar zum Vorbestellpreis, am Mo 01.02. um 18:00, eine Stunde vor allen anderen.""",
     "Kein fertiges Teil im Bild, nur Papier. Link zur Seite mit utm_source=email&utm_campaign=e01.")

mail("E02", "Di 08.12., 19:00 (nur wenn das Proto da ist)", "Segment „E-Mail-Abonnenten“",
     "Das erste echte Paar ist da", ["Zehn Wochen Papier. Heute: Garn.", "Ich habe es gerade ausgepackt"],
     "Der Prototyp ist angekommen. Nicht perfekt, aber echt.",
     """
Hey,

heute kam der Prototyp. Zehn Wochen Papier, und jetzt liegt die erste echte Jeans auf meinem Tisch.

Ehrlich: Sie ist noch nicht perfekt. Diese Woche messe ich alles nach, zwei Leute probieren sie an, und dann geht eine Korrekturliste an die Fabrik. Das nächste Muster ist das finale, nach dem alle 100 Paar gemacht werden.

Das Auspacken habe ich gefilmt, ungeschnitten:
[BUTTON: Das Auspacken ansehen → TikTok-Profil]

Willst du sie in echt sehen? Antworte einfach auf diese Mail. Ich zeige sie bis Weihnachten in kleinen Runden, 15 Minuten, bei mir, im Café oder per Video.

Die Vorbestellung öffnet am Mo 01.02. um 19:00. Die Liste ist um 18:00 drin.""",
     "Nie senden, bevor das Proto wirklich da ist. Termin sonst verschieben.")

mail("E03", "Mi 20.01., 19:00", "Segment „E-Mail-Abonnenten“",
     "Freigegeben. Und: dein Platz in der ersten Stunde", ["Das finale Muster ist freigegeben", "Reservier dir die erste Stunde"],
     "Das Muster für alle 100 Paar steht. Ab heute kannst du dir einen Platz sichern.",
     """
Hey,

am Freitag habe ich das finale Muster freigegeben. Es ist jetzt versiegelt und der Maßstab für alle 100 Paar.

[FOTO: versiegeltes Muster]

Ab heute bis So 31.01. kannst du dir einen Platz in der ersten Stunde sichern. Dann bekommst du am Mo 01.02. um 18:00 den Link als Erste oder Erster.
[BUTTON: Platz sichern]

So läuft der 01.02.:
· 18:00: Link für die Liste
· 19:00: offen für alle
· 35 Paar zu 149 €, danach 169 €
· Lieferung bis spätestens 30.06.2027, geplant Anfang Juni""",
     "Text an die Reservierungs-Entscheidung anpassen (kostenlos oder 10 €).")

mail("E04", "Di 26.01., 18:00", "Segment „E-Mail-Abonnenten“",
     "Montag, 19:00: So läuft die Vorbestellung", ["Noch 6 Tage", "Alles, was du für Montag wissen musst"],
     "Größe, Preis, Lieferung, Geld-zurück-Regel. Alles in einer Mail.",
     """
Hey,

nächsten Montag, 01.02., öffnet die Vorbestellung. Damit du nicht suchen musst, hier alles:

Wann: Mo 01.02. Du bekommst um 18:00 den Link, alle anderen um 19:00.
Was: Time Travel Jeans NVL-TT-01, nummeriert 001–100.
Preis: Die ersten 35 Paar 149 €, danach 169 €.
Größe: W30 bis W38, ehrlich gemessen. Das Etikett ist die echte Bundweite: W34 = 86 cm. So misst du: Lieblingsjeans flach hinlegen, Knopf zu, Bund von Kante zu Kante, mal zwei.
Lieferung: bis spätestens 30.06.2027, geplant Anfang Juni.
Wenn es nicht klappt: Kommen bis zum 15.02. nicht genug Vorbestellungen zusammen, bekommst du dein Geld vollständig zurück.
Nummer: Wer zuerst bestellt, bekommt die kleinste Nummer.

[ZIPPER: Absatz nur, wenn der Zipper vorbestellbar ist: „Auch der Zipper ist ab Montag vorbestellbar, 20 € unter dem Drop-Preis.“]

Fragen? Antworte einfach.""",
     "Geld-zurück-Satz genau wie auf der Seite (rechtlich geprüft in W18).")

mail("E05", "So 31.01., 18:00", "Segment „E-Mail-Abonnenten“",
     "Morgen: 18:00 für dich, 19:00 für alle", ["Morgen ist es so weit", "24 Stunden"],
     "Halte morgen um 18:00 dein Postfach offen.",
     """
Hey,

morgen um 18:00 bekommst du eine Mail mit dem Link zur Vorbestellung. Eine Stunde vor allen anderen.

Zwei Tipps:
1. Miss heute Abend deine Lieblingsjeans (flach, Knopf zu, Bund mal zwei). Dann musst du morgen nicht überlegen.
2. Leg dein Zahlungsmittel bereit. Die 35 Paar zu 149 € sind nur 35.

Bis morgen, 18:00.""")

mail("E06", "Mo 01.02., 18:00 (terminiert)", "Segment „E-Mail-Abonnenten“ (nur die Liste)",
     "Du bist drin. Die Vorbestellung ist offen.", ["Jetzt. Eine Stunde vor allen.", "Dein Link"],
     "35 Paar zu 149 €. Für alle anderen öffnet es um 19:00.",
     """
Hey,

die Vorbestellung ist offen, für dich eine Stunde vor allen anderen.

[BUTTON: Jetzt vorbestellen → Schlüssel-Link]

· 35 Paar zu 149 €, danach 169 €
· nummeriert nach Bestelldatum, ab 001
· Lieferung bis spätestens 30.06.2027, geplant Anfang Juni

Danke, dass du von Anfang an dabei bist.""",
     "Schlüssel-Link testen: öffnet er die Seite schon um 18:00? Nicht in die Story posten.")

mail("E07", "Mo 08.02., 18:00", "Segment „E-Mail-Abonnenten“ ohne Kauf",
     "Noch [Y] Paar zu 149 €", ["Eine Woche Vorbestellung", "[X] von 35 sind weg"],
     "Danach kostet sie 169 €.",
     """
Hey,

eine Woche Vorbestellung: [X] von 35 Paar zu 149 € haben einen Besitzer. Noch [Y] sind übrig, danach kostet die Jeans 169 €.

Unsicher bei der Größe? Mittwoch, 10.02., 18:00–20:00 ist Mess-Abend 2 in [ORT]. Komm vorbei und probier.

[BUTTON: Vorbestellen]""",
     "Nur echte Zahlen. Unter 5 verkauft: Betreff „Mess-Abend am Mittwoch“, ohne Zahl.")

mail("E08", "Di 09.02., 18:00", "Abonnenten ohne Kauf, die E06 geöffnet haben",
     "Eine Frage an dich", ["Was hält dich zurück?", "Kurze Frage, ehrliche Antwort"],
     "Antworte mit einem Wort, das hilft mir sehr.",
     """
Hey,

du hast die Mail zur Vorbestellung geöffnet, aber noch nicht bestellt. Völlig okay. Darf ich fragen, warum?

Antworte einfach mit einem Wort:
· Größe
· Preis
· Lieferzeit
· Design
· später

Ich lese jede Antwort selbst. Wenn es die Größe ist: Mittwoch ist Mess-Abend, oder schick mir deine Bundweite, und ich sage dir, welche passt.""")

mail("E09", "Do 18.02., 19:00", "Segment „E-Mail-Abonnenten“",
     "Bestellt.", ["[100] Paar sind bestellt", "Es passiert wirklich"],
     "Die Fabrik hat die Bestellung. Fertig bis 14.05.",
     """
Hey,

gestern habe ich die Bestellung an die Fabrik geschickt: [100] Paar Time Travel. Heute ist die Anzahlung raus.

Dank [X] Vorbestellungen ist das möglich geworden. Wenn du dazugehörst: Danke. Wirklich.

Wie es weitergeht:
· Produktion ab Mitte Februar
· im März ein Shoot in Berlin
· fertig bis 14.05.
· Lieferung an die Vorbesteller Anfang Juni
· Drop für alle: Do 24.06., 19:00

Noch [Y] Paar gibt es zum Vorbestellpreis.""")

mail("E10", "Mo 08.03., 19:00", "Segment „E-Mail-Abonnenten“",
     "Die ersten echten Fotos", ["Der Shoot", "So sieht Time Travel aus"],
     "Samstag haben wir fotografiert. Hier ist das erste Bild.",
     """
Hey,

am Samstag war der erste Shoot: ein Raum mit einem alten Wandteppich, danach die goldene Stunde draußen.

[FOTO: Hauptbild]

Die Bilder kommen diese Woche auf die Seite. Ab dem 22.03. wird es hier ruhiger: Ich schreibe meine Abiturprüfungen, die Fabrik produziert. Im Mai melde ich mich mit den ersten Fotos der fertigen Serie.

[BUTTON: Alle Bilder ansehen]""")

mail("E11", "Mo 17.05., 18:00", "Segment „E-Mail-Abonnenten“ ohne Kauf",
     "149 € endet am Sonntag", ["Letzte Woche Vorbestellpreis", "Noch 6 Tage"],
     "So 23.05., 20:00. Danach 169 €.",
     """
Hey,

ich bin zurück, und die Jeans sind fast fertig. [FOTO: Serienware]

Der Vorbestellpreis von 149 € endet am So 23.05. um 20:00. Danach kostet sie 169 €.
Samstag, 15.05., war Mess-Abend 3 [oder: ist Mess-Abend 3, wenn die Mail vorher rausgeht].

Lieferung an Vorbesteller: Anfang Juni.

[BUTTON: Vorbestellen]""",
     "Mess-Abend-Satz an das Datum anpassen.")

mail("E12", "So 23.05., 12:00", "Segment „E-Mail-Abonnenten“ ohne Kauf",
     "Heute 20:00 endet der Vorbestellpreis", ["Letzte Stunden zu 149 €", "Heute Abend"],
     "Danach 169 €.",
     """
Hey,

nur kurz: Heute um 20:00 endet der Vorbestellpreis von 149 €. [Y] Paar sind noch übrig zu diesem Preis.

[BUTTON: Vorbestellen]""",
     "Nur senden, wenn noch Paare zu 149 € übrig sind.")

mail("E13", "Mo 24.05., 18:00", "Segment „E-Mail-Abonnenten“ ohne Kauf",
     "Bis So 06.06.: vorbestellen und Anfang Juni tragen", ["Noch zwei Wochen", "169 €, Lieferung Anfang Juni"],
     "Wer jetzt vorbestellt, hat die Jeans vor dem Drop.",
     """
Hey,

der Drop für alle ist am Do 24.06. um 19:00. Wer bis So 06.06. vorbestellt, bekommt die Jeans schon Anfang Juni, für 169 €.

[BUTTON: Vorbestellen]

Danach geht es erst am 24.06. weiter: um 18:00 für die Liste, um 19:00 für alle.""")

mail("E14", "Mi 26.05., 18:00", "nur Vorbesteller (Shopify → Kunden mit Bestellung)",
     "Deine Time Travel kommt Anfang Juni", ["Update zu deiner Bestellung", "Deine Nummer"],
     "Die Ware ist unterwegs. So geht es weiter.",
     """
Hey [Vorname],

kurzes Update zu deiner Vorbestellung: Die 100 Paar sind fertig und unterwegs zu mir. Ich prüfe jedes Paar selbst, dann packe ich.

Deine Nummer: [Nr.]
Deine Größe: [Größe]
Versand: zwischen 08. und 09.06. Du bekommst eine Versandbestätigung mit Sendungsnummer.

Ein Wunsch: Wenn sie da ist, schick mir ein Foto oder markier mich. Nur wenn du magst.

Danke, dass du vorbestellt hast. Ohne dich gäbe es diese 100 Paar nicht.""",
     "Pro Kunde Nummer und Größe richtig. Lieber in kleinen Gruppen senden als falsch.")

mail("E15", "Do 10.06., 18:00", "Segment „E-Mail-Abonnenten“",
     "In zwei Wochen: Drop", ["T−14", "24.06., 19:00"],
     "Die Liste ist um 18:00 drin.",
     """
Hey,

in zwei Wochen ist der Drop: Do 24.06., 19:00. Du bist um 18:00 drin, eine Stunde vor allen.

Die ersten Paare sind schon bei den Vorbestellern. [FOTO: Kunde mit Erlaubnis oder Paket]

Merk dir den Termin: [BUTTON: In den Kalender]""")

mail("E16", "Do 17.06., 18:00", "Segment „E-Mail-Abonnenten“",
     "Noch eine Woche", ["T−7", "Nächsten Donnerstag"],
     "Größen, Zeiten, alles Wichtige.",
     """
Hey,

nächsten Donnerstag, 24.06.:
· 18:00: Link für dich (Liste)
· 19:00: offen für alle
· Preis: 169 €
· Größen W30–W38, das Etikett ist die echte Bundweite

Zipper [Preis] €[, Polo 79 €, falls im Drop].

Unsicher bei der Größe? Antworte mit deiner Bundweite in cm.""")

mail("E17", "Mo 21.06., 18:00", "Segment „E-Mail-Abonnenten“",
     "Donnerstag, 18:00", ["T−3", "Noch drei Tage"],
     "Halt Donnerstag um 18:00 dein Postfach offen.",
     """
Hey,

Donnerstag um 18:00 bekommst du hier den Link, eine Stunde vor allen anderen.

[FOTO: Papiertest Oktober neben Serienware]
Im Oktober war das Papier auf meiner Jeans. Donnerstag ist es deine.""")

mail("E18", "Mi 23.06., 18:00", "Segment „E-Mail-Abonnenten“",
     "Morgen.", ["T−24 h", "Morgen 18:00"],
     "Der Link kommt morgen um 18:00.",
     """
Hey,

morgen um 18:00 kommt der Link. Miss heute Abend noch einmal deine Lieblingsjeans und leg dein Zahlungsmittel bereit.

Bis morgen.""")

mail("E19", "Do 24.06., 18:00 (terminiert)", "Segment „E-Mail-Abonnenten“ (Liste)",
     "Du bist drin.", ["Jetzt, für dich", "Eine Stunde vor allen"],
     "Time Travel ist offen. Für alle anderen um 19:00.",
     """
Hey,

jetzt. Eine Stunde vor allen anderen:

[BUTTON: Zum Drop → Schlüssel-Link]

100 Paar, nummeriert. Danke, dass du dabei bist.""",
     "Schlüssel-Link funktioniert nur für die Liste. Nicht in Stories posten.")

mail("E20", "Do 24.06., 19:00 (terminiert)", "Segment „E-Mail-Abonnenten“",
     "Time Travel ist live", ["Jetzt für alle offen", "Live"],
     "Noch [X] Paar.",
     """
Hey,

Time Travel ist jetzt für alle offen.

[BUTTON: Zum Shop]

Noch verfügbar: [Größen]. Fragen zur Größe beantworte ich heute Abend live auf Instagram.""",
     "Größen um 18:55 aus Shopify eintragen.")

mail("E21", "Fr 25.06., 10:00 (nur wenn Do 21:00 unter 15 Käufe)", "Abonnenten, die E19 und E20 nicht geöffnet haben",
     "Hast du es gestern gesehen?", ["Time Travel ist offen", "Noch da"],
     "Noch [X] Paar, diese Größen.",
     """
Hey,

gestern um 19:00 war der Drop. Falls du die Mail verpasst hast: Es gibt noch [X] Paar.

Verfügbare Größen: [Größen]

[BUTTON: Zum Shop]""")
