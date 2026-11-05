#!/usr/bin/env python3
"""란빵 자동차 이슈 10편 (2026-09-25) — 신차·실물 차종은 공식 뉴스룸/CC 실사 + 출처 번인, 나머지 로컬 SDXL.
script.json / prompts.tsv(생성분만) / photos.json(실사분) / upload.md 생성. 실사는 여기서 바로 1280x800 크롭+출처 번인."""
import json, os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos")
FONT = "/Users/kimyiseul/Desktop/kim/ssul/fonts/Pretendard-SemiBold.ttf"
T = ("photorealistic DSLR photograph, 35mm lens, natural available light, shallow depth of field, "
     "Korean setting, no text no letters no signage no logos no brand marks no watermark")
W1 = "a Korean woman in her early 30s, shoulder-length dark brown hair, natural light makeup"
M1 = "a Korean man in his early 30s, short black hair, clean-shaven, slim build"
M2 = "a Korean man in his mid 30s, short wavy black hair, light stubble, sturdy build"
OUTRO = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
HY, KIA, GEN, HMG = "사진: 현대자동차", "사진: 기아", "사진: 제네시스", "사진: 현대자동차그룹"

def L(text, img, sfx=None, em=None, yellow=False, dlg=None, emo=None):
    d = {"text": text, "img": img}
    if em: d["em"] = [em]
    if yellow: d["em_color"] = "yellow"
    if sfx: d["sfx"] = sfx
    if dlg:
        d["dialogue"] = True
        if dlg == "sub2": d["voice"] = "sub2"
        d["emotion"] = emo or "angry"; d["intensity"] = 2.0
    return d

def P(rel, credit, anchor=0.5):  # 실사
    return ("ph", rel, credit, anchor)

def wm(name, idx):
    m = json.load(open(os.path.join(PH, "roadster_meta.json")))
    f, a, l = m[idx]
    a = a.replace(" from Menlo Park, USA", "")
    return P(f.replace("ph/", ""), f"사진: {a} / Wikimedia Commons, {l}")

def lst(name):
    return [l.strip().replace("ph/", "") for l in open(os.path.join(PH, f"{name}_list.txt"))]

XG, I9B, I9C, EV9, EV9C, EV9D, GV, PV = (lst(n) for n in ["xgran","ioniq9b","ioniq9c","ev9","ev9c","ev9d","gv80","pv5"])

EP = {}

EP["roadster"] = dict(
 t1='9년째 차는 안 나왔는데', t2='또 예약금 7천만 원?',
 hook='9년째 차는 안 나왔는데 또 예약금 7천만 원 받는 차', bar='9년 기다린 테슬라 로드스터, 예약금만 7천만 원',
 kw='#테슬라로드스터', tags='#shorts #테슬라로드스터 #테슬라 #로드스터 #전기차', shop='없음',
 comment='님들이면 7천 내고 기다릴 거임?',
 src='테슬라 2세대 로드스터 2017.11 첫 공개 이후 최소 8차례 연기·고객 인도 0대 ; 2026.9 예약 재개 — 5천 달러 선결제 후 10일 내 4만5천 달러, 총 5만 달러(약 6,920만 원) ; 10월 1일 공개 예고 ; 폴리마켓 2026년 말 인도 확률 5% 미만 (오토헤럴드·디지털투데이·SBS Biz 2026-09)',
 desc='테슬라가 2017년 11월 처음 공개한 2세대 로드스터의 예약 접수를 다시 열었음. 그동안 최소 8차례 일정이 밀렸고 고객에게 인도된 차는 아직 없음.\n새 예약은 5천 달러를 먼저 결제하고 10일 안에 4만5천 달러를 더 보내는 방식으로, 총 5만 달러(약 6,920만 원)임. 테슬라는 10월 1일 공개를 예고했음.\n예측시장 폴리마켓에서는 2026년 말까지 고객 인도 가능성을 5% 미만으로 보고 있음.',
 lines=[
  L("9년째 차는 안 나왔는데 또 예약금 7천만 원을 받는 차가 있음.",1),
  L("테슬라 2세대 로드스터임.",2,"ding",em="로드스터"),
  L("2017년 11월에 머스크가 무대에서 처음 공개한 차였음.",3,"whoosh"),
  L("제로백 2초 안쪽이라고 해서 전 세계가 난리가 났었음.",4,"eng"),
  L("근데 그 뒤로 일정이 최소 8번 밀렸고, 지금까지 고객한테 넘어간 차는 한 대도 없음.",5,"thud",em="한 대도 없음",yellow=True),
  L("그런데 이번에 예약을 다시 열었음.",6,"tick"),
  L("5천 달러 먼저 내고, 10일 안에 4만5천 달러를 더 보내야 확정임.",7,"cash",em="10일 안에"),
  L("다 합치면 5만 달러, 우리 돈으로 약 7천만 원임.",8,"cash",em="약 7천만 원",yellow=True),
  L("9년 기다린 사람한테 또 돈을 내라고?!",9,"boing",dlg="sub2"),
  L("테슬라는 10월 1일에 공개하겠다고 예고했음.",10,"pop",em="10월 1일"),
  L("근데 예측시장에서는 올해 안에 실제로 받을 확률을 5%도 안 되게 보고 있음.",11,"ding",em="5%"),
  L("님들이면 7천 내고 기다릴 거임?",12),
  OUTRO],
 imgs=[wm("roadster",9), wm("roadster",6), wm("roadster",2), wm("roadster",14), wm("roadster",7), wm("roadster",11),
       f"close-up of a hand holding a credit card over a laptop checkout page, dim room, {T}",
       wm("roadster",13), f"{M2} staring at a laptop at night with a shocked face, {T}", wm("roadster",1),
       wm("roadster",10), wm("roadster",0)])

