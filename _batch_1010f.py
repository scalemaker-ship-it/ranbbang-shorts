#!/usr/bin/env python3
"""란빵 2026-10-10 사용자 지정 뉴스 1편 — teslatak(테슬라 탁송 사고·인수 거부 불가). v2(Remotion) 규칙 첫 신규 편.
원문: 연합뉴스TV [무조건간다] 2026-10-08 (n.news.naver.com/article/422/0000913780).
→ work/teslatak/script.json + upload.md + v2/ai_prompts.tsv + v2/real/*.jpg(9:8 크롭)
"""
import json, os
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
S = "teslatak"
WK = os.path.join(ROOT, "work", S)
PH = os.path.join(ROOT, "work", "_photos", S)
os.makedirs(os.path.join(WK, "v2", "real"), exist_ok=True)
os.makedirs(os.path.join(WK, "v2", "ai"), exist_ok=True)


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


SRC = ("연합뉴스TV 2026-10-08 [무조건간다] 새차 샀는데 '반파' 전기차가…'인수 거부는 거부'한다는 테슬라 "
       "(n.news.naver.com/article/422/0000913780) — 탁송 중 사고로 파손된 신차 도착, 테슬라코리아 '안내할 게 없다·탁송업체와 협의하라', "
       "탁송비는 테슬라에 지불·탁송사 선택권 없음, 등록·출고돼 소유권 넘어갔으니 수리해서 타라, 임시번호판 안내 없음, "
       "2024년부터 3년간 테슬라 임시번호판 0건·현대기아 90%대, 광명 인도장 선착순·순번 밖이면 탁송비 20만원, 모경종 의원 법 개정 필요")
lines = [
    L("테슬라 새 차를 주문했는데 반파된 차가 도착함.", 1),
    L("탁송 도중에 사고가 나서 산산조각 난 채로 온 거임.", 2, em=["산산조각"]),
    L("근데 테슬라코리아한테 들은 말은 딱 두 개였음.", 3),
    L("안내할 게 없다, 탁송업체랑 협의해라.", 4, em=["탁송업체랑 협의해라"], em_color="yellow"),
    L("차주는 탁송비도 테슬라에 냈고, 탁송사가 어딘지도 몰랐는데 말임.", 5),
    L("그럼 인수 거부하면 되지 않냐? 그게 안 됨.", 6, em=["안 됨"]),
    L("이미 등록돼서 차주 소유니까 수리해서 타라는 답을 받았다고 함.", 7, em=["수리해서 타라"], em_color="yellow"),
    L("원래 임시 번호판을 달면 차를 검수하고 등록할지 정할 수 있음.", 8, em=["임시 번호판"], em_color="yellow"),
    L("현대·기아는 임시 번호판 달고 나가는 차가 90%대임.", 9, em=["90%대"], em_color="yellow"),
    L("근데 테슬라가 2024년부터 3년간 받은 임시 번호판은 단 한 개도 없었음.", 10, em=["단 한 개도"]),
    L("광명 인도장에서 직접 받으려 해도 선착순이라, 못 들면 20만원 내고 탁송해야 함.", 1, em=["20만원"], em_color="yellow"),
    L("국회에선 원하면 누구나 임시 번호판을 받게 법을 바꿔야 한다는 말까지 나옴.", 2),
    L("님들이 차주면 그냥 수리해서 탈 거임?", 3),
    {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True},
]
bar = "새 차 주문했는데 부서진 차가 도착함"
sc = {"slug": S, "type": "란빵 자동차, 뉴스", "source": SRC, "title_line1": "새 차가 반파돼서 왔는데",
      "title_line2": "인수 거부도 안 되는 테슬라", "hook": bar, "channel": "란빵", "voice": "taesub",
      "style": {"sub_box": True, "bar": bar, "bar_count": None, "watermark": ""}, "lines": lines}
json.dump(sc, open(os.path.join(WK, "script.json"), "w"), ensure_ascii=False, indent=2)

title = "#테슬라 인수거부 불가"
assert len(title) <= 12, len(title)
proof = [("탁송 중 사고로 크게 파손된 신차가 도착", "연합뉴스TV 2026-10-08"),
         ("테슬라코리아 안내 = '안내할 게 없다' '탁송업체와 협의하라'", "연합뉴스TV 2026-10-08"),
         ("탁송비는 테슬라에 지불, 탁송사가 어딘지도 모름", "피해 차주 인터뷰(연합뉴스TV)"),
         ("등록·출고돼 차주 소유이므로 수리해서 타야 한다는 답", "피해 차주 인터뷰(연합뉴스TV)"),
         ("임시번호판 차량은 소유권이 제조사, 등록되면 소비자", "연합뉴스TV 2026-10-08"),
         ("현대·기아 임시번호판 출고 90%대", "연합뉴스TV 2026-10-08(현대·기아 답변)"),
         ("테슬라 2024년부터 3년간 임시번호판 0건", "연합뉴스TV 2026-10-08(임시번호판 현황 자료)"),
         ("광명 인도장 선착순, 순번 밖이면 탁송비 20만원", "피해 차주 인터뷰(연합뉴스TV)"),
         ("소비자가 원하면 임시번호판 발급하도록 법 개정 필요", "모경종 의원(연합뉴스TV)"),
         ("실사 사진", "위키미디어 커먼즈 — Dllu / CC BY-SA 4.0, Alexander Migl / CC BY-SA 4.0, JustAnotherCarDesigner / CC0")]
