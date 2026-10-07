# -*- coding: utf-8 -*-
# Design v1.7 · großer Serp im Stoppelfeld an der linken Seitennaht. B2, C, A, E, D wie v1.6.
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import build as B
    import build15 as N15
    import build16 as N16
import fine as FN
import v16 as V16
import v17 as V
from tree2 import TREE2
F = FN.F
WHITE = FN.WHITE; RED = FN.RED

SC = 1.1                                   # Maßstab des Seitenmotivs
GEO = (9.46, 53.50, 57.01, 97.42)          # Geometrie-Box in v17-Koordinaten (ohne Kontur)
GC = ((GEO[0] + GEO[2]) / 2, (GEO[1] + GEO[3]) / 2)
SIDE_W, SIDE_H = 53, 49                    # mm, gerundet mit Kontur
SEAM_GAP = 10.0
SIDE_ROT = 4.5
HALF_R = (GEO[2] - GC[0]) * SC             # mm von der Mitte bis zur rechten Kante

def side_group(cx, cy, s=1.0, rot=0.0):
    """Motiv mit Mitte bei (cx, cy); s = zusätzlicher Maßstab (0,8 für die Flachzeichnung)."""
    return (f'<g transform="translate({F(cx)} {F(cy)}) rotate({F(rot)}) scale({F(SC * s)}) translate({F(-GC[0])} {F(-GC[1])})">'
            f'{V.SIDE_V17}</g>')

# ---------- vorn (px): linkes Bein = rechts in der Zeichnung, Mitte 45 cm unter der Bundoberkante ----------
CONTOUR_X_500 = N16.CONTOUR_X_500
SIDE_CX = CONTOUR_X_500 - SEAM_GAP * 0.8 - HALF_R * 0.8
FRONT_SIDE = side_group(SIDE_CX, 500.0, 0.8, SIDE_ROT)
FRONT_SIDE_LABEL = ('<rect x="560" y="466" width="20" height="20" style="fill: #c0392b; stroke: #ffffff; stroke-width: 2px"></rect>'
                    '<text x="570" y="480.5" style="fill: #ffffff">B</text>')

# ---------- Seitendetail (Board), viewBox in mm: 0 40 88 102 ----------
SEAM_X = 3 + (GEO[2] - GEO[0]) * SC + 3 + SEAM_GAP        # Naht rechts vom Motiv
def side_detail(denim="#2f4a6e", back="#26405f", labels=True):
    cx = SEAM_X - SEAM_GAP - HALF_R
    o = [f'<rect x="0" y="40" width="88" height="102" style="fill: {denim}"></rect>',
         f'<rect x="{F(SEAM_X)}" y="40" width="{F(88 - SEAM_X)}" height="102" style="fill: {back}"></rect>',
         f'<path d="M{F(SEAM_X)} 40V142" style="fill: none; stroke: #142236; stroke-width: 0.7px"></path>',
         f'<path d="M{F(SEAM_X - 1.8)} 40V142" style="fill: none; stroke: #d4ab52; stroke-width: 0.45px; stroke-dasharray: 1.6 1.2"></path>',
         side_group(cx, 92.0)]
    if labels:
        fam = "font-family: 'IBM Plex Mono', monospace; font-size: 3px; fill: #c8d3e6; letter-spacing: 0.08em"
        o.append(f'<text x="3" y="46" style="{fam}">VORN · LINKES BEIN</text>')
        o.append(f'<text x="{F(SEAM_X + 2.2)}" y="46" style="{fam}">HINTEN</text>')
        o.append(f'<text transform="translate({F(SEAM_X + 4.4)} 112) rotate(-90)" style="{fam}">SEITENNAHT</text>')
        xr = SEAM_X - SEAM_GAP
        o.append(f'<path d="M{F(xr + 0.3)} 127H{F(SEAM_X - 0.3)}M{F(xr + 0.3)} 125.5V128.5M{F(SEAM_X - 0.3)} 125.5V128.5" style="fill: none; stroke: #f4f1ea; stroke-width: 0.35px"></path>')
        o.append(f'<text x="{F((xr + SEAM_X) / 2)}" y="132" style="font-family: \'IBM Plex Mono\', monospace; font-size: 3px; fill: #f4f1ea; text-anchor: middle">10 mm</text>')
    return "\n".join(o)
SIDE_VB = "0 40 88 102"

# ---------- Elementblatt 1:1 (297 x 210 mm) ----------
txt = N15.txt
ROWS = FN.BAND_ROWS; COIN_MM = N15.COIN_MM; COIN_N = N15.COIN_N
AW, AR = FN.alatyr_fine()
S = [f'<rect x="0" y="0" width="297" height="210" style="fill: #efece5"></rect>',
     txt(15, 12, "NOVALIFE · TIME TRAVEL · ELEMENTE 1:1 · DESIGN v1.7", 4.2, 700),
     txt(15, 17.5, "Druck: „Tatsächliche Größe“ / 100 %. Die Kontrolllinie unten muss 100 mm messen. A, C, E: ein Kästchen = ein Kreuzstich = 1,33 mm.", 2.6, 400, "#5f6470")]
