#!/usr/bin/env python3
"""란빵 2026-10-16 — 매일경제 기사(테슬라 로드스터 2세대 공개) 1편 roadster. v2(Remotion) + **영상 컷**(Tesla 공식 유튜브 영상).
사용자 지시 "이 뉴스로 영상도 따다가 소재 만들어줘" — 이미지 대신 Tesla 공식 채널 영상을 1080x960 무음 클립으로 잘라 컷마다 쓴다.
클립 원본: work/_videos/roadster/ (yt-dlp, Tesla 공식 r5vsHHPVhJg·7p5LxFdc-Qg·cvKIR-c1SsU·qt5p-_tE8d0), 자른 클립: work/roadster/v2/vid/
대본 중간 대화체 1줄 필수(머스크 발언, speaker 2).
"""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SLUG = "roadster26"
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")
Y, W, R = "#FBFF56", "#fff", "#FF3B30"
CR = "영상: Tesla"


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
    # 2026-10-16 사용자 지시: 구경꾼 반응 대사(speaker 3, 머스크와 다른 목소리)로 영상 시작, 차가 공중에 뜬 컷
    L("와우, 대박인데?", [V("v03b", s0=1.05, s1=1.15, fy=0.35), V("v05", "대박인데", s0=1.1, s1=1.2, fx=0.4, fy=0.55, punch=True)], say="와우! 대박인데?", dialogue=True, speaker=3, emotion="toneup"),
    L("테슬라가 9년 미룬 로드스터를 드디어 공개했는데, 차가 하늘을 날아버림.",
      [V("v07"), V("v03", "하늘을", punch=True)], say="테슬라가 구 년 미룬 로드스터를 드디어 공개했는데, 차가 하늘을 날아 버림.",
      em=["하늘을"], em_color="yellow", fx=[("hit_trailer_epic", "하늘을", 0.55)], pop=("날았다?!", Y, "하늘을")),
    L("주차된 차 다섯 대를 그냥 점프해서 넘어가 버림.", [V("v02", s0=1.0, s1=1.12)],
      em=["다섯 대"], fx=[("boom_zoom_impact", "점프해서", 0.5)], shake="점프해서"),
    L("비결은 스페이스X 로켓 기술로 만든 압축공기 노즐 열 개임.", [V("v04b"), V("v05", "압축공기", s0=1.1, s1=1.2, fx=0.4, fy=0.55)],
      say="비결은 스페이스엑스 로켓 기술로 만든 압축공기 노즐 열 개임.", em=["압축공기"], em_color="yellow",
      fx=[("drop_futuristic", "압축공기", 0.5)]),
    L("거꾸로 선 벽을 타도 안 떨어지는데, 흡입 팬이 차를 바닥에 꽉 붙잡아줌.",
      [V("v01", s0=1.3, s1=1.45, fx=0.52, fy=0.3), V("v11", "흡입", s0=1.0, s1=1.1)], em=["흡입 팬"]),
    L("시속 97킬로까지 걸린 시간은 고작 0.81초.", [V("v06", s0=1.25, s1=1.35, fy=0.3), V("v07", "0.81초", punch=True)],
      say="시속 구십칠 키로까지 걸린 시간은 고작 영 점 팔일 초.", em=["0.81초"], em_color="yellow",
      fx=[("hit_trailer_epic", "0.81초", 0.55)], pop=("0.81초!!", Y, "0.81초")),
    L("안전이 최우선인 차는 아닙니다. 대신 재미는 10점 만점에 11점이에요.", [V("v08", s0=1.1, s1=1.18, fx=0.5, fy=0.35)],
      say="안전이 최우선인 차는 아닙니다. 대신 재미는 십 점 만점에 십일 점이에요.", dialogue=True, speaker=2, emotion="toneup",
      fx=[("drum_rimshot", "11점이에요", 0.45)]),
    L("근데 이거 2017년에 공개하고 2020년에 낸다던 차임.", [V("v09"), V("v10", "2020년에", s0=1.0, s1=1.1)],
      say="근데 이거 이천십칠 년에 공개하고 이천이십 년에 낸다던 차임.", em=["2020년에"], em_color="yellow",
      info={"kind": "compare", "at": "2017년에", "title": "출시 약속", "items": [
          {"label": "2017년 발표", "color": W, "rows": [["출시", "2020년", Y]]},
          {"label": "현실", "color": Y, "at": "2020년에", "rows": [["출시", "아직", R]]}]}),
    L("한정판 예약자는 25만 달러를 내고 9년째 기다리는 중임.", [V("v07", s0=1.15, s1=1.0), V("v09", "9년째", s0=1.5, s1=1.6, fx=0.6, fy=0.6, punch=True)],
      say="한정판 예약자는 이십오만 달러를 내고 구 년째 기다리는 중임.", em=["9년째"],
      fx=[("wrong_gameshow_buzz", "9년째", 0.45)], pop=("9년째", R, "9년째")),
    L("이번엔 2028년 양산이라는데, 가격이랑 주행거리는 또 비공개임.", [V("v10", s0=1.1, s1=1.0), V("v05", "가격이랑", s0=1.05, s1=1.15)],
      say="이번엔 이천 이십팔 년 양산이라는데, 가격이랑 주행 거리는 또 비 공개임.", em=["비공개"],
      fx=[("scratch_vinyl", "비공개임", 0.45)]),
    L("님들은 이번엔 진짜 2028년에 나온다고 봄?", [V("v11", s0=1.0, s1=1.12)],
      say="님들은 이번엔 진짜 이천이십팔 년에 나온다고 봄?", fx=[("pop_bubble", "봄")]),
]

