# Regeln für die Wochen-Autoren · Docket Rev. 6

Du schreibst Tage des „Time Travel Drop Docket“ für Ernest Veskimäe (Novalife, Denim, Berlin). Drop Do 22.04.2027, 19:00.
Ziel 10.000 € Umsatz (64 Jeans netto, 72 brutto). Heute ist Mi 07.10.2026. Ernest liest jeden Tag oben „Heute“ und arbeitet die Aufgaben ab.
Er will es so detailliert, dass er nie nachdenken muss: was er tut, wohin er geht, welches Video er dreht, mit Links.

## Harte Regeln
- Das Skelett deines Briefings ist verbindlich: Jeder Stichpunkt wird zu einer Aufgabe. Info-Zeilen → "N". Gate-Zeilen → "D" mit den Gegenmaßnahmen als Schritte. „Grind+“-Zeilen → plus:true. Nichts fallen lassen. Kleinigkeiten darfst du zusammenlegen, die Reihenfolge am Tag ordnest du nach Uhrzeit und Dringlichkeit.
- Kern (ohne plus, ohne Spiel) höchstens 120 Min. pro Tag. Ausnahmen nur 08.–11.10., 16.01., 20.02., 30.03.–02.04., 06.–07.04., 22.–25.04.
- Fakten: Keine neuen URLs, Adressen, Preise, Termine erfinden. Nur aus dem Briefing, rev6/briefs/links.md (mit grep durchsuchen), strategie.md, den Recherche-Dateien oder Rev. 5.3. Vorbehalte übernehmen („vor Ort prüfen“, „ungeprüft“, „Schätzung“).
- Keine Aufgabe über Claudes Netzwerk, Sandbox, Proxy oder „Netz freischalten“. Was ungeprüft ist, prüft Ernest selbst („Link öffnen und prüfen“) oder er lässt es Claude per Prompt in einem normalen Chat mit Websuche prüfen.
- Keine Politik. Subjekt ist das Muster, nicht das Volk. Nie „authentisch“. Den Lebensbaum nie „slawisch“ nennen. Wortliste nach außen (9.3). Bildregeln (9.3). Bis zum Proto am Do 03.12.2026: kein fertiges Teil und kein Mockup, das wie eins aussieht. Sperrtermine: 23.–29.11. kein Ernte- und kein Serp-Bild, Sa 28.11. kein Post; Mi 24.02.2027 nichts Werbliches; Teilsperre am 22.04. (9.2).
- Keine Adressen scrapen. Die Gmail-Entwürfe an Hidrock und Lapiztola gehen nie raus. Ernest sendet und postet selbst.
- Stil: Deutsch, Du-Form, kurze klare Sätze, keine Floskeln, keine Gedankenstriche als Stilmittel. Hooks und Captions englisch (Hook zusätzlich deutsch), außer die Strategie verlangt Deutsch.
- Vorlagen (RFQ, Nachfassen, Call, Verhandlung, Absage, Referenz-Check, Berliner Sticker, Patch, Creator-DM) stehen im Docket unter „Referenz → Vorlagen“: nicht abschreiben, darauf verweisen. Neue Texte schreibst du direkt in die Schritte oder als Prompt an Claude.

