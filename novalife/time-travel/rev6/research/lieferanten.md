# Lieferanten · Time Travel (Rev. 6, Recherche)

Stand: Mi 07.10.2026, abends. Für: Ernest. Gehört zu Plan Rev. 5.3, Spec Rev. 13, Docket Rev. 5.3/Rev. 6.

---

## Kurzfassung

**Ehrlicher Stand: In dieser Sitzung konnte ich keine einzige Quelle öffnen.** WebFetch ist in dieser Cloud-Umgebung für jede Domain gesperrt (10 Domains getestet, Protokoll in Abschnitt 7). Das Suchbudget dieses Durchlaufs (200 Suchen, geteilt mit den anderen Recherche-Agenten) war schon aufgebraucht. Deshalb gibt es hier **keine neuen Fabriken, keine neuen Sticker, keine Preise, keine MOQs und keine Kontakte**. Namen aus dem Gedächtnis nenne ich nicht, weil ich weder Existenz noch Fähigkeit noch MOQ prüfen kann. Was unten zu den bekannten Betrieben steht, kommt aus Plan Rev. 5.3 und der alten Sitzung. Es ist überall als „nicht geprüft“ markiert.

**Was trotzdem fertig ist:**
1. Die bekannten Betriebe (4 Fabriken, 4 Berliner Sticker) mit dem, was der Plan über sie sagt, und den offenen Prüffragen.
2. Ein Punkteraster (max. 15) für die 8 Anfragen am Mo 12.10. Das K.-o.-Kriterium: eigene Fabrik mit Stickerei im Haus.
3. Eine 10-Minuten-Prüfliste pro Website.
4. Suchbegriffe auf Deutsch, Englisch, Türkisch und Portugiesisch.
5. Anforderungen und Suchwege für Patch D, Chenille, Etiketten, Hangtags, Knopf und Nieten, Blanks und Digitizer.
6. Ein fertiger Prompt für den Neustart (Abschnitt 5).

**Vorläufiges Ranking der vier bekannten Fabriken (nur aus dem Plan):** 1. Portugal Textile – Jeans Factory (EU, eigene Wäscherei laut Plan). 2. Istanbul Clothing Manufacturers (MOQ 100, 60/40, Stickerei ungeklärt). 3. White Cotton (MOQ ab 50, Plan B bei 75 Stück). 4. Brosan Textile (Vergleichsangebot). **Risiko bei 1 und 2:** Die Namen klingen nach Vermittler oder Sammelportal. Ist es keine eigene Fabrik, fällt das Pflichtkriterium „Stickerei im eigenen Haus“, bis die echte Fabrik genannt und geprüft ist.

**Mein Rat, damit der 12.10. hält:** Schalte den Netzwerkzugang frei (Abschnitt 0) und starte diese Aufgabe am Sa 10.10. neu, als einzige Recherche in der Runde. Geht das nicht, prüfst du am Sa 10.10. die vier Fabriken selbst mit der Prüfliste (40 Min.) und suchst vier weitere mit den Suchbegriffen (60 Min.). Die Anfrage am 12.10. geht an alle, die die Prüfliste bestehen, auch wenn es weniger als 8 sind. Nachzügler bekommen sie bis Mi 14.10. Die Calls am 21.–23.10. bleiben.

**Ein Vorschlag, du entscheidest:** Frag die Fabriken, ob sie Patch D selbst als Einzelteil auf Leinen sticken. Dann fallen ein Lieferant und die Frist 22.01. weg. Vorher Gegenrechnung: Stiche des Patches × Preis pro 1.000 Stiche gegen ~3 € Zukauf (Spec 3.8, Schätzung).

---

## 0 · Warum nichts geprüft ist und wie du es freischaltest

**Netzwerk.** Die Umgebung blockt jede Website. Du änderst das selbst: In der Titelleiste der Sitzung das Menü der Cloud-Umgebung öffnen → **Edit** → **Network access**. Entweder eine breitere Zugriffsstufe wählen oder die Domains unter **Allowed domains** eintragen, das Häkchen bei „Allow package managers“ drin lassen. Anleitung: https://code.claude.com/docs/en/cloud-environments#network-access (in dieser Sitzung aus der Umgebungsdoku gelesen).

**Welche Stufe:** Für die Suche nach **neuen** Fabriken reicht eine Liste nicht, weil die Domains vorher unbekannt sind. Stell für diese eine Recherche-Sitzung die breitere Stufe ein und danach zurück. Für die bekannten Betriebe allein reichen diese Domains:

```
istanbulclothingmanufacturers.com
portugaltextile.com
brosantextile.com
whitecotton.pt
berlin-stick.de
stickerei-druck-berlin.de
machdeinsdraus.de
berlintextil.de
stanleystella.com
```

