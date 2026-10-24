# -*- coding: utf-8 -*-
# Zipper NVL-TT-02 · Mini-Wandteppich vorn (Designvorschlag v0.1, 24.10.2026)
# Persischer Wandteppich wie bei Oma, als ganzer Teppich in klein (Briefing 23.10.):
#   ovales Medaillon dunkelblau, rotes Feld mit kleinen Blüten und Ranken, Viertelmedaillons in den Ecken,
#   eine breite Bordüre mit Blütenranke und zwei schmale, keine Novalife-Zeichen.
#   Bedruckter Baumwollsamt, Kante oben und unten dunkelrot umstickt, cremefarbene Fransen links und rechts.
# Einheiten: mm. Nullpunkt oben links am Samt.
# v0.2 (24.10.): Ernest wählt A und will den Teppich etwas höher und minimal breiter: 250 × 175 statt 240 × 150.
# Medaillon und Viertelmedaillons wachsen mit MED_K, das Feldmuster behält seine Dichte. Endgröße: Papiertest.
import math

F = lambda v: f"{v:.2f}".rstrip('0').rstrip('.')
W, H = 250.0, 175.0
CX, CY = W / 2, H / 2
MED_K = 1.12

PAL = {
    'oma':   dict(field='#8c1d22', abrash='#7f171c', red2='#bd3a32', navy='#1c2748', navy2='#45639a', cream='#e9dab9',
                  gold='#c9973c', green='#4f6d4b', dark='#2a1712', pink='#dc8f80', edge='#6a1418', fringe='#ece1c8'),
    'blass': dict(field='#a9605a', abrash='#b46c64', red2='#c98a7d', navy='#4d5b78', navy2='#8a9bb8', cream='#efe4cf',
                  gold='#c9ac78', green='#8b9b7f', dark='#5b4a43', pink='#e3b8aa', edge='#8d4b46', fringe='#efe6d3'),
}
NAMES = {'oma': 'Wie bei Oma', 'blass': 'Ausgeblichen'}

# Aufbau von außen nach innen (mm)
KILIM = 3.0                      # gewebter Abschluss links und rechts, aus ihm kommen die Fransen
FRAME = 3.0                      # Rand oben und unten unter der gestickten Kante
G_OUT, LINE, MAIN, G_IN = 4.0, 0.6, 15.0, 4.0
INSET = FRAME + G_OUT + LINE + MAIN + LINE + G_IN          # 27,2
FX0, FY0, FX1, FY1 = INSET, INSET, W - INSET, H - INSET     # Feld


def set_size(w, h, k=None):
    """Teppichmaß umstellen, z. B. für den Vergleich mit dem alten Maß 240 × 150 (k = 1.0)"""
    global W, H, CX, CY, FX1, FY1, MED_K
    W, H = float(w), float(h)
    CX, CY = W / 2, H / 2
    FX1, FY1 = W - INSET, H - INSET
    if k is not None:
        MED_K = k


def P(pts):
    return "M" + "L".join(f"{F(x)} {F(y)}" for x, y in pts) + "Z"


def ellipse_pts(cx, cy, rx, ry, n, a0=0.0):
    return [(cx + rx * math.cos(a0 + 2 * math.pi * k / n), cy + ry * math.sin(a0 + 2 * math.pi * k / n)) for k in range(n)]


def scallop(cx, cy, rx, ry, n, bulge=0.12):
    """Ellipse mit Bogenrand: n Bögen nach außen"""
    pts = ellipse_pts(cx, cy, rx, ry, n)
    d = f"M{F(pts[0][0])} {F(pts[0][1])}"
    for k in range(n):
        a = 2 * math.pi * (k + 0.5) / n
        qx, qy = cx + rx * (1 + bulge) * math.cos(a), cy + ry * (1 + bulge) * math.sin(a)
        x2, y2 = pts[(k + 1) % n]
        d += f"Q{F(qx)} {F(qy)} {F(x2)} {F(y2)}"
    return d + "Z"


