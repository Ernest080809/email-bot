# Time Travel · Arbeitsdateien (Stand 07.10.2026, Design v1.7)

Diese Dateien braucht Claude, um Canvas, Docket und Druckvorlagen weiterzubauen.
Die Übergabe steht im Projekt „novalife time travel“ in `uebergabe-time-travel.md`.

- `design/` Motive und Druckvorlagen (Python + Node/Playwright). Wichtig: v16.py, v17.py, wheat3.py, fine.py, build17.py, print17.py
- `r5/` Docket-Generator: build_r5.py → weeks_r5.json, gen5.py → docket_r5.html
- `fitcanvas/project/` aktueller Stand der Canvas-Dateien, patch*.py die Änderungsschritte
- `live_weeks_r41.json` wird von r5/r5_a.py gebraucht (eine Ebene über r5/)
- `docs/` Kopien von Plan, Spec und Übergabe
- `pdf/` Druckvorlagen und Bilder

Neu einrichten: Python 3, Node 18+, `npm install playwright` im Ordner, Chromium von Playwright.
In den .mjs-Skripten steht der Chromium-Pfad der alten Cloud-Sitzung, den Pfad bei Bedarf anpassen.
