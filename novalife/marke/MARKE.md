# Novalife · Marke

**Stand 07.11.2026, entschieden von Ernest.** Diese Datei gilt für alles, wo man Novalife sieht: Posts, Videos, Website, Shop, Hangtag, Karte, Verpackung, Mails, Präsentationen. Wer etwas Sichtbares für Novalife macht, hält sich daran. Abweichungen gibt es nur mit Ernests Ja.

**Die Idee in einem Satz:** Die Marke trägt die Farben ihres Garns: Rot, Gold und Weiß aus der Stickerei, Leinen vom Patch, dunkel wie der Teppich bei Nacht. Das Zeichen ist der Achtstern von der Gesäßtasche.

Übersicht als Bild: `markenblatt.png`. Alles neu erzeugen: `python3 marke.py` (braucht `fonttools` und Playwright).

---

## 1. Zeichen: der Achtstern

- **Form:** Achtstern C der Jeans: 8 Rauten mit der 45°-Spitze in der Mitte, schmale Fugen dazwischen (Fuge = 4,5 % der Breite). Immer dieselbe Form, nie neu zeichnen. Quelle: `time-travel/design/fine.py` → `star8_rhombi`.
- **Name nach außen:** „Achtstern“, englisch „eight-point star“. Nie „Alatyr“.
- **Farbe des Sterns:** Rot auf Leinen, Gold auf Teppich-Schwarz, Garn-Weiß auf Fotos, Dunkelbraun als Stempel. Immer einfarbig und gefüllt.
- **Schutzraum:** rundum ein Viertel der Sternbreite frei. **Mindestgröße:** 8 mm im Druck, 24 px am Bildschirm.
- **Wo er steht:** Profilbild auf allen Kanälen, Endkarte jedes Videos, Website-Kopf und Favicon, Hangtag, Stempel auf dem Karton, Mails, Zipper.
- **Der Baum bleibt Motiv, nicht Logo:** roter Kreuzstich-Baum auf der Polo-Brust, Lebensbaum mit „NL“ auf Patch D.

| Datei in `logo/` | Wofür |
| --- | --- |
| `achtstern_rot.svg`, `_gold`, `_weiss`, `_braun` | Stern allein |
| `novalife_quer_dunkel.svg`, `_hell` (+ `_transparent`) | Stern links, NOVALIFE rechts: Website-Kopf, Mail, Rechnung |
| `novalife_hoch_dunkel.svg`, `_hell` | Stern über NOVALIFE: Hangtag, Endkarte, Karton |
| `profilbild.svg` / `.png` (1080 × 1080) | Gold auf Teppich-Schwarz: Instagram, TikTok, YouTube |

Die Wortmarke ist „NOVALIFE“ in Cinzel 600, Sperrung 0,12 em, als Pfade gesetzt.

## 2. Farben

| Name | Hex (Bildschirm) | Pantone TCX (Garn, Druck) | Rolle |
| --- | --- | --- | --- |
| Teppich-Schwarz | `#1A1416` | – | Grund dunkel |
| Leinen | `#E8DCC6` | – | Grund hell, Text auf dunkel |
| Knallrot | `#CD212A` | 18-1662 | Achtstern, Knöpfe, große Zahlen |
| Gold | `#D8AE47` | 14-0952 | Nummern, Linien, kleine Akzente auf dunkel |
| Garn-Weiß | `#F4EFE6` | 11-0602 | Text und Stern auf Fotos |
| Dunkelbraun | `#56352D` | 19-1432 | Text auf hell, Stempel |
| Kupfer | `#A3623B` | 17-1340 | Nebenfarbe auf hell, nur groß |

- **Dunkel für Bildschirme** (Posts, Videos, Website): Grund Teppich-Schwarz, Text Leinen oder Garn-Weiß, Akzente Rot und Gold.
- **Hell für Papier** (Hangtag, Karte, Verpackung, Rechnung): Grund Leinen oder Naturpapier, Text Dunkelbraun, Stern Rot.
- **Mengen:** rund 70 % Grund, 20 % Text, 10 % Rot und Gold zusammen. Rot ist nie eine Fläche, also kein roter Hintergrund.
- **Hex ist der Bildschirmwert.** Bei Garn und Druck zählt der Pantone-Code und am Ende der echte Garnton.
- **Fotos:** warmes Licht. Das einzige Blau ist der Denim selbst.
- Für Websites und Tools: `farben.css` (CSS-Variablen `--nl-…`) und `farben.gpl` (Palette für GIMP, Aseprite, Krita).

**Kontrast (WCAG):**

| Text auf Grund | Kontrast | Erlaubt für |
| --- | --- | --- |
| Garn-Weiß auf Teppich-Schwarz | 15,9 : 1 | jeden Text |
| Leinen auf Teppich-Schwarz | 13,4 : 1 | jeden Text |
| Gold auf Teppich-Schwarz | 8,7 : 1 | jeden Text |
| Dunkelbraun auf Leinen | 8,0 : 1 | jeden Text |
| Knallrot auf Leinen | 4,0 : 1 | nur große Schrift (ab 24 px oder 18 px fett) |
| Kupfer auf Leinen | 3,5 : 1 | nur große Schrift |
| Knallrot auf Teppich-Schwarz | 3,3 : 1 | nur große Schrift |
| Gold auf Leinen | 1,5 : 1 | nie für Text, nur Flächen und Linien |

## 3. Schrift

- **Cinzel SemiBold (600):** Überschriften, Wortmarke, Endkarten. Nur Großbuchstaben, Sperrung 0,1 bis 0,14 em. Nie für Fließtext.
- **Inter Regular (400) und SemiBold (600):** alles andere: Fließtext, Untertitel, Preise, Nummern, Website, Mails.
- Beide sind kostenlos (Google Fonts, SIL Open Font License). Die Dateien und Lizenzen liegen in `fonts/`.
- In Apps ohne eigene Schriften (Texttool in TikTok oder Instagram): für Überschriften die schlichteste Serifenschrift in Großbuchstaben, für Text die Standardschrift. Besser: Text im Schnittprogramm mit Cinzel und Inter setzen, wenn es eigene Schriften laden kann.

## 4. Bausteine, die immer gleich aussehen

- **Nummer:** „N° 001 / 100“ in Inter, Gold auf dunkel, Dunkelbraun auf hell.
- **Datum:** „24.06.2027“, auf Englisch „24 June 2027“.
- **Endkarte jedes Videos:** Teppich-Schwarz, Achtstern in Gold in der Mitte, darunter „TIME TRAVEL“ in Cinzel (Leinen), darunter Datum oder Code-Wort in Inter (Gold).
- **Post mit Text:** wie die Beispiele im Markenblatt: Stern oben, Überschrift in Cinzel, eine Zeile in Inter, klein „NOVALIFE“ unten.
- **Untertitel in Videos:** Inter SemiBold, Garn-Weiß.

## 5. Sprache (gilt weiter)

- Das Subjekt ist das Muster, nicht die Menschen. Kein „wir“ als Volk.
- Nie „authentisch“. Den Lebensbaum nie „slawisch“ nennen. Keine Politik.
- Englischer Hook, dazu eine deutsche Zeile.

## 6. Nie

- Achtstern auf rotem Grund, neben Ähren als Emblem, mit 5 oder 6 Zacken, verzerrt, gedreht, nur als Umriss, mit Schatten oder Verlauf.
- Flaggen-Paare: Hellblau mit Gelb, Weiß-Blau-Rot zusammen.
- Andere Schriften, andere Rot- oder Goldtöne.
- Der Baum als Logo.
