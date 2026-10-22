# -*- coding: utf-8 -*-
# Tech Pack v1.0 (Entwurf 21.10.2026) für die gewählte Fabrik: Englisch, A4
#   Maße aus dem Messbogen (Eightyfive M, 20.10.), Entscheidungen bis 21.10. (rev6/research/techpack_checkliste.md)
#   Anhang: Artwork 1:1 (pdf/NVL-TT-01_Artwork_1to1_v1.9.pdf) wird per pdfunite angehängt
import base64, io, math, os, subprocess, tempfile
from PIL import Image
import fine as FN

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
PDF_IN = os.path.join(ROOT, "pdf", "NVL_Druckvorlage_v19_Jeans.pdf")
VIS_JPG = os.path.join(ROOT, "mockup", "NVL-TT-01_visual.jpg")
SKIZZEN = os.path.join(ROOT, "rev6", "skizzen")
OUT_HTML = os.path.join(HERE, "v19", "techpack.html")
VERSION, DATE = "v1.0 draft", "21 Oct 2026"
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

# ================= Maße: Basis W32 = Eightyfive M flach gemessen, nach der Wäsche =================
SIZES = ["W30", "W31", "W32", "W33", "W34", "W36", "W38"]
STEP = {"W30": -2, "W31": -1, "W32": 0, "W33": 1, "W34": 2, "W36": 4, "W38": 6}   # Zoll Abstand zur Basis
SPLIT = {"W30": 8, "W31": 10, "W32": 20, "W33": 14, "W34": 20, "W36": 18, "W38": 10}
# (Nr., Messpunkt, Messanleitung, Basis W32, Toleranz ±, Sprung je 1" Bund)
POM = [
    (1, "Waist, half", "Top edge of waistband, buttoned, edge to edge.", 43.0, 1.0, 1.27),
    (2, "Hip, half", "Straight across at the level of the end of the fly (J-stitch).", 52.0, 1.0, 1.27),
    (3, "Thigh, half", "One leg, 2.5 cm below crotch, at right angles to the leg.", 29.0, 0.6, 0.6),
    (4, "Knee, half", "One leg, 33 cm below crotch measured on the inseam, straight across.", 22.5, 0.5, 0.4),
    (5, "Leg opening, half", "At the hem, edge to edge.", 21.0, 0.5, 0.3),
    (6, "Front rise", "Crotch point to top of waistband along the seam, incl. waistband.", 32.0, 0.5, 0.3),
    (7, "Back rise", "Crotch point to top of waistband along the seam, incl. waistband.", 37.0, 0.6, 0.4),
    (8, "Inseam", "Crotch point to hem along the inseam. One length for all sizes (L32).", 81.0, 1.0, 0.0),
    (9, "Outseam", "Top of waistband to hem along the side seam.", 110.0, 1.0, 0.3),
    (10, "Waistband height", "Top to bottom edge of waistband.", 4.0, 0.2, 0.0),
    (11, "Fly opening", "Bottom of waistband to end of J-stitch.", 15.0, 0.3, 0.2),
    (12, "Back yoke at centre back", "Bottom of waistband to yoke seam, on the centre back seam.", 9.5, 0.3, 0.1),
    (13, "Back yoke at side seam", "Bottom of waistband to yoke seam, on the side seam.", 3.0, 0.3, 0.0),
    (14, "Back pocket to centre back", "Centre back seam to inner top corner of back pocket.", 3.5, 0.3, 0.0),
    (15, "Back pocket below waistband", "Bottom of waistband to top of back pocket, at the inner corner.", 8.5, 0.3, 0.0),
    (16, "Front pocket opening, width", "At the bottom of the waistband: side seam to start of pocket opening.", 11.0, 0.3, 0.2),
    (17, "Front pocket opening, depth", "Along the side seam: bottom of waistband to end of pocket opening.", 7.0, 0.3, 0.0),
    (18, "Belt loops, number", "2 front, 2 side back, 1 centre back.", 5, None, None),
    (19, "Belt loop length", "Visible length, top to bottom.", 4.0, 0.2, 0.0),
    (20, "Hem height", "Hem edge to hem stitch line.", 1.0, 0.2, 0.0),
]


