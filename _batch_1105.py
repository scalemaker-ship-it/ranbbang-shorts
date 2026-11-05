#!/usr/bin/env python3
"""란빵 2026-11-05 대상 10편 (11/4 15:00 launchd 헤드리스 실행).
- 보배드림 베스트 7편(관리소장 긁음, 물피도주 발뺌, 도로 파손 타이어, 수신호자, 배터리 40만원, 외벽 세척, 버스 유턴) + 신차 2편(BYD 가격, BMW 7시리즈) + 용품 1편(엔진오일).
- 근거 = work/research_1105.md, 원본 = work/_photos/b1105/ (map.txt). 보배드림 첨부 영상은 vclip() 으로 vid 컷.
- 실명, 상호, 지명, 번호판 없음. 캐릭터 없음(NO_CHAR).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1024 import B, C, L, build, IR, Y, W, R, P   # noqa: E402,F401
from _batch_1027 import cap as _cap   # noqa: E402
import _batch_1102 as _b2   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos", "b1105")
BB = "사진: 보배드림"
BV = "영상: 보배드림"
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


# ───────────────────────── 1. 관리소장이 차를 긁음 ─────────────────────────
def EP_mgrscratch():
    S = "mgrscratch"
    cap(S, "scr", "1045062_00.jpg", box=(0, 250, 1600, 1670), nofaces=True)
    cap(S, "door", "1045062_00.jpg", box=(0, 1100, 1600, 2520), nofaces=True)
    lines = [
        L("합의가 되면 그때 CCTV 영상을 드릴게요.",
          [B("m01", "A security office desk in a Korean apartment management office with CCTV monitors showing an underground parking garage, empty chair, no people, no readable text")],
          None, dialogue=True, speaker=2, emotion="normal", say="합의가 되면 그때 씨씨티비 영상을 드릴게요."),
        L("아파트 지하주차장에 세워 둔 어머니 차가 누군가에게 긁힘.",
          [P("scr", BB, s0=1.0, s1=1.12), P("scr", BB, at="긁힘", s0=1.5, s1=1.7, fx=0.45, fy=0.45, punch=True)], None,
          em=["긁힘"], fx=[("hit_trailer_epic", "긁힘", 0.4)]),
        L("경찰 신고로 잡고 보니 범인은 아파트 관리소장.",
          [B("m02", "A dim Korean apartment underground parking garage with rows of parked cars and pillars, fluorescent lights, no people, no license plates visible", s0=1.0, s1=1.15)],
          None, em=["관리소장"], em_color="yellow", pop=("관리소장?!", R, "관리소장"), shake="관리소장"),
        L("전날 다른 입주민과 싸웠고, 삐딱하게 댄 차를 보고 홧김에 긁었다고 함.",
          [P("door", BB, s0=1.0, s1=1.12)], None, em=["홧김에"]),
        L("작년엔 출구 철제봉에 차가 긁혀 보험 접수를 해 달랬다가 거절당한 사이.",
          [B("m03", "A low steel barrier post installed at the exit lane of an apartment underground parking garage next to a license plate recognition gate, no cars, no people, no readable text")],
          None, em=["거절당한"]),
        L("합의 조건으로 CCTV를 달라 하자 거부.",
          [B("m01", s0=1.15, s1=1.3)], None, say="합의 조건으로 씨씨티비를 달라 하자 거부.", em=["거부"],
          fx=[("wrong_gameshow_buzz", "거부", 0.45)]),
        L("요즘 집에 잘 안 계시는 것 같더라는 말까지 함.",
          [B("m04", "An apartment hallway at night with a closed front door and a dim light, view from a distance, no people, no readable numbers")],
          None, em=["집에 잘 안 계시는"], em_color="yellow", fx=[("drum_rimshot", "말까지", 0.4)]),
        L("결국 글쓴이는 합의를 안 하기로 함.",
          [P("scr", BB, s0=1.2, s1=1.35, fx=0.4, fy=0.5)], None, em=["합의를 안 하기로"]),
        L("형법 366조 재물손괴는 3년 이하 징역 또는 700만원 이하 벌금.",
          [B("m05", "A Korean criminal law book open on a desk with a judge's gavel beside it, soft light, blurred text, no people")],
          None, say="형법 삼백육십육조 재물손괴는 삼년 이하 징역 또는 칠백마넌 이하 벌금.", em=["재물손괴"],
          info={"kind": "quotes", "at": "형법", "title": "형법 366조 재물손괴", "items": [
              {"text": "3년 이하 징역", "at": "3년"}, {"text": "700만원 이하 벌금", "at": "700만원"}]}),
        L("댓글 추천 1위는 착한 코스프레 하지 말라는 조언.",
          [B("m02", s0=1.2, s1=1.3)], None, say="댓글 추천 일위는 착한 코스프레 하지 말라는 조언.", em=["착한 코스프레"]),
        L("님들이면 합의함, 끝까지 감?", [P("door", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "감")]),
    ]
    go(S, lines, "입주민 차 긁은 범인", "관리소장이었다", "지하주차장 고의 긁힘, 범인은 관리소장",
       "#관리소장이 차 긁음", "보배드림 베스트 1045062 (2026-11-03, 추천 583, 댓글 128) https://www.bobaedream.co.kr/view?code=best&No=1045062",
       [("10월 셋째 주 지하주차장 어머니 차 고의 긁힘, 경찰 확인 결과 가해자는 관리소장", "원글 본문"),
        ("전날 다른 입주민과 다툼, 순찰 중 삐딱 주차를 보고 홧김에", "원글 본문(관리소장 말 전달)"),
        ("작년 출구 철제봉 설치 후 차 긁힘, 보험 접수 요청했으나 거부", "원글 본문"),
        ("합의 조건 CCTV 요청 거부, '합의가 되면 그때 CCTV 영상을 드리던지 할게요'", "원글 본문(대사 근거)"),
        ("'요즘 집에 잘 안 계시는 것 같더라고요', 결국 합의 안 하기로", "원글 본문"),
        ("형법 366조 재물손괴: 3년 이하 징역 또는 700만원 이하 벌금", "casenote 형법 366조"),
        ("댓글 '착한 코스프레 할 생각 하지 않는 게 좋으실 듯'(174), '자르는 게 훨씬 이득'(102)", "원글 댓글")],
       "아파트 지하주차장에서 어머니 차를 긁은 사람은 관리소장이었습니다.\n합의 조건으로 CCTV를 요청하자 거부해 글쓴이는 합의하지 않기로 했습니다.\n님들이면 합의하나요, 끝까지 가나요?\n\n#재물손괴 #지하주차장 #아파트 #보배드림 #란빵",
       "님들이면 합의함, 끝까지 감?",
       "자동차 블랙박스 2채널, 블랙박스 메모리카드, 자동차 컴파운드, 자동차 붓펜, 차량용 방향제",
       "아파트 이름, 지역, 관리소장 이름 안 씀. 첨부 사진 1장(긁힌 문)만 실사, 나머지 AI 배경(사람 없음).",
       [P("scr", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 2. 물피도주 후 발뺌 ─────────────────────────
def EP_hitdeny():
    S = "hitdeny"
    vclip(S, "v1", "1045111_m0.mp4", 0, 18, cx=0.5, cy=0.45, zoom=1.0)
    cap(S, "p1", "1045111_00.jpg")
    cap(S, "p2", "1045111_01.jpg")
    lines = [
        L("이제 와서 자기가 박은 게 아니래요.",
          [V("v1", ss=4, s0=1.1, s1=1.2)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("주차장에 세워 둔 빨간 차를 옆 차가 주차하다 쾅.",
          [V("v1", s0=1.0, s1=1.1), V("v1", at="쾅", ss=6, s0=1.3, s1=1.45, fx=0.4, fy=0.4, punch=True)], None,
          em=["쾅"], shake="쾅", fx=[("hit_trailer_epic", "쾅", 0.45)]),
        L("운전석 뒤 펜더랑 범퍼가 다 긁힘.",
          [P("p1", BB, s0=1.0, s1=1.12), P("p2", BB, at="범퍼가", s0=1.0, s1=1.12)], None, em=["다 긁힘"]),
        L("상대는 내려서 확인까지 하고 그냥 떠남.",
          [V("v1", ss=12, s0=1.0, s1=1.1)], None, em=["그냥 떠남"], fx=[("drum_rimshot", "떠남", 0.4)]),
        L("CCTV로 차주를 찾자 할증 무섭다며 현금으로 하자고 함.",
          [B("h01", "Hands holding a smartphone during a phone call in a parked car, dashboard visible, night, no faces, no readable text")],
          None, say="씨씨티비로 차주를 찾자 할증 무섭다며 현금으로 하자고 함.", em=["현금으로"]),
        L("대물접수 하기로 정리했는데, 몇 시간 뒤 반전.",
          [P("p2", BB, s0=1.15, s1=1.3)], None, em=["반전"], pop=("반전", Y, "반전")),
        L("경찰에 본인이 아니라고 발뺌, 차도 못 가져온다고 함.",
          [B("h02", "A Korean police station traffic investigation desk with a monitor and paperwork, fluorescent light, no people, no readable text")],
          None, em=["발뺌"], em_color="yellow", fx=[("wrong_gameshow_buzz", "발뺌", 0.45)]),
        L("주차된 차를 박고 인적사항을 안 남기면 20만원 이하 벌금 대상.",
          [V("v1", ss=8, s0=1.1, s1=1.2)], None, say="주차된 차를 박고 인적사항을 안 남기면 이십마넌 이하 벌금 대상.", em=["인적사항"],
          info={"kind": "quotes", "at": "주차된", "title": "도로교통법 156조 10호", "items": [
              {"text": "주정차된 차만 손괴", "at": "박고"}, {"text": "인적사항 미제공", "at": "인적사항을"}, {"text": "20만원 이하 벌금", "at": "20만원"}]}),
        L("댓글은 경찰에서 사고사실확인원을 받아 상대 보험사에 청구하라는 조언.",
          [B("h03", "A printed traffic accident confirmation document and an insurance claim form on a desk with a pen, blurred text, no people")],
          None, em=["사고사실확인원"]),
        L("아니면 자차로 고치고 보험사가 구상하게 하라는 의견도.",
          [P("p1", BB, s0=1.2, s1=1.35, fx=0.4)], None, em=["구상"]),
        L("님들이면 이런 사람 어떻게 함?", [V("v1", ss=2, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "함")]),
    ]
    go(S, lines, "주차된 차 박고 도망", "잡히자 내가 아니다?", "주차 중 접촉 후 도주, 찾아내자 발뺌",
       "#박고 발뺌한 차주", "보배드림 베스트 1045111 (2026-11-03, 추천 255, 댓글 20) https://www.bobaedream.co.kr/view?code=best&No=1045111",
       [("주차해 둔 차를 상대가 주차하다 운전석 뒤 펜더, 범퍼 파손, 내려서 확인 후 도주", "원글 본문, CCTV 영상, 사진 2장"),
        ("CCTV 확보, 경찰 신고로 특정, 처음엔 할증 때문에 현금 처리 주장, 대물접수 하기로 정리", "원글 본문"),
        ("몇 시간 뒤 경찰에 '본인이 아니다' 부인, 다른 지역이라 차를 못 가져온다", "원글 본문(대사 근거)"),
        ("도로교통법 54조1항2호, 156조10호: 주정차 차만 손괴하고 인적사항 미제공 시 20만원 이하 벌금이나 구류 또는 과료", "casenote 도로교통법"),
        ("댓글 '교통사고사실확인원 받아 상대보험사 청구, 아니면 자차 처리 후 구상권'(14)", "원글 댓글")],
       "주차된 차를 박고 확인까지 한 뒤 떠난 차주가, 찾아내자 본인이 아니라고 발뺌했습니다.\n주차된 차를 손괴하고 인적사항을 남기지 않으면 도로교통법상 처벌 대상입니다.\n님들이면 이런 상대를 어떻게 하나요?\n\n#물피도주 #주차장 #CCTV #보배드림 #란빵",
       "님들이면 이런 사람 어떻게 함?",
       COMMON, "CCTV 영상은 위에서 본 화면, 사람 얼굴 판독 불가, 번호판 안 보임. 지역명 안 씀.",
       [V("v1", ss=10, s0=1.0, s1=1.05)])


# ───────────────────────── 3. 도로 파손 타이어 보상 불가 ─────────────────────────
def EP_roadtire():
    S = "roadtire"
    cap(S, "road", "1045117_00.jpg", nofaces=True)
    cap(S, "tire", "1045117_01.jpg", nofaces=True)
    cap(S, "wheel", "1045117_02.jpg", nofaces=True)
    lines = [
        L("블박이 없고 견인차를 안 불러서 확인이 안 됩니다.",
          [B("r01", "A highway maintenance office service counter with forms and a phone, fluorescent light, no people, no readable text, no logos")],
          None, dialogue=True, speaker=3, emotion="normal"),
        L("고속도로 IC를 빠져나가던 차, 도로랑 교량 이음부가 깨진 곳을 지남.",
          [P("road", BB, s0=1.0, s1=1.12), P("road", BB, at="깨진", s0=1.5, s1=1.7, fx=0.3, fy=0.5, punch=True)], None,
          say="고속도로 아이씨를 빠져나가던 차, 도로랑 교량 이음부가 깨진 곳을 지남.", em=["깨진 곳"]),
        L("그대로 타이어가 찢어짐.",
          [P("tire", BB, s0=1.1, s1=1.3, punch=True)], None, em=["찢어짐"], em_color="yellow",
          shake="찢어짐", pop=("찢어짐!!", R, "찢어짐"), fx=[("hit_trailer_epic", "찢어짐", 0.45)]),
        L("하필 블박은 고장 난 상태.",
          [P("wheel", BB, s0=1.0, s1=1.1)], None, em=["고장 난"], fx=[("drum_rimshot", "상태", 0.4)]),
        L("근처 도로사업소에 바로 신고했더니 담당이 아니라며 다른 곳 번호를 줌.",
          [B("r01", s0=1.15, s1=1.3)], None, em=["담당이 아니라며"]),
        L("톨게이트를 몇 번 돌면서 비상등 켜고 파손 도로 사진까지 찍음.",
          [P("road", BB, s0=1.2, s1=1.35, fx=0.6)], None, em=["사진까지"]),
        L("그런데 돌아온 답은 보상 불가.",
          [P("tire", BB, s0=1.0, s1=1.12)], None, em=["보상 불가"], em_color="yellow",
          pop=("보상 불가", R, "보상"), fx=[("wrong_gameshow_buzz", "불가", 0.45)]),
        L("이유는 블박 영상이 없고 견인차를 안 불렀다는 것.",
          [B("r02", "A tow truck parked on a highway shoulder at dusk with amber lights on, no people, no logos, no readable text")],
          None, em=["견인차"]),
        L("댓글은 저것 때문이라는 증거가 없다는 쪽이 많음.",
          [P("wheel", BB, s0=1.2, s1=1.35, fx=0.4)], None, em=["증거가 없다"]),
        L("타이어 터지면 그 자리 사진과 견인 기록부터 남기라는 조언도.",
          [B("r02", s0=1.15, s1=1.3)], None, em=["견인 기록"], fx=[("correct_ding", "조언도", 0.4)]),
        L("님들은 이거 보상해 줘야 한다고 봄?", [P("road", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "깨진 고속도로 이음부에", "타이어 찢어졌는데", "도로 파손에 타이어 찢어졌는데 보상 불가",
       "#도로 파손 보상 불가", "보배드림 베스트 1045117 (2026-11-03, 추천 100, 댓글 18) https://www.bobaedream.co.kr/view?code=best&No=1045117",
       [("10/24 고속도로 IC 나가는 길 도로와 교량 부분 파손으로 타이어 찢어짐", "원글 본문, 사진 3장"),
        ("블박 고장 상태, 도로공사 민원에 블박 없고 견인차 안 불러 확인 안 된다며 보상 불가", "원글 본문(대사 근거)"),
        ("현장 도로사업소 신고, 담당 아니라 다른 곳 연락처 안내", "원글 본문"),
        ("톨게이트 몇 번 돌며 비상등 켜고 도로 사진 촬영", "원글 본문"),
        ("댓글 '저거 때문에 파손되었다는 증거가 없어서요'(6), '사고 당시 바로 견인차 부르고 사진을 찍어야 보상 가능'(1)", "원글 댓글")],
       "고속도로 IC 출구 도로 파손에 타이어가 찢어졌는데, 블박 영상과 견인 기록이 없어 보상 불가 답을 받았습니다.\n댓글은 증거가 없으면 어렵다는 쪽이 많았습니다.\n님들은 보상해 줘야 한다고 보나요?\n\n#도로파손 #타이어 #고속도로 #보배드림 #란빵",
       "님들은 이거 보상해 줘야 한다고 봄?",
       "자동차 블랙박스 2채널, 블랙박스 메모리카드, 타이어 공기압 주입기, 타이어 펑크 수리킷, 비상삼각대",
       "IC 이름, 지역명 안 씀. 관리주체 배상 조항은 특정 못 해 법 조항 안 씀.",
       [P("road", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 4. 정차 중 수신호자 뒷걸음질 ─────────────────────────
def EP_flagman():
    S = "flagman"
    vclip(S, "v1", "1045197_m0.mp4", 0, 14, cx=0.5, cy=0.6, zoom=1.1, eq="eq=brightness=0.04:gamma=1.2")
    vclip(S, "v2", "1045197_m0.mp4", 13, 6, cx=0.55, cy=0.62, zoom=1.15, eq="eq=brightness=0.04:gamma=1.2")
    lines = [
        L("저는 서 있었는데 사람이 와서 부딪혔어요.",
          [V("v2", ss=1, s0=1.1, s1=1.2)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("비 오는 밤, 수신호를 따라 아주 천천히 움직이던 블박차.",
          [V("v1", s0=1.0, s1=1.08)], None, em=["수신호"]),
        L("앞에서 교통 통제하던 수신호자가 보여서 완전히 멈춤.",
          [V("v1", ss=7, s0=1.05, s1=1.15)], None, em=["완전히 멈춤"]),
        L("그런데 수신호자가 뒷걸음질 치더니 서 있는 차 범퍼에 부딪혀 넘어짐.",
          [V("v2", s0=1.0, s1=1.1), V("v2", at="넘어짐", ss=2, s0=1.2, s1=1.3, punch=True)], None,
          em=["뒷걸음질"], em_color="yellow", shake="넘어짐", pop=("뒷걸음?!", R, "넘어짐"), fx=[("hit_trailer_epic", "넘어짐", 0.45)]),
        L("블박 속도 표시는 0km.",
          [V("v2", ss=3, s0=1.2, s1=1.3, fx=0.3, fy=0.2)], None, say="블박 속도 표시는 영 킬로.", em=["0km"],
          fx=[("drop_futuristic", "0km", 0.45)]),
        L("그런데 보험사는 블박차에도 과실이 있다고 함.",
          [B("f01", "An insurance claim form with a percentage box and a pen on a desk next to a phone, blurred text, no people")],
          None, em=["과실이 있다"], pop=("과실?!", Y, "과실이"), fx=[("wrong_gameshow_buzz", "함", 0.45)]),
        L("근거는 바로 앞이 아닌 맞은편 수신호자 신호를 보고 움직였다는 것.",
          [V("v1", ss=3, s0=1.1, s1=1.2)], None, em=["맞은편"]),
        L("그리고 차가 교차로 안에 있었다는 것.",
          [V("v1", ss=10, s0=1.0, s1=1.1)], None, em=["교차로 안"]),
        L("교통사고 전문 변호사 자문에선 과실 없어 보인다는 의견.",
          [B("f02", "A lawyer's desk with traffic law books, a laptop showing a blurred dashcam frame, desk lamp, no people, no readable text")],
          None, em=["과실 없어"], fx=[("correct_ding", "의견", 0.4)]),
        L("댓글도 서 있는 차에 사람이 넘어진 거라며 무과실 쪽.",
          [V("v2", ss=2, s0=1.0, s1=1.1)], None, em=["무과실"]),
        L("님들은 이거 블박차 과실 있다고 봄?", [V("v1", ss=9, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "멈춰 있는 내 차에", "사람이 뒷걸음질 쿵", "정차 중 수신호자가 뒷걸음질하다 충돌",
       "#멈춘 차에 뒷걸음질", "보배드림 베스트 1045197 (2026-11-04, 추천 55, 댓글 10) https://www.bobaedream.co.kr/view?code=best&No=1045197",
       [("4차로 중 1차로, 맞은편 수신호자 신호에 시속 5km 이하 서행 후 완전 정차(0km/h)", "원글 본문, 영상"),
        ("전방 수신호자가 스스로 뒷걸음질하다 정차한 차 앞범퍼에 부딪혀 넘어짐", "원글 본문(대사 근거)"),
        ("보험사 과실 근거: 바로 앞이 아닌 맞은편 수신호자 신호로 이동, 교차로에 차량 위치", "원글 본문"),
        ("교통사고 전문 변호사 자문 '과실이 없어 보인다'", "원글 본문(이름 안 씀)"),
        ("댓글 '차가 사람을 친 게 아닌 사람이 차에 넘어진 것'(8), '당연히 무과실'(2)", "원글 댓글")],
       "비 오는 밤 정차해 있던 차 앞범퍼에 수신호자가 뒷걸음질하다 부딪혀 넘어졌습니다.\n보험사는 맞은편 수신호를 보고 움직였다는 이유로 블박차 과실을 주장했습니다.\n님들은 블박차 과실이 있다고 보나요?\n\n#과실비율 #블랙박스 #교통사고 #보배드림 #란빵",
       "님들은 이거 블박차 과실 있다고 봄?",
       COMMON, "수신호자 얼굴은 후드와 어둠으로 판독 불가(가까운 장면 13~19초만 사용). 지역명, 변호사 이름 안 씀.",
       [V("v1", ss=5, s0=1.0, s1=1.05)])


# ───────────────────────── 5. 배터리 교체 40만원 ─────────────────────────
def EP_battery40():
    S = "battery40"
    lines = [
        L("저번에는 배터리 얼마 주고 바꾸셨어요?",
          [B("b01", "A car repair shop bay with a car's hood open and a new car battery on a workbench, tools around, daylight, no people, no readable labels, no logos")],
          None, dialogue=True, speaker=2, emotion="normal"),
        L("정비소에서 배터리를 갈던 글쓴이, 전엔 40만원 정도 줬다고 답함.",
          [B("b02", "Close-up of a mechanic's gloved hands lifting an old car battery out of an engine bay, no faces, no readable labels")],
          None, say="정비소에서 배터리를 갈던 글쓴이, 전엔 사십마넌 정도 줬다고 답함.", em=["40만원"]),
        L("그러자 사장님 답은 여기도 40만원.",
          [B("b01", s0=1.15, s1=1.3, punch=True)], None, say="그러자 사장님 답은 여기도 사십마넌.", em=["여기도 40만원"], em_color="yellow",
          pop=("여기도?!", Y, "여기도"), fx=[("drum_rimshot", "여기도", 0.45)]),
        L("나중에 찾아보니 인터넷과 앱에선 공임 포함 20만원대.",
          [B("b03", "Hands holding a smartphone showing an online shopping page of a car battery with a blurred price, at a home desk, no faces, no readable text")],
          None, say="나중에 찾아보니 인터넷과 앱에선 공임 포함 이십마넌대.", em=["20만원대"],
          info={"kind": "compare", "at": "나중에", "title": "배터리 교체 비용", "items": [
              {"label": "정비소 결제", "color": R, "at": "나중에", "rows": [["결제", "40만원", R]]},
              {"label": "인터넷, 앱", "color": Y, "at": "20만원대", "rows": [["공임 포함", "20만원대", Y]]}]}),
        L("명세서를 받아 보니 배터리, 공임, 부가세 합쳐 36만8500원.",
          [B("b04", "A printed itemized repair invoice on a clipboard on a car shop counter, blurred numbers, no people, no readable text")],
          None, say="명세서를 받아 보니 배터리, 공임, 부가세 합쳐 삼십육만 팔천오백원.", em=["36만8500원"],
          info={"kind": "bars", "at": "명세서를", "title": "거래명세서", "items": [
              {"label": "배터리", "num": 275000, "suffix": "원", "at": "배터리,"},
              {"label": "공임", "num": 60000, "suffix": "원", "at": "공임,"},
              {"label": "부가세", "num": 33500, "suffix": "원", "at": "부가세"}]}),
        L("그런데 결제한 돈은 40만원.",
          [B("b05", "A card payment terminal with a printed card receipt on a car shop counter, blurred numbers, no people")],
          None, say="그런데 결제한 돈은 사십마넌.", em=["40만원"], em_color="yellow", fx=[("hit_trailer_epic", "40만원", 0.45)]),
        L("업체는 사장님 와이프가 헷갈린 거라고 함.",
          [B("b04", s0=1.15, s1=1.3)], None, em=["헷갈린"], fx=[("wrong_gameshow_buzz", "헷갈린", 0.45)]),
        L("차액 3만1500원은 돌려받았지만 사과는 못 받음.",
          [B("b05", s0=1.15, s1=1.3)], None, say="차액 삼만 천오백원은 돌려받았지만 사과는 못 받음.", em=["사과는 못 받음"]),
        L("소비자원, 구청 민원도 조치는 어렵다는 답.",
          [B("b06", "A government civil complaint form and a pen on a desk with a laptop, soft light, blurred text, no people")],
          None, em=["조치는 어렵다"]),
        L("댓글은 온라인 주문하고 공임만 받는 곳에서 갈면 훨씬 싸다는 조언.",
          [B("b02", s0=1.15, s1=1.3)], None, em=["훨씬 싸다"], fx=[("correct_ding", "조언", 0.4)]),
        L("님들은 배터리 얼마 주고 갈았음?", [B("b01", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "갈았음")]),
    ]
    go(S, lines, "배터리 갈려는데 사장님", "저번엔 얼마 주셨어요?", "전에 낸 값 말했더니 여기도 40만원",
       "#배터리 교체 40만원", "보배드림 베스트 1045084 (2026-11-03, 추천 20, 댓글 15) https://www.bobaedream.co.kr/view?code=best&No=1045084",
       [("사장 '저번에는 배터리 얼마 주고 교체하셨어요?' → 40만원 → '여기도 40만원입니다', 40만원 결제", "원글 본문(대사 근거)"),
        ("인터넷, 앱에서 같은 배터리 교체비 공임 포함 20만원대", "원글 본문"),
        ("명세서: 배터리 275,000 + 공임 60,000 + 부가세 33,500 = 368,500원", "원글 본문"),
        ("업체 '사장님 와이프분이 헷갈려서', 차액 31,500원 환불", "원글 본문"),
        ("소비자원, 구청 민원, 국세청 진본 확인, 앱 문의 모두 조치 어렵다", "원글 본문"),
        ("댓글 '온라인으로 주문하고 공임나라 예약하면 만원으로 교체 가능'(2)", "원글 댓글")],
       "정비소에서 배터리를 갈며 전에 낸 값을 말했더니 여기도 40만원이라고 해 그대로 결제했습니다.\n명세서 합계는 36만8500원이었고 차액만 돌려받았습니다.\n님들은 배터리 교체에 얼마 냈나요?\n\n#배터리교체 #정비소 #자동차배터리 #보배드림 #란빵",
       "님들은 배터리 얼마 주고 갈았음?",
       "자동차 배터리, 자동차 배터리 충전기, 자동차 점프스타터, 배터리 테스터기, 자동차 블랙박스 2채널",
       "지역, 업체명 안 씀. 첨부 없음, 화면 전부 AI 배경(사람 얼굴, 상표 없음).",
       [B("b01", s0=1.0, s1=1.05)])


# ───────────────────────── 6. 외벽 세척에 차 얼룩 ─────────────────────────
def EP_washcar():
    S = "washcar"
    cap(S, "w0", "1045130_00.jpg", box=(0, 0, 1600, 1000), fit=True, nofaces=True)
    cap(S, "w2", "1045130_02.jpg", nofaces=True)
    cap(S, "w4", "1045130_04.jpg", nofaces=True)
    cap(S, "w5", "1045130_05.jpg", box=(0, 0, 1600, 1420), nofaces=True)
    lines = [
        L("세차로 끝낼 거면 바로 돈 보내 드릴게요.",
          [B("c01", "Construction gondola and water hoses hanging on the exterior wall of a Korean apartment building, wet facade, daytime, no people, no readable text")],
          None, dialogue=True, speaker=3, emotion="normal"),
        L("아파트 외벽 보수 전에 물세척을 하면서, 주차된 차에 얼룩이 잔뜩.",
          [P("w0", BB, s0=1.0, s1=1.1), P("w5", BB, at="얼룩이", s0=1.0, s1=1.15, punch=True)], None, em=["얼룩이"], em_color="yellow"),
        L("비닐을 안 씌운 이유는 관리소랑 소통이 안 돼서였다고 함.",
          [P("w2", BB, s0=1.0, s1=1.12)], None, em=["소통이 안 돼서"]),
        L("차 빼 달라는 방송도 안 했다는 것.",
          [B("c01", s0=1.15, s1=1.3)], None, em=["방송도 안 했다"], fx=[("drum_rimshot", "것", 0.4)]),
        L("아침에 있던 차만 비닐을 씌우고, 나중에 온 차는 그냥 작업.",
          [B("c02", "Cars covered with plastic sheets parked next to uncovered cars in front of an apartment building under facade repair, wet ground, no people, no license plates visible")],
          None, em=["그냥 작업"], fx=[("wrong_gameshow_buzz", "그냥", 0.45)]),
        L("대신 세척하던 고압건으로 한 번 뿌려 줬다고 함.",
          [P("w4", BB, s0=1.0, s1=1.12)], None, em=["고압건"], pop=("고압건?!", Y, "고압건으로")),
        L("현장소장이 제시한 건 세차비 3만원에서 5만원.",
          [P("w5", BB, s0=1.2, s1=1.35, fx=0.4)], None, say="현장소장이 제시한 건 세차비 삼마넌에서 오마넌.", em=["3만원에서 5만원"],
          fx=[("drop_futuristic", "5만원", 0.45)]),
        L("광택에만 3일이 걸렸고 글쓴이는 보험처리를 요구함.",
          [P("w2", BB, s0=1.2, s1=1.35, fx=0.6)], None, say="광택에만 삼일이 걸렸고 글쓴이는 보험처리를 요구함.", em=["보험처리"]),
        L("업체 쪽은 보험은 몇 개월 걸린다고 함.",
          [P("w0", BB, s0=1.15, s1=1.3)], None, em=["몇 개월"]),
        L("댓글은 보양 안내가 없었다면 업체 책임이라는 의견, 공지는 있었을 거라는 의견.",
          [B("c02", s0=1.15, s1=1.3)], None, em=["업체 책임"]),
        L("님들이면 세차비 받고 끝냄, 보험 감?", [P("w4", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "감")]),
    ]
    go(S, lines, "아파트 외벽 물청소에", "주차된 차 얼룩 범벅", "외벽 세척에 차 오염, 제시액은 세차비 3~5만원",
       "#외벽 물청소 차 얼룩", "보배드림 베스트 1045130 (2026-11-04, 추천 51, 댓글 5) https://www.bobaedream.co.kr/view?code=best&No=1045130",
       [("아파트 외벽 보수 전 물세척으로 차량 오염, 현장소장 세차비 3~5만원 지원", "원글 본문, 사진 7장"),
        ("비닐 안 씌운 이유: 관리소와 소통 안 됨, 차량 이동 방송 안 함, 아침 차량만 비닐", "원글 본문"),
        ("이후 들어온 차는 작업 뒤 세척한 고압건으로 한 번 뿌려 줌", "원글 본문"),
        ("업체 이사 '세차로 끝낼 거면 바로 돈 보내주겠다', 보험처리 요구, '몇 개월 걸린다'", "원글 본문(대사 근거)"),
        ("페인트 광택 3일 걸림", "원글 본문"),
        ("댓글 '보양 안내가 제대로 안 되었다면 시공 업체가 세차 비용 책임'(5), '공지문 게시 되어 있었을 텐데'(1)", "원글 댓글")],
       "아파트 외벽 보수 전 물세척 때 비닐을 안 씌운 차들에 얼룩이 생겼습니다.\n업체는 세차비 3~5만원을 제시했고 글쓴이는 보험처리를 요구했습니다.\n님들이면 세차비 받고 끝내나요, 보험 가나요?\n\n#세차 #아파트 #차량오염 #보배드림 #란빵",
       "님들이면 세차비 받고 끝냄, 보험 감?",
       "자동차 물왁스, 세차 타월, 자동차 철분제거제, 자동차 광택제, 자동차 블랙박스 2채널",
       "1045130_00 은 번호판 아래를 잘라냄, 사람이 비치는 사진(03, 06)은 안 씀. 아파트 이름, 지역 안 씀.",
       [P("w2", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 7. 버스 유턴에 오토바이 꽈당 ─────────────────────────
def EP_uturnq():
    S = "uturnq"
    vclip(S, "v1", "1045110_m0.mp4", 9, 13, cx=0.4, cy=0.55, zoom=1.35, blur=((560, 180, 420, 360),))  # 버스 뒤 학원명, 번호판
    vclip(S, "v2", "1045110_m0.mp4", 38, 12, cx=0.4, cy=0.55, zoom=1.35)  # 만든 뒤 0~3.2초 학원명 구간 시간 지정 모자이크(ffmpeg 수동, research_1105 참고)
    lines = [
        L("사고를 기다리는 블박이네요.",
          [V("v2", ss=4, s0=1.1, s1=1.2)], None, dialogue=True, speaker=3, emotion="normal"),
        L("퀵 배달 오토바이가 소형 버스 뒤에 붙어 섬.",
          [V("v1", s0=1.0, s1=1.08)], None, em=["소형 버스"]),
        L("버스 뒤에서 한참을 기다림.",
          [V("v1", ss=7, s0=1.05, s1=1.15)], None, em=["한참을"]),
        L("드디어 버스가 출발하며 유턴을 시작함.",
          [V("v2", s0=1.0, s1=1.1)], None, em=["유턴"]),
        L("그 순간 오토바이도 같이 나가면서 버스 옆으로 바짝.",
          [V("v2", ss=2, s0=1.1, s1=1.2)], None, em=["바짝"]),
        L("결국 중심을 잃고 그대로 넘어짐.",
          [V("v2", ss=5, s0=1.1, s1=1.25, punch=True)], None, em=["넘어짐"], em_color="yellow",
          shake="넘어짐", pop=("꽈당!!", R, "넘어짐"), fx=[("hit_trailer_epic", "넘어짐", 0.45)]),
        L("글쓴이는 과실 비율이 궁금하다며 영상을 올림.",
          [V("v1", ss=9, s0=1.0, s1=1.1)], None, em=["과실 비율"]),
        L("그런데 댓글 추천 1위는 충분히 피할 수 있었다는 지적.",
          [V("v2", ss=3, s0=1.15, s1=1.25)], None, say="그런데 댓글 추천 일위는 충분히 피할 수 있었다는 지적.",
          em=["피할 수 있었다"], fx=[("wrong_gameshow_buzz", "지적", 0.45)]),
        L("큰 차는 한 번에 유턴 못 하니 저 자리로 들어가면 안 된다는 말도.",
          [B("u01", "A small Korean shuttle bus making a wide U-turn at a city intersection at night, seen from behind, light trails, no people visible, no readable text, no license plate visible")],
          None, em=["한 번에 유턴 못 하니"]),
        L("유턴은 앞차가 다 돌고 나서 도는 거라는 댓글도 많음.",
          [B("u01", s0=1.15, s1=1.3)], None, em=["앞차가 다 돌고"]),
        L("님들은 이거 몇 대 몇이라고 봄?", [V("v1", ss=3, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "버스 유턴하는데", "옆에 붙은 오토바이", "유턴하던 버스 옆 오토바이 넘어짐",
       "#버스 유턴에 꽈당", "보배드림 베스트 1045110 (2026-11-03, 추천 22, 댓글 52) https://www.bobaedream.co.kr/view?code=best&No=1045110",
       [("퀵 기사(글쓴이) 오토바이, 소형 버스 뒤 대기, 버스 유턴 중 사고, 과실 질문", "원글 본문, 영상(블박 화면을 휴대폰으로 촬영)"),
        ("댓글 '사고를 기다리는 블박이네요, 충분히 피할 수 있는게 그냥 가만히 있음'(27)", "원글 댓글(대사 근거)"),
        ("댓글 '대형차가 한번에 유턴 못한다 생각하고 저기로 기어들어가지 않음'(21), '회전각을 아는 운전자는 저런 사고가 안 남'(15)", "원글 댓글"),
        ("댓글 '유턴은 선행차 완료되면 도는 것'(9)", "원글 댓글")],
       "소형 버스 뒤에서 기다리던 오토바이가 버스 유턴 순간 같이 나가다 넘어졌습니다.\n댓글은 충분히 피할 수 있었다는 지적이 많았습니다.\n님들은 과실이 몇 대 몇이라고 보나요?\n\n#유턴사고 #과실비율 #블랙박스 #보배드림 #란빵",
       "님들은 이거 몇 대 몇이라고 봄?",
       COMMON, "영상 위쪽 휴대폰 촬영자 실루엣은 잘라냄. 버스 회사명 판독 불가. 지역명 안 씀.",
       [V("v2", ss=6, s0=1.0, s1=1.05)])


# ───────────────────────── 8. BYD 3990만원 ─────────────────────────
def EP_byd4490():
    S = "byd4490"
    cap(S, "seal", "1044985_01.png", fit=True, nofaces=True)
    cap(S, "slion", "1044985_00.png", fit=True, nofaces=True)
    cap(S, "dol", "byd_ebn_a.png", nofaces=True)
    cap(S, "show", "byd_ebn_b.jpg", nofaces=True)
    BS = "화면: 보배드림"
    BY = "사진: BYD코리아"
    lines = [
        L("이 가격 실화야?",
          [P("seal", BS, s0=1.3, s1=1.5, fx=0.82, fy=0.92)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("중국 BYD의 중형 전기 세단 씰이 3990만원부터.",
          [P("seal", BS, s0=1.0, s1=1.1)], None, say="중국 비와이디의 중형 전기 세단 씰이 삼천구백구십마넌부터.", em=["3990만원"], em_color="yellow",
          fx=[("drop_futuristic", "3990만원부터", 0.5)]),
        L("중형 전기 SUV 씨라이언7은 4490만원부터.",
          [P("slion", BS, s0=1.0, s1=1.1), P("show", BY, at="4490만원부터", s0=1.0, s1=1.1)], None,
          say="중형 전기 에스유브이 씨라이언세븐은 사천사백구십마넌부터.", em=["4490만원"]),
        L("아이오닉5 시작가 4735만원보다 200만원 넘게 쌈.",
          [P("show", BY, s0=1.15, s1=1.3)], None, say="아이오닉파이브 시작가 사천칠백삼십오마넌보다 이백마넌 넘게 쌈.", em=["200만원 넘게"],
          info={"kind": "bars", "at": "아이오닉5", "title": "시작 가격", "items": [
              {"label": "아이오닉5", "num": 4735, "suffix": "만원", "at": "아이오닉5"},
              {"label": "씨라이언7", "num": 4490, "suffix": "만원", "at": "200만원", "flash": "쌈"}]}),
        L("소형 해치백 돌핀은 2450만원부터 시작함.",
          [P("dol", BY, s0=1.0, s1=1.12)], None, say="소형 해치백 돌핀은 이천사백오십마넌부터 시작함.", em=["2450만원"]),
        L("근데 BYD는 7월부터 정부 전기차 보조금을 못 받고 있음.",
          [P("dol", BY, s0=1.2, s1=1.35, fx=0.4)], None, say="근데 비와이디는 칠월부터 정부 전기차 보조금을 못 받고 있음.",
          em=["보조금을 못 받고"], pop=("보조금 끊김", R, "보조금을"), fx=[("hit_trailer_epic", "보조금을", 0.45)]),
        L("대신 보조금만큼 자체 지원을 붙였더니 월 판매가 오히려 30% 늘었음.",
          [P("show", BY, s0=1.0, s1=1.1)], None, say="대신 보조금만큼 자체 지원을 붙였더니 월 판매가 오히려 삼십퍼센트 늘었음.", em=["30%"], em_color="yellow",
          info={"kind": "bars", "at": "대신", "title": "BYD 월평균 판매", "items": [
              {"label": "상반기", "num": 1946, "suffix": "대", "at": "대신"},
              {"label": "7~9월", "num": 2531, "suffix": "대", "at": "30%", "flash": "늘었음"}]}),
        L("그런데 보배드림 반응은 싸늘함.",
          [P("seal", BS, s0=1.15, s1=1.3, fx=0.3)], None, em=["싸늘함"], fx=[("drum_rimshot", "싸늘함", 0.4)]),
        L("추천 1위는 중국산 내구성을 걱정하는 댓글.",
          [P("slion", BS, s0=1.2, s1=1.35, fx=0.3)], None, say="추천 일위는 중국산 내구성을 걱정하는 댓글.", em=["내구성"]),
        L("광주에서 고장 나면 부산에서 수리 받는다는 서비스망 걱정도.",
          [P("show", BY, s0=1.2, s1=1.35, fx=0.6)], None, em=["서비스망"]),
        L("님들은 이 가격이면 BYD 삼?", [P("seal", BS, s0=1.0, s1=1.1)], None, say="님들은 이 가격이면 비와이디 삼?",
          fx=[("pop_bubble", "삼")]),
    ]
    go(S, lines, "중국 전기 세단 씰", "3990만원부터", "BYD 씰 3990만원, 씨라이언7 4490만원",
       "#BYD 3990만원", "BYD 가격(시사저널e 424447, 이코노미스트 ecn202608310055, EBN 1724287, 아주경제 20261103145524277) + EBN 1730426(보조금, 판매) + 보배드림 베스트 1044985 (추천 145, 댓글 189)",
       [("씰 3990만원, 씨라이언7 4490만원, 돌핀 2450만원부터", "시사저널e, 이코노미스트, EBN(일치), 보배 견적 화면"),
        ("씨라이언7 4490만원 < 아이오닉5 시작가 4735만원(200만원 이상 저렴)", "아주경제"),
        ("7/1부터 국고, 지방 보조금 제외(수행자 평가 유일 탈락), 국고보조금 수준 자체 지원", "EBN 1730426"),
        ("씨라이언6 DM-i 제외 7~9월 월평균 2531대, 상반기 월평균 1946대보다 30% 증가(KAIDA)", "EBN 1730426"),
        ("보배 댓글 추천 1위(84) 중국산 내구성 비꼼, '광주에서 고장났는데 부산에서 수리 받는다'(65)", "보배드림 1044985 댓글"),
        ("'이 가격 실화야?' 는 구경꾼 반응 대사", "대본 구성")],
       "BYD 씰은 3990만원, 씨라이언7은 4490만원부터 판매되고 있습니다.\n7월부터 정부 보조금이 끊겼지만 자체 지원으로 월평균 판매는 30% 늘었습니다.\n님들은 이 가격이면 BYD를 사나요?\n\n#BYD #전기차 #씰 #씨라이언7 #란빵",
       "님들은 이 가격이면 BYD 삼?",
       "자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 전기차 충전 케이블 정리함, 자동차 시트커버, 차량용 방향제",
       "차 화면은 BYD 견적 화면 캡처(보배드림 게재)와 BYD코리아 보도사진(EBN 게재)만, AI 차 그림 없음. 가격은 보조금 적용 전.",
       [P("slion", BS, s0=1.0, s1=1.05)], typ="란빵 자동차, 신차")


# ───────────────────────── 9. BMW 신형 7시리즈 ─────────────────────────
def EP_bmw7new():
    S = "bmw7new"
    cap(S, "line", "bmw7_a.jpg", nofaces=True)
    cap(S, "out", "bmw7_b.jpg", nofaces=True, boxes=[(318, 381, 46, 24), (406, 342, 34, 22)])
    cap(S, "linew", "bmw7_a.jpg", fit=True, nofaces=True)
    BM = "사진: BMW코리아"
    lines = [
        L("뒷좌석에 영화관을 넣었네?",
          [P("line", BM, s0=1.1, s1=1.25)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("BMW가 7시리즈 부분변경을 11월 4일 국내 출시함.",
          [P("linew", BM, s0=1.0, s1=1.08)], None, say="비엠더블유가 칠시리즈 부분변경을 십일월 사일 국내 출시함.", em=["7시리즈"]),
        L("뒷좌석엔 천장에서 내려오는 31.3인치 8K 시어터 스크린.",
          [P("out", BM, s0=1.0, s1=1.12), P("out", BM, at="31.3인치", s0=1.6, s1=1.8, fx=0.4, fy=0.6, punch=True)], None,
          say="뒷좌석엔 천장에서 내려오는 삼십일쩜삼인치 에잇케이 시어터 스크린.", em=["31.3인치"], em_color="yellow",
          pop=("31.3인치", Y, "31.3인치"), fx=[("drop_futuristic", "31.3인치", 0.5)]),
        L("화면에 카메라가 달려 있어서 화상회의도 됨.",
          [P("line", BM, s0=1.3, s1=1.45, fx=0.3, fy=0.6)], None, em=["화상회의"]),
        L("문턱에선 약 19만 4천 개 픽셀이 바닥에 그림을 비춤.",
          [P("line", BM, s0=1.4, s1=1.6, fx=0.6, fy=0.75)], None, say="문턱에선 약 십구만 사천 개 픽셀이 바닥에 그림을 비춤.", em=["19만 4천 개"],
          info={"kind": "counter", "at": "문턱에선", "title": "라이트 카펫 픽셀", "items": [{"num": 194000, "suffix": "개"}]}),
        L("전기차 i7 50의 국내 인증 주행거리는 508km, 전보다 53km 늘었음.",
          [P("out", BM, s0=1.15, s1=1.3, fx=0.7)], None, say="전기차 아이세븐 오십의 국내 인증 주행거리는 오백팔 킬로, 전보다 오십삼 킬로 늘었음.", em=["508km"],
          info={"kind": "bars", "at": "전기차", "title": "i7 50 주행거리", "items": [
              {"label": "기존", "num": 455, "suffix": "km", "at": "전기차"},
              {"label": "신형", "num": 508, "suffix": "km", "at": "508km,", "flash": "늘었음"}]}),
        L("최상위 M70은 시속 100km까지 3.8초.",
          [P("line", BM, s0=1.5, s1=1.7, fx=0.42, fy=0.8, punch=True)], None, say="최상위 엠칠십은 시속 백 킬로까지 삼쩜팔초.", em=["3.8초"],
          pop=("3.8초!!", R, "3.8초"), fx=[("hit_trailer_epic", "3.8초", 0.45)]),
        L("근데 문제는 가격.",
          [B("w01", "A luxury car showroom price stand with a blank price card under spotlights, polished floor, no cars, no people, no logos, no readable text")],
          None, em=["가격"], fx=[("drum_rimshot", "가격", 0.4)]),
        L("가솔린 740이 1억 6190만원부터, M70은 2억 3500만원.",
          [P("linew", BM, s0=1.1, s1=1.2)], None, say="가솔린 칠사공이 일억 육천백구십마넌부터, 엠칠십은 이억 삼천오백마넌.", em=["2억 3500만원"], em_color="yellow",
          info={"kind": "bars", "at": "가솔린", "title": "시작 가격", "items": [
              {"label": "740 xDrive", "num": 16190, "suffix": "만원", "at": "가솔린"},
              {"label": "i7 M70", "num": 23500, "suffix": "만원", "at": "M70은", "flash": "3500만원"}]}),
        L("퍼스트 에디션 3종은 11월 10일 온라인 한정 판매.",
          [P("out", BM, s0=1.0, s1=1.1)], None, say="퍼스트 에디션 삼종은 십일월 십일 온라인 한정 판매.", em=["한정 판매"]),
        L("님들은 7시리즈 사면 뒷좌석 탐, 운전석 탐?", [P("line", BM, s0=1.0, s1=1.1)], None,
          say="님들은 칠시리즈 사면 뒷좌석 탐, 운전석 탐?", fx=[("pop_bubble", "운전석")]),
    ]
    go(S, lines, "뒷좌석 31.3인치 영화관", "BMW 신형 7시리즈", "BMW 7시리즈 부분변경 11월 4일 국내 출시",
       "#신형 7시리즈 출시", "BMW코리아 11/4 발표: 지디넷 20261104131542, 매일일보 2014373, 데일리카 63068, 뉴스투데이 20261104500136",
       [("11/4 더 뉴 7시리즈(부분변경) 국내 출시", "지디넷, 매일일보, 뉴스투데이(일치)"),
        ("31.3인치 8K 시어터 스크린, 500만 화소 카메라 화상회의", "지디넷"),
        ("도어 실 약 19만4000개 픽셀 세리모니얼 라이트 카펫", "지디넷"),
        ("i7 50 국내 인증 508km(기존보다 53km 증가), M70 0→100km/h 3.8초", "지디넷"),
        ("740 xDrive 1억6190~1억7920만원, i7 M70 2억3500만원", "지디넷, 매일일보, 데일리카(일치)"),
        ("11/10 BMW 샵 온라인 퍼스트 에디션 3종 한정 판매", "지디넷"),
        ("'뒷좌석에 영화관을 넣었네?' 는 구경꾼 반응 대사", "대본 구성")],
       "BMW 7시리즈 부분변경 모델이 11월 4일 국내 출시됐습니다.\n뒷좌석 31.3인치 8K 스크린, i7 50 주행거리 508km, 가격은 1억6190만원부터 2억3500만원입니다.\n님들은 7시리즈를 사면 뒷좌석에 타나요, 운전석에 타나요?\n\n#BMW #7시리즈 #i7 #신차 #란빵",
       "님들은 7시리즈 사면 뒷좌석 탐, 운전석 탐?",
       "자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 자동차 시트커버, 차량용 방향제, 자동차 햇빛가리개",
       "차 화면은 BMW코리아 보도사진 2장(지디넷 게재)만, AI 차 그림 없음. 시어터 스크린 실물 사진은 확보 못 해 차 외관 확대로 대체.",
       [P("linew", BM, s0=1.0, s1=1.05)], typ="란빵 자동차, 신차")


# ───────────────────────── 10. 엔진오일 과다 주입 ─────────────────────────
def EP_oilover():
    S = "oilover"
    lines = [
        L("오일 갈면서 이렇게 많이 넣은 건 처음이네요.",
          [B("o01", "Close-up of a car engine oil dipstick pulled out and held above an open engine bay, the oil level mark far above the max line, daylight, gloved hand, no faces, no readable labels")],
          None, dialogue=True, speaker=2, emotion="toneup"),
        L("최근 네이버 쇼핑 자동차용품 검색어 7위, 엔진오일.",
          [B("o02", "Several unbranded bottles of car engine oil lined up on a garage shelf, warm light, no readable labels, no logos")],
          None, say="최근 네이버 쇼핑 자동차용품 검색어 칠위, 엔진오일.", em=["엔진오일"], em_color="yellow",
          fx=[("drop_futuristic", "7위,", 0.45)]),
        L("한 운전자가 정비 체인점에서 엔진오일을 갈고 집에 옴.",
          [B("o03", "A car parked in front of a small auto repair shop bay with its door open, daytime, no people, no readable signs, no logos, no license plate visible")],
          None, em=["정비 체인점"]),
        L("게이지를 뽑아 보니 최고 눈금보다 4센치나 위.",
          [B("o01", s0=1.2, s1=1.4, punch=True)], None, say="게이지를 뽑아 보니 최고 눈금보다 사센치나 위.", em=["4센치나 위"], em_color="yellow",
          pop=("4cm 초과?!", R, "4센치나"), shake="위", fx=[("hit_trailer_epic", "4센치나", 0.45)]),
        L("게이지 주변엔 없던 오일까지 흥건히 고여 있었음.",
          [B("o04", "Close-up of spilled engine oil pooling around the dipstick tube in a car engine bay, glossy, no people, no readable labels")],
          None, em=["흥건히"]),
        L("가져간 오일 양을 말 안 했더니 다 부은 것 같다고 함.",
          [B("o02", s0=1.15, s1=1.3)], None, em=["다 부은"], fx=[("drum_rimshot", "부은", 0.4)]),
        L("엔진오일이 너무 많으면 출력이 줄고 연비도 떨어진다는 게 점검 안내.",
          [B("o05", "A car engine bay with the oil filler cap open and a funnel inserted, soft garage light, no people, no readable labels")],
          None, em=["출력이 줄고"],
          info={"kind": "quotes", "at": "엔진오일이", "title": "엔진오일 과다 주입", "items": [
              {"text": "출력 감소", "at": "출력이"}, {"text": "연비 감소", "at": "연비도"}]}),
        L("오일 과다 주입 결함 등으로 4만 대 넘게 리콜된 차도 있었음.",
          [B("o04", s0=1.15, s1=1.3)], None, say="오일 과다 주입 결함 등으로 사만 대 넘게 리콜된 차도 있었음.", em=["리콜"],
          info={"kind": "bars", "at": "오일", "title": "2017 리콜 대상", "items": [
              {"label": "경차 리콜", "num": 44567, "suffix": "대", "at": "4만"}]}),
        L("댓글은 알아서 뱉어내긴 해도 엔진룸이 더러워지니 빼 달라는 조언.",
          [B("o05", s0=1.15, s1=1.3)], None, em=["빼 달라는"]),
        L("주사기랑 호스로 직접 빼도 되는데, 주행 후 바로 빼야 잘 빠진다는 팁도.",
          [B("o06", "A large plastic syringe with a thin hose next to a car engine oil dipstick tube in an engine bay, gloved hand, no faces, no readable labels")],
          None, em=["주행 후 바로"], fx=[("correct_ding", "팁도", 0.4)]),
        L("님들은 오일 갈고 게이지 확인함?", [B("o01", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "확인함")]),
    ]
    go(S, lines, "엔진오일 갈았더니", "게이지 4센치 초과", "엔진오일 교체 후 최고 눈금보다 4cm 위",
       "#엔진오일 과다 주입", "보배드림 베스트 1045090 (2026-11-03, 추천 57, 댓글 11) https://www.bobaedream.co.kr/view?code=best&No=1045090 + 네이버 데이터랩 자동차용품(cid 50000055) 10/28~11/3 인기검색어 7위 엔진오일",
       [("데이터랩 자동차용품 10/28~11/3 인기검색어 7위 엔진오일", "네이버 데이터랩 조회"),
        ("교체 후 게이지가 최고치보다 4cm 정도 초과, 게이지 주변 오일 고임, 말을 안 했더니 다 부은 듯", "원글 본문"),
        ("'차 오일 갈면서 이렇게 많이 넣은건 처음이네요'", "원글 본문(대사 근거)"),
        ("과다 주입 시 출력 감소, 연료 소모량 증가로 연비 감소", "경기신문 kgnews 687429"),
        ("한국GM 넥스트 스파크 엔진오일 과다주입 및 ECU 소프트웨어 결함으로 출력 저하 가능성 리콜 4만4567대(2017)", "이데일리, 한국경제, 비즈니스포스트"),
        ("댓글 '알아서 뱉어내긴 합니다만 엔진룸이 더러워지니 빼달라고', '주사기랑 호스로 직접, 주행 후 바로 빼야 수월'", "원글 댓글")],
       "엔진오일을 갈고 왔더니 게이지가 최고 눈금보다 4cm 위였다는 글입니다.\n엔진오일이 너무 많으면 출력과 연비가 떨어질 수 있습니다.\n님들은 오일 교체 후 게이지를 확인하나요?\n\n#엔진오일 #엔진오일교환 #자동차관리 #보배드림 #란빵",
       "님들은 오일 갈고 게이지 확인함?",
       "엔진오일, 엔진오일 교환 석션기, 엔진오일 깔때기, 자동차 정비 장갑, 자동차 블랙박스 2채널",
       "정비 체인 상호는 대본에 안 씀(근거표에만 원문). 리콜 차종은 대본에 안 씀. 첨부 없음, 화면 AI 배경(상표 없음).",
       [B("o01", s0=1.0, s1=1.05)], typ="란빵 자동차, 용품")


EPS = [EP_mgrscratch, EP_hitdeny, EP_roadtire, EP_flagman, EP_battery40, EP_washcar, EP_uturnq, EP_byd4490, EP_bmw7new, EP_oilover]

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in EPS:
        if not want or f.__name__[3:] in want:
            f()
