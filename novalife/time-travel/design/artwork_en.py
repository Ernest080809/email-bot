# -*- coding: utf-8 -*-
# Artwork 1:1 auf Englisch für die Fabriken (20.10.2026): dieselben Teile wie Druckvorlage v1.9, nur Fabrik-Texte
#   1 front A, E, button, rivets · 2 back left B2 · 3 back right C · 4 patch D with snaps
import io, contextlib, os
with contextlib.redirect_stdout(io.StringIO()):
    import print19 as P                      # baut die Druckvorlage mit, Geometrie wird hier wiederverwendet
import fine as FN
import v16 as V16

F, T, cut, INK, GREY, SUB, GUIDE = FN.F, P.T, P.cut, P.INK, P.GREY, P.SUB, P.GUIDE
PAGES = 4


def header(n, title, lines):
    return ([T(12, 14, "NOVALIFE · NVL-TT-01 · ARTWORK v1.9 · 20 OCT 2026 · SCALE 1:1", 2.8, 700, GREY),
             T(198, 14, f"page {n} of {PAGES}", 2.8, 400, GREY, "end"), T(12, 24, title, 6.2, 700)]
            + [T(12, 31 + i * 4.4, s, 3.0, 400, SUB) for i, s in enumerate(lines)])


def checkline(y):
    return (f'<path d="M55 {F(y)}H155M55 {F(y-2.5)}V{F(y+2.5)}M155 {F(y-2.5)}V{F(y+2.5)}" style="fill: none; stroke: {INK}; stroke-width: 0.35px"></path>'
            + T(105, y - 3.4, "Check: this line must measure exactly 100 mm", 2.8, 700, anchor="middle")
            + T(105, y + 6, "Print at 100 % (actual size), not “fit to page”. All measurements in mm, base size M.", 2.6, 400, GREY, "middle"))


def dims(pts, inner_right):
    tl, tr, br, tip, bl = pts
    li, ri = ("outer 120", "inner 125") if inner_right else ("inner 125", "outer 120")
    return [T((tl[0] + tr[0]) / 2, min(tl[1], tr[1]) - 2.5, "160 mm", 2.6, 700, GUIDE, "middle"),
            T((bl[0] + br[0]) / 2, bl[1] - 3, "130 mm", 2.6, 700, "#c9cdd4", "middle"),
            T(tl[0] - 2.5, (tl[1] + bl[1]) / 2, li, 2.6, 700, GUIDE, "end"), T(tr[0] + 2.5, (tr[1] + br[1]) / 2, ri, 2.6, 700, GUIDE),
            T((bl[0] + tip[0]) / 2 - 3, (bl[1] + tip[1]) / 2 + 4, "70", 2.6, 700, GUIDE, "end"),
            T((br[0] + tip[0]) / 2 + 3, (br[1] + tip[1]) / 2 + 4, "70", 2.6, 700, GUIDE)]


