#!/usr/bin/env python3
"""란빵 2026-10-10 사용자 지정 유튜브 쇼츠 2편 — yamujin(삼성 야무진이 망한 이유)·tmaproute(요즘 티맵 길안내).
레퍼런스: youtube.com/shorts/8ljqY-SUCtQ (얘봐라) · youtube.com/shorts/4e6a_WDuoTc (이것만) — 구조만 참고, 사실은 보도로 재확인.
yamujin 은 실사(커먼즈 SV110 3장, 출처 우상단 번인) + 생성 이미지, tmaproute 는 생성 이미지만.
→ work/<slug>/script.json + prompts.tsv + upload.md (+ img/ 실사)
"""
import json, os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos")
FONT = os.path.join(os.path.dirname(ROOT), "assets", "fonts", "Jalnan.ttf")
os.chdir(os.path.join(ROOT, "work"))

T = (", photorealistic DSLR photograph, 35mm lens, natural available light, shallow depth of field, "
     "Korean setting, no text no letters no signage no logos no brand marks no watermark, no readable license plates")
M2 = "a Korean man in his mid 30s, short wavy black hair, light stubble, sturdy build"
M4 = "a Korean man in his late 40s, short graying hair, casual jacket"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


def P(rel, credit, anchor=0.5):   # 실사
    return ("ph", rel, credit, anchor)


OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
eps = {}

# ── 1. 삼성 야무진 ─────────────────────────────────────────────
CR1 = "사진: Chu / CC BY-SA 3.0"
CR2 = "사진: order_242 / CC BY-SA 2.0"
eps["yamujin"] = dict(
    src="카랩(CARLAB) '혹시, 삼성 트럭이라고 들어보셨나요' (carlab.co.kr/news/8706) — 1998년 SV110 출시, 1999년 야무진 개명, 닛산 아틀라스 100 기반 국내 설계 변경, 과적 만연한 국내 사정 못 견뎌 결함 속출, 1.2톤 모델로도 포터·봉고 못 넘음, 1998~2000 2년 남짓 판매 후 2000년 삼성상용차 파산과 함께 단종 ; 다음 '삼성트럭! 야무진과 SM530을 기억하시나요' ; 도로교통법 39조·시행령 22조(적재중량 110% 이내) ; 레퍼런스 youtube.com/shorts/8ljqY-SUCtQ",
    t1="한국에서 현대·기아", t2="1톤 트럭만 남은 이유", bar="삼성이 1톤 트럭 냈다가 2년 만에 접은 이유", cnt=None,
    title="#야무진이 망한 이유", shop="화물 고정 라쳇벨트, 트럭 방수포, 차량용 블랙박스 2채널, 비상삼각대, 차량용 LED 경광봉",
    desc=["삼성도 1톤 트럭을 만들었던 적이 있음. 이름은 야무진.",
          "닛산 아틀라스 기반으로 포터·봉고에 도전했지만 2년 남짓 만에 단종.",
          "한국 1톤 트럭 시장에서 현대·기아만 살아남은 이유."],
    tags="#shorts #야무진 #삼성상용차 #1톤트럭 #포터",
    comment="님들은 1톤 트럭에 진짜 1톤만 싣는 거 본 적 있음?",
    proof=[("1998년 SV110 출시, 1999년 야무진으로 이름 변경", "카랩·다음 자동차 기사"),
           ("닛산 아틀라스 100 기반, 국내에 맞게 설계 변경", "카랩"),
           ("1톤 이상 싣는 과적이 만연한 국내 사정 못 견뎌 결함 속출", "카랩"),
           ("적재량 늘린 1.2톤 모델도 포터·봉고 못 넘음", "카랩"),
           ("2000년 삼성상용차 파산과 함께 단종, 판매 2년 남짓", "카랩·다음 자동차 기사"),
           ("화물차 적재중량 110% 초과 금지", "도로교통법 39조·시행령 22조"),
           ("사진 01·02·08", f"위키미디어 커먼즈 — {CR1.replace('사진: ', '')} / {CR2.replace('사진: ', '')}")],
    lines=[
        L("삼성도 1톤 트럭을 만들었던 거 앎?", 1),
        L("1998년에 삼성상용차가 내놓은 1톤 트럭, 이름이 야무진임.", 2, sfx="whoosh", em=["야무진"], em_color="yellow"),
        L("일본 닛산의 아틀라스 트럭을 바탕으로 한국에 맞게 고쳐서 만들었음.", 3),
        L("포터랑 봉고가 꽉 잡고 있던 시장에 정면으로 도전한 거임.", 4, em=["포터랑 봉고"]),
        L("근데 한국 1톤 트럭 시장엔 무서운 현실이 있었음.", 5, sfx="dudung", shake=False),
        L("1톤이라고 써놓고 그 이상을 싣는 과적이 너무 흔했던 거임.", 6, em=["과적"], em_color="yellow"),
        L("야무진은 이걸 못 버티고 결함이 쏟아졌다는 평가를 받음.", 7, sfx="pop", em=["결함"]),
        L("적재량을 늘린 1.2톤 모델까지 냈지만 포터와 봉고를 못 넘었음.", 8),
        L("결국 2000년 삼성상용차가 파산하면서 2년 남짓 만에 단종됨.", 9, em=["2년 남짓"], em_color="yellow"),
        L("반대로 현대·기아는 그 과적 환경까지 설계에 넣어서 지금까지 살아남은 거임.", 10, sfx="ding"),
        L("참고로 화물차는 적재중량의 110%를 넘기면 단속 대상임.", 6, em=["110%"], em_color="yellow"),
        L("님들은 1톤 트럭에 진짜 1톤만 싣는 거 본 적 있음?", 4), OUT],
    imgs={
        1: P("yamujin/sv2.jpg", CR1, 0.35),
        2: P("yamujin/sv1.jpg", CR2, 0.45),
        3: "a white small cab-over light truck on an automobile factory assembly line in the late 1990s, workers in uniforms, warm industrial light",
        4: "rows of small blue one-ton cab-over pickup trucks parked at a Korean wholesale market in the early morning, wide shot",
        5: "a small white cab-over truck driving on a narrow Korean country road in the 1990s, film photo look",
        6: "a small one-ton cab-over pickup truck heavily overloaded with stacked cabbage sacks far above the cargo bed, rear sagging, Korean market street",
        7: "close-up of a cracked leaf spring and bent rear axle under a small truck in a repair shop, mechanic's work light",
        8: P("yamujin/sv3.jpg", CR1, 0.4),
        9: "an empty quiet truck factory hall with an idle assembly line and dust, dim light through high windows",
        10: "many small blue one-ton pickup trucks driving on a busy Korean city road at dawn, telephoto compression",
    })

