import sys; sys.path.insert(0,'/tmp/claude-0/-home-claude/1b46f4ed-4106-5442-ab27-98357078e4eb/scratchpad/design')
import os; os.chdir('..'); from elements import WHITE,RED,rect_cells,F; os.chdir('coin')
N=12
def xy(r,c): return abs(c-5.5),abs(r-5.5)
def frame(r,c): x,y=xy(r,c); return x==5.5 or y==5.5
def ring(r,c): x,y=xy(r,c); return (x==4.5 or y==4.5) and not frame(r,c)
C={}
def R1(r,c):
    if frame(r,c): return 'W'
    if ring(r,c): return 'R'
    x,y=xy(r,c); s=x+y
    if s in (2,4): return 'W'
    if (x,y)==(3.5,3.5): return 'W'
    return 'R'
C['R1']=R1
def R2(r,c):
    if frame(r,c): return 'W'
    x,y=xy(r,c); s=x+y
    if x==y and s>=5: return 'W'          # Strahlen zu den Ecken
    if ring(r,c): return 'R'
    if s in (2,4): return 'W'
    return 'R'
C['R2']=R2
def R3(r,c):
    if frame(r,c): return 'W'
    x,y=xy(r,c); s=x+y
    if x==y and s>=5 and s<9: return 'W'
    if ring(r,c): return 'R'
    if s in (2,4): return 'W'
    if (x,y) in [(0.5,4.5),(4.5,0.5)]: return 'R'
    # kleine Häkchen an den Seiten: (0.5,3.5)=Spitze, daneben Punkt aussen
    if s==6 and abs(x-y)==4: return 'W'   # (1.5,4.5)? nein -> (0.5,5.5) frame; => (x,y)=(1,5)? n/a
    return 'R'
C['R3']=R3
def R4(r,c):   # Gitter: diagonale weisse Linien, rote Rauten mit weissem Punkt
    if frame(r,c): return 'W'
    x,y=xy(r,c); s=x+y; t=abs(x-y)
    if ring(r,c): return 'R'
    if s==4 or (t==0 and s>=5): return 'W'
    if s==1: return 'W'
    if (x,y) in [(3.5,1.5),(1.5,3.5)]: return 'W'
    return 'R'
C['R4']=R4
def R5(r,c):   # R2 + Punkte in den Seitenfeldern
    v=R2(r,c)
    x,y=xy(r,c)
    if not frame(r,c) and not ring(r,c) and (x,y) in [(0.5,5.5)]: return 'W'
    if (x,y) in [(3.5,1.5),(1.5,3.5)]: return 'R'
    if (x,y) in [(0.5,4.5),(4.5,0.5)] : return 'W'
    return v
C['R5']=R5
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1250" height="300" viewBox="0 0 312.5 75"><rect width="312.5" height="75" style="fill:#efece5"/>']
for i,(k,f) in enumerate(C.items()):
    x0=6+i*61; y0=10
    svg.append(f'<rect x="{x0-4}" y="{y0-4}" width="56" height="56" style="fill:#2d4668"/>')
    W=[(r,c) for r in range(N) for c in range(N) if f(r,c)=='W']
    R=[(r,c) for r in range(N) for c in range(N) if f(r,c)=='R']
    svg.append(f'<path d="{rect_cells(R,x0,y0,4)}" style="fill:{RED}"/><path d="{rect_cells(W,x0,y0,4)}" style="fill:{WHITE}"/>')
    svg.append(f'<text x="{x0}" y="{y0+56}" style="font:4px sans-serif">{k}</text>')
svg.append('</svg>')
open('cand2.svg','w').write("".join(svg))
