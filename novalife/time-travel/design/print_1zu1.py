# -*- coding: utf-8 -*-
# Druckvorlage 1:1 · drei A4-Hochformatseiten · Design v1.4
import io, contextlib, math
with contextlib.redirect_stdout(io.StringIO()):
    import build as B
import fine as FN
from tree2 import TREE2
F=lambda v: f"{v:.2f}".rstrip('0').rstrip('.')
WHITE=FN.WHITE; RED=FN.RED; REDD=FN.REDD; REDL=FN.REDL; WHT2=FN.WHT2
DEN="#2d4668"; INK="#1d2330"; GREY="#8a8f99"; GUIDE="#9aa1ad"
FONT="font-family: Helvetica, Arial, sans-serif"
def T(x,y,s,size=3.4,w=400,col=INK,anchor="start"):
    return f'<text x="{F(x)}" y="{F(y)}" style="{FONT}; font-size: {F(size)}px; font-weight: {w}; fill: {col}; text-anchor: {anchor}">{s}</text>'
def cut(d): return f'<path d="{d}" style="fill: none; stroke: {INK}; stroke-width: 0.25px; stroke-dasharray: 1.6 1.2"></path>'
def checkline(y):
    return (f'<path d="M55 {F(y)}H155M55 {F(y-2.5)}V{F(y+2.5)}M155 {F(y-2.5)}V{F(y+2.5)}" style="fill: none; stroke: {INK}; stroke-width: 0.35px"></path>'
            + T(105,y-3.4,"Kontrolle: diese Linie muss genau 100 mm lang sein",2.8,700,anchor="middle")
            + T(105,y+6,"Sonst falsch gedruckt. Im Druckdialog „Tatsächliche Größe“ bzw. „100 %“ wählen, nicht „An Seite anpassen“.",2.6,400,GREY,"middle"))
def header(n,title,sub):
    return (T(12,14,"NOVALIFE · TIME TRAVEL · DRUCKVORLAGE 1:1 · DESIGN v1.4",2.8,700,GREY)
            + T(198,14,f"Seite {n} von 3",2.8,400,GREY,"end")
            + T(12,24,title,6.2,700) + "".join(T(12,31+i*4.6,line,3.3,400,"#353a46") for i,line in enumerate(sub)))

# ---------- Seite 1: vorn, Band A (gebogen, Kreuzstich) + Münztasche E ----------
UF=B.UF; NF=B.NF; LEADF=B.LEADF
def corners(col,row):
    s_=LEADF+(col+0.5)*UF; x,y,tx,ty,nx,ny=B.at(s_); off=(row-10)*UF
    cx,cy=x+nx*off,y+ny*off; h=UF/2+0.06
    return [(cx-tx*h-nx*h,cy-ty*h-ny*h),(cx+tx*h-nx*h,cy+ty*h-ny*h),(cx+tx*h+nx*h,cy+ty*h+ny*h),(cx-tx*h+nx*h,cy-ty*h+ny*h)]
