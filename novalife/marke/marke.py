# -*- coding: utf-8 -*-
# Novalife Markenzeichen und Markenblatt (Stand 07.11.2026, Entscheidung Ernest: Garnfarben dunkel + hell, Cinzel + Inter, Achtstern überall).
# Erzeugt: logo/*.svg und *.png, farben.css, farben.gpl, markenblatt.html, markenblatt.png. Regeln stehen in MARKE.md.
import os, sys, math, subprocess, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "time-travel", "design"))
import fine as FN            # Achtstern C von der Jeans: 8 Rauten mit Fugen
F = FN.F

# Farben: Hex = Bildschirmwert, Pantone TCX = Garn und Druck
COLORS = [
    ("schwarz", "Teppich-Schwarz", "#1A1416", "",            "Grund dunkel"),
    ("leinen",  "Leinen",          "#E8DCC6", "",            "Grund hell, Text auf dunkel"),
    ("rot",     "Knallrot",        "#CD212A", "18-1662 TCX", "Akzent, Achtstern, Knöpfe"),
    ("gold",    "Gold",            "#D8AE47", "14-0952 TCX", "Akzent, Nummern, Linien"),
    ("weiss",   "Garn-Weiß",       "#F4EFE6", "11-0602 TCX", "Text auf Fotos, Achtstern auf Fotos"),
    ("braun",   "Dunkelbraun",     "#56352D", "19-1432 TCX", "Text auf hell, Stempel"),
    ("kupfer",  "Kupfer",          "#A3623B", "17-1340 TCX", "Nebenfarbe hell, Ziernaht"),
]
HEX = {k: h for k, n, h, p, r in COLORS}


def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def star_path(cx, cy, w, gap=None):
    polys = FN.star8_rhombi(cx, cy, w, gap if gap is not None else w * 0.045)
    return "".join("M" + "L".join(f"{F(x)} {F(y)}" for x, y in q) + "Z" for q in polys)


def text_path(txt, font, size, x, base, track=0.12):
    f = TTFont(font); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
    s = size / upm; d = ""; pos = x
    for ch in txt:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, pos, base)))
        d += pen.getCommands(); pos += gs[g].width * s + size * track
    return d, pos - size * track - x


CINZEL = os.path.join(HERE, "fonts", "Cinzel-600.ttf")


def svg(w, h, body, bg=None):
    b = f'<rect width="{F(w)}" height="{F(h)}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {F(w)} {F(h)}" width="{F(w)}" height="{F(h)}">{b}{body}</svg>'


