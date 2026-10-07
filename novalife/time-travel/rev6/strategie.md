# Master-Strategie Rev. 6.1 · Time Travel

Stand: Mi 07.10.2026, abends, Rev. 6.1 nach der Kritik vom selben Abend (Änderungen in Abschnitt 15.1, Abweichungen in Abschnitt 20). Für Ernest. Grundlage für den neuen Docket (Rev. 6).
Drop **Do 22.04.2027, 19:00** (Liste ab 18:00). Ziel **10.000 € = 64 Jeans netto** (35 Vorbestellungen à 149 € + 29 im Drop à 169 € = 10.116 €). Zipper (139 €) und Polo (79 €) sind Zusatzumsatz.
Tagesplan dazu: `rev6/skeleton.json` (Wochen 4–32, jeder Tag vom 08.10.2026 bis 25.04.2027).

**So liest du die Marker.**
- `[P]` Plan Rev. 5.3 · `[S]` Spec Rev. 13 · `[Ü]` Übergabe 07.10. · `[R5]` Docket Rev. 5.3 (`r5/weeks_r5.json`)
- `[M-Qxx]` Quelle aus `research/markt.md` · `[Z-Qxx]` aus `zielgruppe.md` · `[B-xx]` aus `berlin.md` · `[C]` `community.md` · `[K]` `content.md` · `[W]` `website.md` · `[T]` `tools.md` · `[L]` `lieferanten.md` · `[D]` `design.md`
- `[R]` eigene Rechnung, Weg steht dabei · **Schätzung** = Annahme · **vor Ort prüfen** = Adresse, Zeit oder Preis selbst nachsehen · **ungeprüft** = Fachwissen ohne Quelle
- Die Entwürfe heißen hier **Wachstum**, **Cash** und **Marke** (`rev6/strategie_entwurf_*.md`).

**Quellenlage, ehrlich.** Ich konnte heute selbst keine Seite neu prüfen. Mein Websuche-Versuch am 07.10. meldete „web search budget is used up“, und WebFetch auf berlin.de war vom Netzwerk-Proxy gesperrt. Bei der Überarbeitung (Rev. 6.1) dasselbe: WebSearch meldete wieder „budget is used up“, WebFetch auf gesetze-im-internet.de „EGRESS_BLOCKED“. Alle externen Zahlen kommen aus den Recherche-Dateien. Deren Agenten haben die Quellen heute in dieser Sitzung per Websuche gesehen, meist als Such-Auszug. Die URLs stehen in Abschnitt 18. Kalenderdaten (Wochentage, Ostern 2027, Sommerzeit, 4. Samstag im November, Ramadan 2027 nach dem tabellarischen Islam-Kalender) habe ich lokal nachgerechnet. **Alles Externe, das in Rev. 6.1 neu dazukam, ist als „ungeprüft“ markiert** (Gesetze, Feiertage, Mindestlohn, REACH). **Bevor du eine dieser Regeln umsetzt,** schaltest du das Netz frei (`lieferanten.md` Abschnitt 0, Docket Sa 10.10.). Dann prüft Claude die Liste in Abschnitt 19 gegen die Primärquelle. **Vor jeder Ausgabe** öffnest du die genannte Seite selbst.

---

## 0 · Auf einer Seite

**Die Lage.** Dein Plan Rev. 5.3 trägt im mittleren Fall. Im vorsichtigen Fall endet er bei Break-even, und mit der wahrscheinlichen Einfuhrsteuer reicht das Kontingent von 35 Vorbestellungen nicht für die Restzahlung. Der Engpass ist nicht das Design und nicht der Preis. Es fehlen Reichweite für die Liste und Wärme für die Kaufquote, und das Geld muss vor den Zahlungsterminen da sein.

**Rev. 6 in fünf Sätzen.**
1. Eine **Content-Maschine** mit Hook-Tests und der Varianten-Regel macht Ausreißer-Videos wahrscheinlicher. Nur sie bringen die Liste auf ~3.000.
2. Eine **Wärme-Kette** aus warmem Netz, Papiertest-Abend, Stick-Abend, Proto-Runde, Creator-Preview und drei Mess-Abenden macht aus Adressen Käufer.
3. Eine **Zusagen-Liste „Die ersten 35“** (nur echte Zusagen zählen, „Vielleicht“ steht in einer eigenen Spalte) und eine kostenlose Liste **„Platz in der ersten Stunde sichern“** tragen die Schwelle von 10 Vorbestellungen am 01.02., ohne Zufall.
4. **Kassendisziplin:** zuerst Steuer, Fabrikpreis und Auszahlung klären, Geld nur in Stufen freigeben, **Stufe 2 zu 169 €** statt „Kontingent 45 zu 149 €“ (live, sobald Nr. 035 verkauft ist), Mengenformel 100/75 am 01.02., zwei getrennte Geldtermine: Restzahlung (32 bis Di 16.03.) und Einfuhrsteuer (40 bis Mi 24.03.).
5. **Symbol- und Sprachhygiene:** Wortliste nach außen, Serp-Test vor dem Digitizing, Sperrtermine 23.–29.11. und 24.02., Teilsperre am 22.04.

**Diese Woche (Docket W4, kritischer Pfad, 125–135 Min. Kern pro Tag):**
- **Do 08.10.:** Papiertest 3 mit Varianten-Blatt, Clips filmen, 8 Wash-Fotos der Eightyfive bei Tageslicht, Schnelltest an 10 Leute, Steuertermin buchen.
- **Fr 09.10.:** 12:00 Auswertung, Freeze, Tech Pack bestellen (mit Verschleißkarte), Startseite als Warteliste mit Willkommens-Mail und 15′-Checkliste vor dem Livegang.
- **Sa 10.10.:** Profile mit Impressum-Link, Startwerte, Link-Schema (utm für Kanäle, ref für Personen), Prüfliste der 4 bekannten Fabriken, gekürzter Content-Batch.
- **So 11.10.:** Tech Pack freigeben (Innenbein entscheiden), Fabrikliste freigeben (ohne Netz: 4 weitere selbst suchen), V002 und V003 schneiden.

---

## 1 · Die drei Entwürfe und das Rückgrat

### 1.1 Bewertung

| Entwurf | Stärkstes Stück | Schwächstes Stück | Urteil |
|---|---|---|---|
| **Wachstum** | Greift den größten Engpass an (Liste) und hat als einziger einen vollständigen Kalender neuer Aktionen: Netz, „Bring 3“, Abende, Creator-Vorlauf, Presse, Gates mit Gegenmaßnahmen. Kanal-Mix mit Zahlen | Ignoriert die Steuer. Listen-Soll 3.390 liegt über dem eigenen Kanal-Mix (1.660–3.140). Reservierung mit Anzahlung braucht App und Rechtsprüfung. Laden-Runden vor dem Proto | **Rückgrat**, weil der Tagesplan von Aktionen lebt und dieser Entwurf sie liefert |
| **Cash** | Rechnet die Steuer ein (Schwelle 2 steigt auf 40 > Kontingent 35). Auszahlung prüfen, Kostendeckel, Verhandlung mit Notausgang, Stufe 2 zu 169 €, Mengenformel, Notfall-Leiter, Ausstiegskosten | Wenig dazu, woher die Käufer kommen. Zusagen-Liste ist stark, aber allein zu schmal | **Leitplanken:** alle Geld-Gates und die Notfall-Leiter kommen von hier |
| **Marke** | Kaufquote als billigerer Hebel als Listengröße (Rechnung 2.3), Wortliste, Serp-Test mit Regeln, Nummer am Patch, Vertrauens-Checkliste, Beweisfotos, Marken-KPIs | Verlässt sich bei Reichweite auf die anderen. Grauer Serp als Standard geht strenger gegen deinen Wunsch als nötig | **Conversion-Schicht:** Sprache, Vertrauen, Beweise, Design-Vorschläge |

**Warum Wachstum das Rückgrat ist:** Für 64 Jeans braucht es zuerst Menschen. Cash und Marke machen aus diesen Menschen sicherer Geld, aber sie bringen keine. Ein Tagesplan muss sagen, was du heute tust. Wachstum sagt das am genauesten.

### 1.2 Wo sich die Entwürfe widersprechen, und was gilt

| Thema | Wachstum | Cash | Marke | **Entscheidung Rev. 6** | Warum |
|---|---|---|---|---|---|
| Listen-Soll | 3.390 (Korridor × 1,13 ab W12) | Korridor 3.000 | Korridor, ×1,13 nur bei Kaufquote < 1,5 % | **Soll = Korridor 3.000, Grind+-Ziel 3.390.** Am So 24.01. entscheidet deine gemessene Kaufquote: unter 1,0 % wird das Grind+-Ziel Pflicht | Ein Soll über dem eigenen Kanal-Mix demotiviert. Die echte Quote ist ab 14.01. messbar |
| Wärme vor der Öffnung | Reservierung mit 10 € ab 07.12. | Zusagen-Liste, Anzahlung nur bei < 10 Zusagen am 20.12. | Handheber-Liste | **Zusagen-Liste „Die ersten 35“ immer** (Spalte „Zusage“: Name, Größe, „ich bestelle am 14.01.“; daneben eine eigene Spalte „Vielleicht“, die kein Gate zählt). Dazu ab Mo 07.12. eine **kostenlose** Liste **„Platz in der ersten Stunde sichern“** mit Größe (Option B): DM mit Link um 17:55, Größe vorgemerkt, **keine Nummer versprochen** (Nummern gehen nach Bestelldatum). **10 € Anzahlung (Option A)** nur, wenn am So 29.11. die Liste unter 170 liegt **und** Rechtstexte-Hotline und Shopify zustimmen | Dieselbe Idee in drei Stärken. Die Anzahlung bringt laut Kickstarter-Daten den stärksten Effekt [M-Q26][M-Q27], kostet aber App, Recht und deine Zeit |
| Mehr als 35 Vorbestellungen | Kontingent 45 (Plan) | **Stufe 2: Nr. 036–060 zu 169 €** bis So 04.04. | — | **Stufe 2 zu 169 €** (du entscheidest am Sa 19.12.). **Auslöser:** Stufe 2 geht live, sobald Nr. 035 verkauft ist, frühestens 14.01., spätestens So 21.03., 20:00. Entwurf liegt ab Mo 14.12. bereit, jeden Sonntag ab 17.01. prüfst du: „35 erreicht? Dann heute live, Mail und Story.“ | 45 × 149 € + 19 × 169 € = 9.916 € verfehlt das Ziel. 35 × 149 € + 29 × 169 € = 10.116 €, egal ob die 29 vorher oder im Drop kommen [R]. Stufe 2 bringt nur früher Geld |
| Mess-Abend 3 | Sa 20.03. | **Sa 13.03.** | Sa 20.03. | **Sa 13.03.** | Das Geld vom 20.03. kommt nach der Restzahlung am 19.03. an [Cash] |
| Pixel-Spiel | jetzt streichen (18.10.) | Kriterium für 05.02. | Rat streichen, 05.02. | **Scroll-Story B ist gesetzt.** Spiel: Rat streichen am So 18.10.; wer es offen hält, baut nur bei ≥ 25 Vorbestellungen, keinem roten Gate und grüner Kasse am Fr 05.02. | Kein belegter Verkaufseffekt [M] Hebel 11, 20–40 h [W] |
| Laden-Runden vor dem Proto | ja (17.10., 07.11.) | — | nein, erster Eindruck = echtes Teil | **Nur Grind+, nur Papier, nur Konditionen fragen.** Kern-Besuche erst mit Proto ab Sa 12.12. Ausnahme Sa 21.11.: Burg & Schild mit Stickproben | Die Abende im Januar brauchen eine Zusage bis 19.12. Die holst du mit dem Proto besser |
| Sa 17.10. | Laden-Runde Kreuzberg | — | MEK | **MEK** (Kern) | Die Belegtabelle muss stehen, bevor V002 und V005 Bedeutungen nennen [K 6, Punkt 6] |
| Zipper/Polo vor dem Drop | — | Notfall bei Rot am 28.02. | Notfall bei 7–9 am 01.02. | **Eine Notfall-Option mit zwei Auslösern:** 7–9 Vorbestellungen am 01.02. **oder** Kassen-Ampel rot am 28.02. Du entscheidest | Bricht deine Entscheidung „alles gleichzeitig am 22.04.“ vom 24.09. Darum nur als Notfall |
| Shopify Payments | Mi 25.11. (Plan) | **Fr 30.10.** | — | **Fr 30.10.** | Ob Shopify oder PayPal bei Vorbestellungen Geld zurückhalten, ist ungeprüft [T 1]. Das muss vor dem 20.12. klar sein |
| Werbetest im Januar | — | streichen | — | **Unter 10 Vorbestellungen kein Werbegeld**, ab 10 und grüner Kasse höchstens 50 € Retargeting | Kalte Werbung füllt die Liste nicht: ~4–12 € je Anmeldung (Schätzung aus [M-Q36][M-Q42][M-Q43]) |
| Serp-Farbe | — | — | Grau als Standard, außer der Test ist eindeutig | **Regel aus `design.md` 4.4:** 0 Sowjet-Nennungen → Rot bleibt; 1 → du entscheidest (Rat: Grau); ≥ 2 → Grau; ≥ 4 → Serp nicht in dieser Größe. Ohne ukrainische oder polnische Stimme: Farbvorbehalt bis Sa 07.11. | Hält deinen Wunsch vom 07.10., misst statt glaubt |
| Drop-Link für Top-Werber | 17:30 oder DM 17:55 | — | — | **DM um 17:55** | Hält Early Access 18:00 sauber |

---

## 2 · Kernthese

**Die 10.000 € entstehen in drei Etappen, und jede kann einzeln reißen:**
1. **Bis So 01.11.** beweisen, dass Menschen das wollen: 150 auf der Liste und 10 echte Zusagen.
2. **Bis Di 16.03.** 32 ausgezahlte Vorbestellungen für die Restzahlung am Fr 19.03. **Bei Einfuhrsteuer (DAP)** bis Mi 24.03. 8 mehr ausgezahlt, aus dem Rest der 35 und aus Stufe 2. Sie bezahlen die Fabrik und die Steuer.
3. **Am Do 22.04.** 37 Käufe brutto aus einer Liste von rund 3.000 (weniger, wenn Stufe 2 vorher verkauft hat).

**Der Engpass ist Reichweite für die Liste und Wärme für die Kaufquote, nicht Design oder Preis.** Bestickter Kunst-Denim kostet bei Designer-Labels 270–1.122 $ [M-Q6–Q16]. Mit 169 € bist du in dieser Leiter günstig [M 1.2]. Unbekannt ist die Marke, nicht der Preis.

**Darum baut Rev. 6 drei Dinge, die zusammen laufen:** eine Content-Maschine für Reichweite, eine Wärme-Kette für die Kaufquote und Kassendisziplin mit harten Gates, damit der Drop überhaupt stattfindet. Jede Woche wird gemessen, und für jede Abweichung steht die Gegenmaßnahme vorher fest.

---

## 3 · Ehrliche Einschätzung

### 3.1 Was realistisch ist

| Frage | Antwort | Grundlage |
|---|---|---|
| Hält Rev. 5.3 im mittleren Fall? | Ja. ~21 Vorbestellungen bis 31.01., Drop ~74 brutto | [M 3.4] |
| Im vorsichtigen Fall? | Nur bis Break-even: ~9 Vorbestellungen bis 31.01., ~58–61 Jeans netto | [M 3.4] |
| Kommen 3.000 Adressen von allein? | Eher nicht. Mit durchschnittlichen Posts landest du bei ~2.000–2.800, ohne Ausreißer bei ~700–1.600 | [M 3.6], Wachstum 2.4, Rechnung 5.3 (Schätzungen) |
| Trägt die Kasse mit Steuer? | **Nicht ohne Änderung.** ~1.150 € Einfuhrumsatzsteuer bei Türkei und Kleinunternehmer stehen nicht im Budget [P 3.1, Risiko 2]. Mit Steuer brauchst du 40 statt 32 Vorbestellungen [R: (4.650 € + 1.150 €) ÷ 146 €]. **Bis zur Restzahlung sind 40 nicht erreichbar**, weil es nur 35 Paar zu 149 € gibt. Darum zwei getrennte Termine: 32 ausgezahlt bis Di 16.03. für die Restzahlung, die Steuer erst bei der Einfuhr (~25.–30.03., nur bei DAP) mit 8 mehr bis Mi 24.03. Bei DDP steckt die Steuer schon in der Restzahlung, darum verhandelst du am 27.10. DAP | Portugal ist laut `tools.md` steuerlich wahrscheinlich ähnlich (ungeprüft, Steuerberater am 13.10.) |
| Wie sicher sind die Kosten? | Gar nicht. 63 € Stückkosten und ~60 € Fabrikpreis sind Schätzungen, die echte Stichzahl kommt am Mo 09.11. | [P 3], [S 3.11] |
| Ist das Umsatzziel ohne 64 Jeans erreichbar? | Ja, über Zipper und Polo. Aber die Finanzierung hängt nur an Jeans | Rechnung in 5.5 |

### 3.2 Warum es keine 100 % gibt

