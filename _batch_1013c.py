#!/usr/bin/env python3
"""란빵 2026-10-13 즉시 공개 — 채널A 술타기 단독 1편, v2(Remotion), 경모 목소리(tts_myvoice).
sooltagi
→ work/<slug>/script.json + upload.md + v2/ai_prompts.tsv
숫자가 든 줄은 "say" 에 한글로(금액은 마넌). 제목 위험 단어 금지(schedule_zernio.RISKY).
"""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
T = (", photorealistic candid smartphone photo, natural light, realistic setting, "
     "no text no letters no signage no logos no watermark, no readable license plates")
OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


eps = {}
M = "a Korean man in his 20s, slim, black jacket, dyed brown hair"
eps["sooltagi"] = dict(
    src="https://n.news.naver.com/article/449/0000363693",
    src_note="채널A 2026-10-11 [단독] '경찰 앞에서 버젓이 술타기…현행범 체포' (정서환 기자)",
    t1="음주측정 하자니까", t2="경찰 앞에서 소주 원샷", bar="경찰 앞에서 대놓고 술타기", cnt=None,
    title="#경찰 앞 술타기",
    lines=[
        L("새벽에 음주운전 의심 신고가 들어와서 경찰이 출동했음.", 1, em=["음주운전 의심"]),
        L("운전자는 고급 스포츠카를 몰던 20대 남성이었음.", 2, say="운전자는 고급 스포츠카를 몰던 이십 대 남성이었음.", em=["스포츠카"]),
        L("경찰이 음주측정을 하려는데, 남자가 시원한 거 좀 마시고 싶다고 함.", 3, em=["시원한 거"], em_color="yellow"),
        L("그러고는 경찰이랑 같이 편의점에 들어감.", 4),
        L("한 손엔 이온음료를 들고, 냉장고에서 소주 한 병을 더 꺼냄.", 5, em=["소주 한 병"]),
        L("계산하고 구석으로 가더니 소주병을 따서 그대로 입에 들이부음.", 6, em=["들이부음"]),
        L("옆에 있던 경찰이 부랴부랴 팔을 잡았지만 이미 마신 뒤였음.", 7),
        L("이게 바로 단속 뒤에 술을 더 마셔서 측정을 망치는 술타기임.", 8, em=["술타기"], em_color="yellow"),
        L("근데 이거 작년부터 따로 처벌하는 죄가 생겼음.", 9, em=["따로 처벌"]),
        L("음주측정방해죄, 1년 이상 5년 이하 징역이나 500만원 이상 2천만원 이하 벌금임.", 10,
          say="음주측정방해죄, 일 년 이상 오 년 이하 징역이나 오백마넌 이상 이천마넌 이하 벌금임.", em=["음주측정방해죄"], em_color="yellow"),
        L("남자는 그 자리에서 현행범으로 체포됐음.", 11, em=["현행범"]),
        L("음주운전 숨기려다 죄 하나를 더 얹은 거임.", 12, em=["죄 하나를 더"]),
        L("님들은 술타기 음주운전보다 더 세게 처벌해야 된다고 봄?", 13),
        OUT],
    tags="음주측정기, 자동차 블랙박스 2채널, 차량용 휴대폰 거치대, 블랙박스 메모리카드, 차량용 비상삼각대",
    desc="음주운전 의심 신고로 출동한 경찰 앞에서 편의점 소주를 원샷한 20대 스포츠카 운전자.\n측정 망치려는 술타기, 작년부터 음주측정방해죄로 따로 처벌함.\n그 자리에서 현행범 체포까지 정리함.\n#shorts #술타기 #음주운전 #음주측정방해죄 #현행범",
    cm="님들은 술타기 음주운전보다 더 세게 처벌해야 된다고 봄?",
    proof=[("새벽 음주운전 의심 신고, 경찰 출동, 고급 스포츠카 20대 남성", "채널A 2026-10-11"),
           ("'시원한 걸 마시고 싶다'며 편의점, 이온음료+소주 1병 구매 후 소주 들이부음, 경찰이 팔 잡아 제지", "채널A 2026-10-11 CCTV"),
           ("술타기 = 사고·단속 후 추가 음주로 측정 방해", "채널A 2026-10-11"),
           ("음주측정방해 혐의 현행범 체포, 귀가조치 후 재소환 예정", "채널A 2026-10-11"),
           ("음주측정방해죄 1년 이상 5년 이하 징역 또는 500만~2천만원 벌금(2025.6.4 시행)", "도로교통법 제148조의2 제2항·제44조 제5항")],
    P={
        "a01": "a Korean police patrol car with flashing blue and red lights stopping behind a parked sports car on a city street at dawn, dark blue sky",
        "a02": f"{M} standing next to a sleek black luxury sports car with no badges or logos, at dawn, police officer nearby, face partly turned away",
        "a03": f"a Korean police officer holding a breathalyzer device in front of {M} on a street at night, the man gesturing toward a convenience store",
        "a04": "a Korean convenience store at night seen from outside, bright interior light, a police officer and a young man walking in through the glass door",
        "a05": "inside a Korean convenience store, a young man's hand pulling a green soju bottle from a glass refrigerator while holding a blue sports drink in the other hand, no readable labels",
        "a06": f"{M} tilting a green soju bottle and drinking from it in the corner of a convenience store, a police officer reaching toward him, CCTV-like high angle",
        "a07": "a Korean police officer grabbing a young man's arm holding a green soju bottle inside a convenience store, motion blur, tense",
        "a08": "close-up of a breathalyzer device and a half-empty green soju bottle on a convenience store counter, no readable labels",
        "a09": "a Korean courtroom interior with wooden benches and the judge's bench, empty, serious mood",
        "a10": "a judge's gavel on a desk with legal documents, dramatic light, close-up, text unreadable",
        "a11": "a young man in a black jacket being handcuffed by a Korean police officer next to a patrol car outside a convenience store at night, face not visible",
        "a12": "a black luxury sports car left alone on an empty street at dawn with a police car parked behind, wide shot",
        "a13": "a smartphone screen showing a news comment section in a dark room, text blurred, held in hand",
    })

for slug, e in eps.items():
    wk = os.path.join(ROOT, "work", slug)
    os.makedirs(os.path.join(wk, "v2", "ai"), exist_ok=True)
    for ln in e["lines"]:
        if not ln.get("outro"):
            assert not any(c.isdigit() for c in ln.get("say", ln["text"])), (slug, ln["text"])
            for w in ln.get("em", []):
                assert w in ln["text"], (slug, w)
    sc = {"slug": slug, "type": "란빵 자동차, 뉴스", "source": e["src_note"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["bar"], "channel": "란빵",
          "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
          "style": {"sub_box": True, "bar": e["bar"], "bar_count": e["cnt"], "watermark": ""},
          "lines": e["lines"]}
    json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)
    assert len(e["title"]) <= 12, (slug, e["title"])
    assert not RISKY.search(e["title"] + e["t1"] + e["t2"]), (slug, e["title"])
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    open(os.path.join(wk, "upload.md"), "w").write(
        f"# {slug} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n{e['desc']}\n\n"
        f"## 고정 댓글\n\n{e['cm']}\n\n## 쇼핑태그\n\n{e['tags']}\n\n"
        f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")
    open(os.path.join(wk, "v2", "ai_prompts.tsv"), "w").write("".join(f"{k}\t{v}{T}\n" for k, v in e["P"].items()))
    print("ok", slug, len(e["lines"]), "lines", len(e["P"]), "ai", e["title"])