pages = []
# ---- 1 front
EX, EY, CW, u = 14, 50, P.COIN_W, FN.CELL
E = FN.stitched(FN.coin_white(), None, P.COIN_R, P.COIN_C, EX + (CW - P.COIN_C * u) / 2, EY + (CW - P.COIN_R * u) / 2, u)
BTX, BTY = 196 - P.BAND_W_MM, 266 - P.BAND_H_MM
p = header(1, "Front · band A, coin pocket E, button, rivets", [
    "A and E belong to the wearer's right front pocket (the one with the coin pocket). The inner curved edge of A sits on the pocket opening.",
    "E covers the whole coin pocket, 62 × 62 mm: top flush with the coin pocket seam, centred between side seam and pocket rivet.",
    "Embroidery on the cut panels before sewing, polyester thread that resists the wash. Thread colours from your colour card.",
])
p += [f'<rect x="{F(EX)}" y="{F(EY)}" width="{F(CW)}" height="{F(CW)}" style="fill: #34506f"></rect>', E,
      cut(f"M{F(EX)} {F(EY)}h{F(CW)}v{F(CW)}h{F(-CW)}z"),
      T(EX + CW + 5, EY + 6, "E · Coin pocket", 3.4, 700), T(EX + CW + 5, EY + 11, "62 × 62 mm, embroidery 60 × 60 mm", 3, 400, SUB),
      T(EX + CW + 5, EY + 15.5, f"{P.COIN_C} × {P.COIN_R} cross-stitches, red and white", 3, 400, SUB),
      P.button(170, 64, P.BUTTON_D), cut(f"M{F(170-P.BUTTON_D/2-2)} {F(64-P.BUTTON_D/2-2)}h{F(P.BUTTON_D+4)}v{F(P.BUTTON_D+4)}h{F(-P.BUTTON_D-4)}z"),
      T(170, 82, f"K · Button {F(P.BUTTON_D)} mm", 3, 700, anchor="middle"), T(170, 86.5, "shank, antique copper, embossed star", 2.7, 400, SUB, "middle"),
      P.rivet(152, 98), P.rivet(164, 98), P.rivet(176, 98), P.rivet(188, 98), P.rivet(158, 109), P.rivet(170, 109),
      T(170, 119, "N · 6 rivets 9 mm, plain antique copper", 3, 700, anchor="middle"),
      f'<g transform="translate({F(BTX)} {F(BTY)}) scale(1.25) translate({F(-P.BX0)} {F(-P.BY0)})">{P.BAND}{cut(P.BAND_CUT)}</g>',
      T(14, BTY + 22, "A · Pocket band", 3.4, 700),
      T(14, BTY + 27, "23 mm wide, 17 cross-stitch rows, red and white", 3, 400, SUB),
      T(14, BTY + 31.5, f"inner edge {P.INNER_MM} mm (on the pocket opening),", 3, 400, SUB),
      T(14, BTY + 36, f"outer edge {P.OUTER_MM} mm", 3, 400, SUB),
      checkline(276)]
pages.append(p)

# ---- 2 back left B2
PX, PY = 25, 62
b2x, b2y = P.MOTIF_C[0] - 24.0, P.MOTIF_C[1] - 24.55
p = header(2, "Back left pocket · three wheat ears on a red band (B2)", [
    "Wearer's left back pocket. The inner side (towards centre back) is 5 mm higher than the outer side.",
    "Wheat ears and red band are embroidered. After washing: 9 gold threads, 18–30 mm, different lengths, set by hand",
    "directly under the red band and knotted inside the pocket.",
])
p += [f'<g transform="translate({PX} {PY})">{P.pocket_svg(P.L_PTS, f"<g transform=\"translate({F(b2x)} {F(b2y)})\">{V16.B2_V16}</g>")}</g>',
      f'<g transform="translate({PX} {PY})">{"".join(dims(P.L_PTS, True))}</g>',
      T(PX + 80, PY + P.POCKET_H + 10, "B2 · pocket top 160, bottom 130, point 70 mm each side · band 48 mm · 9 threads 18–30 mm", 3, 700, anchor="middle"),
      checkline(272)]
pages.append(p)

# ---- 3 back right C
p = header(3, "Back right pocket · eight-point star (C)", [
    "Wearer's right back pocket. The inner side (towards centre back) is 5 mm higher than the outer side.",
    "Star centred horizontally, at the same height as the red band on the left pocket.",
    "8 rhombi with 1 mm gaps (denim shows through), solid red, satin stitch across each rhombus.",
])
p += [f'<g transform="translate({PX} {PY})">{P.pocket_svg(P.R_PTS, FN.star8_svg(P.MOTIF_C[0], P.MOTIF_C[1], 36.0, 1.0))}</g>',
      f'<g transform="translate({PX} {PY})">{"".join(dims(P.R_PTS, False))}</g>',
      T(PX + 80, PY + P.POCKET_H + 10, "C · pocket top 160, bottom 130, point 70 mm each side · star 36 × 36 mm, 8 rhombi, 1 mm gaps", 3, 700, anchor="middle"),
      checkline(272)]
pages.append(p)

