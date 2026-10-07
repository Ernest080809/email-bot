# -*- coding: utf-8 -*-
import math, json
F = lambda v: f"{v:.1f}".rstrip('0').rstrip('.')
WHITE="#f4f1ea"; RED="#b3322a"; GOLD="#d2a53a"; GOLDD="#9c7520"; BROWN="#6e4a2a"; BROWND="#4a3220"; LINEN="#d9ceb7"; TH="#e6c463"

# ---------- Rastermotive ----------
DIAMOND=[(r,c) for r in range(5) for c in range(5) if abs(r-2)+abs(c-2)<=2 and (r,c)!=(2,2)]
STAR_ROWS=["X...X",".X.X.","..X..",".X.X.","X...X"]
STAR=[(r,c) for r in range(5) for c in range(5) if STAR_ROWS[r][c]=="X"]
def band_cells(ncols, start=0):
    """weiße Motivzellen (row 1..5) für ein Band mit ncols Spalten; Rapport 12"""
    out=[]
    for col in range(ncols):
        k=(col+start)%12
        if k<5:   out += [(r+2,col) for (r,c) in DIAMOND if c==k]
        elif 6<=k<11: out += [(r+2,col) for (r,c) in STAR if c==k-6]
    return out
ALATYR_W=[(dy+4,dx+4) for dy in range(-4,5) for dx in range(-4,5)
          if abs(dx)+abs(dy)==4 or max(abs(dx),abs(dy))==3 or (abs(dx)+abs(dy)==1)]
ALATYR_R=[(4,4)]
# E · Münztasche voll: 12 x 12 Einheiten = 48 x 48 mm, weißer Rahmen, rote Atemreihe,
# Mittelraute (Ring s=2 und s=4) mit Strahlen zu den Ecken. Achsen liegen zwischen Zelle 5 und 6.
def _coin(r,c):
    x,y=abs(c-5.5),abs(r-5.5); s=x+y
    if x==5.5 or y==5.5: return 'W'
    if x==y and 5<=s<9: return 'W'
    if x==4.5 or y==4.5: return 'R'
    if s in (2,4): return 'W'
    return 'R'
COIN_N=12
COIN_W=[(r,c) for r in range(COIN_N) for c in range(COIN_N) if _coin(r,c)=='W']
COIN_R=[(r,c) for r in range(COIN_N) for c in range(COIN_N) if _coin(r,c)=='R']
TREE=[
"........R........",
".......RGR.......",
"..G...........G..",
".GGG....T....GGG.",
"..G.T...T...T.G..",
".....T..T..T.....",
"R.....T.T.T.....R",
"...G...TTT...G...",
"..GGGTT.T.TTGGG..",
"...G....T....G...",
"....TTTTTTTTT....",
"....G..G..G..G...",   # placeholder, replaced below
"",
"",
""]
# NL (Gold), Reihen 11-14; N cols 4-7, L cols 10-12
N=["X..X","XX.X","X.XX","X..X"]; L=["X..","X..","X..","XXX"]
rows=[list(r) for r in TREE[:11]]
for i in range(4):
    line=["."]*17
    for j,ch in enumerate(N[i]):
        if ch=="X": line[4+j]="G"
    for j,ch in enumerate(L[i]):
        if ch=="X": line[10+j]="G"
    rows.append(line)
TREE_GRID=["".join(r) for r in rows]
assert all(len(r)==17 for r in TREE_GRID) and len(TREE_GRID)==15
COL={"T":BROWN,"G":GOLD,"R":RED}

def rect_cells(cells, x0, y0, u):
    return "".join(f"M{F(x0+c*u)} {F(y0+r*u)}h{F(u)}v{F(u)}h{F(-u)}z" for (r,c) in cells)

def tree_paths(x0,y0,u):
    out=[]
    for sym,color in COL.items():
        cells=[(r,c) for r,row in enumerate(TREE_GRID) for c,ch in enumerate(row) if ch==sym]
        out.append(f'<path d="{rect_cells(cells,x0,y0,u)}" style="fill: {color}"></path>')
    return "\n".join(out)

