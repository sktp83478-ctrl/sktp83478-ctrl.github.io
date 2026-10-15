# 페이지 디자인과 같은 모양의 썸네일(1200x630). 실행: python tools/make_og_design.py
from PIL import Image, ImageDraw, ImageFont
import os
W, H = 1200, 630
BG, SURF, LINE = (247, 246, 249), (255, 255, 255), (230, 225, 234)
INK, MUTED, ACC, ACC_SOFT = (34, 30, 38), (110, 104, 120), (123, 74, 142), (241, 232, 244)
CRIT, CRIT_S, WARN, WARN_S, OK, OK_S = (183, 58, 49), (249, 227, 224), (154, 102, 18), (248, 237, 214), (47, 107, 64), (227, 240, 230)
B = "C:/Windows/Fonts/malgunbd.ttf"; R = "C:/Windows/Fonts/malgun.ttf"
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# 왼쪽: 제목
d.rounded_rectangle((72, 118, 112, 158), radius=12, fill=ACC_SOFT)
d.ellipse((82, 128, 102, 148), fill=ACC)
d.text((72, 180), "AI 공모전", fill=INK, font=ImageFont.truetype(B, 92))
d.text((72, 290), "알림판", fill=ACC, font=ImageFont.truetype(B, 92))
d.text((76, 420), "이번 주 마감부터 한눈에", fill=INK, font=ImageFont.truetype(R, 32))
d.text((76, 466), "국내·해외 공모전·영화제, 매주 월요일 갱신", fill=MUTED, font=ImageFont.truetype(R, 24))

# 오른쪽: 표 미리보기 카드
x0, y0, x1, y1 = 600, 70, 1140, 560
d.rounded_rectangle((x0 + 6, y0 + 8, x1 + 6, y1 + 8), radius=18, fill=(232, 228, 238))
d.rounded_rectangle((x0, y0, x1, y1), radius=18, fill=SURF, outline=LINE, width=2)
d.text((x0 + 24, y0 + 20), "이번 주 마감", fill=INK, font=ImageFont.truetype(B, 24))
d.text((x0 + 178, y0 + 26), "11건", fill=MUTED, font=ImageFont.truetype(R, 18))
hy = y0 + 66
d.rectangle((x0 + 1, hy, x1 - 1, hy + 34), fill=(251, 250, 252))
d.line((x0 + 1, hy + 34, x1 - 1, hy + 34), fill=LINE, width=1)
fh = ImageFont.truetype(R, 15)
for tx, label in [(x0 + 24, "마감"), (x0 + 120, "공모전 · 영화제"), (x0 + 360, "시상"), (x0 + 470, "확인")]:
    d.text((tx, hy + 9), label, fill=MUTED, font=fh)
rows = [
    ("D-0", CRIT, CRIT_S, "과천과학관 AI 과학 숏폼", "대상 100만", "공식", OK, OK_S),
    ("D-0", CRIT, CRIT_S, "울산 U잼 영상 — AI영상", "최우수 150만", "일부", WARN, WARN_S),
    ("D-2", CRIT, CRIT_S, "교통안전 홍보작품 공모전", "대상 200만", "일부", WARN, WARN_S),
    ("D-3", CRIT, CRIT_S, "탄소, 다시 보다 AI 챌린지", "총 400만", "공식", OK, OK_S),
    ("D-5", WARN, WARN_S, "한강버스 AI 영상 공모전", "대상 200만", "공식", OK, OK_S),
    ("D-6", WARN, WARN_S, "국가상징구역 숏폼 영상", "최우수 200만", "공식", OK, OK_S),
    ("D-7", WARN, WARN_S, "제20회 국방 홍보 영상", "대상 300만", "공식", OK, OK_S),
]
fn = ImageFont.truetype(R, 17); fb = ImageFont.truetype(B, 15); fs = ImageFont.truetype(R, 16)
ry = hy + 35
for i, (dd, c, cs, name, prize, lv, lc, ls) in enumerate(rows):
    rh = 56
    if i: d.line((x0 + 1, ry, x1 - 1, ry), fill=LINE, width=1)
    d.rounded_rectangle((x0 + 24, ry + 16, x0 + 84, ry + 40), radius=7, fill=cs)
    d.text((x0 + 54, ry + 28), dd, fill=c, font=fb, anchor="mm")
    d.text((x0 + 120, ry + 17), name, fill=INK, font=fn)
    d.text((x0 + 360, ry + 19), prize, fill=INK, font=ImageFont.truetype(R, 15))
    d.rounded_rectangle((x0 + 470, ry + 17, x0 + 520, ry + 39), radius=11, fill=ls)
    d.text((x0 + 495, ry + 28), lv, fill=lc, font=ImageFont.truetype(R, 13), anchor="mm")
    ry += rh

out = os.path.join(os.path.dirname(__file__), "..", "assets", "og.png")
img.save(out, optimize=True)
print("saved", out)
