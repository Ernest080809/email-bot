# -*- coding: utf-8 -*-
# Patch D als klare Vektor-Vorlage fürs Digitizing (Nargiza, WhatsApp 05.11.2026: „нужен прям четкий рисунок“).
#   Nachzeichnung von v19/patch_d.png als flache Grafik in den 4 Garnfarben, Maße in mm (80 × 71), Leinen bleibt frei.
#   Aufbau wie im Original: Ring mit 4 roten Rauten, Lebensbaum mit gedrehtem Stamm, Krone und Wurzeln mit Einrollungen,
#   links und rechts ein Flechtknoten, unten „NL“, Ecken-Ornamente, Steppstich am Rand.
#   Ausgabe: v19/patch_d_vector.svg (Schrift als Pfade) und v19/patch_d_vector.html (Vorschau).
import math, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import fine as FN

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "fonts", "CinzelDecorative-Bold.woff2")
F = FN.F
COL = dict(linen="#E8DCC6", brown="#56352D", copper="#A3623B", gold="#D8AE47", red="#CD212A")
W, H = 80.0, 71.0
CX, CY = 40.0, 35.5
RING_R, RING_W = 31.0, 1.5
GAP = 0.42                     # Abstand, wo ein Ast unter einem anderen durchläuft
OUT = 0.32                     # Kontur der Goldknoten


# ---------------- Kurven ----------------
def catmull(P, n=14):
    """Glatte Kurve durch alle Punkte P (Catmull-Rom, zentripetal)."""
    P = [P[0]] + list(P) + [P[-1]]
    out = [P[1]]
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        def tj(ti, a, b):
            return ti + max(math.hypot(b[0] - a[0], b[1] - a[1]), 1e-6) ** 0.5
        t0 = 0; t1 = tj(t0, p0, p1); t2 = tj(t1, p1, p2); t3 = tj(t2, p2, p3)
        for k in range(1, n + 1):
            t = t1 + (t2 - t1) * k / n
            def L(a, b, ta, tb):
                if tb - ta < 1e-9: return a
                return ((tb - t) / (tb - ta) * a[0] + (t - ta) / (tb - ta) * b[0], (tb - t) / (tb - ta) * a[1] + (t - ta) / (tb - ta) * b[1])
            A1 = L(p0, p1, t0, t1); A2 = L(p1, p2, t1, t2); A3 = L(p2, p3, t2, t3)
            B1 = L(A1, A2, t0, t2); B2 = L(A2, A3, t1, t3)
            out.append(L(B1, B2, t1, t2))
    return out


