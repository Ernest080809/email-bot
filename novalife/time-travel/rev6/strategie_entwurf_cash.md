# Strategie-Entwurf · Cash und Risiko zuerst

Stand: Mi 07.10.2026, abends. Für Ernest. Teil der Docket-Neuplanung (Rev. 6).
Blickwinkel: **Die Finanzierungslücke sicher schließen, die Schwellen 10 und 32 treffen, nie Geld ausgeben, das noch nicht verdient ist.** Dazu Frühwarnsignale, Gates, Notfallhebel, Fabrik- und Terminrisiken.
Grundlage: Plan Rev. 5.3, Spec Rev. 13, Übergabe vom 07.10., Docket Rev. 5.3 (`r5/weeks_r5.json`), die neun Recherche-Dateien in `rev6/research/`.

---

## 0 · Quellenlage, ehrlich

- **Ich konnte heute nichts selbst im Netz prüfen.** Das Suchbudget dieser Runde war aufgebraucht (Meldung beim ersten Versuch). Der Seitenabruf war gesperrt. Getestet: `help.shopify.com` (Vorbestellungen, Auszahlung) und `gesetze-im-internet.de` (§ 19 UStG). Beide blockiert.
- **Was belegt ist,** stammt aus Quellen, die die Recherche-Agenten heute in dieser Sitzung per Websuche gesehen haben, meist als Suchauszug. Ich zitiere sie mit ihrer Nummer aus `markt.md` [Q..] und mit URL in Abschnitt 8.
- **Kennzeichen in diesem Text:**
  - **[Plan x]**, **[Spec x]**, **[Docket Wx]**: interne Projektdateien.
  - **[markt Qx]**, **[zielgruppe]**, **[tools]**, **[community]**, **[design]**, **[lieferanten]**: aus den Recherche-Dateien. [markt Qx] heißt: URL in Abschnitt 8.
  - **[R]**: meine Rechnung. Der Weg steht dabei. Das Skript liegt im Scratchpad dieser Sitzung.
  - **Schätzung**: Annahme, nicht belegt.
  - **W**: mein Wissensstand bis Mitte 2026, heute nicht prüfbar. **Vor dem Handeln prüfen.**
- Kalenderdaten (Wochentage, Ostern 2027, Beginn der Sommerzeit) habe ich lokal berechnet: Ostersonntag 28.03.2027, Karfreitag 26.03., Ostermontag 29.03., Sommerzeit ab So 28.03.2027 [R].
- **Kein Steuer- und kein Rechtsrat.** Wo es um Steuer oder Recht geht, steht dabei, wer es klärt.

---

## 1 · Kernthese

**Die 10.000 € entscheiden sich nicht am Drop-Tag, sondern zwischen dem 03.02. und dem 30.03. Bis dahin müssen 32 bezahlte Vorbestellungen auf dem Konto sein. Mit der wahrscheinlichen Einfuhr- oder Erwerbsteuer (~1.150 €, nicht im Budget) sind es 40, also mehr, als das Kontingent von 35 hergibt.**
**Deshalb machst du zuerst die Kosten wahr (Steuer bis 23.10., Fabrikpreis und Stichzahl gedeckelt bis 10.11.) und holst dann das Geld vor die Zahlungen: 25 namentliche Zusagen bis 10.01., eine zweite Vorbestellstufe zum vollen Preis und Zahlungsbedingungen mit Notausgang.**
**Bis zur Bestellung am 03.02. ist jeder Ausstieg billig und kein Cent Kundengeld ausgegeben. Danach gibt es nur noch Durchziehen. Die Bestellung wird deshalb nur unterschrieben, wenn die Hochrechnung die Restzahlung trägt, sonst 75 Stück.**

### 1.1 Was realistisch ist

| Frage | Ehrliche Antwort | Grundlage |
|---|---|---|
| Hält der Plan Rev. 5.3 im mittleren Fall? | Ja. ~21 Vorbestellungen bis 31.01., Drop ~74 brutto | [markt 3.4] |
| Hält er im vorsichtigen Fall? | Nur bis Break-even. ~9 Vorbestellungen bis 31.01. (Schwelle 10 knapp verfehlt), ~58–61 Paar netto | [markt 3.4] |
| Hält die Kasse, wenn die Fabrik in der Türkei sitzt und du Kleinunternehmer bleibst? | **Nein, nicht ohne Änderung.** ~1.150 € Einfuhrumsatzsteuer fehlen im Budget. Bedarf steigt auf ~40 Vorbestellungen bis Ende März, das Kontingent ist 35 | [Plan 3.1, Risiko 2] + [R] |
| Und Portugal? | Wahrscheinlich ähnlich teuer: 19 % Erwerbsteuer oder portugiesische MwSt., beides ohne Vorsteuerabzug | [tools 3.3], **W**, Steuerberater |
| Wie sicher ist die Kostenbasis? | **Gar nicht.** 63 € Stückkosten und ~60 € Fabrikpreis sind Schätzungen. Es gibt noch kein einziges Angebot. Die echte Stichzahl kommt am 09.11. | [Plan 3], [Spec 3.11] |
| Steigt der Break-even mit der Steuer? | Ja, von 60 auf ~67 Paar. Dann liegt das Ziel (64 Paar) **unter** dem Break-even | [R]: 1.150 € / 169 € = 6,8 Paar |

### 1.2 Der größte Engpass

**Bezahltes Vertrauen vor dem 17.03.** Nicht Reichweite, nicht die Fabrik, nicht das Design. Eine Vorbestellung zu 149 € im Januar für eine Hose im April kauft man von jemandem, dem man vertraut [zielgruppe 4]. Wie groß dein warmes Netz ist, weiß noch niemand. Das ist die erste Zahl, die du brauchst (Di 13.10.).

Zweiter Engpass: **deine Zeit.** 1–2 Stunden am Tag reichen für den Plan, aber nicht für den Plan plus Spiel plus fünf Abende [Plan 12, Risiko 6]. Jede Stunde, die nicht Geld vor die Zahlungstermine holt, ist aus diesem Blickwinkel zweitrangig.

---

## 2 · Funnel- und Cash-Mathematik

### 2.1 Zwei Ziele, getrennt gezählt

| Ziel | Wofür | Zahl | Quelle |
|---|---|---|---|
| **Finanzierung** | Anzahlung 04.02., Restzahlung 19.03. | ≥ 10 Vorbestellungen bis 01.02., ≥ 32 bis 19.03. (ohne Steuer) | [Plan 3.1] |
| **Umsatz** | 10.000 € | 64 Paar netto = 35 × 149 € + 29 × 169 € = 10.116 € | [Plan 3.2] |
| Umsatz brutto mit Retouren | 64 netto | 71–80 Bestellungen bei 10–20 % Retoure. Plan-Ziel brutto **72** (35 + 37) | [markt 3.1], Retouren DE 11 %, 16–29 Jahre 15 % [markt Q44] |
| Polster | Umsatz, keine Finanzierung | Zipper 139 €, Polo 79 €, auf Bestellung ab 22.04. | [Plan 3.2] |

**Regel:** Zipper und Polo zählen nie für die Schwellen. Sie kommen erst nach dem 22.04. rein [Plan 3.2].

### 2.2 Kapitalbedarf: was im Plan steht und was fehlt

| Posten | Betrag | Status | Quelle |
|---|---|---|---|
| Kapitalbedarf laut Plan | **9.380 €** | Schätzung, ohne Angebot | [Plan 3] |
| Einfuhrumsatzsteuer Türkei bei Kleinunternehmer | **~1.150 €** | im Plan als Risiko, nicht im Budget | [Plan 3.1, Risiko 2] |
| Portugal: Erwerbsteuer 19 % oder PT-MwSt. | ~1.140–1.380 € | **W**, Steuerberater | [tools 3.3] |
| Reverse Charge (§ 13b) auf Digitizing, Shopify, Meta | 0–~200 € | **W**, Steuerberater | [tools 3.3] + Schätzung |
| Puffer 100 € ist mehrfach verplant | ~290 € überbucht | Rechnung | Aseprite ~20 € [tools], Rechtstexte ~80 € [tools 3.1], Werbetest 100 € [Docket W19], Kaffee ~40 € [zielgruppe 5], Abende < 150 € [community 9] |
| Steuerberater, LUCID/Verpackungslizenz, Shopify-Email über Freikontingent | offen | **vor Ort prüfen** | [tools 3.2, 3.3, 1] |
| **Planungswert bis zu den Angeboten** | **~10.500–11.000 €** | Schätzung | [R] |

**Was das heißt:** Die Lücke ist nicht 4.880 €, sondern eher 6.000–6.500 €. Bis der Steuerberater schriftlich etwas anderes sagt, planst du mit dem höheren Wert.

### 2.3 Wie empfindlich die Schwellen sind

Rechenweg [R] nach [design 0]: Schwelle 1 = (1.400 € + Δ zum 01.02.) ÷ 146 €. Schwelle 2 = (4.650 € + Δ zum 19.03.) ÷ 146 €. 146 € = netto je Vorbestellung nach Shopify-Gebühr [Plan 3.1].

