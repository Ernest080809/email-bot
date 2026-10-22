# -*- coding: utf-8 -*-
# Technische Zeichnungen (Flats) NVL-TT-01, Basis W32, vorn und hinten (22.10.2026)
#   Koordinaten in Kleidungs-mm: x = 0 vordere bzw. hintere Mitte, y = 0 Bundoberkante.
#   Vorderansicht: links im Bild = rechts am Träger. Rückansicht: links im Bild = links am Träger.
#   Schematisch nach den Messpunkten; verbindlich sind die Maße im Tech Pack.
import math
import fine as FN

F = FN.F
WB = 40.0
INK, STITCH, RED, GOLD, COP, LINEN = "#1b2230", "#b07a50", "#b8322a", "#c9a24a", "#a8643a", "#efe7d6"
LBL = "#9c5a30"

SIDE = [(215, 0), (221, 40), (252, 140), (260, 190), (266, 290), (248, 620), (242, 1100)]   # Seitennaht (rechte Bildhälfte)
INSEAM = [(0, 290), (7, 330), (24, 620), (32, 1100)]                                          # Innennaht ab Schritt


def cr(pts):
    """Catmull-Rom durch die Punkte als kubische Bezier-Segmente (ohne Anfangs-M)."""
    d = ""
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i else pts[i]; p1, p2 = pts[i], pts[i + 1]; p3 = pts[i + 2] if i + 2 < len(pts) else pts[i + 1]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{F(c1[0])} {F(c1[1])} {F(c2[0])} {F(c2[1])} {F(p2[0])} {F(p2[1])}"
    return d


def mir(pts):
    return [(-x, y) for x, y in pts]


def outline():
    right = SIDE; left = mir(SIDE)
    d = f"M{F(left[0][0])} 0L{F(right[0][0])} 0" + cr(right)
    d += f"L{F(INSEAM[-1][0])} 1100" + cr(INSEAM[::-1])
    d += cr(mir(INSEAM)) + f"L{F(left[-1][0])} 1100" + cr(left[::-1]) + "Z"
    return d


def side_x(y):
    for (x0, y0), (x1, y1) in zip(SIDE, SIDE[1:]):
        if y0 <= y <= y1:
            return x0 + (x1 - x0) * (y - y0) / (y1 - y0)
    return SIDE[-1][0]


def st(d, w=1.6):
    return f'<path d="{d}" style="fill: none; stroke: {STITCH}; stroke-width: {w}; stroke-dasharray: 5 3.5"></path>'


def ln(d, w=2.4, col=INK, fill="none"):
    return f'<path d="{d}" style="fill: {fill}; stroke: {col}; stroke-width: {w}; stroke-linejoin: round"></path>'


def rivet(x, y, r=4.5):
    return f'<circle cx="{F(x)}" cy="{F(y)}" r="{F(r)}" style="fill: {COP}; stroke: #6f3d1f; stroke-width: 1"></circle>'


def tack(x0, y0, x1, y1):
    return f'<path d="M{F(x0)} {F(y0)}L{F(x1)} {F(y1)}" style="stroke: {STITCH}; stroke-width: 4.5; stroke-linecap: round"></path>'


def callout(k, x, y, tx, ty):
    return (f'<path d="M{F(x)} {F(y)}L{F(tx)} {F(ty)}" style="stroke: {LBL}; stroke-width: 1.2"></path>'
            f'<circle cx="{F(tx)}" cy="{F(ty)}" r="17" style="fill: {LBL}"></circle>'
            f'<text x="{F(tx)}" y="{F(ty+6.5)}" style="font: 700 {18 if len(k) < 2 else 14}px Helvetica, Arial, sans-serif; fill: #fff; text-anchor: middle">{k}</text>')


def loops(xs):
    return "".join(f'<rect x="{F(x-5.5)}" y="-4" width="11" height="{F(WB+6)}" rx="2" style="fill: #fff; stroke: {INK}; stroke-width: 1.6"></rect>'
                   + tack(x - 4, -1, x + 4, -1) + tack(x - 4, WB + 1, x + 4, WB + 1) for x in xs)


