# -*- coding: utf-8 -*-
HEAD = """# Content-System und Video-Bibliothek · Time Travel

Stand: Mi 07.10.2026, abends. Für Ernest. Teil der Docket-Neuplanung (Rev. 6).
Drop Do 22.04.2027, 19:00 (Warteliste ab 18:00). Ziel 10.000 € = 64 Jeans (35 Vorbestellungen à 149 € + 29 im Drop à 169 €).
Grundlage: Plan Rev. 5.3, Spec Rev. 13, Docket Rev. 5.3, dazu `markt.md` und `zielgruppe.md` aus diesem Ordner.
Quellen als [Q-Nummer], Liste in Abschnitt 7. Maschinenlesbare Kopie der Bibliothek: `content_library.json` im selben Ordner."""

KURZ = """## Kurzfassung

**Was du hier hast.** 125 Video-Konzepte (V001–V125) und 24 Countdown-Konzepte (CD-T24 bis CD-T01). Jedes hat Datum, Slot, Hook auf Englisch und Deutsch, einen zweiten Hook zum Testen, Shotliste, Drehort, Dauer, Ton, Caption, CTA und Regel-Check. V001–V107 liegen auf den Post-Terminen des Dockets Rev. 5.3. V108–V125 sind Reserve für Extra-Tage und Ersatz für schwache Videos.

**Die fünf wichtigsten Punkte:**

1. **Morgen, Do 08.10., beim Papiertest 3 alles filmen.** V001, V119 und später V093 und CD-T03 leben von diesem Material. Shotliste in 4.1: 12 Clips, 15 Minuten extra.
2. **Reichweite kommt aus Ausreißern.** Kleine Business-Konten (1.000–5.000 Follower) holen auf TikTok im Schnitt 317 Views pro Post. Reels erreichen etwa 10 % der Follower [Q4][Q5]. Für 3.000 Anmeldungen brauchst du grob 1,2 Mio. Views (Schätzung, markt.md 3.5). Deshalb hat jedes Konzept einen Test-Hook. Jedes Video mit mehr als dem Doppelten deines Medians drehst du in fünf Varianten nach.
3. **Drei Achsen tragen den Verkauf:** Teppich und Familie (stärkster Auslöser deiner Kernzielgruppe), Handwerk im Makro (Goldfäden, Kreuzstich, Ton der Nadel), ehrliche Zahlen (Budget, Kosten, „X von 35“).
4. **Acht Änderungen am Rev.-5.3-Plan, alle aus zielgruppe.md abgeleitet, du entscheidest:** zweimal „Älter als jede Grenze“ ersetzt. Teppich-Post vom 25.11. auf den 18.11. vorgezogen. Vom 23. bis 29.11. kein Ernte- oder Sichel-Post, am 28.11. gar keiner. „Das erste Bild“ vom 24.02. auf den 25.02. verschoben. „37 mal 37“ auf 45 × 45 korrigiert. Unboxing am 03.12. neu. Nach außen „cross-stitch band“ und „eight-point star“ statt Vyshyvanka und Alatyr.
5. **Der Ablauf passt in deine Zeit:** Sonntag 75–100 Minuten Dreh, Posttag 20 Minuten, sonst 10 Minuten Community. Ein Schnitt in CapCut, nativ auf TikTok, Reels und Shorts hochgeladen. Musik erst in der jeweiligen App, aus deren Business-Bibliothek.

**Wie belastbar das ist.** Ich konnte in dieser Runde keine Seite selbst öffnen: Das Suchbudget war aufgebraucht, der Seitenabruf gesperrt. Alle Zahlen mit [Q] stammen aus Quellen, die die Markt- und die Zielgruppen-Recherche heute in dieser Sitzung per Websuche gesehen haben. Plattform-Mechanik (Algorithmus-Signale, Längen, Hashtag-Limit, Musikbibliotheken) steht als **UNGEPRÜFT** da, jeweils mit dem Ort, an dem du es in zwei Minuten selbst prüfst. Für die besten Uhrzeiten gibt es keine geprüfte Zahl. Deshalb liest du ab Woche 8 deine eigenen Insights.

**Messen:** jeden Sonntag 15 Minuten, eine Tabelle, vier Kennzahlen pro Video: Views, Ø-Wiedergabezeit, Shares plus Saves, Anmeldungen. Die Schwellen richten sich nach deinem eigenen Median und nach den Wochenzielen aus markt.md 3.7."""

S0 = """## 0 · Wie belastbar die Angaben sind

| Kennzeichnung | Bedeutung |
|---|---|
| **[Q1]–[Q33]** | Quelle in dieser Sitzung (07.10.2026) per Websuche gesehen, von der Markt- oder Zielgruppen-Recherche. Gesehen wurden Such-Auszüge, nicht die Volltexte. Ich habe sie übernommen, nicht selbst erneut geöffnet |
| **UNGEPRÜFT** | Mein Wissensstand (bis Mitte 2026), in dieser Runde nicht prüfbar. Steht nur da, weil du es für die Arbeit brauchst. „Wo prüfen“ sagt dir, wo du es selbst siehst |
| **Schätzung** | meine Rechnung oder Arbeitsregel, nicht belegt |
| **vor Ort prüfen** | Adresse oder Zeit aus Sekundärquelle |

**Was in dieser Runde nicht ging:** Das gemeinsame Suchbudget aller Agenten war beim Start dieser Aufgabe aufgebraucht. Seitenabrufe auf support.tiktok.com, newsroom.tiktok.com, about.instagram.com, blog.youtube und buffer.com hat der Netzwerk-Proxy blockiert. Deshalb gibt es hier **keine** neu geprüften Plattform-Zahlen 2026 (Uhrzeiten, ideale Längen, Frequenz-Studien) und **keine** geprüften Beispiel-Accounts für einzelne Formate. Ich habe nichts davon erfunden. Die Lücken stehen in Abschnitt 6."""

