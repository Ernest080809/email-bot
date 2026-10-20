# -*- coding: utf-8 -*-
# Quote Pack v0.9 (20.10.2026) für die Fabrik-Angebote: Englisch, 3 Seiten A4
#   Bilder: Ausschnitte aus Druckvorlage v1.9 (pdftoppm) und Mockup v1.9, Patch-Bauplan neu als SVG
import base64, io, os, subprocess, tempfile
from PIL import Image
import fine as FN

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
PDF_IN = os.path.join(ROOT, "pdf", "NVL_Druckvorlage_v19_Jeans.pdf")
MOCK = os.path.join(ROOT, "mockup", "NVL_Mockup_v19_Jeans.png")
OUT_HTML = os.path.join(HERE, "v19", "quote_pack.html")
OUT_JPG = os.path.join(ROOT, "mockup", "NVL-TT-01_visual.jpg")
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


IMG = {
    "E": crop(2, 13, 49, 77, 113), "A": crop(2, 40, 146, 197, 267), "K": crop(2, 156, 50, 184, 78),
    "N": crop(2, 146, 92, 194, 114), "B2": crop(3, 24, 61, 186, 213), "C": crop(4, 24, 61, 186, 213),
    "D": crop(5, 13, 55, 95, 128),
}
from PIL import ImageDraw                              # deutsche Beschriftung links neben Band A überdecken
ImageDraw.Draw(IMG["A"]).rectangle((0, int(14 * K), int(68 * K), int(44 * K)), fill="white")
mock = Image.open(MOCK).convert("RGB")
vis = mock.crop((0, 210, mock.width, mock.height - 40))
vis.resize((1600, int(1600 * vis.height / vis.width)), Image.LANCZOS).save(OUT_JPG, "JPEG", quality=82)
VIS = uri(vis.resize((1300, int(1300 * vis.height / vis.width)), Image.LANCZOS), "JPEG", 80)

# Patch-Bauplan (Englisch): Umriss, 4 Druckknöpfe, Raster
PW, PH, PB, SIN, SD = 80.0, 71.0, 5.5, 7.0, 10.0
GX, GY = PW - 2 * SIN, PH - 2 * PB - 2 * SIN
snaps = "".join(f'<circle cx="{F(x)}" cy="{F(y)}" r="{F(SD/2)}" class="snap"></circle><circle cx="{F(x)}" cy="{F(y)}" r="{F(SD*0.36)}" class="snapr"></circle>'
                for x in (SIN, SIN + GX) for y in (PB + SIN, PB + SIN + GY))
PATCH_SVG = (f'<svg viewBox="-12 -8 104 92" class="plan"><path d="{FN.patch_outline(0, 0, PW, PH, PB)}" class="po"></path>{snaps}'
             f'<path d="M{F(SIN)} {F(PB+SIN)}h{F(GX)}M{F(SIN)} {F(PB+SIN)}v{F(GY)}" class="dim"></path>'
             f'<text x="40" y="{F(PB+SIN-2)}" class="dt">{F(GX)} mm</text>'
             f'<text x="{F(SIN+2)}" y="{F(PB+SIN+GY/2+1)}" class="dt" style="text-anchor:start">{F(GY)} mm</text>'
             f'<rect x="{F(SIN+SD/2+1)}" y="{F(PH/2-9)}" width="{F(GX-SD-2)}" height="18" class="tun"></rect>'
             f'<text x="40" y="{F(PH/2+1.2)}" class="tt">belt runs behind</text>'
             f'<path d="M0 {F(PH+4)}h{F(PW)}" class="dim"></path><text x="40" y="{F(PH+8)}" class="dt">80 mm</text>'
             f'<path d="M{F(PW+4)} 0v{F(PH)}" class="dim"></path><text x="{F(PW+6)}" y="{F(PH/2)}" class="dt" style="text-anchor:start">71</text></svg>')

