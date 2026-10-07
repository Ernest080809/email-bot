# -*- coding: utf-8 -*-
# Druckvorlage 1:1 · Design v1.5 · nur die geänderten Teile (2 Seiten A4 hoch)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import build as B
    import build15 as N
import fine as FN
import wheat3 as W
F = FN.F
WHITE = FN.WHITE; REDD = FN.REDD; REDL = FN.REDL; WHT2 = FN.WHT2
INK = "#1d2330"; GREY = "#8a8f99"; GUIDE = "#9aa1ad"; DEN = "#2d4668"
FONT = "font-family: Helvetica, Arial, sans-serif"
def T(x, y, s, size=3.4, w=400, col=INK, anchor="start"):
    return f'<text x="{F(x)}" y="{F(y)}" style="{FONT}; font-size: {F(size)}px; font-weight: {w}; fill: {col}; text-anchor: {anchor}">{s}</text>'
def cut(d): return f'<path d="{d}" style="fill: none; stroke: {INK}; stroke-width: 0.25px; stroke-dasharray: 1.6 1.2"></path>'
def checkline(y):
    return (f'<path d="M55 {F(y)}H155M55 {F(y-2.5)}V{F(y+2.5)}M155 {F(y-2.5)}V{F(y+2.5)}" style="fill: none; stroke: {INK}; stroke-width: 0.35px"></path>'
            + T(105, y - 3.4, "Kontrolle: diese Linie muss genau 100 mm lang sein", 2.8, 700, anchor="middle")
            + T(105, y + 6, "Sonst falsch gedruckt. Im Druckdialog „Tatsächliche Größe“ bzw. „100 %“ wählen, nicht „An Seite anpassen“.", 2.6, 400, GREY, "middle"))
def header(n, title, sub):
    return (T(12, 14, "NOVALIFE · TIME TRAVEL · DRUCKVORLAGE 1:1 · DESIGN v1.5 · NUR DIE GEÄNDERTEN TEILE", 2.8, 700, GREY)
            + T(198, 14, f"Seite {n} von 2", 2.8, 400, GREY, "end")
            + T(12, 24, title, 6.2, 700) + "".join(T(12, 31 + i * 4.6, line, 3.3, 400, "#353a46") for i, line in enumerate(sub)))

# ---------- Seite 1: Band A 23 mm (gebogen) + Münztasche E 62 mm ----------
UF = B.UF; NF = B.NF; LEADF = B.LEADF; ROWS = FN.BAND_ROWS
def corners(col, row):
    s_ = LEADF + (col + 0.5) * UF; x, y, tx, ty, nx, ny = B.at(s_); off = (row - (ROWS - 11)) * UF
    cx, cy = x + nx * off, y + ny * off; h = UF / 2 + 0.06
    return [(cx - tx*h - nx*h, cy - ty*h - ny*h), (cx + tx*h - nx*h, cy + ty*h - ny*h), (cx + tx*h + nx*h, cy + ty*h + ny*h), (cx - tx*h + nx*h, cy - ty*h + ny*h)]