EP["crackdown10"] = dict(
 t1='"깜빡이 안 켜면 벌점 10점"', t2='10월부터 진짜임?',
 hook='"깜빡이 안 켜면 벌점 10점" 10월부터 진짜임?', bar='10월부터 깜빡이 안 켜면 벌점 10점? 팩트체크',
 kw='#방향지시등', tags='#shorts #방향지시등 #벌점 #집중단속 #안전띠', shop='없음',
 comment='님들 주변에 깜빡이 안 켜는 사람 몇 명 있음?',
 src='경찰청 기초질서 캠페인 — 2026.8.1~9.30 계도, 10.1~12.31 집중단속(전 좌석 안전띠·이륜차 안전모·방향지시등) ; 안전띠·방향지시등 벌점 10점 부과안은 2026.8 입법예고 단계로 9.17 기준 시행 규정 아님(톱스타뉴스·오토트리뷴) ; 현행 방향지시 불이행 승용 범칙금 3만 원, 안전띠 미착용 3만 원',
 desc='"10월부터 깜빡이 안 켜면 벌점 10점"이라는 이야기가 퍼졌지만, 벌점 10점 부과는 경찰청이 8월에 입법예고한 개정안 단계로 9월 기준 시행 중인 규정이 아님. 실제 시행 여부와 시점은 절차가 끝나야 확정됨.\n확정된 건 단속 일정임. 8월 1일~9월 30일 계도기간을 거쳐 10월 1일~12월 31일 전 좌석 안전띠, 이륜차 안전모, 방향지시등 점등을 집중단속함.\n현행 기준으로 방향지시 불이행은 승용차 범칙금 3만 원, 안전띠 미착용도 3만 원임.',
 lines=[
  L("10월부터 깜빡이 안 켜면 벌점 10점이라는 말이 돌고 있음.",1),
  L("벌점 40점이면 면허 정지라서 운전자들이 긴장했음.",2,"tick",em="40점"),
  L("깜빡이 몇 번 안 켰다고 면허 정지라고?!",3,"boing",dlg="sub2"),
  L("근데 여기서 반은 맞고 반은 틀림.",4,"dudung",em="반은 틀림",yellow=True),
  L("벌점 10점은 경찰청이 8월에 입법예고한 개정안이라, 아직 시행 중인 규정이 아님.",5,"ding",em="아직 시행 중인 규정이 아님"),
  L("진짜인 건 단속 일정임.",6,"pop"),
  L("9월까지는 계도기간이었고, 10월 1일부터 12월 말까지 석 달간 집중단속임.",7,"siren",em="10월 1일"),
  L("대상은 전 좌석 안전띠, 오토바이 안전모, 그리고 방향지시등임.",8,em="방향지시등"),
  L("지금 기준으로 깜빡이 안 켜면 승용차 범칙금 3만 원이고,",9,"cash"),
  L("뒷좌석 안전띠 안 매도 운전자한테 3만 원이 나옴.",10,"cash",em="3만 원"),
  L("벌점은 아직 확정 전이지만 이 흐름이면 시간문제임.",11,"thud"),
  L("차로 바꿀 때 한 번씩만 탁 켜면 끝나는 거임.",12,"ding"),
  OUTRO],
 imgs=[f"a car changing lanes on a Korean city road without turn signal, seen from behind, daytime, {T}",
       f"close-up of a Korean driver license card on a car dashboard, {T}",
       f"{M2} in a driver seat throwing his hands up in disbelief, {T}",
       f"a Korean traffic police officer holding a notebook beside a road, {T}",
       f"stack of official documents with a pen on a government office desk, {T}",
       f"a large desk calendar showing autumn months with a pen, {T}",
       f"a Korean police traffic checkpoint on a city road with officers and glowing batons, daytime, {T}",
       f"a motorcycle rider wearing a helmet stopped at an intersection beside cars, {T}",
       f"close-up of a car amber turn signal blinking on a rear light, {T}",
       f"interior of a car back seat with passengers wearing seat belts, {T}",
       f"{M1} in a driver seat looking at a smartphone news article with a worried face, parked car, {T}",
       f"close-up of a hand flicking a turn signal lever on a steering column, {T}"])

