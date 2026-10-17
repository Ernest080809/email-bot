# -*- coding: utf-8 -*-
# Druckvorlage 1:1 · Design v1.9 (17.10.2026) · Jeans · Maße aus Papiertest 3 an der Eightyfive
#   Münztasche E bleibt 62 x 62 mm wie v1.8 · Band A Innenkante 175 mm · Knopf 20 mm · Patch D 80 x 71 mm
#   Gesäßtaschen oben 160, unten 130, Seiten innen 125 / außen 120, Spitze je 70 mm
#   1 Übersicht · 2 vorn A, E, Knopf, Nieten · 3 hinten links B2 · 4 hinten rechts C · 5 Patch D
import base64, bisect, io, contextlib, math, os
with contextlib.redirect_stdout(io.StringIO()):
    import build as B
    import build15 as N15
    import v16 as V16
import fine as FN
from PIL import Image

F = FN.F
WHITE = FN.WHITE; REDD = FN.REDD; REDL = FN.REDL; WHT2 = FN.WHT2; RED = FN.RED
INK = "#1d2330"; GREY = "#8a8f99"; SUB = "#353a46"; DEN = "#2f4a6e"; GUIDE = "#9aa1ad"
COP, COPD, COPL = "#a8643a", "#6f3d1f", "#d39a6c"
FONT = "font-family: Helvetica, Arial, sans-serif"
PAGES = 5
HERE = os.path.dirname(os.path.abspath(__file__))
SKIZZEN = os.path.join(HERE, "..", "rev6", "skizzen")
OUT = os.path.join(HERE, "v19")
os.makedirs(OUT, exist_ok=True)

# ---- Maße v1.9
COIN_W = COIN_H = N15.COIN_MM        # Münztasche 62 x 62 wie v1.8 (Entscheidung 17.10.: nicht größer)
COIN_C = COIN_R = N15.COIN_N         # 45 x 45 Kreuzstiche, 60 x 60 mm
BAND_K = 0.944                       # Kurve skaliert: Innenkante 175 mm (vorher 186)
BUTTON_D = 20.0                      # Knopf, Standardgröße 20 mm (Ligne 32)
PATCH_W, PATCH_H = 80.0, 71.0        # Patch D, vorher 76 x 67
POCKET_TOP, POCKET_BOT = 160.0, 130.0
SIDE_IN, SIDE_OUT, TIP_EDGE = 125.0, 120.0, 70.0
MOTIF_C = (80.0, 47.0)               # Mitte von B2-Band und Achtstern in Taschen-mm


def T(x, y, s, size=3.4, w=400, col=INK, anchor="start"):
    return f'<text x="{F(x)}" y="{F(y)}" style="{FONT}; font-size: {F(size)}px; font-weight: {w}; fill: {col}; text-anchor: {anchor}">{s}</text>'


def cut(d):
    return f'<path d="{d}" style="fill: none; stroke: {INK}; stroke-width: 0.25px; stroke-dasharray: 1.6 1.2"></path>'


def checkline(y):
    return (f'<path d="M55 {F(y)}H155M55 {F(y-2.5)}V{F(y+2.5)}M155 {F(y-2.5)}V{F(y+2.5)}" style="fill: none; stroke: {INK}; stroke-width: 0.35px"></path>'
            + T(105, y - 3.4, "Kontrolle: diese Linie muss genau 100 mm lang sein", 2.8, 700, anchor="middle")
            + T(105, y + 6, "Sonst falsch gedruckt. Im Druckdialog „Tatsächliche Größe“ bzw. „100 %“ wählen, nicht „An Seite anpassen“.", 2.6, 400, GREY, "middle"))


def header(n, title, lines, scale="1:1"):
    return ([T(12, 14, f"NOVALIFE · TIME TRAVEL · DESIGN v1.9 · NACH PAPIERTEST 3 · STAND 17.10.2026 · {scale}", 2.8, 700, GREY),
             T(198, 14, f"Seite {n} von {PAGES}", 2.8, 400, GREY, "end"), T(12, 24, title, 6.2, 700)]
            + [T(12, 31 + i * 4.4, s, 3.0, 400, SUB) for i, s in enumerate(lines)])


def poly(pts):
    return "M" + "L".join(f"{F(x)} {F(y)}" for x, y in pts) + "Z"


def img_uri(im):
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=90)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


