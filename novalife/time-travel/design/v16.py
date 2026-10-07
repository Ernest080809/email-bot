# -*- coding: utf-8 -*-
# Design v1.6 (07.10.2026, nach Ernests Skizze)
#   B2 · linke Gesäßtasche: drei Ähren wie in v1.4, Band einfach rot, neun Goldfäden darunter
#   B  · Serp im Stoppelfeld: kleiner Serp mit abgeschnittenen Halmen, linkes Bein vorn an der Seitennaht
# Einheiten: mm. Farben aus wheat3 (gleiche Garne wie bisher).
import math, random
import wheat3 as W
from wheat3 import F, pl, bez, path, rope, add

GOLD = "#d2a53a"; GOLDD = "#9c7520"          # Ähren wie v1.4
RED, REDD, REDL = W.RED, W.REDD, W.REDL
WHITE, WSH, BOUT = W.WHITE, W.WSH, W.BOUT
BR, BRD, BRL, OUT = W.BR, W.BRD, W.BRL, W.OUT
TH, THD = W.TH, W.THD
STUB, STUBK, STUBT = "#d9b45a", "#a8771f", "#f3e1a2"   # Stoppeln: Halm, Schatten, Schnittfläche

# ---------------------------------------------------------------- Ähre im Stil v1.4
def ear14(base, top, pairs=6, rx=1.5, ry=2.7, off=1.7, tilt=28):
    bx, by = base; tx, ty = top
    ang = math.degrees(math.atan2(ty - by, tx - bx))
    nx, ny = -(ty - by), (tx - bx); ln = math.hypot(nx, ny); nx, ny = nx / ln, ny / ln
    els = []
    for i in range(pairs):
        t = 0.14 + i * (0.78 / (pairs - 1))
        cx, cy = bx + (tx - bx) * t, by + (ty - by) * t
        for s in (-1, 1):
            ex, ey = cx + s * off * nx, cy + s * off * ny
            rot = ang + 90 - s * tilt
            els.append(f'<ellipse cx="{F(ex)}" cy="{F(ey)}" rx="{F(rx)}" ry="{F(ry)}" transform="rotate({F(rot)} {F(ex)} {F(ey)})"></ellipse>')
    els.append(f'<ellipse cx="{F(tx)}" cy="{F(ty)}" rx="{F(rx*0.9)}" ry="{F(ry)}" transform="rotate({F(ang+90)} {F(tx)} {F(ty)})"></ellipse>')
    return f'<g style="fill: {GOLD}; stroke: {GOLDD}; stroke-width: 0.3px">' + "".join(els) + '</g>'

# ---------------------------------------------------------------- B2 · Tasche
BAND = ((0.0, 22.0), (7.0, 25.4), (41.0, 25.4), (48.0, 22.0))   # Bandmitte, leicht durchhängend
BAND_W = 3.0                                                     # mm, einfach rot
CX = 24.0
def band_y(xq):
    best = None
    for i in range(801):
        t = i / 800; m = 1 - t
        x = m**3*BAND[0][0] + 3*m*m*t*BAND[1][0] + 3*m*t*t*BAND[2][0] + t**3*BAND[3][0]
        y = m**3*BAND[0][1] + 3*m*m*t*BAND[1][1] + 3*m*t*t*BAND[2][1] + t**3*BAND[3][1]
        if best is None or abs(x - xq) < abs(best[0] - xq): best = (x, y)
    return best[1]
BAND_MID_Y = band_y(CX)                                          # 24,55

THREAD_X = [16.5, 18.6, 20.6, 22.6, 24.5, 26.4, 28.3, 30.2, 32.0]
THREAD_L = [19, 25, 22, 30, 27, 21, 29, 18, 24]

