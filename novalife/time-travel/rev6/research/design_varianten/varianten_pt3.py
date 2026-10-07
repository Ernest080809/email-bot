# -*- coding: utf-8 -*-
# Papiertest 3 · Varianten 1:1 (Claude, 07.10.2026) · nur zum Testen, keine Designänderung.
#   B-G  Serp mit stahlgrauer statt roter Schneide (sonst v1.7)
#   B-GS Serp grau + Stoppelfeld vereinfacht (3 Reihen, breitere Halme, ohne Kontur)
#   B2-W drei Ähren, rotes Band mit weißer Kante
#   E-O  Münztasche offen: nur das weiße Gitter, kein roter Grund
#   N    Lasche „N° ___ / 100“ für den Patch D
# Aufruf: python3 -I varianten_pt3.py  (liest die Module aus novalife/time-travel/design)
import sys, os, io, re, random, math, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
DESIGN = os.path.abspath(os.path.join(HERE, "..", "..", "..", "design"))
sys.path.insert(0, DESIGN)
os.chdir(DESIGN)
with contextlib.redirect_stdout(io.StringIO()):
    import build17 as N
    import v17 as V
    import v16 as V16
    import fine as FN
    import wheat3 as W
F = FN.F
INK = "#1d2330"; GREY = "#8a8f99"; DENIM = "#2f4a6e"; BACK = "#26405f"
FONT = "font-family: Helvetica, Arial, sans-serif"
STEEL, STEELD = "#9ea4ab", "#6b7178"
def T(x, y, s, size=3.2, w=400, col=INK, anchor="start"):
    return f'<text x="{F(x)}" y="{F(y)}" style="{FONT}; font-size: {F(size)}px; font-weight: {w}; fill: {col}; text-anchor: {anchor}">{s}</text>'
def cut(d): return f'<path d="{d}" style="fill: none; stroke: {INK}; stroke-width: 0.25px; stroke-dasharray: 1.6 1.2"></path>'

# --- B-G: rote Schneide -> Stahlgrau
SIDE_G = V.SIDE_V17.replace(W.RED, STEEL).replace(W.REDD, STEELD)

# --- B-GS: Stoppelfeld vereinfacht
ROWS_B = [(76.0, [18.5, 26.5, 34.5], 5.8), (86.5, [14.5, 22.5, 30.5, 38.5], 7.2), (96.8, [12.6, 21.0, 29.4, 37.8, 54.6], 8.6)]
def stalk_bold(b, a_deg, h, col, cut_, w0=1.75, w1=1.55):
    a = math.radians(a_deg); d = (math.sin(a), -math.cos(a)); nn = (-d[1], d[0])
    t = W.add(b, d, h)
    tl = W.add(W.add(t, nn, -w1 / 2), d, cut_ / 2); tr = W.add(W.add(t, nn, w1 / 2), d, -cut_ / 2)
    poly = [W.add(b, nn, -w0 / 2), tl, tr, W.add(b, nn, w0 / 2)]
    return [W.path(W.pl(poly) + "Z", fill=col), W.path(W.pl([tl, tr]), stroke=V.STRAW_TIP, w=0.55)]
def stubble_bold():
    g = []; k = 0
    for r, (yb, xs, h0) in enumerate(ROWS_B):
        rnd = random.Random(40 + r)
        for x0 in xs:
            n = rnd.choice([2, 3])
            spread = {2: [-8, 8], 3: [-12, 0, 12]}[n]
            for i, a_deg in enumerate(spread):
                b = (x0 + (i - (n - 1) / 2) * 1.6, yb + rnd.uniform(-0.4, 0.4))
                h = h0 * rnd.uniform(0.85, 1.08)
                c = rnd.choice([-1, 1]) * rnd.uniform(0.6, 0.9)
                g += stalk_bold(b, a_deg + rnd.uniform(-3, 3), h, [W.GD, W.GDL][k % 2], c); k += 1
    return g