def rosette(cx, cy, r, n, petal, center, outline, rot=0.0, inner=None):
    out = []
    for k in range(n):
        a = rot + 2 * math.pi * k / n
        px, py = cx + r * 0.58 * math.cos(a), cy + r * 0.58 * math.sin(a)
        out.append(f'<ellipse cx="{F(px)}" cy="{F(py)}" rx="{F(r*0.42)}" ry="{F(r*0.25)}" transform="rotate({F(math.degrees(a))} {F(px)} {F(py)})" '
                   f'style="fill:{petal};stroke:{outline};stroke-width:{F(max(0.12, r*0.05))}"/>')
    out.append(f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r*0.34)}" style="fill:{center};stroke:{outline};stroke-width:{F(max(0.12, r*0.05))}"/>')
    if inner:
        out.append(f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r*0.14)}" style="fill:{inner}"/>')
    return "".join(out)


def flower4(cx, cy, r, col, center):
    out = [f'<circle cx="{F(cx + r*0.55*math.cos(a))}" cy="{F(cy + r*0.55*math.sin(a))}" r="{F(r*0.45)}" style="fill:{col}"/>'
           for a in (0, math.pi / 2, math.pi, 3 * math.pi / 2)]
    out.append(f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r*0.32)}" style="fill:{center}"/>')
    return "".join(out)


def leaf(x, y, L, ang, w, col, vein=None):
    ux, uy = math.cos(ang), math.sin(ang); nx, ny = -uy, ux
    tx, ty = x + ux * L, y + uy * L
    c1 = (x + ux * L * 0.5 + nx * w, y + uy * L * 0.5 + ny * w)
    c2 = (x + ux * L * 0.5 - nx * w, y + uy * L * 0.5 - ny * w)
    s = (f'<path d="M{F(x)} {F(y)}Q{F(c1[0])} {F(c1[1])} {F(tx)} {F(ty)}Q{F(c2[0])} {F(c2[1])} {F(x)} {F(y)}Z" style="fill:{col}"/>')
    if vein:
        s += f'<path d="M{F(x)} {F(y)}L{F(x+ux*L*0.85)} {F(y+uy*L*0.85)}" style="stroke:{vein};stroke-width:{F(w*0.18)};fill:none"/>'
    return s


def palmette(cx, cy, s, ang, c_out, c_in, c_line):
    """Fächerblüte: Kelch unten, fünf Lappen oben, zeigt in Richtung ang"""
    out = []
    ux, uy = math.cos(ang), math.sin(ang); nx, ny = -uy, ux
    for k, t in enumerate((-0.9, -0.45, 0, 0.45, 0.9)):
        a = ang + t * 0.9
        lx, ly = cx + math.cos(a) * s * 0.55, cy + math.sin(a) * s * 0.55
        rr = s * (0.30 if k in (0, 4) else 0.34)
        out.append(f'<ellipse cx="{F(lx)}" cy="{F(ly)}" rx="{F(rr)}" ry="{F(rr*0.72)}" transform="rotate({F(math.degrees(a))} {F(lx)} {F(ly)})" '
                   f'style="fill:{c_out};stroke:{c_line};stroke-width:{F(s*0.04)}"/>')
    out.append(f'<ellipse cx="{F(cx + ux*s*0.18)}" cy="{F(cy + uy*s*0.18)}" rx="{F(s*0.42)}" ry="{F(s*0.3)}" transform="rotate({F(math.degrees(ang))} {F(cx + ux*s*0.18)} {F(cy + uy*s*0.18)})" '
               f'style="fill:{c_in};stroke:{c_line};stroke-width:{F(s*0.04)}"/>')
    out.append(f'<path d="M{F(cx - nx*s*0.3)} {F(cy - ny*s*0.3)}Q{F(cx - ux*s*0.35)} {F(cy - uy*s*0.35)} {F(cx + nx*s*0.3)} {F(cy + ny*s*0.3)}Z" style="fill:{c_out};stroke:{c_line};stroke-width:{F(s*0.04)}"/>')
    return "".join(out)


