#!/usr/bin/env python3
"""란빵 자동차 F형 10편 (추석 5 + 일반 5) — script.json / prompts.tsv / upload.md 생성 (2026-09-24)."""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
T = ("photorealistic DSLR photograph, 35mm lens, natural available light, shallow depth of field, "
     "Korean setting, no text no letters no signage no logos no brand marks no watermark")
W1 = "a Korean woman in her early 30s, shoulder-length dark brown hair, natural light makeup"
M1 = "a Korean man in his early 30s, short black hair, clean-shaven, slim build"
M2 = "a Korean man in his mid 30s, short wavy black hair, light stubble, sturdy build"
OLD = "an elderly Korean man in his 70s with gray hair"
OUTRO = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}

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

EP = {}

EP["triangle"] = dict(
 t1='"차 안이 제일 안전하지"', t2='고속도로에서 멈춘 차의 결말',
 hook='"차 안이 제일 안전하지" 고속도로에서 멈춘 차의 결말', bar='고속도로에서 차가 멈췄을 때 차 안에 있으면 안 되는 이유',
 src='도로교통법 제66조(고장 등의 조치) — 고속도로 등에서 운행할 수 없게 되면 고장자동차 표지(안전삼각대 등) 설치, 위반 시 2만 원 ; 한국도로공사 2021~2025 고속도로 사망자 784명 중 138명(약 18%)이 2차사고, 치사율 일반사고의 약 6배 (뉴스핌 2026-06-11) (사례는 각색)',
 kw='#고속도로2차사고', tags='#shorts #고속도로2차사고 #안전삼각대 #비트밖스 #추석귀성길', shop='비상삼각대, 차량용 경광봉',
 comment='님들 트렁크에 삼각대 있음? 마지막으로 꺼내본 게 언제임?',
 desc='귀성길 고속도로에서 차가 멈춘 뒤 차 안에서 기다리다 2차사고 위험에 놓인 사례(각색).\n도로교통법 제66조는 고속도로 등에서 고장 등으로 운행할 수 없게 되면 후방에서 확인할 수 있는 위치에 고장자동차 표지(안전삼각대 등)를 설치하고 차를 안전한 곳으로 옮기도록 정하고 있으며, 위반 시 2만 원이 부과됨.\n한국도로공사에 따르면 2021~2025년 고속도로 사망자 784명 중 138명(약 18%)이 2차사고로 숨졌고, 2차사고 치사율은 일반사고의 약 6배임. 사고 시 행동요령은 비트밖스 — 비상등·트렁크 열기·가드레일 밖 대피·스마트폰 신고.',
 lines=[
  L("추석 귀성길 고속도로에서 차가 갑자기 멈춘 사람이 있었음.",1),
  L("갓길에 겨우 세우고 비상등만 켠 채로 온 가족이 차 안에서 보험사를 기다렸음.",2,"whoosh"),
  L("밖은 위험하잖아. 차 안이 제일 안전하지!",3,"eng",dlg="sub2",emo="happy"),
  L("근데 뒤에서 트럭 한 대가 속도를 못 줄이고 그대로 달려오고 있었음.",4,"siren"),
  L("다행히 옆 차로로 비켜 갔지만 한 뼘 차이였음.",5,"thud",em="한 뼘 차이"),
  L("여기서 제일 위험한 게 바로 이 2차사고임.",6,"tick"),
  L("한국도로공사 집계로 최근 5년 고속도로 사망자 784명 중 138명이 2차사고였고, 치사율은 일반사고의 6배임.",7,"ding",em="6배",yellow=True),
  L("그래서 도로교통법 66조는 고장 나면 뒤차가 보이는 곳에 안전삼각대를 세우게 해놨음.",8,"pop",em="안전삼각대"),
  L("안 세우면 2만 원인데, 진짜 무서운 건 돈이 아니라 뒤차가 못 보고 박는 거임.",9,"cash"),
  L("그럼 삼각대 세우러 차도로 걸어가라는 거임?!",10,"boing",dlg="sub1"),
  L("그래서 순서가 있음. 비상등 켜고, 트렁크 열고, 가드레일 밖으로 먼저 나가서, 폰으로 신고.",11,em="가드레일 밖",yellow=True),
  L("앞글자만 따서 비트밖스라고 부름.",11,"ding",em="비트밖스"),
  L("가족 태우고 내려가는 사람 있으면 이거 보내주셈.",12),
  OUTRO],
 prompts=[
  f"a silver sedan stopped on the shoulder of a busy Korean highway during holiday traffic, hazard lights on, daytime, {T}",
  f"{M1} in the driver seat and {W1} in the passenger seat with a child in the back seat waiting inside a stopped car on a highway shoulder, worried faces, {T}",
  f"{M1} in the driver seat of a car smiling confidently, talking on the phone, seat belt on, {T}",
  f"a large cargo truck approaching fast from behind on a Korean highway seen through a car rear window, motion blur, {T}",
  f"a truck swerving into the next lane passing very close to a stopped car on a highway shoulder, dramatic, {T}",
  f"aftermath of a highway rear-end collision at dusk, damaged car on the shoulder, police lights in the distance, {T}",
  f"aerial view of a long Korean expressway with heavy holiday traffic, {T}",
  f"a red reflective warning triangle placed on asphalt behind a stopped car on a highway, low angle, {T}",
  f"close-up of hands placing a red warning triangle on a highway road surface, {T}",
  f"{W1} looking nervously at fast passing cars from beside a stopped car on a highway shoulder, {T}",
  f"a family standing safely behind a metal guardrail on a highway embankment, car with open trunk and hazard lights in the background, {T}",
  f"{M1} behind a highway guardrail calling on a smartphone, family beside him, relieved, {T}"])

