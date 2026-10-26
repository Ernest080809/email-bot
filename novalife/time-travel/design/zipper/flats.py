# -*- coding: utf-8 -*-
# Zipper NVL-TT-02 · technische Ansichten für den Designvorschlag v0.1 (24.10.2026)
# Maße vorläufig (Größe M, flach): Brust 60 cm, Länge 69 cm ab Halsansatz, Schultern 4 cm überschnitten.
# Die echten Maße kommen aus dem Messbogen RL-Zipper. Einheiten: mm, x = 0 in der vorderen Mitte, y = 0 auf Höhe Halsansatz.
import math, os, random, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import fine as FN
import teppich as TP

F = TP.F
GARMENT, LINE, SHADE, RIBC = '#efe8da', '#7b6b53', '#e2d9c6', '#e7dfcf'
RED, RED_L = '#d0281f', '#e6564b'      # Knallrot für Siebdruck und Stern C, der Ton wird aufs Stickgarn abgestimmt
COPPER, COPPER_D = '#a8643a', '#6f3d1f'

NX, ND = 105, 95                       # Halsansatz, vordere Ausschnitttiefe bis zum Zip-Anfang
SHOULDER, ARMPIT = (285, 45), (300, 255)
RIB_TOP, HEM, RIB_IN = 625, 690, 285   # Saumrippe 65 mm (Platzhalter, mindestens 50 mm für den Stern)
CARPET_TOP = ND + 60                   # Oberkante Teppich 6 cm unter dem Zip-Anfang (Papiertest)
EYELET = (60, 44)
SIDE = [SHOULDER, ARMPIT, (300, RIB_TOP), (RIB_IN, HEM)]


def mirror(pts):
    return [(-x, y) for x, y in pts]


def poly(pts):
    return "M" + "L".join(f"{F(x)} {F(y)}" for x, y in pts) + "Z"


def lines(pts):
    return "".join(f"L{F(x)} {F(y)}" for x, y in pts)


def neck_r():                          # von (0, ND) nach (NX, 0)
    return f"C{F(0.43*NX)} {ND} {F(0.95*NX)} {F(0.63*ND)} {NX} 0"


def neck_l():                          # von (-NX, 0) nach (0, ND)
    return f"C{F(-0.95*NX)} {F(0.63*ND)} {F(-0.43*NX)} {ND} 0 {ND}"


def neck_r_rev():                      # von (NX, 0) nach (0, ND)
    return f"C{F(0.95*NX)} {F(0.63*ND)} {F(0.43*NX)} {ND} 0 {ND}"


def neck_l_rev():                      # von (0, ND) nach (-NX, 0)
    return f"C{F(-0.43*NX)} {ND} {F(-0.95*NX)} {F(0.63*ND)} {-NX} 0"


def sleeve(s):
    pts = [SHOULDER, (420, 548), (412, 616), (330, 632), (322, 570), ARMPIT]
    cuff = [(420, 548), (412, 616), (330, 632), (322, 570)]
    if s < 0:
        pts, cuff = mirror(pts), mirror(cuff)
    ribs = []
    for t in range(1, 12):
        f = t / 12
        ax = cuff[3][0] + (cuff[0][0] - cuff[3][0]) * f; ay = cuff[3][1] + (cuff[0][1] - cuff[3][1]) * f
        bx = cuff[2][0] + (cuff[1][0] - cuff[2][0]) * f; by = cuff[2][1] + (cuff[1][1] - cuff[2][1]) * f
        ribs.append(f"M{F(ax)} {F(ay+2)}L{F(bx)} {F(by-2)}")
    return (f'<path d="{poly(pts)}" style="fill:{GARMENT};stroke:{LINE};stroke-width:1.6;stroke-linejoin:round"/>'
            f'<path d="{poly(cuff)}" style="fill:{RIBC};stroke:{LINE};stroke-width:1.2"/>'
            f'<path d="{"".join(ribs)}" style="stroke:{LINE};stroke-width:0.45;opacity:0.5"/>'
            f'<path d="M{F(s*SHOULDER[0])} {F(SHOULDER[1])}Q{F(s*(SHOULDER[0]+28))} 150 {F(s*ARMPIT[0])} {F(ARMPIT[1])}" style="fill:none;stroke:{LINE};stroke-width:0.9"/>')