1. **Kein Produkt bis 03.12.** Deine Regel ist richtig, aber bis dahin verkaufst du Prozess. Die stärksten Bilder kommen erst ab Dezember.
2. **Kleines Konto.** TikTok-Business-Konten mit 1.000–5.000 Followern holen im Schnitt 317 Views pro Post [M-Q37]. Reels erreichen in dieser Größe ~9,8 % der Follower [M-Q38]. Ausreißer kann niemand planen.
3. **Die Kaufquote ist unbekannt.** Fast alle Wartelisten-Zahlen kommen aus Software und Crowdfunding, nicht aus Mode [M 2.1]. Deine eigene Quote misst du erst ab 14.01.
4. **Lange Wartezeit.** Wer länger als 90 Tage wartet, kauft deutlich seltener als bei schnellem Zugang (Software, nur die Richtung ist übertragbar) [M-Q25].
5. **Kosten und Steuer** sind erst ab 23.10. und 09.11. bekannt.
6. **Fabrik, Zoll, Feiertage:** Ramadan-Fest in der Türkei 08.–11.03. [P 7], Ostern 26.–29.03.2027 [R], Puffer bis zum spätesten Ankunftstermin nur ~16 Tage [Cash 6.1]. **Neu in 6.1:** Nach dem tabellarischen Islam-Kalender läuft der Ramadan etwa vom 08.02. bis 09.03.2027 [R, ±1–2 Tage, ungeprüft], also über die ganze Produktion in der Türkei. Der 29.10. ist Nationalfeiertag in der Türkei, am 28.10. ist nachmittags frei (Allgemeinwissen, ungeprüft): genau die Woche mit Fabrikwahl und Proforma. In Portugal sind 01.12. und 08.12. Feiertage (ungeprüft): Proto-Versand und PP-Bestellung. In Berlin ist der 08.03. Feiertag (ungeprüft). Gegenmaßnahmen stehen im Docket (Calls 21.–23.10., Konditionen bis 27.10. mittags, Produktionsplan 05.02., Event-Tipp 05.03.).
7. **Deine Zeit:** 1–2 Stunden am Tag.

### 3.3 Was uns so nah wie möglich ranbringt

- **Früh messen statt hoffen:** Startwerte am Sa 10.10., Quellen-Tag an jeder Anmeldung, jeden Sonntag ein Gate mit fertiger Gegenmaßnahme.
- **Mehrere unabhängige Quellen:** Netz, Abende, Creator, Presse, Content, Empfehlungen. Fällt eine aus, tragen die anderen.
- **Wärme vor Masse:** Kalte Listen kaufen zu 1–3 %, Gratis-Listen zu 2–5 %, Listen mit Anzahlung zu 15–30 % [M-Q23]. Wer dich, das Papier oder das Sample gesehen hat, kauft eher.
- **Geld vor die Zahlungen holen:** Zusagen, Mess-Abende vor dem 01.02. und vor dem 19.03. (2b am Mi 27.01., 3 am Sa 13.03.), Stufe 2 ab Nr. 036, Backstop 24.03.
- **Billige Ausstiege:** Bis Mi 03.02. ist kein Cent Kundengeld ausgegeben [Cash 4.5]. Die Gates davor sind dafür da, dass du an diesem Tag nicht hoffen musst.
- **Ein Umsatz-Netz:** Zipper und Polo schließen eine Umsatzlücke (5.5).
- **Was du nie tust:** Vorbestellpreis über den 21.03. hinaus verlängern, Kontingent künstlich „ausverkauft“ melden, Rabatt auf nummerierte Teile, Vorbestellungen ohne Lieferung behalten [M 5.2].

---

## 4 · Zielgruppe in 10 Zeilen

1. **Priorität 1 · Warmes Netz und Novalife-Bestand** (Freunde, Familie, Bleach-Käufer): trägt die ersten 10 Vorbestellungen. Größe unbekannt, du zählst sie am Di 13.10. [Z 4].
2. **Priorität 2 · Ost-Wurzeln, zweite Generation, 18–35:** füllt 10 → 32 über die Liste und kauft im Drop. Pool: 1,5 Mio in Polen, 1,3 Mio in der Ukraine, 1,0 Mio in Russland Geborene in DE [Z-Q1], 1,66 Mio Aussiedler aus der früheren Sowjetunion [Z-Q2].
3. Auslöser: **Wiedererkennen**, der Teppich an Omas Wand, Kreuzstich auf Omas Tisch. Kanal: TikTok und Reels, **auf Deutsch** [Z S1]. Instagram erreicht **77–82 %**, TikTok **50–52 %** der 14- bis 29-Jährigen pro Woche [Z-Q23]. *Hinweis:* `zielgruppe.md` nennt 77/50, `markt.md` aus derselben ARD/ZDF-Studie 82/52, `content.md` markiert den Widerspruch. Du öffnest das PDF (Link in 18) am Fr 06.11. selbst und übernimmst eine Zahl. Für die Entscheidungen ändert die Spanne nichts.
4. Einwand: „Ist das russisch, ist das politisch?“ 91 % der Ukrainer sehen Russland negativ [Z-Q46], 72 % der Polen lehnen Russen ab [Z-Q48]. Darum: Subjekt ist das Muster.
5. **Dein Inhalt ist dein Targeting.** Meta hat das Targeting nach ethnischer Herkunft 2022 entfernt [Z-Q52]. Der Teppich-Hook findet sie, Werbung nicht.
6. **Priorität 3 · Denim- und Streetwear-Käufer ohne Ost-Bezug:** Drop-Käufer zu 169 €. Argument: Nummer 1/100, Makros, ehrliche Größe. Anker: Eightyfive 79,95–89,95 €, Carhartt WIP 110 €, Levi's 501 109,95 € [Z-Q26].
7. **Priorität 4 · Handwerk und Stickerei, vor allem Frauen 20–40:** kaufen eher Polo und Zipper. Nie „handgestickt“ sagen, nur die Fäden sind von Hand [Z S4].
8. **Zipper und Polo sind die zweite Tür** für alle, denen 169 € zu viel ist [Z 4].
9. **Prüfstein, keine Zielgruppe:** seit 2022 Angekommene aus der Ukraine. Um Rat fragen, nie bewerben [Z S2].
10. **Keine Zeit für:** Touristen und politische Diaspora-Orte jeder Seite [Z S6, 3.6].

---

## 5 · Funnel-Mathematik

### 5.1 Das Ziel in Stück

| Größe | Wert | Quelle |
|---|---|---|
| Ziel netto | 64 Jeans = 35 × 149 € + 29 × 169 € = 10.116 € (die 29 zu 169 € zählen gleich, ob in Stufe 2 oder im Drop) | [P 3.2] |
| Retouren online in DE | 11 % im Schnitt, 15 % bei 16–29 Jahren, Grund Nr. 1 Größe (67 %) | [M-Q44] |
| **Ziel brutto** | **72 = 35 Vorbestellungen + 37 Drop-Käufe** (Planwert Retoure 10–20 %, Schätzung) | [M 3.1] |
| Break-even | 60 Jeans = 9.440 € | [P 3.2] |
| Verkäuflich | 93 (100 − 5 Creator − 2 Reserve) | [P 3.2] |
| Verkäuflich bei 75 Stück | 68. **Das Ziel von 72 brutto ist dann mit Jeans allein nicht erreichbar**, 64 netto nur bei höchstens 6 % Retoure. Den Rest tragen Zipper und Polo (5.5). Stufe 2 wird bei 75 auf Nr. 036–045 gedeckelt, damit im Drop noch 23 Paar liegen | [R] |
| Nummern (Entscheidung Sa 19.12.) | 001–035 Vorbestellung · 036–060 Stufe 2 · 061–065 Creator · 066–067 Reserve · Rest Drop. Nummern laufen ohne Lücke nach Bestelldatum: Füllt sich Stufe 2 nicht, rücken Creator, Reserve und Drop nach. Das hält deine Entscheidung vom 01.10. („Vorbestellungen 001 ff., dann Creator, dann Drop“), denn Stufe 2 ist auch Vorbestellung | [P 13], [R] |

### 5.2 Drei Szenarien

Formeln wie `markt.md` 3.3 und 3.4. Liste am 13.01. = 28 %, am 21.03. = 85 % der Liste vom 22.04. (Verhältnis aus dem Plan-Korridor). Vorbestellungen gedeckelt bei 35. **Alle Quoten sind Annahmen.** Ab So 01.11. ersetzt du die Anmeldequote, ab So 24.01. die Kaufquote durch deine echten Werte.

| Annahme | **A · vorsichtig** | **B · Plan Rev. 6** | **C · mittel** | Woher |
|---|---|---|---|---|
| Liste → Vorbestellung in der Öffnungswelle (bis 31.01.) | 1,0 % | 1,5 % | 2,0 % | [M-Q23][M-Q29]; B = Marke-Entwurf 2.3 |
| Liste → Vorbestellung bis 21.03. | 1,5 % | 2,0 % | 3,0 % | dazu zweite Welle am Fristende [M-Q31] |
| Liste → Drop-Kauf 22.–25.04. | 1,0 % | 1,5 % | 2,0 % | Zeitverfall [M-Q25] |
| Käufer ohne Listeneintrag | 10 % | 15 % | 20 % | Schätzung |
| Anmeldungen je 1.000 Views | 1,0 | 2,0 | 2,5 | Schätzung [M 3.2]; B interpoliert |

**Rückwärts: Wie groß muss die Liste sein?** [R]

| Wofür | A | B | C |
|---|---|---|---|
| 10 Vorbestellungen bis 31.01. allein aus der Liste (Stand 13.01.) | 900 | 570 | 400 |
| 35 Vorbestellungen bis 21.03. | 2.100 | 1.490 | 935 |
| 37 Drop-Käufe brutto (Liste am 22.04.) | **3.365** | **2.130** | **1.515** |
| Views dafür | ~3,4 Mio | ~1,1 Mio | ~0,6 Mio |

**Vorwärts: Was bringt welche Liste?** (Öffnungswelle · Vorbestellungen bis 21.03. · Drop brutto · Summe brutto) [R]

| Liste am 22.04. | A | B | C |
|---|---|---|---|
| 2.000 | 6 · 28 · 22 · **50** | 10 · 35 · 35 · **70** | 14 · 35 · 49 · **84** |
| **3.000 (Soll)** | 9 · 35 · 33 · **68** | 15 · 35 · 52 · **87** | 21 · 35 · 74 · **93 = ausverkauft** |
| 3.390 (Grind+-Ziel) | 11 · 35 · 37 · **72** | 17 · 35 · 59 · **93 = ausverkauft** | ausverkauft |

**Lesart:**
- Mit dem Soll von 3.000 erreichst du im Fall B das Ziel mit Puffer, im Fall A Break-even.
- **Der Schritt von A nach B bringt bei gleicher Liste rund +20 Käufe.** Für denselben Effekt bräuchtest du im Fall A rund +1.000 Adressen [Marke 2.3]. Deshalb sind die Wärme-Hebel so wichtig wie die Reichweite.
- In A reicht die Öffnungswelle aus der Liste nicht für die Schwelle von 10. Darum tragen **Zusagen** und **Mess-Abende** die Schwelle, nicht die Liste.

### 5.3 Woher die Liste kommt (Kanal-Mix, Schätzung)

| Kanal | Rechnung | Anmeldungen bis 22.04. | Quelle |
|---|---|---|---|
| Eigene Posts | ~240–330 Uploads (TikTok + Instagram) × Ø 400–800 Views × 2,5 je 1.000 | 240–660 (korrigiert: 240 × 400 × 2,5 ÷ 1.000 = 240) | [M 3.6], Wachstum 2.4 |
| 3–5 Ausreißer-Videos | je ~100.000 Views × 2,5 je 1.000 | 750–1.250 | [M 3.6] |
| Warmes Netz, einzeln | du zählst es am 13.10. | 80–150 | [C 1.1] |
| Papiertest- und Stick-Abend | 10–12 Gäste, jeder bringt 1–3 | 30–60 | [C 1.1] |
| 3 Mess-Abende | 20–40 Gäste je Abend | 60–120 | [C 1.1] |
| Creator (5 mit Paar, 10 ohne) | 10 Posts × ~3.000 Views × 5 je 1.000 | ~150 | [M 3.6] |
| Hochschulen | | 20–50 | [C 1.1] |
| Meta-Werbung 300 € | 4–12 € je Anmeldung | 25–75 | [M 2.5] |
| „Bring 3 Freunde“ | Viral-Faktor 0,15–0,25 | +15–25 % auf alles | [M-Q51], Güte C |
| Presse, Flohmarkt-Stand | nicht planbar | Bonus | [C 1.1] |
| **Summe ohne Ausreißer / mit 3–5 Ausreißern** | | **~700–1.600 / ~1.550–3.100** | [R]: (605 bzw. 1.265 + Ausreißer) × 1,15 bzw. 1,25; vorher ~800 / ~1.700 mit der falschen Untergrenze 330 |

**Folge:** Ohne Ausreißer bleibt die Liste unter dem Soll. Darum ist die Content-Maschine der wichtigste Hebel für die Größe. Zusagen, Abende und Stufe 2 sind die Versicherung, falls die Größe ausbleibt.

### 5.4 Cash-Mathematik

| Größe | Wert | Quelle |
|---|---|---|
| Kapitalbedarf · Eigenbudget · Lücke | 9.380 € · 4.500 € · 4.880 € | [P 3] |
| Netto je Vorbestellung | ~146 € (Shopify Payments 2,1 % + 0,30 €) | [P 3.1] |
| **Schwelle 1** (Anzahlung Do 04.02.) | **10** ausgezahlte Vorbestellungen bis Mo 01.02. | [P 3.1] |
| **Schwelle 2a** (Restzahlung Fr 19.03.) | **32** ausgezahlt bis **Di 16.03.** | [P 3.1], [R] |
| **Schwelle 2b** (Einfuhrsteuer, nur Türkei mit DAP, ~25.–30.03.) | **+8 = 40** ausgezahlt bis **Mi 24.03.**, aus dem Rest der 35 und aus Stufe 2. Sonst Brücke | [R: 1.150 € ÷ 146 € ≈ 8] |
| Fabrikpreis +1 €/Paar | Schwelle 2 +0,7 | [Cash 2.3] |
| Zahlung 60/40 statt 50/50 | Schwelle 1 steigt auf 14 | [Cash 2.3] |
| Echter Kreuzstich +10.000 Stiche | Schwelle 2 steigt auf 36 | [D 2.5] |
| Faustregel | ~2.650 Stiche = 1,46 €/Paar = 146 € = 1 Vorbestellung bei Schwelle 2 | [D 0] |
| 75 statt 100 Stück | Schwelle 2 ~22 (Schätzung, gleicher Stückpreis) | [Cash Hebel 9] |

**Regeln, die daraus folgen:**
- Bis zur schriftlichen Antwort des Steuerberaters planst du mit 1.150 € Steuer.
- **Für eine Zahlung zählt nur Geld, das drei Werktage vorher auf dem Konto ist** [Cash Hebel 2]. Daraus folgen die Stichtage: **Mo 01.02.** (Anzahlung Do 04.02.), **Di 16.03.** (Restzahlung Fr 19.03.), **Mi 24.03.** (Steuer bei Einfuhr ab ~25.03.; Karfreitag 26.03. und Ostermontag 29.03. sind keine Werktage [R]). Darum liegt Mess-Abend 2b auf Mi 27.01. und nicht auf Sa 30.01., und Mess-Abend 3 auf Sa 13.03. Am Di 29.12. misst du die echte Auszahlungsdauer, dann rechnet Claude alle Stichtage nach.
- **Stufe 2 geht live, sobald Nr. 035 verkauft ist**, frühestens Do 14.01., spätestens So 21.03., 20:00 (wenn die 149 € enden). Sie läuft bis So 04.04., 20:00.
- **DAP statt DDP** (Rat, du entscheidest am 27.10.): Bei DDP steckt die Steuer im Preis und wäre schon mit der Restzahlung fällig. Dann bräuchtest du 40 bis zum 16.03., und die gibt es mit 35 Paar zu 149 € nicht.
- Die 3 Paar Puffer sind deine Erstattungsreserve, nie für Kostenüberschreitungen [Cash 4.1].
- Jede Ausgabe außerhalb von Plan 3 muss mindestens eine zusätzliche Vorbestellung (146 €) wahrscheinlich machen.
- **Zeile „ungeplant“ im Blatt „Kasse“ (ab Di 13.10.):** Steuerberater, Rechtstexte über 80 € ([T 3.1]: nach Aseprite bleiben 80 € Puffer), Verpackungslizenz, Helferlohn, Abende (bis ~150 €, Schätzung [C]), Einfuhrumsatzsteuer und Kurierpauschale auf Proto und PP, Fotograf und Models, Shopify Email über dem Freikontingent, Produkthaftpflicht. Jede Position mit Schätzung. **Je 146 € Summe steigt Schwelle 2a um 1.**

### 5.5 Das Umsatz-Netz: Zipper und Polo

