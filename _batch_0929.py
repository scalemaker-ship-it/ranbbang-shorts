#!/usr/bin/env python3
"""란빵 2026-09-29 배치 10편 대본·프롬프트 생성기 (보배드림 원글).
birdpoop·cashdeal·gitaxi·trashthrow·tesladoor·factoryticket·stealthcar·drainlid·fingerwrong·zebrapark
→ work/<slug>/script.json + prompts.tsv + upload.md
"""
import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "work"))

T = (", photorealistic DSLR photograph, 35mm lens, natural available light, shallow depth of field, "
     "Korean setting, no text no letters no signage no logos no brand marks no watermark, no readable license plates")
M1 = "a Korean man in his early 30s, short black hair, clean-shaven, slim build"
M2 = "a Korean man in his mid 30s, short wavy black hair, light stubble, sturdy build"
W1 = "a Korean woman in her early 30s, shoulder-length dark brown hair, natural light makeup"
M4 = "a Korean man in his late 40s, short graying hair, casual jacket"
M5 = "a Korean man in his late 50s, taxi driver, short gray hair, light blue collared shirt"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
eps = {}

# ── 1. 새똥 참교육 ─────────────────────────────────────────────
eps["birdpoop"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860206 (조회 6.3만·추천 970) ; 사유지 출입구는 도로교통법상 도로가 아니면 주정차 단속·견인 대상 아님(일반론) ; 형법 314조 업무방해(출입 방해가 업무를 방해할 정도면 성립 가능)",
    t1="입구 막던 차", t2="새가 참교육함", bar="입구에 봉까지 세웠는데 또 댄 차, 새가 참교육", cnt=86,
    title="#입구주차 새똥 참교육", shop="차량용 새똥 제거제, 차량 커버",
    desc=["가게 입구 불법주차 막으려고 두 줄 긋고 봉까지 세웠는데 또 댄 차.",
          "연락처도 없던 그 차 위로 새들이 참교육을 해줌.",
          "사유지 입구 주차, 과태료가 안 나오는 이유와 대처법."],
    tags="#shorts #불법주차 #입구주차 #새똥 #주차빌런",
    comment="님들은 입구 막는 차, 어떻게 대처함?",
    proof=[("입구 두 줄·봉 설치, 연락처 없이 반복 주차, 새똥", "원글 본문·사진"),
           ("사유지 입구는 과태료·견인 어려움", "도로교통법상 '도로' 해당 여부 일반론"),
           ("출입 방해 → 업무방해 가능", "형법 314조")],
    lines=[
        L("입구 막고 주차하던 차가 결국 새들한테 참교육을 당했음.", 1),
        L("어느 건물 입구 앞, 여기에 자꾸 차를 대는 사람이 있었음.", 2, sfx="whoosh"),
        L("그래서 주인이 바닥에 두 줄을 긋고 봉까지 박아놨음.", 3, em=["봉까지"], em_color="yellow"),
        L("근데 이 차는 그 봉 옆에 또 딱 붙여서 세워둠.", 4, sfx="dudung", shake=False),
        L("앞유리에 연락처도 없어서 빼달라고 전화할 방법도 없었음.", 5, em=["연락처도 없어서"]),
        L("그런데 다음 날 보니까 그 차 지붕이랑 유리가 새똥 범벅이 돼 있었음.", 6, sfx="pop", em=["새똥 범벅"], em_color="yellow"),
        L("바로 위 전깃줄이 새들 단골 자리였던 거임.", 7),
        L("댓글은 운전석 손잡이에도 묻었으면 좋겠다는 반응으로 난리가 남.", 8),
        L("근데 이런 차, 왜 사람이 직접 혼내기가 힘드냐면,", 9, sfx="ding"),
        L("건물 입구 같은 사유지는 도로가 아니라서 주정차 과태료나 견인이 거의 안 됨.", 9, em=["과태료나 견인"]),
        L("대신 출입을 막아서 장사를 못 하게 할 정도면 업무방해가 될 수 있음.", 10, em=["업무방해"], em_color="yellow"),
        L("그래서 사진이랑 영상으로 기록부터 남겨두는 게 먼저임.", 10),
        L("님들은 입구 막는 차, 어떻게 대처함?", 6), OUT],
    prompts={
        1: "a dark gray sedan parked right in front of a small building entrance, its roof and windshield splattered with white bird droppings, pigeons on a power line above, morning",
        2: "a narrow entrance driveway of a small commercial building on a Korean side street, two painted yellow lines on the ground, daytime",
        3: f"{M4} hammering a yellow traffic bollard into the ground at a building entrance, painted lines on asphalt, daytime",
        4: "a dark gray sedan parked tightly next to a yellow bollard, blocking a small building entrance, late evening street light",
        5: "close-up of a car windshield dashboard area with no phone number card, empty dashboard, reflections, evening",
        6: "close-up of a dark car roof and windshield covered in many white bird droppings, morning light",
        7: "a row of pigeons and sparrows sitting on a power line directly above a parked car on a Korean side street, low angle, morning",
        8: f"{M4} standing at a building entrance, arms crossed, smirking at a bird-dropping-covered sedan, morning",
        9: "wide shot of a private building entrance area next to a public road, a parked car blocking the entrance, overcast daytime",
        10: f"{M4} photographing a car blocking his shop entrance with his smartphone, daytime",
    })

