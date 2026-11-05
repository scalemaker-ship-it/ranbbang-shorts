#!/usr/bin/env python3
"""란빵 2026-11-04n 10편 (2026-11-03 22:45 사용자 수동 지시 "영상 10개 만들어서 10분간격으로 지금부터 업로드").
- 보배드림 베스트 6편(타이어 휠, 수출 매입, 카센터 도색 20만원, 주차 침 테러, 출고 5일 새 차, 신형 아반떼 페달)
  + 뉴스 1편(청년 차보험 경력 인정) + 신차 2편(사이버캡 국내 전시, 수소 카니발) + 용품 1편(차량용 방향제).
- 근거 = work/research_1103n.md, 원본 = work/_photos/b1103n/ (map.txt).
- 실명, 상호, 지점, 지역, 번호판 없음. 캐릭터 없음(NO_CHAR). 차종이 특정되는 줄엔 AI 차 그림을 쓰지 않는다.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1024 import B, C, L, build, IR, Y, W, R, P   # noqa: E402,F401
from _batch_1027 import cap as _cap   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos", "b1103n")
BB = "사진: 보배드림"
COMMON = "자동차 블랙박스 2채널, 블랙박스 메모리카드, 비상삼각대, 차량용 핸드폰 거치대, 차량용 방향제"
MAXC = 360


def cap(*a, **k):
    k.setdefault("ph", PH)
    return _cap(*a, **k)


def go(S, lines, *rest, **kw):
    n = sum(len(l["text"]) for l in lines)
    assert 10 <= len(lines) <= 12, (S, len(lines))
    assert n <= MAXC, (S, "글자", n)
    for l in lines:
        assert "—" not in l["text"] and "·" not in l["text"], l["text"]
    build(S, lines, *rest, **kw)
    print(f"  chars {S} = {n} ({len(lines)}줄)")


# ───────────────────────── 1. 타이어 갈고 휠 기스 ─────────────────────────
def EP_tirewheel():
    S = "tirewheel"
    cap(S, "wheel", "1044964_00.jpg", cy=0.5)
    lines = [
        L("저희는 절대 그렇게 작업할 리가 없어요.",
          [B("t01", "Inside a small Korean tire repair shop, a tire changing machine and a wheel balancer, stacked tires along the wall, fluorescent light, no people, no readable signs")],
          None, dialogue=True, speaker=3, emotion="toneup"),
        L("공업사에서 공임비만 내고 타이어를 갈았음.",
          [B("t02", "Close-up of a car tire being mounted on a silver alloy wheel on a tire changer machine in a garage, hands in work gloves only, no faces")],
          None, em=["공임비만"]),
        L("그런데 집에 와 보니 휠이 다 긁혀 있었다는 것.",
          [P("wheel", BB, s0=1.0, s1=1.12), P("wheel", BB, at="긁혀", s0=1.5, s1=1.7, fx=0.5, fy=0.55, punch=True)],
          None, em=["휠이 다 긁혀"], em_color="yellow", shake="긁혀", fx=[("hit_trailer_epic", "긁혀", 0.45)]),
        L("다시 찾아가 따지자 전에 찍은 사진이라도 대라는 답.",
          [B("t03", "A tire shop reception counter with a payment terminal and invoices, blurred tires in background, no people, no readable text")],
          None, em=["사진이라도 대라"]),
        L("공업사엔 CCTV도 없다고 함.",
          [B("t04", "A bare ceiling corner of an old car repair garage with exposed wiring and no security camera, dim light, no people")],
          None, say="공업사엔 씨씨티비도 없다고 함.", em=["CCTV도 없다"], fx=[("wrong_gameshow_buzz", "없다고", 0.4)]),
        L("차가 오래돼서 어디서 긁혔는지 모르는 거 아니냐는 말까지.",
          [B("t01", s0=1.2, s1=1.35)], None, em=["차가 오래돼서"]),
        L("글쓴이는 휠 4개가 다 똑같이 긁혔다며 억울해함.",
          [P("wheel", BB, s0=1.2, s1=1.35, fx=0.45, fy=0.5)], None, say="글쓴이는 휠 네 개가 다 똑같이 긁혔다며 억울해함.",
          em=["4개가 다 똑같이"], pop=("4개 다?!", Y, "똑같이")),
        L("그런데 댓글 반응은 정반대였음.",
          [B("t05", "Close-up of hands holding a smartphone showing an online community comment section, text blurred, dim room, no faces")],
          None, em=["정반대"], fx=[("scratch_vinyl", "정반대였음", 0.45)]),
        L("이미 많이 긁혀 있구만, 공짜로 새 휠 바꾸려는 거냐는 댓글이 추천 82.",
          [P("wheel", BB, at="이미", s0=1.6, s1=1.8, fx=0.3, fy=0.7, punch=True)], None,
          say="이미 많이 긁혀 있구만, 공짜로 새 휠 바꾸려는 거냐는 댓글이 추천 팔십이.", em=["이미 많이 긁혀"], em_color="yellow",
          info={"kind": "bars", "at": "이미", "title": "댓글 추천", "items": [
              {"label": "원래 긁혀 있었다", "num": 82, "suffix": "", "at": "이미", "flash": "공짜로"},
              {"label": "새 상처 구분 안 됨", "num": 51, "suffix": "", "at": "댓글이"}]}),
        L("보통은 작업 전에 사진부터 찍는데, 지금은 구분이 안 된다는 의견도.",
          [B("t02", s0=1.2, s1=1.35)], None, em=["작업 전에 사진"]),
        L("님들이 보기엔 이거 공업사 탓임?", [P("wheel", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "탓임")]),
    ]
    go(S, lines, "타이어 갈았더니", "휠 4개가 다 긁힘", "공업사는 절대 아니라는데",
       "#타이어 갈고 휠 기스", "보배드림 베스트 1044964 (2026-11-03, 추천 296, 댓글 34) https://www.bobaedream.co.kr/view?code=best&No=1044964",
       [("공업사에서 공임비만 받고 타이어 교체, 집에 와 보니 휠이 다 긁힘", "원글 본문"),
        ("'절대 그렇게 작업할 리가 없다', '전에 사진이라도 대라', 공업사 CCTV 없음, '차가 오래돼서 어디서 긁혔는지 모르는 것 아니냐'", "원글 본문(대사 근거)"),
        ("'휠 4개가 다 똑같이 긁혔어요'", "원글 본문"),
        ("'어디가 긁힌 건데요 이미 많이 긁혀 있구만, 이참에 공짜로 새 휠'(82)", "원글 댓글"),
        ("'기존 상처와 새로 생긴 상처가 구분이 안 됨, 타이어 교체하는 곳은 미리 사진 찍어 놓고 진행'(51)", "원글 댓글")],
       "공업사에서 타이어를 갈고 왔더니 휠 4개가 다 긁혀 있었다는 글입니다.\n공업사는 절대 아니라고 했고, 댓글은 원래 긁혀 있던 것 아니냐는 반응이 더 많았습니다.\n님들은 누구 말이 맞다고 보나요?\n\n#타이어교체 #휠기스 #공업사 #보배드림 #란빵",
       "님들이 보기엔 이거 공업사 탓임?",
       "휠 기스 복원제, 휠 클리너, 타이어 광택제, 자동차 블랙박스 2채널, 차량용 방향제",
       "공업사 상호, 지역은 안 씀. 첨부 사진 1장(휠)만 실사, 나머지는 AI 배경(차종 특정 안 함).",
       [P("wheel", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 2. 중고차 수출 매입 ─────────────────────────
def EP_exportscam():
    S = "exportscam"
    lines = [
        L("사장님 차가 엉망이라 수출이 안 된대요.",
          [B("x01", "A used sedan loaded on a car transport trailer at night on a highway rest area, shot from behind, no license plate visible, no people, no logos")],
          None, dialogue=True, speaker=2, emotion="toneup"),
        L("유튜브에 중고차보다 더 쳐준다는 수출 매입 광고가 계속 뜸.",
          [B("x02", "Close-up of hands holding a smartphone playing a blurred video advertisement with a car image, sitting on a sofa at night, no faces, no readable text")],
          None, em=["수출 매입"]),
        L("연락처를 남기자 여기저기서 전화가 쏟아짐.",
          [B("x03", "A smartphone on a wooden table with its screen showing many incoming call notifications, blurred text, vibrating, no people")],
          None, em=["전화가 쏟아짐"]),
        L("시세보다 높게 부르길래 계약금만 받고 탁송으로 차를 보냄.",
          [B("x01", s0=1.2, s1=1.35), B("x04", "A car key fob and a small envelope of cash on a car hood in an apartment parking lot, daytime, no people", at="계약금만")],
          None, em=["계약금만 받고"], em_color="yellow"),
        L("차가 떠나자 딜러 연락, 해외 바이어가 검사했는데 엉망이라는 것.",
          [B("x05", "A used car parked inside a large export yard warehouse with many cars lined up, harsh light, no people, no license plates visible")],
          None, em=["엉망"], fx=[("wrong_gameshow_buzz", "엉망이라는", 0.45)]),
        L("얼마 전 정비를 다 하고 기록까지 넘긴 차였음.",
          [B("x06", "A folder of car maintenance receipts and service records on a desk with a car key, blurred text, warm light, no people")],
          None, em=["기록까지"]),
        L("차 가지러 가겠다니 탁송비, 보관비, 검사비 얘기가 나옴.",
          [B("x05", s0=1.2, s1=1.35, punch=True)], None, em=["탁송비, 보관비, 검사비"], em_color="yellow",
          pop=("비용 청구?!", R, "검사비"), fx=[("hit_trailer_epic", "검사비", 0.45)]),
        L("결국 글쓴이는 싸우기 싫어 그냥 가지라고 함.",
          [B("x03", s0=1.2, s1=1.3)], None, em=["그냥 가지라고"]),
        L("댓글은 전형적인 수출 매입 사기, 계약금 먼저 오가면 끝이라는 반응.",
          [B("x02", s0=1.2, s1=1.35)], None, em=["계약금 먼저"],
          info={"kind": "bars", "at": "전형적인", "title": "댓글 추천", "items": [
              {"label": "전형적인 매입 사기", "num": 75, "suffix": "", "at": "전형적인", "flash": "사기,"},
              {"label": "계약금 얘기 나오면 손절", "num": 52, "suffix": "", "at": "계약금"}]}),
        L("현장에서 차 보고 돈 다 받은 뒤 키를 넘기라는 조언이 많았음.",
          [B("x04", s0=1.2, s1=1.35)], None, em=["돈 다 받은 뒤"], fx=[("correct_ding", "키를", 0.45)]),
        L("님들은 이런 광고 보고 차 팔아 본 적 있음?", [B("x01", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "중고차 더 쳐준다더니", "차 가져가고 딴소리", "수출 매입 광고의 함정",
       "#중고차 수출 매입 사기", "보배드림 베스트 1044950 (2026-11-03, 추천 523, 댓글 43) https://www.bobaedream.co.kr/view?code=best&No=1044950",
       [("유튜브 광고 '요즘 중고차보다 더 높은 가격', 연락처 남기니 연락 쇄도, 시세보다 높게 불러 거래", "원글 본문"),
        ("계약금 걸고 로드 탁송, 차가 떠나자 딜러 '차가 엉망이라 수출이 안 된다, 해외 바이어가 직접 검사'", "원글 본문(대사 근거)"),
        ("얼마 전 1급 정비사에게 교환 수리, 정비 기록도 다 줌", "원글 본문"),
        ("가지러 가겠다, 계약금 돌려주겠다 하니 탁송비, 보관비, 검사비 언급, 결국 '그냥 가지라' 함, 말소증은 받음", "원글 본문"),
        ("'전형적인 수출판매 매입 사기, 계약금 먼저 쏘는 순간'(75), '계약금 얘기 나오면 무조건 손절'(52), '현장에서 보고 돈 받고 차키'(51)", "원글 댓글")],
       "유튜브 광고를 보고 중고차를 수출 매입 업체에 넘겼다가 차가 떠난 뒤 딴소리를 들었다는 글입니다.\n댓글은 계약금 먼저, 탁송 먼저면 전형적인 수법이라고 입을 모았습니다.\n님들은 중고차 어디에 팔아 봤나요?\n\n#중고차 #중고차매입 #수출 #보배드림 #란빵",
       "님들은 이런 광고 보고 차 팔아 본 적 있음?",
       COMMON, "업체명, 지역, 금액은 원글에 없어 안 씀. 첨부 없음, 화면 전부 AI 배경(차종 특정 안 함, 번호판 안 보이게).",
       [B("x04", s0=1.0, s1=1.08)])


# ───────────────────────── 3. 카센터 사장 도색 20만원 ─────────────────────────
def EP_sidescrape():
    S = "sidescrape"
    cap(S, "s1", "1044971_00.jpg", cy=0.6)
    cap(S, "s2", "1044971_01.jpg", cx=0.45)
    lines = [
        L("도색 다 해드리고 20만원 드릴게요.",
          [B("c01", "A small Korean car repair shop interior with a car on a lift, tools on the wall, fluorescent light, no people, no readable signs")],
          None, dialogue=True, speaker=3, emotion="normal", say="도색 다 해드리고 이십마넌 드릴게요."),
        L("신호 대기 중이던 흰 차를 우회전하던 차가 쭉 긁고 감.",
          [P("s1", BB, s0=1.0, s1=1.12)], None, em=["쭉 긁고"], shake="긁고", fx=[("glass_smash", "긁고", 0.35)]),
        L("다친 데는 없고 뒤범퍼 옆이 쓸렸음.",
          [P("s2", BB, s0=1.0, s1=1.1), P("s2", BB, at="쓸렸음", s0=1.5, s1=1.7, fx=0.4, fy=0.55, punch=True)], None, em=["뒤범퍼"]),
        L("그런데 알고 보니 상대가 카센터 사장이었음.",
          [B("c01", s0=1.2, s1=1.35, punch=True)], None, em=["카센터 사장"], em_color="yellow",
          pop=("카센터 사장?!", Y, "사장이었음"), fx=[("drum_rimshot", "사장이었음", 0.45)]),
        L("보험 말고 자기가 도색해 주고 20만원을 얹어 준다는 제안.",
          [B("c02", "Hands in work gloves holding a paint spray gun next to a white car bumper in a paint booth, no faces")],
          None, say="보험 말고 자기가 도색해 주고 이십마넌을 얹어 준다는 제안.", em=["20만원"],
          info={"kind": "counter", "at": "20만원을", "title": "도색 + 현금", "items": [{"num": 20, "suffix": "만원"}]},
          fx=[("drop_futuristic", "20만원을", 0.45)]),
        L("첫 사고라 뭐가 나은지 몰라 글쓴이가 물어봄.",
          [B("c03", "View from the driver seat of a white car stopped at a red light at a city intersection, dashboard and steering wheel visible, no people visible, no readable signs")],
          None, em=["첫 사고"]),
        L("댓글은 무과실인데 고민할 이유가 없다, 보험 접수하라는 쪽.",
          [P("s1", BB, s0=1.2, s1=1.35)], None, em=["보험 접수"], fx=[("correct_ding", "접수하라는", 0.45)]),
        L("카센터는 도색을 못 해서 아는 데 맡기는 거라는 말도.",
          [B("c02", s0=1.2, s1=1.35)], None, em=["아는 데 맡기는"]),
        L("20만원은 나중에 색 이상하다는 말 말라는 뜻이라는 해석까지.",
          [P("s2", BB, s0=1.2, s1=1.3)], None, say="이십마넌은 나중에 색 이상하다는 말 말라는 뜻이라는 해석까지.",
          em=["색 이상하다는"], em_color="yellow"),
        L("도색 잘못하면 스트레스 오래 간다는 댓글도 있었음.",
          [B("c04", "Close-up of a white car bumper with slightly mismatched paint color patch under garage light, no people")],
          None, em=["스트레스"]),
        L("님들이면 20만 받고 맡김, 보험 부름?", [P("s1", BB, s0=1.0, s1=1.1)], None,
          say="님들이면 이십만 받고 맡김, 보험 부름?", fx=[("pop_bubble", "부름")]),
    ]
    go(S, lines, "긁고 간 상대가", "카센터 사장이었음", "도색 해주고 20만원 준다는 제안",
       "#도색에 20만원 얹어줌", "보배드림 베스트 1044971 (2026-11-03, 추천 17, 댓글 17) https://www.bobaedream.co.kr/view?code=best&No=1044971",
       [("신호대기 중 상대차가 우회전하다 긁음, 경미해 다치지 않음", "원글 본문"),
        ("상대가 카센터 사장, '도색 다 해주고 20 준다', 대물 맡길지 도색 맡길지 질문, 첫 사고", "원글 본문(대사 근거)"),
        ("'무과실 사고인데 고민할 이유 없음, 보험 접수해서 제대로 수리'(4), '대물 접수번호 받고'(2)", "원글 댓글"),
        ("'카센터는 도색 못 해요, 자기 협력에다 하라는 것'(1), '도색 후 색깔이 이상하다 이야기하지 말라는 얘기'(1), '도색 잘못하면 스트레스 오래 가요'(1)", "원글 댓글")],
       "신호 대기 중 긁고 간 상대가 카센터 사장이었고, 도색을 해 주고 20만원을 더 준다고 했습니다.\n댓글은 무과실이면 보험 접수가 낫다는 쪽이 많았습니다.\n님들이면 어떻게 하나요?\n\n#접촉사고 #도색 #보험처리 #보배드림 #란빵",
       "님들이면 20만 받고 맡김, 보험 부름?",
       "자동차 붓펜, 자동차 컴파운드, 범퍼 가드, 자동차 블랙박스 2채널, 차량용 방향제",
       "첨부 사진 2장(흰 차 뒤범퍼 측면)만 실사, 번호판 안 보임. 카센터 상호, 지역 안 씀.",
       [P("s2", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 4. 청년 차보험 경력 인정 ─────────────────────────
def EP_armyins():
    S = "armyins"
    cap(S, "news", "1044773_00.jpg", box=(0, 100, 800, 1199), fit=True, nofaces=True, boxes=[(25, 330, 80, 80)])
    MT = "사진: 보배드림(매일경제 기사 캡처)"
    lines = [
        L("운전 3년 했는데 왜 초보 보험료예요?",
          [B("y01", "A young driver's hands holding car insurance papers with a calculator inside a small car, steering wheel visible, blurred numbers, no faces")],
          None, dialogue=True, speaker=2, emotion="toneup", say="운전 삼 년 했는데 왜 초보 보험료예요?"),
        L("청년 차보험료 133만원이 71만원으로 내려간 방법이 공개됨.",
          [P("news", MT, s0=1.0, s1=1.1)], None, say="청년 차보험료 백삼십삼마넌이 칠십일마넌으로 내려간 방법이 공개됨.",
          em=["71만원"], em_color="yellow",
          info={"kind": "bars", "at": "청년", "title": "28세 아반떼 보험료", "items": [
              {"label": "경력 인정 전", "num": 133, "suffix": "만원", "at": "청년"},
              {"label": "경력 인정 후", "num": 71, "suffix": "만원", "at": "71만원으로", "flash": "71만원으로"}]},
          fx=[("drop_futuristic", "71만원으로", 0.5)]),
        L("금감원이 청년들이 놓치는 할인 제도를 안내한 것.",
          [B("y02", "A government financial office building exterior in Seoul at dusk, glass facade, no readable signs, no people")], None, em=["놓치는 할인"]),
        L("부모 보험에 자녀를 종피보험자로 올려 두면 경력이 쌓임.",
          [B("y03", "A family car parked in an apartment parking lot with a car key and an insurance card on the dashboard, warm evening light, no people, no license plate")],
          None, em=["종피보험자"], em_color="yellow"),
        L("나중에 첫 가입할 때 최대 3년 운전경력을 인정받음.",
          [B("y01", s0=1.2, s1=1.35)], None, say="나중에 첫 가입할 때 최대 삼 년 운전경력을 인정받음.", em=["최대 3년"]),
        L("등록된 사람이 다 무사고면 무사고 경력까지 인정.",
          [P("news", MT, s0=1.3, s1=1.45, fx=0.5, fy=0.7)], None, em=["무사고 경력까지"], fx=[("correct_ding", "인정", 0.4)]),
        L("군대 운전병, 장기렌터카 기간도 가입경력으로 쳐 줌.",
          [B("y04", "A military style green truck steering wheel and dashboard seen from the driver seat, gloved hands on the wheel, no faces, no insignia")],
          None, em=["군대 운전병"], em_color="yellow"),
        L("운전병 1년 반에 렌터카 1년 반이면 약 38만원 줄어든 사례.",
          [B("y04", s0=1.2, s1=1.35)], None, say="운전병 일 년 반에 렌터카 일 년 반이면 약 삼십팔마넌 줄어든 사례.", em=["38만원"],
          info={"kind": "counter", "at": "운전병", "title": "가입경력 3년 인정", "items": [{"num": 38, "suffix": "만원 할인"}]}),
        L("가입 때 놓쳤어도 나중에 신청하면 환급된다고 함.",
          [B("y05", "Close-up of hands filling out an insurance refund application form with a pen on a desk, blurred text, no faces")],
          None, em=["환급"]),
        L("다만 본인 한정 특약은 남이 몰다 사고 나면 보상이 안 될 수 있음.",
          [B("y03", s0=1.2, s1=1.35)], None, em=["보상이 안 될 수"], fx=[("wrong_gameshow_buzz", "보상이", 0.4)]),
        L("님들은 처음 차보험료 얼마 나왔음?", [B("y01", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "나왔음")]),
    ]
    go(S, lines, "군대에서 운전했으면", "차보험료 확 내려감", "금감원 청년 차보험 할인 안내",
       "#운전병 경력 보험할인", "금감원 2026-11-02 발표 (머니투데이 2026110210330714676, 경향 202611021516001, 연합 AKR20261102075700002) + 보배드림 베스트 1044773",
       [("만 19~34세 청년, 부모 보험에 종피보험자 등록 시 첫 가입 때 최대 3년 운전경력 인정, 전체 피보험자 무사고면 무사고 경력도", "머니투데이, 경향, 연합"),
        ("A씨(28) 아반떼 보험료 133만497원 → 71만6582원", "머니투데이(경향 '130만원대 → 71만원대')"),
        ("군 운전병 1년6개월 + 장기렌터카 1년6개월 = 가입경력 3년, 133만497원 → 94만6300원(28.9%, 약 38만원)", "머니투데이"),
        ("가입 때 놓쳐도 보험기간 중이나 종료 후 신청하면 할인분 환급", "머니투데이"),
        ("운전자 범위, 연령 한정 특약은 해당 안 되는 사람이 운전하다 사고 나면 보상 못 받을 수 있음", "머니투데이, 연합")],
       "부모 보험에 종피보험자로 올라가 있었거나 군 운전병으로 복무했다면 첫 차보험료를 낮출 수 있습니다.\n금감원 사례에서는 133만원이던 보험료가 71만원대로 내려갔습니다.\n님들은 처음 보험료 얼마 나왔나요?\n\n#자동차보험 #사회초년생 #운전병 #금감원 #란빵",
       "님들은 처음 차보험료 얼마 나왔음?",
       "자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 핸드폰 거치대, 초보운전 스티커, 비상삼각대",
       "보험사 이름은 안 씀. 기사 캡처의 기자 사진은 모자이크. 화면 나머지는 AI 배경.",
       [P("news", MT, s0=1.0, s1=1.05)], typ="란빵 자동차, 뉴스")


# ───────────────────────── 5. 주차 자리 침 테러 ─────────────────────────
def EP_spitcar():
    S = "spitcar"
    cap(S, "car", "1044962_00.png", fit=True, boxes=[(90, 268, 110, 45)])
    cap(S, "spit1", "1044962_01.png")
    cap(S, "spit2", "1044962_02.png", fit=True)
    lines = [
        L("전용석? K5랑 카니발 번갈아 주차해 놓으니 좋겠수다.",
          [B("p01", "A handwritten paper note stuck under a car windshield wiper in an underground apartment parking garage, handwriting blurred and unreadable, no people")],
          None, dialogue=True, speaker=3, emotion="normal", say="전용석? 케이파이브랑 카니발 번갈아 주차해 놓으니 좋겠수다."),
        L("아파트 공동현관 옆 자리에 세운 차에 붙은 쪽지 내용임.",
          [P("car", BB, s0=1.0, s1=1.1)], None, em=["공동현관 옆"]),
        L("글쓴이는 5인 가족, 차 두 대 주차비를 다 냄.",
          [B("p02", "An apartment management fee bill and a calculator on a kitchen table, blurred text, no people")], None,
          say="글쓴이는 오인 가족, 차 두 대 주차비를 다 냄.", em=["두 대 주차비"]),
        L("지정석이 아닌 일반 구역에 두 대를 번갈아 세워 왔음.",
          [P("car", BB, s0=1.2, s1=1.35)], None, em=["번갈아"], em_color="yellow"),
        L("그 뒤로 차에 침과 이물질이 계속 묻기 시작함.",
          [P("spit1", BB, s0=1.0, s1=1.12), P("spit1", BB, at="계속", s0=1.5, s1=1.7, punch=True)], None,
          em=["침과 이물질"], em_color="yellow", fx=[("hit_trailer_epic", "침과", 0.45)]),
        L("세차하면 또 침, 닦아 놓으면 또 침.",
          [P("spit2", BB, s0=1.0, s1=1.15, punch=True)], None, em=["또 침"], pop=("또 침!!", R, "닦아"), shake="닦아"),
        L("CCTV엔 같은 라인 남자가 차 쪽으로 고개 돌리는 장면만 찍힘.",
          [B("p03", "Grainy black and white CCTV style view of an apartment parking lot near a building entrance at dusk, a parked minivan, a blurry silhouette of a man walking seen from behind, no faces")],
          None, say="씨씨티비엔 같은 라인 남자가 차 쪽으로 고개 돌리는 장면만 찍힘.", em=["고개 돌리는 장면만"]),
        L("침 뱉는 장면은 안 나와서 단정은 못 하는 상황.",
          [B("p03", s0=1.2, s1=1.35)], None, em=["단정은 못"]),
        L("그런데 댓글 추천 1위는 그 자리 꿀자리 아니냐는 지적.",
          [P("car", BB, s0=1.3, s1=1.45)], None, say="그런데 댓글 추천 일위는 그 자리 꿀자리 아니냐는 지적.", em=["꿀자리"], em_color="yellow",
          fx=[("scratch_vinyl", "꿀자리", 0.45)],
          info={"kind": "bars", "at": "그런데", "title": "댓글 추천", "items": [
              {"label": "번갈아 쓰는 꿀자리", "num": 175, "suffix": "", "at": "꿀자리", "flash": "꿀자리"},
              {"label": "법적으론 문제없지만 얌체", "num": 105, "suffix": "", "at": "지적"}]}),
        L("법적으론 문제없지만 얌체로 보인다, 그래도 침은 아니라는 의견도.",
          [P("spit1", BB, s0=1.2, s1=1.3)], None, em=["얌체로 보인다"]),
        L("님들은 두 대 번갈아 세우는 거 괜찮다고 봄?", [P("car", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "내 돈 내고 주차했는데", "차에 침 테러", "두 대 번갈아 주차하다 생긴 일",
       "#주차 자리 침 테러", "보배드림 베스트 1044962 (2026-11-03, 댓글 77) https://www.bobaedream.co.kr/view?code=best&No=1044962",
       [("5인 가족, K5와 카니발 2대 주차 관리비 납부, 공동현관 옆 일반 주차구역에 번갈아 주차", "원글 본문"),
        ("쪽지 '전용석?', 'K5랑 카니발 서로 번갈아 주차해 놓으니 좋겠수다'", "원글 본문(대사 근거)"),
        ("이후 침, 이물질 반복, 세차하면 또 침", "원글 본문, 첨부 사진"),
        ("11/2 17:42 CCTV, 같은 라인 남성이 차 쪽으로 고개 돌리는 움직임, 침 뱉는 장면은 촬영 안 됨, 단정 못 함", "원글 본문"),
        ("'두 대 번갈아 대 놓은 자리 꿀자리 아닙니까'(175), '법적으로 잘못한 건 없지만 독점하면 얌체처럼, 테러를 잘했다는 건 아님'(105)", "원글 댓글")],
       "차 두 대 주차비를 내고 공동현관 옆 자리에 번갈아 세웠더니 쪽지가 붙고, 그 뒤로 차에 침이 묻기 시작했다는 글입니다.\n댓글은 침은 잘못이지만 꿀자리 독점으로 보인다는 반응이 많았습니다.\n님들은 어떻게 보나요?\n\n#아파트주차 #주차갈등 #카니발 #보배드림 #란빵",
       "님들은 두 대 번갈아 세우는 거 괜찮다고 봄?",
       "자동차 커버, 차량용 세차 타월, 자동차 블랙박스 2채널, 주차번호판, 물왁스",
       "아파트 이름, 지역, 동호수 안 씀. 첨부 사진 3장(카니발, 침 자국), 번호판은 원글이 가린 위를 한 번 더 모자이크. CCTV 화면은 첨부 없어 AI 재연(얼굴 없음).",
       [P("spit2", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 6. 출고 5일 새 차 ─────────────────────────
def EP_newcar5():
    S = "newcar5"
    cap(S, "fender", "1044961_00.jpg", cx=0.4)
    cap(S, "front", "1044961_01.jpg", cx=0.6)
    lines = [
        L("새 차인데 페인트만 살짝 찍고 끝이라고요?",
          [P("fender", BB, s0=1.1, s1=1.25)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("출고 5일 된 첫 차가 주차해 둔 사이에 박혔음.",
          [P("front", BB, s0=1.0, s1=1.12)], None, say="출고 오일 된 첫 차가 주차해 둔 사이에 박혔음.", em=["출고 5일"], em_color="yellow",
          shake="박혔음", fx=[("glass_smash", "박혔음", 0.4)]),
        L("상대는 회사 차라 보험 처리만 된다고 함.",
          [B("n01", "An underground parking garage with a white new SUV parked and an insurance claim document on a clipboard in the foreground, blurred text, no people, no license plate")],
          None, em=["보험 처리만"]),
        L("공업사 견적은 범퍼랑 몰딩은 도색하고 교환.",
          [P("front", BB, s0=1.2, s1=1.4, fx=0.4, fy=0.75)], None, em=["범퍼랑 몰딩"]),
        L("그런데 휀다는 전체 도색이 아깝다며 페인트만 살짝 찍어 준다는 것.",
          [P("fender", BB, s0=1.0, s1=1.12), P("fender", BB, at="살짝", s0=1.6, s1=1.8, fx=0.3, fy=0.55, punch=True)], None,
          em=["페인트만 살짝"], em_color="yellow", pop=("찍기만?!", R, "찍어"), fx=[("wrong_gameshow_buzz", "찍어", 0.45)]),
        L("돈으로 받는 미수선도 금액이 적어서 고민 중.",
          [B("n02", "Close-up of hands holding a smartphone showing a repair cost estimate with blurred numbers, in a car showroom style garage, no faces")],
          None, em=["미수선"]),
        L("색이 스노우펄화이트라 조색도 어렵다는 말까지 들음.",
          [B("n03", "Paint mixing cans and a color sample card with pearl white shades on a workbench in an auto body shop, no people, no readable labels")],
          None, em=["조색도 어렵다"]),
        L("댓글은 저 정도로 휀다 전체 도색하면 바보라는 반응.",
          [P("fender", BB, s0=1.3, s1=1.45, fx=0.4, fy=0.6)], None, em=["바보"], fx=[("drum_rimshot", "바보라는", 0.45)]),
        L("도색하면 수리 이력이 남아 중고로 팔 때 불리하다는 조언도.",
          [B("n04", "A used car dealership lot at dusk with rows of cars, price boards blurred, no people, no license plates visible")],
          None, em=["수리 이력"]),
        L("글쓴이는 새 차라 원래대로 돌리고 싶은 욕심이었다고 함.",
          [P("front", BB, s0=1.2, s1=1.3)], None, em=["원래대로"]),
        L("님들이면 새 차 휀다, 도색함 찍고 탐?", [P("fender", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "탐")]),
    ]
    go(S, lines, "출고 5일 된 첫 차", "휀다는 찍기만?", "새 차 박혔는데 페인트만 살짝",
       "#출고 5일 새차 사고", "보배드림 베스트 1044961 (2026-11-03, 추천 26, 댓글 24) https://www.bobaedream.co.kr/view?code=best&No=1044961",
       [("출고 5일 된 주차된 첫 차를 누가 박음, 가해 차량은 회사 차량 회사 보험이라 보험 처리만 가능", "원글 제목, 본문, 글쓴이 댓글"),
        ("오토큐: 범퍼, 몰딩(블랙 가니쉬)은 도색 교환, 휀다는 전체 도색 아깝다며 페인트 살짝 찍기", "원글 본문(대사 근거)"),
        ("미수선 금액이 많지 않음, 스노우펄화이트 조색 어렵다", "원글 본문"),
        ("'저 정도로 휀다 전체 도색하면 바보'(3), '탈거 도색하면 수리 이력, 중고차로 팔 때 불리'(0)", "원글 댓글"),
        ("'새 차라는 생각, 원복 욕심 때문에 고민'", "글쓴이 댓글")],
       "출고 5일 된 첫 차가 주차 중에 박혔는데, 휀다는 페인트만 살짝 찍어 주겠다는 견적을 받았습니다.\n댓글은 저 정도면 전체 도색이 오히려 손해라는 반응이 많았습니다.\n님들이면 도색하나요, 찍고 타나요?\n\n#새차 #접촉사고 #도색 #보배드림 #란빵",
       "님들이면 새 차 휀다, 도색함 찍고 탐?",
       "자동차 붓펜, 자동차 컴파운드, 도어가드, 자동차 블랙박스 2채널, 주차번호판",
       "첨부 사진 2장(휀다, 앞범퍼)만 실사. 차종은 원글에 없어 안 씀. 공업사 상호 안 씀.",
       [P("front", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 7. 신형 아반떼 페달 공간 ─────────────────────────
def EP_pedalspace():
    S = "pedalspace"
    MA = "화면: mediaAUTO"
    for i in range(5):
        cap(S, f"p{i}", f"1045007_0{i}.jpg", box=(0, 120, 1020, {0: 1000, 1: 1120, 3: 1000}.get(i, 1220)), nofaces=True)
    lines = [
        L("어? 이렇게 갈 때 걸려요, 여기 지금.",
          [P("p0", MA, s0=1.0, s1=1.12)], None, dialogue=True, speaker=2, emotion="surprise"),
        L("신형 아반떼 하이브리드 운전석 발밑 영상이 퍼짐.",
          [P("p3", MA, s0=1.0, s1=1.1)], None, em=["신형 아반떼"], em_color="yellow"),
        L("브레이크로 발을 옮기는데 운동화가 위쪽에 턱 걸림.",
          [P("p1", MA, s0=1.0, s1=1.1), P("p1", MA, at="턱", s0=1.5, s1=1.7, fx=0.65, fy=0.4, punch=True)], None,
          em=["턱 걸림"], shake="걸림", fx=[("hit_trailer_epic", "턱", 0.45)]),
        L("신발이 페달 위 구조물에 끼어 버린다는 것.",
          [P("p2", MA, s0=1.0, s1=1.15, punch=True)], None, em=["끼어 버린다"], pop=("끼었다?!", R, "끼어")),
        L("영상 속 신발은 밑창이 두꺼운 운동화.",
          [P("p3", MA, s0=1.2, s1=1.4, fx=0.5, fy=0.5)], None, em=["밑창이 두꺼운"]),
        L("같은 신발로 다른 차 두 대에선 안 걸렸다고 함.",
          [P("p4", MA, s0=1.0, s1=1.12)], None, em=["안 걸렸다"]),
        L("댓글엔 대차로 5일 타 봤는데 나만 그런 줄 알았다는 경험담.",
          [B("q01", "View down into the driver footwell of a modern compact sedan, brake and accelerator pedals, floor mat, a white sneaker near the pedals, no faces, no logos")],
          None, say="댓글엔 대차로 오일 타 봤는데 나만 그런 줄 알았다는 경험담.", em=["나만 그런 줄"]),
        L("미국 렉서스 매트 문제처럼 넘길 일 아니라는 의견도 있었음.",
          [B("q01", s0=1.2, s1=1.35)], None, em=["넘길 일 아니라는"]),
        L("반면 키높이 운동화라 그렇다는 반응이 추천 1위.",
          [P("p0", MA, s0=1.3, s1=1.45, fx=0.5, fy=0.6)], None, say="반면 키높이 운동화라 그렇다는 반응이 추천 일위.",
          em=["키높이 운동화"], em_color="yellow", fx=[("drum_rimshot", "운동화라", 0.45)]),
        L("매뉴얼에도 운전하기 불편한 신발은 신지 말라는 문구는 있음.",
          [B("q02", "An open car owner's manual book on a car seat with blurred text and pedal diagrams, soft daylight, no people")],
          None, em=["불편한 신발"]),
        L("님들 차도 발 옮길 때 걸리는 데 있음?", [P("p2", MA, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "신형 아반떼 브레이크", "신발이 걸린다?", "운전석 발밑 영상 논란",
       "#신형 아반떼 발 걸림", "보배드림 베스트 1045007 (2026-11-03, 추천 32, 댓글 33) https://www.bobaedream.co.kr/view?code=best&No=1045007",
       [("신형 아반떼 하이브리드 운전석, 운동화가 페달 위쪽에 걸리는 영상 캡처(@mediaAUTO) 5장, '이렇게 갈 때 걸려요 여기 지금', '오버솔 스니커즈이긴 한데'", "원글 첨부(대사 근거)"),
        ("비교 차(아우디 TT, 기아 EV6 GT)에서는 '네 발이 걸리지 않습니다'", "원글 본문, 첨부"),
        ("'키높이 운동화 좋네요 한 5센치 넘을 듯'(11), '대차로 5일 타 본 결과 나만 그런 줄'(3)", "원글 댓글"),
        ("'예전에 북미에서 렉서스 매트 때문에 브레이크 안 밟혀 큰 문제'(2), '매뉴얼에 하이힐 등 운전하기 불편한 신발을 신지 마십시오'(2)", "원글 댓글"),
        ("제조사 공식 입장은 확인 안 됨", "대본에 안 씀")],
       "신형 아반떼 하이브리드에서 브레이크로 발을 옮길 때 운동화가 위쪽에 걸린다는 영상이 돌고 있습니다.\n댓글은 설계 문제라는 쪽과 신발 밑창 탓이라는 쪽으로 갈렸습니다.\n님들 차는 어떤가요?\n\n#아반떼 #신형아반떼 #페달 #보배드림 #란빵",
       "님들 차도 발 옮길 때 걸리는 데 있음?",
       "자동차 매트, 운전용 신발, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 방향제",
       "원글 첨부는 자동차 유튜버(mediaAUTO) 영상 캡처. 앱 아이콘, 핸들명, 댓글 오버레이는 잘라냄, 출처 '화면: mediaAUTO'. 사람 얼굴 없음(발만).",
       [P("p4", MA, s0=1.0, s1=1.05)])


# ───────────────────────── 8. 사이버캡 국내 전시 ─────────────────────────
def EP_cybercab():
    S = "cybercab"
    TS = "사진: 테슬라"
    cap(S, "ext", "cc_677527_291854_4638.png", nofaces=True)
    cap(S, "int", "cc_677527_291855_4658.png", nofaces=True)
    cap(S, "street", "cc_601734_203402_2947.jpg", cx=0.6)
    cap(S, "xpost", "1044994_00.png", fit=True, nofaces=True)
    cap(S, "teaser", "cc_dt.jpg", fit=True, nofaces=True)
    lines = [
        L("와, 이거 운전대가 아예 없네?",
          [P("int", TS, s0=1.0, s1=1.15)], None, dialogue=True, speaker=3, emotion="surprise"),
        L("테슬라가 핸들도 페달도 없는 로보택시 사이버캡을 한국에 가져옴.",
          [P("ext", TS, s0=1.0, s1=1.1), P("ext", TS, at="사이버캡을", s0=1.4, s1=1.6, fx=0.4, fy=0.55, punch=True)], None,
          em=["핸들도 페달도 없는"], em_color="yellow", pop=("핸들 없음?!", Y, "페달도"), fx=[("hit_trailer_epic", "페달도", 0.45)]),
        L("11월 12일부터 15일까지 스타필드 안성에서 전시함.",
          [P("teaser", "사진: 테슬라코리아", s0=1.0, s1=1.1)], None, say="십일월 십이일부터 십오일까지 스타필드 안성에서 전시함.", em=["스타필드 안성"]),
        L("좌석은 딱 두 개, 문은 위로 열리는 버터플라이 도어.",
          [P("street", TS, s0=1.0, s1=1.12), P("int", TS, at="두 개", s0=1.2, s1=1.35)], None, em=["딱 두 개"]),
        L("사이드미러도 없고 운전석 자리엔 화면 하나뿐임.",
          [P("int", TS, s0=1.3, s1=1.5, fx=0.65, fy=0.45, punch=True)], None, em=["화면 하나뿐"]),
        L("미국 오스틴에선 9월부터 돈 받고 손님을 태우는 중.",
          [P("street", TS, s0=1.2, s1=1.35, fx=0.5, fy=0.6)], None, say="미국 오스틴에선 구월부터 돈 받고 손님을 태우는 중.",
          em=["돈 받고 손님을"], fx=[("cash_register_fake", "돈", 0.4)]),
        L("사이버캡은 현재 국내에서 판매되는 차량이 아닙니다.",
          [P("xpost", "화면: 테슬라코리아 X", s0=1.0, s1=1.08)], None, dialogue=True, speaker=2, emotion="normal"),
        L("근데 미국 당국은 이 차가 안전기준에 맞는지 조사 중임.",
          [P("ext", TS, s0=1.2, s1=1.35)], None, em=["안전기준"], em_color="yellow", fx=[("wrong_gameshow_buzz", "조사", 0.4)]),
        L("한국에서 탈 수 있는 날짜는 아직 아무것도 없음.",
          [P("teaser", "사진: 테슬라코리아", s0=1.2, s1=1.3)], None, em=["아무것도 없음"]),
        L("보배 댓글은 택시 기사들 길에 드러눕겠다는 반응.",
          [P("street", TS, s0=1.0, s1=1.08)], None, em=["택시 기사들"], fx=[("drum_rimshot", "드러눕겠다는", 0.45)]),
        L("님들은 운전대 없는 택시 탈 수 있음?", [P("ext", TS, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "운전대 없는 테슬라", "한국에 온다", "로보택시 사이버캡 국내 첫 전시",
       "#핸들 없는 테슬라 택시", "테슬라코리아 공식 X 2026-11-03 (보배드림 베스트 1044994) + 뉴시스 NISX20261103_0003852414, 지디넷 20261103112336, 디지털투데이 712158, 블로터 677527",
       [("11/12~15 스타필드 안성 전시, '현재 국내에서 판매되는 차량이 아닙니다'", "테슬라코리아 X(보배드림 캡처), 뉴시스, 지디넷(대사 근거)"),
        ("2인승, 운전대와 페달 없음, 사이드미러 없음", "뉴시스, 지디넷, 블로터"),
        ("버터플라이 도어", "지디넷"),
        ("9월부터 오스틴에서 유료 승객 운송", "지디넷, 블로터(9/3)"),
        ("NHTSA 가 연방 자동차 안전기준 충족 여부 조사", "뉴시스, 지디넷"),
        ("국내 출시, 상용 운행 일정 공개 안 됨", "지디넷, 블로터"),
        ("'사이버택시 출시되면 택시 기사들 다 밥줄 끊기는 거', 댓글 '개택 기사들 길바닥에 누워서 시위하겄네'", "보배드림 1044994 본문, 댓글")],
       "테슬라가 운전대와 페달이 없는 로보택시 사이버캡을 11월 12일부터 15일까지 스타필드 안성에서 전시합니다.\n테슬라코리아는 국내 판매 차량이 아니라고 밝혔습니다.\n님들은 운전대 없는 택시 타 보실 건가요?\n\n#테슬라 #사이버캡 #로보택시 #자율주행 #란빵",
       "님들은 운전대 없는 택시 탈 수 있음?",
       "차량용 핸드폰 거치대, 차량용 무선충전기, 자동차 블랙박스 2채널, 테슬라 모델Y 매트, 차량용 방향제",
       "차 화면은 전부 테슬라 공식 사진(블로터 '사진 제공=테슬라', 오토데일리)과 테슬라코리아 X 게시물 캡처. AI 그림 없음. 가격, 출시일은 공개 안 돼 안 씀.",
       [P("ext", TS, s0=1.0, s1=1.05)], typ="란빵 자동차, 신차")


# ───────────────────────── 9. 수소 카니발 ─────────────────────────
def EP_h2carnival():
    S = "h2carnival"
    DK = "사진: 대한경제"
    cap(S, "carn", "h2_700181.jpg", nofaces=True, boxes=[(222, 288, 66, 30), (208, 300, 90, 36)])
    cap(S, "news", "1045006_00.jpg", box=(0, 0, 1080, 1120), fit=True)
    lines = [
        L("카니발이 수소차로 나온다고?",
          [P("carn", DK, s0=1.0, s1=1.12)], None, dialogue=True, speaker=3, emotion="surprise"),
        L("기아 노사가 2029년부터 수소 카니발을 만들기로 합의함.",
          [P("news", BB, s0=1.0, s1=1.1)], None, say="기아 노사가 이천이십구년부터 수소 카니발을 만들기로 합의함.",
          em=["수소 카니발"], em_color="yellow", fx=[("hit_trailer_epic", "수소", 0.45)]),
        L("1944년 창사 이후 기아의 첫 양산 수소차임.",
          [P("carn", DK, s0=1.2, s1=1.35, punch=True)], None, say="천구백사십사년 창사 이후 기아의 첫 양산 수소차임.",
          em=["첫 양산 수소차"], pop=("기아 최초!", Y, "첫")),
        L("생산은 경기 광명1공장, 카니발 후속에 수소 모델을 더하는 것.",
          [B("h01", "A modern car factory assembly line with white minivan bodies moving on a conveyor, robotic arms, bright industrial lighting, no people, no logos")],
          None, say="생산은 경기 광명 일공장, 카니발 후속에 수소 모델을 더하는 것.", em=["카니발 후속"]),
        L("현대 넥쏘에 이어 미니밴까지 수소로 넓히는 셈.",
          [B("h02", "A hydrogen fuel dispenser nozzle at a hydrogen refueling station at dusk, blue and white canopy, no people, no readable text, no cars")],
          None, em=["미니밴까지"]),
        L("현대 수소차는 국내 누적 5만대를 넘긴 상황.",
          [B("h02", s0=1.2, s1=1.35)], None, say="현대 수소차는 국내 누적 오만 대를 넘긴 상황.", em=["5만대"],
          info={"kind": "counter", "at": "현대", "title": "현대 수소차 국내 누적", "items": [{"num": 50000, "suffix": "대+"}]}),
        L("충전소는요...?",
          [B("h03", "An empty hydrogen refueling station with a closed sign shutter and traffic cones at night, no people, no readable text")],
          None, dialogue=True, speaker=2, emotion="normal", fx=[("drum_rimshot", "충전소는요", 0.45)]),
        L("보배 댓글 첫 반응은 충전소 걱정이었음.",
          [B("h03", s0=1.2, s1=1.35)], None, em=["충전소 걱정"], em_color="yellow"),
        L("있던 충전소도 없어지거나 버스 때문에 시간제로 넣는다는 댓글.",
          [B("h04", "A long line of hydrogen buses parked at a hydrogen refueling station, daytime, no people, no logos, no readable text")],
          None, em=["시간제로"]),
        L("반대로 보조금 많고 값이 비슷하면 무조건 산다는 넥쏘 차주도 있었음.",
          [P("carn", DK, s0=1.0, s1=1.08)], None, em=["무조건 산다"]),
        L("님들은 수소 카니발 나오면 살 거임?", [P("carn", DK, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "거임")]),
    ]
    go(S, lines, "카니발이", "수소차로 나온다", "기아 첫 양산 수소차, 2029년",
       "#수소 카니발 나온다", "동아일보 20261025/134904983, 연합 AKR20261026060100003, 대한경제 202610261150097240129 + 보배드림 베스트 1045006",
       [("기아 노사 고용안정위원회 합의, 카니발 후속에 수소연료전지차 추가, 2029년부터 광명1공장 생산", "동아, 연합, 대한경제"),
        ("1944년 창사 이래 첫 수소차 양산", "동아(연합, 대한경제 '처음')"),
        ("현대차 수소차 국내 누적 5만대 돌파(9월 말 5만262대)", "대한경제, 머니투데이 2026102611012315690 제목, 뉴시스 제목"),
        ("댓글 '충전소는.........'(2), '있던 충전소도 없어지거나 수소버스 때문에 시간제로'(2), '스택 교체가격 때문에 이미지가 멀어진 듯'(2), '넥쏘 타는 입장, 보조금 많이 주고 하이브리드랑 가격 비슷하면 무조건 수소 카니발'(1)", "보배드림 1045006 댓글(대사 근거)")],
       "기아가 2029년부터 카니발 후속 모델에 수소차를 추가해 광명1공장에서 생산하기로 했습니다.\n기아의 첫 양산 수소차입니다. 댓글 첫 반응은 충전소 걱정이었습니다.\n님들은 수소 카니발 나오면 사실 건가요?\n\n#카니발 #수소차 #기아 #신차 #란빵",
       "님들은 수소 카니발 나오면 살 거임?",
       "카니발 매트, 카니발 햇빛가리개, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 방향제",
       "차 화면은 대한경제 기사 사진(현행 카니발, 번호판 모자이크)과 보배드림 첨부 기사 캡처. 수소 카니발 실물 사진은 없어 안 씀, AI 차 그림 없음(공장, 충전소 배경만). 충전소, 보조금 숫자는 1곳 출처라 안 씀.",
       [P("carn", DK, s0=1.0, s1=1.05)], typ="란빵 자동차, 신차")


# ───────────────────────── 10. 차량용 방향제 ─────────────────────────
def EP_aircare():
    S = "aircare"
    lines = [
        L("이거 해외 직구로 싸게 산 방향제인데 괜찮겠지?",
          [B("a01", "Close-up of a hand clipping a small car air freshener onto a car air vent, dashboard, soft daylight, no faces, no logos, no text")],
          None, dialogue=True, speaker=2, emotion="normal"),
        L("요즘 차량용품 인기 검색어 2위가 차량용 방향제임.",
          [B("a02", "Several different car air fresheners and diffuser bottles arranged on a car dashboard, product shot style, no logos, no text")],
          None, say="요즘 차량용품 인기 검색어 이위가 차량용 방향제임.", em=["2위"], em_color="yellow"),
        L("그런데 소비자원이 해외 구매대행 차량용 화학제품 90개를 검사함.",
          [B("a03", "A laboratory bench with small spray bottles and car air freshener samples next to test tubes and a lab notebook, blurred text, no people")],
          None, say="그런데 소비자원이 해외 구매대행 차량용 화학제품 구십 개를 검사함.", em=["90개"]),
        L("그중 40개, 44.4%가 국내 안전기준에 걸렸음.",
          [B("a03", s0=1.2, s1=1.4, punch=True)], None, say="그중 사십 개, 사십사쩜사퍼센트가 국내 안전기준에 걸렸음.",
          em=["40개"], em_color="yellow", shake="걸렸음", fx=[("hit_trailer_epic", "걸렸음", 0.45)],
          info={"kind": "bars", "at": "그중", "title": "해외 구매대행 차량용 화학제품", "items": [
              {"label": "검사", "num": 90, "suffix": "개", "at": "그중"},
              {"label": "기준 부적합", "num": 40, "suffix": "개", "at": "44.4%가", "flash": "44.4%가"}]}),
        L("코팅제, 세정제, 방향제, 탈취제까지 섞여 있었음.",
          [B("a04", "Assorted unbranded car care spray bottles, coating and cleaner products lined up on a garage shelf, no logos, no readable text, no people")],
          None, em=["방향제"]),
        L("나온 건 벤젠, 폼알데하이드 같은 물질들.",
          [B("a04", s0=1.2, s1=1.35)], None, em=["벤젠, 폼알데하이드"], em_color="yellow"),
        L("특히 MIT, CMIT는 국내 방향제엔 아예 못 쓰는 성분임.",
          [B("a02", s0=1.2, s1=1.35)], None, say="특히 엠아이티, 씨엠아이티는 국내 방향제엔 아예 못 쓰는 성분임.", em=["아예 못 쓰는"],
          fx=[("wrong_gameshow_buzz", "못", 0.4)]),
        L("근데 미국, 일본은 제한이 없어서 직구엔 들어 있을 수 있다는 것.",
          [B("a05", "International shipping parcels and a cardboard box with small bottles inside on a doorstep, no readable labels, no people")],
          None, em=["제한이 없어서"]),
        L("소비자원은 살 때 안전기준 확인 마크를 꼭 보라고 함.",
          [B("a06", "Close-up of the back label area of a plain air freshener bottle held in fingers, label text blurred, a small certification style mark shape blurred, no faces")],
          None, em=["확인 마크"], em_color="yellow", fx=[("correct_ding", "마크를", 0.45)]),
        L("창문 닫고 오래 있는 차 안이라 더 따져 볼 일.",
          [B("a01", s0=1.2, s1=1.35)], None, em=["창문 닫고"]),
        L("님들은 차에 어떤 방향제 씀?", [B("a02", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "씀")]),
    ]
    go(S, lines, "싸게 산 직구 방향제", "이거 확인했음?", "차량용 화학제품 44% 기준 부적합",
       "#직구 차 방향제 주의", "네이버 데이터랩 쇼핑인사이트 자동차용품(cid 50000055) 2026-10-27~11-02 인기검색어 2위 차량용방향제 + 소비자원 2023-11-30 발표(한겨레 1118559, 경향 202311301333001, 컨슈머타임스 570088)",
       [("데이터랩 자동차용품 10/27~11/2 인기검색어 2위 차량용방향제", "네이버 데이터랩 API 조회"),
        ("해외 구매대행 안전기준 미인증 차량용 생활화학제품(코팅제, 세정제, 방향제, 탈취제, 살균제) 90개 조사", "한겨레, 경향, 컨슈머타임스"),
        ("40개(44.4%)에서 금지물질(MIT, CMIT, 염화벤잘코늄류, 벤젠) 또는 제한물질(폼알데하이드, 메탄올 등) 기준 초과", "한겨레, 경향, 컨슈머타임스"),
        ("MIT, CMIT 는 국내 방향제(전 제형) 함유 금지, 미국, 일본은 제한 규정 없음", "컨슈머타임스, 한겨레"),
        ("소비자원 '구매 시 안전기준 확인 마크 확인'", "경향, 컨슈머타임스"),
        ("'창문 닫고 오래 있는 차 안이라 더 따져 볼 일'", "대본 의견(수치 없음)")],
       "차량용 방향제가 자동차용품 검색어 상위에 올라 있습니다.\n소비자원 조사에서 해외 구매대행 차량용 화학제품 90개 중 40개가 국내 안전기준에 맞지 않았습니다(2023년 발표).\n님들은 차에 어떤 방향제 쓰나요?\n\n#차량용방향제 #해외직구 #소비자원 #자동차용품 #란빵",
       "님들은 차에 어떤 방향제 씀?",
       "차량용 방향제, 차량용 디퓨저, 차량용 공기청정기, 차량용 탈취제, 자동차 블랙박스 2채널",
       "조사는 2023-11-30 소비자원, 환경산업기술원 발표(설명란에 연도 표기). 방향제만 따로 몇 개인지는 기사에 없어 '차량용 화학제품'으로 씀. 제품, 브랜드 이름 안 씀. 화면 전부 AI(상표 없음).",
       [B("a06", s0=1.0, s1=1.05)], typ="란빵 자동차, 용품")


EPS = [EP_tirewheel, EP_exportscam, EP_sidescrape, EP_armyins, EP_spitcar, EP_newcar5, EP_pedalspace, EP_cybercab, EP_h2carnival, EP_aircare]

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in EPS:
        if not want or f.__name__[3:] in want:
            f()