EP["ioniq9recall"] = dict(
 t1='아이오닉9', t2='2열 시트 리콜 1만5천 대',
 hook='아이오닉9 1만5천 대 리콜, 이유가 2열 시트라고?', bar='아이오닉9 국내 1만5천 대 리콜, 2열 전동시트 끼임',
 kw='#아이오닉9리콜', tags='#shorts #아이오닉9 #리콜 #현대차 #전동시트', shop='없음',
 comment='님들 차 전동시트 끼임 방지 테스트해본 적 있음?',
 src='현대차 아이오닉9 2열 전동 시트 끼임 방지 기능 이상 리콜 — 국내 약 1만5천 대(아시아경제 2026-09-22 단독), 미국 2025.3.17~2026.5.4 생산 5,360대, 불만 5건 중 부상 주장 2건 ; 시정조치 시트 제어기 소프트웨어 업데이트(서비스센터 또는 무선 OTA) (오토헤럴드·M포스트)',
 desc='현대차 아이오닉9의 2열 전동 시트가 작동 중 탑승자나 물체에 닿았을 때 끼임 방지 기능이 제대로 반응하지 않을 수 있어 리콜에 들어갔음. 국내 대상은 약 1만5천 대로 보도됐고, 미국에서는 2025년 3월 17일~2026년 5월 4일 생산분 5,360대가 대상임.\n미국에서는 관련 불만 5건 중 부상을 주장한 사례가 2건 보고됐음.\n조치는 시트 제어기 소프트웨어 업데이트로, 서비스센터 방문 또는 무선 업데이트(OTA)로 받을 수 있음. 대상 여부는 자동차리콜센터에서 차대번호로 확인 가능.',
 lines=[
  L("아이오닉9이 국내에서만 1만5천 대 리콜에 들어감.",1),
  L("근데 이유가 배터리도 모터도 아니고 2열 시트임.",2,"tick",em="2열 시트",yellow=True),
  L("아이오닉9은 2열 시트를 버튼으로 접고 미는 전동 시트임.",3,"whoosh"),
  L("원래는 움직이다가 뭔가 닿으면 바로 멈춰야 하는데,",4),
  L("이 끼임 방지 기능이 제대로 반응 안 할 수 있다는 게 확인됐음.",5,"thud",em="끼임 방지 기능"),
  L("특히 아이가 시트 사이에 끼면 다칠 수 있는 구조임.",6,"siren",em="아이"),
  L("미국에서는 불만 5건 중에 다쳤다는 주장이 2건 나왔음.",7,"ding",em="2건"),
  L("그럼 차를 맡겨야 하는 거임?!",8,"boing",dlg="sub1"),
  L("다행히 부품 교체가 아니라 시트 제어 소프트웨어 업데이트임.",9,"pop",em="소프트웨어 업데이트"),
  L("서비스센터에 가도 되고, 무선 업데이트로 집에서 받을 수도 있음.",10),
  L("업데이트 전까지는 아이 있을 때 시트 버튼 누르기 전에 한 번 보고 누르셈.",11,"ding"),
  L("아이오닉9 타는 친구 있으면 이거 보내주셈.",12),
  OUTRO],
 imgs=[P(I9C[0],HY), P(I9C[16],HY), P(I9B[8],HY), P(I9C[9],HY), P(I9C[5],HY),
       f"a child's small hand near a folding car seat hinge inside a large SUV, close-up, soft light, {T}",
       f"a stack of paper complaint forms on a desk with a pen, {T}",
       f"{W1} holding a smartphone in a parking lot looking concerned, {T}",
       P(I9B[9],HY), P(I9C[4],HY), f"{W1} leaning into an SUV rear door checking a child seat, {T}", P(I9C[7],HY)])

EP["rental490"] = dict(
 t1='"범퍼 흠집이네요"', t2='렌터카 반납하다 490만 원',
 hook='"범퍼 흠집이네요" 렌터카 반납하다 490만 원 청구받은 사람', bar='연휴 렌터카 반납했더니 흠집 수리비 490만 원',
 kw='#렌터카', tags='#shorts #렌터카 #렌터카수리비 #소비자원 #추석연휴', shop='블랙박스',
 comment='님들 렌터카 빌릴 때 차 한 바퀴 영상 찍음?',
 src='렌터카 반납 시 범퍼 흠집 수리비 요구, 근거 자료 요청하자 청구액 490만 원으로 상향·법적 분쟁 사례(머니투데이 2026-07-23 등 보도) ; 한국소비자원 렌터카 피해구제 신청 최근 3년 1,438건·증가 추세 ; 예방: 인수·반납 시 동일 기준 사진·영상 기록 (사례는 보도 내용 재구성)',
 desc='렌터카를 반납한 뒤 범퍼 흠집을 이유로 수리비를 요구받고, 근거 자료를 요청하자 청구액이 490만 원까지 올라가 분쟁으로 번진 사례가 보도됐음. 업체가 지목한 부위는 이용자가 찍은 영상의 사각지대라 확인이 어려웠음.\n한국소비자원에 접수된 렌터카 피해구제 신청은 최근 3년간 1,438건으로 해마다 늘고 있음.\n분쟁을 줄이려면 차를 받을 때와 반납할 때 같은 기준으로 차 전체를 사진·영상으로 남기고, 수리비를 청구받으면 견적서 등 근거 자료를 요구하는 게 좋음.',
 lines=[
  L("연휴에 렌터카 반납하다가 490만 원을 청구받은 사람이 있었음.",1),
  L("반납할 때 직원이 범퍼 아래를 가리키면서 이렇게 말했음.",2,"whoosh"),
  L("여기 범퍼 흠집이네요. 수리비 나오셔야 해요!",3,"eng",dlg="sub2",emo="happy"),
  L("빌릴 때 영상을 찍어두긴 했는데 하필 그 부위가 사각지대였음.",4,"tick",em="사각지대"),
  L("근거를 보여달라고 했더니 자료는 안 주고 청구액이 490만 원으로 올라갔음.",5,"thud",em="490만 원",yellow=True),
  L("결국 법적 공방까지 갔음.",6,"siren"),
  L("이런 렌터카 피해가 소비자원에 최근 3년간 1,438건 들어왔고 해마다 늘고 있음.",7,"ding",em="1,438건"),
  L("그럼 빌릴 때 뭘 해야 되는데?!",8,"boing",dlg="sub1"),
  L("차 받을 때 범퍼 아래, 휠, 지붕까지 한 바퀴 영상으로 찍고,",9,em="범퍼 아래"),
  L("반납할 때도 똑같은 순서로 한 번 더 찍어야 함.",10,"pop",em="똑같은 순서",yellow=True),
  L("수리비를 청구받으면 견적서 같은 근거 자료부터 달라고 하셈.",11,"cash"),
  L("연휴에 렌터카 쓰는 친구 있으면 이거 보내주셈.",12),
  OUTRO],
 imgs=[f"a Korean rental car return lot with rows of white sedans, daytime, {T}",
       f"{M2} as a rental car staff member in a polo shirt crouching and pointing at a car bumper, {T}",
       f"{M2} as a rental car staff member in a polo shirt smiling politely holding a clipboard, {T}",
       f"{M1} filming a car with a smartphone in a parking lot, {T}",
       f"close-up of a repair estimate paper with large numbers blurred on a counter, {T}",
       f"{M1} and {M2} arguing at a rental car office counter, {T}",
       f"stack of consumer complaint documents on an office desk, {T}",
       f"{W1} raising an eyebrow questioning at a rental car counter, {T}",
       f"close-up of a smartphone recording video of a car front bumper low angle, {T}",
       f"{M1} walking around a white sedan filming with a smartphone, parking lot, {T}",
       f"close-up of a hand receiving a printed estimate document at a counter, {T}",
       f"{M1} and {W1} loading luggage into a rental car trunk, holiday, {T}"])

