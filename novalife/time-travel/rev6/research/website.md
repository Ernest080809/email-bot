# Website und Spiel · Time Travel

Stand: Mi 07.10.2026, abends. Für Ernest. Teil der Docket-Neuplanung (Rev. 6).
Grundlage: Plan Rev. 5.3 Abschnitt 5.1, Spiel-Bauplan im Docket Rev. 5.3, Spec Rev. 13, `zielgruppe.md`, `community.md`, `tools.md` (alle in diesem Ordner bzw. `docs/`).
Quellen stehen als [W-Nummer] im Text und vollständig in Abschnitt 13. **Schätzung** = meine Rechnung oder Annahme. **Vor Ort prüfen** = in dieser Sitzung nicht belegbar, Prüfschritt steht dabei.

---

## Kurzfassung

**Empfehlung: Bau Variante B, die Scroll-Story „Der Weg zur Hütte“, als feste Startseite. Das Pixel-Spiel (A) baust du nur, wenn am Fr 05.02. vier Bedingungen stimmen (Abschnitt 11). Bei 1–2 Stunden am Tag: A streichen.**

**Warum:** B kostet rund 18 Stunden in 24 Schritten (Schätzung), davon ~10,5 Stunden vor dem 05.02. Diese Stunden brauchst du sowieso: Countdown, Wartelisten-Formular mit Quellen- und Größen-Tags, Nummern-Raster 001–100, Vorbestell-Zustände. A kommt mit 20–40 Stunden obendrauf (Schätzung, Docket Rev. 5: ~40 h). A lädt Phaser 3.90.0 mit 1,20 MB roh und 315 KB gzip (eigene Messung [W3]) und stellt sich zwischen Besucher und Kauf. Dass ein Spiel mehr verkauft, ist nirgends belegt. Du misst es selbst.

**Deine Idee bleibt drin.** In B ist Scrollen gleich Laufen: Feld bei Sonnenuntergang → Jeans, Zipper, Polo → Hütte → Teppich. Die Bilder sind SVG-Silhouetten, die Claude Code erzeugt. Du musst nichts zeichnen.

**Architektur (A und B):** Kopie deines Live-Themes mit eigenen Sections. Ein Zeit-Modul `tt-clock.js` kennt sechs Zustände, von „Warteliste“ bis „Ausverkauft“. Die Uhrzeit kommt vom Server (Date-Header [W16]), nicht vom Handy. Liquid-„now“ ist gecacht [W8] und taugt nicht. Das echte Schloss bleibt Shopify. Um 19:00 musst du kein Theme umschalten. Das alte Theme bleibt als PLAN B liegen, Umschalten mit einem Befehl [W7].

**Vor dem 05.02. (Schritte 1–12, ab Sa 31.10.):** Werkzeuge auf dem Mac, Theme-Kopie mit Git, CLAUDE.md mit deinen Regeln, Countdown, Formular, Prozess-Story (live Mi 18.11.), echte Proto-Fotos (Fr 11.12.), Nummern-Raster (Sa 19.12.), Vorbestell-Zustände (Di 05.01.), UTM-Links und Tags (Sa 09.01.).

**Neu gegenüber Rev. 5:** Die Shopify CLI ist jetzt Version 4.8.5 und braucht Node.js ab 22.12 [W7]. Phaser 4 ist seit 10.04.2026 stabil (aktuell 4.2.1), aber größer [W1][W3]. Beim Spiel bleibt es bei 3.90.0.

**Nicht geprüft (Seiten in dieser Sitzung gesperrt):** Future Publishing, Theme-Obergrenze, Freikontingent von Shopify Email, Pfad zum Double-Opt-in, Verhalten der In-App-Browser. Jeder Punkt hat einen Testschritt im Bauplan.

**Design-Vorschläge, du entscheidest:** Palette aus Sonnenuntergang und Teppich, 17 Farben, nur ein Blau (Denim, dunkel). Alle Textpaare liegen bei mindestens 5,8:1 Kontrast. Das Nummern-Raster als 10 × 10 Kreuzstich. Nach außen „Time Travel“, „Kreuzstich-Band“, „Achtstern“. Sichel und Ähren nie freigestellt als Emblem.

---

## 1 · Quellenlage

- **Gesperrt in dieser Sitzung:** shopify.dev, help.shopify.com, community.shopify.com, developer.mozilla.org, w3.org, web.dev, aseprite.org, Steam, docs.phaser.io. Die Websuche war für diesen Lauf aufgebraucht.
- **Deshalb geprüft an Primärquellen auf anderem Weg:**
  - Shopify CLI 4.8.5 selbst installiert und die Hilfetexte gelesen [W7].
  - Die Liquid-Referenz von Shopify, die in der CLI mitgeliefert wird (`dist/data/*.json`; die Einträge verweisen auf shopify.dev, die Online-Fassung war gesperrt) [W8].
  - Shopify-eigene Repos auf GitHub: Dawn, Horizon [W10]–[W13].
  - Phaser und GSAP direkt aus dem npm-Paket, Dateigrößen selbst gemessen [W3][W6].
  - MDN und WCAG aus ihren eigenen GitHub-Repos [W16]–[W21], die Zeitzonen-Datenbank der IANA [W22], die Doku von Claude Code [W23][W24].
- **Nicht belegt, im Text markiert:** Future Publishing (zeitgesteuertes Veröffentlichen), Höchstzahl der Themes, Upload-Grenze für Theme-Dateien, Kompression im Shopify-CDN, Double-Opt-in-Pfad, mehrere Tags in einem Formularfeld, Freikontingent Shopify Email, Aseprite-Preis, BFSG-Ausnahme, In-App-Browser von Instagram und TikTok.

---

## 2 · Zwei Varianten im Vergleich

| | **A · Pixel-Spiel „Das Feld“** | **B · Scroll-Story „Der Weg zur Hütte“** |
|---|---|---|
| Was der Besucher tut | tippt, Figur läuft durchs Feld, Stationen öffnen Karten, Tür der Hütte | scrollt, das Feld zieht vorbei, Kapitel mit Fotos, Ornament-Bedeutungen, Nummern 001–100, Countdown, Formular |
| Technik | Phaser 3.90.0 in einer eigenen Section, Aseprite-Grafiken | Liquid-Sections, ~25 KB eigenes JavaScript, SVG-Silhouetten, Fotos vom Shopify-CDN |
| Dein Aufwand | 8 Zusatzschritte, ~11 h reine Bauzeit, realistisch **20–40 h** mit Fehlersuche und Zeichnen (Schätzung) | 24 Schritte, **~18 h** (Schätzung), ~10,5 h davon vor dem 05.02. |
| Was du selbst können musst | Pixel-Art in 12 Dateien (Stiltest 27.12. zeigt, ob das trägt) | Fotos machen, Texte freigeben |
| Gewicht | Phaser allein 1.196.122 Byte roh, 314.863 Byte gzip [W3] + Grafiken ≤ 150 KB (Schätzung) | eigene Dateien ≤ 95 KB roh (CSS 15, JS 25, Feld-SVGs 25, Motiv-SVGs 30, Budget 3.10) + Fotos |
| Wirkung (Schätzung, nicht belegt) | hoher Wiedererkennungswert, teilbar als Bildschirmaufnahme, eigener Post „Das Feld ist offen“ | erklärt das Produkt: Ornament, Nummer, Preis, Größe. Weniger Wow, mehr Kaufgründe |
| Risiko für den Verkauf | **mittel:** steht zwischen Besucher und Kasse, Ladezeit, In-App-Browser, Bugs am Drop-Tag | **niedrig:** normale Seite, läuft ohne JavaScript, Shop-Link immer oben |
| Risiko für deinen Plan | **hoch:** frisst 20–40 h, die im Februar und März im Content fehlen (Kampagne, Shoot, Countdown-Videos) | niedrig |
| Fallback | B ist der Fallback | altes Theme „PLAN B“ |

**Empfehlung bei 1–2 Stunden am Tag:** B bauen, A streichen.

**Die Begründung in einem Satz:** Die 100 Paar verkauft die Warteliste, nicht die Startseite. Jede Stunde im Spiel fehlt bei den Videos, die die Liste füllen (Plan Risiko 5 und 6).

**Was du mit B von der Spielidee behältst:** den Weg (Feld → Stationen → Hütte → Teppich), den Sonnenuntergang, die Tür, die um 18:00 mit dem Schlüssel und um 19:00 für alle aufgeht. Was du verlierst: das Gefühl, selbst zu laufen.

**Wenn du A trotzdem willst:** A ersetzt in B nur ein Kapitel (Schritt 16). Alles andere (Zeit, Formular, Nummern, Shop-Button, PLAN B) ist gemeinsam und schon gebaut. A ist dann eine Zusatzschicht, kein zweites Projekt.

---

## 3 · Gemeinsame Basis (gilt für A und B)

### 3.1 Architektur

```
Besucher (Instagram/TikTok-Bio, QR, E-Mail)
   │  ?utm_source=…  ?ref=…  ?key=… (nur E-Mail T−1h)
   ▼
Shopify-Storefront · Theme „TT Story“ (Kopie deines Live-Themes)
   ├─ templates/index.json   → nur tt-Sections + Footer
   ├─ sections/tt-hero       → Countdown, Formular, Listenstand, Shop-Button
   ├─ sections/tt-kapitel    → Story-Kapitel (Blöcke: Bild, Text, Motiv)
   ├─ sections/tt-feld-scroll→ „Der Weg zur Hütte“ (B)  ODER  sections/tt-feld (A, Phaser)
   ├─ sections/tt-nummern    → Raster 001–100 aus dem Lagerbestand
   └─ assets/tt-clock.js     → Serverzeit + Zustand, sendet Ereignis „tt:state“
          │ fetch('/cart.js') → Date- und Age-Header [W16][W17]
          ▼
   Zustand: WARTELISTE · VORBESTELLUNG · ZWISCHENZEIT · SCHLÜSSEL · LIVE · AUSVERKAUFT
          │
          ▼
Shopify-Admin (das echte Schloss)
   Produkte: Vorbestellung NVL-TT-01 · Drop NVL-TT-01 · Zipper · Polo
   Sichtbarkeit im Onlineshop: zeitgesteuert oder von Hand (vor Ort prüfen)
   Kunden: Tags aus dem Formular (tt-warteliste, src-…, gr-…)
```

**Entscheidungen dahinter:**
1. **Kein zweiter Server, keine zweite Domain.** Alles liegt im Theme. Der Theme-Code ist mit Git versioniert.
2. **Ein Theme für alle Phasen.** Die Seite wechselt ihre Zustände selbst (3.3). **Abweichung vom Plan Rev. 5:** Dort sollte um 19:00 das Theme „Drop 22.04.“ veröffentlicht werden. Mit Zustands-Logik fällt dieser Handgriff am Drop-Abend weg. Das Umschalten bleibt nur für PLAN B. **Du entscheidest.**
3. **Liquid rendert alles Wichtige als Text vor.** JavaScript verschönert nur. Die Liquid-Referenz warnt: Ein Zeitstempel aus `'now'` „spiegelt die Zeit, zu der das Liquid zuletzt gerendert wurde … abhängig vom Caching“ [W8]. Deshalb steht im HTML nur das feste Datum, der Countdown läuft per JavaScript.
4. **Formulare werden normal abgeschickt, nicht per fetch.** Shopify schützt Storefront-Formulare mit hCaptcha und einer Abfrage „let us know you're not a robot“ [W9]. Ein normales Absenden übersteht diese Abfrage. Wie fetch darauf reagiert, ist ungeprüft.
5. **Live-Theme, Veröffentlichen und Push macht nur Ernest.** Claude Code arbeitet an der Kopie (Regel in CLAUDE.md, Anhang A).

**Welches Theme hast du?** Der Docket ging von Dawn aus. Dawn ist bei Version 16.0.0 [W12]. Shopify baut inzwischen Horizon als „Flaggschiff einer neuen Generation“ mit Theme-Blöcken [W13]. Eigene Sections funktionieren in beiden. Schritt 2 lässt Claude Code nachsehen, welches Theme in deinem Shop live ist.

### 3.2 Dateistruktur

```
~/Claude/Novalife/website/tt-theme/        Git-Repo, privat auf GitHub
├─ CLAUDE.md                     Regeln für Claude Code (Anhang A), wird nicht hochgeladen
├─ .shopifyignore                schließt CLAUDE.md, docs/, tools/ vom Upload aus [W7]
├─ docs/TERMINE.md               Zustände und Uhrzeiten
├─ tools/                        nur lokal
│  ├─ budget-check.mjs           summiert Dateigrößen roh + gzip, bricht bei Überschreitung ab
│  ├─ flaggen-check.mjs          sucht in PNG/SVG nach Hellblau (nur A und Feld-SVGs)
│  └─ motive/                    SVG-Motive aus design/*.svgfrag (Kreuzstich-Band, Münztasche, Achtstern)
├─ config/settings_schema.json   + Gruppe „Time Travel“ (3.11)
├─ templates/index.json          Startseite = tt-Sections
├─ sections/
│  ├─ tt-hero.liquid             Countdown, Formular, Listenstand, Shop-Button
│  ├─ tt-kapitel.liquid          ein Kapitel = Überschrift + Blöcke (max. 50 Blöcke je Section [W8])
│  ├─ tt-nummern.liquid          Raster 001–100
│  ├─ tt-feld-scroll.liquid      B: Feld als Scroll-Szene
│  └─ tt-feld.liquid             A: Spiel (nur bei „bauen“)
├─ snippets/
│  ├─ tt-countdown.liquid        statisches Datum + <time>, JS macht den Countdown
│  ├─ tt-warteliste-form.liquid  {% form 'customer' %} mit Tags [W8][W10]
│  └─ tt-shop-button.liquid      fester Link „Direkt zum Shop“, Text je Zustand
└─ assets/
   ├─ tt-clock.js                Zeit + Zustand (gemeinsam)
   ├─ tt-story.js / tt-story.css Scroll-Story, Bewegung-aus-Schalter
   ├─ tt-nummern.js              Raster nachladen alle 60 s
   ├─ tt-feld-*.svg              Silhouetten für B
   └─ (nur A) phaser-3.90.0.min.js, tt-feld.js, tt-figur.png/.json …
```

### 3.3 Zeit und Zustände

Alle Zeiten Europe/Berlin. Die Sommerzeit beginnt 2027 am So 28.03. (EU-Regel „letzter Sonntag im März, 1:00 UTC“ [W22], nachgerechnet). Deshalb wechselt der Offset von +01:00 auf +02:00.

| Zustand | Von | Bis | Was die Startseite zeigt | „Direkt zum Shop“ führt zu |
|---|---|---|---|---|
| **WARTELISTE** | jetzt | Do 14.01.2027, 19:00 (`2027-01-14T19:00:00+01:00`) | Countdown „Vorbestellung öffnet in …“, Formular, Prozess-Story | Formular (Anker `#liste`), Text „Auf die Liste“ |
| **VORBESTELLUNG** | 14.01., 19:00 | So 21.03.2027, 20:00 (`2027-03-21T20:00:00+01:00`) | „Vorbestellung offen · 149 € statt 169 €“, Nummern-Raster, Countdown „Vorbestellpreis endet in …“ | Produktseite Vorbestellung |
| **ZWISCHENZEIT** | 21.03., 20:00 | Do 22.04.2027, 18:00 (`2027-04-22T18:00:00+02:00`) | Countdown „Drop in …“, ab 29.03. das Feld-Kapitel öffentlich, Formular „Hol dir den Schlüssel“ | Formular, Text „Drop 22.04. · 19:00“ |
| **SCHLÜSSEL** | 22.04., 18:00 | 22.04., 19:00 (`2027-04-22T19:00:00+02:00`) | mit `?key=…` aus der E-Mail T−1h: „Die Tür ist offen“. Ohne Schlüssel: Countdown 60 Minuten | mit Schlüssel: Kollektion. Ohne: Formular |
| **LIVE** | 22.04., 19:00 | bis ausverkauft | Tür offen, drei Produkte, Nummern-Raster füllt sich | Kollektion „Time Travel“ |
| **AUSVERKAUFT** | Lager der Drop-Jeans = 0 | — | „Alle 100 vergeben“, Zipper und Polo weiter bestellbar, Formular „Liste für Drop 2“ | Kollektion (Zipper, Polo) |

**Wie die Uhrzeit entsteht (tt-clock.js):**
1. `fetch('/cart.js', {cache: 'no-store'})`. Aus der Antwort den Header `Date` lesen. Er enthält „Datum und Uhrzeit, zu der die Nachricht entstand“ [W16].
2. Falls ein Header `Age` dabei ist, die Sekunden dazurechnen. `Age` gibt an, wie lange ein Objekt in einem Proxy-Cache lag [W17].
3. Abstand zur Handy-Uhr merken. Alle 5 Minuten und beim Zurückkehren in den Tab neu holen.
4. Klappt das nicht: Handy-Uhr nehmen und das intern markieren. Die Anzeige bleibt trotzdem ungefähr richtig. Gekauft werden kann sowieso erst, wenn Shopify die Produkte freigibt.
5. **Testmodus:** `?t=2027-04-22T18:59:30+02:00` überschreibt die Uhr, aber nur, wenn in den Theme-Einstellungen „Testmodus“ angehakt ist. Am 17.04. wird der Haken entfernt (Schritt 22).

### 3.4 Das echte Schloss