rows = "\n".join(f"| {a} | {b} |" for a, b in proof)
open(os.path.join(WK, "upload.md"), "w").write(
    f"# {S} — 업로드 메타 (란빵)\n\n## 제목\n\n{title}\n\n## 설명\n\n"
    "테슬라 새 차를 주문했는데 탁송 중 사고로 부서진 차가 도착함.\n"
    "인수 거부는 안 되고, 테슬라코리아 답은 탁송업체랑 협의하라는 것뿐.\n"
    "임시 번호판이 왜 중요한지까지 정리함.\n"
    "#shorts #테슬라 #탁송사고 #임시번호판 #인수거부\n\n"
    "## 고정 댓글\n\n님들이 차주면 그냥 수리해서 탈 거임?\n\n"
    "## 쇼핑태그\n\n차량용 블랙박스 2채널, 차량용 손전등, 차량 스크래치 리무버, 차량용 휴대폰 거치대, 차량용 비상삼각대\n\n"
    f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {SRC}\n")

BLUR = {"t1": [(0, 660, 215, 765), (60, 160, 120, 190)]}
# 실사 → 박스 비율 9:8(1080x960), 크레딧은 Remotion 에서 얹는다
for n, anchor in (("t1", 0.5), ("t2", 0.5), ("t3", 0.62)):
    im = Image.open(os.path.join(PH, n + ".jpg")).convert("RGB")
    tw, th = 1080, 960
    s = max(tw / im.width, th / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    left = int((im.width - tw) * anchor)
    top = (im.height - th) // 2
    im = im.crop((left, top, left + tw, top + th))
    for box in BLUR.get(n, []):   # 읽히는 번호판 흐림
        im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(14)), box[:2])
    im.save(os.path.join(WK, "v2", "real", n + ".jpg"), quality=92)

SUV = "a brand-new white modern electric crossover SUV with smooth minimalist design"
M = "a Korean man in his mid 30s, short black hair, casual hoodie"
P = {
    "a01": f"{SUV} with its front end crushed, hood crumpled and bumper torn off, sitting on the upper deck of a car carrier trailer parked at a Korean highway rest area, daytime",
    "a02": "a car carrier truck stopped on the shoulder of a Korean highway after an accident, one white SUV hanging damaged on its deck, traffic cones, flashing hazard lights, dusk",
    "a03": f"close-up of the shattered headlight and crumpled front fender of {SUV}, broken plastic and glass fragments on the ground",
    "a04": f"{M} standing stunned with both hands on his head in front of his damaged new white SUV in a Korean apartment underground parking lot",
    "a05": f"{M} on a phone call with a frustrated face, holding a smartphone to his ear, standing by the window of his apartment living room",
    "a06": "close-up of a hand holding a smartphone showing a short customer service chat reply, the text blurred and unreadable, dim room",
    "a07": "a man's hands holding a credit card in front of a laptop showing an online payment checkout page, screen blurred and unreadable, home desk",
    "a08": f"{M} raising his palm in refusal toward a car delivery driver holding a clipboard, next to a car carrier truck in an apartment parking lot",
    "a09": f"a white paper temporary registration plate taped on the rear of {SUV}, characters blurred and unreadable, close-up",
    "a10": f"{M} inspecting the paint of {SUV} with a flashlight during a new car delivery inspection, crouching beside the door",
    "a11": "rows of brand-new cars parked at a Korean factory shipping yard each with a small white paper temporary plate, aerial view, morning",
    "a12": f"many {SUV.replace('a brand-new ', '')}s lined up inside a large bright vehicle delivery center hall, customers waiting in a queue, no signage",
    "a13": "a car carrier truck loaded with brand-new white SUVs driving on a Korean expressway, side view, daytime",
    "a14": "the National Assembly building of South Korea with its green dome in Yeouido, Seoul, under a clear sky",
    "a15": "a white SUV with a smashed front end raised on a lift in a Korean auto body repair shop, mechanic in uniform looking at it",
    "a16": f"{M} sitting in the driver's seat of a car in a parking lot, staring ahead, thinking, side view through the window",
}
open(os.path.join(WK, "v2", "ai_prompts.tsv"), "w").write("".join(f"{k}\t{v}\n" for k, v in P.items()))
print("ok", len(lines), "lines", len(P), "ai")
