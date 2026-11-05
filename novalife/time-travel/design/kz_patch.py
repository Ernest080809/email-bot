# -*- coding: utf-8 -*-
# Patch D als PDF für Kuzgunlar (Nargiza, WhatsApp 05.11.2026: „поделиться форматом пдф для патча“)
#   Seite 1 Vorlage 1:1 mit Maßen und Garnfarben, Seite 2 vergrößert mit Farbzuordnung, Seite 3 Aufbau.
#   Bild: v19/patch_d_clean.png (patch_clean.py, ohne die sichtbaren Druckknöpfe). Ausgabe v19/kz_patch.html, PDF über kz_patch.mjs.
import base64, io, os
from PIL import Image
import kz_spec as KZ
import fine as FN

HERE = os.path.dirname(os.path.abspath(__file__))
F = FN.F
RED = KZ.RED
im = Image.open(os.path.join(HERE, "v19", "patch_d_clean.png"))
b = io.BytesIO(); im.save(b, "PNG")
PNG = "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()
OUTLINE = FN.patch_outline(0, 0, 80, 71, 5.5)
COL = [("19-1432 TCX", "Chocolate Fondant", "#56352D", "Dark brown", "tree: trunk, branches, roots, outlines"),
       ("17-1340 TCX", "Adobe", "#A3623B", "Copper-gold", "highlights in trunk and branches, outer border stitching"),
       ("14-0952 TCX", "Spicy Mustard", "#D8AE47", "Gold", "knotwork, inner circle, corner ornaments, letters NL"),
       ("18-1662 TCX", "Flame Scarlet", "#CD212A", "Bright red", "the 4 small rhombi (top, bottom, left, right)")]


def art(scale_mm_w, callouts=False):
    """Patch in echter Größe: viewBox in mm, Breite in mm, damit 100 % Druck 1:1 ist."""
    d = KZ.Dim(.5 if not callouts else .35, 3.4 if not callouts else 2.4)
    parts = [f'<defs><clipPath id="pc{int(callouts)}"><path d="{OUTLINE}"></path></clipPath></defs>',
             f'<image href="{PNG}" x="0" y="0" width="80" height="71" preserveAspectRatio="none" clip-path="url(#pc{int(callouts)})"></image>',
             f'<path d="{OUTLINE}" style="fill: none; stroke: #1b2230; stroke-width: {.35 if not callouts else .25}"></path>']
    if not callouts:
        d.ext(0, 5.5, 0, -8); d.ext(80, 5.5, 80, -8); d.line(0, -5.5, 80, -5.5); d.ann(40, -9.5, None, "8 cm")
        d.ext(40, 0, 96, 0); d.ext(40, 71, 96, 71); d.line(92, 0, 92, 71); d.ann(101, 35.5, None, "7.1 cm")
        d.ext(0, 5.5, -11, 5.5); d.ext(0, 65.5, -11, 65.5); d.line(-8, 5.5, -8, 65.5); d.ann(-15, 35.5, None, "6 cm")
        vb, w = "-24 -16 134 92", 134 * scale_mm_w / 134
    else:
        for i, (x, y) in enumerate(SPOTS, 1):
            d.o.append(f'<circle cx="{F(x)}" cy="{F(y)}" r="2.3" style="fill: {RED}; stroke: #fff; stroke-width: .4"></circle>'
                       f'<text x="{F(x)}" y="{F(y + 1.05)}" style="font: 700 3px \'Roboto Condensed\', Arial, sans-serif; fill: #fff; text-anchor: middle">{i}</text>')
        vb, w = "-2 -2 84 75", 168                                    # 84 Einheiten auf 168 mm = genau 2:1
    return d.svg(vb, parts, f"width:{F(w)}mm;height:auto;display:block;margin:0 auto")


SPOTS = [(40, 46), (33, 22), (17, 34), (40, 60), (46.5, 66.5), (4.5, 12), (77, 50)]
SPOT_TXT = [("19-1432 TCX", "Dark brown", "trunk, roots, branches, outlines of the tree"),
            ("17-1340 TCX", "Copper-gold", "highlights in trunk and branches"),
            ("14-0952 TCX", "Gold", "knotwork left and right, inner circle"),
            ("14-0952 TCX", "Gold", "letters NL"),
            ("18-1662 TCX", "Bright red", "4 small rhombi: top, bottom (marked), left, right"),
            ("14-0952 TCX", "Gold", "corner ornaments (no snaps here, linen stays free in the very corner)"),
            ("17-1340 TCX", "Copper-gold", "outer border stitching around the patch")]


def spots():
    hexes = {c: h for c, n, h, r, w in COL}
    rows = "".join(f'<tr><td class="no"><i>{i}</i></td><td><i class="sw" style="background:{hexes[c]}"></i></td><td><b>{c}</b> · {r}</td><td>{w}</td></tr>'
                   for i, (c, r, w) in enumerate(SPOT_TXT, 1))
    return f'<table class="cl sp2"><tr><th></th><th></th><th>Colour</th><th>Area</th></tr>{rows}</table>'