# ---------- Serp mit Garbe (mm, Box 76 x 72) ----------
def ear(base, top, pairs=6, rx=1.5, ry=2.7, off=1.7, tilt=28):
    bx,by=base; tx,ty=top
    ang=math.degrees(math.atan2(ty-by, tx-bx))  # Richtung Basis->Spitze
    nx,ny=-(ty-by),(tx-bx); ln=math.hypot(nx,ny); nx,ny=nx/ln,ny/ln
    els=[]
    for i in range(pairs):
        t=0.14+i*(0.78/(pairs-1))
        cx,cy=bx+(tx-bx)*t, by+(ty-by)*t
        for s in (-1,1):
            ex,ey=cx+s*off*nx, cy+s*off*ny
            rot=ang+90 - s*tilt
            els.append(f'<ellipse cx="{F(ex)}" cy="{F(ey)}" rx="{F(rx)}" ry="{F(ry)}" transform="rotate({F(rot)} {F(ex)} {F(ey)})"></ellipse>')
    ex,ey=bx+(tx-bx)*1.0, by+(ty-by)*1.0
    els.append(f'<ellipse cx="{F(ex)}" cy="{F(ey)}" rx="{F(rx*0.9)}" ry="{F(ry)}" transform="rotate({F(ang+90)} {F(ex)} {F(ey)})"></ellipse>')
    return els

def circle_center(p1,p2,r,side):
    (x1,y1),(x2,y2)=p1,p2
    mx,my=(x1+x2)/2,(y1+y2)/2; dx,dy=x2-x1,y2-y1; d=math.hypot(dx,dy)
    h=math.sqrt(max(r*r-(d/2)**2,0)); ux,uy=-dy/d,dx/d
    return (mx+side*h*ux, my+side*h*uy)

def scene(threads=True, sx=0, sy=0, hlen=24.8):
    g=[]
    # Halme
    stalks=[((21,26),(22.6,44)),((24,24),(24,44)),((27,26),(25.4,44))]
    lower=[((22.6,44),(17,64)),((23.3,44),(20.5,65)),((24,44),(24,66)),((24.7,44),(27.5,65)),((25.4,44),(31,64))]
    d=" ".join(f"M{F(a[0])} {F(a[1])}L{F(b[0])} {F(b[1])}" for a,b in stalks)
    g.append(f'<path d="{d}" style="fill: none; stroke: {GOLD}; stroke-width: 1.6px; stroke-linecap: round"></path>')
    d=" ".join(f"M{F(a[0])} {F(a[1])}L{F(b[0])} {F(b[1])}" for a,b in lower)
    g.append(f'<path d="{d}" style="fill: none; stroke: {GOLD}; stroke-width: 1.6px; stroke-linecap: butt"></path>')
    # Goldfäden (von Hand, nach der Wäsche)
    ends=[(17,64),(20.5,65),(24,66),(27.5,65),(31,64),(19,64.6),(29.2,64.6)]
    lens=[16,12,20,14,18,10,13]
    th=[]
    for (x,y),l in zip(ends,lens):
        sway=1.6 if int(x)%2 else -1.6
        th.append(f"M{F(x)} {F(y)}C{F(x+sway)} {F(y+l*0.35)} {F(x-sway)} {F(y+l*0.7)} {F(x+sway*0.5)} {F(y+l)}")
    if threads: g.append(f'<path d="{" ".join(th)}" style="fill: none; stroke: {TH}; stroke-width: 0.6px; stroke-linecap: round"></path>')
    # Ähren
    els=[]
    for base,top in [((21,26),(11,8)),((24,24),(24,3)),((27,26),(37,8))]:
        els+=ear(base,top)
    g.append(f'<g style="fill: {GOLD}; stroke: {GOLDD}; stroke-width: 0.3px">'+"".join(els)+'</g>')
    # Band um die Garbe
    g.append(f'<rect x="18.5" y="42.2" width="11" height="3.6" rx="1.2" transform="rotate(-10 24 44)" style="fill: {BROWN}"></rect>')
    # Serp: Klinge (Weiß), Schneide (Rot innen), Zwinge, Griff (Braun) — kreuzt die Garbe nicht
    C1=(54,30); R=17
    tip=(C1[0]+R*math.cos(math.radians(-155)), C1[1]+R*math.sin(math.radians(-155)))
    ob=(C1[0]+R*math.cos(math.radians(65)), C1[1]+R*math.sin(math.radians(65)))
    ib=(56.2,44.2); r=13.5
    c2=circle_center(tip,ib,r,side=1)
    if math.hypot(c2[0]-C1[0],c2[1]-C1[1])>6: c2=circle_center(tip,ib,r,side=-1)
    blade=(f"M{F(tip[0])} {F(tip[1])}A{R} {R} 0 1 1 {F(ob[0])} {F(ob[1])}"
           f"L{F(ib[0])} {F(ib[1])}A{r} {r} 0 1 0 {F(tip[0])} {F(tip[1])}Z")
    sk=[]
    sk.append(f'<path d="{blade}" style="fill: {WHITE}; stroke: #cfc9bb; stroke-width: 0.3px; stroke-linejoin: round"></path>')
    # rote Schneide: Bogen innen, 1,3 mm in die Klinge versetzt
    r2=r+1.3
    a0=math.atan2(tip[1]-c2[1],tip[0]-c2[0]); a1=math.atan2(ib[1]-c2[1],ib[0]-c2[0])
    p0=(c2[0]+r2*math.cos(a0+0.10), c2[1]+r2*math.sin(a0+0.10))
    p1=(c2[0]+r2*math.cos(a1-0.10), c2[1]+r2*math.sin(a1-0.10))
    sk.append(f'<path d="M{F(p0[0])} {F(p0[1])}A{F(r2)} {F(r2)} 0 1 1 {F(p1[0])} {F(p1[1])}" style="fill: none; stroke: {RED}; stroke-width: 2px; stroke-linecap: round"></path>')
    ux,uy=7.8/24.86,23.6/24.86
    sk.append(f'<path d="M59.4 47.4L{F(59.4+ux*hlen)} {F(47.4+uy*hlen)}" style="fill: none; stroke: {BROWN}; stroke-width: 5px; stroke-linecap: round"></path>')
    sk.append(f'<path d="M58.6 45.2L60.4 50.6" style="fill: none; stroke: {BROWND}; stroke-width: 6.2px; stroke-linecap: butt"></path>')
    if sx or sy: g.append(f'<g transform="translate({F(sx)} {F(sy)})">'+"\n".join(sk)+'</g>')
    else: g+=sk
    return "\n".join(g), dict(tip=(tip[0]+sx,tip[1]+sy), c2=c2)

