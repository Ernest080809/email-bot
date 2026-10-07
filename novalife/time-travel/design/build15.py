# -*- coding: utf-8 -*-
# Design v1.5 · neue Fragmente, Elementblatt, Taschen-Board
import io, contextlib, json
with contextlib.redirect_stdout(io.StringIO()):
    import build as B
import fine as FN
import wheat3 as W
from tree2 import TREE2
F = FN.F
WHITE = FN.WHITE; RED = FN.RED
UF = B.UF
BSC = 0.92                     # Maßstab von B auf der Tasche (Box 62 x 92 mm -> ~57 x 85)
B_POS = (72 - 29.5 * BSC, 66)  # B in Taschen-mm (linke Tasche)
B2_POS = (47, 31)              # B2 in Taschen-mm
C_CENTER = (72, 52)            # Alatyr-Mitte in Taschen-mm (rechte Tasche)
COIN_MM = 62.0                 # Münztasche
COIN_N = FN.COIN_N             # 45 Stiche = 60 mm
ROWS = FN.BAND_ROWS            # 17 Reihen = 22,7 mm

# ---------- vorn: Band (17 Reihen, Innenkante bleibt auf der Taschenöffnung) ----------
def fquad15(col, row, lead_f):
    s_ = lead_f + (col + 0.5) * UF; x, y, tx, ty, nx, ny = B.at(s_); off = (row - (ROWS - 11)) * UF
    cx, cy = x + nx * off, y + ny * off; h = UF / 2 + 0.08
    c = [(cx - tx*h - nx*h, cy - ty*h - ny*h), (cx + tx*h - nx*h, cy + ty*h - ny*h), (cx + tx*h + nx*h, cy + ty*h + ny*h), (cx - tx*h + nx*h, cy - ty*h + ny*h)]
    return "M" + "L".join(f"{F(a)} {F(b)}" for a, b in c) + "Z"