# ── 2. 범퍼 긁고 현금 합의 ────────────────────────────────────
eps["cashdeal"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860198 (조회 1.2만, 댓글 20) ; 물적사고 할증: 할증기준금액(보통 200만 원) 이하 0.5점·초과 1점, 0.5점도 3년 무사고 할인 유예(뱅크샐러드·보험사 안내) ; 미수선수리비: 수리 대신 현금 수령(860199 댓글)",
    t1="범퍼 긁은 이웃", t2="보험 말고 현금?", bar="같은 아파트 주민이 범퍼 긁고 보험 말고 현금으로 하재요", cnt=20,
    title="#현금합의 범퍼 기스", shop="자동차 스크래치 제거제, 컴파운드",
    desc=["아파트 주차장에서 내 차 범퍼를 긁고 그냥 간 이웃.",
          "블박으로 찾아냈더니 보험 말고 현금으로 하자고 함.",
          "현금 합의 전에 알아야 할 할증 기준과 합의서 쓰는 법."],
    tags="#shorts #현금합의 #자동차보험 #보험할증 #접촉사고",
    comment="님들은 이럴 때 현금 받음, 보험 처리함?",
    proof=[("아파트 주민 범퍼 긁고 연락 없이 감, 블박으로 확인, 현금 합의 요구", "원글 본문"),
           ("할증기준금액 이하 0.5점·초과 1점, 3년 할인 유예", "보험사·뱅크샐러드 할증 기준 안내"),
           ("미수선수리비", "보배드림 860199 댓글·보험 실무")],
    lines=[
        L("내 차 범퍼 긁은 이웃이 보험 말고 현금으로 하자고 함.", 1),
        L("아파트 주차장에 세워둔 차를 같은 아파트 주민이 빼다가 긁고 갔음.", 2, sfx="whoosh"),
        L("연락처도 안 남기고 그냥 가서 블랙박스를 뒤져 차 번호를 찾아냈음.", 3, em=["블랙박스"]),
        L("경비실 통해 연락했더니 긁은 줄 몰랐다고 하다가, 영상 보여주니까 인정함.", 4, sfx="dudung", shake=False),
        L("그러고는 보험 처리 말고 현금으로 해결하자고 한 거임.", 5, em=["현금으로"], em_color="yellow"),
        L("이게 왜 그러냐면, 보험으로 처리하면 상대 보험료가 오르기 때문임.", 6, sfx="ding"),
        L("물적 사고는 200만 원 이하여도 0.5점이 붙고, 3년 동안 무사고 할인이 멈춤.", 6, em=["0.5점"], em_color="yellow"),
        L("그러니까 소액이면 상대 입장에선 현금이 훨씬 싼 거임.", 7),
        L("문제는 받는 쪽이 얼마를 불러야 할지 모른다는 거.", 8),
        L("그래서 먼저 공업사 견적서를 받아서 그 금액을 기준으로 잡아야 함.", 9, em=["견적서"]),
        L("수리 안 하고 돈만 받는 것도 되는데, 이걸 미수선 수리비라고 함.", 9, em=["미수선 수리비"], em_color="yellow"),
        L("그리고 합의서에 금액이랑, 나중에 숨은 손상 나오면 다시 협의한다는 문구를 꼭 넣어야 함.", 10, sfx="pop", em=["합의서"]),
        L("님들은 이럴 때 현금 받음, 보험 처리함?", 5), OUT],
    prompts={
        1: "close-up of a long white scratch on the rear bumper corner of a dark blue sedan in an apartment underground parking garage",
        2: "an apartment complex underground parking garage in Korea with rows of parked cars, fluorescent lights",
        3: f"{M1} watching dashcam footage on a laptop at home at night, focused face, laptop screen glow",
        4: f"{M1} and {M4} talking awkwardly at an apartment security office window, security guard booth, evening",
        5: f"{M4} holding out an envelope of cash with an apologetic smile to {M1} in a parking garage",
        6: "a car insurance renewal notice letter and a calculator on a table, paper text blurred and unreadable, soft light",
        7: "a stack of Korean won banknotes next to a car key on a table, top-down view, soft light",
        8: f"{M1} scratching his head while looking at the scratched bumper of his car, parking garage",
        9: "a car body repair shop estimate being handed over at a counter by a mechanic, paper text blurred, workshop background",
        10: "two people signing a handwritten agreement on a car hood with a pen, paper text blurred and unreadable, close-up of hands",
    })

