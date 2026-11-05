#!/usr/bin/env python3
"""란빵 2026-11-04 사용자 지정 소재(이슈쿠키 쇼츠 TxbY0b4oBC0) 1편 avantehill. v2(Remotion) + 영상 컷.
사용자 지시 "이 소재로 만들어서 올려. 영상 그대로 활용 원본 찾아서" → 원본 = 오토뷰 「2027 현대 아반떼 리뷰」 p-fojL1Acdc 07:41~09:56 '언덕 밀림 특성'.
클립 원본: work/_src/avantehill/hill.webm(07:35~10:00), 자른 클립 work/avantehill/v2/vid/ (얼굴, 번호판, 원본 자막 띠 제외 1012x900 크롭)
"""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SLUG = "avantehill"
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")
Y, W, R = "#FBFF56", "#fff", "#FF3B30"
CR = "영상: 오토뷰"


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
    L("어? 시동이 꺼져 버렸네요.", [V("v01", s0=1.0, s1=1.15, fx=0.45, fy=0.4)], dialogue=True, speaker=2, emotion="toneup",
      fx=[("scratch_vinyl", "꺼져", 0.5)]),
    L("신형 아반떼가 오르막 시험 중에 진짜로 시동이 꺼져버림.", [V("v02"), V("v03", "시동이", punch=True)],
      em=["시동이 꺼져버림"], em_color="yellow", fx=[("boom_zoom_impact", "시동이", 0.5)], pop=("시동 OFF?!", Y, "시동이")),
    L("오토뷰가 언덕에서 브레이크를 떼고 얼마나 밀리는지 봤는데", [V("v02", s0=1.1, s1=1.2), V("v08", "밀리는지")],
      em=["언덕에서"]),
    L("3초쯤 지나자 차가 뒤로 슬슬 밀리기 시작함.", [V("v03", s0=1.05, s1=1.15)],
      say="삼 초쯤 지나자 차가 뒤로 슬슬 밀리기 시작함.", em=["3초쯤"], em_color="yellow"),
    L("근데 밀리다가 퍽 소리와 함께 시동이 그냥 꺼짐.", [V("v01", s0=1.1, s1=1.25, fx=0.45, fy=0.4), V("v08", "꺼짐", punch=True)],
      em=["퍽"], em_color="yellow", fx=[("punch_strong", "퍽", 0.6)], shake="퍽"),
    L("다시 해봐도 퍽 하고 꺼지더니 그대로 쭉 밀려버림.", [V("v04", s0=1.0, s1=1.1, fx=0.4)],
      em=["그대로 쭉"], fx=[("wrong_gameshow_buzz", "밀려버림", 0.45)]),
    L("오토뷰 평가는 동급 모델 대비 주의 등급임.", [V("v05", s0=1.0, s1=1.08, fx=0.6, fy=0.3)],
      em=["주의 등급"], em_color="red", pop=("주의", R, "주의")),
    L("천천히 밀리는 건 그럴 수 있어도, 시동이 꺼지는 건 이상적이지 않다고 함.", [V("v09"), V("v03", "시동이", s0=1.1, s1=1.2)],
      em=["이상적이지 않다"]),
    L("다른 회사처럼 밀림을 감지하면 브레이크를 잡아주는 게 맞다는 거임.", [V("v06"), V("v10", "브레이크를")],
      em=["브레이크를 잡아주는"], em_color="yellow", fx=[("correct_ding", "브레이크를", 0.5)]),
    L("다른 차들은 안 그랬는데, 이 차만 그래서 사실 놀랐거든요.", [V("v07", s0=1.0, s1=1.12)],
      dialogue=True, speaker=2, emotion="toneup"),
    L("님들은 언덕에서 시동 꺼지면 침착하게 대처 가능함?", [V("v04", s0=1.1, s1=1.2, fx=0.4)],
      fx=[("pop_bubble", "가능함")]),
]

assert any(l.get("dialogue") for l in lines)
for l in lines:
    assert not any(c.isdigit() for c in l.get("say", l["text"])), l["text"]
    assert "—" not in l["text"] and "·" not in l["text"]
    if l.get("dialogue"):
        assert l.get("speaker", 1) != 1 and not l.get("em")
    for w in l.get("em", []):
        assert w in l["text"], w