# ---------------------------------------------------------------- Feld
def field_pattern(c):
    """Herati-artiges Rapportmuster: Rosette mit vier Blättern, Ranken zum Nachbarn, Blüten dazwischen.
    Symmetrisch um die Mitte, damit beide Hälften am Reißverschluss gleich sind."""
    dx, dy = 15.0, 10.0
    out = []
    centers = []
    for j in range(-6, 7):
        for i in range(-9, 10):
            x = CX + i * dx + (dx / 2 if j % 2 else 0); y = CY + j * dy
            if FX0 - 6 < x < FX1 + 6 and FY0 - 6 < y < FY1 + 6:
                centers.append((x, y))
    # Ranken: jede Rosette zu den Nachbarn schräg darunter, leicht gebogen
    vines = []
    for (x, y) in centers:
        for sx in (-1, 1):
            x2, y2 = x + sx * dx / 2, y + dy
            mx, my = (x + x2) / 2 + sx * 1.6, (y + y2) / 2 - 1.2
            vines.append(f"M{F(x)} {F(y)}Q{F(mx)} {F(my)} {F(x2)} {F(y2)}")
    out.append(f'<path d="{"".join(vines)}" style="fill:none;stroke:{c["cream"]};stroke-width:0.32;opacity:0.75"/>')
    for (x, y) in centers:
        for k, a in enumerate((math.pi / 4, 3 * math.pi / 4, 5 * math.pi / 4, 7 * math.pi / 4)):
            out.append(leaf(x + 1.6 * math.cos(a), y + 1.6 * math.sin(a), 3.6, a, 0.9, c['green'] if k % 2 else c['navy2']))
        out.append(rosette(x, y, 2.3, 8, c['gold'], c['red2'], c['dark'], rot=math.pi / 8, inner=c['cream']))
    for (x, y) in centers:
        mx = x + dx / 2
        if FX0 - 3 < mx < FX1 + 3:
            out.append(flower4(mx, y, 1.15, c['pink'], c['cream']))
    return "".join(out)


