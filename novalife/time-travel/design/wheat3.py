# -*- coding: utf-8 -*-
# B · Serp schneidet in die Garbe · realistisch (v1.5). Einheiten mm.
# B2 · Ähren über der roten Kreuzstich-Linie, lange Goldfäden.
import math, random
F = lambda v: f"{v:.2f}".rstrip('0').rstrip('.')

# Farben (Garn)
OUT = "#3a250f"      # Kontur Weizen, dunkelbraun
GD = "#d2a53a"; GDL = "#e9c868"; GDK = "#a8771f"; OC = "#b98a2e"; STRAW = "#f3e1a2"; HL = "#f7e7b0"
WHITE = "#f4f1ea"; WSH = "#c9c2b3"; BOUT = "#4a423c"; RED = "#b3322a"; REDD = "#87231d"; REDL = "#c4423a"
BR = "#6e4a2a"; BRD = "#45301c"; BRL = "#94673d"
TH = "#e3bf5a"; THD = "#9c7520"   # Goldfäden

def pl(pts): return "M" + " L".join(f"{F(x)} {F(y)}" for x, y in pts)
def bez(p0, p1, p2, p3, n=30):
    out = []
    for i in range(n + 1):
        t = i / n; m = 1 - t
        out.append((m**3*p0[0] + 3*m*m*t*p1[0] + 3*m*t*t*p2[0] + t**3*p3[0],
                    m**3*p0[1] + 3*m*m*t*p1[1] + 3*m*t*t*p2[1] + t**3*p3[1]))
    return out
def unit(a): return (math.cos(a), math.sin(a))
def add(p, v, s=1.0): return (p[0] + v[0]*s, p[1] + v[1]*s)
def path(d, fill="none", stroke="none", w=0, cap="round", extra=""):
    st = f"fill: {fill}; stroke: {stroke}"
    if stroke != "none": st += f"; stroke-width: {F(w)}px; stroke-linecap: {cap}; stroke-linejoin: round"
    return f'<path d="{d}" style="{st}{extra}"></path>'
def rope(pts, w, col, o=OUT, hl=HL, hlw=0.32, cap="round", hlop=0.6):
    d = pl(pts)
    return [path(d, stroke=o, w=w + 0.5, cap=cap), path(d, stroke=col, w=w, cap=cap),
            path(d, stroke=hl, w=w*hlw, cap=cap, extra=f"; opacity: {hlop}")]

# ---------------------------------------------------------------- Ähre
def spikelet(B, ang, L, Wd):
    d = unit(ang); n = (-d[1], d[0]); T = add(B, d, L)
    c1 = add(add(B, d, 0.28*L), n, 0.62*Wd); c2 = add(add(B, d, 0.80*L), n, 0.40*Wd)
    c3 = add(add(B, d, 0.80*L), n, -0.40*Wd); c4 = add(add(B, d, 0.28*L), n, -0.62*Wd)
    dd = (f"M{F(B[0])} {F(B[1])}C{F(c1[0])} {F(c1[1])} {F(c2[0])} {F(c2[1])} {F(T[0])} {F(T[1])}"
          f"C{F(c3[0])} {F(c3[1])} {F(c4[0])} {F(c4[1])} {F(B[0])} {F(B[1])}Z")
    hl = bez(add(add(B, d, 0.18*L), n, 0.22*Wd), add(add(B, d, 0.35*L), n, 0.40*Wd), add(add(B, d, 0.62*L), n, 0.32*Wd), add(add(B, d, 0.82*L), n, 0.12*Wd), 8)
    cr = [add(B, d, 0.30*L), add(B, d, 0.80*L)]
    return dd, T, hl, cr