S1 = """## 1 · Plattform-Fakten 2026

### 1.1 Wer ist wo

| Fakt | Wert | Status |
|---|---|---|
| Wöchentliche Nutzung, 14–29 Jahre, Deutschland | Instagram 77 %, TikTok 50 % [Q1]. Eine Zusammenfassung derselben Studie nennt 82 % und 52 % [Q2] | belegt. Welche Lesart stimmt, ist offen (Altersgruppe oder Definition) |
| Gen Z in Deutschland entdeckt neue Mode über Social Media | 60 %. Für 53 % ist Mode das wichtigste Mittel des Selbstausdrucks [Q3] | belegt |
| YouTube Shorts, Nutzung in Deutschland | nicht geprüft | offen |

**Folge:** Instagram ist dein Verkaufskanal: Link-Sticker, Countdown-Sticker, DMs, Shop. TikTok bringt Reichweite. YouTube Shorts ist Zweitverwertung und kostet dich keine Extra-Minute: dieselbe Datei, ein Titel.

### 1.2 Was kleine Konten realistisch erreichen

| Kennzahl | Wert | Quelle |
|---|---|---|
| TikTok, Ø Views pro Post, Business-Konten 1.000–5.000 Follower (Jan–Jun 2026) | 317 | [Q4] |
| … 5.000–10.000 Follower | 855 | [Q4] |
| … 10.000–50.000 Follower | 2.500 | [Q4] |
| TikTok, Engagement nach Views, 1.000–5.000 Follower | 4,40 % | [Q4] |
| Instagram Reels, Reichweite in % der Follower, 1.000–5.000 Follower | 9,78 % | [Q5] |
| Modemarken, Median-Engagement Instagram / TikTok | 0,15 % / 0,95 % | [Q6] |
| Instagram Nano-Creator (1.000–10.000 Follower), Engagement | 1,78 %, höchste Gruppe | [Q7] |

**Lesart:** Ein durchschnittlicher Post bringt dich nicht ans Ziel. Ein kleines Konto wächst über drei bis fünf Ausreißer mit 50.000 Views und mehr (markt.md 3.5, Schätzung). Ausreißer kannst du nicht planen. Du machst sie wahrscheinlicher: viele Hooks testen, Gewinner sofort variieren.

### 1.3 Was der Algorithmus belohnt (UNGEPRÜFT)

**TikTok.** TikTok beschreibt seine Empfehlungen selbst so: Es zählen Interaktionen (Likes, Shares, Kommentare, ob du ein Video bis zum Ende schaust, wem du folgst), Informationen am Video (Caption, Sound, Hashtags) und mit geringerem Gewicht Geräte- und Kontoeinstellungen (Sprache, Land). Ein längeres Video bis zum Ende zu schauen gilt als starkes Signal. Die Follower-Zahl ist laut TikTok kein direkter Faktor. *Wo prüfen:* TikTok-Hilfe „How TikTok recommends content“ (support.tiktok.com) und TikTok Newsroom „How TikTok recommends videos #ForYou“ (2020). Beide Abrufe waren am 07.10. blockiert.

**Instagram.** Adam Mosseri (Chef von Instagram) hat 2025 drei Signale als die wichtigsten für Reels genannt: Wiedergabezeit, Likes pro Reichweite und Sends pro Reichweite, also wie oft ein Reel per DM weitergeschickt wird. Sends zählen am meisten, wenn du Nicht-Follower erreichen willst. Instagram bevorzugt Originalinhalte. Reposts fremder Inhalte und Videos mit Wasserzeichen anderer Apps werden schwächer empfohlen. *Wo prüfen:* about.instagram.com, Beitrag „Instagram Ranking Explained“ (Abruf blockiert), und die Videos auf Mosseris Instagram-Konto.

**YouTube Shorts.** Seit Oktober 2024 bis zu 3 Minuten lang. Seit 31.03.2025 zählt YouTube jeden Start und jede Wiederholung eines Shorts als View, „engaged views“ stehen getrennt in YouTube Analytics. *Wo prüfen:* YouTube-Hilfe und blog.youtube (Abruf blockiert).

**Was daraus für dich folgt (gilt unabhängig von der genauen Gewichtung):**

| Signal | Was du baust | Beispiele in der Bibliothek |
|---|---|---|
| Wiedergabezeit, bis zum Ende schauen | Die erste Sekunde zeigt Hook als Text, Bild und ersten Satz gleichzeitig. REACH-Videos sind 6–10 s kurz und loopen | V024, V030, V046, CD-Serie |
| Sends (DM weiterleiten) | Inhalt, den man jemandem schickt: Teppich bei Oma, „Miss deine Jeans“, „Welche Tasche würdest du tragen?“ | V017, V034, V115, V122, V123 |
| Saves | Nutzwert: Anleitungen, Ornament-Karussells, Prozesskette | V034, V069, V108–V112, V115 |
| Kommentare | Am Ende eine konkrete Frage, keine allgemeine. „Did your family have one?“ statt „Thoughts?“ | V017, V027, V037 |
| Originalität | Eigene Clips, eigener Ton, kein Wasserzeichen. Nie das TikTok-Download-Video auf Instagram hochladen | Abschnitt 4.5 |

### 1.4 Länge pro Slot (Arbeitsregel, Schätzung)

| Slot | Länge | Warum |
|---|---|---|
| REACH | 6–10 s | soll loopen, ein Gedanke |
| DETAIL | 8–15 s | ein Makro, ein Satz |
| BUILD | 15–30 s | ein Fortschritt, eine Zahl |
| REAL | 20–35 s | eine Zahl oder ein Fehler, ehrlich erklärt |
| ORIGIN | 20–40 s | Geschichte braucht Zeit, aber keinen Vorlauf |
| Karussell | 4–8 Slides | Slide 1 ist der Hook |

**Regel nach dem Messen:** Liegt die Ø-Wiedergabezeit unter der Hälfte der Videolänge, schneidest du die nächste Version um ein Drittel kürzer (Schätzung). Technische Obergrenzen (UNGEPRÜFT): Reels bis 3 Minuten seit Januar 2025, Shorts bis 3 Minuten, TikTok deutlich länger. Du brauchst keine davon.

### 1.5 Wie oft posten

Keine geprüfte Frequenz-Studie in dieser Runde. Du bleibst beim Plan: **3 pro Woche bis 29.11., 5 pro Woche ab dem Proto, 4–5 während Vorbestellung und Produktion, täglich im Countdown.** Regelmäßigkeit schlägt Menge (Arbeitsregel). Wenn du mehr grinden willst: pro Woche **ein bis zwei Karussells** aus der Reserve (V108–V112), je 10 Minuten. Sie kosten keinen Dreh.

### 1.6 Photo Mode und Karussell (UNGEPRÜFT)

TikTok Photo Mode: mehrere Fotos mit Sound, zum Wischen. Instagram-Karussell: bis zu 20 Bilder oder Clips. Instagram zeigt Karussells Leuten, die nicht gewischt haben, später oft mit der nächsten Slide noch einmal. **Wofür du sie nimmst:** Ornament-Bedeutung (V108–V112), Prozesskette (V069), „Start here“ zum Anheften (V087). Format 4:5 hoch, 1080 × 1350 px (UNGEPRÜFT, im Upload-Dialog sichtbar).

### 1.7 Beste Uhrzeiten in Deutschland

Keine geprüfte Zahl in dieser Runde. Du bleibst bei den Plan-Zeiten: **18:00** für BUILD, ORIGIN, REAL, DETAIL und den Countdown, **19:00** für REACH, **12:00** für ASK-Storys. Deine Zielgruppe ist 18–35 und nach Arbeit oder Uni am Handy. Der Abend ist plausibel (Schätzung).

**Selbsttest:** Nach vier Wochen (So 08.11.) liest du die Aktivzeiten deiner Follower ab. TikTok: Analytics → Follower. Instagram: Insights → Follower → aktivste Zeiten (UNGEPRÜFT, Menünamen können abweichen). Liegt die Spitze mehr als eine Stunde neben 18:00, schiebst du die Postzeit dorthin.

### 1.8 Hashtags und Suche

- **TikTok wird wie eine Suchmaschine benutzt (UNGEPRÜFT).** Deshalb steht das Stichwort dreimal im Video: als Text im Bild, gesprochen und in der Caption. Deine Stichwörter: *embroidered jeans, cross-stitch, denim, gold thread, Berlin, clothing brand*.
- **3–5 Hashtags pro Post:** einer breit (#denim), zwei Nische (#embroidereddenim, #crossstitch), einer Marke (#novalifetimetravel), einer Ort (#berlinfashion). Die Sets je Slot stehen in der Bibliothek. Die Größe der Hashtags ist nicht geprüft.
- **Instagram:** Seit Dezember 2025 sind höchstens 5 Hashtags pro Post möglich (UNGEPRÜFT, du merkst es beim sechsten). Stichwörter in der Caption zählen mehr als Hashtags.
- **Meiden:** #slavicembroidery und ähnliche Tags, weil sich dort die Neuheiden-Szene mischt [Q23]. Dazu alles Politische, #ussr, #soviet, Länderflaggen-Emojis.

### 1.9 Trend-Sounds legal nutzen (UNGEPRÜFT, keine Rechtsberatung)

| Plattform | Regel | Wo |
|---|---|---|
| TikTok, Business-Konto | Nur die **Commercial Music Library** (für Werbung freigegebene Musik). Bekannte Charts-Songs sind für Business-Konten gesperrt | In der App beim Sound-Auswählen. Trends: TikTok Creative Center → Trends → Songs, Region Deutschland, Filter „für Business freigegeben“ |
| Instagram, professionelles Konto | Eingeschränkte Musikbibliothek. Ist ein Song ausgegraut oder fehlt, ist er für dein Konto nicht lizenziert | Beim Reel-Upload „Audio“ |
| YouTube Shorts | Audio aus der YouTube-Bibliothek. Fremde Musik mit Content-ID-Anspruch kann ein Short sperren | YouTube Studio → Audio-Mediathek |

**Deine drei Regeln:**
1. **Eigener Ton zuerst.** Stimme, Papier, Schere, Nadel, Stickmaschine. Er gehört dir und kann selbst zum Sound werden.
2. **Musik erst in der App hinzufügen**, nie in CapCut einbacken. Ob CapCut-Musik für Werbung freigegeben ist, habe ich nicht geprüft. So bleibt dieselbe Datei auf allen drei Plattformen sauber.
3. **Nie auf ein privates Konto wechseln**, um einen Charts-Song zu nutzen. Novalife wirbt, also gilt die Business-Regel.

### 1.10 Story-Werkzeuge (belegt)

- **Umfrage-Sticker** mit bis zu vier Antworten, dazu Emoji-Schieberegler, Quiz, Frage-Sticker [Q9]. Für alle ASK-Storys.
- **Countdown-Sticker:** Wer „Erinnern“ tippt, bekommt zum Ende eine Nachricht [Q8]. Einsatz: 14.01. 19:00, 21.03. 20:00, 22.04. 19:00.
- **Live:** Live-Shopping erreicht bei großen Händlern bis zu ~30 % Conversion [Q10]. Auf dich ist das nicht übertragbar. Ein Live zur Öffnung (14.01.) und zum Drop (22.04.) beantwortet aber Größenfragen in Echtzeit."""

