# -*- coding: utf-8 -*-
# Maßblätter NVL-TT-01 im Format von Kuzgunlar (Vorlage von Nargiza, 1811-Beispiele, 28.10.2026)
#   Kopf mit Season/Size/Name/Designer, gelber Titel, roter Hinweis, Zeichnung mit roten Maßlinien, „Finished size“.
#   Werte aus techpack.py (POM, Gradierung) und der Druckvorlage v1.9. Ausgabe: v19/kz_spec.html, PDF über kz_spec.mjs.
import base64, io, math, os, subprocess, tempfile
from PIL import Image
import fine as FN
import flats as FL

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
F = FN.F
RED, YEL, NOTE, INK, GRN = "#d6261c", "#f2e41f", "#f3e77f", "#1b2230", "#2e9a4a"
SIZES = ["W30", "W31", "W32", "W33", "W34", "W36", "W38"]
STEP = {"W30": -4, "W31": -3, "W32": -2, "W33": -1, "W34": 0, "W36": 2, "W38": 4}
QTY = {"W30": 8, "W31": 10, "W32": 20, "W33": 14, "W34": 20, "W36": 18, "W38": 10}
# (Nr., Messpunkt, kurz wie messen, W34 cm, Toleranz, Sprung je 1")
POM = [(1, "Waist, half", "top edge of waistband, buttoned, edge to edge", 43.0, 1.0, 1.27),
       (2, "Hip, half", "straight across at the end of the fly (J-stitch)", 52.0, 1.0, 1.27),
       (3, "Thigh, half", "one leg, 2.5 cm below crotch, at right angles to the leg", 29.0, 0.6, 0.6),
       (4, "Knee, half", "one leg, 33 cm below crotch (on the inseam), straight across", 22.5, 0.5, 0.4),
       (5, "Leg opening, half", "at the hem, edge to edge", 21.0, 0.5, 0.3),
       (6, "Front rise", "crotch point to top of waistband along the seam, incl. waistband", 32.0, 0.5, 0.3),
       (7, "Back rise", "crotch point to top of waistband along the seam, incl. waistband", 37.0, 0.6, 0.4),
       (8, "Inseam", "crotch point to hem edge along the inseam, hem included · same in all sizes (L32)", 81.0, 1.0, 0.0),
       (9, "Outseam", "top of waistband to hem along the side seam", 110.0, 1.0, 0.3),
       (10, "Waistband height", "top to bottom edge of waistband", 4.0, 0.2, 0.0),
       (11, "Fly opening", "bottom of waistband to end of J-stitch", 15.0, 0.3, 0.2),
       (12, "Back yoke at centre back", "bottom of waistband to yoke seam, on the centre back seam", 9.5, 0.3, 0.1),
       (13, "Back yoke at side seam", "bottom of waistband to yoke seam, on the side seam", 3.0, 0.3, 0.0),
       (14, "Back pocket to centre back", "centre back seam to inner top corner of back pocket", 3.5, 0.3, 0.0),
       (15, "Back pocket below waistband", "bottom of waistband to top of back pocket, at the inner corner", 8.5, 0.3, 0.0),
       (16, "Front pocket opening, width", "at the bottom of the waistband: side seam to start of opening", 11.0, 0.3, 0.0),
       (17, "Front pocket opening, depth", "along the side seam: bottom of waistband to end of opening", 7.0, 0.3, 0.0),
       (18, "Belt loops, number", "2 front, 2 side back, 1 centre back", 5, None, None),
       (19, "Belt loop length", "visible length, top to bottom", 4.0, 0.2, 0.0),
       (20, "Hem height", "hem edge to hem stitch line, sewn hem", 1.0, 0.2, 0.0)]
P = {n: (name, how, v, tol) for n, name, how, v, tol, _ in POM}


def cm(v):
    return f"{v:g} cm"


def graded(v, step, size):
    return v if step is None else math.floor((v + step * STEP[size]) * 10 + 0.5) / 10


# ---------- Bilder aus der Druckvorlage v1.9 (1:1) als Referenz ----------
DPI = 200; K = DPI / 25.4
tmp = tempfile.mkdtemp()
subprocess.run(["pdftoppm", "-r", str(DPI), "-png", "-f", "2", "-l", "5", os.path.join(ROOT, "pdf", "NVL_Druckvorlage_v19_Jeans.pdf"), os.path.join(tmp, "p")], check=True)
PAGES = {n: Image.open(os.path.join(tmp, f"p-{n}.png")).convert("RGB") for n in (2, 3, 4, 5)}


def crop(page, x0, y0, x1, y1):
    return PAGES[page].crop((int(x0 * K), int(y0 * K), int(x1 * K), int(y1 * K)))


def uri(im):
    b = io.BytesIO(); im.save(b, "PNG")
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()


IMG = {"E": crop(2, 13, 49, 77, 113), "A": crop(2, 40, 146, 197, 267), "B2": crop(3, 24, 61, 186, 213),
       "C": crop(4, 24, 61, 186, 213), "D": crop(5, 13, 55, 95, 128)}
