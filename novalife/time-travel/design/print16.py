# -*- coding: utf-8 -*-
# Druckvorlage 1:1 · Design v1.6 · Papiertest 3 (eine Seite A4 hoch): linke Gesäßtasche neu + Serp im Stoppelfeld
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import build16 as N
import fine as FN
import v16 as V
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
lines = [
    "1 · Linke Gesäßtasche (vom Träger aus): ganze Tasche ausschneiden, Oberkante an Oberkante. Sie ersetzt die alte linke Tasche.",
    "2 · Goldfäden echt machen: 9 Stücke gelbes Garn, 2–3 cm, unterschiedlich lang, direkt unter das rote Band kleben.",
    "3 · Serp im Stoppelfeld: Zettel ausschneiden. Hose flach hinlegen, Vorderseite oben. Auf das linke Bein (in der Ansicht rechts),",
    "     die rechte Zettelkante genau auf die Seitennaht. Höhe: Mitte 40–50 cm unter der Bundoberkante, probier es am Körper aus.",
    "4 · Vorn: Band A und Münztasche E aus der Druckvorlage v1.5. Hinten: Alatyr C auf die rechte Tasche, auf Höhe des roten Bands. Patch D bleibt.",
    "5 · Anziehen. 6 Fotos aus 3 m und 1 m (vorn, hinten, seitlich), dazu ein Foto von der Seite aus 30 cm.",
]
parts = [T(12, 14, "NOVALIFE · TIME TRAVEL · DRUCKVORLAGE 1:1 · DESIGN v1.6 · PAPIERTEST 3", 2.8, 700, GREY),
         T(198, 14, "1 Seite", 2.8, 400, GREY, "end"),
         T(12, 24, "Linke Gesäßtasche neu · Serp an der Seite", 6.2, 700)]
parts += [T(12, 31 + i * 4.4, s, 3.0, 400, "#353a46") for i, s in enumerate(lines)]
# Tasche links
PX, PY = 12, 66
pocket = (f'<path d="{N.L_SHAPE}" style="fill: #2f4a6e"></path>'
          f'<path d="{N.L_STITCH}" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>'
          f'<g transform="translate({F(N.B2_POS[0])} {F(N.B2_POS[1])})">{V.B2_V16}</g>')
parts.append(f'<g transform="translate({PX} {PY})">{pocket}{cut("M-0.6 -0.6L144.6 15.5L144.6 144.4L72 172.7L-0.6 144.4Z")}</g>')
parts.append(T(PX + 72, PY + 181, "B2 · linke Gesäßtasche · Band 48 mm · 9 Fäden 18–30 mm", 3, 700, anchor="middle"))
# Seitenmotiv rechts: rechte Zettelkante = Seitennaht
SX, SY = 165, 70
x0, x1 = -4.0, N.SIDE_BOX[2] + N.SEAM_GAP        # 10 mm Abstand zur Naht
y0, y1 = 1.0, 46.0
side = (f'<rect x="{F(x0)}" y="{F(y0)}" width="{F(x1 - x0)}" height="{F(y1 - y0)}" style="fill: #2f4a6e"></rect>'
        f'<path d="M{F(x1 - 0.4)} {F(y0)}V{F(y1)}" style="fill: none; stroke: #d4ab52; stroke-width: 0.6px"></path>'
        f'{V.SIDE_V16}'
        f'<path d="M{F(x0 + 3)} {F(y0 + 5)}l1.8 -2.6l1.8 2.6M{F(x0 + 4.8)} {F(y0 + 2.4)}v5" style="fill: none; stroke: #f4f1ea; stroke-width: 0.35px"></path>'
        + cut(f"M{F(x0)} {F(y0)}H{F(x1)}V{F(y1)}H{F(x0)}Z"))
parts.append(f'<g transform="translate({SX} {SY})">{side}</g>')
lx = SX + x0
parts += [T(lx, SY + y1 + 7, "B · Serp im Stoppelfeld", 3.2, 700),
          T(lx, SY + y1 + 11.5, "ca. 22 × 35 mm", 2.8, 400, "#353a46"),
          T(lx, SY + y1 + 15.5, "Pfeil zeigt zum Bund", 2.8, 400, "#353a46"),
          T(lx, SY + y1 + 19.5, "goldene Kante = Seitennaht", 2.8, 400, "#353a46")]
parts.append(checkline(272))

def page(p):
    return f'<div class="pg"><svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297"><rect width="210" height="297" style="fill: #ffffff"></rect>{"".join(p)}</svg></div>'
html = ('<!doctype html><html lang="de"><head><meta charset="utf-8"><title>NVL Druckvorlage 1:1 v1.6</title>'
        '<style>@page{size:210mm 297mm;margin:0}html,body{margin:0;padding:0}.pg{width:210mm;height:297mm;overflow:hidden}.pg svg{display:block}</style></head><body>'
        + page(parts) + '</body></html>')
open('print16.html', 'w').write(html)
print(len(html))