EP["gv80hev"] = dict(
 t1='GV80 하이브리드', t2='다음 달 나오는데 가격이...',
 hook='다음 달 나오는 GV80 하이브리드, 352마력인데 가격이 관건', bar='GV80 하이브리드 다음 달 출시, 8천만 원 넘을까?',
 kw='#GV80하이브리드', tags='#shorts #GV80하이브리드 #제네시스 #GV80 #하이브리드', shop='없음',
 comment='님들이 보기에 GV80 하이브리드 얼마면 살 만함?',
 src='제네시스 차세대 2.5 터보 하이브리드 시스템 공개(현대자동차그룹 뉴스룸) — 시스템 최고출력 352마력·최대토크 54.0kgf·m(2.5 터보 대비 약 16%·26%↑), 병렬 P1·P2, 하이브리드 첫 액냉 배터리, 연비 25% 이상 개선, 0-100km/h 약 7.1초(자체 측정) ; 판매 10월 개시 예정·가격 미정, 업계 8천만 원 문턱 관측(파이낸셜뉴스 2026-09-23)',
 desc='제네시스 GV80 하이브리드가 다음 달 판매를 시작할 예정임. 2.5 터보 엔진에 모터 두 개(P1·P2)를 붙인 병렬 하이브리드로 시스템 최고출력 352마력, 최대토크 54.0kgf·m를 내며, 기존 2.5 터보보다 출력은 약 16%, 토크는 약 26% 높음.\n하이브리드 최초로 수냉식 배터리를 적용했고 연비는 25% 이상 개선됐다는 게 제네시스 설명임. 0→100km/h는 약 7.1초(자체 측정).\n가격은 판매 시점에 공개되며, 업계에서는 시작가 8천만 원 아래 유지 여부를 관건으로 봄.',
 lines=[
  L("다음 달 나오는 GV80 하이브리드, 352마력인데 가격이 관건임.",1),
  L("제네시스가 처음으로 내놓는 뒷바퀴굴림 기반 하이브리드임.",2,"ding",em="처음"),
  L("2.5 터보 엔진에 모터 두 개를 붙인 구조고,",3,"whoosh"),
  L("합쳐서 352마력, 기존 2.5 터보보다 출력은 16%, 토크는 26% 세짐.",4,"eng",em="352마력",yellow=True),
  L("연비는 25% 넘게 좋아졌다고 함.",5,"pop",em="25%"),
  L("모터로만 가는 구간을 늘려서 전기차처럼 조용하게 나가는 게 목표임.",6),
  L("제로백은 자체 측정 7.1초임.",7,"tick"),
  L("그래서 얼마인데?!",8,"boing",dlg="sub2"),
  L("가격은 아직 안 나왔고 판매 시작할 때 공개함.",9,"thud"),
  L("업계에서는 시작가가 8천만 원 아래로 나오느냐가 흥행을 가른다고 봄.",10,"cash",em="8천만 원",yellow=True),
  L("가솔린이랑 차이가 천만 원 안쪽이면 해볼 만하다는 얘기임.",11),
  L("님들이 보기에 얼마면 살 만함?",12),
  OUTRO],
 imgs=[P(GV[0],GEN), P(GV[5],GEN), P(GV[1],GEN), P(GV[7],GEN), P(GV[3],GEN), P(GV[2],GEN),
       P(GV[6],GEN), f"{M2} raising his eyebrows in a car showroom, {T}", P(XG[13],GEN),
       f"close-up of Korean banknotes and a car key fob on a table, {T}", P(GV[0],GEN,0.3), P(GV[1],GEN,0.7)])

