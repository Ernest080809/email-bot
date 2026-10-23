# -*- coding: utf-8 -*-
# Tech Pack v1.0 (Stand 23.10.2026) für die gewählte Fabrik, A4, Englisch und Deutsch aus einer Quelle
#   python3 techpack.py      -> v19/techpack.html     (Englisch, für die Fabrik)
#   python3 techpack.py de   -> v19/techpack_de.html  (Deutsch, für Ernest)
#   Maße aus dem Messbogen (Eightyfive M, 20.10.), Entscheidungen in rev6/research/techpack_checkliste.md
#   Anhang: Englisch = Artwork 1:1, Deutsch = Druckvorlage v1.9 Seiten 2–5 (beides per pdfunite in techpack_pdf.mjs)
import base64, io, math, os, subprocess, sys, tempfile
from PIL import Image
import fine as FN
import flats as FL

LANG = sys.argv[1] if len(sys.argv) > 1 else "en"
DE = LANG == "de"


def L(en, de):
    return de if DE else en


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
PDF_IN = os.path.join(ROOT, "pdf", "NVL_Druckvorlage_v19_Jeans.pdf")
VIS_JPG = os.path.join(ROOT, "mockup", "NVL-TT-01_visual.jpg")
SKIZZEN = os.path.join(ROOT, "rev6", "skizzen")
OUT_HTML = os.path.join(HERE, "v19", "techpack_de.html" if DE else "techpack.html")
VERSION, DATE = L("v1.0 draft", "v1.0 Entwurf"), L("23 Oct 2026", "23.10.2026")
DPI = 200; K = DPI / 25.4
F = FN.F

tmp = tempfile.mkdtemp()
subprocess.run(["pdftoppm", "-r", str(DPI), "-png", "-f", "2", "-l", "5", PDF_IN, os.path.join(tmp, "p")], check=True)
pages = {n: Image.open(os.path.join(tmp, f"p-{n}.png")).convert("RGB") for n in (2, 3, 4, 5)}


def crop(page, x0, y0, x1, y1):
    return pages[page].crop((int(x0 * K), int(y0 * K), int(x1 * K), int(y1 * K)))


def uri(im, fmt="PNG", q=85):
    b = io.BytesIO(); im.save(b, fmt, quality=q) if fmt == "JPEG" else im.save(b, fmt)
    return f"data:image/{fmt.lower()};base64," + base64.b64encode(b.getvalue()).decode()


def jpg(path, w):
    im = Image.open(path).convert("RGB")
    return uri(im.resize((w, int(w * im.height / im.width)), Image.LANCZOS), "JPEG", 82)


IMG = {"E": crop(2, 13, 49, 77, 113), "A": crop(2, 40, 146, 197, 267), "B2": crop(3, 24, 61, 186, 213),
       "C": crop(4, 24, 61, 186, 213), "D": crop(5, 13, 55, 95, 128)}
from PIL import ImageDraw                              # deutsche Beschriftung links neben Band A überdecken
ImageDraw.Draw(IMG["A"]).rectangle((0, int(14 * K), int(68 * K), int(44 * K)), fill="white")
VIS = jpg(VIS_JPG, 1300)
WASH = jpg(os.path.join(SKIZZEN, "2026-10-21_waesche_referenzen.jpg"), 700)
HONEY = jpg(os.path.join(SKIZZEN, "2026-10-21_honeycomb_ironheart.jpg"), 600)
SVG_FRONT = open(os.path.join(HERE, "techpack", "front.svg")).read()
SVG_BACK = open(os.path.join(HERE, "techpack", "back.svg")).read()

# ================= Maße: Basis W34 = Eightyfive M flach gemessen, nach der Wäsche =================
# Ehrliche Größen (Entscheidung 22.10., wie Spec Rev. 13): Etikett = gemessene Bundweite in Zoll, 86 cm = W34
BASE = "W34"
SIZES = ["W30", "W31", "W32", "W33", "W34", "W36", "W38"]
STEP = {"W30": -4, "W31": -3, "W32": -2, "W33": -1, "W34": 0, "W36": 2, "W38": 4}   # Zoll Abstand zur Basis
SPLIT = {"W30": 8, "W31": 10, "W32": 20, "W33": 14, "W34": 20, "W36": 18, "W38": 10}
# (Nr., Messpunkt, Messanleitung, Basis W34, Toleranz ±, Sprung je 1" Bund)
POM = [
    (1, L("Waist, half", "Bund, halb"), L("Top edge of waistband, buttoned, edge to edge.", "Oberkante Bund, Knopf zu, von Kante zu Kante."), 43.0, 1.0, 1.27),
    (2, L("Hip, half", "Hüfte, halb"), L("Straight across at the level of the end of the fly (J-stitch).", "Waagerecht auf Höhe vom Ende des Schlitzes (J-Naht)."), 52.0, 1.0, 1.27),
    (3, L("Thigh, half", "Oberschenkel, halb"), L("One leg, 2.5 cm below crotch, at right angles to the leg.", "Ein Bein, 2,5 cm unter dem Schritt, rechtwinklig zum Bein."), 29.0, 0.6, 0.6),
    (4, L("Knee, half", "Knie, halb"), L("One leg, 33 cm below crotch measured on the inseam, straight across.", "Ein Bein, 33 cm unter dem Schritt (auf der Innennaht gemessen), quer."), 22.5, 0.5, 0.4),
    (5, L("Leg opening, half", "Saumweite, halb"), L("At the hem, edge to edge.", "Am Saum, von Kante zu Kante."), 21.0, 0.5, 0.3),
    (6, L("Front rise", "Vordere Leibhöhe"), L("Crotch point to top of waistband along the seam, incl. waistband.", "Vom Schritt entlang der Naht bis Oberkante Bund, mit Bund."), 32.0, 0.5, 0.3),
    (7, L("Back rise", "Hintere Leibhöhe"), L("Crotch point to top of waistband along the seam, incl. waistband.", "Vom Schritt hinten entlang der Naht bis Oberkante Bund, mit Bund."), 37.0, 0.6, 0.4),
    (8, L("Inseam", "Innenbeinlänge"), L("Crotch point to the finished hem edge along the inseam, hem included. One length for all sizes (L32).", "Vom Schritt entlang der Innennaht bis zur fertigen Saumkante, Saum eingerechnet. Eine Länge für alle Größen (L32)."), 81.0, 1.0, 0.0),
    (9, L("Outseam", "Außenlänge"), L("Top of waistband to hem along the side seam.", "Von Oberkante Bund entlang der Seitennaht bis zum Saum."), 110.0, 1.0, 0.3),
    (10, L("Waistband height", "Bundhöhe"), L("Top to bottom edge of waistband.", "Oberkante bis Unterkante Bund."), 4.0, 0.2, 0.0),
    (11, L("Fly opening", "Schlitzlänge"), L("Bottom of waistband to end of J-stitch.", "Unterkante Bund bis Ende der J-Naht."), 15.0, 0.3, 0.2),
    (12, L("Back yoke at centre back", "Passe hinten Mitte"), L("Bottom of waistband to yoke seam, on the centre back seam.", "Unterkante Bund bis Passennaht, an der hinteren Mittelnaht."), 9.5, 0.3, 0.1),
    (13, L("Back yoke at side seam", "Passe an der Seite"), L("Bottom of waistband to yoke seam, on the side seam.", "Unterkante Bund bis Passennaht, an der Seitennaht."), 3.0, 0.3, 0.0),
    (14, L("Back pocket to centre back", "Gesäßtasche bis Mitte"), L("Centre back seam to inner top corner of back pocket.", "Hintere Mittelnaht bis zur inneren oberen Taschenecke."), 3.5, 0.3, 0.0),
    (15, L("Back pocket below waistband", "Gesäßtasche unter dem Bund"), L("Bottom of waistband to top of back pocket, at the inner corner.", "Unterkante Bund bis Oberkante Gesäßtasche, an der inneren Ecke."), 8.5, 0.3, 0.0),
    (16, L("Front pocket opening, width", "Eingriff vorn, Breite"), L("At the bottom of the waistband: side seam to start of pocket opening.", "An der Unterkante Bund: Seitennaht bis Anfang der Taschenöffnung."), 11.0, 0.3, 0.0),
    (17, L("Front pocket opening, depth", "Eingriff vorn, Tiefe"), L("Along the side seam: bottom of waistband to end of pocket opening.", "Entlang der Seitennaht: Unterkante Bund bis Ende der Taschenöffnung."), 7.0, 0.3, 0.0),
    (18, L("Belt loops, number", "Gürtelschlaufen, Anzahl"), L("2 front, 2 side back, 1 centre back.", "2 vorn, 2 hinten seitlich, 1 hinten Mitte."), 5, None, None),
    (19, L("Belt loop length", "Gürtelschlaufe, Länge"), L("Visible length, top to bottom.", "Sichtbare Länge von oben bis unten."), 4.0, 0.2, 0.0),
    (20, L("Hem height", "Saumbreite"), L("Hem edge to hem stitch line. Sewn hem, both legs equal ± 0.5 cm.", "Saumkante bis Steppnaht des Saums. Genähter Saum, beide Beine gleich lang ± 0,5 cm."), 1.0, 0.2, 0.0),
]


def r1(x):
    return math.floor(x * 10 + 0.5) / 10


def fmt(x):
    if isinstance(x, float):
        s = f"{x:.1f}"
        return s.replace(".", ",") if DE else s
    return str(x)


def graded(base, step, size):
    return base if step is None else r1(base + step * STEP[size])