- **Die Website zeigt Zustände nur an. Verkauft wird nur, was in Shopify im Onlineshop sichtbar ist.**
- Plan 5.1 sagt: Produkte per Future Publishing auf den 22.04., 18:00 terminieren. **Vor Ort prüfen:** Die Shopify-Hilfe dazu war in dieser Sitzung gesperrt. Der Test steht in Schritt 20 (Generalprobe): Testprodukt zu 1 € auf „in 30 Minuten“ terminieren und beobachten.
- **Falls es die Terminierung so nicht gibt:** Produkte bleiben bis 18:00 im Status „Entwurf“. Um 18:00 stellst du sie von Hand auf „Aktiv“. Das dauert unter einer Minute pro Produkt. Am Drop-Tag steht das dann um 17:55 in deinem Ablauf.
- **Der Schlüssel ist Erzählung, kein Schutz.** Er steht in den Theme-Einstellungen und damit im Seitenquelltext. Wer zwischen 18:00 und 19:00 die Produkt-URL kennt, kommt auch ohne Schlüssel rein. Bei 100 Paar reicht das (so schon im Plan 5.1).

### 3.5 Warteliste

**Formular:** `{% form 'customer' %}` erzeugt laut Shopify ein Formular, um „einen Kunden ohne Konto anzulegen … zum Beispiel für eine Newsletter-Liste“ [W8]. Dawn macht es genau so: verstecktes Feld `contact[tags]` mit dem Wert `newsletter`, dazu `contact[email]` [W10]. Nach dem Absenden sagt `form.posted_successfully?`, ob es geklappt hat [W10]. `return_to: 'back'` schickt den Besucher auf dieselbe Seite zurück [W8].

**Felder:**

| Feld | Pflicht | Wohin |
|---|---|---|
| E-Mail | ja | `contact[email]` |
| Größe W30 / W32 / W34 / W36 / W38 / „weiß ich noch nicht“ | nein | als Tag `gr-w32` usw. |
| Quelle (unsichtbar, aus der URL) | automatisch | Tag `src-instagram`, `src-tiktok`, `src-qr`, `src-email`, sonst `src-direkt` |
| Empfehlungs-Code (unsichtbar, aus `?ref=`) | automatisch | Tag `ref-<code>` (passt zur Ref-Mechanik in `community.md`) |
| Ort des Formulars | automatisch | Tag `tt-story`, `tt-feld` (A) oder `tt-huette` |

**Warum Größe schon bei der Anmeldung:** Am Sa 19.12. legst du das Kontingent und die Größenverteilung der Vorbestellung fest. Bis dahin hast du echte Größen aus der Liste statt der Startannahme 14/30/30/18/8 (Spec 1.3). Kostet den Besucher einen Tipp und ist freiwillig.

**Ungeprüft, im Test (Schritt 5) klären:**
- Speichert Shopify mehrere Tags aus einem Feld mit Komma (`tt-warteliste,src-instagram,gr-w32`)? **Wenn nicht:** ein zusammengesetzter Tag `tt-ig-w32`. Ein Tag ist ein Text, das geht immer.
- Bekommt eine Adresse, die schon Kunde ist, neue Tags?
- Wo genau schaltest du das Double-Opt-in ein (Docket W4: „Einstellungen → Kundendatenschutz“, `community.md` 4.4: Pfad ungeprüft)?

**Text unter dem Formular:** kommt aus deinem Rechtstexte-Generator (Plan 7: e-recht24 07.10., Rechtstexte-Service 24.11.). Die Datenschutzerklärung muss die Quellen-Tags nennen („wir speichern, über welchen Link du dich eingetragen hast“, `community.md`).

### 3.6 Nummern 001–100 und Listenstand

**Nummern-Raster:** 100 Felder, 10 × 10, gezeichnet als Kreuzstich-Raster. Jedes vergebene Feld ist ein gestickter Kreuzstich in Rot und Weiß, jedes freie ein leeres Kästchen.

**Woher die Zahl kommt (nur echte Zahlen):**
- `variant.inventory_quantity` liefert in Liquid den Lagerbestand einer Variante [W8]. Achtung: Wird das Inventar nicht verfolgt, liefert das Feld „die Zahl der verkauften Stücke“ [W8]. Deshalb muss bei beiden Jeans-Produkten „Inventar verfolgen“ an sein.
- Vorbestellt = Startmenge Vorbestellung (35, bei > 25 bis 01.02. dann 45) minus Summe der Bestände aller Größen.
- Im Drop verkauft = Startmenge Drop (58, bei Kontingent 45 dann 48) minus Summe der Bestände.
- 5 Creator-Paare und 2 Reserve sind fest vergeben (Plan 3.2: 93 verkäuflich).
- Reihenfolge wie beim Packen (Entscheidung 01.10.): Vorbestellungen ab 001 nach Bestelldatum, dann Creator, dann Drop. Auf der Seite: Felder 001 bis Zahl der Vorbestellungen in Rot-Weiß. Ab 21.03. folgen 7 Felder „Creator und Reserve“ in Gold. Ab 22.04. füllt der Drop den Rest.
- **Keine Daten zu einzelnen Nummern** (wer, wann). Die gibt es nicht öffentlich, und erfinden geht nicht.

**Live-Aktualisierung:** Die Section wird alle 60 Sekunden neu geholt, solange sie sichtbar ist (`/?section_id=tt-nummern`). Dawn lädt Teile der Seite genau so nach (`?section_id=` in `cart.js` und `facets.js`) [W11]. Ob Shopify die Section dabei aus einem Cache liefert, ist **ungeprüft**. Deshalb steht unter dem Raster „Stand: 19:04“. Test in Schritt 10: Bestand im Admin ändern, Zeit stoppen, bis das Raster springt.

**Listenstand („1.240 auf der Liste“):** Eine Zahl aller Abonnenten gibt es in Liquid nicht (in der Objekt-Referenz [W8] nicht gefunden). Deshalb trägst du sie jeden Sonntag im Wochenreview von Hand in die Theme-Einstellungen ein, mit Datum: „1.240 auf der Liste · Stand So 10.01.“ Dauer 3 Minuten. Nur die echte Zahl aus Shopify (Kunden, gefiltert nach E-Mail-Abo).

### 3.7 Shop-Anbindung

- **„Direkt zum Shop“** sitzt fest oben rechts, mindestens 44 × 44 px, als echter `<a>`-Link außerhalb von Canvas und Animation. Text und Ziel je Zustand: Tabelle 3.3.
- **Preise kommen aus Shopify**, nicht aus dem Text. `{{ product.price | money }}` für 149 € und 169 €. Wenn du einen Preis änderst, stimmt die Startseite automatisch.
- **Produkte in den Theme-Einstellungen:** über den Einstellungstyp `product` und `collection` [W8] wählst du die Vorbestellung, das Drop-Produkt, Zipper, Polo und die Kollektion aus. Kein Link wird von Hand getippt.
- **Ausverkauft:** Sobald die Drop-Jeans auf 0 steht, zeigt die Seite Zipper und Polo als „auf Bestellung, Versand innerhalb von 3 Wochen“ (Plan 3.2) und das Formular „Liste für Drop 2“.

### 3.8 Analytics

**Was du misst (wöchentlich im Wochenreview, 5 Minuten):**

| Kennzahl | Woher | Wofür |
|---|---|---|
| Sitzungen Startseite | Shopify Analytics | Nenner |
| Neue Abonnenten mit Tag `tt-story` / `tt-feld` / `tt-huette` | Kunden, Filter nach Tag | **Anmeldequote der Startseite** = Anmeldungen ÷ Sitzungen |
| Anmeldungen je `src-…` | Kunden, Filter nach Tag | Welcher Kanal bringt Adressen, nicht nur Likes |
| Größenverteilung `gr-…` | Kunden, Filter nach Tag | Kontingent am 19.12. und Größen der 100 |
| Vorbestellungen | Bestellungen | Schwellen 10 (01.02.) und 32 (19.03.) |

**UTM-Links (einmal anlegen, Schritt 12):**
- Instagram-Bio: `https://DEINE-DOMAIN/?utm_source=instagram&utm_medium=bio&utm_campaign=tt`
- TikTok-Bio: `…?utm_source=tiktok&utm_medium=bio&utm_campaign=tt`
- QR auf Papier in Berlin: `…?utm_source=qr&utm_medium=print&utm_campaign=tt`
- E-Mails: `…?utm_source=email&utm_medium=newsletter&utm_campaign=tt-<datum>`

`tt-clock.js` liest `utm_source` und schreibt daraus den Quellen-Tag ins Formular. Das funktioniert ohne Cookies, weil der Besucher die Angabe mit seiner Anmeldung selbst abschickt. Trotzdem gehört es in die Datenschutzerklärung (3.5).

**Eigene Ereignisse (optional, erst ab Schritt 12):** Shopify kennt „Custom Events“, die Händler über eine `publish`-Methode senden. Der Typ `CustomEvent` steht im Paket `@shopify/web-pixels-extension` [W14]. Dawn 15.5.0 hat „Unterstützung für Standard-Storefront-Events“ eingebaut [W12]. Die genaue Aufrufsyntax im Theme und wie die Einwilligung (Cookie-Banner) dazu greift, ist hier **ungeprüft**. Claude Code prüft das in Schritt 12 an der Shopify-Doku auf deinem Mac. Vorschlag für fünf Ereignisse: `tt_kapitel` (Nummer), `tt_motiv_offen` (Name), `tt_formular`, `tt_shop_klick` (Ort), `tt_feld_station` (nur A).

### 3.9 Barrierefreiheit

Ziel: WCAG 2.2, Stufe AA. Das ist auch gut für den Verkauf, weil die Seite dadurch auf kleinen Handys und im grellen Licht lesbar bleibt.

| Regel | Quelle | Umsetzung |
|---|---|---|
| Text-Kontrast mindestens 4,5:1, großer Text 3:1 | WCAG 1.4.3 [W21] | Palette 6.2, alle Paare 5,8:1 bis 15,9:1 (nachgerechnet) |
| Tippziele mindestens 24 × 24 CSS-Pixel | WCAG 2.5.8 [W21] | bei uns 44 × 44 px |
| Alles per Tastatur bedienbar | WCAG 2.1.1 [W21] | Kapitel-Navigation, Formular, Motiv-Karten als `<button>`, im Spiel ← → Enter Esc |
| Bewegung, die automatisch startet und länger als 5 Sekunden läuft, muss man anhalten können | WCAG 2.2.2 [W21] | Schalter „Bewegung aus“ (wiegender Weizen, Parallax) |
| Wunsch nach weniger Bewegung respektieren | `prefers-reduced-motion` [W18], WCAG 2.3.3 [W21] | dann kein Parallax, keine Weizen-Animation, Kapitel springen statt gleiten |
| Countdown nicht jede Sekunde vorlesen | eigene Regel | `<time datetime>`, Ansage für Screenreader nur minütlich (`aria-live="polite"`) |
| Spiel ist nicht die einzige Quelle | eigene Regel | Canvas `aria-hidden`, alle Stationen auch als HTML-Liste „Ohne Spiel ansehen“ |

**BFSG:** Laut `tools.md` sind Kleinstunternehmen mit Dienstleistungen ausgenommen. Das ist dort als Wissen markiert, nicht belegt. Beim Rechtstexte-Anbieter bestätigen lassen. Die Regeln oben gelten trotzdem, weil sie Verkäufe schützen.

### 3.10 Performance-Budget

| Teil | Budget | Woher die Zahl |
|---|---|---|
| Eigene CSS-Dateien (tt-*) | ≤ 15 KB roh | Schätzung |
| Eigene JS-Dateien ohne Phaser | ≤ 25 KB roh | Schätzung |
| Feld-SVGs (B) zusammen | ≤ 25 KB roh | Schätzung |
| Motiv-SVGs (Band, Münztasche, Achtstern) | ≤ 10 KB je | Schätzung |
| Erstes großes Bild | ≤ 120 KB, über `image_url` mit Breite und `srcset` [W8] | Schätzung |
| Spiel A: Phaser 3.90.0 | 1.196.122 Byte roh, 314.863 Byte gzip | eigene Messung [W3] |
| Spiel A: Grafiken (12 PNG) | ≤ 150 KB | Schätzung (Pixel-Art mit 17 Farben ist klein) |
| Spiel A gesamt | **≤ 1,5 MB roh** (Plan 5.1) | 1,20 + 0,15 + 0,04 = 1,39 MB |
| Erstes Bild auf dem Handy | **unter 2 Sekunden im Mobilnetz** (Plan 5.1) | Test in Chrome mit Netzwerk-Drosselung |

**Wichtigste Regel für A:** Phaser wird erst geladen, wenn jemand auf „Ins Feld“ tippt. Vorher sieht man ein Standbild des Feldes (≤ 40 KB). So belastet das Spiel die Startseite nicht.

**Ungeprüft:** ob das Shopify-CDN JavaScript komprimiert ausliefert. Prüfen in Schritt 7: Chrome → Entwicklertools → Netzwerk → Spalte „Content-Encoding“. Theme Check hat eine Prüfung „Prevent Large JavaScript bundles“, die mit einer *komprimierten* Größe rechnet. Sie ist standardmäßig aus [W15].

### 3.11 Theme-Einstellungen (Gruppe „Time Travel“)

Eine Datums-Einstellung gibt es in Shopify nicht. Die Typen sind u. a. `text`, `checkbox`, `number`, `product`, `collection`, `url`, `richtext`, `image_picker`, `font_picker` [W8]. Zeiten werden deshalb als Text mit Offset eingetragen.

| Einstellung | Typ | Wert |
|---|---|---|
| `tt_zeit_vorbestellung` | text | `2027-01-14T19:00:00+01:00` |
| `tt_zeit_preisende` | text | `2027-03-21T20:00:00+01:00` |
| `tt_zeit_schluessel` | text | `2027-04-22T18:00:00+02:00` |
| `tt_zeit_drop` | text | `2027-04-22T19:00:00+02:00` |
| `tt_zeit_feld_oeffentlich` | text | `2027-03-29T18:00:00+02:00` |
| `tt_schluessel` | text | z. B. `weizen-0422` (neu setzen am 15.04.) |
| `tt_testmodus` | checkbox | an bis Sa 17.04., dann aus |
| `tt_produkt_vorbestellung` | product | Vorbestellung NVL-TT-01 |
| `tt_produkt_drop` | product | NVL-TT-01 |
| `tt_produkt_zipper`, `tt_produkt_polo` | product | NVL-TT-02, NVL-TT-03 |
| `tt_kollektion` | collection | „Time Travel“ |
| `tt_start_vorbestellung` | number | 35 (45, falls am 01.02. erhöht) |
| `tt_start_drop` | number | 58 (48 bei Kontingent 45) |
| `tt_reserviert` | number | 7 (5 Creator + 2 Reserve) |
| `tt_liste_zahl`, `tt_liste_datum` | number, text | jeden Sonntag von Hand |

---

## 4 · Variante B · Scroll-Story „Der Weg zur Hütte“

### 4.1 Ablauf in fünf Stufen

Die Seite wächst mit dem Projekt. **Gezeigt wird nur, was es gibt** (Plan 0 und 10).

| Stufe | Ab | Inhalt | Regel |
|---|---|---|---|
| **1 · Prozess** | Mi 18.11.2026 | Kopf mit Countdown bis 14.01. und Formular · Papiertest · Kreuzstich-Raster als Zeichnung · Fabriksuche in echten Zahlen · Teppich | **kein fertiges Teil, kein Mockup**. Motive nur flach, nie auf eine Jeans-Silhouette gelegt |
| **2 · Das Muster** | Fr 11.12.2026 | Detailfotos vom Proto (03.12.) und Mini-Shoot (08. und 10.12.) zu jedem Element, Bedeutungen | Bedeutungstexte nur mit Beleg (4.2) |
| **3 · Die Nummern** | Do 14.01.2027, 19:00 | Vorbestellung offen, Nummern-Raster, Countdown bis Preisende | nur echte Zahlen |
| **4 · Der Weg zur Hütte** | Mo 22.03. still, Mo 29.03. öffentlich | Feld-Kapitel als Scroll-Szene, Shoot-Fotos (20.02.), Countdown bis 22.04. | Himmel nie hellblau über Weizen |
| **5 · Die Tür** | Do 22.04.2027 | Schlüssel 18:00, live 19:00, später „ausverkauft“ | Shop-Link immer oben |

### 4.2 Kapitel und Textentwürfe

Texte sind Entwürfe nach Sprachregel 8.2. Du gibst jeden Satz frei.

**K0 · Kopf** (immer oben)
> **Time Travel**
> 100 Jeans. Jede mit Nummer. Do 22.04.2027, 19:00.
> [Countdown]
> [E-Mail] [Größe, freiwillig] **Auf die Liste**
> Wer auf der Liste ist, kauft zuerst und zum Vorbestellpreis.
> *1.240 auf der Liste · Stand So 10.01.* (nur echte Zahl)

**K1 · Was hier entsteht** (Stufe 1)
> Ich baue eine Jeans aus einem Muster, das älter ist als die Hose. Erst Papier, dann Garn, dann Stoff. Hier siehst du jeden Schritt, auch die, die schiefgehen.
> [3 Fotos Papiertest an der Eightyfive]

*Hinweis:* „Dieses Muster ist älter als jede Grenze“ ist laut `zielgruppe.md` (Punkt 3) riskant. Deshalb hier „älter als die Hose“.

**K2 · Das Raster** (Stufe 1, ab Stufe 2 „Das Muster“)
> Ein Kreuzstich ist 1,33 Millimeter groß. Das Band an der rechten Tasche hat 17 davon in der Höhe. Die Münztasche 45 mal 45.
> [Motiv-Karten zum Antippen: Kreuzstich-Band · Münztasche · Achtstern · Lebensbaum]

Motiv-Karten (Antippen dreht die Karte, `<button aria-expanded>`):