def lerp(a,b,t): return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
Wb=FN.band_white(NF,(3-NF//2)%FN.RAP)
fill={"r":[], "w":[]}; xs={"r":[], "w":[]}
for col in range(NF):
    for row in range(21):
        k="w" if (row,col) in Wb else "r"
        c=corners(col,row)
        fill[k].append("M"+"L".join(f"{F(a)} {F(b)}" for a,b in c)+"Z")
        i=0.12
        p0=lerp(c[0],c[2],i); p2=lerp(c[0],c[2],1-i); p1=lerp(c[1],c[3],i); p3=lerp(c[1],c[3],1-i)
        xs[k].append(f"M{F(p0[0])} {F(p0[1])}L{F(p2[0])} {F(p2[1])}M{F(p1[0])} {F(p1[1])}L{F(p3[0])} {F(p3[1])}")
band=(f'<path d="{"".join(fill["r"])}" style="fill: {REDD}"></path>'
      f'<path d="{"".join(fill["w"])}" style="fill: {WHT2}"></path>'
      f'<path d="{"".join(xs["r"])}" style="fill: none; stroke: {REDL}; stroke-width: {F(UF*0.3)}px; stroke-linecap: round"></path>'
      f'<path d="{"".join(xs["w"])}" style="fill: none; stroke: {WHITE}; stroke-width: {F(UF*0.34)}px; stroke-linecap: round"></path>')
band_cut=B.offset_poly(-10.5*UF-0.4,10.5*UF+0.4)
guides=(f'<path d="M 240 172 L 392 172" style="fill: none; stroke: {GUIDE}; stroke-width: 0.5px"></path>'
        f'<path d="M 356.0 172 C 352 220 296 248.8 245.2 252" style="fill: none; stroke: {GUIDE}; stroke-width: 0.6px; stroke-dasharray: 2 1.5"></path>'
        f'<rect x="287.2" y="160" width="9.6" height="17.6" style="fill: none; stroke: {GUIDE}; stroke-width: 0.4px"></rect>'
        f'<rect x="367.2" y="160" width="9.6" height="17.6" style="fill: none; stroke: {GUIDE}; stroke-width: 0.4px"></rect>'
        f'<circle cx="352.8" cy="176.8" r="3.6" style="fill: none; stroke: {GUIDE}; stroke-width: 0.4px"></circle>'
        f'<circle cx="249.6" cy="254.4" r="3.6" style="fill: none; stroke: {GUIDE}; stroke-width: 0.4px"></circle>')
OX,OY=11,58   # px (240,160) -> mm (OX,OY)
def px2mm(x,y): return (OX+(x-240)*1.25, OY+(y-160)*1.25)
cx0,cy0=px2mm(284,176.8)
E=FN.stitched(FN.coin_white(),None,37,37,cx0+(50-37*FN.CELL)/2,cy0+(50-37*FN.CELL)/2,FN.CELL)
p1=[header(1,"Vorn · Taschenband A und Münztasche E",
           ["Gehört an die Vordertasche mit der kleinen Münztasche (vom Träger aus rechts).",
            "Ausschneiden entlang der gestrichelten Linien. Graue Linien = Hose in unserer Zeichnung, nur als Hilfe.",
            "Band: die kurze, innere Bogenkante genau auf die Taschenöffnung legen.",
            "Läuft dein Taschenbogen anders: Band an 2–3 Stellen von außen fast bis zur Innenkante einschneiden, dann biegt es sich mit.",
            "Münztasche: Quadrat mittig auf deine Münztasche. Alles mit Malerkrepp fixieren."]),
    f'<g transform="translate({F(OX)} {F(OY)}) scale(1.25) translate(-240 -160)">{guides}{band}{cut(band_cut)}</g>',
    E, cut(f"M{F(cx0)} {F(cy0)}h50v50h-50z"),
    T(cx0+25,cy0+57,"E · Münztasche 50 × 50 mm",3,700,anchor="middle"),
    T(*px2mm(300,268), "A · Taschenband 28 mm",3,700),
    T(*px2mm(240,165), "Bundnaht",2.6,400,GUIDE),
    checkline(268)]

# ---------- Seite 2: rechte Gesäßtasche mit B, B2, Goldfäden ----------
PX,PY=33,50   # Taschen-Box (144 x 172 mm) Ursprung
pocket=(f'<path d="M144 0L0 16L0 144L72 172L144 144Z" style="fill: #2f4a6e"></path>'
        f'<path d="M139 6L5 21L5 140L72 166L139 140Z M144 15L0 31" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>'
        f'<g transform="translate(39.75 75.5)">{B.SCENE_NT}</g><g transform="translate(47 28.5)">{B.EARS_T}</g>')
p2=[header(2,"Hinten · rechte Gesäßtasche · B mit Ähren und Goldfäden",
           ["Gehört auf die rechte Gesäßtasche (vom Träger aus rechts).",
            "Ganze Tasche entlang der gestrichelten Kontur ausschneiden und über deine Tasche legen, Oberkante an Oberkante.",
            "Ist deine Tasche kleiner oder größer: Ähren mit Linie oben bündig, Garbe mittig darunter ausschneiden und kleben."]),
    f'<g transform="translate({PX} {PY})">{pocket}{cut("M144.6 -0.6L-0.6 15.5L-0.6 144.4L72 172.7L144.6 144.4Z")}</g>',
    T(PX+72,PY+180,"Tasche 144 × 172 mm · B ca. 48 × 76 mm · B2 50 × 43 mm mit Goldfäden",3,700,anchor="middle"),
    checkline(268)]

# ---------- Seite 3: D Lebensbaum-Patch + C Alatyr ----------
DX,DY=62,52
AW,AR=FN.alatyr_fine()
CX_,CY_=83,170
p3=[header(3,"Hinten oben · Lebensbaum-Patch D und Alatyr C",
           ["Patch D: entlang der Patch-Kante ausschneiden. Zwischen die zwei mittleren Gürtelschlaufen,",
            "rechts neben der hinteren Mittelnaht. Oberkante 6 mm unter der Bundoberkante, er reicht über den Bund auf die Passe.",
            "Alatyr C: Quadrat ausschneiden. Passe hinten links, zwischen den zwei linken Gürtelschlaufen,",
            "in der Mitte zwischen Bundnaht und Passennaht (oben und unten ca. 9 mm Luft)."]),
    f'<g transform="translate({DX} {DY})">{TREE2}</g>',
    cut(f"M{DX+3.6} {DY+2.6} L{DX+26} {DY+2.6} C{DX+33} {DY+2.6} {DX+35} {DY+0.2} {DX+43} {DY+0.2} C{DX+51} {DY+0.2} {DX+53} {DY+2.6} {DX+60} {DY+2.6} L{DX+82.4} {DY+2.6} Q{DX+85.8} {DY+2.6} {DX+85.8} {DY+6} L{DX+85.8} {DY+66.4} Q{DX+85.8} {DY+69.8} {DX+82.4} {DY+69.8} L{DX+62} {DY+69.8} C{DX+54} {DY+69.8} {DX+53} {DY+76} {DX+43} {DY+76} C{DX+33} {DY+76} {DX+32} {DY+69.8} {DX+24} {DY+69.8} L{DX+3.6} {DY+69.8} Q{DX+0.2} {DY+69.8} {DX+0.2} {DY+66.4} L{DX+0.2} {DY+6} Q{DX+0.2} {DY+2.6} {DX+3.6} {DY+2.6} Z"),
    T(DX+43,DY+84,"D · Lebensbaum-Patch 86 × 76 mm",3,700,anchor="middle"),
    f'<rect x="{CX_-4}" y="{CY_-4}" width="44" height="44" style="fill: {DEN}"></rect>',
    FN.stitched(AW,AR,27,27,CX_,CY_,FN.CELL),
    cut(f"M{CX_-4} {CY_-4}h44v44h-44z"),
    T(CX_+18,CY_+48,"C · Alatyr 36 mm",3,700,anchor="middle"),
    T(140,176,"So testest du:",3.4,700),
    T(140,182,"1. Alles ausschneiden und aufkleben.",3.1),
    T(140,187,"2. Hose anziehen.",3.1),
    T(140,192,"3. Aus 3 m und aus 1 m in den Spiegel,",3.1),
    T(140,197,"   von vorn und von hinten.",3.1),
    T(140,202,"4. Fotos machen und mir schicken.",3.1),
    checkline(268)]

def page(parts):
    return f'<div class="pg"><svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297"><rect width="210" height="297" style="fill: #ffffff"></rect>{"".join(parts)}</svg></div>'
html=('<!doctype html><html lang="de"><head><meta charset="utf-8"><title>NVL Druckvorlage 1:1</title>'
      '<style>@page{size:210mm 297mm;margin:0}html,body{margin:0;padding:0}.pg{width:210mm;height:297mm;overflow:hidden;break-after:page}.pg svg{display:block}</style></head><body>'
      + page(p1)+page(p2)+page(p3) + '</body></html>')
open('print_1zu1.html','w').write(html)
print(len(html))
