# -*- coding: utf-8 -*-
import math
from elements import *
from tree2 import TREE2 as TREE_SVG
import fine as FN
SK=(-15,12,15)   # Serp schneidet ein wenig in die Garbe
SCENE=scene(True,*SK)[0]; SCENE_NT=scene(False,*SK)[0]
EARS=ears_line(False); EARS_T=ears_line(True)
FONT="font-family: 'Archivo', Helvetica, sans-serif"; MONO="font-family: 'IBM Plex Mono', monospace"
def txt(x,y,s,size=3.2,w=400,col="#1d2330",anchor="start",mono=False):
    return f'<text x="{F(x)}" y="{F(y)}" style="{MONO if mono else FONT}; font-size: {size}px; font-weight: {w}; fill: {col}; text-anchor: {anchor}">{s}</text>'

# ---------- Elementblatt 1:1 (mm) ----------
def straight_band(x0,y0,ncols,u=4):
    W=ncols*u; h=u/2
    o=[f'<rect x="{F(x0)}" y="{F(y0)}" width="{F(W)}" height="{F(7*u)}" style="fill: {RED}"></rect>']
    o.append(f'<path d="M{F(x0)} {F(y0)}h{F(W)}v{F(h)}h{F(-W)}z M{F(x0)} {F(y0+7*u-h)}h{F(W)}v{F(h)}h{F(-W)}z" style="fill: {WHITE}"></path>')
    o.append(f'<path d="{rect_cells(band_cells(ncols),x0,y0-u,u)}" style="fill: {WHITE}"></path>')
    return "\n".join(o)
def alatyr(x0,y0,u):
    return (f'<path d="{rect_cells(ALATYR_W,x0,y0,u)}" style="fill: {WHITE}"></path>'
            f'<path d="{rect_cells(ALATYR_R,x0,y0,u)}" style="fill: {RED}"></path>')
def coin(x0,y0,u):
    return (f'<path d="{rect_cells(COIN_R,x0,y0,u)}" style="fill: {RED}"></path>'
            f'<path d="{rect_cells(COIN_W,x0,y0,u)}" style="fill: {WHITE}"></path>')
def tree_at(x0,y0,sc=1):
    return f'<g transform="translate({F(x0)} {F(y0)}) scale({F(sc)})">{TREE_SVG}</g>'
def patch(x0,y0,u,edge=1.2,riv=2.4):
    w,h=17*u,15*u
    o=[f'<rect x="{F(x0)}" y="{F(y0)}" width="{F(w)}" height="{F(h)}" rx="{F(u*0.75)}" style="fill: {LINEN}; stroke: {BROWN}; stroke-width: {F(edge)}px"></rect>',
       tree_paths(x0,y0,u)]
    for cx,cy in [(x0+1.5*u,y0+1.5*u),(x0+w-1.5*u,y0+1.5*u),(x0+1.5*u,y0+h-1.5*u),(x0+w-1.5*u,y0+h-1.5*u)]:
        o.append(f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(riv)}" style="fill: #b0703a; stroke: #7d4c24; stroke-width: {F(riv*0.15)}px"></circle>')
    return "\n".join(o)