def resample(pts, step=0.12, closed=False):
    if closed: pts = pts + [pts[0]]
    d = [0.0]
    for a, b in zip(pts, pts[1:]): d.append(d[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    L = d[-1]; n = max(2, int(L / step))
    out, j = [], 0
    for i in range(n + (0 if closed else 1)):
        s = L * i / n
        while j < len(d) - 2 and d[j + 1] < s: j += 1
        seg = d[j + 1] - d[j] or 1
        u = (s - d[j]) / seg
        out.append((pts[j][0] + u * (pts[j + 1][0] - pts[j][0]), pts[j][1] + u * (pts[j + 1][1] - pts[j][1])))
    return out


def curl(pts, r=1.3, turns=1.15, side=1, n=60):
    """Hängt an das Ende eine Einrollung an (side=+1 rechtsherum in Bildkoordinaten, -1 linksherum)."""
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    a = math.atan2(y1 - y0, x1 - x0)
    nx, ny = -math.sin(a) * side, math.cos(a) * side
    cx, cy = x1 + nx * r, y1 + ny * r
    a0 = math.atan2(y1 - cy, x1 - cx)
    out = []
    for i in range(1, n + 1):
        t = i / n
        ang = a0 + side * turns * 2 * math.pi * t
        rr = r * (1 - 0.5 * t)
        out.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    return pts + out


def mirror(pts):
    return [(2 * CX - x, y) for x, y in pts]


def tangent(pts, i, closed):
    n = len(pts)
    a = pts[(i - 1) % n] if closed else pts[max(i - 1, 0)]
    b = pts[(i + 1) % n] if closed else pts[min(i + 1, n - 1)]
    tx, ty = b[0] - a[0], b[1] - a[1]; l = math.hypot(tx, ty) or 1
    return tx / l, ty / l


def poly(pts, ws, extra=0.0, caps=True, closed=False, i0=None, i1=None):
    """Umriss eines Bandes mit Breite ws (+extra). Teilstück i0..i1 mit flachen Enden."""
    n = len(pts)
    if i0 is None:
        idx = list(range(n))
    else:
        idx = [k % n for k in range(i0, i1 + 1)] if closed else list(range(max(i0, 0), min(i1, n - 1) + 1))
        caps = False
    L, R = [], []
    for k in idx:
        tx, ty = tangent(pts, k, closed)
        w = (ws[k] + extra) / 2
        x, y = pts[k]
        L.append((x - ty * w, y + tx * w)); R.append((x + ty * w, y - tx * w))
    if closed and i0 is None:
        return "M" + " L".join(f"{F(x)} {F(y)}" for x, y in L) + "Z M" + " L".join(f"{F(x)} {F(y)}" for x, y in R[::-1]) + "Z"
    d = "M" + " L".join(f"{F(x)} {F(y)}" for x, y in L)
    if caps:
        we = (ws[idx[-1]] + extra) / 2
        d += f" A{F(we)} {F(we)} 0 0 0 {F(R[-1][0])} {F(R[-1][1])}"
    else:
        d += f" L{F(R[-1][0])} {F(R[-1][1])}"
    d += " L" + " L".join(f"{F(x)} {F(y)}" for x, y in R[::-1][1:])
    if caps:
        ws0 = (ws[idx[0]] + extra) / 2
        d += f" A{F(ws0)} {F(ws0)} 0 0 0 {F(L[0][0])} {F(L[0][1])}"
    return d + " Z"


def line(pts, closed=False):
    return "M" + " L".join(f"{F(x)} {F(y)}" for x, y in pts) + ("Z" if closed else "")


# ---------------- Stränge und Kreuzungen ----------------
class Strand:
    def __init__(self, pts, w0, w1=None, style="tree", closed=False, taper=0.25, hl=True):
        self.closed = closed
        self.pts = resample(pts, 0.12, closed)
        n = len(self.pts); w1 = w0 if w1 is None else w1
        if closed or taper >= 1:
            self.ws = [w0] * n
        else:
            self.ws = [w0 + (w1 - w0) * max(0.0, (i / (n - 1) - (1 - taper)) / taper) for i in range(n)]
        self.style = style; self.hl = hl


def seg_x(p1, p2, p3, p4):
    d = (p2[0] - p1[0]) * (p4[1] - p3[1]) - (p2[1] - p1[1]) * (p4[0] - p3[0])
    if abs(d) < 1e-12: return None
    t = ((p3[0] - p1[0]) * (p4[1] - p3[1]) - (p3[1] - p1[1]) * (p4[0] - p3[0])) / d
    u = ((p3[0] - p1[0]) * (p2[1] - p1[1]) - (p3[1] - p1[1]) * (p2[0] - p1[0])) / d
    return (t, u) if 0 <= t < 1 and 0 <= u < 1 else None


def find_crossings(strands, cell=1.0):
    grid = {}
    segs = []
    for si, s in enumerate(strands):
        n = len(s.pts); m = n if s.closed else n - 1
        for i in range(m):
            a, b = s.pts[i], s.pts[(i + 1) % n]
            k = len(segs); segs.append((si, i, a, b))
            for gx in range(int(min(a[0], b[0]) // cell), int(max(a[0], b[0]) // cell) + 1):
                for gy in range(int(min(a[1], b[1]) // cell), int(max(a[1], b[1]) // cell) + 1):
                    grid.setdefault((gx, gy), []).append(k)
    seen = set(); out = []
    for lst in grid.values():
        for ii in range(len(lst)):
            for jj in range(ii + 1, len(lst)):
                k1, k2 = lst[ii], lst[jj]
                if (k1, k2) in seen: continue
                seen.add((k1, k2))
                s1, i1, a1, b1 = segs[k1]; s2, i2, a2, b2 = segs[k2]
                if s1 == s2:
                    n = len(strands[s1].pts)
                    if abs(i1 - i2) < 8 or (strands[s1].closed and n - abs(i1 - i2) < 8): continue
                r = seg_x(a1, b1, a2, b2)
                if r:
                    out.append([s1, i1 + r[0], s2, i2 + r[1], None])
    uniq = []
    for c in out:
        if any(c[0] == u[0] and c[2] == u[2] and abs(c[1] - u[1]) < 3 and abs(c[3] - u[3]) < 3 for u in uniq): continue
        uniq.append(c)
    return uniq


def assign(strands, xs, order=None):
    """Über/unter abwechselnd entlang jedes Strangs (gierig, bei Konflikt wird neu angesetzt). c[4]: 0 = erster Strang oben."""
    order = order or range(len(strands))
    for si in order:
        ev = []
        for k, c in enumerate(xs):
            if c[0] == si: ev.append((c[1], k, 0))
            if c[2] == si: ev.append((c[3], k, 1))
        ev.sort()
        state = None
        for pos, k, side in ev:
            c = xs[k]
            if c[4] is not None:
                state = (c[4] == side)
            else:
                state = True if state is None else not state
                c[4] = side if state else 1 - side
    return xs


def render(strands, xs):
    o = [draw_strand(s) for s in strands]
    for c in xs:
        top, pos, bot, bpos = (c[0], c[1], c[2], c[3]) if c[4] == 0 else (c[2], c[3], c[0], c[1])
        s, u = strands[top], strands[bot]
        t1 = tangent(s.pts, int(pos) % len(s.pts), s.closed); t2 = tangent(u.pts, int(bpos) % len(u.pts), u.closed)
        sin = max(abs(t1[0] * t2[1] - t1[1] * t2[0]), 0.25); cos = abs(t1[0] * t2[0] + t1[1] * t2[1])
        wu = u.ws[int(bpos) % len(u.pts)]; wo = s.ws[int(pos) % len(s.pts)]
        g = GAP if s.style == "tree" else OUT
        half = ((wu / 2 + g + 0.15) + (wo / 2 + g) * cos) / sin
        k = int(round(half / 0.12)) + 2
        o.append(draw_piece(s, int(pos) - k, int(pos) + k))
    return "".join(o)


def draw_strand(s):
    if s.style == "tree":
        o = f'<path d="{poly(s.pts, s.ws, 0, True, s.closed)}" fill="{COL["brown"]}" fill-rule="evenodd"></path>'
        if s.hl: o += hl_line(s, 0, len(s.pts) - 1)
        return o
    o = f'<path d="{poly(s.pts, s.ws, 2 * OUT, True, s.closed)}" fill="{COL["brown"]}" fill-rule="evenodd"></path>'
    return o + f'<path d="{poly(s.pts, s.ws, 0, True, s.closed)}" fill="{COL["gold"]}" fill-rule="evenodd"></path>'


def hl_line(s, i0, i1):
    n = len(s.pts)
    idx = [k % n for k in range(i0, i1 + 1)] if s.closed else list(range(max(i0, 0), min(i1, n - 1) + 1))
    idx = [k for k in idx if s.ws[k] >= 1.55]
    if len(idx) < 3: return ""
    runs, cur = [], [idx[0]]
    for a, b in zip(idx, idx[1:]):
        if (b - a) % n == 1: cur.append(b)
        else: runs.append(cur); cur = [b]
    runs.append(cur)
    return "".join(f'<path d="{line([s.pts[k] for k in r])}" fill="none" stroke="{COL["copper"]}" stroke-width=".42"></path>' for r in runs if len(r) >= 3)


def draw_piece(s, i0, i1):
    if s.style == "tree":
        o = f'<path d="{poly(s.pts, s.ws, 2 * GAP, False, s.closed, i0, i1)}" fill="{COL["linen"]}"></path>'
        o += f'<path d="{poly(s.pts, s.ws, 0, False, s.closed, i0, i1)}" fill="{COL["brown"]}"></path>'
        if s.hl: o += hl_line(s, i0, i1)
        return o
    o = f'<path d="{poly(s.pts, s.ws, 2 * OUT, False, s.closed, i0, i1)}" fill="{COL["brown"]}"></path>'
    return o + f'<path d="{poly(s.pts, s.ws, 0, False, s.closed, i0, i1)}" fill="{COL["gold"]}"></path>'


# ---------------- Flechtknoten (klassisches Zopfmuster, abgerundete Kanten) ----------------
def plait(x0, y0, w, h, nx=6, ny=4, pull=0.42):
    """Zopf auf einem nx × ny Raster (gerade Zahlen): Wege als Billard, an den Kanten umgelenkt."""
    sx, sy = w / nx, h / ny
    visited = set(); loops = []
    for start in [(i, 0) for i in range(1, nx, 2)]:
        for d0 in [(1, 1), (-1, 1)]:
            if (start, d0) in visited: continue
            p, d = start, d0
            path = []
            while True:
                visited.add((p, d))
                path.append(p)
                q = (p[0] + d[0], p[1] + d[1])
                nd = list(d)
                if q[0] <= 0 or q[0] >= nx: nd[0] = -nd[0]
                if q[1] <= 0 or q[1] >= ny: nd[1] = -nd[1]
                p, d = q, tuple(nd)
                if (p, d) == (start, d0) or len(path) > 4 * nx * ny + 8: break
            loops.append(path)
            for a, b in zip(path, path[1:] + path[:1]):
                visited.add((b, (a[0] - b[0], a[1] - b[1])))
    out = []
    for path in loops:
        pts = []
        for gx, gy in path:
            ix = (pull if gx == 0 else -pull if gx == nx else 0) * sx
            iy = (pull if gy == 0 else -pull if gy == ny else 0) * sy
            pts.append((x0 + gx * sx + ix, y0 + gy * sy + iy))
        out.append(pts)
    return out


def smooth_closed(pts, n=10):
    P = pts[-2:] + pts + pts[:3]
    c = catmull(P, n)
    return c[2 * n: 2 * n + len(pts) * n]


def knot_strands(x0, y0, w, h, nx, ny, ws):
    return [Strand(smooth_closed(p), ws, style="gold", closed=True) for p in plait(x0, y0, w, h, nx, ny)]


# ---------------- Ring, Rand, Ecken, Rauten ----------------
GAPS_DEG = (-90, 0, 90, 180)


def ring_svg():
    o = []
    r1, r2 = RING_R - RING_W / 2, RING_R + RING_W / 2
    skip = math.radians(4.2)
    n = int(2 * math.pi * RING_R / 0.95)
    for i in range(n):
        t = 2 * math.pi * i / n
        if any(abs((t - math.radians(g) + math.pi) % (2 * math.pi) - math.pi) < skip for g in GAPS_DEG): continue
        a1, a2 = t, t + 0.045
        o.append(f'M{F(CX + r1 * math.cos(a1))} {F(CY + r1 * math.sin(a1))}L{F(CX + r2 * math.cos(a2))} {F(CY + r2 * math.sin(a2))}')
    rope = f'<path d="{"".join(o)}" stroke="{COL["gold"]}" stroke-width=".55" stroke-linecap="round" fill="none"></path>'
    arcs = []
    for r in (r1 + .12, r2 - .12):
        for k, g in enumerate(GAPS_DEG):
            a = math.radians(g) + skip; b = math.radians(GAPS_DEG[(k + 1) % 4] + (360 if k == 3 else 0)) - skip
            arcs.append(f'M{F(CX + r * math.cos(a))} {F(CY + r * math.sin(a))}A{F(r)} {F(r)} 0 0 1 {F(CX + r * math.cos(b))} {F(CY + r * math.sin(b))}')
    return rope + f'<path d="{"".join(arcs)}" stroke="{COL["gold"]}" stroke-width=".28" fill="none"></path>'


def border_svg(inset=2.0, a=19.0):
    """Steppstich am Rand: entlang der Seiten und der geraden Ober-/Unterkanten; an den Bögen übernimmt der Ring."""
    x0, x1 = inset, W - inset
    yT, yB = 5.5 + inset, H - 5.5 - inset
    xl, xr = CX - a, CX + a
    d = f"M{F(xl)} {F(yT)}H{F(x0)}V{F(yB)}H{F(xl)}M{F(xr)} {F(yT)}H{F(x1)}V{F(yB)}H{F(xr)}"
    return f'<path d="{d}" fill="none" stroke="{COL["copper"]}" stroke-width=".45" stroke-dasharray="1.4 .8" stroke-linecap="round" stroke-linejoin="round"></path>'


def corner_pts():
    outer = catmull([(4.9, 25.5), (4.6, 18), (4.9, 12.2), (7.0, 9.9), (12.0, 9.6), (16.4, 9.8)], 10)
    outer = curl(outer, 1.1, 0.95, 1)
    outer = curl(outer[::-1], 1.1, 0.95, -1)[::-1]
    inner = catmull([(8.6, 19.5), (8.4, 15.4), (9.6, 13.4), (11.6, 13.2), (13.4, 13.4)], 10)
    inner = curl(inner, .85, .9, 1)
    inner = curl(inner[::-1], .85, .9, -1)[::-1]
    return [outer, inner]


def corner_svg():
    o = []
    for P in corner_pts():
        for Q in (P, mirror(P), [(x, H - y) for x, y in P], [(2 * CX - x, H - y) for x, y in P]):
            o.append(f'<path d="{line(Q)}" fill="none" stroke="{COL["gold"]}" stroke-width=".95" stroke-linecap="round" stroke-linejoin="round"></path>')
    return "".join(o)


def rhombus(x, y, s=3.3):
    h = s / 2
    return (f'<path d="M{F(x)} {F(y - h)} L{F(x + h)} {F(y)} L{F(x)} {F(y + h)} L{F(x - h)} {F(y)} Z" fill="none" stroke="{COL["red"]}" stroke-width=".75" stroke-linejoin="miter"></path>'
            f'<circle cx="{F(x)}" cy="{F(y)}" r=".5" fill="{COL["red"]}"></circle>')


def rhombi_svg():
    return "".join(rhombus(CX + RING_R * math.cos(math.radians(g)), CY + RING_R * math.sin(math.radians(g))) for g in GAPS_DEG)


# ---------------- NL als Pfade ----------------
def nl_svg(width=22.0, bottom=63.0, cx=CX):
    """„NL“ aus Cinzel Decorative Bold als Pfade, mit Schwüngen 22 mm breit."""
    f = TTFont(FONT)
    gs = f.getGlyphSet(); cmap = f.getBestCmap()
    track = -70
    xmin, xmax, ymin, ymax = -213, 865 + track + 1029, -241, 838        # Grenzen der beiden Zeichen (BoundsPen)
    s = width / (xmax - xmin)
    x = cx - (xmin + xmax) / 2 * s
    base = bottom + ymin * s
    o = []
    for ch in "NL":
        nm = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[nm].draw(TransformPen(pen, (s, 0, 0, -s, x, base)))
        o.append(f'<path d="{pen.getCommands()}" fill="{COL["gold"]}" stroke="{COL["brown"]}" stroke-width=".38" stroke-linejoin="round" paint-order="stroke"></path>')
        x += (gs[nm].width + track) * s
    return "".join(o)


# ---------------- Baum ----------------
def arc(r, a0, a1, n=40):
    return [(CX + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), CY + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def spiral(pts, L=6.5, k1=1.45, side=-1, k0=0.12, step=0.08):
    """Einrollung als Klothoide: Krümmung steigt gleichmäßig von k0 auf k1 (1/mm). side -1 = gegen den Uhrzeigersinn."""
    (x0, y0), (x, y) = pts[-2], pts[-1]
    th = math.atan2(y - y0, x - x0)
    out = list(pts); n = int(L / step)
    for i in range(n):
        k = (k0 + (k1 - k0) * (i + .5) / n) * side
        th += k * step
        x += step * math.cos(th); y += step * math.sin(th)
        out.append((x, y))
    return out


def trunk_strands(y_top=27.5, y_bot=47.5, twists=1.5):
    """Gedrehter Stamm aus 3 Strängen; halbe Drehungen, damit oben und unten ein Strang mittig steht (symmetrisch)."""
    out = []
    for k in range(3):
        ph = 2 * math.pi * k / 3
        pts = []
        for i in range(121):
            t = i / 120
            y = y_bot + (y_top - y_bot) * t
            a = 2.9 + 2.3 * (abs(t - 0.5) * 2) ** 2.2
            pts.append((CX + a * math.sin(2 * math.pi * twists * t + ph), y))
        out.append(pts)
    return out


def hermite(p0, h0, p1, h1, k0=0.42, k1=0.42, n=60):
    d = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
    a0, a1 = math.radians(h0), math.radians(h1)
    c1 = (p0[0] + k0 * d * math.cos(a0), p0[1] + k0 * d * math.sin(a0))
    c2 = (p1[0] - k1 * d * math.cos(a1), p1[1] - k1 * d * math.sin(a1))
    out = []
    for i in range(n + 1):
        t = i / n; a = (1 - t) ** 3; b = 3 * (1 - t) ** 2 * t; c = 3 * (1 - t) * t * t; e = t ** 3
        out.append((a * p0[0] + b * c1[0] + c * c2[0] + e * p1[0], a * p0[1] + b * c1[1] + c * c2[1] + e * p1[1]))
    return out


def rim(theta, r=27.0):
    return (CX + r * math.cos(math.radians(theta)), CY + r * math.sin(math.radians(theta)))


def at(pts, f):
    """Punkt und Richtung (Grad) bei Anteil f der Länge."""
    d = [0.0]
    for a, b in zip(pts, pts[1:]): d.append(d[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    s = d[-1] * f
    i = next(k for k in range(1, len(d)) if d[k] >= s)
    a, b = pts[i - 1], pts[i]
    return a, math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))


R_END = 27.0


def branch(p0, h0, theta, sense=1, k0=.42, k1=.42, rim_deg=0.0, L=4.6, kc=1.05):
    """Ast vom Stamm zum Rand: kommt bei theta an, läuft tangential (sense +1 im Uhrzeigersinn) und rollt nach innen ein."""
    h1 = theta + 90 * sense
    p = hermite(p0, h0, rim(theta, R_END), h1, k0, k1)
    if rim_deg:
        p = p + arc(R_END, theta, theta + sense * rim_deg, 12)[1:]
    return spiral(p, L, kc, sense, k0=1 / R_END)


# Linke Hälfte; jede Zeile: Punkte, Breite am Anfang, Breite am Ende, Elternast (Index) oder None
def canopy_left():
    B = []
    b1 = branch((41.8, 31.2), -118, -104, 1, .55, .5, rim_deg=18, L=4.0)     # Scheitelbogen: kreuzt das Spiegelbild hinter dem Stamm und oben
    b2 = branch((38.8, 30.2), -124, -125, 1, .45, .45)
    b3 = branch((38.0, 30.4), -143, -145, 1, .45, .45)
    b4 = branch((37.4, 29.0), -170, -164, 1, .4, .5, L=4.0)
    B += [(b1, 1.9, 1.0, None), (b2, 1.95, 1.0, None), (b3, 1.9, 1.0, None), (b4, 1.8, 1.0, None)]
    for par, f, th, dh in ((2, .40, -114, 32), (3, .40, -135, 30), (3, .76, -155, 26)):
        p, h = at(B[par][0], f)
        B.append((branch(p, h + dh, th, 1, .45, .45, L=3.8, kc=1.15), 1.35, .95, par))
    # Mittelstrang: zweimal mit dem Spiegelbild verdreht, oben kleine Einrollung nach außen
    sp = catmull([(40.7, 29.4), (40.6, 26.4), (40.0, 23.6), (38.9, 20.8), (40.0, 18.0), (41.0, 16.0), (41.3, 14.6)], 10)
    B.append((spiral(sp, 3.6, 1.3, 1, k0=.1), 1.6, .95, None))
    # kurze Zweige im Scheitelbogen (links vom Mittelstrang)
    p, h = at(b1, .42)
    B.append((spiral(hermite(p, h + 38, (37.4, 17.2), -70, .4, .4), 3.4, 1.35, 1, k0=.1), 1.3, .95, 0))
    p, h = at(b2, .52)
    B.append((spiral(hermite(p, h + 40, (31.0, 15.4), -40, .4, .4), 3.4, 1.35, 1, k0=.1), 1.25, .95, 1))
    return B


def roots_left():
    B = []
    r1 = branch((37.4, 46.0), 174, 152, -1, .42, .5, L=4.6)
    r2 = branch((38.0, 46.8), 152, 138, -1, .45, .45, L=4.4)
    r3 = branch((38.6, 47.4), 128, 124, -1, .45, .45, L=3.6, kc=1.2)
    B += [(r1, 2.0, 1.0, None), (r2, 1.9, 1.0, None), (r3, 1.7, 1.0, None)]
    for par, f, th, dh in ((0, .5, 130, -30), (1, .55, 115, -26)):
        p, h = at(B[par][0], f)
        B.append((branch(p, h + dh, th, -1, .45, .45, L=3.6, kc=1.2), 1.4, .95, par))
    return B


def tree():
    S = []
    for group in (canopy_left(), roots_left()):
        base = len(S)
        for pts, w0, w1, par in group:
            for m in (False, True):
                s = Strand(mirror(pts) if m else pts, w0, w1, taper=0.35)
                s.parent = None if par is None else base + 2 * par + (1 if m else 0)
                S.append(s)
    return S


def drop_parent(S, xs, skip=2.6):
    k = int(skip / 0.12)
    out = []
    for c in xs:
        a, pa, b, pb = c[0], c[1], c[2], c[3]
        if getattr(S[a], 'parent', None) == b and pa < k: continue
        if getattr(S[b], 'parent', None) == a and pb < k: continue
        out.append(c)
    return out


def tree_svg():
    S = tree()
    xs = drop_parent(S, find_crossings(S))
    assign(S, xs)
    T = [Strand(p, 2.5, 2.5, taper=1) for p in trunk_strands()]
    tx = find_crossings(T)
    assign(T, tx)
    return render(S, xs) + render(T, tx)


KN = (8, 6, 1.2)


def knots_svg():
    o = []
    for x0 in (11.6, 80 - 11.6 - 22.6):
        S = knot_strands(x0, 30.2, 22.6, 14.2, KN[0], KN[1], KN[2])
        xs = find_crossings(S)
        assign(S, xs)
        o.append(render(S, xs))
    return "".join(o)


GROUPS = dict(border=border_svg, ring=lambda: ring_svg() + rhombi_svg(), corners=corner_svg, knots=knots_svg,
              tree=tree_svg, nl=nl_svg)


def svg(vb=f"0 0 {F(W)} {F(H)}", extra="", only=None, bg=True):
    outline = FN.patch_outline(0, 0, W, H, 5.5)
    back = f'<path d="{outline}" fill="{COL["linen"]}" stroke="#1b2230" stroke-width=".3"></path>' if bg else ""
    body = "".join(fn() for k, fn in GROUPS.items() if only is None or k in only)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{F(W)}mm" height="{F(H)}mm">'
            f'<defs><clipPath id="pd"><path d="{outline}"></path></clipPath></defs>{back}<g clip-path="url(#pd)">{body}</g>{extra}</svg>')


if __name__ == "__main__":
    s = svg()
    open(os.path.join(HERE, "v19", "patch_d_vector.svg"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n' + s)
    big = s.replace(f'width="{F(W)}mm" height="{F(H)}mm"', 'width="1600" height="1420"')
    open(os.path.join(HERE, "v19", "patch_d_vector.html"), "w").write(
        f'<!doctype html><meta charset="utf-8"><body style="margin:0;background:#fff"><div style="width:1600px">{big}</div></body>')
    print("ok", len(s) // 1024, "KB")
