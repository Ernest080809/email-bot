import sys; sys.path.insert(0,'/tmp/claude-0/-home-claude/1b46f4ed-4106-5442-ab27-98357078e4eb/scratchpad/design')
from fine import *
u=CELL
o=['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="700" viewBox="0 0 160 70"><rect width="160" height="70" style="fill:#2d4668"/>']
W=band_white(69,0); o.append(stitched(W,None,21,69,4,4,u))
CW=coin_white(); o.append(stitched(CW,None,37,37,4,36,u))
AW,AR=alatyr_fine(); o.append(stitched(AW,AR,27,27,60,38,u))
o.append('</svg>'); open('/tmp/claude-0/-home-claude/1b46f4ed-4106-5442-ab27-98357078e4eb/scratchpad/design/proto/fine.svg','w').write("".join(o))