# ── 3. 미군 택시 먹튀 ─────────────────────────────────────────
eps["gitaxi"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860209 (조회 4.7천, 추천 51) ; 경범죄 처벌법 제3조 제1항 제39호(무임승차 및 무전취식, 10만 원 이하 벌금·구류·과료) ; 처음부터 낼 생각이 없었다면 형법 347조 사기 ; 한미 SOFA 22조(공무 외 범죄는 한국이 1차 재판권) ; 댓글: 험프리스 헌병대 연락처",
    t1="이태원→평택 택시", t2="도착하자 튀었다", bar="이태원에서 태운 미군 2명, 평택 도착하자 요금 안 내고 도주", cnt=13,
    title="#택시먹튀 미군 2명", shop="",
    desc=["이태원에서 미군 2명을 태우고 평택 험프리스까지 간 택시.",
          "카드도 현금도 안 된다더니 편의점 가는 척 골목으로 도주함.",
          "택시 무임승차 처벌과 미군 신고 방법."],
    tags="#shorts #택시먹튀 #무임승차 #택시기사 #평택",
    comment="님들은 이거 잡을 수 있다고 봄?",
    proof=[("이태원→평택 험프리스, 결제 불가, ATM, 골목 도주, 경찰 조서, 영수증 발견", "원글 본문"),
           ("무임승차 10만 원 이하 벌금·구류·과료", "경범죄 처벌법 3조 1항 39호"),
           ("처음부터 안 낼 생각이면 사기죄", "형법 347조"),
           ("공무 외 범죄 한국 1차 재판권", "한미 SOFA 22조")],
    lines=[
        L("이태원에서 태운 미군 2명이 평택까지 가더니 요금도 안 내고 튀었음.", 1),
        L("택시 기사님이 이태원에서 손님 2명을 태웠는데 목적지가 평택 험프리스 기지였음.", 2, sfx="whoosh", em=["평택 험프리스"], em_color="yellow"),
        L("한참을 달려서 도착했는데 카드 결제가 계속 안 됨.", 3),
        L("그러더니 앞에 편의점 현금인출기에서 뽑아주겠다며 내림.", 4),
        L("거기서도 안 뽑힌다더니, 영어로 자기들끼리 속닥속닥함.", 4, sfx="dudung", shake=False, em=["속닥속닥"]),
        L("이번엔 옆 편의점으로 가자면서 한 명이 먼저 슬쩍 사라짐.", 5),
        L("남은 한 명은 따라오라고 하더니 골목이 나오자마자 전력질주로 도망감.", 6, sfx="whoosh", em=["전력질주"], em_color="yellow"),
        L("근데 차 안에 이들이 떨어뜨린 카드 영수증이 남아 있었음.", 7, sfx="ding", em=["카드 영수증"]),
        L("전날 밤 평택에서 영등포 가는 기차표 영수증이라 결제 시간이 다 찍혀 있었음.", 7),
        L("택시비를 안 내고 튀면 경범죄 무임승차로 10만 원 이하 벌금인데,", 8, em=["10만 원 이하"]),
        L("처음부터 안 낼 생각이었으면 사기죄까지 갈 수 있음.", 8, em=["사기죄"], em_color="yellow"),
        L("그리고 미군이라도 공무 중이 아니면 한국 법으로 처벌받고, 기지 헌병대에 신고도 할 수 있음.", 9, sfx="pop"),
        L("기사님은 블박이랑 영수증 들고 끝까지 가겠다고 함.", 10),
        L("님들은 이거 잡을 수 있다고 봄?", 6), OUT],
    prompts={
        1: "view from a taxi driver's seat of two tall young men in casual clothes running away down a narrow alley at night, streetlights",
        2: "a Korean taxi driving on a highway at night with city lights, motion blur, seen from behind",
        3: f"{M5} looking frustrated at a card payment terminal on the taxi dashboard at night, interior light",
        4: "exterior of a small convenience store at night on a quiet street near a military town, ATM visible inside through glass, no signage text",
        5: "two young Western men in hoodies whispering to each other on a sidewalk at night, one glancing back, streetlight",
        6: "a dark narrow alley between low buildings at night with a figure disappearing around the corner, motion blur",
        7: "a crumpled paper receipt lying on the back seat of a taxi, text unreadable, dim interior light",
        8: f"{M5} talking with two Korean police officers next to his taxi at night, flashing lights reflection",
        9: "a military base main gate area in Korea at night with a guard booth and barrier, no text, wide shot",
        10: f"{M5} sitting in his taxi at dawn holding a receipt and looking at a dashcam, determined expression",
    })

# ── 4. 쓰레기 투척 차량 신고 ─────────────────────────────────
eps["trashthrow"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860212 (조회 7.6천, 추천 74) ; 도로교통법 49조 1항(차 밖으로 물건 던지는 행위 금지)·범칙금 5만 원(한국일보 2012.6.17 등) ; 신고 경로: 안전신문고·경찰청 스마트국민제보·지자체 청소행정과(원글 댓글) ; 지자체 무단투기 신고 포상금(서울시 1건당 1만 원, 2026.7 보도)",
    t1="달리면서 쓰레기", t2="창밖으로 휙", bar="차 밖으로 쓰레기 던진 차들, 블박으로 전부 신고", cnt=24,
    title="#쓰레기투척 전부 신고", shop="차량용 쓰레기통",
    desc=["달리는 차 창문 밖으로 쓰레기를 던지는 차들.",
          "블랙박스에 찍힌 차를 하나하나 전부 신고했다는 운전자.",
          "차 밖 투척 범칙금과 신고하는 방법."],
    tags="#shorts #쓰레기투척 #담배꽁초 #안전신문고 #블랙박스",
    comment="님들은 이런 차 보면 신고함?",
    proof=[("쓰레기 투척 차들 각각 신고, 포상금 1만 원 기부", "원글 본문"),
           ("차 밖 물건 투척 금지, 범칙금 5만 원", "도로교통법 49조 1항·범칙금 기준"),
           ("신고 경로 3곳", "원글 댓글"),
           ("지자체 포상금", "서울시 무단투기 제보 포상 보도")],
    lines=[
        L("달리는 차에서 창밖으로 쓰레기 던진 사람들, 전부 신고당함.", 1),
        L("한 운전자 블랙박스에 앞차 창문이 스르륵 내려가는 장면이 찍혔음.", 2, sfx="whoosh"),
        L("그러더니 컵이랑 봉지를 도로에 그냥 휙 던져버림.", 3, sfx="dudung", shake=False, em=["휙"], em_color="yellow"),
        L("한 대도 아니고 여러 대가 이러는 걸 다 모아놨음.", 4),
        L("이 운전자는 각각 전부 신고했다고 함.", 5, em=["전부 신고"]),
        L("그리고 한마디 남김. 미리 포상금 1만 원 고맙다, 모아서 연말에 기부하겠다고.", 6, sfx="pop", em=["포상금 1만 원"], em_color="yellow"),
        L("차 밖으로 물건 던지는 건 도로교통법 위반이라 범칙금 5만 원 나옴.", 7, sfx="ding", em=["5만 원"], em_color="yellow"),
        L("담배꽁초도 똑같음, 불 붙은 채로 뒤차에 날아가면 진짜 위험함.", 8),
        L("신고는 안전신문고나 경찰청 스마트국민제보, 구청 청소과에 하면 됨.", 9, em=["안전신문고"]),
        L("지자체에 따라 신고 포상금을 주는 곳도 있음.", 10),
        L("댓글은 나도 보면 못 참는다는 반응이 대부분이었음.", 5),
        L("님들은 이런 차 보면 신고함?", 4), OUT],
    prompts={
        1: "view through a car windshield of a hand throwing a paper cup out of the driver's window of the car ahead on a city road, daytime",
        2: "dashcam style view from behind of a white sedan on a Korean city road with its driver window rolling down, daytime",
        3: "a crushed paper coffee cup and a plastic bag bouncing on asphalt behind a moving car, motion blur, daytime",
        4: "litter scattered along the shoulder of a Korean urban road, cans cups and plastic bags, daytime",
        5: f"{M2} sitting in his parked car tapping on his smartphone to file a report, focused, daytime",
        6: f"{M2} smiling confidently holding his smartphone in his car, thumbs up, daytime",
        7: "a traffic police officer on the roadside writing a ticket next to a stopped sedan, daytime, background blur",
        8: "close-up of a burning cigarette butt flicked onto a highway lane with sparks, motion blur, dusk",
        9: "a hand holding a smartphone showing a generic report form app with blurred unreadable text, car interior",
        10: "a clean Korean city road lined with trees in the morning, street sweeper cart on the sidewalk",
    })