EP["ev9cut"] = dict(
 t1='나올 땐 7천만 원대였는데', t2='1,600만 원 내린 EV9',
 hook='나올 땐 7천만 원대였는데 1,600만 원 내린 EV9', bar='기아 EV9, 시작가가 1,600만 원 내려간 이유',
 kw='#EV9', tags='#shorts #EV9 #기아 #전기차 #가격인하', shop='없음',
 comment='님들 EV9 지금 가격이면 살 만함?',
 src='2026 EV9 판매가(세제혜택 후) 스탠다드 라이트 6,197만 원부터 — 엔트리 라이트 트림 신설(현대자동차그룹 뉴스룸) ; 출시 초기 7천만 원대 후반 시작 대비 약 1,600만 원 인하(더드라이브·뉴스와) ; 9월 기본 혜택 최대 250만 원 ; 미국 딜러 할인 최대 1만6천 달러',
 desc='기아 EV9의 국내 시작가가 출시 초기보다 약 1,600만 원 내려갔음. 2026 EV9은 엔트리 트림 \'라이트\'를 새로 넣어 스탠다드 라이트가 세제혜택 후 6,197만 원부터 시작함(보조금 별도).\n9월에는 생산 시점 등에 따라 최대 250만 원 기본 혜택도 있음. 미국에서는 딜러 할인까지 더해 최대 1만6천 달러 넘게 깎아 파는 곳도 있음.\n가격·혜택은 트림과 시점에 따라 다름.',
 lines=[
  L("나올 땐 7천만 원대였는데 1,600만 원 내린 차가 있음.",1),
  L("기아 대형 전기 SUV EV9임.",2,"ding",em="EV9"),
  L("처음 나왔을 때 시작 가격이 7천만 원대 후반이었음.",3,"whoosh"),
  L("근데 지금 2026년형 라이트 트림은 6,197만 원부터 시작함.",4,"cash",em="6,197만 원",yellow=True),
  L("엔트리 트림을 새로 만들면서 문턱을 확 낮춘 거임.",5,"pop"),
  L("9월엔 여기서 최대 250만 원을 또 깎아줌.",6,"cash",em="250만 원"),
  L("미국은 더 심해서 딜러 할인까지 합치면 1만6천 달러 넘게 빼주는 데도 있음.",7,"thud",em="1만6천 달러"),
  L("그럼 먼저 산 사람은 뭐가 되는 거임?!",8,"boing",dlg="sub2"),
  L("대형 전기차가 생각보다 안 팔리니까 가격으로 밀어붙이는 거임.",9,"tick"),
  L("대신 3열 시트, 넓은 실내는 그대로라 지금 사는 사람은 이득이라는 얘기도 있음.",10),
  L("보조금까지 붙으면 5천만 원대도 보인다는 계산이 나옴.",11,"ding",em="5천만 원대"),
  L("님들 이 가격이면 살 만함?",12),
  OUTRO],
 imgs=[P(EV9D[1],KIA), P(EV9C[0],KIA), P(EV9D[8],KIA), P(EV9D[0],KIA), P(EV9[1],KIA),
       f"close-up of Korean banknotes stacked next to a car key on a showroom desk, {T}",
       P(EV9D[6],KIA), f"{M2} in a car showroom throwing his hands up in disbelief, {T}",
       P(EV9D[2],KIA), P(EV9D[7],KIA), P(EV9D[4],KIA), P(EV9D[3],KIA)])

EP["xgrancoupe"] = dict(
 t1='제네시스가', t2='2도어 쿠페를 진짜 만드나',
 hook='제네시스가 2도어 쿠페를 진짜 만드나? 미국 특허 등록', bar='제네시스 X 그란 쿠페·컨버터블, 미국 디자인 특허 등록',
 kw='#제네시스', tags='#shorts #제네시스 #X그란쿠페 #컨버터블 #콘셉트카', shop='없음',
 comment='님들 이거 나오면 제네시스 2도어 탈 거임?',
 src='제네시스 X 그란 쿠페·X 그란 컨버터블 콘셉트 — 2025 서울모빌리티쇼(2025.4.3) 세계 최초 공개, G90 기반 2도어(현대자동차그룹 뉴스룸) ; 미국 디자인 특허 X 그란 컨버터블 2026.8.4 US D1,138,892 S, X 그란 쿠페 2026.8.25 US D1,144,037 S, 미국 출원 2025.7.29·한국 우선권 2025.3.19 (오토헤럴드·M포스트 2026-09) ; 양산 여부 미확정',
 desc='제네시스가 지난해 서울모빌리티쇼에서 처음 공개한 2도어 콘셉트카 X 그란 쿠페와 X 그란 컨버터블이 미국 디자인 특허를 받았음. 컨버터블은 2026년 8월 4일(US D1,138,892 S), 쿠페는 8월 25일(US D1,144,037 S) 등록됐음.\n두 차는 플래그십 세단 G90을 기반으로 만든 2도어 콘셉트로, 긴 보닛과 뒤로 밀어낸 캐빈으로 전통적인 그랜드 투어러 비율을 냈음.\n디자인 특허는 양산 확정이 아니라 디자인 보호 절차이며, 제네시스는 양산 여부를 공식 발표하지 않았음.',
 lines=[
  L("제네시스가 2도어 쿠페를 진짜 만드는 거 아니냐는 말이 나옴.",1),
  L("지난해 서울모빌리티쇼에서 처음 공개한 엑스 그란 쿠페랑 엑스 그란 컨버터블임.",2,"ding",em="엑스 그란 쿠페"),
  L("둘 다 제네시스 제일 큰 세단 G90을 바탕으로 문을 두 개로 줄인 차임.",3,"whoosh",em="G90"),
  L("보닛은 길게 빼고 실내는 뒤로 밀어서 전형적인 고급 쿠페 비율을 냈음.",4),
  L("근데 이 두 대가 올해 8월에 미국 디자인 특허를 받았음.",5,"thud",em="미국 디자인 특허",yellow=True),
  L("컨버터블은 8월 4일, 쿠페는 8월 25일 등록됐음.",6,"tick"),
  L("그럼 이제 나오는 거임?!",7,"boing",dlg="sub2"),
  L("디자인 특허는 모양을 보호하는 절차라 양산 확정은 아님.",8,"dudung",em="양산 확정은 아님"),
  L("근데 전시용 콘셉트를 굳이 특허까지 챙긴 건 뭔가 있다는 해석이 나옴.",9,"pop"),
  L("나오면 벤틀리, 애스턴마틴 쪽이랑 붙는 급이라는 얘기도 있음.",10,"eng",em="벤틀리"),
  L("실내도 오렌지 가죽에 G90 급으로 꾸며놨음.",11),
  L("님들 이거 나오면 제네시스 2도어 탈 거임?",12),
  OUTRO],
 imgs=[P(XG[6],GEN), P(XG[0],GEN), P(XG[1],GEN), P(XG[7],GEN), P(XG[4],GEN), P(XG[2],GEN),
       P(XG[9],GEN), f"stack of patent documents with an official stamp on a desk, {T}", P(XG[5],GEN),
       P(XG[1],GEN,0.2), P(XG[8],GEN), P(XG[6],GEN,0.7)])

