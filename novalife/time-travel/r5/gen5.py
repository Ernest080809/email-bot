# -*- coding: utf-8 -*-
# Erzeugt docket_r5.html (Inhalt ohne Seitengerüst, das setzt das Artifact-Tool)
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ref5 as R
from r5_d import MOTIV, tag

LIVE = "/root/.claude/projects/-home-claude/1b46f4ed-4106-5442-ab27-98357078e4eb/tool-results/artifact-c3fa845d-1790504268-2688.html"
live = open(LIVE, encoding="utf-8").read().split("\n")
CSS = "\n".join(live[6:223])          # Zeilen 7–223: eigenes CSS des Dockets
assert CSS.lstrip().startswith(":root{") and "summary{list-style:none}" in CSS
LIVE_TXT = "\n".join(live)

def block(id_or_title):
    """<details class="ref" …> … </details> aus der Live-Fassung holen."""
    i = LIVE_TXT.find(id_or_title)
    s = LIVE_TXT.rfind('<details class="ref"', 0, i)
    j = LIVE_TXT.find("</details>", i)
    # verschachtelte details gibt es dort nicht
    return LIVE_TXT[s:j + len("</details>")]

WEEKS = json.load(open(os.path.join(HERE, "weeks_r5.json"), encoding="utf-8"))

EXTRA_CSS = r"""
/* Rev. 5 · Aufgaben mit Anleitung */
.tk{display:block; padding:8px 18px}
.tkrow{display:flex; gap:11px; align-items:flex-start}
.tk .body{min-width:0; flex:1}
.tk label.ttl{cursor:pointer; display:block}
.chips{display:flex; flex-wrap:wrap; gap:6px; margin-top:5px}
.chip{font-family:'IBM Plex Mono',monospace; font-size:10.5px; letter-spacing:.04em; padding:1px 6px; border:1px solid var(--line2); color:var(--ink2); background:var(--bg); white-space:nowrap}
.chip.cl{border-color:var(--brass); color:var(--brass)}
.chip.sp{border-color:var(--ok); color:var(--ok)}
details.how > summary{display:flex; flex-wrap:wrap; gap:6px 8px; align-items:center; cursor:pointer; padding:2px 0; margin-top:5px}
details.how > summary .sg{font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--indigo); display:inline-flex; gap:6px; align-items:center; white-space:nowrap}
details.how > summary .sg::before{content:"+"; font-weight:700; width:9px}
details.how[open] > summary .sg::before{content:"−"}
details.how > summary:focus-visible{outline:2px solid var(--brass); outline-offset:2px}
.kpis{grid-template-columns:repeat(4,minmax(0,1fr))}
@media(max-width:760px){.kpis{grid-template-columns:repeat(2,minmax(0,1fr))}}
ol.hs{margin:6px 0 8px; padding-left:20px; font-size:13.8px; color:var(--ink2)}
ol.hs li{margin:4px 0; line-height:1.5; padding-left:2px}
.fw{margin:8px 0; font-size:13.5px; color:var(--ink); border-left:3px solid var(--ok); padding:6px 10px; background:var(--okbg)}
.fw b{color:var(--ok); font-family:'IBM Plex Mono',monospace; font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; margin-right:6px}
.tk .prompt{margin:8px 0 4px}
.tk .prompt .ph .eyebrow{font-size:10px}
.tk.note{padding:6px 18px}
.tk.note .ntxt{display:flex; gap:10px; align-items:flex-start; font-size:13.5px; color:var(--ink2)}
.tk.note .ok{flex:none; width:17px; height:17px; margin-top:1px; background:var(--okbg); border:1.5px solid var(--ok); position:relative}
.tk.note .ok::after{content:""; position:absolute; left:5px; top:1px; width:4px; height:9px; border-right:2px solid var(--ok); border-bottom:2px solid var(--ok); transform:rotate(42deg)}
.dayhd .dm{font-family:'IBM Plex Mono',monospace; font-size:10.5px; color:var(--ink3)}
.dayhd .tdy{margin-left:8px}
.dayhd .sp{margin-left:auto}
.tdmeta{padding:10px 18px; border-bottom:1px solid var(--line); font-family:'IBM Plex Mono',monospace; font-size:12px; color:var(--ink2); display:flex; flex-wrap:wrap; gap:6px 18px}
.tdmeta b{color:var(--ink)}
.dtable td:first-child{white-space:nowrap}
.elgrid td:first-child{font-family:'Anton',sans-serif; font-size:18px; width:44px}
a.lnk{color:var(--indigo); text-underline-offset:2px}
"""

# ---------------------------------------------------------------- Kopf
HEAD = r"""<title>Time Travel Drop Docket</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
""" + CSS + EXTRA_CSS + """
</style>
"""

