#!/usr/bin/env python3
"""란빵 2026-10-15 즉시 공개 — 중앙일보 체리 오모다5 뒷바퀴 축 이탈 1편, v2(Remotion), 경모 목소리(tts_myvoice).
omoda5  (실사 = 기사 화면 캡처 + 기사 사진, 사용자 허락 "기사 화면 캡쳐 사용해도 좋아")
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
C = "a sleek black Chinese compact crossover SUV with sharp LED tail light bar, no badges or logos"
eps["omoda5"] = dict(
    src="https://n.news.naver.com/article/025/0003557546",
    src_note="중앙일보 2026-10-13 '달리던 車 뒷바퀴 통째 빠졌다…'수출 올인' 중국차 품질 충격' (신경진 특파원)",
    t1="달리다가 뒷바퀴가", t2="통째로 빠진 중국차", bar="주행 중 뒷바퀴 축째 빠진 SUV", cnt=None,
    title="#뒷바퀴 통째 빠짐",
    lines=[
        L("달리던 SUV 뒷바퀴가 축째로 통째 빠져버렸음.", 1, em=["통째"]),
        L("지난 6일 말레이시아 조호르바루 도로에서 생긴 일임.", 2, say="지난 육 일 말레이시아 조호르바루 도로에서 생긴 일임."),
        L("차는 중국 체리자동차의 2023년형 SUV, 오모다 5임.", 3,
          say="차는 중국 체리자동차의 이천이십삼 년형 에스유브이, 오모다 파이브임.", em=["체리자동차"], em_color="yellow"),
        L("주행 중에 뒷차축이 차체에서 떨어져 나가면서 바퀴 두 개가 같이 빠졌음.", 4, em=["바퀴 두 개"]),
        L("다행히 다친 사람은 없었는데, 영상이 SNS에 퍼지면서 난리가 났음.", 5,
          say="다행히 다친 사람은 없었는데, 영상이 에스엔에스에 퍼지면서 난리가 났음.", em=["난리"]),
        L("결국 말레이시아 당국은 이 차 신규 등록을 아예 막아버렸음.", 6, em=["신규 등록"], em_color="yellow"),
        L("체리는 사과문 내고 뒷차축 용접 부위 강도가 부족했다고 인정했음.", 7, em=["용접 부위"]),
        L("말레이시아에 판 8878대는 전부 리콜임.", 8, say="말레이시아에 판 팔천팔백칠십팔 대는 전부 리콜임.", em=["8878대"], em_color="yellow"),
        L("근데 진짜 문제는 이게 처음이 아니라는 거임.", 9, em=["처음이 아니라는"]),
        L("2024년 4월, 출시 한 달 만에도 뒷바퀴 쪽이 부서지는 사고가 있었음.", 10,
          say="이천이십사 년 사 월, 출시 한 달 만에도 뒷바퀴 쪽이 부서지는 사고가 있었음.", em=["한 달 만에도"]),
        L("그땐 600대 리콜에 60대 차축만 갈고 넘어갔음.", 11, say="그땐 육백 대 리콜에 육십 대 차축만 갈고 넘어갔음.", em=["넘어갔음"]),
        L("2년 반 만에 같은 부위, 같은 용접 문제가 또 터진 거임.", 12, say="이 년 반 만에 같은 부위, 같은 용접 문제가 또 터진 거임.", em=["또 터진"], em_color="yellow"),
        L("그런데도 체리는 올해 9월까지 해외에 155만 대를 팔았음.", 13,
          say="그런데도 체리는 올해 구 월까지 해외에 백오십오만 대를 팔았음.", em=["155만 대"]),
        L("님들은 중국차, 가격 싸면 탈 거임? 아님 절대 안 탐?", 14),
        OUT],
    tags="자동차 블랙박스 2채널, 타이어 공기압 측정기, 차량용 비상삼각대, 블랙박스 메모리카드, 차량용 휴대폰 거치대",
    desc="말레이시아에서 달리던 중국 체리 오모다5 뒷차축이 통째로 빠지면서 뒷바퀴 두 개가 같이 떨어진 사고.\n체리는 용접 강도 부족 인정하고 8878대 리콜, 현지 당국은 신규 등록 중단.\n2024년에도 같은 부위 사고가 있었다는 것까지 정리함.\n#shorts #중국차 #체리자동차 #오모다5 #리콜",
    cm="님들은 중국차, 가격 싸면 탈 거임? 아님 절대 안 탐?",
    proof=[("10/6 말레이시아 조호르바루, 2023년형 체리 오모다5 주행 중 뒷 차축 분리·뒷바퀴 2개 이탈, 인명피해 없음, SNS 확산", "중앙일보 2026-10-13"),
           ("말레이시아 도로교통국 형식승인(VTA)·신규 등록 중단(11일 성명)", "중앙일보 2026-10-13 (홍콩명보 인용)"),
           ("체리 11일 사과, 후륜 차축 용접 부위 강도 부족 인정, 말레이시아 오모다5 8878대 리콜", "중앙일보 2026-10-13"),
           ("2024년 4월 출시 한 달 만 후륜 파손 사고, 600대 리콜·60대 차축 교체", "중앙일보 2026-10-13"),
           ("체리 1~9월 수출 155만 대(+65.6%)", "중앙일보 2026-10-13"),
           ("사고 사진", "페이스북 캡처(중앙일보 게재), 매장 사진 신화=연합뉴스 — 기사 화면 캡처 사용은 사용자 허락")],
    real=["cap", "r1", "r1b", "r2", "r3"],
    P={
        "a01": f"{C} driving on a multi-lane tropical city highway in Malaysia, palm trees, hazy sunny day, seen from a following car dashcam angle",
        "a02": "a busy tropical city road in Southeast Asia with motorcycles and cars, overpass, palm trees, hazy afternoon, wide shot",
        "a03": f"{C} parked on a roadside, rear three-quarter view, sunny tropical city",
        "a04": "close-up of a broken rear axle beam of a car lying on asphalt with a wheel still attached, cracked weld visible, debris on road",
        "a05": "a smartphone in hand showing a social media video feed of a road accident, many likes and comments icons, screen text blurred",
        "a06": "a government vehicle registration office counter with a closed sign shape and stacked paperwork, Southeast Asia, serious mood, text unreadable",
        "a07": "macro close-up of a poor quality cracked welding seam on a steel car suspension part, workshop light",
        "a08": f"a long row of identical {C} lined up in a car dealer lot for recall inspection, aerial view",
        "a09": "a mechanic in a workshop lifting a crossover SUV on a hoist, inspecting the rear suspension from below",
        "a10": "a damaged rear wheel of an SUV bent inward on a road shoulder, tow truck arriving, overcast",
        "a11": "a mechanic replacing a rear axle beam on a lifted SUV in a garage, new part on the floor",
        "a12": "two broken car axle parts side by side on a workbench, same crack at the same weld spot, dramatic light",
        "a13": "a huge export port parking lot in China filled with thousands of new cars waiting for shipment, car carrier ship, aerial view",
        "a14": "a Korean man in his 30s looking at a smartphone in a car showroom, thinking, face partly turned away",
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