**Suchbudget.** Die 200 Suchen gelten pro Runde und werden von allen Agenten der Runde geteilt. Lass die Lieferanten-Recherche deshalb **allein** laufen, nicht zusammen mit Markt, Content und Berlin. Alternativ die Grenze `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` erhöhen.

---

## 1 · Jeansfabriken Türkei und Portugal

### 1.1 Was die Fabrik können muss (aus Plan und Spec, nicht verhandelbar)

| # | Kriterium | Warum | Quelle |
|---|---|---|---|
| 1 | **Denim und Panel-Stickerei im eigenen Haus**, nachgewiesen mit Fotos einer früheren Produktion | Große Stickerei passt nicht in den Rahmen eines geschlossenen Hosenbeins. Wird extern gestickt, wandern die Zuschnitte zwischen zwei Betrieben | Plan 2, Plan 7 |
| 2 | Einzug-Kompensation im Schnitt | Rigider 12-oz-Denim zieht sich unter ~33.000 Stichen zusammen | Plan 2, Spec 3.11 |
| 3 | Eigene Wäscherei, Laser | Fünf Freihaltezonen sind von Hand nicht wiederholbar | Spec 2.3, 2.4 |
| 4 | MOQ ≤ 100 pro Style und Colorway, ideal auch 75 | Schwelle 01.02.: knapp → 75 Stück | Plan 2, Plan 6 |
| 5 | Proto bis 30.11., PP bis 04.01. | Proto am 03.12. in deiner Hand | Plan 5, Vorlage RFQ |
| 6 | Saum nach der Wäsche auf Länge, 9 Goldfäden von Hand nach der Wäsche | Spec 2.6, 3.7, RFQ-Fragen 13 und 14 | Spec |
| 7 | 50/50, DDP Berlin | Cash-Plan 3.1 | Plan 3.1, Vorlage Verhandlung |

### 1.2 Die vier bekannten Fabriken

**Keine Zeile in dieser Tabelle ist in dieser Sitzung geprüft.** Die Websites konnte ich nicht öffnen. Die Angaben stammen aus Plan Rev. 5.3 und der Docket-Referenz „Fabriken“, dort selbst schon als „Angaben aus öffentlichen Quellen, nicht geprüft“ markiert.

| Fabrik | Land / Stadt | Website (aus Plan) | Kontaktweg | Was der Plan sagt | MOQ | Stickerei / Wäscherei / Laser | Risiken | Status |
|---|---|---|---|---|---|---|---|---|
| **Istanbul Clothing Manufacturers** | TR / Stadt prüfen (Name deutet auf Istanbul) | istanbulclothingmanufacturers.com | Kontaktseite auf der Website, URL prüfen | MOQ 100 pro Modell, Sample 7–10 Tage, Produktion 4–5 Wochen bei Lagerstoff, Zahlung 60/40 | 100 pro Modell (nicht geprüft) | Stickerei im Haus **ungeklärt** · Wäscherei und Laser unbekannt | Name klingt nach Vermittler oder Marketing-Seite: eigene Fabrik prüfen · 60/40 statt 50/50 · Türkei: ~1.150 € Einfuhrumsatzsteuer, wenn du Kleinunternehmer bist (Plan 3.1) · Ramadan-Fest 08.–11.03. | nicht geprüft |
| **Portugal Textile – Jeans Factory** | PT / Stadt prüfen | portugaltextile.com | Kontaktseite auf der Website, URL prüfen | Denim mit eigener Wäscherei, Tech-Pack-Unterstützung, 20-Punkte-QC. Teurer als die Türkei | unbekannt | Wäscherei laut Plan ja · Stickerei und Laser unbekannt | Name klingt nach Portal: Ist „Jeans Factory“ ein eigener Betrieb oder ein Partner? Impressum und Adresse prüfen · Preis höher | nicht geprüft |
| **Brosan Textile** | TR / Stadt prüfen | brosantextile.com | Kontaktseite auf der Website, URL prüfen | Denim- und Jeanshersteller. Als Vergleich, ob dein Preis marktgerecht ist | unbekannt | alles unbekannt | Wie bei allen in TR: Einfuhrumsatzsteuer, A.TR, EORI | nicht geprüft |
| **White Cotton** | PT / Stadt prüfen | whitecotton.pt | Kontaktseite auf der Website, URL prüfen | MOQ ab 50. Rückfallebene, falls die Schwelle nur 75 Stück erlaubt | ab 50 (nicht geprüft) | alles unbekannt, auch ob Denim Kernprodukt ist | Wenn kein Denim-Spezialist: Waschung und Laser extern | nicht geprüft |