HEADER = r"""
<div class="wrap">

<header>
  <div class="brandrow">
    <span class="eyebrow">Novalife · Berlin · seit 2023</span>
    <span class="eyebrow">Projekt Slavic · Rev. 5.3 · 07.10.2026</span>
  </div>
  <h1 class="display">Time<br>Trav<span class="fade">el</span></h1>
  <div class="subline"><p>Eine Kultur, eine Fabrik, 100 bestickte Jeans. Zipper und Polo auf Bestellung aus Berlin. Erst wird das Design fertig, dann kommt das Sample, erst dann wird das Produkt gezeigt. Jede Aufgabe hat Dauer, Anleitung und ein „Fertig, wenn“.</p></div>

  <div class="cd">
    <div>
      <div class="cd-days"><span class="num mono" id="cdDays">—</span><span class="lbl">Tage bis Drop</span></div>
      <div class="cd-clock" id="cdClock">--:--:--</div>
    </div>
    <div class="cd-meta">
      <div class="cd-target">Drop <b>Donnerstag, 22. April 2027 · 19:00</b> · Warteliste ab 18:00<br><span id="weekOf">Woche — von 32</span></div>
      <div>
        <div class="megarow"><span>Fortschritt gesamt</span><b><span id="megaPct">0</span>% · <span id="megaCount">0/0</span></b></div>
        <div class="mega"><i id="megaBar"></i></div>
        <div class="savenote" id="saveNote" style="margin-top:7px">Fortschritt wird gespeichert …</div>
      </div>
    </div>
  </div>
</header>

<div id="today">
  <div class="tdhead">
    <span class="big" id="tdTitle">Heute</span>
    <span class="dt" id="tdDate">—</span>
    <span class="wno" id="tdWeek">—</span>
  </div>
  <div class="tdgoal" id="tdGoal">—</div>
  <div class="tdmeta" id="tdMeta"></div>
  <ul id="todayList"></ul>
</div>

<div class="legend">
  <span><span class="tg B">BUILD</span>Produkt, Fabrik, Sample</span>
  <span><span class="tg C">CONTENT</span>Posts, Storys, E-Mails</span>
  <span><span class="tg D">ENTSCHEIDUNG</span>hier legst du etwas fest</span>
  <span><span class="tg A">ADMIN</span>Shop, Recht, Versand</span>
  <span><span class="tg S">SPIEL</span>nur wenn du es in Woche 21 baust · <a href="#spiel" style="color:inherit">Bauplan</a></span>
  <span><span class="chip cl">mit Claude</span>Prompt zum Kopieren in der Anleitung</span>
</div>

<div class="phbar" id="phbar"></div>

<div class="kpis" style="margin-top:26px">
  <div class="kpi hero"><span class="k">Umsatzziel</span><div class="v">10.000 €</div><div class="s">64 Jeans: 35 vorbestellt + 29 im Drop</div></div>
  <div class="kpi"><span class="k">Jeans</span><div class="v">100</div><div class="s">1 Design, 1 Fabrik, nummeriert 001–100</div></div>
  <div class="kpi"><span class="k">Preise</span><div class="v">169 €</div><div class="s">Vorbestellung 149 € · Zipper 139 € · Polo 79 €</div></div>
  <div class="kpi"><span class="k">Stückkosten</span><div class="v">~63 €</div><div class="s">Zipper ~45 € · Polo ~19 €</div></div>
  <div class="kpi"><span class="k">Break-even</span><div class="v">60</div><div class="s">Jeans: 35 vorbestellt + 25 im Drop</div></div>
  <div class="kpi"><span class="k">Kapitalbedarf</span><div class="v">9.380 €</div><div class="s">Budget 4.500 € → Lücke 4.880 €</div></div>
  <div class="kpi"><span class="k">Vorbestellungen</span><div class="v">10 / 32</div><div class="s">mindestens bis 01.02. / bis 19.03.</div></div>
  <div class="kpi"><span class="k">Warteliste</span><div class="v">3.000</div><div class="s">E-Mails bis zum Drop</div></div>
</div>
"""

