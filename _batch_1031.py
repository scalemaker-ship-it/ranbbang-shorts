#!/usr/bin/env python3
"""란빵 2026-10-31 대상 daily 10편 (2026-10-30 15:00 launchd 실행).
- 보배드림 베스트 10/29~30 7편(busrage, armytruck, bbox142, ebikeseat, dumpmerge, slopepark, lane82)
  + 신차 minioxford, missions + 용품 parksafe(데이터랩 11위 주차번호판).
- 근거 = work/research_1031.md. 실사 원본 = work/_photos/b1031/ (map.txt). 캡처는 _batch_1027.cap() 로 얼굴 모자이크.
- 실명, 상호, 번호판 없음. 연예인 방문 사진(1044007) 안 씀. 캐릭터 없음(NO_CHAR).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1024 import B, C, L, build, IR, Y, W, R, P   # noqa: E402,F401
from _batch_1027 import cap as _cap   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos", "b1031")
BB = "사진: 보배드림"
BV = "화면: 보배드림"
MN = "사진: MINI 코리아"
PS = "사진: 포르쉐"
COMMON = "자동차 블랙박스 2채널, 블랙박스 메모리카드, 비상삼각대, 차량용 핸드폰 거치대, 차량용 방향제"
MAXC = 360


def cap(*a, **k):
    k.setdefault("ph", PH)
    return _cap(*a, **k)


def px(slug, name, boxes):
    """cap() 결과(1080x960) 위 좌표로 추가 모자이크(번호판, 노선 표시 등)."""
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


# ───────────────────────── 1. 버스 상향등 경적 ─────────────────────────
def EP_busrage():
    S = "busrage"
    for t in (30, 38, 41, 52):
        cap(S, f"f{t}", f"1043765_f{t}.jpg", nofaces=True)
    px(S, "f38", [(365, 245, 300, 85), (480, 695, 120, 40)])
    px(S, "f41", [(250, 150, 430, 95), (930, 630, 90, 35)])
    px(S, "f52", [(425, 245, 280, 85), (565, 700, 110, 35)])
    lines = [
        L("아니 저 바로 앞에서 우회전해야 된다고요.",
          [P("f38", BV, s0=1.0, s1=1.2)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("출퇴근 때만 버스전용인 차로에, 오후 두 시 반에 들어간 글쓴이.",
          [P("f30", BV, s0=1.0, s1=1.15)], None, em=["오후 두 시 반"]),
        L("300m 앞 주유소로 우회전하려던 거였음.",
          [B("b01", "A Korean roadside gas station entrance seen from a car on a wide suburban road, afternoon, cars passing")],
          None, say="삼백미터 앞 주유소로 우회전하려던 거였음.", em=["주유소로"]),
        L("근데 뒤에서 광역버스가 상향등을 켜고 경적을 계속 울려댐.",
          [P("f38", BV, s0=1.0, s1=1.15), P("f41", BV, at="경적을", s0=1.3, s1=1.5, fx=0.5, fy=0.45, punch=True)],
          None, em=["상향등", "경적을"], em_color="yellow", pop=("빵빵빵!!", R, "경적을"), shake="울려댐",
          fx=[("hit_trailer_epic", "경적을", 0.5)]),
        L("겁먹은 글쓴이는 시속 80에서 60까지 속도를 줄임.",
          [P("f41", BV, s0=1.2, s1=1.35)], None, say="겁먹은 글쓴이는 시속 팔십에서 육십까지 속도를 줄임.", em=["겁먹은"],
          info={"kind": "bars", "at": "시속", "title": "글쓴이 속도(제한 70)", "items": [
              {"label": "차로 변경 후", "num": 80, "suffix": "km/h", "at": "시속"},
              {"label": "겁나서 줄임", "num": 60, "suffix": "km/h", "at": "시속", "flash": "줄임"}]}),
        L("주유소로 붙는 순간까지 경적은 길게 이어짐.",
          [P("f52", BV, s0=1.0, s1=1.2)], None, em=["길게"], fx=[("wrong_gameshow_buzz", "길게", 0.45)]),
        L("다만 실선 구간에서 차로를 바꾼 건 본인도 인정함.",
          [B("b02", "A Korean multi-lane road where a white dashed lane line turns into a solid line, blue bus lane marking on the right, afternoon, seen from driver view")],
          None, em=["실선 구간"]),
        L("실선 변경은 저도 같이 처벌받겠습니다.",
          [B("b02", s0=1.3, s1=1.45, fx=0.6, fy=0.6)], None, dialogue=True, speaker=3, emotion="normal"),
        L("경적을 반복해서 울려 피해를 주는 건 도로교통법상 금지 행위.",
          [B("b03", "Close-up of a bus steering wheel horn pad and dashboard, interior of a red intercity bus, daylight, no people")],
          None, em=["금지 행위"], em_color="yellow", fx=[("drop_futuristic", "금지", 0.5)],
          info={"kind": "quotes", "at": "경적을", "title": "도로교통법 49조", "items": [
              {"text": "반복, 연속 경적 금지", "at": "금지"}]}),
        L("댓글은 신고하라는 쪽과, 왜 안 비켜줬냐는 쪽으로 갈림.",
          [P("f30", BV, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, em=["신고하라는"]),
        L("님들은 이 상황, 누가 더 잘못했다고 봄?", [P("f41", BV, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "잘못했다고")]),
    ]
    go(S, lines, "우회전하려는데", "버스가 상향등 경적", "버스전용 아닌 시간, 뒤 광역버스가 상향등에 연속 경적",
       "#버스가 경적 위협", "보배드림 베스트 1043765 교통사고/블박 (2026-10-29, 추천 70, 댓글 79, 조회 20400)",
       [("07~10시, 17~21시만 버스전용차로, 글쓴이는 14시 25분경 주행", "원글 본문"),
        ("300m 앞 우회전(주유소) 위해 차로 변경, 뒤 버스 상향등, 지속 경적", "원글 본문, 첨부 영상"),
        ("80km/h 까지 가속 후 겁나서 60km/h 로 줄임(제한 70)", "원글 본문"),
        ("점선이 실선으로 바뀌는 구간에서 변경, 안전신문고에 같이 처벌받겠다고 기재", "원글 본문(대사는 본문을 대사체로)"),
        ("반복, 연속 경적으로 피해 주는 소음 금지", "도로교통법 49조 1항 8호 다목(casenote 원문)"),
        ("댓글 '신고하세요'(43) vs '왜 안 비켜주는 거에요?'(반대 37)", "원글 댓글")],
       "버스전용차로 시간이 아닌 오후, 우회전하려고 들어간 차 뒤에서 광역버스가 상향등에 경적을 계속 울렸습니다.\n글쓴이는 실선 변경은 같이 처벌받겠다며 신고했습니다.\n반복, 연속 경적은 도로교통법상 금지 행위입니다.\n\n#버스전용차로 #경적 #블랙박스 #보배드림 #란빵",
       "님들은 이 상황, 누가 더 잘못했다고 봄?", COMMON,
       "영상 정지 프레임의 버스 번호판, 노선 표시는 모자이크. 버스 회사명 안 씀.", [P("f52", BV, s0=1.0, s1=1.1)])


# ───────────────────────── 2. 공군 픽업트럭 1차로 ─────────────────────────
def EP_armytruck():
    S = "armytruck"
    cap(S, "truck", "1043818_00.jpg", nofaces=True, cx=0.45, cy=0.6, boxes=[(410, 890, 225, 85)])
    cap(S, "truckfit", "1043818_00.jpg", nofaces=True, fit=True, boxes=[(410, 890, 225, 85)])
    lines = [
        L("국방의 의무 중인 차를 신고한다고요?",
          [P("truck", BB, s0=1.0, s1=1.2)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("고속도로 1차로를 수십 킬로 동안 달리던 공군 픽업트럭.",
          [P("truckfit", BB, s0=1.0, s1=1.1), P("truck", BB, at="공군", s0=1.3, s1=1.5, fx=0.45, fy=0.5, punch=True)],
          None, say="고속도로 일차로를 수십 킬로 동안 달리던 공군 픽업트럭.", em=["공군 픽업트럭"]),
        L("운전자는 폰까지 보면서 1차로를 안 비켰다고 함.",
          [B("a01", "View from behind of a dark pickup truck driving in the leftmost lane of a Korean expressway, concrete median barrier, overcast autumn day")],
          None, say="운전자는 폰까지 보면서 일차로를 안 비켰다고 함.", em=["폰까지"], fx=[("wrong_gameshow_buzz", "폰까지", 0.45)]),
        L("급한 작전 차량도 아닌데 지정차로 위반으로 신고되냐는 글.",
          [P("truck", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.55)], None, em=["지정차로 위반"]),
        L("댓글은 딱 반반으로 갈림.",
          [B("a02", "A Korean expressway with traffic in multiple lanes seen from a car, autumn hills, overcast, a dark pickup far ahead in the left lane")],
          None, em=["반반으로"], fx=[("drum_rimshot", "반반으로", 0.45)]),
        L("민간인은 밥 벌어먹고 안 사나요?",
          [B("a02", s0=1.3, s1=1.45, fx=0.4, fy=0.5)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("법을 보면, 긴급자동차 특례 목록에 지정차로는 아예 없음.",
          [B("a03", "An open Korean traffic law book on a desk next to a car key, warm desk lamp light, pages blurred, no readable text")],
          None, em=["아예 없음"], em_color="yellow", pop=("특례 없음!", Y, "아예"), fx=[("hit_trailer_epic", "아예", 0.5)],
          info={"kind": "quotes", "at": "법을", "title": "긴급자동차 특례(30조)", "items": [
              {"text": "속도, 앞지르기, 신호 등", "at": "특례"}, {"text": "지정차로는 없음", "at": "아예"}]}),
        L("게다가 특례는 사이렌이나 경광등을 켜고 긴급하게 달릴 때 얘기.",
          [B("a04", "Close-up of a red and blue emergency light bar on the roof of a vehicle, turned off, daylight, highway background blurred")],
          None, em=["경광등을"]),
        L("사진 속 트럭엔 켜진 경광등이 안 보임.",
          [P("truck", BB, s0=1.3, s1=1.5, fx=0.5, fy=0.3, punch=True)], None, em=["안 보임"]),
        L("님들은 군 차량도 똑같이 신고해야 한다고 봄?", [P("truckfit", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "신고해야")]),
    ]
    go(S, lines, "1차로 계속 달린", "공군 트럭 신고 될까?", "급한 작전 아닌 공군 픽업트럭 1차로 주행, 지정차로 신고 논쟁",
       "#공군 트럭 1차로", "보배드림 베스트 1043818 교통사고/블박 (2026-10-29, 추천 49, 댓글 58, 조회 10851)",
       [("공군 픽업트럭이 고속도로 1차로 수십 km 주행, 운전자 폰 사용", "원글 본문, 첨부 사진"),
        ("급한 작전 차량 아닌 것 같은데 지정차로 위반 신고 되나", "원글 본문"),
        ("댓글 '국방의 의무 수행 중인 차를 신고?'(25/반대 24), '민간인은 밥 벌어먹고 안 사나요?'(20/반대 20)", "원글 댓글(대사 2줄은 댓글 인용)"),
        ("긴급자동차 특례 목록(속도, 앞지르기, 끼어들기, 신호 등 12개)에 지정차로(14조) 없음", "도로교통법 30조(casenote 원문)"),
        ("특례는 사이렌, 경광등 켰을 때 적용", "도로교통법 시행령 3조(casenote 판례 인용)"),
        ("범칙금 액수는 확인 안 해 대본에서 뺌", "제작 메모")],
       "공군 픽업트럭이 고속도로 1차로를 수십 킬로 달렸다는 글에 지정차로 위반 신고 논쟁이 붙었습니다.\n도로교통법 긴급자동차 특례 목록에 지정차로는 없습니다.\n특례도 사이렌이나 경광등을 켰을 때 얘기입니다.\n\n#지정차로 #1차로 #군용차 #보배드림 #란빵",
       "님들은 군 차량도 똑같이 신고해야 한다고 봄?", COMMON,
       "첨부 사진 번호판 전체 모자이크(원글은 일부만 가림).", [P("truck", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 3. 블랙박스 142만원 ─────────────────────────
def EP_bbox142():
    S = "bbox142"
    cap(S, "form", "1044007_00.jpg", box=(0, 0, 1600, 1100), fit=True, nofaces=True)
    cap(S, "form2", "1044007_00.jpg", box=(0, 900, 1600, 2134), fit=True, nofaces=True)
    lines = [
        L("네이버만 봐도 120만원 나오는 제품이에요.",
          [B("x01", "Interior of a small car electronics shop in Korea: dashcam boxes on a glass counter, a card terminal, fluorescent light", s0=1.1, s1=1.3)],
          None, dialogue=True, speaker=2, emotion="normal", say="네이버만 봐도 백이십마넌 나오는 제품이에요."),
        L("아버지가 동네 용품점에서 블랙박스를 바꾸고 오심.",
          [B("x02", "A new dashcam mounted behind the windshield of a parked mid-size sedan, cables tucked, daytime, shop bay")],
          None, em=["블랙박스를"]),
        L("자식이 결제 내역을 보니 142만원.",
          [P("form", BB, s0=1.0, s1=1.15), P("form", BB, at="142만원", s0=1.3, s1=1.5, fx=0.5, fy=0.4, punch=True)],
          None, say="자식이 결제 내역을 보니 백사십이마넌.", em=["142만원"], em_color="yellow",
          pop=("142만원?!", R, "142만원"), shake="142만원", fx=[("hit_trailer_epic", "142만원", 0.5)]),
        L("공임 포함 30에서 40만원이면 될 줄 알았다고 함.",
          [B("x03", "A dashcam product box and a receipt on a car passenger seat, close-up, daylight, numbers blurred")],
          None, say="공임 포함 삼십에서 사십마넌이면 될 줄 알았다고 함.", em=["공임 포함"]),
        L("알고 보니 회원제 멤버십을 묶어 비싸게 파는 방식이었음.",
          [P("form", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.2)], None, em=["회원제 멤버십"], fx=[("wrong_gameshow_buzz", "회원제", 0.45)]),
        L("환불해 달라니 이미 설치해서 안 되고 위약금이 생긴다는 답.",
          [P("form2", BB, s0=1.0, s1=1.15)], None, em=["위약금이"]),
        L("중재를 부탁해 부가서비스를 빼고 100만원에 다시 결제함.",
          [B("x04", "A card payment terminal and cash envelope on a shop counter, close-up, warm light, numbers blurred")],
          None, say="중재를 부탁해 부가서비스를 빼고 백마넌에 다시 결제함.", em=["100만원에"],
          info={"kind": "bars", "at": "중재를", "title": "같은 블랙박스", "items": [
              {"label": "처음 결제", "num": 142, "suffix": "만원", "at": "중재를"},
              {"label": "재결제", "num": 100, "suffix": "만원", "at": "100만원에", "flash": "100만원에"}]}),
        L("글쓴이는 다른 회사 최고급 4채널도 60에서 70만원대라고 함.",
          [B("x05", "Several dashcam boxes lined up on an electronics store shelf, price tags blurred, bright store light")],
          None, say="글쓴이는 다른 회사 최고급 사채널도 육십에서 칠십마넌대라고 함.", em=["최고급 4채널도"], em_color="yellow",
          fx=[("drop_futuristic", "최고급", 0.5)]),
        L("매장엔 연예인 방문 사진이 잔뜩 걸려 있었다고 함.",
          [B("x06", "Wall of a small Korean car accessory shop covered with framed photos and banners, faces not visible, all photos blurred, fluorescent light")],
          None, em=["연예인 방문 사진이"], fx=[("drum_rimshot", "잔뜩", 0.45)]),
        L("님들은 부모님 차 용품, 어디서 달아드림?", [P("form", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "달아드림")]),
    ]
    go(S, lines, "아버지 블랙박스 교체", "결제는 142만원?", "회원제 묶음 142만원, 항의 끝에 100만원 재결제",
       "#블랙박스 142만원", "보배드림 베스트 1044007 교통사고/블박 (2026-10-30, 추천 29, 댓글 4)",
       [("10/26 아버지가 동네 용품점에서 4채널 블랙박스 교체, 총 142만원", "원글 본문, 첨부 계약서"),
        ("업체 '네이버 검색만 해봐도 120만원 나오는 제품'", "원글 본문(대사는 업체 발언 그대로)"),
        ("오프라인 전용 고가 + 회원제/멤버십 묶음 판매", "원글 본문"),
        ("환불 요구 → '설치돼서 환불 불가, 위약금'", "원글 본문"),
        ("중재 후 AS, SD카드 교체 등 부가서비스 빼고 현금 100만원 재결제", "원글 본문"),
        ("타사 최고급 4채널도 60~70만원대(글쓴이 주장)", "원글 본문"),
        ("업체가 연예인 방문 사진으로 홍보", "원글 본문(사진은 안 씀)")],
       "아버지가 동네 매장에서 바꾼 블랙박스, 결제 금액은 142만원이었습니다.\n회원제 멤버십을 묶은 판매 방식이었고, 항의 끝에 부가서비스를 빼고 100만원에 재결제했습니다.\n계약 전 모델명과 온라인 가격을 꼭 비교해 보세요.\n\n#블랙박스 #회원제 #소비자피해 #보배드림 #란빵",
       "님들은 부모님 차 용품, 어디서 달아드림?",
       "자동차 블랙박스 4채널, 자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 핸드폰 거치대, 차량용 방향제",
       "계약서 사진은 원글이 개인정보, 상호를 가린 상태 그대로. 연예인 방문 사진 4장과 매장 상호, 지역, 모델명은 안 씀.", [B("x02", s0=1.0, s1=1.1)])


# ───────────────────────── 4. 비접촉 전기자전거 ─────────────────────────
def EP_ebikeseat():
    S = "ebikeseat"
    cap(S, "bike", "1044028_00.png", box=(0, 220, 1179, 2310), fit=True)
    cap(S, "bikec", "1044028_00.png", box=(0, 700, 1179, 1900), cx=0.5, cy=0.5)
    lines = [
        L("자전거 지나가면 멈췄다 가야지 뭐 하는 거야!",
          [P("bikec", BB, s0=1.0, s1=1.2)], None, dialogue=True, speaker=3, emotion="angry"),
        L("쇼핑몰 주차장으로 천천히 우회전하던 차 옆에서 전기자전거가 넘어짐.",
          [P("bike", BB, s0=1.0, s1=1.15), P("bikec", BB, at="전기자전거가", s0=1.2, s1=1.4, punch=True)],
          None, em=["전기자전거가"]),
        L("차랑 닿은 데는 없는 비접촉 상황.",
          [B("e01", "A sedan stopped at the entrance ramp of a shopping mall parking lot at night, an electric bicycle lying on the sidewalk beside it, street lights")],
          None, em=["비접촉"], em_color="yellow", fx=[("drop_futuristic", "비접촉", 0.5)]),
        L("다친 데 없다길래 차에 탔는데, 갑자기 차를 손으로 내리침.",
          [B("e01", at="갑자기", s0=1.3, s1=1.5, fx=0.45, fy=0.5, punch=True)], None, em=["내리침"],
          shake="내리침", fx=[("hit_trailer_epic", "내리침", 0.5)]),
        L("그러더니 자전거 안장이 고장 났다며 수리비를 요구함.",
          [B("e02", "Close-up of a slightly tilted electric bicycle saddle on a sidewalk at night, street light")], None, em=["수리비를"]),
        L("112를 부르자 경찰이 와서 사건을 접수함.",
          [B("e03", "A Korean police patrol car parked near a shopping mall parking entrance at night, lights off, no people")],
          None, say="백십이를 부르자 경찰이 와서 사건을 접수함.", em=["사건을 접수함"]),
        L("안장값 드리겠다니까, 경찰 불렀으니 이젠 싫다고 함.",
          [B("e03", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], None, em=["이젠 싫다고"], fx=[("wrong_gameshow_buzz", "싫다고", 0.45)]),
        L("본인 입으로는 브레이크를 잡다가 넘어졌다고 했다는데.",
          [P("bike", BB, s0=1.2, s1=1.35, fx=0.4, fy=0.5)], None, em=["브레이크를"]),
        L("경찰은 CCTV를 보고 넘어지게 만들었으면 가해자라고 함.",
          [B("e04", "A CCTV camera mounted on a shopping mall exterior wall overlooking a parking entrance at night")],
          None, say="경찰은 씨씨티비를 보고 넘어지게 만들었으면 가해자라고 함.", em=["가해자라고"], em_color="yellow",
          pop=("가해자?!", R, "가해자라고"), fx=[("drum_rimshot", "가해자라고", 0.45)]),
        L("근데 글쓴이 블박엔 자전거가 오는 게 안 보였음.",
          [B("e05", "Dashcam style view from inside a car turning right into a parking lot at night, sidewalk on the right, empty, street lights")],
          None, em=["안 보였음"]),
        L("님들은 안 부딪혔는데 물어줘야 한다고 봄?", [P("bike", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "물어줘야")]),
    ]
    go(S, lines, "닿지도 않았는데", "자전거 안장값 내라?", "비접촉 전기자전거 혼자 넘어짐, 경찰 사건 접수",
       "#안 부딪혔는데 수리비", "보배드림 베스트 1044028 자유게시판 (2026-10-30, 추천 25, 댓글 18)",
       [("쇼핑몰 주차장 서행 우회전 중 옆 인도에 전기자전거 넘어짐, 비접촉", "원글 본문, 첨부 사진"),
        ("'전기자전거가 지나가는데 멈췄다가 지나가고 가야지 뭐하는 거냐'", "원글 본문(대사는 본문 인용을 줄임)"),
        ("다친 데 없다 해서 탔는데 차를 손으로 내리침, 안장 수리비 요구", "원글 본문"),
        ("112 → 경찰 사건 접수, 안장값 주겠다니 '경찰 불렀으니 이젠 싫다'", "원글 본문"),
        ("본인이 브레이크를 잡아 넘어졌다고 말함, 글쓴이 블박엔 자전거 안 보임", "원글 본문"),
        ("경찰 '상가 CCTV 보고 넘어진 거 유발했으면 가해자'", "글쓴이 댓글")],
       "쇼핑몰 주차장에 들어가던 차 옆에서 전기자전거가 혼자 넘어졌습니다.\n닿은 데는 없었지만 상대는 안장 수리비를 요구했고 경찰이 사건을 접수했습니다.\n경찰은 CCTV로 넘어짐을 유발했는지 본다고 했습니다.\n\n#비접촉사고 #전기자전거 #과실 #보배드림 #란빵",
       "님들은 안 부딪혔는데 물어줘야 한다고 봄?", COMMON,
       "첨부 사진의 행인은 다리만 보임(얼굴 없음). 쇼핑몰 이름 안 씀.", [P("bikec", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 5. 덤프 합류 추돌 2:8 ─────────────────────────
def EP_dumpmerge():
    S = "dumpmerge"
    cap(S, "car", "1043939_00.jpg", nofaces=True, cy=0.55)
    cap(S, "scr", "1043939_01.jpg", nofaces=True, cx=0.5, cy=0.5)
    cap(S, "r48", "1043939_f48.jpg", box=(180, 203, 540, 406), fit=True, nofaces=True)
    cap(S, "r63", "1043939_f63.jpg", box=(180, 203, 540, 406), fit=True, nofaces=True)
    cap(S, "fr", "1043939_f52.jpg", box=(180, 0, 540, 203), fit=True, nofaces=True)
    px(S, "r48", [(465, 725, 250, 50)])
    px(S, "r63", [(895, 505, 100, 40)])
    px(S, "fr", [(330, 540, 170, 70)])
    lines = [
        L("제가 피해자고, 과실은 2대 8입니다.",
          [P("r63", BV, s0=1.0, s1=1.2)], None, dialogue=True, speaker=2, emotion="normal", say="제가 피해자예요. 과실은 이대팔입니다."),
        L("톨게이트 지나 길이 좁아지는 구간, 꽉 막혀 거의 기어가던 상황.",
          [P("fr", BV, s0=1.0, s1=1.15)], None, em=["좁아지는 구간"]),
        L("글쓴이 아내 차는 한참 전부터 2차로 직진만 하던 중.",
          [P("car", BB, s0=1.0, s1=1.15)], None, say="글쓴이 아내 차는 한참 전부터 이차로 직진만 하던 중.", em=["직진만"]),
        L("그때 뒤쪽 덤프트럭이 억지로 합류하며 차 뒤 옆구리를 긁음.",
          [P("r48", BV, s0=1.0, s1=1.15), P("scr", BB, at="옆구리를", s0=1.1, s1=1.3, punch=True)],
          None, em=["옆구리를"], em_color="yellow", shake="긁음", fx=[("hit_trailer_epic", "긁음", 0.5)]),
        L("덤프 측은 처음에 자기가 피해자라며 2대 8을 주장함.",
          [P("car", BB, s0=1.3, s1=1.5, fx=0.75, fy=0.35, punch=True)], None,
          say="덤프 측은 처음에 자기가 피해자라며 이 대 팔을 주장함.", em=["자기가 피해자라며"], fx=[("wrong_gameshow_buzz", "피해자라며", 0.45)]),
        L("괘씸해서 경찰에 접수하자 말이 6대 4로 바뀜.",
          [B("d01", "A Korean police station traffic accident report desk with forms and a pen, fluorescent light, no people, no readable text")],
          None, say="괘씸해서 경찰에 접수하자 말이 육 대 사로 바뀜.", em=["바뀜"], em_color="yellow", pop=("말 바꿈?!", R, "바뀜"),
          fx=[("drum_rimshot", "바뀜", 0.45)],
          info={"kind": "compare", "at": "괘씸해서", "title": "덤프 측 주장", "items": [
              {"label": "처음", "color": R, "at": "괘씸해서", "rows": [["덤프", "2", W], ["아내 차", "8", Y]]},
              {"label": "경찰 접수 후", "color": W, "at": "바뀜", "rows": [["덤프", "6", Y], ["아내 차", "4", W]]}]}),
        L("보험사도 아내 쪽 과실이 있다는 식으로 말함.",
          [B("d02", "A smartphone on a car dashboard showing an insurance company call screen, blurred, evening light, no readable text")], None, em=["보험사도"]),
        L("뒤에서 들이미는 걸 대체 어떻게 피하나요?",
          [P("scr", BB, s0=1.2, s1=1.35)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("댓글 대부분은 블박차 과실이 대체 뭐냐는 반응.",
          [P("r48", BV, s0=1.2, s1=1.35, fx=0.6, fy=0.5)], None, em=["대체 뭐냐는"]),
        L("덤프가 뒤 세단을 제치려다 옆 차를 친 거라는 분석도 나옴.",
          [P("r63", BV, s0=1.2, s1=1.35, fx=0.6, fy=0.5)], None, em=["제치려다"]),
        L("님들은 이거 몇 대 몇이라고 봄?", [P("car", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "몇이라고")]),
    ]
    go(S, lines, "뒤에서 덤프가 긁고", "과실은 2대8 주장", "톨게이트 합류 구간 덤프 후측방 접촉, 2:8에서 6:4로 말 바꿈",
       "#덤프가 박고 2:8", "보배드림 베스트 1043939 교통사고/블박 (2026-10-29, 추천 16, 댓글 31)",
       [("톨게이트 지나 좁아지는 곳, 정체 서행, 아내 차 2차로 계속 직진", "원글 본문"),
        ("뒤 덤프트럭이 무리하게 합류하며 후측방 접촉, 첨부 사진 2장, 블박 영상", "원글 본문, 첨부"),
        ("덤프 측 '본인 피해자, 2:8' → 경찰 접수 후 '6:4'", "원글 본문(대사는 상대 주장을 대사체로)"),
        ("보험사도 과실이 있다는 식", "원글 본문"),
        ("'뒤에서 들이미는 걸 어떻게 대처하나'", "원글 본문(대사는 본문 질문을 대사체로)"),
        ("댓글 '덤프가 뒤 세단 제끼려다 블박차 후측방 추돌, 블박 과실이 뭘까'(13)", "원글 댓글")],
       "톨게이트 지나 좁아지는 구간, 2차로로 직진하던 차를 뒤에서 덤프트럭이 긁었습니다.\n덤프 측은 처음엔 2:8을, 경찰 접수 뒤엔 6:4를 주장했습니다.\n댓글은 블박차 과실이 어디 있냐는 반응이 대부분입니다.\n\n#과실비율 #덤프트럭 #블랙박스 #보배드림 #란빵",
       "님들은 이거 몇 대 몇이라고 봄?", COMMON,
       "차 사진은 원글이 번호판을 가린 상태 그대로, 영상 프레임 번호판 확인 후 추가 모자이크.", [P("car", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 6. 내리막 이중주차 ─────────────────────────
def EP_slopepark():
    S = "slopepark"
    cap(S, "wall", "1043934_00.jpg", box=(50, 830, 1035, 1790), nofaces=True)
    cap(S, "post", "1043934_00.jpg", box=(0, 560, 1080, 1800), fit=True, nofaces=True)
    cap(S, "cmt", "1043934_01.jpg", box=(0, 1660, 1080, 1960), fit=True, nofaces=True)
    px(S, "post", [(155, 25, 120, 45)])
    lines = [
        L("블박도 CCTV도 있으니 경찰서 가기 싫으면 연락 주세요.",
          [P("post", BB, s0=1.0, s1=1.15)], None, dialogue=True, speaker=2, emotion="normal",
          say="블박도 씨씨티비도 있으니 경찰서 가기 싫으면 연락 주세요."),
        L("아파트 지하주차장 살짝 내리막에 이중주차를 해둔 차주가 올린 공지.",
          [B("p01", "A Korean apartment underground parking garage with a slight downhill slope, a car double-parked in the aisle, fluorescent light")],
          None, em=["살짝 내리막에"]),
        L("자기 차를 벽에 박아놓고 사라진 아주머니를 찾는다는 내용.",
          [P("wall", BB, s0=1.0, s1=1.15), P("wall", BB, at="벽에", s0=1.3, s1=1.5, fx=0.7, fy=0.6, punch=True)],
          None, em=["사라진 아주머니를"]),
        L("근데 사정을 들어보니 반전이 있었음.",
          [P("wall", BB, s0=1.2, s1=1.35, fx=0.6, fy=0.5)], None, em=["반전이"], fx=[("drum_rimshot", "반전이", 0.45)]),
        L("아주머니가 막힌 차를 밀자 내리막이라 차가 굴러가 버림.",
          [B("p01", at="굴러가", s0=1.3, s1=1.5, fx=0.5, fy=0.55, punch=True)], None, em=["굴러가 버림"], em_color="yellow",
          fx=[("hit_trailer_epic", "굴러가", 0.5)]),
        L("아주머니는 벽 사이에 끼면서 몸으로 차를 막았다고 함.",
          [P("cmt", BB, s0=1.0, s1=1.1)], None, em=["몸으로"], em_color="yellow", pop=("몸으로?!", R, "몸으로"), shake="막았다고"),
        L("관리사무소 연락엔 잘못 없으니 연락하지 말라고 함.",
          [P("cmt", BB, s0=1.15, s1=1.3, fx=0.5, fy=0.6)], None, em=["연락하지 말라고"]),
        L("보배 회원들은 오히려 차주가 위험하다는 반응.",
          [B("p02", "Front of a car pressed against a concrete pillar wall in an underground parking garage, small scrape, fluorescent light, no people")],
          None, em=["차주가 위험하다는"]),
        L("평지 아닌 곳에 이중주차한 사람도 과실이 들어간다는 댓글이 많음.",
          [B("p02", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], None, em=["과실이 들어간다는"], fx=[("drop_futuristic", "과실이", 0.5)]),
        L("님들은 이거 누가 물어줘야 한다고 봄?", [P("wall", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "물어줘야")]),
    ]
    go(S, lines, "내리막 이중주차", "밀어준 사람이 범인?", "중립 이중주차 차가 굴러 벽 충돌, 차주는 밀던 아주머니 찾는 중",
       "#이중주차 밀다 쾅", "보배드림 베스트 1043934 교통사고/블박 (2026-10-29, 추천 72, 댓글 10)",
       [("아파트 앱 게시판: 지하주차장 이중주차한 차를 벽에 박아놓고 잠수 탄 아줌마, 블박, CCTV 있으니 연락 달라", "원글 첨부 캡처 1(대사는 공지 인용)"),
        ("살짝 내리막이라 차가 굴러감, 아주머니가 벽에 끼며 차를 막음, 차를 위로 안 올려놓고 벽에 박힌 채 둠", "원글 첨부 캡처 2(차주 댓글)"),
        ("관리사무소 연락에 아주머니 '잘못 없다, 연락하지 마라'", "원글 첨부 캡처 2"),
        ("보배 글쓴이 '아줌마가 대인하면 역관광'", "원글 본문"),
        ("댓글 '평지가 아닌 곳에 이중주차한 사람 과실 들어감'(13)", "원글 댓글"),
        ("아주머니 부상 여부는 원글에 없음 → 다쳤다고 안 씀", "제작 메모")],
       "내리막 지하주차장에 이중주차한 차를 밀던 아주머니, 차가 굴러가자 벽 사이에 끼며 몸으로 막았습니다.\n차주는 차를 벽에 박아두고 사라졌다며 연락하라는 공지를 올렸습니다.\n평지가 아닌 곳의 이중주차는 차주 과실도 들어간다는 댓글이 많습니다.\n\n#이중주차 #내리막 #주차장 #보배드림 #란빵",
       "님들은 이거 누가 물어줘야 한다고 봄?",
       "비상삼각대, 자동차 블랙박스 2채널, 차량용 주차번호판, 타이어 고임목, 차량용 방향제",
       "앱 캡처의 닉네임, 동 번호는 잘라내거나 원글 모자이크 그대로. 아파트 이름 안 씀.", [P("wall", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 7. 블박 빼둔 날 8:2 ─────────────────────────
def EP_lane82():
    S = "lane82"
    cap(S, "acc", "1043816_00.jpg", cx=0.4, cy=0.55, nofaces=True)
    cap(S, "accfit", "1043816_00.jpg", fit=True, nofaces=True)
    px(S, "acc", [(0, 220, 260, 390)])
    px(S, "accfit", [(0, 190, 240, 170)])
    lines = [
        L("끼어들려는데 그쪽이 속도를 내서 들어왔잖아요.",
          [P("accfit", BB, s0=1.0, s1=1.15)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("2차로를 시속 30에서 40으로 직진하던 글쓴이 차를 옆 차가 박음.",
          [P("acc", BB, s0=1.0, s1=1.15)], None, say="이차로를 시속 삼십에서 사십으로 직진하던 글쓴이 차를 옆 차가 박음.", em=["직진하던"]),
        L("상대는 깜빡이도 없이 실선이 안전지대로 바뀌는 구간에서 들어옴.",
          [B("l01", "A Korean intersection approach at night with a solid white lane line turning into a striped safety zone, wet asphalt, street lights, no cars")],
          None, em=["깜빡이도 없이"], fx=[("wrong_gameshow_buzz", "깜빡이도", 0.45)]),
        L("글쓴이 차 뒷좌석 쪽을 그대로 들이받음.",
          [P("acc", BB, at="뒷좌석", s0=1.3, s1=1.5, fx=0.45, fy=0.5, punch=True)], None, em=["뒷좌석 쪽을"], shake="들이받음",
          fx=[("hit_trailer_epic", "들이받음", 0.5)]),
        L("100대 0일 줄 알았는데 상대 보험사는 8대 2를 주장함.",
          [P("accfit", BB, s0=1.2, s1=1.35)], None, say="백 대 영일 줄 알았는데 상대 보험사는 팔 대 이를 주장함.", em=["8대 2를"], em_color="yellow",
          info={"kind": "compare", "at": "100대", "title": "과실 비율", "items": [
              {"label": "글쓴이 생각", "color": W, "at": "100대", "rows": [["상대", "100", Y], ["글쓴이", "0", W]]},
              {"label": "상대 보험사", "color": R, "at": "8대", "rows": [["상대", "80", W], ["글쓴이", "20", Y]]}]}),
        L("문제는 하필 그날 글쓴이 차에 블박이 없었다는 것.",
          [B("l02", "Empty dashcam mount bracket on a car windshield with a dangling power cable, night, interior view, no people")],
          None, em=["블박이 없었다는"], em_color="yellow", pop=("블박 없음?!", R, "블박이"), fx=[("drum_rimshot", "없었다는", 0.45)]),
        L("거치대가 깨져서 잠깐 빼둔 사이에 사고가 났음.",
          [B("l02", at="거치대가", s0=1.3, s1=1.5, fx=0.5, fy=0.4, punch=True)], None, em=["잠깐 빼둔"]),
        L("상대 차엔 블박이 있는데, 영상을 달라고 해도 안 준다고 함.",
          [B("l03", "A dashcam glowing on the windshield of a dark car parked at night by a road, close-up, no people")],
          None, em=["안 준다고"]),
        L("댓글은 사진만 보면 100대 0이라는 쪽이 많음.",
          [P("acc", BB, s0=1.2, s1=1.35, fx=0.55, fy=0.5)], None, say="댓글은 사진만 보면 백 대 영이라는 쪽이 많음.", em=["사진만 보면"]),
        L("주변 차 블박이나 CCTV를 꼭 구하라는 조언도 이어짐.",
          [B("l04", "A traffic CCTV camera on a pole above a Korean intersection at night, street lights, no people")],
          None, say="주변 차 블박이나 씨씨티비를 꼭 구하라는 조언도 이어짐.", em=["꼭 구하라는"]),
        L("님들은 블박 없으면 과실 안고 가야 한다고 봄?", [P("accfit", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "안고")]),
    ]
    go(S, lines, "실선에서 끼어들다 쾅", "블박 없으면 8대2?", "깜빡이 없이 실선 구간 변경한 차가 추돌, 상대 보험사 8:2",
       "#블박 빼둔 날 사고", "보배드림 베스트 1043816 교통사고/블박 (2026-10-29, 추천 20, 댓글 23)",
       [("2차로 30~40km 정속 직진, 1차로는 교차로 진입차로, 실선에서 안전지대로 바뀌는 구간", "원글 본문"),
        ("상대 깜빡이 없이 진입, 뒷좌석 쪽 추돌, 상대 보험사 8:2", "원글 본문, 첨부 사진"),
        ("상대 주장 '차선변경하려는데 제가 속도를 내서 들어왔다'", "글쓴이 댓글(대사는 상대 주장을 대사체로)"),
        ("블박 거치대가 깨져 잠깐 빼놓은 사이 사고, 상대 차 블박은 있으나 영상 안 줌", "글쓴이 댓글"),
        ("댓글 '사진만 보면 100:0', '주위 차량 블랙박스 구해보세요'", "원글 댓글")],
       "실선이 안전지대로 바뀌는 구간, 깜빡이 없이 들어온 차가 뒷좌석 쪽을 박았습니다.\n상대 보험사는 8:2를 주장하고, 하필 그날 글쓴이 차는 블박 거치대가 깨져 블박을 빼둔 상태였습니다.\n상대 차 블박 영상은 아직 못 받았습니다.\n\n#과실비율 #블랙박스 #차선변경 #보배드림 #란빵",
       "님들은 블박 없으면 과실 안고 가야 한다고 봄?",
       "자동차 블랙박스 2채널, 블랙박스 거치대, 블랙박스 메모리카드, 차량용 핸드폰 거치대, 차량용 방향제",
       "사고 사진 번호판은 원글이 가린 상태 그대로, 멀리 선 사람은 뒷모습(얼굴 검출 시 모자이크).", [P("acc", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 8. MINI 옥스포드 에디션 ─────────────────────────
def EP_minioxford():
    S = "minioxford"
    cap(S, "front", "mini_0.jpg", nofaces=True, cx=0.48)
    cap(S, "top", "mini_3.webp", box=(0, 100, 800, 598), nofaces=True, fit=True)
    cap(S, "rear", "mini_4.webp", box=(0, 100, 800, 532), nofaces=True, cx=0.42)
    cap(S, "inside", "mini_5.webp", box=(0, 90, 800, 507), nofaces=True, cx=0.5)
    cap(S, "frontfit", "mini_0.jpg", nofaces=True, fit=True)
    px(S, "front", [(455, 600, 190, 50)])
    px(S, "frontfit", [(455, 570, 145, 45)])
    px(S, "rear", [(575, 345, 255, 60)])
    lines = [
        L("와, 지붕에 영국 국기를 통째로 둘렀네?",
          [P("top", MN, s0=1.0, s1=1.2)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("미니가 국내에 딱 30대만 파는 한정판을 31일 출시함.",
          [P("frontfit", MN, s0=1.0, s1=1.15), P("front", MN, at="30대만", s0=1.2, s1=1.4, fx=0.5, fy=0.5, punch=True)],
          None, say="미니가 국내에 딱 삼십대만 파는 한정판을 삼십일일 출시함.", em=["30대만"], em_color="yellow",
          pop=("30대 한정!", Y, "30대만"), fx=[("drop_futuristic", "30대만", 0.5)]),
        L("이름은 쿠퍼 옥스포드 에디션.",
          [P("front", MN, s0=1.1, s1=1.25)], None, em=["옥스포드 에디션"]),
        L("옥스포드는 1959년 클래식 미니가 처음 만들어진 곳.",
          [P("rear", MN, s0=1.0, s1=1.15)], None, say="옥스포드는 천구백오십구년 클래식 미니가 처음 만들어진 곳.", em=["처음 만들어진"]),
        L("새 미니를 거기서 만든 지 25년 된 걸 기념한 차임.",
          [P("rear", MN, at="25년", s0=1.2, s1=1.4, fx=0.5, fy=0.45, punch=True)], None, say="새 미니를 거기서 만든 지 이십오년 된 걸 기념한 차임.", em=["25년"]),
        L("남색 차체에 유니언 잭 지붕, 빨간 줄이 보닛부터 트렁크까지 이어짐.",
          [P("top", MN, s0=1.2, s1=1.4, fx=0.4, fy=0.5)], None, em=["유니언 잭 지붕"], em_color="yellow"),
        L("실내도 파란 직물 대시보드에 체커기 무늬 매트까지 전용임.",
          [P("inside", MN, s0=1.0, s1=1.2)], None, em=["체커기 무늬"]),
        L("엔진은 163마력, 시속 100킬로까지 7.7초.",
          [P("frontfit", MN, s0=1.2, s1=1.35)], None, say="엔진은 백육십삼마력, 시속 백킬로까지 칠점칠초.", em=["163마력"],
          info={"kind": "bars", "at": "엔진은", "title": "옥스포드 에디션", "items": [
              {"label": "최고출력", "num": 163, "suffix": "마력", "at": "엔진은"},
              {"label": "0→100km/h", "num": 7.7, "dec": 1, "suffix": "초", "at": "7.7초", "flash": "7.7초"}]}),
        L("근데 가격은 4420만원.",
          [P("front", MN, s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], None, say="근데 가격은 사천사백이십마넌.", em=["4420만원"], em_color="yellow",
          pop=("4420만원!", R, "4420만원"), shake="4420만원", fx=[("hit_trailer_epic", "4420만원", 0.5)]),
        L("실차는 31일부터 이틀간 영종도 미니 행사에서 처음 공개됨.",
          [P("rear", MN, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, say="실차는 삼십일일부터 이틀간 영종도 미니 행사에서 처음 공개됨.", em=["처음 공개됨"]),
        L("님들은 이 디자인에 4420만원, 낼 만하다고 봄?", [P("top", MN, s0=1.0, s1=1.1)], None,
          say="님들은 이 디자인에 사천사백이십마넌, 낼 만하다고 봄?", fx=[("pop_bubble", "낼")]),
    ]
    go(S, lines, "딱 30대만 파는", "영국 국기 두른 미니", "MINI 쿠퍼 옥스포드 에디션, 10월 31일 출시, 4420만원",
       "#30대 한정 미니", "MINI 코리아 2026-10-30 발표 (파이낸셜뉴스 202610301211310707, 전자신문 20261030000150, 대한경제 202610301016597360890, 데일리카 63002)",
       [("MINI 쿠퍼 옥스포드 에디션 10/31 출시, 국내 30대 한정, 4420만원(부가세 포함)", "파이낸셜뉴스, 전자신문, 대한경제, 데일리카"),
        ("옥스포드 공장 새 MINI 생산 25주년 기념, 1959년 클래식 Mini 처음 생산, BMW그룹 2001년부터 생산", "파이낸셜뉴스"),
        ("인디고 선셋 블루, 유니언 잭 루프, 레드/화이트 스트라이프 보닛~테일게이트", "파이낸셜뉴스, 대한경제"),
        ("블루 니티드 직물 대시보드, 체커드 패턴 플로어 매트", "파이낸셜뉴스, 대한경제"),
        ("163마력, 25.5kg.m, 0→100km/h 7.7초, 7단 DCT", "파이낸셜뉴스, 전자신문, 대한경제"),
        ("10/31~11/1 영종도 BMW 드라이빙 센터 '2026 MINI 아워 스토리즈'에서 첫 공개", "전자신문, 대한경제"),
        ("대사 '와, 지붕에 영국 국기를' 은 구경꾼 반응(신차 대본 구조 1번)", "제작 메모")],
       "MINI 코리아가 옥스포드 공장 생산 25주년 기념 한정판 'MINI 쿠퍼 옥스포드 에디션'을 10월 31일 출시합니다.\n국내 30대 한정, 가격 4420만원, 163마력에 0→100km/h 7.7초입니다.\n실차는 10월 31일부터 영종도 MINI 아워 스토리즈에서 처음 공개됩니다.\n\n#MINI #미니쿠퍼 #한정판 #신차 #란빵",
       "님들은 이 디자인에 4420만원, 낼 만하다고 봄?",
       "차량용 방향제, 차량용 핸드폰 거치대, 자동차 블랙박스 2채널, 차량용 무선충전기, 자동차 발매트",
       "사진 = MINI 코리아 제공 보도사진(데일리카 워터마크 잘라냄, 번호판 모자이크). AI 생성 없음.", [P("rear", MN, s0=1.0, s1=1.1)])


# ───────────────────────── 9. 포르쉐 미션 S ─────────────────────────
def EP_missions():
    S = "missions"
    cap(S, "front", "ps_0.jpg", nofaces=True)
    cap(S, "rear", "ps_1.jpg", nofaces=True, cx=0.55)
    cap(S, "inside", "ps_2.jpg", nofaces=True, cx=0.45)
    cap(S, "side", "ps_3.jpg", nofaces=True, cx=0.55)
    cap(S, "ny", "ps_4.jpg", nofaces=True, fit=True)
    lines = [
        L("가격도 없는데 계약서부터 달라고?",
          [P("side", PS, s0=1.0, s1=1.2)], None, dialogue=True, speaker=3, emotion="toneup"),
        L("포르쉐가 이달 중순 뉴욕에서 공개한 콘셉트카 미션 S.",
          [P("ny", PS, s0=1.0, s1=1.15), P("front", PS, at="미션", s0=1.0, s1=1.2)], None, em=["미션 S"]),
        L("911보다 윗급에 들어갈 미드십 슈퍼카의 밑그림임.",
          [P("rear", PS, s0=1.0, s1=1.15)], None, say="구일일보다 윗급에 들어갈 미드십 슈퍼카의 밑그림임.", em=["윗급에"], em_color="yellow",
          fx=[("drop_futuristic", "윗급에", 0.5)]),
        L("가운데 화면을 아예 없애고, 내 폰을 끼워 쓰게 만듦.",
          [P("inside", PS, s0=1.0, s1=1.15), P("inside", PS, at="폰을", s0=1.3, s1=1.5, fx=0.6, fy=0.4, punch=True)],
          None, em=["화면을 아예 없애고"], fx=[("drum_rimshot", "폰을", 0.45)]),
        L("아직 가격도 제원도 없는 콘셉트카인데 반응이 터짐.",
          [P("front", PS, s0=1.1, s1=1.25)], None, em=["반응이 터짐"]),
        L("일부 고객은 지금 서명할 계약서를 달라고 요청했다고 함.",
          [P("side", PS, at="계약서를", s0=1.2, s1=1.4, fx=0.5, fy=0.5, punch=True)], None, em=["계약서를"], em_color="yellow",
          pop=("계약서?!", R, "계약서를"), shake="요청했다고", fx=[("hit_trailer_epic", "계약서를", 0.5)]),
        L("정말 압도적인 피드백을 받았습니다.",
          [P("ny", PS, s0=1.2, s1=1.35, fx=0.4, fy=0.6)], None, dialogue=True, speaker=2, emotion="normal"),
        L("포르쉐 슈퍼카는 918 스파이더 이후 10년 넘게 끊겨 있었음.",
          [P("rear", PS, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], None, say="포르쉐 슈퍼카는 구일팔 스파이더 이후 십년 넘게 끊겨 있었음.", em=["10년 넘게"],
          info={"kind": "quotes", "at": "포르쉐", "title": "포르쉐 슈퍼카 계보", "items": [
              {"text": "카레라 GT", "at": "포르쉐"}, {"text": "918 스파이더", "at": "918"}, {"text": "그리고 10년+ 공백", "at": "10년"}]}),
        L("근데 이건 아직 디자인 모델이라 양산은 2030년 이후로 점쳐짐.",
          [P("side", PS, s0=1.1, s1=1.25)], None, say="근데 이건 아직 디자인 모델이라 양산은 이천삼십년 이후로 점쳐짐.", em=["2030년 이후로"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "2030년", 0.45)]),
        L("님들은 가격도 모르는 차에 계약서 쓸 수 있음?", [P("front", PS, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "계약서")]),
    ]
    go(S, lines, "가격도 제원도 없는데", "계약서 달라는 포르쉐", "포르쉐 미션 S 콘셉트, 일부 고객이 계약서 요청(외신)",
       "#가격도 없는 포르쉐", "포르쉐 미션 S 10/15 공개 (노컷뉴스 6592615, 스포츠서울 1643646, 대한경제 202610160928395370841) + 오토블로그 2026-10 'Porsche fans want contracts for a supercar that isn't for sale yet' (보배드림 1043962)",
       [("10/15 뉴욕 퀸스에서 세계 최초 공개, 911 상위 미드십 슈퍼카 비전 모델", "노컷뉴스, 스포츠서울, 대한경제"),
        ("센터 고정 디스플레이 없애고 맥세이프 호환 스마트폰 거치", "스포츠서울, 대한경제"),
        ("가격, 제원 없는 콘셉트인데 일부 고객이 지금 서명할 계약서, 서류 요청", "오토블로그(보배드림 1043962 번역)"),
        ("CFO 요헨 브레크너 3분기 실적 콜 'really overwhelming feedback'", "오토블로그 원문(대사는 발언 번역)"),
        ("918 스파이더 이후 10년 넘게 슈퍼카 없음, 카레라 GT 는 더 이전", "오토블로그"),
        ("양산은 2030년 이후 관측", "보배드림 1043962 번역 기사(관측으로만 표기)")],
       "포르쉐가 10월 15일 공개한 911 윗급 미드십 콘셉트카 미션 S.\n가격도 제원도 없는데 일부 고객이 지금 서명할 계약서를 요청했다고 외신이 전했습니다.\n양산은 2030년 이후로 점쳐집니다.\n\n#포르쉐 #미션S #슈퍼카 #신차 #란빵",
       "님들은 가격도 모르는 차에 계약서 쓸 수 있음?",
       "차량용 핸드폰 거치대, 맥세이프 차량용 거치대, 차량용 무선충전기, 자동차 블랙박스 2채널, 차량용 방향제",
       "사진 = 포르쉐 제공 보도사진(스포츠서울, 노컷뉴스 게재분). 발표자 얼굴 컷 안 씀. AI 생성 없음.", [P("rear", PS, s0=1.0, s1=1.1)])


# ───────────────────────── 10. 주차번호판 (용품) ─────────────────────────
def EP_parksafe():
    S = "parksafe"
    lines = [
        L("번호는 없고 이 네모난 건 뭐야?",
          [B("k01", "Close-up of a small QR code parking sign card on the dashboard of a double-parked car, seen through the windshield, underground parking light, QR pattern abstract", s0=1.1, s1=1.3)],
          None, dialogue=True, speaker=3, emotion="toneup"),
        L("이번 주 네이버 쇼핑 자동차용품 인기 검색어 11위, 주차번호판.",
          [B("k02", "A parking phone number display plate with blank digit wheels sitting on a car dashboard behind the windshield, daylight, digits blurred")],
          None, say="이번 주 네이버 쇼핑 자동차용품 인기 검색어 십일위, 주차번호판.", em=["11위"], fx=[("drop_futuristic", "11위", 0.5)]),
        L("앞유리에 진짜 내 번호를 그대로 붙여두는 차가 아직 많음.",
          [B("k03", "Row of parked cars in a Korean apartment parking lot, small phone number cards visible behind windshields, numbers unreadable, daytime")],
          None, em=["진짜 내 번호를"]),
        L("그 번호가 스팸이나 범죄에 쓰일 수 있다는 걱정이 나옴.",
          [B("k04", "A smartphone lying on a car seat showing many unknown incoming call notifications, blurred, evening light, no readable text")],
          None, em=["범죄에"], em_color="yellow", fx=[("wrong_gameshow_buzz", "범죄에", 0.45)]),
        L("그래서 나온 게 050으로 시작하는 주차 안심번호.",
          [B("k02", at="안심번호", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], None, say="그래서 나온 게 공오공으로 시작하는 주차 안심번호.",
          em=["주차 안심번호"], em_color="yellow", pop=("안심번호!", Y, "안심번호")),
        L("제주시가 2021년에 처음 시작했고, 서울 성동구도 따라 했음.",
          [B("k05", "A Korean city district office building exterior on a clear day, flag poles, no people, no readable signs")],
          None, say="제주시가 이천이십일년에 처음 시작했고, 서울 성동구도 따라 했음.", em=["처음 시작했고"]),
        L("QR을 찍으면 내 번호 없이 차주에게 전화가 연결되는 방식.",
          [B("k01", at="QR을", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], None, say="큐알을 찍으면 내 번호 없이 차주에게 전화가 연결되는 방식.",
          em=["내 번호 없이"], fx=[("notify_message_pop", "연결되는", 0.45)]),
        L("어떤 제품은 연결될 때마다 안심번호가 새로 바뀜.",
          [B("k06", "A small card-type QR parking sign attached to the inside of a car windshield, close-up, daylight, QR pattern abstract, no readable text")],
          None, em=["새로 바뀜"]),
        L("근데 QR 찍는 법을 모르는 사람 앞에선 그냥 네모 그림일 뿐.",
          [B("k07", "A double-parked car blocking another car in a busy restaurant parking lot at night, no people visible")],
          None, say="근데 큐알 찍는 법을 모르는 사람 앞에선 그냥 네모 그림일 뿐.", em=["네모 그림일 뿐"], em_color="yellow",
          pop=("무용지물?!", R, "네모"), fx=[("drum_rimshot", "네모", 0.45)]),
        L("님들 차엔 진짜 번호 붙어 있음, 안심번호임?", [B("k03", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "안심번호임")]),
    ]
    go(S, lines, "앞유리 주차번호판", "진짜 내 번호 괜찮을까", "인기검색어 11위 주차번호판, 050 안심번호와 QR",
       "#주차번호판 진짜 번호?", "네이버 데이터랩 쇼핑인사이트 자동차용품 10/23~29 인기검색어 11위 + 문화일보 2023022401071027163001, 제주매일 329613, 뉴스1 5809412, 중소기업신문 340355",
       [("자동차용품 인기검색어 11위 주차번호판(1위 요소수, 2위 차량용방향제), 10/23~29", "데이터랩 API 직접 조회"),
        ("앞유리 전화번호 범죄 악용, 스팸 우려 → 050 안심번호 12자리 발급(성동구 시범)", "문화일보 2023-02-24"),
        ("제주시 2021년 12월 전국 처음 도입, 성동구 등으로 확산", "제주매일"),
        ("QR 스캔 시 번호 노출 없이 연결(부산 강서구 안심번호판)", "뉴스1 2025-06-10"),
        ("연결될 때마다 안심번호 변경되는 제품", "중소기업신문 2025-10-15(SM하이플러스)"),
        ("QR 인식법 모르는 사람 앞에선 무용지물, 이중주차 앞 난감 사례", "제주매일"),
        ("대사 '이 네모난 건 뭐야?' 는 제주매일 사례를 대사체로", "제작 메모")],
       "이번 주 자동차용품 인기 검색어 11위는 주차번호판입니다.\n앞유리의 진짜 번호 대신 050 안심번호나 QR 안심번호판을 쓰는 사람이 늘고 있습니다.\nQR을 찍는 법을 모르는 사람에겐 연락이 안 될 수 있다는 점도 함께 알아두세요.\n\n#주차번호판 #안심번호 #자동차용품 #개인정보 #란빵",
       "님들 차엔 진짜 번호 붙어 있음, 안심번호임?",
       "주차번호판 QR, 차량용 주차번호판, 자동차 블랙박스 2채널, 차량용 방향제, 차량용 핸드폰 거치대",
       "실제 제품 사진은 상표 노출이라 안 씀, 전부 AI 배경(상표 없는 카드형). 가격은 확인 안 해 안 씀.", [B("k06", s0=1.0, s1=1.1)])


EPS = [EP_busrage, EP_armytruck, EP_bbox142, EP_ebikeseat, EP_dumpmerge, EP_slopepark, EP_lane82,
       EP_minioxford, EP_missions, EP_parksafe]

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in EPS:
        if not want or f.__name__[3:] in want:
            f()