def b2_v16(threads=True, seed=3):
    rnd = random.Random(seed)
    g = []
    # Goldfäden zuerst, sie kommen unter dem Band hervor
    if threads:
        for x, l in zip(THREAD_X, THREAD_L):
            y = band_y(x) + 1.1
            sway = rnd.uniform(0.8, 1.6) * (1 if rnd.random() < 0.5 else -1)
            pts = bez((x, y), (x + sway, y + l * 0.33), (x - sway, y + l * 0.68), (x + sway * 0.6, y + l), 24)
            g += rope(pts, 0.62, TH, o=THD, hl="#fbe9a8", hlw=0.35, hlop=0.75)
    # Halme der drei Ähren, treffen sich in der Bandmitte
    meet = (CX, BAND_MID_Y - 1.2)
    bases = [(21.4, 16.2), (CX, 15.2), (26.6, 16.2)]
    g.append(path("".join(f"M{F(b[0])} {F(b[1])}L{F(meet[0])} {F(meet[1])}" for b in bases), stroke=GOLD, w=1.2))
    # Band: einfach rot (Satin), keine weißen Zellen, kein weißer Rand
    d = (f"M{F(BAND[0][0])} {F(BAND[0][1])}C{F(BAND[1][0])} {F(BAND[1][1])} {F(BAND[2][0])} {F(BAND[2][1])} {F(BAND[3][0])} {F(BAND[3][1])}")
    g.append(path(d, stroke=REDD, w=BAND_W + 0.3))
    g.append(path(d, stroke=RED, w=BAND_W - 0.2))
    d_hl = (f"M{F(BAND[0][0]+1.2)} {F(BAND[0][1]-0.55)}C{F(BAND[1][0])} {F(BAND[1][1]-0.65)} {F(BAND[2][0])} {F(BAND[2][1]-0.65)} {F(BAND[3][0]-1.2)} {F(BAND[3][1]-0.55)}")
    g.append(path(d_hl, stroke=REDL, w=0.55, extra="; opacity: 0.8"))
    # drei Ähren: links, rechts, Mitte zuletzt (vorn)
    L, a = 12.0, math.radians(31)       # alle drei gleich lang, Abstand zum Taschensaum bleibt > 6 mm
    g.append(ear14(bases[0], (bases[0][0] - L * math.sin(a), bases[0][1] - L * math.cos(a)), pairs=5, rx=1.3, ry=2.3, off=1.5))
    g.append(ear14(bases[2], (bases[2][0] + L * math.sin(a), bases[2][1] - L * math.cos(a)), pairs=5, rx=1.3, ry=2.3, off=1.5))
    g.append(ear14(bases[1], (CX, bases[1][1] - L), pairs=5, rx=1.3, ry=2.3, off=1.5))
    return "\n".join(g)

# ---------------------------------------------------------------- B · Serp im Stoppelfeld
def sickle_small():
    """Kleiner Serp, aufrecht wie ein Fragezeichen: Griff unten, Klinge biegt nach oben und links, Spitze zeigt nach unten.
    Gebaut für Stickerei: wenige Flächen, klare Kontur, keine Glanzlinien unter 0,4 mm."""
    seg1 = bez((15.6, 22.6), (16.9, 15.6), (14.6, 7.6), (9.6, 6.4), 26)
    seg2 = bez((9.6, 6.4), (4.4, 5.2), (1.0, 9.6), (2.3, 15.4), 22)
    outer = seg1 + seg2[1:]
    N = len(outer) - 1
    inner, tt = [], []
    c = (8.8, 15.5)                     # liegt im Innern des Bogens
    for k, o in enumerate(outer):
        t = k / N
        a_, b_ = outer[max(0, k - 1)], outer[min(N, k + 1)]
        dx, dy = b_[0] - a_[0], b_[1] - a_[1]; Ln = math.hypot(dx, dy) or 1
        nrm = (-dy / Ln, dx / Ln)
        if (c[0] - o[0]) * nrm[0] + (c[1] - o[1]) * nrm[1] < 0: nrm = (-nrm[0], -nrm[1])
        w = 2.2 * (1 - t) ** 0.7 + 0.12
        inner.append((o[0] + nrm[0] * w, o[1] + nrm[1] * w)); tt.append((t, w, nrm))
    g = []
    g.append(path(pl(outer + inner[::-1]) + "Z", fill=WHITE, stroke=BOUT, w=0.34))
    # Schliff an der Schneide: grauweißer Streifen innen
    k0, k1 = int(N * 0.04), int(N * 0.96)
    e_in = inner[k0:k1]
    e_out = [(i_[0] - r[0] * min(0.8, w * 0.38), i_[1] - r[1] * min(0.8, w * 0.38)) for i_, (t, w, r) in zip(inner[k0:k1], tt[k0:k1])]
    g.append(path(pl(e_in + e_out[::-1]) + "Z", fill=WSH))
    g.append(path(pl(inner[k0:k1]), stroke=BOUT, w=0.3))
    # Zwinge und Griff, fast senkrecht
    heel = ((outer[0][0] + inner[0][0]) / 2, (outer[0][1] + inner[0][1]) / 2)
    hd = (math.cos(math.radians(86)), math.sin(math.radians(86))); hn = (-hd[1], hd[0])
    f0, f1 = add(heel, hd, 0.2), add(heel, hd, 2.4)
    def quad(a, b, wa, wb, fill, sw=0.34):
        p = [add(a, hn, wa / 2), add(b, hn, wb / 2), add(b, hn, -wb / 2), add(a, hn, -wa / 2)]
        return path(pl(p) + "Z", fill=fill, stroke=OUT, w=sw)
    g.append(quad(f0, f1, 2.5, 2.8, BRD))
    h0 = f1; hlen = 10.5; h1 = add(h0, hd, hlen); hm = add(h0, hd, hlen * 0.5)
    hp = [add(h0, hn, 1.3), add(hm, hn, 1.6), add(h1, hn, 1.35), add(add(h1, hd, 1.0), hn, 0.6),
          add(add(h1, hd, 1.0), hn, -0.6), add(h1, hn, -1.35), add(hm, hn, -1.6), add(h0, hn, -1.3)]
    g.append(path(pl(hp) + "Z", fill=BR, stroke=OUT, w=0.34))
    g.append(path(pl([add(add(h0, hd, 0.7), hn, 0.7), add(hm, hn, 0.8), add(add(h1, hd, 0.1), hn, 0.65)]), stroke=BRL, w=0.45))
    return "\n".join(g), dict(outer=outer, inner=inner, handle_end=add(h1, hd, 1.0))

