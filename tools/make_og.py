# 사용자가 준 그림(assets/bg.webp)을 그대로 썸네일(1200x630)로 자른다. 실행: python tools/make_og.py
from PIL import Image
import os
W, H = 1200, 630
here = os.path.dirname(__file__)
src = Image.open(os.path.join(here, "..", "assets", "bg.webp")).convert("RGB")
s = W / src.width
im = src.resize((W, int(src.height * s)), Image.LANCZOS)
top = int(im.height * 0.30)  # 손과 장미가 가운데 오도록
im = im.crop((0, top, W, top + H))
out = os.path.join(here, "..", "assets", "og.png")
im.save(out, optimize=True, quality=92)
print("saved", out)