URTEIL = r"""
<!-- ===== URTEIL ===== -->
<section>
  <div class="sechead"><span class="n">00</span><h2>Das Urteil</h2><span class="note">Einmal lesen, dann den Tagesplan abarbeiten.</span></div>

  <div class="callout">
    <span class="eyebrow">Die Reihenfolge vom 01.10. · nicht verhandelbar</span>
    <p><b>Eine Kultur. Eine Fabrik. Erst wird das Design fertig, dann wird ein Sample gekauft, und erst wenn es in deiner Hand ist, wird das Produkt gezeigt.</b> Bis das Proto am 03.12. ankommt, zeigt dein Content den Weg dahin: Papier an der Hose, den Bauplan, die Zahlen, die Suche nach der Fabrik, die ersten Stickproben. Kein fertiges Teil und kein Mockup, das wie eins aussieht.</p>
    <p>Rev. 5 baut den ganzen Plan um diese Reihenfolge: 8 Anfragen statt 15, weil du bei genau einer Fabrik bestellst. Content ab 12.10. mit 3 Posts pro Woche, ab dem Proto 5, im Countdown täglich.</p>
  </div>

  <div class="callout bad">
    <span class="eyebrow">Die Zahl, um die du nicht herumkommst</span>
    <p>Kapitalbedarf <b>9.380 €</b> gegen 4.500 € Budget. Die Lücke von <b>4.880 €</b> kommt aus genau einer Quelle: <b>35 Vorbestellungen zu 149 €</b> ab dem 14.01. Mindestens <b>10 bis zur Schwelle am 01.02.</b> für die Anzahlung, mindestens <b>32 bis zur Restzahlung am 19.03.</b></p>
    <p>Zwischen 32 und 35 liegen 3 Paar Puffer. Das ist dünn, deshalb gilt: keine neue Stickerei ohne Gegenrechnung. Deshalb steht in Woche 21 die Regel: Läuft die Vorbestellung stark, wird das Kontingent auf 45 erhöht. Und falls du Kleinunternehmer bist und in der Türkei produzierst, kommen rund 1.150 € Einfuhrumsatzsteuer dazu. Das klärst du am 13.10., bevor du eine Fabrik wählst.</p>
  </div>

  <div class="callout">
    <span class="eyebrow">Drei Punkte, an denen Anhalten billig ist</span>
    <p><b>01.11. Validierung:</b> Nach drei Content-Wochen zählen die Anmeldungen. Unter 50 wird nicht bezahlt, sondern nachgeschärft. Danach gehen die ersten 650 € an die Fabrik.</p>
    <p><b>17.11. Stickproben:</b> Trägt die Stickerei auf echtem, gewaschenem Denim nicht, wird kein Proto genäht. <b>01.02. Schwelle:</b> Unter 10 Vorbestellungen keine Anzahlung, dann 75 Stück oder zwei Wochen schieben.</p>
  </div>

  <div class="grid2">
    <div class="card">
      <h3>Dein echter Engpass: Zeit</h3>
      <p>Du hast 1–2 Stunden am Tag. Der Plan hält sich daran: Die meisten Tage liegen zwischen 15 und 90 Minuten, Sonntage mit Content-Batch bei 1,5–2 Stunden. Rund 200 Stunden bis zum Drop.</p>
      <p>Fünf Tage sind länger und stehen jetzt schon fest: Shoot am 20.02., die Prüfung der Ware vom 31.03. bis 02.04., Drop und Packen vom 22. bis 24.04. Dafür nimmst du frei (Aufgabe am 05.03.). Das Spiel kostet sechs Wochen lang drei zusätzliche Abende und ist deshalb eine Option, keine Pflicht (Entscheidung 05.02.).</p>
    </div>
    <div class="card">
      <h3>Wie du diesen Plan benutzt</h3>
      <p>Oben steht, was <b>heute</b> dran ist, mit aufgeklappter Anleitung. Jede Aufgabe hat eine Dauer, die Schritte, ein <b>„Fertig, wenn“</b> und, wo Claude hilft, einen fertigen Prompt mit Kopier-Knopf.</p>
      <p>Abhaken, wenn das „Fertig, wenn“ stimmt, nicht vorher. Sonntags im Review alles Offene an Claude: „Offen aus Woche X: …“. Claude schiebt es sinnvoll weiter. Der Stand wird gespeichert und ist auf jedem Gerät gleich.</p>
    </div>
  </div>
</section>
"""