EP["backbelt"] = dict(
 t1='"뒷자리는 안 매도 돼"', t2='귀성길 과태료는 누가 냄?',
 hook='"뒷자리는 안 매도 돼" 귀성길 과태료는 누가 냄?', bar='뒷좌석 안전띠 안 맨 부모님, 과태료는 누구한테?',
 src='도로교통법 제50조 제1항 — 운전자는 좌석안전띠를 매고 모든 좌석의 동승자에게도 매도록 해야 함(2018.9.28 전 좌석 확대) ; 동승자 미착용 시 운전자에게 과태료 3만 원, 13세 미만 동승자는 6만 원 (사례는 각색)',
 kw='#전좌석안전띠', tags='#shorts #전좌석안전띠 #안전벨트 #과태료 #추석귀성길', shop='안전벨트 클립 커버',
 comment='님들 뒷자리에서 안전띠 매는 편임? 부모님은 매심?',
 desc='귀성길에 뒷좌석 부모님이 안전띠를 매지 않아 운전자가 과태료를 받은 사례(각색).\n도로교통법 제50조 제1항은 운전자 본인뿐 아니라 모든 좌석의 동승자에게도 좌석안전띠를 매도록 할 의무를 운전자에게 지우고 있음(2018년 9월 28일부터 모든 도로·전 좌석).\n동승자가 매지 않으면 운전자에게 과태료 3만 원, 동승자가 13세 미만이면 6만 원이 부과됨.',
 lines=[
  L("추석에 부모님 모시고 고향 내려가던 사람이 있었음.",1),
  L("아버지가 뒷자리에 타시자마자 안전띠를 풀어버리셨음.",2,"whoosh"),
  L("뒷자리는 안 매도 돼. 답답해서 못 있겠다!",3,"eng",dlg="sub2",emo="happy"),
  L("그렇게 한 시간을 달리다 톨게이트 앞 단속에 걸렸음.",4,"siren"),
  L("근데 과태료가 아버지가 아니라 운전한 아들한테 나왔음.",5,"thud",em="운전한 아들"),
  L("도로교통법 50조는 운전자가 모든 좌석 동승자한테 안전띠를 매게 할 의무를 지워놨음.",6,"ding",em="모든 좌석"),
  L("2018년부터 뒷좌석까지 전부 의무가 됐고,",7,"tick"),
  L("동승자가 안 매면 운전자한테 과태료 3만 원, 13세 미만 아이면 6만 원임.",8,"cash",em="6만 원",yellow=True),
  L("아니 본인이 안 매겠다는데 내가 왜 내?!",9,"boing",dlg="sub2"),
  L("출발 전에 확인하고 매게 하는 게 운전자 몫이라 그럼.",10),
  L("사실 돈보다 무서운 건 사고 때 뒷좌석 사람이 앞으로 튕겨 나오는 거임.",11,"thud",em="튕겨 나오는"),
  L("출발 전에 뒤돌아서 딸깍 소리 들었는지부터 확인하셈.",12,"ding"),
  L("명절에 운전대 잡는 사람 있으면 이거 보내주셈.",12),
  OUTRO],
 prompts=[
  f"{M1} driving a car on a Korean highway with his elderly parents in the back seat, autumn holiday, {T}",
  f"{OLD} in the back seat of a car unbuckling his seat belt with a grumpy face, {T}",
  f"{OLD} waving his hand dismissively in the back seat of a car, {T}",
  f"a Korean police officer at a highway tollgate checking cars, holiday traffic, {T}",
  f"{M1} in the driver seat holding a traffic fine notice with a shocked face, {T}",
  f"close-up of a seat belt buckle in a car back seat, {T}",
  f"interior of a car with all passengers wearing seat belts, front and back seats, bright daylight, {T}",
  f"a young child in a car back seat wearing a seat belt, calm, {T}",
  f"{M1} arguing in a car, frustrated, glancing at the rear-view mirror, {T}",
  f"{M1} turning around from the driver seat checking his parents seat belts before driving, {T}",
  f"crash test dummy in a rear seat during a crash test, lab lighting, {T}",
  f"close-up of a hand clicking a seat belt buckle in a car rear seat, {T}"])