S.append(f'<rect x="11" y="24" width="100" height="{F(ROWS*FN.CELL+8)}" style="fill: #2d4668"></rect>')
S.append(FN.stitched(FN.band_white(69, (3 - 34) % FN.RAP), None, ROWS, 69, 15, 28, FN.CELL))
S.append(txt(11, 24 + ROWS * FN.CELL + 14, "A · Taschenband 23 mm", 3.2, 700))
S.append(txt(11, 24 + ROWS * FN.CELL + 18.4, "17 Kreuzstiche hoch · Rapport 16 · folgt dem Taschenbogen", 2.5, 400, "#4a4f5c"))
S.append(f'<rect x="120" y="24" width="44" height="44" style="fill: #2d4668"></rect>')
S.append(FN.stitched(AW, AR, 27, 27, 124, 28, FN.CELL))
S.append(txt(120, 73, "C · Alatyr · rechte Gesäßtasche", 3.2, 700)); S.append(txt(120, 77.4, "27 × 27 Kreuzstiche = 36 mm", 2.5, 400, "#4a4f5c"))
S.append(f'<g transform="translate(176 24)">{TREE2}</g>')
S.append(txt(176, 106, "D · Lebensbaum-Patch", 3.2, 700)); S.append(txt(176, 110.4, "86 × 76 mm · Naturleinen · fertiger Stickpatch, aufgenäht", 2.5, 400, "#4a4f5c"))
# B · Serp im Stoppelfeld (Kasten 9..85 x 84..146, Naht bei x = 75)
S.append('<rect x="9" y="84" width="76" height="62" style="fill: #2f4a6e"></rect>')
S.append('<rect x="75" y="84" width="10" height="62" style="fill: #26405f"></rect>')
S.append('<path d="M75 84V146" style="fill: none; stroke: #142236; stroke-width: 0.5px"></path>')
S.append(side_group(75 - SEAM_GAP - HALF_R, 115.0))
S.append(txt(9, 152, "B · Serp im Stoppelfeld", 3.2, 700))
S.append(txt(9, 156.4, "linkes Bein vorn · 10 mm neben der Seitennaht", 2.5, 400, "#4a4f5c"))
S.append(txt(9, 160.4, f"ca. {SIDE_W} × {SIDE_H} mm · weiß, rot, grau, braun, gold", 2.5, 400, "#4a4f5c"))
# B2 · drei Ähren, rotes Band, Goldfäden
S.append('<rect x="90" y="84" width="58" height="64" style="fill: #2f4a6e"></rect>')
S.append(f'<g transform="translate(95 88.5)">{V16.B2_V16}</g>')
S.append(txt(90, 154, "B2 · Drei Ähren, rotes Band, Goldfäden", 3.2, 700))
S.append(txt(90, 158.4, "linke Gesäßtasche · Band 48 mm, einfach rot", 2.5, 400, "#4a4f5c"))
S.append(txt(90, 162.4, "9 Fäden 18–30 mm, von Hand nach der Wäsche", 2.5, 400, "#4a4f5c"))
S.append(f'<rect x="154" y="116" width="{F(COIN_MM+6)}" height="{F(COIN_MM+6)}" style="fill: #2d4668"></rect>')
S.append(f'<rect x="157" y="119" width="{F(COIN_MM)}" height="{F(COIN_MM)}" style="fill: #34506f; stroke: #142236; stroke-width: 0.4px"></rect>')
S.append(FN.stitched(FN.coin_white(), None, COIN_N, COIN_N, 157 + (COIN_MM - COIN_N * FN.CELL) / 2, 119 + (COIN_MM - COIN_N * FN.CELL) / 2, FN.CELL))
S.append(txt(154, 190, "E · Münztasche komplett bestickt", 3.2, 700)); S.append(txt(154, 194.4, "45 × 45 Kreuzstiche = 60 mm · Tasche 62 × 62 mm", 2.5, 400, "#4a4f5c"))
lx, ly = 230, 124
for i, (name, col) in enumerate([("Weiß · Muster und Klinge", WHITE), ("Rot · Muster, Band B2, Schneide", RED),
                                  ("Gold · Ähren, Halme, Fäden", V.GD), ("Braun · Griff und Baum", "#6e4a2a")]):
    S.append(f'<rect x="{lx}" y="{ly+i*7}" width="5" height="5" style="fill: {col}; stroke: #8a8f99; stroke-width: 0.25px"></rect>')
    S.append(txt(lx + 7.5, ly + i * 7 + 4, name, 2.5, 400, "#353a46"))
S.append('<path d="M190 203H290M190 200.5V205.5M290 200.5V205.5" style="fill: none; stroke: #1d2330; stroke-width: 0.4px"></path>')
S.append(txt(240, 199, "100 mm", 2.6, 700, anchor="middle", mono=True))
SHEET = "\n".join(S)

if __name__ == "__main__":
    import os
    os.makedirs("v17", exist_ok=True)
    open("v17/front_side.svgfrag", "w").write(FRONT_SIDE)
    open("v17/sheet.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1188" height="840" viewBox="0 0 297 210">{SHEET}</svg>')
    open("v17/detail.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="440" height="510" viewBox="{SIDE_VB}">{side_detail()}</svg>')
    print("ok", round(SIDE_CX, 2), round(HALF_R, 2), round(SEAM_X, 2), len(SHEET))