from PIL import ImageDraw                              # deutsche Beschriftung links neben Band A überdecken (wie im Tech Pack)
ImageDraw.Draw(IMG["A"]).rectangle((0, int(14 * K), int(68 * K), int(44 * K)), fill="white")


# ---------- SVG-Bausteine: rote Maßlinien ----------
class Dim:
    """Sammelt rote Maßlinien für eine Zeichnung. s = Strichstärke, fs = Schriftgröße, beides in Zeichnungseinheiten (mm)."""
    n = 0

    def __init__(self, s, fs):
        Dim.n += 1
        self.id, self.s, self.fs, self.o = f"ar{Dim.n}", s, fs, []

    def defs(self):
        a = self.s * 5
        return (f'<defs><marker id="{self.id}" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="{F(a)}" markerHeight="{F(a)}" orient="auto-start-reverse">'
                f'<path d="M0 0L10 5L0 10Z" fill="{RED}"></path></marker></defs>')

    def line(self, x1, y1, x2, y2):
        self.o.append(f'<path d="M{F(x1)} {F(y1)}L{F(x2)} {F(y2)}" style="stroke: {RED}; stroke-width: {F(self.s)}; fill: none" marker-start="url(#{self.id})" marker-end="url(#{self.id})"></path>')

    def path(self, d):
        self.o.append(f'<path d="{d}" style="stroke: {RED}; stroke-width: {F(self.s)}; fill: none" marker-start="url(#{self.id})" marker-end="url(#{self.id})"></path>')

    def ext(self, x1, y1, x2, y2):
        self.o.append(f'<path d="M{F(x1)} {F(y1)}L{F(x2)} {F(y2)}" style="stroke: {RED}; stroke-width: {F(self.s * .6)}; stroke-dasharray: {F(self.s * 3)} {F(self.s * 2)}"></path>')

    def text(self, x, y, t, anchor="middle", size=1.0, weight=700, col=RED, rot=0):
        fs = self.fs * size
        tr = f' transform="rotate({F(rot)} {F(x)} {F(y)})"' if rot else ""
        self.o.append(f'<text x="{F(x)}" y="{F(y + fs * .35)}"{tr} style="font: {weight} {F(fs)}px \'Roboto Condensed\', Arial, sans-serif; fill: {col}; text-anchor: {anchor}; '
                      f'paint-order: stroke; stroke: #fff; stroke-width: {F(fs * .3)}px; stroke-linejoin: round">{t}</text>')

    def ann(self, x, y, n, t):
        """Nummer im roten Kreis plus Maß, zusammen mittig auf (x, y)."""
        r = self.fs * .62; w = 2 * r + self.fs * .3 + len(t) * self.fs * .46
        x0 = x - w / 2
        if n is not None:
            self.o.append(f'<circle cx="{F(x0 + r)}" cy="{F(y)}" r="{F(r)}" style="fill: {RED}; stroke: #fff; stroke-width: {F(self.fs * .12)}"></circle>'
                          f'<text x="{F(x0 + r)}" y="{F(y + self.fs * .3)}" style="font: 700 {F(self.fs * .8)}px \'Roboto Condensed\', Arial, sans-serif; fill: #fff; text-anchor: middle">{n}</text>')
            self.text(x0 + 2 * r + self.fs * .3, y, t, "start")
        else:
            self.text(x, y, t)

    def ring(self, x, y, r, label=None):
        self.o.append(f'<circle cx="{F(x)}" cy="{F(y)}" r="{F(r)}" style="fill: none; stroke: {RED}; stroke-width: {F(self.s * 1.3)}; stroke-dasharray: {F(self.s * 4)} {F(self.s * 2.5)}"></circle>')
        if label:
            self.text(x + r * .75, y - r * .9, label, "start", 1.2)

    def svg(self, vb, parts, style=""):
        return f'<svg viewBox="{vb}" style="{style}">{self.defs()}{"".join(parts)}{"".join(self.o)}</svg>'


def flat(view):
    """Flat vorn oder hinten ohne die braunen Buchstaben-Markierungen."""
    return [p for p in (FL.front() if view == "front" else FL.back()) if 'r="17"' not in p]


def inseam_x(y):
    pts = FL.INSEAM
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if y0 <= y <= y1:
            return x0 + (x1 - x0) * (y - y0) / (y1 - y0)
    return pts[-1][0]


SX = FL.side_x
WB = FL.WB