| Karte | Vorderseite | Rückseite (Bedeutung) | Status |
|---|---|---|---|
| Raute | Zeichnung aus `front_band` | „In der Stickerei steht die Raute oft für ein bestelltes Feld.“ | **erst mit Beleg** aus der Belegtabelle (Spec Teil 5, offen) |
| Achtstern | Zeichnung aus `front_alatyr` | „Der Achtstern steht für die Sonne.“ | **erst mit Beleg** |
| Zickzack | Ausschnitt Band | „Die Zickzacklinie steht für Wasser.“ | **erst mit Beleg** |
| Lebensbaum | Patch D (ab Muster 13.11.) | Text von dir, nie „slawisch“ | Bedeutung erst mit Beleg |

**Warum „erst mit Beleg“:** Die Drei-von-vier-Regel verlangt den Beleg pro Motiv (Spec 3.2). Die Belegtabelle ist laut Spec Teil 5 noch offen. Eine Bedeutung auf der Startseite ist eine öffentliche Behauptung. Bis der Beleg steht, zeigt die Karte nur Maß und Stichzahl.

**K3 · Die Suche** (Stufe 1)
> 8 Fabriken angefragt. X haben geantwortet. Y können Stickerei auf dem Zuschnitt. Eine näht.
> (X und Y sind echte Zahlen aus deinem Fabrikvergleich, sonst bleibt der Satz weg.)

**K4 · Der Teppich** (Stufe 1)
> Der Teppich hing bei allen an der Wand. Auf dem Zipper ist er wieder da, als Medaillon auf dem Rücken.
> [Foto vom Familienteppich, nur wenn deine Familie zustimmt]

„Der Teppich hing bei allen an der Wand“ steht im Plan 8.2 als erlaubter Satz.

**K5 · Die Ernte und die Fäden** (ab Stufe 2)
> Hinten links drei Ähren auf einem roten Band. Darunter neun Goldfäden, von Hand gesetzt, nach der Wäsche. Sie verlassen die Hose.
> [Proto-Foto am Körper, Gesäßtasche links, dann Seite mit dem Serp]

*Hinweis:* `zielgruppe.md` Punkt 1 und 2: Sichel + Ähren + rotes Band zusammen sind Wappen-Vokabular, Stoppelfeld kann an den Holodomor erinnern (Gedenktag Sa 28.11.2026). Deshalb hier: nur Fotos am getragenen Teil, nie Sichel und Ähren freigestellt nebeneinander als Grafik, kein Text über „abgeschnittene“ Halme. Kapitel K5 kommt erst ab 11.12., also nach dem Gedenktag. **Du entscheidest**, ob der Serp auf der Startseite überhaupt eigens gezeigt wird.

**K6 · Die Nummern** (ab Stufe 3)
> 100 Stück. Nicht mehr. Deine Nummer steht auf dem Hangtag.
> [Raster 001–100] *Stand: 19:04*
> Vorbestellung: 149 € statt 169 €, nur bis So 21.03., 20:00. Lieferung 22.–30.04.2027.

Lieferfenster aus Plan 7 („Vorbestellung mit festem Lieferfenster 22.–30.04.2027“).

**K7 · Der Weg zur Hütte** (Stufe 4, Abschnitt 4.3)

**K8 · Ehrliche Größen** (ab Stufe 1, kurz)
> Wir labeln nach dem echten Maß. W32 heißt 81 Zentimeter Bund.
> [Link Größenseite]

Aus Spec 1.2 („Wir labeln nach dem echten Maß“, W32 = 81,2 cm).

**Fuß:** FAQ, Größen, Versand, Impressum, Datenschutz (Theme-Footer).

### 4.3 K7 · „Der Weg zur Hütte“ als Scroll-Szene

- **Aufbau:** Ein Bereich, der beim Scrollen am Bildschirm „klebt“ (`position: sticky`), etwa 4 Bildschirmhöhen lang. Darin 5 SVG-Ebenen: Himmel, Hügel, Hütte, Weizen hinten, Weizen vorn. Beim Scrollen bewegen sie sich unterschiedlich schnell seitwärts. So entsteht der Eindruck, man läuft nach rechts.
- **Stationen:** Bei 20 %, 45 % und 70 % des Weges erscheint jeweils eine Karte: Jeans an der Vogelscheuche, Zipper über dem Zaun (Medaillon sichtbar), Polo auf der Leine. Jede Karte: Foto vom Shoot, ein Satz, Preis aus Shopify, Link zum Produkt (ab LIVE) oder „22.04. · 19:00“.
- **Am Ende (100 %):** die Hütte. Tür je Zustand zu oder offen. Drinnen: Foto des Teppichs, darunter die drei Teile.
- **Technik:** `IntersectionObserver` für die Stationen. Er läuft in Chrome ab 51, Safari ab 12.1, Firefox ab 55 [W20]. Die Seitwärtsbewegung über `requestAnimationFrame`. **Nicht** über CSS `animation-timeline`: Das läuft erst in Chrome ab 115 und Safari ab 26, in Firefox nur in der Vorschau [W19].
- **GSAP ist nicht nötig.** GSAP ist seit der Übernahme durch Webflow „100 % kostenlos“, auch kommerziell [W6], und ScrollTrigger kostet 18 KB gzip [W6]. Für 5 Ebenen reicht eigenes JavaScript. Nur wenn das Gleiten auf deinem Handy ruckelt, darf Claude Code GSAP nehmen.
- **Bewegung aus / reduzierte Bewegung:** Die Szene wird zu 4 festen Bildern untereinander (Feld, Stationen, Hütte, Teppich).
- **Die Grafik zeichnet Claude Code als SVG-Silhouetten** in der Palette 6.2. Das ist der „Silhouettenstil“, der im Docket Plan B für das Spiel war. Halb so viel Arbeit, sieht gewollt aus. Du zeichnest nichts.

### 4.4 Interaktionen und Mobile

| Interaktion | Handy | Desktop |
|---|---|---|
| Kapitel weiter | scrollen | scrollen, Pfeiltasten |
| Kapitel-Punkte rechts | antippen springt zum Kapitel | klicken, Tab |
| Motiv-Karte drehen | antippen | Klick, Enter |
| Nummern-Raster | ansehen, Antippen eines Feldes zeigt „vergeben“ oder „frei“ | Hover und Fokus |
| Formular | E-Mail-Tastatur (`type="email"`, `autocomplete="email"`) | normal |
| Bewegung aus | Schalter unten links | gleich |
| Direkt zum Shop | fest oben rechts | gleich |

**Gestaltung fürs Handy zuerst.** Fast alle kommen aus Instagram und TikTok (Plan 5.1). Breite ab 320 px ohne waagerechtes Scrollen. Höhe über `svh`-Einheiten, damit die Browserleiste im In-App-Browser nichts abschneidet (**ungeprüft**, im Gerätetest prüfen).

### 4.5 Assets für B

| Datei | Inhalt | Größe | Wer |
|---|---|---|---|
| `tt-feld-himmel.svg` | Sonnenuntergang in 5 harten Stufen T01–T05, Sonne T06 | ≤ 3 KB | Claude Code |
| `tt-feld-huegel.svg` | Hügelkette, Silhouette T07 | ≤ 5 KB | Claude Code |
| `tt-feld-huette.svg` | Hütte, Tür zu und offen als zwei Gruppen | ≤ 4 KB | Claude Code |
| `tt-feld-weizen-hinten.svg`, `-vorn.svg` | Ähren-Silhouetten T08/T09, Lichtkante T10 | ≤ 8 KB je | Claude Code |
| `tt-feld-stationen.svg` | Vogelscheuche, Zaun, Leine als Umriss | ≤ 6 KB | Claude Code |
| `assets/tt-motiv-*.svg` | Kreuzstich-Band (gerader Rapport), Münztasche, Achtstern, flach | ≤ 10 KB je nach Optimierung (Schätzung) | Claude Code aus `design/fine.py` (erzeugt A, C, E) bzw. `design/front_band.svgfrag` (35 KB, folgt der Taschenkurve), `front_coin.svgfrag` (21 KB), `front_alatyr.svgfrag` (1 KB), alle im ZIP der Arbeitsdateien |
| Fotos Papiertest | 3 Stück, Hochformat | in Shopify-Dateien | du (Papiertest 3 am 08.10.) |
| Foto Familienteppich | 1–2 | in Shopify-Dateien | du (Familie fragen, Docket 15.10.) |
| Proto-Details | 6 (A, E, B, B2, C, D) | ab 11.12. | du (Mini-Shoot 08.12., On-Body 10.12.) |
| Shoot-Fotos | 6–8 (3 Produkte, Hütte/Teppich-Motiv falls vorhanden) | ab 27.02. | Shoot 20.02. |

Fotos lädst du in Shopify hoch (Inhalt → Dateien oder als Produktbild). Die Section holt sie über `image_url` mit Breite. Ohne Breite oder Höhe gibt der Filter einen Fehler [W8]. `image_tag` erzeugt `srcset` und kann ein Bild vorladen (`preload`) [W8].

### 4.6 Ereignisse für B

`tt_kapitel` (0–8), `tt_motiv_offen` (Name), `tt_formular` (Ort), `tt_shop_klick` (Ort). Nur mit Einwilligung, siehe 3.8.

---

## 5 · Variante A · Pixel-Spiel „Das Feld“ (nur bei „bauen“ am 05.02.)

### 5.1 Szenenablauf

| Szene | Was passiert | Zustände |
|---|---|---|
| **0 · Standbild** (HTML, kein Phaser) | Bild des Feldes (≤ 40 KB), zwei Knöpfe: „Ins Feld“ und „Direkt zum Shop“. Darunter „Ohne Spiel ansehen“ (springt zur Story B) | immer |
| **1 · Laden** | erst nach Tippen auf „Ins Feld“: Phaser + Grafiken laden, Ladebalken in Weizenfarbe | — |
| **2 · Feld** | Seitenansicht, Weg 4 Bildschirmbreiten lang (720 px intern). Stationen bei x ≈ 150 (Vogelscheuche mit Jeans), 330 (Zaun mit Zipper), 510 (Leine mit Polo), Hütte bei 660. Tippen auf eine Station: Figur läuft hin, HTML-Karte öffnet sich über dem Spiel | ab 22.03. still, ab 29.03. öffentlich |
| **3 · Hütte** | Tür zu: Countdown über der Tür, Formular „Hol dir den Schlüssel“ (HTML, `tt-warteliste-form` mit Tag `tt-feld`) | WARTELISTE bis ZWISCHENZEIT |
| | Tür offen mit Schlüssel | SCHLÜSSEL (18:00–19:00, `?key=`) |
| | Tür offen für alle, **Start direkt vor der Tür** | LIVE |
| **4 · Innen** | Teppich an der Wand, darunter Jeans, Zipper, Polo. Tippen = Produktseite. Bei AUSVERKAUFT: Jeans mit Schild „100/100“, Zipper und Polo weiter kaufbar | SCHLÜSSEL, LIVE, AUSVERKAUFT |

### 5.2 Asset-Liste A

Seitenansicht, interne Auflösung **180 × 320 px Hochformat**, ganzzahlig hochskaliert. Die Figur wird nur nach rechts gezeichnet, nach links spiegelt der Code (`flipX`).

| Datei | Inhalt | Pixel | Frames / Aseprite-Tags | Scroll-Faktor |
|---|---|---|---|---|
| `tt-figur` | Figur in Jeans und Zipper | 16 × 32 | `stehen` 2 · `laufen` 6 | 1 |
| `tt-himmel` | Sonnenuntergang, 5–6 harte Stufen, Sonne | 180 × 320 | 1 | 0 |
| `tt-huegel` | Hügelkette, Silhouette | 360 × 80 | 1 | 0,2 |
| `tt-weizen-hinten` | Kachel, wiegt | 64 × 48 | `wiegen` 3 | 0,8 |
| `tt-weizen-vorn` | Kachel, größer, dunkler, vor der Figur | 64 × 48 | `wiegen` 3 | 1,15 |
| `tt-huette` | außen | 64 × 64 | `zu` 1 · `auf` 2 (halb, offen) | 0,5 |
| `tt-vogelscheuche` | trägt die Jeans | 32 × 48 | `wind` 2 | 1 |
| `tt-zaun` | Zipper über dem Zaun, Medaillon sichtbar | 48 × 40 | 1 | 1 |
| `tt-leine` | Wäscheleine mit Polo | 48 × 40 | `wind` 2 | 1 |
| `tt-glanz` | Hinweis „hier tippen“ | 8 × 8 | `funkeln` 4 | 1 |
| `tt-innen` | Innenraum, Teppich an der Wand, drei Teile | 180 × 320 | 1 | 0 |
| `tt-standbild` | Standbild für Szene 0 (Export aus dem fertigen Feld) | 180 × 320, als PNG 4× = 720 × 1280 | 1 | — |

12 Dateien, die Docket-Liste hatte 10. Neu: `tt-glanz` (zeigt, wo man tippen kann) und `tt-standbild` (Ladezeit).

**Export aus Aseprite für Phaser:** „Sprite Sheet“, Output PNG + „JSON Data“ (Hash oder Array), „Tags“ in den Meta-Optionen anhaken, „Item Filename“ nur `{frame}`, Trim an, Padding 1. So steht es in Phasers eigener Anleitung zu `createFromAseprite` [W4]. Laden mit `this.load.aseprite('tt-figur', 'tt-figur.png', 'tt-figur.json')` [W4], dann `this.anims.createFromAseprite('tt-figur')`. Die Tags heißen in Phaser genauso wie in Aseprite, Groß- und Kleinschreibung zählt [W4].

**Aseprite** steht unter einer Endnutzer-Lizenz (EULA) [W25]. Der Preis (~20 € laut Plan) ist **nicht geprüft**, vor dem Kauf ansehen. **LibreSprite** ist kostenlos (GPLv2) und läuft auf macOS [W26].

### 5.3 Palette (A und die Feld-SVGs von B)

17 Farben. Werte nachgerechnet (Farbton H, Sättigung S, Helligkeit L).

| Nr. | Name | Hex | H / S / L | Rolle |
|---|---|---|---|---|
| T01 | Nachtviolett | `#2B1B3D` | 268° / 39 % / 17 % | Himmel oben, Texthintergrund |
| T02 | Pflaume | `#5A1F3A` | 333° / 49 % / 24 % | Himmel |
| T03 | Glutrot | `#A3312B` | 3° / 58 % / 40 % | Himmel |
| T04 | Abendorange | `#E0662B` | 20° / 74 % / 52 % | Himmel |
| T05 | Horizontgold | `#F2A541` | 34° / 87 % / 60 % | Horizont, Knöpfe |
| T06 | Sonnenkern | `#FCE3A7` | 42° / 93 % / 82 % | Sonne |
| T07 | Hügel | `#3A1C2C` | 328° / 35 % / 17 % | Silhouetten |
| T08 | Weizen Schatten | `#6B3A1E` | 22° / 56 % / 27 % | Weizen im Gegenlicht |
| T09 | Weizen | `#A8642A` | 28° / 60 % / 41 % | Weizen |
| T10 | Weizen Lichtkante | `#E9B35F` | 37° / 76 % / 64 % | Lichtkante |
| T11 | Teppich Bordeaux | `#7A1E2C` | 351° / 61 % / 30 % | Teppich |
| T12 | Teppich Beige | `#E8D6B3` | 40° / 54 % / 81 % | Teppich, Fließtext |
| T13 | Teppich Schwarz | `#1A1416` | 340° / 13 % / 9 % | Teppich, Seitenhintergrund |
| T14 | Teppich Gold | `#C9962E` | 40° / 63 % / 48 % | Teppich, Creator-Felder |
| T15 | Denim Indigo | `#1F2A44` | 222° / 37 % / 19 % | **nur** Jeans und Zipper an den Stationen |
| T16 | Garn Weiß | `#F4EFE6` | 39° / 39 % / 93 % | Stickerei, Text |
| T17 | Garn Rot | `#B3202A` | 356° / 70 % / 41 % | Stickerei, vergebene Nummern |

**Flaggen-Regel technisch:** Es gibt genau ein Blau (T15), und es ist dunkel (L 19 %). `tools/flaggen-check.mjs` liest jedes PNG und SVG im Feld und schlägt Alarm bei jedem Pixel mit Farbton 180–250°, Sättigung > 25 % und Helligkeit > 45 %. Läuft vor jedem Commit von Grafiken.

**Kontraste (nachgerechnet nach WCAG-Formel):** Beige T12 auf Nachtviolett T01 11,1:1 · Weiß T16 auf Schwarz T13 15,9:1 · Schwarz T13 auf Horizontgold T05 8,9:1 · Weiß T16 auf Bordeaux T11 8,9:1 · Weiß T16 auf Garn Rot T17 5,8:1 · Horizontgold T05 auf Nachtviolett T01 7,7:1. Alle über 4,5:1 [W21].

### 5.4 Steuerung

| Eingabe | Wirkung |
|---|---|
| Tippen irgendwo im Feld | Figur läuft zu dieser Stelle |
| Tippen auf Station oder Tür | Figur läuft hin, Karte bzw. Formular öffnet sich (HTML) |
| Zwei Knöpfe ◀ ▶ unten (je 44 × 44 px), halten = laufen | für alle, die nicht zielen wollen |
| Tastatur ← → | laufen |
| Enter / Leertaste | Station öffnen |
| Esc | Karte schließen |

Geschwindigkeit 60 px/s intern, der ganze Weg in rund 12 Sekunden (Schätzung, beim Steuerungstest anpassen). Kamera folgt mit Totzone.

### 5.5 Technik Phaser 3.90.0