**Pro Fabrik zuerst klären (Reihenfolge):** 1. Eigene Fabrik oder Vermittler? 2. Denim als Kernprodukt? 3. Stickerei im Haus, auf dem Zuschnitt? 4. Wäscherei und Laser im Haus? 5. MOQ pro Style? 6. Offizieller Kontaktweg (Formular-URL oder E-Mail genau so, wie sie auf der Seite steht).

### 1.3 Weitere Kandidaten (Auftrag: 8–10)

**Gefunden: 0.** Ohne Web-Zugang habe ich nicht gesucht und nenne keine Namen aus dem Gedächtnis. Die Tabelle ist zum Ausfüllen. Sie hat dieselben Spalten wie das Blatt „Fabriken“ plus Quelle.

| # | Fabrik | Land / Stadt | Website | Kontaktweg (URL) | Beleg Stickerei (Zitat + URL) | Beleg Wäscherei / Laser | MOQ (Zitat + URL) | Eigene Fabrik? | Punkte (1.6) | Risiken |
|---|---|---|---|---|---|---|---|---|---|---|
| K5 | | | | | | | | | | |
| K6 | | | | | | | | | | |
| K7 | | | | | | | | | | |
| K8 | | | | | | | | | | |
| K9 | | | | | | | | | | |
| K10 | | | | | | | | | | |
| K11 | | | | | | | | | | |
| K12 | | | | | | | | | | |
| K13 | | | | | | | | | | |
| K14 | | | | | | | | | | |

### 1.4 So findest du sie (Suchbegriffe)

Google, dann Google Maps für das Gebäude. **Kontakt nur von der eigenen Website** oder vom Firmenprofil, das die Website selbst verlinkt. **Keine B2B-Verzeichnisse, keine Lead- oder Scraper-Datenbanken**, auch nicht zum Namenfinden.

| Sprache | Suchbegriff | Wofür |
|---|---|---|
| Englisch | `denim manufacturer Portugal embroidery in-house low MOQ` | PT, Stickerei im Haus |
| Englisch | `jeans factory Portugal laundry laser embroidery small quantities` | PT, Wäscherei |
| Englisch | `denim garment manufacturer Turkey embroidery laser washing small MOQ` | TR |
| Englisch | `private label jeans manufacturer Istanbul embroidery` | TR, Istanbul |
| Türkisch | `kot pantolon fason üretim nakış` | Lohnfertigung Jeans mit Stickerei |
| Türkisch | `nakışlı kot imalatı yıkama lazer` | bestickte Jeans, Wäscherei, Laser |
| Portugiesisch | `fábrica de calças de ganga bordados` | Jeansfabrik mit Stickerei |
| Portugiesisch | `confeção ganga pequenas quantidades lavandaria` | kleine Mengen, Wäscherei |
| Deutsch | `Jeans produzieren lassen Portugal kleine Mengen` | Gründer-Erfahrungen, Namen |

**Weitere offizielle Wege (Vorwissen, in dieser Sitzung nicht geprüft):** Ausstellerlisten der Denim-Messen (Kingpins, Denim Première Vision, Modtissimo in Porto) und die Mitgliederverzeichnisse der Branchenverbände (Portugal: ATP; Türkei: İTKİB). Dort nur Namen holen, den Kontakt danach von der Firmen-Website.

### 1.5 Prüfliste pro Website (10 Minuten)

1. **Impressum oder „Legal“:** Firmenname, Adresse, Steuernummer (PT: NIF, TR: Vergi No). Fehlt das, Minuspunkt.
2. **Adresse in Google Maps:** Street View oder Satellit. Ist da ein Betriebsgebäude oder ein Büro?
3. **„About“:** Steht da „our factory“, Fläche, Zahl der Mitarbeiter? Sätze wie „our partner factories“, „we source“, „network of manufacturers“ heißen Vermittler.
4. **Produktion:** Fotos von Stickmaschinen (mehrere Köpfe nebeneinander), Industriewaschmaschinen, Laser. Ein Foto mit Google Lens rückwärts suchen. Taucht es auf fremden Seiten auf, ist es ein Stockfoto.
5. **Arbeiten:** Fotos von echter Stickerei auf Denim, am besten auf einem flachen Zuschnitt.
6. **Zahlen:** MOQ, Musterzeit, Zahlung. Den Satz wörtlich kopieren, URL daneben.
7. **Kontakt:** URL des Formulars oder die E-Mail genau so, wie sie auf der Seite steht.
8. **Lebenszeichen:** Instagram oder LinkedIn, von der Website verlinkt, Beitrag in den letzten 3 Monaten?
9. **Punkte** nach 1.6 vergeben, alles ins Blatt „Fabriken“, Spalten „Quelle“ und „geprüft am“.