## Standard-Bausteine
- Drehtag (meist Sonntag-Batch): Video-Briefing komplett ("v" mit Shots, Ort, Ton, Text im Bild), Drehreihenfolge nach Orten, Kamera 9:16, Licht von vorn, je Shot 3 Takes.
- Posttag: "v" mit Caption + Schritte: 17:55 Video in TikTok hochladen (Business-Konto, Musik nur aus der Commercial Music Library), Caption einfügen, 18:00 posten · gleich danach als Reel auf Instagram und als Short auf YouTube · Reel in die Story mit Link-Sticker · 15 Min. Kommentare beantworten (Regeln 9.3 Punkt 9).
- Jeder Sonntag: Wochenreview mit den Gates aus 7.1 (als Schritte: welche Zahl prüfen, was tun wenn darunter), „Zahlen ins Cockpit eintragen“ (bestätigte Warteliste aus Shopify → Kunden → Segment „E-Mail-Abonnenten“, Follower TikTok + Instagram gesamt, bezahlte Vorbestellungen; Docket-Abschnitt „Zahlen-Cockpit“), die Zeile an Claude aus 9.4 als Prompt.
- Orte und Websites gehören immer in "o" (Shopify-Admin https://admin.shopify.com, TikTok, Instagram, CapCut, Google Sheets, Läden, Märkte, Ämter mit Adresse).



## Dateiformat · rev6/weeks/w{n}.json (UTF-8, valides JSON)

{
 "n": 5, "phase": "P1", "goal": "Wochenziel in einem Satz",
 "kpi": [{"k": "Warteliste", "ziel": "40 (Alarm 15)"}, {"k": "Posts", "ziel": "3 + 2 Grind+"}],
 "days": { "2026-10-12": [Aufgabe, …], … jedes Datum der Woche (W4 nur 2026-10-08 bis 2026-10-11) }
}

Aufgabe = {
 "c": "B" | "C" | "V" | "D" | "A" | "S" | "N",
      B BUILD Produkt/Fabrik/Sample · C CONTENT Videos/Posts/E-Mails · V VERKAUF Warteliste/Netz/Zusagen/Creator/Berlin/Presse/Abende
      D ENTSCHEIDUNG (jedes Gate) · A ADMIN Shop/Recht/Steuer/Versand · S SPIEL (nur bei „Spiel bauen“) · N Notiz (nur "c" und "t")
 "t": "Titel, aktiv, max. ~70 Zeichen, feste Uhrzeit vorn („18:00 · V001 posten“)",
 "m": 25,                      ganze Minuten, realistisch
 "plus": true,                 nur bei optionalen Grind+-Aufgaben
 "s": ["…", "…"],              3–8 konkrete Schritte: Klickpfad („Shopify → Kunden → Segmente“), Adresse, was sagen/schreiben, was mitnehmen, welche Datei
 "f": "Fertig, wenn … (prüfbar)",
 "p": "fertiger Prompt an Claude zum Kopieren (wenn Claude Texte, Auswertungen, Rechnungen, Zeichnungen liefert). Platzhalter in [eckigen Klammern]. Der Prompt beginnt mit einem Satz Kontext („Projekt Time Travel, Docket W5 …“), weil ihn Ernest in einen neuen Chat im Projekt „novalife time travel“ einfügt.",
 "o": [{"n": "Name", "u": "https://…", "a": "Adresse · Öffnungszeit", "h": "Hinweis, z. B. vor Ort prüfen"}],
 "v": {                        nur bei Aufgaben, die ein Video/Karussell/Story drehen oder posten
   "id": "V001", "slot": "BUILD", "dauer": "20–25 s", "plattform": "TikTok + Reels + Shorts",
   "hook_en": "…", "hook_de": "…", "shots": ["…"], "ort": "konkreter Drehort",
   "ton": "…", "text": "Text im Bild", "cta": "CTA der Phase (Tabelle unten)",
   "caption": "fertige Caption EN mit CTA und 4–6 Hashtags", "check": "Regel-Check in einem Satz"
 },
 "x": "s"                      nur bei Spiel-Aufgaben
}

Prüfen: python3 rev6/build/check_week.py N  → muss „0 Fehler“ melden.


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

## 14 · Zeitbudget und Grind+

- **Kern:** im Schnitt **72 Minuten pro Tag**, zusammen ~240 Stunden bis 25.04. [R aus `skeleton.json`, Stand 6.1; vorher 68 Min. und ~226 Stunden]. Höchstens **120 Minuten**, mit fünf bewussten Ausnahmen: **Do 08.10. bis So 11.10.** (125–135 Min.: Freeze, Tech Pack und Fabrikanfrage sind der kritische Pfad, der Freeze ist schon einmal gerutscht) und **Sa 16.01.** (125 Min., Mess-Abend 1 plus Umschichten der Größen).
- **Woher die +14 Stunden kommen:** Prüfliste der Fabriken, Wash-Fotos, Checkliste vor dem Livegang, Proto-Runde als Kern (2 × 60′ + 6 Video-Calls), Werkstatt-Mails, Bestellbestätigung, Retouren, Helfer anmelden, Zipper/Polo-Check, Umschichten in den ersten 72 Stunden. Dafür ist die Proto-Runde kein Grind+ mehr: Das Gate am 13.12. hängt an ihr.
- **Ausnahmen** (lange Tage, ~25 Stunden): Shoot Sa 20.02. · Warenannahme und Prüfung Di 30.03.–Fr 02.04. · Vorbestellungen packen Di 06.–Mi 07.04. · Drop und Packen Do 22.–Fr 23.04. · Packen Tag 2 an die Helfer, sonst So 25.04. vormittags · So 11.10. (60′, nur wenn Claude kein Netz hat).
- **Abende** sind als Kern auf 90–110 Minuten begrenzt. Die Verlängerung bis 21:00 steht als Grind+.
- **Grind+** (~50 Stunden, alles optional): Karussells und Varianten, Laden-Runden, Mauerpark, Holy Shit Shopping, Mess-Abend 2b (nur bei Gate), Waschserie mit dem PP, Feld-Drehs, Countdown-Stand, Spiel nur bei „bauen“.
- **Rangfolge, wenn die Zeit nicht reicht:** Fabrik und Sample > Geld-Gates > Abende > Pflicht-Posts > Netz und Zusagen > Grind+.
- Am Tag nach einem langen Abend nur Pflicht.

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