def r1(x):
    return math.floor(x * 10 + 0.5) / 10


def fmt(x):
    return f"{x:.1f}" if isinstance(x, float) else str(x)


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
.vis{width:100%;max-height:80mm;object-fit:contain;border:0.3mm solid #d9dde4}
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
.card{border:0.3mm solid #d9dde4;border-radius:2mm;padding:2.5mm;display:flex;flex-direction:column;gap:1.5mm}
.card img{width:100%;max-height:38mm;object-fit:contain}
.note{background:#f3f5f8;border-radius:2mm;padding:2.5mm 3mm}
.warn{background:#fbf0e6;border-left:1mm solid #a8643a;border-radius:1mm;padding:2.5mm 3mm}
ul,ol{margin:0;padding-left:5mm}
li{margin-bottom:0.8mm}
.diag{display:grid;grid-template-columns:1fr 1fr;gap:6mm;padding:0 14mm}
.diag svg{width:100%;height:auto;max-height:68mm}
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
PAGES = []


def page(title, body):
    PAGES.append((title, body))


def render():
    n = len(PAGES); out = []
    for i, (title, body) in enumerate(PAGES, 1):
        out.append(f'<section class="pg"><div class="hd"><b>Novalife · NVL-TT-01 · Tech Pack {VERSION}</b>'
                   f'<span>{DATE} · page {i} of {n} · {title}</span></div>{body}'
                   '<div class="foot"><span>Novalife, Berlin, Germany · Ernest Veskimäe · ernest.veskimae@gmail.com</span>'
                   '<span>Designs, artwork and patterns are the property of Novalife and confidential.</span></div></section>')
    return out


# ================= 1 · Deckblatt =================
INDEX = ["Cover and style summary", "Design overview", "Points of measure, base size W32", "Grading W30–W38",
         "Bill of materials", "Construction and stitching", "Process and approvals", "Wash", "Labels, packing, compliance",
         "Quality control", "Annex: artwork 1:1 (4 pages)"]
page("Cover", f"""
<div><h1>NVL-TT-01 · Time Travel jeans</h1><p class="sub">Men's 5-pocket straight-leg jeans with embroidery, 100 numbered pairs. Tech pack for the nominated factory.</p></div>
<img class="vis" src="{VIS}" alt="Visual front and back">
<p class="sub">The visual shows the placement of all details. Fit and leg shape follow the measurements on pages 3–4, which are slimmer than the visual. The wash is darker than shown (page 8).</p>
<table class="kv">
<tr><th>Style</th><td>NVL-TT-01 · Time Travel · Novalife, Berlin</td></tr>
<tr><th>Quantity</th><td>100 pairs, one style, one wash, numbered 001–100 on the inner label, plus 3 spare pairs without number (W32, W34, W36)</td></tr>
<tr><th>Sizes</th><td>W30 · W31 · W32 · W33 · W34 · W36 · W38, one inseam 81 cm (L32). Base size and proto: W32.</td></tr>
<tr><th>Fabric</th><td>12 oz rigid 100 % cotton denim, no stretch, residual shrinkage ≤ 3 % after wash</td></tr>
<tr><th>Wash</th><td>Mid-indigo vintage, honeycombs behind the knees, fading on the front thighs, no whiskers, no holes</td></tr>
<tr><th>Embroidery</th><td>4 zones on the cut panels before sewing, about 28,000 stitches (annex)</td></tr>
<tr><th>Trims</th><td>YKK metal zip, 20 mm shank button, 6 rivets, 4 snaps for the detachable back patch, all antique copper, nickel-free</td></tr>
<tr><th>Reference</th><td>The measurements come from our reference jeans (size M = our W32). There is no physical sample for now: the measurements in this tech pack are binding. Before cutting the proto you send us the measurement sheet of your pattern (page 7).</td></tr>
</table>
<div class="grid">
<div><h3>Contents</h3><ol>{"".join(f"<li>{t}</li>" for t in INDEX)}</ol></div>
<div><h3>Revisions</h3><table class="kv">
<tr><th>v0.9 · 20 Oct</th><td>Quote pack (3 pages) and artwork 1:1</td></tr>
<tr><th>{VERSION} · 21 Oct</th><td>Measurements, grading, materials, construction, process, wash, labels, QC</td></tr>
<tr><th>Change · 21 Oct</th><td>3 spare pairs added. Patch D now two layers with a back panel: snaps hidden, a standard belt up to 40 mm runs through.</td></tr>
<tr><th>Next</th><td>Technical flats from the measurements (22–25 Oct)</td></tr>
</table>
<p class="sub" style="margin-top:1.5mm">This tech pack is the only valid reference. Changes only as a new version with a new date, never by chat message.</p></div>
</div>""")

# ================= 2 · Designübersicht =================
page("Design overview", f"""
<h2>Design overview: what goes where</h2>
<div class="grid3">
<div class="card"><img src="{uri(IMG['A'])}" alt="A"><h3>A · Band, right front pocket</h3><p>Cross-stitch band 23 mm wide, 17 rows, red and white. Inner edge 175 mm on the pocket opening.</p></div>
<div class="card"><img src="{uri(IMG['E'])}" alt="E"><h3>E · Coin pocket</h3><p>Pocket 62 × 62 mm, fully embroidered 60 × 60 mm, red and white. Centred between side seam and pocket rivet.</p></div>
<div class="card"><img src="{uri(IMG['D'])}" alt="D"><h3>D · Back patch</h3><p>Two-layer linen loop 80 × 71 mm, supplied by us. 4 hidden snaps, detachable. Back right, top flush with the waistband; the belt runs through.</p></div>
<div class="card"><img src="{uri(IMG['B2'])}" alt="B2"><h3>B2 · Left back pocket</h3><p>Three wheat ears on a red band (48 mm). After washing: 9 gold threads 18–30 mm set by hand, knotted inside.</p></div>
<div class="card"><img src="{uri(IMG['C'])}" alt="C"><h3>C · Right back pocket</h3><p>Eight-point star of 8 rhombi, 36 × 36 mm, 1 mm gaps, solid red, satin stitch. Same height as the B2 band.</p></div>
<div class="card"><h3>Hardware</h3><p><b>Button:</b> 20 mm shank, antique copper, eight-point star embossed.</p><p><b>Rivets:</b> 6 × 9 mm, plain antique copper: corners of both front pocket openings and of the coin pocket.</p><p><b>Snaps:</b> 4 ring-spring snaps 10 mm, hidden behind patch D (page 6).</p></div>
</div>
<table class="kv">
<tr><th>Left / right</th><td>Always as worn. The band A and coin pocket E are on the right front pocket (as worn). B2 is on the left back pocket, C and D are on the right back.</td></tr>
<tr><th>Back pockets</th><td>Top 160 mm, bottom 130 mm, sides 125 mm (inner) and 120 mm (outer), point 70 mm each side, about 150 mm high. The inner side is 5 mm higher. Same size in all sizes.</td></tr>
<tr><th>Not graded</th><td>All embroidery, coin pocket, back pockets, patch D, button, rivets and snaps are the same in every size. One embroidery program per motif.</td></tr>
<tr><th>Exact artwork</th><td>Annex, 4 pages in 1:1 scale. Print at 100 %; the check line must measure 100 mm.</td></tr>
<tr><th>Tolerance</th><td>Position of every embroidery, pocket and patch: ± 3 mm.</td></tr>
</table>""")

# ================= 3 · Messpunkte Basis W32 =================
rows = "".join(
    f'<tr><td class="no">{n}</td><td><b>{name}</b></td><td>{how}</td><td class="n base">{fmt(base)}</td>'
    f'<td class="n">{"" if tol is None else "± " + fmt(tol)}</td><td class="n">{"" if tol is None else f"{base / 2.54:.1f}"}</td></tr>' for n, name, how, base, tol, _ in POM)
page("Points of measure", f"""
<h2>Points of measure · base size W32</h2>
<div class="diag"><div>{SVG_FRONT}<div class="cap">Front</div></div><div>{SVG_BACK}<div class="cap">Back</div></div></div>
<table class="spec"><tr><th>No.</th><th>Point of measure</th><th>How to measure</th><th class="n base">W32 cm</th><th class="n">Tol.</th><th class="n">inch</th></tr>{rows}</table>
<p class="note">All measurements in cm on the <b>finished garment after wash</b>, laid flat, buttoned, not stretched. Widths 1–5 are half measurements (edge to edge, not doubled). Lengths follow the seam. Please set the shrinkage allowance of the pattern from your own wash test on our fabric.</p>""")

# ================= 4 · Gradierung =================
hdr = "".join(f'<th class="n{" base" if s == "W32" else ""}">{s}</th>' for s in SIZES)
grows = ""
for n, name, how, base, tol, step in POM:
    cells = "".join(f'<td class="n{" base" if s == "W32" else ""}">{fmt(graded(base, step, s))}</td>' for s in SIZES)
    grows += (f'<tr><td class="no">{n}</td><td>{name}</td><td class="n">{"" if tol is None else "± " + fmt(tol)}</td>'
              f'<td class="n">{"–" if not step else f"+{step:g}"}</td>{cells}</tr>')
split = "".join(f'<td class="n{" base" if s == "W32" else ""}">{SPLIT[s]}</td>' for s in SIZES)
waist_full = " · ".join(f"{s} {fmt(r1(2 * graded(43.0, 1.27, s)))}" for s in SIZES)
page("Grading", f"""
<h2>Grading W30–W38 (proposal)</h2>
<p class="sub">Grade per 1" of waist size. Between W34, W36 and W38 the step is 2". Please check against your own block and send us your comments before the proto.</p>
<table class="spec"><tr><th>No.</th><th>Point of measure</th><th class="n">Tol.</th><th class="n">Grade / 1"</th>{hdr}</tr>{grows}
<tr class="grp"><td></td><td colspan="3">Estimated quantity (final in February)</td>{split}</tr></table>
<p class="sub">Plus 3 spare pairs without number: W32, W34, W36.</p>
<div class="grid">
<div class="note"><h3>Size names</h3><p>Our size names run larger than the measured waist on purpose: relaxed straight fit, worn with a belt. Full waist in cm: {waist_full}. Size label: W.. L32.</p></div>
<div class="note"><h3>Same in all sizes</h3><p>Inseam 81 cm, waistband 4 cm, hem 1 cm, belt loops, back pocket size and position, coin pocket, all embroidery, patch D and hardware. Zip length per size: your proposal.</p></div>
</div>""")

# ================= 5 · Materialliste =================
BOM = [
    ("Shell fabric", "12 oz (approx. 400 g/m²) rigid 100 % cotton denim, 3/1 twill, indigo, no stretch. Residual shrinkage ≤ 3 % in length and width after wash.", "Body", "Factory proposes mill and article; we approve the swatch before the proto"),
    ("Pocketing", "Cotton, natural white, unprinted, your standard weight.", "Front pocket bags", "Factory"),
    ("Interlining", "Waistband: your standard. Behind each snap stud: 20 × 20 mm reinforcement inside (denim or fusible).", "Waistband, snaps", "Factory"),
    ("Topstitch thread", "Corespun poly/cotton, colour copper-gold, weight your standard for jeans.", "All visible topstitching and bartacks", "Factory, colour card to us"),
    ("Seam thread", "Tonal indigo.", "Inner seams, overlock", "Factory"),
    ("Embroidery thread", "Polyester, wash- and bleach-resistant (e.g. Madeira Polyneon or equivalent). Red, white, gold (non-metallic).", "A, E, B2, C", "Factory, colour card to us"),
    ("Embroidery backing", "Cut-away backing, wash-resistant, trimmed 3–5 mm around each motif. Stitch density: your proposal in the digitizing preview.", "A, E, B2, C", "Factory"),
    ("Gold threads B2", "9 pieces, 18–30 mm, same gold as the embroidery, set by hand after wash, knotted inside the pocket.", "Left back pocket", "Factory"),
    ("Zipper", "YKK metal, antique copper finish, auto-lock slider, tonal tape. Length per size: your proposal.", "Fly", "Factory"),
    ("Shank button", "20 mm (ligne 32), antique copper, eight-point star embossed, nickel-free. Custom tooling.", "Waistband, 1 pc", "Factory sources, sample to us"),
    ("Rivets", "9 mm, plain, antique copper, nickel-free.", "6 pcs: front pocket openings and coin pocket corners", "Factory"),
    ("Snaps", "Ring-spring snaps 10 mm, antique copper, nickel-free. One system for stud, socket and cap.", "4 sets: studs on jeans, sockets and caps on the back panel of patch D", "Factory sources and sets both parts"),
    ("Patch D", "Two layers: embroidered linen front 80 × 71 mm and back panel, joined in the middle 30 mm at top and bottom, open at the sides. Pre-shrunk, sealed edges, sew-in stiff interlining, colourfast threads, without snaps. Washable by hand on its own.", "Back right", "Supplied by Novalife"),
    ("Inner label", "Printed, permanent, readable after washing. Content on page 9.", "Inside back waistband", "Factory prints, text from us"),
    ("Polybag", "Recyclable LDPE, one pair per bag, suffocation warning in German and English.", "Packing", "Factory"),
    ("Hangtag", "Design follows (supplied by Novalife or printed by factory, to be agreed).", "Left back belt loop", "Open"),
]
brows = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in BOM)
page("Bill of materials", f"""
<h2>Bill of materials</h2>
<table class="spec"><tr><th>Item</th><th>Description</th><th>Where / quantity</th><th>Source</th></tr>{brows}</table>
<p class="warn"><b>All metal parts nickel-free</b> (EU REACH: nickel release ≤ 0.5 µg/cm²/week, EN 1811). Please send the supplier declaration or test report with the hardware samples. All trims antique copper in the same tone.</p>
<p class="note">Please send for approval before the proto: fabric swatch with shrinkage result, thread colour card (topstitch and embroidery), button and snap samples. Article numbers and suppliers: please fill in and return this page.</p>""")

# ================= 6 · Verarbeitung =================
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
             f'<text x="40" y="26" class="tt">belt up to 40 mm runs through</text>'
             f'<path d="M0 {F(PH+4)}h{F(PW)}" class="dim"></path><text x="40" y="{F(PH+8)}" class="dt">80 mm</text>'
             f'<path d="M{F(PW+4)} 0v{F(PH)}" class="dim"></path><text x="{F(PW+6)}" y="{F(PH/2)}" class="dt" style="text-anchor:start">71</text></svg>')
CONS = [
    ("Stitch density", "Topstitching 8–10 stitches per inch (3–4 per cm), copper-gold. Inner seams your standard."),
    ("Inseam", "Flat-felled, double needle."),
    ("Side seam", "Safety stitch (overlock + chain), pressed to the back, single topstitch at the top to below the front pocket."),
    ("Centre back and yoke", "Flat-felled, double needle."),
    ("Front rise and fly", "Zip fly, left over right as worn. J-stitch double needle, bartack at the end."),
    ("Waistband", "4 cm, double needle top and bottom. Shank button 20 mm on the right end, buttonhole on the left (keyhole)."),
    ("Front pockets", "Double topstitch on the opening. Rivets at both ends of each opening."),
    ("Coin pocket", "62 × 62 mm, embroidered panel E. Top edge double topstitch, rivets at both top corners."),
    ("Back pockets", "Top hem 15 mm, double topstitch. Bartacks at both top corners (no rivets on back pockets)."),
    ("Belt loops", "5 loops, about 1.0–1.2 cm wide, 4 cm visible length, bartacked top and bottom. Centre back loop on the centre back seam. Positions: your standard for a 5-pocket jeans, shown in the flats."),
    ("Hem", "1 cm, chain stitch."),
    ("Bartacks", "Copper-gold: fly end, belt loops, back pocket corners, crotch."),
]
crows = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in CONS)
page("Construction", f"""
<h2>Construction and stitching</h2>
<table class="kv">{crows}</table>
<div class="grid" style="align-items:center">
<div>{PATCH_SVG}</div>
<div><h3>Patch D: two-layer belt loop, detachable with 4 snaps</h3><ul>
<li>Position: back right as worn, centred between the centre back loop and the right side loop. Top of the patch flush with the top of the waistband.</li>
<li>Grid 66 × 46 mm between snap centres. This grid is the Novalife standard and must be exact: the patch has to fit every future Novalife jeans.</li>
<li>On the jeans: 4 studs, each with a 20 × 20 mm reinforcement inside. The top two go through the waistband, the bottom two through the yoke.</li>
<li>On the patch: sockets and caps on the back panel, set by you on our patches. From outside the snaps are hidden.</li>
<li>The belt runs through the patch, between back panel and front, over the upper pair of snaps. Belts up to 40 mm must pass. Ship every pair with the patch snapped on.</li>
<li>The customer removes the patch before washing the jeans: no indigo on the linen.</li>
</ul></div>
</div>""")

# ================= 7 · Ablauf und Freigaben =================
STEPS = [
    ("Fabric", "Swatch and shrinkage test of the bulk fabric with our wash. You set the pattern allowance from it.", "Swatch + shrinkage values"),
    ("Colours", "Thread colour card: topstitch copper-gold, embroidery red, white, gold.", "We choose on the real thread"),
    ("Pattern check", "Before cutting the proto: measurement sheet of your W32 pattern for points 1–20, finished measurements after wash, and your shrinkage allowance.", "We approve before cutting"),
    ("Digitizing", "Preview of all 4 motifs: stitch count, trims, colour changes. The embroidery files (DST) belong to Novalife.", "PDF/photo preview"),
    ("Strike-off", "Embroidery of all 4 motifs on our denim, washed with our wash recipe. No puckering or waves, red must not bleed, no frayed thread.", "Photos, then physical. Gate before the proto"),
    ("Proto W32", "Complete jeans: embroidered, washed, all trims and patch D. Measurement sheet of points 1–20 against this tech pack.", "Fit and snap test by us"),
    ("Wash standard", "2–3 wash trials on the proto. We choose one physical piece; it is the binding standard for bulk.", "Signed wash standard"),
    ("PP sample", "Pre-production sample W32 in bulk fabric, bulk trims and bulk wash. Once approved it is sealed and is the standard for all 100 pairs. Measurement sheets for W30 and W38 from the first bulk cut.", "Written approval before bulk"),
    ("TOP sample", "One finished pair from the running bulk production, sent to us physically before shipment.", "Approval before shipment"),
]
srows = "".join(f'<tr><td class="no">{i}</td><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for i, (a, b, c) in enumerate(STEPS, 1))
page("Process", f"""
<h2>Process and approvals</h2>
<table class="spec"><tr><th>No.</th><th>Step</th><th>What</th><th>Our approval</th></tr>{srows}</table>
<h3>Order of production</h3>
<p>Cutting → <b>embroidery on the cut panels</b> (A front panel, E coin pocket, B2 and C back pockets) → sewing → wash → 9 gold threads by hand → rivets, button and snap studs (after wash, to protect the antique-copper finish; tell us if you recommend otherwise) → patch D snapped on → numbering → final inspection → packing.</p>
<p class="warn"><b>Biggest risk: embroidery before the wash.</b> The thread must survive enzyme and bleach, and the denim shrinks under the embroidery, which can cause waves. That is why the washed strike-off (step 4) must be approved before the proto. If your test shows waves, propose pre-washing the fabric or a stabiliser.</p>
<table class="kv">
<tr><th>Timeline</th><td>Proto shipped by 30 Nov 2026 · PP sample shipped by 4 Jan 2027 · bulk from mid-February · finished by 14 May 2027</td></tr>
<tr><th>Changes</th><td>No change to fabric, trims, wash or embroidery without our written approval.</td></tr>
<tr><th>Ownership</th><td>Design, artwork, pattern and embroidery files belong to Novalife. No reuse, resale or reproduction. Please send us the pattern and the DST files after production.</td></tr>
</table>""")

# ================= 8 · Wäsche =================
page("Wash", f"""
<h2>Wash</h2>
<div class="refs">
<div><img src="{WASH}" alt="Wash references"><p class="sub" style="margin-top:1mm">Reference collage. Colour target: model photo, middle right. Thigh fading: top right, but without nicks. Honeycombs: bottom right. Bottom left: mood only, no holes or repairs.</p></div>
<div><img src="{HONEY}" alt="Honeycomb reference"><p class="sub" style="margin-top:1mm">Honeycomb target: high contrast behind the knees. On 12 oz we expect softer contrast; show us what your laser or hand-sanding can do.</p></div>
</div>
<table class="kv">
<tr><th>Colour</th><td>Mid-indigo vintage with a slight grey cast. Darker than our first visual.</td></tr>
<tr><th>Must have</th><td>Honeycombs behind both knees. Fading on the front thighs.</td></tr>
<tr><th>Not wanted</th><td>Whiskers, holes, nicks or destroyed areas, sandblasting, potassium permanganate spray (PP spray).</td></tr>
<tr><th>Methods</th><td>Laser and/or hand-sanding, enzyme or ozone. Your proposal, without sandblasting and PP spray.</td></tr>
<tr><th>Embroidery</th><td>No abrasion over the embroidery zones (band A, coin pocket E, both back pockets): mask them during laser and sanding.</td></tr>
<tr><th>Tolerance</th><td>Bulk matches the approved physical wash standard in daylight; no streaks, no shade differences within the lot.</td></tr>
<tr><th>Tests</th><td>Residual shrinkage ≤ 3 % after a home wash at 30 °C. Rubbing fastness (ISO 105-X12): please send your result with the wash standard.</td></tr>
</table>""")

# ================= 9 · Etiketten, Verpackung, Vorschriften =================
page("Labels and packing", f"""
<h2>Labels, packing, compliance</h2>
<table class="kv">
<tr><th>Inner label</th><td>Printed label inside the back waistband, permanent and readable after wash. Same position on every pair.</td></tr>
<tr><th>Side 1</th><td>NOVALIFE · NVL-TT-01 · Size W32 L32 · No. 001/100<br>Each pair has its own number 001–100. We send the number list per size before packing.</td></tr>
<tr><th>Side 2</th><td>100 % Baumwolle / 100 % Cotton<br>Care symbols: wash 30 °C, do not bleach, do not tumble dry, iron medium (2 dots), do not dry clean<br>„Vor dem ersten Tragen separat und auf links waschen. Indigo kann abfärben. Patch vor dem Waschen abnehmen.“<br>Made in [country]</td></tr>
<tr><th>Patch care</th><td>On the hangtag: „Patch separat von Hand waschen, 30 °C, nicht auswringen, flach trocknen, erst trocken wieder anknöpfen.“ (Hand wash the patch separately at 30 °C, do not wring, dry flat, snap on only when dry.)</td></tr>
<tr><th>Manufacturer info</th><td>Novalife · [postal address] · [e-mail]. We send the final text in January 2027 (EU General Product Safety Regulation). Style no. + serial number identify the product.</td></tr>
<tr><th>Fibre content</th><td>German wording is mandatory for Germany (EU Regulation 1007/2011). Please confirm the composition of the bulk fabric in writing.</td></tr>
<tr><th>Folding</th><td>Folded in thirds, front out, patch D snapped on and protected with tissue so the snaps do not mark the denim.</td></tr>
<tr><th>Polybag</th><td>One pair per recyclable bag, suffocation warning in German and English, sticker with size and number.</td></tr>
<tr><th>Cartons</th><td>Max. 15 kg. Marking: NOVALIFE · NVL-TT-01 · sizes and numbers inside · carton x of y.</td></tr>
<tr><th>Shipping papers</th><td>Commercial invoice and packing list with every shipment, including proto and PP. From Turkey: ATR movement certificate for the EU-Turkey customs union. HS code 6203 42 (men's cotton trousers), please confirm.</td></tr>
</table>
<p class="warn"><b>Chemicals:</b> EU REACH applies. No banned azo dyes (Annex XVII entry 43), nickel release ≤ 0.5 µg/cm²/week on all metal parts (EN 1811), no PP spray, no sharp edges on metal parts. Please confirm with test reports or supplier declarations; an OEKO-TEX Standard 100 certificate for the fabric is welcome.</p>""")

# ================= 10 · Qualitätskontrolle =================
page("Quality control", """
<h2>Quality control</h2>
<table class="kv">
<tr><th>100 % check</th><td>Every pair is checked by the factory before packing: measurements 1, 2, 6, 7, 8 on two pairs per size, all other pairs visually.</td></tr>
<tr><th>Spare pairs</th><td>If a numbered pair fails the final inspection, replace it with a spare pair of the same size and give it the same number (new label). Unused spares get a label without number.</td></tr>
<tr><th>Photos</th><td>Before shipment: one photo per numbered pair (front, back, inner label with number) and a short video of the final inspection. The balance is paid after we approve them.</td></tr>
<tr><th>Final inspection</th><td>AQL 2.5 major / 4.0 minor / 0 critical (ISO 2859-1, level II). We may send an inspector.</td></tr>
</table>
<div class="grid3">
<div class="card"><h3>Critical (0 allowed)</h3><ul><li>Holes, broken needle or sharp metal parts</li><li>Wrong or duplicate serial number</li><li>Snap opens by itself or stud comes loose</li><li>Nickel-containing metal</li></ul></div>
<div class="card"><h3>Major</h3><ul><li>Measurement outside tolerance</li><li>Embroidery missing, off by more than 3 mm, puckered or bleeding</li><li>Open or broken seams</li><li>Wash not matching the standard</li><li>Label, number or gold threads missing</li></ul></div>
<div class="card"><h3>Minor</h3><ul><li>Loose threads, untrimmed ends</li><li>Small marks that wash out</li><li>Slightly uneven topstitching</li></ul></div>
</div>
<h3>Snap and hardware test (proto and PP sample, condition for approval)</h3>
<ul>
<li>Pull a 40 mm belt through patch D 20 times and tighten it; sit and bend; open and close every snap 50 times.</li>
<li>The snaps must not open by themselves and the patch must not tear. Studs, rivets and button must stay firm under a 90 N pull.</li>
<li>If the 10 mm snaps fail, we switch to 12.5 mm and adjust the grid; tell us at once.</li>
<li>Patch D (tested by our patch supplier): after 5 hand washes the snap grid stays 66 × 46 mm ± 0.5 mm, no fraying, no colour bleeding, interlining stays flat.</li>
</ul>""")

html = (f'<!doctype html><html><head><meta charset="utf-8"><title>NVL-TT-01 Tech Pack</title><style>{CSS}</style></head>'
        f'<body>{"".join(render())}</body></html>')
open(OUT_HTML, "w").write(html)
print("ok", len(PAGES), "pages", len(html) // 1024, "KB")
