# Docket Rev. 7 (veröffentlicht Mi 28.10.2026)

Live: https://claude.ai/artifact/RCciF8jMPSGhgdcQiHAQTm (Version 37). Kopie der Seite: `../artefakte/docket_rev7/`.

Zum Lesen in anderen Chats: `export/` mit Tagesplan, Content-Plan, Mails, Design-Inventur und Cockpit als Markdown.

## Bauen

`python3 build7.py` setzt die Seite aus Docket v35 (`../artefakte/docket_v35/`) und den Datenmodulen zusammen und schreibt `../docket7/time_travel_docket.html`.
`python3 export7.py export` schreibt die Markdown-Dateien. `test7.js` prüft die Seite in Chromium (Pfade anpassen).

## Module

- `lib7.py`: Bausteine (alte Aufgabe übernehmen, neue anlegen, IDs prüfen)
- `weeks_d.py`: W7–W11, Design-Suche und Design fertig (26.10.–29.11.)
- `weeks_m.py`: W12–W20, Marketing, Recht, Muster (30.11.–31.01.)
- `weeks_px.py`: W21–W41, Vorbestellung, Produktion, Abi-Pause, Countdown, Drop
- `clib.py`, `c_w12_16.py`, `c_w17_21.py`, `c_w22_27.py`, `c_w35_41.py`, `c_rewind.py`: Briefings für Videos, Storys, REWIND und Countdown
- `enrich7.py`: nachgeschärfte Briefings · `mails.py`: Mails E00–E21 · `inventur7.py`: Design-Inventur · `kpi7.py`: Cockpit
- `data7.py`: setzt alle Wochen zusammen, erzeugt die Dreh- und Postaufgaben aus dem Content-Plan, prüft, dass jede v35-Aufgabe ab W7 übernommen, gestrichen oder ersetzt ist
- `fix7.py`: korrigiert alte Termine in übernommenen Aufgaben (jede Ersetzung muss treffen)
- `build7.py`, `docket7.js`, `docket7_sections.js`, `docket7.css`: die Seite
- `weeks_v35.json`, `kpi_v35.json`, `tasks_v35.txt`, `keys_v35.txt`, `sec_head.txt`, `sec_design.txt`: aus Docket v35 gezogene Daten

Häkchen: Aufgaben ab W7 haben feste IDs, W1–W6 behalten ihre alten Positionsschlüssel. So bleiben alle 29 Häkchen aus v35 erhalten.