sk, _geo = W.sickle()
SIDE_GS = "\n".join(stubble_bold() + [sk["blade"], sk["shade"], sk["gloss"], sk["edge"], sk["edge2"], sk["handle"]])
SIDE_GS = SIDE_GS.replace(W.RED, STEEL).replace(W.REDD, STEELD)

def side_group(svg, cx, cy):
    return (f'<g transform="translate({F(cx)} {F(cy)}) scale({F(N.SC)}) translate({F(-N.GC[0])} {F(-N.GC[1])})">{svg}</g>')
GW = (N.GEO[2] - N.GEO[0]) * N.SC; GH = (N.GEO[3] - N.GEO[1]) * N.SC
def side_panel(svg, x0, y0, label, sub):
    w = 5 + GW + N.SEAM_GAP; h = 7 + GH + 7; seam = x0 + w
    o = [f'<rect x="{F(x0)}" y="{F(y0)}" width="{F(w)}" height="{F(h)}" style="fill: {DENIM}"></rect>',
         f'<path d="M{F(seam - 0.5)} {F(y0)}V{F(y0 + h)}" style="fill: none; stroke: #d4ab52; stroke-width: 0.9px"></path>',
         side_group(svg, seam - N.SEAM_GAP - N.HALF_R, y0 + h / 2),
         f'<path d="M{F(x0 + 3)} {F(y0 + 7)}l2 -3l2 3M{F(x0 + 5)} {F(y0 + 4)}v6" style="fill: none; stroke: #f4f1ea; stroke-width: 0.4px"></path>',
         T(x0 + 9, y0 + 7, "Bund", 2.6, 700, "#f4f1ea"),
         T(x0 + w - 3, y0 + 7, label, 3.4, 700, "#f4f1ea", "end"),
         cut(f"M{F(x0)} {F(y0)}H{F(seam)}V{F(y0 + h)}H{F(x0)}Z"),
         T(x0, y0 + h + 5.5, sub, 2.8, 700)]
    return o, h

# --- B2-W: weiße Kante um das rote Band
B2 = V16.B2_V16
m = re.search(r'<path d="([^"]+)" style="fill: none; stroke: ' + re.escape(W.REDD) + r'; stroke-width: 3\.3px[^"]*"></path>', B2)
assert m, "Bandpfad nicht gefunden"
white = W.path(m.group(1), stroke=W.WHITE, w=3.3 + 1.8)
B2_W = B2.replace(m.group(0), white + m.group(0), 1)

# --- E-O: Münztasche offen (nur Weiß)
COIN_MM = 60.0; CN = FN.COIN_N; U = FN.CELL
def coin(x0, y0, open_=True):
    o = [f'<rect x="{F(x0)}" y="{F(y0)}" width="62" height="62" style="fill: #34506f; stroke: #142236; stroke-width: 0.4px"></rect>']
    ox = x0 + 1 + (COIN_MM - CN * U) / 2; oy = y0 + 1 + (COIN_MM - CN * U) / 2
    o.append(FN.stitched(FN.coin_white(), [] if open_ else None, CN, CN, ox, oy, U))
    return o

P = [f'<rect width="210" height="297" style="fill: #ffffff"></rect>',
     T(12, 14, "NOVALIFE · TIME TRAVEL · PAPIERTEST 3 · VARIANTEN 1:1 · NUR ZUM TESTEN", 2.8, 700, GREY),
     T(12, 24, "Varianten für Do 08.10. · gleiche Größe wie v1.7", 6.0, 700)]
for i, s in enumerate([
        "1 · Erst v1.7 aufkleben und fotografieren (Druckvorlage v17, v15 S. 1, 1zu1 S. 3). Dann je eine Variante drüberkleben, gleiche Stelle, gleiches Licht.",
        "2 · B-G und B-GS ersetzen den Serp aus v17 Seite 2 (goldene Kante = Seitennaht). B2-W ersetzt die Ähren auf der linken Gesäßtasche.",
        "3 · E-O auf die Münztasche. N-Lasche unten mittig auf den Papier-Patch D, Nummer von Hand mit Filzstift eintragen.",
        "4 · Fotos je Variante aus 3 m und 1 m. Für den Schnelltest nur Serp v1.7 gegen B-G und B2 v1.7 gegen B2-W zeigen."]):
    P.append(T(12, 31 + i * 4.3, s, 2.75, 400, "#353a46"))