S=[]
S.append(f'<rect x="0" y="0" width="297" height="210" style="fill: #efece5"></rect>')
S.append(txt(15,12,"NOVALIFE · TIME TRAVEL · ELEMENTE 1:1",4.2,700))
S.append(txt(15,17.5,"Druck: „Tatsächliche Größe“ / 100 %. Die Kontrolllinie unten muss 100 mm messen. A, C, E: ein Kästchen = ein Kreuzstich = 1,33 mm.",2.6,400,"#5f6470"))
S.append(f'<rect x="15" y="28" width="116" height="28" style="fill: #2d4668"></rect>')  # Denim-Vorschau hinter dem Band? -> nein: Band liegt direkt
S[-1]=f'<rect x="11" y="24" width="100" height="44" style="fill: #2d4668"></rect>'
S.append(FN.stitched(FN.band_white(69,(3-34)%FN.RAP),None,21,69,15,32,FN.CELL))
S.append(txt(11,74,"A · Taschenband 28 mm",3.2,700)); S.append(txt(11,78.4,"21 Kreuzstiche hoch · Rapport 16 Stiche = 21 mm · folgt dem Taschenbogen",2.5,400,"#4a4f5c"))
S.append(f'<rect x="120" y="24" width="44" height="44" style="fill: #2d4668"></rect>')
_AW,_AR=FN.alatyr_fine()
S.append(FN.stitched(_AW,_AR,27,27,124,28,FN.CELL))
S.append(txt(120,73,"C · Alatyr · Passe hinten links",3.2,700)); S.append(txt(120,77.4,"27 × 27 Kreuzstiche = 36 mm",2.5,400,"#4a4f5c"))
S.append(tree_at(176,24))
S.append(txt(176,106,"D · Lebensbaum-Patch",3.2,700)); S.append(txt(176,110.4,"86 × 76 mm · Naturleinen · fertiger Stickpatch, aufgenäht",2.5,400,"#4a4f5c"))
S.append(f'<rect x="11" y="84" width="84" height="94" style="fill: #2d4668"></rect>')
S.append(f'<g transform="translate({F(53-32.3)} 90)">{SCENE_NT}</g>')
S.append(txt(11,184,"B · Serp mit Garbe · rechte Gesäßtasche",3.2,700)); S.append(txt(11,188.4,"ca. 48 × 76 mm · die Klingenspitze schneidet in die Halme",2.5,400,"#4a4f5c"))
S.append(f'<rect x="106" y="96" width="58" height="48" style="fill: #2d4668"></rect>')
S.append(f'<g transform="translate(110 99)">{EARS_T}</g>')
S.append(txt(106,150,"B2 · Taschenkante über B",3.2,700)); S.append(txt(106,154.4,"50 × 43 mm · Goldfäden 9–16 mm unter der Linie, von Hand",2.5,400,"#4a4f5c"))
S.append(f'<rect x="176" y="118" width="58" height="58" style="fill: #2d4668"></rect>')
S.append(f'<rect x="180" y="122" width="50" height="50" style="fill: #34506f; stroke: #142236; stroke-width: 0.4px"></rect>')
S.append(FN.stitched(FN.coin_white(),None,37,37,180+(50-37*FN.CELL)/2,122+(50-37*FN.CELL)/2,FN.CELL))
S.append(txt(176,182,"E · Münztasche komplett bestickt",3.2,700)); S.append(txt(176,186.4,"37 × 37 Kreuzstiche = 49 mm · Tasche 50 × 50 mm",2.5,400,"#4a4f5c"))
# Farblegende
lx,ly=242,120
for i,(name,col) in enumerate([("Weiß · Pflicht in jedem Element",WHITE),("Rot · nie ohne Weiß daneben",RED),("Gold · Weizen und Baum",GOLD),("Braun · Serpgriff, Band, Baum",BROWN)]):
    S.append(f'<rect x="{lx}" y="{ly+i*7}" width="5" height="5" style="fill: {col}; stroke: #8a8f99; stroke-width: 0.25px"></rect>')
    S.append(txt(lx+7.5,ly+i*7+4,name,2.6,400,"#353a46"))
# Kontrolllinie
S.append(f'<path d="M190 200H290M190 197.5V202.5M290 197.5V202.5" style="fill: none; stroke: #1d2330; stroke-width: 0.4px"></path>')
S.append(txt(240,196,"100 mm",2.6,700,anchor="middle",mono=True))
SHEET_INNER="\n".join(s for s in S if s)
open("sheet_inner.svgfrag","w").write(SHEET_INNER)
open("sheet.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="210mm" viewBox="0 0 297 210">{SHEET_INNER}</svg>')

# ---------- Flach vorn: Band auf der Taschenkurve (px) ----------
P=[(367.2,172),(362.4,224.0),(299.2,259.2),(244.0,263.2)]
def bez(t):
    mt=1-t
    x=mt**3*P[0][0]+3*mt*mt*t*P[1][0]+3*mt*t*t*P[2][0]+t**3*P[3][0]
    y=mt**3*P[0][1]+3*mt*mt*t*P[1][1]+3*mt*t*t*P[2][1]+t**3*P[3][1]
    return x,y
N_=4000; pts=[bez(i/N_) for i in range(N_+1)]
arc=[0.0]
for i in range(1,len(pts)): arc.append(arc[-1]+math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]))
Ltot=arc[-1]
def at(s):
    s=max(0,min(Ltot,s)); lo,hi=0,len(arc)-1
    while hi-lo>1:
        m=(lo+hi)//2
        if arc[m]<s: lo=m
        else: hi=m
    x,y=pts[lo]; x2,y2=pts[min(lo+1,len(pts)-1)]
    tx,ty=x2-x,y2-y; l=math.hypot(tx,ty) or 1
    tx,ty=tx/l,ty/l
    return x,y,tx,ty,-ty,tx