CSS = """
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;font-family:Helvetica,Arial,sans-serif;color:#1b2230;font-size:9.5pt;line-height:1.38}
.pg{width:210mm;height:297mm;padding:13mm 14mm 11mm;overflow:hidden;break-after:page;display:flex;flex-direction:column;gap:4mm}
.hd{display:flex;justify-content:space-between;align-items:baseline;border-bottom:0.4mm solid #1b2230;padding-bottom:2mm}
.hd b{font-size:8pt;letter-spacing:.12em;text-transform:uppercase}
.hd span{font-size:8pt;color:#68707e}
h1{font-size:20pt;margin:0;line-height:1.1}
h2{font-size:12pt;margin:0 0 2mm}
.sub{color:#4a5262;margin:1mm 0 0}
.vis{width:100%;max-height:112mm;object-fit:contain;border:0.3mm solid #d9dde4}
table{width:100%;border-collapse:collapse}
td,th{text-align:left;vertical-align:top;padding:1.3mm 2mm;border-bottom:0.25mm solid #e1e4ea}
th{width:31mm;font-weight:700}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.card{border:0.3mm solid #d9dde4;border-radius:2mm;padding:3mm;display:flex;flex-direction:column;gap:2mm}
.card img{width:100%;max-height:50mm;object-fit:contain}
.card h3{margin:0;font-size:10.5pt}
.card p{margin:0}
.note{background:#f3f5f8;border-radius:2mm;padding:3mm}
.chg li{margin-bottom:1mm}
.plan{width:70mm}
.po{fill:#efe7d6;stroke:#1b2230;stroke-width:0.3}
.snap{fill:#a8643a;stroke:#6f3d1f;stroke-width:0.3}.snapr{fill:none;stroke:#6f3d1f;stroke-width:0.3}
.dim{fill:none;stroke:#8a8f99;stroke-width:0.25;stroke-dasharray:1 0.8}
.dt{font-size:3px;fill:#68707e;text-anchor:middle;font-family:Helvetica,Arial,sans-serif}
.tun{fill:none;stroke:#4a6fa5;stroke-width:0.4;stroke-dasharray:2 1.4}
.tt{font-size:3.2px;fill:#4a6fa5;text-anchor:middle;font-family:Helvetica,Arial,sans-serif}
.foot{margin-top:auto;font-size:7.5pt;color:#68707e;border-top:0.25mm solid #e1e4ea;padding-top:2mm}
"""


def page(n, body):
    return (f'<section class="pg"><div class="hd"><b>Novalife · NVL-TT-01 · Quote Pack v0.9</b><span>20 Oct 2026 · page {n} of 3</span></div>{body}'
            '<div class="foot">Novalife, Berlin, Germany · Ernest Veskimäe · ernest.veskimae@gmail.com · Designs, artwork and patterns are the property of Novalife and confidential.</div></section>')


p1 = page(1, f"""
<div><h1>Embroidered straight-leg jeans, 100 pairs</h1><p class="sub">For your price quotation. This is a short version; the full tech pack with measurement and grading chart follows once we have chosen our partner.</p></div>
<img class="vis" src="{VIS}" alt="Visual">
<p class="sub">Visual only: it shows placement of all details. The fit follows our reference jeans (straight leg). The wash is darker than shown: see below.</p>
<table>
<tr><th>Quantity</th><td>100 pairs, one style, one wash. Sizes W30–W38, estimated split: W30 8 · W31 10 · W32 20 · W33 14 · W34 20 · W36 18 · W38 10 (final split in February).</td></tr>
<tr><th>Fit</th><td>Men's 5-pocket, straight leg, base size M = W34. Reference jeans, measured flat in cm: waist 43 · hip 52 · thigh 29 · knee 22.5 · leg opening 21 · front rise 32 · back rise 37 · inseam 78. Full spec sheet with grading follows.</td></tr>
<tr><th>Fabric</th><td>12 oz rigid 100 % cotton denim, no stretch, residual shrinkage ≤ 3 % after wash.</td></tr>
<tr><th>Wash</th><td>Mid-indigo vintage wash, honeycombs behind the knees, light fading on the front thighs. No holes, no sandblasting, no potassium permanganate spray. Reference photos follow.</td></tr>
<tr><th>Embroidery</th><td>4 zones on cut panels before sewing, approx. 28,000 stitches in total, polyester thread that resists the wash (page 2).</td></tr>
<tr><th>Trims</th><td>Zip fly with 20 mm (ligne 32) custom shank button, antique copper, embossed eight-point star. 6 rivets 9 mm, plain antique copper. All metal parts nickel-free (EU REACH).</td></tr>
<tr><th>Back patch</th><td>Linen patch 80 × 71 mm, supplied by us, detachable with 4 ring-spring snaps 10 mm (page 3).</td></tr>
<tr><th>Labels</th><td>Printed inner waistband label with serial number 001–100 plus fibre content and care in German (text supplied by us).</td></tr>
</table>""")

