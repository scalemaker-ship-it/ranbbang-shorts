#!/usr/bin/env python3
"""란빵 2026-11-04 대상 10편 (11/3 15:00 launchd 헤드리스 실행).
- 보배드림 베스트 7편(KGM 대리점, 벤츠 보증연장, 고라니, 스텔스, 트럭 후진, 공사장 알박기, 자전거) + 신차 2편(필랑트 누아르, 제네시스 라인) + 용품 1편(점프스타터).
- 근거 = work/research_1104.md, 원본 = work/_photos/b1104/ (map.txt). 보배드림 첨부 영상은 vclip() 으로 vid 컷.
- 실명, 상호(딜러사 이름), 지점명, 지명, 번호판 없음. 캐릭터 없음(NO_CHAR). 방송 진행자, 패널 얼굴 컷 안 씀.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1024 import B, C, L, build, IR, Y, W, R, P   # noqa: E402,F401
from _batch_1027 import cap as _cap   # noqa: E402
import _batch_1102 as _b2   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos", "b1104")
BB = "사진: 보배드림"
BV = "영상: 보배드림"
JT = "화면: JTBC 사건반장"
RN = "사진: 르노코리아"
COMMON = "자동차 블랙박스 2채널, 블랙박스 메모리카드, 비상삼각대, 차량용 핸드폰 거치대, 차량용 방향제"
MAXC = 365
V = _b2.V


def cap(*a, **k):
    k.setdefault("ph", PH)
    return _cap(*a, **k)


def vclip(*a, **k):
    _b2.PH = PH
    return _b2.vclip(*a, **k)


def go(S, lines, *rest, **kw):
    n = sum(len(l["text"]) for l in lines)
    assert 10 <= len(lines) <= 12, (S, len(lines))
    assert n <= MAXC, (S, "글자", n)
    for l in lines:
        assert "—" not in l["text"] and "·" not in l["text"], l["text"]
    build(S, lines, *rest, **kw)
    print(f"  chars {S} = {n} ({len(lines)}줄)")


# ───────────────────────── 1. KGM 대리점 2천만원 ─────────────────────────
def EP_kgm1600():
    S = "kgm1600"
    lines = [
        L("고객 주의 소홀이 구체적으로 뭔데요?",
          [B("k01", "A small Korean car dealership storefront at night with lights off and glass doors closed, empty showroom inside, no cars visible, no people, no readable signs or logos")],
          None, dialogue=True, speaker=2, emotion="toneup"),
        L("6월, 한 소비자가 KGM 대리점에서 토레스 구매 계약을 함.",
          [B("k02", "A car purchase contract paper and a pen on a dealership desk, a car key fob next to it, blurred text, warm light, no people, no logos")],
          None, say="유월, 한 소비자가 케이지엠 대리점에서 토레스 구매 계약을 함.", em=["KGM 대리점"]),
        L("계약금 10만원 뒤, 대리점주 계좌로 2천만원까지 보냄.",
          [B("k03", "Close-up of hands holding a smartphone showing a mobile banking transfer screen with blurred numbers, sitting at a desk, no faces, no readable text")],
          None, say="계약금 십마넌 뒤, 대리점주 계좌로 이천마넌까지 보냄.", em=["2천만원"], em_color="yellow",
          fx=[("drop_futuristic", "2천만원", 0.5)],
          info={"kind": "counter", "at": "2천만원까지", "title": "보낸 차값", "items": [{"num": 2000, "suffix": "만원"}]}),
        L("그런데 차는 안 나왔고, 7월에 가 보니 대리점은 문을 닫았음.",
          [B("k01", s0=1.1, s1=1.3, punch=True)], None, say="그런데 차는 안 나왔고, 칠월에 가 보니 대리점은 문을 닫았음.",
          em=["문을 닫았음"], shake="닫았음", fx=[("hit_trailer_epic", "닫았음", 0.45)]),
        L("경찰에 신고했고 사건은 검찰로 넘어간 상태.",
          [B("k04", "A Korean police station counter with complaint forms and a pen, fluorescent light, no people, no readable text")], None, em=["검찰로"]),
        L("본사가 제시한 보상금은 2천만원이 아니라 1600만원.",
          [B("k02", s0=1.2, s1=1.35)], None, say="본사가 제시한 보상금은 이천마넌이 아니라 천육백마넌.", em=["1600만원"], em_color="yellow",
          info={"kind": "bars", "at": "본사가", "title": "보낸 돈 vs 보상 제안", "items": [
              {"label": "보낸 돈", "num": 2000, "suffix": "만원", "at": "본사가"},
              {"label": "본사 제안", "num": 1600, "suffix": "만원", "at": "1600만원", "flash": "1600만원"}]}),
        L("보증보험 한도를 넘는 피해라 20%를 깎아야 한다는 설명.",
          [B("k05", "An insurance guarantee document with a red stamp and a calculator on an office desk, blurred text, no people")],
          None, say="보증보험 한도를 넘는 피해라 이십퍼센트를 깎아야 한다는 설명.", em=["20%"]),
        L("본사 계좌 말고 개인 계좌로 보낸 게 고객 주의 소홀이라고 함.",
          [B("k03", s0=1.2, s1=1.35)], None, em=["주의 소홀"], em_color="yellow", pop=("주의 소홀?!", R, "주의 소홀이라고"),
          fx=[("wrong_gameshow_buzz", "주의", 0.45)]),
        L("글쓴이는 로고 박힌 명함과 견적서에 적힌 계좌로 보냈다고 반박함.",
          [B("k06", "A business card and a printed car price quotation sheet on a desk, blurred text and blurred logo, soft light, no people")],
          None, em=["견적서에 적힌 계좌"]),
        L("댓글은 보통 계약금만 걸고 출고 때 잔금 아니냐는 반응.",
          [B("k06", s0=1.2, s1=1.3)], None, em=["출고 때 잔금"]),
        L("님들이면 1600 받고 끝냄, 소송 감?", [B("k01", s0=1.0, s1=1.1)], None, say="님들이면 천육백 받고 끝냄, 소송 감?",
          fx=[("pop_bubble", "감")]),
    ]
    go(S, lines, "대리점에 2천만원 냈는데", "본사 보상은 1600만원", "대리점주 잠적, 본사는 20% 감액 제안",
       "#대리점 잠적 2천만원", "보배드림 베스트 1044884 (2026-11-03, 추천 372, 댓글 29) https://www.bobaedream.co.kr/view?code=best&No=1044884",
       [("6/16 KGM 대리점에서 뉴 토레스 계약, 차량대금 총 2000만원 송금", "원글 본문"),
        ("계약금 10만원, 다음 날 캐피탈 승인, 선입 1500만원, 추가 500만원", "글쓴이 댓글"),
        ("약속한 시기에 인도 못 받음, 7/3 방문 시 대리점 운영 안 함, 경찰 신고 후 검찰 송치", "원글 본문"),
        ("본사: 서울보증보험 보증한도 초과로 약 20% 감액, 1600만원 제안, 개인 계좌 송금은 고객 주의 소홀", "원글 본문"),
        ("KGM 로고 명함, 견적서에 계좌 기재, 그 계좌로 안내받아 송금", "원글 본문(글쓴이 주장)"),
        ("'고객의 주의 소홀이 구체적으로 무엇인지 묻자'", "원글 본문(대사 근거)"),
        ("댓글 '보통 국내 차량은 계약금(10만) 걸고 출고시 잔금 결재'(34)", "원글 댓글")],
       "대리점에서 차를 계약하고 2천만원을 보냈는데 대리점주가 사라졌습니다.\n본사는 개인 계좌로 보낸 고객에게도 주의 소홀이 있다며 1600만원을 제안했습니다.\n님들이면 받고 끝내나요, 소송 가나요?\n\n#자동차계약 #대리점 #KGM #보배드림 #란빵",
       "님들이면 1600 받고 끝냄, 소송 감?",
       "자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 자동차 시트커버, 차량용 방향제, 비상삼각대",
       "대리점 지역명, 대리점주 이름, 예금주 이름은 안 씀. 첨부 사진 없음, 화면 전부 AI 배경(차종이 특정되는 차 그림 안 씀).",
       [B("k05", s0=1.0, s1=1.08)])


# ───────────────────────── 2. 벤츠 보증연장 위약금 337 ─────────────────────────
def EP_benzew337():
    S = "benzew337"
    cap(S, "ew", "1044641_00.jpg", box=(0, 540, 749, 730), fit=True, nofaces=True, boxes=[(175, 150, 100, 17), (45, 8, 70, 20)])
    cap(S, "sign", "1044641_01.jpg", box=(0, 700, 713, 990), fit=True, nofaces=True, boxes=[(190, 0, 85, 28), (50, 45, 72, 70), (55, 118, 62, 62)])
    lines = [
        L("직원 개인 실수일 뿐이에요. 억울하면 그 직원을 고소하세요.",
          [B("z01", "A luxury car dealership office meeting table with documents and a pen, glass wall, blurred showroom lights behind, no cars, no people, no logos")],
          None, dialogue=True, speaker=3, emotion="normal"),
        L("2021년 벤츠 S클래스 두 대를 뽑으며 대당 629만원 보증연장에 가입함.",
          [P("ew", BB, s0=1.0, s1=1.12, fx=0.4, fy=0.45), P("ew", BB, at="629만원", s0=1.5, s1=1.65, fx=0.27, fy=0.55, punch=True)],
          None, say="이천이십일년 벤츠 에스클래스 두 대를 뽑으며 대당 육백이십구마넌 보증연장에 가입함.", em=["629만원"]),
        L("차를 팔고 남은 기간을 환불받으려다 처음 알게 됨.",
          [B("z02", "A stack of car service warranty papers in a folder on a home desk at night, desk lamp, blurred text, no people")], None, em=["환불받으려다"]),
        L("가입 신청서 서명란에 자기 이름이 다른 필체로 적혀 있었다는 것.",
          [P("sign", BB, s0=1.0, s1=1.12), P("sign", BB, at="다른", s0=1.6, s1=1.8, fx=0.86, fy=0.7, punch=True)],
          None, em=["다른 필체로"], em_color="yellow", pop=("대필?!", R, "필체로"), fx=[("hit_trailer_epic", "필체로", 0.45)]),
        L("해지하면 위약금 20%라는 설명도 못 들었다고 주장함.",
          [P("ew", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, say="해지하면 위약금 이십퍼센트라는 설명도 못 들었다고 주장함.", em=["위약금 20%"]),
        L("한 대는 위약금 없이 환불, 다른 한 대는 337만원이 빠졌음.",
          [B("z02", s0=1.2, s1=1.35)], None, say="한 대는 위약금 없이 환불, 다른 한 대는 삼백삼십칠마넌이 빠졌음.", em=["337만원"], em_color="yellow",
          fx=[("drop_futuristic", "337만원", 0.5)],
          info={"kind": "bars", "at": "다른", "title": "빠진 위약금", "items": [
              {"label": "해지 위약금 20%", "num": 125.8, "dec": 1, "suffix": "만원", "at": "다른"},
              {"label": "일할 위약금", "num": 212.2, "dec": 1, "suffix": "만원", "at": "337만원이"}]}),
        L("같은 직원, 같은 서명인데 결과가 달랐다는 게 글쓴이 말.",
          [P("sign", BB, s0=1.1, s1=1.2)], None, em=["결과가 달랐다"]),
        L("딜러사 책임자 답은 직원 개인 실수, 회사 책임은 없다.",
          [B("z01", s0=1.2, s1=1.3)], None, em=["회사 책임은 없다"], fx=[("wrong_gameshow_buzz", "없다", 0.4)]),
        L("댓글은 직원 잘못이면 회사도 책임 아니냐는 반응이 많았음.",
          [B("z03", "A judge's gavel and a contract with a signature line on a wooden desk, soft light, blurred text, no people")], None, em=["회사도 책임"]),
        L("반면 돈을 보냈으니 동의한 대필이라 위조는 아닐 수 있다는 의견도.",
          [B("z03", s0=1.2, s1=1.3)], None, em=["동의한 대필"]),
        L("님들은 이거 딜러사 책임이라고 봄?", [P("ew", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "벤츠 보증연장 해지했더니", "위약금 337만원", "서명은 대필, 위약금 설명도 없었다는 주장",
       "#보증연장 위약금 337", "보배드림 베스트 1044641 (2026-11-02, 추천 81, 댓글 19) https://www.bobaedream.co.kr/view?code=best&No=1044641",
       [("2021년 S클래스 2대(S450, S350d) 출고, 차량당 629만원 보증연장(EW) 가입", "원글 본문, 첨부 신청서(6,290,000)"),
        ("차량 2대 매각 후 남은 기간 환불 과정에서 서명 대필과 위약금 존재를 알게 됨", "원글 정정 본문"),
        ("영업사원이 해지 시 20% 위약금 설명 안 함, 서명란 대필", "원글 본문(글쓴이 주장)"),
        ("S350d 해지위약금 20% 1,258,000원 + 일할 위약금 2,121,599원 = 337만원 차감, S450은 위약금 없이 환불", "원글 본문"),
        ("책임자 '담당 직원의 개인 실수일 뿐 회사는 책임이 없다, 억울하면 그 직원을 직접 고소해라'", "원글 본문(대사 근거)"),
        ("댓글 '사문서 위조면 회사에도 책임이 있는 거 아닌가요'(21), '보증연장 비용 송금으로 동의, 동의에 의한 대필이라 사문서위조는 아니라고 보임'(1)", "원글 댓글")],
       "벤츠 보증연장을 해지하다 보니 신청서 서명이 다른 필체였고, 위약금 337만원이 빠졌다는 주장입니다.\n딜러사 답은 직원 개인 실수라 회사 책임은 없다는 것이었습니다.\n님들은 누구 책임이라고 보나요?\n\n#벤츠 #보증연장 #위약금 #보배드림 #란빵",
       "님들은 이거 딜러사 책임이라고 봄?",
       "자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 자동차 시트커버, 차량용 방향제, 자동차 햇빛가리개",
       "딜러사 이름, 전시장 이름, 영업사원 이름은 안 씀. 서류 캡처의 회사 로고, 지점명 손글씨, 개인정보는 잘라내거나 모자이크.",
       [B("z01", s0=1.0, s1=1.08)])


# ───────────────────────── 3. 고라니 밟고 미끄러짐 ─────────────────────────
def EP_deerslip():
    S = "deerslip"
    vclip(S, "v1", "1044844_m0.mp4", 3, 8, cx=0.5, cy=0.33, zoom=1.15)
    vclip(S, "v2", "1044844_m0.mp4", 11, 11, cx=0.5, cy=0.36, zoom=1.15)
    lines = [
        L("당황해도 브레이크 밟지 말고 그냥 지나가세요.",
          [V("v2", ss=4, s0=1.1, s1=1.2)], None, dialogue=True, speaker=2, emotion="normal"),
        L("퇴근길 밤, 자동차 전용도로를 달리던 블박차.",
          [V("v1", s0=1.0, s1=1.08)], None, em=["자동차 전용도로"]),
        L("도로 한가운데에 고라니 사체가 툭 나타남.",
          [V("v1", ss=4, s0=1.1, s1=1.2, punch=True)], None, em=["고라니 사체"], em_color="yellow",
          fx=[("hit_trailer_epic", "툭", 0.4)]),
        L("피할 틈 없이 밟자 차가 쫙 미끄러짐.",
          [V("v2", s0=1.0, s1=1.1)], None, em=["미끄러짐"], shake="미끄러짐"),
        L("브레이크에 엔진브레이크까지 썼지만 결국 가드레일에 쾅.",
          [V("v2", ss=3, s0=1.1, s1=1.25, punch=True)], None, em=["가드레일에 쾅"],
          shake="쾅", fx=[("glass_smash", "쾅", 0.5)], pop=("쾅!!", R, "쾅")),
        L("앞서 대형차가 친 사체의 가죽을 밟은 것 같다는 게 렉카 기사 말.",
          [B("d01", "A dark highway at night with a guardrail and reflective road markers, wet asphalt under headlights, no vehicles visible, no people")],
          None, em=["가죽을 밟은"]),
        L("다친 데는 없지만 차 앞과 옆이 다 부서짐.",
          [B("d02", "A damaged sedan's front bumper and side panel crumpled next to a highway guardrail at night, hazard lights glowing, no people, no license plate visible")],
          None, em=["다 부서짐"]),
        L("그런데 댓글 추천 1위는 단 한마디, 빠르다.",
          [V("v1", ss=2, s0=1.0, s1=1.1)], None, say="그런데 댓글 추천 일위는 단 한마디, 빠르다.", em=["빠르다"], em_color="yellow",
          pop=("빠르다...", Y, "빠르다"), fx=[("drum_rimshot", "빠르다", 0.5)]),
        L("반사 표지 지나가는 간격으로 보면 시속 150은 넘어 보인다는 분석도.",
          [V("v1", ss=5, s0=1.15, s1=1.3)], None, say="반사 표지 지나가는 간격으로 보면 시속 백오십은 넘어 보인다는 분석도.", em=["시속 150"]),
        L("글쓴이는 시속 100km 정도였다고 해명함.",
          [V("v2", ss=6, s0=1.0, s1=1.08)], None, say="글쓴이는 시속 백 킬로 정도였다고 해명함.", em=["100km"]),
        L("보험사는 피할 수 없던 사고로 보고 할증을 유예해 줌.",
          [B("d01", s0=1.2, s1=1.3)], None, em=["할증을 유예"], fx=[("correct_ding", "유예해", 0.45)]),
        L("님들은 밤에 저런 거 보이면 밟음, 피함?", [V("v1", ss=4, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "피함")]),
    ]
    go(S, lines, "퇴근길 전용도로에서", "고라니 밟고 미끄러짐", "고라니 사체 밟고 미끄러져 가드레일 충돌",
       "#고라니 밟고 미끄러짐", "보배드림 베스트 1044844 (2026-11-03, 추천 235, 댓글 90) https://www.bobaedream.co.kr/view?code=best&No=1044844",
       [("퇴근길 자동차 전용도로, 도로 한가운데 고라니 사체를 밟고 미끄러짐, 브레이크와 엔진브레이크, 가드레일 충돌", "원글 본문, 영상"),
        ("측면, 전면 파손, 목 뻐근한 것 외 부상 없음", "원글 본문"),
        ("렉카 기사 '앞쪽에서 대형차가 치고 간 지 얼마 안 된 것 같고, 가죽 밟으면서 미끄러진 듯'", "원글 본문"),
        ("댓글 '빠르다'(66), '25m 간격 형광 동그라미가 0.6초면 시속 150km'(9)", "원글 댓글"),
        ("추가: 150~160은 아니고 100km 정도, 보험사가 피할 수 없는 사고로 보고 할증 유예", "원글 추가 내용"),
        ("'당황하시더라도 브레이크 밟지 마시고 그냥 지나가시길'", "원글 추가 내용(대사 근거)")],
       "퇴근길 자동차 전용도로에서 고라니 사체를 밟고 미끄러져 가드레일에 부딪혔습니다.\n댓글 추천 1위는 '빠르다'였고, 보험사는 할증을 유예해 줬다고 합니다.\n님들은 밤에 저런 걸 보면 밟나요, 피하나요?\n\n#로드킬 #블랙박스 #교통사고 #보배드림 #란빵",
       "님들은 밤에 저런 거 보이면 밟음, 피함?",
       COMMON, "영상은 휴대폰으로 블박 화면을 찍은 원글 영상. 사체가 직접 보이는 장면은 화면이 어두워 판별 안 됨(사체 클로즈업 없음).",
       [V("v2", ss=2, s0=1.0, s1=1.05)])


# ───────────────────────── 4. 비 오는 밤 스텔스 ─────────────────────────
def EP_stealthrain():
    S = "stealthrain"
    vclip(S, "v1", "1044718_m0.mp4", 6, 20, cx=0.45, cy=0.6, zoom=1.15, eq="eq=brightness=0.05:gamma=1.3")
    vclip(S, "v2", "1044718_m1.mp4", 0, 11.5, cx=0.5, cy=0.6, zoom=1.15, eq="eq=brightness=0.05:gamma=1.3")
    lines = [
        L("빵빵해도, 쌍라이트를 켜도 그냥 자기 갈 길 가더라고요.",
          [V("v1", ss=3, s0=1.1, s1=1.2)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("비 오는 저녁 국도, 앞의 검은 차가 라이트를 다 끄고 달림.",
          [V("v1", s0=1.0, s1=1.08), V("v1", at="라이트를", ss=5, s0=1.2, s1=1.35, punch=True)], None,
          em=["라이트를 다 끄고"], em_color="yellow", fx=[("wrong_gameshow_buzz", "끄고", 0.4)]),
        L("이른바 스텔스 차량, 1차로에서 거의 안 보임.",
          [V("v1", ss=8, s0=1.1, s1=1.25)], None, say="이른바 스텔스 차량, 일차로에서 거의 안 보임.", em=["스텔스 차량"],
          pop=("스텔스", R, "스텔스")),
        L("글쓴이가 앞질러 속도를 줄이고 자기 라이트를 껐다 켜 봄.",
          [V("v2", s0=1.0, s1=1.1)], None, em=["껐다 켜 봄"]),
        L("그래도 끝까지 못 알아챘다고 함.",
          [V("v2", ss=5, s0=1.1, s1=1.2)], None, em=["못 알아챘다고"], fx=[("drum_rimshot", "못", 0.45)]),
        L("도로교통법 37조, 밤이나 비 올 땐 전조등과 미등을 켜야 함.",
          [B("s01", "A dark sedan driving on a rainy rural Korean road at dusk with its headlights off, seen from behind at a distance, rain on windshield, no people, no license plate visible")],
          None, say="도로교통법 삼십칠조, 밤이나 비 올 땐 전조등과 미등을 켜야 함.", em=["전조등과 미등"],
          info={"kind": "quotes", "at": "도로교통법", "title": "도로교통법 37조 1항", "items": [
              {"text": "밤에 도로를 달릴 때", "at": "밤이나"}, {"text": "비, 눈, 안개 올 때", "at": "비"}, {"text": "전조등, 미등 켜기", "at": "켜야"}]}),
        L("글쓴이는 과태료 30만원에, 사고 나면 스텔스 독박이어야 한다고 함.",
          [V("v1", ss=11, s0=1.0, s1=1.1)], None, say="글쓴이는 과태료 삼십마넌에, 사고 나면 스텔스 독박이어야 한다고 함.", em=["독박"]),
        L("댓글엔 같은 날 스텔스를 봤다는 목격담이 줄줄이.",
          [V("v1", ss=14, s0=1.1, s1=1.2)], None, em=["목격담"]),
        L("세차장이나 카센터 다녀오면 라이트가 꺼져 있을 수 있다는 팁도.",
          [B("s02", "Close-up of a car's headlight control stalk on the steering column in a dim car interior, the switch set to off, no people")],
          None, em=["꺼져 있을 수"], fx=[("correct_ding", "팁도", 0.4)]),
        L("앞에 있을 땐 짜증, 뒤에 있으면 섬뜩하다는 반응.",
          [V("v2", ss=8, s0=1.0, s1=1.1)], None, em=["섬뜩"]),
        L("님들은 스텔스 보면 어떻게 알려 줌?", [V("v1", ss=6, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "줌")]),
    ]
    go(S, lines, "비 오는 국도 1차로", "라이트 끄고 달리는 차", "비 오는 저녁, 라이트 끈 스텔스 차량",
       "#비 오는 날 스텔스", "보배드림 베스트 1044718 (2026-11-02, 추천 62, 댓글 19) https://www.bobaedream.co.kr/view?code=best&No=1044718",
       [("야간, 검정색, 비 오는데, 1차로, 라이트 끄고 주행, 앞질러 속도 낮추고 라이트 꺼 봤지만 못 알아챔", "원글 본문, 영상 2개"),
        ("'주변차들 빵빵에 쌍라에 뭔짓을 해도 그냥 지 갈길'", "원글 본문(대사 근거)"),
        ("'과태료 30만원씩 물리고 사고 나도 스텔스 독박'", "원글 본문(글쓴이 주장)"),
        ("도로교통법 37조 1항 1호 밤, 2호 안개, 비, 눈 올 때 전조등, 차폭등, 미등 켜야 함", "casenote 도로교통법 37조"),
        ("댓글 '어제 스텔스 검정 그랜저 봤다'(3, 2), '손세차장이나 카센터 들어갔다 나오면 라이트 꺼져 있음'(1), '앞에 보일 땐 짜증, 뒤로 보이면 섬뜩'", "원글 댓글")],
       "비 오는 저녁 국도에서 라이트를 다 끈 검은 차가 1차로를 달리고 있었습니다.\n도로교통법 37조는 밤이나 비 올 때 전조등과 미등을 켜도록 합니다.\n님들은 스텔스 차량을 보면 어떻게 알려 주나요?\n\n#스텔스차량 #전조등 #블랙박스 #보배드림 #란빵",
       "님들은 스텔스 보면 어떻게 알려 줌?",
       "자동차 블랙박스 2채널, 차량용 LED 전구, 자동차 발수코팅제, 차량용 핸드폰 거치대, 차량용 방향제",
       "범칙금 액수는 확인 안 돼 안 씀(글쓴이의 30만원은 주장으로만). 지역명 안 씀. 번호판 판독 불가.",
       [V("v2", ss=3, s0=1.0, s1=1.05)])


# ───────────────────────── 5. 트럭 후진에 과실 10 ─────────────────────────
def EP_truckback():
    S = "truckback"
    vclip(S, "v1", "1044712_m0.mp4", 18, 14, cx=0.47, cy=0.5, zoom=1.05)
    lines = [
        L("냅다 후진해서 박아 놓고 제 과실이라고요?",
          [V("v1", ss=10, s0=1.1, s1=1.2)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("우회전하려고 아주 천천히 가던 블박차.",
          [V("v1", s0=1.0, s1=1.06)], None, em=["우회전"]),
        L("가게 앞 트럭 기사가 타자마자 뒤도 안 보고 후진함.",
          [V("v1", ss=6, s0=1.05, s1=1.15)], None, em=["타자마자"]),
        L("그대로 블박차 옆을 쾅.",
          [V("v1", ss=10, s0=1.1, s1=1.25, punch=True)], None, em=["쾅"], shake="쾅",
          fx=[("hit_trailer_epic", "쾅", 0.5)], pop=("쾅!!", R, "쾅")),
        L("트럭이 직각으로 서 있어 후진등도 잘 안 보였다고 함.",
          [V("v1", ss=8, s0=1.2, s1=1.35, fx=0.6)], None, em=["후진등"]),
        L("그런데 보험사는 블박차 과실 10을 주장함.",
          [B("t01", "An insurance claim form with a percentage box and a pen on a desk next to a phone, blurred text, no people")],
          None, say="그런데 보험사는 블박차 과실 십을 주장함.", em=["과실 10"], em_color="yellow",
          pop=("과실 10?!", Y, "과실"), fx=[("wrong_gameshow_buzz", "주장함", 0.45)]),
        L("상대도 같은 보험사라 소송도 안 받아 준다고.",
          [B("t01", s0=1.2, s1=1.3)], None, em=["같은 보험사"]),
        L("댓글은 후진 100이다, 분심위는 가지 말라는 쪽이 많음.",
          [V("v1", ss=11, s0=1.0, s1=1.1)], None, say="댓글은 후진 백이다, 분심위는 가지 말라는 쪽이 많음.", em=["후진 100"]),
        L("손보협회 도표로 기본 8대2에 후진이라 9대1 같다는 분석도.",
          [B("t02", "A printed traffic accident fault ratio chart with simple car diagrams on a desk, blurred text, no people")],
          None, say="손보협회 도표로 기본 팔대이에 후진이라 구대일 같다는 분석도.", em=["9대1"], em_color="yellow",
          info={"kind": "compare", "at": "손보협회", "title": "댓글 분석", "items": [
              {"label": "기본", "color": W, "at": "기본", "rows": [["도표", "8:2", Y]]},
              {"label": "후진 반영", "color": R, "at": "후진이라", "rows": [["추정", "9:1", Y]]}]}),
        L("가게 CCTV를 꼭 확보하라는 조언도 나옴.",
          [B("t03", "A CCTV camera mounted above a Korean convenience store entrance facing the street, daytime, no people, no readable signs")],
          None, say="가게 씨씨티비를 꼭 확보하라는 조언도 나옴.", em=["CCTV"]),
        L("님들이 보기엔 블박차 과실 있음?", [V("v1", ss=10, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "천천히 우회전 중인데", "트럭이 후진으로 쾅", "타자마자 후진한 트럭, 보험사는 블박차 과실 10",
       "#후진 트럭인데 과실10", "보배드림 베스트 1044712 (2026-11-02, 추천 26, 댓글 10) https://www.bobaedream.co.kr/view?code=best&No=1044712",
       [("우회전 위해 매우 서행 중, 트럭이 탑승하자마자 살피지 않고 바로 후진해 충돌", "원글 본문, 영상"),
        ("트럭이 직각이라 후진등이 잘 안 보임", "원글 본문"),
        ("보험사 글쓴이 과실 10 주장, 상대도 같은 보험사라 소송 안 받아 줌, 편의점 CCTV 확보 고민", "원글 본문"),
        ("'냅다 박아버리곤 상대는 제 과실 주장'", "원글 본문(대사 근거)"),
        ("댓글 '후진 100'(3), '분심위는 가는 곳이 아니고 무과실'(3), '손보협 도표 기본 8:2, 후진출차라 +1 해서 9:1'(1)", "원글 댓글")],
       "천천히 우회전하던 블박차를 트럭이 타자마자 후진해서 박았는데, 보험사는 블박차 과실 10을 주장합니다.\n댓글은 후진 100이라는 쪽이 많았습니다.\n님들이 보기엔 블박차 과실 있나요?\n\n#블랙박스 #과실비율 #후진사고 #보배드림 #란빵",
       "님들이 보기엔 블박차 과실 있음?",
       "자동차 블랙박스 2채널, 후방카메라, 차량용 핸드폰 거치대, 비상삼각대, 차량용 방향제",
       "영상은 모니터 화면을 휴대폰으로 찍은 원글 영상, 왼쪽 썸네일 영역은 잘라냄. 번호판 판독 불가. 가게 이름 안 씀.",
       [V("v1", ss=9, s0=1.0, s1=1.05)])


# ───────────────────────── 6. 가스 공사장 알박기 ─────────────────────────
def EP_gasblock():
    S = "gasblock"
    cap(S, "night", "1044892_00.jpg", box=(0, 2470, 1206, 2965))
    cap(S, "car", "1044892_00.jpg", box=(0, 1857, 1206, 2380), nofaces=True)
    cap(S, "sil", "1044892_00.jpg", box=(0, 6767, 1206, 7370), fit=True)
    cap(S, "sil2", "1044892_00.jpg", box=(0, 7394, 1206, 7985), fit=True)
    cap(S, "cctv", "1044892_01.jpg", box=(0, 1833, 1206, 2360), boxes=[(330, 40, 170, 150), (250, 250, 160, 100)])
    cap(S, "note", "1044892_01.jpg", box=(0, 4306, 1206, 4897), fit=True, nofaces=True)
    lines = [
        L("차 건드리지 마세요. 민형사 소송해요.",
          [P("note", JT, s0=1.0, s1=1.12)], None, dialogue=True, speaker=3, emotion="normal"),
        L("도시가스가 안 들어와 올해 1월에 공사를 신청한 건물주.",
          [B("g01", "A small Korean commercial building at night with a shuttered shop front and a narrow sidewalk, orange traffic cones on the road edge, no people, no readable signs")],
          None, say="도시가스가 안 들어와 올해 일월에 공사를 신청한 건물주.", em=["도시가스"]),
        L("몇 달 만에 공사가 시작됐는데 배관 자리에 차 한 대가 보름째 서 있음.",
          [P("night", JT, s0=1.0, s1=1.12), P("car", JT, at="보름째", s0=1.0, s1=1.15)], None, em=["보름째"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "보름째", 0.4)]),
        L("차주는 다른 지역이라 못 뺀다며 연락처도 알려 주지 말라고 함.",
          [P("sil", JT, s0=1.0, s1=1.1), P("sil2", JT, at="연락처도", s0=1.0, s1=1.1)], None, em=["연락처도"]),
        L("구청은 주차선이 있는 곳이라 강제 견인도 안 된다는 입장.",
          [P("car", JT, s0=1.15, s1=1.3, fx=0.4)], None, em=["강제 견인"]),
        L("그런데 11월 1일 새벽, CCTV에 한 남성이 나타남.",
          [P("cctv", JT, s0=1.0, s1=1.15)], None, say="그런데 십일월 일일 새벽, 씨씨티비에 한 남성이 나타남.", em=["CCTV"],
          fx=[("hit_trailer_epic", "나타남", 0.45)]),
        L("차 문을 열고 건드리면 소송한다는 쪽지를 붙이고 사진까지 찍음.",
          [P("note", JT, s0=1.2, s1=1.4, fx=0.5, fy=0.45, punch=True)], None, em=["쪽지를"], em_color="yellow",
          pop=("소송^^", R, "소송한다는")),
        L("그리고 10분쯤 뒤 택시를 몰고 사라졌다고 함.",
          [P("cctv", JT, s0=1.2, s1=1.35, fx=0.6)], None, say="그리고 십분쯤 뒤 택시를 몰고 사라졌다고 함.", em=["택시를 몰고"]),
        L("가스가 안 들어와 기름 말통을 직접 나르는 중이라고.",
          [B("g02", "Two plastic fuel jerry cans on the floor of a small Korean shop next to a portable heater, cold winter light, no people")],
          None, em=["기름 말통"]),
        L("제보자는 업무방해로 고소하고 손해배상도 청구할 예정.",
          [B("g03", "A legal complaint document and a pen on a desk with a winter coat draped on a chair, blurred text, no people")],
          None, em=["업무방해"], fx=[("correct_ding", "고소하고", 0.4)],
          info={"kind": "quotes", "at": "제보자는", "title": "형법 314조 업무방해", "items": [
              {"text": "위력으로 업무 방해", "at": "업무방해로"}, {"text": "5년 이하 징역, 1500만원 이하 벌금", "at": "청구할"}]}),
        L("님들이면 이 차 어떻게 함?", [P("car", JT, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "함")]),
    ]
    go(S, lines, "가스 공사 자리에", "보름째 안 빼는 차", "도시가스 공사 자리 알박기, 쪽지엔 '소송^^'",
       "#가스 공사장 알박기", "보배드림 베스트 1044892 (2026-11-03, 추천 69, 댓글 18, JTBC 사건반장 화면 캡처) https://www.bobaedream.co.kr/view?code=best&No=1044892",
       [("세 들어 영업하던 건물 매입, 도시가스 안 들어와 올 1월 공사 신청, 지난달 공사 시작, 가스관 연결만 남음", "JTBC 사건반장 화면(원글 첨부)"),
        ("보름 전부터 배관 자리에 차 한 대", "JTBC 화면"),
        ("차주 '다른 지역에 있어서 빼줄 수 없다', '절대 내 번호 알려주지 말아라, 임의로 견인하지도 말아라'", "JTBC 화면"),
        ("구청 '주차선 있는 곳이라 강제 견인 불가'", "JTBC 화면"),
        ("11/1 새벽 남성이 차 문 열고 '차 건드리지 마세요 민형사 소송해요~^^ 차량안에 귀중품 있음' 쪽지, 사진 찍고 10분쯤 뒤 택시 몰고 사라짐", "JTBC 화면(대사 = 쪽지 문구)"),
        ("제보자 업무방해 혐의 고소, 손해배상 청구 예정, 기름 말통 직접 나름", "JTBC 화면"),
        ("형법 314조 1항: 위력으로 업무 방해 시 5년 이하 징역 또는 1천500만원 이하 벌금", "casenote 형법 314조")],
       "도시가스 공사 자리에 차 한 대가 보름째 서 있고, 차주는 연락처도 알려 주지 말라고 했습니다.\n새벽엔 한 남성이 '건드리면 소송' 쪽지를 붙이고 사라졌습니다.\n님들이면 이 차 어떻게 하나요?\n\n#알박기 #주차빌런 #업무방해 #보배드림 #란빵",
       "님들이면 이 차 어떻게 함?",
       COMMON, "JTBC 사건반장 화면 중 진행자, 패널 얼굴 컷은 안 씀. CCTV 인물(원본 블러)과 번호판 자리는 한 번 더 모자이크. 지역명 안 씀.",
       [P("night", JT, s0=1.0, s1=1.05)])


# ───────────────────────── 7. 자전거 차로 변경 ─────────────────────────
def EP_bikelane():
    S = "bikelane"
    vclip(S, "v1", "1044723_m0.mp4", 0.8, 7, cx=0.5, cy=0.5, zoom=1.35)
    lines = [
        L("여보, 그냥 넘어가.",
          [V("v1", ss=5, s0=1.1, s1=1.2)], None, dialogue=True, speaker=3, emotion="normal"),
        L("편도 3차로, 2차로를 달리던 블박차.",
          [V("v1", s0=1.0, s1=1.08)], None, say="편도 삼차로, 이차로를 달리던 블박차.", em=["2차로"]),
        L("3차로에 있던 자전거가 갑자기 2차로로 들어옴.",
          [V("v1", ss=2, s0=1.05, s1=1.2, punch=True)], None, say="삼차로에 있던 자전거가 갑자기 이차로로 들어옴.", em=["갑자기"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "들어옴", 0.4)]),
        L("들어오자마자 속도까지 줄여서 브레이크를 밟았지만 쿵.",
          [V("v1", ss=3.5, s0=1.1, s1=1.3)], None, em=["속도까지 줄여서"], shake="쿵", fx=[("hit_trailer_epic", "쿵", 0.45)]),
        L("자전거 운전자는 안 다쳤지만 범퍼는 수리가 필요함.",
          [B("b01", "Close-up of a car's front bumper with a fresh scratch and a small dent, autumn leaves on the road, daylight, no people, no license plate")],
          None, em=["범퍼는"]),
        L("도로교통법상 자전거도 차라서, 뒤차를 방해하는 진로 변경은 금지.",
          [B("b02", "A cyclist seen from behind riding on a Korean multi-lane city road lined with autumn trees, cars far ahead, daylight, no faces")],
          None, em=["자전거도 차"],
          info={"kind": "quotes", "at": "도로교통법상", "title": "도로교통법 19조 3항", "items": [
              {"text": "진로 변경하려는 쪽에서 오는 차", "at": "뒤차를"}, {"text": "통행 방해 우려 땐 변경 금지", "at": "금지"}]}),
        L("그래도 댓글 1위는 싸우면 차가 진다는 반응.",
          [V("v1", ss=4, s0=1.0, s1=1.1)], None, say="그래도 댓글 일위는 싸우면 차가 진다는 반응.", em=["차가 진다"]),
        L("손보협회 기준으로는 기본 5대5로 보인다는 분석도.",
          [V("v1", ss=2.5, s0=1.2, s1=1.35, fx=0.55)], None, say="손보협회 기준으로는 기본 오대오로 보인다는 분석도.", em=["5대5"], em_color="yellow",
          pop=("5:5?", Y, "5대5로")),
        L("넘어오는 게 잘 보이는데 대비를 안 했다는 지적도 나옴.",
          [V("v1", ss=1.5, s0=1.0, s1=1.1)], None, em=["대비를 안 했다"]),
        L("글쓴이는 결국 와이프 말대로 잊기로 함.",
          [B("b03", "A family car interior seen from the back seat, a child's seat and a stuffed toy, blurred autumn street outside, no faces")],
          None, em=["잊기로"], fx=[("drum_rimshot", "잊기로", 0.4)]),
        L("님들은 이거 수리비 청구함?", [V("v1", ss=3, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "청구함")]),
    ]
    go(S, lines, "2차로 달리는데", "자전거가 갑자기 쑥", "3차로 자전거가 2차로로 들어오며 충돌",
       "#자전거가 갑자기 쑥", "보배드림 베스트 1044723 (2026-11-02, 추천 35, 댓글 16) https://www.bobaedream.co.kr/view?code=best&No=1044723",
       [("편도 3차선 중 2차선 주행, 자전거가 3차선에서 2차선으로 진로 변경, 변경 후 급감속, 브레이크 잡았지만 충돌", "원글 본문, 영상"),
        ("자전거 운전자 다친 곳 없다, 범퍼 손상 수리 필요, 와이프는 그냥 넘어가라", "원글 본문(대사 근거)"),
        ("도로교통법 19조 3항: 진로 변경 방향으로 오는 다른 차의 정상 통행에 장애 우려 시 진로 변경 금지, 자전거는 도로교통법상 차", "casenote 도로교통법 19조"),
        ("댓글 '누가 봐도 자전거 잘못이지만 싸우면 차가 짐'(14), '손보협 과실비율 기본 5:5 정도'(1), '넘어오는 게 너무 잘 보이는데 대비를 전혀 안 하신 듯'(1)", "원글 댓글"),
        ("글쓴이 '와이프 말대로 잊어야겠네요'", "글쓴이 댓글")],
       "2차로를 달리는데 3차로 자전거가 갑자기 들어와 속도까지 줄였고, 결국 부딪혔습니다.\n댓글은 싸우면 차가 진다는 반응이 1위였습니다.\n님들은 이런 경우 수리비 청구하나요?\n\n#자전거사고 #블랙박스 #과실비율 #보배드림 #란빵",
       "님들은 이거 수리비 청구함?",
       COMMON, "자전거 운전자는 뒷모습만, 얼굴 안 보임. 번호판 판독 불가. 지역명 안 씀.",
       [V("v1", ss=4, s0=1.0, s1=1.05)])


# ───────────────────────── 8. 르노 필랑트 누아르 ─────────────────────────
def EP_filnoir():
    S = "filnoir"
    cap(S, "front", "fil_d.jpg", nofaces=True, cx=0.4, cy=0.6)
    cap(S, "side", "fil_b.jpg", nofaces=True, cx=0.55, cy=0.5)
    cap(S, "wheel", "fil_d.jpg", box=(3600, 3000, 6800, 5600), nofaces=True)
    cap(S, "grille", "fil_d.jpg", box=(3300, 2300, 6600, 4300), nofaces=True)
    cap(S, "wide", "fil_a.jpg", fit=True, nofaces=True)
    lines = [
        L("와, 휠까지 올블랙이네?",
          [P("wheel", RN, s0=1.0, s1=1.12), P("front", RN, at="올블랙이네", s0=1.0, s1=1.1)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("르노코리아가 필랑트 누아르 에디션을 1000대만 내놓음.",
          [P("wide", RN, s0=1.0, s1=1.08), P("front", RN, at="1000대만", s0=1.1, s1=1.25, punch=True)], None,
          say="르노코리아가 필랑트 누아르 에디션을 천대만 내놓음.", em=["1000대만"], em_color="yellow",
          pop=("1000대 한정", Y, "1000대만"), fx=[("drop_futuristic", "1000대만", 0.5)]),
        L("누아르는 프랑스어로 검은색, 차 안팎을 블랙으로 맞춤.",
          [P("side", RN, s0=1.0, s1=1.1)], None, em=["검은색"]),
        L("20인치 올블랙 휠에 루프와 테일게이트까지 블랙.",
          [P("wheel", RN, s0=1.1, s1=1.3), P("side", RN, at="루프와", s0=1.2, s1=1.35, fy=0.4)], None, say="이십인치 올블랙 휠에 루프와 테일게이트까지 블랙.", em=["20인치"]),
        L("실내는 블랙 스웨이드 천장에 나파 인조가죽 시트.",
          [B("f01", "Interior of a modern crossover SUV with black suede headliner and black leather seats, dim moody light, no people, no logos, no readable screens")],
          None, em=["스웨이드"]),
        L("보스 사운드, AR 헤드업 디스플레이 등 250만원어치가 기본임.",
          [P("grille", RN, s0=1.0, s1=1.15)], None, say="보스 사운드, 에이알 헤드업 디스플레이 등 이백오십마넌어치가 기본임.", em=["250만원어치"],
          info={"kind": "counter", "at": "250만원어치가", "title": "기본으로 넣은 사양", "items": [{"num": 250, "suffix": "만원어치"}]}),
        L("가격은 세제 혜택 기준 약 5194만원.",
          [P("front", RN, s0=1.15, s1=1.3, fx=0.45)], None, say="가격은 세제 혜택 기준 약 오천백구십사마넌.", em=["5194만원"], em_color="yellow",
          fx=[("drop_futuristic", "5194만원", 0.5)]),
        L("근데 같은 달 필랑트는 세일 페스타로 최대 439만원 혜택.",
          [B("f02", "An empty modern car showroom with a sale banner area blurred, bright lights, polished floor, no cars, no people, no readable text")],
          None, say="근데 같은 달 필랑트는 세일 페스타로 최대 사백삼십구마넌 혜택.", em=["439만원"], em_color="yellow",
          pop=("439만원?!", R, "439만원")),
        L("생산월 할인에 재구매, 로열티 조건까지 다 붙여야 나오는 숫자임.",
          [B("f02", s0=1.2, s1=1.3)], None, em=["다 붙여야"],
          info={"kind": "bars", "at": "생산월", "title": "필랑트 11월 최대 혜택", "items": [
              {"label": "생산월 할인", "num": 250, "suffix": "만원", "at": "생산월"},
              {"label": "조건 다 붙이면", "num": 439, "suffix": "만원", "at": "다", "flash": "숫자임"}]}),
        L("누아르는 11월 5일 출시, 보증은 최대 7년 14만km.",
          [P("side", RN, s0=1.0, s1=1.08)], None, say="누아르는 십일월 오일 출시, 보증은 최대 칠년 십사만 킬로.", em=["7년 14만km"]),
        L("님들은 한정판 블랙이랑 할인받은 필랑트 중 뭐 고름?", [P("wide", RN, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "고름")]),
    ]
    go(S, lines, "1000대만 파는", "올블랙 필랑트 나왔다", "필랑트 누아르 에디션 11월 5일 출시",
       "#필랑트 올블랙 한정판", "르노코리아 11/2 발표 필랑트 누아르 에디션 (더드라이브 1065608682530356, 비즈월드 150628) + 11/3 르노 세일 페스타 (이코노믹리뷰 755848, 데일리카 63048)",
       [("필랑트 누아르 에디션 11/5 출시, 1000대 한정, 최상위 트림 에스프리 알핀 기반", "더드라이브, 비즈월드(일치)"),
        ("누아르 = 프랑스어 검은색, 20인치 올 블랙 휠, 블랙 루프와 테일게이트, 블랙 스웨이드 헤드라이닝, 블랙 나파 인조가죽 시트", "더드라이브, 비즈월드"),
        ("BOSE 10스피커, ANC, AR-HUD 등 약 250만원 상당 기본", "더드라이브, 비즈월드"),
        ("친환경차 세제 혜택 기준 5193만9000원(더드라이브 제목 5194만원), 7년 14만km 보증", "더드라이브, 비즈월드"),
        ("11월 르노 세일 페스타: 필랑트 생산월 최대 250만원 + 선쉐이드 또는 액세서리 + 재구매, 로열티 = 최대 439만원", "이코노믹리뷰, 데일리카"),
        ("'와, 휠까지 올블랙이네?' 는 구경꾼 반응 대사(§4-6 1번), 실존 인물 발언 아님", "대본 구성")],
       "르노코리아가 필랑트 누아르 에디션을 1000대 한정으로 11월 5일 내놓습니다.\n블랙 내외관에 약 250만원어치 사양이 기본이고, 가격은 세제 혜택 기준 약 5194만원입니다.\n님들은 한정판과 할인받은 필랑트 중 뭘 고르나요?\n\n#필랑트 #르노코리아 #신차 #한정판 #란빵",
       "님들은 한정판 블랙이랑 할인받은 필랑트 중 뭐 고름?",
       "자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 자동차 시트커버, 차량용 방향제, 자동차 햇빛가리개",
       "차 화면은 르노코리아 보도사진(기사 '사진=르노코리아')만, AI 는 차 없는 실내와 전시장 배경만.",
       [P("front", RN, s0=1.0, s1=1.05)], typ="란빵 자동차, 신차")


# ───────────────────────── 9. 제네시스 라인 멈춤 ─────────────────────────
def EP_genline():
    S = "genline"
    cap(S, "g90", "gen_a.jpg", nofaces=True, cx=0.5)
    cap(S, "g80", "gen_b.jpg", nofaces=True, cx=0.55)
    GN = "사진: 제네시스"
    YN = "사진: 연합뉴스"
    lines = [
        L("신차 넣으려다 라인이 멈췄다고?",
          [B("n01", "A large car factory final assembly line with conveyor and robotic arms standing still, lights on, no cars on the line, no people, no logos")],
          None, dialogue=True, speaker=3, emotion="toneup"),
        L("현대차 울산공장 제네시스 라인이 이틀째 멈춰 섬.",
          [P("g90", GN, s0=1.0, s1=1.1)], None, em=["이틀째"], em_color="yellow", pop=("라인 정지", R, "이틀째")),
        L("11월 2일 아침, 회사가 G80 하이브리드 시험차를 라인에 넣으려 하자.",
          [P("g80", YN, s0=1.0, s1=1.12)], None, say="십일월 이일 아침, 회사가 지팔십 하이브리드 시험차를 라인에 넣으려 하자.", em=["G80 하이브리드"]),
        L("노조 대의원들이 막아서면서 라인이 멈췄음.",
          [B("n01", s0=1.15, s1=1.3, punch=True)], None, em=["막아서면서"], shake="멈췄음", fx=[("hit_trailer_epic", "멈췄음", 0.45)]),
        L("쟁점은 맨아워, 차 한 대 만드는 데 드는 인력과 작업량임.",
          [B("n02", "Workers' tools and a clipboard with a production schedule on a factory workbench, assembly line blurred in background, no people, no readable text")],
          None, em=["맨아워"],
          info={"kind": "quotes", "at": "쟁점은", "title": "맨아워(MH)", "items": [
              {"text": "차 한 대 만드는 인력", "at": "인력과"}, {"text": "노동 투입량", "at": "작업량임"}]}),
        L("G80 하이브리드와 G90 부분변경 양산을 앞두고 인력 조정이 걸린 것.",
          [P("g90", GN, s0=1.15, s1=1.3, fx=0.6)], None, say="지팔십 하이브리드와 지구십 부분변경 양산을 앞두고 인력 조정이 걸린 것.", em=["인력 조정"]),
        L("회사는 의장부 약 800명에게 무노동 무임금을 공지함.",
          [B("n03", "A factory notice board with a printed announcement sheet pinned on it, blurred text, empty factory corridor, no people")],
          None, say="회사는 의장부 약 팔백명에게 무노동 무임금을 공지함.", em=["무노동 무임금"], em_color="yellow",
          info={"kind": "counter", "at": "의장부", "title": "무노동 무임금 공지", "items": [{"num": 800, "suffix": "명"}]}),
        L("인력 재배치 문제로 라인이 멈추는 건 차원이 다른 문제입니다.",
          [B("n02", s0=1.2, s1=1.3)], None, dialogue=True, speaker=2, emotion="normal"),
        L("현대차 월 판매는 13개월째 작년보다 줄었고, 10월 내수는 기아에 밀림.",
          [P("g80", YN, s0=1.15, s1=1.3, fx=0.6)], None, say="현대차 월 판매는 십삼개월째 작년보다 줄었고, 시월 내수는 기아에 밀림.", em=["13개월째"],
          info={"kind": "bars", "at": "10월", "title": "10월 내수 판매", "items": [
              {"label": "기아", "num": 51007, "suffix": "대", "at": "10월"},
              {"label": "현대차", "num": 49042, "suffix": "대", "at": "기아에", "flash": "밀림"}]}),
        L("신차 효과가 급한데 라인부터 멈춘 셈.",
          [B("n01", s0=1.0, s1=1.1)], None, em=["라인부터"]),
        L("님들은 이 싸움 누가 맞다고 봄?", [P("g90", GN, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "신차 넣으려다", "제네시스 라인 멈췄다", "G80 하이브리드 시험차 투입에 라인 이틀째 정지",
       "#제네시스 라인 멈춤", "현대차 울산 5공장 제네시스 라인 정지 (데일리안 1710109, 메트로 20261103500264, 법률방송 61319, 연합뉴스 AKR20261102135300003) + 보배드림 베스트 1044765",
       [("울산 5공장 1라인 제네시스 의장부 11/2 오전 9시 G80 하이브리드 시험차 투입, 노조 대의원 저지로 라인 중단, 11/3 이틀째", "데일리안, 메트로, 법률방송(일치)"),
        ("오전 10시 5분 의장부 약 800명 무노동 무임금 공지", "데일리안, 법률방송"),
        ("쟁점 맨아워(차 한 대 생산 인력, 노동 투입량), G80 하이브리드, G90 부분변경 양산 앞둔 협의", "데일리안, 메트로"),
        ("김필수 대림대 교수 '인력 재배치 문제로 생산라인 자체가 멈춰 서는 것은 차원이 다른 문제'", "메트로(대사 = 발언 요약)"),
        ("현대차 월 판매 13개월 연속 전년 대비 감소, 10월 내수 4만9042대 vs 기아 5만1007대", "연합뉴스, 법률방송, 신아일보"),
        ("'신차 넣으려다 라인이 멈췄다고?' 는 구경꾼 반응 대사", "대본 구성")],
       "현대차 울산공장 제네시스 라인이 G80 하이브리드 시험차 투입을 놓고 이틀째 멈췄습니다.\n쟁점은 신차 양산에 필요한 인력과 작업량(맨아워)입니다.\n님들은 누구 말이 맞다고 보나요?\n\n#제네시스 #현대차 #G80 #신차 #란빵",
       "님들은 이 싸움 누가 맞다고 봄?",
       "자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 자동차 시트커버, 차량용 방향제, 자동차 햇빛가리개",
       "차 화면은 제네시스 공식 사진(데일리안 게재)과 연합뉴스 사진만, 공장 배경은 AI(로고, 차종 없음). 노조, 회사 인물 실명 안 씀.",
       [P("g80", YN, s0=1.0, s1=1.05)], typ="란빵 자동차, 신차")


# ───────────────────────── 10. 겨울 방전 점프스타터 ─────────────────────────
def EP_jumpcold():
    S = "jumpcold"
    cap(S, "prod", "js_a.jpg", box=(40, 100, 420, 410), fit=True, nofaces=True)
    lines = [
        L("아 출근해야 되는데 시동이 왜 안 걸려?",
          [B("j01", "View from the driver's seat of a car on a frosty winter morning, frost on the windshield, dashboard warning lights glowing, hands on the steering wheel, no faces")],
          None, dialogue=True, speaker=2, emotion="toneup"),
        L("겨울 긴급출동 원인 1위는 배터리 방전.",
          [B("j02", "A car parked in an outdoor Korean apartment parking lot covered in frost at dawn, breath-like mist, cold blue light, no people, no license plate visible")],
          None, say="겨울 긴급출동 원인 일위는 배터리 방전.", em=["배터리 방전"], em_color="yellow", pop=("1위", Y, "1위는"),
          fx=[("drop_futuristic", "1위는", 0.5)]),
        L("보험 통계로 겨울 긴급출동의 60%가 배터리 충전이었음.",
          [B("j03", "A roadside assistance service truck with flashing amber lights parked next to a car with its hood open on a cold morning, no people visible, no logos")],
          None, say="보험 통계로 겨울 긴급출동의 육십퍼센트가 배터리 충전이었음.", em=["60%"],
          info={"kind": "counter", "at": "보험", "title": "겨울 긴급출동 중 배터리 충전", "items": [{"num": 60, "suffix": "%"}]}),
        L("영하 10도면 배터리 용량이 최대 절반까지 줄어든다고 함.",
          [B("j04", "Close-up of a car battery under an open hood covered with light frost, cold morning light, no people, no readable labels")],
          None, say="영하 십도면 배터리 용량이 최대 절반까지 줄어든다고 함.", em=["절반까지"], em_color="yellow"),
        L("밤새 켜 둔 블박 주차 녹화도 배터리를 갉아먹음.",
          [B("j05", "A dashcam glowing with a small recording light behind a frosty windshield at night in a parking lot, no people")],
          None, em=["주차 녹화"]),
        L("그래서 겨울엔 블박 저전압 차단값을 12.3V 정도로 올리라는 권장.",
          [B("j05", s0=1.2, s1=1.35)], None, say="그래서 겨울엔 블박 저전압 차단값을 십이쩜삼볼트 정도로 올리라는 권장.", em=["12.3V"],
          info={"kind": "compare", "at": "그래서", "title": "블박 저전압 차단값", "items": [
              {"label": "공장 출고값", "color": W, "at": "그래서", "rows": [["보통", "11.6~12.0V", W]]},
              {"label": "겨울 권장", "color": Y, "at": "12.3V", "rows": [["공단", "12.2~12.3V", Y]]}]}),
        L("방전되면 출동 기다리는 동안 출근은 이미 늦음.",
          [B("j01", s0=1.2, s1=1.3)], None, em=["이미 늦음"], fx=[("drum_rimshot", "늦음", 0.4)]),
        L("그래서 트렁크에 하나씩 넣어 두는 게 휴대용 점프스타터.",
          [P("prod", "사진: 포유디지탈", s0=1.0, s1=1.12)], None, em=["점프스타터"], em_color="yellow",
          fx=[("correct_ding", "점프스타터", 0.45)]),
        L("빨간 집게는 플러스, 검은 집게는 마이너스에 물리고 시동.",
          [B("j06", "Close-up of hands in winter gloves attaching a red jumper clamp to a car battery positive terminal and a black clamp nearby, open hood, no faces")],
          None, em=["빨간 집게는 플러스"]),
        L("시동이 걸려도 정비소에서 배터리 상태는 꼭 확인하라는 조언.",
          [B("j04", s0=1.2, s1=1.35)], None, em=["배터리 상태"]),
        L("님들은 겨울에 방전돼 본 적 있음?", [B("j02", s0=1.1, s1=1.2)], None, fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "겨울 아침 시동 안 걸리면", "이거 하나면 됨", "겨울 긴급출동 1위는 배터리 방전",
       "#겨울 방전엔 이거", "네이버 데이터랩 쇼핑인사이트 자동차용품(cid 50000055) 2026-10-27~11-02 인기검색어 18위 점프스타터 + 매일신문 2026101310083126275, 컨슈머타임스 685743",
       [("데이터랩 자동차용품 10/27~11/2 인기검색어 18위 점프스타터(1위 요소수, 5위 와이퍼)", "네이버 데이터랩 API 조회"),
        ("겨울 긴급출동 원인 1위 배터리 방전(현대해상 교통기후환경연구소)", "컨슈머타임스, 매일신문(일치)"),
        ("보험개발원, 손보협회 겨울(12~2월) 배터리 충전 출동 월평균 106만건, 겨울 긴급출동의 60.4%", "매일신문"),
        ("영하 10도면 배터리 용량 최대 절반(교통안전공단 가이드), 영하 10도 이하 성능 저하", "매일신문, 컨슈머타임스"),
        ("상시녹화 블박이 방전 원인, 공장 출고 차단값 11.6~12.0V, 겨울 권장 12.2~12.3V(공단)", "매일신문"),
        ("시동 걸린 뒤 단순 방전인지 발전기 이상인지 정비 점검", "컨슈머타임스"),
        ("점프스타터 연결: 빨간 집게 +, 검은 집게 -", "일반 사용 안내(제품마다 설명서 확인)")],
       "겨울 긴급출동 원인 1위는 배터리 방전입니다.\n영하 10도면 배터리 용량이 최대 절반까지 줄고, 밤새 켜 둔 블박도 배터리를 씁니다.\n님들은 겨울에 방전돼 본 적 있나요?\n\n#배터리방전 #점프스타터 #겨울철차관리 #블랙박스 #란빵",
       "님들은 겨울에 방전돼 본 적 있음?",
       "자동차 점프스타터, 점프스타터 공기압주입기, 자동차 배터리 충전기, 블랙박스 보조배터리, 자동차 블랙박스 2채널",
       "제품 사진은 보도자료 사진 1장(브랜드명 대본에 안 씀). 가격, 출력 수치는 안 씀. 긴급출동 특약 횟수는 보험사마다 달라 안 씀.",
       [P("prod", "사진: 포유디지탈", s0=1.0, s1=1.05)], typ="란빵 자동차, 용품")


EPS = [EP_kgm1600, EP_benzew337, EP_deerslip, EP_stealthrain, EP_truckback, EP_gasblock, EP_bikelane, EP_filnoir, EP_genline, EP_jumpcold]

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in EPS:
        if not want or f.__name__[3:] in want:
            f()