o, h = side_panel(SIDE_G, 12, 52, "B-G", "B-G · Schneide stahlgrau statt rot · sonst v1.7")
P += o
o2, _ = side_panel(SIDE_GS, 108, 52, "B-GS", "B-GS · grau + Stoppelfeld kräftiger, ohne Kontur")
P += o2
y2 = 52 + h + 16
P.append(f'<rect x="12" y="{F(y2)}" width="58" height="64" style="fill: {DENIM}"></rect>')
P.append(f'<g transform="translate(17 {F(y2 + 4.5)})">{B2_W}</g>')
P.append(T(64, y2 + 6, "B2-W", 3.4, 700, "#f4f1ea", "end"))
P.append(cut(f"M12 {F(y2)}H70V{F(y2 + 64)}H12Z"))
P.append(T(12, y2 + 69.5, "B2-W · rotes Band mit weißer Kante", 2.8, 700))
P += coin(80, y2 + 1)
P.append(cut(f"M80 {F(y2 + 1)}H142V{F(y2 + 63)}H80Z"))
P.append(T(80, y2 + 69.5, "E-O · Münztasche offen, nur Weiß", 2.8, 700))
# N-Lasche
nx, ny = 150, y2 + 10
P.append(f'<rect x="{nx}" y="{F(ny)}" width="40" height="14" rx="2" style="fill: #e8dcc0; stroke: #8a6a3e; stroke-width: 0.4px"></rect>')
P.append(T(nx + 3, ny + 9.2, "N°", 4.2, 700, "#6e4a2a"))
P.append(f'<path d="M{nx + 12} {F(ny + 10)}H{nx + 25}" style="fill: none; stroke: #6e4a2a; stroke-width: 0.35px"></path>')
P.append(T(nx + 37, ny + 9.2, "/ 100", 4.2, 700, "#6e4a2a", "end"))
P.append(cut(f"M{nx} {F(ny)}H{nx + 40}V{F(ny + 14)}H{nx}Z"))
P.append(T(nx, ny + 19.5, "N · Lasche für Patch D", 2.8, 700))
P.append(T(nx, ny + 23.5, "40 × 14 mm, Ziffern 4 mm hoch", 2.5, 400, GREY))
P.append(T(nx, ny + 27.5, "Nummer von Hand eintragen", 2.5, 400, GREY))
yc = 272
P.append(f'<path d="M55 {yc}H155M55 {yc - 2.5}V{yc + 2.5}M155 {yc - 2.5}V{yc + 2.5}" style="fill: none; stroke: {INK}; stroke-width: 0.35px"></path>')
P.append(T(105, yc - 3.4, "Kontrolle: diese Linie muss genau 100 mm lang sein", 2.8, 700, anchor="middle"))
P.append(T(105, yc + 6, "Im Druckdialog „Tatsächliche Größe“ bzw. „100 %“ wählen, nicht „An Seite anpassen“.", 2.6, 400, GREY, "middle"))
html = ('<!doctype html><html lang="de"><head><meta charset="utf-8"><title>NVL Papiertest 3 Varianten</title>'
        '<style>@page{size:210mm 297mm;margin:0}html,body{margin:0;padding:0}.pg{width:210mm;height:297mm;overflow:hidden}.pg svg{display:block}</style></head><body>'
        f'<div class="pg"><svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">{"".join(P)}</svg></div></body></html>')
out = os.path.join(HERE, "papiertest3_varianten.html")
open(out, "w", encoding="utf-8").write(html)
print("ok", out, round(GW, 1), round(GH, 1), round(h, 1), y2)