DESIGN = r"""
<!-- ===== DESIGN ===== -->
<section>
  <div class="sechead"><span class="n">01</span><h2>Das Design · v1.7</h2><span class="note">Nach deiner Skizze vom 07.10., mit großem Serp. Papiertest 3 am 08.10., Freeze am 09.10.</span></div>

  <p class="intro">Fünf gestickte Elemente auf einer Jeans, gebaut aus dem gemeinsamen Kern der Textiltradition: Raute, Zickzack, achtstrahliger Stern, Lebensbaum, Ernte. Feiner Kreuzstich im Raster von 1,33 mm, damit Band und Münztasche aussehen wie auf deinen Referenzfotos und nicht verpixelt. Sicht immer vom Träger aus. Alles zum Ansehen im Canvas <a class="lnk" href="https://claude.ai/artifact/Gi437A61nuWNvgLw98kMwz">Fit-Mockup NVL-TT-01</a>, zum Ausdrucken in <span class="mono">NVL_Druckvorlage_v17.pdf</span> (B2 und B), <span class="mono">NVL_Druckvorlage_v15.pdf</span> (A und E) und <span class="mono">NVL_Druckvorlage_1zu1.pdf</span> (C und D).</p>

  <div class="tablewrap elgrid"><table>
    <thead><tr><th>#</th><th>Element</th><th>Platzierung</th><th>Maß</th><th>Farben</th></tr></thead>
    <tbody>
      <tr><td>A</td><td><b>Vyshyvanka-Band</b></td><td>Bogenkante der rechten Vordertasche, Innenkante auf der Taschenöffnung</td><td>23 mm × ca. 20 cm · 17 Stiche hoch, Rapport 16</td><td>Rot, Weiß</td></tr>
      <tr><td>E</td><td><b>Münztasche, voll bestickt</b></td><td>Münztasche rechts vorn, ganze Fläche. Untere rechte Ecke unter dem Band</td><td>60 × 60 mm auf 62-mm-Tasche · 45 × 45 Stiche</td><td>Rot, Weiß</td></tr>
      <tr><td>B</td><td><b>Serp im Stoppelfeld</b></td><td>Linkes Bein vorn, 10 mm neben der Seitennaht, Mitte ca. 45 cm unter dem Bund. Der Serp wie in v1.5 über goldenen, abgeschnittenen Halmen</td><td>ca. 53 × 49 mm</td><td>Weiß, Rot, Grauweiß, zwei Brauntöne, Gold</td></tr>
      <tr><td>B2</td><td><b>Drei Ähren, rotes Band, Goldfäden</b></td><td>Linke Gesäßtasche, das Band auf Höhe des Alatyr. Neun Fäden hängen unter dem Band</td><td>Band 48 mm · mit Fäden ca. 51 × 56 mm</td><td>Gold, Dunkelgold, Rot</td></tr>
      <tr><td>C</td><td><b>Alatyr</b></td><td>Rechte Gesäßtasche, waagerecht mittig, auf Höhe des roten Bands links</td><td>36 × 36 mm · 27 × 27 Stiche</td><td>Weiß, Rot</td></tr>
      <tr><td>D</td><td><b>Lebensbaum-Patch</b></td><td>Bund hinten, zwischen den mittleren Schlaufen, über Bund und Passe</td><td>86 × 76 mm, Naturleinen</td><td>Gold, Ocker, drei Brauntöne, Rot</td></tr>
    </tbody>
    <caption>Rund 33.000 Stiche am Teil. Rechts das Muster, links die Ernte. Die Goldfäden: 9 Stück, 18–30 mm, dreifach gezwirnt, Polyester, nicht metallisiert, nach der Wäsche von Hand gesetzt und innen in der Tasche verknotet. Ein sechstes Element gibt es nicht.</caption>
  </table></div>

  <div class="grid2" style="margin-top:14px">
    <div class="dcard">
      <span class="no">Bis zum Freeze</span><h3>Papier vor Garn</h3><span class="era">01.–09.10.</span>
      <dl>
        <dt>Do 01.10.</dt><dd>Erledigt: gedruckt und Papiertest 1 gemacht, einen Tag früher. Daraus ist Design v1.5 entstanden.</dd>
        <dt>Mi 07.10.</dt><dd>Deine Skizze: Serp und Garbe runter von der Tasche, drei Ähren auf einem roten Band, ein Serp an der Seite. Claude baut v1.6, abends v1.7 mit großem Serp.</dd>
        <dt>Do 08.10.</dt><dd>Papiertest 3: zwei Seiten drucken, echte Garnfäden ankleben, Fotos an Claude, vier Entscheidungen. Das Aufkleben im Zeitraffer ist dein erster Post.</dd>
        <dt>Fr 09.10.</dt><dd>„Freeze“ und Tech Pack bestellen. Danach ändert sich das Design nur noch, wenn Fabrik oder Stickprobe einen Grund liefern.</dd>
      </dl>
    </div>
    <div class="dcard risky">
      <span class="no">Was verboten ist</span><h3>Neun Regeln</h3><span class="era">aus produkt-spec.md Rev. 10</span>
      <dl>
        <dt>Symbole</dt><dd>Keine Hakenkreuze und keine Ersatzsymbole: kein Kolovrat, keine Schwarze Sonne, kein Valknut, keine Haken, die sich drehen. Motive aus der Textiltradition, keine neuheidnische Symbolik.</dd>
        <dt>Gold und Rot</dt><dd>Gold nur in B, B2 und D. Keine Rotfläche ohne Weiß im nächsten Kreuzstich.</dd>
        <dt>Form</dt><dd>Keine Rundungen in A, C und E. Kein sechstes Element, B nicht spiegeln, nichts auf der Innenseite des Beins.</dd>
        <dt>Herkunft</dt><dd>Jedes Motiv ist in mindestens drei von vier Traditionen belegt. Die Ausführung von D ist die einzige Ausnahme. Nie „authentisch“, den Baum nie „slawisch“ nennen.</dd>
      </dl>
    </div>
  </div>

  <div class="sechead" style="margin-top:34px"><span class="n">01b</span><h2>Die Produktfamilie</h2><span class="note">Eine Fabrik, zwei Produkte ohne Kapitalbindung.</span></div>

  <div class="grid3">
    <div class="card">
      <h3>Jeans · 169 €</h3>
      <p><span class="pill ok">Hero</span> <span class="pill">MOQ 100</span></p>
      <p style="margin-top:10px">NVL-TT-01. Eine Fabrik in der Türkei oder in Portugal, Stickerei auf dem Zuschnitt vor dem Nähen. 12 oz, 100 % Baumwolle, rigid, Straight, ehrliche Größen W30–W38. Stückkosten ~63 €. Vorbestellung 35 Paar zu 149 € ab 14.01., nummeriert 001–100.</p>
    </div>
    <div class="card">
      <h3>Zipper · 139 €</h3>
      <p><span class="pill">MOQ 1</span></p>
      <p style="margin-top:10px">NVL-TT-02. Blank aus Fleece 330–350 g/m², in Berlin bestickt. Vorn zwei Bänder an der Zip-Leiste, hinten das Teppich-Medaillon, gestickt oder als Chenille-Patch (Entscheidung 19.12.). Stückkosten ~45 €. Wird erst nach der Bestellung gefertigt.</p>
    </div>
    <div class="card">
      <h3>Polo · 79 €</h3>
      <p><span class="pill">MOQ 1</span></p>
      <p style="margin-top:10px">NVL-TT-03. Piqué-Blank, zwei Bänder an der Knopfleiste, in Berlin bestickt. Stückkosten ~19 €. Das Einstiegsprodukt. Wird erst nach der Bestellung gefertigt.</p>
    </div>
  </div>

  <div class="callout">
    <span class="eyebrow">Alles geht am 22. April gleichzeitig live</span>
    <p>Ein großer Moment statt drei kleiner. Der Preis dafür: Bis zum Drop ist die Jeans-Vorbestellung die <b>einzige</b> Einnahme. Zipper und Polo bringen Gewinn nach dem Drop, keine Finanzierung davor.</p>
  </div>
</section>

<!-- ===== TAGESPLAN ===== -->
<section id="plan">
  <div class="sechead"><span class="n">02</span><h2>Der Tagesplan</h2><span class="note">32 Wochen, 224 Tage. Die laufende Woche ist offen. Ein Tipp auf „So geht's“ zeigt die Anleitung.</span></div>
  <div id="weeks"></div>
</section>
"""