**Vermittler sind kein Ausschluss für immer, aber für die erste Runde.** Antwortet ein Vermittler, fragst du nach dem Namen der Fabrik und nach Fotos der Panel-Stickerei dort. Ohne das kein Call.

### 1.6 Punkteraster für die 8 Anfragen am 12.10.

**K.-o. (alle drei müssen ja sein):** eigene Fabrik belegt · Jeans/Denim ist Kernprodukt · Kontaktweg steht auf der eigenen Website.

| Kriterium | Punkte |
|---|---|
| Stickerei im Haus: nur im Text 2 · mit Fotos der Maschinen 3 | 0–3 |
| Stickerei auf dem Zuschnitt (Panel) erwähnt oder gezeigt | 0 / 2 |
| Fotos von Stickerei auf Denim | 0 / 2 |
| Wäscherei im Haus | 0 / 2 |
| Laser im Haus | 0 / 1 |
| MOQ öffentlich: ≤ 150 → 1 · ≤ 100 → 2 | 0–2 |
| Arbeitet sichtbar mit kleinen Marken (Text, Tech-Pack-Hilfe, Referenzen) | 0 / 1 |
| Impressum vollständig (Firmenname, Adresse, Steuernummer) | 0 / 1 |
| Website auf Englisch oder Deutsch, klare Ansprechperson oder Formular | 0 / 1 |
| **Summe** | **max. 15** |

**Regel:** Nach Punkten sortieren, die besten 8 anfragen, davon **je mindestens 3 aus TR und aus PT**, bis der Steuerstatus am Di 13.10. klar ist. Bei Gleichstand PT vor TR (keine Einfuhrumsatzsteuer, Plan 3.1). MOQ ≤ 75 in den Notizen markieren, das ist dein Plan B für die Schwelle 01.02.

### 1.7 Vorläufiges Ranking für den 12.10.

| Platz | Fabrik | Begründung | Vorbehalt |
|---|---|---|---|
| 1 | Portugal Textile – Jeans Factory | EU, eigene Wäscherei und Tech-Pack-Hilfe laut Plan | eigene Fabrik? Stickerei im Haus? |
| 2 | Istanbul Clothing Manufacturers | MOQ 100 und Zeiten laut Plan öffentlich genannt | Vermittler? Stickerei ungeklärt, 60/40 |
| 3 | White Cotton | MOQ ab 50, Plan B für 75 Stück | Denim-Spezialist? |
| 4 | Brosan Textile | Preisvergleich TR | keine Fähigkeiten bekannt |
| 5–8 | die vier besten aus 1.3 nach Punkten | — | erst nach der Suche |

Fällt eine der vier bei der Prüfliste durch (K.-o.), rückt der nächste Kandidat aus 1.3 nach.

---

## 2 · Berliner Sticker für Zipper und Polo (MOQ 1)

### 2.1 Was der Sticker können muss

| Punkt | Anforderung | Quelle |
|---|---|---|
| Menge | ab 1 Stück, auf Bestellung | Plan 4, Spec 3C |
| Zipper | Fleece 330–350 g/m², **mit Topping** (wasserlösliche Folie) und Cut-away. Zwei Bänder 25 mm × ca. 25 cm, ~16.000 Stiche (Schätzung) | Spec 3C.1 |
| Zipper-Rücken | Medaillon ca. 200 × 150 mm, falls gestickt statt Chenille (Entscheidung 19.12.). Dafür braucht er einen großen Rahmen | Plan 4.2 |
| Polo | Piqué, Tear-away oder leichtes Cut-away. Zwei Bänder 20 mm × ca. 12 cm, ~8.000 Stiche (Schätzung) | Spec 3C.3 |
| Dateien | nimmt fremde DST/EMB an, oder digitalisiert selbst | Vorlage „Anfrage Berliner Sticker“ |
| Preis und Zeit | Preis bei 1 / 10 / 50 Stück, Lieferzeit pro Auftrag, Musterteil | Vorlage |
| Termine | 3 Anfragen Mi 14.10., 2 Musterteile (Budget 180 €), Wahl Do 17.12. | Plan 7 |

### 2.2 Die vier bekannten

**Nicht geprüft.** Namen und Domains stehen so im Auftrag und in `berlin.md`, Abschnitt 6. Die Websites waren in dieser Sitzung nicht erreichbar.