# ── 5. 테슬라 문 안 열림 ─────────────────────────────────────
eps["tesladoor"] = dict(
    src="https://www.bobaedream.co.kr/view?code=import&No=715125 (조회 2만, 댓글 추천 76 '사고나면 문 안 열려서') ; 오토헤럴드 59410·더드라이브 '中 매립형 도어핸들 2027년부터 금지' — 중국 공업정보화부, 2027.1.1 신규 인증 차량, 외부 손잡이는 손이 걸리는 구조·전원 차단 시에도 기계식 개방 ; 실내 비상 개방 레버는 차종별 위치 상이",
    t1="사고 나면 문이", t2="안 열린다고?", bar="테슬라 사면 사고 날 때 문 안 열린다는 말, 진짜임?", cnt=43,
    title="#숨은손잡이 금지", shop="차량용 비상 탈출 망치",
    desc=["매끈하게 숨은 전기차 도어 손잡이, 사고 나면 안 열린다는 불안.",
          "중국이 2027년부터 숨은 손잡이를 아예 금지하기로 함.",
          "전기차 탈 때 미리 확인할 비상 개방 레버 위치."],
    tags="#shorts #테슬라 #전기차 #도어핸들 #비상탈출",
    comment="님들은 숨은 손잡이, 멋이 먼저임 안전이 먼저임?",
    proof=[("모델3 부러움 글, 댓글 '사고나면 문 안 열려서'(추천 76)", "원글·댓글"),
           ("中 2027.1.1 신규 인증 차량 매립형 금지, 기계식 개방 의무", "오토헤럴드·더드라이브 보도(중국 공업정보화부)"),
           ("실내 수동 개방 레버 위치 확인", "차량 사용설명서 일반 안내")],
    lines=[
        L("전기차 사면 사고 났을 때 문이 안 열린다는 말, 진짜일까?", 1),
        L("추석 귀향길에 모델3가 너무 부럽다는 글이 올라왔는데,", 2, sfx="whoosh"),
        L("추천 제일 많이 받은 댓글이 이거였음.", 3),
        L("사고 나면 문이 안 열려서 갇힐까 봐 무섭다는 거.", 3, sfx="dudung", shake=False, em=["문이 안 열려서"], em_color="yellow"),
        L("요즘 전기차는 손잡이가 차체 안에 쏙 숨어 있다가 전기로 튀어나오는 방식이 많음.", 4, em=["전기로"]),
        L("근데 충돌이나 화재로 전기가 끊기면 밖에서 손잡이를 잡을 수가 없음.", 5),
        L("실제로 구조대가 문을 못 열어서 탈출이 늦어진 사고들이 보고됐음.", 6),
        L("그래서 중국이 세계 처음으로 칼을 뺐음.", 7, sfx="ding"),
        L("2027년 1월부터 새로 인증받는 차는 숨은 손잡이를 못 달게 한 거임.", 7, em=["2027년 1월"], em_color="yellow"),
        L("밖에 손이 걸리는 손잡이가 있어야 하고, 전기가 끊겨도 기계식으로 열려야 함.", 8, em=["기계식으로"]),
        L("그러니까 지금 전기차 타는 사람은 실내 비상 개방 레버 위치부터 꼭 알아둬야 함.", 9, sfx="pop", em=["비상 개방 레버"]),
        L("뒷좌석 가족한테도 알려주고, 비상 탈출 망치 하나쯤은 손 닿는 데 두는 게 좋음.", 10),
        L("님들은 숨은 손잡이, 멋이 먼저임 안전이 먼저임?", 4), OUT],
    prompts={
        1: "close-up of a sleek white electric sedan door with a flush hidden door handle, rain drops, moody light",
        2: "a white electric sedan driving on a Korean highway during holiday traffic, autumn scenery, seen from the side",
        3: f"{M1} reading comments on his smartphone at night on a sofa, worried face, screen glow",
        4: "macro photo of a flush door handle popping out from the body of a modern electric car, clean studio light",
        5: "a damaged electric sedan after a collision on a road at night, smoke, hazard lights, emergency lights reflection",
        6: "Korean firefighters in gear trying to pry open a car door with a tool at a night accident scene, blurred background",
        7: "a large modern factory car assembly line with electric cars, wide shot, industrial light",
        8: "close-up of a traditional protruding pull-style car door handle on a modern electric SUV, daytime",
        9: f"{M1} pointing at the manual door release lever inside a modern car door panel, interior close-up, daytime",
        10: "a small red emergency escape hammer mounted inside a car near the center console, close-up, soft light",
    })

