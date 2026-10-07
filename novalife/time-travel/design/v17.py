# -*- coding: utf-8 -*-
# Design v1.7 (07.10.2026, Ernest: „nicht so klein, ein schöner Serp wie davor, weiß, rot und grau, dazu die goldenen Halme“)
#   B · Serp im Stoppelfeld, groß: der Serp aus v1.5 (weiße Klinge, rote Schneide, grauer Schliff, brauner Griff)
#       steht über goldenen, abgeschnittenen Halmen. Linkes Bein vorn an der Seitennaht.
# Einheiten mm. Die Koordinaten des Serp sind die aus wheat3 (v1.5), die Stoppeln werden darum gesetzt.
import math, random
import wheat3 as W
from wheat3 import F, pl, bez, path, rope, add, cut_face

GD, GDL, GDK, OC, OUT = W.GD, W.GDL, W.GDK, W.OC, W.OUT

# Stoppelfeld: Büschel aus 2–3 abgeschnittenen Halmen mit schräger Schnittkante, in versetzten Reihen.
# Hinten kleiner und enger, vorn größer. Rechts vom Griff ein Büschel wie in Ernests Skizze.
ROWS = [  # (Fuß-y, x-Positionen, Grundhöhe)
    (71.0, [20.5, 26.2, 31.8], 4.4),
    (79.4, [16.6, 22.6, 28.6, 34.6], 5.4),
    (88.0, [14.0, 20.4, 26.8, 33.2, 39.6], 6.4),
    (96.8, [12.6, 19.4, 26.2, 33.0, 39.8, 54.6], 7.4),
]
COLS = [GD, GDL, OC]
STRAW_TIP = "#f3e1a2"

def stalk(b, a_deg, h, col, cut, w0=1.15, w1=0.95):
    a = math.radians(a_deg)
    d = (math.sin(a), -math.cos(a)); nn = (-d[1], d[0])
    t = add(b, d, h)
    tl = add(add(t, nn, -w1 / 2), d, cut / 2); tr = add(add(t, nn, w1 / 2), d, -cut / 2)
    poly = [add(b, nn, -w0 / 2), tl, tr, add(b, nn, w0 / 2)]
    g = [path(pl(poly) + "Z", fill=col, stroke=OUT, w=0.3)]
    g.append(path(pl([add(add(b, nn, w0 * 0.2), d, 0.3), add(add(t, nn, w1 * 0.2), d, -abs(cut) - 0.35)]), stroke=GDK, w=0.26, extra="; opacity: 0.85"))
    g.append(path(pl([tl, tr]), stroke=STRAW_TIP, w=0.36))
    return g

def stubble_big():
    g = []
    k = 0
    for r, (yb, xs, h0) in enumerate(ROWS):
        rnd = random.Random(10 + r)
        for x0 in xs:
            n = rnd.choice([2, 3, 3])
            spread = {2: [-9, 8], 3: [-14, 1, 13]}[n]
            for i, a_deg in enumerate(spread):
                b = (x0 + (i - (n - 1) / 2) * 0.95 + rnd.uniform(-0.25, 0.25), yb + rnd.uniform(-0.6, 0.6))
                h = h0 * rnd.uniform(0.75, 1.12)
                cut = rnd.choice([-1, 1]) * rnd.uniform(0.55, 0.85)
                g += stalk(b, a_deg + rnd.uniform(-4, 4), h, COLS[k % 3], cut); k += 1
    return g

def side_big():
    sk, geo = W.sickle()
    g = stubble_big()
    g += [sk["blade"], sk["shade"], sk["gloss"], sk["edge"], sk["edge2"], sk["handle"]]
    return "\n".join(g)

SIDE_V17 = side_big()

if __name__ == "__main__":
    import os
    os.makedirs("v17", exist_ok=True)
    open("v17/side.svg", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="560" height="600" viewBox="6 48 56 60">'
        f'<rect x="6" y="48" width="56" height="60" style="fill: #2f4a6e"></rect>{SIDE_V17}</svg>')
    print("ok", len(SIDE_V17))