EP["daeri5m"] = dict(
 t1='대리기사가 도로 한복판에', t2='두고 간 차, 5m 옮긴 결말',
 hook='대리기사가 도로 한복판에 두고 간 차, 5m 옮긴 차주의 결말', bar='대리기사가 도로에 차 버리고 감. 술 마신 차주가 5m 옮기면?',
 src='창원지법 형사7단독(2019) 대리기사가 도로에 세우고 간 차를 인근 주차장까지 약 5m 운전한 음주 차주 무죄(긴급피난) — 서울신문 2019-06-11 ; 대리기사와 다툼 뒤 1차로의 차를 3m 이동 무죄(법률신문) ; 도로 한가운데 방치 차 300m 운전 무죄(한국일보 2016·2018) ; 형법 제22조 긴급피난 (사례는 각색, 판결은 개별 사정에 따름)',
 kw='#음주운전', tags='#shorts #음주운전 #대리운전 #긴급피난 #추석', shop='없음',
 comment='님들이 차주였으면 어떻게 했을 것 같음? 그냥 두고 경찰 부름 vs 옮김',
 desc='명절 술자리 뒤 대리기사가 차를 도로에 세우고 떠나, 술 마신 차주가 차를 몇 미터 옮긴 사례(각색).\n창원지법은 대리기사가 도로에 세워두고 간 차를 인근 주차장까지 약 5m 운전한 음주 차주에게 형법상 긴급피난을 인정해 무죄를 선고했고, 1차로에 선 차를 3m 옮긴 사례, 도로 한가운데 방치된 차를 300m 운전한 사례에서도 무죄 판결이 나온 적이 있음.\n다만 긴급피난은 사고 위험을 피할 다른 방법이 없고 이동이 필요한 최소한일 때에만 인정되며, 개별 사정에 따라 판단이 달라짐. 집까지 몰고 가면 음주운전임.',
 lines=[
  L("추석 친척 모임에서 술 마시고 대리를 부른 사람이 있었음.",1),
  L("가는 길에 대리기사랑 말다툼이 붙었는데,",2,"eng"),
  L("그럼 알아서 가세요. 저 여기서 내립니다!",3,"dudung",dlg="sub2"),
  L("기사가 차를 도로 한복판에 세워두고 그냥 가버렸음.",4,"whoosh",em="도로 한복판"),
  L("뒤에서는 차들이 빵빵거리고, 차주는 술 마신 상태였음.",5,"siren"),
  L("결국 차주가 운전대를 잡고 옆 주차장까지 딱 5m를 옮겼음.",6,"tick",em="5m",yellow=True),
  L("근데 그걸 본 대리기사가 음주운전으로 신고했음.",7,"thud"),
  L("당연히 음주운전 유죄 아님?!",8,"boing",dlg="sub1"),
  L("근데 법원 판단은 무죄였음.",9,"ding",em="무죄",yellow=True),
  L("도로 한복판에 차를 두면 사고가 날 수 있으니, 그걸 피하려고 최소한만 옮긴 건 형법상 긴급피난이라고 본 거임.",10,em="긴급피난"),
  L("비슷하게 3m, 300m 옮긴 사건들도 무죄가 나왔음.",11),
  L("대신 조건이 있음. 다른 방법이 없어야 하고, 딱 위험을 피할 만큼만 옮겨야 함.",12,"pop",em="딱 위험을 피할 만큼"),
  L("그 김에 집까지 몰고 가면 그냥 음주운전임.",13,"cash"),
  L("님들이 차주였으면 그냥 두고 경찰 부름, 아니면 옮김?",13),
  OUTRO],
 prompts=[
  f"a Korean family holiday dinner table with food and soju glasses, relatives gathered, warm evening light, {T}",
  f"{M1} in the passenger seat arguing with a designated driver at night inside a car, tense, {T}",
  f"{M2} as a designated driver getting out of a car at night on a city road, angry, walking away, {T}",
  f"a car stopped in the middle of a city road lane at night with hazard lights on, other cars honking behind, {T}",
  f"headlights of cars queued behind a stopped car on a Korean road at night, glare, {T}",
  f"{M1} in the driver seat at night, flushed face, carefully moving a car a few meters into a parking lot, {T}",
  f"{M2} holding a smartphone to his ear on a street at night, pointing at a car, {T}",
  f"a Korean police officer with a breathalyzer next to a car at night, {T}",
  f"a Korean courtroom with a judge bench, empty, solemn, {T}",
  f"close-up of a car parked neatly in a parking space at night just off the road, {T}",
  f"a gavel on a wooden desk with legal books, {T}",
  f"a car driving away on a dark road at night with blurred tail lights, {T}",
  f"{M1} standing next to his car at night calling for help on the phone, {T}"])

EP["lane1"] = dict(
 t1='"규정속도 지켰는데요?"', t2='고속도로 1차로의 함정',
 hook='"규정속도 지켰는데요?" 고속도로 1차로 달리다 딱지 뗀 이유', bar='고속도로 1차로에서 규정속도로 달렸는데 딱지',
 src='도로교통법 제14조·시행규칙 별표9(차로에 따른 통행차의 기준) — 편도 2차로 이상 고속도로 1차로는 앞지르기 차로, 도로상황으로 80km/h 미만 통행 불가피한 경우 예외 ; 지정차로 위반 승용 범칙금 4만 원·벌점 10점 ; 연간 단속 약 5만4천 건 (매일신문 2026-09-22, 뉴시스 2023-06-22) (사례는 각색)',
 kw='#지정차로위반', tags='#shorts #지정차로위반 #고속도로1차로 #추월차로 #추석귀성길', shop='없음',
 comment='님들 고속도로 1차로에서 계속 달리는 차 보면 어떰?',
 desc='고속도로 1차로에서 규정속도로 계속 달리다 지정차로 위반으로 단속된 사례(각색).\n편도 2차로 이상 고속도로의 1차로는 앞지르기를 할 때 쓰는 차로로, 정체 등 도로상황으로 시속 80km 미만으로 달릴 수밖에 없는 경우가 아니면 계속 주행할 수 없음.\n위반 시 승용차 기준 범칙금 4만 원·벌점 10점. 경찰청 집계로 고속도로 지정차로 위반은 한 해 5만 건이 넘음.',
 lines=[
  L("규정속도 딱 지키면서 고속도로 1차로로만 달리던 사람이 있었음.",1),
  L("뒤차가 계속 상향등을 켜도 신경 안 썼음.",2,"whoosh"),
  L("나 100 딱 맞춰 가는데 뭐가 문제임? 급하면 옆으로 가!",3,"eng",dlg="sub2",emo="happy"),
  L("근데 10km쯤 가다가 암행 순찰차에 세워졌음.",4,"siren"),
  L("과속도 아닌데 왜 잡는 거냐고 따졌더니,",5,"tick"),
  L("딱지에 적힌 건 지정차로 위반이었음.",6,"thud",em="지정차로 위반"),
  L("고속도로 1차로는 추월할 때만 잠깐 쓰는 차로임.",7,"ding",em="추월할 때만",yellow=True),
  L("추월했으면 다시 2차로로 돌아와야 하고, 계속 달려도 되는 건 막혀서 80km 밑으로 갈 때뿐임.",8,em="80km"),
  L("걸리면 승용차 기준 범칙금 4만 원에 벌점 10점이고,",9,"cash",em="벌점 10점"),
  L("한 해에 이걸로 걸리는 게 5만 건이 넘음.",10,"pop",em="5만 건"),
  L("그럼 추월차로가 비어 있으면 그냥 달려도 되는 거 아님?!",11,"boing",dlg="sub1"),
  L("비어 있어도 추월 끝나면 비켜줘야 함. 명절 고속도로는 암행차가 특히 많음.",12),
  L("내려갈 때 1차로 붙박이 하는 사람 있으면 이거 보내주셈.",12),
  OUTRO],
 prompts=[
  f"a sedan cruising in the leftmost lane of a wide Korean expressway, daytime, {T}",
  f"view from a car rear window of a following car flashing its high beams closely behind, {T}",
  f"{M2} driving calmly with one hand on the wheel, smug face, expressway outside, {T}",
  f"an unmarked Korean police patrol car with flashing lights pulling over a sedan on the expressway shoulder, {T}",
  f"{M2} arguing with a Korean traffic police officer beside a car on the highway shoulder, {T}",
  f"close-up of a traffic ticket booklet held by a police officer, blurred, {T}",
  f"aerial view of a Korean expressway with a car overtaking in the left lane and returning, {T}",
  f"heavy traffic jam on a Korean expressway in all lanes, holiday, {T}",
  f"{M2} holding a traffic ticket looking frustrated in the driver seat, {T}",
  f"aerial view of many cars on a Korean highway at dusk, {T}",
  f"{W1} in a passenger seat raising her eyebrows questioning, {T}",
  f"an expressway with an empty left lane and cars in right lanes at golden hour, {T}"])