| Fall | Schwelle 1 (01.02.) | Schwelle 2 (19.03.) |
|---|---|---|
| Basis Plan Rev. 5.3 | 10 | 32 |
| Fabrikpreis +1 € je Paar | 10 | 33 |
| Fabrikpreis +2 € | 11 | 34 |
| Fabrikpreis +5 € | 12 | 36 |
| Zahlung 60/40 statt 50/50 | **14** | 32 |
| Echter Kreuzstich +5.000 Stiche | 11 | 34 |
| Echter Kreuzstich +10.000 Stiche | 12 | **36** (über Kontingent) |
| **Einfuhrumsatzsteuer 1.150 €** (fällig bei Einfuhr, ~30.03.) | 10 | **40** |
| Steuer + Fabrikpreis +2 € + Puffer-Überbuchung | 11 | **44** |
| Chenille-Muster gestrichen (−120 €) | 9 | 32 |
| Zipper/Polo-Entwicklung erst nach 01.02. (420 €) | **7** | 32 |
| Münztasche offen, V4b (−345 €) | 9 | 30 |
| Serp klein wie v1.6 (−150 €) | 10 | 31 |
| 75 statt 100 Stück, gleicher Stückpreis (Schätzung) | ~5 | **~22** |

**Faustregel:** Jeder Euro mehr Fabrikpreis kostet dich 0,7 Vorbestellungen bei Schwelle 2. 146 € Mehrkosten sind eine Vorbestellung [R].

### 2.4 Wann Geld fließt und woher es kommen muss

Der Wochenplan in 2.6 legt die Plan-Posten auf die Docket-Wochen. Ergebnis [R]:

- **Bis So 31.01. zahlst du alles aus deinen 4.500 €.** Danach sind 1.990 € übrig [Plan 3.1]. Kein Cent Kundengeld ist bis dahin ausgegeben.
- **Do 04.02., Anzahlung 3.000 €:** Es fehlen 1.010 € = 7 Vorbestellungen, die ausgezahlt auf dem Konto sind. Mit Shoot und Verpackung im Februar sind es 10. Deshalb bleibt die Schwelle bei 10.
- **Fr 19.03., Restzahlung 3.000 €:** 31–32 Vorbestellungen nötig.
- **~30.03., Einfuhr:** Mit Steuer 40.
- **Widerruf (W):** Verbraucher können eine Vorbestellung bis 14 Tage nach Erhalt widerrufen [tools 3.1]. Die Vorbesteller bekommen ihre Hose ~08.04. Ihr Geld ist also erst um den 22.04. wirklich verdient. **Bis dahin ist jede Vorbestellung geliehenes Vertrauen.** Daraus folgt die Regel in 4.1.

### 2.5 Woher die Vorbestellungen kommen

| Quelle | Rechnung | Vorbestellungen bis 19.03. | Annahme und Quelle |
|---|---|---|---|
| **Namentliche Zusagen** aus deinem Netz | 25 Zusagen × 50 % | ~12 | Umwandlung 50 %: **Schätzung**, ab 14.01. messen. Vergleich: VIP-Listen mit Reservierung kaufen zu 20–40 % [markt Q27]. „Aus 50 Namen kaufen 10–15“ ist ebenfalls Schätzung [zielgruppe 4] |
| Mess-Abende 16.01., 23.01., 13.03. | 3 Abende × 3–5 | 9–15 | Schätzung. Pop-ups in Mode 25–40 % Conversion, Güte C [markt Q54]. 67 % der Retouren wegen Größe [markt Q44] |
| Warteliste in der Öffnungswelle | ~850–1.000 × 1,0–3,5 % | 9–35 | [markt 3.2]: a1 = 1,0 / 2,0 / 3,5 %. Gratis-Listen kaufen zu 2–5 %, kalte zu 1–3 % [markt Q23] |
| Warteliste in der Schlusswelle 08.–21.03. | U-Form: Anfang und Ende tragen | in Zeile darüber enthalten | [markt Q31] |
| Creator, Presse | nicht planbar | 0–5 | [community 1.1]: Presse nicht im Soll |
| **Summe** | | **~30–60** | breite Spanne, darum die Gates |

**Lesart:** Die Zusagen sind der einzige Teil, den du steuern kannst und der vor dem 01.02. sicher kommt. Die Liste bringt im vorsichtigen Fall zu wenig für Schwelle 1 [markt 3.4]. **Deshalb ist die Zusagen-Liste Hebel 6 und das Gate am 20.12. hart.**

### 2.6 Drop-Mathematik

| Größe | Wert | Quelle |
|---|---|---|
| Drop-Ziel netto / brutto | 29 / **37** | [markt 3.1] |
| Liste am 22.04. ohne Vorbesteller für 37 brutto | vorsichtig 3.365 · mittel 1.515 · gut 830 | [markt 3.3] |
| Käufe in den ersten 48 h | ~90 % der Listenkäufer (Kickstarter) | [markt Q27] |
| E-Mail-Newsletter normal | 0,12 % Bestellungen je Empfänger | [markt Q32] |
| Werbung | ~4–12 € je Anmeldung, 300 € bringen 25–75 Anmeldungen | [markt 2.5], Schätzung aus [Q36][Q42][Q43] |

**Folge für die Kasse:** Werbung ist kein Hebel für die Schwellen. Sie läuft erst ab 29.03. und nur, wenn die Restzahlung gedeckt ist.

### 2.7 Wochenwerte W5–W32

**So liest du die Tabelle:**
- **Eigenbudget übrig** = 4.500 € minus Plan-Ausgaben bis Sonntag [Plan 3], Zuordnung zu Docket-Wochen [R].
- **Posts/Wo** aus Plan 10. **Liste** und **Follower** aus [markt 3.7]. Follower = 3 je Anmeldung, **Schätzung**, ab 01.11. durch deine echte Quote ersetzen.
- **Zusagen Soll** = namentliche Personen im Blatt „Netz“ mit Größe und dem Satz „Ich bestelle am 14.01.“ **Schätzung**, abgeleitet aus Schwelle 1.
- **Vorbest. bezahlt** = Vorbestellungen, deren Geld ausgezahlt auf dem Konto ist. Soll / Alarm. Verlauf als U-Form [markt Q31].
- **Nötig aus Vorbest.** = Mindestzahl, damit alle fälligen Zahlungen bis zu diesem Sonntag gedeckt sind, ohne / mit Steuer (1.150 € ab Einfuhr) [R].

| W | Sonntag | Was fällig wird (Plan 3) | Eigenbudget übrig | Posts/Wo | Liste Soll / Alarm | Follower Soll | Zusagen Soll | Vorbest. bezahlt Soll / Alarm | Nötig aus Vorbest. (ohne / mit Steuer) |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 18.10. | — | 4.480 € | 3 | 40 / 15 | 120 | Netz gezählt | — | 0 |
| 6 | 25.10. | 2 Blanks | 4.440 € | 3 | 90 / 30 | 270 | 5 | — | 0 |
| 7 | 01.11. | — | 4.440 € | 3 | 150 / 50 | 450 | 10 (Ja/Vielleicht) | — | 0 |
| 8 | 08.11. | Entwicklung 650 · Schnitt 300 | 3.490 € | 3 | 210 / 80 | 630 | 10 | — | 0 |
| 9 | 15.11. | Stoff 90 · Digit. Z/P 240 · Patch-Muster 80 | 3.080 € | 3 | 270 / 110 | 810 | 11 | — | 0 |
| 10 | 22.11. | — | 3.080 € | 3 | 330 / 140 | 990 | 12 | — | 0 |
| 11 | 29.11. | — | 3.080 € | 3 | 390 / 170 | 1.170 | 13 | — | 0 |
| 12 | 06.12. | — | 3.080 € | 5 | 470 / 200 | 1.410 | 15 | — | 0 |
| 13 | 13.12. | PP 220 | 2.860 € | 5 | 550 / 230 | 1.650 | 18 | — | 0 |
| 14 | 20.12. | Patch D 330 · Setup 150 · Berlin-Muster 140 | 2.240 € | 5 | 620 / 260 | 1.860 | 20 | — | 0 |
| 15 | 27.12. | — | 2.240 € | 3 | 680 / 280 | 2.040 | 20 | — | 0 |
| 16 | 03.01. | — | 2.240 € | 3 | 740 / 300 | 2.220 | 22 | — | 0 |
| 17 | 10.01. | Chenille 120 (opt.) · Shopify bis Apr. 130 | 1.990 € | 5 | 850 / 380 | 2.550 | **25** | — | 0 |
| 18 | 17.01. | — | 1.990 € | 5 | 1.000 / 450 | 3.000 | — | 10 / 6 | 0 |
| 19 | 24.01. | — | 1.990 € | 5 | 1.250 / 520 | 3.750 | — | 13 / 8 | 0 |
| 20 | 31.01. | — | 1.990 € | 5 | 1.500 / 600 | 4.500 | — | **16 / 10** | 0 |
| 21 | 07.02. | **Anzahlung 3.000** | 0 € | 5 | 1.700 / 660 | 5.100 | — | 18 / 12 | 7 / 7 |
| 22 | 14.02. | — | 0 € | 4 | 1.900 / 720 | 5.700 | — | 20 / 14 | 7 / 7 |
| 23 | 21.02. | Shoot 150 | 0 € | 4 | 2.150 / 790 | 6.450 | — | 22 / 16 | 8 / 8 |
| 24 | 28.02. | Verpackung 240 | 0 € | 4 | 2.400 / 850 | 7.200 | — | 24 / 18 | 10 / 10 |
| 25 | 07.03. | Versandmaterial 80 | 0 € | 4 | 2.450 / 880 | 7.350 | — | 26 / 21 | 11 / 11 |
| 26 | 14.03. | — | 0 € | 4 | 2.500 / 910 | 7.500 | — | 29 / 25 | 11 / 11 |
| 27 | 21.03. | **Restzahlung 3.000** | 0 € | 4 | 2.560 / 950 | 7.680 | — | **35 / 32** | 31 / 31 |
| 28 | 28.03. | — | 0 € | 4 | 2.620 / 1.050 | 7.860 | — | 37 / 35 | 31 / 31 |
| 29 | 04.04. | Werbung K1 150 · *EUSt ~1.150* | 0 € | 7 | 2.720 / 1.170 | 8.160 | — | **43 / 40** (mit Steuer) | 32 / 40 |
| 30 | 11.04. | — | 0 € | 7 | 2.820 / 1.290 | 8.460 | — | — | 32 / 40 |
| 31 | 18.04. | — | 0 € | 7 | 2.920 / 1.400 | 8.760 | — | — | 32 / 40 |
| 32 | 25.04. | Werbung K2 150 · Puffer 100 | 0 € | 5 | 3.000 / 1.515 | 9.000 | — | Drop: 37 brutto | 34 / 42 |

