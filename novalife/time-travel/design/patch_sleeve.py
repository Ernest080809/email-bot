# -*- coding: utf-8 -*-
# Skizze 21.10.2026: Patch D wie bei Levi's oben auf dem Bund, Standardgürtel läuft durch.
#   Lösung: Patch als flache Schlaufe aus Vorderteil (Baum) und Rückwand, oben und unten verbunden, seitlich offen.
#   Die 4 Druckknöpfe sitzen zwischen Rückwand und Jeans, der Gürtel läuft zwischen Rückwand und Vorderteil.
import base64, os, subprocess
import fine as FN

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_SVG = os.path.join(HERE, "v19", "patch_sleeve.svg")
OUT_PNG = os.path.join(HERE, "..", "rev6", "skizzen", "2026-10-21_patch_schlaufe_levis.png")
F = FN.F
PHOTO = "data:image/png;base64," + base64.b64encode(open(os.path.join(HERE, "v19", "patch_d.png"), "rb").read()).decode()
WB, BELT = 40.0, 38.0
PW, PH, PB, SIN, SD = 80.0, 71.0, 5.5, 7.0, 10.0
DEN, DEN2, STITCH, BELTC, INK = "#3a5a82", "#34516f", "#c8954f", "#5a3a22", "#1b2230"


def T(x, y, s, size=5.2, w=700, fill=INK, anchor="middle"):
    return f'<text x="{F(x)}" y="{F(y)}" style="font: {w} {F(size)}px Helvetica, Arial, sans-serif; fill: {fill}; text-anchor: {anchor}">{s}</text>'


# ---- links: von hinten gesehen, Patch oben auf dem Bund, Gürtel läuft durch
PX = 70.0
outline = FN.patch_outline(PX, 0, PW, PH, PB)
left = [f'<rect x="-15" y="-6" width="230" height="150" style="fill: {DEN}"></rect>',
        f'<rect x="-15" y="0" width="230" height="{F(WB)}" style="fill: {DEN2}"></rect>',
        f'<path d="M-15 3h230M-15 {F(WB-3)}h230" style="fill: none; stroke: {STITCH}; stroke-width: 0.6; stroke-dasharray: 2 1.4"></path>',
        f'<path d="M0 {F(WB)}V144" style="stroke: #22354f; stroke-width: 0.8"></path>',
        f'<rect x="-15" y="1" width="230" height="{F(BELT)}" style="fill: {BELTC}"></rect>',
        f'<rect x="178" y="6" width="22" height="28" rx="2" style="fill: none; stroke: #b98a4a; stroke-width: 2"></rect>',
        "".join(f'<rect x="{F(x-5.5)}" y="-4" width="11" height="{F(WB+6)}" rx="1" style="fill: {DEN}; stroke: #22354f; stroke-width: 0.6"></rect>' for x in (0.0, 175.0)),
        f'<clipPath id="pcl"><path d="{outline}"></path></clipPath>',
        f'<image href="{PHOTO}" x="{F(PX)}" y="0" width="{F(PW)}" height="{F(PH)}" preserveAspectRatio="none" clip-path="url(#pcl)"></image>',
        f'<path d="{outline}" style="fill: none; stroke: #2a1d12; stroke-width: 0.6"></path>',
        "".join(f'<path d="M{F(x)} 20h10" style="stroke: #f3e4d0; stroke-width: 1; marker-end: url(#ar)"></path>' for x in (PX - 14, PX + PW + 4)),
        T(PX + PW / 2, PH + 12, "Gürtel läuft durch den Patch", 6, 700, "#f3e4d0"),
        T(PX + PW / 2, PH + 20, "Knöpfe versteckt dahinter", 5, 400, "#dce6f2"),
        T(100, -14, "Von hinten: oben auf dem Bund wie bei Levi's", 7, 700)]