# ================= Seitenrahmen =================
CSS = """
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;font-family:Helvetica,Arial,sans-serif;color:#1b2230;font-size:9pt;line-height:1.36}
.pg{width:210mm;height:297mm;padding:12mm 13mm 10mm;overflow:hidden;break-after:page;display:flex;flex-direction:column;gap:3.5mm}
.hd{display:flex;justify-content:space-between;align-items:baseline;border-bottom:0.4mm solid #1b2230;padding-bottom:2mm}
.hd b{font-size:8pt;letter-spacing:.12em;text-transform:uppercase}
.hd span{font-size:8pt;color:#68707e}
h1{font-size:21pt;margin:0;line-height:1.1}
h2{font-size:12.5pt;margin:0}
h3{font-size:10pt;margin:0}
p{margin:0}
.sub{color:#4a5262}
.vis{width:100%;max-height:53mm;object-fit:contain;border:0.3mm solid #d9dde4}
table{width:100%;border-collapse:collapse}
td,th{text-align:left;vertical-align:top;padding:1.15mm 1.8mm;border-bottom:0.25mm solid #e1e4ea}
.kv th{width:32mm;font-weight:700}
.spec th{background:#eef1f5;font-size:7.6pt;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap}
.spec td{font-size:8.4pt}
.spec td.n,.spec th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.spec td.no{font-weight:700;width:7mm;text-align:center}
.spec td.base,.spec th.base{background:#fbf3e9;font-weight:700}
.spec tr.grp td{background:#f6f7f9;font-weight:700;font-size:7.8pt;text-transform:uppercase;letter-spacing:.05em}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3mm}
.grid4{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:3mm}
.card{border:0.3mm solid #d9dde4;border-radius:2mm;padding:2.5mm;display:flex;flex-direction:column;gap:1.5mm}
.card img{width:100%;max-height:38mm;object-fit:contain}
.note{background:#f3f5f8;border-radius:2mm;padding:2.5mm 3mm}
.warn{background:#fbf0e6;border-left:1mm solid #a8643a;border-radius:1mm;padding:2.5mm 3mm}
ul,ol{margin:0;padding-left:5mm}
li{margin-bottom:0.8mm}
.diag{display:grid;grid-template-columns:1fr 1fr;gap:6mm;padding:0 14mm}
.diag svg{width:100%;height:auto;max-height:55mm}
.flat{width:100%;height:auto;max-height:150mm}
.diag .cap{text-align:center;font-size:8pt;color:#68707e;margin-top:1mm}
.gm{fill:#dbe4f0;stroke:#41618f;stroke-width:1.6}
.sm,.pk{fill:none;stroke:#41618f;stroke-width:1.2}
.st{fill:none;stroke:#b07a50;stroke-width:1.2;stroke-dasharray:3 2.4}
.lp{fill:#dbe4f0;stroke:#41618f;stroke-width:1}
.bt{fill:#9c5a30}
.ml{stroke:#9c5a30;stroke-width:1.5;fill:none}
.ml.dash{stroke-dasharray:3 3;stroke-width:1}
.bd circle{fill:#9c5a30}
.bd text{fill:#fff;font-family:Helvetica,Arial,sans-serif;font-size:9.5px;font-weight:700;text-anchor:middle}
.plan{width:62mm}
.po{fill:#efe7d6;stroke:#1b2230;stroke-width:0.3}
.snap{fill:#a8643a;stroke:#6f3d1f;stroke-width:0.3}.snapr{fill:none;stroke:#6f3d1f;stroke-width:0.3}
.dim{fill:none;stroke:#8a8f99;stroke-width:0.25;stroke-dasharray:1 0.8}
.dt{font-size:3px;fill:#68707e;text-anchor:middle;font-family:Helvetica,Arial,sans-serif}
.tun{fill:none;stroke:#4a6fa5;stroke-width:0.4;stroke-dasharray:2 1.4}
.tt{font-size:3.2px;fill:#4a6fa5;text-anchor:middle;font-family:Helvetica,Arial,sans-serif}
.refs{display:grid;grid-template-columns:1.25fr 1fr;gap:4mm;align-items:start}
.refs img{width:100%;max-height:112mm;object-fit:contain;border:0.3mm solid #d9dde4}
.foot{margin-top:auto;font-size:7.3pt;color:#68707e;border-top:0.25mm solid #e1e4ea;padding-top:2mm;display:flex;justify-content:space-between;gap:4mm}
"""
if DE:
    CSS += ".spec td{font-size:8.1pt}\n.refs img{max-height:98mm}\n"   # deutscher Text ist länger
PAGES = []


def page(title, body):
    PAGES.append((title, body))


def render():
    n = len(PAGES); out = []
    for i, (title, body) in enumerate(PAGES, 1):
        out.append(f'<section class="pg"><div class="hd"><b>Novalife · NVL-TT-01 · Tech Pack {VERSION}</b>'
                   f'<span>{DATE} · {L("page", "Seite")} {i} {L("of", "von")} {n} · {title}</span></div>{body}'
                   f'<div class="foot"><span>Novalife, Berlin, {L("Germany", "Deutschland")} · Ernest Veskimäe · ernest.veskimae@gmail.com</span>'
                   f'<span>{L("Designs, artwork and patterns are the property of Novalife and confidential.", "Designs, Artwork und Schnitte gehören Novalife und sind vertraulich.")}</span></div></section>')
    return out


# Seitennummern (nach INDEX)
PG = {"flats": 3, "emb": 4, "gold": 5, "pom": 6, "grade": 7, "bom": 8, "cons": 9, "proc": 10, "wash": 11, "labels": 12, "qc": 13}

# ================= 1 · Deckblatt =================
INDEX = L(["Cover and style summary", "Design overview", "Technical flats", "Embroidery", "Gold threads B2", "Points of measure, base size W34", "Grading W30–W38",
           "Bill of materials", "Construction and stitching", "Process and approvals", "Wash", "Labels, packing, compliance",
           "Quality control", "Annex: artwork 1:1 (4 pages)"],
          ["Deckblatt und Eckdaten", "Designübersicht", "Technische Zeichnungen", "Stickerei", "Goldfäden B2", "Messpunkte, Basisgröße W34", "Größen W30–W38",
           "Materialliste", "Verarbeitung und Nähte", "Ablauf und Freigaben", "Wäsche", "Etiketten, Verpackung, Vorschriften",
           "Qualitätskontrolle", "Anhang: Druckvorlage 1:1 (4 Seiten)"])
page(L("Cover", "Deckblatt"), f"""
<div><h1>{L("NVL-TT-01 · Time Travel jeans", "NVL-TT-01 · Time-Travel-Jeans")}</h1><p class="sub">{L("Men's 5-pocket straight-leg jeans with embroidery, 100 numbered pairs. Tech pack for the nominated factory.", "Herren-5-Pocket-Jeans, gerades Bein, mit Stickerei, 100 nummerierte Paare. Tech Pack für die gewählte Fabrik.")}</p></div>
<img class="vis" src="{VIS}" alt="Visual">
<p class="sub">{L(f"The visual shows the placement of all details. Fit and leg shape follow the measurements on pages {PG['pom']}–{PG['grade']}, which are slimmer than the visual. The wash is darker than shown (page {PG['wash']}).", f"Das Bild zeigt, wo alle Details sitzen. Passform und Bein richten sich nach den Maßen auf Seite {PG['pom']}–{PG['grade']} und sind schlanker als im Bild. Die Wäsche ist dunkler als gezeigt (Seite {PG['wash']}).")}</p>
<table class="kv">
<tr><th>{L("Style", "Modell")}</th><td>NVL-TT-01 · Time Travel · Novalife, Berlin</td></tr>
<tr><th>{L("Quantity", "Menge")}</th><td>{L("100 pairs, one style, one wash, numbered 001–100 on the inner label, plus 3 spare pairs without number (W32, W34, W36)", "100 Paare, ein Modell, eine Wäsche, nummeriert 001–100 auf dem Innenetikett, dazu 3 Reservepaare ohne Nummer (W32, W34, W36)")}</td></tr>
<tr><th>{L("Sizes", "Größen")}</th><td>{L("W30 · W31 · W32 · W33 · W34 · W36 · W38, one inseam 81 cm (L32). Base size and proto: W34. Honest sizes: the label is the measured waist in inches.", "W30 · W31 · W32 · W33 · W34 · W36 · W38, eine Innenbeinlänge 81 cm (L32). Basisgröße und Proto: W34. Ehrliche Größen: Das Etikett ist die gemessene Bundweite in Zoll.")}</td></tr>
<tr><th>{L("Fabric", "Stoff")}</th><td>{L("12 oz rigid 100 % cotton denim, no stretch, residual shrinkage ≤ 3 % after wash", "12 oz Denim, 100 % Baumwolle, ohne Stretch, Restschrumpf ≤ 3 % nach der Wäsche")}</td></tr>
<tr><th>{L("Wash", "Wäsche")}</th><td>{L("Mid-indigo vintage, honeycombs behind the knees, fading on the front thighs, no whiskers, no holes. Seams, hem and embroidery without wash effects", "Mittleres Vintage-Indigo, Honeycombs hinter den Knien, Aufhellung vorn auf den Oberschenkeln, keine Whiskers, keine Löcher. Nähte, Saum und Stickerei ohne Wascheffekte")}</td></tr>
<tr><th>{L("Embroidery", "Stickerei")}</th><td>{L("4 zones on the cut panels before sewing, about 28,000 stitches (annex)", "4 Zonen auf den Zuschnittteilen vor dem Nähen, etwa 28.000 Stiche (Anhang)")}</td></tr>
<tr><th>{L("Trims", "Zutaten")}</th><td>{L("YKK metal zip, 20 mm shank button, 6 rivets, 4 snaps for the detachable back patch, all antique copper, nickel-free", "YKK-Metallreißverschluss, Knopf 20 mm, 6 Nieten, 4 Druckknöpfe für den abnehmbaren Patch, alles Antik-Kupfer, nickelfrei")}</td></tr>
<tr><th>{L("Reference", "Referenz")}</th><td>{L(f"The measurements come from our reference jeans (size M, 86 cm waist = W34). There is no physical sample for now: the measurements in this tech pack are binding. Before cutting the proto you send us the measurement sheet of your pattern (page {PG['proc']}).", f"Die Maße stammen von unserer Referenzjeans (Gr. M, 86 cm Bund = W34). Ein physisches Muster gibt es vorerst nicht, die Maße in diesem Tech Pack sind verbindlich. Vor dem Zuschnitt des Protos schickt die Fabrik uns das Maßblatt ihres Schnitts (Seite {PG['proc']}).")}</td></tr>
</table>
<div class="grid">
<div><h3>{L("Contents", "Inhalt")}</h3><ol>{"".join(f"<li>{t}</li>" for t in INDEX)}</ol></div>
<div><h3>{L("Revisions", "Versionen")}</h3><table class="kv">
<tr><th>v0.9 · {L("20 Oct", "20.10.")}</th><td>{L("Quote pack (3 pages) and artwork 1:1", "Quote Pack (3 Seiten) und Artwork 1:1")}</td></tr>
<tr><th>{VERSION} · {L("23 Oct", "23.10.")}</th><td>{L("Complete tech pack. Changes since v0.9: honest sizes, base W34 = 86 cm · patch D in two layers with hidden snaps, a belt up to 40 mm runs through · 3 spare pairs · hem sewn, 1 cm · no wash effects on seams, hem and embroidery · B2 without white, red is bright red · number printed on the inner label.", "Komplettes Tech Pack. Änderungen seit v0.9: ehrliche Größen, Basis W34 = 86 cm · Patch D aus zwei Lagen mit versteckten Druckknöpfen, ein Gürtel bis 40 mm läuft durch · 3 Reservepaare · Saum genäht, 1 cm · keine Wascheffekte an Nähten, Saum und Stickerei · B2 ohne Weiß, Rot ist Knallrot · Nummer aufgedruckt auf dem Innenetikett.")}</td></tr>
</table>
<p class="sub" style="margin-top:1.5mm">{L("This tech pack is the only valid reference. Changes only as a new version with a new date, never by chat message.", "Dieses Tech Pack ist die einzige gültige Vorgabe. Änderungen nur als neue Version mit neuem Datum, nie per Chat-Nachricht.")}</p></div>
</div>""")