S2 = """## 2 · Formate, die für Gründer-Modemarken funktionieren

**Ehrlich vorweg:** Belegte Beispiel-Accounts mit Zahlen für genau diese Formate konnte ich in dieser Runde nicht prüfen. Unten stehen nur Marken, deren Vorgehen in markt.md belegt ist. Das sind Belege für die Strategie, nicht für ein bestimmtes Video. Die Lücke schließt du in 30 Minuten selbst (Abschnitt 6, Punkt 2).

| # | Format | Warum es wirkt (Mechanik, Schätzung) | Bauplan | Beleg aus der Recherche | IDs |
|---|---|---|---|---|---|
| 1 | **Build in Public, „Day X“** | Eine Serie gibt einen Grund zum Folgen. Jeder Teil endet offen | Text oben „Day X of building a 100-pair jeans drop“. Ein Fortschritt, eine Zahl, ein nächster Schritt. Tag 1 = Mo 12.10.2026, Tag 193 = Drop | Strategie-Beleg, kein Format-Beleg: Corteiz baut Community vor Reichweite, Passwort-Shop, Guerilla-Events [Q13] | V001, V004, V007, V010, V013, V016 … alle BUILD |
| 2 | **Zahlen offenlegen** | Echte Zahlen schaffen Vertrauen und lösen Kommentare aus („zu teuer“, „zu billig“), beides ist Reichweite | Handschrift auf weißem Papier, Draufsicht, eine Zahl pro Satz. Nur echte Zahlen | kein externer Beleg geprüft. Regel aus dem Plan: nur echte Zahlen | V003, V009, V021, V039, V055, V060, V106, V121 |
| 3 | **Papiertest** | Zeigt deine Regel „erst Design, dann Sample, dann zeigen“. Kein Mitbewerber hat dieses Material | Zeitraffer Ausschneiden → Aufkleben → Spiegel → Makro. Später Match-Cut Papier → Garn | eigenes Material, kein externer Beleg | V001, V029, V093, V119, CD-T03 |
| 4 | **Prozess-ASMR Stickerei** | Ton an, Hände im Bild, kein Text nötig. Läuft ohne Sprache in jedem Land | Makro, Licht von der Seite, Originalton, 8–20 s | Kapital und Story mfg. verkaufen Handarbeit über Nahaufnahmen und den Menschen hinter dem Stich [Q17][Q19]. 85 % der Frauen machen Handarbeit, 18–29 ist die größte Gruppe [Q21] | V006, V016, V019, V031, V057, V118, V124 |
| 5 | **Fabriksuche** | Dramaturgie 8 → 3 → 1. Jeder will wissen, wie man eine Fabrik findet | Strichliste, verpixelte Mails, Kriterien. Namen nur mit Erlaubnis | eigenes Material | V007, V010, V020, V120 |
| 6 | **„Ich zeige dir meinen Fehler“** | Verletzlichkeit gegen Hochglanz. Fehler beweisen, dass du prüfst, bevor jemand zahlt | Vorher → was falsch war → was du änderst. Ein Fehler pro Video | eigenes Material: v1.5 verworfen, Freeze gerutscht, Stickprobe gewaschen | V018, V028, V113, V114 |
| 7 | **Oma-Teppich-Story** | Stärkster emotionaler Auslöser deiner Kernzielgruppe (zielgruppe.md S1). Man schickt es der Schwester oder dem Cousin weiter, also Sends | Familienfoto → Schwenk über den Teppich → Rasterzeichnung → Zipper-Rücken. Subjekt: der Teppich | Wandteppiche hingen in sehr vielen Wohnungen: Wohlstand, Schutz vor Zugluft und Lärm [Q22] (teils schwache Quelle) | V017, V050, V122, CD-T10, CD-T16 |
| 8 | **Ornament-Bedeutung in 15 Sekunden** | Nutzwert, also Saves. Ruhiges Lernformat zwischen lauten Posts | Karussell: Hook → Motiv gezeichnet → Bedeutung → am Teil → Liste | Bode schreibt Produkttexte wie Museumsschilder [Q18]. Heuritech führt „Slavic Chic“ (Stickerei, Rot/Weiß) als Trend [Q20], das Wort nur intern | V002, V005, V011, V014, V015, V108–V112 |
| 9 | **Ein Bild ohne Text** | Ein Dreh, den man in einer Sekunde versteht, geht über Sprachgrenzen | Goldfäden schwingen beim Gehen, 6 s, Loop | Ksenia Schnaiders asymmetrische Jeans ging viral: ein Design-Dreh, den man in einer Sekunde versteht [Q16] | V031, V089, CD-T20, CD-T08 |
| 10 | **Echte Knappheit, Countdown, Early Access** | Käufe kommen am Anfang und am Ende einer Frist [Q12]. Begrenzte Menge wirkt [Q11] | „X von 35“, Nummern 001–100, Countdown-Sticker, Liste um 18:00 | Broken Planet: Passwort-Drop in Sekunden ausverkauft [Q14]. Ljubav (Rin): erster Drop in ca. 30 Minuten weg [Q15] | V035, V047, V054, V060, V090, V095, CD-Serie |

**Was du nicht machst:** gestellte Reaktionen, Fake-Zahlen, „only 3 left“, wenn es nicht stimmt, Renderings vor dem 03.12., fremde Museumsfotos ohne Lizenz, Fabrikbilder ohne Erlaubnis."""