EP["onlyme"] = dict(
 t1='"잠깐인데 뭐 어때"', t2='명절에 조카한테 차 키 준 결말',
 hook='"잠깐인데 뭐 어때" 명절에 조카한테 차 키 준 결말', bar='명절에 조카가 내 차 몰다 사고, 보험이 안 된다고?',
 src='자동차보험 운전자 범위 한정특약 — 한정 범위 밖 운전자 사고 시 대인배상Ⅰ(책임보험)만 보상, 대인배상Ⅱ·대물배상·자기차량손해는 보상 제외 ; 단기(임시)운전자 확대 특약은 하루 단위 가입 가능 (찾기쉬운 생활법령정보·보험사 약관) (사례는 각색)',
 kw='#운전자한정특약', tags='#shorts #자동차보험 #운전자한정특약 #임시운전자특약 #추석', shop='없음',
 comment='님들 명절에 가족끼리 차 바꿔 탈 때 보험 확인함?',
 desc='명절에 운전자 한정특약 범위 밖인 조카에게 차를 맡겼다가 사고가 난 사례(각색).\n자동차보험을 부부·가족 한정 등으로 가입한 경우 범위 밖 사람이 운전하다 사고를 내면 대인배상Ⅰ(책임보험)만 보상되고, 대인배상Ⅱ·대물배상·자기차량손해는 보상되지 않음.\n다른 사람이 잠시 운전해야 하면 보험사 앱에서 하루 단위로 임시(단기)운전자 특약을 가입할 수 있음. 보상 범위·조건은 보험사 약관에 따라 다름.',
 lines=[
  L("추석에 시골집 가서 조카한테 차 키를 넘긴 사람이 있었음.",1),
  L("조카가 면허 딴 지 1년 됐다길래 읍내 마트만 다녀오라고 했음.",2,"whoosh"),
  L("삼촌, 잠깐인데 뭐 어때요. 금방 갔다 올게요!",3,"eng",dlg="sub2",emo="happy"),
  L("근데 마트 주차장에서 옆 차를 긁고 사람까지 살짝 다쳤음.",4,"thud"),
  L("보험사에 전화했더니 이 한마디가 돌아왔음.",5,"tick"),
  L("고객님 보험은 부부 한정이라 이번 건은 보상이 어렵습니다.",6,"dudung",dlg="sub1"),
  L("운전자 한정특약 밖의 사람이 사고 내면 대인배상1, 그러니까 책임보험만 나옴.",7,"ding",em="책임보험만",yellow=True),
  L("대인2, 대물, 내 차 수리비는 전부 내 돈으로 물어야 함.",8,"cash",em="전부 내 돈"),
  L("아니 종합보험 들었는데 그게 말이 됨?!",9,"boing",dlg="sub2"),
  L("한정특약으로 보험료를 싸게 낸 대신 운전할 사람을 줄여놓은 거라 그럼.",10),
  L("그래서 방법이 있음. 보험사 앱에서 하루짜리 임시운전자 특약을 넣으면 됨.",11,"pop",em="하루짜리",yellow=True),
  L("몇천 원이면 그날은 내 보험 그대로 쓸 수 있음.",12,"ding"),
  L("명절에 차 빌려주는 사람 있으면 이거 보내주셈.",12),
  OUTRO],
 prompts=[
  f"a Korean countryside house yard during Chuseok with family cars parked, autumn, {T}",
  f"{M2} handing car keys to a young Korean man in his early 20s in a countryside yard, {T}",
  f"a young Korean man in his early 20s grinning confidently holding car keys, {T}",
  f"a small scrape between two cars in a supermarket parking lot, close-up of scratched door, {T}",
  f"{M2} on the phone in a parking lot with a worried face, {T}",
  f"{W1} as a call center insurance agent with a headset at a desk, apologetic face, {T}",
  f"close-up of an insurance policy document on a table with a pen, {T}",
  f"a car body repair shop with a damaged car on a lift, {T}",
  f"{M2} throwing his hands up in disbelief in a parking lot, {T}",
  f"a calculator and insurance papers on a kitchen table, {T}",
  f"close-up of a hand holding a smartphone with a blank insurance app screen, {T}",
  f"{M2} relieved and smiling handing car keys to a young man, autumn yard, {T}"])

