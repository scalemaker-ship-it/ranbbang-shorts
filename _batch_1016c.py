#!/usr/bin/env python3
"""란빵 2026-10-16 신차 공개 뉴스 1편 ix4 (BMW iX4 세계 최초 공개 10/8). prd §4-6 「신차 공개 영상형」 구조 첫 적용.
화면 = BMW 공식 유튜브 영상 클립(work/_videos/ix4/: QTqKzj-uP5I 필름, EaT9LWne1eQ 워크어라운드) → work/ix4/v2/vid/
대사 2줄: 0번 구경꾼 반응(speaker 3), 6번 구매자 입장 대사(speaker 2, 실존 인물 발언 아님: BMW 임원 발언 인용을 못 찾음).
"""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SLUG = "ix4"
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")
Y, W, R = "#FBFF56", "#fff", "#FF3B30"
CR = "영상: BMW"


def V(name, at=None, s0=1.0, s1=1.08, fx=0.5, fy=0.5, punch=False, ss=0):
    d = {"vid": f"vid/{name}.mp4", "s0": s0, "s1": s1, "fx": fx, "fy": fy, "credit": CR}
    if at:
        d["at"] = at
    if punch:
        d["punch"] = True
    if ss:
        d["ss"] = ss
    return d


def L(text, sh, **k):
    d = {"text": text, "sh": sh}
    d.update(k)
    return d


lines = [
    L("와, 이게 SUV라고?", [V("h1"), V("h2", "SUV라고", punch=True)], say="와, 이게 에스유브이라고?",
      dialogue=True, speaker=3, emotion="toneup"),
    L("BMW가 X4를 전기차로 바꿔서 공개했는데, 한 번 충전에 828km를 감.", [V("c01"), V("c02", "828km를", punch=True)],
      say="비엠더블유가 엑스포를 전기차로 바꿔서 공개했는데, 한 번 충전에 팔백이십팔 키로를 감.",
      em=["828km를"], em_color="yellow", fx=[("hit_trailer_epic", "828km를", 0.55)], pop=("828km?!", Y, "828km를")),
    L("제원상으로는 서울 부산 왕복을 충전 한 번으로 다녀오는 거리임.", [V("h1", ss=1.0, s0=1.05, s1=1.15)],
      em=["왕복"], em_color="yellow", fx=[("drop_futuristic", "왕복을", 0.45)]),
    L("비결은 공기저항계수 0.23짜리 쿠페 지붕이랑 800볼트 배터리임.", [V("c04"), V("c04", "800볼트", ss=2.0, s0=1.2, s1=1.3)],
      say="비결은 공기저항계수 영 점 이삼짜리 쿠페 지붕이랑 팔백 볼트 배터리임.", em=["0.23짜리"], em_color="yellow"),
    L("급속충전기에 10분만 꽂아도 387km를 더 감.", [V("c05b"), V("c05", "387km를", punch=True)],
      say="급속충전기에 십 분만 꽂아도 삼백팔십칠 키로를 더 감.", em=["387km를"], em_color="yellow",
      fx=[("drop_futuristic", "387km를", 0.5)]),
    L("고성능 M60은 612마력에 제로백 3.9초.", [V("c06"), V("c06", "3.9초", ss=3.5, punch=True)],
      say="고성능 엠육십은 육백십이 마력에 제로백 삼 점 구 초.", em=["3.9초"], em_color="yellow",
      fx=[("hit_trailer_epic", "3.9초", 0.55)], pop=("3.9초!!", Y, "3.9초")),
    L("쿠페라 멋있긴 한데, 짐은 어디다 실어요?", [V("c07")], dialogue=True, speaker=2, emotion="toneup"),
    L("근데 형제차 iX3보다 주행거리는 23km 긴 대신, 짐 공간은 최대 150리터 작음.", [V("c08")],
      say="근데 형제차 아이엑스쓰리보다 주행거리는 이십삼 키로 긴 대신, 짐 공간은 최대 백오십 리터 작음.",
      em=["150리터"], fx=[("wrong_gameshow_buzz", "150리터", 0.45)],
      info={"kind": "compare", "at": "iX3보다", "title": "iX3 vs iX4 (50 xDrive)", "items": [
          {"label": "iX3", "color": W, "rows": [["주행거리", "805km", W], ["최대 적재", "1750L", Y]]},
          {"label": "iX4", "color": Y, "at": "23km", "rows": [["주행거리", "828km", Y], ["최대 적재", "1600L", R]]}]}),
    L("미국 시작가는 6만 6200달러, 출시는 2027년 3월임.", [V("c12"), V("c01", "출시는", ss=1.0, s0=1.1, s1=1.0)],
      say="미국 시작가는 육만 육천이백 달러, 출시는 이천이십칠 년 삼월임.", em=["6만 6200달러"], em_color="yellow"),
    L("근데 국내 출시 일정이랑 가격은 아직 비공개임.", [V("c10", s0=1.05, s1=1.15), V("c02", "가격은", s0=1.1, s1=1.2)], em=["비공개"],
      fx=[("scratch_vinyl", "비공개임", 0.45)]),
    L("님들은 짐 공간 줄어도 이 디자인이면 삼?", [V("h2", ss=1.0, s0=1.0, s1=1.12)], fx=[("pop_bubble", "삼")]),
]

assert any(l.get("dialogue") for l in lines)
for l in lines:
    assert not any(c.isdigit() for c in l.get("say", l["text"])), l["text"]
    if l.get("dialogue"):
        assert l.get("speaker", 1) != 1 and not l.get("em")
    for w in l.get("em", []):
        assert w in l["text"], w