Im Fall A bei 3.000 Adressen: 68 Jeans brutto, nach 10–15 % Retoure ~9.170–9.710 € Jeansumsatz [R: 0,85–0,90 × (35 × 149 € + 33 × 169 €)]. Die Lücke von ~290–830 € schließen **3–6 Zipper** (139 €) oder 4–11 Polos (79 €) [R]. Sie binden kein Kapital, weil Blanks erst nach Zahlung gekauft werden [P 3.2]. **Sie zählen nie für die Schwellen.** Darum zählst du Umsatz und Finanzierung getrennt.

---

## 6 · Wochen-Zielwerte

**So liest du die Tabelle:**
- **Warteliste** = nur bestätigte Anmeldungen (Double-Opt-in, „E-Mail-Marketing: abonniert“) [C 1.2]. Soll = Plan-Korridor, Alarm = Bedarf im mittleren Szenario [M 3.7]. **Grind+-Ziel** = Soll × 1,13 ab W12 (Wachstum).
- **Follower** = neue Follower TikTok + Instagram seit 12.10., Schätzung 3 je Anmeldung [M 3.7]. Ab So 01.11. ersetzt du sie durch deine Quote.
- **Posts** = Feed-Posts und ASK-Storys laut `content.md` + 2 Grind+ (Karussell oder Variante).
- **Vorbestellungen** kumuliert, bezahlt. Für die Schwellen zählt nur ausgezahltes Geld. Soll aus Cash 2.7, Alarm = Mindestwert.
- **Zusagen** = Blatt „Die ersten 35“, nur Spalte „Zusage“: Name, Größe, „ich bestelle am 14.01.“ [Cash Hebel 6]. „Vielleicht“ steht in einer eigenen Spalte und zählt in keinem Gate.

| W | KW-Sonntag | Warteliste Soll (Alarm) | Grind+-Ziel | Follower TikTok + IG, neu (Schätzung) | Posts/Woche (Kern + Grind+) | Vorbestellungen kumuliert Soll (Alarm) | Zusagen „Die ersten 35“ |
|---|---|---|---|---|---|---|---|
| 4 | 11.10.2026 | Startwert zählen (Sa 10.10.) | — | Startwert zählen | 0 | — | — |
| 5 | 18.10. | 40 (15) | — | ~120 | 3 + 2 | — | Netz zählen |
| 6 | 25.10. | 90 (30) | — | ~270 | 3 + 2 | — | 5 |
| 7 | 01.11. | **150** (50) Validierung | — | ~450 | 3 + 2 | — | **10** |
| 8 | 08.11. | 210 (80) | — | ~630 | 3 + 2 | — | 10 |
| 9 | 15.11. | 270 (110) | — | ~810 | 3 + 2 | — | 11 |
| 10 | 22.11. | 330 (140) | — | ~990 | 3 + 2 | — | 12 |
| 11 | 29.11. | 390 (170) | — | ~1.170 | 3 + 2 | — | 13 |
| 12 | 06.12. | 470 (200) | 530 | ~1.410 | 6 + 2 | — | 15 |
| 13 | 13.12. | 550 (230) | 620 | ~1.650 | 5 + 2 | — | 18 |
| 14 | 20.12. | 620 (260) | 700 | ~1.860 | 5 + 2 | — | **20** (Gate ≥ 15) |
| 15 | 27.12. | 680 (280) | 770 | ~2.040 | 3 | — | 20 |
| 16 | 03.01.2027 | 740 (300) | 840 | ~2.220 | 3 | — | 22 |
| 17 | 10.01. | 850 (380) | 960 | ~2.550 | 5 + 2 | — | **25** |
| 18 | 17.01. | 1.000 (450) | 1.130 | ~3.000 | 6 + 2 | 10 (6) | — |
| 19 | 24.01. | 1.250 (520) | 1.410 | ~3.750 | 5 + 2 | 13 (8) | — |
| 20 | 31.01. | **1.500** (600) | 1.690 | ~4.500 | 5 + 2 | **16 (10 = Schwelle 1)** | — |
| 21 | 07.02. | 1.700 (660) | 1.920 | ~5.100 | 3 + 2 | 18 (12) | — |
| 22 | 14.02. | 1.900 (720) | 2.150 | ~5.700 | 5 + 2 | 20 (14) | — |
| 23 | 21.02. | 2.150 (790) | 2.430 | ~6.450 | 4 + 2 | 22 (16) | — |
| 24 | 28.02. | **2.400** (850) | 2.710 | ~7.200 | 4 + 2 | 24 (18) | — |
| 25 | 07.03. | 2.450 (880) | 2.770 | ~7.350 | 5 + 2 | 26 (21) | — |
| 26 | 14.03. | 2.500 (910) | 2.820 | ~7.500 | 5 + 2 | 29 (25); absehbar 32 ausgezahlt bis Di 16.03. | — |
| 27 | 21.03. | 2.560 (950) | 2.890 | ~7.680 | 5 + 2 | **35 (32 ausgezahlt bis Di 16.03. = Schwelle 2a)** | — |
| 28 | 28.03. | 2.620 (1.050) | 2.960 | ~7.860 | 5 + 2 | 37 (35), ab Nr. 036 Stufe 2; **bei Steuer 40 ausgezahlt bis Mi 24.03. = Schwelle 2b** | — |
| 29 | 04.04. | 2.720 (1.170) | 3.070 | ~8.160 | 7 | 43 inkl. Stufe 2 bis So 04.04. | — |
| 30 | 11.04. | 2.820 (1.290) | 3.190 | ~8.460 | 7 | — | — |
| 31 | 18.04. | 2.920 (1.400) | 3.300 | ~8.760 | 7 | — | — |
| 32 | 25.04. | **3.000** (1.515) | 3.390 | ~9.000 | 10 | **Drop: 37 brutto (Alarm < 29 netto)** | — |

**Dazu jeden Sonntag:** Kassen-Ampel K − F − R ≥ 300 € (grün) [Cash 4.1] · Anmeldequote der Wartelisten-Seite ≥ 6,6 % (Landingpage-Median [M-Q36]) · ab 14.01. Produktseiten-Conversion ≥ 1,3 % (Mode-Median [M-Q35]).

---

## 7 · KPI-Gates mit Gegenmaßnahmen

### 7.1 Jeden Sonntag (im Wochenreview, +10 Minuten)

| # | Wenn am Sonntag … | dann … |
|---|---|---|
| G1 | Liste **unter Alarm** | (a) Netz-Runde an alle Offenen bis Mi · (b) „Bring 3“-Story + DM an alle mit 1–2 Freunden · (c) einen Abend in den nächsten 14 Tagen festmachen · (d) Claude die 3 schwächsten Videos zeigen. Zwei Sonntage in Folge: Notfallhebel aus `markt.md` 5.2 |
| G2 | Liste unter Soll, über Alarm | bestes Video der Woche in 2 Varianten nachdrehen, Kommentar-Zeit auf 15′, nichts streichen |
| G3 | Anmeldungen je 1.000 Views **< 1,0** | CTA-Problem: angehefteter Kommentar mit Vorteil („Die Liste kauft zuerst. 35 Paar zum Vorbestellpreis.“), Link-Sticker in jede Story, Seite im Instagram-Browser testen |
| G4 | Anmeldequote der Seite **< 6,6 %** zwei Sonntage in Folge [M-Q36] | echtes Foto oben, Vorteil in einem Satz, nur E-Mail Pflicht, Ladezeit prüfen |
| G5 | Video **≥ 2 × Median** nach 48 h und Teil-Rate über Median | **5 Varianten in 14 Tagen** (neuer Hook, neues erstes Bild, gleicher Kern) [K 5.3] |
| G6 | 3 schwache Videos (< 0,5 × Median) im selben Slot | Slot 2 Wochen durch ein Reserve-Format ersetzen [K 5.3] |
| G7 | **≥ 3 Kommentare** pro Woche mit „Sowjet“, „Wappen“, „Holodomor“ | danken, zählen, nie löschen · 2 Wochen kein Ernte- oder Serp-Bild · vor 09.11.: graue Schneide und weiße B2-Kante einfrieren (0 bis +0,22 €/Paar, Schwellen bleiben [D 3.7]) |
| G8 | ≥ 3 Folklore-Kommentare („Oma“, „Kostüm“) | 2 Wochen: erst die Totale aus 3 m im Streetwear-Outfit, dann das Makro |
| G9 | > 70 % der neuen Anmeldungen aus warmen Tags (`ref-netz`, `ref-papier`, `ref-stick`) | Content trägt nicht: 3 neue Hooks, DE-Hook vorziehen, Karussell „Miss deine Jeans“ |
| G10 | ab 14.01.: Vorbestellungen **unter Alarm** | persönliche DM an jede Zusage ohne Kauf mit ihrer Größe, Einladung zum nächsten Mess-Abend, „X von 35“ nur mit echter Zahl |
| G11 | ab 14.01.: Produktseiten-Conversion **< 1,3 %** bei ≥ 300 Sitzungen | häufigste DM-Frage als erstes FAQ, Größenblock unter den Preis, Goldfäden-Video als zweites Bild |
| G12 | Kassen-Ampel gelb (0–300 €) / rot (< 0) | gelb: keine Ausgaben außerhalb von Plan 3 · rot: Ausgaben-Stopp-Liste, dann Notfall-Leiter (7.3) |
| G13 | ab So 17.01. bis So 21.03.: **Nr. 035 verkauft?** | heute Stufe 2 live (Entwurf vom 14.12. aktivieren), Mail an alle ohne Kauf, Story. Am So 21.03., 20:00 geht Stufe 2 in jedem Fall live |

### 7.2 Harte Gates mit Datum

| Datum | Gate | grün → | sonst → |
|---|---|---|---|
| **Fr 09.10., 12:00** | Freeze und Serp-Test | Tech Pack bis So 11.10. | Anfrage geht trotzdem Mo 12.10. mit v1.7 raus. Ohne UA/PL-Stimme: Farbvorbehalt B/B2 bis Sa 07.11. |
| So 18.10. | Netz ≥ 30 Namen, ≥ 4 Fabrik-Antworten, Steuertermin | weiter | Netz aus Handy-Kontakten ergänzen; 2 Nachzügler-Fabriken; IHK-Gründungsberatung oder anderer Steuerberater bis Fr 23.10. |
| **Mi 21.10.** | **Belegtabelle v1.0** (nach dem MEK; Quelle, Region, Abbildung je Motiv) | V005 heute; V011, V014, V015, V108–V112 nur mit Beleg | V120 statt V005; Tabelle bis So 25.10.; Videos ohne Beleg in die Reserve |
| **Fr 23.10.** | Steuer schriftlich | Kapitalbedarf neu | mit 1.150 € planen, Stufe 2 wird Pflicht |
| Mo 26.10. | Fabrik mit Panel-Stickerei im Haus, Ampel grün/gelb | Konditionen 27.10. (bei Türkei bis 12:00) | Ampel rot: Gegenrechnung, Optionen V4b, kleiner Serp, 75 Stück |
| Fr 30.10. | Bei Türkei: Proforma da | Validierung zählt „50/50 schriftlich“ | anrufen; ohne Proforma gilt „50/50 schriftlich“ am 01.11. als offen |
| **So 01.11.** | **Validierung** ≥ 150, ≥ 10 Zusagen (nur Spalte „Zusage“), 50/50 schriftlich, Markenkriterien | Entwicklung zahlen | gelb 50–149: zahlen, Content und Netz nachschärfen · rot < 50: nicht zahlen, **B-Zeitachse 1 (7.4)**, 6 neue Posts, bestes Video in 5 Varianten |
| Sa 07.11. | Farbe B/B2, Namen, Sprache final, Bildregel „keine Seitenansicht links“, Liefergebiet | Spec Rev. 14 | Ohne Daten gilt der Rat: graue Schneide, weiße Kante, Wortliste, EN-Hook mit DE-Zeile, Bildregel bleibt |
| So 08.11. | Fabrik antwortet in ≤ 3 Werktagen | weiter | Call, Fabrik 2 warm anschreiben |
| Di 10.11. | Stiche ≤ 33.000 | freigeben | Gegenrechnung, Füllung statt echtem Kreuzstich |
| **Di 17.11.** | Stickproben bestanden | Proto | kein Proto; benannten Fehler beheben (**B-Zeitachse 1**) oder Fabrik 2 (**B-Zeitachse 2**) |
| So 22.11. | Proto-Versand schriftlich ≤ 30.11. | weiter | Call; bei Portugal Feiertage 01.12. und 08.12. einrechnen (ungeprüft) |
| So 29.11. | Liste ≥ 170 · Payments verifiziert · Rechtstexte live | „Platz in der ersten Stunde sichern“ (Option B) | Liste < 170: Option A mit 10 €, nur mit Recht und Shopify · Payments offen: Reservierung ohne Zahlung, Ticket beim Payments-Support · Rechtstexte offen: bis Fr 04.12. |
| Sa 05.12. | Proto und Fit | PP Mo 07.12. | zweites Proto, Öffnung nach **B-Zeitachse 1** (Do 21.01.) |
| So 13.12. | Zusagen ≥ 18 · Reservierungen ≥ 15 | weiter | bis 20.12. jeden Tag 3 Termine · DM an jeden aus dem Netz |
| **So 20.12.** | Zusagen ≥ 15, Auszahlung geklärt, Stufe 2 entschieden, Patch bestellt | Vorbestellung wie geplant | < 10 Zusagen: Ausgaben-Stopp, Proto-Runde verlängern · Auszahlung unklar: kein Start · Patch offen: Bestellung Mo 21.12., Fabrik über neue Patch-Frist Fr 29.01. informieren |
| Di 05.01. | PP freigegeben | Öffnung 14.01. | Öffnung höchstens Do 21.01. (**B-Zeitachse 1**) |
| So 10.01. | Zusagen ≥ 25 | weiter | alle „Vielleicht“ persönlich zum Mess-Abend 1 |
| So 17.01. | ≥ 8 Vorbestellungen | weiter | zweite DM-Welle, Mess-Abend 2 doppelt bewerben |
| **So 24.01.** | eigene Kaufquote (Vorbestellungen ÷ Liste 13.01.) · Mess-Abend 2b · Patches bei der Fabrik | > 1,5 %: Kurs halten | 1,0–1,5 %: Mess-Abend 13.03. als Hauptereignis · < 1,0 %: Grind+-Ziel 3.390 wird Pflicht · Mess-Abend 2b am **Mi 27.01.** (Do 28.01. nur bei Auszahlung ≤ 2 Werktage), wenn am 13.01. < 60 Reservierungen + Zusagen oder Vorbestellungen unter Soll · Patches fehlen: Call und neue Rechnung für den Produktionsstart |
| **Mo 01.02.** | **Schwelle 1** + Mengenformel (ausgezahlt am 31.01. + 6 × Wochenrate W19–W20) | ≥ 10 und Hochrechnung ≥ 32 ausgezahlt bis Di 16.03. → 100 Stück (bei Steuer zusätzlich 40 bis Mi 24.03. inkl. Stufe 2) | Schwelle erfüllt, Hochrechnung darunter → 75 Stück, Stufe 2 nur Nr. 036–045 · < 10 → 2 Wochen schieben (**B-Zeitachse 2**) · 7–9 → Notfall-Option Zipper-Vorbestellung |
| Fr 05.02. | Spiel | ≥ 25 Vorbestellungen, kein Gate rot, Kasse grün | streichen |
| So 07.02. | PO bestätigt, Anzahlung bezahlt | weiter | Call, Produktionsstart neu rechnen |
| So 14.02. | Stoff da (reserviert seit 06.01.) | weiter | sofort Call |
| So 21.02. | Inline-Fotos 1 | weiter | Call, Liefertermin bestätigen lassen |
| So 28.02. | ≥ 18 Vorbestellungen, Liste ≥ 850, Shopify-Email-Kontingent | weiter | Mail „Noch X von 35“, Brücke vorwarnen, Notfall-Option Zipper/Polo entscheiden · Kontingent zu klein: Preis ins Blatt „Kasse“ oder T−14 und T−7 nur an Abonnenten, die in 90 Tagen geöffnet oder geklickt haben |
| So 07.03. | Inline-Fotos 2, Steuer-Rücklage | weiter | Call, Liefertermin schriftlich · ohne Rücklage Kampagne 1 streichen |
| **So 14.03.** | ≥ 29 (Alarm 25) · absehbar **32 ausgezahlt bis Di 16.03.** (mit der Auszahlungsdauer vom 29.12.) | Restzahlung 19.03. | Notfall-Leiter ab Stufe 3, Backstop Mi 24.03. vorbereiten |
| **Fr 19.03.** | ≥ 32 ausgezahlt bis Di 16.03. und Endkontroll-Nachweis aus der PO vollständig | zahlen | nur Geld fehlt: Backstop Mi 24.03. · Endkontrolle durchgefallen: nicht zahlen, Fotos an die Fabrik |
| So 21.03., 20:00 | 35 zu 149 € voll | — | 149 € endet trotzdem; Stufe 2 läuft spätestens ab jetzt bis So 04.04. Preis nie verlängern |
| **Mi 24.03.** | Tracking da · bei Steuer (DAP): **40 ausgezahlt** (35 + Stufe 2) | weiter | tägliche Mail an die Fabrik, ab 31.03. Drop-Plan B · Steuer-Geld fehlt: Brücke abrufen (Stufe 7) |
| So 28.03. | Ware mit Tracking, Stufe 2 ≥ 2, Kasse deckt die Steuer | weiter | Stufe 2 < 2: Mail und Story „Stufe 2 bis 04.04.“ · Steuer nicht gedeckt: Brücke abrufen |
| So 04.04. | Ware geprüft, Steuer bezahlt | weiter | Brücke |
| **Do 15.04.** | Ware da (spätester Termin) | Drop 22.04. | Drop 29.04. (**B-Zeitachse 2**) oder „Versand ab Ankunft“, offen angekündigt [P 6] · Ware erst nach So 25.04.: Mail an alle Vorbesteller mit neuem Datum und dem Angebot voller Erstattung |
| Do 22.–So 25.04. | Do 21:00 ≥ 15 · Fr 19:00 ≥ 26 (**Schätzung aus Crowdfunding**: rund 90 % der Listenkäufer kaufen in 48 h [M-Q27], für Mode nicht belegt) · So ≥ 29 netto | — | Do < 15 um 21:15: DM an alle Zusagen und Handheber ohne Kauf, Fr 10:00 Mail an die Nicht-Öffner · Fr < 26 um 19:00: Story mit den Restgrößen · So < 29: Retargeting 72 h, Bundle Jeans + Polo, Zipper/Polo pushen, Rest zu 169 € im Shop, Konsignation erst danach |

