import sys,math; sys.path.insert(0,'/tmp/claude-0/-home-claude/1b46f4ed-4106-5442-ab27-98357078e4eb/scratchpad/design')
import os; os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
from tree2 import knot, OC, GD
def lis(cx,cy,ax,ay,fx,fy,ph,n=260):
    return [(cx+ax*math.sin(fx*t+ph), cy+ay*math.sin(fy*t)) for t in [2*math.pi*i/n for i in range(n+1)]]
def tref(cx,cy,s,n=260):
    return [(cx+s*(math.sin(t)+2*math.sin(2*t))/3, cy+s*(math.cos(t)-2*math.cos(2*t))/3) for t in [2*math.pi*i/n for i in range(n+1)]]
V=[("a 3:2",lis(10,10,6.5,6,3,2,0.5)),("c 3:2 breit",lis(10,10,7.8,5.6,3,2,0.7)),("d Trefoil",tref(10,10,6.5)),("e 3:4",lis(10,10,6.5,6.5,3,4,0.3)),("f 3:2 hoch",lis(10,10,6,7,3,2,0.5))]
o=['<svg xmlns="http://www.w3.org/2000/svg" width="1250" height="300" viewBox="0 0 125 30"><rect width="125" height="30" style="fill:#dacdb1"/>']
for i,(n,P) in enumerate(V):
    o.append(f'<g transform="translate({i*25} 2)">'+"".join(knot(P,0.95,OC))+f'<text x="3" y="27" style="font:2.5px sans-serif">{n}</text></g>')
o.append('</svg>'); open('proto/knots.svg','w').write("".join(o))