**Wichtig:** Die Zahlen 37 und 43 in W28 und W29 gibt es nur mit der zweiten Vorbestellstufe (Hebel 5). Ohne sie endet die Vorbestellung bei 35.

---

## 3 · Die 10 wichtigsten Hebel

Sortiert nach Wirkung pro Stunde deiner Zeit. Wirkung in Vorbestellungen oder Euro [R]. Alle sind Vorschläge. **Du entscheidest.**

| # | Hebel | Wirkung | Aufwand | Wichtigste Termine |
|---|---|---|---|---|
| 1 | Steuer- und Kostenwahrheit | ±8 Vorbestellungen (1.150 €) | 1,5 h | Do 08.10. buchen · Di 13.10. Gespräch · spätestens Fr 23.10. |
| 2 | Auszahlung prüfen, bevor du sie brauchst | kritisch: ohne Auszahlung zählt keine Vorbestellung | 45 Min. | Fr 30.10. · Di 29.12. |
| 3 | Kostendeckel im Tech Pack und Fabrikpreis-Ampel | verhindert +2 bis +4 bei Schwelle 2 | 15 Min. | Fr 09.10. · So 11.10. · Mo 12.10. · Mo 19.10. · Di 10.11. |
| 4 | Konditionen mit Notausgang verhandeln | Schwelle 1: 10 statt 14 · 5 Tage Puffer im März | 30 Min. | Di 27.10. · Mi 06.01. · Mi 03.02. |
| 5 | Zweite Vorbestellstufe zum vollen Preis | +5 bis +8 Vorbestellungen ohne Rabatt | 20 Min. | Mo 14.12. · Sa 19.12. · aktiv ab Ausverkauf der 35 |
| 6 | Zusagen-Liste „Die ersten 35“ | sichert Schwelle 1 am ersten Abend | 10–20 Min. an 3–4 Tagen pro Woche | Di 13.10. · Sa 24.10. · Do 03.12. · So 20.12. · So 10.01. |
| 7 | Geld nur in Stufen freigeben | Schwelle 1 bis −3, Ausstieg bleibt billig | gering | jedes Gate |
| 8 | Mess-Abende vor die Zahlungstermine legen | 9–15 Vorbestellungen (Schätzung) | 3 h je Abend | Sa 16.01. · Sa 23.01. · **Sa 13.03.** |
| 9 | Mengenregel 100 oder 75 per Formel | verhindert die Restzahlungs-Falle | 20 Min. | Mo 12.10. · Do 28.01. · Mo 01.02. |
| 10 | Notfall-Brücke vorher klären | Versicherung für den teuersten Fall | 1 Gespräch | bis Do 31.12. |

### Hebel 1 · Steuer- und Kostenwahrheit

**Warum zuerst:** Der größte einzelne Posten, der nicht im Budget steht, ist Steuer. Er ist größer als jede Design-Frage [Plan Risiko 2], [tools 3.3].

**Was du tust:**
- **Do 08.10.:** Steuerberater-Termin buchen. Gewerbeschein raussuchen: Deckt er Produktion und Online-Handel? [tools 3.3]
- **Di 13.10.:** Gespräch mit den 8 Fragen aus [tools 3.3]. Dazu eine neunte aus diesem Blickwinkel: *„Wann genau ist die Steuer fällig, bei DDP und bei DAP, und kann ein Spediteur sie mit Zahlungsziel vorstrecken?“*
- **Kein Termin bis 13.10.:** IHK-Gründungsberatung, spätestens **Fr 23.10.** Das ist vor der Fabrikwahl am Mo 26.10. [tools 3.3]
- **Ergebnis an Claude.** Claude rechnet Kapitalbedarf, Schwellen und Kontingent neu.

**Regel bis zur schriftlichen Antwort:** Du planst mit 1.150 € Steuer, egal ob Türkei oder Portugal.

**Zur Regelbesteuerung (W, Steuerberater):** Dann bekommst du die Einfuhrumsatzsteuer zurück. Aber die Umsatzsteuer auf die Vorbestellungen wird wahrscheinlich schon fällig, wenn das Geld eingeht. Das sind bei 35 Paar ~830 € im Februar und März [R: 35 × 149 € × 19/119]. Für die Kasse ist das schlechter. [tools 3.3] schätzt auch insgesamt: Kleinunternehmer bleibt günstiger.

### Hebel 2 · Auszahlung prüfen, bevor du sie brauchst

**Warum:** Der ganze Plan setzt voraus, dass das Geld einer Vorbestellung wenige Tage später auf deinem Konto ist. Ob Shopify Payments oder PayPal bei Vorbestellungen eine Reserve zurückhalten oder erst nach Versand auszahlen, ist **ungeprüft** [tools 1]. Hält einer der beiden Geld bis April zurück, fehlt es am 04.02.

**Was du tust:**
- **Fr 30.10.** (neu, statt erst Mi 25.11.): Shopify Payments aktivieren, Ausweis und Bankkonto prüfen lassen. Die Prüfung kann dauern (W) [tools 1].
- Gleicher Tag, Frage an den Shopify-Support, schriftlich: *„Ich verkaufe ab 14.01.2027 Vorbestellungen mit Lieferung im April. Haltet ihr dafür eine Reserve zurück? Wann wird ausgezahlt?“* Antwort als Screenshot ins Blatt „Kasse“.
- Den Auszahlungsplan im Admin nachsehen (Einstellungen → Zahlungen) und die Zahl der Werktage notieren.
- **Di 29.12.** (Testbestellung, Docket W16): mit echter Karte kaufen und die Auszahlung bis aufs Bankkonto verfolgen. Tage zählen. Danach erstatten.
- PayPal: dieselbe Frage. Bei neuen Händlern hält PayPal manchmal Geld zurück (W).

**Gate:** Bis So 20.12. ist klar, nach wie vielen Werktagen Geld auf dem Konto ist. Ab dann gilt: **Für eine Zahlung zählt nur Geld, das drei Werktage vorher auf dem Konto ist.**

### Hebel 3 · Kostendeckel im Tech Pack und Fabrikpreis-Ampel

**Warum:** Der teuerste Kostenfall ist nicht der Serp, sondern echter Kreuzstich an A und E: +5.000 bis +10.000 Stiche, Schwelle 2 steigt auf 34–36 [design 2.5], [Spec 3.11].

**Was du tust:**
- **Fr 09.10., Freeze, und So 11.10., Tech Pack:** Den Satz aus [design V4a] ins Tech Pack. Feine Füllung ist Standard. Echter Kreuzstich nur, wenn er am gewaschenen Stitch-out deutlich näher an deinen Referenzfotos ist **und** höchstens 2 € je Paar mehr kostet. Deckel 33.000 Stiche, jede Überschreitung braucht dein Ja.
- **Mo 12.10., RFQ:** zusätzlich fragen: Preis bei **75 und 100** Stück, Preis je 1.000 Stiche, Fadenschnitte und Farbwechsel pro Element, Zahlungsbedingungen, Preis DDP und DAP Berlin, **Preis in Euro**, Betriebsferien Oktober bis April.
- **Mo 19.10., Vergleich:** Jedes Angebot bekommt eine Ampel. Fabrikpreis je Paar inklusive Stickerei, ohne Patch D:

| Fabrikpreis | Ampel | Schwelle 2 | Was dann |
|---|---|---|---|
| ≤ 60 € | grün | 32 | Plan läuft |
| 61–63 € | gelb | 33–34 | Puffer schrumpft auf 1–2 Paar. Hebel 5 wird Pflicht |
| > 63 € | rot | ≥ 35 | Gegenrechnung an dich. Optionen: V4b, Serp klein [design 3.7], 75 Stück, andere Fabrik |

- **Di 10.11., Digitizing-Freigabe:** nur bei ≤ 33.000 Stichen ohne Rückfrage. Darüber mit Gegenrechnung (Prompt in 5.3).

**Warum in Euro:** Ein Angebot in USD oder TRY schwankt. ±5 % auf 6.000 € sind ±300 € oder ±2 Vorbestellungen [R, Schätzung].

### Hebel 4 · Konditionen mit Notausgang verhandeln

**Warum:** Am 27.10. hast du Verhandlungsmacht, im März nicht mehr. 60/40 statt 50/50 hebt Schwelle 1 von 10 auf 14 [R]. Istanbul Clothing Manufacturers nennt laut Plan 60/40 [Plan 7], nicht geprüft.

