# -*- coding: utf-8 -*-
# Patch D ohne die vier Druckknöpfe (sie sitzen versteckt hinter dem Patch und werden nicht gestickt), 05.11.2026
#   Eingang v19/patch_d.png (aus patch_cut.py), Ausgang v19/patch_d_clean.png. Die Ecken werden mit Leinen-Struktur aus der Nähe gefüllt.
import os
import cv2, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
im = cv2.imread(os.path.join(HERE, "v19", "patch_d.png"), cv2.IMREAD_UNCHANGED)
bgr, alpha = im[..., :3].copy(), im[..., 3]
SNAPS = [(50, 112), (817, 112), (55, 653), (807, 653)]     # Mitte der Kupferkappen in px, Radius etwa 33 px
mask = np.zeros(alpha.shape, np.uint8)
for x, y in SNAPS:
    cv2.circle(mask, (x, y), 38, 255, -1)
fill = cv2.inpaint(bgr, mask, 12, cv2.INPAINT_TELEA)
# Leinen-Struktur: feines Rauschen aus einer glatten Leinenfläche oben in der Mitte zurück auf die gefüllten Kreise
src = bgr[18:58, 300:380].astype(np.float32)
tex = src - cv2.GaussianBlur(src, (0, 0), 3)
h, w = tex.shape[:2]
tile = np.tile(tex, (alpha.shape[0] // h + 1, alpha.shape[1] // w + 1, 1))[:alpha.shape[0], :alpha.shape[1]]
soft = cv2.GaussianBlur(mask.astype(np.float32) / 255, (0, 0), 2)[..., None]
out = np.clip(fill.astype(np.float32) + tile * soft, 0, 255).astype(np.uint8)
cv2.imwrite(os.path.join(HERE, "v19", "patch_d_clean.png"), np.dstack([out, alpha]))
print("ok")