# ── 6. 공단 주차딱지 (E형 찬반) ───────────────────────────────
eps["factoryticket"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860262 (조회 6.3천, 댓글 19) ; 댓글: 통행 방해 없으면 배려 가능하나 코너·횡단보도·소화전 주차는 신고 대상 ; 5대 절대 주정차 금지(소화전·교차로 모퉁이 5m·버스정류소 10m·횡단보도·어린이보호구역)+인도, 안전신문고 1분 신고(정책브리핑)",
    t1="일하고 나왔더니", t2="주차딱지 한 장", bar="공단 근로자 퇴근길 주차딱지, 봐줘야 함?", cnt=19,
    title="#공단 주차딱지", shop="",
    desc=["공장에서 하루 종일 일하고 나왔더니 앞유리에 주차딱지.",
          "주차할 곳이 없다는 근로자와 불법은 불법이라는 쪽이 맞붙음.",
          "공단 주차난, 봐줘야 할까 단속해야 할까."],
    tags="#shorts #주차딱지 #공단주차 #불법주차 #주차난",
    comment="님들은 공단 주차, 봐줘야 한다고 봄?",
    proof=[("화성시 공단 퇴근길 주차딱지, 대책 필요 주장", "원글 본문"),
           ("코너·횡단보도·소화전 주차는 신고 대상이라는 반론", "원글 댓글"),
           ("5대 절대 주정차 금지구역·1분 신고", "정책브리핑 6대 불법 주정차 안내")],
    lines=[
        L("공장에서 하루 종일 일하고 나왔는데 앞유리에 주차딱지가 붙어 있음.", 1),
        L("화성시 한 공단 이야기임.", 2, sfx="whoosh"),
        L("출근해서 열심히 일하고 퇴근하는데 차마다 딱지가 한 장씩 꽂혀 있었음.", 3, sfx="dudung", shake=False, em=["딱지가 한 장씩"], em_color="yellow"),
        L("글쓴이는 공장 근로자도 주차할 곳이 필요하다고 함.", 4),
        L("공단은 주차장은 모자라고 대중교통도 멀어서 차 없이는 출근이 어렵다는 거.", 5, em=["주차장은 모자라고"]),
        L("단속만 하지 말고 대책부터 만들어달라는 주장임.", 5),
        L("근데 댓글 반응은 좀 달랐음.", 6, sfx="ding"),
        L("통행에 방해 안 되면 봐줄 수 있는데, 사진 속 자리는 전부 신고될 만하다는 거.", 7),
        L("교차로 모퉁이, 횡단보도, 소화전 앞은 봉을 박아서라도 막아야 한다는 댓글까지 나옴.", 8, em=["소화전 앞"], em_color="yellow"),
        L("실제로 이 세 곳은 1분만 세워도 누구나 신고할 수 있는 절대 금지 구역임.", 9, sfx="pop", em=["1분만"]),
        L("일하러 간 사람을 봐줘야 한다는 쪽과, 불법은 불법이라는 쪽으로 갈림.", 10),
        L("님들은 공단 주차, 봐줘야 한다고 봄?", 3), OUT],
    prompts={
        1: "close-up of a yellow parking violation notice slip tucked under the windshield wiper of a car, evening light, text unreadable",
        2: "wide shot of a Korean industrial complex street with factories and cars parked along both sides, overcast day",
        3: "a row of cars parked along a factory road each with a notice slip under the wipers, evening",
        4: f"{M2} in a gray work uniform walking out of a factory gate at dusk, tired face",
        5: "an overcrowded small factory parking lot with cars packed tightly, no empty spaces, daytime",
        6: f"{M2} in work uniform reading his phone next to his car in an industrial area, frowning, evening",
        7: "a car parked right at the corner of an intersection in an industrial area, blocking visibility, daytime",
        8: "a red fire hydrant with a car parked directly in front of it on a Korean street, daytime",
        9: "a person photographing an illegally parked car on a crosswalk with a smartphone, daytime",
        10: "a balance scale on a table with a toy car on one side and a small toy factory worker figure on the other, soft studio light",
    })