EP["kiaboys"] = dict(
 t1='현대·기아', t2='미국서 1조 원 소송 재점화',
 hook='현대·기아 미국에서 1조 원 소송 다시 열림, 이유가 이모빌라이저?', bar='현대·기아 미국 도난 소송 재점화, 청구액 10억 달러',
 kw='#현대기아', tags='#shorts #현대차 #기아 #기아보이즈 #이모빌라이저', shop='없음',
 comment='님들 이건 제조사 책임이라고 봄, 훔친 사람 책임이라고 봄?',
 src='미국 제9연방항소법원 2026.9.14 — 현대차·기아 한국 본사 상대 보험사 소송을 대인관할권 부족으로 기각한 캘리포니아 연방법원 결정 파기, 오렌지카운티 연방법원 환송 ; 보험사 약 200곳, 지급 보험금 등 10억 달러(약 1조3,840억 원) 이상 구상 청구 ; 쟁점 엔진 이모빌라이저 미장착 ; 배상 명령 아님 (더드라이브·미주중앙일보·비즈니스포스트 2026-09)',
 desc='미국 제9연방항소법원이 9월 14일, 보험사들이 현대차·기아 한국 본사를 상대로 낸 소송을 관할권 부족으로 기각했던 1심 결정을 뒤집었음. 사건은 캘리포니아 오렌지카운티 연방법원으로 돌아가 다시 심리됨.\n약 200개 보험사는 이모빌라이저가 없는 일부 현대·기아 차량의 도난과 파손으로 지급한 보험금 등이 10억 달러(약 1조3,840억 원)를 넘는다며 구상을 청구하고 있음.\n이번 결정은 배상 명령이 아니라 소송 절차를 다시 진행할 수 있다는 의미임.',
 lines=[
  L("현대·기아가 미국에서 1조 원짜리 소송을 다시 하게 됐음.",1),
  L("시작은 몇 년 전 미국 틱톡에서 유행한 도난 챌린지였음.",2,"whoosh"),
  L("일부 현대·기아 차에 이모빌라이저가 없어서 쉽게 시동을 걸 수 있다는 영상이 퍼졌음.",3,"thud",em="이모빌라이저"),
  L("이모빌라이저는 전용 키가 아니면 시동이 안 걸리게 막는 장치임.",4,"ding"),
  L("그 뒤로 도난이 쏟아졌고, 보험사들이 낸 보험금이 10억 달러를 넘었음.",5,"cash",em="10억 달러",yellow=True),
  L("그래서 보험사 약 200곳이 그 돈을 돌려달라고 소송을 걸었음.",6,"siren",em="약 200곳"),
  L("근데 1심은 한국 본사까지 재판할 권한이 없다고 기각했었음.",7,"tick"),
  L("그런데 9월 14일 항소법원이 그 결정을 뒤집었음.",8,"dudung",em="뒤집었음"),
  L("그럼 1조 원 물어줘야 되는 거임?!",9,"boing",dlg="sub2"),
  L("배상하라는 게 아니라 재판을 다시 하라는 거라, 결과는 이제부터임.",10,"pop",em="재판을 다시 하라는 거"),
  L("원래 법원으로 돌아가서 보험사 청구를 다시 따지게 됨.",11),
  L("님들은 이게 제조사 책임 같음, 훔친 사람 책임 같음?",12),
  OUTRO],
 imgs=[f"an American federal courthouse exterior with columns, daytime, {T.replace('Korean setting','American setting')}",
       f"a teenager in a hoodie filming a smartphone video on a dark suburban street at night, face hidden, {T.replace('Korean setting','American setting')}",
       f"a broken steering column of a car with exposed wires, close-up, {T}",
       f"close-up of a car key fob next to a push start button, {T}",
       f"a row of damaged cars with broken windows in a police impound lot, {T.replace('Korean setting','American setting')}",
       f"a stack of legal filings with a gavel on a desk, {T}",
       f"a judge bench in an empty American courtroom, solemn, {T.replace('Korean setting','American setting')}",
       f"close-up of a gavel striking, dramatic light, {T}",
       f"{M2} reading news on a smartphone with a shocked face, office, {T}",
       f"lawyers in suits walking up courthouse steps, from behind, {T.replace('Korean setting','American setting')}",
       f"aerial view of a large federal building in Southern California, sunny, {T.replace('Korean setting','American setting')}",
       f"a parked car with a steering wheel lock device installed, close-up, {T}"])