# ================= Seite: Maße vorn =================
def svg_front_main():
    d = Dim(2.6, 27)
    d.ext(-215, -6, -215, -78); d.ext(215, -6, 215, -78); d.line(-215, -60, 215, -60); d.ann(0, -96, 1, cm(43))
    d.line(-SX(190), 190, SX(190), 190); d.ann(-140, 166, 2, cm(52))
    y = 315; d.line(-SX(y), y, -inseam_x(y), y); d.ann(-140, y - 24, 3, cm(29))
    y = 620; d.line(-SX(y), y, -inseam_x(y), y); d.ann(-140, y - 24, 4, cm(22.5))
    d.ext(-242, 1104, -242, 1160); d.ext(-32, 1104, -32, 1160); d.line(-242, 1145, -32, 1145); d.ann(-137, 1185, 5, cm(21))
    d.line(0, 2, 0, 288); d.ann(96, 252, 6, cm(32))
    d.line(18, 298, 50, 1094); d.ann(110, 760, 8, cm(81))
    d.ext(219, 0, 350, 0); d.ext(246, 1100, 350, 1100); d.line(336, 2, 336, 1098); d.ann(336, 560, 9, cm(110))
    return d.svg("-400 -135 840 1350", flat("front"), "height:100%;width:auto")


def svg_front_detail():
    d = Dim(1.3, 13.5)
    d.ext(-215, 0, -268, 0); d.ext(-221, 40, -268, 40); d.line(-258, 1, -258, 39); d.ann(-296, 20, 10, cm(4))
    d.ext(38, 190, 80, 190); d.line(66, 41, 66, 189); d.ann(66, 118, 11, cm(15))
    d.ext(111, 40, 111, -52); d.ext(221, 40, 221, -52); d.line(112, -42, 220, -42); d.ann(166, -60, 16, cm(11))
    xs = SX(110); d.ext(221, 40, 272, 40); d.ext(xs, 110, 272, 110); d.line(262, 41, 262, 109); d.ann(300, 75, 17, cm(7))
    d.ext(-92, -4, -60, -4); d.ext(-92, 42, -60, 42); d.line(-66, -3, -66, 41); d.ann(-66, -30, 19, cm(4))
    return d.svg("-332 -82 664 300", flat("front"), "width:100%")


def svg_hem():
    d = Dim(.9, 7)
    d.ext(-205, 1090, -238, 1090); d.ext(-205, 1100, -238, 1100); d.line(-230, 1090.5, -230, 1099.5); d.ann(-190, 1080, 20, "1 cm")
    d.text(-192, 1113, "chain stitch, copper-gold", "middle", .8, 400, INK)
    return d.svg("-262 1060 140 62", flat("front"), "width:100%")


# ================= Seite: Maße hinten =================
def svg_back_main():
    d = Dim(3.4, 46)
    d.line(0, 2, 0, 288); d.ann(-130, 250, 7, cm(37))
    for x in (-180, 0, 180):
        d.ann(x, -46, 18, "")
    d.ring(90, 36, 70)
    return d.svg("-410 -135 820 1350", flat("back"), "height:100%;width:auto")


def svg_back_detail():
    d = Dim(1.3, 13.5)
    d.line(0, 41, 0, 134); d.ann(0, 164, 12, cm(9.5))
    s40, s70 = SX(40), SX(70)
    d.ext(s40, 40, 270, 40); d.ext(s70, 70, 270, 70); d.line(258, 41, 258, 69); d.ann(296, 55, 13, cm(3))
    d.ext(35, 125, 35, 100); d.line(1, 110, 34, 110); d.ann(92, 96, 14, cm(3.5))
    d.ext(-35, 125, -62, 125); d.line(-52, 41, -52, 124); d.ann(-102, 82, 15, cm(8.5))
    return d.svg("-332 -30 664 230", flat("back"), "width:100%")


# ================= Detail: Gesäßtasche (B2 links, C rechts) =================
H_IN = math.sqrt(125 ** 2 - 15 ** 2); TIP = math.sqrt(70 ** 2 - 65 ** 2); DROP = H_IN - math.sqrt(120 ** 2 - 15 ** 2)


def pocket_pts(left):
    """Taschenumriss in Taschen-mm; left = linke Gesäßtasche vom Träger aus (in der Rückansicht links, innen = rechts im Bild)."""
    if left:
        return [(0, DROP), (160, 0), (145, H_IN), (80, H_IN + TIP), (15, H_IN)]
    return [(0, 0), (160, DROP), (145, H_IN), (80, H_IN + TIP), (15, H_IN)]


