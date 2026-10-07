# -*- coding: utf-8 -*-
# D · Lebensbaum-Patch, organisch nach Ernests Referenzfoto. mm, Box 68 x 60. Ohne NL.
import math
F = lambda v: f"{v:.2f}".rstrip('0').rstrip('.')
LINEN="#d9ceb7"; EDGE="#6e4a2a"; DARK="#4a3220"; MID="#6e4a2a"; LIGHT="#9a6a34"; RED="#b3322a"; RIV="#b0703a"; RIVD="#7d4c24"
CX,CY,RC=34,29,22.5

def mirror(d):
    """spiegelt einen Pfad (nur M/C/L/Q mit absoluten Koordinaten) an x=CX"""
    out=[];tok=d.replace(',',' ').split()
    i=0
    res=[]
    for t in tok:
        if t[0].isalpha():
            res.append(t[0]); t=t[1:]
            if not t: continue
        res.append(t)
    # Zahlenpaare spiegeln
    o=[];k=0
    for t in res:
        if t.isalpha(): o.append(t); k=0; continue
        v=float(t)
        o.append(F(2*CX-v) if k%2==0 else F(v)); k+=1
    s=""
    for t in o:
        s+= t if t.isalpha() else " "+t
    return s.strip()

def curl(x,y,r,dirx,up=True,turns=1.1):
    """kleine Spirale am Astende, beginnt in (x,y)"""
    pts=[];n=18
    cx=x+dirx*r*0.0; 
    a0=math.atan2(-1 if up else 1,0)
    for i in range(n+1):
        t=i/n; a=a0+dirx*(t*turns*2*math.pi); rr=r*(1-0.62*t)
        pts.append((x+dirx*r + rr*math.cos(a+math.pi) * 1, y + rr*math.sin(a+math.pi)))
    return "M"+" L".join(f"{F(px)} {F(py)}" for px,py in pts)

def stroke(d,col,w,cap="round"):
    return f'<path d="{d}" style="fill: none; stroke: {col}; stroke-width: {w}px; stroke-linecap: {cap}; stroke-linejoin: round"></path>'