EP["pv5ioniq6n"] = dict(
 t1='자동차 본고장 독일에서', t2='한국 차 2대가 1위',
 hook='자동차 본고장 독일 올해의 차에서 한국 차 2대가 1위 먹음', bar='독일 올해의 차 2027, 아이오닉 6 N·PV5 부문 1위',
 kw='#독일올해의차', tags='#shorts #아이오닉6N #PV5 #독일올해의차 #현대차', shop='없음',
 comment='님들은 둘 중에 뭐가 더 탐남?',
 src='2027 독일 올해의 차(GCOTY) — 현대 아이오닉 6 N 퍼포먼스 부문, 기아 PV5 콤팩트(2만5천~4만 유로) 부문 1위, 5개 부문 1위 차량이 최종 본선 진출, 11월 2일 최종 발표(현대자동차그룹 저널·오토헤럴드 2026-09) ; 아이오닉 6 N 최대 650마력·제로백 3.2초(유카포스트)',
 desc='현대차 아이오닉 6 N과 기아 PV5가 독일 올해의 차(GCOTY) 2027에서 각각 퍼포먼스 부문과 콤팩트 부문(2만5천~4만 유로) 1위에 올랐음.\n5개 부문 1위 차량이 최종 본선에 올라 11월 2일 단 한 대의 \'독일 올해의 차 2027\'이 발표됨.\n아이오닉 6 N은 최대 650마력, 0→100km/h 3.2초의 고성능 전기차이고, PV5는 기아의 첫 전용 PBV(목적기반차량)임.',
 lines=[
  L("자동차 본고장 독일 올해의 차에서 한국 차 두 대가 1위를 먹었음.",1),
  L("독일 올해의 차 2027에서 5개 부문 중 두 개를 가져갔음.",2,"ding",em="5개 부문 중 두 개"),
  L("첫 번째는 현대 아이오닉 6 N, 퍼포먼스 부문 1위임.",3,"whoosh",em="퍼포먼스 부문"),
  L("최대 650마력에 제로백 3.2초짜리 전기차임.",4,"eng",em="3.2초",yellow=True),
  L("포르쉐, BMW가 자기 동네에서 붙는 부문이라 더 의미가 큼.",5),
  L("두 번째는 기아 PV5, 콤팩트 부문 1위임.",6,"pop",em="PV5"),
  L("짐차랑 승합차를 오가는 기아 첫 목적기반차량임.",7),
  L("짐차가 올해의 차라고?!",8,"boing",dlg="sub2"),
  L("유럽은 이런 밴 수요가 커서, 실용성으로 제대로 평가받은 거임.",9,"tick"),
  L("그리고 이 두 대가 부문 1위 5대만 올라가는 최종 본선에 들어갔음.",10,"ding",em="최종 본선"),
  L("최종 1대는 11월 2일에 발표됨.",11,"thud",em="11월 2일"),
  L("님들은 둘 중에 뭐가 더 탐남?",12),
  OUTRO],
 imgs=[P(PV[3],HMG), P(PV[5],HY), P(PV[10],HY,0.3), P(PV[10],HY), P(PV[8],HY), P(PV[15],KIA),
       P(PV[14],KIA), P(PV[6],KIA), P(PV[13],KIA), P(PV[12],KIA), P(PV[16],KIA), P(PV[3],HMG,0.3)])

EP["sleepdrive"] = dict(
 t1='시속 97km로 달리는데', t2='운전자가 자고 있었다',
 hook='시속 97km로 달리는데 운전자가 자고 있었다', bar='자율주행 켜고 고속도로에서 잠든 운전자의 최후',
 kw='#자율주행', tags='#shorts #자율주행 #FSD #졸음운전 #테슬라', shop='졸음방지 껌',
 comment='님들 반자율주행 켜놓고 딴짓해본 적 있음? 솔직히',
 src='미국 캘리포니아고속도로순찰대(CHP) 솔라노 카운티 고속도로 — 테슬라 FSD(감독형) 작동 중 시속 60마일(약 97km) 주행, 운전자 잠든 듯한 모습 오토바이 경찰관 발견 후 정차 (머니투데이·아시아경제·문화일보 2026-09-20~22) ; FSD 등은 레벨2 운전자 보조, 운전 책임은 운전자',
 desc='미국 캘리포니아 솔라노 카운티 고속도로에서 테슬라의 FSD(감독형) 기능을 켠 채 시속 60마일(약 97km)로 달리던 차의 운전자가 잠든 듯한 모습으로 고속도로순찰대(CHP) 오토바이 경찰관에게 발견돼 정차 조치됐음.\n경찰은 FSD 같은 기능은 자율주행이 아니라 레벨2 운전자 보조 시스템이며, 기능을 켰다고 운전 책임이 차로 넘어가지 않는다고 경고했음.\n국내에서 판매되는 차량의 차로 유지·차간 거리 유지 기능 역시 운전자 보조 기능으로, 운전자는 항상 전방을 주시해야 함.',
 lines=[
  L("시속 97km로 달리는 차 안에서 운전자가 자고 있었음.",1),
  L("미국 캘리포니아 고속도로 얘기임.",2,"whoosh"),
  L("오토바이 순찰 경찰이 옆에 붙어서 보니까 운전자가 선글라스를 쓴 채 축 늘어져 있었음.",3,"siren",em="축 늘어져"),
  L("차는 테슬라 FSD를 켠 상태로 혼자 차로를 따라가고 있었음.",4,"tick",em="FSD"),
  L("경찰이 옆에서 깨워서 겨우 세웠음.",5,"thud"),
  L("자율주행이면 자도 되는 거 아님?!",6,"boing",dlg="sub2"),
  L("근데 이건 자율주행이 아니라 레벨2 운전자 보조 기능임.",7,"ding",em="레벨2 운전자 보조",yellow=True),
  L("차가 운전을 도와줄 뿐이고, 법적으로 운전하는 사람은 여전히 운전자임.",8,em="여전히 운전자"),
  L("사고 나면 책임도 전부 운전자한테 감.",9,"cash"),
  L("우리나라에서 파는 차들 차로 유지, 앞차 따라가기 기능도 전부 같은 보조 기능임.",10,"pop"),
  L("그래서 핸들에서 손 오래 떼면 경고가 뜨는 거임.",11),
  L("졸리면 휴게소 들르셈. 기능은 운전자를 대신 안 해줌.",12,"ding"),
  OUTRO],
 imgs=[f"a white electric sedan cruising on a California freeway at dusk, {T.replace('Korean setting','American setting')}",
       f"aerial view of a California highway with light traffic, golden hour, {T.replace('Korean setting','American setting')}",
       f"a highway patrol motorcycle officer riding beside a car on a freeway, {T.replace('Korean setting','American setting')}",
       f"a man wearing dark sunglasses slumped asleep in a driver seat, hands off the steering wheel, view through side window, {T.replace('Korean setting','American setting')}",
       f"a car pulled over on a freeway shoulder with a police motorcycle behind it with flashing lights, {T.replace('Korean setting','American setting')}",
       f"{M2} in a driver seat leaning back relaxed with arms crossed, {T}",
       f"close-up of a car dashboard screen showing lane lines graphics, no text, {T}",
       f"close-up of hands holding a steering wheel firmly on a highway, {T}",
       f"a wrecked car after a highway crash, police lights, {T}",
       f"interior view of a Korean driver on a highway with hands on the wheel, daytime, {T}",
       f"a steering wheel with a glowing warning light on the dashboard, close-up, {T}",
       f"a Korean highway rest area parking lot at night with cars, {T}"])