O_LO, O_HI = -(ROWS - 10.5) * UF, 10.5 * UF       # -6,5 / +10,5 Zellen
WB = FN.band_white(B.NF, (3 - B.NF // 2) % FN.RAP)
FRONT_BAND = (f'<path d="{B.offset_poly(O_LO, O_HI)}" style="fill: {RED}"></path>\n'
              f'<path d="{"".join(fquad15(c, r, B.LEADF) for (r, c) in sorted(WB))}" style="fill: {WHITE}"></path>')
# Münztasche 62 mm = 49,6 px; Stickerei 45 x 45 Zellen = 48 px
CP_X, CP_Y, CP_W = 280.0, 176.8, COIN_MM * 0.8
cx0 = CP_X + (CP_W - COIN_N * UF) / 2; cy0 = CP_Y + (CP_W - COIN_N * UF) / 2
FRONT_COIN = (f'<rect x="{F(cx0)}" y="{F(cy0)}" width="{F(COIN_N*UF)}" height="{F(COIN_N*UF)}" style="fill: {RED}"></rect>'
              f'<path d="{FN.cells_path(sorted(FN.coin_white()), cx0, cy0, UF)}" style="fill: {WHITE}"></path>')
COIN_OUTLINE = f'<rect x="{F(CP_X)}" y="{F(CP_Y)}" width="{F(CP_W)}" height="{F(CP_W)}" style="fill: none; stroke: #142236; stroke-width: 1.2px"></rect>'
COIN_STITCH = f'<path d="M {F(CP_X+4)} 181.6 L {F(CP_X+CP_W-4)} 181.6" style="fill: none; stroke: #d4ab52; stroke-width: 1.2px; stroke-dasharray: 3 2.5"></path>'

# ---------- hinten (px, 0,8 px/mm) ----------
LP = (291.2, 239.2)    # linke Tasche, Box-Ursprung
RP = (473.6, 239.2)    # rechte Tasche, Box-Ursprung
BACK_B = f'<g transform="translate({F(LP[0]+B_POS[0]*0.8)} {F(LP[1]+B_POS[1]*0.8)}) scale({F(0.8*BSC)})">{W.B_SVG}</g>'
BACK_B2 = f'<g transform="translate({F(LP[0]+B2_POS[0]*0.8)} {F(LP[1]+B2_POS[1]*0.8)}) scale(0.8)">{W.B2_SVG}</g>'
AW, AR = FN.alatyr_fine()
ax0 = RP[0] + C_CENTER[0] * 0.8 - 13.5 * UF; ay0 = RP[1] + C_CENTER[1] * 0.8 - 13.5 * UF
BACK_C = (f'<path d="{FN.cells_path(sorted(AW), ax0, ay0, UF)}" style="fill: {WHITE}"></path>'
          f'<path d="{FN.cells_path(sorted(AR), ax0, ay0, UF)}" style="fill: {RED}"></path>')

# ---------- Taschen in mm (für Board und Druck) ----------
L_SHAPE = "M0 0L144 16L144 144L72 172L0 144Z"; L_STITCH = "M5 6L139 21L139 140L72 166L5 140Z M0 15L144 31"
R_SHAPE = "M144 0L0 16L0 144L72 172L144 144Z"; R_STITCH = "M139 6L5 21L5 140L72 166L139 140Z M144 15L0 31"
def pocket_left(denim="#2f4a6e", bg=True):
    o = []
    if bg: o.append('<rect x="-14" y="-14" width="172" height="200" style="fill: #2d4668"></rect>')
    o += [f'<path d="{L_SHAPE}" style="fill: {denim}; stroke: #142236; stroke-width: 0.9px; stroke-linejoin: round"></path>',
          f'<path d="{L_STITCH}" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>',
          f'<g transform="translate({F(B_POS[0])} {F(B_POS[1])}) scale({F(BSC)})">{W.B_SVG}</g>',
          f'<g transform="translate({F(B2_POS[0])} {F(B2_POS[1])})">{W.B2_SVG}</g>']
    return "\n".join(o)
def pocket_right(denim="#2f4a6e", bg=True):
    o = []
    if bg: o.append('<rect x="-14" y="-14" width="172" height="200" style="fill: #2d4668"></rect>')
    o += [f'<path d="{R_SHAPE}" style="fill: {denim}; stroke: #142236; stroke-width: 0.9px; stroke-linejoin: round"></path>',
          f'<path d="{R_STITCH}" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>',
          FN.stitched(AW, AR, 27, 27, C_CENTER[0] - 18, C_CENTER[1] - 18, FN.CELL)]
    return "\n".join(o)

# ---------- Elementblatt 1:1 (297 x 210 mm) ----------
def txt(x, y, s, size=3.2, w=400, col="#1d2330", anchor="start", mono=False):
    fam = "font-family: 'IBM Plex Mono', monospace" if mono else "font-family: 'Archivo', Helvetica, sans-serif"
    return f'<text x="{F(x)}" y="{F(y)}" style="{fam}; font-size: {F(size)}px; font-weight: {w}; fill: {col}; text-anchor: {anchor}">{s}</text>'
S = [f'<rect x="0" y="0" width="297" height="210" style="fill: #efece5"></rect>',
     txt(15, 12, "NOVALIFE · TIME TRAVEL · ELEMENTE 1:1 · DESIGN v1.5", 4.2, 700),
     txt(15, 17.5, "Druck: „Tatsächliche Größe“ / 100 %. Die Kontrolllinie unten muss 100 mm messen. A, C, E: ein Kästchen = ein Kreuzstich = 1,33 mm.", 2.6, 400, "#5f6470")]
S.append(f'<rect x="11" y="24" width="100" height="{F(ROWS*FN.CELL+8)}" style="fill: #2d4668"></rect>')
S.append(FN.stitched(FN.band_white(69, (3 - 34) % FN.RAP), None, ROWS, 69, 15, 28, FN.CELL))
S.append(txt(11, 24 + ROWS * FN.CELL + 14, "A · Taschenband 23 mm", 3.2, 700))
S.append(txt(11, 24 + ROWS * FN.CELL + 18.4, "17 Kreuzstiche hoch (v1.4: 21) · Rapport 16 · folgt dem Taschenbogen", 2.5, 400, "#4a4f5c"))
S.append(f'<rect x="120" y="24" width="44" height="44" style="fill: #2d4668"></rect>')
S.append(FN.stitched(AW, AR, 27, 27, 124, 28, FN.CELL))
S.append(txt(120, 73, "C · Alatyr · rechte Gesäßtasche", 3.2, 700)); S.append(txt(120, 77.4, "27 × 27 Kreuzstiche = 36 mm", 2.5, 400, "#4a4f5c"))
S.append(f'<g transform="translate(176 24)">{TREE2}</g>')
S.append(txt(176, 106, "D · Lebensbaum-Patch", 3.2, 700)); S.append(txt(176, 110.4, "86 × 76 mm · Naturleinen · fertiger Stickpatch, aufgenäht", 2.5, 400, "#4a4f5c"))
S.append(f'<rect x="11" y="82" width="64" height="94" style="fill: #2d4668"></rect>')
S.append(f'<g transform="translate({F(43 - 29.5*BSC)} 82) scale({F(BSC)})">{W.B_SVG}</g>')
S.append(txt(11, 182, "B · Serp schneidet in die Garbe", 3.2, 700)); S.append(txt(11, 186.4, "linke Gesäßtasche · realistisch · Klinge hinter den Halmen", 2.5, 400, "#4a4f5c"))
S.append(f'<rect x="84" y="88" width="58" height="66" style="fill: #2d4668"></rect>')
S.append(f'<g transform="translate(88 94)">{W.B2_SVG}</g>')
S.append(txt(84, 160, "B2 · Ähren, rote Linie, Goldfäden", 3.2, 700)); S.append(txt(84, 164.4, "Linie 49 mm · 9 Fäden 18–30 mm, von Hand", 2.5, 400, "#4a4f5c"))
S.append(f'<rect x="150" y="116" width="{F(COIN_MM+6)}" height="{F(COIN_MM+6)}" style="fill: #2d4668"></rect>')
S.append(f'<rect x="153" y="119" width="{F(COIN_MM)}" height="{F(COIN_MM)}" style="fill: #34506f; stroke: #142236; stroke-width: 0.4px"></rect>')
S.append(FN.stitched(FN.coin_white(), None, COIN_N, COIN_N, 153 + (COIN_MM - COIN_N * FN.CELL) / 2, 119 + (COIN_MM - COIN_N * FN.CELL) / 2, FN.CELL))
S.append(txt(150, 190, "E · Münztasche komplett bestickt", 3.2, 700)); S.append(txt(150, 194.4, "45 × 45 Kreuzstiche = 60 mm · Tasche 62 × 62 mm", 2.5, 400, "#4a4f5c"))
lx, ly = 228, 128
for i, (name, col) in enumerate([("Weiß · Pflicht in jedem Element", WHITE), ("Rot · nie ohne Weiß daneben", RED), ("Gold, Ocker, Stroh · Weizen", W.GD), ("Braun · Griff, Kontur, Baum", W.BR)]):
    S.append(f'<rect x="{lx}" y="{ly+i*7}" width="5" height="5" style="fill: {col}; stroke: #8a8f99; stroke-width: 0.25px"></rect>')
    S.append(txt(lx + 7.5, ly + i * 7 + 4, name, 2.5, 400, "#353a46"))
S.append('<path d="M190 203H290M190 200.5V205.5M290 200.5V205.5" style="fill: none; stroke: #1d2330; stroke-width: 0.4px"></path>')
S.append(txt(240, 199, "100 mm", 2.6, 700, anchor="middle", mono=True))
SHEET = "\n".join(S)

if __name__ == "__main__":
    import os
    os.makedirs("v15", exist_ok=True)
    for n, v in [("front_band", FRONT_BAND), ("front_coin", FRONT_COIN), ("back_b", BACK_B), ("back_b2", BACK_B2), ("back_c", BACK_C)]:
        open(f"v15/{n}.svgfrag", "w").write(v)
    open("v15/sheet.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1188" height="840" viewBox="0 0 297 210">{SHEET}</svg>')
    open("v15/pockets_board.svg", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="700" viewBox="-14 -14 344 200"><g>{pocket_left()}</g><g transform="translate(172 0)">{pocket_right()}</g></svg>')
    print("ok", len(FRONT_BAND), len(FRONT_COIN), len(BACK_B), len(BACK_B2), len(BACK_C), len(SHEET))
