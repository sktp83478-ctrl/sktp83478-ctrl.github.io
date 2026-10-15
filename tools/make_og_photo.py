# 사용자가 준 그림을 배경으로 쓰는 썸네일(1200x630). 실행: python tools/make_og_photo.py <그림 경로>
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1200, 630
src = Image.open(sys.argv[1]).convert("RGB")
# 가로 1200에 맞춰 키운 뒤, 장미와 손이 보이는 아래쪽 위주로 자름
s = W / src.width
im = src.resize((W, int(src.height * s)), Image.LANCZOS)
top = int(im.height * 0.34)
im = im.crop((0, top, W, top + H))
# 왼쪽에 부드러운 밝은 안개를 깔아 글자가 읽히게
veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
vp = veil.load()
for x in range(W):
    a = max(0, min(1, (0.62 - x / W) / 0.62))
    alpha = int(205 * (a ** 1.1))
    for y in range(H):
        vp[x, y] = (253, 244, 246, alpha)
im = Image.alpha_composite(im.convert("RGBA"), veil)
d = ImageDraw.Draw(im)
plum = (112, 52, 92)
d.line((84, 150, 84, 480), fill=(190, 140, 170, 230), width=3)
f_title = ImageFont.truetype("C:/Windows/Fonts/malgunbd.ttf", 104)
d.text((116, 196), "AI 공모전", fill=plum, font=f_title)
d.text((116, 318), "알림판", fill=plum, font=f_title)
f_sub = ImageFont.truetype("C:/Windows/Fonts/malgun.ttf", 32)
d.text((120, 470), "이번 주 마감부터 한눈에, 매주 월요일 갱신", fill=(125, 85, 112), font=f_sub)
out = os.path.join(os.path.dirname(__file__), "..", "assets", "og.png")
im.convert("RGB").save(out, optimize=True, quality=90)
print("saved", out)