# ================= 2 · Designübersicht =================
page(L("Design overview", "Designübersicht"), f"""
<h2>{L("Design overview: what goes where", "Designübersicht: was wohin kommt")}</h2>
<div class="grid3">
<div class="card"><img src="{uri(IMG['A'])}" alt="A"><h3>{L("A · Band, right front pocket", "A · Band, rechte Vordertasche")}</h3><p>{L("Cross-stitch band 23 mm wide, 17 rows, red and white. Inner edge 175 mm on the pocket opening.", "Kreuzstich-Band 23 mm breit, 17 Reihen, Rot und Weiß. Innenkante 175 mm auf der Taschenöffnung.")}</p></div>
<div class="card"><img src="{uri(IMG['E'])}" alt="E"><h3>{L("E · Coin pocket", "E · Münztasche")}</h3><p>{L("Pocket 62 × 62 mm, fully embroidered 60 × 60 mm, red and white. Centred between side seam and pocket rivet.", "Tasche 62 × 62 mm, voll bestickt 60 × 60 mm, Rot und Weiß. Mittig zwischen Seitennaht und Taschenniete.")}</p></div>
<div class="card"><img src="{uri(IMG['D'])}" alt="D"><h3>{L("D · Back patch", "D · Patch hinten")}</h3><p>{L("Two-layer linen loop 80 × 71 mm, supplied by us. 4 hidden snaps, detachable. Back right, top flush with the waistband; the belt runs through.", "Schlaufe aus zwei Lagen Leinen, 80 × 71 mm, liefern wir. 4 versteckte Druckknöpfe, abnehmbar. Hinten rechts, oben bündig mit dem Bund, der Gürtel läuft durch.")}</p></div>
<div class="card"><img src="{uri(IMG['B2'])}" alt="B2"><h3>{L("B2 · Left back pocket", "B2 · Linke Gesäßtasche")}</h3><p>{L("Three wheat ears on a red band (48 mm). After washing: 9 gold threads 18–30 mm set by hand, knotted inside.", "Drei Ähren auf rotem Band (48 mm). Nach der Wäsche: 9 Goldfäden 18–30 mm von Hand, innen verknotet.")}</p></div>
<div class="card"><img src="{uri(IMG['C'])}" alt="C"><h3>{L("C · Right back pocket", "C · Rechte Gesäßtasche")}</h3><p>{L("Eight-point star of 8 rhombi, 36 × 36 mm, 1 mm gaps, solid red, satin stitch. Same height as the B2 band.", "Achtstern aus 8 Rauten, 36 × 36 mm, Fugen 1 mm, einfarbig Rot, Plattstich. Gleiche Höhe wie das B2-Band.")}</p></div>
<div class="card"><h3>{L("Hardware", "Metallteile")}</h3><p><b>{L("Button:", "Knopf:")}</b> {L("20 mm shank, antique copper, eight-point star embossed.", "20 mm, Antik-Kupfer, Achtstern geprägt.")}</p><p><b>{L("Rivets:", "Nieten:")}</b> {L("6 × 9 mm, plain antique copper: corners of both front pocket openings and of the coin pocket.", "6 × 9 mm, glatt, Antik-Kupfer: an den Ecken beider Vordertaschen und der Münztasche.")}</p><p><b>{L("Snaps:", "Druckknöpfe:")}</b> {L(f"4 ring-spring snaps 10 mm, hidden behind patch D (page {PG['cons']}).", f"4 Ringfeder-Druckknöpfe 10 mm, versteckt hinter Patch D (Seite {PG['cons']}).")}</p></div>
</div>
<table class="kv">
<tr><th>{L("Left / right", "Links / rechts")}</th><td>{L("Always as worn. The band A and coin pocket E are on the right front pocket (as worn). B2 is on the left back pocket, C and D are on the right back.", "Immer vom Träger aus. Band A und Münztasche E sitzen an der rechten Vordertasche. B2 ist auf der linken Gesäßtasche, C und D sind hinten rechts.")}</td></tr>
<tr><th>{L("Back pockets", "Gesäßtaschen")}</th><td>{L("Top 160 mm, bottom 130 mm, sides 125 mm (inner) and 120 mm (outer), point 70 mm each side, about 150 mm high. The inner side is 5 mm higher. Same size in all sizes.", "Oben 160 mm, unten 130 mm, Seiten 125 mm (innen) und 120 mm (außen), Spitze je 70 mm, etwa 150 mm hoch. Die Innenseite ist 5 mm höher. In allen Größen gleich.")}</td></tr>
<tr><th>{L("Not graded", "Nicht gradiert")}</th><td>{L("All embroidery, coin pocket, back pockets, front pocket opening, patch D, button, rivets and snaps are the same in every size. One embroidery program per motif.", "Alle Stickereien, Münztasche, Gesäßtaschen, Taschenöffnung vorn, Patch D, Knopf, Nieten und Druckknöpfe sind in jeder Größe gleich. Ein Stickprogramm je Motiv.")}</td></tr>
<tr><th>{L("Exact artwork", "Genaue Vorlage")}</th><td>{L("Annex, 4 pages in 1:1 scale. Print at 100 %; the check line must measure 100 mm.", "Anhang, 4 Seiten im Maßstab 1:1. Mit 100 % drucken, die Kontrolllinie muss 100 mm messen.")}</td></tr>
<tr><th>{L("Tolerance", "Toleranz")}</th><td>{L("Position of every embroidery, pocket and patch: ± 3 mm.", "Position jeder Stickerei, Tasche und des Patches: ± 3 mm.")}</td></tr>
</table>""")

# ================= 3 · Technische Zeichnungen =================
lrows = "".join(f'<tr><td class="no">{k}</td><td>{t}</td></tr>' for k, t in (FL.LEGEND_DE if DE else FL.LEGEND))
page(L("Technical flats", "Technische Zeichnungen"), f"""
<h2>{L("Technical flats · base size W34", "Technische Zeichnungen · Basisgröße W34")}</h2>
<div class="grid" style="gap:6mm;padding:0 6mm">{FL.FRONT_DE if DE else FL.FRONT}{FL.BACK_DE if DE else FL.BACK}</div>
<table class="spec"><tr><th>{L("Key", "Teil")}</th><th>{L("Detail", "Beschreibung")}</th></tr>{lrows}</table>
<p class="sub">{L(f"Drawn from our measurements, not to scale. The measurements on page {PG['pom']} are binding. Dashed brown lines are topstitching in copper-gold, short thick lines are bartacks. Front view: left in the drawing is the wearer's right.", f"Aus unseren Maßen gezeichnet, nicht maßstäblich. Verbindlich sind die Maße auf Seite {PG['pom']}. Gestrichelte braune Linien sind Ziernähte in Kupfer-Gold, kurze dicke Striche sind Riegel. Vorderansicht: links im Bild ist rechts am Träger.")}</p>""")

# ================= 4 · Stickerei =================
EMB = [
    ("A", L("Right front pocket (as worn), along the opening. Inner edge of the band on the opening edge, from the waistband to the side seam.", "Rechte Vordertasche (vom Träger aus), entlang der Öffnung. Innenkante des Bands auf der Taschenkante, vom Bund bis zur Seitennaht."),
     L("Band 23 mm wide, inner edge 175 mm", "Band 23 mm breit, Innenkante 175 mm"), L("Cross-stitch, 17 rows, cell 1.33 mm, repeat 16 stitches", "Kreuzstich, 17 Reihen, Zelle 1,33 mm, Rapport 16 Stiche"), L("Red, white", "Rot, Weiß"), "≈ " + L("12,000", "12.000")),
    ("E", L("Coin pocket, whole pocket, top flush with the coin pocket seam. Also embroider the lower inner corner that runs under the front panel, so no plain edge shows.", "Münztasche, ganze Fläche, oben bündig an der Münztaschennaht. Die untere innere Ecke, die unter das Vorderteil läuft, mitsticken, damit keine ungestickte Kante blitzt."), L("Pocket 62 × 62 mm, embroidery 60 × 60 mm", "Tasche 62 × 62 mm, Stickerei 60 × 60 mm"),
     L("Cross-stitch, 45 × 45 cells of 1.33 mm", "Kreuzstich, 45 × 45 Zellen à 1,33 mm"), L("Red, white", "Rot, Weiß"), "≈ " + L("10,500", "10.500")),
    ("B2", L("Left back pocket (as worn), centred. Middle of the red band about 45 mm below the pocket top edge, measured at the pocket centre. Ear tips at least 6 mm below the pocket hem stitching.", "Linke Gesäßtasche (vom Träger aus), mittig. Bandmitte etwa 45 mm unter der Taschenoberkante, in der Taschenmitte gemessen. Ährenspitzen mindestens 6 mm unter der Saumnaht der Tasche."),
     L("Band 48 mm long (51 mm with round ends), 3 mm wide. Three ears, 12 mm each, fanned", "Band 48 mm lang (51 mm mit runden Enden), 3 mm breit. Drei Ähren je 12 mm, gefächert"), L("Band: satin, single red. Ears: satin and fill", "Band: Plattstich, einfach Rot. Ähren: Platt- und Füllstich"), L("Gold, dark gold, red (no white)", "Gold, Dunkelgold, Rot (kein Weiß)"), "≈ " + L("2,500", "2.500")),
    ("C", L("Right back pocket, centred. Centre at the same height as the B2 band.", "Rechte Gesäßtasche, mittig. Mitte auf gleicher Höhe wie das B2-Band."), L("Star 36 × 36 mm, 8 rhombi, 1 mm gaps", "Stern 36 × 36 mm, 8 Rauten, Fugen 1 mm"),
     L("Satin stitch", "Plattstich"), L("Red", "Rot"), "≈ " + L("2,500", "2.500")),
]
erows = "".join(f'<tr><td class="no">{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td class="n">{f}</td></tr>' for a, b, c, d, e, f in EMB)
page(L("Embroidery", "Stickerei"), f"""
<h2>{L("Embroidery specification", "Stickerei")}</h2>
<table class="spec"><tr><th>{L("Zone", "Zone")}</th><th>{L("Position", "Position")}</th><th>{L("Size", "Größe")}</th><th>{L("Technique", "Technik")}</th><th>{L("Colours", "Farben")}</th><th class="n">{L("Stitches", "Stiche")}</th></tr>{erows}
<tr class="grp"><td></td><td colspan="4">{L("Total, estimate. The digitizing preview gives the real numbers.", "Summe, geschätzt. Die echten Zahlen kommen mit der Digitizing-Vorschau.")}</td><td class="n">≈ {L("27,500", "27.500")}</td></tr></table>
<table class="kv">
<tr><th>{L("When", "Wann")}</th><td>{L("On the cut panels <b>before sewing</b>: A on the front panel, E on the coin pocket, B2 and C on the back pockets.", "Auf den Zuschnittteilen <b>vor dem Nähen</b>: A auf dem Vorderteil, E auf der Münztasche, B2 und C auf den Gesäßtaschen.")}</td></tr>
<tr><th>{L("Shrinkage", "Schrumpf")}</th><td>{L("The denim shrinks in the wash, the thread does not. Digitize the motifs so they have the size above <b>after</b> the wash, or pre-wash the fabric. The washed strike-off shows which way works.", "Der Denim schrumpft in der Wäsche, das Garn nicht. Die Motive so digitalisieren, dass sie <b>nach</b> der Wäsche die Größe oben haben, oder den Stoff vorwaschen. Die gewaschene Stickprobe zeigt, was funktioniert.")}</td></tr>
<tr><th>{L("Thread", "Garn")}</th><td>{L("Polyester embroidery thread, resistant to bleach and enzyme wash (e.g. Madeira Polyneon 40 or equivalent). Bright red (signal red, not dark red or burgundy), white, gold and dark gold (non-metallic), chosen by us from your colour card.", "Polyester-Stickgarn, beständig gegen Bleiche und Enzymwäsche (z. B. Madeira Polyneon 40 oder gleichwertig). Knallrot (Signalrot, kein Dunkelrot oder Bordeaux), Weiß, Gold und Dunkelgold (nicht metallisch) wählen wir auf der Farbkarte der Fabrik.")}</td></tr>
<tr><th>{L("Backing", "Stickvlies")}</th><td>{L("Cut-away, wash-resistant, trimmed 3–5 mm around each motif.", "Schneidvlies, waschbeständig, 3–5 mm um jedes Motiv zurückgeschnitten.")}</td></tr>
<tr><th>{L("Finish", "Ausführung")}</th><td>{L("No loose jump stitches on the visible side, all ends tied off. No puckering. Red must not bleed into white or denim.", "Keine losen Spannfäden auf der Sichtseite, alle Enden vernäht. Keine Wellen. Rot darf nicht in Weiß oder Denim ausbluten.")}</td></tr>
<tr><th>{L("Same in all sizes", "In allen Größen gleich")}</th><td>{L("One embroidery program per motif. Back pockets and front pocket opening do not change between sizes.", "Ein Stickprogramm je Motiv. Gesäßtaschen und Taschenöffnung vorn ändern sich nicht zwischen den Größen.")}</td></tr>
<tr><th>{L("Tolerance", "Toleranz")}</th><td>{L("Position ± 3 mm, size ± 1 mm.", "Position ± 3 mm, Größe ± 1 mm.")}</td></tr>
<tr><th>{L("Files", "Dateien")}</th><td>{L("The embroidery files (DST) belong to Novalife. Exact artwork 1:1: annex.", "Die Stickdateien (DST) gehören Novalife. Genaue Vorlage 1:1: Anhang.")}</td></tr>
</table>
<div class="grid4">{"".join(f'<div class="card"><img src="{uri(IMG[k])}" alt="{k}"><h3>{k}</h3></div>' for k in ("A", "E", "B2", "C"))}</div>""")

