import sys,os; sys.path.insert(0,'/tmp/claude-0/-home-claude/1b46f4ed-4106-5442-ab27-98357078e4eb/scratchpad/design'); os.chdir('/tmp/claude-0/-home-claude/1b46f4ed-4106-5442-ab27-98357078e4eb/scratchpad/design/proto')
from elements import scene
V=[(-13,11,16,'c -13/+11'),(-15,12,15,'e -15/+12'),(-16,14,13,'f -16/+14')]
o=['<svg xmlns="http://www.w3.org/2000/svg" width="1350" height="495" viewBox="0 0 270 99"><rect width="270" height="99" style="fill:#2d4668"/>']
for i,(dx,dy,hl,n) in enumerate(V):
    sc,d=scene(False,dx,dy,hl)
    o.append(f'<g transform="translate({4+i*89} 4)">{sc}<text x="2" y="92" style="font:4px sans-serif;fill:#fff">{n}</text></g>')
o.append('</svg>'); open('scene_try.svg','w').write("".join(o))
