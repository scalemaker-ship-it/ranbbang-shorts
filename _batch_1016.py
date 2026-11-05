#!/usr/bin/env python3
"""란빵 2026-10-16 — 보배드림 베스트 1편 spikeroad(맛집 진입로 쇠말뚝). v2(Remotion), 경모 목소리(tts_myvoice).
대본 중간 대화체(대사) 줄 최소 1개 필수(2026-10-16 사용자 지시) — 나레이션이 talk1 이라 대사는 "speaker": 2 로 목소리를 바꾼다.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
T = (", photorealistic candid smartphone photo, natural light, realistic setting, "
     "no text no letters no signage no logos no watermark, no readable license plates")
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")
Y, W, R = "#FBFF56", "#fff", "#FF3B30"
SHOT_KEYS = ("sh", "fx", "pop", "shake", "info")
GEN_TAGS = "자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 휴대폰 거치대, 차량용 비상삼각대"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


def A(img, at=None, punch=False, close=False, fx=0.5, fy=0.5, zin=True, credit=None):
    s0, s1 = (1.6, 1.75) if close else ((1.0, 1.12) if zin else (1.12, 1.0))
    src = img if "/" in str(img) else f"ai/a{int(img):02d}.png"
    d = {"img": src, "s0": s0, "s1": s1, "fx": fx, "fy": fy}
    if at:
        d["at"] = at
    if punch:
        d["punch"] = True
    if credit:
        d["credit"] = credit
    return d


def shot_line(ln, i):
    if ln.get("outro"):
        return {"shots": [A(ln["img"])], "sfx": [["pop_long", "구독!"]], "pop": ["구독!", "#FFE629", "구독!"]}
    if "sh" in ln:
        shots = ln["sh"]
    else:
        em = ln.get("em") or []
        at = em[0] if em else None
        if not at:   # 강조어 없으면 문장 중간 어절에서 반대 방향 켄번즈
            ws = ln["text"].rstrip(".?!").split()
            at = ws[len(ws) // 2].strip(",") if len(ws) > 2 else None
        shots = [A(ln["img"], zin=(i % 2 == 0))]
        if at:
            shots.append(A(ln["img"], at, close=bool(em), punch=bool(ln.get("pop")), zin=(i % 2 == 1)))
    d = {"shots": shots}
    if ln.get("fx"):
        d["sfx"] = [list(x) for x in ln["fx"]]
    for k in ("pop", "shake", "info"):
        if ln.get(k):
            d[k] = list(ln[k]) if k == "pop" else ln[k]
    return d


def info_q(text, at):
    return {"kind": "quotes", "items": [{"text": text, "at": at}]}


def info_c(title, items, at=None):
    d = {"kind": "compare", "title": title, "items": items}
    if at:
        d["at"] = at
    return d


def info_n(title, num, suffix, label, at):
    return {"kind": "counter", "at": at, "title": title, "items": [{"num": num, "suffix": suffix, "label": label, "at": at}]}


def info_b(title, at, items):
    return {"kind": "bars", "at": at, "title": title, "items": items}


OUT = lambda img: {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": img}
eps = {}

# ───────────────────────── spikeroad ─────────────────────────
BB = "사진: 보배드림 글쓴이"
eps["spikeroad"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1040201",
    src_note="보배드림 베스트 2026-10-15 '유명 맛집 가다가 차가 다 망가졌습니다… 도로 한가운데 쇠말뚝'",
    t1="맛집 가는 길 한복판", t2="숨어 있던 쇠말뚝", bar="도로 한가운데 박힌 쇠말뚝", cnt=None,
    title="#맛집길 쇠말뚝",
    lines=[
        L("유명 만두전골집 가려고 우회전하는데 차 밑에서 끄드득 소리가 났음.", 1, em=["끄드득"],
          sh=[A(1), A(2, "끄드득", punch=True, close=True)], fx=[("sting_glitch", "끄드득", 0.5)], shake="끄드득"),
        L("내려서 보니 도로 한가운데 쇠말뚝이 박혀 있었음.", 3, em=["쇠말뚝"], em_color="yellow",
          sh=[A("real/r1.jpg", credit=BB), A(3, "쇠말뚝이", punch=True, close=True)],
          fx=[("hit_trailer_epic", "쇠말뚝이", 0.55)], pop=("쇠말뚝?!", R, "쇠말뚝이")),
        L("도로 색이랑 똑같아서 처음 오는 차는 볼 수가 없음.", 4, em=["똑같아서"]),
        L("하부는 다 긁히고 머플러까지 찌그러졌음.", 5, em=["머플러"],
          sh=[A("real/r2.jpg", credit=BB), A("real/r3.jpg", "머플러까지", credit=BB)],
          fx=[("glass_smash", "찌그러졌음", 0.45)], shake="찌그러졌음"),
        L("근데 땅주인이 나와서 한다는 말이,", 6, em=["땅주인"]),
        L("말뚝 휘었으니까 원상복구 해요, 내가 하면 30만원이고.", 7, dialogue=True, speaker=2, emotion="angry",
          say="말뚝 휘었으니까 원상복구 해요, 내가 하면 삼십마넌이고.",
          fx=[("wrong_gameshow_buzz", "원상복구", 0.45)], pop=("적반하장", R, "30만원이고")),
        L("수리비만 150만원인데, 하이브리드 배터리까지 다쳤으면 1000만원 가량 나온다 함.", 8,
          say="수리비만 백오십마넌인데, 하이브리드 배터리까지 다쳤으면 천마넌 가량 나온다 함.", em=["1000만원"], em_color="yellow",
          info=info_c("예상 수리비", [{"label": "하부·머플러", "color": W, "rows": [["견적", "150만원", Y]]},
                                    {"label": "배터리까지", "color": Y, "at": "배터리까지", "rows": [["예상", "1000만원", R]]}], "150만원인데,")),
        L("렉카 기사 말로는 여기서 당한 차가 스무 번도 넘는다 함.", 9, em=["스무 번"],
          fx=[("drum_rimshot", "넘는다", 0.45)], pop=("20번+", Y, "스무")),
        L("근데 대법원은 사람들이 다니던 길이면 땅주인이 막아도 일반교통방해로 봤음.", 10, em=["일반교통방해"], em_color="yellow",
          sh=[A(10), A(11, "땅주인이", zin=False)], fx=[("hit_trailer_epic", "일반교통방해로", 0.5)],
          info=info_q("“내 땅이어도 일반교통방해”", "일반교통방해로")),
        L("10년 이하 징역이나 1500만원 이하 벌금이고, 수리비는 민사로 따로 청구할 수 있음.", 12,
          say="십 년 이하 징역이나 천오백마넌 이하 벌금이고, 수리비는 민사로 따로 청구할 수 있음.", em=["민사"],
          info=info_c("형법 제185조 + 민사", [{"label": "형사", "color": W, "rows": [["징역", "10년 이하", Y], ["벌금", "1500만원 이하", Y]]},
                                           {"label": "민사", "color": Y, "at": "수리비는", "rows": [["청구", "수리비", Y]]}], "10년")),
        L("님들은 내 땅에 숨은 쇠말뚝 박는 거, 권리라고 봄?", 13, fx=[("pop_bubble", "봄")]),
        OUT(14)],
    tags=GEN_TAGS + ", 언더코팅 스프레이",
    desc="유명 맛집 가는 우회전 진입로 한가운데 숨은 쇠말뚝, 하부·머플러 박살에 하이브리드 배터리 손상 의심.\n땅주인은 오히려 말뚝 원상복구 30만원 요구, 렉카 기사 말로는 피해 차량만 스무 대 넘음.\n사유지라도 사람들이 다니던 길이면 일반교통방해, 수리비 민사 청구까지 정리함.\n#shorts #보배드림 #쇠말뚝 #사유지 #일반교통방해",
    cm="님들은 내 땅에 숨은 쇠말뚝 박는 거, 권리라고 봄?",
    proof=[("유명 만두전골집 가던 우회전 진입로 한가운데 쇠말뚝, 하부·머플러 손상", "보배드림 2026-10-15 글쓴이(사진 포함)"),
           ("상대방이 말뚝 원상복구 요구, 직접 하면 30만원", "보배드림 2026-10-15 글쓴이"),
           ("수리비 약 150만원, 하이브리드 배터리 손상 의심 — 카센터 '최소 700만, 1000만원가량'", "보배드림 2026-10-15 글쓴이"),
           ("렉카가 스무 번도 넘게 왔다", "보배드림 2026-10-15 글쓴이(전해 들은 말)"),
           ("불특정 다수 통행로의 토지 소유자가 도로에 바위를 놓아 차량 통행을 막음 → 일반교통방해·업무방해", "대법원 2002. 4. 26. 선고 2001도6903 판결"),
           ("일반교통방해: 10년 이하 징역 또는 1천500만원 이하 벌금", "형법 제185조"),
           ("수리비 손해배상 청구", "민법 제750조(불법행위)")],
    P={
        "a01": "a Korean family in a silver hybrid sedan turning right onto a narrow rural asphalt road toward a small countryside restaurant, mountains, daytime",
        "a02": "low angle view under a car, a short iron stake scraping the car underbody and exhaust pipe on asphalt, small sparks",
        "a03": "close-up of a thin rusty iron stake sticking up from gray asphalt in the middle of a rural road, nearly invisible, same color as the road",
        "a04": "a driver's point of view of a rural road entrance turning right, the road looks empty and normal, nothing visible",
        "a05": "a Korean man in his 40s kneeling on the road looking under his silver sedan with a shocked face, side view, face partly hidden",
        "a06": "a Korean man in his 60s in work clothes standing with arms crossed on a rural roadside next to a bent iron stake, face turned away",
        "a07": "an older Korean man's hand pointing at a bent iron stake on the road while another man listens, cropped, no faces",
        "a08": "a mechanic in a Korean auto repair shop examining the underside of a lifted silver hybrid sedan, battery warning light concept",
        "a09": "a tow truck parked behind a damaged silver sedan on a narrow rural road near small restaurants, daytime",
        "a10": "a narrow countryside access road between two small Korean restaurant buildings, cars passing, daytime",
        "a11": "large rocks placed in the middle of a narrow rural road blocking cars, a car stopped in front",
        "a12": "a Korean courtroom with a judge's gavel on the bench, legal documents, text unreadable",
        "a13": "several rusty iron stakes and rebar piled against a wall next to a rural road, moody",
        "a14": "a silver hybrid sedan parked in front of a small Korean countryside restaurant at dusk, warm lights",
    })


def write_shots(slug, spec_lines):
    sc = json.load(open(os.path.join(ROOT, "work", slug, "script.json")))
    assert len(spec_lines) == len(sc["lines"]), (slug, len(spec_lines), len(sc["lines"]))
    lines = []
    for i, ln in enumerate(spec_lines):
        base = dict(sc["lines"][i])
        base.update(ln)
        lines.append(shot_line(base, i))
    texts = [l["text"].rstrip(".") for l in sc["lines"]]

    def chk(li, w):
        if w:
            assert w in texts[li], (slug, li, w, texts[li])
    for li, l in enumerate(lines):
        for s in l["shots"]:
            chk(li, s.get("at"))
        for x in l.get("sfx", []):
            chk(li, x[1])
        if "pop" in l:
            chk(li, l["pop"][2])
        chk(li, l.get("shake"))
        inf = l.get("info")
        if inf:
            chk(li, inf.get("at"))
            for it in inf.get("items", []):
                chk(li, it.get("at"))
                chk(li, it.get("flash"))
    json.dump({"bgmVol": 0.09, "bgm": "bgm/sneaky-123.mp3", "lines": lines},
              open(os.path.join(ROOT, "work", slug, "v2", "shots.json"), "w"), ensure_ascii=False, indent=1)
    print("shots", slug, len(lines))


only = sys.argv[1:]
for slug, e in eps.items():
    if only and slug not in only:
        continue
    wk = os.path.join(ROOT, "work", slug)
    os.makedirs(os.path.join(wk, "v2", "ai"), exist_ok=True)
    n_ai = len(e["P"])
    # 2026-10-16 사용자 지시: 대본 중간에 대화체 한 문장씩 — 대사 줄 없으면 생성 중단
    assert any(ln.get("dialogue") for ln in e["lines"]), (slug, "대화체(dialogue) 줄 없음")
    for ln in e["lines"]:
        assert 1 <= ln["img"] <= n_ai, (slug, ln)
        if ln.get("dialogue"):
            assert ln.get("speaker", 1) != 1 and not ln.get("em"), (slug, "대사는 speaker≠1(나레이션=talk1), em 금지", ln["text"])
        if not ln.get("outro"):
            assert not any(c.isdigit() for c in ln.get("say", ln["text"])), (slug, ln["text"])
            for w in ln.get("em", []):
                assert w in ln["text"], (slug, w)
    lines = [{k: v for k, v in ln.items() if k not in SHOT_KEYS} for ln in e["lines"]]
    sc = {"slug": slug, "type": "란빵 자동차, 보배드림", "source": e["src_note"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["bar"], "channel": "란빵",
          "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
          "style": {"sub_box": True, "bar": e["bar"], "bar_count": e["cnt"], "watermark": ""},
          "lines": lines}
    json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)
    assert len(e["title"]) <= 12, (slug, e["title"], len(e["title"]))
    assert not RISKY.search(e["title"] + e["t1"] + e["t2"]), (slug, e["title"])
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    open(os.path.join(wk, "upload.md"), "w").write(
        f"# {slug} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n{e['desc']}\n\n"
        f"## 고정 댓글\n\n{e['cm']}\n\n## 쇼핑태그\n\n{e['tags']}\n\n"
        f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")
    open(os.path.join(wk, "v2", "ai_prompts.tsv"), "w").write("".join(f"{k}\t{v}{T}\n" for k, v in e["P"].items()))
    write_shots(slug, e["lines"])
    print("ok", slug, len(lines), "lines", n_ai, "ai", e["title"])