def body(front=True):
    right, left = lines(SIDE), lines(mirror(list(reversed(SIDE))))
    if front:
        d = f"M0 {ND}{neck_r()}{right}{left}L{-NX} 0{neck_l()}Z"
    else:
        d = f"M{-NX} 0Q0 16 {NX} 0{right}{left}Z"
    rib = [(-300, RIB_TOP), (300, RIB_TOP), (RIB_IN, HEM), (-RIB_IN, HEM)]
    ribl = "".join(f"M{F(x)} {RIB_TOP+3}L{F(x*0.97)} {HEM-3}" for x in range(-292, 293, 7))
    return (f'<path d="{d}" style="fill:{GARMENT};stroke:{LINE};stroke-width:1.6;stroke-linejoin:round"/>'
            f'<path d="{poly(rib)}" style="fill:{RIBC};stroke:{LINE};stroke-width:1.2"/>'
            f'<path d="{ribl}" style="stroke:{LINE};stroke-width:0.45;opacity:0.45"/>')


HOOD_OUT = f"M{-NX} 0C-160 -110 -122 -334 0 -348C122 -334 160 -110 {NX} 0"
FACE = f"M0 {ND}C-62 70 -94 -40 -80 -170C-72 -258 72 -258 80 -170C94 -40 62 70 0 {ND}Z"


def hood_up(front=True):
    if front:
        d = HOOD_OUT + neck_r_rev() + neck_l_rev() + "Z"
        rim = f"M-9 {ND-5}C-74 64 -110 -40 -95 -177C-85 -274 85 -274 95 -177C110 -40 74 64 9 {ND-5}"
        return (f'<path d="{d}" style="fill:{GARMENT};stroke:{LINE};stroke-width:1.6;stroke-linejoin:round"/>'
                f'<path d="{FACE}" style="fill:{SHADE};stroke:{LINE};stroke-width:1.3"/>'
                f'<path d="{rim}" style="fill:none;stroke:{LINE};stroke-width:0.7;stroke-dasharray:3 2.2;opacity:0.8"/>')
    d = HOOD_OUT + f"Q0 16 {-NX} 0Z"
    return (f'<path d="{d}" style="fill:{GARMENT};stroke:{LINE};stroke-width:1.6;stroke-linejoin:round"/>'
            f'<path d="M0 -346V9" style="stroke:{LINE};stroke-width:0.9"/>')


# liegende Kapuze, von hinten gesehen (Platzhalter bis zum Messbogen)
HOOD_DOWN = [((-NX, 0), (-176, 26), (-206, 160), (-150, 262)),
             ((-150, 262), (-110, 334), (110, 334), (150, 262)),
             ((150, 262), (206, 160), (176, 26), (NX, 0))]


def hood_down_d():
    s = HOOD_DOWN
    return f"M{s[0][0][0]} {s[0][0][1]}" + "".join(
        f"C{F(b[1][0])} {F(b[1][1])} {F(b[2][0])} {F(b[2][1])} {F(b[3][0])} {F(b[3][1])}" for b in s) + "Z"


def hood_down_back():
    return (f'<path d="{hood_down_d()}" style="fill:{GARMENT};stroke:{LINE};stroke-width:1.5;filter:drop-shadow(0 3px 3px rgba(60,45,30,.18))"/>'
            f'<path d="M-92 14C-158 38 -186 160 -136 254C-100 318 100 318 136 254C186 160 158 38 92 14" style="fill:none;stroke:{LINE};stroke-width:0.7;stroke-dasharray:3 2.2;opacity:0.8"/>'
            f'<path d="M0 8V316" style="stroke:{LINE};stroke-width:0.9"/>')


def cords():
    out = []
    ex, ey = EYELET
    for s in (-1, 1):
        x = s * ex
        d = f"M{x} {ey + 3}C{x + s*3} 140 {x - s*6} 240 {x + s*1} 314"
        out.append(f'<path d="{d}" style="fill:none;stroke:{LINE};stroke-width:5.2;stroke-linecap:round"/>'
                   f'<path d="{d}" style="fill:none;stroke:{GARMENT};stroke-width:3.6;stroke-linecap:round"/>')
        out.append(f'<rect x="{F(x + s*1 - 3.4)}" y="312" width="6.8" height="26" rx="2.2" style="fill:{COPPER};stroke:{COPPER_D};stroke-width:0.8"/>')
        out.append(f'<circle cx="{x}" cy="{ey}" r="5.2" style="fill:{COPPER};stroke:{COPPER_D};stroke-width:0.9"/><circle cx="{x}" cy="{ey}" r="2.6" style="fill:{SHADE}"/>')
    return "".join(out)


