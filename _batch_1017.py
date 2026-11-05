#!/usr/bin/env python3
"""란빵 2026-10-17 — 테슬라 로드스터 '날으는 차' 개드립 반응·원리·가격추측 편 roadsterfly. v2(Remotion) + 영상 컷.
사용자 지시 "테슬라 자동차 날으는걸로 영상 만들어줘. 사람들의 반응이나 원리, 가격추측등 개드립에서 찾아봐".
roadster26(공개 뉴스형, 10/16 공개)과 다른 각도 = 커뮤니티 반응. 클립은 roadster26 의 Tesla 공식 영상 클립 재사용(work/roadsterfly/v2/vid/).
수치: Electrek 2026-10-15(트림·0-60·예약금 5만 달러·로켓 공도 불가·냉가스 추진기 COPV·흡입 팬), Supercar Blondie(쓰러스트 예약 25만 달러).
"""

import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SLUG = "roadsterfly"
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
    # 2026-10-17 2차: "중간중간 대화체 + 더 신나는 톤" — 대사 6줄(speaker 3 = 들뜬 구경꾼, 2 = 딴지 거는 사람), exag 상향
    L("에이 이거 AI 아냐? 뭐, 진짜라고?", [V("v03b", s0=1.05, s1=1.15, fy=0.35), V("v03", "진짜라고", s0=1.05, s1=1.15, punch=True)],
      say="에이, 이거 에이아이 아냐? 뭐? 진짜라고?", dialogue=True, speaker=3, emotion="toneup", exag=0.95),
    L("테슬라 신차가 진짜로 하늘을 날자 커뮤니티가 난리 남!", [V("v02"), V("v03b", "하늘을", s0=1.1, s1=1.2, fy=0.35, punch=True, ss=1.0)],
      em=["하늘을"], em_color="yellow", fx=[("hit_trailer_epic", "하늘을", 0.55)], pop=("날았다?!", Y, "하늘을"), exag=0.85),
    L("비결은 탄소섬유 통에 꽉 눌러 담은 압축가스를 뿜는 추진기임!", [V("v04b"), V("v05", "뿜는", s0=1.1, s1=1.2, fx=0.4, fy=0.55)],
      say="비결은 탄소섬유 통에 꽉 눌러 담은 압축가스를 뿜는 추진기 임!",
      em=["압축가스"], em_color="yellow", fx=[("drop_futuristic", "압축가스를", 0.5)], exag=0.8),
    L("벽에 거꾸로 붙는 건, 팬이 바닥 공기를 빨아들여서 차를 꾹 눌러주는 원리!",
      [V("v01", s0=1.3, s1=1.45, fx=0.52, fy=0.3), V("v11", "빨아들여서", s0=1.0, s1=1.1)], em=["빨아들여서"], exag=0.8),
    L("와 이거 완전 카트라이더 부스터잖아!", [V("v06", s0=1.2, s1=1.3, fy=0.3)],
      dialogue=True, speaker=3, emotion="toneup", exag=0.95, fx=[("notify_message_pop", "카트라이더", 0.5)],
      info={"kind": "quotes", "at": "카트라이더", "title": "커뮤니티 반응", "items": [{"text": "“카트라이더 부스터 채우기네”"}]}),
    L("근데 타이어가 버팀? 버터 되겠는데?", [V("v05", s0=1.05, s1=1.15, fx=0.4, fy=0.55, ss=1.5)],
      dialogue=True, speaker=2, emotion="toneup", exag=0.9, fx=[("drum_rimshot", "버터", 0.45)]),
    L("제일 센 로켓 트림은 시속 97킬로까지 0.59초도 안 걸림!", [V("v06", s0=1.0, s1=1.1, fy=0.3, ss=0.5), V("v07", "0.59초도", punch=True)],
      say="제일 센 로켓 트림은 시속 구십칠 키로까지 영 점 오구 초도 안 걸림!", em=["0.59초"], em_color="yellow", exag=0.85,
      fx=[("drop_futuristic", "로켓", 0.45), ("hit_trailer_epic", "0.59초도", 0.55)],
      info={"kind": "bars", "at": "로켓", "title": "시속 97km까지", "sub": "테슬라 발표", "items": [
          {"label": "퍼포먼스", "value": 1.0, "num": 1.6, "dec": 1, "suffix": "초", "color": W},
          {"label": "쓰러스트", "value": 0.56, "num": 0.9, "dec": 1, "suffix": "초", "color": W},
          {"label": "로켓", "value": 0.37, "num": 0.59, "dec": 2, "suffix": "초", "color": Y, "at": "0.59초도", "flash": "0.59초도"}]}),
    L("근데 이거 어따 씀? 그리고 3억이잖아.", [V("v10", s0=1.0, s1=1.12), V("v07", "3억이잖아", s0=1.1, s1=1.2, punch=True)],
      say="근데 이거 어따 씀? 그리고 삼억이잖아!", dialogue=True, speaker=2, emotion="toneup", exag=0.9,
      fx=[("wrong_gameshow_buzz", "3억이잖아", 0.4)]),
    L("가격은 아직 비공개고, 예약금만 기본형 5만 달러, 쓰러스트 25만 달러임!", [V("v07", s0=1.15, s1=1.0), V("v10", "25만", s0=1.0, s1=1.1)],
      say="가격은 아직 비공개고, 예약금만 기본형 오만 달러, 쓰러스트 이십오만 달러임!", em=["25만 달러"], em_color="yellow", exag=0.8,
      fx=[("count_counter", "25만", 0.45)],
      info={"kind": "compare", "at": "예약금만", "title": "예약금(차값 아님)", "items": [
          {"label": "퍼포먼스", "color": W, "rows": [["예약금", "5만 달러", W]]},
          {"label": "쓰러스트", "color": Y, "at": "25만", "rows": [["예약금", "25만 달러", Y]]}]}),
    L("예약금이 3억이면 차값은 30억이겠네!", [V("v10", s0=1.1, s1=1.0), V("v09", "30억이겠네", s0=1.5, s1=1.6, fx=0.6, fy=0.6, punch=True)],
      say="예약금이 삼억이면 차값은 삼십억이겠네!", dialogue=True, speaker=3, emotion="toneup", exag=0.95,
      fx=[("cash_register_fake", "30억이겠네", 0.5)], pop=("30억?!", R, "30억이겠네"), shake="30억이겠네"),
    L("저거 지나가다 고라니도 빨려 들어가는 거 아냐?", [V("v01", s0=1.1, s1=1.2, fy=0.3, ss=2.0), V("v05", "고라니도", s0=1.05, s1=1.15, fx=0.4, fy=0.55)],
      dialogue=True, speaker=2, emotion="toneup", exag=0.9, fx=[("scratch_vinyl", "고라니도", 0.45)]),
    L("참고로 로켓 트림은 일반 도로 주행 자체가 안 됨!", [V("v11", s0=1.0, s1=1.12), V("v03b", "안", s0=1.0, s1=1.1, fy=0.35)],
      em=["안 됨"], em_color="yellow", fx=[("scratch_vinyl", "안", 0.45)], exag=0.85),
    L("님들은 이 차 얼마면 살 것 같음?", [V("v03", s0=1.0, s1=1.12)], fx=[("pop_bubble", "같음")], exag=0.85),
]