def cubic(p0, c1, c2, p1, n=60):
    out = []
    for i in range(n + 1):
        t = i / n; a = (1 - t) ** 3; b = 3 * (1 - t) ** 2 * t; c = 3 * (1 - t) * t * t; e = t ** 3
        out.append((a * p0[0] + b * c1[0] + c * c2[0] + e * p1[0], a * p0[1] + b * c1[1] + c * c2[1] + e * p1[1]))
    return out


def offset(pts, dist):
    res = []
    for i, (x, y) in enumerate(pts):
        a = pts[max(i - 1, 0)]; b = pts[min(i + 1, len(pts) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]; L = math.hypot(tx, ty) or 1
        res.append((x - ty / L * dist, y + tx / L * dist))
    return res


def poly(pts, close=False):
    return "M" + "L".join(f"{F(x)} {F(y)}" for x, y in pts) + ("Z" if close else "")


# ================= Vorderansicht =================
def front():
    o = [ln(outline(), 2.6, INK, "#ffffff")]
    xs40 = side_x(WB)
    o.append(ln(f"M{F(-xs40)} {F(WB)}L{F(xs40)} {F(WB)}"))                        # Bundunterkante
    o.append(st(f"M{F(-214)} 3.5H214M{F(-xs40+1)} {F(WB-3.5)}H{F(xs40-1)}"))
    o.append(ln(f"M0 {F(WB)}V190", 1.8))                                          # vordere Mitte (Schlitzkante)
    o.append(ln("M0 190V290", 1.8))
    o.append(st("M38 41V160Q38 188 4 192M32 41V158Q32 182 4 185"))               # J-Naht doppelt
    o.append(tack(2, 192, 10, 196))
    o.append(f'<circle cx="0" cy="20" r="10" style="fill: {COP}; stroke: #6f3d1f; stroke-width: 1.2"></circle>')
    for s in (-1, 1):                                                             # Vordertaschen 11 x 7 cm
        ys = WB + 70; xs = side_x(ys)
        p0, c1, c2, p1 = (s * (xs40 - 110), WB), (s * (xs40 - 106), WB + 46), (s * (xs40 - 50), ys - 2), (s * xs, ys)
        o.append(ln(f"M{F(p0[0])} {F(p0[1])}C{F(c1[0])} {F(c1[1])} {F(c2[0])} {F(c2[1])} {F(p1[0])} {F(p1[1])}", 2.2))
        crv = cubic(p0, c1, c2, p1)
        inward = -1 if s < 0 else 1                                               # Richtung Vorderteil
        o.append(st(poly(offset(crv, 4 * inward))))
        o.append(st(poly(offset(crv, 10 * inward))))
        o.append(rivet(p0[0] + s * -3, WB + 6)); o.append(rivet(p1[0] - s * 7, p1[1] - 3))
        if s < 0:                                                                 # rechts am Träger: Band A und Münztasche E
            band = offset(crv, 23 * inward)
            o.append(f'<path d="{poly(crv + band[::-1], True)}" style="fill: {RED}; opacity: 0.85"></path>')
            fac = f"M{F(p0[0])} {F(p0[1])}C{F(c1[0])} {F(c1[1])} {F(c2[0])} {F(c2[1])} {F(p1[0])} {F(p1[1])}L{F(-xs40)} {F(WB)}Z"
            ex0 = (-xs40 + p0[0]) / 2 - 31
            o.append(f'<clipPath id="facing"><path d="{fac}"></path></clipPath>')
            o.append(f'<rect x="{F(ex0)}" y="{F(WB+5)}" width="62" height="62" style="fill: none; stroke: {INK}; stroke-width: 1.2; stroke-dasharray: 4 3"></rect>')
            o.append(f'<g clip-path="url(#facing)"><rect x="{F(ex0)}" y="{F(WB+5)}" width="62" height="62" style="fill: {RED}; stroke: {INK}; stroke-width: 1.6"></rect></g>')
            o.append(rivet(ex0 + 5, WB + 10)); o.append(rivet(ex0 + 57, WB + 10))
            A_at, E_at = band[len(band) // 2], (ex0 + 31, WB + 36)
    o.append(loops((-98, 98)))
    o.append(st(poly([(x - 7, y) for x, y in mir(INSEAM)])) + st(poly([(x + 7, y) for x, y in INSEAM])))
    o.append(callout("A", A_at[0], A_at[1], -170, 230))
    o.append(callout("E", E_at[0], E_at[1], -300, 40))
    o.append(callout("K", 8, 22, 110, -60))
    o.append(callout("N", -112, 46, -60, 120))
    o.append(callout("J", 38, 150, 120, 200))
    o.append(callout("H", -150, 1100, -300, 1060))
    return o


# ================= Rückansicht =================
def back():
    o = [ln(outline(), 2.6, INK, "#ffffff")]
    xs40 = side_x(WB)
    o.append(ln(f"M{F(-xs40)} {F(WB)}L{F(xs40)} {F(WB)}"))
    o.append(st(f"M{F(-214)} 3.5H214M{F(-xs40+1)} {F(WB-3.5)}H{F(xs40-1)}"))
    yk = [(-side_x(WB + 30), WB + 30), (0, WB + 95), (side_x(WB + 30), WB + 30)]  # Passe 9,5 cm Mitte, 3 cm Seite
    o.append(ln(poly(yk), 2.0)); o.append(st(poly([(x, y + 5) for x, y in yk])))
    o.append(ln(f"M0 {F(WB)}V290", 2.0)); o.append(st(f"M-6 {F(WB+95)}V285M6 {F(WB+95)}V285"))
    dx = 15; h_in = math.sqrt(125**2 - dx**2); h_out = math.sqrt(120**2 - dx**2); tip = math.sqrt(70**2 - 65**2)
    pockets = {}
    for s in (-1, 1):                                                             # Gesäßtaschen 160/130, innen 5 mm höher
        if s < 0:
            pts = [(0, h_in - h_out), (160, 0), (145, h_in), (80, h_in + tip), (15, h_in)]; X0 = -195
        else:
            pts = [(0, 0), (160, h_in - h_out), (145, h_in), (80, h_in + tip), (15, h_in)]; X0 = 35
        P = [(X0 + x, WB + 85 + y) for x, y in pts]
        o.append(ln(poly(P, True), 2.2))
        o.append(st(poly([(x + (4 if x < X0 + 80 else -4), y + (3 if y < WB + 100 else -4)) for x, y in P], True), 1.4))
        o.append(tack(P[0][0] + 2, P[0][1] + 2, P[0][0] + 2, P[0][1] + 12)); o.append(tack(P[1][0] - 2, P[1][1] + 2, P[1][0] - 2, P[1][1] + 12))
        pockets[s] = (X0 + 80, WB + 85 + 47)
    bx, by = pockets[-1]                                                          # B2: Band, drei Ähren, Goldfäden
    o.append(f'<rect x="{F(bx-24)}" y="{F(by-3)}" width="48" height="6" style="fill: {RED}"></rect>')
    for ex in (-9, 0, 9):
        o.append(f'<ellipse cx="{F(bx+ex)}" cy="{F(by-14)}" rx="3.5" ry="10" style="fill: {GOLD}"></ellipse>')
    o.append("".join(f'<path d="M{F(bx-12+i*3)} {F(by+3)}v{F(18+(i%3)*5)}" style="stroke: {GOLD}; stroke-width: 1.2"></path>' for i in range(9)))
    cx, cy = pockets[1]
    o.append(FN.star8_svg(cx, cy, 36.0, 1.0))
    o.append(loops((-180, 0, 180)))
    D = FN.patch_outline(50, 0, 80, 71, 5.5)                                       # Patch D hinten rechts, oben bündig
    o.append(f'<path d="{D}" style="fill: {LINEN}; stroke: {INK}; stroke-width: 2"></path>')
    o.append("".join(f'<circle cx="{F(x)}" cy="{F(y)}" r="5" style="fill: none; stroke: {COP}; stroke-width: 1.2; stroke-dasharray: 2 1.5"></circle>'
                     for x in (57, 123) for y in (12.5, 58.5)))
    o.append(f'<text x="90" y="44" style="font: 700 22px Helvetica, Arial, sans-serif; fill: {INK}; text-anchor: middle">D</text>')
    o.append(st(poly([(x - 7, y) for x, y in mir(INSEAM)])) + st(poly([(x + 7, y) for x, y in INSEAM])))
    o.append(callout("D", 130, 30, 300, 10))
    o.append(callout("B2", bx - 20, by, -300, 150))
    o.append(callout("C", cx + 18, cy, 300, 230))
    o.append(callout("Y", 120, WB + 66, 300, 110))
    return o


def svg(parts, title):
    return (f'<svg viewBox="-330 -95 660 1215" class="flat"><text x="0" y="-62" style="font: 700 26px Helvetica, Arial, sans-serif; fill: {INK}; text-anchor: middle">{title}</text>'
            + "".join(parts) + "</svg>")


FRONT = svg(front(), "FRONT")
BACK = svg(back(), "BACK")
LEGEND = [("A", "Cross-stitch band along the right front pocket opening (as worn), inner edge on the opening"),
          ("E", "Coin pocket fully embroidered, 62 × 62 mm. Keep the pocket opening as specified (11 × 7 cm). The lower inner corner may sit under the opening edge, as on a classic 5-pocket jeans"),
          ("K", "20 mm shank button, eight-point star"), ("N", "Rivets 9 mm: both ends of each front pocket opening, both top corners of the coin pocket"),
          ("J", "Zip fly, J-stitch double needle, bartack at the end"),
          ("B2", "Left back pocket (as worn): band 48 mm, three wheat ears, 9 gold threads by hand after wash"),
          ("C", "Right back pocket: eight-point star 36 × 36 mm, same height as the B2 band"),
          ("D", "Patch D: two-layer belt loop, top flush with the waistband, centred between centre back loop and right loop. Snaps hidden (dashed)"),
          ("Y", "Back yoke: 9.5 cm at centre back, 3 cm at the side seam, flat-felled"),
          ("H", "Hem: raw edge, cut after the wash, no stitching")]

FRONT_DE = svg(front(), "VORN")
BACK_DE = svg(back(), "HINTEN")
LEGEND_DE = [("A", "Kreuzstich-Band an der rechten Vordertasche (vom Träger aus), Innenkante auf der Taschenöffnung"),
             ("E", "Münztasche voll bestickt, 62 × 62 mm. Taschenöffnung bleibt 11 × 7 cm, die untere innere Ecke darf unter dem Rand liegen wie bei einer klassischen 5-Pocket"),
             ("K", "Knopf 20 mm mit Achtstern"), ("N", "Nieten 9 mm: an beiden Enden jeder Vordertaschenöffnung, an beiden oberen Ecken der Münztasche"),
             ("J", "Reißverschluss, J-Naht doppelt gesteppt, Riegel am Ende"),
             ("B2", "Linke Gesäßtasche (vom Träger aus): Band 48 mm, drei Ähren, 9 Goldfäden von Hand nach der Wäsche"),
             ("C", "Rechte Gesäßtasche: Achtstern 36 × 36 mm, gleiche Höhe wie das B2-Band"),
             ("D", "Patch D: Gürtelschlaufe aus zwei Lagen, oben bündig mit dem Bund, mittig zwischen Mittelschlaufe und rechter Schlaufe. Druckknöpfe versteckt (gestrichelt)"),
             ("Y", "Passe hinten: 9,5 cm an der Mitte, 3 cm an der Seitennaht, Kappnaht"),
             ("H", "Saum: roh, nach der Wäsche geschnitten, ohne Naht")]

if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "v19", "flats.html"), "w").write(
        '<!doctype html><html><body style="margin:0;background:#fff;display:flex;gap:20px">'
        f'<div style="width:480px">{FRONT}</div><div style="width:480px">{BACK}</div></body></html>')
    print("ok")
