# Docket Rev. 7 · Entwurf (Stand 27.10.2026)

Unfertig und nicht veröffentlicht. Nicht als Plan verwenden.

Python-Datenmodule, aus denen Claude den neuen Docket baut. Sie lesen `weeks_v35.json` (die Aufgaben aus Docket v35) und übernehmen alte Aufgaben mit stabiler ID, streichen sie mit Begründung oder legen neue an.

- `lib7.py`: Bausteine (alte Aufgabe übernehmen, neue anlegen, IDs prüfen)
- `weeks_d.py`: W7–W11, Design-Suche und Design fertig (26.10.–29.11.)
- `weeks_m.py`: W12–W20, Marketing, Recht, Muster (30.11.–31.01.)
- `weeks_px.py`: W21–W41, Vorbestellung, Produktion, Abi-Pause, Countdown, Drop
- `clib.py`, `c_w12_16.py`, `c_w17_21.py`, `c_w22_27.py`, `c_w35_41.py`, `c_rewind.py`: Briefings für Videos, Storys und den Countdown
- `mails.py`: Mails E00–E21 mit vollem Text
- `inventur7.py`: Design-Inventur, `kpi7.py`: Zahlen-Cockpit
- `weeks_v35.json`, `kpi_v35.json`, `tasks_v35.txt`, `keys_v35.txt`, `sec_head.txt`, `sec_design.txt`: aus Docket v35 gezogene Daten