- **Version:** 3.90.0 vom 23.05.2025 [W1][W2]. Es ist die neueste 3.x-Version auf npm, Stand 07.10.2026 [W3]. Phaser 4.0.0 erschien am 10.04.2026, aktuell ist 4.2.1 vom 09.07.2026 [W1][W3]. **Warum trotzdem 3.90:** Die Datei von 4.2.1 ist größer (1.375.976 Byte roh, 352.227 gzip, eigene Messung [W3]), und für v3 gibt es Jahre an Beispielen, die Claude Code kennt. Lizenz beider Versionen: MIT [W5].
- **Datei:** `phaser.min.js` aus dem npm-Paket nach `assets/phaser-3.90.0.min.js`. Nicht vom fremden CDN laden.
- **Schärfe:** `pixelArt: true` schaltet die Kantenglättung ab und setzt `roundPixels` auf an. So steht es in Phasers `Config.js` [W4].
- **Ganzzahlig skalieren:** Phaser 3.90 hat die Skalier-Modi NONE, WIDTH_CONTROLS_HEIGHT, HEIGHT_CONTROLS_WIDTH, FIT, ENVELOP, RESIZE und EXPAND [W4]. Einen Modus „nur ganze Zahlen“ gibt es nicht. Deshalb: Modus NONE, Zoom selbst rechnen: `zoom = max(1, floor(min(Breite / 180, Höhe / 320)))`, bei jeder Größenänderung neu.
- **Konsole:** `banner: false` blendet die Phaser-Zeile in der Konsole aus [W4].
- **Karten, Formular, Shop-Button sind HTML**, nicht im Canvas. Dadurch funktionieren Screenreader, Tastatur, Autofill und das Shopify-Formular.

### 5.6 Performance, Barrierefreiheit, Analytics, Anbindung für A

- **Performance:** Budget 3.10. Phaser erst nach Tippen. Grafiken als PNG mit Palette. Ziel: Feld flüssig auf deinem Handy und einem älteren iPhone (Gerätetest, Schritt 17).
- **Barrierefreiheit:** Canvas `aria-hidden="true"`. Unter dem Spiel die Liste „Ohne Spiel ansehen“ mit allen Stationen als Links. Bewegung-aus-Schalter stoppt Weizen und Glanz. Bei `prefers-reduced-motion` startet das Spiel nicht von selbst, nur das Standbild mit Links.
- **Analytics:** `tt_feld_start`, `tt_feld_station` (Name), `tt_tuer` (Zustand), `tt_shop_klick` (Ort: Button, Station, Innen). Dazu der Tag `tt-feld` an jeder Anmeldung aus der Hütte. Damit siehst du am So 04.04. (Docket W29), ob das Feld Adressen bringt oder nur Likes.
- **Anbindung:** dieselbe Uhr (`tt-clock.js`), dasselbe Formular-Snippet, derselbe Shop-Button wie B. Das Spiel liest nur den Zustand und zeigt die Tür passend.

---

## 6 · Design-Vorschläge (du entscheidest)

1. **Die Startseite erzählt, sie verkauft nicht als Raster.** Kein Produktgitter oben. Oben stehen Countdown und Formular, darunter die Geschichte. Gekauft wird über den festen Shop-Button.
2. **Palette 5.3 für die ganze Seite.** Hintergrund Teppich-Schwarz T13, Text Beige T12 und Weiß T16, Akzente Garn-Rot T17 und Horizontgold T05. Die Seite sieht dann aus wie der Teppich bei Sonnenuntergang. Das einzige Blau ist der Denim auf den Fotos. So hebt sich die Jeans ab.
3. **Nummern-Raster als Kreuzstich.** 10 × 10 Kästchen, vergeben = rot-weißer Kreuzstich, Creator/Reserve = Gold. Es ist dieselbe Grammatik wie auf der Hose (Spec 3.5). Das Raster ist ein Motiv für Posts: „Nr. 001–017 vergeben“ als Bildschirmfoto.
4. **Nach außen „Time Travel“, nicht „Projekt Slavic“ und nicht „Eine Kultur“.** Vorschlag aus `zielgruppe.md` Punkt 5.
5. **Neutrale Namen für die Elemente:** „Kreuzstich-Band“ statt „Vyshyvanka-Band“, „Achtstern“ statt „Alatyr“. Vorschlag aus `zielgruppe.md` Punkt 4. Intern bleiben die Namen wie in der Spec. **Das ist eine Abweichung von deinen bisherigen Namen.**
6. **Sichel und Ähren nie als freigestellte Grafik nebeneinander**, nie als Icon, Favicon oder Logo (Regel Serp + Risiko 1 aus `zielgruppe.md`). Auf der Website nur als Foto am getragenen Teil.
7. **Schrift:** eine Schrift für Überschriften über die Theme-Einstellung `font_picker` [W8], Fließtext in der Systemschrift. Keine Pixel-Schrift für Fließtext, nur für die Zahl im Countdown, wenn überhaupt.
8. **Echte Fotos vor Grafik.** In Stufe 1 tragen die Papiertest-Fotos die Seite. Sie zeigen, dass hier jemand wirklich baut. Das passt zu „Gezeigt wird nur, was es gibt“.
9. **Ruhige Bewegung.** Nur Parallax und wiegender Weizen. Kein Wackeln, keine Pop-ups. Ein einziges Formular, zweimal auf der Seite (oben und am Ende).

---

## 7 · Testplan (A und B)

| # | Test | Wie | Bestanden, wenn |
|---|---|---|---|
| T1 | Zustände | `?t=` mit Testmodus: 2027-01-14T18:59:30+01:00, 2027-03-21T19:59:30+01:00, 2027-04-22T17:59:30+02:00, 2027-04-22T18:59:30+02:00, mit und ohne `?key=` | Seite wechselt Text, Countdown und Shop-Button genau an der Grenze |
| T2 | Sommerzeit | `?t=2027-03-28T01:59:00+01:00` und `…T03:01:00+02:00` | Countdown springt nicht um eine Stunde |
| T3 | Serverzeit | Handy-Uhr von Hand 2 Stunden vorstellen | Countdown bleibt richtig |
| T4 | Formular neu | neue Testadresse | Bestätigungs-Mail kommt, nach Bestätigen „abonniert“ mit allen Tags |
| T5 | Formular doppelt | dieselbe Adresse noch einmal | freundliche Meldung, kein Fehler |
| T6 | hCaptcha | Formular fünfmal schnell hintereinander | Abfrage erscheint und lässt sich lösen, danach Erfolg |
| T7 | Nummern | Bestand des Testprodukts im Admin um 2 senken | Raster zeigt 2 mehr, Zeit bis zum Sprung notiert |
| T8 | Ohne JavaScript | in Safari JavaScript aus | Datum, Formular, Produktlinks sind da |
| T9 | Bewegung | iPhone: Bedienungshilfen → Bewegung reduzieren an; Schalter „Bewegung aus“ | keine Parallax, keine Animation |
| T10 | Geräte | iPhone Safari, Instagram-In-App (Link aus der Bio), TikTok-In-App, Android Chrome, kleines iPhone (SE), Laptop | nichts abgeschnitten, kein waagerechtes Scrollen, Shop-Button immer sichtbar |
| T11 | Ladezeit | Chrome Entwicklertools, Netzwerk gedrosselt, Cache aus | erstes Bild unter 2 s, Budget 3.10 eingehalten (`tools/budget-check.mjs`) |
| T12 | Tastatur | nur Tab, Enter, Pfeile | alles erreichbar, Fokus sichtbar |
| T13 | Theme Check | `shopify theme check` [W7] | keine Fehler in tt-Dateien |
| T14 | Future Publishing | Testprodukt auf „in 30 Minuten“ terminieren (Schritt 20) | Produkt erscheint pünktlich, vorher 404 |
| T15 | PLAN B | `shopify theme publish --theme "PLAN B" --force` [W7] | unter 1 Minute live, Zeit gestoppt |
| T16 | Flaggen-Check | `tools/flaggen-check.mjs` | 0 Treffer |
| A-T1 | Spiel lädt erst nach Tippen | Netzwerk-Tab | vor dem Tippen keine Phaser-Datei geladen |
| A-T2 | Spiel im Querformat | Handy drehen | Hinweis „Handy drehen“ oder sauber skaliert, nie verzerrt |
| A-T3 | Playtest | 5 Leute, ohne Erklärung (Sa 13.03.) | 4 von 5 finden Tür und Shop ohne Hilfe |

---

## 8 · Fallback und PLAN B

1. **Ebene 1: ohne JavaScript.** Jede Section rendert in Liquid Datum, Text, Formular und Links. Fällt das Skript aus, bleibt eine schlichte, funktionierende Seite.
2. **Ebene 2: ohne Spiel.** Hakt A, schaltest du in den Section-Einstellungen von A die Checkbox „Spiel zeigen“ aus. Dann steht die Story B wieder oben. Dauer: 30 Sekunden im Theme-Editor.
3. **Ebene 3: PLAN B.** Das Theme, das vor Stufe 1 live war (Dawn-Warteliste vom 08.10.), heißt ab Schritt 8 „PLAN B“. Hakt alles: `shopify theme publish --theme "PLAN B" --force` [W7] oder im Admin auf „Veröffentlichen“. Geübt am Mi 17.03. (Schritt 18). Ziel unter einer Minute.
4. **Am Drop-Tag wird nicht debuggt.** Ab Sa 17.04. ist Code-Freeze. Hängt am 22.04. etwas, PLAN B veröffentlichen und weitermachen.
5. **Unabhängig von allem:** Gekauft wird über Shopify-Produktseiten und Checkout. Die laufen auch, wenn deine Startseite hängt. Der Link zur Kollektion steht in der E-Mail T−1h und LIVE.

---

## 9 · Bauplan in 32 Schritten

**So arbeitest du mit Claude Code:** Ein Prompt pro Schritt. Der nächste kommt erst, wenn der letzte am Handy funktioniert und committet ist. Claude Code pusht nur nach deinem „ja“. Veröffentlichen machst du selbst.

**Schritte 1–24 gelten immer (Variante B).** **A1–A8 gelten nur bei „bauen“ am 05.02.** und ersetzen dann Schritt 16.

Die Daten liegen auf Tagen, an denen im Docket Rev. 5.3 wenig steht. Die Zahl „Docket“ nennt, wie viele Minuten dort an dem Tag schon geplant sind.

| # | Datum | Schritt | Dauer | Docket |
|---|---|---|---|---|
| 1 | Sa 31.10.2026 | Werkzeuge auf dem Mac | 60 | 30 |
| 2 | Mi 04.11. | Theme-Kopie, Git, GitHub | 45 | 30 |
| 3 | Sa 07.11. | CLAUDE.md | 30 | 30 (Puffer) |
| 4 | Di 10.11. | Zeit-Modul und Countdown | 60 | 40 |
| 5 | Mi 11.11. | Wartelisten-Formular mit Tags | 60 | 35 |
| 6 | Sa 14.11. | Startseite Stufe 1 | 90 | 30 (Puffer) |
| 7 | So 15.11. | Prüfen | 30 | 45 |
| 8 | Mi 18.11. | Stufe 1 live, PLAN B | 20 | 60 |
| 9 | Fr 11.12. | Stufe 2: Das Muster | 60 | 15 |
| 10 | Sa 19.12. | Nummern-Raster | 90 | 40 |
| 11 | Di 05.01.2027 | Vorbestell-Zustände | 60 | 45 |
| 12 | Sa 09.01. | Analytics | 30 | 10 |
| 13 | Fr 05.02. | Entscheidung A | 20 | 80 (inkl. dieser Aufgabe) |
| 14 | Sa 27.02. | Shoot-Bilder | 60 | 10 |
| 15 | Do 04.03. | Drop-Zustände | 60 | 45 |
| 16 | Sa 06.03. | Der Weg zur Hütte (entfällt bei A) | 90 | 10 |
| 17 | Mo 08.03. | Gerätetest | 60 | 30 |
| 18 | Mi 17.03. | PLAN B üben | 20 | 45 |
| 19 | Mo 22.03. | Stiller Launch Stufe 4 | 30 | 30 |
| 20 | Fr 09.04. | Generalprobe | 45 | 20 |
| 21 | Do 15.04. | Schlüssel-Link | 20 | 30 |
| 22 | Sa 17.04. | Code-Freeze | 5 | 70 |
| 23 | Do 22.04. | Drop-Tag | ~30 | Drop |
| 24 | So 25.04. | Auswertung | 20 | 95 |
| A1 | Di 09.02. | Graubox | 60 | 15 |
| A2 | Mo 15.02. | Palette, Flaggen-Check | 30 | 15 |
| A3 | Di 16.02. | Steuerung am Daumen | 20 | 35 |
| A4 | Do 18.02., Mo 22.02., Mi 24.02. | Pixel-Art | 3 × 90 | 0 / 15 / 45 |
| A5 | Fr 26.02. | Grafik einbauen | 60 | 45 |
| A6 | Mo 01.03. | Stationen, Karten, Formular | 90 | 45 |
| A7 | Mi 03.03. | Tür, Innenraum, Ladezeit | 60 | 55 |
| A8 | Sa 13.03. | Playtest | 60 | 10 |

**Summe B:** 1.095 Minuten ≈ 18 Stunden, davon Schritte 1–12 = 635 Minuten ≈ 10,5 Stunden vor dem 05.02. **A zusätzlich:** 650 Minuten geplant, minus Schritt 16 (90) = +9,5 Stunden reine Bauzeit. Realistisch mit Fehlersuche 20–40 Stunden (Schätzung).

---

### Schritt 1 · Werkzeuge auf dem Mac
**Wann:** Sa 31.10.2026 · **Dauer:** 60 min

**Was du tust:**
1. Terminal öffnen: ⌘ + Leertaste, „Terminal“ tippen, Enter.
2. **Node.js:** Auf nodejs.org die LTS-Version als macOS-Installer laden und installieren. Die Shopify CLI 4.8.5 verlangt Node.js 22.12.0 oder neuer [W7]. Prüfen: `node -v`. *(Download-Seite vor Ort ansehen, hier nicht geprüft.)*
3. **Git:** `git --version` eingeben. Fragt der Mac nach den „Command Line Tools“, auf Installieren klicken. *(Mac-Verhalten, hier nicht geprüft.)*
4. **Shopify CLI:** `npm install -g @shopify/cli` [W7]. Kommt „permission denied“: **kein** `sudo`, sondern Claude fragen. Prüfen: `shopify version` zeigt 4.8.5 oder höher. Laut README geht auch `brew tap shopify/shopify && brew install shopify-cli` [W7], wenn du Homebrew schon hast.
5. **Claude Code:** `curl -fsSL https://claude.ai/install.sh | bash` [W23]. Neues Terminal-Fenster, `claude --version`. Braucht macOS 13 oder neuer und ein Pro-, Max-, Team- oder Enterprise-Konto [W23].
6. Ordner: `mkdir -p ~/Claude/Novalife/website && cd ~/Claude/Novalife/website`, dann `claude`.

**Fertig, wenn:** Claude Code zeigt dir eine Tabelle mit fünf Werkzeugen, alle „ok“.

**Prompt für Claude Code:**
```
Ich bin neu auf dem Mac und kein Entwickler. Prüfe nur, installiere nichts und benutze nie sudo:
node -v (muss 22.12.0 oder neuer sein), npm -v, git --version, shopify version, claude --version.
Zeig mir eine Tabelle: Werkzeug | Version | ok / nicht ok.
Wenn etwas fehlt oder zu alt ist, erklär mir in einfachen Schritten, was ich selbst tun muss.
```

---

### Schritt 2 · Theme-Kopie holen, Git und GitHub
**Wann:** Mi 04.11. · **Dauer:** 45 min

**Was du tust:**
1. Im Ordner `~/Claude/Novalife/website`: `shopify theme list --store DEIN-SHOP`. DEIN-SHOP ist der Teil vor `.myshopify.com`, die CLI nimmt auch nur dieses Präfix [W7]. Beim ersten Mal öffnet sich der Browser zum Einloggen. Notiere die ID des Themes mit der Rolle „live“.
2. `shopify theme duplicate --theme <ID> --name "TT Story" --store DEIN-SHOP` [W7]. Meldet Shopify „Maximum number of themes reached“ [W7], alte Test-Themes im Admin löschen. Die Höchstzahl ist hier nicht geprüft.
3. `mkdir tt-theme && cd tt-theme && shopify theme pull --theme "TT Story" --store DEIN-SHOP` [W7]
4. `git init && git add -A && git commit -m "Ausgangsstand TT Story"`
5. `claude` starten, Prompt unten.

**Fertig, wenn:** Der erste Commit liegt in einem privaten GitHub-Repo, und du weißt, welches Theme (Dawn, Horizon oder ein anderes) du hast.

**Prompt für Claude Code:**
```
Dieser Ordner ist eine Kopie meines Shopify-Themes. In Shopify heißt sie „TT Story“ und ist NICHT veröffentlicht.
1. Lies config/settings_schema.json und sag mir: Welches Theme ist das (Name, Version)?
2. Lege eine .gitignore an mit: node_modules/, .DS_Store, .env, *.log.
3. Lege eine .shopifyignore an, die CLAUDE.md, docs/ und tools/ vom Hochladen zu Shopify ausschließt.
4. Hilf mir, dieses Repo als PRIVATES GitHub-Repo „novalife-tt-theme“ zu sichern. Erklär jeden Schritt in einem Satz, bevor du ihn ausführst, und frag mich vor jedem Push.
Lade nichts zu Shopify hoch. Commit am Ende: „gitignore und shopifyignore“.
```

---

### Schritt 3 · CLAUDE.md: deine Regeln für Claude Code
**Wann:** Sa 07.11. (Puffer-Tag) · **Dauer:** 30 min

**Was du tust:** Anhang A dieser Datei als `CLAUDE.md` in den Ordner `tt-theme` kopieren (TextEdit, „Als reinen Text sichern“). DEIN-SHOP und DEINE-DOMAIN ersetzen. Claude Code lädt eine `CLAUDE.md` im Projektordner zu Beginn jeder Sitzung [W24]. Mit `/context` siehst du, ob sie geladen ist [W24].