assert any(l.get("dialogue") for l in lines)
for l in lines:
    assert not any(c.isdigit() for c in l.get("say", l["text"])), l["text"]
    if l.get("dialogue"):
        assert l.get("speaker", 1) != 1 and not l.get("em")
    for w in l.get("em", []):
        assert w in l["text"], w

t1, t2, bar = "9년 미룬 테슬라 신차", "결국 하늘을 날았다", "차 5대를 점프로 넘는 로드스터"
title = "#하늘나는 테슬라"
assert len(title) <= 12 and not RISKY.search(title + t1 + t2)

wk = os.path.join(ROOT, "work", SLUG)
os.makedirs(os.path.join(wk, "v2"), exist_ok=True)
SK = ("sh", "fx", "pop", "shake", "info")
sc_lines = [{**{k: v for k, v in l.items() if k not in SK}, "img": 1} for l in lines]
sc_lines.append({"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": 1})
sc = {"slug": SLUG, "type": "란빵 자동차, 신차 뉴스", "source": "매일경제 2026-10-16 테슬라 로드스터 2세대 공개",
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

proof = [("테슬라 2세대 로드스터 공개, 2017년 첫 공개 후 9년", "매일경제 2026-10-16 원호섭 특파원"),
         ("차량 5대 뛰어넘기, 공중 회전 착륙 시연", "매일경제 2026-10-16 / Tesla 공식 영상 'The Kickflip | Roadster'"),
         ("스페이스X 로켓 기술 응용 압축공기 추진, 노즐 10개", "매일경제 2026-10-16"),
         ("차체 아래 흡입 팬이 최대 2G 로 노면 밀착(거꾸로 주행)", "매일경제 2026-10-16(라스 모라비 부사장 발언)"),
         ("0~60마일(약 97km/h) 최단 0.81초", "매일경제 2026-10-16(테슬라 발표)"),
         ("'안전 최우선 차는 아니지만 재미는 10점 만점에 11점'", "매일경제 2026-10-16(머스크 발언, 의역)"),
         ("2017년 11월 공개, 2020년 생산 약속", "매일경제 2026-10-16"),
         ("파운더스 시리즈 예약금 25만 달러(1000대 한정)", "매일경제 2026-10-16"),
         ("2028년 양산, 가격·주행거리 미공개", "매일경제 2026-10-16")]
rows = "\n".join(f"| {a} | {b} |" for a, b in proof)
desc = ("테슬라가 9년 미룬 2세대 로드스터 공개, 압축공기 노즐로 차 5대를 점프해서 넘고 공중 회전 착륙까지.\n"
        "흡입 팬으로 거꾸로 선 벽 주행, 시속 97km까지 0.81초.\n"
        "2020년 출시 약속했던 차가 이번엔 2028년 양산 예고, 가격과 주행거리는 비공개.\n"
        "#shorts #테슬라 #로드스터 #일론머스크 #전기차")
open(os.path.join(wk, "upload.md"), "w").write(
    f"# {SLUG}: 업로드 메타 (란빵)\n\n## 제목\n\n{title}\n\n## 설명\n\n{desc}\n\n"
    f"## 고정 댓글\n\n님들은 이번엔 진짜 2028년에 나온다고 봄?\n\n"
    f"## 쇼핑태그\n\n테슬라 액세서리, 차량용 휴대폰 거치대, 자동차 블랙박스 2채널, 차량용 무선충전기, 전기차 충전 케이블\n\n"
    f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n"
    f"원출처: https://www.mk.co.kr/news/it/12177632\n"
    f"영상: Tesla 공식 유튜브 r5vsHHPVhJg(The Kickflip), 7p5LxFdc-Qg(The Ramp), cvKIR-c1SsU(Last Best Driver's Car), qt5p-_tE8d0(Roadster Event)\n")
print("ok", SLUG, len(sc_lines), "lines")