| Betrieb | Website | Adresse / Bezirk | Kontaktweg | MOQ 1? | Fleece mit Topping? | Piqué? | DST/EMB von außen? | Status |
|---|---|---|---|---|---|---|---|---|
| Berlin Stick | berlin-stick.de | prüfen | Kontaktseite prüfen | prüfen | prüfen | prüfen | prüfen | nicht geprüft |
| Stickerei & Druck Berlin | stickerei-druck-berlin.de | prüfen | Kontaktseite prüfen | prüfen | prüfen | prüfen | prüfen | nicht geprüft |
| Mach Deins Draus | machdeinsdraus.de | prüfen | Kontaktseite prüfen | prüfen | prüfen | prüfen | prüfen | nicht geprüft |
| Berlin Textil | berlintextil.de | prüfen | Kontaktseite prüfen | prüfen | prüfen | prüfen | prüfen | nicht geprüft |

### 2.3 Weitere Berliner Sticker

**Gefunden: 0.** So suchst du (30 Min., spätestens Di 13.10. abends, damit die Anfrage am 14.10. an die 3 besten geht):

1. Google Maps: `Stickerei Berlin`, `Textilveredelung Berlin`, `Embroidery Berlin`, `Hoodie besticken lassen Berlin`, `Stickerei Kreuzberg`, `Stickerei Neukölln`, `Stickerei Wedding`.
2. Nur Betriebe mit **eigener Website und Fotos echter Stickerei**, am besten auf Hoodie und Polo.
3. Auf der Website suchen: „ab 1 Stück“, Einrichtungs- oder Digitalisierungskosten, „eigene Stickdatei“ oder „DST“.
4. Ins Blatt „Sticker“: Name, Website, Bezirk, Kontaktweg (URL), Fotos von Fleece ja/nein, Piqué ja/nein.

**Worauf du achtest:** Bei Stückzahl 1 entscheiden die Einrichtungskosten über den Preis, nicht die Stiche. Deshalb fragt die Vorlage nach dem Preis bei 1, 10 und 50.

---

## 3 · Zulieferer

### 3.1 Label-Patch D (Lebensbaum, 86 × 76 mm)

| Anforderung | Wert | Quelle |
|---|---|---|
| Größe, Form | 86 × 76 mm, oben leichter Bogen, unten mittige Lasche | Spec 3.8 |
| Grund | Naturleinen, **vorgewaschen**, Kante umgeschlagen und gesteppt | Spec 3.8, Docket W9 |
| Stickerei | Gold, Ocker, drei Brauntöne, Rot. Linien mind. 0,8 mm, Einrollungen mind. 2,5 mm | Spec 3.8 |
| Belastung | wird angenäht, dann Enzym-/Steinwäsche der ganzen Jeans | Spec 2.3 |
| Menge | 3 Muster, dann 110 Stück (100 + 10 Reserve) | Plan 7 |
| Termine | Anfrage Mi 28.10. · Muster Fr 13.11. · Waschtest 3× 60 °C Do 26.11. · Bestellung Do 17.12. · **direkt an die Fabrik bis Fr 22.01.** | Plan 7 |
| Budget | Muster 80 € · Serie ~330 € (Schätzung ~2,50–3,50 € je Stück) | Plan 3, Spec 3.8 |

**Kandidaten geprüft: 0.**

**Suchbegriffe:** `Aufnäher sticken lassen ab 50 Stück` · `gestickte Patches Kleinauflage` · `Stickabzeichen Hersteller Deutschland` · `custom embroidered patches low minimum Europe` · `embroidered patch manufacturer Portugal`.

**Prüfkriterien:** Nahaufnahmen von fein gestickten Mehrton-Patches auf der eigenen Website (nicht nur Logos in zwei Farben). Gestickt auf Leinen oder Canvas möglich? Eigene Produktion oder Import? Musterpreis und Musterzeit.

**Klären vor der Anfrage am 28.10.:** Spec 3.8 nennt „vier Kupfernieten in den Ecken“. Sind das gestickte Nieten oder echte Metallnieten? Echte Nieten macht kein Patch-Sticker, das wäre ein zweiter Arbeitsschritt.

**Vorschlag, du entscheidest:** Die Jeansfabrik hat Stickmaschinen im Haus. Frag in den Calls am 21.–23.10., ob sie D als Einzelpatch auf Leinen stickt. Vorteil: kein zweiter Lieferant, keine Frist 22.01., Waschverhalten aus einer Hand. Gegenrechnung: Stichzahl des Patches (vom Digitizer) × Preis pro 1.000 Stiche + Leinen + Kante gegen ~3 € Zukauf.

### 3.2 Chenille-Patch (Zipper-Rücken, nur falls am 19.12. gewählt)