**Fertig, wenn:** Claude Code fasst dir die Regeln richtig zusammen, Commit ist gemacht.

**Prompt für Claude Code:**
```
Lies CLAUDE.md. Fasse mir die harten Regeln in 8 kurzen Punkten zusammen, damit ich sehe, dass du sie verstanden hast.
Dann lege docs/TERMINE.md an: die Zustandstabelle aus CLAUDE.md, dazu für jeden Zustand einen Test-Link mit ?t= (30 Sekunden vor der Grenze) und einen mit ?t= und ?key=.
Commit: „Regeln und Termine“.
```

---

### Schritt 4 · Zeit-Modul und Countdown
**Wann:** Di 10.11. · **Dauer:** 60 min

**Was du tust:** Prompt geben, dann `shopify theme dev --store DEIN-SHOP` in einem zweiten Terminal-Fenster. Den Vorschau-Link öffnest du am Handy [W7].

**Fertig, wenn:** Der Countdown läuft am Handy bis Do 14.01., 19:00. Mit `?t=2027-01-14T18:59:30+01:00` springt er nach 30 Sekunden auf „Vorbestellung offen“.

**Prompt für Claude Code:**
```
Baue das Zeit-Modul für die Drop-Seite. Halte dich an CLAUDE.md.

1. config/settings_schema.json: neue Gruppe „Time Travel“ mit allen Einstellungen aus CLAUDE.md, Abschnitt „Theme-Einstellungen“ (Zeiten als text mit Offset, tt_testmodus als checkbox, Produkte als product, Kollektion als collection, Zahlen als number). Werte aus der Termin-Tabelle als Standard.

2. assets/tt-clock.js, ohne Bibliotheken:
   - Serverzeit: fetch('/cart.js', {cache: 'no-store'}), Header „Date“ lesen, Header „Age“ (Sekunden) addieren, Abstand zur Geräteuhr merken. Alle 5 Minuten und bei visibilitychange neu. Wenn das scheitert: Geräteuhr nehmen und intern markieren.
   - Testmodus: Nur wenn tt_testmodus an ist, überschreibt ?t=<ISO mit Offset> die Uhr.
   - Zustand berechnen: WARTELISTE, VORBESTELLUNG, ZWISCHENZEIT, SCHLUESSEL (nur mit ?key= gleich tt_schluessel, sonst weiter ZWISCHENZEIT), LIVE, AUSVERKAUFT (wenn irgendwo data-tt-ausverkauft="true" im HTML steht).
   - Ereignis „tt:state“ auf window mit {zustand, jetzt, naechsteGrenze} bei jedem Wechsel, „tt:tick“ einmal pro Sekunde.
   - ?key= im sessionStorage merken (in try/catch), damit er beim Weiterklicken erhalten bleibt.

3. snippets/tt-countdown.liquid: rendert in Liquid das feste Zieldatum als Text („Do 14.01.2027, 19:00“) in <time datetime="…">. JavaScript ersetzt den Text durch „Noch 12 T 04 Std 31 Min 09 Sek“. Für Screenreader nur minütlich ansagen (eigenes, visuell verstecktes Element mit aria-live="polite").

4. Eine erste sections/tt-hero.liquid nur mit dem Countdown, oben in templates/index.json eingebaut, damit ich testen kann.

Benutze nie Liquid 'now' für Zeitentscheidungen. Erklär mir danach, wie ich mit shopify theme dev die Vorschau aufs Handy hole und welche ?t=-Links aus docs/TERMINE.md ich teste. Commit, wenn ich „läuft“ schreibe.
```

---

### Schritt 5 · Wartelisten-Formular mit Quellen- und Größen-Tags
**Wann:** Mi 11.11. · **Dauer:** 60 min

**Was du tust:** Prompt geben, dann zweimal mit einer neuen Testadresse eintragen: einmal ohne Größe, einmal mit Größe und mit `?utm_source=instagram`. Bestätigungs-Mail anklicken. In Shopify unter Kunden nachsehen.

**Fertig, wenn:** Deine Testadresse steht in Shopify als abonniert, mit den Tags `tt-warteliste`, `tt-story`, `src-instagram`, `gr-w32` (oder dem zusammengesetzten Ersatz-Tag). Du hast notiert, ob mehrere Tags gehen und ob eine bestehende Adresse neue Tags bekommt.

**Prompt für Claude Code:**
```
Baue snippets/tt-warteliste-form.liquid und binde es in sections/tt-hero.liquid unter dem Countdown ein. Halte dich an CLAUDE.md.

- {% form 'customer', return_to: 'back' %} wie in Dawns sections/newsletter.liquid: verstecktes Feld contact[tags], Eingabe contact[email] (type="email", autocomplete="email", required, sichtbares <label>).
- Freiwillige Auswahl „Deine Größe“: W30, W32, W34, W36, W38, „weiß ich noch nicht“.
- Parameter „ort“ beim Einbinden (tt-story, tt-huette, tt-feld, tt-drop2), Standard tt-story.
- In assets/tt-story.js: setzt vor dem Absenden contact[tags] auf „tt-warteliste,<ort>,src-<quelle>,gr-<groesse>“ und, falls ?ref= in der URL steht, zusätzlich „ref-<code>“. Quelle aus utm_source (instagram, tiktok, qr, email), sonst „direkt“. Nur Kleinbuchstaben, Ziffern und Bindestrich zulassen, max. 30 Zeichen je Tag.
- Formular normal absenden, NICHT per fetch (Shopify kann eine hCaptcha-Abfrage zeigen).
- Nach dem Absenden: bei form.posted_successfully? „Fast geschafft. Bestätige deine Adresse in der E-Mail, die gerade kommt.“ Bei form.errors die Meldung von Shopify.
- Einstellung datenschutz_text (richtext) für den Satz aus meinem Rechtstexte-Generator, unter dem Knopf.
- Knopf „Auf die Liste“, mindestens 44 px hoch, Farben aus der Palette in CLAUDE.md.

Sag mir danach genau, wo ich in Shopify die Testadresse und ihre Tags sehe. Ich teste erst mit EINEM Tag, dann mit allen. Speichert Shopify nur einen Tag, bau es um auf einen zusammengesetzten Tag „tt-<ort>-<quelle>-<groesse>“. Commit nach meinem „passt“.
```

---

### Schritt 6 · Startseite Stufe 1: Prozess-Story
**Wann:** Sa 14.11. (Puffer-Tag) · **Dauer:** 90 min

**Was du tust vorher (15 min):**
1. 3 Papiertest-Fotos (Hochformat) und 1 Teppich-Foto in Shopify hochladen: Inhalt → Dateien. Teppich nur, wenn deine Familie zustimmt.
2. `design/fine.py` und `front_band.svgfrag`, `front_coin.svgfrag`, `front_alatyr.svgfrag` aus dem ZIP der Arbeitsdateien nach `tt-theme/tools/motive/` kopieren. `fine.py` ist laut Übergabe die Quelle der Kreuzstich-Elemente A, C und E.
3. Abschnitt 4.2 dieser Datei (K0, K1–K4, K8) nach `tt-theme/docs/TEXTE-STUFE1.md` kopieren und Sätze ändern, die nicht nach dir klingen. K3 nur mit echten Zahlen.

**Fertig, wenn:** Die Vorschau zeigt Kopf, K1–K4 und K8, ohne Mockup einer fertigen Jeans, und sieht am Handy gut aus.

**Prompt für Claude Code:**
```
Baue die Startseite Stufe 1 der Scroll-Story. Halte dich an CLAUDE.md, besonders an die Sprachregeln und „kein Mockup bis 03.12.“.

1. sections/tt-kapitel.liquid: ein Kapitel mit Einstellungen (Überschrift, Anker-ID) und Blöcken: „bild“ (image_picker, Alt-Text Pflicht), „text“ (richtext), „motiv“ (Auswahl band, muenztasche, achtstern; zeigt das SVG und eine Karte mit Maß und Stichzahl; eine Rückseite „Bedeutung“ nur, wenn ein Text eingetragen ist; Karte ist ein <button aria-expanded>). Bilder über image_url mit width und image_tag mit widths und sizes.
2. Baue aus tools/motive/ (fine.py und die drei .svgfrag-Dateien) eigenständige, kleine SVGs in assets/: tt-motiv-band.svg (das Band als GERADER Streifen, ein bis zwei Rapporte, 17 Stiche hoch, nicht der Taschenkurve folgend), tt-motiv-muenztasche.svg (45 × 45), tt-motiv-achtstern.svg (27 × 27). Eigene viewBox, gleiche Kästchen zu einem Pfad zusammenfassen, je höchstens 10 KB. Flach, NICHT auf eine Jeans-Silhouette gelegt. Zeig mir die Bytes.
3. sections/tt-hero.liquid fertig machen: „Time Travel“, Zeile „100 Jeans. Jede mit Nummer. Do 22.04.2027, 19:00.“, Countdown, Formular, Listenstand aus tt_liste_zahl und tt_liste_datum („1.240 auf der Liste · Stand So 10.01.“, ausblenden bei 0).
4. snippets/tt-shop-button.liquid: fester Link oben rechts, mindestens 44 × 44 px, Text und Ziel je Zustand laut CLAUDE.md; ohne JavaScript „Auf die Liste“ → #liste.
5. templates/index.json: tt-hero, dann K1 „Was hier entsteht“, K2 „Das Raster“, K3 „Die Suche“, K4 „Der Teppich“, K8 „Ehrliche Größen“, am Ende noch einmal das Formular. Texte aus docs/TEXTE-STUFE1.md. Prüfe jeden Satz gegen die Sprachregeln und markiere mir Treffer.
6. assets/tt-story.css: Palette aus CLAUDE.md (Hintergrund T13, Text T12/T16), mobil zuerst, ab 320 px Breite ohne waagerechtes Scrollen, Schalter „Bewegung aus“ unten links (merkt sich die Wahl im localStorage, in try/catch).
Keine Bibliotheken. Zeig mir am Ende die neuen Dateien mit Größe in KB. Commit nach meinem „passt“.
```

---

### Schritt 7 · Prüfen: Theme Check, Handy, Instagram
**Wann:** So 15.11. · **Dauer:** 30 min

**Was du tust:** Prompt geben. Den Vorschau-Link aus `shopify theme dev` schickst du dir selbst per Instagram-DM und tippst ihn dort an. So öffnet er im In-App-Browser von Instagram.

**Fertig, wenn:** Theme Check ohne Fehler in tt-Dateien, Seite in Instagram geprüft, `tools/budget-check.mjs` grün, du weißt, ob tt-Dateien komprimiert ausgeliefert werden.

**Prompt für Claude Code:**
```
Prüf die Startseite wie ein strenger Tester. Halte dich an CLAUDE.md.
1. Lege tools/budget-check.mjs an (Node, ohne Pakete): summiert alle assets/tt-* roh und gzip und bricht ab, wenn eigene CSS > 15 KB, eigene JS > 25 KB oder tt-feld-*.svg zusammen > 25 KB roh. Führ es aus.
2. Führ shopify theme check aus und erklär mir Fehler in tt-Dateien. Andere Theme-Dateien nicht anfassen.
3. Prüfliste: Kontrast laut Palette, Tippziele ≥ 44 px, Tab-Reihenfolge und sichtbarer Fokus, Schalter „Bewegung aus“, prefers-reduced-motion, Seite ohne JavaScript (Datum, Formular, Links da?), Alt-Texte.
4. Sag mir, wie ich in Chrome auf dem Laptop die Netzwerk-Drosselung einschalte, die Zeit bis zum ersten Bild messe und in der Spalte „Content-Encoding“ sehe, ob tt-story.js komprimiert kommt.
Gib mir alle Probleme als Liste nach Schwere. Repariere die ersten fünf, dann stopp und zeig mir die Änderungen.
```

---

### Schritt 8 · Stufe 1 live, altes Theme wird PLAN B
**Wann:** Mi 18.11. · **Dauer:** 20 min

**Was du tust:**
1. Prompt geben. Claude Code pusht nach deinem „ja“ auf „TT Story“ (`shopify theme push --theme "TT Story"` [W7]).
2. Im Admin (Onlineshop → Themes) das bisher veröffentlichte Theme (die Dawn-Warteliste vom 08.10.) in „PLAN B“ umbenennen. Die CLI kann das auch (`shopify theme rename` [W7]).
3. „TT Story“ veröffentlichen: im Admin auf „Veröffentlichen“ oder `shopify theme publish --theme "TT Story"` [W7]. Das machst du selbst.
4. Mit dem Handy über deine Instagram-Bio auf die Seite, mit einer neuen Testadresse eintragen.

**Fertig, wenn:** Stufe 1 ist live, „PLAN B“ liegt unveröffentlicht in der Theme-Bibliothek, die Test-Anmeldung ist mit Tags angekommen.

**Prompt für Claude Code:**
```
Ich will Stufe 1 live schalten. Prüfe vorher: git status sauber, tools/budget-check.mjs grün, shopify theme check ohne Fehler in tt-Dateien. Zeig mir den push-Befehl auf „TT Story“ und führ ihn erst aus, wenn ich „ja“ schreibe. Den publish mache ich selbst im Admin. Danach eine Checkliste, was ich auf dem Handy über die Instagram-Bio teste.
```

---

### Schritt 9 · Stufe 2: Das Muster mit echten Proto-Fotos
**Wann:** Fr 11.12. · **Dauer:** 60 min
**Voraussetzung:** Mini-Shoot Di 08.12. und On-Body-Fotos Do 10.12. (Docket). Für jede Bedeutung, die gezeigt wird, ein Beleg in der Belegtabelle (Spec Teil 5). Ohne Beleg zeigt die Karte nur Maß und Stichzahl.

**Was du tust vorher:** 6 Detailfotos in Shopify hochladen. Text K5 aus Abschnitt 4.2 nach `docs/TEXTE-STUFE2.md` kopieren und anpassen.

**Fertig, wenn:** K2 heißt „Das Muster“ und hat echte Fotos, K5 „Die Ernte und die Fäden“ ist da, keine Bedeutung ohne Beleg.

**Prompt für Claude Code:**
```
Stufe 2: Ab heute zeigt die Startseite das echte Proto. Halte dich an CLAUDE.md.
1. Kapitel K2 umbenennen in „Das Muster“. Für jedes Element ein Motiv-Block mit echtem Foto (in Shopify hochgeladen, Dateinamen: …): Kreuzstich-Band, Münztasche, Achtstern, Lebensbaum. Bedeutungstext nur dort, wo in docs/BELEGE.md „freigegeben: ja“ und eine Quelle steht. Lege docs/BELEGE.md als Tabelle an: Motiv | Bedeutungssatz | Quelle | Region | freigegeben ja/nein.
2. Neues Kapitel K5 „Die Ernte und die Fäden“ nach K4, Text aus docs/TEXTE-STUFE2.md. Nur Fotos am getragenen Teil. Sichel und Ähren nie freigestellt nebeneinander.
3. Prüfe alle Texte gegen die Sprachregeln in CLAUDE.md und markiere mir jeden Satz, der eine Regel berührt.
Zeig mir die Vorschau-Schritte. Commit nach meinem „passt“.
```

---

### Schritt 10 · Nummern-Raster 001–100
**Wann:** Sa 19.12. (nach der Kontingent-Entscheidung am selben Tag) · **Dauer:** 90 min
**Voraussetzung:** Vorbestell-Produkt angelegt (Docket Mo 14.12.), „Inventar verfolgen“ an. Ein Testprodukt „TT Test“ mit Bestand 35, auf Aktiv, aber in keiner Kollektion und nirgends verlinkt. *(Ob ein Produkt im Status „Entwurf“ in Liquid gelesen werden kann, ist ungeprüft. Darum für den Test kurz auf Aktiv, danach zurück.)*

**Fertig, wenn:** Das Raster zeigt mit „TT Test“ die richtige Zahl. Nach Senken des Bestands um 2 springt es. Du hast notiert, wie lange das dauert. „TT Test“ ist wieder Entwurf.

**Prompt für Claude Code:**
```
Baue sections/tt-nummern.liquid und assets/tt-nummern.js. Halte dich an CLAUDE.md.
- Liest aus den Theme-Einstellungen: tt_produkt_vorbestellung, tt_produkt_drop, tt_start_vorbestellung, tt_start_drop, tt_reserviert.
- Rechnet in Liquid: vorbestellt = tt_start_vorbestellung minus Summe von variant.inventory_quantity aller Varianten; drop_verkauft genauso mit tt_start_drop. Nie unter 0, nie über 100. Fehlt ein Produkt oder ist variant.inventory_management leer (Inventar nicht verfolgt), zeig das Raster NICHT und gib im Theme-Editor einen Hinweis aus.
- Zeichnet 100 Felder (10 × 10) als Kreuzstich-Raster in SVG oder CSS: vergeben = Kreuzstich Rot T17 mit Weiß T16, Creator/Reserve = Gold T14 (erst ab Zustand ZWISCHENZEIT, direkt nach den Vorbestellungen), frei = leeres Kästchen. Reihenfolge: Vorbestellungen ab 001, dann Creator/Reserve, dann Drop. Beim Antippen oder Fokus: „Nr. 017 · vergeben“ oder „frei“. Keine weiteren Daten zu einzelnen Nummern.
- Darüber eine Zeile in Worten („17 von 35 Vorbestellungen vergeben“, ab Drop „64 von 100 vergeben“), darunter „Stand: HH:MM“ (Uhrzeit aus tt-clock.js).
- tt-nummern.js: alle 60 Sekunden, nur wenn die Section sichtbar und der Tab aktiv ist, mit fetch('/?section_id=tt-nummern') neu holen und den Inhalt ersetzen, so wie Dawn in assets/cart.js Sections nachlädt. Bei Fehler alten Stand lassen.
- Wenn drop_verkauft >= tt_start_drop: data-tt-ausverkauft="true" setzen.
Erst mit „TT Test“ als tt_produkt_vorbestellung testen. Sag mir, wie ich den Bestand ändere und die Zeit bis zum Sprung messe. Commit nach meinem „passt“.
```