### 7.3 Notfall-Leiter (immer von oben nach unten)

| Stufe | Hebel | Kostet |
|---|---|---|
| 1 | Warm: persönliche Nachrichten an alle Zusagen und „Vielleicht“, ein zusätzlicher Abend | Zeit |
| 2 | Ausgaben-Stopp-Liste: Chenille-Muster (−120 €), Werbetest, Kampagne 1 nur bei grüner Kasse; im Extremfall Zipper/Polo-Entwicklung erst ab 01.02. | Abstriche |
| 3 | Mess-Abend extra, Bestand je Größe so umschichten, dass keine Größe die 149 € blockiert (Stufe 2 öffnet von selbst, sobald Nr. 035 verkauft ist) | 20 Min. + 1 Abend |
| 4 | Restzahlung auf Backstop Mi 24.03. | Puffer zum 15.04. schrumpft |
| 5 | **Zipper und Polo vorbestellbar** (Abweichung von deiner Entscheidung vom 24.09., du entscheidest) | bricht den gemeinsamen Launch |
| 6 | Teil-Lieferung gegen Teilzahlung | Rest nach dem Drop |
| 7 | Brücke: Stand-by-Zusage über 1.500 € in der Familie (klären bis Do 31.12.) | Schulden |
| 8 | 75 statt 100 Stück (nur am 01.02. möglich) | weniger Ausverkaufs-Umsatz |
| 9 | Drop auf Do 29.04. | Glaubwürdigkeit |
| 10 | Ausstieg mit voller Erstattung | nur bis Mi 03.02. ohne Schaden für Kunden |

### 7.4 B-Zeitachse (Claude, Stand 07.10.; mit den echten Fabrikterminen nachrechnen)

Gilt, sobald ein Gate „schieben“ sagt. Entschieden wird **am Tag des Gates**. Gerechnet ab den Abständen im Plan: Anzahlung → Produktionsstart 4 Tage, Produktion bis Endkontrolle 6 Wochen, Transport ~8 Tage [R aus P 5]. Ramadan und Fest liegen in beiden Fällen in der Produktion (ungeprüft, siehe 3.2).

| Termin | Plan | **B1 · 1 Woche später** | **B2 · 3 Wochen später** |
|---|---|---|---|
| Auslöser | — | Validierung rot (01.11.), Stickprobe mit benanntem Fehler (17.11.), zweites Proto (05.12.), PP nicht ok (05.01.) | Fabrik 2 (17.11.), Schwelle < 10 (01.02.) |
| Proto · PP | 03.12. · ~04.01. | ~10.12. · ~11.01. | Fabrik 2: Proto frühestens Januar (Schätzung) |
| Öffnung Vorbestellung | Do 14.01. | **Do 21.01.** | **Do 04.02.** |
| Schwelle 1 · ausgezahlt bis | Mo 01.02. | **Mo 08.02.** | **Mo 22.02.** |
| Anzahlung · Produktionsstart | Do 04.02. · Mo 08.02. | Do 11.02. · Mo 15.02. | Do 25.02. · Mo 01.03. |
| Endkontrolle und Restzahlung | Fr 19.03. (Geld bis Di 16.03.) | **Do 25.03.** (Fr 26.03. ist Karfreitag; Geld bis Mo 22.03.) | **Fr 09.04.** (Geld bis Di 06.04.) |
| Vorbestellpreis endet | So 21.03., 20:00 | So 21.03., 20:00 (bleibt) | **So 04.04., 20:00** |
| Stufe 2 bis | So 04.04. | So 04.04. | So 18.04. |
| Ware da | ~30.03. | ~06.04. | ~19.04. (nach dem spätesten Termin 15.04.) |
| Vorbestellungen raus | 06.–07.04. | ~08.–09.04. | ~21.–22.04. |
| **Drop** | Do 22.04. | **Do 22.04.** (Puffer bis 15.04. nur ~9 Tage) | **Do 29.04.** |

**Folgen:** B1 hält den Drop, kostet aber Puffer. B2 verschiebt den Drop. Die Zusage „Lieferung bis spätestens 30.04.2027“ hält in B2 nur knapp. Darum gilt in B2 die Regel vom 15.04.: Kommt die Ware später, Mail an alle Vorbesteller mit neuem Datum und vollem Erstattungsangebot. Ein öffentlich genanntes Öffnungsdatum (14.01.) verschiebst du nur einmal und sagst es offen.

---

## 8 · Die 10 Top-Hebel

Sortiert nach Wirkung pro Stunde deiner Zeit. Wirkung ist meine Einschätzung auf Basis der Belege.

| # | Hebel | Wirkung | Kerntermine |
|---|---|---|---|
| 1 | **Warmes Netz + Zusagen-Liste „Die ersten 35“** | trägt Schwelle 1 | Di 13.10. zählen · Fr 16.10. N1 · Do 29.10. N2 · Proto-Runde 03.–13.12. · DMs 15.12., 13.01., 27.01. |
| 2 | **Content-Maschine:** 3 Hook-Typen (Zahl, Fehler, Frage), Varianten-Regel, Serien „Day X“, „Omas Teppich“, „Miss deine Jeans“, DE-Test | einziger Weg zu Ausreißern | ab Mo 12.10. jede Woche |
| 3 | **Abende:** Papiertest 24.10., Stick 27.11., Mess-Abende 16.01., 23.01., 13.03., Drop-Abend 24.04. | Wärme + Größen-Sicherheit; Pop-ups in der Mode 25–40 % Conversion [M-Q54, Güte C] | siehe Berlin-Plan |
| 4 | **Event-Momente:** Proto im Broadcast zuerst, Early Access 18:00 für die ganze Liste, Live 19:00, Countdown-Sticker, Mail am Fristende („heute 20:00 endet 149 €“) | Käufe kommen am Anfang und Ende einer Frist [M-Q31] | 03.12., 14.01., 21.03. 12:00, 29.03., 22.04. |
| 5 | **Steuer- und Kostenwahrheit, Auszahlung prüfen** | ±8 Vorbestellungen bei Schwelle 2 | 13.10., 23.10., 30.10., 10.11., 29.12. |
| 6 | **Stufe 2 zu 169 € + Mengenformel** | +5–8 Vorbestellungen ohne Rabatt (Schätzung Cash), deckt die Einfuhrsteuer am 24.03. | 14.12. Entwurf, 19.12. Nummern, ab 14.01. live bei Nr. 035, 01.02., 22.03. Mail, 04.04. |
| 7 | **Creator früh:** Erst-DM 11.12., Preview 12.01., Nano-Welle 20.01. | Clips treffen die Öffnung; Nano-Engagement 1,78 % [M-Q40] | 07.11.–12.01. |
| 8 | **Vertrauen und Größe:** Checkliste 9/9, Geld-zurück-Regel, „W32 = 81 cm“, „Miss deine Lieblingsjeans“ | 67 % der Retouren wegen Größe [M-Q44]; dieselbe Unsicherheit bremst den Kauf (Schätzung) | 12.11., 19.11., 15.12., 07.01. |
| 9 | **„Bring 3 Freunde“ + Quellen-Tags** | +15–25 % (Viral-Faktor [M-Q51]); Power-Referrer kaufen zu 30–50 % [M-Q23] | Sa 10.10. Schema, Do 15.10. Einbau, Mi 11.11. in die Theme-Kopie, Mi 18.11. Test |
| 10 | **Symbol- und Sprachhygiene** | verhindert, dass das Kernsegment abspringt | Fr 09.10., Sa 07.11., 23.–29.11., Mi 24.02. |

**Anti-Hebel: das Pixel-Spiel.** Kein belegter Verkaufseffekt [M] Hebel 11, 20–40 Stunden, Phaser allein 315 KB gzip [W-W3]. Die Idee bleibt in der Scroll-Story.

---

## 9 · Content-System

### 9.1 Slots

| Slot | Inhalt | Zeit | Länge (Arbeitsregel) |
|---|---|---|---|
| BUILD | Fortschritt, Serie „Day X of building a 100-pair jeans drop“ (Tag 1 = Mo 12.10.) | Mo 18:00 | 15–30 s |
| ORIGIN | Muster, Bedeutung (nur mit Beleg), Teppich | Mi 18:00, ab Proto Di | 20–40 s |
| REAL | echte Zahlen, Fehler | Fr 18:00 im Wechsel | 20–35 s |
| DETAIL | ein Makro, ein Satz | Fr 18:00 | 8–15 s |
| REACH | kurz, loopt, für Nicht-Follower | Mi 19:00 ab Proto | 6–10 s |
| ASK | Story mit Umfrage, Frage, Countdown | Sa 12:00 ab Proto | — |
| Grind+ | Karussell aus der Reserve oder Variante des besten Videos | P1: Di und Do · ab W12: Do und So | 4–8 Slides |

Quelle: [K 1.4, 3]. Uhrzeiten sind Plan-Zeiten, keine geprüften Bestzeiten. Am So 08.11. liest du die Aktivzeiten deiner Follower ab und schiebst bei mehr als einer Stunde Abweichung [K 1.7].

### 9.2 Rhythmus je Phase

| Zeitraum | Kern-Posts | Was | Zusatz |
|---|---|---|---|
| 12.10.–29.11. (P1/P2) | **3/Woche** | Papier, Bauplan, Zahlen, Fabriksuche, Stickproben, Teppich. **Kein fertiges Teil, kein Mockup** | 8 Story-Umfragen Di/Do bis 05.11. · 2 Grind+-Karussells |
| 23.–29.11. | 3, **ohne Ernte- und Serp-Bild**, Sa 28.11. gar keiner | Holodomor-Gedenktag am 4. Samstag im November [Z-Q51] | |
| 30.11.–20.12. | **5–6/Woche** | ab 03.12. Proto: Unboxing V025, Makros, Fit, „Uhrwerk“ | Broadcast ab Mo 30.11. |
| 21.12.–03.01. | 3/Woche | Feiertage | |
| 04.01.–07.02. | 5–6/Woche | Vorbestellung, echte Zahlen „X von 35“, Creator-Clips | Live 14.01. |
| 08.02.–28.03. | 4–5/Woche + Story | Produktion, Shoot, Kampagnenfilm, Set | **Mi 24.02. nichts Werbliches** (5. Jahrestag des Großangriffs [Z-Q32]), V078 am Do 25.02. |
| 29.03.–21.04. | **täglich 18:00** | Countdown CD-T24 bis CD-T01, vorproduziert am 18. und 20.03. aus dem Shoot-Rohmaterial (die 24 Motive stehen ab 17.02. auf der Shotliste). CD-T06 wird V125, CD-T13 heißt „So ist der Shoot entstanden.“ | an echten Tagen ersetzt ein Live-Clip das Asset |
| 22.–25.04. | 7 Drop-Posts | V101–V107. **Teilsperre am 22.04.:** kein Serp im Hero-Bild, keine Ernte-Hooks (Lenins Geburtstag, 22.04.1870, Allgemeinwissen, ungeprüft). Antwortbaustein: „Der Termin ist der Donnerstag nach der Lieferung, sonst nichts.“ Der Termin bleibt | Live 18:00–18:30 |

### 9.3 Regeln

1. **Gezeigt wird nur, was es gibt.** Bis 03.12. kein fertiges Teil und kein Mockup, das wie eins aussieht.
2. **Sprachregel:** Subjekt ist das Muster. Nie „authentisch“. Lebensbaum nie „slawisch“.
3. **Wortliste nach außen** (Vorschlag aus `zielgruppe.md` 3.5, du entscheidest am Fr 09.10.): „Time Travel“ statt „Projekt Slavic“ · „Kreuzstich-Band“ statt „Vyshyvanka“ · „Achtstern“ statt „Alatyr“ · „Das Feld danach“ für den Serp · „maschinengestickt auf dem Zuschnitt, Fäden von Hand“ statt „handgestickt“ · „entworfen in Berlin“ statt „Made in Berlin“ · Länder nur alphabetisch und nur wenn nötig. Warum: „Vyshyvanka“ ist ukrainisches Nationalsymbol [Z-Q32], „Alatyr“ ist in der Neuheiden-Szene verbreitet [Z-Q39], „slawisch“ und „ein Volk“ sind politisch besetzt [Z-Q42][Z-Q43].
4. **Hooks:** „Älter als jede Grenze“ ersetzt (V002, V030). Nie „fünf Ähren“, B2 hat drei.
5. **Bildregeln:** nie hellblauer Himmel über gelbem Weizen · keine echte Sichel als Requisite · B und B2 nie im selben Bild, keine Seitenansicht links · kein roter Hintergrund · keine Sowjet-Kulisse, keine Streifen in Blau-Gelb, Rot-Schwarz, Orange-Schwarz, Rot-Grün, Weiß-Rot-Weiß [Z 3.6] · Farbtreue mit Graukarte [D 6.3]. **Folgen (6.1):** „Keine Seitenansicht links“ gilt ohne Ausnahme, bis du sie am Sa 07.11. nach dem Serp-Test bewusst lockerst. Bis dahin: V119 (Serp-Papier an der Seite) frühestens Do 12.11. und nur bei gelockerter Regel; CD-T06 wird V125. In Sequenzen (V099, CD-T02) gilt die Reihenfolge **B · A · E · C · D · B2**, damit Serp und Ähren auf Rot nicht direkt nacheinander kommen (sonst Wappen-Vokabular). Bis 03.12. zeigt kein Bild die farbige Flachzeichnung mit allen fünf Elementen (V004: nur Maßtabelle, Schnittzeichnung schwarz-weiß, ein Element flach).
6. **Varianten-Regel:** ≥ 2 × Median Views nach 48 h und Teil-Rate über Median → 5 Varianten in 14 Tagen [K 5.3].
7. **Hook-Test:** eine Variable pro Test; drei Typen im Wechsel. **DE-Test:** V004, V006, V007, V009 bekommen Test-Hook B auf Deutsch. Entscheidung Sa 07.11. nach Anmeldungen je 1.000 Views.
8. **Musik** nur aus der Business-Bibliothek der jeweiligen App, eigener Ton zuerst, nie in CapCut einbacken [K 1.9] (Plattformregeln ungeprüft).
9. **Kommentare:** Z, V, Georgsband, Kriegsverherrlichung sofort ausblenden. Kritik nie löschen. Standard: „Das Muster gibt es in Belarus, Polen, Russland und der Ukraine. Es gehört keinem allein.“ [Z 3.8]
10. **Keine** Telegram-Gruppen, keine russischsprachigen Captions, kein #slavicembroidery [K 1.8][C 3.1].
11. **CTA je Phase** (ersetzt die Standard-CTA in `content.md` 3, Wortlaut prüft die Rechtstexte-Hotline am 24.11.). Grund: „Wer auf der Liste ist, kauft zuerst und zum Vorbestellpreis“ kann bei ~850 Adressen und 35 Paar zu 149 € für die meisten nicht stimmen (Risiko irreführende Werbung, UWG, ungeprüft). „149 € statt 169 €“ entfällt, weil du 169 € nie verlangt hast (Streichpreis ohne früheren Preis, PAngV § 11, ungeprüft, keine Rechtsberatung).

| Zeitraum | CTA (DE) | CTA (EN) |
|---|---|---|
| bis 13.01. | Link in Bio: Trag dich ein. Die Liste kauft zuerst. 35 Paar zum Vorbestellpreis. | Link in bio: join the list. The list buys first. 35 pairs at the pre-order price. |
| 14.01.–21.03. | Vorbestellen über den Link in Bio. Vorbestellpreis 149 € bis 21.03. · ab 22.04. 169 €. Noch [Y] von 35. | Pre-order in bio. Pre-order price €149 until 21.03. · from 22.04. €169. [Y] of 35 left. |
| 22.03.–04.04. | Drop 22.04., 19:00. Bis So 04.04. noch vorbestellen: 169 €, Lieferung Anfang April. Link in Bio. | Drop 22.04., 19:00. Pre-order until Sun 04.04.: €169, ships early April. Link in bio. |
| 05.04.–21.04. | Drop 22.04., 19:00. Die Liste kommt um 18:00 rein. Link in Bio. | Drop 22.04., 19:00. The list gets in at 18:00. Link in bio. |
| ab 22.04., 19:00 | Jetzt live. Link in Bio. | Live now. Link in bio. |