LIB_INTRO = """## 3 · Video-Bibliothek

**Umfang:** {n_total} Video-Konzepte ({n_dated} mit Datum, {n_res} Reserve) und {n_cd} Countdown-Konzepte.
Nach Phase: P1 Prozess {p1} · P2 Ab Proto {p2} · P3 Vorbestellung {p3} · P4 Produktion {p4} · P6 Drop {p6} · Countdown {n_cd} · Reserve {n_res}.
Nach Slot: BUILD {b} · ORIGIN {o} · REAL {re_} · DETAIL {de} · REACH {rh} · ASK {a}.

**Die sechs Slots**

| Slot | Inhalt | Zeit |
|---|---|---|
| BUILD | Fortschritt, Serie „Day X“ | Mo 18:00 |
| ORIGIN | Muster, Bedeutung, Teppich, Herkunft der Idee | Mi 18:00 (ab Proto Di) |
| REAL | Zahlen, Fehler, ehrliche Entscheidungen | Fr 18:00 (im Wechsel mit DETAIL) |
| DETAIL | Makro eines Elements | Fr 18:00 |
| REACH | kurz, Trend-Sound, für Nicht-Follower | Mi 19:00 (ab Proto) |
| ASK | Story mit Umfrage, Frage oder Countdown | Sa 12:00 (ab Proto) |

**So liest du einen Block:** Kopf = ID · Datum Uhrzeit · Slot · Titel. „Hook EN“ steht als Text in den ersten zwei Sekunden und ist dein erster gesprochener Satz. „Test-Hook B“ nimmst du für den Hook-Test (5.5). „Caption EN“ enthält schon CTA und Hashtags. Platzhalter in eckigen Klammern füllst du mit echten Zahlen, nie mit geschätzten. `{{day}}` ist schon eingesetzt: Tag 1 = Mo 12.10.2026.

**Maschinenlesbar:** Jeder Block beginnt mit `#### V…` oder `#### CD-T…`, jedes Feld mit `- **Feldname:**`. Dieselben Daten als JSON in `content_library.json` (Schlüssel `videos` und `countdown`).

**Standard-CTA nach Phase**

| Zeitraum | CTA (EN) | CTA (DE) |
|---|---|---|
| bis 13.01. | Link in bio: join the list. The list buys first, at the pre-order price. | Link in Bio: Trag dich ein. Wer auf der Liste ist, kauft zuerst und zum Vorbestellpreis. |
| 14.01.–21.03. | Pre-order in bio: €149 instead of €169. [Y] of 35 left. | Vorbestellen über den Link in Bio: 149 € statt 169 €. Noch [Y] von 35. |
| 22.03.–21.04. | Drop 22.04., 19:00. The list gets in at 18:00. Link in bio. | Drop 22.04., 19:00. Die Liste kommt um 18:00 rein. Link in Bio. |
| ab 22.04. 19:00 | Live now. Link in bio. | Jetzt live. Link in Bio. |

**Sprache, Abweichung benannt, du entscheidest:** Novalife-Content ist englisch. Die Zielgruppen-Recherche empfiehlt für deine Kernzielgruppe (Ost-Wurzeln, in Deutschland aufgewachsen) Deutsch. Vorschlag: Hook im Bild auf Englisch, in der Caption eine zweite Zeile auf Deutsch. In Woche 7 testest du bei zwei Videos den deutschen Hook als Test-Hook B (5.5)."""

COUNTDOWN_INTRO = """**Vorlage (aus Docket Rev. 5.3, bleibt):** CapCut, 9:16, dunkler Indigo-Grund, oben groß „T−n“, unten „22.04. · 19:00“, in der Mitte ein Clip von 4–6 Sekunden. 18:00 auf TikTok, als Reel und als Story mit Countdown-Sticker [Q8]. Alle 24 werden am Do 18.03. (T−24 bis T−13) und Sa 20.03. (T−12 bis T−1) vorproduziert. An echten Tagen ersetzt ein Live-Clip das Asset (Zeile „Echter Tag“). E-Mails laut Plan: T−14 (08.04.), T−7 (15.04.), T−3 (19.04.), T−24h (21.04.)."""

RESERVE_INTRO = """Reserve heißt: kein fester Termin. Du nimmst sie (a) als Extra-Post, wenn du mehr grinden willst, (b) als Ersatz, wenn ein geplantes Video nicht drehbar ist (Paket kommt später, Fabrik gibt keine Erlaubnis), (c) für Hook-Tests. Pro Woche höchstens zwei Extras, sonst sprengst du deine 1–2 Stunden."""