# ---------------------------------------------------------------- Referenz: Spiel & Sizing aus Rev. 4.1, angepasst
spiel = block('id="spiel"')
for a, b in [
    ('<span class="pill ok" style="font-size:9.5px">Neu 27.09.</span>', '<span class="pill ok" style="font-size:9.5px">nur bei „bauen“</span>'),
    ('<span class="eyebrow">Entscheidung vom 27. September 2026</span>', '<span class="eyebrow">Idee vom 27. September 2026 · gebaut wird nur nach der Entscheidung am 05.02.</span>'),
    ('Kosten: ~20 € für Aseprite, aus dem Puffer. Dafür fällt der separate Countdown-Timer weg, denn die Tür ist der Countdown.</p>',
     'Kosten: ~20 € für Aseprite, aus dem Puffer.</p><p><b>Ob es gebaut wird, entscheidest du am Fr 05.02. (Woche 21).</b> Bauen nur, wenn die Vorbestellung läuft und du sechs Wochen lang drei zusätzliche Abende hast. Mein Rat bei 1–2 Stunden am Tag: streichen oder Silhouetten-Version. Die Kampagne verkauft, das Spiel ist Kür. Ohne Spiel bleibt die Startseite die Warteliste, und am 22.04. um 19:00 veröffentlichst du das Theme „Drop 22.04.“.</p>'),
    ('zusammen mit T−25', 'zusammen mit T−24'),
]:
    assert a in spiel, a[:40]
    spiel = spiel.replace(a, b)

sizing = block("Sizing · Maßtabelle")
for a, b in [
    ('Entscheidung am Proto-Sample in Woche 14', 'Entscheidung am Proto beim Fit-Test am Sa 05.12. (Woche 12)'),
    ('Ebenso offen: Innenbein-Gradierung +1,0 oder +1,5 cm, vor Woche 9.', 'Ebenso offen: Innenbein-Gradierung +1,0 oder +1,5 cm, festlegen im Tech Pack v1.1 (Woche 8).'),
]:
    assert a in sizing, a[:40]
    sizing = sizing.replace(a, b)

REF = ('\n<!-- ===== REFERENZ ===== -->\n<section>\n  <div class="sechead"><span class="n">03</span><h2>Referenz</h2>'
       '<span class="note">Nachschlagen, nicht durchlesen. Die Aufgaben verweisen hierher.</span></div>\n'
       + R.REF_ZEIT + "\n" + R.REF_VORL + "\n" + R.REF_PRUEF + "\n" + R.ref_content(MOTIV, tag) + "\n"
       + R.ref_fabriken() + "\n" + R.ref_kalk() + "\n" + R.ref_techpack() + "\n" + sizing + "\n" + spiel + "\n"
       + R.ref_risiken() + "\n</section>\n")

FOOTER = r"""
<footer>
  <p><b>Novalife · Time Travel · Projekt Slavic, Revision 5 vom 01.10.2026.</b> Neu gegenüber Rev. 4.1: eine Kultur und eine Fabrik ohne Ausnahme, die Reihenfolge Design fertig → Sample → erst dann zeigen, Content ab 12.10. mit Prozess statt Produkt, jede Aufgabe ab Woche 3 mit Dauer, Anleitung, „Fertig, wenn“ und Prompt, Vorlagen und Prüfplan als Referenz, Preise 169 / 149 / 139 / 79 €, Stückkosten nach Spec Rev. 10, Ramadan-Fest und Ostern im Zeitplan, das Spiel als Option. Woche 1 und 2 bleiben als Verlauf stehen.</p>
  <p style="margin-top:8px">Kosten und Preise sind Planwerte, keine Angebote. Fabrikangaben stammen aus öffentlichen Quellen und sind nicht geprüft. Ich bin weder Steuerberater noch Anwalt: Steuerstatus (13.10.) und Rechtstexte (24.11.) klärst du mit Fachleuten.</p>
  <div class="srcs">
    Quellen: <a href="https://www.ihk.de/stuttgart/fuer-unternehmen/recht-und-steuern/steuerrecht/umsatzsteuer-national/kleinunternehmerregelung-in-der-umsatzsteuer-1843632">IHK Stuttgart · Kleinunternehmerregelung</a> · <a href="https://www.cnnturk.com/turkiye/ramazan-bayrami-tarihi-2027-ramazan-bayrami-ne-zaman-arefe-hangi-gun-3457100">CNN Türk · Ramazan Bayramı 2027</a> · <a href="https://ohn.haendlerbund.de/logistik/paketdienste/dhl-monatspauschale-geschaeftskunden">Händlerbund · DHL-Monatspauschale</a> · <a href="https://www.sendcloud.com/de/dhl-kunde-werden/">Sendcloud · DHL ab dem ersten Paket</a> · <a href="https://trusted.de/shopify-kosten">Shopify-Kosten 2026</a> · <a href="https://www.yagemi.de/blog/e-commerce/shopify-payments-deutschland/">Shopify-Payments-Gebühren</a> · <a href="https://help.shopify.com/en/manual/shopify-admin/productivity-tools/future-publishing">Shopify · Future publishing</a> · <a href="https://www.futurebiz.de/artikel/instagram-stories-countdown-sticker/">Instagram Countdown-Sticker</a> · <a href="https://www.istanbulclothingmanufacturers.com/low-quantity-clothing-manufacturer/">Istanbul Clothing Manufacturers</a> · <a href="https://portugaltextile.com/jeans-factory/">Portugal Textile Jeans Factory</a> · <a href="https://arklavo.com/blogs/custom-apparel-guide/how-much-does-embroidery-cost">Stickpreise nach Stichzahl</a> · <a href="https://phaser.io/download/release/v3.90.0">Phaser v3.90.0</a> · <a href="https://shopify.dev/docs/storefronts/themes/tools/cli">Shopify CLI</a>
  </div>
</footer>
</div>
"""