def ear(base, ang, L, nodes=13, bend=0.0, fill=GD, seed=1, awn=1.0, wscale=1.0):
    """Weizenähre: Spindel mit wechselständigen Ährchen, oben kleiner, mit Grannen."""
    rnd = random.Random(seed)
    # Spindel als leicht gebogene Linie
    pts = []
    for i in range(21):
        t = i / 20; a = ang + bend * t
        if i == 0: p = base
        else: p = add(pts[-1], unit(a), L / 20)
        pts.append(p)
    def at(t):
        k = min(19, int(t * 20)); r = t * 20 - k
        p = (pts[k][0] + (pts[k+1][0] - pts[k][0]) * r, pts[k][1] + (pts[k+1][1] - pts[k][1]) * r)
        return p, ang + bend * t
    sk, aw = [], []
    for k in range(nodes):
        t = 0.04 + k * (0.80 / (nodes - 1))
        p, a = at(t); s = 1 if k % 2 == 0 else -1
        n = (-math.sin(a), math.cos(a))
        Ls = L * 0.30 * (1 - 0.30 * t) * (0.94 + 0.12 * rnd.random())
        Wd = Ls * 0.56 * wscale
        B = add(p, n, s * 0.30)
        sa = a + s * math.radians(26 + 6 * rnd.random())
        sk.append(spikelet(B, sa, Ls, Wd))
        if awn:
            T = add(B, unit(sa), Ls)
            la = L * (0.42 + 0.20 * rnd.random()) * awn * (1 - 0.25 * t)
            aa = a + s * math.radians(9 + 6 * rnd.random())
            aw.append([T, add(T, unit(aa), la)])
    # Endährchen
    p, a = at(0.86)
    sk.append(spikelet(p, a, L * 0.24, L * 0.13 * wscale))
    if awn:
        T = add(p, unit(a), L * 0.24); aw.append([T, add(T, unit(a), L * 0.45 * awn)])
    g = [path(pl(pts[:18]), stroke=OUT, w=0.9)]
    for dd, T, hl, cr in sk:
        g.append(path(dd, fill=fill, stroke=OUT, w=0.32))
        g.append(path(pl(hl), stroke=GDL, w=0.38, extra="; opacity: 0.85"))
        g.append(path(pl(cr), stroke=GDK, w=0.22, extra="; opacity: 0.8"))
    awns = "".join(f"M{F(a[0])} {F(a[1])}L{F(b[0])} {F(b[1])}" for a, b in aw)
    g.append(path(awns, stroke=GDK, w=0.34))
    tip = pts[-1]
    return g, tip

# ---------------------------------------------------------------- Garbe + Serp
def sheaf_scene(seed=7):
    rnd = random.Random(seed)
    g_back, g_ears, g_low, g_bind = [], [], [], []
    BX, BY = 29.5, 50.5
    NS = 11
    upper = []
    for i in range(NS):
        f = (i - (NS - 1) / 2) / ((NS - 1) / 2)
        th = math.radians(33 * f + rnd.uniform(-3, 3))
        S = (BX + 2.5 * f, BY - 1.6)
        Lst = 19.0 - 3.2 * abs(f) + rnd.uniform(-1.2, 1.2)
        E = (S[0] + Lst * math.sin(th), S[1] - Lst * math.cos(th))
        c1 = (S[0] + 0.1 * (E[0] - S[0]), S[1] - 0.42 * Lst)
        c2 = (E[0] - 0.30 * Lst * math.sin(th), E[1] + 0.30 * Lst * math.cos(th))
        pts = bez(S, c1, c2, E, 24)
        a_end = math.atan2(pts[-1][1] - pts[-3][1], pts[-1][0] - pts[-3][0])
        upper.append((abs(f), f, pts, a_end, i))
    # hinten (außen) zuerst, vorn (Mitte) zuletzt
    for af, f, pts, a_end, i in sorted(upper, key=lambda u: -u[0]):
        col = [GD, OC, GDL][i % 3] if af < 0.5 else [OC, GDK][i % 2]
        g_back += rope(pts, 1.0, col)
        Le = 13.2 - 1.6 * af + rnd.uniform(-0.8, 0.8)
        eg, _ = ear(pts[-1], a_end, Le, nodes=13, bend=0.10 * f, fill=GD if af < 0.6 else OC, seed=100 + i)
        g_back += eg
    # untere Halme
    lower = []
    for i in range(NS):
        f = (i - (NS - 1) / 2) / ((NS - 1) / 2)
        S = (BX + 2.8 * f, BY + 1.4)
        E = (BX + 12.5 * f + rnd.uniform(-0.6, 0.6), 79.0 - 1.6 * abs(f) + rnd.uniform(-0.7, 0.7))
        c1 = (S[0] + 0.12 * (E[0] - S[0]), S[1] + 9)
        c2 = (E[0] - 0.12 * (E[0] - S[0]), E[1] - 9)
        lower.append((f, bez(S, c1, c2, E, 30), i))
    return dict(BX=BX, BY=BY, upper=g_back, lower=lower, rnd=rnd)