chars = sum(len(l.get("say", l["text"])) for l in lines)
assert chars <= 370, chars

t1, t2, bar = "오르막서 밀리다", "시동 꺼진 신형 아반떼", "오토뷰 언덕 밀림 시험, 동급 대비 주의"
title = "#아반떼 언덕서 시동꺼짐"
assert len(title) <= 14 and not RISKY.search(title + t1 + t2)

wk = os.path.join(ROOT, "work", SLUG)
os.makedirs(os.path.join(wk, "v2"), exist_ok=True)
SK = ("sh", "fx", "pop", "shake", "info")
sc_lines = [{**{k: v for k, v in l.items() if k not in SK}, "img": 1} for l in lines]
sc_lines.append({"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": 1})
sc = {"slug": SLUG, "type": "란빵 자동차, 신차 시승 이슈",
      "source": "오토뷰 2027 현대 아반떼 리뷰 https://www.youtube.com/watch?v=p-fojL1Acdc 07:41 언덕 밀림 특성 (레퍼런스: 이슈쿠키 TxbY0b4oBC0)",
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
    for w in ws:
        assert not w or w in texts[i], (i, w, texts[i])
    shot_lines.append(d)
shot_lines.append({"shots": [{"img": "real/outro.jpg", "s0": 1.0, "s1": 1.1}],
                   "sfx": [["pop_long", "구독!"]], "pop": ["구독!", "#FFE629", "구독!"]})
json.dump({"bgmVol": 0.09, "bgm": "bgm/sneaky-123.mp3", "lines": shot_lines},
          open(os.path.join(wk, "v2", "shots.json"), "w"), ensure_ascii=False, indent=1)
open(os.path.join(wk, "v2", "ai_prompts.tsv"), "w").write("")

proof = [("브레이크를 떼고 약 3초 뒤 뒤로 밀림", "오토뷰 p-fojL1Acdc 07:49~07:58"),
         ("밀리던 중 시동 꺼짐 ('시동이 꺼져 버렸네요')", "오토뷰 08:02~08:05"),
         ("재시도(가속페달 살짝 뗌)에서도 '퍽' 하며 시동 꺼지고 그대로 밀림", "오토뷰 08:09~08:19"),
         ("언덕 밀림 특성 그래픽: 동급 모델 대비 '주의'", "오토뷰 08:39 화면 그래픽"),
         ("'천천히 밀리는 건 있을 수 있지만 시동 꺼지고 쭉 밀리는 건 이상적이지 않다'", "오토뷰 08:32~08:47"),
         ("'다른 회사처럼 미끌림 감지 시 브레이크 제어, 파크 브레이크 체결이 이상적'", "오토뷰 09:15~09:24"),
         ("'다른 차들은 안 그랬는데 이 차만 그러다 보니 놀랐다'", "오토뷰 09:51~09:55")]
rows = "\n".join(f"| {a} | {b} |" for a, b in proof)
desc = ("오토뷰 언덕 밀림 시험에서 신형 아반떼가 뒤로 밀리다 시동이 꺼졌습니다.\n"
        "두 번째 시도에서도 퍽 하고 꺼진 뒤 그대로 밀렸고, 평가는 동급 대비 주의.\n"
        "님들은 언덕에서 시동 꺼지면 바로 대처 가능함?\n"
        "#shorts #아반떼 #현대차 #신차 #오토뷰")
open(os.path.join(wk, "upload.md"), "w").write(
    f"# {SLUG}: 업로드 메타 (란빵)\n\n## 제목\n\n{title}\n\n## 설명\n\n{desc}\n\n"
    f"## 고정 댓글\n\n님들은 언덕에서 시동 꺼지면 침착하게 대처 가능함?\n\n"
    f"## 쇼핑태그\n\n차량용 고임목, 자동차 블랙박스 2채널, 차량용 휴대폰 거치대, 비상삼각대, 차량용 방향제\n\n"
    f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n"
    f"영상: 오토뷰(AutoView) https://www.youtube.com/watch?v=p-fojL1Acdc (07:35~10:00 일부 사용)\n"
    f"레퍼런스: https://youtube.com/shorts/TxbY0b4oBC0\n")
print("ok", SLUG, len(sc_lines), "lines", "chars", chars)