def lerp(a, b, t): return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
Wb = FN.band_white(NF, (3 - NF // 2) % FN.RAP)
fill = {"r": [], "w": []}; xs = {"r": [], "w": []}
for col in range(NF):
    for row in range(ROWS):
        k = "w" if (row, col) in Wb else "r"
        c = corners(col, row)
        fill[k].append("M" + "L".join(f"{F(a)} {F(b)}" for a, b in c) + "Z")
        i = 0.12
        p0 = lerp(c[0], c[2], i); p2 = lerp(c[0], c[2], 1 - i); p1 = lerp(c[1], c[3], i); p3 = lerp(c[1], c[3], 1 - i)
        xs[k].append(f"M{F(p0[0])} {F(p0[1])}L{F(p2[0])} {F(p2[1])}M{F(p1[0])} {F(p1[1])}L{F(p3[0])} {F(p3[1])}")
band = (f'<path d="{"".join(fill["r"])}" style="fill: {REDD}"></path>'
        f'<path d="{"".join(fill["w"])}" style="fill: {WHT2}"></path>'
        f'<path d="{"".join(xs["r"])}" style="fill: none; stroke: {REDL}; stroke-width: {F(UF*0.3)}px; stroke-linecap: round"></path>'
        f'<path d="{"".join(xs["w"])}" style="fill: none; stroke: {WHITE}; stroke-width: {F(UF*0.34)}px; stroke-linecap: round"></path>')
band_cut = B.offset_poly(N.O_LO - 0.4, N.O_HI + 0.4)
guides = (f'<path d="M 356.0 172 C 352 220 296 248.8 245.2 252" style="fill: none; stroke: {GUIDE}; stroke-width: 0.6px; stroke-dasharray: 2 1.5"></path>')
OX, OY = 11, 120
CS = N.COIN_MM; CX0, CY0 = 14, 57
E = FN.stitched(FN.coin_white(), None, N.COIN_N, N.COIN_N, CX0 + (CS - N.COIN_N * FN.CELL) / 2, CY0 + (CS - N.COIN_N * FN.CELL) / 2, FN.CELL)
p1 = [header(1, "Vorn · Band A 23 mm und Münztasche E 62 mm",
             ["Beide gehören an die Vordertasche mit der Münztasche (vom Träger aus rechts), wie beim ersten Test.",
              "Band: die innere Bogenkante genau auf die Taschenöffnung legen, wie bisher. Es ist 5 mm schmaler.",
              "Münztasche: das Quadrat füllt jetzt fast deine ganze Münztasche. Oben bündig an die Münztaschen-Naht,",
              "die untere rechte Ecke darf unter das Band rutschen. So sitzt es später auch an der echten Hose.",
              "Alles mit Malerkrepp fixieren. Die alten Teile A und E kannst du wegwerfen."]),
      f'<rect x="{F(CX0)}" y="{F(CY0)}" width="{F(CS)}" height="{F(CS)}" style="fill: #34506f"></rect>', E,
      cut(f"M{F(CX0)} {F(CY0)}h{F(CS)}v{F(CS)}h{F(-CS)}z"),
      T(CX0 + CS + 5, CY0 + 6, "E · Münztasche", 3.4, 700), T(CX0 + CS + 5, CY0 + 11, "62 × 62 mm, Stickerei 60 × 60 mm", 3, 400, "#353a46"),
      T(CX0 + CS + 5, CY0 + 15.5, "45 × 45 Kreuzstiche (vorher 37 × 37)", 3, 400, "#353a46"),
      f'<g transform="translate({F(OX)} {F(OY)}) scale(1.25) translate(-240 -160)">{band}{cut(band_cut)}</g>',
      T(14, 142, "A · Taschenband", 3.4, 700),
      T(14, 147, "23 mm breit, 17 Kreuzstiche (vorher 28 mm, 21)", 3, 400, "#353a46"),
      T(14, 151.5, "Die innere Kante des Bogens kommt auf die Taschenöffnung.", 3, 400, "#353a46"),
      checkline(272)]

# ---------- Seite 2: linke Gesäßtasche mit B neu, B2, Goldfäden ----------
PX, PY = 33, 58
pocket = (f'<path d="{N.L_SHAPE}" style="fill: #2f4a6e"></path>'
          f'<path d="{N.L_STITCH}" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>'
          f'<g transform="translate({F(N.B_POS[0])} {F(N.B_POS[1])}) scale({F(N.BSC)})">{W.B_SVG}</g>'
          f'<g transform="translate({F(N.B2_POS[0])} {F(N.B2_POS[1])})">{W.B2_SVG}</g>')
p2 = [header(2, "Hinten · linke Gesäßtasche · B neu, Goldfäden länger",
             ["Gehört auf die linke Gesäßtasche (vom Träger aus links), dort hattest du B beim ersten Test.",
              "Ganze Tasche entlang der gestrichelten Kontur ausschneiden, Oberkante an Oberkante auf deine Tasche.",
              "Tipp: Für echte Goldfäden 9 Stücke gelbes Garn oder Wolle, 2–3 cm lang, unter die rote Linie kleben.",
              "Alatyr C aus dem ersten Ausdruck (Seite 3) auf die rechte Gesäßtasche: waagerecht mittig, die Mitte",
              "ca. 45 mm unter der Oberkante (in der Taschenmitte gemessen), also auf Höhe der roten Linie. D bleibt."]),
      f'<g transform="translate({PX} {PY})">{pocket}{cut("M-0.6 -0.6L144.6 15.5L144.6 144.4L72 172.7L-0.6 144.4Z")}</g>',
      T(PX + 72, PY + 181, "Tasche 144 × 172 mm · B ca. 44 × 75 mm · B2 49 mm breit, Fäden 18–30 mm", 3, 700, anchor="middle"),
      checkline(272)]

def page(parts):
    return f'<div class="pg"><svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297"><rect width="210" height="297" style="fill: #ffffff"></rect>{"".join(parts)}</svg></div>'
html = ('<!doctype html><html lang="de"><head><meta charset="utf-8"><title>NVL Druckvorlage 1:1 v1.5</title>'
        '<style>@page{size:210mm 297mm;margin:0}html,body{margin:0;padding:0}.pg{width:210mm;height:297mm;overflow:hidden;break-after:page}.pg svg{display:block}</style></head><body>'
        + page(p1) + page(p2) + '</body></html>')
open('print15.html', 'w').write(html)
print(len(html))