**Was du verhandelst (Di 27.10., Vorlage „Verhandlung“ erweitern):**
1. **50/50.** Kein Vertrag mit 60/40, solange du unter 14 Vorbestellungen planen musst.
2. **Restzahlung „nach Freigabe des Endkontroll-Videos, spätestens Mi 24.03.2027“.** Geplant bleibt Fr 19.03. Die fünf Tage sind dein Puffer, falls die letzte Vorbestellwelle erst nach dem 19.03. ausgezahlt wird (siehe 4.4).
3. **Teil-Lieferung gegen Teilzahlung** als Option: Fehlen dir am 24.03. Mittel, zahlst du für X Paar und bekommst X Paar. Der Rest kommt nach dem Drop.
4. **Preis bei 75 und 100 schriftlich**, gültig bis 01.02.
5. **Entwicklungskosten werden mit der Bestellung verrechnet** (steht schon im Plan).
6. **Keine Bestellpflicht,** wenn Stickproben (17.11.), Proto (05.12.) oder PP (05.01.) die schriftlichen Kriterien nicht erfüllen.
7. **Preis in Euro, DDP oder DAP Berlin** je nach Steuer-Ergebnis.
8. **Bankdaten-Regel:** Gezahlt wird nur auf das Konto aus der ersten Proforma. Kommt per E-Mail ein neues Konto: nicht zahlen, die Fabrik anrufen. Geänderte Bankdaten sind ein bekanntes Betrugsmuster (W).

**Wieder aufgreifen:** Mi 06.01. (Bestellkonditionen, Docket W17) und Mi 03.02. (PO, Docket W21). Punkte 2, 3 und 8 stehen in der PO.

### Hebel 5 · Zweite Vorbestellstufe zum vollen Preis

**Warum:** Mit Steuer brauchst du ~40 Vorbestellungen bis Ende März, das Kontingent ist 35 [R]. Der Plan sieht Kontingent 45 zu 149 € vor, aber nur bei mehr als 25 bis 01.02. [Plan 3.1]. 45 zu 149 € plus 19 im Drop ergeben nur 9.916 € [R]. Das Ziel wäre knapp verfehlt.

**Vorschlag (Abweichung vom Plan, du entscheidest):**
- **Stufe 1:** Nr. 001–035 zu 149 €, wie geplant. „Noch X von 35“ bleibt wahr.
- **Stufe 2:** Sobald die 35 weg sind, Nr. 036–060 als **Vorbestellung zum Drop-Preis 169 €**, Lieferung Anfang April. Der Vorteil für den Käufer: kleine Nummer, sichere Größe, Lieferung drei Wochen vor dem Drop.
- **Schluss Stufe 2: So 04.04., 20:00,** damit diese Paare mit dem Versand am 06.–07.04. rausgehen. Was danach übrig ist, geht in den Drop.
- **Umsatz:** 35 × 149 € + 29 × 169 € = 10.116 € für 64 Paar, egal ob die 29 vor oder im Drop kommen [R]. Kein Rabatt, nur früheres Geld.
- **Ersetzt die Regel „Kontingent 45“** aus [Plan 3.1].

**Termine:** Mo 14.12. als zweites Produkt im Entwurf anlegen (Docket W14). Sa 19.12. entscheiden (Docket W14, Kontingent). Rechtstext wie bei Stufe 1, Lieferdatum fest [tools 3.1].

### Hebel 6 · Zusagen-Liste „Die ersten 35“

**Warum:** Schwelle 1 hängt an deinem Netz und deinen Bestandskunden [zielgruppe 4]. Eine Zusage mit Namen und Größe ist mehr wert als eine Anmeldung. Sie kostet nichts, keine App, kein Rechtstext.

**Was du tust:**
- **Di 13.10.:** Blatt „Netz“: alle Kontakte zählen, die dir schon vertrauen. Freunde, Familie, Bleach-Kunden [community 6.6]. **Diese Zahl ist die wichtigste Unbekannte im ganzen Plan.**
- **Fr 16.10. und Do 29.10.:** Netz-Runden 1 und 2 [community 6.6], persönlich, mit eigenem Link.
- **Sa 24.10., Papiertest-Abend** [community 6.1]: Wer „Ja“ sagt, kommt mit Größe ins Blatt.
- **Bis So 01.11.:** 10 Personen mit „Ja“ oder „Vielleicht zu 149 €“ (Frage 9 aus [zielgruppe 5.1]).
- **Do 03.12.–So 13.12., Proto-Runde:** Das Proto ist in deiner Hand, du darfst es zeigen [Plan 0]. 20 Leute persönlich treffen oder per Video. Frage: *„Bestellst du am 14.01. um 18:00?“* Größe messen.
- **So 20.12.:** ≥ 15 „Ja“ mit Größe (Gate).
- **So 10.01.:** ≥ 25 „Ja“ (Gate).
- **Mi 13.01.:** persönliche Nachricht an jede Person. **Do 14.01., 18:00:** Link.

**Alternative aus [markt Hebel 1]:** Nummern-Reservierung mit 10 € Anzahlung ab 07.12. Aus Cash-Sicht ist die Zusagen-Liste gleichwertig und billiger. Die Anzahlung finanziert nichts [tools 1] und braucht App und Rechtscheck. Nur nehmen, wenn die Zusagen am 20.12. unter 10 liegen. Dann bleiben aber nur drei Wochen zum Bauen.

### Hebel 7 · Geld nur in Stufen freigeben

**Regel:** Jeder Posten aus Plan 3 wird erst bezahlt, wenn das Gate davor bestanden ist (4.2). So bleibt jeder Ausstieg bis zum 03.02. billig (4.5).

**Ausgaben-Stopp-Liste** (greift bei Rot an einem Gate):
1. Chenille-Muster 120 € streichen. Der Plan empfiehlt ohnehin gestickt [Plan 4.2]. Schwelle 1 sinkt auf 9.
2. Zipper/Polo-Entwicklung (Digitizing 240 €, Rest Berlin-Muster) erst ab Mo 01.02. Schwelle 1 sinkt auf 7. **Nachteil:** Zipper und Polo im Shoot am 20.02. werden knapp. Nur bei Rot am 20.12.
3. Werbetest 100 € (Docket W19) streichen. Siehe 5.3.
4. Kampagne 1 (150 €) läuft nur, wenn Restzahlung und Steuer gedeckt sind.

**Puffer neu ordnen:** Der Puffer von 100 € ist ~290 € überbucht (2.2). Abende laufen mit Unkostenbeitrag oder gar nicht. Kein Posten wird aus Kundengeld bezahlt, bevor die PO steht.

### Hebel 8 · Mess-Abende vor die Zahlungstermine legen

**Warum:** Ein Abend mit Sample und Maßband bringt Vorbestellungen mit niedriger Retourenquote. 67 % der Retouren liegen an der Größe [markt Q44]. Aber: **Mess-Abend 3 am Sa 20.03. liegt nach der Restzahlung am 19.03.** [community 6.3]. Sein Geld kommt zu spät.

**Was du tust:**
- **Sa 16.01. und Sa 23.01.** bleiben. Beide liegen vor Schwelle 1.
- **Mess-Abend 3 auf Sa 13.03.** vorziehen. Dann ist das Geld bis ~Mi 17.03. ausgezahlt (Hebel 2).
- QR-Code mit `ref-mess` [community 1.2]. Vorbestellen am eigenen Handy, vor Ort.

### Hebel 9 · Mengenregel 100 oder 75 per Formel

**Warum:** Mit der PO am 03.02. verpflichtest du dich zu 6.000 €. Hast du dann nur 10 Vorbestellungen, hoffst du auf 22 weitere bis 19.03. Das ist die teuerste Wette im Plan. Bei 75 Stück liegt Schwelle 2 bei ~22 (Schätzung, gleicher Stückpreis). 75 minus 5 Creator minus 2 Reserve = 68 verkäufliche Paare. **64 sind damit immer noch erreichbar.** Für den Ausverkauf (15.017 €) fehlt dann die Menge [Plan 3.2].

**Die Formel (Do 28.01. rechnen, Mo 01.02. entscheiden):**
`Hochrechnung 19.03. = Vorbestellungen bezahlt am 31.01. + 6 × Wochenrate aus W19–W20`

| Hochrechnung | Entscheidung |
|---|---|
| ≥ 32 (ohne Steuer) bzw. ≥ 40 (mit Steuer) | 100 Stück |
| darunter, Schwelle 1 erfüllt | **75 Stück**, Preis aus dem RFQ |
| Schwelle 1 nicht erfüllt | 2 Wochen schieben [Plan 6] |

**Voraussetzung:** Der Preis bei 75 steht im Angebot (RFQ Mo 12.10.). White Cotton nennt laut Plan MOQ ab 50 [Plan 7], nicht geprüft [lieferanten 1.2].

### Hebel 10 · Notfall-Brücke vorher klären

**Warum:** Der teuerste Fall: Die Ware ist fertig, die Restzahlung fehlt, die Fabrik hält die Ware, 35 Vorbesteller warten. Dann musst du in Tagen Geld finden.

**Vorschlag (du entscheidest, es ist ein Kredit):** Bis Do 31.12. fragst du eine Person aus deiner Familie nach einer schriftlichen Stand-by-Zusage über 1.500 €. Gezogen wird sie nur bei Rot am 14.03. oder 19.03., und nur für Restzahlung, Steuer oder Erstattungen. Nie für Werbung oder Design. 1.500 € decken die Steuer oder ~10 fehlende Vorbestellungen [R].

**Aus deinem Blickwinkel ehrlich:** Auch das ist Geld, das noch nicht verdient ist. Es ist die Versicherung, nicht der Plan.

---

## 4 · KPI-Gates mit vordefinierten Gegenmaßnahmen