---

### Schritt 11 · Vorbestell-Zustände und Shop-Links
**Wann:** Di 05.01.2027 · **Dauer:** 60 min

**Was du tust zusätzlich:** Bei der Generalprobe der Vorbestellung am Mo 11.01. (Docket) testest du **auch Future Publishing**: das Vorbestell-Produkt auf „heute in 20 Minuten“ terminieren und beobachten. So weißt du schon im Januar, ob das Schloss für den 14.01. und den 22.04. so funktioniert, und nicht erst im April.

**Fertig, wenn:** Mit `?t=2027-01-14T18:59:30+01:00` wechselt die Seite pünktlich: Knopf „Vorbestellen · 149 €“ zur Vorbestellung, Countdown „Vorbestellpreis endet in …“, Raster sichtbar.

**Prompt für Claude Code:**
```
Baue die Zustände für die Vorbestellung. Halte dich an CLAUDE.md.
- tt-hero hört auf „tt:state“. WARTELISTE: wie bisher. VORBESTELLUNG: Überschrift „Vorbestellung offen“, Knopf „Vorbestellen · {{ Preis von tt_produkt_vorbestellung | money }}“, daneben durchgestrichen der Preis von tt_produkt_drop, Link zur Produktseite der Vorbestellung, Countdown bis tt_zeit_preisende, Zeile „Lieferung 22.–30.04.2027“. Formular darunter mit „Noch nicht? Auf die Liste“.
- Liquid rendert als Grundzustand den WARTELISTE-Text mit festem Datum. JavaScript schaltet um. Ohne JavaScript steht zusätzlich ein normaler Link „Zur Vorbestellung“, aber nur, wenn product.available für die Vorbestellung wahr ist.
- tt-shop-button: VORBESTELLUNG → „Vorbestellen“ → Produktseite.
- Preise nie als Text eintippen, immer aus Shopify.
Teste alle Grenzen aus docs/TERMINE.md mit ?t= und zeig mir die Links. Commit nach meinem „passt“.
```

---

### Schritt 12 · Analytics: UTM-Links, Tags, Wochenzahlen
**Wann:** Sa 09.01. · **Dauer:** 30 min

**Fertig, wenn:** Die UTM-Links stehen in beiden Bios und in deinen E-Mail-Vorlagen. Die Tracking-Tabelle (Docket W4) hat ein Blatt „Website“ mit den Spalten aus 3.8. Claude Code hat dir mit Link zur Shopify-Doku gesagt, ob eigene Ereignisse mit Einwilligung gehen.

**Prompt für Claude Code:**
```
Analytics für die Drop-Seite, schlank. Halte dich an CLAUDE.md.
1. Erzeuge die vier UTM-Links (Instagram-Bio, TikTok-Bio, QR-Druck, E-Mail) für DEINE-DOMAIN als Liste zum Kopieren und einen QR-Code als SVG in docs/ für den Druck-Link.
2. Schreib mir eine 5-Minuten-Anleitung für den Sonntag: In Shopify Kunden nach Tag filtern (tt-story, tt-huette, src-instagram, gr-w32 …) und in diese Spalten eintragen: Woche | Sitzungen Startseite | Anmeldungen tt-story | tt-huette | tt-feld | je Quelle | je Größe | Vorbestellungen | Anmeldequote.
3. Prüfe in der aktuellen Shopify-Dokumentation (shopify.dev), wie ein Theme eigene Ereignisse sendet (Custom Events über die publish-Methode) und wie das mit der Einwilligung im Cookie-Banner zusammenhängt. Sag mir mit Link, was gilt. Baue es NUR ein, wenn es ohne zusätzliche App und nur nach Einwilligung läuft: tt_kapitel, tt_motiv_offen, tt_formular, tt_shop_klick.
```

---

### Schritt 13 · Entscheidung: Spiel bauen oder streichen
**Wann:** Fr 05.02. · **Dauer:** 20 min (das ist die Docket-Aufgabe „Spiel: bauen oder streichen“)

**Was du tust:** Abschnitt 11 durchgehen, Zahlen eintragen, Prompt an Claude in der Docket-Sitzung (nicht an Claude Code).

**Fertig, wenn:** Die Entscheidung steht. Bei „streichen“ werden die Spiel-Aufgaben im Docket zu Notizen, es geht mit Schritt 14 weiter. Bei „bauen“ gelten A1–A8, Schritt 16 entfällt.

**Prompt (an Claude, Docket-Sitzung):**
```
Spiel-Entscheidung 05.02. Meine Zahlen: Vorbestellungen bis heute: __. Warteliste am 31.01.: __ (Korridor 1.500). Anmeldequote Startseite letzte 4 Wochen: __ %. Stiltest 27.12.: Pixel / Silhouette / nicht gemacht. Freie Abende pro Woche bis 21.03.: __.
Prüf die vier Bedingungen aus website.md Abschnitt 11 und sag mir klar: bauen oder streichen. Wenn bauen: welche Docket-Tage von Februar bis März dafür frei werden müssen.
```

---

### Schritt 14 · Shoot-Bilder in die Story
**Wann:** Sa 27.02. · **Dauer:** 60 min
**Voraussetzung:** Shoot Sa 20.02., Shop-Bilder aufbereitet Di 23.02. (Docket).

**Fertig, wenn:** Kopf, K5 und drei Stations-Blöcke haben Shoot-Fotos. Das erste große Bild ist in 750 px Breite höchstens 120 KB groß. Budget grün.

**Prompt für Claude Code:**
```
Tausche in der Story die Proto-Fotos gegen die Shoot-Fotos (Dateinamen: …). Halte dich an CLAUDE.md.
- Kopf: ein Hochformat-Bild als erstes großes Bild, image_tag mit preload, widths 375/750/1100. In 750 px Breite höchstens 120 KB. Zeig mir die echten Bytes.
- Lege in tt-kapitel einen Blocktyp „station“ an (Produkt-Auswahl, Foto, ein Satz). Preis aus dem Produkt, Link zum Produkt erst ab Zustand LIVE, vorher „22.04. · 19:00“. Drei Stationen: Jeans, Zipper, Polo.
- Führ tools/budget-check.mjs aus und miss die Seite einmal gedrosselt.
Commit nach meinem „passt“.
```

---

### Schritt 15 · Drop-Zustände: Schlüssel, Live, Ausverkauft
**Wann:** Do 04.03. · **Dauer:** 60 min

**Fertig, wenn:** Mit `?t=2027-04-22T18:00:30+02:00&key=…` ist die Tür offen, ohne Schlüssel läuft ein 60-Minuten-Countdown. Mit `?t=2027-04-22T19:00:30+02:00` ist die Seite LIVE. Mit „TT Test“ auf 0 zeigt sie AUSVERKAUFT.

**Prompt für Claude Code:**
```
Baue die Drop-Zustände. Halte dich an CLAUDE.md und docs/TERMINE.md.
- ZWISCHENZEIT: Countdown „Drop in …“ bis tt_zeit_drop. Das Formular heißt „Hol dir den Schlüssel“ (ort=tt-huette), darunter: „Am 22.04. um 18:00 kommt dein Schlüssel per E-Mail. Damit bist du eine Stunde früher drin.“
- SCHLUESSEL (18:00–19:00 und gültiger ?key=): Kopf „Die Tür ist offen“, Knopf zur Kollektion tt_kollektion. Ohne Schlüssel: Countdown bis 19:00 und Formular.
- LIVE: Kopf zeigt die drei Produkte mit Preis und Link, darunter das Nummern-Raster, Shop-Button „Zum Shop“.
- AUSVERKAUFT (data-tt-ausverkauft): „Alle 100 vergeben.“ Zipper und Polo weiter mit „auf Bestellung, Versand innerhalb von 3 Wochen“, Formular „Liste für den nächsten Drop“ (ort=tt-drop2).
- Ohne JavaScript: fester Text „Drop Do 22.04.2027, 19:00“ und ein Link zur Kollektion.
Teste jeden Zustand mit ?t= und zeig mir eine Tabelle: Zustand | Test-Link | was ich sehen muss. Commit nach meinem „passt“.
```

---

### Schritt 16 · „Der Weg zur Hütte“ (entfällt bei „bauen“)
**Wann:** Sa 06.03. · **Dauer:** 90 min

**Fertig, wenn:** Am Handy zieht das Feld beim Scrollen vorbei, die drei Stationen erscheinen, am Ende steht die Hütte mit dem Teppich. Mit „Bewegung aus“ sind es vier feste Bilder. Flaggen-Check meldet 0 Treffer.

**Prompt für Claude Code:**
```
Baue sections/tt-feld-scroll.liquid: „Der Weg zur Hütte“. Halte dich an CLAUDE.md (Palette, Flaggen-Regel, Budget).
1. Zeichne SVG-Silhouetten in der Palette: assets/tt-feld-himmel.svg (Sonnenuntergang in 5 harten Stufen T01–T05, Sonne T06, KEIN Blau), tt-feld-huegel.svg (T07), tt-feld-huette.svg (Tür zu und Tür offen als zwei Gruppen mit id), tt-feld-weizen-hinten.svg und tt-feld-weizen-vorn.svg (Ähren T08/T09, Lichtkante T10), tt-feld-stationen.svg (Vogelscheuche, Zaun, Wäscheleine als Umriss). Zusammen höchstens 25 KB.
2. Ein Bereich mit position: sticky, 400svh hoch. Beim Scrollen verschieben sich die Ebenen seitwärts mit den Faktoren Himmel 0 · Hügel 0,2 · Hütte 0,5 · Weizen hinten 0,8 · Weizen vorn 1,15. Nur transform, requestAnimationFrame, passive Scroll-Listener. Kein CSS animation-timeline, kein GSAP.
3. Bei 20 %, 45 % und 70 % erscheint je eine Stations-Karte (die Blöcke „station“ aus Schritt 14), gesteuert mit IntersectionObserver. Bei 100 % die Hütte: Tür je Zustand aus tt-clock.js zu oder offen; darunter Foto des Teppichs und die drei Teile.
4. Bei „Bewegung aus“ oder prefers-reduced-motion: keine Bewegung, vier feste Bilder untereinander.
5. Lege tools/flaggen-check.mjs an (Node, ohne Pakete; liest bei SVG die Farben aus fill, stroke und stop-color): Alarm bei Farbton 180–250°, Sättigung über 25 % und Helligkeit über 45 %. Führ ihn aus.
6. Die Section bleibt bis tt_zeit_feld_oeffentlich (29.03., 18:00) ausgeblendet, außer im Testmodus mit ?t=.
Danach budget-check. Commit nach meinem „passt“.
```

---

### Schritt 17 · Gerätetest und strenger Prüf-Prompt
**Wann:** Mo 08.03. · **Dauer:** 60 min

**Was du tust vorher:** Abschnitt 7 dieser Datei nach `tt-theme/docs/TESTPLAN.md` kopieren. Ein zweites Handy leihen (Android oder kleines iPhone).

**Fertig, wenn:** Tests T1–T13 und T16 sind bestanden oder als Aufgabe notiert, die fünf schwersten Probleme sind repariert.

**Prompt für Claude Code:**
```
Prüf die ganze Startseite wie ein strenger Tester vor einem Verkaufsstart. Halte dich an CLAUDE.md. Arbeite die Tests T1–T13 und T16 aus docs/TESTPLAN.md ab, soweit du sie selbst prüfen kannst. Für alles, was nur ich am Handy prüfen kann (Instagram-In-App, TikTok-In-App, kleines iPhone, Android, Querformat), gib mir eine Checkliste zum Abhaken. Dazu: Gesamtgewicht, Zeit bis zum ersten Bild gedrosselt, Verhalten ohne JavaScript, Tastatur.
Probleme als Liste nach Schwere. Repariere die ersten fünf, dann stopp und zeig mir die Änderungen.
```

---

### Schritt 18 · PLAN B anlegen und Umschalten üben
**Wann:** Mi 17.03. · **Dauer:** 20 min (gleiche Docket-Aufgabe)

**Was du tust:** Am besten spät abends. Stoppuhr an. `shopify theme publish --theme "PLAN B" --force` [W7], Seite am Handy neu laden, Zeit notieren. Dann `shopify theme publish --theme "TT Story" --force`, wieder Zeit notieren.

**Fertig, wenn:** PLAN B existiert unverändert, beide Wechsel dauerten unter einer Minute.

**Prompt für Claude Code:**
```
Ich übe gleich PLAN B. Prüfe nur mit shopify theme list, ob es ein Theme „PLAN B“ und ein Theme „TT Story“ gibt und welches live ist. Zeig mir die zwei publish-Befehle zum Kopieren. Führ selbst nichts aus.
```

---

### Schritt 19 · Stiller Launch Stufe 4
**Wann:** Mo 22.03. · **Dauer:** 30 min · öffentlich ab Mo 29.03., 18:00 mit T−24

**Was du tust:** Push nach Prüfung. Das Feld-Kapitel (oder bei A das Spiel) erscheint für alle automatisch am 29.03. um 18:00. Bis dahin 48 Stunden echte Besucher auf allem anderen. Selbst aus Instagram öffnen.

**Fertig, wenn:** Stufe 4 ist auf „TT Story“ live, das Feld erscheint mit `?t=2027-03-29T18:00:30+02:00`, in 48 Stunden keine Fehler.

**Prompt für Claude Code:**
```
Stiller Launch Stufe 4. Prüfe: git status sauber, budget-check grün, flaggen-check 0 Treffer, theme check ohne Fehler in tt-Dateien, tt_zeit_feld_oeffentlich = 2027-03-29T18:00:00+02:00. Dann push auf „TT Story“ erst nach meinem „ja“. Danach eine Checkliste für 48 Stunden Beobachtung: was ich am Handy anschaue und wo ich in Shopify die Anmeldungen der letzten 48 Stunden mit Tag tt-huette sehe.
```

---

### Schritt 20 · Generalprobe mit Testprodukt
**Wann:** Fr 09.04. · **Dauer:** 45 min

**Was du tust:**
1. `shopify theme duplicate --theme "TT Story" --name "TT Probe"` [W7].
2. In „TT Probe“ (Theme-Editor): `tt_zeit_schluessel` auf heute in 30 Minuten, `tt_zeit_drop` auf heute in 45 Minuten, „TT Test“ zu 1 € als Drop-Produkt.
3. „TT Test“ in Shopify auf heute in 30 Minuten terminieren. Falls die Terminierung am 11.01. nicht ging: von Hand auf Aktiv stellen und die Zeit stoppen.
4. Über die Vorschau von „TT Probe“ alles durch: Feld, Schlüssel-Link, Tür, Produkt, Kauf mit echter Karte, Erstattung.
5. „TT Probe“ löschen, „TT Test“ zurück auf Entwurf.

**Fertig, wenn:** Die Generalprobe lief einmal komplett durch, und dein Ablauf für 18:00 am Drop-Tag steht (Terminierung oder Handbetrieb).

**Prompt für Claude Code:**
```
Generalprobe heute auf der Theme-Kopie „TT Probe“. Ändere NICHTS an „TT Story“. Jetzt ist __:__. Gib mir eine Liste mit Uhrzeiten: wann ich was öffne, welche Links mit ?key= und ohne, was ich jeweils sehen muss, und eine Tabelle zum Ausfüllen: Schritt | erwartet | gesehen | ok. Am Ende: wie ich „TT Probe“ lösche.
```

---

### Schritt 21 · Schlüssel-Link in die E-Mail T−1h
**Wann:** Do 15.04. · **Dauer:** 20 min (gleiche Docket-Aufgabe)

**Was du tust:** Neuen Schlüssel in den Theme-Einstellungen von „TT Story“ setzen, z. B. `weizen-0422`. Den Link aus dem Prompt in den Entwurf der E-Mail T−1h. In einem privaten Fenster mit `&t=2027-04-22T18:00:30+02:00` testen (Testmodus ist bis 17.04. an).

**Fertig, wenn:** Der Schlüssel-Link steht in der E-Mail und öffnet im Testmodus die Tür.

**Prompt für Claude Code:**
```
Hol mit shopify theme pull --theme "TT Story" --only config/settings_data.json die aktuellen Einstellungen und lies sie mir vor: alle tt_zeit_*, tt_schluessel, Produkte, Kollektion, Startmengen, Testmodus. Vergleiche mit docs/TERMINE.md und markiere jede Abweichung. Erzeuge den Schlüssel-Link für die E-Mail T−1h: https://DEINE-DOMAIN/?key=<schluessel>&utm_source=email&utm_medium=newsletter&utm_campaign=tt-t1h. Ändere nichts.
```

---

### Schritt 22 · Code-Freeze
**Wann:** Sa 17.04. · **Dauer:** 5 min (gleiche Docket-Aufgabe)

**Was du tust:** In den Theme-Einstellungen von „TT Story“ den Testmodus AUS. Ab jetzt keine Änderung am Code, auch keine Kleinigkeit. Nur noch der Listenstand am Sonntag.

**Fertig, wenn:** Testmodus aus, ein `?t=`-Link wirkt nicht mehr, letzter Commit „Freeze 17.04.“.

**Prompt für Claude Code:**
```
Code-Freeze. Mach einen letzten Commit „Freeze 17.04.“ und einen Git-Tag „drop-2027-04-22“. Hol mit shopify theme pull --theme "TT Story" --only config/settings_data.json die Einstellungen und bestätige mir, dass tt_testmodus aus ist. Sag mir einen ?t=-Link, mit dem ich prüfe, dass er nicht mehr wirkt. Danach änderst du an diesem Repo nichts mehr bis zum 25.04.
```