ORDER = ["roadster","crackdown10","ioniq9recall","rental490","gv80hev","ev9cut","xgrancoupe","kiaboys","pv5ioniq6n","sleepdrive"]

def burn(src, dst, credit, anchor, first=False):
    im = Image.open(os.path.join(PH, src)).convert("RGB")
    tw, th = 1280, 800
    w, h = im.size; s = max(tw / w, th / h)
    im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    W, H = im.size
    left = int((W - tw) * anchor); top = (H - th) // 2
    im = im.crop((left, top, left + tw, top + th)).convert("RGBA")
    f = ImageFont.truetype(FONT, 26)
    bb = ImageDraw.Draw(im).textbbox((0, 0), credit, font=f)
    tw2, th2 = bb[2] - bb[0], bb[3] - bb[1]
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    # 화면(1080x835 cover)에 보이는 원본 가로 영역 = x 123~1157, 하단은 자막 박스 → 우상단에 둔다
    x1 = 1157 - 16; y0 = 118 if first else 18
    x0, y1 = x1 - tw2 - 24, y0 + th2 + 18
    d.rectangle([x0, y0, x1, y1], fill=(0, 0, 0, 150))
    d.text((x0 + 12, y0 + 9 - bb[1]), credit, font=f, fill=(255, 255, 255, 235))
    Image.alpha_composite(im, ov).convert("RGB").save(dst)

for slug in ORDER:
    e = EP[slug]
    wd = os.path.join(ROOT, "work", slug); os.makedirs(os.path.join(wd, "img"), exist_ok=True)
    nimg = max(l.get("img", 0) for l in e["lines"])
    assert nimg == len(e["imgs"]), (slug, nimg, len(e["imgs"]))
    gens, credits = [], set()
    for i, it in enumerate(e["imgs"], 1):
        if isinstance(it, tuple):
            burn(it[1], os.path.join(wd, "img", f"{i:02d}.png"), it[2], it[3], first=(i == 1)); credits.add(it[2])
        else:
            gens.append(f"{i:02d}\t{it}")
    open(os.path.join(wd, "prompts.tsv"), "w").write("\n".join(gens) + ("\n" if gens else ""))
    sj = {"slug": slug, "type": "D형 (뉴스) — 란빵 자동차 이슈", "source": e["src"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["hook"], "channel": "란빵",
          "voice": "taesub", "style": {"sub_box": True, "bar": e["bar"], "watermark": ""},
          "lines": e["lines"]}
    json.dump(sj, open(os.path.join(wd, "script.json"), "w"), ensure_ascii=False, indent=2)
    title = f"{e['kw']} {e['hook']}"; assert len(title) <= 100
    cr = ""
    if credits:
        cr = "※ 사진 출처 (영상 내 표기)\n" + "\n".join(f"· {c.replace('사진: ','')}" for c in sorted(credits)) + "\n"
    note = "별도 표기가 없는 이미지는 AI 연출 자료입니다." if gens else "이미지는 모두 실제 사진입니다."
    up = (f"# {slug} — 업로드 메타\n\n## 제목\n\n{title}\n\n## 설명\n\n{e['desc']}\n\n"
          f"{cr}※ {note} 기준일 2026-09-25.\n※ 근거: script.json 의 source 필드 참조.\n\n{e['tags']}\n\n"
          f"## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop']}\n")
    open(os.path.join(wd, "upload.md"), "w").write(up)
    print(f"{slug:13s} lines={len(e['lines'])} imgs={nimg} real={nimg-len(gens)} gen={len(gens)} title={len(title)}")