### 4.1 Sonntags-Kassencheck (10 Minuten, im Wochenreview)

Neues Blatt „Kasse“ (Claude baut die Vorlage). Jeden Sonntag vier Zahlen:

| Zahl | Woher |
|---|---|
| **K** Projektkonto heute | Bank |
| **V** Vorbestellungen bezahlt und ausgezahlt | Shopify → Bestellungen, Auszahlungen |
| **F** fällig bis zum nächsten harten Gate | Wochentabelle 2.7 |
| **R** Rücklagen: Steuer (ab Fabrikwahl, falls fällig) + 3 Paar Erstattungsreserve (~440 €) | Blatt „Kasse“ |

**Kassen-Ampel = K − F − R**
- **grün** ≥ 300 €
- **gelb** 0 bis 300 €: keine neuen Ausgaben außerhalb von Plan 3
- **rot** < 0: Ausgaben-Stopp-Liste (Hebel 7), dann Notfallhebel-Leiter (4.4)

**Regel:** Die 3 Paar Puffer aus [Plan 3.1] sind deine Erstattungsreserve. Sie werden nie für Kostenüberschreitungen verbraucht.

### 4.2 Harte Gates: hier fließt Geld oder nicht

| Datum | Gate | Grün → | Sonst → |
|---|---|---|---|
| **Fr 09.10.** | Design-Freeze [Plan 6] | Tech Pack So 11.10. | Die RFQ geht trotzdem Mo 12.10. raus, mit v1.7 und dem Satz „final placement confirmed by 16.10.“ Der Preis hängt an Stichen und Zonen, nicht an 5 cm Höhe. **Die Fabrikanfrage rutscht nicht.** |
| **Fr 23.10.** | Steuer schriftlich klar | Kapitalbedarf neu, Fabrik mit Steuer-Spalte | Mit 1.150 € planen. Hebel 5 wird Pflicht |
| **Mo 26.10.** | Fabrik gewählt | Panel-Stickerei im Haus mit Fotos belegt, Ampel grün oder gelb | Ampel rot: Gegenrechnung, Optionen an dich. Kein Vermittler ohne genannte Fabrik [lieferanten 1.5] |
| **So 01.11.** | **Validierung** [Plan 6] | Liste ≥ 150 **und** ≥ 10 Zusagen „Ja/Vielleicht zu 149 €“ **und** 50/50 schriftlich | Gelb (50–149 oder < 10 Zusagen): zahlen, Content und Netz-Runde nachschärfen. Rot (< 50): **nicht zahlen**, eine Woche schieben [Plan 6]. Letzter Ausstieg für ~60 € |
| **Di 10.11.** | Digitizing | ≤ 33.000 Stiche | Gegenrechnung, Kostendeckel (Hebel 3) |
| **Di 17.11.** | Stickproben [Plan 6] | Proto wird genäht | Kein Proto. Fabrik 2 aktivieren (Schätzung: ~650 € Entwicklung neu, +3–4 Wochen, Vorbestellung ~28.01., Drop 06.05.) oder Fehler beheben, wenn die Fabrik ihn klar benennt |
| **Sa 05.12.** | Proto und Fit | PP Mo 07.12. bestellen | Zweites Proto statt PP. Vorbestellung höchstens eine Woche schieben |
| **So 20.12.** | Zusagen ≥ 15 · Auszahlung geklärt · Stufe 2 entschieden | Vorbestellung wie geplant | Zusagen < 10: Ausgaben-Stopp (Hebel 7) und Proto-Runde verlängern. Auszahlung unklar: kein Start ohne Antwort |
| **Di 05.01.** | PP-Freigabe [Docket W17] | Öffnung Do 14.01., 19:00 | Öffnung höchstens auf Do 21.01. Schwelle wandert mit (Plan-Regel „2 Wochen schieben“) |
| **Mo 01.02.** | **Schwelle 1** + Mengenformel (Hebel 9) | ≥ 10 ausgezahlt, Hochrechnung trägt → 100, PO Mi 03.02. | 75 Stück oder schieben. **Keine PO ohne gedeckte Anzahlung** |
| **So 14.03.** | Vorbestellungen ≥ 29, ausgezahlt bis Mi 17.03. ≥ 30 | Restzahlung Fr 19.03. | Notfallhebel-Leiter (4.4) ab Stufe 3 |
| **Fr 19.03.** | Endkontrolle bestanden und ≥ 32 ausgezahlt [Plan 6] | zahlen | Nicht zahlen, wenn die Endkontrolle durchfällt. Fehlt nur Geld: Backstop Mi 24.03. (Hebel 4) |
| **~30.03.** | Steuer bei Einfuhr gedeckt (≥ 40 mit Steuer) | Ware freigeben lassen | Brücke (Hebel 10). Kampagne 1 streichen |
| **Do 15.04.** | Ware angekommen [Plan 6] | Drop 22.04. | Drop 29.04. oder Drop mit „Versand ab Ankunft“, offen angekündigt [Plan 6] |

### 4.3 Wochen-Gates W5–W32

Jeden Sonntag, im Wochenreview. „Alarm“ = die Zahl, unter der du sofort handelst. Liste Soll/Alarm aus [markt 3.7], der Rest aus 2.7.

| W | Sonntag | Prüfen | Wenn darunter → sofort |
|---|---|---|---|
| 5 | 18.10. | Liste ≥ 15 · Netz gezählt · ≥ 4 von 8 Fabriken haben geantwortet · Steuertermin steht | Netz < 40 Leute: Papiertest-Abend auf 15 Gäste, Proto-Runde im Dezember doppelt planen, Preis bei 75 bei jeder Fabrik nachfordern · < 4 Antworten: Nachfassen Fr 16.10., zwei Nachzügler aus der Prüfliste [lieferanten 1.5] · kein Steuertermin: IHK bis 23.10. |
| 6 | 25.10. | Liste ≥ 30 · ≥ 3 Angebote mit Preis bei 75 und 100 · Fabrikpreis-Ampel | Ampel rot: Gegenrechnung, Optionen V4b und Serp klein an dich · < 3 Angebote: Calls mit 2, Reserve aus Portugal · Liste < 30: drei neue Hooks, bestes Video in 5 Varianten [markt 5.2] |
| 7 | 01.11. | **Validierung** (4.2) | siehe 4.2 |
| 8 | 08.11. | Entwicklung nur bei Grün/Gelb bezahlt · Liste ≥ 80 · Fabrik antwortet in ≤ 3 Werktagen | Antwortzeit > 3 Werktage zweimal: Frühwarnung, Reserve-Fabrik anrufen und warm halten · Liste < 80: Netz-Runde 3 |
| 9 | 15.11. | Digitizing ≤ 33.000 Stiche · Liste ≥ 110 · Zusagen ≥ 11 | Stiche darüber: Kostendeckel · Zusagen < 8: Gesprächsliste [zielgruppe 5.1] um 5 Leute erweitern |
| 10 | 22.11. | Stickproben bestanden · Proto-Versanddatum schriftlich ≤ 30.11. · Liste ≥ 140 | kein Datum: Call mit der Fabrik, PP-Plan prüfen · Stickproben durchgefallen: 4.2 |
| 11 | 29.11. | Shopify Payments verifiziert · Support-Antwort zur Auszahlung · Rechtstexte live · Liste ≥ 170 | keine Verifizierung: Support anrufen, PayPal parallel · Liste < 170: Stick-Abend 27.11. nachfassen, Fotos mit eigenem Link [community 7] |
| 12 | 06.12. | Proto da, Fit ok · PP bestellt Mo 07.12. · Liste ≥ 200 · Proto-Runde gestartet | Proto verspätet: Proto-Runde beginnt mit Stickproben, Öffnung bleibt 14.01., wenn PP bis 05.01. kommt |
| 13 | 13.12. | Zusagen ≥ 18 („Ja“, mit Größe) · Liste ≥ 230 | < 12: jeden Tag 3 persönliche Termine bis 20.12. |
| 14 | 20.12. | **Gate** (4.2): Zusagen ≥ 15 · Auszahlung geklärt · Stufe 2 entschieden · Patch D bestellt | Zusagen < 10: Ausgaben-Stopp, Mess-Abende 16./23.01. fix, Reservierung prüfen (Hebel 6) |
| 15 | 27.12. | PP mit Tracking unterwegs | kein Tracking bis 28.12.: Fabrik schreiben, Öffnung 21.01. als Plan B notieren |
| 16 | 03.01. | Testbestellung: Auszahlung angekommen, Tage gezählt · Liste ≥ 300 (Korridor 700 am 31.12. [Plan 6]) · Brücke geklärt | Auszahlung > 3 Werktage: für jede Zahlung eine Woche Vorlauf rechnen · Liste < 300: zwei Netz-Runden im Januar |
| 17 | 10.01. | PP freigegeben · **Zusagen ≥ 25** · Liste ≥ 380 | Zusagen < 15: Mess-Abend 1 mit persönlicher Einladung an alle „Vielleicht“, Creator-Preview Di 12.01. voll nutzen [community 2.4] |
| 18 | 17.01. | Vorbestellungen ≥ 6 (Soll 10) | jede Zusage ohne Bestellung persönlich anrufen oder per DM, keine Massenmail · Mess-Abend 2 (23.01.) an alle Anmeldungen ohne Bestellung · Ausgaben-Stopp |
| 19 | 24.01. | ≥ 8 (Soll 13) | **keine Werbung** (5.3), stattdessen: Creator-Clips einsammeln, Zwischenstand „X von 35“ mit echter Zahl [markt Q48] · Mail an Abonnenten ohne Kauf vorziehen |
| 20 | 31.01. | **≥ 10 ausgezahlt** · Hochrechnung (Hebel 9) | 4.2 Schwelle 1 |
| 21 | 07.02. | PO bestätigt, Anzahlung bezahlt · ≥ 12 (Soll 18) · Kasse grün | < 12: Stufe 2 vorbereiten, Mess-Abend 3 (13.03.) jetzt einladen · Kasse rot: Shoot auf Handy und Freunde, 150 € sparen |
| 22 | 14.02. | ≥ 14 · Produktionsplan schriftlich · Stoff für die Menge reserviert | Stoff nicht reserviert: sofort schriftlich anfordern, sonst rutscht alles |
| 23 | 21.02. | ≥ 16 · Inline-Fotos 1 (16.02.) da | keine Fotos: Frühwarnung, Call, Liefertermin bestätigen lassen |
| 24 | 28.02. | ≥ 18 · Liste ≥ 850 | < 18: Mail „Noch X von 35“, persönliche DMs an alle mit 2 bestätigten Freunden [community 7], Brücke vorwarnen · Notfallhebel Zipper/Polo (4.4, Stufe 5) entscheiden |
| 25 | 07.03. | ≥ 21 · Inline-Fotos 2 (01.03.) · Steuer-Rücklage im Blatt | Rücklage fehlt: Kampagne 1 streichen |
| 26 | 14.03. | **≥ 25, besser 29** · ausgezahlt bis Mi 17.03. ≥ 30 | 4.4 ab Stufe 3 |
| 27 | 21.03. | Restzahlung raus (19.–24.03.) · 35 voll · Stufe 2 läuft · Versanddatum schriftlich | nicht gedeckt: Teil-Lieferung oder Brücke |
| 28 | 28.03. | Ware unterwegs mit Tracking · Stufe 2 ≥ 2 · Kasse für die Steuer | keine Tracking-Nummer bis Mi 24.03.: tägliche Mail, ab 31.03. Drop-Plan B vorbereiten |
| 29 | 04.04. | Ware da und geprüft (Stichprobe [Spec Teil 4]) · Steuer bezahlt · **≥ 40 mit Steuer** · Stufe 2 geschlossen | Fehlerquote hoch: reklamieren, Fehlerteile nicht verkaufen · < 40: Brücke |
| 30 | 11.04. | Vorbestellungen verschickt (06.–07.04.) · Liste ≥ 1.290 | Verzug beim Versand: Mail an alle Vorbesteller mit neuem Datum, bevor sie fragen |
| 31 | 18.04. | Ankunft war bis 15.04. · Liste ≥ 1.400 · Drop-Bestand im Shop | 4.2 Do 15.04. |
| 32 | 25.04. | **Drop:** Do 22.04., 21:00 ≥ 15 · Fr 23.04., 19:00 ≥ 26 (90 % in 48 h [markt Q27]) · So 25.04. ≥ 29 netto | Retargeting 72 h aus Drop-Umsatz, Drop-Abend Sa 24.04., Bundle mit Polo, Rest bleibt zu 169 € im Shop, kein Rabatt auf nummerierte Teile, Konsignation erst danach [markt 5.2] |