def tree_patch():
    g=[]
    # Patch-Form: oben leichter Bogen, unten Lasche wie im Foto
    outline=("M3 2.5 L20 2.5 C26 2.5 28 0.6 34 0.6 C40 0.6 42 2.5 48 2.5 L65 2.5 Q67.5 2.5 67.5 5 L67.5 50 Q67.5 52.5 65 52.5 "
             "L50 52.5 C44 52.5 43 59.4 34 59.4 C25 59.4 24 52.5 18 52.5 L3 52.5 Q0.5 52.5 0.5 50 L0.5 5 Q0.5 2.5 3 2.5 Z")
    g.append(f'<path d="{outline}" style="fill: {LINEN}; stroke: {EDGE}; stroke-width: 1.2px; stroke-linejoin: round"></path>')
    # Steppkante innen
    inner=("M4 4.6 L20 4.6 C26 4.6 28 2.8 34 2.8 C40 2.8 42 4.6 48 4.6 L64 4.6 Q65.4 4.6 65.4 6 L65.4 49 Q65.4 50.4 64 50.4 "
           "L50 50.4 C43.5 50.4 42.5 57.2 34 57.2 C25.5 57.2 24.5 50.4 18 50.4 L4 50.4 Q2.6 50.4 2.6 49 L2.6 6 Q2.6 4.6 4 4.6 Z")
    g.append(f'<path d="{inner}" style="fill: none; stroke: {LIGHT}; stroke-width: 0.45px; stroke-dasharray: 1.2 0.8"></path>')
    # Kreisrahmen doppelt
    g.append(f'<circle cx="{CX}" cy="{CY}" r="{RC}" style="fill: none; stroke: {LIGHT}; stroke-width: 1px"></circle>')
    g.append(f'<circle cx="{CX}" cy="{CY}" r="{RC-1.5}" style="fill: none; stroke: {LIGHT}; stroke-width: 0.45px; stroke-dasharray: 1.2 0.8"></circle>')
    # Eckranken (links oben, gespiegelt)
    corner_l=["M9.5 6.2 C11 6.4 12.5 7.5 13 9.4 C13.4 11 12.4 12.2 11.2 11.8",
              "M6.4 10 C6.6 11.8 7.6 13.4 9.4 14 C11 14.5 12 13.4 11.6 12.2"]
    corner_lb=["M9.5 46.8 C11 46.6 12.5 45.5 13 43.6 C13.4 42 12.4 40.8 11.2 41.2",
               "M6.4 43 C6.6 41.2 7.6 39.6 9.4 39 C11 38.5 12 39.6 11.6 40.8"]
    for d in corner_l+corner_lb:
        g.append(stroke(d,LIGHT,0.8)); g.append(stroke(mirror(d),LIGHT,0.8))
    # Wurzeln (Mittelbraun), mit Einrollungen
    roots_l=["M31.4 44.4 C28.6 45.8 24.8 46.2 21.2 45.4 C17.8 44.6 15.2 42.6 14.4 40.4 C13.9 38.9 15.2 38 16.4 38.6 C17.4 39.1 17.2 40.4 16.2 40.6",
             "M32.4 45 C30 47.6 26.4 49 22.4 49 C19.8 49 18.2 47.8 18.8 46.4 C19.3 45.4 20.8 45.6 20.9 46.6",
             "M33.2 45.4 C32.2 48.2 29.8 50.4 26.6 51.2 C25 51.6 24 50.8 24.4 49.9",
             "M33.8 45.6 C33.6 47.8 32.6 49.8 31 51.2"]
    for d in roots_l:
        g.append(stroke(d,MID,1.2)); g.append(stroke(mirror(d),MID,1.2))
    g.append(stroke("M34 44.8 L34 50.6",MID,1.2))
    # Seitenschlaufen: verschlungene Astschlingen links/rechts unten in der Krone (wie die Knotenfelder im Foto)
    loop_l=["M32.2 35 C28.6 34.6 25.2 33 22.2 33.2 C18.6 33.4 16 35.6 16.6 38 C17.2 40.2 20.4 40.6 22.6 38.8 C25 36.8 24.2 33.2 21.2 32.2 C18.6 31.4 15.8 32.6 15.2 35",
            "M32.4 37 C29 38.4 26.2 40.6 22.8 41 C20.2 41.3 18.8 40.2 19.2 39",
            "M15.2 35 C14.8 37 15.6 39.6 17.6 40.8"]
    for d in loop_l:
        g.append(stroke(d,LIGHT,0.95)); g.append(stroke(mirror(d),LIGHT,0.95))
    # Krone: Hauptäste steigen aus dem Stamm, schwingen nach außen und rollen sich am Kuppelrand ein
    def pol(a,r): return (CX+r*math.cos(math.radians(a)), CY+r*math.sin(math.radians(a)))
    def spiral(ex,ey,hx,hy,size=1.0,turn=320,n=16):
        """Einrollung ab (ex,ey) in Richtung (hx,hy); dreht links herum (auf dem Bildschirm gegen den Uhrzeiger)"""
        h=math.atan2(hy,hx); x,y=ex,ey; out=[]
        dl=math.radians(turn)/n
        for k in range(n):
            L=size*(0.62-0.40*k/n)
            h-=dl; x+=L*math.cos(h); y+=L*math.sin(h); out.append(f"{F(x)} {F(y)}")
        return " L"+" L".join(out)
    mains=[(-97,18.6,27.0,0.0),(-114,19.0,27.4,0.4),(-131,19.2,27.9,0.8),(-147,18.8,28.6,1.1),(-162,18.2,29.6,1.3),(-176,16.8,31.0,1.4)]
    for i,(a,r,sy,sx) in enumerate(mains):
        ex,ey=pol(a,r); bx,by=33.2-sx,sy
        c1=(bx-0.4-i*0.5, by-7.5+i*0.9)
        c2=(ex+(CX-ex)*0.28, ey+(CY-ey)*0.05-3.2+i*0.6)
        d=f"M{F(bx)} {F(by)} C{F(c1[0])} {F(c1[1])} {F(c2[0])} {F(c2[1])} {F(ex)} {F(ey)}"+spiral(ex,ey,ex-c2[0],ey-c2[1],1.25)
        col=MID if i%2==0 else LIGHT
        g.append(stroke(d,col,1.05)); g.append(stroke(mirror(d),col,1.05))
        if i<5:
            t=0.55; mt=1-t
            qx=mt**3*bx+3*mt*mt*t*c1[0]+3*mt*t*t*c2[0]+t**3*ex
            qy=mt**3*by+3*mt*mt*t*c1[1]+3*mt*t*t*c2[1]+t**3*ey
            fx,fy=pol(a+9,r-5.4)
            cx_,cy_=(qx+fx)/2-0.4,(qy+fy)/2-1.9
            d2=f"M{F(qx)} {F(qy)} Q{F(cx_)} {F(cy_)} {F(fx)} {F(fy)}"+spiral(fx,fy,fx-cx_,fy-cy_,0.85,300,12)
            c2c=LIGHT if i%2==0 else MID
            g.append(stroke(d2,c2c,0.8)); g.append(stroke(mirror(d2),c2c,0.8))
    top="M34 26.8 C33.4 20 34.6 14 34 10"
    g.append(stroke(top,LIGHT,1.05))
    tl="M34 10 C33.2 8.6 31.8 8.2 31 8.9"+spiral(31,8.9,-0.8,0.7,0.7,280,10)
    g.append(stroke(tl,LIGHT,0.95)); g.append(stroke(mirror(tl),LIGHT,0.95))
    # Stamm: gefüllt, darauf drei verdrehte Stränge
    trunk=("M28.4 45.4 C31 44 31.8 41 31.8 37.4 L31.6 30.2 C31.4 28.4 32 26.4 34 26.4 C36 26.4 36.6 28.4 36.4 30.2 "
           "L36.2 37.4 C36.2 41 37 44 39.6 45.4 Z")
    g.append(f'<path d="{trunk}" style="fill: {DARK}"></path>')
    for d,c in [("M32.6 44.4 C35.2 40 32.4 35.4 34.4 30.8 C35 29.4 34.4 27.8 33.4 27.2",MID),
                ("M35.4 44.4 C32.8 40 35.6 35.4 33.6 30.8 C33 29.4 33.6 27.8 34.6 27.2",LIGHT),
                ("M34 44.6 C34.8 41 33.2 37.6 34 34.2",MID)]:
        g.append(stroke(d,c,0.75))
    # rote Akzente wie im Foto: oben, links, rechts, unten
    def rh(x,y,s=1.6):
        return (f'<path d="M{F(x)} {F(y-s)}L{F(x+s)} {F(y)}L{F(x)} {F(y+s)}L{F(x-s)} {F(y)}Z" style="fill: none; stroke: {RED}; stroke-width: 0.7px; stroke-linejoin: round"></path>'
                f'<path d="M{F(x)} {F(y-s-0.9)}V{F(y-s)}M{F(x)} {F(y+s)}V{F(y+s+0.9)}M{F(x-s-0.9)} {F(y)}H{F(x-s)}M{F(x+s)} {F(y)}H{F(x+s+0.9)}" style="fill: none; stroke: {RED}; stroke-width: 0.7px; stroke-linecap: round"></path>')
    g.append(rh(34,3.6,1.2)); g.append(rh(6.2,29)); g.append(rh(61.8,29)); g.append(rh(34,54.4,1.3))
    # Kupfernieten
    for x,y in [(6,8.2),(62,8.2),(6,46.8),(62,46.8)]:
        g.append(f'<circle cx="{F(x)}" cy="{F(y)}" r="2.3" style="fill: {RIV}; stroke: {RIVD}; stroke-width: 0.35px"></circle>')
    return "\n".join(g)

TREE_SVG=tree_patch()
if __name__=="__main__":
    open("tree.svgfrag","w").write(TREE_SVG)
    open("proto/tree.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="816" height="720" viewBox="-2 -2 72 64"><rect x="-2" y="-2" width="72" height="64" style="fill:#2d4668"/>{TREE_SVG}</svg>')
