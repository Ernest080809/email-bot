# -*- coding: utf-8 -*-
# Druckvorlage 1:1 · Design v1.7 · Papiertest 3 (zwei Seiten A4 hoch)
#   Seite 1: linke Gesäßtasche mit B2   ·   Seite 2: Serp im Stoppelfeld (B) mit Lageplan
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import build16 as N16
    import build17 as N
import fine as FN
import v16 as V16
F = FN.F
INK = "#1d2330"; GREY = "#8a8f99"
FONT = "font-family: Helvetica, Arial, sans-serif"
def T(x, y, s, size=3.4, w=400, col=INK, anchor="start"):
    return f'<text x="{F(x)}" y="{F(y)}" style="{FONT}; font-size: {F(size)}px; font-weight: {w}; fill: {col}; text-anchor: {anchor}">{s}</text>'
def cut(d): return f'<path d="{d}" style="fill: none; stroke: {INK}; stroke-width: 0.25px; stroke-dasharray: 1.6 1.2"></path>'
def checkline(y):
    return (f'<path d="M55 {F(y)}H155M55 {F(y-2.5)}V{F(y+2.5)}M155 {F(y-2.5)}V{F(y+2.5)}" style="fill: none; stroke: {INK}; stroke-width: 0.35px"></path>'
            + T(105, y - 3.4, "Kontrolle: diese Linie muss genau 100 mm lang sein", 2.8, 700, anchor="middle")
            + T(105, y + 6, "Sonst falsch gedruckt. Im Druckdialog „Tatsächliche Größe“ bzw. „100 %“ wählen, nicht „An Seite anpassen“.", 2.6, 400, GREY, "middle"))
def header(n, title, lines):
    return ([T(12, 14, "NOVALIFE · TIME TRAVEL · DRUCKVORLAGE 1:1 · DESIGN v1.7 · PAPIERTEST 3", 2.8, 700, GREY),
             T(198, 14, f"Seite {n} von 2", 2.8, 400, GREY, "end"), T(12, 24, title, 6.2, 700)]
            + [T(12, 31 + i * 4.4, s, 3.0, 400, "#353a46") for i, s in enumerate(lines)])

# ---------- Seite 1: linke Gesäßtasche ----------
p1 = header(1, "Linke Gesäßtasche · drei Ähren, rotes Band, Goldfäden", [
    "1 · Ganze Tasche ausschneiden, Oberkante an Oberkante auf deine linke Gesäßtasche (vom Träger aus).",
    "2 · Goldfäden echt machen: 9 Stücke gelbes Garn, 2–3 cm, unterschiedlich lang, direkt unter das rote Band kleben.",
    "3 · Alatyr C auf die rechte Tasche, auf Höhe des roten Bands. Patch D bleibt am Bund.",
    "4 · Vorn: Band A und Münztasche E aus der Druckvorlage v1.5. Seite 2: der Serp für dein linkes Bein.",
    "5 · Fotos: aus 3 m und 1 m je vorn, hinten, seitlich, dazu ein Foto von der Seite aus 30 cm.",
])
PX, PY = 33, 62
pocket = (f'<path d="{N16.L_SHAPE}" style="fill: #2f4a6e"></path>'
          f'<path d="{N16.L_STITCH}" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>'
          f'<g transform="translate({F(N16.B2_POS[0])} {F(N16.B2_POS[1])})">{V16.B2_V16}</g>')
p1.append(f'<g transform="translate({PX} {PY})">{pocket}{cut("M-0.6 -0.6L144.6 15.5L144.6 144.4L72 172.7L-0.6 144.4Z")}</g>')
p1.append(T(PX + 72, PY + 181, "B2 · linke Gesäßtasche · Band 48 mm · 9 Fäden 18–30 mm", 3, 700, anchor="middle"))
p1.append(checkline(272))

# ---------- Seite 2: Serp im Stoppelfeld ----------
p2 = header(2, "Linkes Bein · Serp im Stoppelfeld", [
    "1 · Zettel entlang der gestrichelten Linie ausschneiden. Die goldene Kante rechts ist die Seitennaht.",
    "2 · Hose flach hinlegen, Vorderseite oben. Dein linkes Bein liegt in der Ansicht rechts.",
    "3 · Goldene Kante genau auf die Seitennaht, der Pfeil zeigt zum Bund. Mitte ca. 45 cm unter der Bundoberkante.",
    "4 · Anziehen und die Höhe am Körper prüfen, zwischen 40 und 50 cm. Die Höhe, die dir gefällt, an Claude.",
])
# Zettel: 4 mm Rand links, Motiv, 10 mm bis zur Naht = rechte Zettelkante
GW = (N.GEO[2] - N.GEO[0]) * N.SC; GH = (N.GEO[3] - N.GEO[1]) * N.SC
x0, y0 = 14.0, 62.0
w = 5 + GW + N.SEAM_GAP; h = 7 + GH + 7
seam = x0 + w
p2.append(f'<rect x="{F(x0)}" y="{F(y0)}" width="{F(w)}" height="{F(h)}" style="fill: #2f4a6e"></rect>')
p2.append(f'<path d="M{F(seam - 0.5)} {F(y0)}V{F(y0 + h)}" style="fill: none; stroke: #d4ab52; stroke-width: 0.9px"></path>')
p2.append(N.side_group(seam - N.SEAM_GAP - N.HALF_R, y0 + h / 2))
p2.append(f'<path d="M{F(x0 + 3)} {F(y0 + 7)}l2 -3l2 3M{F(x0 + 5)} {F(y0 + 4)}v6" style="fill: none; stroke: #f4f1ea; stroke-width: 0.4px"></path>')
p2.append(T(x0 + 9, y0 + 7, "Bund", 2.6, 700, "#f4f1ea"))
p2.append(cut(f"M{F(x0)} {F(y0)}H{F(seam)}V{F(y0 + h)}H{F(x0)}Z"))
p2.append(T(x0, y0 + h + 7, f"B · Serp im Stoppelfeld · ca. {N.SIDE_W} × {N.SIDE_H} mm", 3.2, 700))
p2.append(T(x0, y0 + h + 11.5, "goldene Kante = Seitennaht · Motiv 10 mm daneben", 2.8, 400, "#353a46"))
# Lageplan rechts, verkleinert
LP_INNER = open("v17/lageplan_inner.svgfrag", encoding="utf-8").read()
lx, ly, lw = 108, 58, 92
p2.append(f'<svg x="{F(lx)}" y="{F(ly)}" width="{F(lw)}" height="{F(lw)}" viewBox="200 96 640 640">{LP_INNER}</svg>')
p2.append(T(lx + lw / 2, ly + lw + 5, "Wo: dein linkes Bein, an der Seitennaht, 45 cm unter dem Bund", 2.8, 700, anchor="middle"))
p2.append(T(lx + lw / 2, ly + lw + 9.5, "(verkleinert, nur zur Orientierung)", 2.6, 400, GREY, "middle"))
p2.append(checkline(272))

def page(p):
    return f'<div class="pg"><svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297"><rect width="210" height="297" style="fill: #ffffff"></rect>{"".join(p)}</svg></div>'
html = ('<!doctype html><html lang="de"><head><meta charset="utf-8"><title>NVL Druckvorlage 1:1 v1.7</title>'
        '<style>@page{size:210mm 297mm;margin:0}html,body{margin:0;padding:0}.pg{width:210mm;height:297mm;overflow:hidden;break-after:page}.pg svg{display:block}</style></head><body>'
        + page(p1) + page(p2) + '</body></html>')
open('print17.html', 'w').write(html)
print(len(html), round(w, 1), round(h, 1))