S4 = """## 4 · Workflow für 1–2 Stunden am Tag

### 4.1 Morgen, Do 08.10.: Papiertest 3 filmen (15 Minuten extra)

Handy hochkant, 4K oder 1080p, Linse putzen, Fensterlicht von der Seite. Jeder Clip 5–10 Sekunden. Ordner `content/archiv/papiertest3`.

| # | Clip | Für |
|---|---|---|
| 1 | Drucker gibt `NVL_Druckvorlage_v17.pdf` aus (Ton) | V001 |
| 2 | Ausschneiden, Draufsicht, als Zeitraffer | V001, V113 |
| 3 | Malerkrepp abreißen (Ton) | V001 |
| 4 | Aufkleben, jedes Element einzeln: A, E, B, B2, C, D | V001, V024, CD-T03 |
| 5 | Lineal am Bein: Serp-Papier bei 40, 45, 50 cm | V119 |
| 6 | Flurspiegel von vorn | V001 |
| 7 | Flurspiegel von hinten | V036-Vorher, V093 |
| 8 | Gehen im Flur, Rückansicht | V093, CD-T03 |
| 9 | Makro Papier an der Taschenkante (A), Finger fährt entlang | V029-Vorher |
| 10 | Münztasche der Eightyfive messen (Lineal im Bild) | V094-Vorher |
| 11 | Dein Gesicht beim Entscheiden, ehrlich | V119 |
| 12 | Gleiche Kameraposition wie Clip 7 und 9 notieren (Klebeband auf dem Boden) | Match-Cuts im März |

Clip 12 ist der wichtigste für später: Mit derselben Position drehst du im März das fertige Teil (V093, CD-T03).

### 4.2 Einmal einrichten: Sa 10.10. (Docket „Profile vorbereiten“, 60–75 Minuten)

1. **Konten:** TikTok als Business-Konto, Instagram als professionelles Konto (Creator oder Business). Damit hast du Insights, und für Werbung ist die Business-Musik die saubere Wahl (UNGEPRÜFT). YouTube-Kanal „Novalife“ für Shorts.
2. **Bio-Link mit Herkunft:** zwei Links auf dieselbe Wartelisten-Seite, `?utm_source=tiktok` und `?utm_source=instagram`. So siehst du in Shopify, woher die Anmeldungen kommen (UNGEPRÜFT: Bericht „Sitzungen nach Quelle“, Name kann abweichen).
3. **Ordner auf dem Mac:** `~/Claude/Novalife/time-travel/content/` mit `W05/`, `W06/` … und darin `raw/`, `edit/`, `final/`. Dazu `archiv/` und `vorlagen/`. Dateinamen: `V001_final.mp4`.
4. **Fünf CapCut-Vorlagen** (Projekt duplizieren statt neu bauen):
   - **T1 Hook:** Text oben im mittleren Drittel, weiß auf dunklem Indigo-Balken, eine Schrift, Größe für 6 Wörter pro Zeile.
   - **T2 Zahlen:** ohne Text-Overlay. Die Zahlen schreibst du von Hand, die Kamera filmt das Papier.
   - **T3 Makro:** nur ein Etikett mit 2–3 Wörtern unten links.
   - **T4 Countdown:** wie in 3.5 beschrieben.
   - **T5 Karussell:** 4:5, Slide 1 Hook groß, Slides 2–n ein Satz pro Slide.
   - **Farben (Vorschlag, deine Entscheidung):** Indigo `#1B2240`, Naturweiß `#F5F2EA`, Rot `#B3262E`, Gold `#C9A24A`. Nie Hellblau mit Gelb kombinieren.
   - **Untertitel:** automatische Untertitel in CapCut (UNGEPRÜFT: Funktionsname kann abweichen), danach jede Zeile Korrektur lesen.
   - **Sicherer Bereich:** Text nicht ins untere Fünftel und nicht an den rechten Rand, dort liegen die App-Knöpfe (Schätzung).
5. **Hook-Bank:** eine Notiz am Handy. Jeder Hook, der dir einfällt, kommt dorthin. Sonntags wählst du daraus.

### 4.3 Sonntag: Batch-Dreh (75–100 Minuten, steht im Docket)

| Minuten | Schritt |
|---|---|
| 0–10 | Bibliothek öffnen, die IDs der kommenden Woche lesen, Shotlisten auf einen Zettel. Requisiten auf den Tisch |
| 10–50 | **Drehen in Ortsreihenfolge, nicht in Videoreihenfolge:** erst alles am Schreibtisch, dann Fenster, dann Spiegel, dann draußen. Pro Shot zwei Takes. Hook-Satz für Version A und B je einmal sprechen |
| 50–85 | **Schneiden in CapCut:** Vorlage duplizieren, Clips rein, Untertitel, Hook-Text. Ohne Musik exportieren, 1080 × 1920 |
| 85–100 | Captions aus der Bibliothek kopieren, Platzhalter füllen. Posts in TikTok und Instagram für die Woche **planen** (beide Apps können Beiträge vorplanen, UNGEPRÜFT wie weit im Voraus) |

**Wenn ein Dreh nicht klappt** (Paket kommt später, Licht schlecht): Reserve-ID nehmen, nicht ausfallen lassen.

### 4.4 Posttag (20 Minuten)

1. **17:55** Ist der geplante Post da? Wenn nicht: hochladen. TikTok: Sound aus der Commercial Music Library leise unter den O-Ton. Instagram: gleiche Datei, Audio aus der App, Titelbild wählen, höchstens 5 Hashtags.
2. **18:00** Live. Reel in die Story teilen, Link-Sticker auf die Warteliste.
3. **18:00–18:15 Antworten:** jeden Kommentar beantworten. Die beste Frage anheften. Eine Frage als Video-Antwort für nächste Woche notieren (V117).
4. **YouTube Shorts:** gleiche Datei, Titel = Hook EN + ein Stichwort. 3 Minuten, darf auch am Sonntag passieren.

### 4.5 Repurposing: eine Datei, drei Plattformen

| Schritt | TikTok | Instagram Reels | YouTube Shorts |
|---|---|---|---|
| Datei | `V0xx_final.mp4` aus CapCut, ohne Musik, ohne Wasserzeichen | dieselbe Datei. **Nie** das TikTok-Download-Video (Wasserzeichen, schwächer empfohlen, UNGEPRÜFT) | dieselbe Datei |
| Ton | CML-Track leise | Audio aus der App, falls verfügbar | Audio-Mediathek oder nur O-Ton |
| Text | Caption EN + 3–5 Hashtags + Stichwort | Caption EN + DE-Zeile + max. 5 Hashtags | Titel: Hook EN |
| Extra | — | Story mit Link-Sticker | — |

**Weiterverwerten:** Gute Makros aus den REACH-Videos werden Countdown-Material. Gute O-Töne aus ORIGIN werden Karussell-Texte. Gute Kommentare werden V117-Antworten.

### 4.6 Die 15 Minuten Antworten: Regeln

- Jede Frage bekommt eine Antwort, auch die kritische.
- **Standard bei „Ist das russisch?“:** „No. This pattern exists in Belarus, Poland, Russia and Ukraine. It belongs to no one alone.“ (DE: „Nein. Das Muster gibt es in Belarus, Polen, Russland und der Ukraine. Es gehört keinem allein.“) Aus zielgruppe.md 3.8.
- **Sofort ausblenden:** Z, V, Georgsband-Emojis, Kriegsverherrlichung, Beleidigungen gegen eine Nation (zielgruppe.md 3.8).
- **Ernst nehmen und zählen:** „Erinnert mich an Sowjetsymbole“ oder „an den Holodomor“. Danken, notieren, im Sonntags-Review zählen. Drei solche Kommentare in einer Woche sind ein Signal für die B2-Farboption aus zielgruppe.md 3.5.
- Nie diskutieren. Nie Kritik löschen.
- **10 Minuten Community an Nicht-Posttagen:** fünf sinnvolle Kommentare bei Accounts aus deiner Nische (Denim, Stickerei, Berliner Streetwear). Kein „nice“ mit Emoji, sondern ein Satz mit Inhalt (Arbeitsregel).

### 4.7 Zeitbudget pro Woche (Schätzung)

| Phase | Batch So | Posttage | Community | Review | Summe Content |
|---|---|---|---|---|---|
| P1 (3 Posts) | 75 min | 3 × 20 min | 4 × 10 min | 15 min | ~3,2 h |
| P2–P4 (4–5 Posts + Story) | 100 min | 5 × 20 min | 2 × 10 min | 15 min | ~4 h |
| Countdown (täglich, vorproduziert) | 0 (Assets am 18. und 20.03.) | 7 × 20 min | — | 15 min | ~2,6 h |

Bei 1–2 Stunden pro Tag (7–14 h pro Woche) bleiben in P1 noch 4–10 Stunden für Fabrik, Tech Pack und Shop.

### 4.8 Drehorte

| Ort | Wofür | Hinweis |
|---|---|---|
| Schreibtisch, Draufsicht | Zahlen, Papier, Zeichnen, Pakete | Handy auf Stativ oder Bücherstapel, Licht von der Seite |
| Fensterbank | Makros, Gold, Stoffe | Gold glänzt nur im Gegenlicht oder Streiflicht |
| Flurspiegel | Ganzkörper | nur von vorn oder hinten (B und B2 nie zusammen) |
| Weiße Wand oder Tür | Hose auf Bügel, 3-m-Totale | |
| Mac-Bildschirm | Mails, Tech Pack, Shopify, Digitizing | Cmd + Shift + 5. Namen verpixeln |
| Familie | Teppich, Fotos | nur mit Einverständnis, keine Sowjet-Deko im Bild |
| Berliner Sticker (Woche 10) | Stickmaschine | nur mit Erlaubnis, vor dem 03.12. kein fertiger Zipper oder Polo im Bild |
| Hinterhof, Treppenhaus | Gehen, Rückansicht | kein Flaggen- oder Monumenthintergrund |
| Tempelhofer Feld bei Sonnenuntergang | Goldfäden, Kampagnenstimmung | Öffnungszeiten vor Ort prüfen. Himmel orange, nie Blau über Gelb [Q27] |
| Mauerpark-Flohmarkt (sonntags) | Straßenfrage V123 | Sekundärquelle, vor Ort prüfen [Q32]. Personen nur mit Einwilligung |
| Vor Overkill, Köpenicker Straße 195A, Kreuzberg | Straßenfrage V123 | Adresse aus Sekundärquelle, vor Ort prüfen [Q31]. Drinnen nur mit Erlaubnis |

**Nicht drehen:** an sowjetischen Ehrenmalen (Treptower Park, Tiergarten). Dort hat die Berliner Polizei zum 8./9. Mai 2025 Flaggen verboten [Q30]. Ebenfalls nicht vor Sowjet- oder DDR-Monumentalarchitektur als Kulisse, nicht vor Flaggen und nicht vor Streifen in Blau-Gelb, Rot-Schwarz, Orange-Schwarz, Rot-Grün oder Weiß-Rot-Weiß [Q29] (zielgruppe.md 3.6)."""

