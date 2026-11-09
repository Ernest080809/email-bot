# Patch D: Rückansicht mit Patch und Maßen für Nargiza (09.11.2026). Ausgabe über Playwright als v19/patch_position_W34.png
import sys, base64, os
D = '/home/user/email-bot/novalife/time-travel/design'
sys.path.insert(0, D); os.chdir(D)
import kz_spec as KZ, flats as FL, fine as FN
F = FN.F
png = base64.b64encode(open(D + '/v19/patch_d_clean.png', 'rb').read()).decode()
parts = [p for p in KZ.flat("back") if '>D</text>' not in p and 'stroke-dasharray: 2 1.5' not in p]
px, lr = FL.PATCH_X, FL.LOOP_R
out = FN.patch_outline(px, 0, 80, 71, 5.5)
parts.append(f'<defs><clipPath id="pc"><path d="{out}"/></clipPath></defs>'
             f'<image href="data:image/png;base64,{png}" x="{F(px)}" y="0" width="80" height="71" preserveAspectRatio="none" clip-path="url(#pc)"/>'
             f'<path d="{out}" style="fill:none;stroke:#1b2230;stroke-width:1.2"/>')
d = KZ.Dim(1.1, 11)
# 12,5 cm von der hinteren Mitte bis Patch-Mitte
d.ext(0, -6, 0, -44); d.ext(px + 40, -6, px + 40, -44); d.line(0.5, -37, px + 39.5, -37); d.ann((px + 40) / 2, -46, None, "12,5 cm (W34)")
# 1 cm Patch bis Schlaufe, über dem Bund
d.ext(px + 80, -3, px + 80, -22); d.ext(lr - 5.5, -3, lr - 5.5, -22); d.line(px + 80.5, -15, lr - 6, -15); d.ann(lr + 24, -12, None, "1 cm")
# Oberkante bündig: Linie nach rechts hinaus
d.ext(lr + 7, 0, 300, 0)
d.text(306, 2, "верх патча = верх пояса", "start", .95, 700)
d.text(306, 15, "top of patch = top of waistband", "start", .85, 400, "#566076")
d.text(306, 48, "патч / patch 8 × 7,1 см", "start", .95, 700)
d.text(306, 61, "(по бокам / sides 6 см)", "start", .85, 400, "#566076")
svg = d.svg("-270 -72 760 225", parts, "width:100%")
html = f'''<!doctype html><html><head><meta charset="utf-8">{KZ.FONT}<style>{KZ.CSS}
body{{margin:0;background:#fff;width:1100px}}.w{{padding:24px 28px;font-family:'Roboto Condensed',Arial,sans-serif}}
h1{{margin:0 0 4px;font-size:24px}}p{{margin:0 0 14px;color:#566076;font-size:15px}}</style></head><body><div class="w">
<h1>NVL-TT-01 · PATCH D · POSITION (W34)</h1><p>Сзади справа, как на Levi's · Back right, like Levi's · 1 см до правой задней шлёвки · 12,5 см от среднего заднего шва</p>{svg}</div></body></html>'''
open('/tmp/claude-0/-home-user-email-bot/54727a9c-5c3e-59b1-82f7-802a7ce6ad79/scratchpad/pos/pos.html', 'w').write(html)