| Anforderung | Wert | Quelle |
|---|---|---|
| Größe | ca. 200 × 150 mm | Spec 3C.2 |
| Aufbau | Chenille-Flor auf Filz oder Twill, Kante umstochen (merrowed) oder eingefasst | Spec 3C.2 |
| Farben | Bordeaux, Beige, Schwarz, Gold | Spec 3C.2 |
| Befestigung | **aufgenäht, nicht aufgebügelt** | Spec 3C.2 |
| MOQ | **≤ 20 ideal.** Darüber bindet der Patch 300–600 € vor dem Drop | Plan 2, Plan 4.2 |
| Budget | Muster 120 € (nur falls gewählt) | Plan 3 |

**Kandidaten geprüft: 0.** Suchbegriffe: `Chenille Aufnäher Kleinauflage` · `custom chenille patches low minimum EU`. **Hinweis (Vorwissen, nicht geprüft):** Chenille braucht eigene Maschinen, ein normaler Sticker macht das meist nicht. Viele „ohne Mindestmenge“-Angebote im Netz werden außerhalb der EU gefertigt. Dann kommen Lieferzeit, Zoll und Einfuhrumsatzsteuer dazu. **Plan-Empfehlung bleibt: gestickt in Berlin.**

### 3.3 Gewebte Etiketten

| Etikett | Wo | Anforderung | Quelle |
|---|---|---|---|
| Hauptlabel | Bund hinten | gewebt | Spec 2.8 |
| Größenlabel | Bund | „W32“ = gemessener Bund | Spec 1.2 |
| Pflegelabel | Seitennaht | **EU-Pflicht: Faserzusammensetzung** („100 % Baumwolle“). Dazu „Auf links waschen, Fäden nicht abschneiden“ | Plan 7 Rechtliches, Spec 3.7 |
| Nackenlabel Zipper und Polo | Nacken innen | gewebt, vereinfachter Baum. **Offen, Entscheidung Do 08.10.** | Übergabe 4 |

**Weg 1 (Empfehlung):** Die Jeansfabrik liefert Haupt-, Größen- und Pflegelabel mit (RFQ-Frage 15). Du gibst nur Dateien und Freigabe.
**Weg 2:** Eigener Label-Hersteller, vor allem für die Nackenlabels von Zipper und Polo. Suchbegriffe: `Webetiketten Kleinauflage` · `gewebte Etiketten ab 50 Stück` · `woven labels low minimum EU`. Mindestmenge laut Docket „meist 50–100 Stück“ (nicht geprüft). Vorher den Berliner Sticker fragen, ob er die Labels beim Besticken einnäht.

**Kandidaten geprüft: 0.**

### 3.4 Hangtags

| Anforderung | Wert | Quelle |
|---|---|---|
| Material | Recyclingkarton 300 g/m² | Spec 2.8 |
| Nummer | 001–100, beim Packen: erst Vorbestellungen nach Datum, dann Creator, dann Drop | Spec 2.8, Plan 13 (01.10.) |
| Wer bringt sie an | Novalife selbst | Plan 13 (01.10.) |
| Budget | in „Verpackung inkl. Hangtags“ 240 € | Plan 3 |

**Wege (Vorwissen, nicht geprüft):** Deutsche Online-Druckereien wie flyeralarm, WIRmachenDRUCK oder Saxoprint. Dort prüfen: Gibt es „Anhänger“ oder „Hangtags“ in 300 g/m² Recyclingkarton, mit Loch, und eine Nummerierung als Option? Ohne Nummerierung druckst du 100 gleiche Tags und nummerierst mit Stempel oder Stift. Das passt zur Handarbeit der Goldfäden.

### 3.5 Knopf und Nieten

| Teil | Spec | Quelle |
|---|---|---|
| Knopf | Shank Button 17 mm, Antik-Messing, „NOVALIFE“ | Spec 2.8 |
| Nieten | 9 mm, Antik-Messing, 6 Stück | Spec 2.8 |
| Reißverschluss | YKK 4,5 Metall, Antik-Messing | Spec 2.8 |
| Budget Setup | in „Labels, Hangtags, Knopf-Gravur (Setup)“ 150 € | Plan 3 |

**Empfehlung:** Knopf und Nieten **über die Jeansfabrik** (RFQ-Frage 15). Dann liegt das Zubehör schon dort, wo genäht wird, und du verschickst nichts. Frag nach Werkzeugkosten, MOQ, Muster und ob das Logo geprägt oder graviert wird.
**Weg 2 (Vorwissen, nicht geprüft):** EU-Hersteller von Jeans-Zubehör, z. B. Prym in Deutschland. Bei 100 Hosen ist die Mindestmenge dort vermutlich zu hoch (Schätzung). Nur anfragen, wenn die Fabrik es nicht kann.