PH = {"P0": ["Design fertig", "14. Sep – 11. Okt 2026"],
      "P1": ["Fabrik finden", "12. Okt – 8. Nov 2026"],
      "P2": ["Sample", "9. Nov – 20. Dez 2026"],
      "P3": ["Vorbestellung", "21. Dez 2026 – 7. Feb 2027"],
      "P4": ["Produktion & Kampagne", "8. Feb – 28. Mär 2027"],
      "P5": ["Countdown & Drop", "29. Mär – 25. Apr 2027"]}

JS = r"""
<script>
(function(){
"use strict";
var WEEKS = __WEEKS__;
var PH = __PH__;
var DROP = new Date("2027-04-22T19:00:00+02:00").getTime();

var DNAMES = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"];
var DSHORT = ["Mo","Di","Mi","Do","Fr","Sa","So"];
var MON = ["Jan","Feb","Mär","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Dez"];
var TAGNAME = {B:"BUILD", C:"CONTENT", D:"ENTSCHEIDUNG", A:"ADMIN", S:"SPIEL"};

function parseISO(s){ var p = s.split("-"); return new Date(+p[0], +p[1]-1, +p[2]); }
function addDays(d, n){ var x = new Date(d.getTime()); x.setDate(x.getDate()+n); return x; }
function iso(d){
  var m = d.getMonth()+1, dd = d.getDate();
  return d.getFullYear() + "-" + (m<10?"0":"") + m + "-" + (dd<10?"0":"") + dd;
}
function fmt(d){ return DSHORT[(d.getDay()+6)%7] + ", " + d.getDate() + ". " + MON[d.getMonth()] + " " + d.getFullYear(); }
function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
function isTask(t){ return t[0] !== "N"; }
function minTxt(m){ if (m >= 60){ var h = Math.floor(m/60), r = m%60; return h + " Std." + (r ? " " + r + " Min." : ""); } return m + " Min."; }

var TOTAL = 0, DAYMAP = {};
WEEKS.forEach(function(w){
  w._start = parseISO(w.start);
  w.days.forEach(function(day, di){
    day.forEach(function(t){ if (isTask(t)) TOTAL++; });
    DAYMAP[iso(addDays(w._start, di))] = {w:w, di:di};
  });
});

var done = Object.create(null);
var db = null, writing = false, pending = false;
var noteEl = document.getElementById("saveNote");
function note(s){ noteEl.textContent = s; }

function taskRow(wn, di, ti, t, pfx, open){
  var key = "w" + wn + "d" + di + "t" + ti;
  var id = (pfx || "") + key;
  if (t[0] === "N"){
    return '<li class="tk note"><span class="ntxt"><span class="ok"></span><span>' + esc(t[1]) + '</span></span></li>';
  }
  var mins = t[2] || 0, steps = t[3] || [], fertig = t[4] || "", prompt = t[5] || "", flag = t[6] || "";
  var h = '<li class="tk"><div class="tkrow">' +
    '<input type="checkbox" id="' + id + '" data-ms="' + key + '">' +
    '<div class="body"><label class="ttl" for="' + id + '"><span class="tg ' + t[0] + '">' + TAGNAME[t[0]] + '</span>' +
    '<span class="txt">' + esc(t[1]) + '</span></label>';
  var chips = "";
  if (mins) chips += '<span class="chip">' + minTxt(mins) + '</span>';
  if (prompt) chips += '<span class="chip cl">mit Claude</span>';
  if (flag === "s") chips += '<span class="chip sp">nur bei „Spiel bauen“</span>';
  if (steps.length || fertig || prompt){
    h += '<details class="how"' + (open ? ' open' : '') + '><summary>' + chips + '<span class="sg">So geht’s</span></summary>';
    if (steps.length){
      h += '<ol class="hs">';
      steps.forEach(function(s){ h += '<li>' + esc(s) + '</li>'; });
      h += '</ol>';
    }
    if (fertig) h += '<div class="fw"><b>Fertig, wenn</b>' + esc(fertig) + '</div>';
    if (prompt){
      var pid = "p_" + id;
      h += '<div class="prompt"><div class="ph"><span class="eyebrow">Prompt an Claude</span>' +
        '<button type="button" data-copy="' + pid + '">Kopieren</button></div>' +
        '<pre class="code" id="' + pid + '">' + esc(prompt) + '</pre></div>';
    }
    h += '</details>';
  } else if (chips){
    h += '<div class="chips">' + chips + '</div>';
  }
  return h + '</div></div></li>';
}

function dayMins(day){
  var m = 0, s = 0;
  day.forEach(function(t){ if (!isTask(t)) return; if (t[0] === "S") s += t[2] || 0; else m += t[2] || 0; });
  return [m, s];
}

/* ---- phase bar ---- */
(function(){
  var host = document.getElementById("phbar"), h = "";
  Object.keys(PH).forEach(function(k){
    h += '<div class="phcell" data-ph="' + k + '"><span class="id">' + k + '</span>' +
      '<div class="nm">' + PH[k][0] + '</div><div class="dt">' + PH[k][1] + '</div>' +
      '<div class="bar"><i data-phbar="' + k + '"></i></div>' +
      '<div class="ct" data-phct="' + k + '">0/0</div></div>';
  });
  host.innerHTML = h;
})();

/* ---- weeks ---- */
(function(){
  var host = document.getElementById("weeks"), h = "";
  WEEKS.forEach(function(w){
    var s = w._start, e = addDays(s, 6);
    var n = 0;
    w.days.forEach(function(d){ d.forEach(function(t){ if (isTask(t)) n++; }); });
    var range = s.getDate() + ". " + MON[s.getMonth()] + " – " + e.getDate() + ". " + MON[e.getMonth()] + " " + e.getFullYear();
    h += '<details class="wk" id="wk' + w.n + '" data-wk="' + w.n + '" data-ph="' + w.phase + '">' +
      '<summary class="wkhead"><span class="wktag">W' + w.n + " · " + w.phase + '</span>' +
      '<span class="wkti"><span class="g">' + esc(w.goal) + '</span><span class="d">' + range + '</span></span>' +
      '<span class="wkri"><span class="wkct" data-wct="' + w.n + '">0/' + n + '</span>' +
      '<span class="wkbar"><i data-wbar="' + w.n + '"></i></span><span class="chev"></span></span></summary>';
    w.days.forEach(function(day, di){
      var d = addDays(s, di), mm = dayMins(day);
      var mt = mm[0] ? "≈ " + minTxt(mm[0]) : "";
      if (mm[1]) mt += (mt ? " · " : "") + "+" + minTxt(mm[1]) + " Spiel";
      h += '<div class="day" data-date="' + iso(d) + '"><div class="dayhd">' +
        '<span class="dn">' + DNAMES[di] + '</span><span class="dd">' + d.getDate() + ". " + MON[d.getMonth()] + '</span>' +
        '<span class="tdy" hidden>Heute</span><span class="dm sp">' + mt + '</span></div><ul>';
      day.forEach(function(t, ti){ h += taskRow(w.n, di, ti, t, "", false); });
      if (!day.length) h += '<li class="tk note"><span class="ntxt" style="color:var(--ink3)">Frei.</span></li>';
      h += '</ul></div>';
    });
    h += '</details>';
  });
  host.innerHTML = h;
})();

/* ---- today ---- */
(function(){
  var now = new Date();
  var t = iso(now), todayISO = null;
  var first = WEEKS[0]._start, last = addDays(WEEKS[WEEKS.length-1]._start, 6);
  var target = t, entry = DAYMAP[t];
  if (!entry){
    if (now < first){ target = iso(first); entry = DAYMAP[target]; }
    else { target = iso(last); entry = DAYMAP[target]; }
  } else { todayISO = t; }

  var d = parseISO(target);
  var w = entry.w, di = entry.di, day = w.days[di];
  document.getElementById("tdTitle").textContent = (todayISO ? "Heute · " : "Plan-Tag · ") + DNAMES[di];
  document.getElementById("tdDate").textContent = fmt(d);
  document.getElementById("tdWeek").textContent = "Woche " + w.n + " von 32 · " + w.phase + " " + PH[w.phase][0];
  document.getElementById("tdGoal").innerHTML = "<b>Wochenziel:</b> " + esc(w.goal);
  var mm = dayMins(day), meta = "";
  meta += '<span>Heute: <b>' + (mm[0] ? "≈ " + minTxt(mm[0]) : "frei") + '</b>' + (mm[1] ? " · +" + minTxt(mm[1]) + " nur bei Spiel" : "") + '</span>';
  var nd = addDays(d, 1), ne = DAYMAP[iso(nd)];
  if (ne){
    var nt = ne.w.days[ne.di].filter(isTask);
    meta += '<span>Morgen: <b>' + (nt.length ? esc(nt[0][1]) + (nt.length > 1 ? " + " + (nt.length-1) + " weitere" : "") : "frei") + '</b></span>';
  }
  document.getElementById("tdMeta").innerHTML = meta;
  var ul = document.getElementById("todayList"), h = "";
  day.forEach(function(t, ti){ h += taskRow(w.n, di, ti, t, "td_", true); });
  if (!h) h = '<li class="tk note"><span class="ntxt" style="color:var(--ink3)">Heute ist nichts geplant.</span></li>';
  ul.innerHTML = h;

  var wk = document.getElementById("wk" + w.n);
  if (wk){ wk.open = true; wk.classList.add("cur"); }
  var dayEl = document.querySelector('.day[data-date="' + target + '"] .tdy');
  if (dayEl && todayISO) dayEl.hidden = false;
})();

/* ---- render state ---- */
var megaBar = document.getElementById("megaBar");
var megaPct = document.getElementById("megaPct");
var megaCount = document.getElementById("megaCount");

function render(){
  var total = 0, phAgg = {};
  Object.keys(PH).forEach(function(k){ phAgg[k] = [0,0]; });
  WEEKS.forEach(function(w){
    var n = 0, cap = 0;
    w.days.forEach(function(day, di){
      day.forEach(function(t, ti){
        if (!isTask(t)) return;
        cap++;
        if (done["w" + w.n + "d" + di + "t" + ti]) n++;
      });
    });
    total += n;
    phAgg[w.phase][0] += n;
    phAgg[w.phase][1] += cap;
    var c = document.querySelector('[data-wct="' + w.n + '"]');
    var b = document.querySelector('[data-wbar="' + w.n + '"]');
    if (c) c.textContent = n + "/" + cap;
    if (b) b.style.width = (cap ? n/cap*100 : 0) + "%";
    var el = document.getElementById("wk" + w.n);
    if (el) el.classList.toggle("done", cap > 0 && n === cap);
  });
  Object.keys(PH).forEach(function(k){
    var a = phAgg[k];
    var b = document.querySelector('[data-phbar="' + k + '"]');
    var c = document.querySelector('[data-phct="' + k + '"]');
    if (b) b.style.width = (a[1] ? a[0]/a[1]*100 : 0) + "%";
    if (c) c.textContent = a[0] + "/" + a[1];
  });
  var boxes = document.querySelectorAll("[data-ms]");
  for (var i = 0; i < boxes.length; i++){
    boxes[i].checked = !!done[boxes[i].getAttribute("data-ms")];
  }
  megaPct.textContent = Math.round(total / TOTAL * 100);
  megaCount.textContent = total + "/" + TOTAL;
  megaBar.style.width = (total / TOTAL * 100) + "%";
}

document.addEventListener("change", function(e){
  var t = e.target;
  if (!t || !t.getAttribute || !t.getAttribute("data-ms")) return;
  var id = t.getAttribute("data-ms");
  if (t.checked) done[id] = true; else delete done[id];
  render();
  save();
});

function save(){
  if (!db){ note("Nur in diesem Tab · Speicher nicht verfügbar"); return; }
  if (writing){ pending = true; return; }
  writing = true;
  var snap = {};
  Object.keys(done).forEach(function(k){ snap[k] = true; });
  db.doc("progress/tasks").set({ done: snap, updatedAt: new Date().toISOString() })
    .then(function(){ note("Gespeichert · " + new Date().toLocaleTimeString("de-DE")); })
    .catch(function(err){ note("Nicht gespeichert (" + (err && err.code ? err.code : "Fehler") + ")"); })
    .then(function(){ writing = false; if (pending){ pending = false; save(); } });
}

render();

/* ---- countdown ---- */
var dEl = document.getElementById("cdDays");
var cEl = document.getElementById("cdClock");
var wEl = document.getElementById("weekOf");
var STARTMS = WEEKS[0]._start.getTime();
function tick(){
  var now = Date.now(), ms = DROP - now;
  if (ms <= 0){
    dEl.textContent = "0"; cEl.textContent = "DROP IST LIVE"; wEl.textContent = "Woche 32 von 32"; return;
  }
  var s = Math.floor(ms/1000), d = Math.floor(s/86400), h = Math.floor(s%86400/3600), m = Math.floor(s%3600/60), sec = s%60;
  function p(n){ return n < 10 ? "0"+n : ""+n; }
  dEl.textContent = d;
  cEl.textContent = p(h) + ":" + p(m) + ":" + p(sec) + " verbleibend";
  var wk = Math.floor((now - STARTMS)/604800000) + 1;
  wEl.textContent = "Woche " + Math.max(1, Math.min(32, wk)) + " von 32";
}
tick();
setInterval(tick, 1000);

/* ---- copy buttons ---- */
document.addEventListener("click", function(e){
  var b = e.target && e.target.closest ? e.target.closest("[data-copy]") : null;
  if (!b) return;
  e.preventDefault();
  var pre = document.getElementById(b.getAttribute("data-copy"));
  if (!pre) return;
  var txt = pre.innerText;
  function ok(){ b.textContent = "Kopiert"; setTimeout(function(){ b.textContent = "Kopieren"; }, 1600); }
  function fallback(){
    try {
      var r = document.createRange(); r.selectNodeContents(pre);
      var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      if (document.execCommand && document.execCommand("copy")) ok(); else b.textContent = "Markiert";
    } catch(err){ b.textContent = "Markiert"; }
  }
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(ok, fallback);
    else fallback();
  } catch(err){ fallback(); }
});

/* ---- db ---- */
if (window.claude && window.claude.use){
  window.claude.use("db").then(function(d){
    if (!d){ note("Nur in diesem Tab · Speicher nicht verfügbar"); return; }
    db = d;
    note("Fortschritt wird gespeichert");
    db.doc("progress/tasks").onSnapshot(function(snap){
      if (!snap.exists){ note("Fortschritt wird gespeichert"); return; }
      var data = snap.data() || {}, rec = data.done || {};
      done = Object.create(null);
      Object.keys(rec).forEach(function(k){ if (rec[k]) done[k] = true; });
      render();
      if (!snap.metadata.hasPendingWrites) note("Gespeichert");
    }, function(err){
      note("Speicher unterbrochen (" + (err && err.code ? err.code : "Fehler") + ")");
    });
  }).catch(function(){ note("Nur in diesem Tab · Speicher nicht verfügbar"); });
} else {
  note("Nur in diesem Tab · Speicher nicht verfügbar");
}
})();
</script>
"""

wjson = json.dumps(WEEKS, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
js = JS.replace("__WEEKS__", wjson).replace("__PH__", json.dumps(PH, ensure_ascii=False))
OUT = HEAD + HEADER + URTEIL + DESIGN + REF + FOOTER + js
outp = os.path.join(HERE, "docket_r5.html")
open(outp, "w", encoding="utf-8").write(OUT)
print("geschrieben:", outp, len(OUT.encode("utf-8")), "Bytes")