p2 = page(2, f"""
<h2>Embroidery and hardware (shown 1:1 in our artwork file)</h2>
<div class="grid">
<div class="card"><img src="{uri(IMG['A'])}" alt="A"><h3>A · Band along the right front pocket</h3><p>23 mm wide, 17 cross-stitch rows, red and white. Inner edge 175 mm on the pocket opening (base size M).</p></div>
<div class="card"><img src="{uri(IMG['E'])}" alt="E"><h3>E · Fully embroidered coin pocket</h3><p>Pocket 62 × 62 mm, embroidery 60 × 60 mm, 45 × 45 cross-stitches, red and white. Centred between side seam and pocket rivet.</p></div>
<div class="card"><img src="{uri(IMG['B2'])}" alt="B2"><h3>B2 · Left back pocket</h3><p>Three wheat ears on a red band (band 48 mm), gold, red, white. After washing: 9 short gold threads (18–30 mm) set by hand under the band and knotted inside the pocket.</p></div>
<div class="card"><img src="{uri(IMG['C'])}" alt="C"><h3>C · Right back pocket</h3><p>Eight-point star of 8 rhombi, 36 × 36 mm, 1 mm gaps, solid red, satin stitch. Same height as the B2 band.</p></div>
</div>
<div class="grid">
<div class="card"><img src="{uri(IMG['K'])}" alt="K" style="max-height:22mm"><h3>Button</h3><p>20 mm shank button, antique copper, eight-point star embossed. Tooling cost please quote separately.</p></div>
<div class="card"><img src="{uri(IMG['N'])}" alt="N" style="max-height:22mm"><h3>Rivets</h3><p>6 × 9 mm, plain antique copper: front pocket corners and coin pocket corners.</p></div>
</div>
<p class="note">Back pockets: top 160 mm, bottom 130 mm, sides 125 mm (inner) and 120 mm (outer), point 70 mm each side, about 150 mm high. Thread colours to be chosen from your colour card.</p>""")

p3 = page(3, f"""
<h2>Back patch D: detachable with snaps</h2>
<div class="grid">
<div class="card"><img src="{uri(IMG['D'])}" alt="D"><h3>Artwork (supplied by us)</h3><p>Embroidered linen patch, 80 mm wide, 71 mm high in the middle, 60 mm at the sides, max. 4 thread colours: dark brown, gold, red, copper.</p></div>
<div class="card">{PATCH_SVG}<h3>Construction</h3><p>4 ring-spring snaps 10 mm, antique copper, grid 66 × 46 mm. Cap and socket on the patch (stiff interlining), studs on the jeans with 20 × 20 mm reinforcement inside. Position: back right, centred between centre back loop and right loop, top of the patch flush with the top of the waistband. Belt runs behind the patch.</p></div>
</div>
<h2>What we need in your quotation</h2>
<table>
<tr><th>Price</th><td>Price per pair at 100 pcs including fabric, embroidery, wash, zipper, button, rivets, snaps, labels and hand-set threads. EXW and DAP Berlin.</td></tr>
<tr><th>One-off costs</th><td>Sample (proto and pre-production sample), embroidery digitizing, tooling for button and snaps.</td></tr>
<tr><th>Terms</th><td>Payment terms, lead time for sample and bulk, factory holidays Dec 2026 – May 2027.</td></tr>
<tr><th>Process</th><td>Who embroiders and who washes (in-house or partner), and whether you can do a wash test on an embroidered panel before the proto.</td></tr>
</table>
<h2>Timeline</h2>
<table>
<tr><th>Partner chosen</th><td>Monday 26 October 2026, full tech pack the same week</td></tr>
<tr><th>Proto</th><td>early December 2026</td></tr>
<tr><th>Pre-production sample</th><td>4 January 2027</td></tr>
<tr><th>Bulk</th><td>mid-February to mid-May 2027</td></tr>
</table>""")

html = f'<!doctype html><html><head><meta charset="utf-8"><title>NVL-TT-01 Quote Pack</title><style>{CSS}</style></head><body>{p1}{p2}{p3}</body></html>'
open(OUT_HTML, "w").write(html)
print("ok", len(html) // 1024, "KB")