# ---------------------------------------------------------------- Medaillon und Ecken
def medallion(c):
    rx, ry = 50.0, 33.0
    out = [f'<path d="{scallop(CX, CY, rx + 2.2, ry + 2.0, 30, 0.10)}" style="fill:{c["cream"]};stroke:{c["dark"]};stroke-width:0.35"/>',
           f'<path d="{scallop(CX, CY, rx, ry, 30, 0.10)}" style="fill:{c["navy"]};stroke:{c["dark"]};stroke-width:0.3"/>']
    # Anhänger links und rechts
    for s in (-1, 1):
        px = CX + s * (rx + 9.5)
        cart = [(px - s * 5.5, CY), (px, CY - 6.0), (px + s * 4.5, CY), (px, CY + 6.0)]
        out.append(f'<path d="{P(cart)}" style="fill:{c["cream"]};stroke:{c["dark"]};stroke-width:0.35"/>')
        out.append(flower4(px - s * 0.4, CY, 2.0, c['red2'], c['gold']))
        out.append(palmette(px + s * 7.0, CY, 5.2, 0 if s > 0 else math.pi, c['navy'], c['red2'], c['dark']))
        out.append(f'<path d="M{F(CX + s*(rx+1.5))} {F(CY)}L{F(px - s*5.5)} {F(CY)}" style="stroke:{c["cream"]};stroke-width:0.7"/>')
    # Kranz innen
    out.append(f'<ellipse cx="{F(CX)}" cy="{F(CY)}" rx="{F(rx-6)}" ry="{F(ry-5)}" style="fill:none;stroke:{c["cream"]};stroke-width:2.6"/>')
    for k in range(28):
        a = 2 * math.pi * k / 28
        x, y = CX + (rx - 6) * math.cos(a), CY + (ry - 5) * math.sin(a)
        out.append(flower4(x, y, 0.95, c['red2'] if k % 2 else c['navy2'], c['gold']))
    # Mitte: Ranken zu den Palmetten, Blüten dazwischen, Blattkranz, große Rosette
    vines = []
    for k in range(10):
        a = 2 * math.pi * k / 10 + math.pi / 10
        x0, y0 = CX + 11 * math.cos(a), CY + 9 * math.sin(a)
        x1, y1 = CX + 20 * math.cos(a), CY + 13.2 * math.sin(a)
        b = a + 0.45
        cx1, cy1 = CX + 16 * math.cos(b), CY + 12 * math.sin(b)
        vines.append(f"M{F(x0)} {F(y0)}Q{F(cx1)} {F(cy1)} {F(x1)} {F(y1)}")
        b2 = a + math.pi / 10
        x2, y2 = CX + 31 * math.cos(b2), CY + 20.5 * math.sin(b2)
        vines.append(f"M{F(x1)} {F(y1)}Q{F(CX + 27*math.cos(a + 0.05))} {F(CY + 19*math.sin(a + 0.05))} {F(x2)} {F(y2)}")
        out.append(flower4(x2, y2, 1.35, c['pink'], c['gold']))
        out.append(leaf(CX + 27 * math.cos(b2 - 0.12), CY + 18 * math.sin(b2 - 0.12), 3.0, b2 + math.pi / 2, 0.8, c['navy2']))
    out.append(f'<path d="{"".join(vines)}" style="fill:none;stroke:{c["gold"]};stroke-width:0.45"/>')
    out.append(f'<ellipse cx="{F(CX)}" cy="{F(CY)}" rx="{F(rx-11)}" ry="{F(ry-9)}" style="fill:none;stroke:{c["gold"]};stroke-width:0.35;stroke-dasharray:0.6 0.9"/>')
    for k in range(10):
        a = 2 * math.pi * k / 10 + math.pi / 10
        x, y = CX + 22 * math.cos(a), CY + 14.5 * math.sin(a)
        out.append(palmette(x, y, 5.0, a, c['red2'], c['gold'], c['dark']))
        lx, ly = CX + 13 * math.cos(a + math.pi / 10), CY + 8.6 * math.sin(a + math.pi / 10)
        out.append(leaf(lx, ly, 4.2, a + math.pi / 10, 1.0, c['green'], c['dark']))
    for k in range(14):
        a = 2 * math.pi * k / 14
        out.append(leaf(CX + 12.2 * math.cos(a), CY + 10.2 * math.sin(a), 2.6, a, 0.75, c['green'] if k % 2 else c['gold']))
    out.append(f'<ellipse cx="{F(CX)}" cy="{F(CY)}" rx="12.5" ry="10.5" style="fill:{c["cream"]};stroke:{c["dark"]};stroke-width:0.35"/>')
    out.append(rosette(CX, CY, 10.0, 12, c['red2'], c['navy'], c['dark'], rot=math.pi / 12, inner=c['gold']))
    out.append(rosette(CX, CY, 4.4, 6, c['gold'], c['red2'], c['dark'], inner=c['cream']))
    return "".join(out)