### 4.4 Notfallhebel-Leiter: vom billigsten zum teuersten

Immer von oben nach unten. Die nächste Stufe erst, wenn die vorige nicht reicht.

| Stufe | Hebel | Kostet | Wirkt bis |
|---|---|---|---|
| 1 | Warm: persönliche Nachrichten an alle Zusagen und „Vielleicht“, ein zusätzlicher Abend | Zeit | 1–2 Wochen |
| 2 | Ausgaben-Stopp-Liste (Hebel 7) | Abstriche bei Zipper/Polo und Werbung | sofort |
| 3 | Stufe 2 zum vollen Preis öffnen, Mess-Abend 3 am 13.03. | 20 Min. + 1 Abend | bis 17.03. |
| 4 | Restzahlung auf den Backstop Mi 24.03. legen (Hebel 4) | Versand 5 Tage später, Puffer zum 15.04. schrumpft auf ~11 Tage | 24.03. |
| 5 | **Zipper und Polo ab März auf Bestellung öffnen** (Abweichung von deiner Entscheidung „alles gleichzeitig am 22.04.“ vom 24.09.). Zipper ~82 € Marge, das Geld kommt vor dem Blank-Kauf [Spec 3C.5]. Nur bei Rot am 28.02. | bricht den gemeinsamen Launch | Mitte März |
| 6 | Teil-Lieferung gegen Teilzahlung (Hebel 4) | Rest kommt nach dem Drop | 24.03. |
| 7 | Brücke ziehen (Hebel 10) | Schulden | sofort |
| 8 | 75 statt 100 Stück | nur am 01.02. möglich | 01.02. |
| 9 | Drop schieben (29.04.) | Glaubwürdigkeit | 15.04. |
| 10 | Ausstieg mit voller Erstattung | siehe 4.5 | nur bis 03.02. ohne Verlust für Kunden |

**Was du nie tust:** den Vorbestellpreis über den 21.03. hinaus verlängern, ein Kontingent künstlich „ausverkauft“ melden, Vorbestellungen ohne Lieferung behalten [markt 5.2].

### 4.5 Was ein Ausstieg kostet

Kumuliert aus Plan 3, Zuordnung [R].

| Ausstieg bis | Schon ausgegeben (dein Geld) | Kundengeld |
|---|---|---|
| So 01.11. (Validierung) | ~60 € | keins |
| Mo 07.12. (PP-Bestellung) | ~1.420 € | keins |
| Do 17.12. (Patch D in Serie) | ~2.260 € | keins |
| **Mi 03.02. (PO)** | ~2.510 € | **alles unberührt, volle Erstattung möglich** |
| ab Do 04.02. (Anzahlung) | 4.500 € (dazu ~1.010 € Kundengeld in der Anzahlung) | **kein Ausstieg mehr ohne Schaden für Vorbesteller** |

**Der 03.02. ist der Punkt ohne Rückweg.** Alle Gates davor sind dafür da, dass du an diesem Tag nicht hoffen musst.

---

## 5 · Was sich gegenüber Rev 5.3 ändern muss

**Technikregel aus der Übergabe:** Aufgaben werden nie eingefügt oder verschoben, nur **angehängt** oder **an derselben Stelle** geändert oder in eine Notiz umgewandelt. Sonst verrutschen deine Häkchen. Alle Vorschläge unten halten sich daran.

### 5.1 Was bleibt (feste Termine)

Freeze Fr 09.10. · RFQ Mo 12.10. · Steuer Di 13.10. · Fabrik Mo 26.10. · Validierung So 01.11. · Entwicklung Mo 02.11. · Digitizing Mo 09.11. · Stickproben Di 17.11. · Proto Do 03.12. · PP Mo 07.12. · PP-Freigabe Di 05.01. · **Vorbestellung Do 14.01., 19:00** · **Schwelle Mo 01.02.** · Anzahlung Do 04.02. · Spiel-Entscheidung Fr 05.02. · Shoot Sa 20.02. · **Restzahlung Fr 19.03.** · **Vorbestellpreis endet So 21.03., 20:00** · Ware ~30.03. · Vorbestellungen raus 06.–07.04. · spätester Ankunftstermin Do 15.04. · **Drop Do 22.04., 19:00** · Auswertung So 25.04.

### 5.2 Neue Aufgaben (anhängen)

| Tag | W | Aufgabe | Min. | Fertig, wenn | Quelle / Grund |
|---|---|---|---|---|---|
| Do 08.10. | 4 | Steuerberater-Termin buchen, Gewerbeschein prüfen | 10 | Termin bis 13.10. steht | Hebel 1, [tools 3.3] |
| Di 13.10. | 5 | Blatt „Kasse“ anlegen (Vorlage von Claude) | 20 | Wochen, Plan-Posten, Gates, Ampel-Formel drin | 4.1 |
| Di 13.10. | 5 | Blatt „Netz“: Kontakte zählen, Spalte „Zusage“ und „Größe“ | 20 | Zahl steht | Hebel 6, [community 6.6] |
| Fr 23.10. | 6 | Steuer-Deadline: Ergebnis schriftlich an Claude | 10 | Kapitalbedarf neu gerechnet | Hebel 1 |
| Fr 30.10. | 7 | Shopify Payments aktivieren, Support-Frage zur Auszahlung | 30 | Antwort als Screenshot im Blatt „Kasse“ | Hebel 2 |
| Do 03.12. | 12 | Proto-Runde starten: 20 Termine bis So 13.12. | 15 | Termine im Kalender | Hebel 6 |
| Mo 14.12. | 14 | Stufe-2-Produkt (169 €, Nr. 036–060) als Entwurf | 20 | Produkt im Entwurf, Text mit Lieferdatum | Hebel 5 |
| Do 31.12. | 16 | Brücke klären (Gespräch) | 30 | Ja oder Nein steht im Blatt „Kasse“ | Hebel 10 |
| Sa 13.03. | 26 | Mess-Abend 3 (vorgezogen vom 20.03.) | 180 | Vorbestellungen vor Ort im Blatt | Hebel 8 |
| So 04.04. | 29 | Stufe 2 schließen, 20:00, Drop-Bestand rechnen | 15 | Produkt auf Entwurf, Blatt „Bestand“ neu | Hebel 5 |
| jeden So | 5–32 | **Kassencheck** (als Schritt im Wochenreview, siehe 5.3) | +10 | Ampel steht im Blatt | 4.1 |