def cut_face(p, a, rx=0.75, ry=0.42):
    ang = math.degrees(a) + 90
    return (f'<ellipse cx="{F(p[0])}" cy="{F(p[1])}" rx="{F(rx)}" ry="{F(ry)}" transform="rotate({F(ang)} {F(p[0])} {F(p[1])})" '
            f'style="fill: {STRAW}; stroke: {OUT}; stroke-width: 0.26px"></ellipse>')

def blade_curve(n=90):
    """Mittellinie der Außenkante: sanft von der Ferse nach oben, dann engerer Haken zur Spitze."""
    seg1 = bez((45.2, 74.6), (46.6, 62.2), (38.6, 53.7), (28.6, 53.5), 45)
    seg2 = bez((28.6, 53.5), (18.2, 53.3), (11.2, 60.0), (14.4, 69.8), 45)
    return seg1 + seg2[1:]

def inside(pt, poly):
    x, y = pt; c = False; n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1 + 1e-12) + x1: c = not c
    return c

def sickle(wmax=3.8, hdir=72, hlen=12.0, center=(30.0, 65.0)):
    outer = blade_curve()
    N = len(outer) - 1
    inner, tt = [], []
    for k, o in enumerate(outer):
        t = k / N
        a, b = outer[max(0, k - 1)], outer[min(N, k + 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy) or 1
        nrm = (-dy / L, dx / L)
        if (center[0] - o[0]) * nrm[0] + (center[1] - o[1]) * nrm[1] < 0: nrm = (-nrm[0], -nrm[1])
        w = wmax * (1 - t) ** 0.72 + 0.1
        inner.append((o[0] + nrm[0] * w, o[1] + nrm[1] * w)); tt.append((t, w, nrm))
    heel = outer[0]
    poly = outer + inner[::-1]
    parts = {}
    parts["blade"] = path(pl(poly) + "Z", fill=WHITE, stroke=BOUT, w=0.36)
    sh = [(o[0] + r[0] * min(0.75, w * 0.32), o[1] + r[1] * min(0.75, w * 0.32)) for o, (t, w, r) in zip(outer, tt)]
    parts["shade"] = path(pl(outer[:int(N*0.95)] + sh[:int(N*0.95)][::-1]) + "Z", fill=WSH)
    gl = [(o[0] + r[0] * w * 0.42, o[1] + r[1] * w * 0.42) for o, (t, w, r) in zip(outer[6:int(N*0.75)], tt[6:int(N*0.75)])]
    parts["gloss"] = path(pl(gl), stroke="#ffffff", w=0.36, extra="; opacity: 0.9")
    k0, k1 = int(N * 0.05), int(N * 0.97)
    ed_in = inner[k0:k1]
    ed_out = [(i_[0] - r[0] * min(1.0, w * 0.42), i_[1] - r[1] * min(1.0, w * 0.42)) for i_, (t, w, r) in zip(inner[k0:k1], tt[k0:k1])]
    parts["edge"] = path(pl(ed_in + ed_out[::-1]) + "Z", fill=RED)
    parts["edge2"] = path(pl(ed_in), stroke=REDD, w=0.3)
    hd = (math.cos(math.radians(hdir)), math.sin(math.radians(hdir))); hn = (-hd[1], hd[0])
    mid_heel = ((outer[0][0] + inner[0][0]) / 2, (outer[0][1] + inner[0][1]) / 2)
    f0, f1 = add(mid_heel, hd, 1.4), add(mid_heel, hd, 4.4)
    g = []
    tang = [outer[0], inner[0], add(f0, hn, -1.1), add(f0, hn, 1.1)]
    g.append(path(pl(tang) + "Z", fill=WSH, stroke=BOUT, w=0.32))
    def quad(a, b, wa, wb, fill, stroke=OUT, sw=0.38):
        p = [add(a, hn, wa / 2), add(b, hn, wb / 2), add(b, hn, -wb / 2), add(a, hn, -wa / 2)]
        return path(pl(p) + "Z", fill=fill, stroke=stroke, w=sw)
    g.append(quad(f0, f1, 3.2, 3.6, BRD))
    g.append(path(pl([add(add(f0, hd, 1.0), hn, 1.7), add(add(f0, hd, 1.0), hn, -1.7)]) + pl([add(add(f0, hd, 2.0), hn, 1.75), add(add(f0, hd, 2.0), hn, -1.75)]), stroke=WSH, w=0.32))
    h0, h1 = f1, add(f1, hd, hlen)
    hm = add(h0, hd, hlen * 0.5)
    hp = [add(h0, hn, 1.8), add(hm, hn, 2.3), add(h1, hn, 1.9), add(add(h1, hd, 1.3), hn, 0.8), add(add(h1, hd, 1.3), hn, -0.8), add(h1, hn, -1.9), add(hm, hn, -2.3), add(h0, hn, -1.8)]
    g.append(path(pl(hp) + "Z", fill=BR, stroke=OUT, w=0.38))
    for off, col, w in [(1.0, BRL, 0.5), (-0.35, BRD, 0.28), (-1.2, BRD, 0.26), (0.35, BRD, 0.2)]:
        g.append(path(pl([add(add(h0, hd, 0.8), hn, off), add(hm, hn, off * 1.15), add(add(h1, hd, 0.2), hn, off * 0.9)]), stroke=col, w=w))
    parts["handle"] = "".join(g)
    return parts, dict(outer=outer, inner=inner, poly=poly, heel=heel, tt=tt)

def b_scene(seed=7, ncut=0):
    S = sheaf_scene(seed)
    BX, BY = S["BX"], S["BY"]
    g = []
    g += S["upper"]
    sk, geo = sickle()
    # 1 · Klinge hinter den unteren Halmen
    g += [sk["blade"], sk["shade"], sk["gloss"], sk["edge"], sk["edge2"]]
    lower = S["lower"]
    order = sorted(lower, key=lambda u: -abs(u[0]))
    cutset = sorted([u for u in lower if u[0] > 0], key=lambda u: -u[0])[:ncut]
    cutids = {u[2] for u in cutset}
    faces = []
    rnd = random.Random(seed + 9)
    edge_poly = None
    for f, pts, i in order:
        col = [GD, OC, GDL, OC][i % 4]
        if f >= 0.75:
            hit = [j for j, p in enumerate(pts) if inside(p, geo["poly"])]
            if len(hit) >= 2:
                # Schnitt an der roten Innenkante: Lücke von ~1,4 mm, unteres Stück leicht versetzt
                jm = hit[len(hit) // 2]
                j0, j1 = max(1, jm - 1), min(len(pts) - 3, jm + 2)
                top = pts[:j0 + 1]
                g += rope(top, 1.0, col)
                a_t = math.atan2(top[-1][1] - top[-2][1], top[-1][0] - top[-2][0])
                faces.append(cut_face(top[-1], a_t, 0.6, 0.34))
                piv = pts[j1]; rot = math.radians(5)
                low = []
                for p in pts[j1:]:
                    dx, dy = p[0] - piv[0], p[1] - piv[1]
                    low.append((piv[0] + 0.45 + dx * math.cos(rot) - dy * math.sin(rot), piv[1] + 0.35 + dx * math.sin(rot) + dy * math.cos(rot)))
                g += rope(low, 1.0, col)
                a0 = math.atan2(low[1][1] - low[0][1], low[1][0] - low[0][0])
                faces.append(cut_face(low[0], a0 + math.pi, 0.6, 0.34))
                e, e2 = low[-1], low[-3]
                faces.append(cut_face(e, math.atan2(e[1] - e2[1], e[0] - e2[0])))
                continue
        g += rope(pts, 1.0, col)
        t = rnd.uniform(0.55, 0.8); j = int(t * 30)
        p, q = pts[j], pts[j + 1]
        a = math.atan2(q[1] - p[1], q[0] - p[0]); n = (-math.sin(a), math.cos(a))
        g.append(path(pl([add(p, n, 0.55), add(p, n, -0.55)]), stroke=GDK, w=0.36))
        e, e2 = pts[-1], pts[-3]
        faces.append(cut_face(e, math.atan2(e[1] - e2[1], e[0] - e2[0])))
    g += faces
    # 2 · Garbenband
    band = bez((BX - 5.6, BY - 0.6), (BX - 2.5, BY + 1.6), (BX + 2.5, BY + 1.6), (BX + 5.6, BY - 0.6), 30)
    g += rope(band, 3.2, OC, hlw=0.18)
    tw = ""; tw2 = ""
    for j in range(2, 29, 2):
        p = band[j]; q = band[j + 1]; a = math.atan2(q[1] - p[1], q[0] - p[0]); d = unit(a + math.radians(62))
        tw += f"M{F(p[0] - d[0]*1.45)} {F(p[1] - d[1]*1.45)}L{F(p[0] + d[0]*1.45)} {F(p[1] + d[1]*1.45)}"
        p = band[j + 1]
        tw2 += f"M{F(p[0] - d[0]*1.2)} {F(p[1] - d[1]*1.2)}L{F(p[0] + d[0]*1.2)} {F(p[1] + d[1]*1.2)}"
    g.append(path(tw, stroke=GDK, w=0.42)); g.append(path(tw2, stroke=HL, w=0.38, extra="; opacity: 0.8"))
    k1 = bez((BX + 5.2, BY - 0.2), (BX + 7.4, BY + 0.2), (BX + 8.3, BY + 2.2), (BX + 7.6, BY + 4.2), 14)
    k2 = bez((BX + 5.4, BY + 0.4), (BX + 7.8, BY - 0.6), (BX + 9.4, BY - 0.3), (BX + 10.4, BY + 1.0), 14)
    g += rope(k2, 1.0, GD); g += rope(k1, 1.1, OC)
    g.append(cut_face(k1[-1], math.atan2(k1[-1][1] - k1[-3][1], k1[-1][0] - k1[-3][0]), 0.6, 0.34))
    g.append(cut_face(k2[-1], math.atan2(k2[-1][1] - k2[-3][1], k2[-1][0] - k2[-3][0]), 0.55, 0.32))
    # 3 · Griff vorn
    g.append(sk["handle"])
    return "\n".join(g)

# ---------------------------------------------------------------- B2: Ähren, rote Linie, Goldfäden
def xline(cx, y0, ncols=37, sag=2.6, cell=4/3):
    """rote Kreuzstich-Linie, 3 Reihen rot mit weißen Atemzellen, weiße Steppkante oben und unten"""
    w = ncols * cell
    def ypos(x):
        t = (x - (cx - w / 2)) / w
        return y0 + sag * 4 * t * (1 - t)
    fills = {"w": [], "r": []}; xs = {"w": [], "r": []}
    top, bot = [], []
    for c in range(ncols):
        x = cx - w / 2 + c * cell
        for r in range(3):
            k = "w" if (r == 1 and c % 4 == 1) else "r"
            yy = ypos(x + cell / 2) - 1.5 * cell + r * cell
            fills[k].append(f"M{F(x)} {F(yy)}h{F(cell)}v{F(cell)}h{F(-cell)}z")
            i = cell * 0.12
            xs[k].append(f"M{F(x+i)} {F(yy+i)}l{F(cell-2*i)} {F(cell-2*i)}M{F(x+cell-i)} {F(yy+i)}l{F(-(cell-2*i))} {F(cell-2*i)}")
        top.append((x + cell / 2, ypos(x + cell / 2) - 1.5 * cell - 0.35)); bot.append((x + cell / 2, ypos(x + cell / 2) + 1.5 * cell + 0.35))
    g = [path("".join(fills["r"]), fill=REDD), path("".join(fills["w"]), fill="#dcd6c9"),
         path("".join(xs["r"]), stroke=REDL, w=cell * 0.3), path("".join(xs["w"]), stroke=WHITE, w=cell * 0.34),
         path(pl(top), stroke=WHITE, w=0.42, extra="; stroke-dasharray: 0.9 0.45"), path(pl(bot), stroke=WHITE, w=0.42, extra="; stroke-dasharray: 0.9 0.45")]
    return g, ypos

def b2_scene(threads=True, seed=3, lens=None):
    rnd = random.Random(seed)
    g = []
    CXL, Y0 = 25.0, 22.0
    line, ypos = xline(CXL, Y0)
    # zwei Ähren, gekreuzte Halme, aus der Linienmitte
    for s, i in [(-1, 0), (1, 1)]:
        S = (CXL - s * 0.8, ypos(CXL) - 2.2)
        th = math.radians(36 * s)
        E = (S[0] + 9.5 * math.sin(th), S[1] - 9.5 * math.cos(th))
        pts = bez(S, (S[0] + 0.2 * s, S[1] - 3), (E[0] - 2.2 * math.sin(th), E[1] + 2.2 * math.cos(th)), E, 16)
        g += rope(pts, 0.95, [OC, GD][i])
        a_end = math.atan2(pts[-1][1] - pts[-3][1], pts[-1][0] - pts[-3][0])
        eg, _ = ear(pts[-1], a_end, 12.5, nodes=12, bend=0.10 * s, fill=GD, seed=50 + i)
        g += eg
    th_g = []
    if threads:
        xs = [17.5, 19.6, 21.6, 23.6, 25.5, 27.4, 29.3, 31.2, 33.0]
        L = lens or [19, 25, 22, 30, 27, 21, 29, 18, 24]
        for x, l in zip(xs, L):
            y = ypos(x) + 1.6
            sway = rnd.uniform(0.8, 1.6) * (1 if rnd.random() < 0.5 else -1)
            pts = bez((x, y), (x + sway, y + l * 0.33), (x - sway, y + l * 0.68), (x + sway * 0.6, y + l), 24)
            th_g += rope(pts, 0.62, TH, o=THD, hl="#fbe9a8", hlw=0.35, hlop=0.75)
    return "\n".join(th_g + line + g)

B_SVG = b_scene()
B2_SVG = b2_scene(True)
if __name__ == "__main__":
    import os
    os.makedirs("v15", exist_ok=True)
    open("v15/b.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="620" height="920" viewBox="0 0 62 92"><rect width="62" height="92" style="fill: #2f4a6e"></rect>{B_SVG}</svg>')
    open("v15/b2.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="500" height="600" viewBox="0 0 50 60"><rect width="50" height="60" style="fill: #2f4a6e"></rect>{B2_SVG}</svg>')
    print(len(B_SVG), len(B2_SVG))