S5 = """## 5 · Messsystem

### 5.1 Eine Tabelle, jeden Sonntag 15 Minuten

Google Sheet oder Numbers, Blatt „Content“. Eine Zeile pro Video und Plattform.

| Spalte | Woher (UNGEPRÜFT, Menünamen können abweichen) |
|---|---|
| ID, Datum, Plattform, Hook-Variante (A/B) | du |
| Views nach 48 h und nach 7 Tagen | TikTok: Video → Analytics · Instagram: Reel → Insights |
| Ø Wiedergabezeit (s) und % ganz angesehen | TikTok Analytics. Instagram zeigt die durchschnittliche Wiedergabezeit, teils auch eine Überspringrate |
| Shares/Sends, Saves, Kommentare | beide Apps |
| Profilaufrufe, neue Follower | beide Apps |
| Link-Klicks | Instagram Story-Insights (Link-Sticker), TikTok Profil-Analytics |
| **Neue Anmeldungen am Tag** | Shopify, nach `utm_source` |

### 5.2 Fünf Kennzahlen, auf die du schaust

| Kennzahl | Formel | Wofür |
|---|---|---|
| **Hook-Rate** | % ganz angesehen (TikTok) bzw. Ø Wiedergabezeit ÷ Länge | Zieht der Anfang? |
| **Teil-Rate** | (Shares + Saves) ÷ Views × 1.000 | Ist es wert, weitergegeben zu werden? |
| **Engagement** | (Likes + Kommentare + Shares + Saves) ÷ Views | Vergleich mit dem Benchmark 4,4 % auf TikTok [Q4] |
| **Anmeldungen je 1.000 Views** | neue Anmeldungen der Woche ÷ Views der Woche × 1.000 | Planwert 2,5 (Schätzung aus markt.md 3.2). Ab So 01.11. durch deine echte Quote ersetzen |
| **Anmeldequote der Wartelisten-Seite** | Anmeldungen ÷ Seitenbesuche (Shopify) | Vergleich: Landingpage-Median 6,6 % über alle Branchen [Q33]. Darunter: Seite prüfen (Vorteil in einem Satz oben, ein Feld, ein Knopf) |

### 5.3 Schwellen

**a) Gegen dich selbst (wichtigste Regel).** Median der letzten 9 Videos je Plattform, rollierend.

| Ergebnis nach 48 h | Einstufung | Was du tust |
|---|---|---|
| Views ≥ 2 × Median **und** Teil-Rate über Median | **Ausreißer** | Innerhalb von 14 Tagen **fünf Varianten** desselben Inhalts: neuer Hook, neues erstes Bild, gleicher Kern (markt.md 3.5) |
| Views 0,5–2 × Median | normal | weiter nach Plan |
| Views < 0,5 × Median | **schwach** | Diagnose 5.4 |
| Drei schwache Videos im selben Slot hintereinander | Slot-Problem | Slot für zwei Wochen durch Reserve-Format ersetzen und Claude die drei Videos zeigen |

**b) Gegen den Markt [Q4][Q5][Q6].** TikTok-Engagement ≥ 4,4 % nach Views (Konten 1.000–5.000 Follower). Reels-Reichweite ≈ 10 % der Follower. Modemarken-Median 0,15 % (Instagram) bzw. 0,95 % (TikTok). Liegt ein Hook-Typ dreimal unter 4,4 %, wechselst du ihn (markt.md 3.7).

**c) Gegen das Ziel (aus markt.md 3.7, jeden Sonntag).**

| Woche | Sonntag | Liste Soll | Alarm | Views pro Woche nötig |
|---|---|---|---|---|
| W5 | 18.10.2026 | 40 | 15 | 16.000 |
| W6 | 25.10. | 90 | 30 | 20.000 |
| W7 | 01.11. **Validierung** | 150 | 50 | 24.000 |
| W8–W11 | 08.–29.11. | +60 pro Woche | 80–170 | 24.000 |
| W12 | 06.12. (Proto) | 470 | 200 | 32.000 |
| W16 | 03.01.2027 | 740 | 300 | 24.000 |
| W18 | 17.01. (Vorbestellung) | 1.000 | 450 | 60.000 |
| W20 | 31.01. (Schwelle ≥ 10) | 1.500 | 600 | 100.000 |
| W24 | 28.02. | 2.400 | 850 | 100.000 |
| W27 | 21.03. (35 Vorbestellungen) | 2.560 | 950 | 24.000 |
| W32 | 25.04. | 3.000 | 1.515 | 32.000 |

Unter „Alarm“: Notfallhebel aus markt.md Abschnitt 5. Die Validierung am So 01.11. bleibt die Plan-Regel: grün ≥ 150, gelb 50–149, rot < 50.

### 5.4 Diagnose bei schwachen Videos

| Befund | Ursache | Maßnahme |
|---|---|---|
| Wenige Views **und** niedrige Hook-Rate | Hook | Drei neue Hooks für denselben Inhalt (5.5). Erstes Bild ändern: Hände oder Gesicht statt Totale |
| Hook-Rate gut, Ø Wiedergabezeit unter der Hälfte | Mitte zu lang | Ein Drittel rausschneiden. Die Zahl oder das Detail nach vorn |
| Wird zu Ende geschaut, aber kaum geteilt oder gespeichert | kein Grund zum Weitergeben | Nutzwert ergänzen („Save this“, Anleitung) oder Sends-Frage („Send this to someone who …“) |
| Gutes Engagement, keine Anmeldungen | CTA | Angeheftete Kommentar-Antwort mit Link-Hinweis. Vorteil schärfer sagen: „first access at 18:00, €20 less“ |
| Viele Views, viele kritische Kommentare | Inhalt trifft einen Nerv | Ruhig antworten (4.6), zählen, nicht löschen. Bei Ernte-, Sichel- oder Sowjet-Assoziationen: zielgruppe.md 3.5 |

### 5.5 Hook-Test-Protokoll

1. **Eine Variable pro Test:** entweder Text-Hook oder erstes Bild oder erster gesprochener Satz. Nie alles gleichzeitig.
2. **Instagram:** Test-Hook B als „Probe-Reel“ (Trial Reel) nur an Nicht-Follower, wenn dein Konto die Funktion hat (UNGEPRÜFT). Nach 48 h vergleichen, Gewinner als normales Reel.
3. **TikTok:** keine geprüfte Split-Test-Funktion. Den Inhalt mit Hook B frühestens nach 7 Tagen neu posten, mit anderem ersten Bild.
4. **Drei Hook-Typen im Wechsel:** Zahl („My budget: €4,500.“), Kontrast oder Fehler („I scrapped it.“), Frage oder POV („Remember it?“). Nach 6 Wochen weißt du, welcher Typ bei dir trägt.
5. **Monats-Review mit Claude** (letzter Sonntag im Monat): die drei besten und die drei schwächsten Videos mit Zahlen. Daraus kommen neue Hooks für die Bibliothek.

### 5.6 Was du Claude jeden Sonntag gibst

Eine Zeile reicht: „W[n]: Liste [X] (+[Y]), Views [Z], bestes Video V0xx ([Views]), schwächstes V0xx ([Views]), Anmeldungen je 1.000 Views [Q], kritische Kommentare [K].“ Damit lassen sich Schwellen und Bibliothek nachziehen."""

