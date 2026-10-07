# -*- coding: utf-8 -*-
# D · Lebensbaum-Patch v2 — realistisch nach Ernests Foto. mm, Box 86 x 76. Ohne NL.
import math
F=lambda v: f"{v:.2f}".rstrip('0').rstrip('.')
W,H=86,76; CX=43; RCY=36.5; RING=30
LIN="#dacdb1"; LIN2="#c9b995"; EDGE="#8a6a44"
OUT="#2b1a0e"; B1="#553520"; B2="#734a2b"; CU="#95622f"; OC="#b5832e"; GD="#d2a53a"; HL="#efd592"
RED="#a82c26"; RIV="#b0703a"; RIVD="#6e4424"

def pl(pts): return "M"+" L".join(f"{F(x)} {F(y)}" for x,y in pts)
def bez(p0,p1,p2,p3,n=40):
    out=[]
    for i in range(n+1):
        t=i/n; m=1-t
        out.append((m**3*p0[0]+3*m*m*t*p1[0]+3*m*t*t*p2[0]+t**3*p3[0], m**3*p0[1]+3*m*m*t*p1[1]+3*m*t*t*p2[1]+t**3*p3[1]))
    return out
def curl_pts(p,prev,size=1.3,turn=330,n=16,sign=-1):
    """Spirale am Ende, sign -1 = gegen den Uhrzeiger (Bildschirm)"""
    h=math.atan2(p[1]-prev[1],p[0]-prev[0]); x,y=p; out=[]
    dl=math.radians(turn)/n
    for k in range(n):
        L=size*(0.62-0.40*k/n); h+=sign*dl; x+=L*math.cos(h); y+=L*math.sin(h); out.append((x,y))
    return out
def rope(pts,w,col,hl=HL,o=OUT,hlw=0.3,cap="round"):
    d=pl(pts)
    return [f'<path d="{d}" style="fill: none; stroke: {o}; stroke-width: {F(w+0.55)}px; stroke-linecap: {cap}; stroke-linejoin: round"></path>',
            f'<path d="{d}" style="fill: none; stroke: {col}; stroke-width: {F(w)}px; stroke-linecap: {cap}; stroke-linejoin: round"></path>',
            f'<path d="{d}" style="fill: none; stroke: {hl}; stroke-width: {F(w*hlw)}px; stroke-linecap: {cap}; stroke-linejoin: round; opacity: 0.55"></path>']
def mir(pts): return [(2*CX-x,y) for x,y in pts]

def self_crossings(P):
    """Schnittpunkte eines geschlossenen Polygonzugs: Liste (i,j,x,y) mit i<j Segmentindizes"""
    n=len(P); res=[]
    for i in range(n-1):
        a,b=P[i],P[i+1]
        for j in range(i+2,n-1):
            if i==0 and j==n-2: continue
            c,d=P[j],P[j+1]
            den=(b[0]-a[0])*(d[1]-c[1])-(b[1]-a[1])*(d[0]-c[0])
            if abs(den)<1e-12: continue
            t=((c[0]-a[0])*(d[1]-c[1])-(c[1]-a[1])*(d[0]-c[0]))/den
            u=((c[0]-a[0])*(b[1]-a[1])-(c[1]-a[1])*(b[0]-a[0]))/den
            if 0<=t<1 and 0<=u<1: res.append((i+t,j+u))
    return res
def knot(P,w,col):
    """alternierendes Über-Unter: ganzen Strang zeichnen, dann die 'Über'-Stücke erneut obenauf"""
    out=rope(P,w,col)
    cr=self_crossings(P)
    ev=sorted([(a,k,0) for k,(a,b) in enumerate(cr)]+[(b,k,1) for k,(a,b) in enumerate(cr)])
    for idx,(pos,k,_) in enumerate(ev):
        if idx%2==0:   # jede zweite Begegnung liegt oben
            i=int(pos); seg=P[max(0,i-4):min(len(P),i+6)]
            out+=rope(seg,w,col,cap="butt")
    return out