# ── 7. 스텔스 차량 ───────────────────────────────────────────
eps["stealthcar"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860178 (조회 7.8천, 추천 46) ; 도로교통법 37조 1항(밤 운행 시 전조등·차폭등·미등 점등, 안개·비·눈 등 악천후 포함) ; 범칙금 승용 2만 원(토픽트리·정책브리핑 안내)",
    t1="비 오는 밤인데", t2="라이트를 껐다", bar="비 오는데 라이트 끄고 달리는 스텔스 차량", cnt=12,
    title="#스텔스차량 빗길", shop="",
    desc=["비 오는 어두운 도로에서 혼자만 라이트를 끄고 달리는 차.",
          "앞뒤로 다른 차는 다 켜고 다니는데 저 차만 안 보임.",
          "스텔스 차량 범칙금과 본인이 모르는 이유."],
    tags="#shorts #스텔스차량 #전조등 #빗길운전 #블랙박스",
    comment="님들도 스텔스 차 보면 상향 깜빡여줌?",
    proof=[("비 오는 날 라이트 안 켠 차, 주변 차는 다 켬", "원글 본문·영상"),
           ("밤·악천후 등화 의무", "도로교통법 37조 1항"),
           ("범칙금 승용 2만 원", "경찰 범칙금 기준 안내")],
    lines=[
        L("비 오는 어두운 도로에서 혼자만 라이트를 끄고 달리는 차가 있었음.", 1),
        L("한 운전자 블랙박스에 찍힌 장면인데 앞뒤로 다른 차들은 전부 불을 켜고 있었음.", 2, sfx="whoosh"),
        L("근데 바로 앞 차선에 시커먼 차 한 대가 거의 안 보이게 달리고 있었음.", 3, sfx="dudung", shake=False, em=["거의 안 보이게"], em_color="yellow"),
        L("이런 차를 스텔스 차량이라고 부름.", 4, em=["스텔스 차량"]),
        L("댓글은 앞이 뻥 뚫린 것 같다, 차로 전세 냈다는 반응이었음.", 5),
        L("문제는 본인은 잘 모른다는 거임.", 6, sfx="ding"),
        L("요즘 차는 계기판이 항상 밝게 켜져 있어서 라이트 켠 줄 착각하기 쉬움.", 6, em=["계기판"]),
        L("근데 밤이나 비, 안개처럼 어두울 땐 전조등이랑 미등을 켜는 게 의무임.", 7, em=["의무"], em_color="yellow"),
        L("안 켜면 승용차 기준 범칙금 2만 원이 나옴.", 8, sfx="pop", em=["2만 원"], em_color="yellow"),
        L("돈보다 무서운 건 뒤차가 못 보고 그대로 박는 거임.", 9),
        L("라이트 스위치는 오토에 두고, 출발 전에 한 번만 확인하면 됨.", 10),
        L("님들도 스텔스 차 보면 상향 깜빡여줌?", 3), OUT],
    prompts={
        1: "dashcam style view of a rainy dark Korean road at dusk, a dark sedan ahead with no lights on while other cars have headlights and taillights on",
        2: "rainy evening Korean highway traffic with glowing headlights and red taillights reflecting on wet asphalt, seen from inside a car",
        3: "a black sedan almost invisible on a wet dark road with no taillights, rain streaks, other cars' lights around",
        4: "silhouette of a dark car on a dark rainy road barely visible, dramatic low light",
        5: "view through a rain-covered windshield of an empty-looking lane ahead in the dark, wipers mid-swipe",
        6: "close-up of a brightly lit modern digital car instrument cluster at night, glowing display, no readable text",
        7: "close-up of a car headlight switch on the steering column being turned, interior night light",
        8: "a traffic police officer with a reflective vest and light baton signaling a car to stop on a rainy night",
        9: "a car braking hard behind a dark unlit sedan on a rainy night road, bright brake lights, spray",
        10: f"{M1} turning the headlight stalk to auto before driving, interior view, evening",
    })

# ── 8. 주차장 배수로 덮개 ─────────────────────────────────────
eps["drainlid"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860258 (조회 2.3천, 추천 19) ; 민법 758조(공작물 설치·보존 하자 → 점유자, 점유자 면책 시 소유자 책임) ; 대차료(렌트비)는 수리기간 통상손해로 청구 가능(일반 손해배상 법리) ; 댓글: 렌트비 영수증 모아 민사 청구",
    t1="주차장 들어갔는데", t2="덮개가 차를 긁음", bar="건물 주차장 배수로 덮개에 차 긁혔는데 렌트비는 못 준대요", cnt=11,
    title="#배수로덮개 차 파손", shop="",
    desc=["건물 지하주차장으로 내려가다 배수로 덮개가 들리며 차 하부가 긁힘.",
          "건물은 시설보험도 없고 렌트비는 못 준다고 함.",
          "건물 시설 때문에 차가 망가졌을 때 청구할 수 있는 것."],
    tags="#shorts #주차장사고 #배수로 #렌트비 #손해배상",
    comment="님들은 이거 건물 책임이라고 봄?",
    proof=[("배수로 덮개 들림·하부 손상, 집합건물·시설보험 없음, 렌트비 거부", "원글 본문"),
           ("공작물 하자 → 점유자·소유자 책임", "민법 758조"),
           ("렌트비 청구", "손해배상 통상손해 법리·원글 댓글")],
    lines=[
        L("건물 주차장에 들어가다 바닥 덮개에 차가 긁혔는데, 렌트비는 못 준다고 함.", 1),
        L("퇴근하고 헬스장 건물 지하주차장으로 평소처럼 내려가던 중이었음.", 2, sfx="whoosh"),
        L("그런데 배수로 쇠 덮개가 들리면서 차 밑바닥을 그대로 긁어버림.", 3, sfx="dudung", shake=False, em=["배수로 쇠 덮개"], em_color="yellow"),
        L("블박을 보면 정상 속도로 내려가고 있었음.", 4),
        L("근데 이 건물은 호실마다 주인이 다른 집합건물이라 시설보험도 안 들어 있었음.", 5, em=["시설보험"]),
        L("관리 쪽에선 자차 보험으로 고치면 자기부담금이랑 수리비는 주겠다고 함.", 6),
        L("근데 수리하는 동안 탈 렌트비는 못 준다는 거임.", 6, sfx="pop", em=["렌트비는 못 준다"], em_color="yellow"),
        L("출퇴근해야 하는 직장인이라 차가 없으면 안 되는 상황.", 7),
        L("근데 법은 좀 다르게 봄.", 8, sfx="ding"),
        L("민법 758조는 건물 시설에 하자가 있어서 손해가 나면 관리하는 쪽이 책임진다고 함.", 8, em=["민법 758조"], em_color="yellow"),
        L("수리 기간 렌트비도 사고로 생긴 손해라 같이 청구할 수 있음.", 9, em=["렌트비도"]),
        L("댓글 조언은 일단 렌트하고 영수증을 모아서 같이 청구하라는 거였음.", 10),
        L("님들은 이거 건물 책임이라고 봄?", 3), OUT],
    prompts={
        1: "a sedan driving down a ramp into an underground parking garage, a metal drainage grate cover tilted up scraping the car underside, sparks, dim light",
        2: "the entrance ramp of an underground parking garage of a mid-size Korean commercial building, evening",
        3: "close-up of a lifted steel drainage grate at the bottom of a parking ramp, scratched metal, fluorescent light",
        4: "dashcam style view descending a parking garage ramp slowly, fluorescent lights, concrete walls",
        5: "exterior of a mid-size Korean multi-owner commercial building with a gym on upper floor, evening, no signage text",
        6: f"{M1} talking to a building manager in an office, frustrated gesture, fluorescent light",
        7: f"{M1} in office clothes standing at a bus stop checking the time, stressed, morning",
        8: "a steel drainage grate at a parking garage floor, one side raised and loose, close-up, dim light",
        9: "car rental counter with car keys on the desk and a receipt, text unreadable, soft light",
        10: f"{M1} organizing receipts and photos on a desk with a laptop at night, determined",
    })