Jeder Link trägt das Schema vom Sa 10.10.: `utm_source` zeigt den Kanal (Bio, QR, Mail), `?ref=` zeigt Person, Abend oder Creator (`netz`, `papier`, `stick`, `mess1`–`mess3`, `mess2b`, `c-[name]`, `p-[medium]`, `h-[kürzel]`, `code`). In den Bios steht deshalb kein `?ref=ig` mehr, sonst landet „ref-ig“ als Werber-Code. Nur bestätigte Anmeldungen zählen.
12. **Wörter:** „Quellen-Tag“ meint die Quelle einer Anmeldung (`src-`, `ref-`). Die Frage nach der Familienherkunft gibt es nur anonym in Tally. **Ethnische Herkunft speicherst du nie neben Name oder E-Mail** (Art. 9 DSGVO).

### 9.4 Wochenablauf

- **Sonntag:** Wochenreview mit Gate und Kassencheck (20–30′), Batch-Dreh in Ortsreihenfolge und Schnitt (75–100′) [K 4.3].
- **Posttag:** 17:55 prüfen, 18:00 live, Reel in die Story mit Link-Sticker, 15′ antworten (20′ gesamt) [K 4.4].
- **Werktag ohne Post:** 10′ Community, fünf Kommentare mit Inhalt in deiner Nische.
- **An Claude jeden Sonntag eine Zeile:** „W[n]: Liste [X] (+[Y]), Views [Z], bestes Video V0xx, schwächstes V0xx, Anmeldungen je 1.000 Views [Q], kritische Kommentare [K], Kasse [Ampel].“

### 9.5 E-Mail-Plan (neu in 6.1)

Risiko 7 „Liste altert“ verlangt alle 2–4 Wochen ein Ereignis. Vorher bekam die Liste acht Wochen lang keine Mail. Jede Werkstatt-Mail ist kurz, Text von Claude, 15′ für dich. Vor der ersten großen Mail (07.12.) authentifizierst du am Mo 30.11. die Absender-Domain in Shopify (vor Ort prüfen).

| Datum | Mail |
|---|---|
| ab Fr 09.10. | Willkommens-Mail nach dem Double-Opt-in (ab Do 15.10. mit „Bring 3“-Link) |
| Mo 02.11. | Werkstatt 1: Ergebnis der Validierung |
| Do 03.12., 19:00 | Werkstatt 2: Das Proto ist da (terminiert am 02.12.) |
| Mo 07.12., 19:00 | „Platz in der ersten Stunde sichern“ öffnet |
| Do 07.01. · Mi 13.01. | Vorbestellung 1 (Mess-Abende) · „Morgen: 18:00 für die Liste, 19:00 für alle“ |
| **Do 14.01., 18:00** | **an die ganze Liste:** Die Liste kauft zuerst (17:55 DM an Reservierer und Zusagen) |
| Mo 18.01. · Di 26.01. | „Noch X Paar“ · an Abonnenten ohne Kauf |
| Do 04.02. | Werkstatt 3: „Bestellt. X von 35“ |
| Mo 22.02. | Werkstatt 4: Der Shoot |
| Mo 15.03. | „Vorbestellpreis endet So 20:00“ |
| **So 21.03., 12:00** | „Heute 20:00 endet 149 €“ (terminiert am 20.03.; U-Form am Fristende [M-Q31]) |
| Mo 22.03. | an alle ohne Kauf: Stufe 2 bis So 04.04. |
| Do 08.04. · Do 15.04. · Mo 19.04. · Mi 21.04. | T−14 · T−7 · T−3 · T−24h (T−14 und T−7 nur an Aktive, falls das Kontingent am 28.02. nicht reicht) |
| **Do 22.04., 18:00 und 19:00** | T−1h mit Schlüssel-Link · LIVE-Mail (beide terminiert am 21.04.) |
| Fr 23.04., 10:00 | nur wenn Do 21:00 unter 15: an alle, die die LIVE-Mail nicht geöffnet haben |

---

## 10 · Berlin-Offline-Plan

Adressen und Zeiten aus Suchtreffern der Recherche (`berlin.md`), **vor jedem Besuch prüfen**. Bis 03.12. zeigst du nur Prozess. Kontakte nur offiziell.

| Datum | Ort | Was | Kern / Grind+ | Quelle |
|---|---|---|---|---|
| Sa 17.10. | **MEK**, Arnimallee 25, Dahlem (laut berlin.de Mi–Fr 10–17, Sa–So 11–18 Uhr, 10 €) | Belegtabelle: Raute, Achtstern, Zickzack, Lebensbaum an echten Stücken; filmen nur mit Erlaubnis | Kern 120′ | [B-58][B-59] |
| So 18.10. | Nowkoelln Flowmarkt, Maybachufer | ansehen (Termin nur fortgeschrieben) | Grind+ | [B-35] |
| Sa 24.10. | bei dir oder einem Freund | **Papiertest-Abend** 18:00–19:30 | Kern | [C 6.1] |
| So 25.10. | Mauerpark-Flohmarkt | 15 Leute fragen, nur wenn < 6 Gespräche | Grind+ | [B-34][Z-Q58] |
| So 01.11. | Berlin Vintage & Heritage Market, Ballhaus Berlin | Kontakte, nach der Validierung | Grind+ | [B-38] |
| Sa 07.11. | Studio183 (Brunnenstr. 183), Civilist (Brunnenstr. 13), Firmament (Linienstr. 40), Soto (Torstr. 72) | nur Papier, Konditionen und Abende fragen | Grind+ | [B-23][B-8][B-6][B-16] |
| Sa 21.11. | **Burg & Schild**, Rosa-Luxemburg-Str. 3 | gewaschene Stickproben, Feedback der Denim-Kenner | Kern | [B-1] |
| Fr 27.11. | bei dir oder Kunstraum Heartspace, Danziger Str. 172 (Anfrage 05.11.) | **Stick-Abend** 18:30–20:00, nur Raute und Achtstern | Kern | [Z-Q59][C 6.2] |
| Sa 28.11. | Holy Shit Shopping, CANK, Karl-Marx-Straße, Neukölln (28.–29.11.) | als Besucher: Designer nach Bewerbung und Standpreis fragen; kein Post | Grind+ | [B-39][B-40] |
| Mi 18.11. | GATE194 über store@gate194.berlin, Sing Blackbird und Studio183 über ihre offiziellen Kanäle | **schriftliche Voranfrage** (15′): Di 12.01., Sa 16.01., Sa 23.01., Sa 13.03. abends freihalten, Proto ab 03.12. | Kern | [B-10][B-15][B-23] |
| Sa 12.12. | **GATE194**, Köpenicker Str. 194 (Hinterhof, laut Website Mo–Sa 12–20 Uhr) und **Sing Blackbird**, Sanderstr. 11 | mit Proto: Abende fest anfragen, gebündelt mit 3 Treffen der Proto-Runde (90′ statt 60′, zwei Läden samt Weg sind sonst zu knapp) | Kern | [B-10][B-15] |
| So 13.12. | — | kein Laden hat zugesagt: Ersatz über Giggster suchen (10′) | Kern | [B-46] |
| Fr 18.12. | Studio183, Konk (Kleine Hamburger Str. 15, Status prüfen) | A-Liste Teil 2 | Grind+ | [B-23][B-11][B-12] |
| Sa 19.12. | — | **Orte fest**, sonst Fläche über Giggster | Kern | [B-46] |
| Di 12.01. | Ort vom 19.12. | **Creator-Preview** 18:30–20:00 | Kern | [C 2.4] |
| Sa 16.01. · Sa 23.01. · **Sa 13.03.** | Ort vom 19.12. | **Mess-Abende** 18:00–20:00 (bis 21:00 Grind+) | Kern | [C 6.3], Cash |
| **Mi 27.01.** (Ausweich Do 28.01.) | Ort vom 19.12. | Mess-Abend 2b 18:30–20:00, nur bei Gate So 24.01. Nicht mehr Sa 30.01.: Wer dort bestellt, ist bis Mo 01.02. nicht ausgezahlt | Grind+ | Wachstum, Regel 5.4 |
| Do 15.10. · Sa 09.01. · Fr 15.01. | Familie · Lette Verein oder Studierende (offizieller Kontakt) · Feld am Stadtrand | Teppich leihen? · Fotograf mit schriftlichen Nutzungsrechten (Shop, Werbung, Presse) · Landwirt fragen | Kern | [B 5][B 4.2][B 7] (ungeprüft) |
| Sa 20.02. | Wohnung mit Familienteppich + Feld zur goldenen Stunde | **Shoot „Die Hütte“**; Shotliste ab 17.02. mit den 24 Countdown-Motiven | Ausnahme | [B 4.1] |
| Sa 27.03. | Holzmarkt-Flohmarkt (Saison 2027 nur fortgeschrieben) | Countdown-Stand, nur wenn Stand < ~146 € | Grind+ | [B-37] |
| So 28.03., 04.04., 11.04., 18.04. | ein Feld am Stadtrand, nur mit Erlaubnis des Landwirts | „Das Feld wächst“, gleicher Platz, Sonnenuntergang | Grind+ | [B 4.1] (Weizen-Kalender ungeprüft) |
| **Sa 24.04.** | Partnerladen | **Drop-Abend** 17–20 Uhr. Ja am Fr 05.03. nur, wenn Packen Tag 2 an die Helfer geht oder auf So 25.04. vormittags rückt; Laden schriftlich bis Fr 12.03., Abend in Presse-Welle 3. Geht beides nicht, entfällt der Abend | Ausnahme | [C 6.4] |

**Nie:** an sowjetischen Ehrenmalen drehen [K 4.8]; Russisches Haus in der Friedrichstraße [Z S1]; politische Diaspora-Orte.

---

## 11 · Creator- und PR-Plan

### 11.1 Creator

| Datum | Schritt |
|---|---|
| Sa 07.11. · So 15.11. · Do 26.11. | Longlist von Hand, 30 Namen, nur folgen und kommentieren. Kriterien: Berlin oder deutschsprachig, 5.000–80.000 Follower (Kern 5.000–30.000), eigene Jeans-Outfits, keine Politik, keine Flaggen als Statement, keine Kolovrat-, Schwarze-Sonne-, Valknut-Symbolik [C 2.1] |
| Mi 02.12. | Shortlist 12 mit Brand-Safety-Prüfung (10 Min. je Kandidat) [C 2.3] |
| **Fr 11.12.** | Erst-DM C2 an die Top 8 |
| Fr 18.12. | einmal nachfassen; unter 5 Zusagen Nr. 9–12 |
| Di 05.01. | Zusage, Briefing-Karte |
| **Di 12.01., 18:30** | **Preview** mit Proto und PP, eigener Link `?ref=c-[name]` |
| Mi 13.–Fr 15.01. | Clips zur Öffnung |
| Mi 20.01. | Nano-Welle 2: 10 Nano-Creator aus deinen Kommentaren zum Mess-Abend 2, ohne Paar |
| Mo 25.01. | Clips einsammeln, Anmeldungen je Creator |
| Mo 15.03. · Do 08.04. · Do 15.04. | Story-Bitte „Preis endet“ · Pakete · Erinnerung Post 17.–21.04. |

**Abmachung (Vorschlag, du entscheidest):** 1 Clip bis 15.01., 1 Story 17.–21.04. Kein Rabattcode, kein Geld. Geschenktes Paar = „Anzeige“ ganz vorn plus Plattform-Label; die Rechtslage (§ 5a UWG, BGH 09.09.2021) ist in den Recherchen ungeprüft, du klärst sie vor Fr 11.12. über die Hotline des Rechtstexte-Service [C 2.6]. Die 5 Paare sind im Plan schon abgezogen [P 3.2].

### 11.2 Presse

| Datum | Welle | Winkel |
|---|---|---|
| Sa 14.11. · Do 19.11. | Presseliste (17 Medien aus [C 5.2], Kontakt nur aus Impressum oder offizieller Seite) | — |
| Mi 09.12. | Pressemappe v1, Seite `/pages/presse` | — |
| **Di 15.12.** | **Welle 1** „Vorbestellung ab 14.01.“: Lokalpresse, Gründer-Medien, Denim-Blogs | Ehrliche Größen · Die Vorbestellung baut die Fabrik · Vom Bleichen zur eigenen Hose |
| Mi 30.12. → Sa 02.01. | Event-Tipp Mess-Abende an tip Berlin, Mit Vergnügen, iHeartBerlin, The Berliner | Ein Abend in Berlin |
| Sa 27.02. | Pressemappe v2 mit Shoot-Fotos | — |
| **Do 04.03.** | **Welle 2** „Drop 22.04.“ (nicht am 24.02.) | Der Faden, der die Hose verlässt · Ehrliche Größen · Teppich nur mit Sprachregel |
| **Fr 05.03., 09:00** | Event-Tipp Mess-Abend 3 (nicht Mo 08.03.: Frauentag ist in Berlin Feiertag, Allgemeinwissen, ungeprüft) | |
| So 28.03. → **Mo 05.04.** | **Welle 3** Event Drop + Drop-Abend | |

Presse ist Bonus und steht nicht im Soll [C 1.1]. Nachfassen einmal, nie öfter. Statt „Or this drop doesn't happen“ schreibst du: „Vorbestellungen entscheiden, ob 100 oder 75 Paar entstehen. Startet die Produktion nicht, geht jedes Geld zurück.“ [Marke Hebel 5]

---

## 12 · Design-Empfehlungen für den Freeze (du entscheidest)

**Urteil aus `design.md`:** v1.7 kann verkaufen. A und E tragen vorn den Preis, hinten Patch, B2 mit Goldfäden und C. Fast das ganze Risiko steckt im Serp mit roter Schneide: Aus 3 m verschwindet das Stoppelfeld, übrig bleibt eine weiße Sichel mit roter Kante, hinten Ähren auf rotem Band [D 2.1, 2.2]. Rechtlich ist der Serp allein laut übernommener Übersicht kein verbotenes Zeichen [M-Q5]. Ein Verkaufsrisiko im Kernsegment ist er trotzdem.

| # | Vorschlag | Δ €/Paar | Schwellen | Mein Rat |
|---|---|---|---|---|
| V2 | Serp-Schneide stahlgrau (B-G), optional kräftigeres Stoppelfeld (B-GS) | 0 (B-GS −0,28 bis −0,55) | 10/32 | **Test entscheidet** nach der Regel aus 1.2. Abweichung von deinem Wunsch vom 07.10. nur bei ≥ 2 Sowjet-Nennungen |
| V3 | B2-Band mit weißer Kante (1 Stich) | +0,08 bis +0,22 | 10/32 | **ja.** Deine eigene Regel 2 sagt: Rot ohne Weiß verschwindet aus 2 m [S 3.4] |
| V1 | „N° ___ / 100“ von Hand auf der Patch-Lasche | +0,20 bis +0,30 | 10/32 | **ja.** Macht Knappheit sichtbar: „Wer zuerst bestellt, bekommt die kleinste Nummer“ |
| V4a | Füllung als Standard, Deckel 33.000 Stiche | 0 | schützt 10/32 vor 11–12/34–36 | **ja, Pflicht im Tech Pack** |
| V4b | Münztasche offen | −3,30 bis −3,60 | 9/30 | **nein.** E ist dein stärkstes Detail und bestes Thumbnail [D 1.2] |
| V5 | Patch D nach Gürteltest kleiner: 76 × 67 mm am Bund oder 66 × 58 mm auf der Passe | −0,50 bis −0,20 | 10/32 | **ja.** 3 mm Luft zu den Schlaufen hält keine Serie [D 2.3] |
| V6 | Bedeutung innen als Hangtag-Karte (Taschenfutter-Druck nur ≤ 0,50 €) | 0 bis +0,50 | 10/32 | **ja als Karte** |
| — | Taschenklappe | +1–2 (ungeprüft) | bis +1,4 | **keine Klappe** |
| — | Nackenlabel Zipper/Polo gewebt, vereinfachter Baum, **mit Novalife-Adresse** (Herstellerangabe nach GPSR, falls du bei bestickten Blanks als Hersteller giltst; Frage an die Hotline am 24.11.) | Marge ~+1 € (Schätzung) | — | **ja** |
| — | Lebensbaum D: Ursprung der Referenz | 0 | — | **klären bis Di 20.10.** Stammt die Vorlage von einem fremden Künstler, kann die Nachbildung auf 110 Patches ein Urheberrechtsproblem sein (ungeprüft). Dann zeichnet Claude vor der Patch-Anfrage am 28.10. eine eigene Fassung |
| — | „Goldene Nähte“ = Steppnaht im selben Gold wie das Stickgarn | 0 | — | **ja, falls du das meinst.** Keine Ziernaht um den Serp (Wappen-Effekt) |
| — | Serp-Höhe | — | — | Mitte **45 cm** bei W32, +0,5 cm je Größe, endgültig nach Block 3 |
| — | Tech-Pack-Zusätze | 0 | — | 2 mm Denim zwischen Band A und Kante · Weiß nach der Wäsche L* ≥ 80 · Anti-Backstaining-Frage · Schlaufen ≥ 8 mm vom Patch · GPSR-Herstellerangabe aufs Pflegeetikett [T 3.1] · **neu 6.1 aus Spec Teil 5:** Verschleißkarte mit den Freihaltezonen (Spec 3.9, Claude bis So 11.10.) · Wash Reference Sheet aus 8 Fotos der Eightyfive (Do 08.10.) · Innenbein-Gradierung +1,0 oder +1,5 (du am So 11.10.) · Shade Card und 3 Lab Dips (Ziel, heller, dunkler) mit L*-Werten der Fabrik, angefordert Di 03.11., freigegeben Mi 18.11. bei Tageslicht. **L* ohne eigenes Messgerät:** Die Fabrik misst, du vergleichst bei Tageslicht mit dem freigegebenen Stofflappen. Der Lappen ist der Waschstandard bis zum Wareneingang · REACH-Bestätigung für Knopf, Nieten (Nickel) und Farbstoffe (Azo) schriftlich, ungeprüft welche Werte gelten |