### 5.3 Geänderte Aufgaben (an derselben Stelle, neue Schritte)

| Tag | Aufgabe im Docket | Was dazukommt |
|---|---|---|
| Fr 09.10. | Design-Freeze abnehmen und Tech Pack bestellen | Kostendeckel 33.000 Stiche [design V4a] · Herstellerangabe aufs Pflegeetikett [tools 3.1] · Wenn der Freeze nicht steht: RFQ geht trotzdem am 12.10. raus (4.2) |
| So 11.10. | Tech Pack v1 prüfen und freigeben | Kostendeckel-Satz prüfen |
| Mo 12.10. | Anfrage (RFQ) an 8 Fabriken | Zusatzfragen aus Hebel 3: Preis bei 75 und 100, je 1.000 Stiche, Fadenschnitte, DDP und DAP, Euro, Betriebsferien, Zahlung |
| Di 13.10. | Steuerstatus klären | 8 Fragen aus [tools 3.3] + Frage 9 (Fälligkeit, Spediteur) |
| Mo 19.10. | Angebote in den Vergleich | Fabrikpreis-Ampel (Hebel 3), Schwellen je Angebot. Prompt: *„Hier sind die Angebote: … Rechne für jedes Fabrikpreis je Paar inkl. Stickerei, Kapitalbedarf, Schwelle 1 und 2 nach Plan 3.1, mit und ohne 1.150 € Steuer, bei 100 und 75 Stück. Sag mir ehrlich, welche Fabrik die Kasse am wenigsten belastet.“* |
| Mo 26.10. | Fabrik entscheiden | Scorecard mit Spalten Steuer und Zahlungsbedingungen. EORI am selben Tag beantragen, wenn Türkei [tools 3.3] (statt erst Fr 30.10.) |
| Di 27.10. | Konditionen verhandeln | Die 8 Punkte aus Hebel 4 |
| So 01.11. | VALIDIERUNG | Zweites Kriterium: ≥ 10 Zusagen · drittes: 50/50 schriftlich (4.2) |
| Mo 02.11. | Proforma prüfen und Entwicklung bezahlen | Bankdaten-Regel (Hebel 4) · nur bei Grün/Gelb |
| Di 10.11. | Digitizing freigeben | ≤ 33.000 ohne Rückfrage, sonst Gegenrechnung: *„Die Digitizing-Vorschau hat … Stiche. Rechne Stückkosten, Kapital, Schwellen nach Spec 3.11 und Plan 3.1 neu und sag mir, welche Vereinfachung am wenigsten vom Design wegnimmt.“* |
| Mi 25.11. | Zahlungsanbieter einrichten | wird zu: PayPal verbinden, Auszahlungsplan beider Anbieter notieren (Shopify Payments ist seit 30.10. aktiv) |
| Sa 19.12. | Vorbestellung: Kontingent und Start festlegen | 35 zu 149 € + Stufe 2 zu 169 € (Hebel 5) statt „Kontingent 45“ |
| Di 29.12. | Testbestellung im Shop | Auszahlung bis aufs Bankkonto verfolgen, Werktage zählen, dann erstatten |
| Mi 06.01. | Bestellkonditionen festzurren | Backstop 24.03., Teil-Lieferung, Preis bei 75, Euro |
| Di 19.01. | Tempo bewerten | **Regel umgedreht:** Unter 10 nach 5 Tagen gibt es kein Werbegeld. Kalte Werbung füllt die Liste nicht [markt 2.5], und das Geld fehlt bei der Anzahlung. Stattdessen Notfallhebel-Leiter Stufe 1–2. Ab ≥ 10 darfst du 50 € auf das beste Video als Retargeting testen, wenn die Kasse grün ist |
| Do 28.01. | Hochrechnung Cash-Schwelle | Mengenformel (Hebel 9). Nur ausgezahltes Geld zählt (Hebel 2) |
| Mo 01.02. | SCHWELLE: 100, 75 oder schieben | Formel statt Gefühl. „> 25 → Kontingent 45“ ersetzt durch Stufe 2 |
| Mi 03.02. | Bestellung (PO) senden | Klauseln aus Hebel 4: Rest „spätestens 24.03.“, Teil-Lieferung, Bankdaten, Euro |
| Mi 10.03. | Restzahlung vorbereiten | Steuer-Rücklage mitrechnen. Stand So 14.03. ist das Gate |
| Fr 19.03. | Endkontrolle und Restzahlung | Backstop Mi 24.03., wenn nur Geld fehlt. Nie zahlen, wenn die Endkontrolle durchfällt |
| So 21.03. | Vorbestellung schließen | Nur der Preis 149 € endet. Stufe 2 läuft bis So 04.04. |
| Fr 26.03. | Werbung aufsetzen | nur bei Kassen-Ampel grün nach Restzahlung und Steuer |
| jeden So | Wochenreview | Schritt „Kassencheck“ (4.1) und „Wochen-Gate“ (4.3) |

### 5.4 Terminänderungen mit Begründung

| Was | Rev. 5.3 | Neu | Warum |
|---|---|---|---|
| Shopify Payments aktivieren | Mi 25.11. | **Fr 30.10.** | Prüfung kann dauern (W). Die Auszahlungsfrage muss vor dem 20.12. beantwortet sein |
| EORI (nur Türkei) | Fr 30.10. | Mo 26.10. | kostet nichts, Proto kommt ~30.11. [tools 3.3] |
| Mess-Abend 3 | Sa 20.03. [community] | **Sa 13.03.** | Das Geld vom 20.03. kommt nach der Restzahlung |
| Restzahlung | Fr 19.03. | Fr 19.03. **mit Backstop Mi 24.03.** | Die Schlusswelle (U-Form [markt Q31]) liegt am 20.–21.03., ihr Geld kommt erst danach |
| Vorbestellung schließen | So 21.03. | So 21.03. (149 €) + So 04.04. (Stufe 2) | Hebel 5 |
| Spiel-Entscheidung | Fr 05.02. | Termin bleibt, **Kriterium jetzt festlegen** | siehe 5.5 |

### 5.5 Streichungen und Empfehlungen

- **Pixel-Spiel:** Aus Cash-Sicht streichen. Keine belegte Verkaufswirkung [markt Hebel 11]. ~40 Stunden laut Docket Rev. 5 [website Kurzfassung]. Diese Stunden brauchst du für Zusagen und Abende. Der Termin 05.02. bleibt. **Kriterium für „bauen“:** ≥ 25 Vorbestellungen am 05.02., kein Gate rot, Kasse grün. Sonst streichen. Die 27 S-Aufgaben werden dann an derselben Stelle zu Notizen.
- **Chenille-Muster (120 €):** Streichen, wenn du am 19.12. gestickt wählst, wie der Plan empfiehlt [Plan 4.2]. Schwelle 1 sinkt auf 9.
- **Werbetest im Januar (100 € aus dem Puffer, Docket W19):** streichen (5.3).
- **Kontingent 45 zu 149 €:** ersetzt durch Stufe 2 zu 169 € (Hebel 5).
- **Design:** Kein Vorschlag aus diesem Blickwinkel, der dein Design ändert. Die Gegenrechnung steht in 2.3. V4a (Kostendeckel) ist Pflicht, V4b und „Serp klein“ sind Notfalloptionen bei Ampel rot [design 3.7].

### 5.6 Zeitbedarf

Neu dazu: ~10 Min. Kassencheck pro Woche (28 Wochen ≈ 4,7 h), ~1,5 h Steuer, ~1 h Auszahlung und Test, ~3 h Proto-Runde verteilt, ~1 h Konditionen. Zusammen ~11 Stunden bis April [R]. Ohne Spiel sparst du ~40 Stunden [website]. **Netto hast du mehr Zeit als in Rev. 5.3.**

---

## 6 · Risiken aus diesem Blickwinkel

Schaden in Euro und in Vorbestellungen bei Schwelle 2 (146 € = 1) [R].