def corners(c):
    out = []
    rx, ry = 40.0, 27.0
    for (x, y) in ((FX0, FY0), (FX1, FY0), (FX0, FY1), (FX1, FY1)):
        out.append(f'<g transform="translate({F(x)} {F(y)}) scale({MED_K}) translate({F(-x)} {F(-y)})">')
        out.append(f'<path d="{scallop(x, y, rx + 2.0, ry + 1.8, 32, 0.10)}" style="fill:{c["cream"]};stroke:{c["dark"]};stroke-width:0.35"/>')
        out.append(f'<path d="{scallop(x, y, rx, ry, 32, 0.10)}" style="fill:{c["navy"]};stroke:{c["dark"]};stroke-width:0.3"/>')
        out.append(f'<ellipse cx="{F(x)}" cy="{F(y)}" rx="{F(rx-6)}" ry="{F(ry-5)}" style="fill:none;stroke:{c["cream"]};stroke-width:2.2"/>')
        sx = 1 if x == FX0 else -1; sy = 1 if y == FY0 else -1
        for k in range(9):
            a = math.atan2(sy, sx) + (k - 4) * 0.19
            fx, fy = x + (rx - 6) * math.cos(a), y + (ry - 5) * math.sin(a)
            out.append(flower4(fx, fy, 0.9, c['red2'] if k % 2 else c['gold'], c['cream']))
        arc = []
        for k in range(13):
            a = math.atan2(sy, sx) + (k - 6) * 0.13
            arc.append((x + (rx - 14) * math.cos(a), y + (ry - 11.5) * math.sin(a)))
        out.append(f'<path d="M' + "L".join(f"{F(px)} {F(py)}" for px, py in arc) + f'" style="fill:none;stroke:{c["gold"]};stroke-width:0.45"/>')
        for k, (px, py) in enumerate(arc):
            if k % 3 == 0:
                out.append(flower4(px, py, 1.3, c['pink'] if k % 2 else c['cream'], c['red2']))
            elif k % 3 == 1:
                out.append(leaf(px, py, 2.6, math.atan2(sy, sx) + (0.9 if k % 2 else -0.9), 0.7, c['green']))
        out.append(palmette(x + sx * 12, y + sy * 8, 7.0, math.atan2(sy, sx * 1.4), c['red2'], c['gold'], c['dark']))
        out.append(leaf(x + sx * 4, y + sy * 15, 6, math.atan2(0.2 * sy, sx), 1.3, c['green'], c['dark']))
        out.append(leaf(x + sx * 20, y + sy * 3, 6, math.atan2(sy, 0.3 * sx), 1.3, c['green'], c['dark']))
        out.append('</g>')
    return "".join(out)


# ---------------------------------------------------------------- Bordüren
def guard(x0, y0, x1, y1, c, step=5.5):
    """schmale Wächterbordüre: Creme, Blüte und Punkt im Wechsel, rundum"""
    w = G_OUT
    out = [f'<path d="M{F(x0)} {F(y0)}H{F(x1)}V{F(y1)}H{F(x0)}Z M{F(x0+w)} {F(y0+w)}V{F(y1-w)}H{F(x1-w)}V{F(y0+w)}Z" style="fill:{c["cream"]};fill-rule:evenodd"/>',
           f'<path d="M{F(x0+0.35)} {F(y0+0.35)}H{F(x1-0.35)}V{F(y1-0.35)}H{F(x0+0.35)}Z M{F(x0+w-0.35)} {F(y0+w-0.35)}H{F(x1-w+0.35)}V{F(y1-w+0.35)}H{F(x0+w-0.35)}Z" style="fill:none;stroke:{c["red2"]};stroke-width:0.3"/>']
    pts = []
    def run(ax, ay, bx, by):
        L = math.hypot(bx - ax, by - ay); n = max(1, round(L / step))
        for k in range(n):
            t = (k + 0.5) / n
            pts.append((ax + (bx - ax) * t, ay + (by - ay) * t, k % 2))
    m = w / 2
    run(x0 + w, y0 + m, x1 - w, y0 + m); run(x0 + w, y1 - m, x1 - w, y1 - m)
    run(x0 + m, y0 + w, x0 + m, y1 - w); run(x1 - m, y0 + w, x1 - m, y1 - w)
    for (x, y, k) in pts:
        out.append(flower4(x, y, 1.15, c['red2'], c['gold']) if k == 0 else f'<circle cx="{F(x)}" cy="{F(y)}" r="0.6" style="fill:{c["navy"]}"/>')
    for (x, y) in ((x0 + m, y0 + m), (x1 - m, y0 + m), (x0 + m, y1 - m), (x1 - m, y1 - m)):
        out.append(flower4(x, y, 1.2, c['navy'], c['gold']))
    return "".join(out)