# ── 2. 요즘 티맵 길안내 ─────────────────────────────────────────
eps["tmaproute"] = dict(
    src="비즈한국 2024-12-09 '농로 대란 티맵 오락가락 길안내, 원인은?' (bizhankook.com/articles/28730.html) — 2024 추석 귀경길 충남 아산 인주면~평택호 방향 논길에 차량 1000여 대 최대 5시간 고립, 국도 주행시간 예년 5배, 정민규 CTO 해명, 전국 이면도로 전수조사·알고리즘 개선 ; 아이뉴스24 2023-08-10 '티맵이 비싼 길 안내? 티맵 사실 아냐' (inews24.com/view/1621531) — 민자도로 유도 의혹 부인, 시간·거리 이득이 통행료보다 클 때 추천, 무료도로 경로 선택·실시간 경로 탐색 끄기 안내 ; 레퍼런스 youtube.com/shorts/4e6a_WDuoTc",
    t1="갈수록 이상해지는", t2="요즘 티맵 길안내", bar="큰길 두고 골목으로 집어넣는 내비", cnt=None,
    title="#요즘 티맵 길안내", shop="차량용 휴대폰 거치대, 차량용 고속 충전기, 하이패스 단말기, 차량용 블랙박스 2채널, 송풍구 거치대",
    desc=["큰길 놔두고 좁은 골목으로 넣는 길안내, 운전자 불만이 계속 나옴.",
          "추석 귀경길 논길에 차 1000여 대가 최대 5시간 갇힌 일도 있었음.",
          "통행료 아끼고 이상한 경로 피하는 설정법."],
    tags="#shorts #티맵 #내비게이션 #길안내 #운전꿀팁",
    comment="님들은 티맵이 이상한 길 알려준 적 있음?",
    proof=[("좁은 이면도로·우회 경로 안내 불만", "비즈한국 2024-12-09"),
           ("추석 귀경길 아산 논길 차량 1000여 대 최대 5시간 고립", "비즈한국 2024-12-09"),
           ("국도 주행시간 예년 5배 → 이면도로로 안내, 전국 이면도로 전수조사·알고리즘 개선", "비즈한국 2024-12-09"),
           ("민자도로 유도 의혹, 티맵은 시간·거리 이득이 통행료보다 클 때 추천이라고 부인", "아이뉴스24 2023-08-10"),
           ("무료도로 경로 선택, 실시간 경로 탐색 끄기", "아이뉴스24 2023-08-10")],
    lines=[
        L("큰길 놔두고 좁은 골목으로 집어넣는 내비, 겪어본 적 있음?", 1),
        L("요즘 티맵 길안내 때문에 운전자들 불만이 꽤 나옴.", 2, sfx="whoosh", em=["티맵"], em_color="yellow"),
        L("몇 분 빠르다고 좁은 골목으로 넣고, 쉬운 길 두고 빙 돌아가게 한다는 거임.", 3, em=["빙 돌아가게"]),
        L("제일 크게 터진 건 재작년 추석 귀경길이었음.", 4, sfx="dudung", shake=False),
        L("충남 아산 논길로 안내받은 차 1000여 대가 최대 5시간이나 갇혀버림.", 5, em=["5시간"], em_color="yellow"),
        L("국도가 평소보다 5배 막히니까 이면도로로 돌렸는데, 거기가 더 막힌 거임.", 6, sfx="pop"),
        L("티맵은 전국 이면도로를 전수조사하고 알고리즘을 고치겠다고 했음.", 7),
        L("그 전엔 비싼 민자도로로 일부러 보낸다는 의혹도 있었음.", 8, em=["민자도로"], em_color="yellow"),
        L("티맵은 시간이랑 거리 아끼는 게 통행료보다 클 때만 추천한 거라고 해명함.", 9),
        L("통행료 아끼고 싶으면 출발 전에 무료도로 경로를 고르면 됨.", 10, sfx="ding", em=["무료도로"], em_color="yellow"),
        L("갑자기 유료 도로로 바뀌는 게 싫으면 설정에서 실시간 경로 탐색을 끄면 됨.", 2, em=["실시간 경로 탐색"]),
        L("님들은 티맵이 이상한 길 알려준 적 있음?", 3), OUT],
    imgs={
        1: "view through a windshield of a car squeezing into a very narrow Korean residential alley with parked cars on both sides, daytime",
        2: f"{M2} frowning at a smartphone navigation mounted on the dashboard while driving, screen blurred and unreadable, daytime",
        3: "aerial view of a car taking a winding detour through small back streets while a wide empty main road runs beside it, Korean city",
        4: "a long traffic jam on a Korean national road during a holiday at dusk, red tail lights stretching to the horizon",
        5: "hundreds of cars stuck bumper to bumper on a narrow farm road between rice paddies at night, headlights, aerial view",
        6: f"{M4} sitting exhausted in a car stuck on a dark farm road at night, side view through the window",
        7: "engineers looking at a large digital road network map on monitors in an office, screens blurred and unreadable",
        8: "a highway toll gate in Korea with cars passing through lanes, daytime, no readable signs",
        9: "close-up of a car dashboard clock and a smartphone navigation with a blurred route line, daytime",
        10: "close-up of a hand tapping a smartphone mounted on a car air vent before driving, screen blurred and unreadable",
    })


