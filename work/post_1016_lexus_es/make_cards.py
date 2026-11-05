"""란빵 커뮤니티 게시글 카드 (1080x1080) — 렉서스 올 뉴 ES 국내 출시."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.expanduser("~/Library/Fonts/")
def font(name, size): return ImageFont.truetype(F + name, size)
JAL = "Jalnan2TTF.ttf"; PB = "Pretendard-Bold.ttf"; PEB = "Pretendard-ExtraBold.ttf"; PS = "Pretendard-SemiBold.ttf"
if not os.path.exists(F + PS): PS = PB
S = 1080; LIME = (190, 255, 60); CREDIT = "사진: Lexus (Toyota 글로벌 뉴스룸)"

def cover(path, focus_x=0.5):
    im = Image.open(os.path.join(HERE, path)).convert("RGB")
    w, h = im.size; s = S / min(w, h); im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    w, h = im.size; x = int((w - S) * focus_x); return im.crop((x, (h - S) // 2, x + S, (h - S) // 2 + S))

def grad(im, top=0, bottom=0):
    ov = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    for y in range(S):
        a = 0
        if top and y < top: a = int(230 * (1 - y / top))
        if bottom and y > S - bottom: a = max(a, int(235 * (y - (S - bottom)) / bottom))
        d.line([(0, y), (S, y)], fill=(0, 0, 0, a))
    return Image.alpha_composite(im.convert("RGBA"), ov)

def credit(d):
    f = font(PS, 24); w = d.textlength(CREDIT, font=f)
    d.rounded_rectangle([S - w - 44, 24, S - 20, 66], 8, fill=(0, 0, 0, 150))
    d.text((S - w - 32, 31), CREDIT, font=f, fill=(255, 255, 255))

def center(d, y, text, f, fill):
    d.text(((S - d.textlength(text, font=f)) / 2, y), text, font=f, fill=fill)

# 1) 표지
im = grad(cover("src_088.jpg", 0.62), top=420, bottom=330); d = ImageDraw.Draw(im, "RGBA")
d.rounded_rectangle([60, 100, 330, 156], 28, fill=LIME)
d.text((84, 108), "신차 출시 소식", font=font(PEB, 34), fill=(0, 0, 0))
d.text((60, 182), "렉서스 ES가", font=font(JAL, 92), fill="white")
d.text((60, 292), "전기차로 나왔다", font=font(JAL, 92), fill=LIME)
center(d, S - 200, "8세대 '올 뉴 ES' · 10월 13일 국내 출시", font(PB, 40), "white")
center(d, S - 140, "전기차가 하이브리드보다 130만원 싸다?", font(PEB, 44), LIME)
credit(d); im.convert("RGB").save(os.path.join(HERE, "card1.jpg"), quality=92)

# 2) 가격표
bg = cover("src_037.jpg", 0.5).filter(ImageFilter.GaussianBlur(2))
bg = Image.blend(bg, Image.new("RGB", (S, S), (12, 12, 14)), 0.72); im = bg
d = ImageDraw.Draw(im, "RGBA")
center(d, 70, "트림별 가격", font(JAL, 72), "white")
center(d, 165, "부가세 포함 · 개소세 5% 기준", font(PS, 30), (190, 190, 190))
rows = [("ES 350e", "전기 · 전륜 · 227마력", "7,160 ~ 8,390만원", True),
        ("ES 500e", "전기 · 사륜 · 347마력", "7,700 ~ 8,490만원", False),
        ("ES 350h", "하이브리드 · 247마력", "7,290 ~ 7,780만원", False),
        ("ES 350h AWD", "하이브리드 · 사륜", "7,590 ~ 8,080만원", False)]
y = 250
for name, sub, price, hl in rows:
    d.rounded_rectangle([60, y, S - 60, y + 150], 22, fill=(255, 255, 255, 30), outline=LIME if hl else None, width=4)
    d.text((95, y + 28), name, font=font(PEB, 46), fill=LIME if hl else "white")
    d.text((95, y + 92), sub, font=font(PS, 30), fill=(200, 200, 200))
    f = font(PEB, 44); d.text((S - 95 - d.textlength(price, font=f), y + 50), price, font=f, fill="white")
    y += 172
center(d, y + 14, "주행거리 478km (ES 350e 복합) · 하이브리드 연비 19.4km/ℓ", font(PB, 30), (220, 220, 220))
credit(d); im.convert("RGB").save(os.path.join(HERE, "card2.jpg"), quality=92)

# 3) 실내
im = grad(cover("src_011.jpg", 0.5), bottom=380); d = ImageDraw.Draw(im, "RGBA")
d.text((60, S - 330), "차체 더 커졌다", font=font(JAL, 76), fill=LIME)
for i, t in enumerate(["전장 5,140mm (+165) · 휠베이스 2,950mm (+80)",
                       "12.3인치 계기판 + 14인치 센터 디스플레이",
                       "손 가까이 대면 나타나는 '히든 스위치'"]):
    d.text((60, S - 220 + i * 58), t, font=font(PB, 38), fill="white")
credit(d); im.convert("RGB").save(os.path.join(HERE, "card4.jpg"), quality=92)

# 3) 전기차 성능 (컷어웨이)
im = grad(cover("src_065.jpg", 0.5), top=360, bottom=330); d = ImageDraw.Draw(im, "RGBA")
d.rounded_rectangle([60, 100, 300, 156], 28, fill=LIME)
d.text((84, 108), "첫 ES 전기차", font=font(PEB, 34), fill=(0, 0, 0))
d.text((60, 180), "한 번 충전에 478km", font=font(JAL, 80), fill="white")
for i, t in enumerate(["ES 350e · 74.69kWh 배터리 · 227마력 (전륜)",
                       "10→80% 급속충전 약 28분 (DC 최대 150kW)",
                       "ES 500e · 앞뒤 모터 사륜 'DIRECT4' · 347마력",
                       "고전압 배터리 보증 10년 / 20만km"]):
    d.text((60, S - 290 + i * 60), t, font=font(PB, 36), fill="white")
credit(d); im.convert("RGB").save(os.path.join(HERE, "card3.jpg"), quality=92)

# 5) 마무리 질문
im = grad(cover("src_084.jpg", 0.5), top=480); d = ImageDraw.Draw(im, "RGBA")
center(d, 110, "여러분의 선택은?", font(JAL, 84), "white")
center(d, 230, "전기 ES 350e  vs  하이브리드 ES 350h", font(PEB, 46), LIME)
center(d, 305, "7,160만원  ·  7,290만원", font(PB, 40), (230, 230, 230))
d.rounded_rectangle([290, S - 160, S - 290, S - 90], 35, fill=LIME)
center(d, S - 150, "댓글로 알려주세요 👇".replace(" 👇", ""), font(PEB, 40), (0, 0, 0))
credit(d); im.convert("RGB").save(os.path.join(HERE, "card5.jpg"), quality=92)
print("ok")