# ---- 4 patch D
PW, PH, PB, PS = P.PATCH_W, P.PATCH_H, P.PATCH_BULGE, P.PATCH_SIDE
p = header(4, "Back right · patch D, detachable with snaps", [
    f"Embroidered linen patch supplied by Novalife: {F(PW)} mm wide, {F(PH)} mm high in the middle, {F(PS)} mm at the sides, max. 4 colours.",
    "Back right, centred between centre back loop and right loop. Highest point of the patch flush with the top of the waistband.",
    "Open at top and bottom, the belt runs behind the patch. Removed for washing.",
])
px, py = 14, 56
p += [f'<image href="{P.PATCH_PHOTO}" x="{px}" y="{py}" width="{F(PW)}" height="{F(PH)}" preserveAspectRatio="none"></image>',
      cut(FN.patch_outline(px, py, PW, PH, PB)), P.snaps(px, py),
      T(px + PW / 2, py + PH + 6, f"D · {F(PW)} × {F(PH)} mm, sides {F(PS)} mm · artwork 1:1", 3, 700, anchor="middle")]
by, bw, bh = 150, PW, PH
gx, gy, sin_, sd = P.SNAP_GX, P.SNAP_GY, P.SNAP_IN, P.SNAP_D
p += [T(14, by, "Construction", 3.6, 700),
      f'<path d="{FN.patch_outline(14, by + 5, bw, bh, PB)}" style="fill: #efe7d6; stroke: {INK}; stroke-width: 0.3px"></path>', P.snaps(14, by + 5),
      f'<path d="M{F(14+sin_)} {F(by+5+PB+sin_)}h{F(gx)}M{F(14+sin_)} {F(by+5+PB+sin_)}v{F(gy)}" style="fill: none; stroke: {GUIDE}; stroke-width: 0.25px; stroke-dasharray: 1 0.8"></path>',
      T(14 + bw / 2, by + 5 + PB + sin_ - 1.5, f"{F(gx)} mm", 2.4, 700, GUIDE, "middle"),
      T(14 + sin_ + 1.5, by + 5 + PB + sin_ + gy / 2 + 6, f"{F(gy)} mm", 2.4, 700, GUIDE),
      f'<rect x="{F(14+sin_+sd/2+1)}" y="{F(by+5+bh/2-9.5)}" width="{F(gx-sd-2)}" height="19" style="fill: none; stroke: #4a6fa5; stroke-width: 0.5px; stroke-dasharray: 2 1.4"></rect>',
      T(14 + bw / 2, by + 5 + bh / 2 - 1.5, "belt runs behind", 2.8, 700, "#4a6fa5", "middle"),
      T(14 + bw / 2, by + 5 + bh / 2 + 3, f"tunnel approx. {F(gx-sd)} mm wide", 2.6, 400, "#4a6fa5", "middle")]
for i, s in enumerate(["4 ring-spring snaps 10 mm, antique copper, nickel-free.", "Cap and socket on the patch, stud on the jeans.",
                       f"Snap centres {F(sin_)} mm from the side edge and the side ends.", f"Grid {F(gx)} × {F(gy)} mm, the same on every Novalife jeans.",
                       "Patch with stiff interlining so the snaps cannot tear out.", "Jeans: reinforce each stud inside, interlining 20 × 20 mm.",
                       "Edge folded and topstitched, natural linen.", "Lines min. 0.8 mm, curls min. 2.5 mm.",
                       "Approved sample from the patch maker before 100 pcs.", "Shape: straight sides, 5.5 mm curve top and bottom.",
                       "Plain snaps without letters."]):
    p.append(T(102, by + 10 + i * 5, s, 2.8, 400, SUB))
p.append(checkline(272))
pages.append(p)

html = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>NVL-TT-01 Artwork 1:1</title>'
        '<style>@page{size:210mm 297mm;margin:0}html,body{margin:0;padding:0}.pg{width:210mm;height:297mm;overflow:hidden;break-after:page}.pg svg{display:block}</style></head><body>'
        + "".join(P.page(pp) for pp in pages) + '</body></html>')
open(os.path.join(P.OUT, "artwork_en.html"), "w").write(html)
print("ok", len(pages), "Seiten")