def legend():
    rows = "".join(f'<tr><td><i style="background:{h}"></i></td><td><b>{c}</b><br><span>{n}</span></td><td>{role}</td><td>{where}</td></tr>' for c, n, h, role, where in COL)
    return f'<table class="cl"><tr><th></th><th>Pantone</th><th>Colour</th><th>Where</th></tr>{rows}</table>'


def page(n, title, body):
    return (f'<section class="pg">{KZ.header(title)}{body}<div class="ft"><span>NVL-TT-01 · patch D artwork v1.0 · 05 Nov 2026 · same patch for all sizes</span>'
            f'<span>page {n} of 3</span></div></section>')


RU = "Печатать в масштабе 100 %. Вышивка на натуральном льне, не более 4 цветов ниток. 4 кнопки не вышиваются и не видны: они спрятаны сзади."
pages = [
    page(1, "BACK PATCH · D · ARTWORK 1:1", KZ.note("Print at 100 % (actual size), not “fit to page”. Embroidery on pre-shrunk natural linen, max. 4 thread colours. "
                                                   "The 4 snaps are NOT embroidered and NOT visible: they sit hidden behind the patch.")
         + f'<p class="ru">{RU}</p><div class="art">{art(134)}</div>'
         '<div class="chk"><div class="ln"></div><span>Check: this line must measure exactly 100 mm</span></div>'
         f'<h4 class="h4">THREAD COLOURS · max. 4</h4>{legend()}'),
    page(2, "BACK PATCH · D · ARTWORK 2:1", KZ.note("Enlarged twice, to see the details. Use this page for the colour areas; use page 1 for the size. "
                                                   "The photo shows shades of each colour: please digitize them with the 4 colours below.")
         + f'<div class="art big">{art(168, True)}</div>{spots()}'),
    page(3, "BACK PATCH · D · CONSTRUCTION", KZ.note("Two layers: tree in front, back panel behind, joined only in the middle 3 cm at top and bottom, open at the sides. "
                                                    "4 ring-spring snaps 10 mm, antique copper, on the BACK panel. A belt up to 4 cm runs between back panel and front.")
         + f'<div class="dt"><div class="dw dd">{KZ.svg_patch()}</div><div class="loc"><h4>LOCATION</h4>{KZ.loc("back", 90, 36, 80, "D")}</div>'
         '<div class="col"><p class="fs">FINISHED SIZE</p><p class="sp">Size 8 × 7.1 cm (6 cm at the sides), curve 5.5 mm top and bottom<br>'
         'Snap grid 6.6 × 4.6 cm, snap centres 0.7 cm from the side edges · cap and socket on the back panel, stud on the jeans with 2 × 2 cm reinforcement inside<br>'
         'Stiff interlining in the patch so the snaps cannot tear out · edges folded and topstitched · no indigo on the linen<br>'
         'Washable by hand on its own: 30 °C, do not wring, dry flat</p></div>'
         '<div class="col"><p class="sp">Please send for approval before the proto: photo of the digitized patch (stitch count) and one embroidered sample on our linen, washed once by hand.</p></div></div>'),
]
CSS = KZ.CSS + """.ru{margin:-1mm 6mm 2mm 18mm;font-size:9pt;color:#566076}
.art{margin:2mm 0}.art.big{margin:0 0 1mm}
.chk{display:flex;flex-direction:column;align-items:center;gap:1mm;margin:1mm 0 4mm}.chk .ln{width:100mm;height:0;border-top:.5mm solid #1b2230;position:relative}
.chk .ln::before,.chk .ln::after{content:"";position:absolute;top:-1.5mm;height:3mm;border-left:.5mm solid #1b2230}.chk .ln::before{left:0}.chk .ln::after{right:0}
.chk span{font-size:8.5pt;color:#566076}
.h4{margin:0 0 1mm;color:#d6261c;font:700 13pt 'Roboto Condensed',Arial}
table.cl{width:100%;border-collapse:collapse;font-size:10pt}table.cl th{text-align:left;color:#d6261c;font-size:8pt;text-transform:uppercase;border-bottom:.4mm solid #d6261c;padding:1mm}
table.cl td{border-bottom:.2mm solid #d8dbe2;padding:1.4mm 1mm;vertical-align:middle}table.cl td span{color:#566076;font-size:8.5pt}
table.cl i{display:block;width:11mm;height:8mm;border:.25mm solid #c9ced8;border-radius:1mm}table.cl i.sw{width:8mm;height:5mm}table.cl td.no i{display:inline-block;width:5.5mm;height:5.5mm;border:0;border-radius:50%}table.cl.sp2{font-size:9pt}table.cl.sp2 td{padding:.6mm 1mm}"""
html = f'<!doctype html><html><head><meta charset="utf-8">{KZ.FONT}<style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(os.path.join(HERE, "v19", "kz_patch.html"), "w").write(html.replace("NVL-TT-01 JEANS", "NVL-TT-01 · PATCH D"))
print("ok")
