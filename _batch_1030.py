#!/usr/bin/env python3
"""란빵 2026-10-30 대상 daily 10편 (2026-10-29 15:00 launchd 실행).
- 보배드림 베스트 10/28~29 6편(stalkmis, disabled3, dealervat, brakecheck, doorscrape, caymancut)
  + 판결 teslafsd89 + 신차 gv90tech, zeekr7x + 용품 연계 뉴스 ureaend.
- 근거 = work/research_1030.md. 실사 원본 = work/_photos/b1030/ (map.txt). 캡처는 _batch_1027.cap() 로 얼굴 모자이크.
- 실명, 상호, 번호판 없음. 발표자(실존 인물) 컷은 안 씀. 캐릭터 없음(NO_CHAR).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1024 import B, C, L, build, IR, Y, W, R, P   # noqa: E402
from _batch_1027 import cap as _cap   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos", "b1030")
BB = "사진: 보배드림"
BV = "화면: 보배드림"
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


# ───────────────────────── 1. 스토킹 오해 신고 ─────────────────────────
def EP_stalkmis():
    S = "stalkmis"
    cap(S, "man1", "1043694_00.jpg", fit=True, boxes=[(250, 240, 80, 85)])
    cap(S, "man2", "1043694_01.jpg", fit=True, boxes=[(118, 50, 70, 80)])
    lines = [
        L("경찰서인데요, 보복운전 신고가 들어왔습니다.",
          [B("s01", "A smartphone lying on a car dashboard showing an incoming call screen, morning commute light, apartment parking lot outside, no text", s0=1.1, s1=1.3)],
          C("police", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("관리사무소로 경찰이 글쓴이 연락처를 물어왔다는 전화가 옴.",
          [B("s02", "A Korean apartment management office counter with a desk phone and visitor log, fluorescent light, no people")],
          C("drv_shock"), em=["연락처를"]),
        L("신고 내용은 글쓴이가 자기를 쫓아다니며 교통법규 위반을 신고한다는 것.",
          [B("s03", "Rear-view mirror view of a car following on a Korean city road in the morning, the following car slightly blurred, no people visible")],
          C("rage", "r"), em=["쫓아다니며"], fx=[("wrong_gameshow_buzz", "신고한다는", 0.45)]),
        L("근거는 과태료 고지서 사진에 찍힌 대시보드 모양.",
          [B("s04", "A Korean traffic fine notice letter with a blurred dashcam style photo printed on it, lying on a kitchen table, close-up, no readable text"),
           B("s04", at="대시보드", s0=1.3, s1=1.5, fx=0.5, fy=0.45, punch=True)],
          C("komatta"), em=["대시보드 모양"], em_color="yellow", pop=("대시보드?!", R, "대시보드"), fx=[("drum_rimshot", "대시보드", 0.45)]),
        L("근데 글쓴이는 위반 내역이 단 한 건도 없는 사람.",
          [B("s05", "A clean car dashboard and steering wheel seen from the driver seat, calm morning light, no people")],
          C("drv_smile", "r"), em=["단 한 건도"], fx=[("correct_ding", "없는", 0.45)]),
        L("경찰도 보복운전은 아니라며 스토킹 담당에게 넘김.",
          [B("s06", "A Korean police station office desk with case folders and a desk phone, fluorescent light, no people")],
          C("police"), em=["스토킹 담당"]),
        L("이건 스토킹으로 보기 어렵습니다. 얘기만 듣고 마무리할게요.",
          [B("s06", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_smile", "r"), dialogue=True, speaker=3, emotion="normal"),
        L("블박을 돌려보니 그날 아침 동선이 겹친 차가 한 대 있었음.",
          [B("s07", "A dashcam footage still on a laptop screen showing a car ahead on a Korean road, timestamp area blurred, desk at night, no people")],
          C("drv_think"), em=["동선이 겹친"]),
        L("그 신고자가 아빠까지 불러서 앞뒤로 글쓴이 차를 막아 세웠던 것.",
          [P("man1", BB, s0=1.0, s1=1.15), P("man2", BB, at="막아", s0=1.0, s1=1.15)],
          C("aori", "r"), em=["아빠까지"], em_color="yellow", pop=("부자 출동?!", R, "아빠까지"), shake="막아", fx=[("hit_trailer_epic", "아빠까지", 0.5)]),
        L("경찰이 차번 조회로 관리사무소까지 연락한 것도 찝찝하다고 함.",
          [B("s02", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("komatta"), em=["찝찝하다고"]),
        L("님들은 이런 신고 당하면 그냥 넘어감, 맞대응함?", [P("man2", BB, s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "맞대응함")]),
    ]
    go(S, lines, "과태료 사진 보고", "나를 스토커로 신고", "대시보드만 보고 보복운전 신고, 경찰은 스토킹 아니라고 종결",
       "#대시보드 보고 신고", "보배드림 베스트 1043694 교통사고/블박 (2026-10-29, 추천 242, 댓글 24)",
       [("경찰이 관리사무소에 연락처 문의, 관리소는 공문 요구", "원글 본문"),
        ("신고 내용: 쫓아다니며 국민신문고에 교통법규 위반 신고한다, 과태료 사진 속 대시보드로 차를 추측", "원글 본문 요약 2"),
        ("경찰 '보복운전으로 보기 어렵다' → 스토킹 담당 '출석 요구 없이 이야기 듣고 마무리'", "원글 본문(대사는 본문 인용을 줄임)"),
        ("글쓴이 교통법규 위반 내역 0건, 블박 확인 결과 동선이 겹친 차 있었음", "원글 본문"),
        ("신고자가 아버지를 불러 앞뒤로 차를 막아 세움, 첨부 사진 2장", "원글 본문 요약 4, 첨부"),
        ("댓글 '세상은 넓고 도라이들도 많다'(31)", "원글 댓글")],
       "과태료 고지서 사진 속 대시보드만 보고 다른 차를 자기를 쫓는 신고자로 찍은 사람이 보복운전으로 신고했습니다.\n경찰은 보복운전도 스토킹도 아니라며 마무리했습니다.\n신고자는 아버지까지 불러 차를 막아 세웠습니다.\n\n#보복운전 #스토킹 #블랙박스 #보배드림 #란빵",
       "님들은 이런 신고 당하면 그냥 넘어감, 맞대응함?", COMMON,
       "첨부 사진 속 인물은 원글이 얼굴을 가렸고 한 번 더 모자이크. 번호판 없음.", [P("man1", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 2. 장애인구역 3칸 막은 차 ─────────────────────────
def EP_disabled3():
    S = "disabled3"
    cap(S, "map", "1043667_00.png", fit=True, nofaces=True)
    lines = [
        L("저기요, 차 좀 빼주실래요?",
          [B("d01", "Night view of an officetel building entrance parking area in Seoul, a compact SUV parked sideways blocking several parking spaces, no people", s0=1.1, s1=1.3)],
          C("drv_q"), dialogue=True, speaker=2, emotion="normal"),
        L("오피스텔 앞, 스포티지 한 대가 장애인 주차구역 세 칸 앞을 가로로 막고 섬.",
          [P("map", BB, s0=1.0, s1=1.15), P("map", BB, at="세", s0=1.4, s1=1.6, fx=0.6, fy=0.5, punch=True)],
          C("komatta", "r"), em=["세 칸"], em_color="yellow", fx=[("drop_futuristic", "세", 0.5)]),
        L("일반칸에 댄 글쓴이 차 앞까지 같이 막고 있었음.",
          [B("d02", "Front bumper view of a parked sedan blocked by an SUV parked crosswise right in front of it, Korean parking lot at dusk, no people")],
          C("drv_shock"), em=["글쓴이 차 앞까지"]),
        L("전화하니 젊은 남자가 나와서 사과 한마디 없이 인상 쓰며 뺌.",
          [B("d03", "Back view silhouette of a young man walking toward an SUV in a parking lot at night with car keys in hand, face not visible")],
          C("rage", "r"), em=["사과 한마디 없이"], fx=[("wrong_gameshow_buzz", "인상", 0.45)]),
        L("그날은 참았는데, 다음 주에 같은 차가 똑같이 막고 있었음.",
          [B("d01", at="다음", s0=1.3, s1=1.5, fx=0.5, fy=0.55, punch=True)], C("biz_think"), em=["똑같이"]),
        L("이번엔 전화 전에 장애인 주차구역 신고앱부터 켬.",
          [B("d04", "Hand holding a smartphone in a parking lot at night taking a photo of an illegally parked SUV, screen shows a camera viewfinder, no readable text")],
          C("drv_smile", "r"), em=["신고앱부터"], fx=[("shutter_digital", "켬", 0.45)]),
        L("막힌 세 곳 모두 접수됐고, 정상 처리됐다는 답이 옴.",
          [B("d04", at="정상", s0=1.3, s1=1.5, fx=0.5, fy=0.45, punch=True)],
          C("biz_laugh"), em=["정상 처리"], em_color="yellow", pop=("접수 완료!", Y, "정상"), fx=[("correct_ding", "정상", 0.5)]),
        L("아 또 뭔데요, 지금 빼요.",
          [B("d03", s0=1.2, s1=1.35)], C("rage", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("장애인 주차구역 앞을 막는 주차방해는 과태료 50만원.",
          [B("d05", "A blue disabled parking sign and painted wheelchair symbol on asphalt with yellow hatched lines, Korean parking lot, close-up, no people")],
          C("judge"), say="장애인 주차구역 앞을 막는 주차방해는 과태료 오십마넌.", em=["50만원"], em_color="yellow",
          fx=[("hit_trailer_epic", "50만원", 0.5)],
          info={"kind": "counter", "at": "과태료", "title": "장애인구역 주차방해", "items": [{"num": 50, "suffix": "만원", "label": "과태료", "at": "50만원"}]}),
        L("그 뒤로 그 차는 다시 안 보인다고 함.",
          [B("d06", "An empty row of blue disabled parking spaces in front of an officetel at night, clean, no cars, no people")], C("drv_smile", "r"), em=["다시 안"]),
        L("님들은 이럴 때 바로 신고함, 한 번은 봐줌?", [P("map", BB, s0=1.0, s1=1.1)], C("biz_q"), fx=[("pop_bubble", "봐줌")]),
    ]
    go(S, lines, "장애인구역 3칸 막고", "적반하장 하더니", "사과 없이 인상 쓰던 차주, 다음 주 신고 3건 접수",
       "#장애인구역 3칸 막은 차", "보배드림 베스트 1043667 자유게시판 (2026-10-29, 추천 553, 댓글 40)",
       [("오피스텔 앞 장애인 주차구역 앞을 스포티지가 막고 일반칸 글쓴이 차 앞도 막음, 첨부 그림", "원글 본문, 첨부"),
        ("빼달라고 전화하자 젊은 남자가 사과 없이 인상 쓰며 뺌", "원글 본문"),
        ("다음 주 같은 상황, 장애인 주차구역 신고앱으로 세 곳 신고, 모두 접수 정상 처리 답변, 이후 안 보임", "원글 본문"),
        ("장애인등편의법 17조 5항 주차방해 과태료 50만원", "casenote 원문(10/29 benzfire 조사), 노컷뉴스 10/25"),
        ("대사 '아 또 뭔데요' 는 본문 '거만한 자세, 인사도 없음' 을 대사체로", "제작 메모"),
        ("세 곳이 각각 50만원인지(150만원)는 확인 안 돼 대본에서 뺌", "댓글 '50x3해서 150인가요?'(51)")],
       "장애인 주차구역 세 칸 앞을 막고 선 차, 빼달라니 사과 없이 인상만 썼습니다.\n다음 주 같은 차가 또 막자 신고앱으로 세 곳을 신고했고 모두 접수됐습니다.\n장애인구역 주차방해 과태료는 50만원입니다.\n\n#장애인주차구역 #주차방해 #과태료 #보배드림 #란빵",
       "님들은 이럴 때 바로 신고함, 한 번은 봐줌?", COMMON,
       "첨부 그림 그대로(번호판, 상호 없음). 실제 사진은 원글에 없어 AI 배경.", [B("d06", s0=1.0, s1=1.1)])


# ───────────────────────── 3. 특장차 부가세 별도 ─────────────────────────
def EP_dealervat():
    S = "dealervat"
    lines = [
        L("그리고 부가세 10%는 별도입니다.",
          [B("v01", "A used car dealer's small office desk with a contract form, calculator and pen, fluorescent light, no people, no readable text", s0=1.1, s1=1.3)],
          C("sales", "r"), dialogue=True, speaker=2, emotion="normal", say="그리고 부가세 십퍼센트는 별도입니다."),
        L("회사 지시로 중고 특장차를 사러 간 글쓴이. 광고 가격은 2990만원.",
          [B("v02", "A used one-ton box truck with a special body parked in a gravel storage yard in Korea, daytime, no people, no license plate visible")],
          C("drv_smile"), say="회사 지시로 중고 특장차를 사러 간 글쓴이. 광고 가격은 이천구백구십마넌.", em=["2990만원"]),
        L("주소에 가 보니 매매상사가 아니라 야적장, 딜러는 나오지도 않음.",
          [B("v02", at="야적장", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], C("komatta", "r"), em=["야적장"], fx=[("drum_rimshot", "야적장", 0.45)]),
        L("계약하자니 알선수수료 2.2퍼센트가 붙는다고 함.",
          [B("v01", at="알선수수료", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("drv_think"), say="계약하자니 알선수수료 이점이퍼센트가 붙는다고 함.", em=["알선수수료"]),
        L("거기에 특장차는 부가세 별도라며 299만원을 더 내라고 함.",
          [B("v03", "Close-up of a calculator display and a hand-written price memo on a dealer desk, numbers blurred, warm light, no people")],
          C("bill_shock", "r"), say="거기에 특장차는 부가세 별도라며 이백구십구마넌을 더 내라고 함.",
          em=["299만원"], em_color="yellow", pop=("299만원?!", R, "299만원"), fx=[("hit_trailer_epic", "299만원", 0.5)],
          info={"kind": "bars", "at": "거기에", "title": "차값 말고 더 내라는 돈", "items": [
              {"label": "알선수수료", "num": 66, "suffix": "만원", "at": "거기에"}, {"label": "부가세", "num": 299, "suffix": "만원", "at": "299만원", "flash": "299만원"}]}),
        L("혹시 몰라 아는 딜러한테 같은 차 번호를 불러봄.",
          [B("v04", "A hand holding a smartphone during a call inside a parked company van, dashboard visible, daytime, face not visible")], C("drv_q")),
        L("같은 차가 2890만원, 부가세 없고 수수료는 44만원 정찰제.",
          [B("v04", at="같은", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("biz_laugh", "r"),
          say="같은 차가 이천팔백구십마넌, 부가세 없고 수수료는 사십사마넌 정찰제.", em=["2890만원"], em_color="yellow", fx=[("correct_ding", "2890만원", 0.5)],
          info={"kind": "compare", "at": "같은", "title": "같은 차, 다른 딜러", "items": [
              {"label": "첫 딜러", "color": R, "at": "같은", "rows": [["차값", "2990만원", W], ["부가세", "+299만원", Y]]},
              {"label": "아는 딜러", "color": W, "at": "2890만원", "rows": [["차값", "2890만원", Y], ["부가세", "없음", W]]}]}),
        L("근데 알고 보니 첫 딜러가 그 차 주인이었음.",
          [B("v02", s0=1.2, s1=1.35, fx=0.4, fy=0.5)], C("drv_shock"), em=["차 주인"], em_color="yellow", pop=("차주였어?!", R, "주인"), shake="주인"),
        L("오늘 계약 안 하시면 내일부터 100만원 올립니다.",
          [B("v01", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("sales", "r"), dialogue=True, speaker=3, emotion="toneup",
          say="오늘 계약 안 하시면 내일부터 백마넌 올립니다."),
        L("퇴근하고 광고를 보니 진짜로 100만원을 올려놨음.",
          [B("v05", "A laptop screen at night showing a used car listing page with a price tag area blurred, home desk, no readable text")],
          C("biz_laugh"), say="퇴근하고 광고를 보니 진짜로 백마넌을 올려놨음.", em=["진짜로"], fx=[("drum_rimshot", "올려놨음", 0.45)]),
        L("님들은 이런 딜러, 그래도 차 좋으면 삼?", [B("v02", s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "삼")]),
    ]
    go(S, lines, "중고 특장차 사러 갔더니", "부가세 별도라고?", "알선수수료 2.2%에 부가세 299만원, 알고 보니 딜러가 차주",
       "#특장차 부가세 별도?", "보배드림 베스트 1043698 자유게시판 (2026-10-28, 추천 52)",
       [("법인용 중고 특장차, 광고 2990만원, 주소지는 야적장, 딜러 안 나옴", "원글 본문"),
        ("알선수수료 2.2%(약 66만원) + 부가세 10% 별도(299만원) → 차값 외 약 365만원", "원글 본문"),
        ("아는 딜러 조회: 2890만원, 부가세 없음, 알선 44만원 정찰, 탁송 무료", "원글 본문"),
        ("첫 딜러 '젊은 애들이 이 차 찾던데 고객님 아니세요?' → 정황상 첫 딜러가 차주", "원글 본문"),
        ("'오늘 계약 안 하면 내일부터 100만원 올림' → 실제로 광고가 100만원 오름", "원글 본문(대사는 본문 인용 그대로)"),
        ("부가세 자체는 거래 방식에 따라 생길 수 있다고 글쓴이도 언급, 위법 단정 안 함", "원글 본문")],
       "중고 특장차를 사러 갔더니 알선수수료 2.2%에 부가세 10% 별도라는 딜러.\n아는 딜러에게 같은 차를 물으니 100만원 싸고 부가세도 없었습니다.\n알고 보니 첫 딜러가 차 주인이었습니다.\n\n#중고차 #특장차 #부가세 #보배드림 #란빵",
       "님들은 이런 딜러, 그래도 차 좋으면 삼?",
       "차량용 핸드폰 거치대, 자동차 블랙박스 2채널, 1톤 트럭 적재함 커버, 차량용 공구세트, 차량용 방향제",
       "원글에 사진 없음, 전부 AI 배경. 매매상사, 지역 상호 안 씀.", [B("v05", s0=1.0, s1=1.1)])


# ───────────────────────── 4. 정속주행 보복운전 신고 ─────────────────────────
def EP_brakecheck():
    S = "brakecheck"
    lines = [
        L("보복운전이라 면허정지 100일입니다.",
          [B("k01", "A Korean police station traffic investigation room with a desk, a monitor and a chair, fluorescent light, no people", s0=1.1, s1=1.3)],
          C("police", "r"), dialogue=True, speaker=2, emotion="normal", say="보복운전이라 면허정지 백일입니다."),
        L("자동차전용도로 1차로를 시속 85에서 90으로 달리던 글쓴이.",
          [B("k02", "Driver's view on a Korean three-lane expressway in the leftmost lane in the afternoon, light traffic, speedometer not visible")],
          C("drv_smile"), say="자동차전용도로 일차로를 시속 팔십오에서 구십으로 달리던 글쓴이.", em=["1차로"]),
        L("뒤에서 빨간 스팅어가 쌍라이트를 켜고, 옆에 붙어 욕설에 경적까지.",
          [B("k03", "Rear-view mirror showing a red sports sedan very close behind with headlights flashing, Korean expressway, daytime"),
           B("k03", at="옆에", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("aori", "r"), em=["쌍라이트"], fx=[("boom_subby_kick", "경적까지", 0.45)]),
        L("번쩍거리는 빛에 놀라 브레이크를 살짝 밟았다고 함.",
          [B("k04", "Close-up of a driver's shoe lightly pressing a brake pedal in a car footwell, daylight, no face")],
          C("drv_shock"), em=["살짝"]),
        L("석 달 뒤, 스팅어 차주가 보복운전으로 신고함.",
          [B("k01", at="신고함", s0=1.3, s1=1.45)], C("komatta", "r"), em=["보복운전으로"], pop=("신고?!", R, "신고함"), shake="신고함"),
        L("증거는 브레이크등이 1초쯤 켜지는 10초짜리 영상 두 개.",
          [B("k05", "Close-up of a car's rear brake lights glowing red on an expressway, motion blur, daytime, no license plate visible")],
          C("biz_think"), say="증거는 브레이크등이 일초쯤 켜지는 십초짜리 영상 두 개.", em=["영상 두 개"], fx=[("drum_rimshot", "두", 0.45)]),
        L("한 달 뒤 보복운전은 무혐의로 끝났음.",
          [B("k06", "A stamped Korean police notice document on a desk next to a car key, soft light, no readable text")],
          C("drv_smile", "r"), em=["무혐의"], em_color="yellow", fx=[("correct_ding", "무혐의로", 0.5)]),
        L("근데 브레이크 밟은 걸로 벌점 10점에 과태료 8만원을 물리겠다고 함.",
          [B("k06", at="벌점", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("bill_shock"), say="근데 브레이크 밟은 걸로 벌점 십점에 과태료 팔마넌을 물리겠다고 함.",
          em=["8만원"], em_color="yellow", pop=("벌점?!", R, "벌점"), fx=[("hit_trailer_epic", "벌점", 0.5)],
          info={"kind": "compare", "at": "근데", "title": "결론", "items": [
              {"label": "보복운전", "color": W, "at": "근데", "rows": [["결과", "무혐의", Y]]},
              {"label": "브레이크", "color": R, "at": "벌점", "rows": [["벌점", "10점", W], ["과태료", "8만원", Y]]}]}),
        L("번쩍거린다고 브레이크 밟는 게 상식적으로 말이 돼요?",
          [B("k01", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("ignore", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("댓글에선 1차로는 추월차로라 계속 달린 것도 문제라는 말이 나옴.",
          [B("k02", s0=1.2, s1=1.35, fx=0.4, fy=0.5)], C("biz_think"), say="댓글에선 일차로는 추월차로라 계속 달린 것도 문제라는 말이 나옴.", em=["추월차로"]),
        L("님들은 이거 벌점 맞는 게 맞음, 억울함?", [B("k05", s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "억울함")]),
    ]
    go(S, lines, "쌍라이트 피해자였는데", "벌점은 내가 받는다?", "보복운전은 무혐의, 브레이크 1초로 벌점 10점 통보",
       "#브레이크 1초 벌점", "보배드림 베스트 1043711 자유게시판 (2026-10-28, 추천 20, 댓글 16)",
       [("5월 초 의왕~봉담 자동차전용도로(제한 90, 편도 3차로) 1차로 85~90 주행", "원글 본문"),
        ("빨간 스팅어 쌍라이트, 옆에서 창문 열고 욕설, 경적 → 놀라 브레이크 살짝", "원글 본문"),
        ("8월 말 보복운전 신고 접수, 조사관 '면허정지 100일' 언급", "원글 본문(대사 인용)"),
        ("증거 = 브레이크등 1초가량 들어오는 10초짜리 영상 2개", "원글 본문"),
        ("보복운전 무혐의 자체 종결, 브레이크 행위로 벌점 10점, 과태료 8만원 부과 예정 통보, 이의 제기 후 도로교통공단 판독 의뢰 언급(진행 중)", "원글 본문(근거 조항은 본문에 없어 대본에 안 씀)"),
        ("조사관 '쌍라이트 빛을 보았다고 브레이크 밟는 게 상식적으로 말이 되냐'", "원글 본문(대사체로 줄임)"),
        ("댓글 '1차로는 추월차로'(3), '1차선 점유하고 느리게 가면 안 됨'(4)", "원글 댓글")],
       "쌍라이트와 욕설에 놀라 브레이크를 1초 밟았더니 석 달 뒤 보복운전으로 신고당했습니다.\n보복운전은 무혐의, 대신 벌점 10점과 과태료 8만원을 통보받았습니다.\n사건은 아직 진행 중입니다.\n\n#보복운전 #급제동 #벌점 #보배드림 #란빵",
       "님들은 이거 벌점 맞는 게 맞음, 억울함?", COMMON,
       "원글에 사진, 영상 없음. 전부 AI 배경. 경찰서 이름, 조사관 성별은 안 씀.", [B("k03", s0=1.0, s1=1.1)])


# ───────────────────────── 5. 문콕 흠집 3곳 ─────────────────────────
def EP_doorscrape():
    S = "doorscrape"
    cap(S, "s1", "1043646_00.jpg", box=(0, 150, 904, 870), fit=True, nofaces=True)
    cap(S, "s2", "1043646_00.jpg", box=(0, 860, 904, 1560), fit=True, nofaces=True)
    cap(S, "s3", "1043646_00.jpg", box=(0, 1520, 904, 2240), fit=True, nofaces=True)
    cap(S, "v1", "1043646_f3.jpg", fit=True)
    cap(S, "v2", "1043646_f7.jpg", fit=True)
    lines = [
        L("이 세 군데 중에 한 군데는 따님이 낸 거예요.",
          [P("s1", BB, s0=1.0, s1=1.2)], C("sagi", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("주차장에서 딸이 차 문을 열다가 옆 차에 부딪힘.",
          [P("v1", BV, s0=1.0, s1=1.15), P("v2", BV, at="부딪힘", s0=1.2, s1=1.4, fx=0.5, fy=0.5, punch=True)],
          C("drv_shock"), em=["차 문을"], fx=[("boom_subby_kick", "부딪힘", 0.45)]),
        L("상대 차주가 보내온 사진엔 빨간 동그라미가 세 개.",
          [P("s1", BB, s0=1.0, s1=1.15), P("s2", BB, at="세", s0=1.0, s1=1.15), P("s3", BB, at="개", s0=1.0, s1=1.15)],
          C("bill_shock", "r"), em=["세 개"], em_color="yellow", pop=("3군데?!", R, "세"), fx=[("drop_futuristic", "세", 0.5)]),
        L("이 중 하나는 분명 문콕이니 보험처리 해달라는 것.",
          [P("s2", BB, s0=1.2, s1=1.4, fx=0.5, fy=0.5)], C("sagi"), em=["보험처리"]),
        L("근데 흠집을 보면 위치도 방향도 다 제각각임.",
          [P("s3", BB, s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], C("drv_think", "r"), em=["제각각"], fx=[("wrong_gameshow_buzz", "제각각임", 0.45)]),
        L("댓글은 찍힌 자국이 아니라 긁힌 자국이라는 말이 많았음.",
          [P("s2", BB, s0=1.4, s1=1.6, fx=0.5, fy=0.45)], C("biz_think"), em=["긁힌 자국"]),
        L("쿵 하고 부딪힌 걸로는 저렇게 길게 안 긁혀요.",
          [P("s3", BB, s0=1.2, s1=1.35)], C("lawyer", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("기존 흠집까지 한 번에 얹으려는 덤터기 아니냐는 것.",
          [P("s1", BB, s0=1.3, s1=1.5, fx=0.5, fy=0.4, punch=True)], C("ohagya"), em=["덤터기"], em_color="yellow",
          pop=("덤터기?!", R, "덤터기"), shake="덤터기", fx=[("hit_trailer_epic", "덤터기", 0.5)]),
        L("반대로 차가 들어오는데 문부터 왜 열었냐는 지적도 나옴.",
          [P("v1", BV, s0=1.1, s1=1.3, fx=0.6, fy=0.5)], C("komatta", "r"), em=["문부터"]),
        L("글쓴이도 잘했다는 건 아니라며 의견을 물어본 상황.",
          [B("o01", "Close-up of a car door edge and the side panel of a white parked car in an underground parking lot, small scratches, no people")],
          C("biz_q"), em=["잘했다는 건 아니라며"]),
        L("님들은 한 군데 인정하고 끝냄, 끝까지 따짐?", [P("s2", BB, s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "따짐")]),
    ]
    go(S, lines, "문콕 한 번 했는데", "흠집이 세 군데?", "세 곳 중 한 곳은 문콕이라며 보험처리 요구",
       "#문콕 흠집 3군데", "보배드림 베스트 1043646 교통사고/블박 (2026-10-28, 추천 98, 댓글 12)",
       [("딸이 문 열다 부딪힘, 상대가 사진 3군데 중 한 군데라 우기며 보험처리 요구", "원글 본문, 첨부 사진(빨간 동그라미 3개)"),
        ("블박 화면 영상 12초(문 여는 장면)", "원글 첨부 영상"),
        ("댓글 '긁힌 자국, 방향도 제각각, 기존에 있던 거 덤탱이'(7), '쿵 한 상태에서 움직임이 있으면 긁기라도'", "원글 댓글(대사는 댓글 요지를 대사체로)"),
        ("댓글 '차 오는데 문은 왜 여는'(5), '고의사고네'(8)", "원글 댓글"),
        ("글쓴이 '물론 잘했다고 하는 건 아니니 오해는 없으시길'", "원글 본문")],
       "딸이 문 열다 옆 차에 부딪혔는데 상대 차주가 흠집 세 곳을 보내며 보험처리를 요구했습니다.\n댓글은 위치도 방향도 제각각인 긁힌 자국이라며 덤터기를 의심했습니다.\n님들 생각은 어떤가요?\n\n#문콕 #보험처리 #주차장 #보배드림 #란빵",
       "님들은 한 군데 인정하고 끝냄, 끝까지 따짐?",
       "차량용 도어가드, 문콕 방지 패드, 자동차 블랙박스 2채널, 차량용 컴파운드, 차량용 방향제",
       "영상 화면은 블박 재생 화면을 휴대폰으로 찍은 것, 사람 얼굴 안 보임. 번호판 없음.", [P("v1", BV, s0=1.0, s1=1.1)])


# ───────────────────────── 6. 카이맨 칼치기 반전 ─────────────────────────
def EP_caymancut():
    S = "caymancut"
    cap(S, "car", "1043647_00.jpg", box=(0, 380, 828, 1250), nofaces=True, cy=0.55)
    cap(S, "f1", "1043647_f1.jpg", nofaces=True)
    cap(S, "f3", "1043647_f3.jpg", nofaces=True)
    cap(S, "f5", "1043647_f5.jpg", nofaces=True)
    cap(S, "f7", "1043647_f7.jpg", nofaces=True)
    px(S, "car", [(520, 590, 280, 110)])
    lines = [
        L("어어, 저 사이로 들어온다고?",
          [P("f5", BV, s0=1.0, s1=1.2)], C("drv_shock", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("경북 영주의 한 국도, 구형 카이맨이 블박차 앞으로 칼치기를 함.",
          [P("f3", BV, s0=1.0, s1=1.15), P("f5", BV, at="칼치기를", s0=1.3, s1=1.5, fx=0.35, fy=0.6, punch=True)],
          C("aori"), em=["칼치기"], em_color="yellow", pop=("칼치기!!", R, "칼치기를"), shake="칼치기를", fx=[("boom_subby_kick", "칼치기를", 0.5)]),
        L("좁은 틈을 비집고 순식간에 앞으로 빠져나감.",
          [P("f7", BV, s0=1.0, s1=1.2, fx=0.5, fy=0.55)], C("drv_shock", "r"), em=["순식간에"]),
        L("글쓴이는 따라가서 번호까지 따고, 이 사람 아는 분 있냐고 올림.",
          [P("car", BB, s0=1.0, s1=1.15)], C("rage"), em=["번호까지"]),
        L("근데 댓글 반응이 예상과 정반대였음.",
          [P("f1", BV, s0=1.0, s1=1.15)], C("komatta", "r"), em=["정반대"], em_color="yellow", pop=("반전?!", Y, "정반대였음"),
          fx=[("scratch_vinyl", "정반대였음", 0.45)]),
        L("추천 34개 1등 댓글은 영상 초반에 일부러 가속해서 길막한 거 아니냐는 것.",
          [P("f1", BV, s0=1.2, s1=1.4, fx=0.5, fy=0.6, punch=True)], C("biz_think"),
          say="추천 삼십사개 일등 댓글은 영상 초반에 일부러 가속해서 길막한 거 아니냐는 것.", em=["일부러 가속해서"],
          fx=[("wrong_gameshow_buzz", "길막한", 0.45)],
          info={"kind": "quotes", "at": "추천", "title": "댓글 반응", "items": [
              {"text": "일부러 가속해서 길막?", "at": "추천"}, {"text": "갑자기 급가속을 하네", "at": "가속해서"}, {"text": "1차로 정속 없으면 칼치기도 없다", "at": "길막한"}]}),
        L("갑자기 급가속을 하네? 앞질러 가는 게 싫었나 봄.",
          [P("f3", BV, s0=1.2, s1=1.4)], C("biz_laugh", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("1차로에서 버티는 차가 있으니 칼치기가 생긴다는 말까지 나옴.",
          [P("f7", BV, s0=1.2, s1=1.35, fx=0.4, fy=0.6)], C("drv_think"), say="일차로에서 버티는 차가 있으니 칼치기가 생긴다는 말까지 나옴.", em=["버티는 차"]),
        L("물론 좁은 틈으로 파고드는 칼치기 자체는 위험한 운전임.",
          [P("car", BB, s0=1.2, s1=1.4, fx=0.5, fy=0.5)], C("judge", "r"), em=["위험한 운전"], fx=[("correct_ding", "위험한", 0.45)]),
        L("님들이 보기엔 칼치기가 잘못임, 길막이 잘못임?", [P("f5", BV, s0=1.0, s1=1.1)], C("biz_q"), fx=[("pop_bubble", "잘못임")]),
    ]
    go(S, lines, "칼치기 당했다고 올렸는데", "댓글이 내 편이 아니다", "카이맨 칼치기 제보, 댓글은 블박차 가속을 지적",
       "#카이맨 칼치기 반전", "보배드림 베스트 1043647 교통사고/블박 (2026-10-28, 추천 39, 댓글 44)",
       [("경북 영주, 구형 회색 카이맨 칼치기, 번호 땀, 아는 사람 있냐는 글", "원글 본문, 첨부 사진, 영상 17.7초"),
        ("댓글 '영상 초반 일부러 가속해서 길막하려고 한 거 아니죠?'(34)", "원글 댓글"),
        ("댓글 '갑자기 급가속을 하네, 포르쉐가 앞질러 가게 놔두고 싶지 않았나 봄'(14)", "원글 댓글(대사는 댓글을 줄임)"),
        ("댓글 '1차로 정속충 없으면 칼치기도 없다'(6)", "원글 댓글"),
        ("본문의 '죽을 뻔했다' 표현은 제목, 대본에 안 씀", "제작 메모")],
       "경북 영주에서 카이맨에게 칼치기를 당했다는 블박 제보.\n그런데 추천 1등 댓글은 블박차가 일부러 가속해 길을 막은 것 아니냐고 지적했습니다.\n칼치기 자체는 위험한 운전입니다.\n\n#칼치기 #카이맨 #블랙박스 #보배드림 #란빵",
       "님들이 보기엔 칼치기가 잘못임, 길막이 잘못임?", COMMON,
       "카이맨 번호판은 원글이 스티커로 가림. 블박 프레임 속 다른 차 번호판은 너무 작아 안 보임.", [P("car", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 7. 테슬라 FSD 환불소송 패소 ─────────────────────────
SW = "사진: 시사위크"


def EP_teslafsd89():
    S = "teslafsd89"
    cap(S, "t1", "fsd_0.jpg", nofaces=True, cx=0.5)
    cap(S, "t2", "fsd_1.jpg", nofaces=True, cx=0.45)
    px(S, "t2", [(60, 800, 260, 160)])
    lines = [
        L("옵션값 수백만원 냈는데 환불이 안 된다고?",
          [P("t1", SW, s0=1.0, s1=1.2)], C("wow", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("테슬라 FSD 옵션을 산 차주 89명이 돈을 돌려달라고 소송을 냄.",
          [P("t2", SW, s0=1.0, s1=1.15)], C("lawyer"), say="테슬라 에프에스디 옵션을 산 차주 팔십구명이 돈을 돌려달라고 소송을 냄.", em=["89명이"]),
        L("옵션값은 사는 시점에 따라 600만에서 900만원 수준.",
          [B("f01", "Interior of a white electric car at night, large center touchscreen glowing, steering wheel, empty driver seat, no readable text")],
          C("bill_shock", "r"), say="옵션값은 사는 시점에 따라 육백만에서 구백마넌 수준.", em=["900만원"], em_color="yellow",
          fx=[("drop_futuristic", "900만원", 0.5)],
          info={"kind": "bars", "at": "옵션값은", "title": "FSD 옵션값", "items": [
              {"label": "최저", "num": 600, "suffix": "만원", "at": "600만에서"}, {"label": "최고", "num": 900, "suffix": "만원", "at": "900만원", "flash": "900만원"}]}),
        L("운전자 없이 달리는 완전자율주행은 아직이라는 이유.",
          [B("f01", at="운전자", s0=1.3, s1=1.5, fx=0.45, fy=0.55, punch=True)], C("komatta"), em=["완전자율주행"]),
        L("근데 오늘 나온 1심 결과는 차주들 패소.",
          [B("f02", "Exterior of a Korean district courthouse building in Seoul on an overcast day, wide steps, no people")],
          C("judge", "r"), say="근데 오늘 나온 일심 결과는 차주들 패소.", em=["패소"], em_color="yellow",
          pop=("패소!!", R, "패소"), shake="패소", fx=[("hit_trailer_epic", "패소", 0.5)]),
        L("법원은 계약상 FSD가 완전자율주행이 아니라고 봄.",
          [P("t1", SW, s0=1.2, s1=1.4, fx=0.4, fy=0.6)], C("judge"), say="법원은 계약상 에프에스디가 완전자율주행이 아니라고 봄.", em=["아니라고"]),
        L("운전자 개입이 필요한 부분 자동화를 의미할 뿐입니다.",
          [B("f02", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("lawyer", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("규제랑 기술이 따라오면 주기로 한, 기한 없는 계약이라는 것.",
          [B("f03", "A signed car option purchase contract on a desk with a pen, fine print visible but unreadable, soft light, no people")],
          C("biz_think"), em=["기한 없는 계약"], em_color="yellow",
          info={"kind": "quotes", "at": "규제랑", "title": "1심 판단", "items": [
              {"text": "레벨5 아닌 부분 자동화", "at": "규제랑"}, {"text": "불확정기한부 계약", "at": "기한"}, {"text": "기본 기능은 이미 제공", "at": "계약이라는"}]}),
        L("구형 하드웨어 차에도 최근 신호등 인식이 들어온 점도 근거가 됨.",
          [P("t2", SW, s0=1.2, s1=1.4, fx=0.5, fy=0.5)], C("drv_think", "r"), em=["신호등 인식"], fx=[("correct_ding", "근거가", 0.45)]),
        L("항소할지는 아직 안 알려짐.",
          [B("f02", s0=1.1, s1=1.25)], C("biz_q"), em=["항소할지는"]),
        L("님들은 언제 될지 모르는 옵션, 돈 내고 기다릴 수 있음?", [P("t1", SW, s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "옵션값 수백만원 냈는데", "테슬라 차주들 패소", "FSD 환불소송 1심, 차주 89명 청구 기각",
       "#FSD 환불소송 패소", "서울중앙지법 민사합의30부 2026-10-29 선고 (내일신문 606900, 대한경제 202610291209243740734, 시사위크 238675)",
       [("차주 89명(2019~2022 FSD 구매), 2024-12 제소, 매매대금 반환 청구 기각", "내일신문, 대한경제, 시사위크"),
        ("옵션가 구매 시점에 따라 600만~900만원 수준", "시사위크"),
        ("'운전자 개입이 필요한 부분 자동화(신호등 인식, 도심 자동조향 등)를 의미할 뿐'", "재판부, 대한경제, 시사위크(대사는 어미만 다듬음)"),
        ("규제 승인과 기술 발전 전제의 불확정기한부 계약, AP/EAP 이미 제공", "내일신문, 대한경제, 시사위크"),
        ("최근 HW3 차량에도 FSD v14 Lite 로 신호등, 표지판 인식, 시내 자동주행 추가", "내일신문, 대한경제"),
        ("원고 항소 여부 미정", "시사위크")],
       "테슬라 FSD 옵션을 산 차주 89명이 낸 환불 소송이 1심에서 기각됐습니다.\n법원은 계약상 FSD가 완전자율주행이 아니라 운전자 개입이 필요한 부분 자동화라고 봤습니다.\n항소 여부는 아직 알려지지 않았습니다.\n\n#테슬라 #FSD #자율주행 #판결 #란빵",
       "님들은 언제 될지 모르는 옵션, 돈 내고 기다릴 수 있음?",
       "테슬라 모델Y 매트, 차량용 무선충전 거치대, 전기차 충전구 커버, 자동차 블랙박스 2채널, 차량용 방향제",
       "차 사진은 시사위크 기사 게재 사진(테슬라 전시장, 충전소). 원고 대표 변호사 실명은 안 씀.", [P("t2", SW, s0=1.0, s1=1.1)])


# ───────────────────────── 8. GV90 테크 데이 ─────────────────────────
GN = "사진: 제네시스"


def EP_gv90tech():
    S = "gv90tech"
    cap(S, "g0", "gv90_0.jpg", nofaces=True, cx=0.5)
    cap(S, "g4", "gv90_4.jpg", nofaces=True, cx=0.5)
    cap(S, "g5", "gv90_5.jpg", nofaces=True, fit=True)
    cap(S, "g3", "gv90_3.jpg", cx=0.3)
    px(S, "g3", [(760, 470, 320, 230)])
    lines = [
        L("문짝 사이 기둥이 어디 갔어?",
          [P("g4", GN, s0=1.0, s1=1.2)], C("wow", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("제네시스가 GV90 기술 행사를 열었는데, 앞뒤 문 사이 기둥이 안 보임.",
          [P("g4", GN, s0=1.0, s1=1.15), P("g4", GN, at="기둥이", s0=1.4, s1=1.6, fx=0.5, fy=0.55, punch=True)],
          C("dealer"), say="제네시스가 지브이구십 기술 행사를 열었는데, 앞뒤 문 사이 기둥이 안 보임.", em=["기둥이 안 보임"],
          fx=[("hit_trailer_epic", "기둥이", 0.5)]),
        L("B필러를 숨기고 앞뒤 문이 따로 열리는 코치 도어임.",
          [P("g4", GN, s0=1.2, s1=1.35, fx=0.55, fy=0.55)], C("drv_heart", "r"), say="비필러를 숨기고 앞뒤 문이 따로 열리는 코치 도어임.", em=["코치 도어"]),
        L("뒷문은 바깥으로 밀려 나온 다음 돌면서 열림.",
          [P("g0", GN, s0=1.0, s1=1.2)], C("drv_surprise"), em=["밀려 나온 다음"]),
        L("기둥이 없는데도 지붕은 14톤포스 넘는 하중을 버텼다고 함.",
          [P("g0", GN, at="지붕은", s0=1.3, s1=1.5, fx=0.5, fy=0.35, punch=True)], C("drv_laugh", "r"),
          say="기둥이 없는데도 지붕은 십사톤포스 넘는 하중을 버텼다고 함.", em=["14톤포스"], em_color="yellow",
          pop=("14톤!!", Y, "14톤포스"), shake="14톤포스", fx=[("boom_subby_kick", "14톤포스", 0.5)]),
        L("차가 뒤집히면 천장을 따라 터지는 루프 에어백도 세계 최초로 달림.",
          [P("g5", GN, s0=1.0, s1=1.2)], C("drv_surprise"), em=["세계 최초"], fx=[("drop_futuristic", "세계", 0.5)]),
        L("펼쳐지는 데 걸리는 시간은 0.08초.",
          [P("g5", GN, at="시간은", s0=1.3, s1=1.5, fx=0.5, fy=0.3, punch=True)], C("wow", "r"), say="펼쳐지는 데 걸리는 시간은 영점영팔초.",
          em=["0.08초"],
          info={"kind": "bars", "at": "펼쳐지는", "title": "루프 에어백 전개", "items": [{"label": "전개 시간", "num": 0.08, "dec": 2, "suffix": "초", "at": "0.08초", "flash": "0.08초"}]}),
        L("차체 구조물의 72퍼센트는 알루미늄.",
          [P("g3", GN, s0=1.0, s1=1.2)], C("drv_think"), say="차체 구조물의 칠십이퍼센트는 알루미늄.", em=["알루미늄"]),
        L("자동차의 한계를 정면으로 넘어선 최고 수준의 플래그십입니다.",
          [P("g4", GN, s0=1.2, s1=1.35, fx=0.4, fy=0.5)], C("biz_smile", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("근데 정작 가격은 아직 공개 안 됨. 출시도 내년이라고만 함.",
          [P("g0", GN, s0=1.2, s1=1.35, fx=0.5, fy=0.6)], C("biz_think"), em=["가격은 아직"], em_color="yellow",
          pop=("가격은?!", R, "가격은"), fx=[("wrong_gameshow_buzz", "가격은", 0.45)]),
        L("님들은 이 차 얼마면 살 만하다고 봄?", [P("g4", GN, s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "기둥 없앤 제네시스", "근데 가격은 비밀", "GV90 테크 데이, 히든 B필러 코치 도어와 루프 에어백",
       "#GV90 기둥 없는 문", "제네시스 GV90 테크 데이 2026-10-28 영종도 (BBS 4115521, 위클리오늘 800213, 전남일보 90000077847, 이투데이 2641818)",
       [("히든 B필러 코치 도어, 뒷문 바깥으로 밀어낸 뒤 회전(듀얼 모션 힌지)", "BBS, 위클리오늘, 전남일보"),
        ("지붕 14톤포스 이상 하중 견딤(자체 시험)", "BBS, 위클리오늘, 전남일보"),
        ("세계 최초 양산차 루프 에어백, 0.08초 전개", "BBS, 위클리오늘, 전남일보(0.08초는 위클리오늘, 전남일보)"),
        ("차체 구조물 72% 알루미늄, eMP 플랫폼", "위클리오늘, 전남일보"),
        ("허광훈 상무 '일반적인 자동차의 한계를 정면으로 넘어선 글로벌 최고 수준의 플래그십'", "위클리오늘, 전남일보(대사는 줄임)"),
        ("국내 출시 내년(현대차 3분기 컨퍼런스콜), 가격 미발표(2억원 예상은 1곳 보도라 뺌)", "이투데이, 한국경제TV")],
       "제네시스가 GV90 테크 데이에서 B필러를 숨긴 코치 도어를 공개했습니다.\n지붕은 14톤포스 이상을 견디고, 세계 최초 루프 에어백은 0.08초 만에 펼쳐집니다.\n가격은 아직 공개되지 않았고 출시는 내년입니다.\n\n#제네시스 #GV90 #신차 #전기SUV #란빵",
       "님들은 이 차 얼마면 살 만하다고 봄?",
       "차량용 트렁크 정리함, 차량용 뒷좌석 태블릿 거치대, 전기차 충전구 커버, 차량용 열선 방석, 자동차 블랙박스 2채널",
       "차 화면은 제네시스(현대차) 제공 보도사진. 발표자, 대담자 사진은 안 씀. 전시장 관람객은 모자이크.", [P("g5", GN, s0=1.0, s1=1.1)])


# ───────────────────────── 9. 지커 7X ─────────────────────────
MT = "사진: 엠투데이"
BL = "사진: 블로터"


def EP_zeekr7x():
    S = "zeekr7x"
    cap(S, "z0", "zk_0.jpg", nofaces=True, cx=0.4)
    cap(S, "z8", "zk_8.jpg", nofaces=True, cx=0.5)
    cap(S, "z9", "zk_9.jpg", nofaces=True, cx=0.5)
    cap(S, "z1", "zk_1.jpg", nofaces=True, cx=0.55)
    px(S, "z1", [(860, 670, 170, 100)])
    cap(S, "zr", "zkb_2.jpg", cx=0.5)
    lines = [
        L("중국차인데 뒷좌석에 냉장고가 있다고?",
          [P("z0", MT, s0=1.0, s1=1.2)], C("wow", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("지리그룹의 고급 브랜드 지커가 중형 전기 SUV 7X를 국내에 내놓음.",
          [P("z8", MT, s0=1.0, s1=1.15), P("z1", MT, at="7X를", s0=1.0, s1=1.15)],
          C("dealer"), say="지리그룹의 고급 브랜드 지커가 중형 전기 에스유브이 세븐엑스를 국내에 내놓음.", em=["7X"]),
        L("가격은 5299만원부터, 최상위 울트라는 6999만원.",
          [P("z1", MT, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("bill_shock", "r"),
          say="가격은 오천이백구십구마넌부터, 최상위 울트라는 육천구백구십구마넌.", em=["5299만원부터"], em_color="yellow",
          fx=[("drop_futuristic", "가격은", 0.5)],
          info={"kind": "bars", "at": "가격은", "title": "지커 7X 국내 가격", "items": [
              {"label": "프로", "num": 5299, "suffix": "만원", "at": "가격은"}, {"label": "울트라", "num": 6999, "suffix": "만원", "at": "6999만원"}]}),
        L("울트라는 645마력에 제로백 3.9초.",
          [P("z8", MT, at="645마력", s0=1.3, s1=1.5, fx=0.5, fy=0.6, punch=True)], C("drv_laugh"),
          say="울트라는 육백사십오마력에 제로백 삼점구초.", em=["645마력"], pop=("645마력!", Y, "645마력"), fx=[("boom_subby_kick", "645마력", 0.5)]),
        L("2열에는 영하 6도부터 50도까지 맞추는 5.3리터 냉온장고.",
          [P("zr", BL, s0=1.0, s1=1.2)], C("drv_heart", "r"), say="이열에는 영하 육도부터 오십도까지 맞추는 오점삼리터 냉온장고.", em=["냉온장고"]),
        L("실내엔 16인치 화면에 버튼은 최소한만 남김.",
          [P("z9", MT, s0=1.0, s1=1.2)], C("drv_think"), say="실내엔 십육인치 화면에 버튼은 최소한만 남김.", em=["16인치"]),
        L("근데 국내 1호 고객이 한국 배터리 회사 SK온이었음.",
          [P("z0", MT, s0=1.2, s1=1.4, fx=0.4, fy=0.5)], C("drv_surprise", "r"),
          say="근데 국내 일호 고객이 한국 배터리 회사 에스케이온이었음.", em=["1호 고객"], em_color="yellow",
          pop=("1호 고객?!", R, "1호"), fx=[("hit_trailer_epic", "1호", 0.5)]),
        L("업무용 차량으로 다양하게 활용할 계획입니다.",
          [P("z1", MT, s0=1.1, s1=1.3)], C("biz_smile"), dialogue=True, speaker=2, emotion="normal"),
        L("정작 이 차 배터리는 중국 CATL 제품.",
          [P("z8", MT, s0=1.2, s1=1.35, fx=0.4, fy=0.6)], C("biz_think", "r"), say="정작 이 차 배터리는 중국 씨에이티엘 제품.", em=["CATL"],
          fx=[("drum_rimshot", "CATL", 0.45)],
          info={"kind": "compare", "at": "정작", "title": "1호차의 반전", "items": [
              {"label": "1호 고객", "color": W, "at": "정작", "rows": [["회사", "SK온", Y]]},
              {"label": "차 배터리", "color": R, "at": "CATL", "rows": [["공급", "CATL", Y]]}]}),
        L("님들은 7천 주고 중국 전기차 삼?", [P("z0", MT, s0=1.0, s1=1.1)], C("biz_q"), say="님들은 칠천 주고 중국 전기차 삼?", fx=[("pop_bubble", "삼")]),
    ]
    go(S, lines, "중국 전기 SUV에", "뒷좌석 냉장고가?", "지커 7X 5299만원부터, 국내 1호 고객은 SK온",
       "#지커 7X 1호 고객", "지커코리아 7X 국내 출시, 시승 2026-10-27~28 (뉴시스 NISX20261022_0003836353, 블로터 676913, 소비자가만드는신문 767011)",
       [("가격 프로 5299, 맥스 5999, 울트라 6999만원", "뉴시스, 블로터, 뉴스핌, 더팩트"),
        ("울트라 645마력, 0→100km/h 3.9초", "블로터, 오토데일리, 뉴시스(마력)"),
        ("2열 5.3L 냉온장고 -6~50도", "오토데일리, 소비자가만드는신문"),
        ("16인치 센터 디스플레이", "오토데일리, 소비자가만드는신문"),
        ("국내 1호 고객 SK온(울트라), 관계자 '7X를 업무용 차량으로 다양하게 활용할 계획'", "뉴시스(대사는 줄임)"),
        ("맥스, 울트라 배터리 CATL 공급 100kWh NCM", "블로터, 소비자가만드는신문")],
       "지리그룹 지커가 중형 전기 SUV 7X를 5299만원부터 내놨습니다.\n울트라는 645마력, 2열엔 5.3L 냉온장고가 있습니다.\n국내 1호 고객은 SK온, 배터리는 CATL입니다.\n\n#지커 #7X #전기차 #신차 #란빵",
       "님들은 7천 주고 중국 전기차 삼?",
       "차량용 냉온장고, 차량용 트렁크 정리함, 전기차 충전구 커버, 차량용 무선충전 거치대, 차량용 열선 방석",
       "차 사진은 엠투데이(오토데일리 게재), 블로터 시승 사진. 시승차 번호판은 보이는 컷을 피하거나 모자이크. 1호 고객 인도식 사진(인물)은 안 씀.",
       [P("z8", MT, s0=1.0, s1=1.1)])


# ───────────────────────── 10. 요소수 매점매석 금지 종료 ─────────────────────────
def EP_ureaend():
    S = "ureaend"
    lines = [
        L("요소수 사재기 금지가 이제 풀린다고?",
          [B("u01", "Rows of white 10-liter diesel exhaust fluid jugs on a Korean auto parts store shelf, fluorescent light, no readable labels, no people", s0=1.1, s1=1.3)],
          C("wow", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("이번 주 네이버 쇼핑 자동차용품 인기 검색어 1위가 요소수.",
          [B("u02", "Close-up of a hand pouring diesel exhaust fluid from a white jug into a blue-capped filler of a diesel SUV, daylight, no face")],
          C("drv_smile"), say="이번 주 네이버 쇼핑 자동차용품 인기 검색어 일위가 요소수.", em=["1위가"], fx=[("drop_futuristic", "1위가", 0.5)]),
        L("올해 3월 중동전쟁으로 원료 수급이 불안해지자, 정부가 매점매석을 막았음.",
          [B("u03", "A large cargo ship with containers at a Korean port under a cloudy sky, cranes, no people")],
          C("police", "r"), say="올해 삼월 중동전쟁으로 원료 수급이 불안해지자, 정부가 매점매석을 막았음.", em=["매점매석을"]),
        L("판매자는 작년 월평균의 두 배 넘는 물량을 7일 넘게 쌓아둘 수 없었음.",
          [B("u04", "A warehouse with stacked pallets of white plastic jugs wrapped in film, forklift aisle, fluorescent light, no people")],
          C("biz_think"), say="판매자는 작년 월평균의 두 배 넘는 물량을 칠일 넘게 쌓아둘 수 없었음.", em=["두 배"], em_color="yellow",
          info={"kind": "quotes", "at": "판매자는", "title": "매점매석 금지 기준", "items": [
              {"text": "전년 월평균 판매량 200% 초과", "at": "두"}, {"text": "7일 이상 보관 금지", "at": "쌓아둘"}]}),
        L("이 고시가 10월 31일로 끝남.",
          [B("u05", "A desk calendar showing the end of October with a circled date, next to a car key, soft light, no readable text")],
          C("drv_surprise", "r"), say="이 고시가 시월 삼십일일로 끝남.", em=["끝남"], em_color="yellow", pop=("종료!", Y, "끝남"), fx=[("hit_trailer_epic", "끝남", 0.5)]),
        L("국내 요소 재고가 4에서 5개월치라 수급이 안정됐다는 판단.",
          [B("u04", at="재고가", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], C("biz_smile"),
          say="국내 요소 재고가 사에서 오개월치라 수급이 안정됐다는 판단.", em=["5개월치"], fx=[("correct_ding", "안정됐다는", 0.5)]),
        L("같이 묶였던 주사기, 주사침 사재기 금지도 함께 끝남.",
          [B("u06", "Boxes of medical syringes on a pharmacy storage shelf, clean light, no readable text, no people")], C("drv_think", "r"), em=["주사기"]),
        L("고시 종료 뒤에도 재고와 가격은 계속 점검하겠습니다.",
          [B("u03", s0=1.2, s1=1.35)], C("biz_smile"), dialogue=True, speaker=2, emotion="normal"),
        L("디젤차 차주라면 트렁크에 한 통쯤 실어두는 사람도 많음.",
          [B("u07", "Open trunk of a diesel SUV with one white diesel exhaust fluid jug and a small organizer box, parking lot, daytime, no people")],
          C("drv_smile", "r"), em=["한 통쯤"]),
        L("님들 차에 요소수 미리 쟁여둠, 그때그때 삼?", [B("u01", s0=1.0, s1=1.1)], C("biz_q"), fx=[("pop_bubble", "삼")]),
    ]
    go(S, lines, "요소수 사재기 금지", "이번 달로 끝난다", "3월 중동전쟁 때 막은 매점매석 금지, 10월 31일 종료",
       "#요소수 사재기 금지 끝", "기획재정부 경제관계장관회의 2026-10-28 (세계일보 20261028516920, 연합뉴스TV MYH20261028201606ng1, 서울신문 20261029031004)",
       [("요소수, 요소 매점매석 금지 고시 3/27 시행, 10/31 종료", "세계일보, 연합뉴스TV, 서울신문"),
        ("중동전쟁 원료 수급 불안 대응, 물가안정법", "세계일보, 연합뉴스TV"),
        ("전년 월평균 판매량 200% 초과 물량 7일 이상 보관 금지", "세계일보"),
        ("국내 요소 재고 공공비축+민간 4~5개월분, 종료 후에도 재고, 가격 점검", "연합뉴스TV(대사는 정부 방침을 대사체로)"),
        ("주사기, 주사침 고시도 함께 종료", "세계일보, 연합뉴스TV"),
        ("네이버 데이터랩 쇼핑인사이트 자동차용품 인기검색어 1위 요소수(10/22~28)", "research_1029_newcar.md")],
       "중동전쟁 원료 수급 불안으로 3월부터 묶였던 요소수 매점매석 금지가 10월 31일로 끝납니다.\n정부는 국내 요소 재고가 4~5개월분이라 수급이 안정됐다고 봤습니다.\n종료 뒤에도 재고와 가격은 계속 점검합니다.\n\n#요소수 #디젤 #매점매석 #자동차용품 #란빵",
       "님들 차에 요소수 미리 쟁여둠, 그때그때 삼?",
       "요소수 10L, 요소수 주입 깔때기, 차량용 트렁크 정리함, 디젤 연료첨가제, 차량용 방향제",
       "기사에 쓸 만한 사진 없음, 전부 AI 배경(상표 없는 용기). 데이터랩 1위는 10/29 조사분 재사용.", [B("u07", s0=1.0, s1=1.1)])


EPS = [EP_stalkmis, EP_disabled3, EP_dealervat, EP_brakecheck, EP_doorscrape, EP_caymancut,
       EP_teslafsd89, EP_gv90tech, EP_zeekr7x, EP_ureaend]

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in EPS:
        if not want or f.__name__[3:] in want:
            f()
