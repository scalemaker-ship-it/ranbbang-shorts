#!/usr/bin/env python3
"""란빵 2026-11-01 대상 daily 10편 (2026-10-31 15:00 launchd 실행).
- 보배드림 베스트 10/30 6편(parkseat, bumperall, carrotdeal, oring50, hiddencam, g90park)
  + 신차 tucson5, usedavante, gtimoss + 용품 antifreeze(데이터랩 12위 부동액).
- 근거 = work/research_1101.md. 실사 원본 = work/_photos/b1101/ (map.txt). 캡처는 _batch_1027.cap() 로 얼굴 모자이크.
- 실명, 상호, 번호판 없음. 캐릭터 없음(NO_CHAR). 제목, 대본에 '폭행' 단어 안 씀.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1024 import B, C, L, build, IR, Y, W, R, P   # noqa: E402,F401
from _batch_1027 import cap as _cap   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos", "b1101")
BB = "사진: 보배드림"
BV = "화면: 보배드림"
HY = "사진: 현대차"
ND = "사진: 뉴데일리"
SN = "사진: 스타뉴스"
COMMON = "자동차 블랙박스 2채널, 블랙박스 메모리카드, 비상삼각대, 차량용 핸드폰 거치대, 차량용 방향제"
MAXC = 360


def cap(*a, **k):
    k.setdefault("ph", PH)
    return _cap(*a, **k)


def px(slug, name, boxes):
    """cap() 결과(1080x960) 위 좌표로 추가 모자이크(번호판 등)."""
    import cv2
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import mosaic as M
    p = os.path.join(ROOT, "work", slug, "v2", "real", name + ".jpg")
    arr = cv2.imread(p)
    for b in boxes:
        M.pixelate(arr, *b, 14)
    cv2.imwrite(p, arr, [cv2.IMWRITE_JPEG_QUALITY, 92])


def go(S, lines, *rest):
    n = sum(len(l["text"]) for l in lines)
    assert 10 <= len(lines) <= 12, (S, len(lines))
    assert n <= MAXC, (S, "글자", n)
    for l in lines:
        assert "—" not in l["text"] and "·" not in l["text"], l["text"]
    build(S, lines, *rest)
    print(f"  chars {S} = {n} ({len(lines)}줄)")


# ───────────────────────── 1. 주차칸 맡던 자매 ─────────────────────────
def EP_parkseat():
    S = "parkseat"
    cap(S, "notice", "1044033_00.jpg", fit=True, nofaces=True,
        boxes=[(690, 405, 200, 55), (260, 150, 140, 55), (1100, 335, 440, 80)])
    cap(S, "noticec", "1044033_00.jpg", box=(950, 480, 1600, 640), fit=True, nofaces=True)
    lines = [
        L("여기 우리 자리예요, 차 빼세요!",
          [B("p01", "A Korean apartment underground parking garage, one empty parking space between cars, a woman seen only from behind standing in the empty space with arms spread, fluorescent light", s0=1.0, s1=1.2)],
          None, dialogue=True, speaker=3, emotion="toneup"),
        L("아파트 지하주차장 빈칸에 들어가려는데, 여자 한 명이 막아섬.",
          [B("p02", "View through a car windshield in a Korean apartment underground parking lot, a person's back blocking an empty parking spot, headlights on")],
          None, em=["막아섬"]),
        L("곧 다른 차에서 언니까지 내려 차 빼라고 고함침.",
          [B("p01", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], None, em=["고함침"], fx=[("wrong_gameshow_buzz", "고함침", 0.45)]),
        L("동생은 아예 글쓴이 차에 손목을 대고 버팀.",
          [B("p03", "Close-up of a woman's hand and wrist pressed flat on the front hood of a gray car in an underground parking garage, no face visible")],
          None, em=["손목을"]),
        L("잠깐 떨어진 틈에 주차했더니, 차로 손목을 쳤다며 경찰에 신고함.",
          [B("p03", at="신고함", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], None, em=["경찰에 신고함"], em_color="yellow",
          pop=("신고?!", R, "신고함"), shake="신고함", fx=[("hit_trailer_epic", "신고함", 0.5)]),
        L("한번 고생해 봐라, 죗값 한번 받아 봐라.",
          [B("p04", "An elderly man seen from behind standing in an apartment parking garage with hands behind his back, dim light, no face")],
          None, dialogue=True, speaker=2, emotion="angry"),
        L("자매 아버지까지 와서 이러며 웃었다고 함.",
          [B("p04", s0=1.2, s1=1.35, fx=0.5, fy=0.4)], None, em=["아버지까지"]),
        L("경찰은 그쪽 말만 듣고 글쓴이를 가해자로 검찰에 넘김.",
          [B("p05", "A Korean police station hallway with a desk and chairs, documents on the desk, no people, fluorescent light")],
          None, em=["가해자로"], em_color="yellow"),
        L("두 달을 시달린 끝에 검찰 통지서가 날아옴.",
          [P("notice", BB, s0=1.0, s1=1.15)], None, em=["검찰 통지서"], fx=[("notify_message_pop", "통지서가", 0.45)]),
        L("결과는 혐의없음, 증거불충분.",
          [P("noticec", BB, at="혐의없음", s0=1.0, s1=1.2, punch=True)], None, em=["혐의없음"], em_color="yellow",
          pop=("혐의없음!", Y, "혐의없음"), fx=[("drop_futuristic", "혐의없음", 0.5)]),
        L("댓글은 제대로 조사 안 한 경찰이 제일 문제라는 반응.",
          [P("notice", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, em=["경찰이"]),
        L("님들은 이럴 때 무고로 고소함, 그냥 넘어감?", [B("p02", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "무고로")]),
    ]
    go(S, lines, "주차칸 몸으로 맡던", "자매 신고 결말", "빈칸 맡던 자매, 차로 손목 쳤다며 신고 → 혐의없음",
       "#주차칸 맡던 자매 결말", "보배드림 베스트 1044033 자유게시판 (2026-10-30, 추천 1288, 댓글 154, 조회 65276)",
       [("빈칸에 서서 '우리 자리다', 다른 차에서 한 명 더 와서 고함", "원글 본문"),
        ("동생이 차에 손목 대고 버팀, 떨어진 틈에 주차하자 '손목을 쳤다' 경찰 신고", "원글 본문"),
        ("아버지 '당신은 한번 고생해봐라, 죄값을 한번 받아봐라'", "원글 본문(대사는 원문을 대사체로)"),
        ("경찰이 그쪽 말만 듣고 가해자로 검찰 송치, 두 달 시달림", "원글 본문"),
        ("검찰 결정 혐의없음(증거불충분), 결정일 2026-10-15", "첨부 피의사건 결정결과 통지서"),
        ("댓글 '경찰이 제일 문제'(342), '무고죄로 고발하세요'(25)", "원글 댓글")],
       "아파트 지하주차장 빈칸을 몸으로 맡던 자매가, 주차하자 차로 손목을 쳤다며 신고했습니다.\n글쓴이는 가해자로 검찰에 넘겨졌다가 두 달 만에 혐의없음 통지를 받았습니다.\n댓글은 제대로 조사하지 않은 경찰을 지적했습니다.\n\n#주차자리 #자리맡기 #혐의없음 #보배드림 #란빵",
       "님들은 이럴 때 무고로 고소함, 그냥 넘어감?", COMMON,
       "통지서 캡처의 이름, 사건번호 모자이크. 아파트 이름, 지역 안 씀.", [P("notice", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 2. 오토홀드 추돌, 범퍼 통째 교체 ─────────────────────────
def EP_bumperall():
    S = "bumperall"
    cap(S, "f2", "1044116_f2.jpg", nofaces=True, cx=0.4)
    cap(S, "f13", "1044116_f13.jpg", nofaces=True, cx=0.47)
    cap(S, "bumper", "1044116_01.jpg", nofaces=True)
    lines = [
        L("이 정도로 입원까지 한다고요?",
          [P("f13", BV, s0=1.0, s1=1.2)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("빨간불에 멈췄다가 잠깐 딴생각을 한 글쓴이.",
          [P("f2", BV, s0=1.0, s1=1.15)], None, em=["딴생각"]),
        L("오토홀드가 꺼져 있어서 차가 스르륵 앞으로 굴러감.",
          [B("b01", "Close-up of a car center console with an auto hold button, the indicator light off, driver hand resting nearby, dusk light, no readable text")],
          None, em=["오토홀드가"], em_color="yellow", fx=[("drum_rimshot", "굴러감", 0.45)]),
        L("결국 앞차를 쿵 박고 나서야 알아챔.",
          [P("f13", BV, at="쿵", s0=1.2, s1=1.45, fx=0.5, fy=0.6, punch=True)], None, em=["쿵"],
          pop=("쿵!", R, "쿵"), shake="박고", fx=[("glass_smash", "쿵", 0.45)]),
        L("과실 100대0은 인정, 근데 입원은 오버라며 거절함.",
          [P("f2", BV, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, say="과실 백 대 영은 인정, 근데 입원은 오버라며 거절함.", em=["거절함"]),
        L("상대가 경찰에 고소까지 하자 결국 대인 접수를 해 줌.",
          [B("b02", "A smartphone on a car seat showing an insurance company call screen, blurred, evening light, no readable text")],
          None, em=["고소까지"]),
        L("2주 뒤 보험사 연락, 입원은 안 하고 통원 치료만 했다고 함.",
          [B("b02", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], None, say="이주 뒤 보험사 연락, 입원은 안 하고 통원 치료만 했다고 함.", em=["통원 치료만"]),
        L("대신 범퍼를 통째로 갈았다며, 글쓴이는 지독하다고 분노함.",
          [P("bumper", BB, at="통째로", s0=1.0, s1=1.25, punch=True)], None, em=["통째로"], em_color="yellow",
          pop=("범퍼 교체?!", Y, "통째로"), fx=[("hit_trailer_epic", "통째로", 0.5)]),
        L("근데 댓글 반응은 정반대.",
          [P("f13", BV, s0=1.3, s1=1.5, fx=0.5, fy=0.55)], None, em=["정반대"], fx=[("wrong_gameshow_buzz", "정반대", 0.45)]),
        L("뒤에서 박았으면 그냥 조용히 계세요.",
          [P("bumper", BB, s0=1.2, s1=1.4, fx=0.5, fy=0.6)], None, dialogue=True, speaker=2, emotion="angry"),
        L("님들은 이 정도 추돌에 범퍼 교체, 과하다고 봄?", [P("f2", BV, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "과하다고")]),
    ]
    go(S, lines, "신호 대기 중 딴생각", "앞차 박고 억울?", "오토홀드 꺼진 채 앞차 추돌, 상대는 범퍼 통째 교체",
       "#박아놓고 억울?", "보배드림 베스트 1044116 교통사고/블박 (2026-10-30, 추천 682, 댓글 316) + accident 860813 (2026-10-15)",
       [("적색 정차 후 딴 데 정신 팔림, 오토홀드 꺼져 차가 진행해 앞차 추돌, 부딪히고서야 앎", "860813 본문, 블박 영상"),
        ("100% 과실 인정, 입원비는 거절 → 상대 경찰 고소 → 대인접수", "860813 본문"),
        ("2주 뒤 입원은 안 하고 통원치료만, 범퍼 통째 교체, '지독하네요'", "1044116 본문"),
        ("댓글 '뒷빵은 아닥'(190), '쿵인데 경미라고 하기엔'(136)", "1044116 댓글(대사는 댓글 요지를 대사체로)")],
       "신호 대기 중 오토홀드가 꺼진 줄 모르고 앞차를 추돌한 글쓴이.\n상대는 통원 치료를 받고 범퍼를 통째로 교체했습니다.\n지독하다는 글쓴이와 달리 댓글은 가해자가 할 말이 아니라는 반응이었습니다.\n\n#추돌사고 #오토홀드 #범퍼교체 #보배드림 #란빵",
       "님들은 이 정도 추돌에 범퍼 교체, 과하다고 봄?",
       "자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 핸드폰 거치대, 비상삼각대, 차량용 방향제",
       "블박 정지 프레임 번호판은 원글이 가린 상태 그대로.", [P("f13", BV, s0=1.0, s1=1.1)])


# ───────────────────────── 3. 당근 딜러 계약금 30만원 ─────────────────────────
def EP_carrotdeal():
    S = "carrotdeal"
    cap(S, "msg30", "1044199_00.jpg", box=(0, 1150, 1290, 2100), fit=True, nofaces=True)
    cap(S, "msglaw", "1044199_01.jpg", box=(0, 60, 1290, 1500), fit=True, nofaces=True)
    lines = [
        L("30만원 안 보내시면 민사 진행하겠습니다.",
          [P("msg30", BB, s0=1.0, s1=1.2)], None, say="삼십마넌 안 보내시면 민사 진행하겠습니다.", dialogue=True, speaker=2, emotion="angry"),
        L("중고 거래 앱에 내 차를 올렸더니 인증 딜러가 연락해 옴.",
          [B("c01", "A hand holding a smartphone showing a used car listing app with a car photo, in a parked car, blurred UI, no readable text")],
          None, em=["인증 딜러가"]),
        L("차도 안 보고 계약금부터 걸겠다며 10만원을 입금함.",
          [B("c02", "Smartphone screen showing a bank transfer notification, blurred, on a car dashboard, no readable text")],
          None, say="차도 안 보고 계약금부터 걸겠다며 십마넌을 입금함.", em=["차도 안 보고"]),
        L("계약서도, 잔금 날짜도 정한 게 하나도 없었음.",
          [B("c03", "An empty blank contract form and a pen on a car hood, daylight, no readable text")], None, em=["하나도"]),
        L("그 사이 차를 보고 간 사람이 바로 사겠다고 함.",
          [B("c04", "A man seen from behind looking at a used silver sedan parked in a Korean apartment lot, daylight, no face")], None, em=["바로 사겠다고"]),
        L("글쓴이는 10만원 바로 돌려줄 테니 계좌를 달라고 함.",
          [B("c02", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], None, say="글쓴이는 십마넌 바로 돌려줄 테니 계좌를 달라고 함.", em=["바로 돌려줄"]),
        L("그러자 딜러는 4배 배상이라며 30만원을 요구함.",
          [P("msg30", BB, at="30만원을", s0=1.2, s1=1.45, fx=0.5, fy=0.7, punch=True)], None,
          say="그러자 딜러는 네 배 배상이라며 삼십마넌을 요구함.", em=["30만원을"], em_color="yellow",
          pop=("30만원?!", R, "30만원을"), shake="요구함", fx=[("hit_trailer_epic", "30만원을", 0.5)]),
        L("법무팀이 등록증 인적 사항으로 소송 걸겠다는 문자까지 옴.",
          [P("msglaw", BB, s0=1.0, s1=1.15)], None, em=["법무팀이"], fx=[("drum_rimshot", "법무팀이", 0.45)]),
        L("근데 민법을 보면, 계약금 받은 쪽은 두 배를 돌려주고 해제할 수 있음.",
          [B("c05", "An open Korean law book on a desk next to car keys and a 50000 won bill, warm light, pages blurred, no readable text")],
          None, em=["두 배를"], em_color="yellow", fx=[("drop_futuristic", "두", 0.5)],
          info={"kind": "compare", "at": "계약금", "title": "계약금 10만원 받았다면",
                "items": [{"label": "딜러 요구", "color": "#fff", "at": "계약금", "rows": [["돌려줄 돈", "30만원", "#FF3B30"]]},
                          {"label": "민법 565조", "color": "#FBFF56", "at": "두", "rows": [["배액", "20만원", "#7CFF6B"]]}]}),
        L("댓글도 20만원 물어주고 끝내라는 쪽이 대부분.",
          [P("msglaw", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.4)], None, say="댓글도 이십마넌 물어주고 끝내라는 쪽이 대부분.", em=["대부분"]),
        L("님들은 계약금 받았다가 취소하면 얼마 돌려줌?", [B("c04", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "얼마")]),
    ]
    go(S, lines, "계약금 10만원 걸고", "30만원 내놓으라는 딜러", "직거래 취소하자 딜러 '30만원, 안 주면 민사'",
       "#계약금 3배 요구", "보배드림 베스트 1044199 자유게시판 (2026-10-30, 추천 364, 댓글 49, 조회 17347)",
       [("당근 개인 매물, 인증 딜러가 차 안 보고 계약금 10만원 입금, 계약서, 잔금 기한 없음", "원글 본문"),
        ("앞서 보러 온 사람이 당장 구매 → 10만원 전액 환불 제안", "원글 본문"),
        ("딜러 '계약취소시 4배', '30만원 안 보내주시면 법무팀 통해 등록증 인적 사항으로 민사'", "첨부 문자 캡처(대사는 문자 원문 요약)"),
        ("계약금 수령자는 이행 착수 전까지 배액 상환으로 해제 가능", "민법 565조 1항(casenote 원문)"),
        ("댓글 '20만원 물어주고 치우세요'(56), '계약금 10만 위약금 10만 합 20만'(55)", "원글 댓글")],
       "중고차 직거래에서 딜러가 차도 보지 않고 계약금 10만원을 보냈습니다.\n글쓴이가 취소하자 딜러는 4배 배상이라며 30만원과 민사 소송을 언급했습니다.\n민법 565조는 계약금을 받은 쪽이 배액을 돌려주고 해제할 수 있다고 정합니다.\n\n#중고차직거래 #계약금 #배액배상 #보배드림 #란빵",
       "님들은 계약금 받았다가 취소하면 얼마 돌려줌?",
       "차량용 방향제, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 자동차 발매트, 차량용 무선충전기",
       "문자 캡처에 이름, 번호 없음. 딜러 상호, 앱 이름 대본에 안 씀(설명란 '직거래').", [P("msg30", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 4. 엔진오일 오링 누락 ─────────────────────────
def EP_oring50():
    S = "oring50"
    lines = [
        L("엔진에서 쇠 갈리는 소리가 나요.",
          [B("o01", "A car engine bay with the hood open in a small Korean auto repair shop, oil filter area visible, mechanic hands with gloves, no face")],
          None, dialogue=True, speaker=3, emotion="toneup"),
        L("카센터에서 엔진오일을 간 지 이틀 뒤, 고속도로에서 이상한 소리가 남.",
          [B("o02", "View from the driver seat of a sedan on a Korean expressway at dusk, dashboard and steering wheel, no people visible")],
          None, em=["이틀 뒤"]),
        L("다음 날엔 노란 엔진 경고등까지 뜸.",
          [B("o03", "Close-up of a car instrument cluster with a yellow check engine warning light glowing, night, no readable text")],
          None, em=["엔진 경고등까지"], em_color="yellow", fx=[("wrong_gameshow_buzz", "경고등까지", 0.45)]),
        L("다시 찾아가 보니, 교환할 때 오링을 안 끼웠던 것.",
          [B("o04", "Close-up of a car oil filter and a small black rubber o-ring lying separately on a greasy workbench, shop light")],
          None, em=["오링을"], em_color="yellow", pop=("오링 누락!", R, "오링을"), shake="끼웠던", fx=[("hit_trailer_epic", "오링을", 0.5)]),
        L("카센터 사장님도 직접 인정함.",
          [B("o01", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], None, em=["직접 인정함"]),
        L("그 상태로 달린 거리만 약 50km.",
          [B("o05", "Oil drips on the concrete floor under a parked sedan in a garage, close-up, daylight")],
          None, say="그 상태로 달린 거리만 약 오십킬로.", em=["50km"], pop=("50km!", Y, "50km"), fx=[("drop_futuristic", "50km", 0.5)]),
        L("다시 끼우고 오일을 새로 넣자 소리는 사라졌는데, 탄 냄새가 조금 남.",
          [B("o06", "A mechanic's gloved hand pouring new engine oil into a car engine through a funnel, close-up, no face")],
          None, em=["탄 냄새가"]),
        L("글쓴이는 한 달 지켜보고 문제 생기면 책임져 달라고 문자를 남김.",
          [B("o07", "A smartphone on a car seat with a long text message being typed, blurred, no readable text")], None, em=["책임져 달라고"]),
        L("예약 내역, 누유 사진, 경고등 사진까지 증거도 챙겨 둠.",
          [B("o03", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], None, em=["증거도"], fx=[("notify_message_pop", "증거도", 0.45)]),
        L("댓글은 이미 손상됐을 수 있다는 걱정과 괜찮을 거란 의견으로 갈림.",
          [B("o02", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, em=["갈림"]),
        L("님들은 이러면 카센터에 어디까지 요구함?", [B("o04", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "어디까지")]),
    ]
    go(S, lines, "엔진오일 갈고 이틀 뒤", "엔진에서 쇳소리", "오링 빠진 채 약 50km 주행, 카센터 사장 인정",
       "#엔진오일 갈고 쇳소리", "보배드림 베스트 1044187 자유게시판 (2026-10-30, 추천 343, 댓글 46, 조회 9910)",
       [("이틀 전 엔진오일 교환, 다음 날 고속 이상한 소리, 그다음 날 노란 경고등", "원글 본문"),
        ("교환 때 오링 장착 안 함, 사장 직접 인정, 그 상태로 약 50km", "원글 본문"),
        ("재장착, 재교환 후 소음 사라짐, 약간의 탄 냄새", "원글 본문"),
        ("한 달 지켜보고 문제 시 책임 요청 문자, 사장 '알겠다'", "원글 본문"),
        ("예약내역, 누유흔적 사진, 카톡, 경고등 사진 확보", "글쓴이 댓글"),
        ("댓글 '이미 엔진 손상 입은 거 같다' vs '보통은 괜찮다'", "원글 댓글"),
        ("대사 '쇠 갈리는 소리' 는 본문 묘사를 대사체로", "제작 메모")],
       "엔진오일 교환 이틀 뒤 엔진에서 쇳소리와 경고등이 떴습니다.\n교환할 때 오링을 끼우지 않은 채 약 50km를 달렸고 카센터도 인정했습니다.\n글쓴이는 증거를 챙기고 한 달간 상태를 지켜보기로 했습니다.\n\n#엔진오일 #오링 #카센터 #보배드림 #란빵",
       "님들은 이러면 카센터에 어디까지 요구함?",
       "엔진오일 5W30, 엔진오일 교환 세트, 엔진세정제, 자동차 블랙박스 2채널, 차량용 방향제",
       "원글 첨부 사진 없음, 전부 AI 배경. 카센터 상호, 지역 안 씀.", [B("o06", s0=1.0, s1=1.1)])


# ───────────────────────── 5. 화단 속 단속 카메라 ─────────────────────────
def EP_hiddencam():
    S = "hiddencam"
    cap(S, "cam0", "1044180_00.jpg", nofaces=True, cx=0.5)
    cap(S, "cam1", "1044180_01.jpg", nofaces=True, cx=0.5)
    lines = [
        L("여기 어디 있는지 찾아보세요.",
          [P("cam1", BB, s0=1.0, s1=1.2)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("대구의 한 큰길, 지하도 위 화단에 과속 카메라가 숨어 있었다는 글.",
          [P("cam0", BB, s0=1.0, s1=1.15)], None, em=["숨어 있었다는"]),
        L("소나무 사이에 이동식 단속 장비를 감춰 둔 모습.",
          [P("cam1", BB, at="감춰", s0=1.2, s1=1.5, fx=0.45, fy=0.45, punch=True)], None, em=["감춰 둔"], em_color="yellow",
          pop=("숨은 카메라!", Y, "감춰"), fx=[("hit_trailer_epic", "감춰", 0.5)]),
        L("글쓴이는 사고 예방이 아니라 실적용 단속 같다고 주장함.",
          [B("h01", "A portable speed camera on a tripod hidden among pine trees and shrubs on a roadside median in Korea, sunny autumn day, no people")],
          None, em=["실적용 단속"]),
        L("이 글은 추천 336개를 받으며 베스트에 오름.",
          [P("cam0", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, say="이 글은 추천 삼백삼십육 개를 받으며 베스트에 오름.", em=["336개를"],
          info={"kind": "counter", "at": "추천", "title": "보배드림 추천", "items": [{"num": 336, "suffix": "개"}]}),
        L("댓글 1위는 단속 구간이 맞는지 소명 민원을 넣으라는 조언.",
          [B("h02", "A hand typing a complaint form on a smartphone in a car, blurred screen, no readable text")],
          None, say="댓글 일위는 단속 구간이 맞는지 소명 민원을 넣으라는 조언.", em=["소명 민원을"], fx=[("notify_message_pop", "민원을", 0.45)]),
        L("과속을 안 하면 되는 거 아님?",
          [B("h03", "A car speedometer needle steady at 60 km/h on a sunny Korean city road, dashboard close-up, no people")],
          None, dialogue=True, speaker=2, emotion="normal"),
        L("반대로 이렇게 정속 주행하면 그만이라는 댓글도 이어짐.",
          [B("h03", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], None, em=["정속 주행하면"], fx=[("drum_rimshot", "그만이라는", 0.45)]),
        L("현지인 댓글은 그 동네 밤마다 쏘는 차가 많아 그럴 만하다는 반응.",
          [B("h04", "A wide Korean city boulevard at night with light trails of speeding cars, overpass, no people")],
          None, em=["밤마다 쏘는 차가"]),
        L("숨긴 단속이 함정이냐 예방이냐로 의견이 갈림.",
          [P("cam1", BB, s0=1.1, s1=1.25)], None, em=["함정이냐 예방이냐"], em_color="yellow"),
        L("님들은 숨겨 둔 단속 카메라, 괜찮다고 봄?", [P("cam0", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "괜찮다고")]),
    ]
    go(S, lines, "지하도 위 화단에", "숨어 있던 카메라", "도로 화단 속 이동식 과속 단속, 함정 vs 예방",
       "#화단 속 단속카메라", "보배드림 베스트 1044180 자유게시판 (2026-10-30, 추천 336, 댓글 38, 조회 10240)",
       [("대구 월드컵대로 지하도 위 화단에 숨겨 설치, 사고 예방 아닌 실적 목적 주장", "원글 본문, 첨부 사진"),
        ("댓글 1위 '이동식 단속구간인지 소명 요구 민원 넣으세요'(49)", "원글 댓글(법 판단은 안 함)"),
        ("'과속을 안 하면 되는 거 아님?', '정속주행하시면 되잖아요?'", "원글 댓글(대사는 댓글 원문)"),
        ("'그 동네는 낮이며 밤이며 쏘는 애들이 많아서 저래도 돼요'", "원글 댓글(현지인)")],
       "도로 화단 소나무 사이에 이동식 과속 카메라가 숨어 있었다는 글이 베스트에 올랐습니다.\n실적용 단속이라는 주장과 과속만 안 하면 된다는 반응이 맞섰습니다.\n숨긴 단속, 함정인지 예방인지 의견이 갈립니다.\n\n#과속단속 #단속카메라 #이동식단속 #보배드림 #란빵",
       "님들은 숨겨 둔 단속 카메라, 괜찮다고 봄?",
       "자동차 블랙박스 2채널, 헤드업디스플레이, 차량용 핸드폰 거치대, 블랙박스 메모리카드, 차량용 방향제",
       "원글 사진은 화단, 나무만 있음(사람, 번호판 없음).", [P("cam1", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 6. 과태료 와도 또 주차 G90 ─────────────────────────
def EP_g90park():
    S = "g90park"
    for k in range(4):
        cap(S, f"g{k}", f"1044113_0{k}.jpg", fit=True, nofaces=True)
    lines = [
        L("과태료 날아갔다는데 또 댔네?",
          [P("g3", BB, s0=1.0, s1=1.2)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("검은 제네시스 G90 한 대가 같은 자리에 또 불법주차를 함.",
          [P("g2", BB, s0=1.0, s1=1.15)], None, say="검은 제네시스 지구공 한 대가 같은 자리에 또 불법주차를 함.", em=["같은 자리에"]),
        L("글쓴이는 이미 신고했고, 과태료도 날아갔다고 함.",
          [B("g01", "A parking violation notice envelope on a car dashboard, close-up, blurred, no readable text")], None, em=["과태료도"]),
        L("그런데도 다음 날 또 그 자리.",
          [P("g0", BB, s0=1.0, s1=1.2)], None, em=["또 그 자리"], em_color="yellow", fx=[("drum_rimshot", "또", 0.45)]),
        L("글쓴이는 이번이 다섯 번째 기념샷이라며 또 찍음.",
          [P("g1", BB, at="다섯", s0=1.1, s1=1.35, punch=True)], None, em=["다섯 번째"], em_color="yellow",
          pop=("5번째!", R, "다섯"), shake="찍음", fx=[("hit_trailer_epic", "다섯", 0.5)]),
        L("해 보입시다, 누가 이기나.",
          [P("g1", BB, s0=1.2, s1=1.4, fx=0.5, fy=0.5)],
          None, say="한번 해 봅시다. 누가 이기나 봅시다.", dialogue=True, speaker=2, emotion="angry"),
        L("댓글은 주소지가 달라 모를 수도 있으니 계속 쌓아 주라는 반응.",
          [P("g2", BB, s0=1.2, s1=1.4, fx=0.4, fy=0.5)], None, em=["계속 쌓아"]),
        L("연간 마일리지처럼 차곡차곡 쌓으라는 말까지 나옴.",
          [P("g3", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, em=["마일리지처럼"], fx=[("count_counter", "마일리지처럼", 0.45)]),
        L("국가 세수에 기여하는 애국자라는 비꼼도 붙음.",
          [B("g03", "Korean won banknotes and coins on a dark car seat, close-up, evening light")], None, em=["애국자라는"]),
        L("다른 회원은 그 차 아직도 거기 댄다고 증언함.",
          [P("g0", BB, s0=1.2, s1=1.4, fx=0.5, fy=0.5)], None, em=["아직도"]),
        L("님들은 이 대결, 누가 이길 것 같음?", [P("g1", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "누가")]),
    ]
    go(S, lines, "과태료 날아갔는데도", "또 그 자리 G90", "같은 자리 불법주차, 신고 기념샷 5번째",
       "#과태료 와도 또 주차", "보배드림 베스트 1044113 교통사고/블박 (2026-10-30, 추천 67, 댓글 12, 조회 7460)",
       [("과태료 날아갔다는데도 계속 주차, '해보입시다 5번째 기념샷'", "원글 본문(대사는 원문을 대사체로)"),
        ("검은 G90 같은 자리 주차 사진 4장", "첨부 사진(번호판 안 보임)"),
        ("'주소지가 달라서 모를 수도, 연간 마일리지처럼'(11), '애국자네 국가 세수', '아직도 거기 대고 있답니다'", "원글 댓글")],
       "과태료가 날아갔다는데도 같은 자리에 또 주차한 검은 G90.\n글쓴이는 다섯 번째 기념샷을 찍으며 누가 이기나 해보자고 했습니다.\n댓글은 마일리지처럼 계속 쌓으라는 반응이었습니다.\n\n#불법주차 #과태료 #제네시스 #보배드림 #란빵",
       "님들은 이 대결, 누가 이길 것 같음?",
       "주차번호판, 자동차 블랙박스 2채널, 문콕방지가드, 차량용 방향제, 차량용 핸드폰 거치대",
       "첨부 사진에 번호판 안 보임. 과태료 금액은 확인 안 해 안 씀.", [P("g2", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 7. 신형 투싼 첫날 1만5045대 ─────────────────────────
def EP_tucson5():
    S = "tucson5"
    cap(S, "two", "tuc_1.jpg", nofaces=True, cx=0.4)
    cap(S, "twofit", "tuc_1.jpg", nofaces=True, fit=True)
    cap(S, "inside", "tuc_0.jpg", nofaces=True, cx=0.45)
    cap(S, "tunnel", "tuc_2.jpg", nofaces=True, cy=0.55)
    cap(S, "road", "tuc_3.jpg", nofaces=True, cx=0.45)
    px(S, "road", [(192, 515, 116, 38), (838, 505, 85, 32)])
    px(S, "tunnel", [(532, 532, 96, 34)])
    lines = [
        L("와, 투싼 앞모습이 완전 딴 차네?",
          [P("two", HY, s0=1.0, s1=1.2)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("6년 만에 완전히 바뀐 5세대 투싼, 계약 첫날 1만5045대가 몰림.",
          [P("twofit", HY, s0=1.0, s1=1.15), P("two", HY, at="1만5045대가", s0=1.2, s1=1.4, fx=0.4, fy=0.5, punch=True)],
          None, say="육년 만에 완전히 바뀐 오세대 투싼, 계약 첫날 만오천사십오대가 몰림.", em=["1만5045대가"], em_color="yellow",
          pop=("1만5045대!", Y, "1만5045대가"), fx=[("drop_futuristic", "1만5045대가", 0.5)]),
        L("4세대 첫날 1만842대보다 약 39% 많은 역대 최다.",
          [P("road", HY, s0=1.0, s1=1.15)], None, say="사세대 첫날 만팔백사십이대보다 약 삼십구퍼센트 많은 역대 최다.", em=["역대 최다"],
          info={"kind": "bars", "at": "4세대", "title": "투싼 계약 첫날", "items": [
              {"label": "4세대(2020)", "num": 10842, "suffix": "대", "at": "4세대"},
              {"label": "5세대", "num": 15045, "suffix": "대", "at": "4세대", "flash": "역대"}]}),
        L("가격은 가솔린 3140만원, 하이브리드 3615만원부터.",
          [P("tunnel", HY, s0=1.0, s1=1.2)], None, say="가격은 가솔린 삼천백사십마넌, 하이브리드 삼천육백십오마넌부터.", em=["3140만원"],
          fx=[("cash_register_fake", "3140만원", 0.45)]),
        L("차체는 길이 6cm, 폭 4cm 커졌고 트렁크는 645리터.",
          [P("twofit", HY, s0=1.2, s1=1.35)], None, say="차체는 길이 육센티, 폭 사센티 커졌고 트렁크는 육백사십오리터.", em=["645리터"]),
        L("주 전원이 나가도 문이 열리게 예비 전원을 넣은 건 현대차 최초.",
          [P("inside", HY, s0=1.0, s1=1.2)], None, em=["현대차 최초"], em_color="yellow"),
        L("근데 계약자 44%가 제일 비싼 인스퍼레이션을 고름.",
          [P("inside", HY, at="44%가", s0=1.3, s1=1.5, fx=0.55, fy=0.4, punch=True)], None,
          say="근데 계약자 사십사퍼센트가 제일 비싼 인스퍼레이션을 고름.", em=["44%가"], em_color="yellow",
          pop=("44%!", R, "44%가"), shake="고름", fx=[("hit_trailer_epic", "44%가", 0.5)]),
        L("하이브리드 비중도 55%로 가솔린을 앞섬.",
          [P("road", HY, s0=1.2, s1=1.4, fx=0.5, fy=0.5)], None, say="하이브리드 비중도 오십오퍼센트로 가솔린을 앞섬.", em=["55%로"]),
        L("최상위 하이브리드는 4270만원까지 올라감.",
          [P("tunnel", HY, s0=1.2, s1=1.35, fx=0.5, fy=0.6)], None, say="최상위 하이브리드는 사천이백칠십마넌까지 올라감.", em=["4270만원까지"],
          fx=[("wrong_gameshow_buzz", "4270만원까지", 0.45)]),
        L("님들은 투싼 산다면 기본형이랑 풀옵션 중 뭐 고름?", [P("two", HY, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "뭐")]),
    ]
    go(S, lines, "6년 만에 바뀐 투싼", "첫날 1만5045대", "디 올 뉴 투싼 계약 첫날 역대 최다",
       "#투싼 첫날 1만5045대", "현대차 디 올 뉴 투싼 10/21 계약 개시, 10/22 첫날 계약 (연합뉴스 AKR20261021036600003, 한국경제 202610214878g, 뉴스1 6328315, 신아일보 5075123)",
       [("5세대 완전변경, 6년 만", "연합뉴스, 한국경제"),
        ("계약 첫날 1만5045대, 4세대 첫날 1만842대 대비 약 38.8% 증가, 역대 최다", "뉴스1, 신아일보"),
        ("가솔린 3140만~3790만원, 하이브리드 3615만~4270만원(세제 혜택)", "연합뉴스, 한국경제"),
        ("전장 +60mm, 전폭 +40mm, 트렁크 645L, 도어 언락 전원 이중화 현대차 최초", "연합뉴스"),
        ("인스퍼레이션 비중 29%→44%, 하이브리드 48%→55%", "신아일보, 뉴스1"),
        ("대사 '앞모습이 완전 딴 차네' 는 구경꾼 반응(신차 대본 구조 1번)", "제작 메모")],
       "현대차 5세대 디 올 뉴 투싼이 계약 첫날 1만5045대로 역대 투싼 최다 기록을 세웠습니다.\n가격은 가솔린 3140만원, 하이브리드 3615만원부터입니다.\n계약자 44%가 최상위 인스퍼레이션을 골랐습니다.\n\n#투싼 #신형투싼 #현대차 #신차 #란빵",
       "님들은 투싼 산다면 기본형이랑 풀옵션 중 뭐 고름?",
       "투싼 발매트, 차량용 무선충전기, 차량용 핸드폰 거치대, 자동차 블랙박스 2채널, 트렁크정리함",
       "사진 = 현대차그룹 제공 보도사진(한국경제 게재). AI 생성 없음.", [P("twofit", HY, s0=1.0, s1=1.1)])


# ───────────────────────── 8. 중고 아반떼 시세 상승 ─────────────────────────
def EP_usedavante():
    S = "usedavante"
    cap(S, "new", "av_0.jpg", nofaces=True, cx=0.45)
    cap(S, "old", "av_1.jpg", nofaces=True, cx=0.5)
    cap(S, "newfit", "av_0.jpg", nofaces=True, fit=True)
    px(S, "new", [(130, 550, 220, 70)])
    px(S, "newfit", [(185, 530, 165, 52)])
    lines = [
        L("중고 아반떼가 왜 더 비싸졌지?",
          [B("u01", "A used car dealership lot in Korea with rows of compact sedans, price boards blurred, overcast day, no people")],
          None, dialogue=True, speaker=3, emotion="toneup"),
        L("중고차 값이 줄줄이 떨어진 10월, 아반떼만 거꾸로 오름.",
          [P("old", HY, s0=1.0, s1=1.15)], None, say="중고차 값이 줄줄이 떨어진 시월, 아반떼만 거꾸로 오름.", em=["거꾸로 오름"], em_color="yellow",
          fx=[("drum_rimshot", "거꾸로", 0.45)]),
        L("국산 중고 평균은 1.1%, 수입차는 1.7% 내려감.",
          [B("u01", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, say="국산 중고 평균은 일점일퍼센트, 수입차는 일점칠퍼센트 내려감.", em=["내려감"],
          info={"kind": "bars", "at": "국산", "title": "10월 중고차 시세", "items": [
              {"label": "국산 평균 하락", "num": 1.1, "dec": 1, "suffix": "%", "at": "국산"},
              {"label": "수입 평균 하락", "num": 1.7, "dec": 1, "suffix": "%", "at": "국산"}]}),
        L("근데 2020년 나온 7세대 아반떼는 한 달 새 37만원 올라 1503만원.",
          [P("old", HY, at="37만원", s0=1.2, s1=1.4, fx=0.5, fy=0.55, punch=True)], None,
          say="근데 이천이십년 나온 칠세대 아반떼는 한 달 새 삼십칠마넌 올라 천오백삼마넌.", em=["37만원"], em_color="yellow",
          pop=("+37만원!", R, "37만원"), fx=[("drop_futuristic", "37만원", 0.5)]),
        L("2023년식 더 뉴 아반떼도 평균 2천만원을 찍음.",
          [P("newfit", HY, s0=1.0, s1=1.15)], None, say="이천이십삼년식 더 뉴 아반떼도 평균 이천마넌을 찍음.", em=["2천만원을"]),
        L("이유는 8월에 나온 신형 아반떼 값.",
          [B("u03", s0=1.1, s1=1.3, fx=0.5, fy=0.5)], None, say="이유는 팔월에 나온 신형 아반떼 값.", em=["신형 아반떼 값"]),
        L("시작 가격이 2398만원, 이전보다 336만원 올랐음.",
          [B("u01", at="336만원", s0=1.2, s1=1.4, fx=0.5, fy=0.5, punch=True)], None,
          say="시작 가격이 이천삼백구십팔마넌, 이전보다 삼백삼십육마넌 올랐음.", em=["336만원"], shake="올랐음",
          fx=[("hit_trailer_epic", "336만원", 0.5)],
          info={"kind": "compare", "at": "시작", "title": "아반떼 시작 가격",
                "items": [{"label": "이전 모델", "color": "#fff", "at": "시작", "rows": [["시작가", "2062만원"]]},
                          {"label": "신형", "color": "#FBFF56", "at": "336만원", "rows": [["시작가", "2398만원", "#FF3B30"]]}]}),
        L("신차가 비싸지자 이전 세대 중고로 눈을 돌린 것.",
          [B("u02", "A young person seen from behind looking at a used compact sedan at a Korean used car lot, daylight, no face")],
          None, em=["중고로"]),
        L("그 돈이면 차라리 중고 중형차 사지.",
          [B("u02", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], None, dialogue=True, speaker=2, emotion="normal"),
        L("실제로 같은 예산의 중고 중형 세단도 관심이 커졌다는 분석.",
          [B("u03", "Several used midsize sedans parked in a row at a Korean used car market, price signs blurred, overcast day, no people")],
          None, em=["중고 중형 세단도"]),
        L("님들은 첫차로 신형 아반떼, 중고 아반떼 중 뭐 고름?", [P("newfit", HY, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "뭐")]),
    ]
    go(S, lines, "중고차 값 다 떨어지는데", "아반떼만 올랐다", "10월 시세, 7세대 아반떼 한 달 새 37만원 상승",
       "#중고 아반떼 값 올랐다", "케이카 10월 중고차 시세 (한겨레 1284858, 한국경제 202610304903g)",
       [("국산 중고 평균 -1.1%, 수입 -1.7%", "한겨레, 한국경제"),
        ("7세대 아반떼(2020) 1466만→1503만원, +37만원(2.5%)", "한겨레, 한국경제"),
        ("더 뉴 아반떼(2023) 1995만→2000만원", "한겨레"),
        ("8월 출시 신형 시작가 2398만원, 이전 2062만원 대비 +336만원", "한겨레, 한국경제"),
        ("같은 예산 중고 중형 세단 관심", "한국경제(대사는 가상 구매자 반응)")],
       "중고차 시세가 전반적으로 떨어진 10월, 이전 세대 아반떼 시세는 거꾸로 올랐습니다.\n7세대 아반떼는 한 달 새 37만원 올라 평균 1503만원입니다.\n신형 아반떼 시작 가격이 336만원 오른 영향이라는 분석입니다.\n\n#아반떼 #중고차시세 #중고차 #신차 #란빵",
       "님들은 첫차로 신형 아반떼, 중고 아반떼 중 뭐 고름?",
       "아반떼 발매트, 차량용 방향제, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용청소기",
       "사진 = 현대차 제공 보도사진(한겨레, 한국경제 게재), 번호판 모자이크. 중고차 매장 장면은 AI 배경.", [P("old", HY, s0=1.0, s1=1.1)])


# ───────────────────────── 9. 골프 GTI 다크 모스 100대 ─────────────────────────
def EP_gtimoss():
    S = "gtimoss"
    cap(S, "front", "gti_0.jpg", box=(0, 0, 800, 420), nofaces=True, cx=0.55)
    cap(S, "frontfit", "gti_0.jpg", box=(0, 0, 800, 420), fit=True)
    cap(S, "rear", "gti_5.jpg", box=(0, 0, 800, 420), nofaces=True, cx=0.5)
    cap(S, "badge", "gti_6.jpg", box=(0, 0, 800, 470), nofaces=True, cx=0.45)
    cap(S, "inside", "gti_1.jpg", box=(0, 0, 800, 470), nofaces=True, cx=0.5)
    cap(S, "top", "gtis_1.jpg", box=(0, 0, 1200, 760), cx=0.5)
    lines = [
        L("와, GTI가 빨간색 대신 초록색이네?",
          [P("front", ND, s0=1.0, s1=1.2)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("폭스바겐이 GTI 탄생 50주년 한정판을 한국에 딱 100대만 냄.",
          [P("frontfit", ND, s0=1.0, s1=1.15), P("badge", ND, at="100대만", s0=1.1, s1=1.3, punch=True)],
          None, say="폭스바겐이 지티아이 탄생 오십주년 한정판을 한국에 딱 백대만 냄.", em=["100대만"], em_color="yellow",
          pop=("100대 한정!", Y, "100대만"), fx=[("drop_futuristic", "100대만", 0.5)]),
        L("이름은 골프 GTI 다크 모스 리미티드 에디션.",
          [P("badge", ND, s0=1.1, s1=1.25)], None, say="이름은 골프 지티아이 다크 모스 리미티드 에디션.", em=["다크 모스"]),
        L("GTI 상징이던 빨강 대신, 짙은 숲색 다크 모스 그린을 입음.",
          [P("top", SN, s0=1.0, s1=1.15)], None, say="지티아이 상징이던 빨강 대신, 짙은 숲색 다크 모스 그린을 입음.", em=["다크 모스 그린을"], em_color="yellow"),
        L("지붕과 미러는 블랙, 바닥엔 GTI 로고가 빛나는 매트까지 깜.",
          [P("inside", ND, s0=1.0, s1=1.2)], None, say="지붕과 미러는 블랙, 바닥엔 지티아이 로고가 빛나는 매트까지 깜.", em=["빛나는 매트"]),
        L("엔진은 245마력에 7단 DSG.",
          [P("rear", ND, s0=1.0, s1=1.15)], None, say="엔진은 이백사십오마력에 칠단 디에스지.", em=["245마력에"],
          info={"kind": "bars", "at": "엔진은", "title": "다크 모스 에디션", "items": [
              {"label": "최고출력", "num": 245, "suffix": "마력", "at": "엔진은"},
              {"label": "최대토크", "num": 37.7, "dec": 1, "suffix": "kg.m", "at": "엔진은"}]}),
        L("차마다 고유 번호가 새겨진 한정판 플레이트도 줌.",
          [P("badge", ND, at="고유", s0=1.3, s1=1.5, fx=0.5, fy=0.7, punch=True)], None, em=["고유 번호가"], fx=[("notify_message_pop", "플레이트도", 0.45)]),
        L("근데 가격은 5425만원.",
          [P("front", ND, s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], None, say="근데 가격은 오천사백이십오마넌.", em=["5425만원"], em_color="yellow",
          pop=("5425만원!", R, "5425만원"), shake="5425만원", fx=[("hit_trailer_epic", "5425만원", 0.5)]),
        L("대신 5년 15만km 무상 보증에, 첫 1년 사고 수리 자기부담금도 지원함.",
          [P("rear", ND, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None,
          say="대신 오년 십오만킬로 무상 보증에, 첫 일년 사고 수리 자기부담금도 지원함.", em=["자기부담금도"]),
        L("출시는 11월, 100대가 끝이면 끝임.",
          [P("top", SN, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, say="출시는 십일월, 백대가 끝이면 끝임.", em=["끝이면 끝임"]),
        L("님들은 이 색 하나에 5425만원, 살 거임?", [P("frontfit", ND, s0=1.0, s1=1.1)], None,
          say="님들은 이 색 하나에 오천사백이십오마넌, 살 거임?", fx=[("pop_bubble", "살")]),
    ]
    go(S, lines, "GTI 50주년 기념", "한국에 딱 100대", "골프 GTI 다크 모스 리미티드 에디션, 11월 100대 한정",
       "#딱 100대 GTI", "폭스바겐코리아 2026-10-28 사전계약 (스타뉴스 2026102814141630110, 신아일보 5075123, 뉴시스 NISX20261026_0003841861, 프라임경제 752659)",
       [("GTI 50주년 기념 다크 모스 리미티드 에디션, 11월 국내 100대 한정", "스타뉴스, 신아일보, 프라임경제"),
        ("GTI 상징 레드 대신 다크 모스 그린, 블랙 루프, 미러, 일루미네이티드 플로어 매트", "스타뉴스, 뉴시스"),
        ("2.0 TSI, 7단 DSG, 245마력, 37.7kg.m", "스타뉴스"),
        ("5425만원, 고유 번호 한정판 플레이트, 5년/15만km 보증, 첫 1년 사고 수리 자기부담금 지원", "스타뉴스, 신아일보(가격)"),
        ("대사 '빨간색 대신 초록색' 은 구경꾼 반응(신차 대본 구조 1번)", "제작 메모")],
       "폭스바겐 골프 GTI 50주년 기념 한정판 다크 모스 리미티드 에디션이 11월 국내 100대만 출시됩니다.\n245마력 2.0 TSI, 가격은 5425만원입니다.\n고유 번호 플레이트와 5년 15만km 보증이 붙습니다.\n\n#골프GTI #폭스바겐 #한정판 #신차 #란빵",
       "님들은 이 색 하나에 5425만원, 살 거임?",
       "차량용 방향제, 차량용 핸드폰 거치대, 자동차 블랙박스 2채널, 차량용 무선충전기, 자동차 발매트",
       "사진 = 뉴데일리, 스타뉴스 기자 사진(워터마크 잘라냄, 사람 있으면 모자이크). AI 생성 없음.", [P("rear", ND, s0=1.0, s1=1.1)])


# ───────────────────────── 10. 부동액 (용품) ─────────────────────────
def EP_antifreeze():
    S = "antifreeze"
    lines = [
        L("보닛 열어서 뭘 보라는 거야?",
          [B("a01", "A person's hands opening the hood of a gray sedan in a Korean apartment parking lot on a frosty morning, breath vapor, no face")],
          None, dialogue=True, speaker=3, emotion="toneup"),
        L("이번 주 네이버 쇼핑 자동차용품 인기 검색어 12위, 부동액.",
          [B("a02", "Several plain coolant antifreeze jugs in green and pink liquid on a garage shelf, no brand labels, no readable text")],
          None, say="이번 주 네이버 쇼핑 자동차용품 인기 검색어 십이위, 부동액.", em=["12위"], fx=[("drop_futuristic", "12위", 0.5)]),
        L("부동액은 냉각수가 영하에서 얼지 않게 어는점을 낮춰 줌.",
          [B("a03", "Close-up of a car engine coolant reservoir tank with pink coolant inside, frost on the engine bay edges, morning light")],
          None, em=["어는점을"]),
        L("농도가 낮으면 냉각수가 얼면서 엔진 블록이나 라디에이터가 갈라질 수 있음.",
          [B("a04", "Close-up of a cracked car radiator with frost and ice crystals, cold winter morning, garage")],
          None, em=["갈라질 수"], em_color="yellow", pop=("균열!", R, "갈라질"), shake="갈라질", fx=[("glass_smash", "갈라질", 0.45)]),
        L("먼저 보조탱크 수위가 최저선 아래인지부터 봄.",
          [B("a03", at="최저선", s0=1.3, s1=1.55, fx=0.5, fy=0.55, punch=True)], None, em=["최저선 아래인지"]),
        L("색이 탁해졌다면 보충이나 교체가 필요하다는 신호.",
          [B("a05", "Two clear plastic cups side by side, one with clean bright pink coolant and one with murky brown old coolant, on a workbench")],
          None, em=["탁해졌다면"], fx=[("wrong_gameshow_buzz", "탁해졌다면", 0.45)]),
        L("정비업계는 보통 2년 주기 교체를 원칙으로 봄.",
          [B("a06", "A mechanic's gloved hands draining old coolant from a car radiator into a pan, garage light, no face")],
          None, say="정비업계는 보통 이년 주기 교체를 원칙으로 봄.", em=["2년 주기"], em_color="yellow",
          pop=("2년!", Y, "2년"), fx=[("hit_trailer_epic", "2년", 0.5)]),
        L("보충할 땐 순정이나 차에 맞는 규격 제품을 쓰고, 물 비율을 마음대로 바꾸지 말 것.",
          [B("a02", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], None, em=["규격 제품을"]),
        L("워셔액도 겨울용으로 바꿔야 노즐이 안 얼음.",
          [B("a07", "Windshield washer fluid spraying on a frosty car windshield in winter morning, close-up, no people")],
          None, em=["겨울용으로"]),
        L("님들은 부동액 마지막으로 언제 갈았음?", [B("a01", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "언제")]),
    ]
    go(S, lines, "겨울 오기 전에", "부동액 확인했음?", "자동차용품 인기 검색어 12위 부동액, 점검법",
       "#부동액 2년 지났으면", "네이버 데이터랩 쇼핑인사이트 자동차용품 10/24~30 인기검색어 12위 + 고코리아 882891",
       [("자동차용품 인기검색어 12위 부동액(1위 요소수, 2위 차량용방향제), 10/24~30", "데이터랩 API 직접 조회"),
        ("부동액은 냉각수 어는점을 낮춤, 농도 낮으면 엔진 블록, 라디에이터 균열 가능", "고코리아 882891"),
        ("색 탁하거나 보조탱크 최저선 아래면 보충, 교체", "고코리아 882891"),
        ("정비업계 '통상 2년 주기 교체가 원칙'", "고코리아 882891(정비업계 관계자)"),
        ("순정, 규격 제품 사용, 혼합 비율 임의 조정 금지, 워셔액 겨울용", "고코리아 882891"),
        ("대사 '보닛 열어서 뭘 보라는 거야' 는 가상 운전자 반응", "제작 메모")],
       "이번 주 자동차용품 인기 검색어 12위는 부동액입니다.\n보조탱크 수위와 냉각수 색을 확인하고, 통상 2년 주기로 교체를 점검합니다.\n보충할 땐 차에 맞는 규격 제품을 쓰고 혼합 비율을 임의로 바꾸지 마세요.\n\n#부동액 #냉각수 #겨울차량점검 #자동차용품 #란빵",
       "님들은 부동액 마지막으로 언제 갈았음?",
       "부동액, 사계절 부동액, 겨울용 워셔액, 자동차 배터리 점프스타터, 성에제거 스프레이",
       "제품 사진은 상표 노출이라 안 씀, 전부 AI 배경(상표 없음). 가격은 확인 안 해 안 씀.", [B("a05", s0=1.0, s1=1.1)])


EPS = [EP_parkseat, EP_bumperall, EP_carrotdeal, EP_oring50, EP_hiddencam, EP_g90park,
       EP_tucson5, EP_usedavante, EP_gtimoss, EP_antifreeze]

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in EPS:
        if not want or f.__name__[3:] in want:
            f()