def main_border(x0, y0, x1, y1, c):
    """breite Bordüre: dunkelblauer Grund, Wellenranke mit Rosetten und Palmetten, Eckrosetten"""
    w = MAIN
    out = [f'<path d="M{F(x0)} {F(y0)}H{F(x1)}V{F(y1)}H{F(x0)}Z M{F(x0+w)} {F(y0+w)}V{F(y1-w)}H{F(x1-w)}V{F(y0+w)}Z" style="fill:{c["navy"]};fill-rule:evenodd"/>']
    def side(ax, ay, bx, by, nx, ny):
        L = math.hypot(bx - ax, by - ay); ux, uy = (bx - ax) / L, (by - ay) / L
        n = max(2, round(L / 22.0)); per = L / n
        pts = []
        for i in range(int(L * 2) + 1):
            s = i / 2.0
            off = 3.0 * math.sin(2 * math.pi * s / per)
            pts.append((ax + ux * s + nx * off, ay + uy * s + ny * off))
        out.append(f'<path d="M' + "L".join(f"{F(x)} {F(y)}" for x, y in pts) + f'" style="fill:none;stroke:{c["cream"]};stroke-width:0.85"/>')
        for k in range(n * 2):
            s = (k + 0.5) * per / 2
            sign = 1 if k % 2 == 0 else -1
            x, y = ax + ux * s + nx * 3.0 * sign, ay + uy * s + ny * 3.0 * sign
            if k % 2 == 0:
                out.append(rosette(x, y, 3.5, 8, c['red2'], c['cream'], c['dark'], inner=c['gold']))
            else:
                out.append(palmette(x, y, 4.2, math.atan2(-ny, -nx) if sign < 0 else math.atan2(ny, nx), c['cream'], c['red2'], c['dark']))
            # Blätter an der Ranke
            ls = s + per / 4
            lx, ly = ax + ux * ls, ay + uy * ls
            out.append(leaf(lx, ly, 3.2, math.atan2(uy + ny * 0.8, ux + nx * 0.8), 0.9, c['green']))
            out.append(leaf(lx, ly, 3.2, math.atan2(uy - ny * 0.8, ux - nx * 0.8), 0.9, c['navy2']))
    m = w / 2
    side(x0 + w, y0 + m, x1 - w, y0 + m, 0, 1)
    side(x0 + w, y1 - m, x1 - w, y1 - m, 0, -1)
    side(x0 + m, y0 + w, x0 + m, y1 - w, 1, 0)
    side(x1 - m, y0 + w, x1 - m, y1 - w, -1, 0)
    for (x, y) in ((x0 + m, y0 + m), (x1 - m, y0 + m), (x0 + m, y1 - m), (x1 - m, y1 - m)):
        out.append(rosette(x, y, 5.2, 10, c['gold'], c['red2'], c['dark'], inner=c['cream']))
        for a in (0, math.pi / 2, math.pi, 3 * math.pi / 2):
            out.append(leaf(x + 4.8 * math.cos(a + math.pi / 4), y + 4.8 * math.sin(a + math.pi / 4), 2.4, a + math.pi / 4, 0.8, c['green']))
    return "".join(out)