def burn(src, dst, credit, anchor, first=False):   # _batch_0925.py 와 동일 (출처 우상단)
    im = Image.open(os.path.join(PH, src)).convert("RGB")
    tw, th = 1280, 800
    w, h = im.size; s = max(tw / w, th / h)
    im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    W, H = im.size
    left = int((W - tw) * anchor); top = (H - th) // 2
    im = im.crop((left, top, left + tw, top + th)).convert("RGBA")
    f = ImageFont.truetype(FONT, 26)
    bb = ImageDraw.Draw(im).textbbox((0, 0), credit, font=f)
    tw2, th2 = bb[2] - bb[0], bb[3] - bb[1]
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    x1 = 1157 - 16; y0 = 118 if first else 18
    x0, y1 = x1 - tw2 - 24, y0 + th2 + 18
    d.rectangle([x0, y0, x1, y1], fill=(0, 0, 0, 150))
    d.text((x0 + 12, y0 + 9 - bb[1]), credit, font=f, fill=(255, 255, 255, 235))
    Image.alpha_composite(im, ov).convert("RGB").save(dst)


def upload_md(s, e):
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    return (f"# {s} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n" + "\n".join(e["desc"]) +
            f"\n{e['tags']}\n\n## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop']}\n\n"
            f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")


for s, e in eps.items():
    os.makedirs(os.path.join(s, "img"), exist_ok=True)
    assert len(e["title"]) <= 12, (s, e["title"], len(e["title"]))
    sc = {"slug": s, "type": "란빵 자동차, 유튜브 레퍼런스", "source": e["src"], "title_line1": e["t1"], "title_line2": e["t2"],
          "hook": e["bar"], "channel": "란빵", "voice": "taesub",
          "style": {"sub_box": True, "bar": e["bar"], "bar_count": e["cnt"], "watermark": ""}, "lines": e["lines"]}
    json.dump(sc, open(f"{s}/script.json", "w"), ensure_ascii=False, indent=2)
    gens = []
    for k in sorted(e["imgs"]):
        it = e["imgs"][k]
        if isinstance(it, tuple):
            burn(it[1], os.path.join(s, "img", f"{k:02d}.png"), it[2], it[3], first=(k == 1))
        else:
            gens.append(f"{k:02d}\t{it}{T}")
    open(f"{s}/prompts.tsv", "w").write("\n".join(gens) + "\n")
    open(f"{s}/upload.md", "w").write(upload_md(s, e))
    imgs = sorted({l["img"] for l in e["lines"] if "img" in l})
    assert imgs == sorted(e["imgs"]), (s, imgs)
    print(s, len(e["lines"]) - 1, "lines, imgs", len(imgs), "gen", len(gens), "|", e["title"], len(e["title"]))