# ── 9. 오인 손가락 욕 ────────────────────────────────────────
eps["fingerwrong"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860166 (조회 2.9천, 추천 50) ; 형법 311조 모욕(1년 이하 징역·금고 또는 200만 원 이하 벌금, 공연성 필요) ; 도로교통법 38조 방향지시등 ; 댓글: 진짜 범인 차로변경 위반 신고",
    t1="깜빡이 없던 건", t2="내가 아닌데요", bar="끼어든 차로 오인당해 손가락 욕까지 먹은 억울한 운전자", cnt=9,
    title="#오인 손가락 욕", shop="블랙박스",
    desc=["깜빡이 없이 끼어든 차 때문에 사고 날 뻔한 운전자가 엉뚱한 차에 분노.",
          "억울하게 사진 찍히고 손가락 욕까지 먹은 뒤차 운전자.",
          "도로 위 손가락 욕, 모욕죄가 되는 경우."],
    tags="#shorts #손가락욕 #모욕죄 #방향지시등 #블랙박스",
    comment="님들은 이런 오해 받아본 적 있음?",
    proof=[("깜빡이 없이 끼어든 차, 오인·사진·영상·손가락 욕", "원글 본문"),
           ("모욕죄 1년 이하 또는 200만 원 이하, 공연성", "형법 311조"),
           ("진짜 범인 차로변경 위반 신고", "원글 댓글·도로교통법 38조")],
    lines=[
        L("나는 아무 잘못도 안 했는데 손가락 욕을 먹었음.", 1),
        L("앞에서 한 차가 깜빡이도 없이 훅 끼어들어서 사고가 날 뻔했음.", 2, sfx="whoosh", em=["깜빡이도 없이"]),
        L("뒤에 있던 글쓴이는 놀라서 경적을 길게 눌렀음.", 3),
        L("근데 사고 날 뻔한 차 운전자가 뒤를 돌아보더니 글쓴이 차를 범인으로 찍었음.", 4, sfx="dudung", shake=False, em=["범인으로"], em_color="yellow"),
        L("사진 찍고, 동영상 찍고, 나중엔 손가락 욕까지 날림.", 5, sfx="pop", em=["손가락 욕"], em_color="yellow"),
        L("글쓴이는 저 아니라고, 이 영상 꼭 봤으면 좋겠다고 호소함.", 6),
        L("이게 반대로 억울한 쪽이 따질 수 있는 문제임.", 7, sfx="ding"),
        L("도로에서 다른 사람들이 볼 수 있게 욕을 하면 모욕죄가 될 수 있음.", 8, em=["모욕죄"]),
        L("모욕죄는 1년 이하 징역이나 200만 원 이하 벌금임.", 8, em=["200만 원 이하"], em_color="yellow"),
        L("그리고 엉뚱한 번호판을 찍어서 인터넷에 올리면 더 커질 수도 있음.", 9),
        L("댓글은 진짜 끼어든 차를 차로변경 위반으로 신고하라는 조언이 많았음.", 10),
        L("님들은 이런 오해 받아본 적 있음?", 1), OUT],
    prompts={
        1: "view through a car windshield of an angry driver in the car ahead turning back and raising a hand in an offensive gesture, blurred hand, daytime city traffic",
        2: "dashcam style view of a car abruptly cutting into the lane ahead without a turn signal on a Korean city road, daytime",
        3: f"{W1} pressing the car horn with a startled expression, hands on the steering wheel, daytime",
        4: "a driver in the car ahead looking back angrily through the rear window, seen from the following car, daytime",
        5: "a hand holding a smartphone out of a car window filming the car behind, daytime traffic",
        6: f"{W1} sitting in her parked car looking upset and wronged, holding her phone, evening",
        7: "a courthouse-like gavel on a desk next to a toy car, soft light",
        8: "busy Korean city road with many cars and pedestrians on sidewalk watching, daytime",
        9: "a laptop showing a blurred social media post with a car photo, room at night, screen glow",
        10: "dashcam memory card being held between fingers above a car dashboard, close-up, daytime",
    })