u=3.2; ncols=int(Ltot//u); SH=0.0
lead=(Ltot-ncols*u)/2
def quad(col,row):
    s=lead+(col+0.5)*u; x,y,tx,ty,nx,ny=at(s); off=(row-4)*u
    cx,cy=x+nx*(off-SH),y+ny*(off-SH); h=u/2+0.15
    c=[(cx-tx*h-nx*h,cy-ty*h-ny*h),(cx+tx*h-nx*h,cy+ty*h-ny*h),(cx+tx*h+nx*h,cy+ty*h+ny*h),(cx-tx*h+nx*h,cy-ty*h+ny*h)]
    return "M"+"L".join(f"{F(a)} {F(b)}" for a,b in c)+"Z"
def offset_poly(o1,o2,steps=80):
    a=[];b=[]
    for i in range(steps+1):
        s=lead+i*(ncols*u)/steps; x,y,tx,ty,nx,ny=at(s)
        a.append((x+nx*(o1-SH),y+ny*(o1-SH))); b.append((x+nx*(o2-SH),y+ny*(o2-SH)))
    ring=a+b[::-1]
    return "M"+"L".join(f"{F(p)} {F(q)}" for p,q in ring)+"Z"
UF=0.8*FN.CELL
def fquad(col,row,lead_f):
    s_=lead_f+(col+0.5)*UF; x,y,tx,ty,nx,ny=at(s_); off=(row-10)*UF
    cx,cy=x+nx*off,y+ny*off; h=UF/2+0.08
    c=[(cx-tx*h-nx*h,cy-ty*h-ny*h),(cx+tx*h-nx*h,cy+ty*h-ny*h),(cx+tx*h+nx*h,cy+ty*h+ny*h),(cx-tx*h+nx*h,cy-ty*h+ny*h)]
    return "M"+"L".join(f"{F(a)} {F(b)}" for a,b in c)+"Z"
NF=int(Ltot//UF); LEADF=(Ltot-NF*UF)/2
FRONT_BAND=(f'<path d="{offset_poly(-10.5*UF,10.5*UF)}" style="fill: {RED}"></path>\n'
            f'<path d="{"".join(fquad(c,r,LEADF) for (r,c) in sorted(FN.band_white(NF,(3-NF//2)%FN.RAP)))}" style="fill: {WHITE}"></path>')
_cx0=284+(40-37*UF)/2; _cy0=176.8+(40-37*UF)/2
FRONT_COIN=(f'<rect x="{F(_cx0)}" y="{F(_cy0)}" width="{F(37*UF)}" height="{F(37*UF)}" style="fill: {RED}"></rect>'
            f'<path d="{FN.cells_path(sorted(FN.coin_white()),_cx0,_cy0,UF)}" style="fill: {WHITE}"></path>')
_AW,_AR=FN.alatyr_fine()
BACK_ALATYR=(f'<path d="{FN.cells_path(sorted(_AW),307.6,179.2,UF)}" style="fill: {WHITE}"></path>'
             f'<path d="{FN.cells_path(sorted(_AR),307.6,179.2,UF)}" style="fill: {RED}"></path>')
BACK_TREE=tree_at(447.6,144.8,0.8)
BACK_SCENE=f'<g transform="translate(505.4 300) scale(0.8)">{SCENE_NT}</g>'
BACK_EARS=f'<g transform="translate(511.2 262) scale(0.8)">{EARS_T}</g>'
# Taschen-Nahaufnahme in mm (Ursprung = linke obere Ecke der Taschen-Box bei 473.6/239.2 px)
def pocket_close(variant):
    o=[f'<rect x="-14" y="-14" width="172" height="200" style="fill: #2d4668"></rect>',
       f'<path d="M144 0L0 16L0 144L72 172L144 144Z" style="fill: #2f4a6e; stroke: #142236; stroke-width: 0.9px; stroke-linejoin: round"></path>',
       f'<path d="M139 6L5 21L5 140L72 166L139 140Z M144 15L0 31" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>']
    if variant==1:
        o.append(f'<g transform="translate(39.75 63.5)">{SCENE}</g>'); o.append(f'<g transform="translate(47 28.5)">{EARS}</g>')
    else:
        o.append(f'<g transform="translate(39.75 75.5)">{SCENE_NT}</g>'); o.append(f'<g transform="translate(47 28.5)">{EARS_T}</g>')
    return "\n".join(o)
open("pocket_v1.svgfrag","w").write(pocket_close(1)); open("pocket_v2.svgfrag","w").write(pocket_close(2))
for n,v in [("front_band",FRONT_BAND),("front_coin",FRONT_COIN),("back_alatyr",BACK_ALATYR),("back_tree",BACK_TREE),("back_scene",BACK_SCENE),("back_ears",BACK_EARS)]:
    open(n+".svgfrag","w").write(v)
print("Bandlänge px",round(Ltot,1),"Spalten",ncols,"= cm",round(ncols*0.4,1))
for n in ["front_band","front_coin","back_alatyr","back_tree","back_scene","back_ears","sheet_inner"]:
    print(n, len(open(n+".svgfrag").read()))