# ---------------------------------------------------------------- ganzer Teppich
def carpet(variant='oma', uid='a', texture=True):
    """Gibt den Teppich als <g> in mm zurück (0..W, 0..H), ohne Fransen und ohne Kante"""
    c = PAL[variant]
    clip = f'clip-{uid}'
    out = [f'<defs><clipPath id="{clip}"><rect x="{F(FX0)}" y="{F(FY0)}" width="{F(FX1-FX0)}" height="{F(FY1-FY0)}"/></clipPath>'
           f'<filter id="velvet-{uid}" x="0" y="0" width="1" height="1"><feTurbulence type="fractalNoise" baseFrequency="1.7" numOctaves="2" seed="7" result="n"/>'
           f'<feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.16 0" in="n" result="a"/><feComposite in="a" in2="SourceGraphic" operator="in"/></filter></defs>']
    out.append(f'<rect x="0" y="0" width="{F(W)}" height="{F(H)}" style="fill:{c["field"]}"/>')
    # Abrasch: ganz leichte Farbstreifen im Feld, wie Wolle aus verschiedenen Färbungen
    for k, (y, h) in enumerate(((38, 9), (66, 5), (97, 11))):
        out.append(f'<rect x="{F(FX0)}" y="{F(y * H / 150)}" width="{F(FX1-FX0)}" height="{F(h * H / 150)}" style="fill:{c["abrash"]};opacity:0.45"/>')
    out.append(f'<g clip-path="url(#{clip})">{field_pattern(c)}{corners(c)}</g>')
    out.append(f'<g transform="translate({F(CX)} {F(CY)}) scale({MED_K}) translate({F(-CX)} {F(-CY)})">{medallion(c)}</g>')
    # Bordüren
    x0, y0, x1, y1 = KILIM, FRAME, W - KILIM, H - FRAME
    out.append(f'<rect x="{F(x0)}" y="{F(y0)}" width="{F(x1-x0)}" height="{F(y1-y0)}" style="fill:none;stroke:{c["dark"]};stroke-width:0.5"/>')
    out.append(guard(x0, y0, x1, y1, c))
    b0 = G_OUT
    out.append(f'<rect x="{F(x0+b0+LINE/2)}" y="{F(y0+b0+LINE/2)}" width="{F(x1-x0-2*b0-LINE)}" height="{F(y1-y0-2*b0-LINE)}" style="fill:none;stroke:{c["dark"]};stroke-width:{F(LINE)}"/>')
    mx0, my0, mx1, my1 = x0 + b0 + LINE, y0 + b0 + LINE, x1 - b0 - LINE, y1 - b0 - LINE
    out.append(main_border(mx0, my0, mx1, my1, c))
    out.append(f'<rect x="{F(mx0+MAIN+LINE/2)}" y="{F(my0+MAIN+LINE/2)}" width="{F(mx1-mx0-2*MAIN-LINE)}" height="{F(my1-my0-2*MAIN-LINE)}" style="fill:none;stroke:{c["dark"]};stroke-width:{F(LINE)}"/>')
    gx0, gy0, gx1, gy1 = mx0 + MAIN + LINE, my0 + MAIN + LINE, mx1 - MAIN - LINE, my1 - MAIN - LINE
    out.append(guard(gx0, gy0, gx1, gy1, c, step=5.0))
    # gewebter Abschluss links und rechts (Kelim), aus dem die Fransen kommen
    for xk in (0, W - KILIM):
        out.append(f'<rect x="{F(xk)}" y="0" width="{F(KILIM)}" height="{F(H)}" style="fill:{c["cream"]}"/>')
        out.append(f'<path d="M{F(xk+1.0)} 0V{F(H)}M{F(xk+2.0)} 0V{F(H)}" style="stroke:{c["red2"]};stroke-width:0.25"/>')
    if texture:
        out.append(f'<rect x="0" y="0" width="{F(W)}" height="{F(H)}" style="fill:#000" filter="url(#velvet-{uid})" opacity="0.9"/>')
    return "".join(out)


def edge(variant='oma'):
    """dunkelrote Stickkante oben und unten (Plattstich), 4 mm, deckt die Schnittkante des Samts"""
    c = PAL[variant]; out = []
    for y in (-1.5, H - 2.5):
        out.append(f'<rect x="-0.5" y="{F(y)}" width="{F(W+1)}" height="4" rx="0.8" style="fill:{c["edge"]}"/>')
        hatch = "".join(f"M{F(x)} {F(y+0.3)}l0.9 3.4" for x in [i * 0.55 for i in range(int((W + 0.5) / 0.55))])
        out.append(f'<path d="{hatch}" style="stroke:#ffffff;stroke-opacity:0.16;stroke-width:0.22"/>')
    return "".join(out)