**Kandidaten geprüft: 0.**

### 3.6 Blanks für Zipper und Polo

| Anforderung | Wert | Quelle |
|---|---|---|
| Zipper | Zip-Hoodie, Fleece **330–350 g/m²**, ~28 € (Schätzung) | Spec 3C.1 |
| Polo | Piqué-Polo, ~12 € (Schätzung) | Spec 3C.3 |
| Farbe | Navy (Docket-Empfehlung, Woche 6) | Docket W6 |
| Muster | je 1 Stück in deiner Größe, Woche 6, danach zum Berliner Sticker | Docket W6 |
| Serie | erst nach bezahlter Bestellung, So 25.04. für die ersten 72 Stunden | Plan 3.2 |

| Marke | Was ich weiß (Vorwissen, **nicht geprüft**) | Was du prüfst |
|---|---|---|
| Stanley/Stella | belgische Marke für Blanks, verkauft B2B an Veredler | Zip-Hoodie mit 330–350 g/m²? Piqué-Polo? Kauf direkt oder nur über Händler? Händler in DE? |
| AS Colour (Europa) | Blanks-Marke aus Neuseeland mit Europa-Geschäft | offizielle Europa-Domain (ascolour.eu war gesperrt, Existenz nicht geprüft) · Konto für Gewerbe? Versand nach DE? Lager in der EU? |
| Continental / EarthPositive | britischer Blanks-Anbieter, EarthPositive ist eine Linie davon | Seit dem Brexit: Lieferung aus UK = Zoll und Einfuhrumsatzsteuer? Oder EU-Händler? |
| Neutral | dänische Marke für Blanks | Zip-Hoodie und Polo im Sortiment? Händler in DE? |
| Großhändler in DE | z. B. L-Shop-Team (Unna), führt mehrere Blanks-Marken | Gewerbenachweis nötig? Mindestbestellwert? Einzelstück möglich? |

**Großhandelszugang:** Rechne damit, dass ein Gewerbenachweis verlangt wird (Schätzung). Den hast du über Novalife. Mindestbestellwert und Versandkosten bei Einzelstücken prüfen, weil du auf Bestellung kaufst.

**Kandidaten geprüft: 0.**

---

## 4 · Digitizer als Backup

**Wann du einen brauchst:** wenn die Fabrik nicht selbst digitalisiert, wenn die Vorschau am Mo 09.11. nicht trägt, oder wenn der Berliner Sticker die Zipper- und Polo-Bänder nicht digitalisiert. Budget: Jeans 320 €, Zipper/Polo/Medaillon 240 € (Plan 3).

| Anforderung | Wert | Quelle |
|---|---|---|
| Dateien | **DST** (für die Maschine) + **EMB** oder anderes Quellformat (zum Ändern) + PDF mit Stichzahl, Farbfolge, Maßen | Vorschlag |
| Vorlage | Druckvorlagen 1:1: v17 (B2, B), v15 S. 1 (A, E), 1zu1 S. 3 (C, D) | Übergabe 3 |
| Kreuzstich | A, C, E im 1,33-mm-Raster: A 17 Stiche hoch, C 27 × 27, E 45 × 45. Echter Kreuzstich oder feine Füllung, Entscheidung am Stitch-out | Spec 3.5, 3.6 |
| Satin | Halme von B 1,1–1,3 mm, Band B2 3 mm | Spec 3.6 |
| Stoff | 12 oz rigider Denim, Zuschnitt, Cut-away mittel | Spec 2.7, 2.8 |
| Kompensation | Pull-Kompensation im Programm, Einzug wird im Schnitt ausgeglichen | Plan 2 |
| Rechte | Du bekommst alle Dateien und darfst sie bei jedem Sticker nutzen | Vorschlag |

**Kandidaten geprüft: 0.**

**Wege:** 1. Die Berliner Sticker fragen (viele digitalisieren selbst). 2. Suchbegriffe: `Punchservice Stickdatei` · `Stickdatei erstellen lassen DST` · `embroidery digitizing cross stitch`. 3. Freelancer-Plattformen (z. B. Fiverr, Upwork): nur mit Portfolio, das echten Kreuzstich zeigt, und mit Bewertungen.

**Testauftrag (Vorschlag):** Element C (Alatyr, 36 × 36 mm, 27 × 27) bei zwei Digitizern bezahlt digitalisieren lassen. Beide Dateien beim Berliner Sticker auf ein Stück Denim sticken, waschen und neben Ernests Referenzfotos legen. Der Bessere bekommt den Rest.

---