def write(name, s):
    open(os.path.join(HERE, "logo", name), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n' + s)


def build_logos():
    for k in ("rot", "gold", "weiss", "braun"):
        write(f"achtstern_{k}.svg", svg(100, 100, f'<path d="{star_path(50, 50, 100)}" fill="{HEX[k]}"/>'))
    # Wortmarke quer: Stern links, NOVALIFE rechts, Stern = Versalhöhe × 1,9
    d, tw = text_path("NOVALIFE", CINZEL, 40, 0, 0)
    for mode, star_c, txt_c, bg in (("dunkel", "gold", "leinen", "schwarz"), ("hell", "rot", "braun", "leinen")):
        sw = 54; pad = 14; gap = 18; W = pad + sw + gap + tw + pad; H = 82
        dq, _ = text_path("NOVALIFE", CINZEL, 40, pad + sw + gap, 41 + 14)
        body = f'<path d="{star_path(pad + sw / 2, H / 2, sw)}" fill="{HEX[star_c]}"/><path d="{dq}" fill="{HEX[txt_c]}"/>'
        write(f"novalife_quer_{mode}.svg", svg(W, H, body, HEX[bg]))
        write(f"novalife_quer_{mode}_transparent.svg", svg(W, H, body))
        # hoch: Stern oben, Wortmarke darunter
        dh, _ = text_path("NOVALIFE", CINZEL, 40, (max(tw, 120) + 40 - tw) / 2, 0)
        Wv = max(tw, 120) + 40; sv = 96
        dh, _ = text_path("NOVALIFE", CINZEL, 40, (Wv - tw) / 2, 24 + sv + 26 + 29)
        body = f'<path d="{star_path(Wv / 2, 24 + sv / 2, sv)}" fill="{HEX[star_c]}"/><path d="{dh}" fill="{HEX[txt_c]}"/>'
        write(f"novalife_hoch_{mode}.svg", svg(Wv, 24 + sv + 26 + 29 + 24, body, HEX[bg]))
    # Profilbild: Gold auf Teppich-Schwarz, Stern 56 % (runder Zuschnitt der Apps lässt Rand)
    write("profilbild.svg", svg(1080, 1080, f'<path d="{star_path(540, 540, 605)}" fill="{HEX["gold"]}"/>', HEX["schwarz"]))


def build_css():
    css = ":root{\n" + "".join(f"  --nl-{k}: {h};{'  /* Pantone ' + p + ' */' if p else ''}\n" for k, n, h, p, r in COLORS)
    css += "  --nl-font-head: 'Cinzel', Georgia, serif;   /* nur Großbuchstaben, 600, Sperrung .1em */\n  --nl-font-text: 'Inter', system-ui, sans-serif;\n}\n"
    open(os.path.join(HERE, "farben.css"), "w").write(css)
    gpl = "GIMP Palette\nName: Novalife\nColumns: 7\n#\n" + "".join(
        f"{int(h[1:3], 16):3d} {int(h[3:5], 16):3d} {int(h[5:7], 16):3d}\t{n} {p}\n" for k, n, h, p, r in COLORS)
    open(os.path.join(HERE, "farben.gpl"), "w").write(gpl)


def contrast_rows():
    pairs = [("leinen", "schwarz"), ("gold", "schwarz"), ("weiss", "schwarz"), ("rot", "schwarz"),
             ("braun", "leinen"), ("rot", "leinen"), ("kupfer", "leinen"), ("gold", "leinen")]
    return [(a, b, contrast(HEX[a], HEX[b])) for a, b in pairs]


def build_sheet():
    star = lambda w, c: f'<svg viewBox="0 0 100 100" width="{w}" height="{w}"><path d="{star_path(50, 50, 100)}" fill="{HEX[c]}"/></svg>'
    logo = lambda n: open(os.path.join(HERE, "logo", n)).read().split("?>", 1)[1]
    sw = "".join(f'<div class="sw"><i style="background:{h}"></i><b>{n}</b><span>{h}{" · Pantone " + p if p else ""}<br>{r}</span></div>' for k, n, h, p, r in COLORS)
    ct = "".join(f'<tr><td><span style="background:{HEX[b]};color:{HEX[a]}">Aa</span></td><td>{dict((k, n) for k, n, *_ in COLORS)[a]} auf {dict((k, n) for k, n, *_ in COLORS)[b]}</td><td>{c:.1f} : 1</td><td>{"Text" if c >= 4.5 else "nur groß" if c >= 3 else "nur Fläche"}</td></tr>' for a, b, c in contrast_rows())
    post_d = (f'<div class="post" style="background:{HEX["schwarz"]}">{star(120, "rot")}<h4 style="color:{HEX["leinen"]}">TIME TRAVEL</h4>'
              f'<p style="color:{HEX["gold"]}">N° 001 / 100 · 24.06.2027</p><small style="color:{HEX["leinen"]}">NOVALIFE</small></div>')
    post_h = (f'<div class="post" style="background:{HEX["leinen"]}">{star(120, "rot")}<h4 style="color:{HEX["braun"]}">TIME TRAVEL</h4>'
              f'<p style="color:{HEX["braun"]}">N° 001 / 100 · 24.06.2027</p><small style="color:{HEX["braun"]}">NOVALIFE</small></div>')
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Cinzel;font-weight:600;src:url(fonts/Cinzel-600.ttf)}}@font-face{{font-family:Inter;font-weight:400;src:url(fonts/Inter-400.ttf)}}@font-face{{font-family:Inter;font-weight:600;src:url(fonts/Inter-600.ttf)}}
body{{margin:0;background:#f3f1ec;font:14px Inter;color:#1b1b1b;width:1200px}}.wrap{{padding:30px 34px}}
h1{{font:600 30px Cinzel;letter-spacing:.12em;margin:0}}.sub{{color:#666;margin:4px 0 0}}h2{{font:600 13px Inter;text-transform:uppercase;letter-spacing:.14em;color:{HEX["rot"]};margin:26px 0 10px}}
.card{{background:#fff;border:1px solid #e2ddd3;border-radius:10px;padding:16px}}.g2{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}.g3{{display:grid;grid-template-columns:1fr 220px 220px;gap:16px}}
.sws{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px 14px}}.sw{{display:grid;grid-template-columns:34px 1fr;column-gap:8px;font-size:12px}}.sw i{{grid-row:span 2;width:34px;height:34px;border-radius:6px;border:1px solid #0002}}.sw span{{color:#666;font-size:11px;line-height:1.3}}
.lk{{display:flex;gap:14px;align-items:center;flex-wrap:wrap}}.lk svg{{height:64px;width:auto;border-radius:6px}}.lk .v svg{{height:150px}}
.t1{{font:600 34px Cinzel;letter-spacing:.12em}}.t2{{font:600 18px Cinzel;letter-spacing:.1em;margin:4px 0 10px}}.t3{{font-size:14px;line-height:1.5}}
.post{{width:220px;height:275px;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}}.post h4{{font:600 20px Cinzel;letter-spacing:.14em;margin:16px 0 4px}}.post p{{font:400 10.5px Inter;letter-spacing:.12em;margin:0}}.post small{{font:600 9px Cinzel;letter-spacing:.3em;margin-top:26px;opacity:.8}}
table{{border-collapse:collapse;font-size:12px;width:100%}}td{{padding:4px 6px;border-bottom:1px solid #eee}}td span{{display:inline-block;padding:2px 8px;border-radius:4px;font-weight:600}}
ul{{margin:0;padding-left:18px;line-height:1.6;font-size:13px}}.no svg{{opacity:.95}}
</style></head><body><div class="wrap"><h1>NOVALIFE · MARKE</h1><p class="sub">Stand 07.11.2026 · gilt für alles, wo man uns sieht: Posts, Videos, Website, Hangtag, Verpackung, Mails. Quelle: <b>novalife/marke/MARKE.md</b></p>
<h2>Zeichen: der Achtstern</h2><div class="card lk">{logo("profilbild.svg").replace('width="1080" height="1080"', 'width="150" height="150" style="border-radius:50%;flex:none"', 1)}<div class="v">{logo("novalife_hoch_dunkel.svg")}</div><div class="v">{logo("novalife_hoch_hell.svg")}</div><div>{logo("novalife_quer_dunkel.svg")}<br><br>{logo("novalife_quer_hell.svg")}</div></div>
<h2>Farben: die Garnfarben der Jeans</h2><div class="card sws">{sw}</div>
<h2>Schrift und Beispiele</h2><div class="g3"><div class="card"><div class="t1">NOVALIFE</div><div class="t2">CINZEL 600 · NUR VERSALIEN · ÜBERSCHRIFTEN</div><div class="t3">Inter 400 und 600 für alles andere: Fließtext, Untertitel, Preise, Nummern wie N° 001 / 100. Cinzel nie für Fließtext und nie in Kleinbuchstaben.</div></div>{post_d}{post_h}</div>
<div class="g2" style="margin-top:16px"><div class="card"><h2 style="margin-top:0">Kontrast (WCAG)</h2><table>{ct}</table></div>
<div class="card"><h2 style="margin-top:0">Nie</h2><ul><li>Achtstern auf rotem Grund, neben Ähren als Emblem, mit 5 oder 6 Zacken, verzerrt, nur als Umriss</li><li>Hellblau mit Gelb, Weiß-Blau-Rot zusammen. Das einzige Blau ist der Denim auf Fotos</li><li>Nach außen „Alatyr“, „authentisch“, „slawisch“ für den Lebensbaum</li><li>Andere Schriften, andere Rot- oder Goldtöne, Farbverläufe, Schatten auf dem Zeichen</li><li>Der Baum als Logo: Er bleibt Motiv (Polo-Brust, Patch D)</li></ul></div></div>
</div></body></html>'''
    p = os.path.join(HERE, "markenblatt.html"); open(p, "w").write(html)
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
          "let p=await b.newPage({viewport:{width:1200,height:900},deviceScaleFactor:2});"
          f"await p.goto('file://{p}');await p.evaluate(()=>document.fonts.ready);await p.screenshot({{path:'{os.path.join(HERE, 'markenblatt.png')}',fullPage:true}});"
          "p=await b.newPage({viewport:{width:1080,height:1080}});"
          f"await p.goto('file://{os.path.join(HERE, 'logo', 'profilbild.svg')}');await p.screenshot({{path:'{os.path.join(HERE, 'logo', 'profilbild.png')}'}});"
          "await b.close();})();")
    subprocess.run(["node", "-e", js], check=True)


if __name__ == "__main__":
    build_logos(); build_css(); build_sheet()
    for a, b, c in contrast_rows(): print(f"{a} auf {b}: {c:.2f}")
