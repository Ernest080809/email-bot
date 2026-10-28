# -*- coding: utf-8 -*-
"""Docket Rev. 7, Teil 2: die Seite v35 umbauen und mit den neuen Daten füllen. Jede Ersetzung muss genau einmal treffen."""
import datetime, html, json, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data7 as DT
import lib7, clib, mails, kpi7, inventur7

SRC = next(p for p in (os.path.join(HERE, '..', 'docket', 'time_travel_docket.html'),                     # Scratchpad
                       os.path.join(HERE, '..', 'artefakte', 'docket_v35', 'Time_Travel_Drop_Docket_v35.html'))  # Repository
           if os.path.exists(p))
OUTD = os.path.join(HERE, '..', 'docket7')
os.makedirs(OUTD, exist_ok=True)
OUT = os.path.join(OUTD, 'time_travel_docket.html')
E = html.escape
s = open(SRC, encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, f"{c}× statt {n}×: {a[:90]}"
    s = s.replace(a, b)


def rep_between(start, end, new, include_end=True):
    """Ersetzt von start bis end (end ab start gesucht)."""
    global s
    assert s.count(start) == 1, f"Start {s.count(start)}×: {start[:80]}"
    i = s.index(start)
    j = s.index(end, i) + (len(end) if include_end else 0)
    s = s[:i] + new + s[j:]


def js(x):
    return json.dumps(x, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')


dl = lib7.dlabel

# ---------- Zahlen ----------
TASKS = [(w, di, t) for w, di, t in DT.ALL if t.get('c') != 'N']
NT = len(TASKS)
rows = []
for w in DT.WEEKS:
    if w['n'] < 7:
        continue
    for di, day in enumerate(w['days']):
        iso = DT.date_of(w, di)
        core = sum(t.get('m', 0) for t in day if t.get('c') != 'N' and not t.get('plus') and t.get('x') != 's')
        rows.append((iso, core))
cores = [c for iso, c in rows if not ("2027-03-22" <= iso <= "2027-05-09")]
AVG = int(round(statistics.mean(cores) / 5.0) * 5)
NLONG = sum(1 for c in cores if c > 120)
PLUSH = round(sum(t.get('m', 0) for w, _, t in TASKS if t.get('plus') and w['n'] >= 7) / 60)
SCHED = sorted(clib.SCHED, key=lambda x: (x['post'][0], x['post'][1]))
N_CD = sum(1 for x in SCHED if x['id'].startswith('CD-'))
N_RW = sum(1 for x in SCHED if x['kind'] == 'rewind')
N_ST = sum(1 for x in SCHED if x['kind'] == 'story')
N_VID = sum(1 for x in SCHED if x['kind'] in ('video', 'karussell', 'live') and not x['id'].startswith('CD-'))
N_PLUS = sum(1 for x in SCHED if x.get('plus'))
N_MAIL = len(mails.M)

# ---------- Kopf, Leiste, Legende ----------
rep('<span class="eyebrow">Drop Docket · Rev. 6 · 08.10.2026</span>', '<span class="eyebrow">Drop Docket · Rev. 7 · 28.10.2026</span>')
rep('<a href="#cockpit">Cockpit</a><a href="#urteil">Urteil</a><a href="#zielgruppe">Zielgruppe</a><a href="#design">Design</a><a href="#referenz">Referenz</a>',
    '<a href="#cockpit">Cockpit</a><a href="#urteil">Urteil</a><a href="#inventur">Inventur</a><a href="#contentplan">Content</a><a href="#mails">Mails</a><a href="#zielgruppe">Zielgruppe</a><a href="#design">Design</a><a href="#referenz">Referenz</a>')
rep('Ganzer Plan bis zum Drop: 794 Aufgaben in 41 Wochen ↓', f'Ganzer Plan bis zum Drop: {NT} Aufgaben in 41 Wochen ↓')
rep('<span><span class="tg B">BUILD</span>Produkt, Fabrik, Sample</span>',
    '<span><span class="tg G">DESIGN</span>Designs suchen und festlegen</span>\n  <span><span class="tg B">BUILD</span>Produkt, Fabrik, Muster</span>')
rep('<span><span class="tg A">ADMIN</span>Shop, Recht, Steuer, Versand</span>',
    '<span><span class="tg A">ADMIN</span>Shop, Versand, Organisation</span>\n  <span><span class="tg R">RECHT</span>Gewerbe, Steuer, Rechtstexte</span>\n  <span><span class="tg W">WEBSITE</span>Bauschritte der Seite</span>')
rep('41 Wochen, 794 Aufgaben. Die laufende Woche ist offen. „So geht’s“ zeigt Schritte, Orte, Links und Video-Briefing.',
    f'41 Wochen, {NT} Aufgaben. W1–W6 sind das Archiv mit deinen Häkchen. Die laufende Woche ist offen. „So geht’s“ zeigt Schritte, Links, Prompts und das volle Briefing für Videos, Storys und Mails.')
rep('placeholder="Suchen: Fabrik, Mauerpark, V014, Shopify …"', 'placeholder="Suchen: Fabrik, Teppich, V214, E07, Shopify …"')

# ---------- Cockpit ----------
rep('<span class="note">Jeden Sonntag drei Zahlen eintragen. Das Cockpit sagt dir, ob du im Plan bist und was du sonst tust.</span>',
    '<span class="note">Ab So 06.12. jeden Sonntag die Zahlen eintragen. Das Cockpit sagt dir, ob du im Plan bist und was du sonst tust.</span>')
rep_between('<p class="intro">Die Ziele sind die Wochenwerte aus der Strategie', '</p>',
            '<p class="intro">Die Ziele sind die Wochenwerte aus Rev. 7, in Klammern der Alarmwert. Bis zum Design-Gate am So 29.11. stehen hier nur die Prüfpunkte. '
            'Am So 29.11. trägst du die Startwerte ein, ab So 06.12. jeden Sonntagabend die echten Zahlen: bestätigte Warteliste (Shopify → Kunden, „E-Mail-Marketing: abonniert“), '
            'Follower TikTok und Instagram zusammen als Gesamtzahl (die Seite zieht den Startwert ab), Zusagen aus dem Blatt „Die ersten 35“ (nur Spalte „Zusage“), bezahlte Jeans-Bestellungen. '
            '<b>Grün</b>: alles im Soll. <b>Gelb</b>: unter Soll, aber über Alarm, dann greifen die Gegenmaßnahmen. <b>Rot</b>: unter Alarm.</p>')

# ---------- Urteil ----------
rep('<div class="s">Schätzung, echte Stichzahl am 09.11. · Zipper nach Angebot (eigener Schnitt) · Polo ~19 € (Plan)</div>',
    '<div class="s">Schätzung, echte Stichzahl mit dem Digitizing am Fr 13.11. · Zipper nach Angebot (eigener Schnitt) · Polo ~19 € (Plan)</div>')
rep('<div class="s">bestätigte Adressen bis 24.06. · 150 bis 01.11. · 1.500 bis 07.02.</div>',
    '<div class="s">bestätigte Adressen bis 24.06. · 250 bis 20.12. · 1.100 bis 07.02.</div>')

REV7 = f'''<div class="callout">
  <span class="eyebrow">Entscheidung Di 27.10. · Rev. 7: erst Design, dann Marketing und Recht, Website parallel</span>
  <p><b>Deine Reihenfolge:</b> Zuerst suchst du jedes Design, das noch fehlt. Bis So 29.11. ist jedes Teil fertig und hat eine gültige Datei. Ab Mo 30.11. starten Marketing und das Rechtliche, die Website läuft nebenher. Jedes Video, jede Story und jede Mail hat ein volles Briefing.</p>
  <ul>
    <li><b>Design-Suche, W7 (26.10.–01.11.):</b> fünf Boards (Etiketten · Hangtag, Karte, Verpackung · Polo · Website- und Content-Look · Zipper-Zubehör und Marke), Herkunft des Baum-Bildes, Bestandsaufnahme W5/W6, Kuzgunlar-Call.</li>
    <li><b>Design fertig, W8–W11 (02.–29.11.):</b> Zipper-Papiertest Mo 02.11. · Jeansfabrik wählen Di 03.11. (ohne schriftlichen Preis Fr 06.11.) · Entwicklung bezahlen Do 05.11. · Digitizing bis 28.000 Stiche Fr 13.11. · Zipper-Fabrik, Preis und Schwelle Mo 16.11. · Polo-Weg Di 17.11. · Website- und Content-Look Mi 18.11. · Gate Stickproben Di 24.11. · Design-Gate So 29.11.</li>
    <li><b>Marketing, Recht und Muster, W12–W20 (30.11.–31.01.):</b> erster Post Mo 30.11. · Gewerbe Mo 07.12. · Proto Di 08.12. · Steuer-Fragebogen Do 10.12. · Shopify Payments Di 15.12. · Stick-Abend Fr 18.12. · Validierung So 20.12. · Website Stufe 1 Do 31.12. · LUCID Mo 04.01. · Rechtstexte Di 05.01. · Sample-Gate Fr 15.01.</li>
    <li><b>Bleibt:</b> Vorbestellung Mo 01.02., 19:00 · Schwelle Mo 15.02. · Bestellung Mi 17.02. · Anzahlung Do 18.02. · Shoot Sa 06.03. · Abi-Pause 22.03.–09.05. · Drop Do 24.06., 19:00.</li>
  </ul>
  <p><b>Was es kostet:</b> Öffentlich gepostet wird erst ab dem 30.11., Rev. 6 hatte mit dem 12.10. gerechnet. Bis zur Vorbestellung bleiben neun statt sechzehn Wochen. Das Cockpit rechnet deshalb am So 07.02. mit 1.100 statt 1.500 bestätigten Adressen, und die 35 Vorbestellungen werden enger. Außerdem zahlst du die Entwicklung (Do 05.11.) vor der Validierung (So 20.12.). Darum fließt bis zur Schwelle am 15.02. nur Geld für Entwicklung, Proto und Proben. Die Anzahlung für die Serie kommt erst danach.</p>
  <p><b>Was du gewinnst:</b> Du zeigst nur Designs, die feststehen, und musst nichts zurücknehmen. Recht und Website liegen im Dezember statt alle im Januar neben der Schule. Das Material für die ersten Content-Wochen entsteht schon jetzt: Jede Design-Aufgabe sagt dir, was du nebenbei für den Vorrat filmst.</p>
  <p><b>Der Dezember wird der härteste Monat:</b> Proto, Gewerbe, Steuer, Zahlungen, Stick-Abend, Validierung und jeden Tag Content. An Wochenenden mit Drehs sind es oft zwei bis vier Stunden. Wenn ein Tag nicht geht, rückst du die Drehs auf den nächsten freien Tag vor dem Posttermin, nie die Fabrik-Aufgaben.</p>
</div>
<div class="callout">
  <span class="eyebrow">Entscheidungen Sa 24.10. bis Mo 26.10. · Zipper-Design</span>
  <ul>
    <li><b>Teppich:</b> Variante A „wie bei Oma“, Größe M 25 × 17,5 cm. Der Papiertest prüft dazu S 21 × 14,7 und L 29 × 20,3 cm.</li>
    <li><b>Rückendruck:</b> Weg 1, die Fläche, als echter Abdruck deiner RL-Kapuze. Band A sitzt oben am Hals, Muster E füllt den Abdruck bis in die Spitze, rote Kante, etwa 22 × 25 cm. Der echte Umriss kommt aus deiner Abpausung.</li>
    <li><b>Passform:</b> Brust 60 cm in M (dein RL hat 57), Schulter 2 cm pro Seite tiefer, die Saumrippe zieht zusammen wie beim RL, Oberarm 22,5 cm. Die Maßtabelle S–XL steht im Zipper-Briefing.</li>
  </ul>
  <p><b>Noch offen:</b> Gewicht und Material vom RL-Etikett, ein Foto der Taschenart und ob die Kordeln über dem Teppich hängen dürfen.</p>
</div>
'''
rep('<div class="callout">\n  <span class="eyebrow">Entscheidung Fr 23.10. · Zipper: eigener Schnitt, vorbestellbar</span>',
    REV7 + '<div class="callout">\n  <span class="eyebrow">Entscheidung Fr 23.10. · Zipper: eigener Schnitt, vorbestellbar</span>')
rep('Alles Weitere steht im Briefing <code>rev6/research/zipper_briefing.md</code>.</p>',
    'Alles Weitere steht im Briefing <code>rev6/research/zipper_briefing.md</code>.</p>\n  <p><b>Geändert am 27.10. (Rev. 7):</b> Zipper-Fabrik, Preis, Menge und Zipper-Schwelle legst du am Mo 16.11. fest, am selben Tag geht das Tech Pack an die Fabrik. Das Zipper-Muster prüfst du am Do 14.01., das Sample-Gate ist Fr 15.01. Das Polo klären wir in drei Runden (Sa 07.11., Di 10.11., Di 17.11.).</p>')
rep('Oktober bis Dezember werden um rund 19 Stunden leichter, Zeit für Fabrik, Muster und Videos.</p>',
    'Oktober bis Dezember werden um rund 19 Stunden leichter, Zeit für Fabrik, Muster und Videos.</p>\n  <p><b>Überholt am 27.10. (Rev. 7):</b> Das Sample-Gate ist jetzt Fr 15.01. Recht und Website warten nicht mehr bis Januar: Gewerbe Mo 07.12., Steuer-Fragebogen Do 10.12., Zahlungen Di 15.12., Website Stufe 1 Do 31.12., LUCID Mo 04.01., Rechtstexte Di 05.01. Dafür startet das Marketing öffentlich erst am Mo 30.11.</p>', n=2)
rep('Außerdem liegt der Drop eine Woche vor den Sommerferien, die am 01.07. beginnen.</p>',
    'Außerdem liegt der Drop eine Woche vor den Sommerferien, die am 01.07. beginnen.</p>\n  <p><b>Stand Rev. 7:</b> Proto Di 08.12., PP bis Mi 13.01., Sample-Gate Fr 15.01., Vorbestellung Mo 01.02. Aufholwochen gibt es keine mehr.</p>')
rep('Bis zum Proto am 03.12. hast du kein Produkt zum Zeigen.', 'Bis zum Proto (Ziel Di 08.12.) hast du kein Produkt zum Zeigen.')
rep('Stichzahl, Fabrikpreis und Steuer sind erst im Oktober und November klar.', 'Stichzahl, Fabrikpreis und Steuer sind erst im November klar.')
rep('Darum gibt es das Zahlen-Cockpit direkt unter diesem Abschnitt.', 'Darum gibt es das Zahlen-Cockpit (Abschnitt 02).')
rep('<span class="no">Etappe 1 · bis So 01.11.</span><h3>Beweis</h3><span class="era">Validierung</span>\n    <dl><dt>Ziel</dt><dd>150 auf der Liste und 10 echte Zusagen im Blatt „Die ersten 35“.</dd><dt>Sonst</dt><dd>Kein Geld an die Fabrik. Eine Woche schieben, sechs neue Posts, das beste Video in fünf Varianten.</dd></dl>',
    '<span class="no">Etappe 1 · bis So 20.12.</span><h3>Beweis</h3><span class="era">Validierung</span>\n    <dl><dt>Ziel</dt><dd>Grün: mindestens 250 auf der Liste und 10 echte Zusagen im Blatt „Die ersten 35“.</dd><dt>Sonst</dt><dd>Gelb (100–249): bis So 10.01. nur Ausgaben nach Plan, das beste Video in drei Varianten. Rot (unter 100): Ausgaben-Stopp außer der Patch-Serie, Claude ändert Hooks, Kanäle und Abende.</dd></dl>')
rep_between('<h3>Was Rev. 6 dafür baut</h3>', 'Grind+ kommt zuletzt.</p>', f'''<h3>Was Rev. 7 dafür baut</h3>
    <p><b>Design zuerst:</b> Bis So 29.11. hat jedes Teil eine gültige Datei. Danach ändert sich am Design nur etwas, wenn Fabrik, Stickprobe oder Muster einen Grund liefern. Neue Ideen kommen in die Liste „Drop 2“.</p>
    <p><b>Eine Content-Maschine mit vollem Briefing:</b> {N_VID} Videos, {N_ST} Storys, {N_RW} REWIND und {N_CD} Countdown-Tage, jedes mit Hook, Takten, Dreh, Schnitt, Caption, erstem Kommentar und Messregel. Läuft ein Video doppelt so gut wie dein Schnitt, drehst du es in fünf Varianten nach.</p>
    <p><b>Eine Wärme-Kette:</b> Proto-Runde, Stick-Abend, Creator-Preview und drei Mess-Abende. Aus Adressen werden Käufer.</p>
    <p><b>Kassendisziplin:</b> erst Steuer, Fabrikpreis und Auszahlungsdauer klären, Geld nur in Stufen. Ab Nr. 036 gilt Stufe 2 zu 169 €.</p>
    <p><b>Symbol- und Sprachhygiene:</b> Wortliste nach außen, Sperrtermine, Regel-Check in jedem Briefing.</p>
  </div>
  <div class="card">
    <h3>Deine Zeit</h3>
    <p>Kern im Schnitt <b>rund {AVG} Minuten pro Tag</b> ab Woche 7, die Abi-Pause nicht mitgerechnet. An {NLONG} Tagen sind es mehr als zwei Stunden: Drehtage am Wochenende, Proto, Stick-Abend, Shoot, Packen und Drop.</p>
    <p><b>Grind+</b> ist alles, was du zusätzlich tun kannst, wenn du mehr Zeit hast: Karussells, Varianten, Laden-Runden, Märkte. Das sind rund {PLUSH} Stunden, alles optional. Mit dem Schalter im Tagesplan blendest du sie aus.</p>
    <p>Reicht die Zeit nicht, gilt diese Reihenfolge: Fabrik und Muster, dann Geld-Gates, Recht, Abende, Pflicht-Posts, Netz und Zusagen. Grind+ kommt zuletzt.</p>''')
rep_between('<span class="eyebrow">Diese Woche · kritischer Pfad</span>', '</div>', '''<span class="eyebrow">Diese zwei Wochen · kritischer Pfad</span>
  <p><b>Mi 28.10.:</b> Kuzgunlar-Call, falls Emirhan 15:00 Istanbuler Zeit bestätigt (14:00 in Zypern, 13:00 in Berlin) · Design-Inventur lesen · Bestandsaufnahme W5/W6. <b>Do 29.10.:</b> Herkunft des Baum-Bildes, Board 1 Etiketten (in der Türkei Feiertag). <b>Fr 30.10.:</b> LOGIC-Frist, DiZNEW abschließen, Board 2. <b>Sa und So:</b> Boards 3 bis 5, Lücken-Liste an Claude, Wochenreview.</p>
  <p><b>Mo 02.11.:</b> Zipper-Papiertest auf dem RL und Kapuze abpausen, nur wenn du in Berlin bist · Steuerfrage vor der Fabrikwahl · Versandweg. <b>Di 03.11.:</b> Jeansfabrik wählen, nur mit schriftlichem Preis. <b>Mi bis Fr:</b> Konditionen, Proforma, Entwicklung bezahlen, Dateien und Lab Dips, Patch-Anfrage. <b>Sa 07.11.:</b> Etiketten wählen, Polo-Runde 1.</p>
</div>''')
rep_between('<span class="eyebrow">Mein Rat als Mentor</span>', '</div>', '''<span class="eyebrow">Mein Rat als Mentor</span>
  <p><b>1 · Ohne schriftlichen Preis keine Fabrikwahl.</b> Der Call mit Kuzgunlar ist gut, aber ein Preis am Telefon ist kein Angebot. Bitte Emirhan, die Zahlen danach zu mailen. Liegt am Di 03.11. nichts Schriftliches vor, schiebst du auf Fr 06.11. Blind zu wählen kostet dich später mehr als drei Tage.</p>
  <p><b>2 · Das Design-Gate am 29.11. ist eine Mauer.</b> Was dir danach einfällt, kommt in Drop 2. Jede Änderung nach dem Gate kostet eine neue Stickprobe, also rund zwei Wochen, und schiebt das Sample-Gate.</p>
  <p><b>3 · Film jetzt schon.</b> Die ersten Content-Wochen leben von dem, was du in den Design-Wochen aufnimmst: Papiertests, Zuschnitt, Stickdatei am Bildschirm, das Auspacken jeder Probe. Ohne diesen Vorrat startest du am 30.11. mit leeren Händen.</p>
  <p><b>4 · Der Patch trägt den Gürtel.</b> Druckknöpfe und Nähte müssen den Zug jeden Tag aushalten. Zug- und Waschtest am Proto sind Pflicht. Reißt er bei Kunden aus, sind das Retouren und schlechte Bewertungen.</p>
  <p><b>5 · Die Liste ist dein Job, nicht das Posten.</b> Frag dich jeden Abend: Wie viele Menschen haben heute zum ersten Mal von Time Travel gehört? Ein Video, das niemand sieht, zählt nicht. Ein Gespräch im Laden zählt.</p>
</div>''')

NEWDEC = [
    ("<strong>Di 27.10.</strong>", "<strong>Entschieden:</strong> Docket komplett neu (Rev. 7). Erst die komplette Design-Suche, dann alle Designs fertig bis So 29.11., danach Marketing und das Rechtliche ab Mo 30.11., die Website parallel. Jedes Video, jede Story und jede Mail mit vollem Briefing.", "erledigt"),
    ("<strong>Mo 26.10.</strong>", "<strong>Entschieden:</strong> Rückendruck Zipper mit Band A oben am Hals, Muster E füllt den Abdruck bis in die Spitze, rote Kante, etwa 22 × 25 cm · Passform: Brust 60 cm in M (RL 57), Schulter 2 cm pro Seite tiefer, Saumrippe zieht wie beim RL, Oberarm 22,5 cm, Maßtabelle S–XL", "erledigt · der echte Umriss kommt aus deiner Abpausung"),
    ("<strong>So 25.10.</strong>", "<strong>Entschieden:</strong> Rückendruck Weg 1, die Fläche, als echter Abdruck deiner RL-Kapuze („Es muss wirklich der Abdruck vom Ralph Lauren sein.“)", "erledigt"),
    ("<strong>Sa 24.10.</strong>", "<strong>Entschieden:</strong> Teppich A „wie bei Oma“, Größe M 25 × 17,5 cm; Papiertest mit S 21 × 14,7 und L 29 × 20,3 cm", "erledigt · Größe nach dem Papiertest"),
    ("sofort", "Wann bist du zurück in Berlin? Davon hängt der Zipper-Papiertest ab (Plan: Mo 02.11.).", "Papiertest erst, wenn du den RL-Zipper vor dir hast. Rückt er, rücken nur Teppichgröße und Rückendruck mit, nicht die Fabrikwahl."),
    ("So 01.11.", "Wie alt bist du? Unter 18 brauchst du für die Gewerbe-Anmeldung (Mo 07.12.) die Eltern und das Familiengericht.", "Alter an Claude, dann plane ich den Weg. Das Familiengericht braucht Wochen."),
    ("Di 03.11.", "Jeansfabrik wählen: Kuzgunlar, DiZNEW oder LOGIC", "nur mit schriftlichem Preis; ohne Preis auf Fr 06.11. schieben, nicht blind wählen"),
]
rep('Deine Entscheidungen mit Datum</h3><div class="tablewrap"><table>\n<thead>\n<tr>\n<th>Bis</th>\n<th>Frage</th>\n<th>Mein Rat</th>\n</tr>\n</thead>\n<tbody>\n',
    'Deine Entscheidungen mit Datum</h3><div class="tablewrap"><table>\n<thead>\n<tr>\n<th>Bis</th>\n<th>Frage</th>\n<th>Mein Rat</th>\n</tr>\n</thead>\n<tbody>\n' + ''.join(f'<tr>\n<td>{a}</td>\n<td>{b}</td>\n<td>{c}</td>\n</tr>\n' for a, b, c in NEWDEC))
rep('<td>erledigt · Preis, Menge und Schwelle am Mo 09.11.</td>', '<td>erledigt · Preis, Menge und Schwelle am Mo 16.11.</td>')
rep('<td><strong>Do 29.10.</strong></td>\n<td>Versand:', '<td><strong>Mo 02.11.</strong></td>\n<td>Versand:')
rep('<td>fremd → Claude zeichnet eine eigene Fassung vor dem 28.10.</td>', '<td>fremd → Claude zeichnet eine eigene Fassung, sobald die Herkunft am Do 29.10. geklärt ist</td>')
rep('<strong>angemeldet wird Mi 06.01.</strong> nach dem Sample-Gate (Fragebogen zur steuerlichen Erfassung Do 07.01.)',
    '<strong>angemeldet wird Mo 07.12.</strong> (Fragebogen zur steuerlichen Erfassung Do 10.12.)')
rep('<td>Sa 07.11.</td>\n<td>Sprache der Hooks', '<td>So 20.12.</td>\n<td>Sprache der Hooks')
rep('<td>So 29.11.</td>\n<td>„Platz in der ersten Stunde sichern“', '<td>So 20.12.</td>\n<td>„Platz in der ersten Stunde sichern“')
rep('<td>Fr 11.12.</td>\n<td>Creator-Abmachung', '<td>Fr 18.12.</td>\n<td>Creator-Abmachung')
rep('<td>ja / Zahl am Mo 09.11.</td>', '<td>ja / Zahl am Mo 16.11.</td>')

# ---------- neue Abschnitte ----------
CP_STAT = (f'<div class="cpstat"><span><b>{N_VID}</b> Videos</span><span><b>{N_ST}</b> Storys</span><span><b>{N_RW}</b> REWIND</span>'
           f'<span><b>{N_CD}</b> Countdown-Tage</span><span>davon <b>{N_PLUS}</b> Grind+</span><span><b>{N_MAIL}</b> Mails</span></div>')
NEWSEC = f'''
<section id="inventur">
  <div class="sechead"><span class="n">04</span><h2>Design-Inventur</h2><span class="note">Jedes Design, sein Status, die gültige Datei und wann es dran ist. Stand Di 27.10.</span></div>
  <p class="intro">Was es an Designs gibt, was davon gilt und was noch fehlt. <b>Fertig</b> heißt: Die Datei ist verbindlich. <b>Entschieden</b> heißt: Die Richtung steht, die Datei fehlt noch. Die Termine in der Spalte „Wann“ sind Aufgaben im Tagesplan. Bis zum Design-Gate am So 29.11. soll jede Zeile fertig oder entschieden sein.</p>
  {inventur7.html_inventur()}
</section>

<section id="contentplan">
  <div class="sechead"><span class="n">05</span><h2>Content-Plan</h2><span class="note">Jedes Video, jede Story und jeder Countdown-Tag mit vollem Briefing.</span></div>
  <p class="intro">Alle Posts von Mo 30.11. bis nach dem Drop, nach Datum. Ein Klick öffnet das volle Briefing: Ziel, Hook mit Alternativen, Takte, Dreh, Ort, Requisiten, Licht, Kamera, Schnitt, Cover, Caption, erster Kommentar, Story, Regel-Check und wie du misst. Dieselben Briefings hängen im Tagesplan an den Dreh- und Posttagen. Vom 26.10. bis 29.11. wird nichts gepostet, nur Material gesammelt.</p>
  {CP_STAT}
  <div class="planbar">
    <input type="search" id="cpq" placeholder="Suchen: Teppich, REWIND, V231 …" aria-label="Content-Plan durchsuchen">
    <select id="cpk" aria-label="Art filtern"><option value="">Alle</option><option value="video">Videos</option><option value="story">Storys</option><option value="rewind">REWIND</option><option value="cd">Countdown</option><option value="karussell">Karussells</option><option value="live">Live</option><option value="plus">Grind+</option></select>
    <span class="hits" id="cphits"></span>
  </div>
  <div id="cplanList"></div>
</section>

<section id="mails">
  <div class="sechead"><span class="n">06</span><h2>E-Mails an die Liste</h2><span class="note">{N_MAIL} Mails, fertig geschrieben. Platzhalter vor dem Senden füllen.</span></div>
  <p class="intro">Alle Mails an die Liste, von der Willkommens-Mail bis zur Nacht nach dem Drop. In [eckigen Klammern] stehen Platzhalter, die du vor dem Senden mit echten Zahlen füllst. Gesendet wird aus Shopify Email, immer erst als Testmail an dich.</p>
  <div id="mailList"></div>
</section>
'''
rep('<section id="zielgruppe">', NEWSEC + '\n<section id="zielgruppe">')
rep('<div class="sechead"><span class="n">04</span><h2>Die Zielgruppe</h2>', '<div class="sechead"><span class="n">07</span><h2>Die Zielgruppe</h2>')
rep('<div class="sechead"><span class="n">05</span><h2>Das Design · v1.7 und Vorschläge</h2><span class="note">Papiertest 3 am Do 08.10., Freeze am Fr 09.10. Du entscheidest.</span></div>',
    '<div class="sechead"><span class="n">08</span><h2>Das Design · Herleitung und Varianten</h2><span class="note">Der Weg bis zum Freeze. Was heute gilt, steht in der Design-Inventur (04).</span></div>')
rep('<div class="sechead"><span class="n">06</span><h2>Referenz</h2>', '<div class="sechead"><span class="n">09</span><h2>Referenz</h2>')

# ---------- Referenz ----------
def zeit_html():
    out = []
    for w in DT.WEEKS:
        if w['n'] < 7:
            continue
        items = []
        for di, d in enumerate(w['days']):
            for t in d:
                if t.get('c') == 'N':
                    continue
                tt = re.sub(r'^\s*\d{1,2}:\d{2}(?:–\d{1,2}:\d{2})?\s*·\s*', '', t['t'])
                gate = re.search(r'GATE|Gate', tt)
                if t.get('vr') and not gate:
                    continue
                if t['c'] == 'D' or gate or re.search(r'\b[A-ZÄÖÜ]{5,}', tt):
                    items.append(f"{dl(DT.date_of(w, di))} {E(tt)}")
        st = DT.D(w['start'])
        en = st + datetime.timedelta(days=6)
        out.append(f'<tr><td class="mono">W{w["n"]} · {w["phase"]}</td><td class="mono">{st:%d.%m.}–{en:%d.%m.%y}</td><td>{"<br>".join(items) or "—"}</td></tr>')
    return ('<details class="ref" id="zeit"><summary><span class="chev"></span>Zeitachse · feste Termine je Woche <span class="pill ok" style="font-size:9.5px">Neu Rev. 7</span></summary>'
            '<div class="inner"><p class="intro">Die festen Termine, Entscheidungen und Gates je Woche, am 28.10. aus dem Tagesplan Rev. 7 erzeugt (W7–W41, Drop Do 24.06.2027). '
            'Verschiebt sich einer, schreib es Claude, dann wird der Rest neu geschnitten.</p><div class="tablewrap"><table><thead><tr><th>Woche</th><th>Zeitraum</th><th>Feste Termine und Gates</th></tr></thead><tbody>'
            + ''.join(out) + '</tbody></table></div></div></details>')


def v35_html():
    rows, cnt = [], {'ü': 0, 'g': 0, 'c': 0}
    start = {w['n']: w['start'] for w in lib7.V35}
    for k, t in lib7.OLD.items():
        n = int(k[1:k.index('d')])
        if n < 7 or t.get('c') == 'N':
            continue
        di = int(k[k.index('d') + 1:k.index('t')])
        od = (DT.D(start[n]) + datetime.timedelta(days=di)).isoformat()
        if k in lib7.USED:
            nid = lib7.USED[k]
            if nid in DT.IDX:
                w2, di2, nt = DT.IDX[nid]
                res = f'übernommen · {dl(DT.date_of(w2, di2))}' + ('' if nt['t'] == t['t'] else f' · „{E(nt["t"])}“')
            else:
                res = 'als Notiz übernommen'
            cnt['ü'] += 1
        elif k in lib7.DROPPED:
            res = 'gestrichen: ' + E(lib7.DROPPED[k])
            cnt['g'] += 1
        else:
            new = DT.CONTENT_DROP.get(k)
            res = f'Content-Plan: {new} am {E(clib.VIDS[new]["slot"])}' if new else 'Content-Plan: neu geplant'
            cnt['c'] += 1
        rows.append(f'<tr><td class="mono">W{n} · {dl(od)}</td><td>{E(t["t"])}</td><td>{res}</td></tr>')
    return (f'<details class="ref" id="v35"><summary><span class="chev"></span>Was aus dem alten Plan (v35) geworden ist <span class="pill ok" style="font-size:9.5px">Neu Rev. 7</span></summary>'
            f'<div class="inner"><p class="intro">Jede Aufgabe aus Docket v35 ab Woche 7, mit dem, was daraus geworden ist: {cnt["ü"]} übernommen (meist mit neuem Datum), '
            f'{cnt["g"]} gestrichen mit Grund, {cnt["c"]} Content-Aufgaben durch den Content-Plan ersetzt. W1–W6 sind unverändert im Archiv, deine Häkchen bleiben.</p>'
            '<div class="tablewrap"><table><thead><tr><th>Alt</th><th>Aufgabe in v35</th><th>Rev. 7</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div></div></details>')


assert s.count('<details class="ref" id="zeit">') == 1
zi = s.index('<details class="ref" id="zeit">')
ze = s.index('</details>', zi) + len('</details>')
s = s[:zi] + zeit_html() + '\n' + v35_html() + s[ze:]
rep('<div class="callout"><span class="eyebrow">Bereinigt am 22.10.</span>',
    '<div class="callout"><span class="eyebrow">Rev. 7 · 28.10.</span><p>Die Referenz stammt im Kern aus Rev. 6. Neu in Rev. 7: die Zeitachse (aus dem neuen Tagesplan erzeugt), „Was aus dem alten Plan geworden ist“ und der Content-Plan (Abschnitt 05) statt der alten Video-Bibliothek. '
    'Bei Widerspruch gilt der Tagesplan, für die Jeans das Tech Pack v1.0, für den Zipper das Zipper-Briefing.</p></div>\n<div class="callout"><span class="eyebrow">Bereinigt am 22.10.</span>')
rep_between('<h3>Video-Bibliothek</h3><div class="tablewrap">', '</table></div></div></details>',
            '<h3>Video-Bibliothek</h3><p>Die alte Bibliothek mit 149 Konzepten (V001–V149) ist in Rev. 7 durch den Content-Plan ersetzt (Abschnitt 05). '
            'Welche alte Nummer wohin gewandert ist, steht unter „Was aus dem alten Plan (v35) geworden ist“.</p></div></details>')
s = s.replace('V0xx', 'V2xx')

# ---------- Fußzeile ----------
rep_between('<p><b>Novalife · Time Travel · Rev. 6 vom 08.10.2026.</b>', '</p>',
            '<p><b>Novalife · Time Travel · Rev. 7 vom 28.10.2026.</b> Neu gegenüber Rev. 6 (v35): komplett neu geplant ab Woche 7 in deiner Reihenfolge, erst die Design-Suche, dann alle Designs fertig bis 29.11., '
            'danach Marketing und Recht, die Website parallel. Design-Inventur, Content-Plan mit vollem Briefing für jedes Video, jede Story und jeden Countdown-Tag, alle Mails fertig geschrieben, '
            'neue Kategorien Design, Recht und Website, Zeitachse und eine Liste, was aus jeder alten Aufgabe geworden ist. Woche 1 bis 6 sind unverändert, deine Häkchen bleiben.</p>')

# ---------- Daten ----------
CPLAN = [dict(id=x['id'], kind=x['kind'], post=list(x['post']), film=list(x['film']) if x.get('film') else None,
              plus=bool(x.get('plus')), auto=bool(x.get('auto'))) for x in SCHED]
lines = s.split('\n')
wi = [i for i, l in enumerate(lines) if l.startswith('var WEEKS = ')]
ki = [i for i, l in enumerate(lines) if l.startswith('var KPI = ')]
assert len(wi) == 1 and len(ki) == 1 and ki[0] == wi[0] + 1
lines[wi[0]] = 'var WEEKS = ' + js(DT.WEEKS) + ';'
lines[ki[0]] = ('var KPI = ' + js(kpi7.kpi()) + ';\nvar VIDS = ' + js(clib.VIDS) + ';\nvar MAILS = ' + js(mails.M) + ';\nvar CPLAN = ' + js(CPLAN) + ';')
s = '\n'.join(lines)

# ---------- Skript ----------
rep('var PH = {"P0": ["Design fertig", "14. Sep – 11. Okt 2026"], "P1": ["Fabrik finden", "12. Okt – 8. Nov 2026"], "P2": ["Sample und Sample-Gate", "9. Nov 2026 – 10. Jan 2027"], "P3": ["Shop und Vorbestellung", "11. Jan – 21. Feb 2027"], "P4": ["Produktion, Abi-Pause, Kampagne", "22. Feb – 30. Mai 2027"], "P5": ["Countdown & Drop", "31. Mai – 27. Jun 2027"]};',
    'var PH = ' + js({"A0": ["Bisher: Konzept, Freeze, Anfragen", "14. Sep – 25. Okt 2026"], "D1": ["Design-Suche", "26. Okt – 1. Nov 2026"],
                      "D2": ["Design fertig", "2. – 29. Nov 2026"], "M1": ["Marketing, Recht, Muster", "30. Nov 2026 – 31. Jan 2027"],
                      "M2": ["Vorbestellung", "1. – 21. Feb 2027"], "P": ["Produktion, Shoot, Abi-Pause", "22. Feb – 30. Mai 2027"],
                      "X": ["Countdown und Drop", "31. Mai – 27. Jun 2027"]}) + ';')
rep('var TAGNAME = {B:"BUILD", C:"CONTENT", D:"ENTSCHEIDUNG", A:"ADMIN", S:"SPIEL", V:"VERKAUF"};',
    'var TAGNAME = {G:"DESIGN", B:"BUILD", C:"CONTENT", D:"ENTSCHEIDUNG", A:"ADMIN", R:"RECHT", W:"WEBSITE", S:"SPIEL", V:"VERKAUF"};')
JSNEW = open(os.path.join(HERE, 'docket7.js'), encoding='utf-8').read()
ti = s.index('function taskRow(wn, di, ti, t, pfx, open){')
te = s.index('function dayMins(day){')
s = s[:ti] + JSNEW + '\n' + s[te:]
rep('if (done["w" + w.n + "d" + di + "t" + ti]) n++;', 'if (done[t.id || ("w" + w.n + "d" + di + "t" + ti)]) n++;')
rep('  if (!h) h = \'<li class="tk note"><span class="ntxt" style="color:var(--ink3)">Heute ist nichts geplant.</span></li>\';\n  ul.innerHTML = h;',
    '  if (!h) h = \'<li class="tk note"><span class="ntxt" style="color:var(--ink3)">Heute ist nichts geplant.</span></li>\';\n  ul.innerHTML = h;\n  fillLazy(ul);')
rep('["fo","Follower neu seit 12.10.",null]', '["fo","Follower neu seit 29.11.",null]')
rep('Startwert Follower (TikTok + Instagram zusammen, gezählt am Sa 10.10.)', 'Startwert Follower (TikTok + Instagram zusammen, gezählt am So 29.11.)')
JSSEC = open(os.path.join(HERE, 'docket7_sections.js'), encoding='utf-8').read()
rep('/* ---- cockpit ---- */', JSSEC + '\n/* ---- cockpit ---- */')

# ---------- Stil ----------
CSS = open(os.path.join(HERE, 'docket7.css'), encoding='utf-8').read()
i = s.index('</style>', s.index('<style>\n:root{'))
s = s[:i] + CSS + '\n' + s[i:]

open(OUT, 'w', encoding='utf-8').write(s)
print(OUT, f"{len(s.encode('utf-8')) / 1048576:.2f} MB · Aufgaben {NT} · Schnitt {AVG} Min. · lange Tage {NLONG} · Grind+ {PLUSH} h")