def star_charm(cx, cy, w=25):
    polys = FN.star8_rhombi(cx, cy, w, 0.8)
    d = "".join("M" + "L".join(f"{F(x)} {F(y)}" for x, y in q) + "Z" for q in polys)
    return (f'<path d="M{F(cx)} {F(cy - w/2 - 9)}V{F(cy - w/2 - 1)}" style="stroke:{COPPER_D};stroke-width:1.6"/>'
            f'<circle cx="{F(cx)}" cy="{F(cy - w/2 - 2.5)}" r="2.6" style="fill:none;stroke:{COPPER};stroke-width:1.4"/>'
            f'<path d="{d}" style="fill:{COPPER};stroke:{COPPER_D};stroke-width:0.6"/>')


def zipper_front(y0=ND):
    out = [TP.zip_strip(y0, HEM, 0, 5.0, stitch=LINE).replace('opacity:0.9', 'opacity:0.7')]
    out.append(f'<rect x="-9" y="{y0 - 8}" width="18" height="16" rx="3" style="fill:{GARMENT};stroke:{LINE};stroke-width:1.1"/>')
    out.append(f'<rect x="-5" y="{y0 + 10}" width="10" height="13" rx="2" style="fill:#4a3b2e;stroke:#2a2019;stroke-width:0.7"/>')
    out.append(star_charm(0, y0 + 46))
    return "".join(out)


def pockets():
    out = []
    for s in (-1, 1):
        a, b = (s * 160, 440), (s * 214, 594)
        out.append(f'<path d="M{a[0]} {a[1]}L{b[0]} {b[1]}" style="stroke:{LINE};stroke-width:1.6"/>')
        out.append(f'<path d="M{a[0] - s*7} {a[1] + 2}L{b[0] - s*7} {b[1] + 2}" style="stroke:{LINE};stroke-width:0.7;stroke-dasharray:3 2.2;opacity:0.8"/>')
        out.append(f'<path d="M{a[0] - s*7} {a[1] + 2}L{a[0]} {a[1]}M{b[0] - s*7} {b[1] + 2}L{b[0]} {b[1]}" style="stroke:{LINE};stroke-width:1.4"/>')
    return "".join(out)


def carpet_on_body(variant, uid, scale=1.0):
    g = TP.carpet(variant, uid=uid) + TP.edge(variant)
    x0 = -TP.W * scale / 2
    return (f'<g transform="translate({F(x0)} {F(CARPET_TOP)}) scale({F(scale)})">'
            f'<g style="filter:drop-shadow(0 1.2px 1.2px rgba(40,25,15,.35))">{TP.fringes(variant)}{g}</g></g>')


# ---------------------------------------------------------------- Druck unter der Kapuze
# Fläche = liegende Kapuze rundum 2 cm kleiner, unten gerade mit einem Streifen Band A abgeschlossen.
# Nur ganze Zellen: keine Splitter am Rand, die im Siebdruck zulaufen oder ausbrechen.
INSET_MM = 20.0
PRINT_BOTTOM = 272.0                   # Unterkante Band A (vorläufig, die Kapuze kommt aus dem Messbogen)


def _bez(b, n):
    out = []
    for k in range(n):
        t = k / n; m = 1 - t
        out.append((m**3*b[0][0] + 3*m*m*t*b[1][0] + 3*m*t*t*b[2][0] + t**3*b[3][0],
                    m**3*b[0][1] + 3*m*m*t*b[1][1] + 3*m*t*t*b[2][1] + t**3*b[3][1]))
    return out


def hood_poly(n=48):
    pts = []
    for b in HOOD_DOWN:
        pts += _bez(b, n)
    return pts + [HOOD_DOWN[-1][3]]


def _area(pts):
    return sum(pts[i][0]*pts[(i+1) % len(pts)][1] - pts[(i+1) % len(pts)][0]*pts[i][1] for i in range(len(pts))) / 2