assert any(l.get("dialogue") for l in lines)
for l in lines:
    assert not any(c.isdigit() for c in l.get("say", l["text"])), l["text"]
    if l.get("dialogue"):
        assert l.get("speaker", 1) != 1 and not l.get("em")
    for w in l.get("em", []):
        assert w in l["text"], w

t1, t2, bar = "\"이거 AI 아님?\"", "진짜 나는 로드스터", "공중제비 도는 로드스터 실제 영상"
title = "#하늘나는 테슬라 반응"
assert len(title) <= 12 and not RISKY.search(title + t1 + t2)

wk = os.path.join(ROOT, "work", SLUG)
os.makedirs(os.path.join(wk, "v2"), exist_ok=True)
SK = ("sh", "fx", "pop", "shake", "info")
sc_lines = [{**{k: v for k, v in l.items() if k not in SK}, "img": 1} for l in lines]
sc_lines.append({"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": 1})
sc = {"slug": SLUG, "type": "란빵 자동차, 커뮤니티 반응", "source": "개드립 2026-10-16~17 테슬라 로드스터 반응 글 + Electrek 2026-10-15",
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

proof = [("'에이 이건 AI... 진짜라고?'", "개드립 729911991 댓글(의역)"),
         ("냉가스 추진기, 탄소섬유 압력용기(COPV)에 압축가스 저장", "Electrek 2026-10-15"),
         ("흡입 팬이 바닥 공기를 빨아 거꾸로도 붙어 있음", "Electrek 2026-10-15 / 개드립 729893101"),
         ("'카트라이더 부스터 채우기네' / '타이어가 버터됨'", "개드립 729904706 / 729858990 댓글(대사로 각색)"),
         ("트림별 0-60mph: 퍼포먼스 1.6초 미만, 쓰러스트 0.9초 미만, 로켓 0.59초 미만", "Electrek 2026-10-15(테슬라 발표) / 개드립 729858990"),
         ("'근데 3억이잖아 / 실생활 어디에 필요?'", "개드립 729904706 본문(의역)"),
         ("가격 비공개, 예약금 퍼포먼스 5만 달러", "Electrek 2026-10-15"),
         ("쓰러스트 예약금 25만 달러", "Supercar Blondie / 매일경제 2026-10-16(파운더스 25만 달러)"),
         ("'예약금이 3억이라 30억임'(추측, 대사로 각색)", "개드립 729904706 댓글. 25만 달러 = 약 3.5억 원"),
         ("'고라니 빨려 들어갈 것 같음'", "개드립 729951481 댓글(대사로 각색)"),
         ("로켓 트림 공도 주행 불가", "Electrek 2026-10-15(테슬라 로드스터 페이지)")]
rows = "\n".join(f"| {a} | {b} |" for a, b in proof)
desc = ("하늘을 나는 테슬라 로드스터 공개에 커뮤니티 반응 폭발, 압축가스 추진기와 흡입 팬 원리 정리.\n"
        "로켓 트림 시속 97km까지 0.59초 미만, 가격은 비공개에 예약금만 최대 25만 달러.\n"
        "예약금이 3억대면 차값은 얼마일까, 댓글 가격 추측까지.\n"
        "#shorts #테슬라 #로드스터 #일론머스크 #전기차")
open(os.path.join(wk, "upload.md"), "w").write(
    f"# {SLUG}: 업로드 메타 (란빵)\n\n## 제목\n\n{title}\n\n## 설명\n\n{desc}\n\n"
    f"## 고정 댓글\n\n님들은 이 차 얼마면 살 것 같음?\n\n"
    f"## 쇼핑태그\n\n테슬라 액세서리, 차량용 휴대폰 거치대, 자동차 블랙박스 2채널, 차량용 무선충전기, 전기차 충전 케이블\n\n"
    f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n"
    f"원출처: 개드립 https://www.dogdrip.net/dogdrip/729904706 , /729951481 , /729893101 , /729858990 , /729911991\n"
    f"https://electrek.co/2026/10/15/tesla-unveils-cyberfied-new-roadster-kickflip/\n"
    f"영상: Tesla 공식 유튜브 r5vsHHPVhJg(The Kickflip), 7p5LxFdc-Qg(The Ramp), cvKIR-c1SsU(Last Best Driver's Car), qt5p-_tE8d0(Roadster Event)\n")
print("ok", SLUG, len(sc_lines), "lines")