S6 = """## 6 · Offene Punkte

1. **Plattform-Fakten 2026 nachprüfen.** In dieser Runde nicht möglich (Suchbudget aufgebraucht, Seitenabruf gesperrt). Mit einer neuen Sitzung prüfen: TikTok-Empfehlungssignale, Mosseris Signale 2025/2026, Instagram-Hashtag-Limit, Reels- und Shorts-Länge, Trial Reels, Commercial Music Library, beste Uhrzeiten DE (Studien von Buffer, Sprout Social, Later o. ä.), Frequenz-Studien. Bis dahin gilt: Plan-Zeiten und eigener Selbsttest ab So 08.11.
2. **Beispiel-Accounts für die Formate fehlen.** Deine 30-Minuten-Aufgabe: In der TikTok-Suche „day 1 of starting a clothing brand“, „building a clothing brand“, „embroidery asmr“, „denim brand behind the scenes“ eingeben. Zehn Videos mit sichtbar vielen Views speichern, Links an Claude. Daraus werden echte Beispiele mit Hook-Analyse.
3. **Startwerte fehlen:** Follower heute auf TikTok und Instagram, Größe der Bleach-Kundenliste, E-Mail-Adressen mit Einwilligung. Ohne sie sind die Wochenziele bis 01.11. grob (so auch markt.md).
4. **Deine Entscheidungen zu den Änderungen am Plan:** Hooks „Älter als jede Grenze“ ersetzen (V002, V030) · Teppich auf 18.11. · Sperrwoche 23.–29.11. · 24.02. → 25.02. · Wörter nach außen („cross-stitch band“, „eight-point star“) · Sprache der Hooks (EN mit DE-Zeile).
5. **Familien-Fakten:** V017, V050 und V122 setzen voraus, dass deine Familie einen Wandteppich hatte und Fotos davon existieren. Nur posten, was stimmt (Docket: Familie befragen, Do 15.10.).
6. **Belegtabelle zur Drei-von-vier-Regel** (Spec Teil 5) muss stehen, bevor V005 läuft.
7. **Serp-Test:** V056 und CD-T06 nur nach dem Diaspora-Test bis 08.11. (zielgruppe.md, Test in 4 Wochen).
8. **Erlaubnisse schriftlich einholen:** Fabrik (Bilder, Name), Digitizer (Bildschirm), Berliner Sticker (Maschine), Shoot-Models (Bildrechte).
9. **Zahlen in V003, V009, V021 mit Rev. 6 abgleichen**, bevor sie gepostet werden. Nach der Digitizing-Vorschau am 09.11. neu rechnen.
10. **CapCut und Musik:** Ob CapCut-Musik und -Vorlagen für Werbung freigegeben sind, ist nicht geprüft. Deshalb Musik nur in der jeweiligen App.
11. **YouTube-Shorts-Nutzung in Deutschland** ist nicht geprüft. Bleibt Zweitverwertung."""

