# Übernahme-Check · 07.10.2026 (neue Sitzung)

Die Übergabe `docs/uebergabe-time-travel.md` ist gelesen, dazu Plan und Spec Rev. 13. Danach wurde geprüft:

| Punkt | Ergebnis |
|---|---|
| Docket-Artifact `RCciF8jMPSGhgdcQiHAQTm` | erreichbar, Rev. 5.3. Live-Inhalt = `r5/docket_r5.html` (nur der Publish-Rahmen unterscheidet sich) |
| `r5/build_r5.py` | läuft und erzeugt `weeks_r5.json` byte-gleich zum ZIP-Stand |
| `r5/gen5.py` | bricht ab: liest die Live-Docket-HTML von einem festen Pfad der alten Sitzung (`/root/.claude/projects/-home-claude/.../artifact-c3fa845d-1790504268-2688.html`). Vor dem nächsten Lauf das Artifact neu lesen und den Pfad in `gen5.py` auf die frische Datei setzen |
| Canvas-Artifact `Gi437A61nuWNvgLw98kMwz` | erreichbar. **Live weicht vom ZIP ab:** neues Board `project/Artboard-9ah3.dc.html`, `Rueckansicht.dc.html` 26 Bytes anders. Vor jedem Veröffentlichen die Live-Dateien lesen, nicht die ZIP-Kopie hochladen |
| Skripte in `design/` | vorhanden (v16.py, v17.py, wheat3.py, fine.py, build17.py, print17.py). `.mjs`-Skripte enthalten noch den Chromium-Pfad der alten Sitzung, hier wäre es `/opt/pw-browsers/chromium` |

Nächster Termin laut Plan: **Do 08.10. Papiertest 3**, Fr 09.10. Freeze.
