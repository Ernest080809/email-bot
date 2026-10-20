# -*- coding: utf-8 -*-
# Patch D (Vorlage 20.10.2026) freistellen: weißer Hintergrund und Schatten raus, Form als Alpha-Kanal
import os, sys
import numpy as np, cv2

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "rev6", "skizzen", "2026-10-20_patch_d_form.jpg")
OUT = os.path.join(HERE, "v19", "patch_d.png")

im = cv2.imread(SRC)
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
m = ((hsv[..., 1] > 38) & (hsv[..., 2] < 250)).astype(np.uint8)     # Leinen und Garn, nicht der graue Schatten
m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(m)
i = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
mask = (lab == i).astype(np.uint8)
cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
mask = np.zeros_like(mask); cv2.drawContours(mask, [max(cnts, key=cv2.contourArea)], -1, 1, -1)   # Löcher füllen
x, y, w, h = cv2.boundingRect(mask)
alpha = cv2.GaussianBlur(mask.astype(np.float32) * 255, (0, 0), 1.0)
rgba = np.dstack([im, alpha.astype(np.uint8)])[y:y + h, x:x + w]
cv2.imwrite(OUT, rgba)
print("Patch", w, "x", h, "px, Verhältnis", round(h / w, 3))