**Paket V1 + V3 + V4a + V5 + V6 (+ V2 nach Test):** −0,77 bis +0,54 €/Paar, **Schwellen bleiben 10/32** [D 3.7]. Fallback, falls der Serp durchfällt: kleiner Serp aus v1.6 ohne Rot (10/31) oder streichen (9/30) [D 3.7]. **Keine neue Stickerei ohne Gegenrechnung.**

---

## 13 · Website-Empfehlung

**Scroll-Story „Der Weg zur Hütte“ (Variante B) bauen, Pixel-Spiel (A) streichen.** [W Kurzfassung, 2]

| | Scroll-Story B | Pixel-Spiel A |
|---|---|---|
| Aufwand | 24 Schritte, ~18 h (Schätzung), ~10,5 h vor dem 05.02. | +20–40 h (Schätzung) |
| Gewicht | eigene Dateien ≤ 95 KB | Phaser 3.90.0 allein 1,20 MB roh, 315 KB gzip [W-W3] |
| Risiko am Drop-Tag | niedrig, läuft ohne JavaScript | steht zwischen Besucher und Kasse |
| Deine Idee | bleibt: Scrollen ist Laufen, Feld bei Sonnenuntergang → Jeans, Zipper, Polo → Hütte → Teppich | voll |

**Was B kann:** Countdown mit Serverzeit, Formular mit Größen- und Quellen-Tags, Nummern-Raster 001–100 als Kreuzstich (vergeben = rot-weiß), Zustände Warteliste → Vorbestellung → Zwischenzeit → Schlüssel 18:00 → Live 19:00 → Ausverkauft, fester Button „Direkt zum Shop“, PLAN B in unter einer Minute [W 3].

**Korrekturen an `website.md` (6.1, gelten vor der Datei).** „Stufe 2“ heißt hier immer die Preisstufe zu 169 €, nicht die Website-Stufe 2 „Das Muster“.
- **Stufe 2 fehlt dort.** `website.md` rechnet noch mit „Kontingent 45“ (`tt_start_vorbestellung` 35/45, `tt_start_drop` 58/48). Neu: Produkt `tt_produkt_stufe2`, Zahl `tt_start_stufe2` = 25 (bei 75 Stück 10). `tt_start_drop` setzt du am So 04.04. auf 93 − 35 − Stufe-2-Verkäufe.
- **Raster (Schritt 10, Mo 21.12.):** füllt ab 001 ohne Lücke: Vorbestellungen (149 € und Stufe 2), dann 5 Creator, 2 Reserve, dann Drop. Bei vollem Verkauf 001–035 · 036–060 · 061–065 · 066–067 · 068–100.
- **Schritt 11 (Do 07.01.):** kein durchgestrichener Drop-Preis, stattdessen „Vorbestellpreis 149 € bis 21.03. · ab 22.04. 169 €“. Lieferzeile „Lieferung bis spätestens 30.04.2027, geplant Anfang April“ statt „22.–30.04.2027“ (K6 genauso). Ist die Vorbestellung ausverkauft, zeigt der Knopf „Vorbestellen · 169 € · Lieferung Anfang April“.
- **Schritt 15 (Fr 05.03.):** ZWISCHENZEIT zeigt bis So 04.04., 20:00 zusätzlich den Stufe-2-Knopf, danach nur „Hol dir den Schlüssel“.
- **Schritt 5 (Mi 11.11.):** Größen auch „kleiner als W30“ und „größer als W38“ (`gr-klein`, `gr-gross`). Die Empfehlungs-Lösung vom 15.10. wird übernommen: `code-[6 Zeichen]`, Danke-Text mit persönlichem Link, WhatsApp-Knopf. Test am Mi 18.11. mit `?ref=test`.
- **Schritt 11 und Generalprobe Mo 11.01.:** Zeitsteuerung mit einem Testprodukt „in 20 Minuten“ prüfen. Am 14.01. um 17:50 Vorbestellung aktiv oder Zeitsteuerung geprüft, 17:58 Link im privaten Fenster testen.
- **Drop-Tag:** Der Rev.-5.3-Schritt „19:00 Theme ‚Drop 22.04.‘ veröffentlichen“ entfällt (website.md 2), im Docket steht dazu eine Notiz.
**Design der Seite:** Palette aus Teppich und Sonnenuntergang, das einzige Blau ist der Denim auf den Fotos; echte Fotos vor Grafik; Sichel und Ähren nie als freigestellte Grafik, Icon oder Favicon [W 6].
**Termine:** Schritt 1 Sa 31.10. · Formular Mi 11.11. · Stufe 1 live Mi 18.11. · Stufe 2 Fr 11.12. · Raster Mo 21.12. · Vorbestell-Zustände Do 07.01. · Shoot-Bilder Sa 27.02. · „Der Weg zur Hütte“ Sa 06.03. · PLAN B üben Mi 17.03. · stiller Launch Mo 22.03. · Generalprobe Fr 09.04. · Code-Freeze Sa 17.04. Claude Code arbeitet an der Theme-Kopie, veröffentlichen und pushen machst nur du.
**Ungeprüft, mit Testschritt:** zeitgesteuertes Veröffentlichen, mehrere Tags in einem Feld, Shopify-Email-Freikontingent, In-App-Browser [W 1].

---

## 14 · Zeitbudget und Grind+

- **Kern:** im Schnitt **72 Minuten pro Tag**, zusammen ~240 Stunden bis 25.04. [R aus `skeleton.json`, Stand 6.1; vorher 68 Min. und ~226 Stunden]. Höchstens **120 Minuten**, mit fünf bewussten Ausnahmen: **Do 08.10. bis So 11.10.** (125–135 Min.: Freeze, Tech Pack und Fabrikanfrage sind der kritische Pfad, der Freeze ist schon einmal gerutscht) und **Sa 16.01.** (125 Min., Mess-Abend 1 plus Umschichten der Größen).
- **Woher die +14 Stunden kommen:** Prüfliste der Fabriken, Wash-Fotos, Checkliste vor dem Livegang, Proto-Runde als Kern (2 × 60′ + 6 Video-Calls), Werkstatt-Mails, Bestellbestätigung, Retouren, Helfer anmelden, Zipper/Polo-Check, Umschichten in den ersten 72 Stunden. Dafür ist die Proto-Runde kein Grind+ mehr: Das Gate am 13.12. hängt an ihr.
- **Ausnahmen** (lange Tage, ~25 Stunden): Shoot Sa 20.02. · Warenannahme und Prüfung Di 30.03.–Fr 02.04. · Vorbestellungen packen Di 06.–Mi 07.04. · Drop und Packen Do 22.–Fr 23.04. · Packen Tag 2 an die Helfer, sonst So 25.04. vormittags · So 11.10. (60′, nur wenn Claude kein Netz hat).
- **Abende** sind als Kern auf 90–110 Minuten begrenzt. Die Verlängerung bis 21:00 steht als Grind+.
- **Grind+** (~50 Stunden, alles optional): Karussells und Varianten, Laden-Runden, Mauerpark, Holy Shit Shopping, Mess-Abend 2b (nur bei Gate), Waschserie mit dem PP, Feld-Drehs, Countdown-Stand, Spiel nur bei „bauen“.
- **Rangfolge, wenn die Zeit nicht reicht:** Fabrik und Sample > Geld-Gates > Abende > Pflicht-Posts > Netz und Zusagen > Grind+.
- Am Tag nach einem langen Abend nur Pflicht.

---

## 15 · Änderungen gegenüber Rev. 5.3

**Technikregel für den Docket-Bau:** Rev.-5.3-Aufgaben werden nie eingefügt oder verschoben, nur an derselben Stelle umgewidmet oder in eine Notiz verwandelt. Neue Aufgaben werden angehängt [Ü 8].

| Datum | Rev. 5.3 | Rev. 6 | Warum |
|---|---|---|---|
| Do 08.10. | Startseite (60′) + Papiertest (45′) | Papiertest mit Varianten-Blatt, Clips, Schnelltest, Steuertermin; Startseite als Notiz → **Fr 09.10.** angehängt | Papiertest entscheidet den Freeze |
| Fr 09.10. | Freeze | + Freeze-Zettel mit Namen, Farbvorbehalt, V1, V4a, V5, V6, GPSR | [D 4.5][T 3.1] |
| Sa 10.10. | Profile | + Startwerte, `?ref`-Links, Wortliste, Netzwerkzugang | ohne Startwert sind die Gates blind |
| So 11.10. | Tech Pack | + RFQ-Zusatzfragen (75/100, je 1.000 Stiche, DDP/DAP, Euro, Betriebsferien, Taschenfutter, Anti-Backstaining, Patch im Haus) | Cash Hebel 3, [D V6] |
| Di 13.10. | Steuer (30′) | Steuer mit Fragen 9 und 10 (45′) + Blätter „Netz“, „Die ersten 35“ und „Kasse“ mit Zeile „ungeplant“ + Tally mit Datenschutz-Absatz + Story 1 + Belegtabelle | Cash, Wachstum, Marke |
| Mi 14.10. | ORIGIN „Älter als jede Grenze“ | V002 „Jede Region stickt die Raute anders“ | [Z-Q42] |
| Do 15.10. | Teppich-Fotos | + „Bring 3“-Mechanik, Story 2, Teppich für den Shoot klären | [C 4.2] |
| Fr 16.10. | REAL „Die Zahlen“ | gleicher Post, CTA mit Geld-zurück-Satz + Netz-Runde 1 | Marke Hebel 5 |
| Sa 17.10. | Puffer | **MEK** | Belegtabelle |
| So 18.10. | Review | + Gate W5 + Spiel-Entscheidung (Rat streichen) | |
| Sa 24.10. | Referenzen prüfen | + **Papiertest-Abend** | [C 6.1] |
| Mo 26.10. | Fabrik | + EORI am selben Tag (bei TR) | [T 6] |
| Di 27.10. | Konditionen | 8 Verhandlungspunkte inkl. Backstop 24.03. und Bankdaten-Regel | Cash Hebel 4 |
| Fr 30.10. | EORI | Kontrolle; **Shopify Payments + Support-Frage Auszahlung** | Cash Hebel 2 |
| So 01.11. | Validierung | + Zusagen, 50/50 schriftlich, Markenkriterien | |
| Sa 07.11. | Puffer | **Entscheidungen Farbe, Namen, Sprache**, Creator-Longlist, Website Schritt 3 | Marke Hebel 2 |
| Di 10.11. | Digitizing freigeben | mit Deckel 33.000 und Gegenrechnung | [D V4a] |
| Mi 18.11. ↔ Mi 25.11. | Panel-Stickerei ↔ Teppich | **Teppich am 18.11.**, Panel am 25.11. | Holodomor-Gedenktag Sa 28.11. [Z-Q51] |
| Sa 21.11. | Puffer | **Burg & Schild** mit Stickproben | [B-1] |
| Mi 25.11. | Zahlungsanbieter | umgewidmet: PayPal + Auszahlungsplan | Payments seit 30.10. |
| Fr 27.11. | REAL „Warum 169 €“ | + **Stick-Abend** | [C 6.2] |
| Sa 28.11. | Versand im Shop | + kein Post | Gedenktag |
| Do 03.12. | Sample da | + **V025 Unboxing 19:00** + Proto-Runde | [K] |
| Mo 07.12. | PP bestellen | + 19:00 „Platz in der ersten Stunde sichern“ öffnen | |
| Mi 09.12. | REACH „Älter als jede Grenze“ | V030 „Uhrwerk“ | [Z-Q42] |
| Fr 11.12. | DETAIL Goldfäden | + **Creator-DM** (5 Wochen früher) | U-Form [M-Q31] |
| Mo 14.12. | Vorbestellung anlegen | + Stufe-2-Produkt, Liefertext „bis spätestens 30.04.2027“ | Cash Hebel 5, [T 3.1] |
| Di 15.12. | rechtlich sauber | + Geld-zurück-Regel, **Presse-Welle 1** | |
| Sa 19.12. | Kontingent festlegen | **35 zu 149 € + Stufe 2 zu 169 €** statt Kontingent 45 | 10.116 € statt 9.916 € [R] |
| So 27.12. | Spiel-Stiltest (150′) | umgewidmet: 12 beste Proto-Bilder auswählen; Stiltest nur Grind+ | |
| Di 29.12. | Testbestellung | + Auszahlung bis aufs Konto verfolgen | Cash |
| Do 31.12. | Monatsabschluss | + Brücke klären | Cash Hebel 10 |
| Di 12.01. | ORIGIN | + **Creator-Preview** | |
| Do 14.01. | Öffnung 19:00 | + 17:55 DM an Reservierer und Zusagen, 18:00 Mail an die ganze Liste, Live 19:00–19:30 | |
| Sa 16.01. · Sa 23.01. | Story | + **Mess-Abende 1 und 2** | [C 6.3] |
| Di 19.01. | Tempo bewerten (Werbetest) | Regel umgedreht: unter 10 kein Werbegeld | Cash |
| Mi 20.01. | 5 Creator anfragen | umgewidmet: Nano-Welle 2 | [C 8] |
| Mo 25.01. | Creator-Anproben terminieren | umgewidmet: Clips einsammeln | [C 8] |
| Do 28.01. · Mo 01.02. | Hochrechnung · Schwelle | Mengenformel 100/75, nur ausgezahltes Geld | Cash Hebel 9 |
| Fr 05.02. | Spiel bauen/streichen | mit Kriterium; 27 Spiel-Aufgaben werden Notiz oder Grind+ „nur bei bauen“ | |
| Mi 24.02. | REACH „Das erste Bild“ | Notiz „nichts Werbliches“; V078 am Do 25.02. | [Z-Q32] |
| Di 23.02. | Verpackung | + Verpackungslizenz, LUCID-Meldung | [T 3.2] |
| Sa 13.03. | ASK + Playtest | + **Mess-Abend 3** (vorgezogen) | Cash Hebel 8 |
| Fr 19.03. | DETAIL „37 mal 37“ | V094 „45 × 45“ | [S 3.6] |
| Fr 19.03. | Restzahlung | + Backstop Mi 24.03. | Cash |
| So 21.03. | Vorbestellung schließen | nur der Preis 149 € endet, Stufe 2 bis So 04.04. | |
| Mo 22.03. · Mo 29.03. | Spiel-Launch | Scroll-Story Stufe 4 still, Feld-Kapitel öffentlich | [W] |
| Do 22.04. | Drop | + 17:55 DM an Top-Werber, Live 18:00–18:30 | |
| Sa 24.04. | Packen Tag 2 | + **Drop-Abend** (nur mit Packhilfe) | [C 6.4] |
| jeden So | Wochenreview | + Gate, Kassencheck, Marken-KPIs | |
| neu | — | 10′ Community an Werktagen ohne Post; 2 Grind+-Karussells pro Woche | [K 4.6] |

### 15.1 Überarbeitung nach der Kritik (Rev. 6.1, 07.10. abends)

Alle Änderungen stehen im Docket (`skeleton.json`) am genannten Tag. Abweichungen vom Vorschlag der Kritik stehen in Abschnitt 20.

