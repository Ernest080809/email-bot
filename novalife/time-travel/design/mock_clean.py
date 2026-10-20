# -*- coding: utf-8 -*-
# Mockup v1.9, Schritt 1: Referenzfoto bereinigen (Löcher, fremdes Label, alte Gesäßtaschen) und 2x hochskalieren
import os, sys
import numpy as np, cv2

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "rev6", "skizzen", "2026-10-17_referenz_fit_baggy.jpg")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "v19", "mock_base.png")

img = cv2.imread(SRC)
H, W = img.shape[:2]
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)

# Jeans-Maske: alles, was nicht weißer Hintergrund ist und mit dem Rand verbunden ist
bg = ((hsv[..., 1] < 18) & (hsv[..., 2] > 235)).astype(np.uint8)
ff = bg.copy(); fmask = np.zeros((H + 2, W + 2), np.uint8)
for seed in [(0, 0), (W - 1, 0), (0, H - 1), (W - 1, H - 1), (W // 2, 0), (W // 2, H - 1)]:
    if ff[seed[1], seed[0]] == 1:
        cv2.floodFill(ff, fmask, seed, 2)
jeans = (ff != 2).astype(np.uint8)
inner = cv2.erode(jeans, np.ones((7, 7), np.uint8))

# Löcher und Ausfransungen: heller als die Umgebung und fast ohne Farbe
local = cv2.GaussianBlur(gray, (0, 0), 9)
spec = (gray - local > 16) & (hsv[..., 1] < 58) & (inner == 1)
spec |= (hsv[..., 1] < 28) & (hsv[..., 2] > 218) & (inner == 1)
spec = spec.astype(np.uint8)
spec = cv2.morphologyEx(spec, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
spec = cv2.dilate(spec, np.ones((4, 4), np.uint8))

# Fremdes Label hinten: Bund daneben klonen
lab = (936, 108, 1012, 152)
src = img[lab[1]:lab[3], lab[0] - 70:lab[2] - 70].copy()
img[lab[1]:lab[3], lab[0]:lab[2]] = src
seam = np.zeros((H, W), np.uint8)
cv2.rectangle(seam, (lab[0] - 2, lab[1]), (lab[0] + 2, lab[3]), 1, -1)
cv2.rectangle(seam, (lab[2] - 2, lab[1]), (lab[2] + 2, lab[3]), 1, -1)

# Alte Gesäßtaschen (größer als unsere): Kontur und Steppnähte entfernen
OLD = [np.array([(673, 233), (826, 233), (811, 362), (738, 397), (679, 361)], np.int32),
       np.array([(900, 233), (1040, 232), (1031, 363), (972, 398), (912, 360)], np.int32)]
pk = np.zeros((H, W), np.uint8)
for poly in OLD:
    # Seiten und Spitze; die alte Oberkante liegt fast genau auf unserer und bleibt
    cv2.polylines(pk, [np.vstack([poly[1:], poly[:1]])], False, 1, 30)
# alte linke Tasche ist breiter als unsere (140 px): überstehende Enden der alten Oberkante weg
cv2.rectangle(pk, (666, 222), (683, 256), 1, -1)
cv2.rectangle(pk, (816, 222), (834, 256), 1, -1)

# Saum: ausgefranste Stellen und Löcher an der Saumkante schließen, Flecken dort strenger erkennen
yy = np.arange(H)[:, None] > H * 0.84
closed = np.zeros_like(jeans)                       # je Jeans einzeln schließen, sonst wächst die Lücke zwischen vorn und hinten zu
ncomp, comp = cv2.connectedComponents(jeans)
for c in range(1, ncomp):
    part = (comp == c).astype(np.uint8)
    if part.sum() > 20000:
        closed |= cv2.morphologyEx(part, cv2.MORPH_CLOSE, np.ones((31, 31), np.uint8))
notch = ((closed == 1) & (jeans == 0) & yy).astype(np.uint8)
hem = ((gray - local > 8) & (hsv[..., 1] < 75) & (closed == 1) & yy).astype(np.uint8)
edge = np.arange(H)[:, None] > H * 0.955                 # unterste Saumkante: Fransen ohne Farbe
hem |= ((hsv[..., 1] < 60) & (closed == 1) & edge).astype(np.uint8)
hem |= (((hsv[..., 0] < 85) | (hsv[..., 0] > 135)) & (hsv[..., 1] > 25) & (closed == 1) & yy).astype(np.uint8)   # braune Flecken
hem = cv2.dilate(hem, np.ones((5, 5), np.uint8)) | cv2.dilate(notch, np.ones((3, 3), np.uint8))

mask = ((spec | seam | pk | hem) > 0).astype(np.uint8) * 255
clean = cv2.inpaint(img, mask, 4, cv2.INPAINT_TELEA)

# Denim-Körnung in den gefüllten Flächen nachbilden
rng = np.random.default_rng(7)
noise = rng.normal(0, 1, (H, W)).astype(np.float32)
noise = cv2.GaussianBlur(noise, (0, 0), 0.8) * 6
streak = cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (1, 0), sigmaX=0.6, sigmaY=4) * 4
m = cv2.GaussianBlur(mask.astype(np.float32) / 255, (0, 0), 1.5)[..., None]
clean = np.clip(clean.astype(np.float32) + (noise + streak)[..., None] * m, 0, 255).astype(np.uint8)

big = cv2.resize(clean, (W * 2, H * 2), interpolation=cv2.INTER_LANCZOS4)
cv2.imwrite(OUT, big)
cv2.imwrite(OUT.replace(".png", "_mask.png"), mask)
print("ok", W, H, "maske px", int((mask > 0).sum()))
