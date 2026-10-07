# -*- coding: utf-8 -*-
# Canvas auf Design v1.7: großer Serp im Stoppelfeld (weiß, rot, grau, braun, gold) an der linken Seitennaht
import sys, os, json, io, contextlib
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "design")
sys.path.insert(0, D)
os.chdir(D)
with contextlib.redirect_stdout(io.StringIO()):
    import build16 as N16
    import build17 as N
os.chdir(os.path.dirname(os.path.abspath(__file__)))
P = "project/"
def rd(fn): return open(fn, encoding="utf-8").read()
def rep(s, a, b, cnt=1):
    assert s.count(a) == cnt, (a[:90], s.count(a))
    return s.replace(a, b)

M = rd(P + "Main.dc.html")
M = rep(M, N16.FRONT_SIDE, N.FRONT_SIDE)
M = rep(M, N16.FRONT_SIDE_LABEL, N.FRONT_SIDE_LABEL)
M = rep(M, '<path d="M5 15V11.5M9 15V12.5M13 15V11.8M27 15V12.4" style="stroke: #dcc07a; stroke-width: 1.3px"></path>',
        '<path d="M5 15V11.5M9 15V12.5M13 15V11.8M27 15V12.4" style="stroke: #d2a53a; stroke-width: 1.3px"></path>')
M = rep(M, '<path d="M21 9C22 3 13.5 0.5 11.5 6" style="fill: none; stroke: #f4f1ea; stroke-width: 2px; stroke-linecap: round"></path>',
        '<path d="M21 9C22 3 13.5 0.5 11.5 6" style="fill: none; stroke: #f4f1ea; stroke-width: 2px; stroke-linecap: round"></path>'
        '<path d="M20.1 8.7C20.6 4.3 14.6 2.4 12.7 6.1" style="fill: none; stroke: #b3322a; stroke-width: 0.9px; stroke-linecap: round"></path>')
M = rep(M, "<span><b>B</b> · Serp im Stoppelfeld · ca. 22 × 35 mm · linkes Bein vorn, 10 mm neben der Seitennaht, Mitte ca. 45 cm unter dem Bund (v1.6, Vorschlag nach deiner Skizze)</span>",
        f"<span><b>B</b> · Serp im Stoppelfeld · ca. {N.SIDE_W} × {N.SIDE_H} mm · weiß, rot, grau, braun, gold · linkes Bein vorn, 10 mm neben der Seitennaht, Mitte ca. 45 cm unter dem Bund (v1.7)</span>")
open(P + "Main.dc.html", "w", encoding="utf-8").write(M)

G = rd(P + "Goldfaeden.dc.html")
head = G[:G.index('<div style="width: 1000px; height: 840px;')]
tail = G[G.index("</x-dc>"):]
def card(svg, vb, label, num, title, text):
    return ('<div style="display: flex; flex-direction: column; gap: 14px; width: 280px">'
            f'<svg width="280" height="326" viewBox="{vb}" role="img" aria-label="{label}" style="display: block">{svg}</svg>'
            '<div style="display: flex; gap: 12px; align-items: flex-start"><span style="display: flex; flex-shrink: 0; width: 28px; height: 28px; border-radius: 14px; background: #1d2330; color: #ffffff; font-family: \'IBM Plex Mono\', monospace; font-size: 12px; font-weight: 600; align-items: center; justify-content: center">'
            f'{num}</span><div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; font-weight: 700; color: #1d2330">{title}</span>'
            f'<span style="font-size: 13px; line-height: 1.45; color: #4a4f5c">{text}</span></div></div></div>')
body = ('<div style="width: 1000px; height: 840px; box-sizing: border-box; padding: 44px 40px 40px; display: flex; flex-direction: column; gap: 26px; background: #efece5; color: #1d2330; font-family: \'Archivo\', Helvetica, sans-serif">'
        '<div style="display: flex; flex-direction: column; gap: 8px">'
        '<div style="font-family: \'IBM Plex Mono\', monospace; font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: #5f6470">NVL-TT-01 · hinten und an der Seite · Design v1.7</div>'
        '<h1 style="margin: 0; font-family: \'Anton\', Impact, sans-serif; font-weight: 400; font-size: 44px; line-height: 1; text-transform: uppercase; color: #1d2330">Details · v1.7</h1>'
        '</div><div style="display: flex; gap: 40px">'
        + card(N16.pocket_left(), "-14 -14 172 200", "Linke Gesäßtasche: drei Ähren auf einem einfach roten Band, darunter neun Goldfäden", "B2",
               "Linke Tasche · Ähren und Fäden",
               "Drei Ähren wie in v1.4, Band einfach rot, 48 mm. Darunter neun Goldfäden, 18–30 mm, von Hand nach der Wäsche.")
        + card(N16.pocket_right(), "-14 -14 172 200", "Rechte Gesäßtasche: Alatyr im feinen Kreuzstich, waagerecht mittig", "C",
               "Rechte Tasche · Alatyr",
               "36 mm, waagerecht mittig, auf Höhe des roten Bands links. Der Patch D sitzt darüber am Bund.")
        + card(N.side_detail(), N.SIDE_VB, "Linkes Bein vorn an der Seitennaht: Serp mit weißer Klinge und roter Schneide über goldenen, abgeschnittenen Halmen", "B",
               "Linkes Bein · Serp im Stoppelfeld",
               f"Der Serp wie vorher: weiße Klinge, rote Schneide, grauer Schliff, brauner Griff. Darunter goldene, abgeschnittene Halme. Ca. {N.SIDE_W} × {N.SIDE_H} mm, 10 mm neben der Seitennaht, Mitte ca. 45 cm unter dem Bund.")
        + '</div></div>\n')
G = head + body + tail
G = G.replace("<title>Details v1.6</title>", "<title>Details v1.7</title>")
open(P + "Goldfaeden.dc.html", "w", encoding="utf-8").write(G)

C = json.loads(rd(P + "canvas.json"))
C["boards"]["Goldfaeden.dc.html"]["title"] = "Details · v1.7"
C["notes"]["titel"]["text"] = "NVL-TT-01 · Projekt Slavic · Design v1.7"
open(P + "canvas.json", "w", encoding="utf-8").write(json.dumps(C, ensure_ascii=False, indent=2))
print("ok", len(M), len(G))