def pocket_svg(left):
    d = Dim(1.0, 9)
    pts = pocket_pts(left)
    poly = lambda q, z=True: "M" + "L".join(f"{F(x)} {F(y)}" for x, y in q) + ("Z" if z else "")
    parts = [f'<path d="{poly(pts)}" style="fill: #2f4a6e; stroke: {INK}; stroke-width: 1.2"></path>',
             f'<path d="{poly([(x + (4 if x < 80 else -4), y + (4 if y < 10 else -4)) for x, y in pts])}" style="fill: none; stroke: #c9976f; stroke-width: .7; stroke-dasharray: 2.5 1.6"></path>']
    top_mid = DROP / 2
    cy = top_mid + 45
    if left:
        parts.append(f'<rect x="56" y="{F(cy - 1.5)}" width="48" height="3" rx="1.5" style="fill: #e0322a"></rect>')
        for ex, rot in ((-7, -18), (0, 0), (7, 18)):
            parts.append(f'<ellipse cx="{F(80 + ex)}" cy="{F(cy - 9)}" rx="2.6" ry="6.5" transform="rotate({rot} {F(80 + ex)} {F(cy - 2)})" style="fill: #d8ae47; stroke: #997b38; stroke-width: .5"></ellipse>')
        lens = [19, 25, 22, 30, 27, 21, 29, 18, 24]
        for i, L in enumerate(lens):
            x = 72 + i * 2
            parts.append(f'<path d="M{F(x)} {F(cy + 1.5)}v{F(L)}" style="stroke: #dec05f; stroke-width: .9; stroke-linecap: round"></path>')
    else:
        parts.append(FN.star8_svg(80, cy, 36.0, 1.0))
    # Maße Tasche
    (x0, y0), (x1, y1) = pts[0], pts[1]
    d.ext(x0, y0, x0, -14); d.ext(x1, y1, x1, -14); d.line(x0, -10, x1, -10); d.ann(80, -18, None, "16 cm")
    d.line(15.5, H_IN, 144.5, H_IN)
    d.ann(80, H_IN - 7, None, "13 cm")
    inner, outer = ((pts[1], pts[2]), (pts[0], pts[4])) if left else ((pts[0], pts[4]), (pts[1], pts[2]))
    for (a, b), t in ((inner, "12.5 cm inner side"), (outer, "12 cm outer side")):
        side = 1 if a[0] > 80 else -1                                         # rechts oder links im Bild
        ox = 5 * side
        d.line(a[0] + ox, a[1], b[0] + ox, b[1])
        mx, my = (a[0] + b[0]) / 2 + 14 * side, (a[1] + b[1]) / 2
        d.text(mx, my, t, "middle", 1, 700, RED, math.degrees(math.atan2(-(b[1] - a[1]), -(b[0] - a[0]))) if side > 0 else math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) - 180)
    d.line(15 - 4, H_IN + 3, 80 - 4, H_IN + TIP + 3)
    d.ann(36, H_IN + TIP + 6, None, "7 cm")
    d.line(80 + 4, H_IN + TIP + 3, 145 + 4, H_IN + 3)
    d.ann(124, H_IN + TIP + 6, None, "7 cm")
    xr = 196 if left else -36
    d.ext(160 if left else 0, 0, xr, 0); d.ext(80, H_IN + TIP, xr, H_IN + TIP); d.line(xr - (6 if left else -6), 0, xr - (6 if left else -6), H_IN + TIP)
    d.ann(xr + (6 if left else -6), 75, None, "15 cm")
    # Motiv
    if left:
        d.ext(104, cy, 116, cy); d.line(112, top_mid + .5, 112, cy - .5); d.ann(131, top_mid + 22, None, "4.5 cm")
        d.ext(56, cy - 1.5, 56, cy - 25); d.ext(104, cy - 1.5, 104, cy - 25); d.line(56.5, cy - 21, 103.5, cy - 21)
        d.ann(76, cy - 29, None, "band 4.8 × 0.3 cm")
        d.ext(71, cy + 32, 71, cy + 42); d.ext(89, cy + 32, 89, cy + 42); d.line(71.5, cy + 39, 88.5, cy + 39); d.ann(80, cy + 48, None, "1.6 cm · 9 threads 1.8–3.0 cm")
    else:
        d.ext(62, cy, 44, cy); d.line(48, top_mid + .5, 48, cy - .5); d.ann(30, top_mid + 22, None, "4.5 cm")
        d.ext(62, cy, 62, cy + 26); d.ext(98, cy, 98, cy + 26); d.line(62.5, cy + 23, 97.5, cy + 23); d.ann(80, cy + 31, None, "3.6 cm")
        d.ext(98, cy - 18, 112, cy - 18); d.ext(98, cy + 18, 112, cy + 18); d.line(108, cy - 17.5, 108, cy + 17.5); d.ann(124, cy, None, "3.6 cm")
    return d.svg("-62 -32 284 200", parts, "width:100%")


# ================= Detail: Band A, Münztasche E, Patch D =================
def band_geometry():
    xs40 = SX(WB); ys = WB + 70; xs = SX(ys)
    p0, c1, c2, p1 = (-(xs40 - 110), WB), (-(xs40 - 106), WB + 46), (-(xs40 - 50), ys - 2), (-xs, ys)
    crv = FL.cubic(p0, c1, c2, p1)
    band = FL.offset(crv, -23)
    return crv, band, xs40