# Stoppeln: Büschel aus 2–3 abgeschnittenen Halmen, schräge Schnittkante, oben kleiner (weiter weg), unten größer
TUFTS = [  # (x, Fuß-y, Grundhöhe, Anzahl Halme, Seed)
    (3.0, 16.4, 2.2, 2, 1), (8.2, 17.0, 2.0, 3, 2), (12.6, 17.6, 2.3, 2, 3),
    (1.8, 24.0, 3.0, 3, 4), (7.0, 24.6, 2.8, 2, 5), (11.6, 25.4, 3.2, 3, 6),
    (3.4, 32.2, 3.8, 2, 7), (8.6, 33.0, 3.6, 3, 8), (13.0, 33.4, 3.4, 2, 9),
    (2.0, 40.0, 4.4, 3, 10), (7.4, 40.6, 4.0, 2, 11), (12.4, 41.0, 4.6, 3, 12), (20.2, 40.4, 3.8, 2, 13),
]
STUB, STUBK = "#dcc07a", "#a8833a"
def stubble():
    g = []
    for x0, yb, h0, n, seed in TUFTS:
        rnd = random.Random(seed)
        angs = {2: [-9, 8], 3: [-13, 1, 12]}[n]
        for k, a_deg in enumerate(angs):
            a = math.radians(a_deg + rnd.uniform(-3, 3))
            h = h0 * rnd.uniform(0.75, 1.1)
            w = 0.72
            d = (math.sin(a), -math.cos(a)); nn = (-d[1], d[0])
            b = (x0 + (k - (n - 1) / 2) * 0.55, yb)
            t = add(b, d, h)
            cut = 0.55 * (1 if rnd.random() < 0.5 else -1)          # schräger Schnitt
            poly = [add(b, nn, -w / 2), add(add(t, nn, -w / 2), d, cut / 2), add(add(t, nn, w / 2), d, -cut / 2), add(b, nn, w / 2)]
            g.append(path(pl(poly) + "Z", fill=STUB, stroke=STUBK, w=0.16))
            g.append(path(pl([add(add(b, nn, w * 0.22), d, 0.2), add(add(t, nn, w * 0.22), d, -0.5)]), stroke=STUBK, w=0.22, extra="; opacity: 0.8"))
    return "\n".join(g)

def side_v16():
    sk, _ = sickle_small()
    return stubble() + "\n" + sk

B2_V16 = b2_v16(True)
B2_V16_NT = b2_v16(False)
SIDE_V16 = side_v16()

if __name__ == "__main__":
    import os
    os.makedirs("v16", exist_ok=True)
    open("v16/b2.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="560" height="640" viewBox="-4 -4 56 64"><rect x="-4" y="-4" width="56" height="64" style="fill: #2f4a6e"></rect>{B2_V16}</svg>')
    open("v16/side.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="300" height="460" viewBox="-3 0 30 46"><rect x="-3" y="0" width="30" height="46" style="fill: #2f4a6e"></rect><path d="M25 0V46" style="stroke: #d4ab52; stroke-width: 0.5px; stroke-dasharray: 1.6 1.2"></path>{SIDE_V16}</svg>')
    print("ok", len(B2_V16), len(SIDE_V16))