# ================= Hardware =================
def button(cx, cy, d):
    r = d / 2
    def star(r1, r2):
        pts = []
        for k in range(16):
            ang = math.pi / 8 * k - math.pi / 2
            rr = r1 if k % 2 == 0 else r2
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        return poly(pts)
    return (f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r)}" style="fill: {COP}; stroke: {COPD}; stroke-width: {F(d*0.02)}px"></circle>'
            f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r*0.84)}" style="fill: none; stroke: {COPD}; stroke-width: {F(d*0.018)}px"></circle>'
            f'<path d="{star(r*0.62, r*0.36)}" style="fill: {COPD}; fill-opacity: 0.55; stroke: {COPD}; stroke-width: {F(d*0.012)}px"></path>'
            f'<path d="{star(r*0.30, r*0.17)}" style="fill: {COPL}"></path>')


def rivet(cx, cy, d=9.0):
    r = d / 2
    return (f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r)}" style="fill: {COP}; stroke: {COPD}; stroke-width: 0.25px"></circle>'
            f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r*0.45)}" style="fill: {COPL}; fill-opacity: 0.7"></circle>')


# ================= Band A auf skalierter Taschenkurve (px wie build.py, 1 px = 1,25 mm) =================
P0 = [(367.2, 172), (362.4, 224.0), (299.2, 259.2), (244.0, 263.2)]
PK = [(P0[0][0] + (x - P0[0][0]) * BAND_K, P0[0][1] + (y - P0[0][1]) * BAND_K) for x, y in P0]


def bez(t):
    mt = 1 - t
    return (mt**3 * PK[0][0] + 3 * mt * mt * t * PK[1][0] + 3 * mt * t * t * PK[2][0] + t**3 * PK[3][0],
            mt**3 * PK[0][1] + 3 * mt * mt * t * PK[1][1] + 3 * mt * t * t * PK[2][1] + t**3 * PK[3][1])


PTS = [bez(i / 4000) for i in range(4001)]
ARC = [0.0]
for i in range(1, len(PTS)):
    ARC.append(ARC[-1] + math.hypot(PTS[i][0] - PTS[i - 1][0], PTS[i][1] - PTS[i - 1][1]))
