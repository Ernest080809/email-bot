# -*- coding: utf-8 -*-
# Design v1.6 · Fragmente für den Canvas, Taschen- und Seitendetail, Elementblatt
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import build as B
    import build15 as N15
import fine as FN
import v16 as V
from tree2 import TREE2
F = FN.F
WHITE = FN.WHITE; RED = FN.RED
UF = B.UF

B2_POS = (48.0, 28.45)         # B2 in Taschen-mm: Bandmitte bei (72, 53), wie die Alatyr-Mitte rechts (72, 52)
C_CENTER = N15.C_CENTER
SIDE_BOX = (0.24, 6.21, 21.32, 41.08)      # Geometrie-Box des Seitenmotivs in mm
SIDE_C = ((SIDE_BOX[0] + SIDE_BOX[2]) / 2, (SIDE_BOX[1] + SIDE_BOX[3]) / 2)
SIDE_W, SIDE_H = 22, 35                    # gerundet, mit Kontur
SEAM_GAP = 10.0                            # mm von der Seitennaht bis zur Motivkante
SIDE_ROT = 4.5                             # parallel zur Seitennaht in Oberschenkelhöhe

# ---------- vorn (px, 0,8 px/mm): linkes Bein = rechts in der Zeichnung, 45 cm unter der Bundoberkante ----------
CONTOUR_X_500 = 641.55                     # Außenkontur bei y = 500 (= 140 + 450 mm * 0,8)
SIDE_CX = CONTOUR_X_500 - SEAM_GAP * 0.8 - (SIDE_BOX[2] - SIDE_C[0]) * 0.8
SIDE_CY = 500.0
FRONT_SIDE = (f'<g transform="translate({F(SIDE_CX)} {F(SIDE_CY)}) rotate({F(SIDE_ROT)}) scale(0.8) translate({F(-SIDE_C[0])} {F(-SIDE_C[1])})">'
              f'{V.SIDE_V16}</g>')
FRONT_SIDE_LABEL = ('<rect x="590" y="478" width="20" height="20" style="fill: #c0392b; stroke: #ffffff; stroke-width: 2px"></rect>'
                    '<text x="600" y="492.5" style="fill: #ffffff">B</text>')

# ---------- hinten (px) ----------
LP, RP = N15.LP, N15.RP
BACK_B2 = f'<g transform="translate({F(LP[0]+B2_POS[0]*0.8)} {F(LP[1]+B2_POS[1]*0.8)}) scale(0.8)">{V.B2_V16}</g>'
BACK_C = N15.BACK_C

# ---------- Taschen und Seite in mm (Board und Druck) ----------
L_SHAPE, L_STITCH, R_SHAPE, R_STITCH = N15.L_SHAPE, N15.L_STITCH, N15.R_SHAPE, N15.R_STITCH
def pocket_left(denim="#2f4a6e", bg=True):
    o = []
    if bg: o.append('<rect x="-14" y="-14" width="172" height="200" style="fill: #2d4668"></rect>')
    o += [f'<path d="{L_SHAPE}" style="fill: {denim}; stroke: #142236; stroke-width: 0.9px; stroke-linejoin: round"></path>',
          f'<path d="{L_STITCH}" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>',
          f'<g transform="translate({F(B2_POS[0])} {F(B2_POS[1])})">{V.B2_V16}</g>']
    return "\n".join(o)
pocket_right = N15.pocket_right

def side_detail(denim="#2f4a6e", back="#26405f", labels=True):
    """Ausschnitt linkes Bein, vorn, mit der Seitennaht rechts. viewBox in mm: -12 -6 60 70."""
    seam_x = SIDE_BOX[2] + SEAM_GAP
    o = [f'<rect x="-12" y="-6" width="60" height="70" style="fill: {denim}"></rect>',
         f'<rect x="{F(seam_x)}" y="-6" width="{F(48 - seam_x)}" height="70" style="fill: {back}"></rect>',
         f'<path d="M{F(seam_x)} -6V64" style="fill: none; stroke: #142236; stroke-width: 0.6px"></path>',
         f'<path d="M{F(seam_x - 1.6)} -6V64" style="fill: none; stroke: #d4ab52; stroke-width: 0.35px; stroke-dasharray: 1.4 1.1"></path>',
         V.SIDE_V16]
    if labels:
        fam = "font-family: 'IBM Plex Mono', monospace; font-size: 2.4px; fill: #c8d3e6; letter-spacing: 0.08em"
        o.append(f'<text x="{F(seam_x + 2.2)}" y="2" style="{fam}">HINTEN</text>')
        o.append(f'<text x="-10" y="2" style="{fam}">VORN · LINKES BEIN</text>')
        o.append(f'<text transform="translate({F(seam_x + 3.4)} 40) rotate(-90)" style="{fam}">SEITENNAHT</text>')
        o.append(f'<path d="M{F(SIDE_BOX[2] + 0.3)} 46.5H{F(seam_x - 0.3)}M{F(SIDE_BOX[2] + 0.3)} 45.3V47.7M{F(seam_x - 0.3)} 45.3V47.7" style="fill: none; stroke: #f4f1ea; stroke-width: 0.3px"></path>')
        o.append(f'<text x="{F((SIDE_BOX[2] + seam_x) / 2)}" y="50.6" style="font-family: \'IBM Plex Mono\', monospace; font-size: 2.6px; fill: #f4f1ea; text-anchor: middle">10 mm</text>')
    return "\n".join(o)