---

### Schritt 23 · Drop-Tag (Website-Teil)
**Wann:** Do 22.04. · **Dauer:** ~30 min, verteilt

| Uhrzeit | Was |
|---|---|
| 17:30 | Startseite am Handy und am Laptop: ZWISCHENZEIT, Countdown stimmt |
| 17:50 | Schlüssel-Link im privaten Fenster: Tür noch zu, 10 Minuten Countdown |
| 17:55 | Nur bei Handbetrieb: Produkte im Admin geöffnet, bereit zum Umstellen |
| 18:00 | Produkte sichtbar? Schlüssel-Link: Tür offen? (E-Mail T−1h geht laut Docket raus) |
| 19:00 | Ohne Schlüssel: LIVE? Kollektion zeigt alle drei Produkte? |
| 19:15 · 20:00 · 21:00 | Springt das Nummern-Raster mit den Bestellungen? |
| jederzeit | Hängt etwas: PLAN B (Schritt 18). Nicht debuggen |

**Fertig, wenn:** Die Tür war um 18:00 und um 19:00 offen, oder PLAN B läuft.

**Prompt für Claude Code (morgens):**
```
Heute ist Drop-Tag. Du änderst nichts. Gib mir nur meinen Website-Ablauf von 17:30 bis 21:00 als Checkliste mit Uhrzeiten und die zwei PLAN-B-Befehle zum Kopieren.
```

---

### Schritt 24 · Auswertung und Modus nach dem Drop
**Wann:** So 25.04. · **Dauer:** 20 min (zusammen mit Docket „Auswertung nach 72 Stunden“)

**Fertig, wenn:** Die Zahlen stehen im Blatt „Website“. Entschieden ist, was die Startseite die nächsten 4 Wochen zeigt (Vorschlag: „Zipper und Polo auf Bestellung“ + Liste für Drop 2).

**Prompt für Claude Code:**
```
Auswertung Website nach 72 Stunden. Meine Zahlen: Sitzungen Startseite __, Anmeldungen je Ort (tt-story __, tt-huette __, tt-feld __, tt-drop2 __), Bestellungen __. Rechne die Anmeldequote und sag mir in 5 Sätzen: Was hat die Seite gebracht, was nicht, was nehme ich für Drop 2 mit. Der Code-Freeze endet heute: Schlag mir die eine Änderung vor, die sich für die nächsten 4 Wochen lohnt.
```

---

### A1 · Graubox (nur bei „bauen“)
**Wann:** Di 09.02. · **Dauer:** 60 min (ersetzt die drei Docket-Aufgaben 09.–11.02., die Werkzeuge hast du seit Schritt 1)

**Fertig, wenn:** Am Handy läuft ein graues Rechteck flüssig durchs Feld, Tippen = hinlaufen. Phaser lädt erst nach „Ins Feld“ (im Netzwerk-Tab geprüft).

**Prompt für Claude Code:**
```
Baue einen Graubox-Prototyp für das Pixel-Spiel als neue Section sections/tt-feld.liquid. Halte dich an CLAUDE.md.
- Hol Phaser 3.90.0 über npm (npm pack phaser@3.90.0 in einem Ordner AUSSERHALB des Themes) und kopiere dist/phaser.min.js nach assets/phaser-3.90.0.min.js. Nicht von einem CDN laden.
- Szene 0 ist HTML: Platzhalter-Standbild, Knopf „Ins Feld“, tt-shop-button, Link „Ohne Spiel ansehen“ zur Story. phaser-3.90.0.min.js und assets/tt-feld.js werden erst beim Tippen auf „Ins Feld“ per <script> nachgeladen.
- Phaser-Config: type AUTO, pixelArt: true, banner: false, width 180, height 320, scale.mode NONE. Zoom selbst rechnen: max(1, floor(min(innerWidth/180, innerHeight/320))), bei resize neu. Canvas aria-hidden.
- Seitenansicht: Weg 720 px breit, Kamera folgt der Figur mit Totzone. Figur = graues Rechteck 16×32. Tippen irgendwo = Figur läuft dorthin (60 px/s). Dazu zwei HTML-Knöpfe ◀ ▶ (44×44, halten = laufen) und Pfeiltasten.
- Section-Einstellung „Spiel zeigen“ (checkbox). Aus = die Section rendert nur den Link zur Story.
- In templates/index.json tt-feld-scroll durch tt-feld ersetzen. tt-feld-scroll bleibt als Datei liegen.
Keine weiteren Features. Erklär mir danach, wie ich es am Handy teste und wo ich im Netzwerk-Tab sehe, dass Phaser erst nach dem Tippen lädt. Commit nach meinem „läuft“. Melde mir, falls der Upload der 1,2-MB-Datei zu Shopify scheitert.
```

---

### A2 · Palette und Flaggen-Check für PNG
**Wann:** Mo 15.02. · **Dauer:** 30 min

**Fertig, wenn:** Die Palette ist in Aseprite oder LibreSprite geladen, der Flaggen-Check prüft auch PNG.

**Prompt für Claude Code:**
```
1. Erzeuge die 17 Farben aus CLAUDE.md als Palette in zwei Formaten: tools/tt-palette.gpl (GIMP-Palette) und tools/tt-palette.hex (eine Hex-Farbe pro Zeile), Namen T01–T17. Sag mir, welches Format meine Aseprite- oder LibreSprite-Version lädt und wo ich es einstelle.
2. Erweitere tools/flaggen-check.mjs um PNG (ohne Pakete, mit zlib aus Node; indizierte und RGBA-PNGs). Alarm bei Farbton 180–250°, Sättigung über 25 %, Helligkeit über 45 %. Zusätzlich Warnung bei jeder Farbe, die nicht in der Palette ist.
```

---

### A3 · Steuerung am Daumen
**Wann:** Di 16.02. · **Dauer:** 20 min

**Fertig, wenn:** Laufen mit dem Daumen fühlt sich gut an. Vorher wird keine Grafik eingebaut.

**Prompt für Claude Code:**
```
Ich teste gleich die Steuerung am Handy. Gib mir 6 Dinge, auf die ich achten soll (Reaktionszeit, Tippen am Rand, Halten der Knöpfe, ob die Seite beim Spielen mitscrollt, Querformat, Zurück-Wischen in Instagram). Danach beschreibe ich dir, was sich falsch anfühlt, und du reparierst nur das.
```

---

### A4 · Pixel-Art zeichnen (3 Abende)
**Wann:** Do 18.02., Mo 22.02., Mi 24.02. · **Dauer:** je 90 min. *(Docket hatte den dritten Abend am 25.02.; da steht schon „Kampagnenfilm schneiden“, deshalb Mi 24.02.)*

**Was du tust:** Die 12 Dateien aus 5.2 mit der Palette T01–T17. Export wie in 5.2.
- Abend 1: Figur, Himmel, Hügel, Weizen hinten
- Abend 2: Weizen vorn, Hütte, Vogelscheuche, Zaun
- Abend 3: Leine, Glanz, Innenraum, Standbild

**Fertig, wenn:** 12 PNG + JSON in `assets/`, Flaggen-Check 0 Treffer, zusammen höchstens 150 KB.

**Prompt für Claude Code (nach jedem Abend):**
```
In assets/ liegen neue Aseprite-Exporte (PNG + JSON). Prüfe jede Datei gegen docs/ASSETS.md (lege die Tabelle aus Abschnitt 5.2 an, ich füge sie ein): Größe in Pixeln, Tags vorhanden und richtig geschrieben, nur Palettenfarben (flaggen-check.mjs), Dateigröße. Gib mir eine Tabelle Datei | ok | Problem. Ändere die Bilder nicht.
```

---

### A5 · Grafik einbauen
**Wann:** Fr 26.02. · **Dauer:** 60 min

**Fertig, wenn:** Das Feld sieht aus wie gezeichnet, die Pixel sind scharf, der Weizen wiegt versetzt. Spiel gesamt ≤ 1,5 MB roh.

**Prompt für Claude Code:**
```
Ersetze die Grauboxen in assets/tt-feld.js durch meine Aseprite-Exporte in assets/: tt-figur, tt-himmel, tt-huegel, tt-weizen-hinten, tt-weizen-vorn, tt-huette.
- Laden mit this.load.aseprite(key, png, json), Animationen mit this.anims.createFromAseprite(key). Figur: Tags „stehen“ und „laufen“, nach links flipX.
- Parallax mit setScrollFactor: Himmel 0 · Hügel 0.2 · Hütte 0.5 · Weizen hinten 0.8 · Weizen vorn 1.15 (vor der Figur).
- Weizen wiegt in einer 3-Frame-Schleife, jede Kachel mit eigenem Startframe, damit es nicht im Gleichtakt zuckt. Bei „Bewegung aus“ oder prefers-reduced-motion steht der Weizen still.
- Pixel bleiben scharf: keine Glättung, nur ganzzahliger Zoom.
Danach budget-check (Spiel gesamt höchstens 1,5 MB roh). Commit nach meinem „passt“.
```

---

### A6 · Stationen, Karten, Formular an der Tür
**Wann:** Mo 01.03. · **Dauer:** 90 min

**Fertig, wenn:** Drei Stationen öffnen HTML-Karten mit Preis aus Shopify. An der Tür steht das Formular. Eine Test-Anmeldung kommt mit Tag `tt-feld` an.

**Prompt für Claude Code:**
```
Füge Stationen und Hütte hinzu. Neue Dateien in assets/: tt-vogelscheuche, tt-zaun, tt-leine, tt-glanz.
- Reihenfolge am Weg: Jeans an der Vogelscheuche (x≈150), Zipper am Zaun (x≈330), Polo auf der Leine (x≈510), Hütte (x≈660). Über jeder Station funkelt tt-glanz (aus bei „Bewegung aus“).
- Tippen auf eine Station: Figur läuft hin, dann öffnet sich eine Karte als HTML über dem Spiel, nicht im Canvas: Name, ein Satz, Preis aus dem Produkt in den Theme-Einstellungen, Zeile je Zustand („22.04. · 19:00“ oder Link zum Produkt ab LIVE). Schließen mit ×, Esc oder Tippen daneben. Fokus springt in die Karte und danach zurück.
- An der Hüttentür: snippets/tt-warteliste-form.liquid mit ort=tt-feld, Titel „Hol dir den Schlüssel“.
- Unter dem Spiel die Liste „Ohne Spiel ansehen“ mit denselben drei Karten als normales HTML.
Zeig mir danach, wo ich in Shopify die Anmeldungen mit Tag tt-feld sehe. Commit nach meinem „passt“.
```

---

### A7 · Tür mit Zuständen, Innenraum, Ladezeit
**Wann:** Mi 03.03. · **Dauer:** 60 min (Docket hat dort schon „Button ‚Direkt zum Shop‘ prüfen“)

**Fertig, wenn:** Die Tür folgt `tt-clock.js` (zu, Schlüssel, offen), ab LIVE startet man vor der Tür, der Innenraum verlinkt die Produkte, vor dem Tippen lädt kein Byte Phaser.

**Prompt für Claude Code:**
```
Verbinde das Spiel mit assets/tt-clock.js. Im Spiel wird keine eigene Zeit gerechnet.
- Ereignis „tt:state“: WARTELISTE, VORBESTELLUNG, ZWISCHENZEIT → Tür zu, Countdown als HTML über der Tür. SCHLUESSEL → Tür öffnet (Tag „auf“). LIVE → Tür offen, der Spieler startet direkt vor der Tür. AUSVERKAUFT → Tür offen, innen ein Schild „100/100“ an der Jeans, Zipper und Polo kaufbar.
- Innenraum tt-innen: Tippen auf eines der drei Teile = Produktseite (normaler Link, gleicher Tab).
- tt-standbild als Szene 0 (HTML-<img>, höchstens 40 KB, preload).
- <noscript>-Block mit den drei Produktlinks und dem Drop-Datum.
- Miss: Bytes bis zum ersten Bild ohne Tippen (darf kein Phaser enthalten) und Bytes nach „Ins Feld“. Führ budget-check aus.
Teste alle Zustände mit ?t= und ?key=. Commit nach meinem „passt“.
```

---

### A8 · Playtest mit 5 Leuten
**Wann:** Sa 13.03. · **Dauer:** 60 min (gleiche Docket-Aufgabe)

**Was du tust:** 5 Leute, Handy in die Hand, nur ein Satz: „Kauf dir die Jeans.“ Vorschau im Testmodus mit `?t=2027-04-22T19:00:30+02:00`. Nicht helfen. Notieren: Wer findet den Shop, wie lange, wo hängt jemand.

**Fertig, wenn:** 4 von 5 finden Tür und Shop ohne Hilfe. Die Hänger, die einen Kauf verhindern, sind repariert.

**Prompt für Claude Code:**
```
Hier sind meine Notizen vom Playtest mit 5 Leuten: … Ordne die Probleme nach „verhindert Kauf“, „kostet Zeit“, „stört nur“. Repariere nur „verhindert Kauf“, dann stopp und zeig mir die Änderungen.
```

---

## 10 · Was vor dem 05.02. schon sinnvoll ist, egal ob mit Spiel

| Was | Ab | Warum jetzt |
|---|---|---|
| **Dawn-Warteliste** (Docket Do 08.10., ohne Code) | 08.10. | Liste läuft ab dem ersten Post am 12.10. Wird ab 18.11. zu PLAN B |
| **Countdown bis Vorbestellung** | 18.11. | Jeder Post hat ab dann ein Datum. Wer die Seite öffnet, sieht, wann es losgeht |
| **Formular mit Quellen-Tags** | 18.11. | Du siehst, welcher Kanal Adressen bringt. Wichtig für den Zielkorridor 700 bis 31.12. |
| **Größe bei der Anmeldung** | 18.11. | Echte Größenverteilung für die Entscheidung am Sa 19.12. statt Startannahme |
| **Listenstand mit Datum** | 18.11. | Echte Zahl als sozialer Beweis, jeden Sonntag 3 Minuten |
| **Prozess-Story Stufe 1** | 18.11. | Zeigt, dass hier wirklich gebaut wird, ohne Produkt zu zeigen (Regel 01.10.) |
| **PLAN B** | 18.11. | Ab dem ersten Live-Gang gibt es einen Rückweg |
| **Echte Proto-Fotos, Stufe 2** | 11.12. | Der erste Moment, in dem die Seite das Produkt zeigen darf |
| **Nummern-Raster** | 19.12. gebaut, sichtbar ab 14.01. | „X von 35“ ist der Kern des Contents vom 04.01. bis 07.02. (Plan 10) |
| **Vorbestell-Zustände** | 05.01. | Startseite schaltet am 14.01. um 19:00 von selbst um |
| **Future Publishing testen** | Mo 11.01. | Klärt das Schloss drei Monate vor dem Drop |
| **Analytics-Grundlage** | 09.01. | Ohne Zahlen ist die Spiel-Entscheidung am 05.02. Bauchgefühl |
| Spiel-Stiltest (Docket So 27.12., 150 min) | 27.12. | **Nur machen, wenn du A ernsthaft willst.** Sonst die 150 Minuten in Content stecken |

**Nicht vor dem 05.02.:** Phaser, Pixel-Art, Feld-Scroll-Szene. Die gehören zu Stufe 4 im März.

---

## 11 · Entscheidung am Fr 05.02.

**Bauen nur, wenn alle vier stimmen:**
1. **Mindestens 10 Vorbestellungen** (Schwelle 01.02., Plan 6).
2. **Drei zusätzliche Abende pro Woche** à 60–90 Minuten bis 21.03. frei (Plan 5.1).
3. **Die Warteliste liegt im Korridor:** mindestens 1.500 am 31.01. (Plan 6). Liegt sie darunter, gehört jede freie Stunde den Videos, nicht dem Spiel.
4. **Der Stiltest vom 27.12. hat getragen:** Du hast eine Figur und eine Weizen-Kachel gezeichnet und würdest das zehnmal in dieser Qualität schaffen.

**Fehlt eine:** streichen. Die Story B hat dann das Feld als Scroll-Szene (Schritt 16). Die 27 Spiel-Aufgaben im Docket werden zu Notizen.

**Mein Rat:** streichen. Die Kampagne verkauft, das Spiel ist Kür. Wenn du nach dem Drop Zeit hast, ist das Spiel ein starkes Gerüst für Drop 2.

---

## 12 · Offene Punkte

1. **Future Publishing:** in dieser Sitzung nicht belegt. Test am Mo 11.01. (Schritt 11) und Fr 09.04. (Schritt 20). Ersatz: Handbetrieb um 18:00.
2. **Mehrere Tags in `contact[tags]`** und neue Tags für bestehende Adressen: Test am Mi 11.11. (Schritt 5). Ersatz: zusammengesetzter Tag.
3. **Double-Opt-in:** Pfad im Admin vor Ort (Docket Di 06.10.).
4. **Theme-Obergrenze** der Bibliothek: nicht belegt. Es gibt die Meldung „Maximum number of themes reached“ [W7].
5. **Upload-Grenze für Theme-Dateien** (nur A, Phaser 1,2 MB): nicht belegt, Test in A1.
6. **Kompression im Shopify-CDN:** Test in Schritt 7.
7. **Liefert Shopify die Section im Nummern-Raster aus einem Cache?** Test in Schritt 10.
8. **In-App-Browser von Instagram und TikTok:** Höhe (`svh`), Zurück-Wischen, Formular. Test in Schritten 7 und 17.
9. **Liquid-Zugriff auf Produkte im Status Entwurf:** ungeprüft, Test in Schritt 10.
10. **Custom Events und Einwilligung:** Claude Code prüft an der Shopify-Doku (Schritt 12).
11. **Shopify-Email-Kontingent im April** (6 Mails × 3.000): siehe `tools.md`, nicht belegt.
12. **Belegtabelle für Ornament-Bedeutungen** (Spec Teil 5) fehlt noch. Ohne sie keine Bedeutungstexte auf der Seite.
13. **Deine Entscheidungen:** neutrale Namen nach außen (Kreuzstich-Band, Achtstern, „Time Travel“) · Serp auf der Startseite ja oder nein · ein Theme mit Zuständen statt Theme-Wechsel um 19:00 · Teppich-Foto der Familie.
14. **Welches Theme ist live** (Dawn oder Horizon)? Schritt 2.
15. **Aseprite-Preis** (~20 € laut Plan) und Lizenz vor dem Kauf ansehen [W25]. LibreSprite ist die kostenlose Alternative [W26].
16. **BFSG-Ausnahme** für Kleinstunternehmen: beim Rechtstexte-Anbieter bestätigen.

