# Docket Rev. 8 (veröffentlicht Fr 30.10.2026)

Live: https://claude.ai/artifact/RCciF8jMPSGhgdcQiHAQTm (Version 38). Kopie der Seite: `../artefakte/docket_rev8/`.

Neu geplant nach Ernests Antworten vom 30.10.: öffentlich ab dem ersten Proto (erster Post Di 15.12.), Drop Do 24.06.2027 19:00, Vorbestellung ab Mo 15.02., 3–5 Stunden pro Woche bis zum Abi.
Reihenfolge wie am 17.10. besprochen: erst Design und Fabrik bis zur Muster-Freigabe (Fr 15.01.), dann Gewerbe, Recht und Shop parallel zum Marketing.

## Bauen

`python3 build8.py <ausgabe.html>` schreibt die Seite. `node test8.js` prüft sie in Chromium (erwartet die Seite als `time_travel_docket_rev8.html` und einen Abzug der Datenbank unter `db/progress/`).

## Dateien

- `plan8.py`: alle Aufgaben, Wochenziele, Zahlen (Ziele und Alarm), Erledigtes, offene Fragen
- `content8.py`: 60 Posts mit Terminen, übernommen aus den Rev.-7-Briefings (`vids7_sel.json`), angepasste Daten und CTAs; erzeugt Dreh- und Post-Aufgaben
- `mails8.py`: 19 Mails aus Rev. 7 (`mails7.json`) mit neuen Terminen
- `lib8.py`: Tage, Links, Aufgaben-Bausteine
- `build8.py`, `docket8.css`, `docket8.js`: die Seite
- `old_done.json`: die 43 Häkchen aus dem alten Docket, im Abschnitt „Erledigt“ erhalten

Häkchen liegen in der Datenbank des Artefakts (`progress/tasks`), Zahlen in `progress/kpi`. Neue Aufgaben haben IDs `r8-…`.