def print_outline(cut_y=PRINT_BOTTOM, inset=INSET_MM):
    hp = hood_poly()
    pts = FN._inset(hp, inset)
    if abs(_area(pts)) > abs(_area(hp)):          # falsche Richtung erwischt
        pts = FN._inset(hp, -inset)
    out, n = [], len(pts)
    for i in range(n):
        p, q = pts[i], pts[(i + 1) % n]
        pin, qin = p[1] <= cut_y, q[1] <= cut_y
        if pin:
            out.append(p)
        if pin != qin:
            f = (cut_y - p[1]) / (q[1] - p[1])
            out.append((p[0] + (q[0] - p[0]) * f, cut_y))
    return out


def _inside(x, y, pg):
    c, n = False, len(pg)
    for i in range(n):
        (x1, y1), (x2, y2) = pg[i], pg[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            c = not c
    return c


def _e_white(x, y):
    """Muster E der Münztasche als Fläche: Rautengitter mit Rapport 8 und kleine Kreuze in den Rauten"""
    if (x + y) % 8 == 0 or (x - y) % 8 == 0:
        return True
    for dx, dy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
        a, b = x + dx, y + dy
        if (a % 8 == 4 and b % 8 == 0) or (a % 8 == 0 and b % 8 == 4):
            return True
    return False


def _smooth(e0, e1, t):
    t = min(1.0, max(0.0, (t - e0) / (e1 - e0)))
    return t * t * (3 - 2 * t)


def _keep_diamond(x, y, u, e_h, half_w, seed=11):
    """Verlauf: Jede Raute des Gitters bleibt oder fällt als Ganzes. Unten am Band bleiben alle,
    nach oben und zur Seite fallen immer mehr weg, bis das Muster ausläuft.
    Links und rechts gespiegelt (Zufall pro Rautenpaar), damit es gewollt aussieht wie ein Ornament."""
    a, b = (x + y) // 8, (x - y) // 8
    xc, yc = 4 * a + 4 * b + 4, 4 * a - 4 * b
    t = math.hypot(yc * u / e_h, 0.85 * abs(xc) * u / half_w)
    return random.Random(f"{abs(xc)},{yc},{seed}").random() < 1 - _smooth(0.28, 0.98, t)


# Wege für den Rückendruck (Ernest 24.10.: „sieht irgendwie mid aus“)
MODES = {'flaeche': 'Fläche wie bisher', 'linien': 'Nur die Linien',
         'verlauf': 'Verlauf nach oben', 'streifen': 'Querstreifen'}
MODE_SCALE = {'flaeche': 2, 'linien': 2, 'verlauf': 1, 'streifen': 1}     # so gezeichnet, Papiertest entscheidet


def print_cells(scale=2, mode='flaeche', cut_y=PRINT_BOTTOM):
    """Rote Zellen der Rückenfläche. Reihen j von unten: Band A, eine Reihe Luft, darüber Muster E.
    flaeche: roter Grund wie an der Münztasche, eine Reihe Rot als Kante
    linien:  nur Linien und Kreuze von E rot, eine Reihe Rot als Kante
    verlauf: roter Grund, die Rauten lösen sich nach oben und zur Seite auf, keine Kante"""
    if mode == 'streifen':
        return stripe_cells(scale)
    u = FN.CELL * scale
    pg = print_outline(cut_y)
    BR = FN.BAND_ROWS
    top = min(p[1] for p in pg)
    half_w = max(abs(p[0]) for p in pg)
    e_h = cut_y - (BR + 1) * u - top
    hc = int(half_w / u) + 1
    ncols, nrows = 2 * hc + 1, int((cut_y - top) / u) + 1
    bw = FN.band_white(ncols, start=(11 - hc) % FN.RAP)          # Stern-Motiv von Band A in der hinteren Mitte
    cell_in = {}
    for j in range(nrows):
        for c in range(ncols):
            cx, cy = (c - hc) * u, cut_y - (j + 0.5) * u
            cell_in[(j, c)] = _inside(cx, cy, pg)
    def whole(x, y):                                          # Raute liegt ganz in der Fläche (unten darf das Band sie schneiden)
        a, b = (x + y) // 8, (x - y) // 8
        xc, yc = 4 * a + 4 * b + 4, 4 * a - 4 * b
        ends = [(xc - 3, yc), (xc + 3, yc), (xc, yc + 3)] + ([(xc, yc - 3)] if yc >= 3 else [])
        return all(cell_in.get((ey + BR + 1, ex + hc), False) for ex, ey in ends)

    red = set()
    for (j, c), ok in cell_in.items():
        if not ok:
            continue
        if j < BR:                                            # Band A, Reihe 0 oben
            if (BR - 1 - j, c) not in bw:
                red.add((j, c))
        elif j == BR:
            continue                                          # eine Reihe Luft
        else:
            x, y = c - hc, j - BR - 1
            w = _e_white(x, y)
            if mode == 'linien':
                if w:
                    red.add((j, c))
            elif not w and (mode == 'flaeche' or (whole(x, y) and _keep_diamond(x, y, u, e_h, half_w))):
                red.add((j, c))
    if mode in ('flaeche', 'linien'):
        for (j, c), ok in cell_in.items():
            if ok and j > BR and any(not cell_in.get((j + dj, c + dc), False) for dj, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                red.add((j, c))
    return red, u, hc, pg


STRIPE_TOP = 52.0                      # Oberkante Querstreifen, unter dem Halsansatz über den Schulterblättern


def stripe_cells(scale=1, top=STRIPE_TOP):
    """Querstreifen: Band A oben und unten, dazwischen zwei Rautenreihen Muster E mit roter Kante.
    Die Enden liegen in der Lücke zwischen zwei Motiven von Band A. Liegt ganz unter der liegenden Kapuze."""
    u = FN.CELL * scale
    BR, ER = FN.BAND_ROWS, 17
    hc = 92 if scale == 1 else 44
    ncols = 2 * hc + 1
    nrows = 2 * BR + ER + 2
    cut_y = top + nrows * u
    bw = FN.band_white(ncols, start=(11 - hc) % FN.RAP)
    red = set()
    for j in range(nrows):
        for c in range(ncols):
            if j < BR:
                band_r = BR - 1 - j
            elif j >= BR + ER + 2:
                band_r = BR - 1 - (j - BR - ER - 2)
            else:
                band_r = None
            if band_r is not None:
                if (band_r, c) not in bw:
                    red.add((j, c))
            elif j in (BR, BR + ER + 1):
                continue
            else:
                y = j - BR - 1
                edge = y in (0, ER - 1) or c in (0, ncols - 1)
                if edge or not _e_white(c - hc, y):
                    red.add((j, c))
    pg = print_outline()
    assert all(_inside((c - hc) * u, cut_y - (j + 0.5) * u, pg) for j, c in red), 'Querstreifen ragt unter der Kapuze hervor'
    return red, u, hc, pg, cut_y


def runs_path(cells, u, hc, cut_y=PRINT_BOTTOM):
    rows = {}
    for j, c in cells:
        rows.setdefault(j, []).append(c)
    d = []
    for j, cs in rows.items():
        cs.sort(); s = p = cs[0]
        for c in cs[1:] + [None]:
            if c is not None and c == p + 1:
                p = c; continue
            x = (s - hc - 0.5) * u; y = cut_y - (j + 1) * u
            d.append(f"M{F(x)} {F(y)}h{F((p - s + 1) * u)}v{F(u)}h{F(-(p - s + 1) * u)}z")
            if c is not None:
                s = p = c
    return "".join(d)


def hood_print(scale=2, mode='flaeche'):
    res = print_cells(scale, mode)
    red, u, hc = res[:3]
    cut_y = res[4] if len(res) > 4 else PRINT_BOTTOM
    return f'<path d="{runs_path(red, u, hc, cut_y)}" style="fill:{RED}"/>'


def print_outline_d():
    return poly(print_outline())


# ---------------------------------------------------------------- Abdruck der echten RL-Kapuze (Weg 1, Ernest 25.10.)
# Vorläufig aus dem Messbogen (14: 30 cm tief, 15: 26 cm breit) und dem Foto vom 25.10.: Die liegende Kapuze
# ist oben am Hals gerade, wird bis zur Mitte etwas breiter und läuft unten in eine Spitze (Ende der Mittelnaht).
# Wird ersetzt, sobald Ernest den Umriss abgepaust hat.
RL_HOOD = [((-100, 0), (-112, 22), (-130, 60), (-130, 110)),
           ((-130, 110), (-130, 175), (-48, 262), (0, 295)),
           ((0, 295), (48, 262), (130, 175), (130, 110)),
           ((130, 110), (130, 60), (112, 22), (100, 0))]


def rl_hood_d():
    s = RL_HOOD
    return f"M{F(s[0][0][0])} {F(s[0][0][1])}" + "".join(
        f"C{F(b[1][0])} {F(b[1][1])} {F(b[2][0])} {F(b[2][1])} {F(b[3][0])} {F(b[3][1])}" for b in s) + "Z"


def rl_hood_poly():
    hp = []
    for b in RL_HOOD:
        hp += _bez(b, 48)
    return hp + [RL_HOOD[-1][3]]


def rl_print_outline(inset=INSET_MM):
    """Umriss rundum inset kleiner. An den oberen Ecken bildet die Linienverschiebung eine kleine Schleife,
    deshalb prüfen die Zellen den Abstand zum Kapuzenrand direkt (_in_abdruck) und nicht diesen Umriss."""
    hp = rl_hood_poly()
    pts = FN._inset(hp, inset)
    return pts if abs(_area(pts)) < abs(_area(hp)) else FN._inset(hp, -inset)


def _dist_to_edges(x, y, pg):
    best = 1e9
    for i in range(len(pg)):
        (x1, y1), (x2, y2) = pg[i], pg[(i + 1) % len(pg)]
        dx, dy = x2 - x1, y2 - y1
        t = max(0.0, min(1.0, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy or 1)))
        best = min(best, math.hypot(x - x1 - t * dx, y - y1 - t * dy))
    return best


def _in_abdruck(x, y, hp, inset=INSET_MM):
    return _inside(x, y, hp) and _dist_to_edges(x, y, hp) >= inset


def _cut_below(pts, cut_y):
    out, n = [], len(pts)
    for i in range(n):
        p, q = pts[i], pts[(i + 1) % n]
        if p[1] <= cut_y:
            out.append(p)
        if (p[1] <= cut_y) != (q[1] <= cut_y):
            f = (cut_y - p[1]) / (q[1] - p[1])
            out.append((p[0] + (q[0] - p[0]) * f, cut_y))
    return out


ABDRUCK = {'unten': 'Band A unten, gerade abgeschnitten', 'oben': 'Band A oben am Hals', 'ohne': 'Ohne Band, nur Muster E'}


def abdruck_cells(scale=2, band='oben', min_band=150.0):
    """Rote Zellen für Weg 1 im echten Kapuzen-Abdruck, Reihen r von oben.
    band='unten': Band A schließt unten gerade ab, darunter fällt die Spitze weg (Schnitt, wo die Fläche noch min_band breit ist)
    band='oben':  Band A läuft oben am Hals entlang, Muster E füllt den Abdruck bis in die Spitze
    band='ohne':  nur Muster E bis in die Spitze
    Muster E immer mit roter Kante aus einer Zellreihe, zwischen Band und Muster eine Reihe frei."""
    u = FN.CELL * scale
    pg = rl_print_outline()
    hp = rl_hood_poly()
    cut = None
    if band == 'unten':
        y = max(p[1] for p in pg) - 0.5
        while True:
            span = _row_span(pg, y)
            if span and span[1] - span[0] >= min_band:
                break
            y -= 1
        cut = y
        pg = _cut_below(pg, y)
    top = max(min(p[1] for p in pg), min(p[1] for p in hp) + INSET_MM)
    bottom = max(p[1] for p in pg)
    half_w = max(abs(p[0]) for p in pg)
    hc = int(half_w / u) + 1
    ncols, nrows = 2 * hc + 1, int((bottom - top) / u)
    BR = FN.BAND_ROWS
    bw = FN.band_white(ncols, start=(11 - hc) % FN.RAP)
    cell_in = {}
    for r in range(nrows):
        cy = top + (r + 0.5) * u
        for c in range(ncols):
            cx = (c - hc) * u
            cell_in[(r, c)] = (cut is None or cy <= cut) and _in_abdruck(cx, cy, hp)
    if band == 'oben':
        band_rows, e_rows = range(0, BR), range(BR + 1, nrows)
    elif band == 'unten':
        band_rows, e_rows = range(nrows - BR, nrows), range(0, nrows - BR - 1)
    else:
        band_rows, e_rows = range(0), range(0, nrows)
    e0 = e_rows.start
    red = set()
    for (r, c), ok in cell_in.items():
        if not ok:
            continue
        if r in band_rows:
            if (r - band_rows.start, c) not in bw:
                red.add((r, c))
        elif r in e_rows:
            edge = any(not cell_in.get((r + dr, c + dc), False) or (r + dr) not in e_rows
                       for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            if edge or not _e_white(c - hc, r - e0):
                red.add((r, c))
    return red, u, hc, top, pg


def _row_span(pg, y):
    xs = []
    for i in range(len(pg)):
        (x1, y1), (x2, y2) = pg[i], pg[(i + 1) % len(pg)]
        if (y1 > y) != (y2 > y):
            xs.append(x1 + (y - y1) * (x2 - x1) / (y2 - y1))
    return (min(xs), max(xs)) if len(xs) >= 2 else None


def abdruck_print(scale=2, band='oben'):
    red, u, hc, top, _ = abdruck_cells(scale, band)
    d = "".join(f"M{F((c - hc - 0.5) * u)} {F(top + r * u)}h{F(u)}v{F(u)}h{F(-u)}z" for r, c in sorted(red))
    return f'<path d="{d}" style="fill:{RED}"/>'


def star_c(cx, cy, w=36):
    return FN.star8_svg(cx, cy, w).replace(FN.REDD, RED).replace(FN.REDL, RED_L)


STAR_RIB = (-200, (RIB_TOP + HEM) / 2)


# ---------------------------------------------------------------- Ansichten
def front_view(variant, uid, carpet_scale=1.0, carpet=True):
    rug = carpet_on_body(variant, uid, carpet_scale) if carpet else ''
    return (f'<g>{sleeve(-1)}{sleeve(1)}{body(True)}{hood_up(True)}{pockets()}'
            f'{rug}{zipper_front()}{cords()}</g>')


def back_view(hood='down', scale=2, mode='flaeche', hidden=False):
    parts = [sleeve(-1), sleeve(1), body(False)]
    if hood == 'up':
        parts.append(hood_print(scale, mode))
        parts.append(f'<path d="M{-NX} 0Q0 16 {NX} 0" style="fill:none;stroke:{LINE};stroke-width:1.2"/>')
        parts.append(hood_up(False))
    else:
        parts.append(hood_down_back())
        if hidden:                                     # verdeckte Druckfläche als Strichlinie
            parts.append(f'<path d="{print_outline_d()}" style="fill:none;stroke:{RED};stroke-width:1.3;stroke-dasharray:6 4"/>')
    parts.append(star_c(*STAR_RIB))
    return "<g>" + "".join(parts) + "</g>"


VB_FULL = (-430, -356, 860, 1056)      # mit stehender Kapuze
VB_DOWN = (-430, -12, 860, 712)        # Kapuze liegt


def svg(inner, vb=VB_FULL, w_px=900):
    h_px = w_px * vb[3] / vb[2]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{F(w_px)}" height="{F(h_px)}" '
            f'viewBox="{" ".join(F(v) for v in vb)}"><rect x="{vb[0]}" y="{vb[1]}" width="{vb[2]}" height="{vb[3]}" style="fill:#ffffff"/>{inner}</svg>')


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    files = {'vorn_oma': svg(front_view('oma', 'fo')), 'hinten_unten': svg(back_view('down', hidden=True), VB_DOWN)}
    for m, sc in MODE_SCALE.items():
        files['hinten_oben_' + m] = svg(back_view('up', sc, m))
    for k, v in files.items():
        open(os.path.join(out, k + '.svg'), 'w').write(v)
    pg = print_outline()
    xs, ys = [p[0] for p in pg], [p[1] for p in pg]
    bottom = [x for x, y in pg if abs(y - PRINT_BOTTOM) < 1e-6]
    print('Druckfläche mm: Breite', round(max(xs) - min(xs)), 'Höhe', round(max(ys) - min(ys)), 'oben', round(min(ys)),
          'Bandbreite unten', round(max(bottom) - min(bottom)))