EP["rightturn"] = dict(
 t1='"빨간불에도 우회전은 되잖아"', t2='6만 원 딱지 뗀 이유',
 hook='"빨간불에도 우회전은 되잖아" 6만 원 딱지 뗀 이유', bar='우회전 신호등 빨간불에 돌았다가 범칙금 6만 원',
 src='도로교통법 시행규칙 개정(2023.1.22 시행) — 우회전 신호등 설치 교차로는 녹색 화살표에서만 우회전, 미설치 교차로에서 차량 신호 적색이면 일시정지 후 우회전 ; 위반 시 승용 범칙금 6만 원·벌점 15점 (서울신문 2023-01-17) (사례는 각색)',
 kw='#우회전신호등', tags='#shorts #우회전신호등 #우회전일시정지 #범칙금 #도로교통법', shop='블랙박스',
 comment='님들 동네에 우회전 신호등 생겼음? 다들 기다림?',
 desc='우회전 신호등이 적색인데 우회전했다가 단속된 사례(각색).\n2023년 1월 22일부터 우회전 신호등이 설치된 교차로에서는 녹색 화살표 신호일 때만 우회전할 수 있고, 신호등이 없는 교차로에서는 차량 신호가 적색이면 정지선에서 일시정지한 뒤 우회전해야 함.\n위반 시 승용차 기준 범칙금 6만 원·벌점 15점. 녹색 신호라도 횡단보도에 보행자가 있으면 멈춰야 함.',
 lines=[
  L("빨간불에도 우회전은 된다며 그냥 돌아버린 사람이 있었음.",1),
  L("교차로에 서 있었는데 뒤차가 빵 하고 눌렀음.",2,"whoosh"),
  L("우회전은 원래 아무 때나 되는 거잖아. 가자!",3,"eng",dlg="sub2",emo="happy"),
  L("근데 모퉁이 돌자마자 경찰이 손짓으로 세웠음.",4,"siren"),
  L("그 교차로엔 우회전 전용 신호등이 따로 있었음.",5,"thud",em="우회전 전용 신호등"),
  L("2023년부터 우회전 신호등이 있는 곳은 녹색 화살표일 때만 돌 수 있음.",6,"ding",em="녹색 화살표",yellow=True),
  L("빨간불이면 녹색 뜰 때까지 기다려야 하고,",7,"tick"),
  L("걸리면 승용차 기준 범칙금 6만 원에 벌점 15점임.",8,"cash",em="6만 원"),
  L("그럼 신호등 없는 데는 그냥 돌아도 되는 거임?!",9,"boing",dlg="sub1"),
  L("없는 곳도 차량 신호가 빨간불이면 정지선에서 일단 멈췄다가 돌아야 함.",10,em="일단 멈췄다가"),
  L("녹색이어도 횡단보도에 사람 있으면 서야 하고.",11),
  L("뒤차가 빵빵거려도 우회전 신호등부터 보셈.",12,"ding"),
  OUTRO],
 prompts=[
  f"a sedan waiting at a Korean city intersection about to turn right, red traffic light, daytime, {T}",
  f"view from a car interior of a car behind honking, rear-view mirror, city street, {T}",
  f"{M2} in the driver seat turning the wheel confidently with a careless smile, {T}",
  f"a Korean traffic police officer signaling a car to pull over at a street corner, {T}",
  f"a traffic signal pole at a Korean intersection with a separate right-turn arrow signal glowing red, {T}",
  f"a green right-turn arrow traffic light at a Korean intersection, {T}",
  f"cars waiting at a stop line at a Korean intersection with red lights, {T}",
  f"{M2} holding a traffic ticket looking annoyed beside his car, {T}",
  f"{W1} in a passenger seat looking puzzled, {T}",
  f"a car stopped exactly at a white stop line before a crosswalk at a Korean intersection, {T}",
  f"pedestrians crossing a zebra crosswalk in front of a stopped car turning right, {T}",
  f"a Korean city intersection at dusk with cars and traffic lights, {T}"])

