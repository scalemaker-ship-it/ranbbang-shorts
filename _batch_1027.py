#!/usr/bin/env python3
"""란빵 2026-10-27: 자동차 이슈 13편 (보배드림 베스트 10/24~26 11편 + 개드립 테슬라 FSD + 헤럴드 마라톤 사고).
- 화면 = GPT 리얼 배경(gen.sh luna, 사람 없음) + いらすとや 캐릭터 + **원글 캡처 실사**(2026-10-27 사용자 지시:
  사진이 있으면 캡처해서 쓰고, 얼굴이 있으면 모자이크). 캡처는 cap() 이 tools/mosaic.py(YuNet) 로 얼굴을 찾아 픽셀화하고
  9:8(1080x960) 로 맞춘다(fit=True 는 블러 배경 위에 전체를 올려 글자 캡처용). 출처는 컷 우상단 credit.
- 근거 = work/research_1027.md (본문·댓글·첨부·판결문 원문·법령 확인). 실사 원본 = work/_photos/b1027/ (map.txt).
- 상호(지넷 AS점 이름)·실명·번호판은 대본에 안 씀. 실존 인물 얼굴(김한용 썸네일)은 안 씀.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1024 import B, C, L, build, IR, Y, W, R, P   # noqa: E402  (1024 → 1021 → 1020 헬퍼 + IR 누적)

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos", "b1027")
TW, TH = 1080, 960


def cap(slug, name, src, box=None, cx=0.5, cy=0.5, fit=False, boxes=(), nofaces=False, score=0.4, ph=None):
    """원글 캡처 → work/<slug>/v2/real/<name>.jpg (1080x960). 얼굴은 YuNet 으로 찾아 모자이크(+boxes 수동, 크롭 좌표 기준).
    ph = 원본 사진 폴더(기본 PH). 다른 배치에서 `from _batch_1027 import cap` 후 ph=work/_photos/b<날짜> 로 재사용."""
    ph = ph or PH
    import cv2, numpy as np
    from PIL import Image, ImageFilter
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import mosaic as M
    im = Image.open(os.path.join(ph, src)).convert("RGB")
    if box:
        im = im.crop(box)
    arr = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    faces = [] if nofaces else M.detect(arr, score)
    for f in faces:
        M.pixelate(arr, *f, 14)
    for b in boxes:
        M.pixelate(arr, *b, 14)
    im = Image.fromarray(cv2.cvtColor(arr, cv2.COLOR_BGR2RGB))
    if fit:
        bg = im.resize((TW, TH)).filter(ImageFilter.GaussianBlur(40)).point(lambda p: int(p * 0.45))
        r = min(TW / im.width, TH / im.height)
        fg = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
        bg.paste(fg, ((TW - fg.width) // 2, (TH - fg.height) // 2))
        out = bg
    else:
        r = max(TW / im.width, TH / im.height)
        im2 = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
        x = min(max(int(im2.width * cx - TW / 2), 0), im2.width - TW)
        y = min(max(int(im2.height * cy - TH / 2), 0), im2.height - TH)
        out = im2.crop((x, y, x + TW, y + TH))
    d = os.path.join(ROOT, "work", slug, "v2", "real")
    os.makedirs(d, exist_ok=True)
    out.save(os.path.join(d, name + ".jpg"), quality=92)
    print(f"  cap {slug}/{name} faces={len(faces)} boxes={len(boxes)}")
    return len(faces)


BB = "사진: 보배드림"
COMMON = "자동차 블랙박스 2채널, 블랙박스 메모리카드, 비상삼각대, 차량용 핸드폰 거치대, 차량용 방향제"


# ───────────────────────── 1. 블랙박스 168만원 ─────────────────────────
def EP_bbox168():
    S = "bbox168"
    cap(S, "pay", "1042874_00.jpg", box=(0, 0, 1080, 1150), fit=True, nofaces=True)
    cap(S, "form", "1042874_01.jpg", fit=True, nofaces=True)
    cap(S, "warr", "1042874_02.jpg", box=(0, 0, 1080, 1000), fit=True, nofaces=True)
    lines = [
        L("월 7만원 프로모션이에요. 기기는 무상이고요.",
          [B("x01", "Interior of a small car electronics shop in Seoul: dashcam boxes on a glass counter, a card terminal, fluorescent light", s0=1.1, s1=1.3)],
          C("sales", "r"), dialogue=True, speaker=2, emotion="normal", say="월 칠마넌 프로모션이에요. 기기는 무상이고요."),
        L("첫 차 산 사회초년생이 공식 AS점이라는 매장에서 블랙박스를 달았음.",
          [B("x02", "A new dashcam being installed behind the windshield of a compact car inside a shop bay, cables hanging, daytime")],
          C("drv_smile"), em=["공식 AS점"]),
        L("SD카드를 석 달마다 안 바꾸면 고장 난다며 24개 구독 조건이라고 함.",
          [B("x03", "A stack of 24 microSD card packages fanned out on a counter next to a dashcam, close-up, shop lighting"),
           B("x03", at="24개", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("sagi", "r"), say="에스디카드를 석 달마다 안 바꾸면 고장 난다며 이십사개 구독 조건이라고 함.",
          em=["석 달마다"], fx=[("wrong_gameshow_buzz", "고장", 0.45)]),
        L("카드를 넘기고 받은 문자엔 168만원, 24개월 무이자 할부가 찍혀 있었음.",
          [P("pay", BB, s0=1.0, s1=1.15), P("pay", BB, at="168만원", s0=1.5, s1=1.7, fx=0.3, fy=0.2, punch=True)],
          C("bill_shock"), say="카드를 넘기고 받은 문자엔 백육십팔마넌, 이십사개월 무이자 할부가 찍혀 있었음.",
          em=["168만원"], em_color="yellow", pop=("168만원?!", R, "168만원"), fx=[("hit_trailer_epic", "168만원", 0.5)],
          info={"kind": "compare", "at": "카드를", "title": "설명 vs 결제", "items": [
              {"label": "매장 설명", "color": W, "at": "카드를", "rows": [["월", "7만원", W]]},
              {"label": "실제 결제", "color": R, "at": "168만원", "rows": [["총액", "168만원", Y], ["할부", "24개월", Y]]}]}),
        L("총액 설명은 한 줄도 없었고, 결제 단말기에 서명한 적도 없다고 함.",
          [P("form", BB, s0=1.0, s1=1.2, fx=0.5, fy=0.4)], C("komatta", "r"), em=["서명한 적도"]),
        L("환불을 요구하자 철거비 40만원에 원상복구 10만원을 더 내라고 함.",
          [P("warr", BB, s0=1.0, s1=1.15), B("x04", "A dashcam partially removed from a car headliner with wires exposed, a mechanic's tool tray below, shop bay", at="철거비")],
          C("ohagya"), say="환불을 요구하자 철거비 사십마넌에 원상복구 십마넌을 더 내라고 함.",
          em=["철거비 40만원"], fx=[("drop_futuristic", "철거비", 0.5)]),
        L("어디에 제보하든 상관없어요. 저희는 정상 거래예요.",
          [B("x01", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("ignore", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("할부거래법 16조, 20만원 넘고 석 달 이상 할부면 남은 할부금 지급을 거절할 수 있음.",
          [B("x06", "A law book open on a desk next to a credit card and a calculator, warm desk lamp light, no people")],
          C("judge", "r"), say="할부거래법 십육조, 이십마넌 넘고 석 달 이상 할부면 남은 할부금 지급을 거절할 수 있음.",
          em=["지급을 거절"], em_color="yellow", fx=[("correct_ding", "거절할", 0.5)],
          info={"kind": "quotes", "at": "할부거래법", "title": "할부거래법 16조 항변권", "items": [
              {"text": "20만원 이상", "at": "20만원"}, {"text": "3개월 이상 할부", "at": "석 달"}, {"text": "잔여 할부금 거절", "at": "거절할"}]}),
        L("글쓴이는 사기와 사문서위조로 고소를 진행 중임.",
          [B("x07", "A police station civil complaint counter with a stack of forms and a pen, Korean interior, fluorescent light")],
          C("police"), em=["고소를"], fx=[("swipe_card", "고소를", 0.4)]),
        L("님들 블랙박스 달 때 총액부터 물어봄, 아니면 월 얼마만 들음?", [B("x02", s0=1.0, s1=1.12)], C("biz_q", "r"), fx=[("pop_bubble", "들음")]),
    ]
    build(S, lines, "월 7만원이라더니", "168만원 할부 블랙박스", "공식 AS점이 SD카드 24개 구독으로 168만원 24개월 할부",
          "#블랙박스 168만원 할부", "보배드림 베스트 1042874 교통사고/블박 (2026-10-26, 추천 195, 댓글 56)",
          [("서울 강서구 제조사 공식 AS 지정점, Smart Q8000, '월 7만원 프로모션, 기기 무상, SD카드 24개 구독' 설명", "원글 본문, 신청서 캡처(메모리카드 24회 교체 서비스)"),
           ("실제 결제 1,680,000원 24개월 무이자 할부, 2026-10-21 18:37 승인", "원글 결제내역 캡처"),
           ("총액 안내 없음, 결제패드 서명 안 함, 직원이 끊은 영수증 보고 알게 됨", "원글 본문"),
           ("환불 거부, 철거비 40만원+원상복구 10만원 요구, '어디에 제보하든 상관없다'는 태도", "원글 본문(대사는 본문 서술을 대사체로)"),
           ("카드사 할부항변 1차 거절('업체의 정상 판매 주장'), 매출전표 전자서명본 요청 예정, 사기·사문서위조 고소 진행, 소비자원 접수", "원글 본문"),
           ("할부거래법 제16조 소비자의 항변권: 20만원 이상, 3개월 이상 할부 거래는 사유 발생 시 잔여 할부금 지급 거절 가능", "국가법령정보센터"),
           ("댓글 '블랙박스, 타이어 대표적 눈탱이'(8), '첫차 사회초년생은 계속 나옴'(4)", "원글 댓글")],
          "공식 AS점에서 월 7만원 프로모션이라며 블랙박스를 달아줬는데, 문자엔 168만원 24개월 할부.\n환불하려면 철거비 40만원을 더 내라고 합니다.\n할부거래법 16조 항변권으로 맞서는 중입니다.\n\n#블랙박스 #할부사기 #소비자원 #보배드림 #란빵",
          "님들 블랙박스 달 때 총액부터 물어봄, 아니면 월 얼마만 들음?",
          "자동차 블랙박스 2채널, 블랙박스 메모리카드 128GB, 블랙박스 상시전원, 차량용 핸드폰 거치대, 차량용 방향제",
          "상호·지점명 미표기. 캡처의 지도·사업자 정보는 원글이 가린 상태 그대로.", [B("x03", s0=1.0, s1=1.1)])


# ───────────────────────── 2. 대법원 입헹굼물 ─────────────────────────
def EP_rinse0():
    S = "rinse0"
    cap(S, "knn1", "1042950_00.jpg", fit=True)
    cap(S, "knn2", "1042950_02.jpg", fit=True)
    cap(S, "knn3", "1042950_03.jpg", fit=True, nofaces=True)
    cap(S, "knn4", "1042950_04.jpg", fit=True, nofaces=True)
    cap(S, "n1", "1042582_00.jpg", box=(0, 0, 800, 640), fit=True)
    lines = [
        L("물 한 컵 안 줬다고 음주측정이 무효라고요?",
          [P("knn1", "화면: KNN", s0=1.0, s1=1.15)], C("wow", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("세종시 도로 한가운데, 시동을 켠 채 운전석에서 잠든 남성이 신고됨.",
          [B("r01", "A sedan stopped in the middle of a two-lane Korean city road at night, headlights on, hazard lights off, streetlights, no people visible", s0=1.1, s1=1.3)],
          C("sleep"), em=["잠든"]),
        L("경찰은 지구대로 옮겼고, 남성은 벤치에 누운 채 계속 잠들어 있었음.",
          [B("r02", "An empty wooden bench inside a small Korean police substation at night, fluorescent light, a paper cup of water on a nearby desk")],
          C("police", "r"), em=["벤치에 누운 채"]),
        L("한 경찰관이 종이컵에 생수를 담아 다가갔다가, 깨우지 않고 그냥 돌아섬.",
          [B("r02", at="종이컵에", s0=1.4, s1=1.6, fx=0.75, fy=0.5, punch=True)],
          C("komatta"), em=["그냥 돌아섬"], fx=[("drum_rimshot", "돌아섬", 0.4)]),
        L("25분 뒤 누운 자세 그대로 불대를 입에 대서 잰 수치가 0.081퍼센트.",
          [P("knn2", "화면: KNN", s0=1.0, s1=1.15), P("knn2", "화면: KNN", at="0.081", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)],
          C("drv_shock", "r"), say="이십오분 뒤 누운 자세 그대로 불대를 입에 대서 잰 수치가 영점영팔일퍼센트.",
          em=["0.081퍼센트"], em_color="yellow", fx=[("drop_futuristic", "0.081", 0.5)],
          info={"kind": "bars", "at": "수치가", "title": "호흡측정 결과", "items": [{"label": "입헹굼 없이", "num": 0.081, "dec": 3, "suffix": "%", "at": "0.081", "flash": "0.081"}]}),
        L("1심과 2심은 징역 1년에 집행유예 2년. 그런데 대법원이 이걸 깼음.",
          [P("knn4", "화면: KNN", s0=1.0, s1=1.15)], C("judge"), say="일심과 이심은 징역 일년에 집행유예 이년. 그런데 대법원이 이걸 깼음.",
          em=["대법원이 이걸 깼음"], pop=("파기!", R, "깼음"), shake="깼음", fx=[("hit_trailer_epic", "깼음", 0.5)]),
        L("시행규칙상 입 헹굴 물을 줘야 하는데, 그 절차를 안 거친 측정은 위법수집증거라는 것.",
          [P("n1", "화면: 뉴스1", s0=1.0, s1=1.15)], C("lawyer", "r"), em=["위법수집증거"], em_color="yellow",
          info={"kind": "quotes", "at": "시행규칙상", "title": "대법 2025도16613", "items": [
              {"text": "시행규칙 27조의2", "at": "시행규칙상"}, {"text": "입헹굼물 제공 의무", "at": "헹굴"}, {"text": "안 지키면 증거 못 씀", "at": "위법수집증거"}]}),
        L("잠들어 있었다고 절차가 면제되진 않는다고 대법원은 못 박았음.",
          [P("knn3", "화면: KNN", s0=1.0, s1=1.15)], C("judge", "r"), em=["면제되진 않는다"], fx=[("correct_ding", "못", 0.5)]),
        L("다만 무죄가 아니라 파기환송이라 다시 재판을 받음.",
          [B("r04", "Exterior of a Korean district courthouse on an overcast day, wide steps, no people")],
          C("biz_think"), em=["파기환송"], em_color="yellow"),
        L("님들은 이 판결, 절차가 중요함, 아니면 음주운전 면죄부임?", [P("knn1", "화면: KNN", s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "면죄부")]),
    ]
    build(S, lines, "입 헹굴 물 안 줬다고", "음주측정 증거 무효", "잠든 운전자에게 물 안 주고 잰 0.081%, 대법원이 집유 판결 파기",
          "#물 안 주면 측정 무효", "대법원 2025도16613 (2026-10-01 선고) 판결문 + 뉴스1 2026-10-25 + KNN 화면 (보배드림 1042582·1042950)",
          [("2023-12-09 20:25 세종시 도로 한가운데 시동 켠 채 운전석에서 잠든 신고, 현행범 체포, 지구대 벤치에 눕힘", "판결문 3.가.3) 가)~나)"),
           ("경찰관이 생수 든 종이컵 들고 다가갔다가 다른 경찰관 손짓에 돌아감, 이후 물 제공 없음", "판결문 다)"),
           ("20:50 누운 채 불대에 숨 불어 0.081% 측정", "판결문 라)"),
           ("원심(대전지법 2025노937) 징역 1년 집유 2년 → 파기환송", "판결문 주문, 뉴스1"),
           ("도로교통법 시행규칙 27조의2 2항 1호 나목 입헹굼물 제공(2023-07-04 부령 상향), 형사소송법 308조의2 위법수집증거", "판결문 2)"),
           ("'운전자가 잠들어 있다는 사정만으로 절차 이행이 면제된다고 볼 수 없다'", "판결문 바)"),
           ("구강 내 잔류 알코올로 실제보다 높게 측정될 수 있어 입헹굼 절차 도입", "판결문 다)"),
           ("댓글 '환송했군'(14), '전국민 생수 알레르기'(10)", "보배드림 1042582 댓글")],
          "도로에서 잠든 운전자를 깨우지 않고 입 헹굴 물도 없이 잰 음주측정 0.081%.\n대법원은 시행규칙 절차를 안 지킨 위법수집증거라며 집행유예 판결을 파기했습니다.\n무죄가 아니라 파기환송입니다.\n\n#음주측정 #대법원 #위법수집증거 #보배드림 #란빵",
          "님들은 이 판결, 절차가 중요함, 아니면 음주운전 면죄부임?",
          "휴대용 음주측정기, 차량용 물컵홀더, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 방향제",
          "피고인 실명·성별 미표기(기사 '김 모 씨'). 2019년 벌금 100만원 전력은 대본에서 뺌.", [P("knn4", "화면: KNN", s0=1.0, s1=1.1)])


# ───────────────────────── 3. BMW 10분 추격 ─────────────────────────
def EP_bmwchase():
    S = "bmwchase"
    cap(S, "turn", "bmw_turn_33.jpg", cx=0.5, cy=0.55, nofaces=True)
    cap(S, "turn2", "bmw_turn_35.jpg", cx=0.5, cy=0.55, nofaces=True)
    cap(S, "chase", "bmw_chase_6.jpg", cx=0.6, cy=0.5, nofaces=True)
    cap(S, "chase2", "bmw_chase_7.jpg", cx=0.6, cy=0.5, nofaces=True)
    cap(S, "man", "bmw_man.jpg", cx=0.5, cy=0.45, boxes=[(820, 0, 280, 300)])
    lines = [
        L("야, 너 왜 내 차선으로 끼어들어? 차도 거지 같은 거 끌면서.",
          [P("man", BB, s0=1.0, s1=1.2, fx=0.5, fy=0.4)], C("rage", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("태안의 한 교차로, 글쓴이는 2차로에서 좌회전 신호를 받고 정상적으로 돌았음.",
          [P("turn", BB, s0=1.0, s1=1.15), P("turn2", BB, at="정상적으로", s0=1.1, s1=1.3)],
          C("drv_smile"), say="태안의 한 교차로, 글쓴이는 이차로에서 좌회전 신호를 받고 정상적으로 돌았음.", em=["정상적으로"]),
        L("1차로에서 빠르게 오던 BMW가 급제동하더니, 뒤에서 쌍라이트에 경적을 울림.",
          [P("chase", BB, s0=1.0, s1=1.2), P("chase2", BB, at="쌍라이트", s0=1.3, s1=1.5, fx=0.65, fy=0.5, punch=True)],
          C("aori", "r"), say="일차로에서 빨리 오던 비엠이 급제동을 했음. 그리고 뒤에서 쌍라이트에 경적을 울림.",
          em=["쌍라이트"], fx=[("boom_subby_kick", "경적", 0.45)]),
        L("차선을 바꿀 때마다 따라붙으며 10분 넘게 쫓아옴.",
          [B("m01", "Rear-view mirror of a car showing a dark sedan tailgating very close on a rural Korean highway at dusk, headlights glaring")],
          C("drv_shock"), say="차선을 바꿀 때마다 따라붙으며 십분 넘게 쫓아옴.", em=["10분 넘게"], pop=("추격!!", R, "쫓아옴"), shake="쫓아옴"),
        L("결국 글쓴이 본가 주차장까지 따라 들어와서, 얼굴에 대고 욕을 퍼부음.",
          [B("m02", "A small residential parking lot in a Korean town at dusk, two cars parked, an apartment entrance behind, no people")],
          C("rage", "r"), em=["얼굴에 대고"], fx=[("hit_trailer_epic", "욕을", 0.5)]),
        L("이유는 3차로에서 자기 차선으로 끼어들었다는 것. 영상엔 그런 장면이 없음.",
          [P("turn", BB, s0=1.2, s1=1.4, fx=0.5, fy=0.5)], C("komatta"), say="이유는 삼차로에서 자기 차선으로 끼어들었다는 것. 영상엔 그런 장면이 없음.",
          em=["그런 장면이 없음"], em_color="yellow", fx=[("wrong_gameshow_buzz", "없음", 0.45)]),
        L("저는 무리하게 가지 않았습니다만, 그렇게 보였다면 죄송합니다.",
          [B("m02", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("sorry"), dialogue=True, speaker=2, emotion="normal"),
        L("차로 위협하며 따라붙으면 특수협박, 7년 이하 징역. 욕설은 모욕죄가 따로 붙음.",
          [B("m03", "A Korean police report form and a dashcam memory card on a desk, pen beside, fluorescent light, no people")],
          C("judge"), say="차로 위협하며 따라붙으면 특수협박, 칠년 이하 징역. 욕설은 모욕죄가 따로 붙음.",
          em=["특수협박"], em_color="yellow", fx=[("drop_futuristic", "특수협박", 0.5)],
          info={"kind": "compare", "at": "차로", "title": "보복운전 처벌", "items": [
              {"label": "특수협박", "color": R, "at": "차로", "rows": [["형법 284조", "7년 이하", Y]]},
              {"label": "모욕죄", "color": W, "at": "욕설은", "rows": [["형법 311조", "1년 이하", W]]}]}),
        L("보복운전으로 형사 입건되면 벌점 100점, 면허정지까지 감.",
          [B("m04", "A Korean driver's license lying on a police counter next to a stamp, close-up, no people")],
          C("police", "r"), say="보복운전으로 형사 입건되면 벌점 백점, 면허정지까지 감.", em=["면허정지"], fx=[("correct_ding", "면허정지", 0.5)]),
        L("댓글은 글쓴이 잘못 하나도 없음. 님들은 이거 신고함?",
          [P("man", BB, s0=1.0, s1=1.12, fx=0.5, fy=0.4)], C("biz_q"), fx=[("pop_bubble", "신고함")]),
    ]
    build(S, lines, "좌회전 한 번 했다고", "10분 쫓아와 욕한 BMW", "태안 교차로, 끼어들었다는 오해로 본가 주차장까지 추격해 욕설",
          "#10분 쫓아온 BMW", "보배드림 베스트 1042712 교통사고/블박 (2026-10-25, 추천 329, 댓글 70, 영상 7개)",
          [("2026-10-24 오후 충남 태안, 1·2차로 좌회전, 3차로 직진. 글쓴이 2차로에서 좌회전 신호 진행", "원글 본문, 영상 1 정지 프레임"),
           ("1차로 상대 차 빠른 속도로 진입 후 급제동, 쌍라이트+경적 1회, 차선 변경마다 따라옴, 약 10분", "원글 본문, 영상 2(후방)"),
           ("본가 주차장까지 따라와 얼굴에 대고 욕설, '3차로에서 끼어들었다' 주장, 뒷좌석 아이 2명", "원글 본문"),
           ("'저는 무리하게 가지 않았습니다만.. 그렇게 보였다면 죄송합니다' → 욕설 후 떠남", "원글 본문(글쓴이 발언 직접 인용), 상대 욕설은 본문의 'ㄱ지, 병ㅅ같은 차' 를 순화해 각색"),
           ("형법 284조 특수협박 7년 이하 징역, 311조 모욕 1년 이하 징역·200만원 이하 벌금", "국가법령정보센터"),
           ("보복운전 형사입건 시 벌점 100점 면허정지, 구속 시 취소", "도로교통법 93조, 시행규칙 별표 28"),
           ("댓글 1위(62) '글쓴이 잘못 하나도 없네요', 3위(41) '상대가 1차로에서 2차로로 넘어온 것'", "원글 댓글")],
          "좌회전 한 번 했다고 10분을 쫓아와 본가 주차장에서 욕을 퍼부은 BMW.\n영상엔 끼어든 장면이 없습니다.\n차로 위협하며 따라붙으면 특수협박, 벌점 100점 면허정지 대상입니다.\n\n#보복운전 #특수협박 #블랙박스 #보배드림 #란빵",
          "댓글은 글쓴이 잘못 하나도 없음. 님들은 이거 신고함?", COMMON,
          "상대 차종은 댓글 추정(4시리즈 컨버터블)이라 'BMW' 까지만. 영상 속 남성은 원글이 PutMask 로 가린 데다 추가 모자이크.", [P("chase", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 4. 벤츠 CLE 결함 11개 ─────────────────────────
def EP_cle11():
    S = "cle11"
    lines = [
        L("새 차인데 시동이 다섯 번 만에 걸려요.",
          [B("c01", "A luxury convertible coupe's start button and dashboard with a warning message area blurred, leather interior, close-up", s0=1.1, s1=1.3)],
          C("drvw_surprise", "r"), dialogue=True, speaker=3, emotion="normal"),
        L("9월에 강남 전시장에서 CLE 카브리올레를 새로 산 글쓴이.",
          [B("c02", "A white luxury convertible coupe parked in front of a glass showroom in Gangnam, Seoul, daytime, no people")],
          C("dealer"), say="구월에 강남 전시장에서 씨엘이 카브리올레를 새로 산 글쓴이."),
        L("한 달 만에 적어 본 증상이 열한 가지임.",
          [B("c03", "A handwritten checklist on a notepad on a car hood, many lines with check marks, text unreadable, daylight"),
           B("c03", at="열한", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)],
          C("bill_shock", "r"), em=["열한 가지"], pop=("11가지!", R, "열한"), fx=[("hit_trailer_epic", "열한", 0.5)]),
        L("주행 보조는 시스템 오류, 창문은 안 닫히고, 뒷좌석 스피커는 소리가 안 남.",
          [B("c04", "A convertible's side window stuck half open with rain drops on the glass, parked, close-up")],
          C("drv_angry"), em=["시스템 오류"],
          info={"kind": "bars", "at": "주행", "title": "한 달 만에 나온 증상", "items": [
              {"label": "주행보조 오류", "num": 2, "suffix": "건", "at": "주행"}, {"label": "창문·소음·스피커", "num": 4, "suffix": "건", "at": "창문은"},
              {"label": "시동·밀림·쏠림", "num": 3, "suffix": "건", "at": "뒷좌석"}, {"label": "기타", "num": 2, "suffix": "건", "at": "안 남"}]}),
        L("휠 얼라인먼트도 틀어져 있었고, 평지에서 출발할 때 뒤로 밀림.",
          [B("c05", "A luxury coupe on a wheel alignment lift in a service center, laser sensors on the wheels, no people")],
          C("seibishi", "r"), em=["뒤로 밀림"], fx=[("wrong_gameshow_buzz", "밀림", 0.45)]),
        L("몇 달째 벤츠만 이런 글이 수십 개 올라와요.",
          [B("c06", "A smartphone showing a car community thread with many comments, text blurred, on a cafe table", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("biz_laugh", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("추천 104개 댓글은 구형 벤츠가 진짜 벤츠라는 말.",
          [B("c07", "An older generation silver luxury sedan from the 2010s parked under trees, clean, daytime, no people")],
          C("drv_heart"), say="추천 백사개 댓글은 구형 벤츠가 진짜 벤츠라는 말.", em=["구형 벤츠"], fx=[("crowd_laugh", "진짜", 0.4)]),
        L("인도 1년 안에 중대 하자 2번, 일반 하자 3번 고치고도 재발하면 교환이나 환불 중재를 신청할 수 있음.",
          [B("c08", "A thick vehicle warranty booklet and a car key on a desk, close-up, soft light, no people")],
          C("judge", "r"), say="인도 일년 안에 중대 하자 두번, 일반 하자 세번 고치고도 재발하면 교환이나 환불 중재를 신청할 수 있음.",
          em=["교환이나 환불"], em_color="yellow", fx=[("drop_futuristic", "교환이나", 0.5)],
          info={"kind": "compare", "at": "인도", "title": "자동차관리법 47조의2", "items": [
              {"label": "중대 하자", "color": R, "at": "중대", "rows": [["수리", "2회 후 재발", Y]]},
              {"label": "일반 하자", "color": W, "at": "일반", "rows": [["수리", "3회 후 재발", W]]}]}),
        L("오류가 뜰 때마다 계기판을 영상으로 찍어 두라는 게 수입차 20년 차 댓글의 팁.",
          [B("c09", "A hand-free view of a smartphone mounted to record a car's digital instrument cluster showing a blurred warning, interior")],
          C("drv_idea"), say="오류가 뜰 때마다 계기판을 영상으로 찍어 두라는 게 수입차 이십년 차 댓글의 팁.", em=["영상으로 찍어"], fx=[("shutter_digital", "찍어", 0.45)]),
        L("님들은 새 차 한 달 만에 증상 열한 개면 공장 보냄, 환불 감?", [B("c02", s0=1.0, s1=1.12)], C("biz_q", "r"), fx=[("pop_bubble", "환불")]),
    ]
    build(S, lines, "한 달 된 벤츠 CLE", "결함 11개 적어 봤더니", "시동 5번, 창문 안 닫힘, 뒤로 밀림. 공장 입고 전 조언 구하는 글",
          "#벤츠 한 달 결함 11개", "보배드림 베스트 1042486 자유게시판 (2026-10-24, 추천 484, 댓글 92)",
          [("9월 강남 벤츠 전시장 구입 CLE200 카브리올레, 10월 현재 증상 11개 목록", "원글 본문"),
           ("액티브 비상 어시스트·차선변경 어시스트 오류, 창문 안 닫힘, 뒷좌석 스피커, 시동 5번, 차선유지 불량, 휠얼라인먼트 쏠림, 평지 뒤로 밀림 등", "원글 본문"),
           ("'몇달째 벤츠만 이런글 수십개 올라오네요'(94), '벤츠는 역시 구형벤스가 찐벤스'(104)", "원글 댓글(대사체로 다듬음)"),
           ("수입차 20년 댓글(10): 오류 메시지 뜰 때 계기판 영상 촬영, 서비스센터 '재현 안 됨' 대비", "원글 댓글"),
           ("자동차관리법 47조의2: 인도 1년·2만km 이내 중대하자 2회, 일반하자 3회 수리 후 재발 시 자동차안전·하자심의위 교환·환불 중재", "국가법령정보센터, 기아 고객센터 안내"),
           ("막대 그래프 분류(2·4·3·2)는 원글 11개 항목을 성격별로 묶은 것", "원글 본문 기준 정리")],
          "9월에 산 벤츠 CLE 카브리올레, 한 달 만에 적어 본 증상이 11개.\n댓글은 몇 달째 벤츠만 이런 글이 수십 개라고 합니다.\n1년 안에 중대 하자 2회면 교환·환불 중재 대상입니다.\n\n#벤츠 #신차결함 #레몬법 #보배드림 #란빵",
          "님들은 새 차 한 달 만에 증상 열한 개면 공장 보냄, 환불 감?",
          "OBD2 스캐너, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 점프스타터, 차량용 방향제",
          "원글 첨부 사진 없음. 딜러·센터명 없음.", [B("c03", s0=1.0, s1=1.1)])


# ───────────────────────── 5. 신호 바뀌고 6초 뒤 스파크 ─────────────────────────
def EP_spark6s():
    S = "spark6s"
    cap(S, "s1", "spark_57.jpg", cx=0.3, cy=0.55, nofaces=True)
    cap(S, "s2", "spark_59.5.jpg", cx=0.25, cy=0.6, nofaces=True)
    cap(S, "s3", "spark_61.jpg", cx=0.3, cy=0.6, nofaces=True)
    lines = [
        L("벤츠한테 과실 안 잡히겠죠?",
          [P("s1", BB, s0=1.0, s1=1.15)], C("drv_q", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("토요일 아침 7시 56분, 대전 대덕대교 남단 교차로.",
          [P("s1", BB, s0=1.1, s1=1.3, fx=0.3, fy=0.5)], C("drv_smile"), say="토요일 아침 일곱시 오십육분, 대전 대덕대교 남단 교차로."),
        L("글쓴이 벤츠는 신호가 바뀌고 6초가 넘어서 교차로에 들어갔음.",
          [B("p01", "Dashcam view through a wet windshield of a wide Korean city intersection, green traffic light ahead, overcast morning, no people"),
           B("p01", at="6초", s0=1.3, s1=1.5, fx=0.5, fy=0.4, punch=True)],
          C("drv_smile", "r"), say="글쓴이 벤츠는 신호가 바뀌고 육초가 넘어서 교차로에 들어갔음.", em=["6초가"], em_color="yellow",
          info={"kind": "counter", "at": "신호가", "title": "신호 바뀐 뒤", "items": [{"num": 6, "suffix": "초", "label": "경과 후 진입", "at": "6초"}]}),
        L("그런데 옆에서 스파크가 속도를 줄일 생각도 없이 그대로 들어와 옆구리를 때려 박음.",
          [P("s2", BB, s0=1.0, s1=1.25, fx=0.25, fy=0.6), P("s3", BB, at="때려", s0=1.3, s1=1.5, fx=0.3, fy=0.6, punch=True)],
          C("jiko_man"), em=["그대로"], pop=("쾅!!", R, "때려"), shake="때려", fx=[("glass_smash", "때려", 0.5)]),
        L("블랙박스 소리가 커서 글쓴이가 미리 사과까지 한 영상임.",
          [B("p02", "A dashcam unit mounted on a windshield seen from inside, red recording light on, blurred wet road behind")],
          C("sorry", "r"), em=["미리 사과까지"], fx=[("drum_rimshot", "사과까지", 0.4)]),
        L("신호가 막 바뀐 것도 아니고 5초 넘게 지났는데, 스파크 100이요.",
          [P("s3", BB, s0=1.2, s1=1.4, fx=0.3, fy=0.6)], C("biz_angry"), dialogue=True, speaker=3, emotion="toneup",
          say="신호가 막 바뀐 것도 아니고 오초 넘게 지났는데, 스파크 백이요."),
        L("추천 116개 1등 댓글은, 재판까지 가서 벤츠 과실을 잡으려면 판사가 좀 이상한 사람이어야 한다는 말.",
          [B("p03", "A smartphone showing a community post comment section with a highlighted top comment, text blurred, on a car seat")],
          C("biz_laugh", "r"), say="추천 백십육개 일등 댓글은, 재판까지 가서 벤츠 과실을 잡으려면 판사가 좀 이상한 사람이어야 한다는 말.",
          em=["판사가 좀 이상한"], fx=[("crowd_laugh", "이상한", 0.4)]),
        L("신호위반은 12대 중과실. 보험 과실 기준표에서도 신호위반 차가 100임.",
          [B("p04", "A printed traffic accident fault ratio chart on a desk, diagrams of intersection collisions, text unreadable, no people")],
          C("judge"), say="신호위반은 십이대 중과실. 보험 과실 기준표에서도 신호위반 차가 백임.", em=["12대 중과실"], em_color="yellow",
          fx=[("drop_futuristic", "12대", 0.5)],
          info={"kind": "compare", "at": "신호위반은", "title": "과실비율", "items": [
              {"label": "신호위반 스파크", "color": R, "at": "신호위반은", "rows": [["과실", "100", Y]]},
              {"label": "직진 벤츠", "color": W, "at": "100임", "rows": [["과실", "0", W]]}]}),
        L("중과실이라 종합보험에 들었어도 형사 처벌을 피하지 못함.",
          [B("p05", "A Korean police traffic accident investigation car parked at an intersection with cones, overcast, no people")],
          C("police", "r"), em=["형사 처벌"], fx=[("correct_ding", "피하지", 0.5)]),
        L("님들은 신호 바뀌고 몇 초 뒤에 출발함?", [P("s2", BB, s0=1.0, s1=1.12, fx=0.25, fy=0.6)], C("biz_q"), fx=[("pop_bubble", "출발함")]),
    ]
    build(S, lines, "신호 바뀌고 6초 뒤", "옆구리 때려 박은 스파크", "대전 대덕대교 남단, 신호위반 측면 충돌. 벤츠 과실 나올까?",
          "#신호 6초 뒤 충돌 과실", "보배드림 베스트 1042705 교통사고/블박 (2026-10-25, 추천 338, 댓글 76, 영상 2개)",
          [("2026-10-25 07:56 대전 서구-유성구 대덕대교 남단, 벤츠(글쓴이) vs 스파크 측면 충돌, 신호 바뀌고 6초 경과", "원글 본문, 영상 1 타임스탬프"),
           ("'소리가 큽니다 정말 죄송합니다 소리 줄여 주세요', '벤츠에게 과실 안잡히겠죠???'", "원글 본문(대사 직접 인용)"),
           ("댓글 1위(116) '재판까지 가서 벤츠 과실 잡으려면 판사가 정신병 환자일 가능성이' → 순화", "원글 댓글"),
           ("댓글 2위(100) '신호위반 스파크 100이요. 신호가 막 바뀐것도 아니고 5초 이상 지났고 속도 내네요'", "원글 댓글(대사체)"),
           ("신호위반 = 교통사고처리특례법 3조 2항 단서 1호 12대 중과실, 종합보험 가입해도 공소 제기", "국가법령정보센터"),
           ("과실비율인정기준: 신호위반 차 100 : 0", "손해보험협회 과실비율정보포털 기본 유형")],
          "신호가 바뀌고 6초나 지나 교차로에 들어갔는데, 옆에서 스파크가 그대로 들어와 옆구리를 때렸습니다.\n신호위반은 12대 중과실, 과실 100입니다.\n댓글은 판사가 이상해야 벤츠 과실이 나온다고 합니다.\n\n#신호위반 #12대중과실 #블랙박스 #보배드림 #란빵",
          "님들은 신호 바뀌고 몇 초 뒤에 출발함?", COMMON,
          "영상 속 차량 번호판은 원본 해상도에서 식별 어려움, 크롭으로 더 작게. 상대 운전자 정보 없음.", [P("s3", BB, s0=1.0, s1=1.1, fx=0.3, fy=0.6)])


# ───────────────────────── 6. 경차칸 두 칸 Z4 ─────────────────────────
def EP_z4light():
    S = "z4light"
    cap(S, "z1", "1042767_00.jpg", cx=0.5, cy=0.35, nofaces=True)
    cap(S, "z2", "1042767_00.jpg", cx=0.5, cy=0.75, nofaces=True)
    lines = [
        L("안 그래도 주차 전쟁인데, 아침에 보고 깜짝 놀랐습니다.",
          [P("z1", BB, s0=1.0, s1=1.15)], C("biz_shock", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("울산 동구, 구청이 관리하는 공영주차장. 대기업 직원들이 매일 자리 싸움을 하는 곳임.",
          [B("z01", "A crowded multi-level public parking garage in a Korean industrial city, concrete pillars, full rows of cars, morning, no people")],
          C("drv_think"), em=["자리 싸움"]),
        L("그 한가운데 흰색 로드스터가 경차 칸 두 개에 걸쳐 비스듬히 서 있었음.",
          [P("z1", BB, s0=1.1, s1=1.35, fx=0.5, fy=0.3), P("z2", BB, at="두 개에", s0=1.2, s1=1.4, fx=0.4, fy=0.6, punch=True)],
          C("meiwaku", "r"), em=["두 개에 걸쳐"], pop=("두 칸!", R, "두 개"), fx=[("hit_trailer_epic", "두 개에", 0.5)]),
        L("바닥엔 파란 글씨로 경차라고 크게 적혀 있음.",
          [P("z2", BB, s0=1.3, s1=1.5, fx=0.3, fy=0.6)], C("drv_angry"), em=["경차라고"], fx=[("wrong_gameshow_buzz", "경차라고", 0.4)]),
        L("댓글 추천 1등은 앞뒤로 경차를 바르게 대고 연락처를 안 남기면 참교육이 된다는 것.",
          [B("z02", "A white roadster boxed in tightly between two small Korean kei cars in a parking garage, no space to move, no people")],
          C("biz_laugh", "r"), say="댓글 추천 일등은 앞뒤로 경차를 바르게 대고 연락처를 안 남기면 참교육이 된다는 것.",
          em=["참교육"], fx=[("crowd_laugh", "참교육", 0.4)]),
        L("Z4가 얼마나 크다고요? 경차 칸에 제대로 대도 쏙 들어가요.",
          [P("z1", BB, s0=1.2, s1=1.4, fx=0.5, fy=0.35)], C("biz_angry"), dialogue=True, speaker=3, emotion="toneup",
          say="제트포가 얼마나 크다고요? 경차 칸에 제대로 대도 쏙 들어가요."),
        L("그런데 이 차, 과태료는 0원임.",
          [B("z03", "A blue painted compact-car-only parking bay in an empty Korean parking garage, Korean text unreadable, concrete floor, no cars")],
          C("ohagya", "r"), say="그런데 이 차, 과태료는 영원임.", em=["0원"], em_color="yellow", fx=[("drum_rimshot", "0원", 0.45)],
          info={"kind": "compare", "at": "과태료는", "title": "전용구역 주차 과태료", "items": [
              {"label": "장애인 구역", "color": W, "at": "과태료는", "rows": [["과태료", "10만원", W]]},
              {"label": "경차 구역", "color": R, "at": "0원", "rows": [["과태료", "0원", Y]]}]}),
        L("주차장법은 경차 전용 칸을 만들라고만 했지, 일반 차가 대면 어떻게 한다는 조항이 없음.",
          [B("z04", "A law book open on a table with a parking garage visible through a window behind, no people")],
          C("judge"), em=["조항이 없음"], em_color="yellow"),
        L("장애인 구역은 10만원, 전기차 충전구역도 10만원인데 경차 칸만 빈칸임.",
          [B("z05", "Side by side: a disabled parking bay sign and an EV charging bay sign in a Korean parking lot, daytime, no people")],
          C("lawyer", "r"), say="장애인 구역은 십마넌, 전기차 충전구역도 십마넌인데 경차 칸만 빈칸임.", em=["빈칸"]),
        L("님들 주차장에서 경차 칸 두 개 쓰는 차 보면 어떻게 함?", [P("z1", BB, s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "함")]),
    ]
    build(S, lines, "경차 칸 두 개 쓴 Z4", "과태료는 0원인 이유", "울산 공영주차장 경차 구역에 걸쳐 댄 로드스터, 주차장법엔 제재 조항 없음",
          "#경차칸 Z4 과태료 0원", "보배드림 베스트 1042767 자유게시판 (2026-10-26, 추천 347, 댓글 43)",
          [("울산 동구 동구청 관리 공영주차장, 대기업 직원 주차전쟁, 아침에 발견", "원글 본문, 본인 댓글 '대기업근처 동구청에 관리하는 공영주차장'"),
           ("흰색 BMW Z4가 경차 구획 두 칸에 걸쳐 주차, 바닥 '경차' 표기", "원글 사진(번호판은 원글이 가림)"),
           ("댓글 1위(61) '앞뒤로 경차 바르게 주차하고 연락처 안남기면 참교육', (5) 'Z4가 얼마나 크다고 저렇게 주차하지'", "원글 댓글(대사체)"),
           ("주차장법 6조·10조는 경형자동차 전용주차구획 설치·지정 근거만 두고 일반차 주차 시 과태료 규정 없음", "주차장법 원문, 한국경제 2024-03 보도"),
           ("장애인전용구역 주차 과태료 10만원(장애인등편의법 27조), 충전구역 주차 10만원(친환경자동차법 시행령)", "국가법령정보센터"),
           ("같은 소재 escalade(10/10) 과 각도 다름: 이번 편은 '과태료 0원' 법 공백", "used-sources 대조")],
          "울산 공영주차장 경차 칸 두 개에 걸쳐 댄 BMW Z4.\n장애인 구역은 10만원, 충전구역도 10만원인데 경차 칸은 과태료가 0원입니다.\n주차장법에 제재 조항이 없기 때문입니다.\n\n#주차빌런 #경차구역 #주차장법 #보배드림 #란빵",
          "님들 주차장에서 경차 칸 두 개 쓰는 차 보면 어떻게 함?",
          "주차 연락처 번호판, 주차 알림판, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 방향제",
          "차주 정보 없음. 과태료 비교의 장애인·충전구역 금액은 승용차 기준.", [P("z2", BB, s0=1.0, s1=1.1, fx=0.4, fy=0.6)])


# ───────────────────────── 7. 문 열면 자동 P, 조건 ─────────────────────────
def EP_autop():
    S = "autop"
    cap(S, "hb", "1042692_01.jpg", fit=True, nofaces=True)
    lines = [
        L("P 눌렀는데 왜 움직이지?",
          [P("hb", "화면: JTBC 한블리", s0=1.0, s1=1.15)], C("drv_shock", "r"), dialogue=True, speaker=3, emotion="toneup", say="피 눌렀는데 왜 움직이지?"),
        L("한블리에 나온 카니발 언덕 밀림 사고. 운전자가 내리자 차가 혼자 굴러감.",
          [B("a01", "A large Korean minivan rolling backward down a steep rural slope with the driver door open, no people, overcast daylight")],
          C("jiko_man"), em=["혼자 굴러감"], fx=[("glass_smash", "굴러감", 0.4)]),
        L("요즘 차는 문을 열면 자동으로 P로 바뀌는데, 왜 안 바뀌었냐는 게 논쟁이 됨.",
          [B("a02", "Close-up of a rotary gear dial in a modern Korean minivan with the P indicator lit, leather console, interior light")],
          C("drv_q", "r"), say="요즘 차는 문을 열면 자동으로 피로 바뀌는데, 왜 안 바뀌었냐는 게 논쟁이 됨.", em=["자동으로 P"]),
        L("매뉴얼을 보면 자동 P에는 조건이 세 개 붙어 있음.",
          [B("a03", "An open car owner's manual on a passenger seat, a page about the gear selector with diagrams, text unreadable"),
           B("a03", at="세 개", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)],
          C("biz_idea"), say="매뉴얼을 보면 자동 피에는 조건이 세 개 붙어 있음.", em=["조건이 세 개"], em_color="yellow",
          info={"kind": "quotes", "at": "매뉴얼을", "title": "문 열면 P, 조건", "items": [
              {"text": "차가 완전히 정차", "at": "조건이"}, {"text": "페달에서 발 뗌", "at": "세 개"}, {"text": "안전벨트 해제", "at": "있음"}]}),
        L("차가 완전히 섰을 것, 페달에서 발을 뗐을 것, 그리고 안전벨트를 풀었을 것.",
          [B("a04", "A seat belt buckle unlatched next to the driver's seat of a minivan, close-up, daylight through window")],
          C("drv_think", "r"), em=["안전벨트를 풀었을 것"]),
        L("벨트를 맨 채 문을 열면 차는 아직 운전 중이라고 보고 P로 안 바꿈.",
          [B("a04", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("drv_surprise"), say="벨트를 맨 채 문을 열면 차는 아직 운전 중이라고 보고 피로 안 바꿈.",
          em=["P로 안 바꿈"], pop=("안 바뀜!", R, "안 바꿈"), fx=[("wrong_gameshow_buzz", "안 바꿈", 0.45)]),
        L("글쓴이의 추리는 벨트 경고음 끄는 클립을 꽂았거나, 등 뒤로 돌려 맸을 거라는 것.",
          [B("a05", "A metal seat belt alarm stopper clip inserted in a car's seat belt buckle, no belt attached, close-up, interior")],
          C("sagi", "r"), em=["클립을"], fx=[("drum_rimshot", "클립을", 0.4)]),
        L("벨트 꼼수 쓰면 차는 끝까지 운전 중인 줄 알아요.",
          [B("a05", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("seibishi"), dialogue=True, speaker=2, emotion="normal"),
        L("설명서도 보조 기능이니, 내릴 땐 P에 들어갔는지 눈으로 확인하라고 적어 둠.",
          [B("a02", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], C("judge", "r"), say="설명서도 보조 기능이니, 내릴 땐 피에 들어갔는지 눈으로 확인하라고 적어 둠.",
          em=["눈으로 확인"], em_color="yellow", fx=[("correct_ding", "확인하라고", 0.5)]),
        L("님들은 내릴 때 P 직접 누름, 아니면 문 열면 알아서 되겠지 함?", [P("hb", "화면: JTBC 한블리", s0=1.0, s1=1.12)], C("biz_q"),
          say="님들은 내릴 때 피 직접 누름, 아니면 문 열면 알아서 되겠지 함?", fx=[("pop_bubble", "함")]),
    ]
    build(S, lines, "문 열면 자동 P라더니", "카니발이 굴러간 이유", "한블리 언덕 밀림 사고, 자동 P 조건 3개와 벨트 꼼수",
          "#자동 P 안 되는 조건", "보배드림 베스트 1042692 국산차게시판 (2026-10-25, 추천 38) + JTBC 한블리 191회(10/13) 캡처 + 기아 오너스매뉴얼",
          [("한블리 191회 카니발 언덕 밀림 사고, 'D에 놓고 내렸기 때문' 자막", "원글 첨부 한블리 캡처"),
           ("글쓴이 주장: 벨트 착용+D에서 문 열면 P 안 들어감, 벨트 클립·등 뒤로 돌려 맨 꼼수의 최후", "원글 본문"),
           ("기아 매뉴얼: N/R/D에서 운전석 도어 열면 P 변속, 조건 = 브레이크·가속페달 안 밟음, 안전벨트 풀림, 정차 상태(1회)", "ownersmanual.kia.com 자동변속기(변속 다이얼) 항목"),
           ("현대 매뉴얼: 안전 보조 기능, 주차 시 P 위치 직접 확인 안내", "ownersmanual.hyundai.com 변속 위치 선택하기"),
           ("댓글(4) '문 열면 파킹은 안전장치, 기능 유무와 상관없이 P 넣고 사이드'", "원글 댓글"),
           ("김한용 MOCAR 검증 영상(20만뷰) 썸네일은 실존 인물 얼굴이라 미사용", "제작 메모")],
          "운전석 문을 열면 자동으로 P가 되는 차인데 카니발이 언덕에서 굴러갔습니다.\n매뉴얼의 자동 P 조건은 정차, 페달 뗌, 안전벨트 해제 세 가지.\n벨트 클립 꼼수를 쓰면 차는 끝까지 운전 중인 줄 압니다.\n\n#카니발 #자동P #안전벨트 #한블리 #란빵",
          "님들은 내릴 때 P 직접 누름, 아니면 문 열면 알아서 되겠지 함?",
          "고임목, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 비상삼각대, 차량용 방향제",
          "카니발 전용 매뉴얼 문구는 미확인, 기아 공통 변속 다이얼 문구 기준. 사고 당사자 조작은 글쓴이 추리로 표현.", [B("a01", s0=1.0, s1=1.1)])


# ───────────────────────── 8. 술타기 판결 ─────────────────────────
def EP_sojucourt():
    S = "sojucourt"
    cap(S, "d1", "1042657_00.jpg", box=(0, 0, 1440, 760), fit=True, nofaces=True)
    cap(S, "d2", "1042657_00.jpg", box=(0, 560, 1440, 1200), cx=0.5, cy=0.5, nofaces=True)
    lines = [
        L("차 좀 빼 주세요. 술 냄새 나시는데요?",
          [B("j01", "A cramped parking lot of a one-room apartment building in a Korean city at night, two cars nose to nose, streetlight", s0=1.1, s1=1.3)],
          C("drvw_surprise", "r"), dialogue=True, speaker=3, emotion="normal"),
        L("울산의 원룸 주차장, 40대 남성이 공간이 좁자 다른 차주에게 차를 빼 달라고 함.",
          [B("j01", at="차를", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], C("drv_angry"),
          say="울산의 원룸 주차장, 사십대 남성이 공간이 좁자 다른 차주에게 차를 빼 달라고 함."),
        L("말다툼 끝에 상대가 술 냄새를 맡고 경찰에 신고함.",
          [B("j02", "A smartphone held up in a dark parking lot showing the emergency call screen, screen blurred, car headlights behind")],
          C("phone_man", "r"), em=["신고함"], fx=[("notify_message_pop", "신고함", 0.5)]),
        L("경찰이 온다는 걸 알자 남성은 차에 올라타 안에 있던 소주 한 병을 들이켬.",
          [B("j03", "A green soju bottle lying empty on the passenger seat of a car at night, interior dome light on, no people"),
           B("j03", at="소주", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)],
          C("sagi"), em=["소주 한 병을"], pop=("술타기!", R, "들이켬"), shake="들이켬", fx=[("hit_trailer_epic", "소주", 0.5)]),
        L("측정을 못 하게 하려고 술을 더 마시는, 이른바 술타기임.",
          [P("d1", "화면: 동아일보", s0=1.0, s1=1.15)], C("police_angry", "r"), em=["술타기"], em_color="yellow"),
        L("작년부터 생긴 음주측정 방해죄는 측정 거부와 똑같이 1년 이상 5년 이하 징역임.",
          [B("j04", "A Korean law book open on a desk with a gavel beside it, warm lamp light, no people")],
          C("judge"), say="작년부터 생긴 음주측정 방해죄는 측정 거부와 똑같이 일년 이상 오년 이하 징역임.",
          em=["1년 이상 5년 이하"], em_color="yellow", fx=[("drop_futuristic", "1년", 0.5)],
          info={"kind": "compare", "at": "작년부터", "title": "도로교통법 148조의2", "items": [
              {"label": "측정 거부", "color": W, "at": "작년부터", "rows": [["징역", "1~5년", W]]},
              {"label": "술타기(측정 방해)", "color": R, "at": "똑같이", "rows": [["징역", "1~5년", Y], ["벌금", "500~2천만", Y]]}]}),
        L("울산지법은 징역 1년 6개월에 집행유예 3년, 사회봉사 80시간을 선고함.",
          [P("d2", "화면: 동아일보", s0=1.0, s1=1.2)], C("judge", "r"),
          say="울산지법은 징역 일년 육개월에 집행유예 삼년, 사회봉사 팔십시간을 선고함.", em=["집행유예 3년"],
          info={"kind": "bars", "at": "울산지법은", "title": "선고", "items": [
              {"label": "징역(집유 3년)", "num": 18, "suffix": "개월", "at": "징역"}, {"label": "사회봉사", "num": 80, "suffix": "시간", "at": "사회봉사"},
              {"label": "준법운전 강의", "num": 40, "suffix": "시간", "at": "선고함"}]}),
        L("과거에도 음주운전으로 두 번 처벌받은 사람이었음.",
          [B("j05", "A stack of old court documents in a folder on a desk, Korean paper forms, text unreadable, no people")],
          C("biz_shock"), em=["두 번"], fx=[("wrong_gameshow_buzz", "두 번", 0.45)]),
        L("마지막 음주운전이 9년 넘게 지났고, 잘못을 뉘우친다고 해서 봐줬어요.",
          [B("j04", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("lawyer", "r"), dialogue=True, speaker=2, emotion="normal",
          say="마지막 음주운전이 구년 넘게 지났고, 잘못을 뉘우친다고 해서 봐줬어요."),
        L("추천 1등 댓글은 술타기는 더 세게 처벌했어야 한다는 것. 님들 생각은?",
          [P("d1", "화면: 동아일보", s0=1.0, s1=1.12)], C("biz_q"), say="추천 일등 댓글은 술타기는 더 세게 처벌했어야 한다는 것. 님들 생각은?", fx=[("pop_bubble", "생각은")]),
    ]
    build(S, lines, "경찰 온다니까 소주 원샷", "술타기 판결 결과", "울산 원룸 주차장 시비, 측정 방해죄로 기소된 40대 선고",
          "#술타기 선고 결과", "동아일보 2026-10-25 (송치훈 기자) 캡처 = 보배드림 베스트 1042657 (추천 62, 댓글 16)",
          [("울산지법 형사9단독 송인철 판사, 도로교통법 위반(음주측정방해) 40대 남성 징역 1년 6개월 집행유예 3년, 사회봉사 80시간, 준법운전강의 40시간", "동아일보 캡처"),
           ("2025년 12월 울산 남구 원룸 주차장, 차 빼 달라 요청 → 말다툼 → 술 냄새 신고 → 경찰 출동 안 뒤 차 안 소주 1병", "동아일보 캡처"),
           ("'정당한 사유 없이 측정을 방해하는 행위는 음주운전에 준하는 엄중한 처벌 필요', 과거 2회 음주운전 전력", "동아일보 캡처(재판부 판시)"),
           ("양형 이유: 범행 인정·반성, 마지막 음주운전 처벌 후 9년 이상 경과", "동아일보 캡처(대사체로 다듬음)"),
           ("도로교통법 44조 5항 음주측정방해행위, 148조의2 2항 2호 1년 이상 5년 이하 징역 또는 500만~2천만원 벌금(측정거부와 동일)", "casenote 도로교통법 148조의2, nepla 44조"),
           ("댓글 1위(46) '술타기는 진짜 더 심하게 했어야', 2위(44) '벌금도 없고'", "보배드림 댓글"),
           ("sooltagi(10/11, 채널A 현행범 체포)와 다른 사건", "used-sources 대조")],
          "차 빼 달라는 시비 끝에 술 냄새로 신고당하자, 경찰이 오기 전 차 안에서 소주 한 병을 들이켠 40대.\n새로 생긴 음주측정 방해죄는 측정 거부와 같은 1년 이상 5년 이하 징역입니다.\n선고는 징역 1년 6개월에 집행유예 3년.\n\n#술타기 #음주측정방해 #집행유예 #울산지법 #란빵",
          "추천 1등 댓글은 술타기는 더 세게 처벌했어야 한다는 것. 님들 생각은?",
          "휴대용 음주측정기, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 대리운전 호출 거치대, 차량용 방향제",
          "'작년부터' = 2025년 6월 시행 기준 2026년 시점 표현. 판사 실명은 대본에 안 넣음.", [B("j03", s0=1.0, s1=1.1)])


# ───────────────────────── 9. 책임보험만 든 상대차 ─────────────────────────
def EP_uninsured():
    S = "uninsured"
    lines = [
        L("저 책임보험밖에 없는데요. 알아서 하세요.",
          [B("u01", "A minor rear-end collision between two sedans on a Korean city street at night, hazard lights blinking, no people", s0=1.1, s1=1.3)],
          C("ignore", "r"), dialogue=True, speaker=3, emotion="normal"),
        L("보배드림 경고 글. 책임보험만 들고 다니는 차가 생각보다 많다는 것.",
          [B("u02", "A smartphone showing a car community warning post, text blurred, on a desk with car keys")],
          C("drv_think"), em=["책임보험만"]),
        L("책임보험은 법이 강제하는 최소한이라, 상대 차 수리비는 2천만원까지만 나옴.",
          [B("u03", "A badly crumpled front end of a luxury SUV after a collision, parked at a repair shop entrance, daylight, no people"),
           B("u03", at="2천만원", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("hoken", "r"), say="책임보험은 법이 강제하는 최소한이라, 상대 차 수리비는 이처만넌까지만 나옴.", em=["2천만원까지만"], em_color="yellow",
          fx=[("drop_futuristic", "2천만원", 0.5)],
          info={"kind": "bars", "at": "책임보험은", "title": "의무보험 한도", "items": [
              {"label": "대물(상대 차)", "num": 2000, "suffix": "만원", "at": "상대"}, {"label": "대인 부상(최대)", "num": 3000, "suffix": "만원", "at": "2천만원"},
              {"label": "대인 사망(최대)", "num": 15000, "suffix": "만원", "at": "나옴"}]}),
        L("수입차 한 대 제대로 박으면 수리비가 그 한도를 훌쩍 넘김.",
          [B("u03", s0=1.3, s1=1.5, fx=0.5, fy=0.4)], C("bill_shock"), em=["훌쩍 넘김"], fx=[("wrong_gameshow_buzz", "넘김", 0.45)]),
        L("넘는 돈은 가해자 개인한테 받아야 하는데, 재산이 없거나 출국해 버리면 끝임.",
          [B("u04", "An empty airport departure gate with a plane visible through the window at dusk, no people")],
          C("komatta", "r"), em=["출국해 버리면"], pop=("출국?!", R, "출국해"), fx=[("hit_trailer_epic", "출국해", 0.5)]),
        L("그래서 글쓴이의 결론은 내 보험을 빵빵하게 넣으라는 것.",
          [B("u05", "A car insurance policy document with coverage checkboxes on a desk, a pen and a car key, text unreadable")],
          C("drv_idea"), em=["내 보험을"]),
        L("무보험차 상해 특약이 있으면, 상대가 보험이 없어도 내 보험사가 먼저 합의금을 줌.",
          [B("u06", "A hospital corridor with a wheelchair by the wall and a nurse station sign blurred, daylight, no people")],
          C("lawyer", "r"), em=["무보험차 상해"], em_color="yellow", fx=[("correct_ding", "먼저", 0.5)],
          info={"kind": "quotes", "at": "무보험차", "title": "내 보험에서 챙길 것", "items": [
              {"text": "무보험차 상해", "at": "무보험차"}, {"text": "자기차량손해", "at": "상대가"}, {"text": "구상은 보험사가", "at": "합의금을"}]}),
        L("내 보험으로 먼저 처리하고, 상대한텐 보험사가 구상권을 청구하면 돼요.",
          [B("u05", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_smile"), dialogue=True, speaker=2, emotion="normal"),
        L("자차 보험까지 있으면 내 차 수리비도 상대 재산 상황과 상관없이 나옴.",
          [B("u07", "A sedan being repaired in a clean body shop bay, new bumper being fitted, no people")],
          C("seibishi", "r"), em=["자차 보험"]),
        L("님들 보험 갱신할 때 무보험차 상해 넣었는지 확인해 봄?", [B("u01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "상대가 책임보험만", "들었을 때 내 돈 지키는 법", "대물 한도 2천만원, 넘는 돈은 가해자 개인에게. 무보험차 상해로 대비",
          "#책임보험만 든 상대차", "보배드림 베스트 1042579 자유게시판 (2026-10-24, 추천 51) + 자동차손해배상보장법 시행령",
          [("'외국인들 책임보험만 들고 타고다녀요', '내보험으로 처리하고 상대편한테 구상권청구하라고 해도 된다면서요'", "원글 본문(국적 언급은 대본에서 뺌, 보험 상식으로 일반화)"),
           ("의무보험(대인Ⅰ) 사망 1억 5천만원, 부상 3천만원 한도, 대물 2천만원", "자동차손해배상보장법 5조, 시행령 3조"),
           ("무보험자동차에 의한 상해 담보: 상대 무보험·책임보험만 가입 시 내 보험사가 보상 후 구상", "자동차보험 표준약관"),
           ("자기차량손해 담보로 내 차 수리", "자동차보험 표준약관")],
          "상대 차가 책임보험만 들었으면 내 차 수리비는 2천만원까지만 나옵니다.\n넘는 돈은 가해자 개인에게 받아야 하고, 재산이 없거나 출국하면 끝.\n무보험차 상해와 자차 특약이 답입니다.\n\n#자동차보험 #책임보험 #무보험차상해 #보배드림 #란빵",
          "님들 보험 갱신할 때 무보험차 상해 넣었는지 확인해 봄?", COMMON,
          "원글의 '외국인' 특정은 대본에서 제외(근거 없는 일반화 방지). 금액은 승용차 의무보험 기준.", [B("u05", s0=1.0, s1=1.1)])


# ───────────────────────── 10. 아반떼 값 수입차 ─────────────────────────
def EP_cheapimport():
    S = "cheapimport"
    IK = "화면: INSSA K STUDIO"
    cap(S, "k1", "1042744_02.png", cx=0.5, cy=0.5, nofaces=True)
    cap(S, "k2", "1042744_03.png", cx=0.5, cy=0.5)
    cap(S, "k3", "1042744_05.png", cx=0.5, cy=0.5, nofaces=True)
    cap(S, "k4", "1042744_09.png", cx=0.5, cy=0.5, nofaces=True)
    cap(S, "k5", "1042744_13.png", cx=0.5, cy=0.5, nofaces=True)
    cap(S, "k6", "1042744_11.png", cx=0.5, cy=0.5)
    lines = [
        L("이젠 수입차가 가성비네요.",
          [P("k4", IK, s0=1.0, s1=1.15)], C("biz_surprise", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("보배드림에 올라온 캡처 묶음. 아반떼나 투싼 값으로 사는 수입차 목록임.",
          [P("k1", IK, s0=1.0, s1=1.2)], C("drv_think"), em=["아반떼나 투싼 값"]),
        L("푸조 308이 3,460만원, 폭스바겐 골프 디젤이 3,758만원.",
          [P("k2", IK, s0=1.0, s1=1.2), P("k5", IK, at="골프", s0=1.0, s1=1.2)],
          C("dealer", "r"), say="푸조 삼백팔이 삼천사백육십마넌, 폭스바겐 골프 디젤이 삼천칠백오십팔마넌.", em=["3,460만원"], em_color="yellow",
          fx=[("drop_futuristic", "3,460만원", 0.5)]),
        L("BMW 2시리즈 그란쿠페는 프로모션 적용하면 4천만원 초반, 벤츠 A클래스 해치백은 4,383만원.",
          [P("k6", IK, s0=1.0, s1=1.2), P("k3", IK, at="벤츠", s0=1.0, s1=1.2)],
          C("open_man"), say="비엠더블유 이시리즈 그란쿠페는 프로모션 적용하면 사처만넌 초반, 벤츠 에이클래스 해치백은 사천삼백팔십삼마넌.",
          em=["4,383만원"], em_color="yellow",
          info={"kind": "bars", "at": "BMW", "title": "영상 속 가격(만원)", "items": [
              {"label": "푸조 308", "num": 3460, "at": "BMW"}, {"label": "골프 TDI", "num": 3758, "at": "2시리즈"},
              {"label": "2시리즈 그란쿠페", "num": 4210, "at": "프로모션"}, {"label": "벤츠 A220", "num": 4383, "at": "벤츠", "flash": "벤츠"}]}),
        L("그런데 신형 아반떼 하이브리드 최고 트림에 옵션을 다 넣으면 4,314만원까지 올라감.",
          [B("i01", "A brand-new Korean compact sedan in a showroom with a price tag card on the windshield, text unreadable, bright light, no people"),
           B("i01", at="4,314만원", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("bill_shock", "r"), say="그런데 신형 아반떼 하이브리드 최고 트림에 옵션을 다 넣으면 사천삼백십사마넌까지 올라감.",
          em=["4,314만원"], pop=("4,314만원!", R, "4,314만원"), fx=[("hit_trailer_epic", "4,314만원", 0.5)]),
        L("그래서 추천 51개 1등 댓글이 이젠 수입차가 가성비라는 말이었음.",
          [P("k4", IK, s0=1.1, s1=1.3)], C("biz_laugh"), say="그래서 추천 오십일개 일등 댓글이 이젠 수입차가 가성비라는 말이었음.", em=["가성비"],
          fx=[("crowd_laugh", "가성비", 0.4)]),
        L("근데 사고 나면 수리비랑 유지비가 얼마나 차이 나는지 좀 알려주세요.",
          [B("i02", "A European hatchback on a lift in an independent repair shop, parts boxes on shelves, no people")],
          C("drv_q", "r"), dialogue=True, speaker=3, emotion="normal"),
        L("댓글 답은 오일과 타이어는 국산과 거의 같고, 큰 고장만 아니면 수리비도 아득히 비싸진 않다는 것.",
          [B("i02", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("seibishi"), em=["거의 같고"]),
        L("님들은 같은 4천만원이면 아반떼 풀옵 감, 수입차 깡통 감?", [P("k6", IK, s0=1.0, s1=1.12)], C("biz_q"),
          say="님들은 같은 사처만넌이면 아반떼 풀옵 감, 수입차 깡통 감?", fx=[("pop_bubble", "깡통")]),
    ]
    build(S, lines, "아반떼 풀옵 4,314만원", "그 돈이면 수입차 뭐 사냐", "푸조 308 3,460만원, 골프 3,758만원, 벤츠 A클래스 4,383만원",
          "#아반떼 값 수입차 목록", "보배드림 베스트 1042744 신유머 (2026-10-26, 추천 148, 댓글 49, 유튜브 INSSA K STUDIO 영상 캡처 17장) + SBS Biz 아반떼 가격",
          [("푸조 308 알뤼르 1.2 3,460만원, 골프 2.0 TDI 프레스티지 3,758만원, BMW 2시리즈 그란쿠페 4,210만원, 벤츠 A220 4,383만원, X1 5,110만원, ID.5 5,158만원", "원글 캡처 자막(영상 제작 시점 가격, 프로모션 포함 가능)"),
           ("신형 아반떼 하이브리드 인스퍼레이션 풀옵션 4,314만원, 가솔린 모던 2,398만원", "SBS Biz 'AI·첨단 기능 품었더니…아반떼 가격에 소비자 깜짝'(2026-08)"),
           ("댓글 1위(51) '이젠 수입차가 가성비네요', (32) '유지비 좀 알려주십시오', (17) '엔진오일·타이어 국산과 차이 없음, 부품은 배 타고 옴', (10) '보증기간까지만 타고 팔 거면'", "원글 댓글(대사체로 다듬음)"),
           ("원글 본문 '노조 해결 못하면 가격경쟁력 안 좋을 것'은 논쟁 소지라 대본 제외", "제작 메모")],
          "푸조 308 3,460만원, 골프 디젤 3,758만원, 벤츠 A클래스 4,383만원.\n신형 아반떼 하이브리드 풀옵션은 4,314만원까지 갑니다.\n댓글은 이젠 수입차가 가성비라고 합니다.\n\n#아반떼 #수입차가격 #가성비 #보배드림 #란빵",
          "님들은 같은 4천만원이면 아반떼 풀옵 감, 수입차 깡통 감?",
          "OBD2 스캐너, 차량용 핸드폰 거치대, 자동차 블랙박스 2채널, 차량용 공기청정기, 차량용 방향제",
          "캡처 속 가격은 영상 제작 시점 기준이라 '영상 속 가격'으로 표기. 아반떼 가솔린 풀옵 가격은 미확인이라 하이브리드 기준으로만.", [P("k2", IK, s0=1.0, s1=1.1)])


# ───────────────────────── 11. 신형 투싼 고급유 권장 ─────────────────────────
def EP_tucson95():
    S = "tucson95"
    cap(S, "m1", "1042399_00.webp", fit=True, nofaces=True)
    cap(S, "m2", "1042399_00.webp", box=(0, 600, 1221, 714), fit=True, nofaces=True)
    lines = [
        L("고급유 넣을 거면 누가 사요?",
          [P("m1", "화면: 현대차 매뉴얼", s0=1.0, s1=1.15)], C("drv_q", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("보배드림에 올라온 신형 투싼 매뉴얼 한 장.",
          [P("m1", "화면: 현대차 매뉴얼", s0=1.1, s1=1.3)], C("drv_think"), em=["매뉴얼 한 장"]),
        L("맨 아래 주석. 최적의 엔진 성능을 위해 RON 95 이상의 고급 휘발유 사용을 권장합니다.",
          [P("m2", "화면: 현대차 매뉴얼", s0=1.0, s1=1.2), P("m2", "화면: 현대차 매뉴얼", at="RON", s0=1.4, s1=1.6, fx=0.4, fy=0.5, punch=True)],
          C("biz_shock", "r"), say="맨 아래 주석. 최적의 엔진 성능을 위해 론 구십오 이상의 고급 휘발유 사용을 권장합니다.",
          em=["고급 휘발유"], em_color="yellow", pop=("고급유?!", R, "고급"), fx=[("hit_trailer_epic", "고급", 0.5)]),
        L("일반 휘발유를 넣으면 출력이 떨어지거나 기름을 더 먹을 수 있다는 말도 붙어 있음.",
          [B("t01", "A gas station pump nozzle inserted into a compact SUV's fuel door, Korean gas station canopy, daytime, no people")],
          C("drv_cry"), em=["기름을 더"]),
        L("보통 휘발유는 옥탄가 91 이상, 고급은 94 이상이라 리터당 200원에서 300원 더 비쌈.",
          [B("t02", "A Korean gas station price sign board with two fuel price rows, numbers blurred, blue sky, no people")],
          C("sales", "r"), say="보통 휘발유는 옥탄가 구십일 이상, 고급은 구십사 이상이라 리터당 이배권에서 삼배권 더 비쌈.",
          em=["200원에서 300원"], em_color="yellow",
          info={"kind": "compare", "at": "보통", "title": "휘발유 옥탄가", "items": [
              {"label": "보통 휘발유", "color": W, "at": "보통", "rows": [["RON", "91 이상", W]]},
              {"label": "고급 휘발유", "color": Y, "at": "고급은", "rows": [["RON", "94 이상", Y], ["리터당", "+200~300원", Y]]}]}),
        L("연료통이 54리터니까 한 번 가득 넣을 때마다 만 원 넘게 더 드는 셈.",
          [B("t01", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("saifu"), say="연료통이 오십사리터니까 한 번 가득 넣을 때마다 마넌 넘게 더 드는 셈.",
          em=["만 원 넘게"], fx=[("coin_drop", "만 원", 0.45)],
          info={"kind": "bars", "at": "연료통이", "title": "가득 주유 시 추가(300원 기준)", "items": [{"label": "54L x 300원", "num": 16200, "suffix": "원", "at": "만 원"}]}),
        L("댓글은 투싼에 고성능 엔진이라도 올라간 줄 알겠다며 웃었음.",
          [B("t03", "A compact Korean SUV engine bay with the hood open, clean turbo engine cover, no logos, daylight")],
          C("biz_laugh", "r"), em=["고성능 엔진"], fx=[("crowd_laugh", "웃었음", 0.4)]),
        L("권장은 권장이지 필수가 아니잖아요. 게임 권장 사양 같은 거죠.",
          [B("t03", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_idea"), dialogue=True, speaker=2, emotion="normal"),
        L("매뉴얼도 넣으면 안 된다가 아니라, 성능이 조금 달라질 수 있다고만 써 놨음.",
          [P("m2", "화면: 현대차 매뉴얼", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], C("judge", "r"), em=["조금 달라질 수"], fx=[("correct_ding", "써", 0.5)]),
        L("님들은 권장이면 고급유 넣음, 그냥 일반유 넣음?", [B("t02", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "넣음")]),
    ]
    build(S, lines, "신형 투싼 매뉴얼에", "고급 휘발유 권장이 적힘", "RON 95 이상 권장, 일반유는 출력 저하·연비 증가 가능 문구",
          "#투싼 고급유 권장", "보배드림 베스트 1042399 국산차게시판 (2026-10-24, 추천 29) 신형 투싼 매뉴얼 '추천 오일 및 용량' 캡처",
          [("매뉴얼 주석 5: '최적의 엔진 성능을 위해 RON 95 이상의 고급 휘발유 사용을 권장합니다. 일반 휘발유 사용 시 다소 출력이 저하되거나 연료 소비가 증가할 수 있습니다'", "원글 캡처(글자 그대로)"),
           ("연료 54L, 엔진오일 4.8L", "원글 캡처"),
           ("국내 휘발유 옥탄가(RON) 보통 91 이상, 고급 94 이상", "석유 및 석유대체연료 사업법 시행규칙 품질기준"),
           ("고급유-보통유 가격차 리터당 200~300원", "오피넷 일반 시세 범위, 추가 비용 16,200원은 54L x 300원 계산"),
           ("댓글(6) '고급유 넣을거면 누가 사', (5) '투싼에 AMG나 M시리즈 엔진 올라간 줄', (0) '권장과 필수 차이, 게임 권장사양'", "원글 댓글(대사체)")],
          "신형 투싼 매뉴얼 주석에 RON 95 이상 고급 휘발유 권장이 적혔습니다.\n일반유를 넣으면 출력이 조금 떨어지거나 기름을 더 먹을 수 있다는 문구.\n고급유는 리터당 200~300원 더 비쌉니다.\n\n#투싼 #고급휘발유 #옥탄가 #보배드림 #란빵",
          "님들은 권장이면 고급유 넣음, 그냥 일반유 넣음?",
          "연료첨가제, 차량용 핸드폰 거치대, 자동차 블랙박스 2채널, 타이어 공기주입기, 차량용 방향제",
          "엔진 종류별 차이는 캡처에 없어 '신형 투싼 매뉴얼' 로만. 가격차는 범위로 표현.", [P("m1", "화면: 현대차 매뉴얼", s0=1.0, s1=1.1)])


# ───────────────────────── 12. 테슬라 FSD 승인 신청 ─────────────────────────
def EP_fsdapply():
    S = "fsdapply"
    lines = [
        L("어제 날짜로 메일로 보냈다고 들었습니다.",
          [B("f01", "An empty National Assembly committee hearing room in Seoul with microphones and nameplates, text unreadable, wide shot", s0=1.1, s1=1.3)],
          C("biz_think", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("국감에서 국토부 장관이 밝힌 말. 테슬라코리아가 드디어 FSD 승인을 신청했다는 것.",
          [B("f02", "A white electric sedan driving on a Korean highway at dusk, hands-free style wide shot from behind, no badges visible")],
          C("jidou"), say="국감에서 국토부 장관이 밝힌 말. 테슬라코리아가 드디어 에프에스디 승인을 신청했다는 것.", em=["드디어"]),
        L("22일 메일, 23일 등기로 국토부에 서류가 들어갔음.",
          [B("f03", "A registered mail envelope and a laptop showing a sent email on a desk, Korean government office interior, text unreadable")],
          C("phone_man", "r"), say="이십이일 메일, 이십삼일 등기로 국토부에 서류가 들어갔음.", em=["등기로"], fx=[("notify_message_pop", "서류가", 0.5)]),
        L("2주 전 국감에서 테슬라 대표가 검증 요청한 적이 없다고 해서 혼이 난 뒤의 일임.",
          [B("f01", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("sorry"), say="이주 전 국감에서 테슬라 대표가 검증 요청한 적이 없다고 해서 혼이 난 뒤의 일임.",
          em=["요청한 적이 없다"], fx=[("drum_rimshot", "혼이", 0.4)]),
        L("지금 국내 테슬라 23만 9천 대 중에 FSD를 켤 수 있는 차는 22퍼센트뿐임.",
          [B("f04", "A large parking lot full of identical white electric SUVs seen from above, Korean port delivery yard, no people"),
           B("f04", at="22퍼센트", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("graph_down", "r"), say="지금 국내 테슬라 이십삼만 구천 대 중에 에프에스디를 켤 수 있는 차는 이십이퍼센트뿐임.",
          em=["22퍼센트"], em_color="yellow", fx=[("drop_futuristic", "22퍼센트", 0.5)],
          info={"kind": "bars", "at": "지금", "title": "국내 테슬라 (9월 말)", "items": [
              {"label": "FSD 가능(미국산)", "num": 53477, "suffix": "대", "at": "켤"}, {"label": "FSD 불가(중국산 등)", "num": 185491, "suffix": "대", "at": "22퍼센트", "flash": "22퍼센트"}]}),
        L("중국산 모델 3와 모델 Y 18만 대는 아예 막혀 있음.",
          [B("f05", "A dark car interior at night with a large center touchscreen showing a greyed-out menu, screen content blurred, no people")],
          C("drv_cry"), say="중국산 모델 쓰리와 모델 와이 십팔만 대는 아예 막혀 있음.", em=["아예 막혀"]),
        L("국제표준을 도입하려는데, FSD는 그 기준에도 안 맞아서 예외 승인밖에 길이 없어요.",
          [B("f06", "A stack of technical regulation documents with charts on a desk, a pair of glasses on top, text unreadable")],
          C("lawyer", "r"), dialogue=True, speaker=3, emotion="normal",
          say="국제표준을 도입하려는데, 에프에스디는 그 기준에도 안 맞아서 예외 승인밖에 길이 없어요."),
        L("개드립 분석은 국토부가 거부하면 욕먹고, 승인하면 특혜 논란이라 애매하다는 것.",
          [B("f07", "The exterior of a Korean government complex building on an overcast day, flagpoles, no people")],
          C("komatta"), em=["애매하다"], pop=("딜레마", Y, "애매하다")),
        L("국토부는 아직 접수 여부도, 검증 일정도 안 밝혔음.",
          [B("f03", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_shock", "r"), em=["검증 일정도"], em_color="yellow", fx=[("wrong_gameshow_buzz", "안", 0.45)]),
        L("님들은 FSD 국내 승인, 내년 안에 남, 안 남?", [B("f02", s0=1.0, s1=1.12)], C("biz_q"), say="님들은 에프에스디 국내 승인, 내년 안에 남, 안 남?", fx=[("pop_bubble", "안 남")]),
    ]
    build(S, lines, "테슬라 FSD 승인 신청", "국토부는 지금 딜레마", "10/22 메일·23 등기 접수, 국내 테슬라 78%는 FSD 못 켬",
          "#테슬라 FSD 승인 신청", "개드립 731674110 (추천 41) + 블로터 2026-10-23 676623 + 국민일보 9000021045",
          [("테슬라코리아 10/22 메일, 10/23 등기로 국토부 모빌리티자동차국에 감독형 FSD 승인 신청, 10/23 국토위 종합국감에서 공개", "블로터, 장종태 의원실"),
           ("홍지선 장관 '22일 어제 날짜로 메일로 보냈다고 들었다'", "블로터(대사 직접 인용)"),
           ("10/8 국감 서영득 대표 '검증 요청한 적 없다' → '승인 신청 추진'", "블로터 675303, teslafsdkr 편 근거"),
           ("9월 말 등록 238,968대, FSD 불가 185,491대(77.6%), 그중 중국산 모델3·Y 183,407대, 가능 53,477대(22.4%)", "국민일보"),
           ("국토부: 국제기준 없음, 검증 실적·계획 없음, 접수·검증 일정 미공개", "블로터, 국민일보"),
           ("'DCAS 국제표준 도입 예정, 테슬라는 표준에도 안 맞아 예외승인뿐, 거부하면 욕먹고 승인하면 특혜' 는 개드립 글쓴이 분석", "개드립 본문(대사체, 분석임을 명시)")],
          "테슬라코리아가 10월 22일 국토부에 FSD 승인을 신청했습니다.\n국내 테슬라 23만 9천 대 중 FSD를 켤 수 있는 차는 22%뿐.\n국토부는 접수 여부도 검증 일정도 아직입니다.\n\n#테슬라 #FSD #자율주행 #국토부 #란빵",
          "님들은 FSD 국내 승인, 내년 안에 남, 안 남?",
          "테슬라 핸드폰 거치대, 테슬라 센터 콘솔 트레이, 자동차 블랙박스 2채널, 차량용 공기청정기, 차량용 방향제",
          "화면에 테슬라 로고·실존 인물 없음(AI 배경 no logos). 장관·의원 실명은 대본에 안 넣음.", [B("f04", s0=1.0, s1=1.1)])


# ───────────────────────── 13. 마라톤 완주 후 운전 ─────────────────────────
def EP_marathon():
    S = "marathon"
    cap(S, "h1", "1042810_00.jpg", box=(0, 0, 1248, 560), fit=True, nofaces=True)
    cap(S, "h2", "1042810_00.jpg", box=(0, 880, 1248, 1634), cx=0.5, cy=0.5, score=0.3)
    lines = [
        L("사고 당시 상황이 기억나지 않습니다.",
          [P("h2", "화면: 헤럴드경제", s0=1.0, s1=1.15)], C("komatta", "r"), dialogue=True, speaker=3, emotion="normal"),
        L("일요일 오후 2시 50분, 춘천 의암공원 풋살장 근처 삼거리.",
          [B("w01", "A three-way intersection next to a riverside park with a futsal court fence in Chuncheon, Korea, autumn trees, afternoon, no people")],
          C("drv_smile"), say="일요일 오후 두시 오십분, 춘천 의암공원 풋살장 근처 삼거리."),
        L("카니발이 유턴하다가 인도로 올라가 보행자들을 들이받음.",
          [P("h2", "화면: 헤럴드경제", s0=1.1, s1=1.35, fx=0.6, fy=0.5), P("h2", "화면: 헤럴드경제", at="들이받음", s0=1.4, s1=1.6, fx=0.75, fy=0.5, punch=True)],
          C("jiko_man", "r"), em=["인도로"], pop=("돌진!", R, "들이받음"), shake="들이받음", fx=[("glass_smash", "들이받음", 0.5)]),
        L("65세 남성과 32세 여성이 크게 다쳤고, 35세 남성도 병원으로 갔음.",
          [B("w02", "An ambulance with rear doors open parked by a park sidewalk, emergency lights on, autumn afternoon, no people")],
          C("fire119"), say="육십오세 남성과 삼십이세 여성이 크게 다쳤고, 삼십오세 남성도 병원으로 갔음.", em=["크게 다쳤고"]),
        L("운전자는 40대 여성. 그날 춘천 마라톤 풀코스를 완주하고 집에 가던 길이었음.",
          [P("h1", "화면: 헤럴드경제", s0=1.0, s1=1.2), B("w03", "A marathon finish line arch in a Korean city with scattered paper cups on the road after the race, autumn, no people", at="풀코스")],
          C("drv_cry", "r"), say="운전자는 사십대 여성. 그날 춘천 마라톤 풀코스를 완주하고 집에 가던 길이었음.",
          em=["풀코스를 완주"], em_color="yellow", fx=[("hit_trailer_epic", "풀코스", 0.5)]),
        L("42.195킬로를 뛴 직후라, 경찰은 일시적인 의식 장애 가능성을 보고 있음.",
          [B("w04", "A runner's finisher medal and a race bib lying on a car's passenger seat, afternoon light through window, no people")],
          C("sick"), say="사십이점일구오킬로를 뛴 직후라, 경찰은 일시적인 의식 장애 가능성을 보고 있음.", em=["의식 장애"],
          info={"kind": "bars", "at": "42.195", "title": "완주 직후 운전", "items": [{"label": "풀코스", "num": 42.195, "dec": 3, "suffix": "km", "at": "42.195"}]}),
        L("마라톤도 만만하게 볼 운동이 아닌데, 운동은 본인 체력에 맞게 합시다.",
          [B("w03", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("umbrella", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("도로교통법 45조는 과로나 질병으로 정상 운전이 어려운 상태의 운전도 금지함.",
          [B("w05", "A Korean law book open on a desk next to a car key and a running shoe, soft light, no people")],
          C("judge"), say="도로교통법 사십오조는 과로나 질병으로 정상 운전이 어려운 상태의 운전도 금지함.",
          em=["과로나 질병"], em_color="yellow", fx=[("drop_futuristic", "과로나", 0.5)],
          info={"kind": "compare", "at": "도로교통법", "title": "과로 운전", "items": [
              {"label": "도로교통법 45조", "color": W, "at": "도로교통법", "rows": [["위반 시", "30만원 이하", W]]},
              {"label": "사람 다치면", "color": R, "at": "금지함", "rows": [["교특법", "업무상 과실", Y]]}]}),
        L("벌칙은 30만원 이하 벌금이지만, 사람이 다치면 교통사고처리특례법으로 넘어감.",
          [B("w06", "A police traffic accident investigation vehicle parked at a park road with cones and tape, afternoon, no people")],
          C("police", "r"), say="벌칙은 삼십마넌 이하 벌금이지만, 사람이 다치면 교통사고처리특례법으로 넘어감.", em=["교통사고처리특례법"]),
        L("님들은 풀코스 뛰고 직접 운전해서 감, 누가 데리러 옴?", [B("w04", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "데리러")]),
    ]
    build(S, lines, "풀코스 완주하고 운전", "유턴하다 인도로 돌진", "춘천 의암공원 삼거리, 카니발이 보행자 3명 들이받음. 운전자는 기억 안 난다",
          "#마라톤 완주 후 운전", "헤럴드경제 2026-10-25 19:02 (김성훈 기자) 캡처 = 보배드림 베스트 1042810 + 강원도민일보 인용",
          [("10/25 14:50 강원 춘천시 삼천동 의암공원 풋살장 인근 삼거리, 40대 A씨 카니발이 인도 보행자 들이받음", "헤럴드경제 캡처"),
           ("65세 남·32세 여 중상, 35세 남 찰과상", "헤럴드경제 캡처"),
           ("마라톤 풀코스 완주 후 귀가 중 유턴하다 사고, '사고 당시 상황이 기억나지 않는다' 진술", "헤럴드경제(강원도민일보 인용), 대사 직접 인용"),
           ("일시적 의식장애 가능성 조사", "SBS 10/26 보도(검색 결과 요약)"),
           ("도로교통법 45조 1항 과로·질병 운전 금지, 154조 3호 30만원 이하 벌금·구류", "nepla 도로교통법 조문"),
           ("보행자 부상 → 교통사고처리특례법 3조 업무상과실치상", "국가법령정보센터"),
           ("보배 원글 '마라톤도 만만하게 볼 운동이 아닌데 운동도 본인 체력에 맞게 합시다'", "원글 본문(대사체)"),
           ("기사 사진 속 사람들(구급대·경찰·시민) 모자이크, 번호판 없음", "제작 메모")],
          "마라톤 풀코스를 완주하고 집에 가던 40대 운전자가 유턴하다 인도로 올라가 보행자 3명을 들이받았습니다.\n운전자는 기억이 안 난다고 했습니다.\n도로교통법 45조는 과로 운전도 금지합니다.\n\n#춘천마라톤 #과로운전 #교통사고 #도로교통법 #란빵",
          "님들은 풀코스 뛰고 직접 운전해서 감, 누가 데리러 옴?",
          "차량용 목쿠션, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 비상삼각대, 차량용 방향제",
          "제목·본문에 사망 없음(부상 사고). 운전자 신상은 '40대 여성'까지(기사 표기).", [B("w01", s0=1.0, s1=1.1)])


EPS = [EP_bbox168, EP_rinse0, EP_bmwchase, EP_cle11, EP_spark6s, EP_z4light, EP_autop,
       EP_sojucourt, EP_uninsured, EP_cheapimport, EP_tucson95, EP_fsdapply, EP_marathon]

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in EPS:
        if not want or f.__name__[3:] in want:
            f()