def svg_band():
    d = Dim(1.0, 7.5)
    crv, band, xs40 = band_geometry()
    poly = lambda q: "M" + "L".join(f"{F(x)} {F(y)}" for x, y in q)
    parts = [f'<path d="M{F(-xs40 - 6)} 0H-60V{F(WB)}H{F(-xs40)}Z" style="fill: #eef1f6; stroke: {INK}; stroke-width: .9"></path>',
             f'<path d="M{F(-xs40)} {F(WB)}L{F(-SX(130))} 130" style="stroke: {INK}; stroke-width: 1.2"></path>',
             f'<path d="{poly(crv + band[::-1])}Z" style="fill: #e0322a; stroke: {INK}; stroke-width: .8"></path>']
    for i in range(0, len(crv), 6):                                   # Kreuzstich-Andeutung
        x, y = (crv[i][0] + band[i][0]) / 2, (crv[i][1] + band[i][1]) / 2
        parts.append(f'<path d="M{F(x - 2)} {F(y - 2)}l4 4m0 -4l-4 4" style="stroke: #fff; stroke-width: .7"></path>')
    d.s, d.fs = 1.1, 9
    d.line(crv[30][0], crv[30][1], band[30][0], band[30][1]); d.ann(band[30][0] + 20, band[30][1] - 4, None, "2.3 cm")
    d.o.append(f'<path d="M{F(crv[22][0])} {F(crv[22][1])}L-190 60" style="stroke: {RED}; stroke-width: .7"></path>')
    d.ann(-205, 54, None, "inner edge 17.5 cm")
    d.text(-205, 64, "on the pocket opening", "middle", .85, 400)
    d.o.append(f'<path d="M{F(band[44][0])} {F(band[44][1])}L-170 150" style="stroke: {RED}; stroke-width: .7"></path>')
    d.ann(-170, 156, None, "outer edge 20.7 cm")
    d.text(-150, -10, "waistband", "middle", .9, 400, INK); d.text(-SX(120) - 6, 128, "side seam", "end", .9, 400, INK)
    d.text(-92, 150, "front panel", "middle", .9, 400, INK)
    return d.svg("-292 -24 240 192", parts, "width:100%")