LTOT = ARC[-1]
UF = B.UF; NF = int(LTOT // UF); LEADF = (LTOT - NF * UF) / 2; ROWS = FN.BAND_ROWS
O_LO, O_HI = N15.O_LO, N15.O_HI


def at(s):
    s = max(0, min(LTOT, s)); i = min(max(bisect.bisect_left(ARC, s), 1), len(ARC) - 1)
    x, y = PTS[i - 1]; x2, y2 = PTS[i]; tx, ty = x2 - x, y2 - y; l = math.hypot(tx, ty) or 1
    tx, ty = tx / l, ty / l
    return x, y, tx, ty, -ty, tx


def corners(col, row):
    s_ = LEADF + (col + 0.5) * UF; x, y, tx, ty, nx, ny = at(s_); off = (row - (ROWS - 11)) * UF
    cx, cy = x + nx * off, y + ny * off; h = UF / 2 + 0.06
    return [(cx - tx*h - nx*h, cy - ty*h - ny*h), (cx + tx*h - nx*h, cy + ty*h - ny*h), (cx + tx*h + nx*h, cy + ty*h + ny*h), (cx - tx*h + nx*h, cy - ty*h + ny*h)]


def offset_line(off, steps=200):
    q = []
    for j in range(steps + 1):
        s = LEADF + j * (NF * UF) / steps; x, y, tx, ty, nx, ny = at(s); q.append((x + nx * off, y + ny * off))
    return q


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


Wb = FN.band_white(NF, (3 - NF // 2) % FN.RAP)
fill = {"r": [], "w": []}; xs = {"r": [], "w": []}
for col in range(NF):
    for row in range(ROWS):
        k = "w" if (row, col) in Wb else "r"
        c = corners(col, row)
        fill[k].append(poly(c))
        i = 0.12
        p0 = lerp(c[0], c[2], i); p2 = lerp(c[0], c[2], 1 - i); p1 = lerp(c[1], c[3], i); p3 = lerp(c[1], c[3], 1 - i)
        xs[k].append(f"M{F(p0[0])} {F(p0[1])}L{F(p2[0])} {F(p2[1])}M{F(p1[0])} {F(p1[1])}L{F(p3[0])} {F(p3[1])}")
BAND = (f'<path d="{"".join(fill["r"])}" style="fill: {REDD}"></path>'
        f'<path d="{"".join(fill["w"])}" style="fill: {WHT2}"></path>'
        f'<path d="{"".join(xs["r"])}" style="fill: none; stroke: {REDL}; stroke-width: {F(UF*0.3)}px; stroke-linecap: round"></path>'
        f'<path d="{"".join(xs["w"])}" style="fill: none; stroke: {WHITE}; stroke-width: {F(UF*0.34)}px; stroke-linecap: round"></path>')
LO_EDGE = offset_line(O_LO - 0.4); HI_EDGE = offset_line(O_HI + 0.4)
BAND_CUT = poly(LO_EDGE + HI_EDGE[::-1])
edge_mm = lambda q: sum(math.hypot(q[i][0] - q[i - 1][0], q[i][1] - q[i - 1][1]) for i in range(1, len(q))) * 1.25
INNER_MM = round(edge_mm(offset_line(O_HI))); OUTER_MM = round(edge_mm(offset_line(O_LO)))
ALLB = LO_EDGE + HI_EDGE
BX0 = min(p[0] for p in ALLB); BX1 = max(p[0] for p in ALLB); BY0 = min(p[1] for p in ALLB); BY1 = max(p[1] for p in ALLB)
BAND_W_MM = (BX1 - BX0) * 1.25; BAND_H_MM = (BY1 - BY0) * 1.25


# ================= Gesäßtaschen =================
def pocket_shape(inner_right=True):
    """Fünfeck in Taschen-mm. Innenseite (zur hinteren Mitte) ist 5 mm länger, Spitze unten mittig."""
    dx = (POCKET_TOP - POCKET_BOT) / 2
    h_in = math.sqrt(SIDE_IN**2 - dx**2); h_out = math.sqrt(SIDE_OUT**2 - dx**2)
    tip_d = math.sqrt(TIP_EDGE**2 - (POCKET_BOT / 2)**2)
    yb = h_in
    if inner_right:      # linke Tasche, von hinten gesehen: Innenseite rechts
        top_l, top_r = (0, h_in - h_out), (POCKET_TOP, 0)
    else:                # rechte Tasche: Innenseite links
        top_l, top_r = (0, 0), (POCKET_TOP, h_in - h_out)
    return [top_l, top_r, (POCKET_TOP - dx, yb), (POCKET_TOP / 2, yb + tip_d), (dx, yb)]


def inset(pts, d):
    """Konvexes Polygon (im Uhrzeigersinn, y nach unten) um d nach innen versetzen."""
    n = len(pts); lines = []
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        ex, ey = x2 - x1, y2 - y1; l = math.hypot(ex, ey); nx, ny = -ey / l, ex / l   # Innen-Normale
        lines.append(((x1 + nx * d, y1 + ny * d), (ex, ey)))
    out = []
    for i in range(n):
        (p, r), (q, s) = lines[i - 1], lines[i]
        den = r[0] * s[1] - r[1] * s[0]
        t = ((q[0] - p[0]) * s[1] - (q[1] - p[1]) * s[0]) / den
        out.append((p[0] + r[0] * t, p[1] + r[1] * t))
    return out


def hem_line(pts, d):
    """Linie parallel zur Oberkante, d mm darunter, zwischen den beiden Seiten."""
    (x1, y1), (x2, y2) = pts[0], pts[1]
    ex, ey = x2 - x1, y2 - y1; l = math.hypot(ex, ey); nx, ny = -ey / l, ex / l
    a = (x1 + nx * d, y1 + ny * d); dirv = (ex, ey)

    def hit(p1, p2):
        r = (p2[0] - p1[0], p2[1] - p1[1]); den = dirv[0] * r[1] - dirv[1] * r[0]
        t = ((p1[0] - a[0]) * r[1] - (p1[1] - a[1]) * r[0]) / den
        return (a[0] + dirv[0] * t, a[1] + dirv[1] * t)
    return hit(pts[4], pts[0]), hit(pts[1], pts[2])


def pocket_svg(pts, motif):
    st = inset(pts, 5.0); h1, h2 = hem_line(pts, 15.0)
    return (f'<path d="{poly(pts)}" style="fill: {DEN}"></path>'
            f'<path d="{poly(st)}M{F(h1[0])} {F(h1[1])}L{F(h2[0])} {F(h2[1])}" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>'
            + motif + cut(poly(pts)))


def dims(pts, inner_right):
    """Maßangaben an Ober-, Unter- und Seitenkanten"""
    o = []
    tl, tr, br, tip, bl = pts
    o.append(T((tl[0] + tr[0]) / 2, min(tl[1], tr[1]) - 2.5, "160 mm", 2.6, 700, GUIDE, "middle"))
    o.append(T((bl[0] + br[0]) / 2, bl[1] - 3, "130 mm", 2.6, 700, "#c9cdd4", "middle"))
    li, ri = ("außen 120", "innen 125") if inner_right else ("innen 125", "außen 120")
    o.append(T(tl[0] - 2.5, (tl[1] + bl[1]) / 2, li, 2.6, 700, GUIDE, "end"))
    o.append(T(tr[0] + 2.5, (tr[1] + br[1]) / 2, ri, 2.6, 700, GUIDE))
    o.append(T((bl[0] + tip[0]) / 2 - 3, (bl[1] + tip[1]) / 2 + 4, "70", 2.6, 700, GUIDE, "end"))
    o.append(T((br[0] + tip[0]) / 2 + 3, (br[1] + tip[1]) / 2 + 4, "70", 2.6, 700, GUIDE))
    return o


# ================= Patch D =================
src = Image.open(os.path.join(SKIZZEN, "2026-10-16_baum_referenz_patch_d.jpg")).convert("RGB")
PATCH_PHOTO = img_uri(src.crop((80, 118, 948, 884)).resize((800, 710), Image.LANCZOS))

pages = []

# ---- 1 Übersicht
L_PTS = pocket_shape(True); POCKET_H = round(max(p[1] for p in L_PTS))
rows = [
    ("A", "Taschenband vorn rechts", f"23 mm breit, 17 Kreuzstiche, Innenkante {INNER_MM} mm auf der Taschenöffnung", "Rot, Weiß", "Jeansfabrik"),
    ("E", "Münztasche voll bestickt", f"Tasche 62 × 62 mm, Stickerei 60 × 60 mm, {COIN_C} × {COIN_R} Stiche, wie v1.8", "Rot, Weiß", "Jeansfabrik"),
    ("B2", "Drei Ähren, rotes Band, Goldfäden", "linke Gesäßtasche, Band 48 mm, 9 Fäden 18–30 mm von Hand", "Gold, Rot, Weiß", "Jeansfabrik"),
    ("C", "Achtstern", "rechte Gesäßtasche, 36 × 36 mm, 27 × 27 Stiche, Höhe wie B2-Band", "Rot, Weiß", "Jeansfabrik"),
    ("T", "Gesäßtaschen", f"oben 160, unten 130, Seiten innen 125 / außen 120, Spitze je 70 mm, ~{POCKET_H} mm hoch", "Denim", "Jeansfabrik"),
    ("D", "Patch hinten rechts, Gürtelschlaufe", f"{F(PATCH_W)} × {F(PATCH_H)} mm, Naturleinen, 4 Kupfernieten, „NL“, max. 4 Garnfarben", "4 Garnfarben", "Patch-Hersteller"),
    ("K", "Knopf", f"Shank Button {F(BUTTON_D)} mm, Antik-Kupfer, Achtstern vertieft", "Kupfer", "Fabrik (Knopf-Lieferant)"),
    ("N", "Nieten", "Antik-Kupfer, glatt: 6 × 9 mm vorn, 4 × 6 mm am Patch", "Kupfer", "Fabrik"),
]
p = header(1, "Übersicht · was sich nach Papiertest 3 geändert hat", [
    "Seiten 2–5 sind 1:1. Alle Maße gelten für Basisgröße M (gemessen an deiner Eightyfive in M).",
    "Neu: Band A kürzer, Knopf 20 mm, Patch D 80 × 71 mm. Münztasche E bleibt 62 × 62 mm wie in v1.8.",
    "Gesäßtaschen kleiner und nur leicht schräg (innen 5 mm höher). Ohne Serp, alle Metallteile Antik-Kupfer.",
], "ÜBERSICHT")
y = 52
p.append(f'<rect x="12" y="{y-4.5}" width="186" height="6.5" style="fill: #eef0f3"></rect>')
for x, s in [(14, "Teil"), (24, "Was"), (80, "Maß und Lage"), (148, "Farben"), (172, "Geht an")]:
    p.append(T(x, y, s, 2.9, 700))
y += 8
for k, a, b, c, d in rows:
    p.append(T(14, y, k, 3.2, 700)); p.append(T(24, y, a, 2.8, 700))
    words = b.split(" "); line = ""; yy = y
    for wd in words:
        if len(line + " " + wd) > 38:
            p.append(T(80, yy, line.strip(), 2.7, 400, SUB)); yy += 3.6; line = ""
        line += " " + wd
    p.append(T(80, yy, line.strip(), 2.7, 400, SUB))
    p.append(T(148, y, c, 2.7, 400, SUB)); p.append(T(172, y, d, 2.6, 400, SUB))
    y = max(yy, y) + 7.5
    p.append(f'<path d="M12 {F(y-5.2)}H198" style="stroke: #e2e5ea; stroke-width: 0.3px"></path>')
y += 4
p.append(T(12, y, "Was sich gegenüber v1.8 geändert hat", 3.4, 700)); y += 6
for s in ["Münztasche E: bleibt 62 × 62 mm (Entscheidung 17.10.). Stickerei bleibt bei ~28.000 Stichen.",
          f"Band A: Innenkante {INNER_MM} mm statt 186 mm. Die Außenkante ist {OUTER_MM} mm lang, weil das Band 23 mm breit im Bogen läuft.",
          "Knopf: 17 → 20 mm. 20 mm ist die Standardgröße (Ligne 32), dafür gibt es die meisten Lieferanten.",
          "Patch D: 76 × 67 → 80 × 71 mm, gleiche Proportion. Der Gürtel passt weiter durch.",
          "Gesäßtaschen: 144 × 172 → 160/130 × ~150 mm. Neigung jetzt 5 mm statt 16 mm, und andersherum: innen höher.",
          "Patch D: sitzt jetzt hinten rechts statt in der Mitte. Die hintere Mittelschlaufe bleibt."]:
    p.append(T(14, y, "· " + s, 2.8, 400, SUB)); y += 5
y += 4
p.append(T(12, y, "Größen W30–W38", 3.4, 700)); y += 6
for s in ["Basisgröße ist M. Die Fabrik gradiert die Gesäßtaschen und die Taschenöffnung vorn für die anderen Größen.",
          "Band A wird dabei um ganze Musterrapporte länger oder kürzer, nie gestreckt.",
          "Gleich in allen Größen: Münztasche E, Ähren B2, Stern C, Patch D, Knopf und Nieten (ein Stickprogramm je Motiv)."]:
    p.append(T(14, y, "· " + s, 2.8, 400, SUB)); y += 5
pages.append(p)

# ---- 2 Vorn
u = FN.CELL
EX, EY = 14, 50
ex0 = EX + (COIN_W - COIN_C * u) / 2; ey0 = EY + (COIN_H - COIN_R * u) / 2
E = FN.stitched(FN.coin_white(), None, COIN_R, COIN_C, ex0, ey0, u)
BTX, BTY = 196 - BAND_W_MM, 266 - BAND_H_MM      # Band rechts unten
band_g = f'<g transform="translate({F(BTX)} {F(BTY)}) scale(1.25) translate({F(-BX0)} {F(-BY0)})">{BAND}{cut(BAND_CUT)}</g>'
p = header(2, "Vorn · Band A, Münztasche E, Knopf, Nieten", [
    "A und E gehören an die Vordertasche mit der Münztasche (vom Träger aus rechts). Innere Bogenkante von A auf die Taschenöffnung.",
    "E: die ganze Münztasche, 62 × 62 mm. Oben bündig an die Münztaschen-Naht, rechte Kante direkt an der Niete der Taschenöffnung.",
    "Knopf: auf deinen Bundknopf kleben. Nieten: an die Ecken der Vordertaschen und der Münztasche.",
])
p += [f'<rect x="{F(EX)}" y="{F(EY)}" width="{F(COIN_W)}" height="{F(COIN_H)}" style="fill: #34506f"></rect>', E,
      cut(f"M{F(EX)} {F(EY)}h{F(COIN_W)}v{F(COIN_H)}h{F(-COIN_W)}z"),
      T(EX + COIN_W + 5, EY + 6, "E · Münztasche", 3.4, 700), T(EX + COIN_W + 5, EY + 11, "62 × 62 mm, Stickerei 60 × 60 mm", 3, 400, SUB),
      T(EX + COIN_W + 5, EY + 15.5, f"{COIN_C} × {COIN_R} Kreuzstiche, Rot und Weiß", 3, 400, SUB),
      button(170, 64, BUTTON_D), cut(f"M{F(170-BUTTON_D/2-2)} {F(64-BUTTON_D/2-2)}h{F(BUTTON_D+4)}v{F(BUTTON_D+4)}h{F(-BUTTON_D-4)}z"),
      T(170, 82, f"K · Knopf {F(BUTTON_D)} mm", 3, 700, anchor="middle"), T(170, 86.5, "Antik-Kupfer, Achtstern vertieft", 2.7, 400, SUB, "middle"),
      rivet(152, 98), rivet(164, 98), rivet(176, 98), rivet(188, 98), rivet(158, 109), rivet(170, 109),
      T(170, 119, "N · 6 Nieten 9 mm, Antik-Kupfer", 3, 700, anchor="middle"),
      band_g,
      T(14, BTY + 22, "A · Taschenband", 3.4, 700),
      T(14, BTY + 27, "23 mm breit, 17 Kreuzstiche, Rot und Weiß", 3, 400, SUB),
      T(14, BTY + 31.5, f"Innenkante {INNER_MM} mm (kommt auf die Taschenöffnung),", 3, 400, SUB),
      T(14, BTY + 36, f"Außenkante {OUTER_MM} mm. Vorher innen 186 mm.", 3, 400, SUB),
      checkline(276)]
pages.append(p)

# ---- 3 Hinten links: B2
PX, PY = 25, 62
b2x, b2y = MOTIF_C[0] - 24.0, MOTIF_C[1] - 24.55
p = header(3, "Hinten links · drei Ähren, rotes Band, Goldfäden (B2)", [
    "Tasche ausschneiden und auf deine linke Gesäßtasche legen (vom Träger aus links). Die Innenseite (zur Mitte) ist 5 mm höher.",
    "Goldfäden echt machen: 9 Stücke gelbes Garn, 18–30 mm, unterschiedlich lang, direkt unter das rote Band kleben.",
    "In der Fabrik: Ähren und Band gestickt, die 9 Fäden nach der Wäsche von Hand gesetzt und innen in der Tasche verknotet.",
])
p += [f'<g transform="translate({PX} {PY})">{pocket_svg(L_PTS, f"<g transform=\"translate({F(b2x)} {F(b2y)})\">{V16.B2_V16}</g>")}</g>',
      f'<g transform="translate({PX} {PY})">{"".join(dims(L_PTS, True))}</g>',
      T(PX + 80, PY + POCKET_H + 10, "B2 · Tasche oben 160, unten 130, Spitze je 70 mm · Band 48 mm · 9 Fäden 18–30 mm", 3, 700, anchor="middle"),
      checkline(272)]
pages.append(p)

# ---- 4 Hinten rechts: C
R_PTS = pocket_shape(False)
AW, AR = FN.alatyr_fine()
star = FN.stitched(AW, AR, 27, 27, MOTIF_C[0] - 27 * u / 2, MOTIF_C[1] - 27 * u / 2, u)
p = header(4, "Hinten rechts · Achtstern (C)", [
    "Tasche ausschneiden und auf deine rechte Gesäßtasche legen (vom Träger aus rechts). Die Innenseite (zur Mitte) ist 5 mm höher.",
    "Der Stern sitzt waagerecht mittig, auf gleicher Höhe wie das rote Band links.",
    "Nach außen heißt er „eight-point star“, nicht „Alatyr“.",
])
p += [f'<g transform="translate({PX} {PY})">{pocket_svg(R_PTS, star)}</g>',
      f'<g transform="translate({PX} {PY})">{"".join(dims(R_PTS, False))}</g>',
      T(PX + 80, PY + POCKET_H + 10, "C · Tasche oben 160, unten 130, Spitze je 70 mm · Stern 36 × 36 mm, 27 × 27 Stiche", 3, 700, anchor="middle"),
      checkline(272)]
pages.append(p)

# ---- 5 Patch D
p = header(5, "Hinten rechts · Patch D als Gürtelschlaufe", [
    f"Dein Baum-Bild 1:1, jetzt {F(PATCH_W)} × {F(PATCH_H)} mm. Die 4 Garnfarben legt der Patch-Hersteller mit dir fest: Gold, Kupfer, Dunkelbraun, Rot.",
    "Sitz hinten rechts (vom Träger aus), zwischen Mittelschlaufe und rechter Schlaufe.",
    "Nur links und rechts genäht und genietet, oben und unten offen, der Gürtel läuft dahinter.",
    "Papiertest: Bild auf Pappe kleben, ausschneiden, hinten rechts mit Krepp nur links und rechts fixieren, Gürtel durchziehen.",
])
px, py = 14, 56
p += [f'<image href="{PATCH_PHOTO}" x="{px}" y="{py}" width="{F(PATCH_W)}" height="{F(PATCH_H)}" preserveAspectRatio="none"></image>',
      cut(f"M{px} {py}h{F(PATCH_W)}v{F(PATCH_H)}h{F(-PATCH_W)}z"),
      T(px + PATCH_W / 2, py + PATCH_H + 6, f"D · {F(PATCH_W)} × {F(PATCH_H)} mm · Foto 1:1", 3, 700, anchor="middle")]
by = 150; bw, bh = PATCH_W, PATCH_H
p += [T(14, by, "Bauplan für die Fabrik", 3.6, 700),
      f'<rect x="14" y="{by+5}" width="{F(bw)}" height="{F(bh)}" style="fill: #efe7d6; stroke: {INK}; stroke-width: 0.3px"></rect>',
      f'<rect x="14" y="{by+5}" width="8" height="{F(bh)}" style="fill: url(#hatch)"></rect>',
      f'<rect x="{F(14+bw-8)}" y="{by+5}" width="8" height="{F(bh)}" style="fill: url(#hatch)"></rect>',
      rivet(18, by + 11, 6), rivet(14 + bw - 4, by + 11, 6), rivet(18, by + bh - 1, 6), rivet(14 + bw - 4, by + bh - 1, 6),
      f'<rect x="22" y="{F(by+5+bh/2-9.5)}" width="{F(bw-16)}" height="19" style="fill: none; stroke: #4a6fa5; stroke-width: 0.5px; stroke-dasharray: 2 1.4"></rect>',
      T(14 + bw / 2, by + 5 + bh / 2 - 1.5, "Gürtel läuft dahinter", 2.8, 700, "#4a6fa5", "middle"),
      T(14 + bw / 2, by + 5 + bh / 2 + 3, f"Tunnel innen ca. {F(bw-16)} mm breit", 2.6, 400, "#4a6fa5", "middle")]
for i, s in enumerate(["Schraffiert: je 8 mm Nahtzone links und rechts, dort genäht", "und mit je 2 Kupfernieten (6 mm) gesichert.",
                       "Oben und unten offen, keine Naht.", "Kante umgeschlagen und gesteppt, Grund Naturleinen.",
                       "Linien mind. 0,8 mm, Einrollungen mind. 2,5 mm.", "Muster vom Patch-Hersteller ist Pflicht vor 100 Stück.",
                       "Sitz: hinten rechts, mittig zwischen", "Mittelschlaufe und rechter Schlaufe.", "Oberkante bündig mit der Bundoberkante."]):
    p.append(T(102, by + 10 + i * 5, s, 2.8, 400, SUB))
p.append(checkline(272))
pages.append(p)

DEFS = ('<defs><pattern id="hatch" width="2" height="2" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<rect width="2" height="2" style="fill: #efe7d6"></rect><path d="M0 0V2" style="stroke: #b9a98a; stroke-width: 0.6px"></path></pattern></defs>')


def page(parts):
    return (f'<div class="pg"><svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">{DEFS}'
            f'<rect width="210" height="297" style="fill: #ffffff"></rect>{"".join(parts)}</svg></div>')


html = ('<!doctype html><html lang="de"><head><meta charset="utf-8"><title>NVL Druckvorlage v1.9</title>'
        '<style>@page{size:210mm 297mm;margin:0}html,body{margin:0;padding:0}.pg{width:210mm;height:297mm;overflow:hidden;break-after:page}.pg svg{display:block}</style></head><body>'
        + "".join(page(pp) for pp in pages) + '</body></html>')
open(os.path.join(OUT, "print19.html"), "w").write(html)
print("Band innen", INNER_MM, "außen", OUTER_MM, "NF", NF, "Bandbox mm", round(BAND_W_MM), round(BAND_H_MM), "Tasche hoch", POCKET_H)
print("L", [(round(x, 1), round(y, 1)) for x, y in L_PTS])