# ================= 5 · Goldfäden B2 =================
TX = [16.5, 18.6, 20.6, 22.6, 24.5, 26.4, 28.3, 30.2, 32.0]          # wie v16.py, Bandmitte bei 24
TL = [19, 25, 22, 30, 27, 21, 29, 18, 24]
GOLD_SVG = ('<svg viewBox="-6 -16 60 58" style="width:105mm;display:block;margin:0 auto">'
            '<path d="M0 0H48" style="stroke:#b8322a;stroke-width:3;stroke-linecap:round"></path>'
            + "".join(f'<ellipse cx="{F(24+dx)}" cy="-7" rx="1.4" ry="5" transform="rotate({a} {F(24+dx)} -1)" style="fill:#c9a24a"></ellipse>' for dx, a in ((-4, -28), (0, 0), (4, 28)))
            + "".join(f'<path d="M{F(x)} 1.6v{F(l)}" style="stroke:#c9a24a;stroke-width:1;stroke-linecap:round"></path>'
                      f'<text x="{F(x)}" y="{F(l+5)}" style="font:700 2.2px Helvetica,Arial,sans-serif;fill:#1b2230;text-anchor:middle">{l}</text>' for x, l in zip(TX, TL))
            + '<path d="M16.5 36h15.5M16.5 35v2M32 35v2" style="stroke:#8a8f99;stroke-width:0.25"></path>'
            + f'<text x="24.25" y="38.6" style="font:400 2px Helvetica,Arial,sans-serif;fill:#68707e;text-anchor:middle">≈ 16 mm</text>'
            + f'<text x="24" y="-13" style="font:400 2px Helvetica,Arial,sans-serif;fill:#68707e;text-anchor:middle">{L("band 48 mm, three ears, threads in mm (visible length)", "Band 48 mm, drei Ähren, Fäden in mm (sichtbare Länge)")}</text></svg>')
page(L("Gold threads B2", "Goldfäden B2"), f"""
<h2>{L("Gold threads B2: the moment", "Goldfäden B2: der Moment")}</h2>
<p class="sub">{L("The idea of the jeans: a thread that leaves the jeans. This detail must be exactly right.", "Die Idee der Jeans: ein Faden, der die Hose verlässt. Dieses Detail muss genau stimmen.")}</p>
{GOLD_SVG}
<table class="kv">
<tr><th>{L("What", "Was")}</th><td>{L("9 gold threads hang freely out of the left back pocket, directly under the red band of B2, pointing down. Visible ends, not embroidered.", "9 Goldfäden hängen frei aus der linken Gesäßtasche, direkt unter dem roten Band von B2, nach unten. Sichtbare Enden, nicht gestickt.")}</td></tr>
<tr><th>{L("Lengths", "Längen")}</th><td>{L("Visible length from left to right (seen from behind): 19, 25, 22, 30, 27, 21, 29, 18, 24 mm. Spread over about 16 mm, centred under the band, about 2 mm apart.", "Sichtbare Länge von links nach rechts (von hinten gesehen): 19, 25, 22, 30, 27, 21, 29, 18, 24 mm. Verteilt auf etwa 16 mm, mittig unter dem Band, etwa 2 mm Abstand.")}</td></tr>
<tr><th>{L("Thread", "Garn")}</th><td>{L("Gold polyester, non-metallic, three-ply twisted, about 1 mm thick. Metallic thread breaks; thin thread disappears on denim.", "Gold, Polyester, nicht metallisiert, dreifach gezwirnt, etwa 1 mm dick. Metallgarn bricht, dünnes Garn verschwindet auf dem Denim.")}</td></tr>
<tr><th>{L("Fixing", "Befestigung")}</th><td>{L("Through the back pocket only, not through the body panel. Knotted inside the pocket (reach through the pocket opening). Ends knotted or heat-sealed so they do not unravel.", "Nur durch die Gesäßtasche gestochen, nicht durch das Hosenteil. Innen in der Tasche verknotet (durch die Taschenöffnung erreichbar). Enden verknotet oder heiß versiegelt, damit sie nicht aufdröseln.")}</td></tr>
<tr><th>{L("When", "Wann")}</th><td>{L("By hand, after wash and finishing, as a separate step. Not negotiable: loose threads do not survive the industrial wash.", "Von Hand, nach Wäsche und Finish, als eigener Arbeitsschritt. Nicht verhandelbar: Lose Fäden überleben die Industriewäsche nicht.")}</td></tr>
<tr><th>{L("Test", "Test")}</th><td>{L("On the PP sample: put on and take off, sit, 5 home washes inside out. A thread that catches or comes loose is shortened.", "Am PP-Muster: anziehen, ausziehen, sitzen, 5 Haushaltswäschen auf links. Ein Faden, der hängen bleibt oder sich löst, wird gekürzt.")}</td></tr>
</table>
<div class="grid" style="grid-template-columns:1fr 1fr"><div class="card"><img src="{uri(IMG['B2'])}" alt="B2" style="max-height:60mm"><h3>{L("B2 in the artwork 1:1 (annex)", "B2 in der Druckvorlage 1:1 (Anhang)")}</h3></div><div class="note"><h3>{L("Care label", "Pflegeetikett")}</h3><p>{L("The care text says: „Goldfäden nicht abschneiden“ (do not cut the gold threads), page ", "Auf dem Etikett steht: „Goldfäden nicht abschneiden“, Seite ")}{PG['labels']}.</p></div></div>""")

# ================= 6 · Messpunkte Basis W34 =================
rows = "".join(
    f'<tr><td class="no">{n}</td><td><b>{name}</b></td><td>{how}</td><td class="n base">{fmt(base)}</td>'
    f'<td class="n">{"" if tol is None else "± " + fmt(tol)}</td><td class="n">{"" if tol is None else fmt(r1(base / 2.54))}</td></tr>' for n, name, how, base, tol, _ in POM)
page(L("Points of measure", "Messpunkte"), f"""
<h2>{L("Points of measure · base size W34", "Messpunkte · Basisgröße W34")}</h2>
<div class="diag"><div>{SVG_FRONT}<div class="cap">{L("Front", "Vorn")}</div></div><div>{SVG_BACK}<div class="cap">{L("Back", "Hinten")}</div></div></div>
<table class="spec"><tr><th>{L("No.", "Nr.")}</th><th>{L("Point of measure", "Messpunkt")}</th><th>{L("How to measure", "So wird gemessen")}</th><th class="n base">W34 cm</th><th class="n">{L("Tol.", "Tol.")}</th><th class="n">{L("inch", "Zoll")}</th></tr>{rows}</table>
<p class="note">{L("All measurements in cm on the <b>finished garment after wash</b>, laid flat, buttoned, not stretched. Widths 1–5 are half measurements (edge to edge, not doubled). Lengths follow the seam. Please set the shrinkage allowance of the pattern from your own wash test on our fabric.", "Alle Maße in cm am <b>fertigen Teil nach der Wäsche</b>, flach gelegt, Knopf zu, nicht gedehnt. Weiten 1–5 sind halbe Maße (von Kante zu Kante, nicht verdoppelt). Längen folgen der Naht. Die Fabrik legt die Schrumpfzugabe im Schnitt nach ihrem eigenen Waschtest mit unserem Stoff fest.")}</p>""")

# ================= 6 · Gradierung =================
hdr = "".join(f'<th class="n{" base" if s == BASE else ""}">{s}</th>' for s in SIZES)
grows = ""
for n, name, how, base, tol, step in POM:
    cells = "".join(f'<td class="n{" base" if s == BASE else ""}">{fmt(graded(base, step, s))}</td>' for s in SIZES)
    gstep = "–" if not step else "+" + (f"{step:g}".replace(".", ",") if DE else f"{step:g}")
    grows += (f'<tr><td class="no">{n}</td><td>{name}</td><td class="n">{"" if tol is None else "± " + fmt(tol)}</td>'
              f'<td class="n">{gstep}</td>{cells}</tr>')