t1, t2, bar = "X4가 전기차가 되자", "충전 한 번에 828km", "BMW iX4, 10월 8일 첫 공개"
title = "#충전 1번 828km"
assert len(title) <= 12 and not RISKY.search(title + t1 + t2)

wk = os.path.join(ROOT, "work", SLUG)
os.makedirs(os.path.join(wk, "v2"), exist_ok=True)
SK = ("sh", "fx", "pop", "shake", "info")
sc_lines = [{**{k: v for k, v in l.items() if k not in SK}, "img": 1} for l in lines]
sc_lines.append({"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": 1})
sc = {"slug": SLUG, "type": "란빵 자동차, 신차 뉴스", "source": "BMW iX4 세계 최초 공개 2026-10-08 (오토뷰, 오토트리뷴, Electrek)",
      "title_line1": t1, "title_line2": t2, "hook": bar, "channel": "란빵",
      "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
      "style": {"sub_box": True, "bar": bar, "bar_count": None, "watermark": ""}, "lines": sc_lines}
json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)

texts = [l["text"].rstrip(".") for l in sc_lines]
shot_lines = []
for i, l in enumerate(lines):
    d = {"shots": l["sh"]}
    if l.get("fx"):
        d["sfx"] = [list(x) for x in l["fx"]]
    for k in ("pop", "shake", "info"):
        if l.get(k):
            d[k] = list(l[k]) if k == "pop" else l[k]
    ws = [s.get("at") for s in d["shots"]] + [x[1] for x in d.get("sfx", [])] + [d.get("shake")]
    ws += [d["pop"][2]] if "pop" in d else []
    if "info" in d:
        ws += [d["info"].get("at")] + [it.get("at") for it in d["info"]["items"]]
    for w in ws:
        assert not w or w in texts[i], (i, w, texts[i])
    shot_lines.append(d)
shot_lines.append({"shots": [{"img": "real/outro.jpg", "s0": 1.0, "s1": 1.1, "credit": CR}],
                   "sfx": [["pop_long", "구독!"]], "pop": ["구독!", "#FFE629", "구독!"]})
json.dump({"bgmVol": 0.09, "bgm": "bgm/sneaky-123.mp3", "lines": shot_lines},
          open(os.path.join(wk, "v2", "shots.json"), "w"), ensure_ascii=False, indent=1)

proof = [("BMW iX4 세계 최초 공개 2026-10-08, 노이어 클라쎄 기반 전기 SUV 쿠페", "오토뷰 2026-10-08, Electrek 2026-10-08"),
         ("50 xDrive WLTP 최대 828km", "오토뷰, 오토트리뷴, BMW 공식 영상 자막 '828 km'"),
         ("서울 부산 왕복(약 800km)을 충전 한 번에: 제원상 828km 기준 계산", "828km(WLTP) 기준, 실주행은 더 짧을 수 있음"),
         ("공기저항계수 0.23(iX3 0.24), 800V 배터리", "오토뷰(Cd), 오토트리뷴(800V)"),
         ("최대 400kW 급속, 10분 충전 최대 387km(WLTP)", "오토트리뷴, BMW 공식 영상 자막 'up to 387 km in 10 minutes'"),
         ("M60 xDrive 612마력, 0~100km/h 3.9초", "오토뷰, BMW 공식 영상 자막"),
         ("'쿠페라 멋있긴 한데 짐은 어디다 실어요?'", "가상 구매자 대사(실존 인물 발언 아님)"),
         ("iX3 대비 주행거리 23km 길고(805→828km) 최대 적재 150L 작음(1750→1600L, 기본 520→490L)", "오토뷰 2026-10-08"),
         ("미국 시작가 6만 6200달러, 2027년 3월 출시", "Electrek 2026-10-08, 오토뷰/오토트리뷴(2027년 3월)"),
         ("국내 출시 일정과 가격 미공개", "오토헤럴드, 다나와 자동차")]
rows = "\n".join(f"| {a} | {b} |" for a, b in proof)
desc = ("BMW가 X4를 노이어 클라쎄 기반 전기 SUV 쿠페 iX4로 공개, 한 번 충전에 최대 828km.\n"
        "10분 급속충전으로 387km, 고성능 M60은 612마력에 제로백 3.9초.\n"
        "형제차 iX3보다 주행거리는 23km 길지만 짐 공간은 최대 150L 작음, 국내 출시와 가격은 미정.\n"
        "#shorts #BMW #iX4 #전기차 #신차")
open(os.path.join(wk, "upload.md"), "w").write(
    f"# {SLUG}: 업로드 메타 (란빵)\n\n## 제목\n\n{title}\n\n## 설명\n\n{desc}\n\n"
    f"## 고정 댓글\n\n님들은 짐 공간 줄어도 이 디자인이면 삼?\n\n"
    f"## 쇼핑태그\n\n전기차 충전 케이블, 트렁크 정리함, 차량용 휴대폰 거치대, 자동차 블랙박스 2채널, 차량용 무선충전기\n\n"
    f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n"
    f"원출처: https://www.autoview.co.kr/ko-kr/articles/102017 , https://www.autotribune.co.kr/news/articleView.html?idxno=46335 , https://electrek.co/2026/10/08/bmws-new-ix4-428-miles-range-66000-price-tag/\n"
    f"영상: BMW 공식 유튜브 QTqKzj-uP5I(Strikingly Vibrant | THE NEW BMW iX4), EaT9LWne1eQ(Walkaround iX4/iX3 M60)\n")
print("ok", SLUG, len(sc_lines), "lines")