S7 = """## 7 · Quellen

Alle [Q] am 07.10.2026 in dieser Sitzung per Websuche gesehen (Such-Auszüge), von der Markt-Recherche (`markt.md`, „M“) oder der Zielgruppen-Recherche (`zielgruppe.md`, „Z“). Von mir übernommen, nicht erneut geöffnet.

**Nutzung und Plattform-Benchmarks**
- [Q1] (Z Q23) ARD/ZDF-Medienstudie 2025, Media Perspektiven 31/2025: Instagram 77 %, TikTok 50 % wöchentlich bei 14–29. https://www.media-perspektiven.de/fileadmin/user_upload/media-perspektiven/pdf/2025/MP_31_2025_ARD_ZDF-Medienstudie_Social_Media_zwischen_Wachstum_und_Saettigung_Nutzungsmuster_und_Plattformdynamiken_in_Deutschland.pdf
- [Q2] (M Q2) ARD/ZDF-Medienstudie 2025, Zusammenfassungen: 82 % / 52 %. https://onlinemarketing.de/cases/ard-zdf-medienstudie-2025 · https://www.schieb.de/ardzdf-onlinestudie-mehr-video-weniger-text
- [Q3] (Z Q20) Mintel, Germany Gen Z Fashion Shopper 2025. https://store.mintel.com/report/germany-gen-z-fashion-shopper-market-report
- [Q4] (M Q37) Socialinsider, 2026 TikTok Benchmarks. https://www.socialinsider.io/social-media-benchmarks/tiktok
- [Q5] (M Q38) Socialinsider, Instagram Reels statistics. https://socialinsider.io/blog/instagram-reels-statistics/
- [Q6] (M Q39) Rival IQ, 2025 Social Media Industry Benchmark Report. https://www.rivaliq.com/blog/social-media-industry-benchmark-report/
- [Q7] (M Q40) eMarketer zu HypeAuditor, Nano-Creator. https://www.emarketer.com/content/smaller-creators-deliver-efficiency-roi-pressure-mounts
- [Q8] (M Q49) Instagram-Countdown-Sticker. https://www.socialmediaexaminer.com/how-to-use-instagram-countdown-sticker-business/ · https://www.socialmediatoday.com/news/instagram-adds-new-countdown-sticker-to-instagram-stories/544247/
- [Q9] (Z Q62) Instagram-Umfrage-Sticker mit bis zu vier Antworten. https://www.socialmediatoday.com/news/instagram-increases-response-options-in-stories-polls-facilitating-expande/617815 · https://www.schieb.de/754805/umfragen-in-instagram-erstellen
- [Q10] (M Q52) McKinsey, „It's showtime! How live commerce is transforming the shopping experience“. https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/its-showtime-how-live-commerce-is-transforming-the-shopping-experience

**Verhalten bei Drops**
- [Q11] (M Q48) Aggarwal, Jun, Huh (2011), Scarcity messages, Journal of Advertising 40(3). https://experts.umn.edu/en/publications/scarcity-messages-a-consumer-competition-perspective/
- [Q12] (M Q31) Kuppuswamy/Bayus, U-förmiger Verlauf bei Kickstarter. https://yannigroth.com/2013/02/24/the-dynamics-of-backer-support-in-crowdfunding-findings-from-kickstarter · https://arxiv.org/pdf/1607.06839

**Marken als Beispiele**
- [Q13] (M Q17) Corteiz. https://www.euronews.com/2023/03/17/the-rise-of-corteiz-inside-the-genius-marketing-strategies-of-londons-hottest-streetwear-b · https://www.complex.com/style/corteiz-streetwear-everything-to-know · https://www.theculturecrypt.com/posts/inside-corteizs-99p-store
- [Q14] (M Q18) Broken Planet, Valentins-Drop. https://www.complex.com/style/broken-planet-valentines-drop
- [Q15] (M Q21) Ljubav (Rin), FashionUnited 2021. https://fashionunited.de/nachrichten/mode/vom-rapper-zum-modemacher-was-rin-mit-seinen-label-vorhat/2021071641948
- [Q16] (M Q12) Ksenia Schnaider. https://fashionunited.uk/news/fashion/viral-denim-designer-ksenia-schnaider-launches-menswear-line/2019032842436 · https://www.upi.com/Asymmetric-Jeans-turning-heads-online/3241547661505/
- [Q17] (M Q6) Kapital. https://bdgastore.com/products/14oz-denim-kountry-motocross-pants · https://www.epitomeofedinburgh.com/collections/kapital
- [Q18] (M Q7) Bode. https://bdgastore.com/products/embroidered-denim-knolly-brook-trouser-mrs24bt039
- [Q19] (M Q10) Story mfg. bei END. https://www.endclothing.com/nl/brands/story-mfg
- [Q20] (M Q3) Heuritech, „Slavic Fashion: Heritage Craft Meets Modern Chic“. https://heuritech.com/articles/slavic-chic-fashion/
- [Q21] (Z Q24) t-online zur Studie der Initiative Handarbeit: 85 % der Frauen machen Handarbeit, 18–29 größte Gruppe. https://www.t-online.de/leben/aktuelles/id_100586036/stricken-und-haekeln-trendet-auf-social-media-das-ist-der-grund.html

**Symbole, Sprache, Sensibilität**
- [Q22] (Z Q40) Wandteppiche: The Moscow Times, „Gankevich's Magic Carpets“ (2014). https://www.themoscowtimes.com/2014/02/23/gankevichs-magic-carpets-take-viewers-back-to-the-ussr-a32171 · schwache Zusatzquelle: https://homehub.decorexpro.com/en/idei-dlya-doma/zachem-veshali-kovry-na-stenu
- [Q23] (Z Q39) Rodnovery und Politik, Alatyr. https://en.wikipedia.org/wiki/Slavic_Native_Faith_and_politics · https://theconversation.com/from-nordic-symbols-to-sledgehammer-executions-inside-the-wagner-groups-neo-pagan-rituals-213127
- [Q24] (Z Q32) Vyshyvanka Day. https://en.wikipedia.org/wiki/Vyshyvanka_Day · https://cjir.iir.cz/index.php/cjir/article/view/776
- [Q25] (Z Q42) „On the Historical Unity of Russians and Ukrainians“. https://en.wikipedia.org/wiki/On_the_Historical_Unity_of_Russians_and_Ukrainians
- [Q26] (Z Q51) Holodomor: „Gesetz über fünf Ähren“, Gedenktag 4. Samstag im November. https://holodomormuseum.org.ua/en/news-museji/the-law-on-five-ears-of-grain-is-a-bloody-tool-of-the-holodomor-organizers/ · https://www.ukrainianworldcongress.org/november-marks-month-of-remembrance-for-holodomor-victims/ · https://www.bundestag.de/dokumente/textarchiv/2022/kw48-de-holodomor-923060
- [Q27] (Z Q50) Kyiv Independent, Flagge als Himmel über Weizen. https://kyivindependent.com/everything-you-didnt-know-about-ukraines-flag/
- [Q28] (Z Q34, Q35) Staatswappen Belarus und Sowjetunion. https://en.wikipedia.org/wiki/National_emblem_of_Belarus · https://en.wikipedia.org/wiki/State_Emblem_of_the_Soviet_Union
- [Q29] (Z Q33) Flagge von Belarus, Weiß-Rot-Weiß. https://en.wikipedia.org/wiki/Flag_of_Belarus · https://balticworlds.com/the-flag-revolution-understanding-the-political-symbols-of-belarus/
- [Q30] (Z Q38) Polizei Berlin, Flaggenverbote an sowjetischen Ehrenmalen 8./9. Mai 2025. https://www.berlin.de/polizei/polizeimeldungen/2025/pressemitteilung.1558188.php · https://taz.de/Gedenken-zum-8-und-9-Mai-in-Berlin/!6176834/

**Orte**
- [Q31] (Z Q56) Overkill, Köpenicker Straße 195A (Sekundärquelle). https://www.sneakerjagers.com/en/n/sneaker-touring-the-15-best-sneaker-shops-in-berlin/23388
- [Q32] (Z Q58) Mauerpark-Flohmarkt (Sekundärquellen). https://berlinecho.de/flohmarkt-mauerpark-oeffnungszeiten-berlin/ · https://www.top10berlin.de/en/cat/shopping-261/flea-markets-and-jumble-sales-1587/mauerpark-flea-market-1182

**Konversion**
- [Q33] (M Q36) Unbounce, Conversion Benchmark Report: Landingpage-Median 6,6 %. https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/

**Versucht, aber am 07.10.2026 vom Netzwerk-Proxy blockiert (nicht gesehen, nicht gezählt):** support.tiktok.com („How TikTok recommends content“), newsroom.tiktok.com („How TikTok recommends videos #ForYou“), about.instagram.com („Instagram Ranking Explained“), blog.youtube, buffer.com („Best time to post on TikTok“).

**Interne Grundlagen:** `docs/time-travel-drop-plan.md` (Rev. 5.3), `docs/produkt-spec_rev13.md`, `docs/uebergabe-time-travel.md`, `r5/weeks_r5.json` (Docket Rev. 5.3), `rev6/research/markt.md`, `rev6/research/zielgruppe.md`."""