# ── 10. 공영주차장 두고 횡단보도 ─────────────────────────────
eps["zebrapark"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860257 (조회 2.7천, 추천 31) ; 절대 주정차 금지구역(횡단보도 등) 안전신문고 1분 신고·현장 확인 없이 과태료, 횡단보도 과태료 승용 4만 원(정책브리핑 6대 불법 주정차 안내)",
    t1="10m 앞이 주차장", t2="횡단보도에 댐", bar="10m 앞 무료 공영주차장 두고 횡단보도에 댄 차", cnt=9,
    title="#횡단보도 주차 4만", shop="",
    desc=["추석 연휴 무료로 열어준 공영주차장이 10m 앞인데 텅텅 비어 있음.",
          "그 앞 횡단보도 위에 떡하니 세워둔 차.",
          "횡단보도 주차 과태료와 1분 신고 기준."],
    tags="#shorts #횡단보도주차 #불법주차 #안전신문고 #과태료",
    comment="님들은 몇 걸음이 귀찮아서 이러는 거 이해됨?",
    proof=[("10m 앞 공영주차장 연휴 무료·텅텅, 횡단보도 주차, 안전신문고 신고", "원글 본문"),
           ("1분 즉시 신고·과태료 승용 4만 원", "정책브리핑 6대 불법 주정차 안내")],
    lines=[
        L("10m 앞에 텅 빈 무료 주차장을 두고 횡단보도 위에 차를 세움.", 1),
        L("추석 연휴라 공영주차장을 무료로 열어줬는데 안이 거의 텅텅 비어 있었음.", 2, sfx="whoosh", em=["무료"], em_color="yellow"),
        L("근데 바로 앞 횡단보도 위에 차 한 대가 떡하니 서 있음.", 3, sfx="dudung", shake=False, em=["횡단보도 위에"]),
        L("주차장까지 딱 10m, 걸어서 몇 초 거리임.", 4, em=["10m"], em_color="yellow"),
        L("글쓴이는 얼마나 걷기 싫었으면 이랬을까 생각하다가,", 5),
        L("손이 자동으로 안전신문고 앱을 켜고 있었다고 함.", 6, sfx="pop", em=["안전신문고"]),
        L("댓글은 커피 사러 와서 걷기 귀찮았던 모양이라는 반응.", 7),
        L("횡단보도는 1분만 세워도 누구나 신고할 수 있는 절대 금지 구역임.", 8, sfx="ding", em=["1분만"], em_color="yellow"),
        L("사진 두 장이면 단속 공무원이 안 와도 바로 과태료가 나옴.", 9),
        L("승용차는 4만 원, 몇 걸음 아끼려다 4만 원 내는 셈임.", 10, em=["4만 원"], em_color="yellow"),
        L("님들은 몇 걸음이 귀찮아서 이러는 거 이해됨?", 3), OUT],
    prompts={
        1: "a white sedan parked directly on a zebra crosswalk in front of a small coffee shop street in Korea, an almost empty public parking lot visible behind, daytime",
        2: "an almost empty open-air public parking lot in a Korean town on a holiday, only two cars, daytime",
        3: "close-up of a car's wheels stopped on the white stripes of a pedestrian crosswalk, daytime",
        4: "wide shot showing a public parking lot entrance just a few meters from a crosswalk where a car is parked, daytime",
        5: f"{M4} standing on the sidewalk shaking his head at a car parked on a crosswalk, daytime",
        6: "a hand holding a smartphone taking a photo of a car parked on a crosswalk, screen shows camera view, daytime",
        7: f"{W1} walking out of a small cafe holding a takeaway coffee toward her car parked on a crosswalk, daytime",
        8: "pedestrians including an elderly woman and a child walking around a car parked on a crosswalk into the road, daytime",
        9: "a parking violation notice envelope placed on a car seat, text unreadable, soft light",
        10: "a few Korean won banknotes and coins on a car dashboard next to a coffee cup, close-up, daytime",
    })


def upload_md(s, e):
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    return (f"# {s} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n" + "\n".join(e["desc"]) +
            f"\n{e['tags']}\n\n## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop'] or '차량용 블랙박스 2채널, 차량용 휴대폰 거치대'}\n\n"
            f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")


for s, e in eps.items():
    os.makedirs(s, exist_ok=True)
    assert len(e["title"]) <= 12, (s, e["title"], len(e["title"]))
    sc = {"slug": s, "type": "란빵 자동차, 보배드림", "source": e["src"], "title_line1": e["t1"], "title_line2": e["t2"],
          "hook": e["bar"], "channel": "란빵", "voice": "taesub",
          "style": {"sub_box": True, "bar": e["bar"], "bar_count": e["cnt"], "watermark": ""}, "lines": e["lines"]}
    json.dump(sc, open(f"{s}/script.json", "w"), ensure_ascii=False, indent=2)
    with open(f"{s}/prompts.tsv", "w") as f:
        for k in sorted(e["prompts"]):
            f.write(f"{k:02d}\t{e['prompts'][k]}{T}\n")
    open(f"{s}/upload.md", "w").write(upload_md(s, e))
    imgs = sorted({l["img"] for l in e["lines"] if "img" in l})
    assert imgs == sorted(e["prompts"]), (s, imgs)
    print(s, len(e["lines"]) - 1, "lines, imgs", len(imgs), "|", e["title"], len(e["title"]))