| # | Risiko | Schaden | Frühwarnsignal | Gegenmaßnahme | Termin |
|---|---|---|---|---|---|
| 1 | **Steuer nicht im Budget** (Türkei sicher, Portugal wahrscheinlich, **W**) | ~1.150 € = 8 | Steuerberater bestätigt | Hebel 1 und 5, Brücke | 13.10. / 23.10. |
| 2 | **Fabrikpreis über ~60 €** | +1 € = +0,7 | Angebote ab 19.10. | Ampel (Hebel 3), 75 Stück, Kostenoptionen | 19.10. |
| 3 | Stichzahl über 33.000 (echter Kreuzstich) | +275 bis +550 € = +2 bis +4 | Vorschau 09.11. | Kostendeckel (Hebel 3) | 09.–10.11. |
| 4 | 60/40 statt 50/50 | Schwelle 1: 14 statt 10 | Angebot, Verhandlung | Hebel 4 | 27.10. |
| 5 | **Auszahlung verzögert oder zurückgehalten** | bis zur gesamten Vorbestellsumme | Support-Antwort, Testauszahlung | Hebel 2, PayPal parallel | 30.10. / 29.12. |
| 6 | Vorbestellungen unter Schwelle 1 | Anzahlung ungedeckt | Zusagen < 15 am 20.12. | Hebel 6, 8, 9 | 20.12. / 17.01. |
| 7 | Vorbestellungen unter Schwelle 2 | Restzahlung ungedeckt | < 18 am 28.02. | Notfallhebel-Leiter | 28.02. / 14.03. |
| 8 | **Zeitversatz:** Preisende 21.03. nach Restzahlung 19.03., Auszahlung dauert | Schlusswelle zählt nicht | Auszahlungstage aus dem Test | Backstop 24.03., Mess-Abend 13.03. | 03.02. (PO) |
| 9 | **Fabrik fällt nach der Anzahlung aus** | 3.000 € weg, 35 Erstattungen à 149 € = 5.215 € offen [R] | Antwortzeiten, fehlende Inline-Fotos, Stoff nicht reserviert | Gates bis PP, Referenzen, Inline-Fotos 16.02. und 01.03., Reserve-Fabrik warm halten, Brücke | laufend |
| 10 | Zahlung an Betrüger (geänderte Bankdaten, **W**) | eine ganze Rate | neue Kontodaten per E-Mail | Bankdaten-Regel (Hebel 4) | jede Zahlung |
| 11 | Lieferverzug: Ramadan-Fest TR 08.–11.03. [Plan 7], Ostern 26.–29.03. [R], Zoll | Drop 29.04., Verunsicherung bei Vorbestellern | kein Tracking bis 24.03. | Puffer bis 15.04. (16 Tage ab ~30.03. [R]), Plan-Regel 15.04. | 04.03. / 24.03. |
| 12 | Feiertage im Entwicklungsfenster (**W**, prüfen): TR 29.10. (Woche der Fabrikwahl), PT 01.12. und 08.12. (Proto, PP), Weihnachten (PP-Versand) | Tage, die im Plan fehlen | Betriebsferien-Frage im RFQ | Termine im RFQ abfragen, PP-Versand vor 23.12. verlangen | 12.10. |
| 13 | Qualitätsmängel bei Wareneingang | Nacharbeit, weniger verkaufbare Paare | Inline-Fotos | Endkontrolle vor Restzahlung, nie vorher zahlen | 19.03. |
| 14 | Retouren 10–20 % | 7–13 Paar, Erstattungen Ende April | Größenfragen in DMs | ehrliche Größen, Mess-Abende, 3 Paar Erstattungsreserve [markt 2.6] | ab 08.04. |
| 15 | Kleine Kosten ohne Budgetzeile (Steuerberater, LUCID und Lizenz, Rechtstexte, Shopify Email im April, **W**) | ~300–500 € (Schätzung) | Blatt „Ausgaben“ > Plan | Puffer neu ordnen, Ausgaben-Stopp | 13.10. / 24.11. / 29.03. |
| 16 | Abmahnung (LUCID fehlt, Rechtstexte, Kennzeichnung, Herstellerangabe, **W**) | unbekannt | — | LUCID vor dem ersten Paket, Rechtstexte 24.11., GPSR ins Tech Pack [tools 3] | 11.10. / 24.11. |
| 17 | Scope-Drift (neue Stickerei, Spiel, Chenille) | je nach Idee | „nur noch schnell …“ | Gegenrechnung vor jeder Idee [Übergabe 7] | immer |
| 18 | Symbol-Risiko senkt die Nachfrage im Kernsegment | Schwellen wackeln | ≥ 2 von 10 sagen „Sowjet/Wappen“ [design 4] | Test vor dem Digitizing, Farbe kostet 0 Stiche [zielgruppe 5.6] | 08.10. / bis 08.11. |
| 19 | Deine Zeit, Ausfall an langen Tagen | Gates werden verpasst | 2 Wochenreviews ausgefallen | Spiel streichen, Tag nach langen Tagen nur Pflicht [community 8] | laufend |

### 6.1 Der kritische Pfad der Fabrik, mit Puffer

RFQ 12.10. → Fabrik 26.10. → Entwicklung bezahlt 02.11. → Digitizing 09.11. → Stickproben 17.11. → Proto 03.12. → PP bestellt 07.12. → PP-Freigabe 05.01. → Vorbestellung 14.01. → Schwelle 01.02. → Anzahlung 04.02. → Produktion ab 08.02. → Ramadan-Fest 08.–11.03. → Endkontrolle und Rest 19.03. (Backstop 24.03.) → Versand ~22.03. → Ostern 26.–29.03. → Ware ~30.03. → spätestens 15.04. → Drop 22.04. [Plan 5, 6, 7]

**Puffer:** 16 Tage zwischen geplanter Ankunft (~30.03.) und spätestem Ankunftstermin (15.04.) [R]. Mit Backstop 24.03. bleiben ~11 Tage (Schätzung, LKW 3–7 Tage [Plan 7]). **Das ist der einzige Zeitpuffer im ganzen Plan.** Jede Woche Verzug vor dem 04.02. frisst ihn auf. Darum rutscht die RFQ nicht, auch wenn der Freeze rutscht.

---

## 7 · Deine Entscheidungen (aus diesem Blickwinkel)

1. **Planst du bis zur Steuer-Antwort mit 1.150 € mehr?** (Empfehlung: ja)
2. **Stufe 2 zum vollen Preis 169 €** statt Kontingent 45 zu 149 €? (Hebel 5)
3. **Restzahlung mit Backstop 24.03. und Teil-Lieferung** in die Verhandlung? (Hebel 4)
4. **Mengenformel 100/75** am 01.02. statt Bauchgefühl? (Hebel 9)
5. **Mess-Abend 3 auf Sa 13.03.?** (Hebel 8)
6. **Brücke** über 1.500 € in der Familie anfragen? (Hebel 10)
7. **Pixel-Spiel:** Kriterium für den 05.02. jetzt festlegen oder gleich streichen? (5.5)
8. **Notfallhebel Zipper/Polo ab März** als Option akzeptieren, nur bei Rot am 28.02.? (4.4)

---

## 8 · Quellen

**Selbst geprüft in dieser Teilaufgabe: 0.** Suchbudget aufgebraucht, `help.shopify.com` und `gesetze-im-internet.de` vom Proxy blockiert. Die folgenden Quellen haben die Recherche-Agenten heute in dieser Sitzung per Websuche gesehen, meist als Suchauszug. Güte aus `markt.md`: A = Studie/Primärquelle, B = großer Datensatz/Fachpresse, C = Agentur/Blog.

**Intern**
- Plan Rev. 5.3: `docs/time-travel-drop-plan.md` (Abschnitte 1, 3, 3.1, 3.2, 4.2, 5, 6, 7, 10, 12, 13)
- Spec Rev. 13: `docs/produkt-spec_rev13.md` (2.8, 3.11, 3C.5, Teil 4)
- Übergabe: `docs/uebergabe-time-travel.md`
- Docket Rev. 5.3: `r5/weeks_r5.json` (W4–W32)
- Recherche: `rev6/research/markt.md`, `zielgruppe.md`, `community.md`, `tools.md`, `lieferanten.md`, `design.md`, `website.md`, `berlin.md`, `content.md`

**Extern (über `markt.md`)**
- [Q23] C · LaunchList, Waitlist → Kauf 2–5 %, kalt 1–3 %: https://getlaunchlist.com/blog/convert-waitlist-to-paying-customers
- [Q26] B · LaunchBoom, 1-$-Reservierung 30× Kaufwahrscheinlichkeit: https://www.launchboom.com/crowdfunding-tips/how-to-build-a-prelaunch-email-list/
- [Q27] B · LaunchBoom, VIP-Liste 20–40 %, 90 % der Käufer in 48 h: https://www.launchboom.com/crowdfunding-tips/how-to-promote-your-kickstarter-campaign-updated/
- [Q31] A · Kuppuswamy/Bayus, U-förmiger Verlauf: https://yannigroth.com/2013/02/24/the-dynamics-of-backer-support-in-crowdfunding-findings-from-kickstarter · https://arxiv.org/pdf/1607.06839
- [Q32] B · Klaviyo, E-Mail-Benchmarks 2026 (0,12 % Bestellungen je Empfänger): https://www.klaviyo.com/uk/blog/email-marketing-benchmarks-open-click-and-conversion-rates
- [Q36] B · Unbounce, Landingpage-Median 6,6 %: https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/
- [Q37] B · Socialinsider, TikTok-Benchmarks 2026: https://www.socialinsider.io/social-media-benchmarks/tiktok
- [Q42] C · ostend.digital, Meta-Kosten DE: https://ostend.digital/meta-ads-kosten-kompass/
- [Q43] C · Adamigo, Meta CPM/CPC 2026: https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026
- [Q44] A · Bitkom, Retouren 11 %, 67 % wegen Größe: https://www.bitkom.org/Presse/Presseinformation/Online-Shopping-Jeder-zehnte-Kauf-geht-zurueck
- [Q48] A · Aggarwal, Jun, Huh (2011), Knappheit: https://experts.umn.edu/en/publications/scarcity-messages-a-consumer-competition-perspective/
- [Q54] C · ATTN Agency, Pop-up-ROI: https://www.attnagency.com/blog/popup-shop-experiential-marketing-roi-measurement-dtc-2026
- [Q55] A · Shopify Help Center, Vorbestellungen und Teilzahlung: https://help.shopify.com/en/manual/products/purchase-options/pre-orders

**Nicht belegt, vor dem Handeln prüfen (W):** Steuerfolgen Portugal und Regelbesteuerung, Reverse Charge, Widerruf vor Lieferung, Auszahlungsreserven bei Shopify Payments und PayPal, Feiertage TR 29.10. und PT 01.12./08.12., Laufzeit von Auslandsüberweisungen, Betrugsmuster „geänderte Bankdaten“, LUCID-Pflichten. Wer klärt: Steuerberater (13.10.), Shopify-Support (30.10.), Rechtstexte-Anbieter (24.11.), Fabrik im RFQ (12.10.).
