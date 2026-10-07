import sys; sys.path.insert(0,'/tmp/claude-0/-home-claude/1b46f4ed-4106-5442-ab27-98357078e4eb/scratchpad/design')
import os; os.chdir('..')
from elements import WHITE,RED,rect_cells,F
os.chdir('coin')
N=12
def frame(r,c): return r in (0,N-1) or c in (0,N-1)
def d(r,c): return abs(c-5.5)+abs(r-5.5)
cands={}
# V1: gerahmte konzentrische Rauten, Spitzen hängen am Rahmen
def v1(r,c):
    if frame(r,c): return 'W'
    k=d(r,c)
    return {1:'R',2:'W',3:'W',4:'R',5:'W',6:'R',7:'W',8:'R',9:'R'}[int(k)]
cands['v1']=v1
# V2: Rahmen + Atemreihe + 4 kleine Rauten (3x3) + Mittelraute
def v2(r,c):
    if frame(r,c): return 'W'
    k=d(r,c)
    if k in (1,): return 'R'
    if k in (2,3): return 'W'
    # Eckmotive: kleine Raute um (2.5,2.5)-Zentren -> Zellen um (2,2)... gespiegelt
    x=abs(c-5.5); y=abs(r-5.5)   # 0.5..4.5
    if abs(x-3.5)+abs(y-3.5)<=1 and not (x==3.5 and y==3.5): return 'W'
    if (x,y) in [(4.5,0.5),(0.5,4.5)]: return 'W'
    return 'R'
cands['v2']=v2
# V3: Diagonal-Gitter (Vyshyvanka-Flächenmuster) mit Punkten
def v3(r,c):
    if frame(r,c): return 'W'
    x=abs(c-5.5); y=abs(r-5.5)
    s=x+y; t=abs(x-y)
    if s in (1,) : return 'R'
    if s==3 or t==3 and s>3: return 'W'
    if s==2: return 'W'
    if (x,y) in [(4.5,4.5),(3.5,3.5)] : return 'R'
    if s==6 and t==0: return 'W'
    return 'R'
cands['v3']=v3
# V4: grosse Raute mit X-Haken (Widderhoerner) Ecken
def v4(r,c):
    if frame(r,c): return 'W'
    x=abs(c-5.5); y=abs(r-5.5); s=x+y
    if s==1: return 'R'
    if s in (2,3): return 'W'
    if s==4: return 'R'
    if s==5: return 'W'
    if s==6: return 'R'
    if (x,y) in [(4.5,4.5)]: return 'W'
    if (x,y) in [(3.5,3.5)]: return 'W'
    return 'R'
cands['v4']=v4
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="300" viewBox="0 0 250 75"><rect width="250" height="75" style="fill:#efece5"/>']
for i,(k,f) in enumerate(cands.items()):
    x0=6+i*61; y0=10
    svg.append(f'<rect x="{x0-4}" y="{y0-4}" width="56" height="56" style="fill:#2d4668"/>')
    W=[(r,c) for r in range(N) for c in range(N) if f(r,c)=='W']
    R=[(r,c) for r in range(N) for c in range(N) if f(r,c)=='R']
    svg.append(f'<path d="{rect_cells(R,x0,y0,4)}" style="fill:{RED}"/><path d="{rect_cells(W,x0,y0,4)}" style="fill:{WHITE}"/>')
    svg.append(f'<text x="{x0}" y="{y0+56}" style="font:4px sans-serif">{k}</text>')
svg.append('</svg>')
open('cand.svg','w').write("".join(svg))