| # | Thema | Wo im Docket | Was jetzt gilt |
|---|---|---|---|
| 1 | Quellenlage | Sa 10.10. | Netz freischalten, dann prüft Claude die Liste in Abschnitt 19 |
| 2 | Stufe 2: Auslöser und zwei Geldtermine | Mo 14.12., Mi 13.01., jeden So 17.01.–14.03., So 21.03., Mi 24.03. | live bei Nr. 035 (frühestens 14.01., spätestens 21.03., 20:00); 32 bis Di 16.03., +8 bis Mi 24.03. (5.4) |
| 3 | Mess-Abend 2b, Gate W26 | So 24.01., Mi 27.01., So 14.03., Di 29.12. | Mi 27.01. statt Sa 30.01.; „ausgezahlt bis Di 16.03.“; Auszahlungsdauer messen |
| 4 | CTA-Versprechen | Sa 10.10., Di 24.11., Mi 13.01., Do 14.01. | „Die Liste kauft zuerst. 35 Paar zum Vorbestellpreis.“; 18:00 Mail an die ganze Liste, 17:55 DM an Reservierer und Zusagen |
| 5 | Website ohne Stufe 2 | Mo 21.12., Do 07.01., Fr 05.03., Mo 22.03. | `tt_produkt_stufe2`, Raster, Knopf bis 04.04., eigener CTA, Mail am 22.03. (13) |
| 6 | Nummernlogik | Sa 19.12., So 04.04., Di 06.04. | 001–035 · 036–060 · 061–065 · 066–067 · Rest; ohne Lücke; bei 75 Stufe 2 nur 036–045 |
| 7 | Bestand je Größe | Sa 19.12., Mo 11.01., Do 14.–So 17.01. | 35 nach gr-Tags verteilen, 72 h zweimal täglich umschichten, Satz „Deine Größe ist weg?“ |
| 8 | Proto bleibt bei dir | Di 27.10., Mo 07.12., Fr 11.12., Mo 04.01. | schriftlich vereinbart; Waschserie erst mit dem PP |
| 9 | Proto-Runde braucht Zeit | Fr 04.12.–So 13.12. | Mi und Do je 60′ Kern, Sa 90′ mit Läden, 6 Video-Calls à 15′, Batch am 13.12. 60′ |
| 10 | Fabrikliste ungeprüft | Sa 10.10., So 11.10., Mo 12.10., Mi 14.10. | Prüfliste 1.5 als Kern 40′; ohne Netz 4 weitere selbst (60′); Nachzügler bis Mi |
| 11 | Tech-Pack-Lücken | Do 08.10., Fr 09.10., So 11.10., Di 03.11., Mi 18.11. | Wash-Fotos, Verschleißkarte, Innenbein, Lab Dips, Stofflappen als Waschstandard |
| 12 | Patches fürs PP, PP-Prüfung | Mo 07.12., Mo 04.01. | Express mit Tracking; Knopf, Nieten, Labels mit Faser- und GPSR-Angabe |
| 13 | Ramadan und Feiertage | Mi 21.–Fr 23.10., Mo 26.10., So 22.11., Fr 05.02., Mo 08.02. | fragen, Konditionen bis 27.10. mittags, Proforma bis 30.10., Produktionsplan mit Antworten |
| 14 | A.TR | Di 27.10., Do 03.12. | für jede Sendung, auch Proto und PP |
| 15 | Patch-Serie | Do 17.12., Fr 22.01., So 24.01. | Adresse, Incoterm, Zollweg schriftlich; Fotobeweis; sonst Call |
| 16 | Stoff und Endkontrolle | Mi 06.01., Mi 03.02., So 14.02., Fr 19.03. | Stoff reserviert; Endkontroll-Nachweis in der PO, ohne Nachweis keine Zahlung |
| 17 | Liefertext | Mo 14.12., Do 07.01., Do 15.04. | ein Satz überall; Mail mit Erstattungsangebot, wenn die Ware nach 25.04. kommt |
| 18 | Drop-Tag | Di 09.03., Fr 26.03., Do 25.03., Mi 21.04., Do 22.04., Fr 23.04. | Kampagne 2, LIVE-Mail, Theme-Notiz, Sofort-Maßnahmen, Helfer für DMs |
| 19 | E-Mails | Fr 09.10. bis Mo 22.03. | Willkommens-Mail, Werkstatt-Mails, Fristende-Mail (9.5) |
| 20 | Retouren | Do 21.01., Mo 12.04., So 25.04. | Umtausch nur bei Bestand, Nummer neu verkaufen, Grund als Feld, täglich ab 26.04. |
| 21 | Helfer legal | Di 13.10., Sa 13.02., Do 25.03. | Steuerberater-Frage 10, Aushang erst danach, Vertrag und Anmeldung bis 25.03. |
| 22 | Kasse „ungeplant“ | Di 13.10. | Zeile mit Schätzungen, je 146 € +1 Vorbestellung (5.4) |
| 23 | Gewerbe | Mi 14.10. | falls nötig ummelden |
| 24 | Datenschutz am selben Tag | Di 13.10., Do 15.10., Mi 11.11., Di 24.11. | je Absatz am Tag der Datenerhebung, 24.11. nur Endkontrolle |
| 25 | Livegang der Startseite | Fr 09.10., Sa 10.10. | 15′-Checkliste, nie das Canvas als Bild, Impressum in den Profilen |
| 26 | Streichpreis | Di 24.11., Do 07.01. | „Vorbestellpreis 149 € bis 21.03. · ab 22.04. 169 €“ (9.3) |
| 27 | Zipper/Polo: Widerruf, GPSR | Di 24.11., Di 16.03., Fr 09.10., Mi 04.11. | Hotline-Fragen, Pflichtangaben auf den Seiten, Nackenlabel mit Adresse |
| 28 | Bestellbestätigung | Mo 14.12., Mo 11.01. | Textblock, abgebrochene Bestellungen testen und einschalten |
| 29 | „Nummer reservieren“ | Sa 05.12., Mo 07.12., So 29.11. | heißt „Platz in der ersten Stunde sichern“ |
| 30 | „Bring 3“ und Link-Schema | Sa 10.10., Mi 11.11., Mi 18.11. | utm = Kanal, ref = Person; Code und Danke-Link in der Theme-Kopie |
| 31 | Zeitsteuerung | Mo 11.01., Do 14.01. | Test „in 20 Minuten“; 17:50 und 17:58 Handgriffe |
| 32 | Sprache des Shops | Sa 07.11., Di 24.11., Sa 28.11., Fr 18.12. | englisch → EN-Rechtstexte und EN-Seite; deutsch → nur Versand nach DE |
| 33 | Größenfeld | Mi 11.11., So 25.04. | „kleiner als W30“, „größer als W38“, Auswertung nach dem Drop |
| 34 | Belegtabelle | Mo 19.10., Mi 21.10., Videos mit Bedeutung | Gate Mi 21.10.; V011, V015, V108–V112 nur mit Beleg |
| 35 | V004 | Mo 19.10. | nur Maßtabelle, Schnitt schwarz-weiß, ein Element |
| 36 | Bildregeln | Di 27.10., Sa 07.11., Do 12.11., Fr 26.03., Fr 09.04., Fr 16.04., Di 20.04. | V119 nach dem 07.11., CD-T06 → V125, Reihenfolge B · A · E · C · D · B2, CD-T13 ohne „wir“ |
| 37 | 22.04. | Mi 14.04., Mo 19.04., Do 22.04. | Teilsperre, Antwortbaustein |
| 38 | 08.03. | Do 04.03., Fr 05.03., Mo 08.03. | Event-Tipp Fr 05.03., 09:00 |
| 39 | Orte für die Abende | Mi 18.11., Sa 12.12., So 13.12. | Voranfrage, 90′, Giggster am 13.12. |
| 40 | Shoot | Do 15.10., Sa 09.01., Fr 15.01., Mi 17.02. | Teppich, Fotograf mit Rechten, Feld, 24 Countdown-Motive |
| 41 | Drop-Abend und Packen | Fr 05.03., Fr 12.03., Sa 24.04., So 25.04. | Bestätigung bis 12.03.; Packen Tag 2 an Helfer oder So |
| 42 | Zipper/Polo | Do 29.10., Mo 12.04., So 25.04. | Digitizing beauftragen, Check, wöchentliche Sammelbestellung |
| 43 | Größensplit | Di 02.02. | mit Stufe-2-Annahme, Creator und Reserve |
| 44 | Marke und Baum-Referenz | Fr 16.10., Di 20.10. | Markenrecherche; Ursprung der Referenz vor dem 28.10. |
| 45 | Haftung, REACH | So 11.10., Mo 12.10., Fr 06.11., Mi 03.02. | REACH-Frage und Erklärung, Preis Produkthaftpflicht |
| 46 | Gates ohne „sonst“ | So 18.10., 08.11., 29.11., 20.12., 07.02., 07.03., 28.03. | jedes Gate hat jetzt eine Gegenmaßnahme (7.2) |
| 47 | B-Zeitachse | Sa 31.10. und alle „schieben“-Gates | 7.4 |
| 48 | Shopify Email | Mo 30.11., So 28.02. | Domain authentifizieren; Regel bei zu kleinem Kontingent |
| 49 | Bank | Mo 02.11., Di 29.12. | Auslandsüberweisung als Test, Tageslimit ≥ 3.100 €, Auszahlungskonto |
| 50 | Zusage gegen Vielleicht | Di 13.10., alle Zusagen-Gates | zwei Spalten, Gates zählen nur „Zusage“ |
| 51 | „Herkunfts-Tag“ | überall | heißt „Quellen-Tag“; Regel zur ethnischen Herkunft (9.3, Punkt 12) |
| 52 | V005 | Di 20.10., Mi 21.10. | Ausnahme D im Video selbst nennen, sonst V120 |
| 53 | Zahlen in 4, 5.3, 7.2 | Fr 06.11., Fr 23.04. | 77–82 %, 240–660, 90 % als Schätzung |

---

## 16 · Risiken

| # | Risiko | Frühwarnung | Gegenmaßnahme |
|---|---|---|---|
| 1 | **Kein Ausreißer**, Liste bleibt bei 700–1.600 | G1/G2 ab W6 | Varianten-Regel, Hook-Tests, Wärme-Kette, Gate 24.01. |
| 2 | **Steuer nicht im Budget** (~1.150 €, 40 statt 32 Vorbestellungen) | Steuerberater 13.10. | mit 1.150 € planen, DAP verhandeln (27.10.), Steuer getrennt von der Restzahlung: 40 ausgezahlt bis Mi 24.03. über Stufe 2, sonst Brücke |
| 3 | **Fabrikpreis oder Stiche zu hoch** | Angebote 19.10., Vorschau 09.11. | Ampel, Stichdeckel, 75 Stück, Fallback-Serp |
| 4 | **Auszahlung verzögert** | Support-Antwort 30.10., Test 29.12. | nur ausgezahltes Geld zählt, PayPal parallel |
| 5 | **Symbol-Shitstorm** (Sichel + Ähren + Rot, Stoppelfeld) [Z-Q34][Z-Q35][Z-Q51] | Schnelltest 09.10., G7 | Serp-Test, Wortliste, Bildregeln, Sperrtermine, nie diskutieren, nie Kritik löschen |
| 6 | **Vertrauenslücke Vorbestellung** | G10, G11, Handheber < 20 am 13.01. | Checkliste 9/9, Geld-zurück, Mess-Abende, Gesicht |
| 7 | **Liste altert** (6 Monate Warten) [M-Q25] | Klickrate der Drop-Mails | alle 2–4 Wochen ein Ereignis, Broadcast, „Day X“ |
| 8 | **Fabrik fällt aus** nach der Anzahlung | Antwortzeiten, Inline-Fotos 16.02./01.03. | Gates bis PP, Reserve-Fabrik warm, Bankdaten-Regel, Brücke |
| 9 | **Lieferverzug** (Ramadan ca. 08.02.–09.03. und Fest, Ostern, Zoll; Feiertage TR 28./29.10., PT 01./08.12., ungeprüft) | kein Tracking bis 24.03.; Antworten aus den Calls 21.–23.10. | Produktionsplan mit Ramadan-Arbeitszeit (05.02.), Puffer bis 15.04., B-Zeitachse 2 mit Drop 29.04., Mail mit Erstattungsangebot, wenn die Ware nach 25.04. kommt |
| 10 | **Recht:** Kennzeichnung, Reservierung, LUCID, GPSR, Lieferdatum, CTA-Versprechen (UWG), Streichpreis (PAngV § 11), Widerruf bei Zipper/Polo (§ 312g BGB), Helfer (Minijob, Mindestlohn), REACH, Produkthaftung, Markenrecht „Novalife“, Urheberrecht am Baum (alles ungeprüft, keine Rechtsberatung) | — | Rechtstexte-Service mit Hotline 24.11. (Fragenliste dort), Steuerberater 13.10. (Frage 10), REACH-Erklärung in der PO, Haftpflicht-Preis 06.11., Markenrecherche 16.10., Baum-Referenz 20.10., Netz-Prüfliste 19 |
| 11 | **Deine Zeit** | zwei Wochenreviews ausgefallen | Spiel streichen, Kern ≤ 120′, Grind+ wirklich optional |
| 12 | **Scope-Drift** | „nur noch schnell …“ | jede neue Idee kostet eine alte; Gegenrechnung vor jeder Stickerei |
| 13 | **Shopify Email reicht nicht** für 6 Drop-Mails an ~3.000 Adressen (Freikontingent ungeprüft); Spam-Risiko ohne authentifizierte Domain | Prüfung So 28.02. | Domain am 30.11. authentifizieren; Preis ins Blatt „Kasse“ oder T−14 und T−7 nur an Aktive der letzten 90 Tage [T 1] |
| 14 | **Mess-Abend ohne Ort** | Voranfrage 18.11., Zusage bis Sa 19.12. | vier Läden parallel, Giggster-Suche am 13.12., Notfall bei dir |
| 15 | **Größe ausverkauft, andere frei** (Shopify führt Bestand je Größe; ein Gesamtdeckel von 35 geht ohne App nicht, Fachwissen, ungeprüft) | Vorbestellungen je Größe in den ersten 72 h | 35 nach gr-Tags verteilen, zweimal täglich umschichten, Satz „Deine Größe ist weg? Stufe 2 oder Liste.“ |
| 16 | **Proto weg oder verändert** vor der Proto-Runde | — | Proto bleibt bei dir (27.10.), Waschserie erst mit dem PP |
| 17 | **Lesart am Drop-Tag** (22.04. ist Lenins Geburtstag, Allgemeinwissen, ungeprüft) | G7 | Teilsperre: kein Serp im Hero, keine Ernte-Hooks, Antwortbaustein; Termin bleibt |
| 18 | **Retouren in der Drop-Woche** (Widerruf der Vorbesteller läuft bis ~21.04.) | Retourengrund | Ablauf vom 21.01., Bearbeitung ab 12.04., täglich ab 26.04. |

---

## 17 · Deine Entscheidungen

| Bis | Frage | Mein Rat |
|---|---|---|
| **Fr 09.10.** | Serp-Farbe nach Testregel, B2-Kante, V1 Nummer, V5 Patch, V6 Karte, Taschenklappe, Nackenlabel (mit Novalife-Adresse), „goldene Nähte“, Namen nach außen | wie Abschnitt 12 |
| So 11.10. | Innenbein-Gradierung +1,0 oder +1,5 | kein eigener Rat, mir fehlen Daten. Die Spec steht auf +1,0; ohne Grund für +1,5 bleibt es dabei |
| Do 15.10. | Wie viel Familie in den Content; Teppich für den Shoot leihen | über Gegenstände, nicht über Länder |
| So 18.10. | Pixel-Spiel | streichen, Scroll-Story B |
| Di 20.10. | Baum-Referenz: eigene oder fremde Vorlage? | fremd → Claude zeichnet eine eigene Fassung vor dem 28.10. |
| Di 27.10. | DAP oder DDP | DAP, damit die Steuer nicht schon in der Restzahlung steckt |
| Sa 07.11. | Sprache der Hooks und damit das Liefergebiet; Bildregel „keine Seitenansicht links“ | Test entscheidet; deutsch → nur Versand nach DE bis zum Drop; Bildregel halten |
| So 29.11. | „Platz in der ersten Stunde sichern“ A (10 €) oder B (kostenlos) | B, A nur bei Liste < 170 und grünem Recht |
| Fr 11.12. | Creator-Abmachung 1 Clip + 1 Story | ja |
| Mo 14.12. | Liefertext | „Lieferung bis spätestens 30.04.2027, geplant Anfang April“, überall derselbe Satz |
| Di 15.12. | Geld-zurück-Regel, Vorbestellgeld bis 01.02. unangetastet | ja |
| **Sa 19.12.** | Stufe 2 zu 169 € statt Kontingent 45; Nummern 001–035 · 036–060 · 061–065 · 066–067 · Rest | ja |
| Do 31.12. | Brücke 1.500 € in der Familie | anfragen, nur als Versicherung |
| So 24.01. | Mess-Abend 2b (Mi 27.01.) | ja, wenn am 13.01. < 60 Reservierungen + Zusagen oder Vorbestellungen unter Soll |
| Mo 01.02. | Mengenformel 100/75; Notfall-Option Zipper bei 7–9 | ja / bereithalten |
| Fr 05.03. | Drop-Abend Sa 24.04.; Countdown-Stand | ja nur, wenn Packen Tag 2 an die Helfer geht oder auf So 25.04. rückt / nur unter ~146 € |
| nach dem Drop | Marke „Novalife“ anmelden; W28 in den Größenlauf | Markenrecherche vom 16.10. und Nachfrage „kleiner als W30“ auswerten, erst dann rechnen |

---

## 18 · Quellen