def fringes(variant='oma', length=35.0, step=5.0):
    """Fransen links und rechts: Bündel aus 4 Fäden, 5 mm nach der Kante geknotet"""
    c = PAL[variant]; out = []
    n = int(H / step)
    for side in (-1, 1):
        x0 = 0.0 if side < 0 else W
        for k in range(n):
            y = (k + 0.5) * H / n
            kx = x0 + side * 5.0
            for t in range(4):
                sy = y + (t - 1.5) * 0.9
                ey = y + (t - 1.5) * 1.5 + (0.6 if k % 2 else -0.4)
                ex = x0 + side * (length - (t % 2) * 1.4)
                out.append(f'<path d="M{F(x0)} {F(sy)}Q{F(kx-side*1.5)} {F(sy)} {F(kx)} {F(y)}Q{F(kx+side*(length-5)*0.5)} {F((y+ey)/2+0.8*(1 if t%2 else -1))} {F(ex)} {F(ey)}" '
                           f'style="fill:none;stroke:{c["fringe"]};stroke-width:0.62;stroke-linecap:round"/>')
            out.append(f'<ellipse cx="{F(kx)}" cy="{F(y)}" rx="1.2" ry="1.5" style="fill:{c["fringe"]};stroke:#9b8f78;stroke-width:0.25"/>')
    return f'<g style="filter:drop-shadow(0 0.4px 0.3px rgba(0,0,0,.25))">{"".join(out)}</g>'


def zip_strip(y0=-6.0, y1=None, x=CX, w=5.0, stitch='#6a1418'):
    """geschlossener Reißverschluss, dunkles Antik-Metall, verzahnt, läuft durch die Mitte.
    Die Innenkanten des Teppichs stecken in der Zip-Naht, die Steppnaht läuft 3 mm daneben."""
    y1 = H + 6.0 if y1 is None else y1
    n = int((y1 - y0) / 1.0)
    teeth = "".join(f'<rect x="{F(x - w/2 if i % 2 else x - 0.4)}" y="{F(y0 + i*1.0)}" width="{F(w/2 + 0.4)}" height="0.72" rx="0.25" '
                    f'style="fill:{"#6e5a47" if i % 2 else "#806a55"}"/>' for i in range(n))
    return (f'<rect x="{F(x - w/2 - 0.3)}" y="{F(y0)}" width="{F(w + 0.6)}" height="{F(y1 - y0)}" style="fill:#2f251e"/>' + teeth +
            f'<path d="M{F(x - w/2 - 3.0)} {F(y0)}V{F(y1)}M{F(x + w/2 + 3.0)} {F(y0)}V{F(y1)}" style="stroke:{stitch};stroke-width:0.32;stroke-dasharray:1.5 0.9;opacity:0.9"/>')


def standalone(variant, with_zip=True, pad=45):
    """eigenständiges SVG zum Ansehen: Teppich mit Kante, Fransen und Reißverschluss"""
    vb_w, vb_h = W + 2 * pad, H + 30
    g = carpet(variant, uid=variant) + edge(variant) + (zip_strip(stitch=PAL[variant]['edge']) if with_zip else '')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{F(vb_w*4)}" height="{F(vb_h*4)}" viewBox="{F(-pad)} -15 {F(vb_w)} {F(vb_h)}">'
            f'<rect x="{F(-pad)}" y="-15" width="{F(vb_w)}" height="{F(vb_h)}" style="fill:#efe8da"/>'
            f'{fringes(variant)}{g}</svg>')


if __name__ == '__main__':
    import os, sys
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    for v in PAL:
        open(os.path.join(out, f'teppich_{v}.svg'), 'w', encoding='utf-8').write(standalone(v))
    print('ok')