# ---- rechts: Schnitt von der Seite (Dicke 4-fach gezeichnet)
K = 4.0                                   # Dicke überhöht
X0 = 300.0                                # Außenseite Jeans
jeans_t, stud_t, back_t, belt_t, front_t = 2.0, 3.0, 1.2, 4.0, 1.6
xb = X0 + stud_t * K                      # Rückwand
xg = xb + back_t * K                      # Gürtel
xf = xg + belt_t * K + 1.5                # Vorderteil
y0, y1 = 0.0, PH
right = [f'<rect x="{F(X0-jeans_t*K)}" y="-6" width="{F(jeans_t*K)}" height="150" style="fill: {DEN}"></rect>',
         f'<rect x="{F(X0-jeans_t*K-0.6)}" y="0" width="{F(jeans_t*K+0.6)}" height="{F(WB)}" style="fill: {DEN2}"></rect>',
         T(X0 - jeans_t * K - 3, WB / 2, "Bund", 4.6, 700, INK, "end"), T(X0 - jeans_t * K - 3, WB + 30, "Passe", 4.6, 700, INK, "end"),
         T(X0 - jeans_t * K - 3, 140, "Jeans", 5, 700, INK, "end")]
for yy in (PB + SIN, PH - PB - SIN):      # Druckknöpfe zwischen Jeans und Rückwand
    right.append(f'<rect x="{F(X0)}" y="{F(yy-SD/2)}" width="{F(stud_t*K)}" height="{F(SD)}" rx="1.5" style="fill: #a8643a; stroke: #6f3d1f; stroke-width: 0.5"></rect>')
right += [f'<rect x="{F(xb)}" y="{F(y0+2)}" width="{F(back_t*K)}" height="{F(y1-y0-4)}" style="fill: #e8dcc4; stroke: #6b5a40; stroke-width: 0.4"></rect>',
          f'<rect x="{F(xg)}" y="1" width="{F(belt_t*K)}" height="{F(BELT)}" style="fill: {BELTC}"></rect>',
          f'<rect x="{F(xf)}" y="{F(y0+2)}" width="{F(front_t*K)}" height="{F(y1-y0-4)}" style="fill: #c99a6a; stroke: #6b4a2a; stroke-width: 0.4"></rect>',
          f'<path d="M{F(xb)} {F(y0+2)}Q{F((xb+xf+front_t*K)/2)} {F(y0-5)} {F(xf+front_t*K)} {F(y0+2)}" style="fill: none; stroke: #6b4a2a; stroke-width: 1.6"></path>',
          f'<path d="M{F(xb)} {F(y1-2)}Q{F((xb+xf+front_t*K)/2)} {F(y1+5)} {F(xf+front_t*K)} {F(y1-2)}" style="fill: none; stroke: #6b4a2a; stroke-width: 1.6"></path>']
lx = xf + front_t * K + 8
for yy, s in [(-1, "oben verbunden"), (PB + SIN + 1, "Druckknopf (versteckt)"), (25, "Gürtel 38–40 mm"), (45, "Rückwand vom Patch"),
              (57, "Vorderteil mit Baum"), (PH + 1, "unten verbunden"), (PH - PB - SIN + 1, "")]:
    if s:
        right.append(T(lx, yy, s, 4.8, 700 if "Gürtel" in s else 400, INK, "start"))
right += [f'<path d="M{F(lx-1)} {F(PB+SIN-1)}H{F(X0+stud_t*K+1)}M{F(lx-1)} 23H{F(xg+belt_t*K/2)}M{F(lx-1)} 43H{F(xb+back_t*K/2)}M{F(lx-1)} 55H{F(xf+front_t*K/2)}" style="stroke: #8a8f99; stroke-width: 0.35; fill: none"></path>',
          T(370, -14, "Schnitt von der Seite", 7, 700),
          T(370, 128, "Seiten offen: hier geht der Gürtel rein und raus", 4.8, 400, "#4a5262")]

W, H = 480, 175
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W*3}" height="{H*3}" viewBox="-20 -28 {W} {H}">'
       '<defs><marker id="ar" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0L6 3L0 6z" fill="#f3e4d0"></path></marker></defs>'
       f'<rect x="-20" y="-28" width="{W}" height="{H}" style="fill: #ffffff"></rect>'
       + "".join(left) + "".join(right) + "</svg>")
open(OUT_SVG, "w").write(svg)
subprocess.run(["node", os.path.join(HERE, "svg2png.mjs"), OUT_SVG, OUT_PNG, "1"], check=True)
os.remove(OUT_SVG)
print("ok", OUT_PNG)
