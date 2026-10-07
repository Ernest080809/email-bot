# -*- coding: utf-8 -*-
# Feines Kreuzstich-Raster: 1 Zelle = 4/3 mm (ein Drittel des alten 4-mm-Moduls)
import math
F=lambda v: f"{v:.2f}".rstrip('0').rstrip('.')
CELL=4/3
WHITE="#f4f1ea"; RED="#b3322a"; REDD="#962720"; REDL="#c4423a"; WHT2="#dcd6c9"

# ---------- A · Taschenband ----------
# v1.4: 21 Reihen = 28 mm · v1.5: 17 Reihen = 22,7 mm (Punktlinien entfallen, Zickzack und Motive bleiben)
BAND_ROWS=17; RAP=16
def band_white(ncols,start=0,rows=None):
    rows = rows or BAND_ROWS
    W=set(); mid=rows//2
    for c in range(ncols):
        k=(c+start)
        z={0:1,1:2,2:3,3:2}[k%4]
        W.add((z,c)); W.add((rows-1-z,c))
        if rows>=21 and k%2==0: W.add((5,c)); W.add((rows-6,c))
        m=k%RAP
        if m<7:
            dx=m-3
            for dy in range(-3,4):
                d=abs(dx)+abs(dy)
                if d in (2,3) or d==0: W.add((mid+dy,c))
        elif 8<=m<15:
            dx=m-11
            for dy in range(-3,4):
                if (dx==0 and abs(dy)<=3) or (dy==0 and abs(dx)<=3) or (abs(dx)==abs(dy) and abs(dx)<=2):
                    if not (dx==0 and dy==0): W.add((mid+dy,c))
    return W

# ---------- E · Münztasche ----------
# v1.4: 37 x 37 = 49 mm · v1.5: 45 x 45 = 60 mm (Tasche 62 x 62 mm)
COIN_N=45
def coin_white(N=None):
    N=N or COIN_N; W=set(); h=N//2
    for c in range(N):
        x=c-h
        z={0:3,1:2,2:1,3:2}[abs(x)%4]
        W.add((z,c))
        if x%2==0: W.add((5,c))
    for r in range(7,N):
        for c in range(N):
            x=c-h; y=r-7
            if (x+y)%8==0 or (x-y)%8==0: W.add((r,c))
            if ((x%8==4 and y%8==0) or (x%8==0 and y%8==4)) and y>0:
                for dr,dc in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
                    if 7<=r+dr<N and 0<=c+dc<N: W.add((r+dr,c+dc))
    return W

# ---------- C · Alatyr, 27 x 27 = 36 mm ----------
def alatyr_fine():
    N=27; W=set(); R=set()
    def inside(dx,dy,a,b): return (max(abs(dx),abs(dy))<=a) or (abs(dx)+abs(dy)<=b)
    for r in range(N):
        for c in range(N):
            dx=c-13; dy=r-13
            o=inside(dx,dy,9,13); i1=inside(dx,dy,7,10); i2=inside(dx,dy,5,7)
            if o and not i1: W.add((r,c))            # äußere Sternkontur, 2 Zellen
            elif i2 and not inside(dx,dy,4,5): W.add((r,c))   # innere Kontur
            elif abs(dx)+abs(dy)<=2 and not (dx==0 and dy==0): W.add((r,c))  # Kernraute
            elif dx==0 and dy==0: R.add((r,c))
            elif i1 and not i2: R.add((r,c))          # roter Ring zwischen den Konturen
    return W,R

def cells_path(cells,x0,y0,u):
    return "".join(f"M{F(x0+c*u)} {F(y0+r*u)}h{F(u)}v{F(u)}h{F(-u)}z" for (r,c) in cells)
def xstitch(cells,x0,y0,u,col,w):
    i=u*0.12
    d="".join(f"M{F(x0+c*u+i)} {F(y0+r*u+i)}l{F(u-2*i)} {F(u-2*i)}M{F(x0+c*u+u-i)} {F(y0+r*u+i)}l{F(-(u-2*i))} {F(u-2*i)}" for (r,c) in cells)
    return f'<path d="{d}" style="fill: none; stroke: {col}; stroke-width: {F(w)}px; stroke-linecap: round"></path>'
def stitched(W,Rset,rows,cols,x0,y0,u):
    """1:1-Darstellung mit Kreuzstich-Textur: roter Grund, jede Zelle ein Kreuz"""
    allc=[(r,c) for r in range(rows) for c in range(cols)]
    red=[p for p in allc if p not in W] if Rset is None else list(Rset)
    o=[f'<path d="{cells_path(red,x0,y0,u)}" style="fill: {REDD}"></path>',
       f'<path d="{cells_path(sorted(W),x0,y0,u)}" style="fill: {WHT2}"></path>',
       xstitch(red,x0,y0,u,REDL,u*0.3), xstitch(sorted(W),x0,y0,u,WHITE,u*0.34)]
    return "\n".join(o)