# ---------- Elementblatt 1:1 (297 x 210 mm) ----------
txt = N15.txt
ROWS = FN.BAND_ROWS; COIN_MM = N15.COIN_MM; COIN_N = N15.COIN_N
AW, AR = FN.alatyr_fine()
S = [f'<rect x="0" y="0" width="297" height="210" style="fill: #efece5"></rect>',
     txt(15, 12, "NOVALIFE · TIME TRAVEL · ELEMENTE 1:1 · DESIGN v1.6", 4.2, 700),
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
# B · Serp im Stoppelfeld, mit Seitennaht rechts
S.append('<rect x="11" y="88" width="46" height="50" style="fill: #2f4a6e"></rect>')
S.append('<rect x="47.3" y="88" width="9.7" height="50" style="fill: #26405f"></rect>')
S.append('<path d="M47.3 88V138" style="fill: none; stroke: #142236; stroke-width: 0.5px"></path>')
S.append(f'<g transform="translate({F(47.3 - SEAM_GAP - SIDE_BOX[2])} 90.5)">{V.SIDE_V16}</g>')
S.append(txt(11, 144, "B · Serp im Stoppelfeld", 3.2, 700))
S.append(txt(11, 148.4, "linkes Bein vorn · 10 mm neben der Seitennaht", 2.5, 400, "#4a4f5c"))
S.append(txt(11, 152.4, "ca. 22 × 35 mm · Halme 2–5 mm hoch", 2.5, 400, "#4a4f5c"))
# B2 · drei Ähren, rotes Band, Goldfäden
S.append('<rect x="70" y="88" width="62" height="66" style="fill: #2f4a6e"></rect>')
S.append(f'<g transform="translate(77 92.5)">{V.B2_V16}</g>')
S.append(txt(70, 160, "B2 · Drei Ähren, rotes Band, Goldfäden", 3.2, 700))
S.append(txt(70, 164.4, "linke Gesäßtasche · Band 48 mm, einfach rot", 2.5, 400, "#4a4f5c"))
S.append(txt(70, 168.4, "9 Fäden 18–30 mm, von Hand nach der Wäsche", 2.5, 400, "#4a4f5c"))
S.append(f'<rect x="150" y="116" width="{F(COIN_MM+6)}" height="{F(COIN_MM+6)}" style="fill: #2d4668"></rect>')
S.append(f'<rect x="153" y="119" width="{F(COIN_MM)}" height="{F(COIN_MM)}" style="fill: #34506f; stroke: #142236; stroke-width: 0.4px"></rect>')
S.append(FN.stitched(FN.coin_white(), None, COIN_N, COIN_N, 153 + (COIN_MM - COIN_N * FN.CELL) / 2, 119 + (COIN_MM - COIN_N * FN.CELL) / 2, FN.CELL))
S.append(txt(150, 190, "E · Münztasche komplett bestickt", 3.2, 700)); S.append(txt(150, 194.4, "45 × 45 Kreuzstiche = 60 mm · Tasche 62 × 62 mm", 2.5, 400, "#4a4f5c"))
lx, ly = 228, 128
for i, (name, col) in enumerate([("Weiß · Muster und Klinge", WHITE), ("Rot · Muster und Band B2", RED),
                                  ("Gold, Stroh · Ähren, Stoppeln, Fäden", V.GOLD), ("Braun · Griff und Baum", V.BR)]):
    S.append(f'<rect x="{lx}" y="{ly+i*7}" width="5" height="5" style="fill: {col}; stroke: #8a8f99; stroke-width: 0.25px"></rect>')
    S.append(txt(lx + 7.5, ly + i * 7 + 4, name, 2.5, 400, "#353a46"))
S.append('<path d="M190 203H290M190 200.5V205.5M290 200.5V205.5" style="fill: none; stroke: #1d2330; stroke-width: 0.4px"></path>')
S.append(txt(240, 199, "100 mm", 2.6, 700, anchor="middle", mono=True))
SHEET = "\n".join(S)

if __name__ == "__main__":
    import os
    os.makedirs("v16", exist_ok=True)
    for n, v in [("front_side", FRONT_SIDE), ("back_b2", BACK_B2)]:
        open(f"v16/{n}.svgfrag", "w").write(v)
    open("v16/sheet.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1188" height="840" viewBox="0 0 297 210">{SHEET}</svg>')
    open("v16/details.svg", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1290" height="500" viewBox="-14 -14 430 200">'
        f'<g>{pocket_left()}</g><g transform="translate(172 0)">{pocket_right()}</g>'
        f'<g transform="translate(344 0) scale(1.0)"><svg x="0" y="0" width="60" height="70" viewBox="-12 -6 60 70">{side_detail()}</svg></g></svg>')
    print("ok", round(SIDE_CX, 2), len(FRONT_SIDE), len(BACK_B2), len(SHEET))