EP["blinker"] = dict(
 t1='"깜빡이 켜면 안 끼워주잖아"', t2='칼치기한 차에 날아온 고지서',
 hook='"깜빡이 켜면 안 끼워주잖아" 칼치기한 차에 날아온 고지서', bar='깜빡이 없이 끼어든 차, 블박 신고 한 번에 고지서',
 src='도로교통법 제38조 제1항(차의 신호) — 진로 변경 시 방향지시기로 신호, 일반도로 30m·고속도로 100m 전부터 ; 신호 불이행 승용 범칙금 3만 원 ; 영상 공익신고(안전신문고)로 부과 시 과태료 4만 원 (경미·방해 없음은 경고 가능) (사례는 각색)',
 kw='#방향지시등', tags='#shorts #방향지시등 #깜빡이 #칼치기 #안전신문고', shop='블랙박스',
 comment='님들 깜빡이 켜면 끼워주는 편임, 안 끼워주는 편임?',
 desc='방향지시등 없이 차로를 바꾸다 블랙박스 영상 공익신고로 고지서를 받은 사례(각색).\n도로교통법 제38조 제1항은 진로를 바꾸려는 경우 그 행위가 끝날 때까지 방향지시기 등으로 신호하도록 정하고 있으며, 일반도로는 30m, 고속도로는 100m 전부터 켜야 함.\n위반 시 승용차 기준 범칙금 3만 원이고, 안전신문고 영상 신고로 부과되면 과태료 4만 원이 나올 수 있음. 경미하거나 교통에 방해가 없으면 경고로 끝나기도 함.',
 lines=[
  L("깜빡이 켜면 안 끼워준다며 늘 그냥 끼어들던 사람이 있었음.",1),
  L("그날도 옆 차로 틈으로 깜빡이 없이 쑥 들어갔음.",2,"whoosh",em="깜빡이 없이"),
  L("켜봤자 안 끼워주잖아. 그냥 들어가는 게 빨라!",3,"eng",dlg="sub2",emo="happy"),
  L("뒤차가 급브레이크를 밟았고, 그 장면이 블랙박스에 그대로 찍혔음.",4,"thud"),
  L("2주 뒤 집으로 고지서가 날아왔음.",5,"tick",em="고지서"),
  L("뒤차 운전자가 영상을 안전신문고에 올린 거임.",6,"ding"),
  L("도로교통법 38조는 차로를 바꿀 때 방향지시등을 켜게 해놨고,",7,"pop",em="방향지시등"),
  L("일반도로는 30m, 고속도로는 100m 전부터 켜야 함.",8,em="100m",yellow=True),
  L("경찰이 잡으면 범칙금 3만 원, 영상 신고로 날아오면 과태료 4만 원임.",9,"cash",em="4만 원"),
  L("그깟 깜빡이 하나로 신고까지 한다고?!",10,"boing",dlg="sub2"),
  L("깜빡이 없이 들어오면 뒤차는 피할 시간이 없어서, 신고가 제일 많이 들어오는 항목 중 하나임.",11),
  L("끼어들 땐 켜고 들어가셈. 뒤에 블박 달린 차 엄청 많음.",12,"ding"),
  OUTRO],
 prompts=[
  f"dense city traffic on a Korean multi-lane road, cars close together, daytime, {T}",
  f"a car abruptly cutting into a narrow gap in the next lane without signaling, seen from behind, {T}",
  f"{M2} in the driver seat smirking while changing lanes, {T}",
  f"dashboard camera point of view of a car cutting in dangerously close ahead, brake lights, {T}",
  f"a white envelope with an official notice in a Korean apartment mailbox, {T}",
  f"{W1} in a driver seat uploading a video on her smartphone, parked car, {T}",
  f"close-up of a car turn signal lever being pushed by a hand, {T}",
  f"a car with its amber turn signal blinking changing lanes on an expressway, {T}",
  f"{M2} at home opening an official envelope with a shocked face, {T}",
  f"{M2} throwing a paper notice on a table in frustration, {T}",
  f"a near collision between two cars on a Korean road, tire smoke, {T}",
  f"a windshield-mounted dashcam in a car interior, road ahead, {T}"])

EP["fineorpoint"] = dict(
 t1='과속 고지서 받으면', t2='과태료 vs 범칙금 뭐 냄?',
 hook='과속 고지서 받으면 과태료 vs 범칙금, 뭐 내는 게 이득임?', bar='과속 고지서, 과태료로 낼까 범칙금으로 낼까',
 src='도로교통법 제160조 제3항(무인단속 과태료, 차 소유자 부과) ; 속도위반 승용 20km/h 이하 과태료 4만 원(사전납부 3.2만)·범칙금 3만 원·벌점 없음, 20~40km/h 과태료 7만 원·범칙금 6만 원+벌점 15점 ; 과태료 의견진술 기간 중 운전자 확인 시 범칙금 전환 (이파인·찾기쉬운 생활법령정보) (사례는 각색)',
 kw='#과속과태료', tags='#shorts #과속과태료 #범칙금 #벌점 #과속카메라', shop='블랙박스',
 comment='님들은 과태료파임 범칙금파임?',
 desc='과속 무인단속 고지서를 받고 과태료와 범칙금 중 무엇을 낼지 고민한 사례(각색).\n무인카메라에 찍히면 차 소유자에게 과태료가 나오고, 운전자를 밝히면 운전자에게 범칙금과 벌점이 부과됨.\n승용차 기준 제한속도 20km/h 이하 초과는 과태료 4만 원(사전납부 시 20% 감경)·범칙금 3만 원으로 벌점이 없고, 20km/h 초과~40km/h 이하는 과태료 7만 원·범칙금 6만 원에 벌점 15점임. 금액은 위반 속도·차종에 따라 다름.',
 lines=[
  L("과속 고지서를 받고 과태료로 낼지 범칙금으로 낼지 고민하던 사람이 있었음.",1),
  L("카메라에 찍힌 건 제한속도보다 25km 빨랐던 거였음.",2,"whoosh",em="25km"),
  L("범칙금이 만 원 싸다며? 그럼 범칙금으로 바꿔야지!",3,"eng",dlg="sub2",emo="happy"),
  L("근데 여기서 함정이 하나 있음.",4,"tick"),
  L("무인카메라에 찍히면 차 주인한테 과태료가 나오고, 운전자를 밝히면 범칙금으로 바뀜.",5,"ding",em="운전자를 밝히면"),
  L("20km 넘게 초과했으면 과태료는 7만 원, 범칙금은 6만 원임.",6,"cash",em="7만 원",yellow=True),
  L("근데 범칙금으로 가면 벌점 15점이 같이 붙음.",7,"thud",em="벌점 15점"),
  L("과태료는 만 원 비싼 대신 벌점이 없는 거임.",8,"pop",em="벌점이 없는"),
  L("벌점 40점 넘으면 면허 정지인데?!",9,"boing",dlg="sub1"),
  L("그래서 벌점이 쌓여 있으면 만 원 더 내고 과태료가 이득임.",10,em="과태료가 이득",yellow=True),
  L("대신 20km 이하 초과는 원래 벌점이 없어서 범칙금 3만 원이 더 쌈.",11),
  L("고지서 받으면 초과 속도랑 내 벌점부터 확인하셈.",12,"ding"),
  OUTRO],
 prompts=[
  f"{M2} at a kitchen table holding a traffic violation notice with a thinking face, {T}",
  f"a speed enforcement camera pole beside a Korean highway, {T}",
  f"{M2} pointing at a paper notice and grinning, home, {T}",
  f"close-up of a paper notice and a pen on a wooden table, dim light, {T}",
  f"a car passing under an overhead speed camera on a Korean road, motion blur, {T}",
  f"Korean banknotes on a table next to car keys, {T}",
  f"close-up of a Korean driver license card on a table, blurred details, {T}",
  f"two stacks of Korean banknotes side by side on a desk, comparison, {T}",
  f"{W1} raising an eyebrow looking at a notice, living room, {T}",
  f"{M2} nodding and smiling while paying on a laptop at home, {T}",
  f"a speedometer needle in a car dashboard at night, {T}",
  f"a car driving calmly on a Korean highway at golden hour, {T}"])