def ears_line(threads=False):
    g=[]
    g.append(f'<path d="M3 22C10 25.4 40 25.4 47 22" style="fill: none; stroke: {WHITE}; stroke-width: 4px; stroke-linecap: round"></path>')
    g.append(f'<path d="M3 22C10 25.4 40 25.4 47 22" style="fill: none; stroke: {RED}; stroke-width: 2px; stroke-linecap: round"></path>')
    g.append(f'<path d="M21 17L25 19.6M29 17L25 19.6" style="fill: none; stroke: {GOLD}; stroke-width: 1.4px; stroke-linecap: round"></path>')
    els=[]
    for base,top in [((21,17),(13,2)),((29,17),(37,2))]:
        els+=ear(base,top,pairs=5,rx=1.3,ry=2.3,off=1.5)
    g.append(f'<g style="fill: {GOLD}; stroke: {GOLDD}; stroke-width: 0.3px">'+"".join(els)+'</g>')
    if threads:
        # Variante 2: Goldfäden unter den Ähren, kommen unter der Linie heraus, innen in der Tasche verknotet
        def cy(xq):
            best=None
            for i in range(401):
                t=i/400; mt=1-t
                x=mt**3*3+3*mt*mt*t*10+3*mt*t*t*40+t**3*47
                y=mt**3*22+3*mt*mt*t*25.4+3*mt*t*t*25.4+t**3*22
                if best is None or abs(x-xq)<abs(best[0]-xq): best=(x,y)
            return best[1]
        th=[]
        for x,l in zip([19,21,23,25,27,29,31],[10,13,11,16,12,14,9]):
            y=cy(x)+2.4; sway=1.4 if x%4==1 else -1.4
            th.append(f"M{F(x)} {F(y)}C{F(x+sway)} {F(y+l*0.35)} {F(x-sway)} {F(y+l*0.7)} {F(x+sway*0.5)} {F(y+l)}")
        g.append(f'<path d="{" ".join(th)}" style="fill: none; stroke: {TH}; stroke-width: 0.6px; stroke-linecap: round"></path>')
    return "\n".join(g)

SCENE, dbg = scene()
SCENE_NT = scene(False)[0]
EARS_T = ears_line(True)
open("scene_nt.svgfrag","w").write(SCENE_NT); open("ears_t.svgfrag","w").write(EARS_T)
EARS = ears_line()
open("scene.svgfrag","w").write(SCENE); open("ears.svgfrag","w").write(EARS)
json.dump({"TREE":TREE_GRID,"dbg":dbg},open("dbg.json","w"))
print("\n".join(TREE_GRID)); print(dbg)
