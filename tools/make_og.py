# 카톡 미리보기용 썸네일(1200x630). 실행: python tools/make_og.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
W, H = 1200, 630

# 파스텔 그라데이션 (블러시 → 라벤더 → 민트빛)
base = Image.new("RGB", (W, H))
px = base.load()
c1, c2, c3 = (252, 228, 236), (232, 224, 246), (222, 238, 240)
for y in range(H):
    for x in range(W):
        t = (x / W) * 0.65 + (y / H) * 0.35
        if t < 0.5:
            k = t / 0.5; c = tuple(int(c1[i] + (c2[i] - c1[i]) * k) for i in range(3))
        else:
            k = (t - 0.5) / 0.5; c = tuple(int(c2[i] + (c3[i] - c2[i]) * k) for i in range(3))
        px[x, y] = c

# 부드러운 빛 번짐 (보케)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
g = ImageDraw.Draw(glow)
for (cx, cy, r, col) in [(980, 140, 190, (255, 255, 255, 120)), (1080, 470, 150, (250, 200, 225, 110)),
                          (780, 520, 110, (255, 255, 255, 90)), (160, 560, 130, (240, 215, 240, 100)),
                          (420, 90, 90, (255, 255, 255, 80))]:
    g.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
glow = glow.filter(ImageFilter.GaussianBlur(40))
img = Image.alpha_composite(base.convert("RGBA"), glow)

# 꽃잎 몇 장 (단순 타원, 살짝 투명)
petals = Image.new("RGBA", (W, H), (0, 0, 0, 0))
p = ImageDraw.Draw(petals)
import math
def flower(cx, cy, size, col, n=5, tilt=0):
    for i in range(n):
        a = tilt + i * 360 / n
        rx, ry = size, int(size * 0.55)
        petal = Image.new("RGBA", (rx * 2 + 6, ry * 2 + 6), (0, 0, 0, 0))
        ImageDraw.Draw(petal).ellipse((3, 3, rx * 2 + 3, ry * 2 + 3), fill=col)
        petal = petal.rotate(a, expand=True, resample=Image.BICUBIC)
        ox = int(math.cos(math.radians(a)) * size * 0.9); oy = -int(math.sin(math.radians(a)) * size * 0.9)
        petals.alpha_composite(petal, (cx + ox - petal.width // 2, cy + oy - petal.height // 2))
    p.ellipse((cx - size // 4, cy - size // 4, cx + size // 4, cy + size // 4), fill=(255, 240, 246, 200))
flower(1000, 300, 70, (244, 176, 204, 120), tilt=15)
flower(880, 450, 46, (240, 168, 200, 100), tilt=40)
flower(1120, 470, 40, (247, 196, 216, 110), tilt=5)
# 흩날리는 작은 꽃잎
for (cx, cy, rx, ry, ang) in [(760, 200, 26, 12, 30), (1130, 150, 22, 10, -40), (940, 580, 24, 11, 15), (660, 560, 18, 9, 60)]:
    petal = Image.new("RGBA", (rx * 2 + 4, ry * 2 + 4), (0, 0, 0, 0))
    ImageDraw.Draw(petal).ellipse((2, 2, rx * 2 + 2, ry * 2 + 2), fill=(244, 180, 206, 110))
    petal = petal.rotate(ang, expand=True, resample=Image.BICUBIC)
    petals.alpha_composite(petal, (cx - petal.width // 2, cy - petal.height // 2))
petals = petals.filter(ImageFilter.GaussianBlur(2))
img = Image.alpha_composite(img, petals)

d = ImageDraw.Draw(img)
plum = (120, 60, 105)
# 가는 장식 선
d.line((88, 150, 88, 480), fill=(185, 135, 170, 255), width=3)
# 제목 (바탕체 세리프)
f_title = ImageFont.truetype("C:/Windows/Fonts/batang.ttc", 118, index=0)
d.text((120, 190), "AI 공모전", fill=plum, font=f_title)
d.text((120, 318), "알림판", fill=plum, font=f_title)
f_sub = ImageFont.truetype("C:/Windows/Fonts/malgun.ttf", 34)
d.text((124, 470), "이번 주 마감부터 한눈에  ·  매주 월요일 갱신", fill=(130, 95, 120), font=f_sub)

out = os.path.join(os.path.dirname(__file__), "..", "assets", "og.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
img.convert("RGB").save(out, optimize=True)
print("saved", out)