**Selbst geprüft in dieser Aufgabe: 0.** WebSearch meldete am 07.10.2026 „web search budget is used up (limit: 200 WebSearch calls per turn, shared by every agent in it)“. WebFetch auf www.berlin.de: „EGRESS_BLOCKED“. Bei der Überarbeitung 6.1 am selben Abend: WebSearch wieder „budget is used up“, WebFetch auf www.gesetze-im-internet.de „EGRESS_BLOCKED“. Neue externe Angaben aus 6.1 sind deshalb als „ungeprüft“ markiert und stehen in Abschnitt 19. Die folgenden Quellen haben die Recherche-Agenten heute in dieser Sitzung per Websuche gesehen, meist als Such-Auszug. Güte A/B/C laut `markt.md`.

**Markt (`markt.md`)**
- [M-Q5] Bans on communist symbols: https://en.wikipedia.org/wiki/Bans_on_communist_symbols
- [M-Q6] Kapital: https://bdgastore.com/products/14oz-denim-kountry-motocross-pants · [M-Q7] Bode: https://bdgastore.com/products/embroidered-denim-knolly-brook-trouser-mrs24bt039 · [M-Q11] Denim Tears × Levi's: https://stockx.com/es-mx/denim-tears-x-levis-cotton-wreath-jean-black · [M-Q16] Gerrit Jacob: https://www.clothbase.com/items/439bf663_gerrit-jacob-blue-overdyed-jeans_gerrit-jacob
- [M-Q23] C · LaunchList, Waitlist → Kauf: https://getlaunchlist.com/blog/convert-waitlist-to-paying-customers
- [M-Q25] B · Lenny's Newsletter, Waitlist conversion: https://www.lennysnewsletter.com/p/what-is-good-waitlist-conversion
- [M-Q26] B · LaunchBoom, Prelaunch email list: https://www.launchboom.com/crowdfunding-tips/how-to-build-a-prelaunch-email-list/
- [M-Q27] B · LaunchBoom, Kickstarter promotion: https://www.launchboom.com/crowdfunding-tips/how-to-promote-your-kickstarter-campaign-updated/
- [M-Q29] C · Adam Webb, VIP list conversion: https://adamwebb.pro/blog/kickstarter-vip-conversion-problem
- [M-Q31] A · Kuppuswamy/Bayus, U-Form: https://yannigroth.com/2013/02/24/the-dynamics-of-backer-support-in-crowdfunding-findings-from-kickstarter · https://arxiv.org/pdf/1607.06839
- [M-Q35] B · Littledata, Conversion Mode: https://www.littledata.io/ecommerce-conversion-rate
- [M-Q36] B · Unbounce, Landingpage-Median: https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/
- [M-Q37] B · Socialinsider, TikTok-Benchmarks 2026: https://www.socialinsider.io/social-media-benchmarks/tiktok
- [M-Q38] B · Socialinsider, Reels: https://socialinsider.io/blog/instagram-reels-statistics/
- [M-Q40] B · eMarketer zu HypeAuditor, Nano-Creator: https://www.emarketer.com/content/smaller-creators-deliver-efficiency-roi-pressure-mounts
- [M-Q42] C · ostend.digital, Meta-Kosten: https://ostend.digital/meta-ads-kosten-kompass/ · [M-Q43] C · Adamigo: https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026
- [M-Q44] A · Bitkom, Retouren: https://www.bitkom.org/Presse/Presseinformation/Online-Shopping-Jeder-zehnte-Kauf-geht-zurueck
- [M-Q48] A · Aggarwal, Jun, Huh (2011), Knappheit: https://experts.umn.edu/en/publications/scarcity-messages-a-consumer-competition-perspective/
- [M-Q51] C · LaunchList, Referral: https://blog.getlaunchlist.com/blog/waitlist-referral-program-guide
- [M-Q54] C · ATTN Agency, Pop-up: https://www.attnagency.com/blog/popup-shop-experiential-marketing-roi-measurement-dtc-2026

**Zielgruppe (`zielgruppe.md`)**
- [Z-Q1] Destatis, PM 13.04.2026: https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/04/PD26_128_125.html
- [Z-Q2] bpb, (Spät-)Aussiedler: https://www.bpb.de/nachschlagen/zahlen-und-fakten/soziale-situation-in-deutschland/61643/spaet-aussiedler
- [Z-Q10] Goethe-Institut, Russische Orte in Berlin: https://www.goethe.de/ins/ru/de/kul/mag/21445554.html
- [Z-Q23] ARD/ZDF-Medienstudie 2025: https://www.media-perspektiven.de/fileadmin/user_upload/media-perspektiven/pdf/2025/MP_31_2025_ARD_ZDF-Medienstudie_Social_Media_zwischen_Wachstum_und_Saettigung_Nutzungsmuster_und_Plattformdynamiken_in_Deutschland.pdf
- [Z-Q26] Preisanker: https://www.zalando.de/damenbekleidung-jeans/eightyfive · https://www.careofcarl.com/en/carhartt-wip-landon-pant-robertson-denim-black-stone-washed · https://www.levi.com/DE/de_DE/bekleidung/herren/501-levis-original-jeans/p/005013279
- [Z-Q32] Vyshyvanka Day: https://en.wikipedia.org/wiki/Vyshyvanka_Day
- [Z-Q34] National emblem of Belarus: https://en.wikipedia.org/wiki/National_emblem_of_Belarus · [Z-Q35] State Emblem of the Soviet Union: https://en.wikipedia.org/wiki/State_Emblem_of_the_Soviet_Union
- [Z-Q39] Slavic Native Faith and politics: https://en.wikipedia.org/wiki/Slavic_Native_Faith_and_politics
- [Z-Q42] On the Historical Unity of Russians and Ukrainians: https://en.wikipedia.org/wiki/On_the_Historical_Unity_of_Russians_and_Ukrainians · [Z-Q43] Pan-Slavism: https://en.wikipedia.org/wiki/Pan-Slavism
- [Z-Q46] KIIS, September 2025: https://english.nv.ua/nation/kiis-poll-91-of-ukrainians-now-hold-negative-views-of-russia-4-positive-50555297.html
- [Z-Q48] CBOS 2025: https://www.cbos.pl/SPISKOM.POL/2025/K_013_25.PDF
- [Z-Q51] Holodomor, Gedenktag am 4. Samstag im November: https://www.ukrainianworldcongress.org/november-marks-month-of-remembrance-for-holodomor-victims/ · https://holodomormuseum.org.ua/en/news-museji/the-law-on-five-ears-of-grain-is-a-bloody-tool-of-the-holodomor-organizers/
- [Z-Q52] Meta, Detailed targeting: https://developers.facebook.com/blog/post/2021/12/08/updating-metas-detailed-targeting-options/
- [Z-Q58] Mauerpark (Sekundärquelle): https://berlinecho.de/flohmarkt-mauerpark-oeffnungszeiten-berlin/
- [Z-Q59] Kunstraum Heartspace: https://www.berlin.de/tickets/freizeit/embroidery-workshop-50fe0879-2b66-46b8-bf66-806c8c366965/

**Berlin (`berlin.md`)**
- [B-1] Burg & Schild: https://rawlooks.com/store/burg-und-schild-berlin/
- [B-6] Firmament: https://www.firmamentberlin.com/about · [B-8] Civilist: https://magazine.032c.com/magazine/more-than-a-shop-alex-foley-s-civilist
- [B-10] GATE Store: https://www.overkillshop.com/pages/gate-store
- [B-11] Konk (2014): https://www.yonder.fr/cityguides/berlin/shopping/konk · [B-12] TextilWirtschaft, Konk: https://www.textilwirtschaft.de/fashion-management/berliner-designer-store-konk-richtet-sich-neu-aus-62843
- [B-15] Sing Blackbird: https://www.top10berlin.de/de/cat/shopping-271/vintage-mode-3141/sing-blackbird-vintage-5580
- [B-16] Soto: https://www.complex.com/style/2012/10/dope-interiors-soto-store-berlin
- [B-23] Studio183: https://bikiniberlin.de/en/shopping/studio183/
- [B-34] Mauerpark: https://www.berlin.de/special/shopping/flohmaerkte/1998222-1724959-flohmarkt-am-mauerpark.html
- [B-35] Nowkoelln Flowmarkt: https://www.berlin.de/en/shopping/markets/flea-markets/1762126-2983302-nowkoelln-flowmarkt.en.html
- [B-37] Holzmarkt-Flohmarkt: https://www.berlin.de/en/shopping/markets/flea-markets/9680476-2983302-holzmarkt-flohmarkt.en.html
- [B-38] Berlin Vintage & Heritage Market: https://www.visitberlin.de/en/event/berlin-vintage-and-heritage-market
- [B-39] Holy Shit Shopping: https://www.festivalsindeutschland.de/festival/holy-shit-shopping-berlin · [B-40] https://www.berlin.de/weihnachtsmarkt/2208886-3496862-holy-shit-shopping.html
- [B-46] Giggster Pop-up: https://giggster.com/de/find/berlin--de/pop-up
- [B-58] MEK: https://www.berlin.de/museum/3108962-2926344-museum-europaeischer-kulturen.html · [B-59] SMB, Antrag Film/Foto: https://www.smb.museum/presse/formulare/antrag-auf-presseberichterstattung/

**Website (`website.md`)**
- [W-W3] Phaser 3.90.0, Dateigröße selbst gemessen aus dem npm-Paket (1.196.122 Byte roh, 314.863 Byte gzip)

**Intern:** `docs/uebergabe-time-travel.md`, `docs/time-travel-drop-plan.md` (Rev. 5.3), `docs/produkt-spec_rev13.md`, `r5/weeks_r5.json`, `rev6/strategie_entwurf_wachstum.md`, `_cash.md`, `_marke.md`, `rev6/research/*.md`, `rev6/research/content_library.json`.
**Eigene Rechnungen [R]:** Funnel-Szenarien, Kalender (4. Samstag im November 2026 = 28.11.; Ostersonntag 2027 = 28.03.; Sommerzeit ab 28.03.2027; Ramadan 1448 im tabellarischen Islam-Kalender 08.02.–09.03.2027, 1. Schawwal 10.03.2027, ±1–2 Tage gegenüber dem amtlichen Kalender; alle Wochentage der neuen Termine), Werktags-Stichtage (5.4), B-Zeitachse (7.4), Zeitsummen aus `skeleton.json`. Generator: `build_skeleton.py` und `weeks_meta.py` im Scratchpad dieser Sitzung, Rev. 6.1 per `kritik61.py` und `minuten.py` im Scratchpad.

**Vor dem Geldausgeben selbst öffnen:** [M-Q26], [M-Q27] (Reservierung), Shopify-Preise und Auszahlungsregeln, Rechtstexte-Anbieter, Standpreise [B-35][B-37], Shopify-Email-Kontingent, Verpackungslizenz.

---

## 19 · Netz-Prüfliste (sobald das Netz frei ist)

Claude prüft diese Punkte gegen die Primärquelle, **bevor** du die Regel umsetzt. Bis dahin gilt die Angabe als ungeprüft. Reihenfolge nach Fälligkeit.

| # | Was | Primärquelle (zu öffnen) | Fällig vor | Wo im Plan |
|---|---|---|---|---|
| 1 | Feiertage Türkei: 28.10. nachmittags, 29.10.; Ramadan 2027 und Ramadan-Fest | Diyanet bzw. amtlicher Kalender der Türkei | Mo 26.10. | 3.2, Docket 21.–27.10. |
| 2 | Feiertage Portugal 01.12. und 08.12. | amtlicher Kalender Portugal | So 22.11. | Docket 22.11. |
| 3 | Minijob oder kurzfristige Beschäftigung, Mindestlohn 2027, Unfallversicherung für Helfer | Minijob-Zentrale, Bundesregierung, Steuerberater | Sa 13.02. (Aushang) | Steuerberater-Frage 10 |
| 4 | PAngV § 11 (Preisermäßigung, niedrigster Preis der letzten 30 Tage) | gesetze-im-internet.de, PAngV | Di 24.11. | 9.3, Website Schritt 11 |
| 5 | § 312g BGB (Widerruf bei Waren nach Kundenspezifikation), § 312j BGB, Art. 246a EGBGB (Liefertermin) | gesetze-im-internet.de | Di 24.11. | Zipper/Polo, Liefertext |
| 6 | UWG bei „Die Liste kauft zuerst“ und Creator-Kennzeichnung | Rechtstexte-Hotline | Di 24.11. | 9.3 |
| 7 | REACH: Nickelabgabe bei Metallteilen mit Hautkontakt, Azofarbstoffe | ECHA, REACH Anhang XVII | Mo 12.10. (RFQ) | Tech Pack, PO |
| 8 | Feiertag Berlin 08.03. (Frauentag) | berlin.de | Do 04.03. | Event-Tipp |
| 9 | Shopify: Bestand je Variante, Zeitsteuerung, abgebrochene Bestellungen, Domain-Authentifizierung, Willkommens-Automation, Email-Freikontingent | help.shopify.com | jeweils vor dem Docket-Tag | Docket |
| 10 | Zoll auf Patches und Muster in die Türkei, A.TR für Proto und PP | zoll.de, Fabrik | Mo 07.12. | Docket 07.12., 17.12. |
| 11 | Lenins Geburtstag 22.04.1870 | Nachschlagewerk | Mi 14.04. | 9.2 |
| 12 | ARD/ZDF-Medienstudie 2025, Instagram- und TikTok-Wert | PDF [Z-Q23] | Sa 07.11. | 4 |

---

## 20 · Nicht übernommen oder anders umgesetzt

Alle 53 Punkte der Kritik sind umgesetzt (Liste in 15.1). An diesen Stellen weicht die Umsetzung vom Vorschlag ab:

1. **Markenrecherche am Fr 16.10. statt Di 13.10.** Der Dienstag hat mit Steuer (Fragen 9 und 10), Blättern, Tally und Datenschutz schon 115 Min. Kern. Vor den Labels (04.11.) und der Patch-Anfrage (28.10.) reicht der Freitag.
2. **Stufe-2-Check ab So 17.01. statt „So 18.01.“** Der 18.01.2027 ist ein Montag [R]. Der erste Sonntag nach der Öffnung ist der 17.01.
3. **Ursprung der Baum-Referenz am Di 20.10. statt „vor dem 28.10.“** Er muss vor V005 (Mi 21.10.) klar sein, weil das Video die Ausnahme D selbst nennt. Den Satz „folgt meiner eigenen Vorlage“ sagst du nur, wenn die Klärung das trägt; sonst V120.
4. **Englische Produktseite am Fr 18.12. statt Sa 12.12.** Der Samstag trägt Läden und drei Treffen (90′). Die Vorbestellung öffnet erst am 14.01.
5. **Produktseite mit echten Bildern am So 13.12. statt Sa 12.12., auf 30′ gekürzt.** Sonst läge der Samstag bei 145 Min.
6. **Handheber-DMs am Di 15.12. statt Mo 14.12.** Der Montag bekommt die Bestellbestätigung (20′) und läge sonst bei 135 Min.
7. **Werkstatt-Mails am 03.12. und am 21.03. werden am Vortag terminiert,** nicht am Tag selbst geschrieben. Beide Tage sind voll (Proto-Ankunft, Wochenreview).
8. **Mess-Abend 2b:** Standard ist Mi 27.01., Do 28.01. nur, wenn die Auszahlung höchstens 2 Werktage braucht. Nach der 3-Werktage-Regel ist Donnerstagsgeld erst am Di 02.02. da.
9. **Willkommens-Mail am Fr 09.10. ohne „Bring 3“-Link.** Der Link existiert erst ab Do 15.10. und kommt dann dazu.
10. **Nummern ohne Lücke.** Die feste Aufteilung 001–035 · 036–060 · 061–065 · 066–067 gilt bei vollem Verkauf. Füllt sich Stufe 2 nicht, rücken Creator, Reserve und Drop beim Packen nach. Sonst stünden auf den Hangtags Lücken, und deine Regel vom 01.10. („Creator direkt nach den Vorbestellungen“) wäre gebrochen.
11. **Waschserie mit dem PP ab Mo 04.01.** (statt „nach dem 13.01.“ mit dem Proto). Das PP muss laut Spec Teil 4 ohnehin fünf Wäschen bestehen, und V058 (22.01.) braucht das Material.
12. **Notfall-Leiter Stufe 3** heißt nicht mehr „Stufe 2 öffnen“. Mit dem neuen Auslöser öffnet Stufe 2 von selbst. Zwei Preise gleichzeitig (149 € frei und 169 € offen) wären sinnlos.
13. **Lab Dips:** Die L*-Werte misst die Fabrik. Ein eigenes Messgerät plane ich nicht ein, weil keins im Budget steht. Dein Werkzeug ist der freigegebene Stofflappen bei Tageslicht.
14. **W4 Do–So und Sa 16.01. liegen über 120 Min. Kern.** Die Kritik verlangt dort zusätzliche Kern-Aufgaben (Prüfliste, Wash-Fotos, Checkliste, V002/V003, Umschichten). Kürzen ließe sich nur am kritischen Pfad. Ich habe es offen markiert (14).

**Was ich nicht direkt geändert habe:** `content.md` und `website.md` selbst. Diese Aufgabe umfasst `strategie.md` und `skeleton.json`. Die Korrekturen für beide Dateien stehen verbindlich in 9.3 (CTA) und 13 (Website) und in den Docket-Aufgaben am jeweiligen Tag. Beim Bau des Dockets gelten sie vor den Recherche-Dateien.