## 5 · Prompt für den Neustart (sobald das Netz frei ist)

> Lies `rev6/research/lieferanten.md`. Prüfe mit WebSearch und WebFetch die vier bekannten Fabriken und die vier Berliner Sticker auf ihren offiziellen Websites nach der Prüfliste 1.5. Suche dann mit den Suchbegriffen aus 1.4 acht bis zehn weitere Jeansfabriken in der Türkei und in Portugal, die Denim und Stickerei auf dem Zuschnitt im eigenen Haus können, MOQ 50–150. Danach je drei Kandidaten für Patch D, Chenille, gewebte Etiketten, Blanks-Händler in DE und Digitizer. Für jede Angabe die URL der Seite, auf der sie steht, und das Zitat. Kontakt nur von der eigenen Website, keine Verzeichnisse, keine E-Mail erfinden. Vergib Punkte nach 1.6 und schreib das Ranking für die 8 Anfragen am 12.10. Ergänze die Tabellen in dieser Datei, lösch nichts.

---

## 6 · Spalten für das Blatt „Fabriken“

Wie im Docket (Name, Land, Website, E-Mail, gesendet, Antwort, Stickerei im Haus, Panel-Stickerei, MOQ, Preis Basis, Preis pro 1.000 Stiche, Sample-Preis, Zahlung, Lieferzeit, Notizen), **dazu neu:**

| Spalte | Inhalt |
|---|---|
| Kontaktweg | Formular-URL oder E-Mail, genau so wie auf der Website |
| Quelle | URL der Seite, auf der die Angabe steht |
| geprüft am | Datum |
| Eigene Fabrik | ja / Vermittler / unklar |
| Punkte | nach 1.6 |
| MOQ ≤ 75 | ja / nein (Plan B für die Schwelle) |

---

## 7 · Protokoll dieser Sitzung

| Werkzeug | Ziel | Ergebnis |
|---|---|---|
| WebFetch | istanbulclothingmanufacturers.com | gesperrt (Netzwerk-Regel) |
| WebFetch | portugaltextile.com | gesperrt |
| WebFetch | brosantextile.com | gesperrt |
| WebFetch | whitecotton.pt | gesperrt |
| WebFetch | www.stanleystella.com | gesperrt |
| WebFetch | www.ascolour.eu | gesperrt |
| WebFetch | berlin-stick.de | gesperrt |
| WebFetch | www.lshop.de | gesperrt |
| WebFetch | www.atp.pt | gesperrt |
| WebFetch | en.wikipedia.org | gesperrt |
| WebSearch | „Istanbul Clothing Manufacturers jeans embroidery MOQ“ | nicht ausgeführt, Suchbudget der Runde aufgebraucht |

**Geprüfte Quellen im Netz: 0.** Benutzt wurden nur die Projektdateien: `docs/uebergabe-time-travel.md`, `docs/time-travel-drop-plan.md`, `docs/produkt-spec_rev13.md`, `r5/weeks_r5.json`, `rev6/build/r5_ref_fabriken.html`, `rev6/build/r5_ref_vorlagen.html`, `rev6/research/berlin.md`.

---

## 8 · Offen

| # | Punkt | Bis wann | Wer |
|---|---|---|---|
| 1 | Netzwerkzugang freischalten, Recherche allein neu starten (Prompt in 5) | Sa 10.10. | Ernest (5 Min.), dann Claude |
| 2 | Die vier Fabriken: eigene Fabrik oder Vermittler, Stickerei im Haus, Kontaktweg | Sa 10.10. | Claude oder Ernest mit Prüfliste 1.5 |
| 3 | 8–10 weitere Fabriken finden und nach 1.6 bewerten | So 11.10. | Claude |
| 4 | Vier Berliner Sticker prüfen, weitere finden | Di 13.10. | Claude oder Ernest |
| 5 | Patch D: „vier Kupfernieten“ gestickt oder echt? | vor Mi 28.10. | Ernest |
| 6 | Patch D bei der Fabrik sticken lassen? Gegenrechnung | Calls 21.–23.10. | Ernest entscheidet |
| 7 | Patch-, Chenille-, Etiketten-, Hangtag-Anbieter finden | Mi 28.10. | Claude |
| 8 | Blanks: Grammatur, Händler in DE, Gewerbezugang, Preise ~28 € / ~12 € prüfen | Woche 6 (19.–25.10.) | Claude |
| 9 | Digitizer-Backup: zwei Kandidaten, Testauftrag Element C | vor Mo 09.11. | Claude, dann Ernest |
| 10 | Steuerstatus entscheidet die Gewichtung TR gegen PT | Di 13.10. | Ernest mit Steuerberater |
