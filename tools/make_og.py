# 카톡 미리보기용 썸네일(1200x630) 생성. 실행: python tools/make_og.py
from PIL import Image, ImageDraw, ImageFont
import os
W, H = 1200, 630
img = Image.new("RGB", (W, H), (14, 111, 126))  # 알림판 포인트 색(청록)
d = ImageDraw.Draw(img)
# 오른쪽 아래 밝은 사선 띠
d.polygon([(760, 0), (W, 0), (W, H), (560, H)], fill=(18, 131, 148))
d.polygon([(900, 0), (W, 0), (W, H), (700, H)], fill=(22, 150, 168))
# 달력 아이콘 느낌의 카드
d.rounded_rectangle((80, 110, 360, 350), radius=28, fill=(255, 255, 255))
d.rounded_rectangle((80, 110, 360, 175), radius=28, fill=(184, 50, 42))
d.rectangle((80, 145, 360, 175), fill=(184, 50, 42))
F = "C:/Windows/Fonts/malgunbd.ttf"
f_big = ImageFont.truetype(F, 110)
d.text((220, 262), "D-7", fill=(26, 34, 43), font=f_big, anchor="mm")
f_small = ImageFont.truetype(F, 30)
d.text((220, 142), "마감 임박", fill=(255, 255, 255), font=f_small, anchor="mm")
# 제목
f_title = ImageFont.truetype(F, 84)
d.text((80, 420), "AI 공모전 알림판", fill=(255, 255, 255), font=f_title)
f_sub = ImageFont.truetype("C:/Windows/Fonts/malgun.ttf", 38)
d.text((84, 530), "국내·해외 AI 공모전과 영화제 · 매주 월요일 갱신", fill=(221, 240, 243), font=f_sub)
os.makedirs(os.path.join(os.path.dirname(__file__), "..", "assets"), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "..", "assets", "og.png")
img.save(out, optimize=True)
print("saved", out)