---

## 13 · Quellen

Geprüft am 07.10.2026 in dieser Sitzung. 26 Quellen.

- **[W1]** Phaser, Releases auf GitHub: v3.90.0 (23.05.2025), v4.0.0 (10.04.2026), v4.1.0 (30.04.2026), v4.2.0 (19.06.2026), v4.2.1 (09.07.2026). https://github.com/phaserjs/phaser/releases
- **[W2]** Phaser v3.90.0, Release-Notiz „Version 3.90 – Tsugumi – 23rd May 2025“. https://github.com/phaserjs/phaser/releases/tag/v3.90.0
- **[W3]** npm-Registry `phaser`: Veröffentlichungsdaten (3.90.0 am 23.05.2025, keine neuere 3.x; latest = 4.2.1). Eigene Messung der Pakete `phaser-3.90.0.tgz` (`dist/phaser.min.js` 1.196.122 Byte, gzip -9 314.863 Byte; `phaser-arcade-physics.min.js` 1.086.308 / 282.301) und `phaser-4.2.1.tgz` (`dist/phaser.min.js` 1.375.976 / 352.227). https://registry.npmjs.org/phaser
- **[W4]** Phaser 3.90.0, Quelltext im npm-Paket: `src/animations/AnimationManager.js` (`createFromAseprite`, seit 3.50.0, Export-Anleitung), `src/loader/filetypes/AsepriteFile.js` (`this.load.aseprite`), `src/core/Config.js` (`pixelArt` → `antialias` aus, `roundPixels` an; `banner: false`), `src/scale/const/SCALE_MODE_CONST.js` (NONE … EXPAND). Gleiche Dateien unter https://github.com/phaserjs/phaser/tree/v3.90.0/src
- **[W5]** Phaser `package.json`, Lizenz MIT (3.90.0 und 4.2.1). https://registry.npmjs.org/phaser
- **[W6]** GSAP 3.15.0 (npm, 13.04.2026), README: „GSAP is now 100% FREE including ALL of the bonus plugins … even for commercial use“, Standard „no charge“ license. Eigene Messung: `gsap.min.js` 72.927 / 28.268 Byte gzip, `ScrollTrigger.min.js` 44.575 / 17.998. https://registry.npmjs.org/gsap · https://github.com/greensock/GSAP
- **[W7]** Shopify CLI 4.8.5 (npm, 06.10.2026), `engines.node >= 22.12.0`; Hilfetexte von `shopify theme dev | push | pull | publish | duplicate | list | rename | share | check` in Version 4.8.5 lokal ausgeführt (u. a. `--store` nimmt auch das Präfix, `duplicate` kennt die Meldung „Maximum number of themes reached“, `dev` liefert einen teilbaren Vorschau-Link); `.shopifyignore` wird im CLI-Code ausgewertet. README: `npm install -g @shopify/cli`, `brew tap shopify/shopify && brew install shopify-cli`. https://registry.npmjs.org/@shopify/cli · https://github.com/Shopify/cli
- **[W8]** Liquid-Referenz von Shopify, mitgeliefert in `@shopify/cli@4.8.5` unter `dist/data/` (`filters.json`, `tags.json`, `objects.json`, `section.json`, `setting.json`; Online-Fassung auf shopify.dev, dort in dieser Sitzung gesperrt): `date` mit `'now'` („timestamp will reflect the time that the Liquid was last rendered … caching“), `form 'customer'` (Newsletter ohne Konto), `return_to`, `variant.inventory_quantity` (ohne Inventarverfolgung „number of items sold“), `variant.inventory_management`, `image_url` (Breite oder Höhe Pflicht, `quality` 10–90), `image_tag` (`widths`, `sizes`, `preload`), Section-Schema (höchstens 50 Blöcke), Einstellungstypen (u. a. text, checkbox, number, product, collection, url, richtext, image_picker, font_picker; kein Datumstyp).
- **[W9]** Shopify-Systemübersetzungen, mitgeliefert in `@shopify/cli@4.8.5` (`shopify_system_translations.json`): „Protected by hCaptcha“, „This site is protected by hCaptcha …“, „To continue, let us know you're not a robot.“
- **[W10]** Dawn, `sections/newsletter.liquid`: `{% form 'customer' %}`, `contact[tags]` = newsletter, `contact[email]`, `form.posted_successfully?`. https://github.com/Shopify/dawn/blob/main/sections/newsletter.liquid
- **[W11]** Dawn, `assets/cart.js` und `assets/facets.js`: Teile der Seite per `?section_id=` nachladen. https://github.com/Shopify/dawn/blob/main/assets/cart.js
- **[W12]** Dawn, Releases: 16.0.0 aktuell; 15.5.0 „Adds support for standard storefront events“. https://github.com/Shopify/dawn/releases
- **[W13]** Horizon, README: „flagship of a new generation of first party Shopify themes … theme blocks“. https://github.com/Shopify/horizon
- **[W14]** `@shopify/web-pixels-extension` 2.18.0 (npm), Typdefinition `CustomEvent`: „custom events emitted by partners or merchants via the `publish` method“. https://registry.npmjs.org/@shopify/web-pixels-extension
- **[W15]** Theme Check in `@shopify/cli@4.8.5`: Prüfung `AssetSizeJavaScript` „Prevent Large JavaScript bundles“, rechnet mit komprimierter Größe, `recommended: false`.
- **[W16]** MDN, Date-Header: „contains the date and time at which the message originated“. https://github.com/mdn/content/blob/main/files/en-us/web/http/reference/headers/date/index.md
- **[W17]** MDN, Age-Header: „time in seconds for which an object was in a proxy cache“. https://github.com/mdn/content/blob/main/files/en-us/web/http/reference/headers/age/index.md
- **[W18]** MDN, `prefers-reduced-motion`. https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/prefers-reduced-motion/index.md
- **[W19]** MDN Browser-Kompatibilitätsdaten, `animation-timeline`: Chrome 115, Safari 26, Firefox nur Vorschau. https://github.com/mdn/browser-compat-data/blob/main/css/properties/animation-timeline.json
- **[W20]** MDN Browser-Kompatibilitätsdaten, `IntersectionObserver`: Chrome 51, Safari 12.1, Firefox 55. https://github.com/mdn/browser-compat-data/blob/main/api/IntersectionObserver.json
- **[W21]** WCAG 2.2, Erfolgskriterien 1.4.3 Kontrast (4,5:1, groß 3:1), 2.1.1 Tastatur, 2.2.2 Pausieren/Stoppen/Ausblenden (> 5 s), 2.3.3 Animation durch Interaktion (AAA), 2.5.8 Zielgröße (24 × 24 CSS-Pixel). https://github.com/w3c/wcag/tree/main/guidelines/sc
- **[W22]** IANA-Zeitzonendatenbank, Datei `europe`: `Rule EU 1981 max - Mar lastSun 1:00u 1:00 S`, `Europe/Berlin` folgt `EU`. Daraus berechnet: Sommerzeit ab So 28.03.2027. https://github.com/eggert/tz/blob/main/europe
- **[W23]** Claude Code, Advanced setup: macOS 13.0+, `curl -fsSL https://claude.ai/install.sh | bash`, `brew install --cask claude-code`, Pro/Max/Team/Enterprise/Console-Konto nötig. https://code.claude.com/docs/en/setup
- **[W24]** Claude Code, Memory: Projekt-`CLAUDE.md` wird in jeder Sitzung geladen, Prüfung mit `/context`. https://code.claude.com/docs/en/memory
- **[W25]** Aseprite, README: Vertrieb unter EULA, Preis nicht im README. https://github.com/aseprite/aseprite
- **[W26]** LibreSprite, README: kostenlos, Open Source (GPLv2), Releases für macOS. https://github.com/LibreSprite/LibreSprite

**Interne Quellen:** `docs/time-travel-drop-plan.md` (Rev. 5.3), `docs/produkt-spec_rev13.md`, `docs/uebergabe-time-travel.md`, `r5/weeks_r5.json` und `r5/docket_r5.html` (Spiel-Bauplan, Docket-Lasten pro Tag), `rev6/research/zielgruppe.md`, `community.md`, `tools.md`.

---

## Anhang A · CLAUDE.md für das Theme-Repo

In `~/Claude/Novalife/website/tt-theme/CLAUDE.md` kopieren (Schritt 3). DEIN-SHOP und DEINE-DOMAIN ersetzen.

````markdown
# Novalife Time Travel · Theme-Repo

## Was das ist
Kopie des Shopify-Themes von Novalife, in Shopify „TT Story“ (Shop: DEIN-SHOP.myshopify.com, Domain: DEINE-DOMAIN).
Hier entsteht die Startseite für den Drop „Time Travel“: 100 nummerierte, bestickte Jeans, Drop Do 22.04.2027, 19:00 Berlin.
Ich (Ernest) bin neu auf dem Mac und kein Entwickler. Erklär kurz, auf Deutsch, in einfachen Sätzen.

## Harte Regeln
1. Das Live-Theme wird nie angefasst. Kein --live, kein --allow-live, kein `shopify theme publish`. Veröffentlichen mache ich selbst.
2. Kein `shopify theme push` ohne mein „ja“. Ziel ist immer --theme "TT Story" (oder eine Kopie, die ich nenne).
3. Nach jedem Schritt, der auf meinem Handy funktioniert: Commit mit kurzer deutscher Nachricht. Vor größeren Umbauten fragen.
4. Keine neuen Bibliotheken, Apps oder externen Skripte ohne Rückfrage. Nichts von fremden CDNs laden. Alles liegt in assets/.
5. Eigene Dateien heißen tt-*. Bestehende Theme-Dateien nur ändern, wenn es nicht anders geht, und mir sagen, welche.
6. Zeit nie aus Liquid 'now' (gecacht) und nie nur vom Handy. Immer über assets/tt-clock.js (Serverzeit aus Date + Age von /cart.js).
7. Das echte Schloss ist Shopify (Produkt sichtbar oder nicht). Die Seite zeigt Zustände nur an.
8. „Direkt zum Shop“ ist immer sichtbar, als echter Link außerhalb von Canvas und Animationen.
9. Jede Section funktioniert ohne JavaScript: Liquid rendert Datum, Text, Formular und Links.
10. Formulare normal absenden (POST), nie per fetch. Shopify kann eine hCaptcha-Abfrage zeigen.
11. Barrierefreiheit: Kontrast ≥ 4,5:1, Tippziele ≥ 44 × 44 px, alles per Tastatur, sichtbarer Fokus, prefers-reduced-motion, Schalter „Bewegung aus“, Alt-Texte.
12. Budget: eigene CSS ≤ 15 KB, eigene JS ≤ 25 KB, Feld-SVGs ≤ 25 KB roh. Spiel (falls gebaut) inkl. Phaser ≤ 1,5 MB roh und erst nach Tippen auf „Ins Feld“ laden.
13. Preise, Produktnamen und Links immer aus Shopify (Theme-Einstellungen), nie als Text eintippen.
14. Nur echte Zahlen. Keine erfundenen Zähler, Bewertungen, Knappheit oder Daten zu einzelnen Nummern.
15. Lies diese Regeln vor jeder Änderung am Code noch einmal.

## Sprache und Bilder auf der Seite
- Keine Politik in der Marke. Subjekt ist das Muster, nicht das Volk.
- Nie „authentisch“. Den Lebensbaum nie „slawisch“ nennen. Nach außen „Time Travel“, nicht „Projekt Slavic“, nicht „eine Kultur“.
- Keine Landkarten, keine Flaggen, keine Flaggenfarben. NIE hellblauer Himmel über gelbem Weizen.
- Serp/Sichel: nie freigestellt als Icon, Logo oder Grafik, nie mit Stern, Hammer oder rotem Grund, nie neben Ähren als Emblem.
- Keine Hakenkreuz-, Kolovrat-, Schwarze-Sonne-, Valknut-Symbolik, auch nicht als Deko-Muster.
- Bis das Proto da ist (Do 03.12.2026): kein fertiges Teil und kein Mockup einer Jeans. Motive nur flach.
- Bedeutungen von Motiven nur mit Beleg aus docs/BELEGE.md.
- Prüfe jeden neuen Text gegen diese Liste und markiere mir Treffer.

## Termine (Europe/Berlin, Sommerzeit ab So 28.03.2027)
| Zustand | ab | ISO |
|---|---|---|
| WARTELISTE | jetzt | — |
| VORBESTELLUNG | Do 14.01.2027 19:00 | 2027-01-14T19:00:00+01:00 |
| ZWISCHENZEIT (Preisende) | So 21.03.2027 20:00 | 2027-03-21T20:00:00+01:00 |
| Feld öffentlich | Mo 29.03.2027 18:00 | 2027-03-29T18:00:00+02:00 |
| SCHLUESSEL (nur mit ?key=) | Do 22.04.2027 18:00 | 2027-04-22T18:00:00+02:00 |
| LIVE | Do 22.04.2027 19:00 | 2027-04-22T19:00:00+02:00 |
| AUSVERKAUFT | Drop-Jeans Bestand 0 | — |
Code-Freeze: Sa 17.04.2027. Danach keine Änderung bis 25.04.

## Theme-Einstellungen (Gruppe „Time Travel“)
tt_zeit_vorbestellung, tt_zeit_preisende, tt_zeit_feld_oeffentlich, tt_zeit_schluessel, tt_zeit_drop (text, ISO mit Offset) ·
tt_schluessel (text) · tt_testmodus (checkbox; ?t=<ISO> wirkt nur, wenn an) ·
tt_produkt_vorbestellung, tt_produkt_drop, tt_produkt_zipper, tt_produkt_polo (product) · tt_kollektion (collection) ·
tt_start_vorbestellung (35), tt_start_drop (58), tt_reserviert (7) (number) · tt_liste_zahl (number), tt_liste_datum (text)

## Palette (17 Farben)
T01 #2B1B3D Nachtviolett · T02 #5A1F3A Pflaume · T03 #A3312B Glutrot · T04 #E0662B Abendorange · T05 #F2A541 Horizontgold ·
T06 #FCE3A7 Sonnenkern · T07 #3A1C2C Hügel · T08 #6B3A1E Weizen Schatten · T09 #A8642A Weizen · T10 #E9B35F Weizen Lichtkante ·
T11 #7A1E2C Teppich Bordeaux · T12 #E8D6B3 Teppich Beige · T13 #1A1416 Teppich Schwarz · T14 #C9962E Teppich Gold ·
T15 #1F2A44 Denim Indigo (NUR für Jeans/Zipper) · T16 #F4EFE6 Garn Weiß · T17 #B3202A Garn Rot
Seite: Hintergrund T13, Text T12/T16, Akzente T17 und T05.
Flaggen-Regel: kein Pixel mit Farbton 180–250°, Sättigung > 25 %, Helligkeit > 45 % (tools/flaggen-check.mjs).

## Dateien
sections/tt-hero, tt-kapitel, tt-nummern, tt-feld-scroll (B), tt-feld (A) · snippets/tt-countdown, tt-warteliste-form, tt-shop-button ·
assets/tt-clock.js, tt-story.js, tt-story.css, tt-nummern.js, tt-feld-*.svg, tt-motiv-*.svg · nur A: phaser-3.90.0.min.js, tt-feld.js, Aseprite-PNG/JSON ·
docs/ (TERMINE, TEXTE-*, BELEGE, TESTPLAN, ASSETS) und tools/ werden per .shopifyignore nicht hochgeladen.

## Testen
- Vorschau: shopify theme dev --store DEIN-SHOP (Vorschau-Link am Handy öffnen)
- Prüfen: shopify theme check · node tools/budget-check.mjs · node tools/flaggen-check.mjs
- Zeit: ?t=2027-04-22T18:59:30+02:00 (nur mit tt_testmodus) · Schlüssel: &key=<tt_schluessel>
````

---

## Anhang B · Spickzettel Terminal

| Wofür | Befehl | Quelle |
|---|---|---|
| Themes anzeigen | `shopify theme list --store DEIN-SHOP` | [W7] |
| Theme kopieren | `shopify theme duplicate --theme <ID> --name "TT Story"` | [W7] |
| Theme holen | `shopify theme pull --theme "TT Story"` | [W7] |
| Vorschau mit Live-Änderungen | `shopify theme dev --store DEIN-SHOP` | [W7] |
| Prüfen | `shopify theme check` | [W7] |
| Hochladen (nur nach deinem Ja) | `shopify theme push --theme "TT Story"` | [W7] |
| Veröffentlichen (nur du) | `shopify theme publish --theme "TT Story"` | [W7] |
| PLAN B in unter einer Minute | `shopify theme publish --theme "PLAN B" --force` | [W7] |
| Teilbare Vorschau für Tester | `shopify theme share` | [W7] |
| Stand sichern | `git add -A && git commit -m "Was jetzt geht"` | — |
| Claude Code starten | `cd ~/Claude/Novalife/website/tt-theme && claude` | [W23] |
