# -*- coding: utf-8 -*-
# Skizze 21.10.2026: Patch D und Standardgürtel (38 mm), jetzt vs. Vorschlag „Patch unter dem Bund“
#   Maße in mm, Rückseite von hinten gesehen, hintere Mitte links. Basis W32.
import base64, os, subprocess
import fine as FN

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_SVG = os.path.join(HERE, "v19", "patch_belt.svg")
OUT_PNG = os.path.join(HERE, "..", "rev6", "skizzen", "2026-10-21_patch_guertel_varianten.png")
F = FN.F
PHOTO = "data:image/png;base64," + base64.b64encode(open(os.path.join(HERE, "v19", "patch_d.png"), "rb").read()).decode()

WB, BELT = 40.0, 38.0                    # Bundhöhe, Standardgürtel
PW, PH, PB, SIN, SD = 80.0, 71.0, 5.5, 7.0, 10.0
PX = 15.0                                # Patch links, mittig zwischen Mittelschlaufe (0) und rechter Schlaufe (110)
LOOPS = (0.0, 110.0)
YOKE = lambda x: WB + 95 - 65 * x / 215  # Passennaht: 9,5 cm an der Mitte, 3 cm an der Seite
DEN, DEN2, STITCH, BELTC = "#3a5a82", "#34516f", "#c8954f", "#5a3a22"


def T(x, y, s, size=5.2, w=700, fill="#1b2230", anchor="middle"):
    return f'<text x="{F(x)}" y="{F(y)}" style="font: {w} {F(size)}px Helvetica, Arial, sans-serif; fill: {fill}; text-anchor: {anchor}">{s}</text>'


def panel(ox, top, title, sub, ok):
    g = [f'<g transform="translate({F(ox)} 0)">',
         f'<rect x="-15" y="-6" width="230" height="186" style="fill: {DEN}"></rect>',
         f'<rect x="-15" y="0" width="230" height="{F(WB)}" style="fill: {DEN2}"></rect>',
         f'<path d="M-15 3h230M-15 {F(WB-3)}h230" style="fill: none; stroke: {STITCH}; stroke-width: 0.6; stroke-dasharray: 2 1.4"></path>',
         f'<path d="M0 {F(WB)}V180" style="stroke: #22354f; stroke-width: 0.8"></path>',
         f'<path d="M0 {F(YOKE(0))}L215 {F(YOKE(215))}" style="stroke: {STITCH}; stroke-width: 0.6; stroke-dasharray: 2 1.4; fill: none"></path>',
         f'<path d="M35 {F(WB+85)}L195 {F(WB+90)}L192 180M35 {F(WB+85)}L38 180" style="fill: none; stroke: {STITCH}; stroke-width: 0.7; stroke-dasharray: 2 1.4"></path>',
         T(115, WB + 103, "rechte Gesäßtasche C", 4.2, 400, "#c9d6e8")]
    belt = (f'<rect x="-15" y="1" width="230" height="{F(BELT)}" style="fill: {BELTC}"></rect>'
            f'<rect x="168" y="6" width="22" height="28" rx="2" style="fill: none; stroke: #b98a4a; stroke-width: 2"></rect>')
    loops = "".join(f'<rect x="{F(x-5.5)}" y="-4" width="11" height="{F(WB+6)}" rx="1" style="fill: {DEN}; stroke: #22354f; stroke-width: 0.6"></rect>' for x in LOOPS)
    outline = FN.patch_outline(PX, top, PW, PH, PB)
    patch = (f'<clipPath id="pc{int(ox)}"><path d="{outline}"></path></clipPath>'
             f'<image href="{PHOTO}" x="{F(PX)}" y="{F(top)}" width="{F(PW)}" height="{F(PH)}" preserveAspectRatio="none" clip-path="url(#pc{int(ox)})"></image>'
             f'<path d="{outline}" style="fill: none; stroke: #2a1d12; stroke-width: 0.6"></path>')
    snaps = [(PX + SIN, top + PB + SIN), (PX + PW - SIN, top + PB + SIN),
             (PX + SIN, top + PH - PB - SIN), (PX + PW - SIN, top + PH - PB - SIN)]
    if ok:      # Gürtel frei über dem Bund, Patch darunter
        g += [belt, loops, patch]
        g += [f'<circle cx="{F(x)}" cy="{F(y)}" r="{F(SD/2)}" style="fill: #a8643a; stroke: #6f3d1f; stroke-width: 0.6"></circle>' for x, y in snaps]
        g.append(T(150, 22, "Gürtel läuft frei", 6, 700, "#e9f3ea"))
    else:       # Gürtel soll hinter dem Patch durch, obere Knöpfe im Weg
        g += [belt, loops, patch,
              f'<rect x="{F(PX)}" y="1" width="{F(PW)}" height="{F(BELT)}" style="fill: none; stroke: #f0c060; stroke-width: 0.8; stroke-dasharray: 3 2"></rect>']
        for i, (x, y) in enumerate(snaps):
            bad = i < 2
            g.append(f'<circle cx="{F(x)}" cy="{F(y)}" r="{F(SD/2)}" style="fill: {"#d23b2e" if bad else "#a8643a"}; stroke: {"#fff" if bad else "#6f3d1f"}; stroke-width: {0.9 if bad else 0.6}"></circle>')
        y0, y1 = top + PB + SIN + SD / 2, top + PH - PB - SIN - SD / 2
        g += [f'<path d="M{F(PX+PW+12)} {F(y0)}V{F(y1)}M{F(PX+PW+9)} {F(y0)}h6M{F(PX+PW+9)} {F(y1)}h6" style="stroke: #fff; stroke-width: 0.7; fill: none"></path>',
              T(PX + PW + 16, (y0 + y1) / 2 + 1.5, "nur 36 mm frei", 4.6, 700, "#fff", "start"),
              T(150, 22, "Gürtel 38 mm", 6, 700, "#f3e4d0"),
              T(PX + PW / 2, top + PH + 10, "obere Knöpfe sitzen im Gürtelweg", 5, 700, "#ffd2cc")]
    g += ["</g>", T(ox + 100, -14, title, 7.5, 700), T(ox + 100, 189, sub, 5.6, 700, "#4a5262")]
    return "".join(g)


W, H = 500, 222
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W*3}" height="{H*3}" viewBox="-20 -28 {W} {H}">'
       f'<rect x="-20" y="-28" width="{W}" height="{H}" style="fill: #ffffff"></rect>'
       + panel(0, 0, "Jetzt: Patch auf dem Bund", "Standardgürtel passt nicht durch", False)
       + panel(250, WB + 2, "Vorschlag: Patch direkt unter dem Bund", "Gürtel frei, Patch voll sichtbar, Knöpfe ohne Zug", True)
       + "</svg>")
open(OUT_SVG, "w").write(svg)
subprocess.run(["node", os.path.join(HERE, "svg2png.mjs"), OUT_SVG, OUT_PNG, "1"], check=True)
print("ok", OUT_PNG)