def tree_patch2():
    g=[]
    g.append('<defs><pattern id="nvlLinen" x="0" y="0" width="0.9" height="0.9" patternUnits="userSpaceOnUse">'
             f'<rect x="0" y="0" width="0.9" height="0.9" style="fill: {LIN}"></rect>'
             f'<path d="M0 0.45H0.9M0.45 0V0.9" style="fill: none; stroke: {LIN2}; stroke-width: 0.16px; opacity: 0.7"></path></pattern></defs>')
    outline=(f"M4 3.2 L26 3.2 C33 3.2 35 0.8 43 0.8 C51 0.8 53 3.2 60 3.2 L82 3.2 Q85.2 3.2 85.2 6.4 L85.2 66 Q85.2 69.2 82 69.2 "
             f"L62 69.2 C54 69.2 53 75.4 43 75.4 C33 75.4 32 69.2 24 69.2 L4 69.2 Q0.8 69.2 0.8 66 L0.8 6.4 Q0.8 3.2 4 3.2 Z")
    g.append(f'<path d="{outline}" style="fill: url(#nvlLinen); stroke: {EDGE}; stroke-width: 0.9px; stroke-linejoin: round"></path>')
    inner=(f"M5 5.4 L26 5.4 C33 5.4 35 3 43 3 C51 3 53 5.4 60 5.4 L81 5.4 Q83 5.4 83 7.4 L83 65 Q83 67 81 67 "
           f"L62 67 C54.5 67 53.5 73.2 43 73.2 C32.5 73.2 31.5 67 24 67 L5 67 Q3 67 3 65 L3 7.4 Q3 5.4 5 5.4 Z")
    g.append(f'<path d="{inner}" style="fill: none; stroke: {CU}; stroke-width: 0.45px; stroke-dasharray: 1.3 0.7"></path>')
    # Ring: gedrehte Goldkordel
    for r,col,w in [(RING,OC,1.3),(RING-2.2,CU,0.7)]:
        g.append(f'<circle cx="{CX}" cy="{RCY}" r="{r}" style="fill: none; stroke: {OUT}; stroke-width: {F(w+0.5)}px"></circle>')
        g.append(f'<circle cx="{CX}" cy="{RCY}" r="{r}" style="fill: none; stroke: {col}; stroke-width: {F(w)}px"></circle>')
    g.append(f'<circle cx="{CX}" cy="{RCY}" r="{RING}" style="fill: none; stroke: {HL}; stroke-width: 1.1px; stroke-dasharray: 0.5 0.9; opacity: 0.8"></circle>')
    # Eckranken
    corner=[bez((10,7.5),(15,7.5),(18.5,10.5),(17.5,14.5),20)+curl_pts((17.5,14.5),(17.8,13.5),1.0,300,12,1),
            bez((6.5,12),(6.5,17),(9.5,20),(13,19.5),20)+curl_pts((13,19.5),(12,19.8),0.9,300,12,-1)]
    for c in corner:
        for pts in (c, mir(c), [(x,2*RCY-y) for x,y in c], [(2*CX-x,2*RCY-y) for x,y in c]):
            g+=rope(pts,0.75,OC)
    # --- Wurzeln ---
    N=10
    def trunk_x(y,i):
        w=3.9-1.3*math.exp(-((y-44)/5)**2)+0.6*max(0,(36-y)/4)
        th=2*math.pi*(53-y)/15+2*math.pi*i/N
        return CX+w*math.sin(th), math.cos(th)
    base=sorted(range(N),key=lambda i: trunk_x(53,i)[0])
    top=sorted(range(N),key=lambda i: trunk_x(31.5,i)[0])
    roots=[]
    for k,i in enumerate(base):
        bx,_=trunk_x(53,i)
        b=math.radians(162-k*(144/(N-1)))
        r=21+2.5*math.sin(k*1.7)
        E=(CX+r*math.cos(b), 45+r*0.62*math.sin(b)+4)
        S=(bx,53)
        pts=bez(S,(S[0]+(E[0]-S[0])*0.15,S[1]+5),(E[0]-(E[0]-S[0])*0.25,E[1]+1.5),E,30)
        pts+=curl_pts(E,pts[-2],1.2,320,14,-1 if E[0]<CX else 1)
        roots.append((pts,[B2,CU,B1,OC][k%4]))
    for pts,col in roots: g+=rope(pts,0.95,col)
    # --- Seitenknoten (Lissajous 3:2, echtes Über-Unter) ---
    def tref(cx,cy,sx,sy,rot,n=300):
        out=[]
        for i in range(n+1):
            t=2*math.pi*i/n
            x=(math.sin(t)+2*math.sin(2*t))/3; y=(math.cos(t)-2*math.cos(2*t))/3
            c,s_=math.cos(rot),math.sin(rot)
            xr,yr=x*c-y*s_, x*s_+y*c
            out.append((cx+sx*xr, cy+sy*yr))
        return out
    con=bez((40.6,43.2),(37.4,41.8),(34.2,42.2),(31.2,44.6),20)
    g+=rope(con,0.9,GD); g+=rope(mir(con),0.9,GD)
    KL=tref(25.2,45.2,7.4,6.2,math.radians(-90),200)
    g+=knot(KL,0.95,OC); g+=knot(mir(KL),0.95,OC)
    # --- Stamm: gedrehte Stränge, hinten dunkel, vorn hell ---
    ys=[53-i*0.4 for i in range(int((53-31.5)/0.4)+1)]+[31.5]
    runs=[]
    for i in range(N):
        pts=[(trunk_x(y,i)[0],y) for y in ys]; dep=[trunk_x(y,i)[1] for y in ys]
        def cls(d): return 2 if d>0.55 else (1 if d>0.15 else (0 if d>-0.2 else -1))
        cur=[pts[0]]; cd=[dep[0]]; c0=cls(dep[0])
        for j in range(1,len(ys)):
            cur.append(pts[j]); cd.append(dep[j])
            c=cls(dep[j])
            if c!=c0 or j==len(ys)-1:
                runs.append((sum(cd)/len(cd),c0,i,cur)); cur=[pts[j]]; cd=[dep[j]]; c0=c
    runs.sort(key=lambda r: r[0])
    g.append(f'<path d="M{F(CX-4.3)} 53.4 C{F(CX-2.6)} 48 {F(CX-2.8)} 40 {F(CX-3.6)} 31.4 L{F(CX+3.6)} 31.4 C{F(CX+2.8)} 40 {F(CX+2.6)} 48 {F(CX+4.3)} 53.4 Z" style="fill: {OUT}"></path>')
    for dm,c,i,pts in runs:
        col={2:[B2,CU,OC,B2,GD][i%5],1:[B2,CU,OC,B2,GD][i%5],0:B2,-1:B1}[c]
        d=pl(pts)
        g.append(f'<path d="{d}" style="fill: none; stroke: {OUT}; stroke-width: 1.65px; stroke-linecap: round; stroke-linejoin: round"></path>')
        g.append(f'<path d="{d}" style="fill: none; stroke: {col}; stroke-width: 1.2px; stroke-linecap: round; stroke-linejoin: round"></path>')
        if c==2: g.append(f'<path d="{d}" style="fill: none; stroke: {HL}; stroke-width: 0.35px; stroke-linecap: round; opacity: 0.5"></path>')
    # --- Krone: Äste verlassen den Stamm schräg, wölben sich zur Kuppel und hängen außen über ---
    def branch(S,E,s_ang,e_ang,n=40):
        L=math.hypot(E[0]-S[0],E[1]-S[1])
        c1=(S[0]+0.42*L*math.cos(s_ang), S[1]+0.42*L*math.sin(s_ang))
        c2=(E[0]-0.38*L*math.cos(e_ang), E[1]-0.38*L*math.sin(e_ang))
        return bez(S,c1,c2,E,n)
    AC=(CX,30.5)
    limbs=[]
    for k,i in enumerate(top):
        sx,_=trunk_x(31.5,i); S=(sx,31.5)
        a=-176+k*(172/(N-1)); ar=math.radians(a)
        E=(AC[0]+24.2*math.cos(ar), AC[1]+21.5*math.sin(ar))
        sgn=-1 if E[0]<CX else 1
        s_ang=math.radians(-90+0.55*(a+90))
        e_ang=math.radians(a+sgn*(-1)*0+ (28 if E[0]>CX else -28)*abs(math.cos(ar)))
        pts=branch(S,E,s_ang,e_ang,28)
        tip=pts+curl_pts(E,pts[-2],1.3,330,15,sgn)
        col=[GD,OC,CU,GD,OC,CU,GD,OC,CU,GD][k]
        limbs.append((tip,col,1.05))
        # Zweige: zwei je Ast, nach außen versetzt
        for t0,da,rr,sz in [(0.42,15,0.72,0.95),(0.66,-11,0.86,0.8)]:
            j=int(t0*28); P0=pts[j]
            a2=math.radians(a+da*(1 if E[0]>CX else -1)*(-1))
            E2=(AC[0]+24.2*rr*math.cos(a2), AC[1]+21.5*rr*math.sin(a2))
            tang=math.atan2(pts[j+1][1]-pts[j-1][1],pts[j+1][0]-pts[j-1][0])
            e2=math.atan2(E2[1]-P0[1],E2[0]-P0[0])+(0.5 if E2[0]>CX else -0.5)
            tw=branch(P0,E2,tang,e2,18)
            tw+=curl_pts(E2,tw[-2],sz,310,12,sgn)
            limbs.append((tw,[OC,GD,CU][(k+int(t0*10))%3],0.82))
    for pts,col,w in limbs: g+=rope(pts,w,col)
    # rote Akzente: kleine Kreuzstich-Rauten
    def rh(x,y,s=1.8):
        cells=[(0,-2),(-1,-1),(1,-1),(-2,0),(2,0),(-1,1),(1,1),(0,2)]
        q=s/2
        return "".join(f'<path d="M{F(x+cx*q-q/2)} {F(y+cy*q-q/2)}l{F(q)} {F(q)}M{F(x+cx*q+q/2)} {F(y+cy*q-q/2)}l{F(-q)} {F(q)}" style="fill: none; stroke: {RED}; stroke-width: 0.42px; stroke-linecap: round"></path>' for cx,cy in cells)
    for x,y in [(CX,3.9),(6.4,RCY),(W-6.4,RCY),(CX,71)]:
        g.append(rh(x,y))
    # Kupfernieten
    for x,y in [(6.6,9.4),(79.4,9.4),(6.6,63),(79.4,63)]:
        g.append(f'<circle cx="{F(x)}" cy="{F(y)}" r="2.7" style="fill: {RIV}; stroke: {RIVD}; stroke-width: 0.4px"></circle>')
        g.append(f'<circle cx="{F(x-0.7)}" cy="{F(y-0.7)}" r="0.9" style="fill: #d49a62; opacity: 0.7"></circle>')
    return "\n".join(g)

TREE2=tree_patch2()
if __name__=="__main__":
    open("tree2.svgfrag","w").write(TREE2)
    open("proto/tree2.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1032" height="912" viewBox="-0 -0 86 76"><rect width="86" height="76" style="fill:#2d4668"/>{TREE2}</svg>')
    print(len(TREE2))