def svg_coin():
    d = Dim(.5, 4.2)
    parts = [f'<rect x="0" y="0" width="62" height="62" style="fill: #2f4a6e; stroke: {INK}; stroke-width: .6"></rect>',
             f'<rect x="1" y="1" width="60" height="60" style="fill: #e0322a"></rect>']
    for r in range(0, 45, 4):
        for c in range(0, 45, 4):
            if (r // 4 + c // 4) % 2 == 0:
                x, y = 1 + c * 60 / 45, 1 + r * 60 / 45
                parts.append(f'<path d="M{F(x)} {F(y)}l1.3 1.3m0 -1.3l-1.3 1.3" style="stroke: #fff; stroke-width: .45"></path>')
    for x in (4, 58):
        parts.append(f'<circle cx="{x}" cy="4" r="2.6" style="fill: #a8643a; stroke: #6f3d1f; stroke-width: .4"></circle>')
    d.ext(0, 0, 0, -9); d.ext(62, 0, 62, -9); d.line(0, -6, 62, -6); d.ann(31, -11, None, "6.2 cm")
    d.ext(62, 0, 72, 0); d.ext(62, 62, 72, 62); d.line(69, 0, 69, 62); d.ann(80, 31, None, "6.2 cm")
    d.ext(1, 61, 1, 70); d.ext(61, 61, 61, 70); d.line(1, 67, 61, 67); d.ann(31, 72, None, "embroidery 6.0 × 6.0 cm")
    d.ann(31, 78, None, "45 × 45 cross-stitches, cell 1.33 mm")
    d.text(4, 11, "rivet", "middle", .7, 400, "#fff"); d.text(58, 11, "rivet", "middle", .7, 400, "#fff")
    return d.svg("-12 -18 104 100", parts, "width:100%")


def svg_patch():
    d = Dim(.8, 6.2)
    parts = [f'<path d="{FN.patch_outline(0, 0, 80, 71, 5.5)}" style="fill: #e8dcc4; stroke: {INK}; stroke-width: .9"></path>']
    for x in (7, 73):
        for y in (12.5, 58.5):
            parts.append(f'<circle cx="{x}" cy="{y}" r="5" style="fill: none; stroke: #a8643a; stroke-width: .7; stroke-dasharray: 1.6 1"></circle>')
    parts.append(f'<path d="M25 0.6H55M25 70.4H55" style="stroke: #7a4b2a; stroke-width: 1.6"></path>')
    d.ext(0, 5.5, 0, -10); d.ext(80, 5.5, 80, -10); d.line(0, -7, 80, -7); d.ann(40, -13, None, "8 cm")
    d.ext(40, 0, 100, 0); d.ext(40, 71, 100, 71); d.line(96, 0, 96, 71); d.ann(106, 35.5, None, "7.1 cm")
    d.ext(0, 5.5, -16, 5.5); d.ext(0, 65.5, -16, 65.5); d.line(-12, 5.5, -12, 65.5); d.ann(-22, 35.5, None, "6 cm")
    d.ext(7, 58.5, 7, 84); d.ext(73, 58.5, 73, 84); d.line(7, 80, 73, 80); d.ann(40, 86, None, "snap grid 6.6 cm")
    d.ext(73, 12.5, 88, 12.5); d.ext(73, 58.5, 88, 58.5); d.line(84, 12.5, 84, 58.5); d.ann(84, 35.5, None, "4.6")
    d.line(0, 30, 7, 30); d.ann(3.5, 25, None, "0.7")
    d.line(25, 4, 55, 4); d.ann(40, 9.5, None, "joined 3 cm")
    d.text(40, 40, "TREE OF LIFE", "middle", .9, 700, "#7a4b2a")
    return d.svg("-36 -22 154 116", parts, "width:100%")


# ================= Lage-Skizzen (klein) =================
def loc(view, x, y, r, label):
    d = Dim(3, 40)
    d.ring(x, y, r, label)
    return d.svg("-300 -60 600 1180", flat(view), "height:100%;width:auto")


# ================= Seitenrahmen =================
def header(title):
    sz = "".join(f'<td class="{"y" if s == "W34" else ""}">{s}</td>' for s in SIZES)
    return f"""<div class="logo">N O V A L I F E<small>BERLIN</small></div>
<table class="hd"><colgroup><col style="width:40mm">{"".join('<col>' for _ in SIZES)}</colgroup><tr><td class="l">Season/Сезон:</td><td class="v" colspan="3">TIME TRAVEL 2027</td><td class="l" colspan="2">Name/Артикул:</td><td class="v" colspan="2">NVL-TT-01 JEANS</td></tr>
<tr><td class="l">Size/Размер:</td>{sz}</tr>
<tr><td class="l">Designer/Дизайнер:</td><td class="v" colspan="3">Ernest Veskimäe</td><td class="v" colspan="4">KUZGUNLAR</td></tr></table>
<div class="ttl"><span>{title}</span></div>"""


def note(t):
    return f'<div class="nt"><b>!</b><div>{t}</div></div>'


def page(n, title, body):
    return f'<section class="pg">{header(title)}{body}<div class="ft"><span>NVL-TT-01 · measurements v1.1 · 30 Oct 2026 · sample size W34</span><span>page {n} of 9</span></div></section>'


def legend(nums):
    rows = "".join(f'<tr><td class="no"><i>{n}</i></td><td><b>{P[n][0]}</b><br><span>{P[n][1]}</span></td>'
                   f'<td class="val">{P[n][2] if P[n][3] is None else cm(P[n][2])}</td><td class="tol">{"" if P[n][3] is None else "± " + f"{P[n][3]:g}"}</td></tr>' for n in nums)
    return f'<table class="lg"><tr><th></th><th>Point of measure</th><th>W34</th><th>Tol.</th></tr>{rows}</table>'


def ref(key, cap):
    return f'<div class="ref"><img src="{uri(IMG[key])}" alt="{key}"><span>{cap}</span><em>REFERENCE</em></div>'


pages = []
pages.append(page(1, "MEASUREMENTS · FRONT", note("Measure the finished jeans AFTER the wash, laid flat, buttoned, not stretched. Widths 1–5 are HALF measurements (edge to edge, not doubled). Lengths follow the seam.")
                  + f'<div class="two"><div class="dw">{svg_front_main()}</div><div>{legend([1, 2, 3, 4, 5, 6, 8, 9])}<p class="fs">FINISHED SIZE<br><small>(after wash, size W34)</small></p></div></div>'))
pages.append(page(2, "FRONT DETAILS", note("Same in all sizes: waistband 4 cm, front pocket opening 11 × 7 cm, belt loops 4 cm, hem 1 cm. Fly opening grows 0.2 cm per size.")
                  + f'<div class="dw w">{svg_front_detail()}</div><div class="two b"><div>{legend([10, 11, 16, 17, 19, 20])}</div><div><div class="inset"><h4>HEM</h4>{svg_hem()}</div><p class="fs">FINISHED SIZE<br><small>(after wash, size W34)</small></p></div></div>'))
pages.append(page(3, "MEASUREMENTS · BACK", note("Back pockets, yoke at the side seam and back pocket position are the same in all sizes. Patch D: see page 9.")
                  + f'<div class="two bk"><div class="dw">{svg_back_main()}</div><div>{legend([7, 12, 13, 14, 15, 18])}<p class="fs">FINISHED SIZE<br><small>(after wash, size W34)</small></p></div></div>'
                  f'<div class="inset"><h4>UPPER BACK</h4>{svg_back_detail()}</div>'))

rows = ""
for n, name, how, v, tol, step in POM:
    cells = "".join(f'<td class="{"y" if s == "W34" else ""}">{graded(v, step, s):g}</td>' for s in SIZES)
    rows += f'<tr><td class="no"><i>{n}</i></td><td class="nm">{name}</td><td>{"" if tol is None else "± " + f"{tol:g}"}</td><td>{"–" if not step else "+" + f"{step:g}"}</td>{cells}</tr>'
qty = "".join(f'<td class="{"y" if s == "W34" else ""}">{QTY[s]}</td>' for s in SIZES)
pages.append(page(4, "SIZE CHART W30–W38", note("Sample size W34 (yellow). Honest sizes: the size label is the measured waist in inches. One inseam for all sizes: 81 cm (L32). Please check the grading against your block and comment before the proto.")
                  + f'<table class="sc"><tr><th></th><th>Point of measure (cm)</th><th>Tol.</th><th>Grade / 1"</th>{"".join(f"<th class={chr(34)}{"y" if s == "W34" else ""}{chr(34)}>{s}</th>" for s in SIZES)}</tr>{rows}'
                  f'<tr class="q"><td></td><td class="nm">Quantity (estimate, final in February)</td><td></td><td></td>{qty}</tr></table>'
                  '<p class="sm">Full waist in cm: W30 75.8 · W31 78.4 · W32 81.0 · W33 83.4 · W34 86.0 · W36 91.0 · W38 96.2. Plus 3 spare pairs without number: W32, W34, W36.</p>'))

crv, band, xs40 = band_geometry()
m = band[len(band) // 2]
def detail(n, title, nt, drawing, spec, key, cap, locsvg, fs="FINISHED SIZE<br><small>(after wash)</small>"):
    return page(n, title, note(nt) + f'<div class="dt"><div class="dw dd">{drawing}</div>{ref(key, cap)}'
                f'<div class="col"><p class="fs">{fs}</p><p class="sp">{spec}</p></div><div class="loc"><h4>LOCATION</h4>{locsvg}</div></div>')


pages.append(detail(5, "FRONT POCKET BAND · A", "Wearer's RIGHT front pocket (the one with the coin pocket). Cross-stitch on the cut front panel BEFORE sewing. The inner edge of the band sits exactly on the pocket opening, from the waistband to the side seam.",
                    svg_band(), "17 cross-stitch rows · cell 1.33 mm · repeat 16 stitches<br>Bright red 18-1662 TCX and white 11-0602 TCX<br>About 12,000 stitches",
                    "A", "Artwork 1:1, annex page 1", loc("front", -150, 80, 75, "A")))
pages.append(detail(6, "COIN POCKET · E", "The WHOLE coin pocket is embroidered. Top flush with the coin pocket seam, centred between side seam and pocket rivet. Embroider the panel before sewing. Also embroider the lower inner corner that runs under the front panel, so no plain edge shows.",
                    svg_coin(), "Cross-stitch, 45 × 45 cells of 1.33 mm<br>Bright red 18-1662 TCX and white 11-0602 TCX<br>About 10,500 stitches · rivets 9 mm at both top corners",
                    "E", "Artwork 1:1, annex page 1", loc("front", -190, 82, 60, "E")))
pages.append(detail(7, "LEFT BACK POCKET · B2", "Wearer's LEFT back pocket. Band and wheat ears embroidered on the pocket BEFORE sewing, no white. The 9 gold threads are set by hand AFTER the wash, knotted inside the pocket, through the pocket only.",
                    pocket_svg(True), "Band: satin, bright red 18-1662 TCX, round ends (5.1 cm with ends)<br>Ears: 1.2 cm each, gold 14-0952 TCX and dark gold 18-0835 TCX<br>"
                    "Gold threads 13-0739 TCX, non-metallic, 3-ply, about 1 mm. Visible lengths left to right: 1.9 · 2.5 · 2.2 · 3.0 · 2.7 · 2.1 · 2.9 · 1.8 · 2.4 cm, about 2 mm apart",
                    "B2", "Artwork 1:1, annex page 2", loc("back", -115, 150, 90, "B2")))
pages.append(detail(8, "RIGHT BACK POCKET · C", "Wearer's RIGHT back pocket. Eight-point star centred, its centre at the SAME HEIGHT as the B2 band on the left pocket (4.5 cm below the pocket top edge). 8 rhombi, 1 mm gaps (denim shows through).",
                    pocket_svg(False), "Satin stitch across each rhombus, solid bright red 18-1662 TCX<br>Star 3.6 × 3.6 cm · about 2,500 stitches<br>Same pocket shape as B2",
                    "C", "Artwork 1:1, annex page 3", loc("back", 115, 150, 90, "C")))
pages.append(detail(9, "BACK PATCH · D", "Back RIGHT (as worn). Top of the patch flush with the top of the waistband, centred between centre back loop and right back loop. Two layers: tree in front, back panel behind, joined only in the middle 3 cm at top and bottom. 4 snaps HIDDEN behind, plain caps without letters. A belt up to 4 cm runs through.",
                    svg_patch(), "Embroidery on pre-shrunk natural linen, max. 4 colours: dark brown 19-1432 TCX, copper-gold 17-1340 TCX, gold 14-0952 TCX, bright red 18-1662 TCX<br>"
                    "Snaps: ring-spring 10 mm, antique copper, cap and socket on the back panel, stud on the jeans with 2 × 2 cm reinforcement inside<br>Stiff interlining in the patch",
                    "D", "Embroidery artwork. The snaps in this picture are NOT visible on the real patch: they sit hidden behind.", loc("back", 90, 36, 80, "D"), "FINISHED SIZE"))

CSS = """@page{size:210mm 297mm;margin:0}*{box-sizing:border-box}
html,body{margin:0;padding:0;font-family:'Roboto Condensed',Arial,sans-serif;color:#1b2230;font-size:9.5pt;line-height:1.3}
.pg{width:210mm;height:297mm;padding:7mm;break-after:page;display:flex;flex-direction:column}
.pg>*{flex:none}
section.pg{outline:.5mm solid #1b2230;outline-offset:-4mm}
.logo{text-align:center;color:#9a3a24;font:700 17pt 'Roboto Condensed',Arial;letter-spacing:.25em;margin:1mm 0 2mm}.logo small{display:block;font-size:7pt;letter-spacing:.5em;margin-top:.3mm}
table.hd{width:100%;border-collapse:collapse;font-size:11pt;table-layout:fixed}table.hd td{border:.35mm solid #1b2230;padding:1mm 2mm;background:#ece6ef;text-align:center}
table.hd td.l{text-align:left;width:40mm}table.hd td.v{color:#c0392b}table.hd td.y{background:#f0e6a0;color:#c0392b}
.ttl{text-align:center;margin:4mm 0 3mm}.ttl span{display:inline-block;background:#f2e41f;color:#d6261c;font:700 20pt 'Roboto Condensed',Arial;padding:1mm 10mm}
.nt{display:flex;gap:3mm;align-items:center;margin:0 6mm 3mm}.nt b{color:#d6261c;font:900 38pt 'Roboto Condensed',Arial;line-height:1}
.nt div{flex:1;border:.7mm solid #d6261c;background:#f3e77f;color:#d6261c;font:700 11.5pt 'Roboto Condensed',Arial;padding:2mm 3mm;line-height:1.25}
.two{display:grid;grid-template-columns:1fr 1fr;gap:4mm;flex:1 1 auto;min-height:0}.two.b{flex:1 1 auto}.two.bk{flex:none;height:112mm}.two.bk .dw svg{height:112mm !important}
.dt{display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:auto 1fr;gap:4mm;flex:1 1 auto;min-height:0}.dd svg{width:100%}
.dt .loc svg{max-height:88mm}.dt .col{justify-content:flex-start}
.dw{display:flex;justify-content:center;min-height:0}.dw svg{max-height:100%}.dw.w{flex:none}.dw.sm2{flex:none}
.col{display:flex;flex-direction:column;gap:3mm;min-height:0}
table.lg{width:100%;border-collapse:collapse;font-size:9pt}table.lg th{text-align:left;color:#d6261c;font-size:8pt;text-transform:uppercase;border-bottom:.4mm solid #d6261c;padding:1mm}
table.lg td{border-bottom:.2mm solid #d8dbe2;padding:1.2mm 1mm;vertical-align:top}table.lg td span{color:#566076;font-size:8pt}
td.no i{display:inline-block;width:5.5mm;height:5.5mm;border-radius:50%;background:#d6261c;color:#fff;font-style:normal;font-weight:700;text-align:center;line-height:5.5mm;font-size:8.5pt}
td.val{color:#d6261c;font-weight:700;white-space:nowrap;font-size:11pt}td.tol{white-space:nowrap;color:#566076}
.fs{color:#d6261c;font:700 15pt 'Roboto Condensed',Arial;text-align:right;margin:3mm 0 0;line-height:1.05}.fs small{font-size:11pt;font-weight:400}
.inset{border:.3mm solid #c8ccd4;padding:2mm;margin-top:3mm}.inset h4,.loc h4{margin:0 0 1mm;color:#d6261c;font:700 13pt 'Roboto Condensed',Arial}
table.sc{width:100%;border-collapse:collapse;font-size:10pt;margin-top:1mm}table.sc th{background:#ece6ef;border:.3mm solid #1b2230;padding:1mm;font-size:9pt}
table.sc td{border:.3mm solid #1b2230;padding:.9mm 1.2mm;text-align:center}table.sc td.nm{text-align:left}table.sc .y{background:#f0e6a0;color:#c0392b;font-weight:700}
table.sc tr.q td{font-weight:700}.sm{font-size:9pt;color:#566076;margin:2mm 0 0}
.ref{border:.8mm solid #2e9a4a;padding:2mm;display:flex;flex-direction:column;align-items:center;gap:1mm;position:relative}
.ref{align-self:start}.ref img{max-width:100%;max-height:70mm}.ref span{font-size:8.5pt;color:#566076;text-align:center}.ref em{position:absolute;right:2mm;top:1mm;color:#2e9a4a;font:700 12pt 'Roboto Condensed',Arial;font-style:normal}
.loc{min-height:0;display:flex;flex-direction:column}.loc svg{height:88mm;align-self:center}
.sp{font-size:10.5pt;margin:2mm 0 0;background:#f6f6f8;padding:2.5mm 3mm;border-left:.8mm solid #d6261c;line-height:1.45}
.ft{margin-top:auto;display:flex;justify-content:space-between;font-size:7.5pt;color:#6b7280;padding-top:2mm}"""

FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700;900&display=swap">'
open(os.path.join(HERE, "v19", "kz_spec.html"), "w").write(f'<!doctype html><html><head><meta charset="utf-8">{FONT}<style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
print("ok", len(pages))