EP["drunkhelp"] = dict(
 t1='"가까운데 괜찮아"', t2='술 먹은 친구한테 키 준 사람',
 hook='"가까운데 괜찮아" 술 먹은 친구한테 차 키 준 사람의 결말', bar='술 먹은 친구한테 차 키 건넨 사람도 처벌?',
 src='형법 제32조(종범) — 음주운전을 알면서 차 키 제공·운전 권유·독려 시 음주운전 방조, 정범보다 감경 ; 동승자 벌금 500만 원, 운전 독촉한 배우자 벌금 100만 원 선고 사례 (법무법인 이현·대륜 법률정보) (사례는 각색)',
 kw='#음주운전방조', tags='#shorts #음주운전방조 #음주운전 #동승자처벌 #도로교통법', shop='없음',
 comment='님들 술 먹은 친구가 운전한다고 하면 어떻게 말림?',
 desc='술 마신 친구에게 차 키를 건넸다가 음주운전 방조로 처벌된 사례(각색).\n운전자가 술에 취한 사실을 알면서 차 키를 건네거나 운전을 권유·독려하면 형법 제32조의 방조범(종범)으로 처벌될 수 있고, 형은 운전자(정범)보다 감경됨.\n실제로 동승자에게 벌금 500만 원, 남편에게 운전을 독촉한 아내에게 벌금 100만 원이 선고된 사례가 있음. 처벌 여부·수위는 구체적 사정에 따라 다름.',
 lines=[
  L("가까운데 괜찮다며 술 먹은 친구한테 차 키를 건넨 사람이 있었음.",1),
  L("회식 끝나고 대리가 30분 넘게 안 잡혔음.",2,"whoosh"),
  L("야 5분 거리잖아. 너 운전 잘하잖아, 그냥 가!",3,"eng",dlg="sub2",emo="happy"),
  L("친구는 그 키를 받아서 운전석에 앉았고, 조수석엔 키 준 사람이 탔음.",4,"tick"),
  L("그리고 2km도 못 가서 음주단속에 걸렸음.",5,"siren",em="음주단속"),
  L("근데 입건된 건 운전한 친구만이 아니었음.",6,"thud",em="운전한 친구만이 아니었음"),
  L("술 취한 걸 알면서 키를 건네고 운전하라고 부추긴 건 음주운전 방조임.",7,"ding",em="음주운전 방조",yellow=True),
  L("형법 32조 방조범이라 운전자보다는 가볍지만 처벌은 받음.",8,"pop"),
  L("실제로 동승자한테 벌금 500만 원이 나온 판결도 있음.",9,"cash",em="500만 원",yellow=True),
  L("아니 운전은 걔가 했는데 내가 왜?!",10,"boing",dlg="sub2"),
  L("키를 주고, 가라고 등 떠밀고, 옆자리에 같이 탄 게 다 도운 걸로 보는 거임.",11),
  L("친구 아끼면 키를 뺏으셈. 대리비가 벌금보다 훨씬 쌈.",12,"ding"),
  OUTRO],
 prompts=[
  f"{M1} and {M2} leaving a Korean restaurant at night after a company dinner, slightly drunk, {T}",
  f"{M1} looking at a smartphone on a street at night waiting impatiently, {T}",
  f"{M2} handing car keys to a friend on a street at night, laughing, {T}",
  f"{M1} in the driver seat and {M2} in the passenger seat of a car at night, city lights, {T}",
  f"a Korean police drunk driving checkpoint at night with traffic cones and glowing batons, {T}",
  f"a Korean police officer questioning a passenger through a car window at night, {T}",
  f"close-up of car keys being passed from one hand to another, night, {T}",
  f"a Korean police station interior at night with a desk and paperwork, {T}",
  f"a gavel on a wooden desk with legal books, {T}",
  f"{M2} in a police station throwing his hands up in disbelief, {T}",
  f"{M2} sitting alone on a bench at night regretting, head down, {T}",
  f"{M1} taking car keys away from a friend and calling a designated driver on the phone, night street, {T}"])