split = "".join(f'<td class="n{" base" if s == BASE else ""}">{SPLIT[s]}</td>' for s in SIZES)
waist_full = " · ".join(f"{s} {fmt(r1(2 * graded(43.0, 1.27, s)))}" for s in SIZES)
page(L("Grading", "Größen"), f"""
<h2>{L("Grading W30–W38 (proposal)", "Größen W30–W38 (Vorschlag)")}</h2>
<p class="sub">{L('Grade per 1" of waist size. Between W34, W36 and W38 the step is 2". Please check against your own block and send us your comments before the proto.', 'Sprung je 1 Zoll Bundweite. Zwischen W34, W36 und W38 sind es 2 Zoll. Die Fabrik prüft das gegen ihren eigenen Grundschnitt und schickt uns ihre Anmerkungen vor dem Proto.')}</p>
<table class="spec"><tr><th>{L("No.", "Nr.")}</th><th>{L("Point of measure", "Messpunkt")}</th><th class="n">{L("Tol.", "Tol.")}</th><th class="n">{L('Grade / 1"', "Sprung / 1 Zoll")}</th>{hdr}</tr>{grows}
<tr class="grp"><td></td><td colspan="3">{L("Estimated quantity (final in February)", "Geschätzte Menge (endgültig im Februar)")}</td>{split}</tr></table>
<p class="sub">{L("Plus 3 spare pairs without number: W32, W34, W36.", "Dazu 3 Reservepaare ohne Nummer: W32, W34, W36.")}</p>
<div class="grid">
<div class="note"><h3>{L("Honest sizes", "Ehrliche Größen")}</h3><p>{L("The size label is the measured waist in inches, no vanity sizing. Full waist in cm: ", "Das Größenetikett ist die gemessene Bundweite in Zoll, nichts geschönt. Bundweite rundum in cm: ")}{waist_full}. {L("Size label: W.. L32.", "Größenetikett: W.. L32.")}</p></div>
<div class="note"><h3>{L("Same in all sizes", "In allen Größen gleich")}</h3><p>{L("Inseam 81 cm, waistband 4 cm, hem 1 cm, belt loops, back pocket size and position, front pocket opening, coin pocket, all embroidery, patch D and hardware. Zip length per size: your proposal.", "Innenbein 81 cm, Bund 4 cm, Saum 1 cm, Gürtelschlaufen, Größe und Lage der Gesäßtaschen, Taschenöffnung vorn, Münztasche, alle Stickereien, Patch D und Metallteile. Länge des Reißverschlusses je Größe: Vorschlag der Fabrik.")}</p></div>
</div>""")

# ================= 7 · Materialliste =================
BOM = [
    (L("Shell fabric", "Oberstoff"), L("12 oz (approx. 400 g/m²) rigid 100 % cotton denim, 3/1 twill, indigo, no stretch. Residual shrinkage ≤ 3 % in length and width after wash.", "12 oz (etwa 400 g/m²) Denim, 100 % Baumwolle, Köper 3/1, Indigo, ohne Stretch. Restschrumpf ≤ 3 % in Länge und Breite nach der Wäsche."),
     L("Body", "Hose"), L("Factory proposes mill and article; we approve the swatch before the proto", "Fabrik schlägt Weberei und Artikel vor, wir geben das Stoffmuster vor dem Proto frei")),
    (L("Pocketing", "Taschenbeutel"), L("Cotton, natural white, unprinted, your standard weight.", "Baumwolle, naturweiß, unbedruckt, Standardgewicht der Fabrik."), L("Front pocket bags", "Vordertaschen"), L("Factory", "Fabrik")),
    (L("Interlining", "Einlage"), L("Waistband: your standard. Behind each snap stud: 20 × 20 mm reinforcement inside (denim or fusible).", "Bund: Standard der Fabrik. Hinter jedem Druckknopf-Unterteil innen 20 × 20 mm Verstärkung (Denim oder Bügeleinlage)."), L("Waistband, snaps", "Bund, Druckknöpfe"), L("Factory", "Fabrik")),
    (L("Topstitch thread", "Ziernahtgarn"), L("Corespun polyester/polyester, colour copper-gold, colourfast to enzyme and bleach: it keeps its colour in the wash. Weight your standard for jeans.", "Umspinnzwirn Polyester/Polyester, Farbe Kupfer-Gold, farbecht gegen Enzym und Bleiche: Es behält in der Wäsche seine Farbe. Stärke Jeans-Standard der Fabrik."), L("All visible topstitching and bartacks", "Alle sichtbaren Ziernähte und Riegel"), L("Factory, colour card to us", "Fabrik, Farbkarte an uns")),
    (L("Seam thread", "Nähgarn"), L("Tonal indigo.", "Indigo, Ton in Ton."), L("Inner seams, overlock", "Innennähte, Overlock"), L("Factory", "Fabrik")),
    (L("Embroidery thread", "Stickgarn"), L("Polyester, wash- and bleach-resistant (e.g. Madeira Polyneon or equivalent). Bright red, white, gold, dark gold (non-metallic).", "Polyester, wasch- und bleichbeständig (z. B. Madeira Polyneon oder gleichwertig). Knallrot, Weiß, Gold, Dunkelgold (nicht metallisch)."), "A, E, B2, C", L("Factory, colour card to us", "Fabrik, Farbkarte an uns")),
    (L("Embroidery backing", "Stickvlies"), L("Cut-away backing, wash-resistant, trimmed 3–5 mm around each motif. Stitch density: your proposal in the digitizing preview.", "Schneidvlies, waschbeständig, 3–5 mm um jedes Motiv zurückgeschnitten. Stichdichte: Vorschlag der Fabrik in der Digitizing-Vorschau."), "A, E, B2, C", L("Factory", "Fabrik")),
    (L("Gold threads B2", "Goldfäden B2"), L(f"Gold polyester, non-metallic, three-ply twisted, about 1 mm. 9 pieces, visible length 18–30 mm (page {PG['gold']}), set by hand after wash, knotted inside the pocket, ends sealed.", f"Gold, Polyester, nicht metallisiert, dreifach gezwirnt, etwa 1 mm. 9 Stück, sichtbare Länge 18–30 mm (Seite {PG['gold']}), nach der Wäsche von Hand gesetzt, innen in der Tasche verknotet, Enden versiegelt."), L("Left back pocket", "Linke Gesäßtasche"), L("Factory", "Fabrik")),
    (L("Zipper", "Reißverschluss"), L("YKK metal no. 4.5, antique copper finish, auto-lock slider, tonal tape. Length per size: your proposal.", "YKK Metall Nr. 4,5, Antik-Kupfer, Schieber mit Autolock, Band Ton in Ton. Länge je Größe: Vorschlag der Fabrik."), L("Fly", "Schlitz"), L("Factory", "Fabrik")),
    (L("Shank button", "Knopf"), L("20 mm (ligne 32), antique copper, eight-point star embossed, nickel-free. Custom tooling.", "20 mm (Ligne 32), Antik-Kupfer, Achtstern geprägt, nickelfrei. Eigenes Werkzeug."), L("Waistband, 1 pc", "Bund, 1 Stück"), L("Factory sources, sample to us", "Fabrik besorgt, Muster an uns")),
    (L("Rivets", "Nieten"), L("9 mm, plain, antique copper, nickel-free.", "9 mm, glatt, Antik-Kupfer, nickelfrei."), L("6 pcs: front pocket openings and coin pocket corners", "6 Stück: Vordertaschen und Ecken der Münztasche"), L("Factory", "Fabrik")),
    (L("Snaps", "Druckknöpfe"), L("Ring-spring snaps 10 mm, antique copper, nickel-free. One system for stud, socket and cap.", "Ringfeder-Druckknöpfe 10 mm, Antik-Kupfer, nickelfrei. Ein System für Unterteil, Oberteil und Kappe."), L("4 sets: studs on jeans, sockets and caps on the back panel of patch D", "4 Sätze: Unterteile an der Jeans, Oberteile und Kappen an der Rückwand von Patch D"), L("Factory sources and sets both parts", "Fabrik besorgt und setzt beide Teile")),
    (L("Patch D", "Patch D"), L("Two layers: embroidered linen front 80 × 71 mm and back panel, joined in the middle 30 mm at top and bottom, open at the sides. Pre-shrunk, sealed edges, sew-in stiff interlining, colourfast threads, without snaps. Washable by hand on its own.", "Zwei Lagen: besticktes Leinen vorn 80 × 71 mm und Rückwand, oben und unten in der Mitte auf 30 mm verbunden, seitlich offen. Vorgeschrumpft, Kanten versiegelt, eingenähte feste Einlage, farbechte Garne, ohne Druckknöpfe. Einzeln von Hand waschbar."), L("Back right", "Hinten rechts"), L("Supplied by Novalife", "Liefert Novalife")),
    (L("Inner label", "Innenetikett"), L(f"Printed, permanent, readable after washing. Content on page {PG['labels']}.", f"Bedruckt, dauerhaft, nach dem Waschen lesbar. Inhalt auf Seite {PG['labels']}."), L("Inside back waistband", "Innen am hinteren Bund"), L("Factory prints, text from us", "Fabrik druckt, Text von uns")),
    (L("Polybag", "Polybeutel"), L("Recyclable LDPE, one pair per bag, suffocation warning in German and English.", "Recycelbares LDPE, ein Paar pro Beutel, Erstickungswarnung auf Deutsch und Englisch."), L("Packing", "Verpackung"), L("Factory", "Fabrik")),
    (L("Hangtag", "Hangtag"), L("Design follows (supplied by Novalife or printed by factory). No number.", "Design folgt (liefert Novalife oder druckt die Fabrik). Ohne Nummer."), L("Left back belt loop", "Linke hintere Gürtelschlaufe"), L("Open", "Offen")),
]
brows = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in BOM)
page(L("Bill of materials", "Materialliste"), f"""
<h2>{L("Bill of materials", "Materialliste")}</h2>
<table class="spec"><tr><th>{L("Item", "Teil")}</th><th>{L("Description", "Beschreibung")}</th><th>{L("Where / quantity", "Wo / Menge")}</th><th>{L("Source", "Bezug")}</th></tr>{brows}</table>
<p class="warn"><b>{L("All metal parts nickel-free", "Alle Metallteile nickelfrei")}</b> {L("(EU REACH: nickel release ≤ 0.5 µg/cm²/week, EN 1811). Please send the supplier declaration or test report with the hardware samples. All trims antique copper in the same tone.", "(EU-REACH: Nickelabgabe ≤ 0,5 µg/cm²/Woche, EN 1811). Die Fabrik schickt die Erklärung des Lieferanten oder einen Prüfbericht mit den Metallmustern. Alle Metallteile Antik-Kupfer im gleichen Ton.")}</p>
<p class="note">{L("Please send for approval before the proto: fabric swatch with shrinkage result, thread colour card (topstitch and embroidery), button and snap samples, one printed inner label. Article numbers and suppliers: please fill in and return this page.", "Vor dem Proto zur Freigabe an uns: Stoffmuster mit Schrumpfwert, Garnfarbkarte (Ziernaht und Stickerei), Muster von Knopf und Druckknöpfen, ein gedrucktes Innenetikett. Artikelnummern und Lieferanten trägt die Fabrik auf dieser Seite ein.")}</p>""")