EP["plateseize"] = dict(
 t1='아침에 나왔더니', t2='내 차 번호판이 없어졌다',
 hook='아침에 나왔더니 내 차 번호판이 없어졌다', bar='출근하려는데 번호판이 사라진 이유',
 src='지방세징수법 — 자동차세 체납 차량 등록번호판 영치(통상 2회 이상 체납 시, 1회는 영치 예고) ; 질서위반행위규제법 제55조 — 자동차 관련 과태료 합계 30만 원 이상·60일 이상 체납 시 영치 ; 5회 이상·100만 원 이상 고액 체납 차량은 견인·공매 가능 ; 번호판 없이 운행은 자동차관리법 위반 (서울신문 2025-04-03, 찾기쉬운 생활법령정보) (사례는 각색)',
 kw='#번호판영치', tags='#shorts #번호판영치 #자동차세 #과태료체납 #자동차관리법', shop='없음',
 comment='님들 자동차세 연납 하는 편임? 고지서 제때 챙김?',
 desc='자동차세와 과태료를 밀려 번호판이 영치된 사례(각색).\n자동차세는 보통 6월·12월 두 번 고지되며, 체납이 쌓이면(통상 2회 이상) 지자체가 등록번호판을 떼어 보관(영치)함. 자동차 관련 과태료도 합계 30만 원 이상을 60일 넘게 안 내면 영치 대상임.\n번호판 없이 차를 운행하면 자동차관리법 위반이고, 5회 이상 상습·100만 원 이상 고액 체납 차량은 견인 후 공매될 수 있음. 체납액을 내면 번호판을 돌려받음.',
 lines=[
  L("출근하려고 주차장에 내려왔더니 내 차 번호판이 없어진 사람이 있었음.",1),
  L("앞뒤 번호판 자리에 스티커 한 장만 붙어 있었음.",2,"whoosh",em="스티커 한 장"),
  L("누가 번호판을 훔쳐 간 거야? 경찰 불러야겠네!",3,"eng",dlg="sub2"),
  L("근데 가져간 건 도둑이 아니라 구청이었음.",4,"thud",em="구청"),
  L("자동차세를 두 번 넘게 안 내고 미뤄뒀던 거임.",5,"tick"),
  L("자동차세가 쌓이면 지자체가 번호판을 떼서 보관하는데 이걸 영치라고 함.",6,"ding",em="영치",yellow=True),
  L("주차 과태료도 합계 30만 원 넘게 60일 이상 밀리면 똑같이 떼감.",7,"pop",em="30만 원"),
  L("그럼 번호판 없이 그냥 타고 다니면 되는 거 아님?!",8,"boing",dlg="sub1"),
  L("번호판 없이 달리면 그 자체로 자동차관리법 위반이라 더 커짐.",9,"siren"),
  L("5번 넘게 밀리거나 100만 원 넘게 쌓이면 차를 견인해서 공매로 팔아버리기도 함.",10,"cash",em="공매",yellow=True),
  L("결국 그날 출근은 버스로 하고, 체납액 다 내고서야 번호판을 돌려받았음.",11),
  L("고지서 밀린 거 있으면 오늘 확인하셈.",12,"ding"),
  OUTRO],
 prompts=[
  f"{M1} in office clothes walking into an underground apartment parking garage in the morning, {T}",
  f"rear of a parked sedan with its license plate removed, empty plate holder, underground parking garage, {T}",
  f"{M1} shocked pointing at his car in a parking garage, {T}",
  f"a Korean district office civil servant in a vest removing a license plate from a car with a screwdriver, {T}",
  f"a pile of unopened official envelopes on a table at home, {T}",
  f"a storage room with stacks of seized car license plates on shelves, no readable numbers, {T}",
  f"a parking violation notice tucked under a car windshield wiper, {T}",
  f"{W1} raising an eyebrow questioning, {T}",
  f"a car being stopped by Korean police on a road, {T}",
  f"a tow truck towing a sedan out of a parking lot, {T}",
  f"{M1} in office clothes standing on a crowded city bus in the morning, tired face, {T}",
  f"close-up of a smartphone showing a payment confirmation screen, blurred, on a desk, {T}"])

ORDER = ["triangle","backbelt","daeri5m","lane1","onlyme","rightturn","blinker","fineorpoint","drunkhelp","plateseize"]

for slug in ORDER:
    e = EP[slug]
    wd = os.path.join(ROOT, "work", slug); os.makedirs(wd, exist_ok=True)
    nimg = max(l.get("img", 0) for l in e["lines"])
    assert nimg == len(e["prompts"]), (slug, nimg, len(e["prompts"]))
    sj = {"slug": slug, "type": "F형 (법조항 사이다) — 각색, 란빵 자동차", "source": e["src"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["hook"], "channel": "란빵",
          "voice": "taesub", "style": {"sub_box": True, "bar": e["bar"], "watermark": ""},
          "lines": e["lines"]}
    json.dump(sj, open(os.path.join(wd, "script.json"), "w"), ensure_ascii=False, indent=2)
    with open(os.path.join(wd, "prompts.tsv"), "w") as f:
        for i, p in enumerate(e["prompts"], 1): f.write(f"{i:02d}\t{p}\n")
    title = f"{e['kw']} {e['hook']}"
    assert len(title) <= 100, (slug, len(title))
    up = (f"# {slug} — 업로드 메타\n\n## 제목\n\n{title}\n\n## 설명\n\n{e['desc']}\n\n"
          f"※ 사례는 각색이며, 이미지는 AI 연출 자료입니다. 기준일 2026-09-24.\n"
          f"※ 근거: script.json 의 source 필드 참조.\n\n{e['tags']}\n\n"
          f"## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop']}\n")
    open(os.path.join(wd, "upload.md"), "w").write(up)
    print(slug, len(e["lines"]), "lines", nimg, "imgs", len(title), "title chars")