# ================= 8 · Verarbeitung =================
PW, PH, PB, SIN, SD = 80.0, 71.0, 5.5, 7.0, 10.0
GX, GY = PW - 2 * SIN, PH - 2 * PB - 2 * SIN
snaps = "".join(f'<circle cx="{F(x)}" cy="{F(y)}" r="{F(SD/2)}" class="snap"></circle><circle cx="{F(x)}" cy="{F(y)}" r="{F(SD*0.36)}" class="snapr"></circle>'
                for x in (SIN, SIN + GX) for y in (PB + SIN, PB + SIN + GY))
PATCH_SVG = (f'<svg viewBox="-12 -8 104 92" class="plan"><path d="{FN.patch_outline(0, 0, PW, PH, PB)}" class="po"></path>{snaps}'
             f'<path d="M{F(SIN)} {F(PB+SIN)}h{F(GX)}M{F(SIN)} {F(PB+SIN)}v{F(GY)}" class="dim"></path>'
             f'<text x="40" y="{F(PB+SIN-2)}" class="dt">{F(GX)} mm</text>'
             f'<text x="{F(SIN+2)}" y="{F(PB+SIN+GY/2+1)}" class="dt" style="text-anchor:start">{F(GY)} mm</text>'
             f'<rect x="-6" y="4" width="{F(PW+12)}" height="38" class="tun"></rect>'
             f'<path d="M25 1.4h30M25 {F(PH-1.4)}h30" style="stroke:#6b4a2a;stroke-width:1.2"></path>'
             f'<text x="40" y="26" class="tt">{L("belt up to 40 mm runs through", "Gürtel bis 40 mm läuft durch")}</text>'
             f'<path d="M0 {F(PH+4)}h{F(PW)}" class="dim"></path><text x="40" y="{F(PH+8)}" class="dt">80 mm</text>'
             f'<path d="M{F(PW+4)} 0v{F(PH)}" class="dim"></path><text x="{F(PW+6)}" y="{F(PH/2)}" class="dt" style="text-anchor:start">71</text></svg>')
CONS = [
    (L("Stitch density", "Stichdichte"), L("Topstitching 8–10 stitches per inch (3–4 per cm), copper-gold. Inner seams your standard.", "Ziernähte 8–10 Stiche pro Zoll (3–4 pro cm), Kupfer-Gold. Innennähte Standard der Fabrik.")),
    (L("Inseam", "Innennaht"), L("Flat-felled, double needle.", "Kappnaht, doppelt gesteppt.")),
    (L("Side seam", "Seitennaht"), L("Safety stitch (overlock + chain), pressed to the back, single topstitch at the top to below the front pocket.", "Sicherheitsnaht (Overlock + Kettstich), nach hinten gebügelt, oben bis unter die Vordertasche einfach abgesteppt.")),
    (L("Centre back and yoke", "Hintere Mitte und Passe"), L("Flat-felled, double needle.", "Kappnaht, doppelt gesteppt.")),
    (L("Front rise and fly", "Vordere Mitte und Schlitz"), L("Zip fly, left over right as worn. J-stitch double needle, bartack at the end.", "Reißverschluss, links über rechts vom Träger aus. J-Naht doppelt gesteppt, Riegel am Ende.")),
    (L("Waistband", "Bund"), L("4 cm, double needle top and bottom. Shank button 20 mm on the right end, buttonhole on the left (keyhole).", "4 cm, oben und unten doppelt gesteppt. Knopf 20 mm am rechten Ende, Knopfloch links (Augenknopfloch).")),
    (L("Front pockets", "Vordertaschen"), L("Double topstitch on the opening. Rivets at both ends of each opening.", "Öffnung doppelt abgesteppt. Nieten an beiden Enden jeder Öffnung.")),
    (L("Coin pocket", "Münztasche"), L("62 × 62 mm, embroidered panel E. Top edge double topstitch, rivets at both top corners.", "62 × 62 mm, bestickt mit E. Oberkante doppelt abgesteppt, Nieten an beiden oberen Ecken.")),
    (L("Back pockets", "Gesäßtaschen"), L("Top hem 15 mm, double topstitch. Bartacks at both top corners (no rivets on back pockets).", "Oberer Saum 15 mm, doppelt abgesteppt. Riegel an beiden oberen Ecken (keine Nieten hinten).")),
    (L("Belt loops", "Gürtelschlaufen"), L("5 loops, about 1.0–1.2 cm wide, 4 cm visible length, bartacked top and bottom. Centre back loop on the centre back seam. Positions: your standard for a 5-pocket jeans, shown in the flats.", "5 Schlaufen, etwa 1,0–1,2 cm breit, 4 cm sichtbar, oben und unten verriegelt. Mittelschlaufe auf der hinteren Mittelnaht. Positionen: Standard der Fabrik für 5-Pocket-Jeans, siehe Zeichnungen.")),
    (L("Hem", "Saum"), L("1 cm, chain stitch, copper-gold. The inseam of 81 cm includes the hem. The chain stitch must not rope in your wash; if it does on the hem sample (step 5), tell us before the proto.", "1 cm, Kettstich, Kupfer-Gold. Die 81 cm Innenbein schließen den Saum ein. Der Kettstich darf in der Wäsche nicht ropen (Saumkante verdreht und hell gerieben). Ropt er an der Saumprobe (Schritt 5), sagt die Fabrik es uns vor dem Proto.")),
    (L("Bartacks", "Riegel"), L("Copper-gold: fly end, belt loops, back pocket corners, crotch.", "Kupfer-Gold: Ende Schlitz, Gürtelschlaufen, Ecken der Gesäßtaschen, Schritt.")),
]
crows = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in CONS)
page(L("Construction", "Verarbeitung"), f"""
<h2>{L("Construction and stitching", "Verarbeitung und Nähte")}</h2>
<table class="kv">{crows}</table>
<div class="grid" style="align-items:center">
<div>{PATCH_SVG}</div>
<div><h3>{L("Patch D: two-layer belt loop, detachable with 4 snaps", "Patch D: Gürtelschlaufe aus zwei Lagen, abnehmbar mit 4 Druckknöpfen")}</h3><ul>
<li>{L("Position: back right as worn, centred between the centre back loop and the right side loop. Top of the patch flush with the top of the waistband.", "Sitz: hinten rechts vom Träger aus, mittig zwischen Mittelschlaufe und rechter Schlaufe. Oberkante Patch bündig mit Oberkante Bund.")}</li>
<li>{L("Grid 66 × 46 mm between snap centres. This grid is the Novalife standard and must be exact: the patch has to fit every future Novalife jeans.", "Raster 66 × 46 mm zwischen den Knopfmitten. Das Raster ist der Novalife-Standard und muss genau stimmen: Der Patch muss auf jede künftige Novalife-Jeans passen.")}</li>
<li>{L("On the jeans: 4 studs, each with a 20 × 20 mm reinforcement inside. The top two go through the waistband, the bottom two through the yoke.", "An der Jeans: 4 Unterteile, jedes innen mit 20 × 20 mm Verstärkung. Die oberen zwei sitzen im Bund, die unteren zwei in der Passe.")}</li>
<li>{L("On the patch: sockets and caps on the back panel, set by you on our patches. From outside the snaps are hidden.", "Am Patch: Oberteile und Kappen an der Rückwand, setzt die Fabrik auf unsere Patches. Von außen sind die Knöpfe nicht zu sehen.")}</li>
<li>{L("The belt runs through the patch, between back panel and front, over the upper pair of snaps. Belts up to 40 mm must pass. Ship every pair with the patch snapped on.", "Der Gürtel läuft durch den Patch, zwischen Rückwand und Vorderteil, über die oberen Knöpfe. Gürtel bis 40 mm müssen durchpassen. Jedes Paar wird mit angeknöpftem Patch verschickt.")}</li>
<li>{L("The customer removes the patch before washing the jeans: no indigo on the linen.", "Der Kunde nimmt den Patch vor dem Waschen der Jeans ab: kein Indigo auf dem Leinen.")}</li>
</ul></div>
</div>""")

# ================= 9 · Ablauf und Freigaben =================
STEPS = [
    (L("Fabric", "Stoff"), L("Swatch and shrinkage test of the bulk fabric with our wash. You set the pattern allowance from it.", "Stoffmuster und Schrumpftest des Produktionsstoffs mit unserer Wäsche. Daraus legt die Fabrik die Schrumpfzugabe fest."), L("Swatch + shrinkage values", "Stoffmuster + Schrumpfwerte")),
    (L("Colours", "Farben"), L("Thread colour card: topstitch copper-gold, embroidery bright red, white, gold, dark gold.", "Garnfarbkarte: Ziernaht Kupfer-Gold, Stickerei Knallrot, Weiß, Gold, Dunkelgold."), L("We choose on the real thread", "Wir wählen am echten Garn")),
    (L("Pattern check", "Schnitt-Maßblatt"), L("Before cutting the proto: measurement sheet of your W34 pattern for points 1–20, finished measurements after wash, and your shrinkage allowance.", "Vor dem Zuschnitt des Protos: Maßblatt des W34-Schnitts für die Punkte 1–20, Fertigmaße nach der Wäsche und Schrumpfzugabe."), L("We approve before cutting", "Freigabe vor dem Zuschnitt")),
    (L("Digitizing", "Digitizing"), L("Preview of all 4 motifs: stitch count, trims, colour changes. The embroidery files (DST) belong to Novalife.", "Vorschau aller 4 Motive: Stichzahl, Fadenschnitte, Farbwechsel. Die Stickdateien (DST) gehören Novalife."), L("PDF/photo preview", "Vorschau als PDF oder Foto")),
    (L("Strike-off", "Stickprobe"), L("Embroidery of all 4 motifs on our denim, washed with our wash recipe. No puckering or waves, red must not bleed, no frayed thread. Plus a seam and hem sample (flat-felled seam with copper-gold topstitching, 1 cm chain-stitch hem), washed the same way: no abrasion, no roping, the thread keeps its colour.", "Alle 4 Motive auf unserem Denim gestickt und mit unserer Wäsche gewaschen. Keine Wellen, Rot blutet nicht aus, kein ausgefranstes Garn. Dazu eine Naht- und Saumprobe (Kappnaht mit Kupfer-Gold-Ziernaht, 1-cm-Kettstichsaum), genauso gewaschen: kein Abrieb, kein Roping, das Garn behält seine Farbe."), L("Photos, then physical. Gate before the proto", "Erst Fotos, dann physisch. Bedingung vor dem Proto")),
    (L("Proto W34", "Proto W34"), L("Complete jeans: embroidered, washed, all trims and patch D. Measurement sheet of points 1–20 against this tech pack.", "Komplette Jeans: bestickt, gewaschen, alle Zutaten und Patch D. Maßblatt der Punkte 1–20 gegen dieses Tech Pack."), L("Fit and snap test by us", "Passform- und Druckknopf-Test durch uns")),
    (L("Wash standard", "Waschstandard"), L("2–3 wash trials on the proto. We choose one physical piece; it is the binding standard for bulk.", "2–3 Waschproben am Proto. Wir wählen ein echtes Teil, es ist der verbindliche Standard für die Produktion."), L("Signed wash standard", "Unterschriebener Waschstandard")),
    (L("PP sample", "PP-Muster"), L("Pre-production sample W34 in bulk fabric, bulk trims and bulk wash. Once approved it is sealed and is the standard for all 100 pairs. Measurement sheets for W30 and W38 from the first bulk cut.", "Vorproduktionsmuster W34 aus Produktionsstoff, mit Produktionszutaten und Produktionswäsche. Nach der Freigabe wird es versiegelt und ist der Standard für alle 100 Paare. Maßblätter für W30 und W38 aus dem ersten Produktionszuschnitt."), L("Written approval before bulk", "Schriftliche Freigabe vor der Produktion")),
    (L("TOP sample", "TOP-Muster"), L("One finished pair from the running bulk production, sent to us physically before shipment.", "Ein fertiges Paar aus der laufenden Produktion, physisch an uns vor dem Versand."), L("Approval before shipment", "Freigabe vor dem Versand")),
]
srows = "".join(f'<tr><td class="no">{i}</td><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for i, (a, b, c) in enumerate(STEPS, 1))
page(L("Process", "Ablauf"), f"""
<h2>{L("Process and approvals", "Ablauf und Freigaben")}</h2>
<table class="spec"><tr><th>{L("No.", "Nr.")}</th><th>{L("Step", "Schritt")}</th><th>{L("What", "Was")}</th><th>{L("Our approval", "Unsere Freigabe")}</th></tr>{srows}</table>
<h3>{L("Order of production", "Reihenfolge der Produktion")}</h3>
<p>{L("Cutting → <b>embroidery on the cut panels</b> (A front panel, E coin pocket, B2 and C back pockets) → sewing → laser and wash → 9 gold threads by hand → rivets, button and snap studs (after wash, to protect the antique-copper finish; tell us if you recommend otherwise) → patch D snapped on → final inspection (size and number against our list) → packing.", "Zuschnitt → <b>Stickerei auf den Zuschnittteilen</b> (A Vorderteil, E Münztasche, B2 und C Gesäßtaschen) → Nähen → Laser und Wäsche → 9 Goldfäden von Hand → Nieten, Knopf und Druckknopf-Unterteile (nach der Wäsche, schützt die Antik-Kupfer-Oberfläche; die Fabrik darf widersprechen) → Patch D anknöpfen → Endkontrolle (Größe und Nummer gegen unsere Liste) → Verpackung.")}</p>
<p class="warn"><b>{L("Biggest risk: embroidery before the wash.", "Größtes Risiko: Stickerei vor der Wäsche.")}</b> {L("The thread must survive enzyme and bleach, and the denim shrinks under the embroidery, which can cause waves. That is why the washed strike-off (step 5) must be approved before the proto. If your test shows waves, propose pre-washing the fabric or a stabiliser.", "Das Garn muss Enzym und Bleiche aushalten, und der Denim schrumpft unter der Stickerei, das kann Wellen geben. Deshalb muss die gewaschene Stickprobe (Schritt 5) vor dem Proto freigegeben sein. Zeigt der Test Wellen, schlägt die Fabrik Vorwaschen des Stoffs oder ein Stabilisierungsvlies vor.")}</p>
<table class="kv">
<tr><th>{L("Timeline", "Termine")}</th><td>{L("Proto shipped by 30 Nov 2026 · PP sample shipped by 4 Jan 2027 · bulk from mid-February · finished by 14 May 2027", "Proto verschickt bis 30.11.2026 · PP-Muster verschickt bis 04.01.2027 · Produktion ab Mitte Februar · fertig bis 14.05.2027")}</td></tr>
<tr><th>{L("Changes", "Änderungen")}</th><td>{L("No change to fabric, trims, wash or embroidery without our written approval.", "Keine Änderung an Stoff, Zutaten, Wäsche oder Stickerei ohne unsere schriftliche Freigabe.")}</td></tr>
<tr><th>{L("Ownership", "Rechte")}</th><td>{L("Design, artwork, pattern and embroidery files belong to Novalife. No reuse, resale or reproduction. Please send us the pattern and the DST files after production.", "Design, Artwork, Schnitt und Stickdateien gehören Novalife. Keine Weiterverwendung, kein Verkauf, keine Nachproduktion. Nach der Produktion schickt die Fabrik uns Schnitt und DST-Dateien.")}</td></tr>
</table>""")

# ================= 10 · Wäsche =================
page(L("Wash", "Wäsche"), f"""
<h2>{L("Wash", "Wäsche")}</h2>
<div class="refs">
<div><img src="{WASH}" alt="Wash references"><p class="sub" style="margin-top:1mm">{L("Reference collage. Colour target: model photo, middle right. Thigh fading: top right, but without nicks. Honeycombs: bottom right. Bottom left: mood only, no holes or repairs.", "Referenz-Collage. Farbziel: Model-Foto rechts in der Mitte. Oberschenkel: oben rechts, aber ohne kleine Risse. Honeycombs: unten rechts. Unten links: nur Stimmung, keine Löcher und Reparaturen.")}</p></div>
<div><img src="{HONEY}" alt="Honeycomb reference"><p class="sub" style="margin-top:1mm">{L("Honeycomb target: high contrast behind the knees. On 12 oz we expect softer contrast; show us what your laser or hand-sanding can do.", "Ziel für die Honeycombs: hoher Kontrast hinter den Knien. Auf 12 oz erwarten wir weniger Kontrast, die Fabrik zeigt, was ihr Laser oder Handschliff kann.")}</p></div>
</div>
<table class="kv">
<tr><th>{L("Colour", "Farbe")}</th><td>{L("Mid-indigo vintage with a slight grey cast. Darker than our first visual.", "Mittleres Vintage-Indigo mit leichtem Grau-Stich. Dunkler als unser erstes Bild.")}</td></tr>
<tr><th>{L("Shade (L*)", "Helligkeit (L*)")}</th><td>{L("Base shade after the base wash L* 34–40. Fades (honeycombs, thighs) L* 52–58, contrast ΔL* 15–20. Tolerance L* ± 2 against the approved standard. White embroidery needs the dark base to stay readable.", "Grundton nach der Grundwäsche L* 34–40. Aufhellungen (Honeycombs, Oberschenkel) L* 52–58, Kontrast ΔL* 15–20. Toleranz L* ± 2 zum freigegebenen Standard. Die weiße Stickerei braucht den dunklen Grund, sonst ist sie nicht lesbar.")}</td></tr>
<tr><th>{L("Must have", "Pflicht")}</th><td>{L("Honeycombs behind both knees. Fading on the front thighs.", "Honeycombs hinter beiden Knien. Aufhellung vorn auf den Oberschenkeln.")}</td></tr>
<tr><th>{L("Not wanted", "Nicht gewünscht")}</th><td>{L("Whiskers, holes, nicks or destroyed areas, sandblasting, potassium permanganate spray (PP spray). Any wash effect on sewn places: seam abrasion, roping on the hem, edge wear.", "Whiskers, Löcher, kleine Risse oder zerstörte Stellen, Sandstrahlen, Kaliumpermanganat-Spray (PP-Spray). Jeder Wascheffekt an genähten Stellen: Nahtabrieb, Roping am Saum, Kantenabrieb.")}</td></tr>
<tr><th>{L("Methods", "Methoden")}</th><td>{L("Base wash: <b>enzyme wash without stones</b> (stones rub seams and edges white), garments inside out, an anti-backstaining agent in every bath. Grey cast by tint or a light bleach only if the strike-off shows that red, white and copper-gold stay clean. Local fades: <b>laser preferred</b>, it repeats exactly over 100 numbered pairs. Hand-sanding only where the laser cannot reach. No sandblasting, no PP spray.", "Grundwäsche: <b>Enzymwäsche ohne Steine</b> (Steine reiben Nähte und Kanten hell), auf links, in jedem Bad ein Mittel gegen Rückanfärbung. Grau-Stich über Tönung oder leichte Bleiche nur, wenn die Stickprobe zeigt, dass Rot, Weiß und Kupfer-Gold sauber bleiben. Lokale Aufhellung: <b>bevorzugt Laser</b>, er wiederholt sich bei 100 nummerierten Paaren genau. Handschliff nur, wo der Laser nicht hinkommt. Kein Sandstrahlen, kein PP-Spray.")}</td></tr>
<tr><th>{L("Protected zones", "Schutzzonen")}</th><td>{L("<b>No wash effects on sewn places:</b> no laser, sanding or abrasion on seams, topstitching, bartacks, hem, waistband, belt loops, fly and pocket edges. Fades end at least 10 mm before any seam and run out softly. Mask the embroidery zones (band A, coin pocket E, both back pockets). Seat fades run out softly around both back pockets; the pocket surfaces stay clean. After the wash the copper-gold thread keeps its colour, without indigo staining.", "<b>Keine Wascheffekte an genähten Stellen:</b> kein Laser, Schliff oder Abrieb an Nähten, Ziernähten, Riegeln, Saum, Bund, Gürtelschlaufen, Schlitz und Taschenkanten. Aufhellungen enden mindestens 10 mm vor jeder Naht und laufen weich aus. Die Stickzonen (Band A, Münztasche E, beide Gesäßtaschen) abdecken. Am Gesäß läuft die Aufhellung um beide Gesäßtaschen weich aus, die Taschenflächen bleiben frei. Nach der Wäsche hat das Kupfer-Gold-Garn seine Farbe, ohne Indigo-Anfärbung.")}</td></tr>
<tr><th>{L("Approval", "Freigabe")}</th><td>{L("Shade card, then 3 wash trials on our fabric (target, lighter, darker), judged in daylight after the full wash program. We choose one; it becomes the physical wash standard.", "Farbkarte, dann 3 Waschproben auf unserem Stoff (Ziel, heller, dunkler), bei Tageslicht nach dem vollen Waschprogramm beurteilt. Wir wählen eine, sie wird der physische Waschstandard.")}</td></tr>
<tr><th>{L("Tolerance", "Toleranz")}</th><td>{L("Bulk matches the approved physical wash standard in daylight; no streaks, no shade differences within the lot.", "Die Produktion entspricht im Tageslicht dem freigegebenen Waschstandard, keine Streifen, keine Farbunterschiede innerhalb der Lieferung.")}</td></tr>
<tr><th>{L("Tests", "Prüfungen")}</th><td>{L("Residual shrinkage ≤ 3 % after a home wash at 30 °C. Rubbing fastness (ISO 105-X12): please send your result with the wash standard.", "Restschrumpf ≤ 3 % nach einer Haushaltswäsche bei 30 °C. Reibechtheit (ISO 105-X12): Ergebnis kommt mit dem Waschstandard.")}</td></tr>
</table>""")

# ================= 11 · Etiketten, Verpackung, Vorschriften =================
page(L("Labels and packing", "Etiketten und Verpackung"), f"""
<h2>{L("Labels, packing, compliance", "Etiketten, Verpackung, Vorschriften")}</h2>
<table class="kv">
<tr><th>{L("Inner label", "Innenetikett")}</th><td>{L("Printed label inside the back waistband, permanent and readable after wash. Same position on every pair.", "Bedrucktes Etikett innen am hinteren Bund, dauerhaft und nach der Wäsche lesbar. Bei jedem Paar an der gleichen Stelle.")}</td></tr>
<tr><th>{L("Side 1", "Seite 1")}</th><td>NOVALIFE · NVL-TT-01 · {L("Size", "Größe")} W34 L32 · {L("No.", "Nr.")} 001/100<br>{L("Each pair has its own number 001–100, printed on this label. We send the number list per size with the order (PO). The label is sewn in with the waistband, so size and number stay together.", "Jedes Paar hat seine eigene Nummer 001–100, aufgedruckt auf diesem Etikett. Die Nummernliste je Größe schicken wir mit der Bestellung (PO). Das Etikett wird mit dem Bund eingenäht, Größe und Nummer bleiben zusammen.")}</td></tr>
<tr><th>{L("Side 2", "Seite 2")}</th><td>100 % Baumwolle / 100 % Cotton<br>{L("Care symbols: wash 30 °C, do not bleach, do not tumble dry, iron medium (2 dots), do not dry clean", "Pflegesymbole: Wäsche 30 °C, nicht bleichen, nicht in den Trockner, mittlere Bügelstufe (2 Punkte), keine chemische Reinigung")}<br>„Vor dem ersten Tragen separat und auf links waschen. Indigo kann abfärben. Patch vor dem Waschen abnehmen. Goldfäden nicht abschneiden.“<br>Made in [{L("country", "Land")}]</td></tr>
<tr><th>{L("Patch care", "Patch-Pflege")}</th><td>{L("On the hangtag: „Patch separat von Hand waschen, 30 °C, nicht auswringen, flach trocknen, erst trocken wieder anknöpfen.“ (Hand wash the patch separately at 30 °C, do not wring, dry flat, snap on only when dry.)", "Auf dem Hangtag: „Patch separat von Hand waschen, 30 °C, nicht auswringen, flach trocknen, erst trocken wieder anknöpfen.“")}</td></tr>
<tr><th>{L("Manufacturer info", "Herstellerangaben")}</th><td>{L("Novalife · [postal address] · [e-mail]. We send the final text in January 2027 (EU General Product Safety Regulation). Style no. + serial number identify the product.", "Novalife · [Postanschrift] · [E-Mail]. Den endgültigen Text schicken wir im Januar 2027 (EU-Produktsicherheitsverordnung GPSR). Modellnummer und Seriennummer kennzeichnen das Produkt.")}</td></tr>
<tr><th>{L("Fibre content", "Faserangabe")}</th><td>{L("German wording is mandatory for Germany (EU Regulation 1007/2011). Please confirm the composition of the bulk fabric in writing.", "Für Deutschland ist die deutsche Angabe Pflicht (EU-Verordnung 1007/2011). Die Fabrik bestätigt die Zusammensetzung des Produktionsstoffs schriftlich.")}</td></tr>
<tr><th>{L("Folding", "Falten")}</th><td>{L("Folded in thirds, front out, patch D snapped on and protected with tissue so the snaps do not mark the denim.", "Gedrittelt gefaltet, Vorderseite außen, Patch D angeknöpft und mit Seidenpapier geschützt, damit die Knöpfe keine Abdrücke machen.")}</td></tr>
<tr><th>{L("Polybag", "Polybeutel")}</th><td>{L("One pair per recyclable bag, suffocation warning in German and English, sticker with size and number.", "Ein Paar pro recycelbarem Beutel, Erstickungswarnung auf Deutsch und Englisch, Aufkleber mit Größe und Nummer.")}</td></tr>
<tr><th>{L("Cartons", "Kartons")}</th><td>{L("Max. 15 kg. Marking: NOVALIFE · NVL-TT-01 · sizes and numbers inside · carton x of y.", "Höchstens 15 kg. Beschriftung: NOVALIFE · NVL-TT-01 · Größen und Nummern im Karton · Karton x von y.")}</td></tr>
<tr><th>{L("Shipping papers", "Versandpapiere")}</th><td>{L("Commercial invoice and packing list with every shipment, including proto and PP. From Turkey: ATR movement certificate for the EU-Turkey customs union. HS code 6203 42 (men's cotton trousers), please confirm.", "Handelsrechnung und Packliste bei jeder Sendung, auch bei Proto und PP. Aus der Türkei: ATR-Warenverkehrsbescheinigung für die Zollunion EU-Türkei. Zolltarifnummer 6203 42 (Herrenhosen aus Baumwolle), bitte bestätigen.")}</td></tr>
</table>
<p class="warn"><b>{L("Chemicals:", "Chemie:")}</b> {L("EU REACH applies. No banned azo dyes (Annex XVII entry 43), nickel release ≤ 0.5 µg/cm²/week on all metal parts (EN 1811), no PP spray, no sharp edges on metal parts. Please confirm with test reports or supplier declarations; an OEKO-TEX Standard 100 certificate for the fabric is welcome.", "Es gilt EU-REACH. Keine verbotenen Azofarbstoffe (Anhang XVII Nr. 43), Nickelabgabe ≤ 0,5 µg/cm²/Woche an allen Metallteilen (EN 1811), kein PP-Spray, keine scharfen Kanten an Metallteilen. Nachweis durch Prüfberichte oder Lieferantenerklärungen, ein OEKO-TEX-Standard-100-Zertifikat für den Stoff ist erwünscht.")}</p>""")

# ================= 12 · Qualitätskontrolle =================
page(L("Quality control", "Qualitätskontrolle"), f"""
<h2>{L("Quality control", "Qualitätskontrolle")}</h2>
<table class="kv">
<tr><th>{L("100 % check", "100-%-Prüfung")}</th><td>{L("Every pair is checked by the factory before packing: measurements 1, 2, 6, 7, 8 on two pairs per size, all other pairs visually.", "Die Fabrik prüft jedes Paar vor dem Verpacken: Maße 1, 2, 6, 7, 8 an zwei Paaren pro Größe, alle anderen Paare per Sichtprüfung.")}</td></tr>
<tr><th>{L("Spare pairs", "Reservepaare")}</th><td>{L("If a numbered pair fails the final inspection, replace it with a spare pair of the same size and give it the same number (new label). Unused spares get a label without number.", "Fällt ein nummeriertes Paar in der Endkontrolle durch, ersetzt es ein Reservepaar gleicher Größe mit derselben Nummer (neues Etikett). Nicht gebrauchte Reservepaare bekommen ein Etikett ohne Nummer.")}</td></tr>
<tr><th>{L("Photos", "Fotos")}</th><td>{L("Before shipment: one photo per numbered pair (front, back, inner label with number) and a short video of the final inspection. The balance is paid after we approve them.", "Vor dem Versand: ein Foto pro nummeriertem Paar (vorn, hinten, Innenetikett mit Nummer) und ein kurzes Video der Endkontrolle. Die Restzahlung erfolgt nach unserer Freigabe.")}</td></tr>
<tr><th>{L("Final inspection", "Endkontrolle")}</th><td>{L("AQL 2.5 major / 4.0 minor / 0 critical (ISO 2859-1, level II). We may send an inspector.", "AQL 2,5 schwer / 4,0 leicht / 0 kritisch (ISO 2859-1, Stufe II). Wir können einen Prüfer schicken.")}</td></tr>
</table>
<div class="grid3">
<div class="card"><h3>{L("Critical (0 allowed)", "Kritisch (0 erlaubt)")}</h3><ul>{L("<li>Holes, broken needle or sharp metal parts</li><li>Wrong or duplicate serial number</li><li>Snap opens by itself or stud comes loose</li><li>Nickel-containing metal</li>", "<li>Löcher, Nadelreste oder scharfe Metallteile</li><li>Falsche oder doppelte Nummer</li><li>Druckknopf geht von selbst auf oder Unterteil löst sich</li><li>Nickelhaltiges Metall</li>")}</ul></div>
<div class="card"><h3>{L("Major", "Schwer")}</h3><ul>{L("<li>Measurement outside tolerance</li><li>Embroidery missing, off by more than 3 mm, puckered or bleeding</li><li>Open or broken seams</li><li>Wash not matching the standard</li><li>Wash effects on seams, hem or embroidery</li><li>Label, number or gold threads missing</li><li>Legs of different length (more than 5 mm)</li>", "<li>Maß außerhalb der Toleranz</li><li>Stickerei fehlt, mehr als 3 mm verschoben, wellig oder ausgeblutet</li><li>Offene oder gerissene Nähte</li><li>Wäsche entspricht nicht dem Standard</li><li>Wascheffekte an Nähten, Saum oder Stickerei</li><li>Etikett, Nummer oder Goldfäden fehlen</li><li>Beine unterschiedlich lang (mehr als 5 mm)</li>")}</ul></div>
<div class="card"><h3>{L("Minor", "Leicht")}</h3><ul>{L("<li>Loose threads, untrimmed ends</li><li>Small marks that wash out</li><li>Slightly uneven topstitching</li>", "<li>Lose Fäden, nicht abgeschnittene Enden</li><li>Kleine Flecken, die herausgehen</li><li>Leicht ungleichmäßige Ziernaht</li>")}</ul></div>
</div>
<h3>{L("Snap and hardware test (proto and PP sample, condition for approval)", "Test von Druckknöpfen und Metallteilen (Proto und PP-Muster, Bedingung für die Freigabe)")}</h3>
<ul>
<li>{L("Pull a 40 mm belt through patch D 20 times and tighten it; sit and bend; open and close every snap 50 times.", "Einen 40-mm-Gürtel 20-mal durch Patch D ziehen und festziehen, hinsetzen und bücken, jeden Druckknopf 50-mal öffnen und schließen.")}</li>
<li>{L("The snaps must not open by themselves and the patch must not tear. Studs, rivets and button must stay firm under a 90 N pull.", "Die Druckknöpfe dürfen nicht von selbst aufgehen, der Patch darf nicht reißen. Unterteile, Nieten und Knopf müssen 90 N Zug aushalten.")}</li>
<li>{L("If the 10 mm snaps fail, we switch to 12.5 mm and adjust the grid; tell us at once.", "Halten die 10-mm-Knöpfe nicht, wechseln wir auf 12,5 mm und passen das Raster an. Die Fabrik meldet das sofort.")}</li>
<li>{L("Patch D (tested by our patch supplier): after 5 hand washes the snap grid stays 66 × 46 mm ± 0.5 mm, no fraying, no colour bleeding, interlining stays flat.", "Patch D (prüft unser Patch-Hersteller): Nach 5 Handwäschen misst das Raster noch 66 × 46 mm ± 0,5 mm, nichts franst aus, keine Farbe blutet aus, die Einlage bleibt flach.")}</li>
</ul>""")

html = (f'<!doctype html><html lang="{LANG}"><head><meta charset="utf-8"><title>NVL-TT-01 Tech Pack</title><style>{CSS}</style></head>'
        f'<body>{"".join(render())}</body></html>')
open(OUT_HTML, "w").write(html)
print("ok", LANG, len(PAGES), "pages", len(html) // 1024, "KB")
