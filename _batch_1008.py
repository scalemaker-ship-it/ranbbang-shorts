#!/usr/bin/env python3
"""란빵 2026-10-07 배치 10편 — 운전 상식·교통법 (원글 없음, 법령·공단 안내 근거).
minspeed50·inspect60·roundabout·wintertire·rightpass·tunnellight·safedist·idling5·washer25·dashsd
→ work/<slug>/script.json + prompts.tsv + upload.md   (10/8 12:00~21:00 10칸 Zernio 예약)
"""
import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "work"))

T = (", photorealistic DSLR photograph, 35mm lens, natural available light, shallow depth of field, "
     "Korean setting, no text no letters no signage no logos no brand marks no watermark, no readable license plates")
M1 = "a Korean man in his early 30s, short black hair, clean-shaven, slim build"
M2 = "a Korean man in his mid 30s, short wavy black hair, light stubble, sturdy build"
W1 = "a Korean woman in her early 30s, shoulder-length dark brown hair, natural light makeup"
M4 = "a Korean man in his late 40s, short graying hair, casual jacket"
POL = "a Korean traffic police officer in a reflective yellow vest"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
eps = {}

# ── 2. 정기검사 늦으면 60만 원 ──────────────────────────────
eps["inspect60"] = dict(
    src="자동차관리법 43조(정기검사), 84조 및 시행령 별표2: 검사기간 만료 후 30일 이내 4만 원, 30일 초과 시 3일 초과마다 2만 원 가산, 최고 60만 원 ; 2025년부터 수검기간 유효기간 만료일 전후 90일·31일(한국교통안전공단 안내)",
    t1="깜빡한 자동차 검사", t2="과태료 최대 60만 원", bar="자동차 검사 깜빡했더니 과태료 날아옴", cnt=None,
    title="#검사 늦으면 60만", shop="차량용 블랙박스, 차량용 휴대폰 거치대",
    desc=["자동차 정기검사 기간 놓치면 과태료가 날마다 불어나는 구조.",
          "처음 30일은 4만 원, 그다음부터 3일마다 2만 원씩, 최대 60만 원.",
          "검사 기간 확인하는 법과 미리 받는 법."],
    tags="#shorts #자동차검사 #정기검사 #과태료 #운전상식",
    comment="님들 차 검사 언제인지 알고 있음?",
    proof=[("만료 후 30일 이내 4만 원", "자동차관리법 시행령 별표2"),
           ("30일 초과 시 3일마다 2만 원, 최고 60만 원", "자동차관리법 시행령 별표2"),
           ("유효기간 만료일 전후로 수검 가능 기간", "한국교통안전공단 안내")],
    lines=[
        L("자동차 검사 깜빡했다가 과태료 60만 원까지 갈 수 있음.", 1),
        L("차 산 지 4년 지나면 2년마다 정기검사를 받아야 함.", 2, sfx="whoosh", em=["2년마다"]),
        L("근데 이 기간이 지나면 과태료가 그냥 끝나는 게 아님.", 3, sfx="dudung", shake=False),
        L("검사 기간 끝나고 30일 안이면 4만 원.", 4, em=["4만 원"], em_color="yellow"),
        L("그 뒤로는 3일 늦을 때마다 2만 원씩 계속 붙음.", 5, sfx="pop", em=["3일"], em_color="yellow"),
        L("그렇게 쌓이면 최대 60만 원까지 나옴.", 6, em=["60만 원"], em_color="yellow"),
        L("오래 안 받고 버티면 번호판 영치까지 갈 수 있음.", 7),
        L("검사 날짜는 공단에서 문자랑 우편으로 미리 알려줌.", 8, sfx="ding", em=["문자"]),
        L("만료일 전후로 받을 수 있는 기간이 있으니, 문자 오면 그때 예약하면 됨.", 9),
        L("자동차365나 교통안전공단 앱에서 내 차 검사 날짜 바로 조회됨.", 10, em=["조회"]),
        L("님들 차 검사 언제인지 알고 있음?", 2), OUT],
    prompts={
        1: "a stack of overdue notice envelopes on a car dashboard, paper text blurred and unreadable, morning light",
        2: "a Korean vehicle inspection center with cars lined up in inspection lanes and a technician, daytime",
        3: f"{M4} frowning at a letter in front of his apartment mailbox, paper text blurred and unreadable",
        4: "a wall calendar with a date circled in red marker, no readable text, soft light",
        5: "an hourglass next to Korean won banknotes on a table, soft light",
        6: "a pile of Korean 50000 won banknotes spread on a car seat, close-up",
        7: "a car parked on a residential street with its front license plate holder empty, daytime",
        8: f"{M4} reading a text message on his smartphone in his car, screen content blurred",
        9: f"{M4} handing his car key to a technician at a vehicle inspection center reception, daytime",
        10: f"{M1} scrolling a car management app on his smartphone on the sofa, screen content blurred, evening",
    })

# ── 5. 오른쪽 추월 ─────────────────────────────────────────
eps["rightpass"] = dict(
    src="도로교통법 21조 1항(앞지르려면 앞차의 왼쪽으로 통행), 21조 3항(안전한 속도·방법), 위반 시 앞지르기 방법 위반 범칙금·벌점(시행령 별표8, 시행규칙 별표28) ; 고속도로 1차로는 앞지르기 차로(시행규칙 별표9)",
    t1="1차로가 느려서", t2="오른쪽으로 추월함", bar="1차로 느린 차 답답해서 오른쪽으로 추월함", cnt=None,
    title="#우측 추월 불법", shop="차량용 블랙박스 2채널, 광각 사이드미러",
    desc=["1차로에서 느리게 가는 차, 답답하다고 오른쪽으로 추월하면 불법일까.",
          "도로교통법은 앞지르기를 앞차 왼쪽으로만 하라고 정해둠.",
          "느린 1차로 차도 위반, 우측 추월도 위반."],
    tags="#shorts #우측추월 #앞지르기 #1차로 #교통법규",
    comment="님들은 1차로 정속 주행 차 만나면 어떻게 함?",
    proof=[("앞지르기는 앞차의 왼쪽으로", "도로교통법 21조 1항"),
           ("위반 시 앞지르기 방법 위반 범칙금·벌점", "도로교통법 시행령 별표8·시행규칙 별표28"),
           ("고속도로 1차로는 앞지르기 차로", "도로교통법 시행규칙 별표9")],
    lines=[
        L("1차로에서 느리게 가는 차 때문에 오른쪽으로 쓱 추월함.", 1),
        L("1차로는 비켜주지도 않고 앞이 텅 비었는데 계속 정속 주행임.", 2, sfx="whoosh"),
        L("근데 오른쪽으로 앞지르는 것도 불법임.", 3, sfx="dudung", shake=False, em=["불법"], em_color="yellow"),
        L("도로교통법은 앞지르기를 하려면 앞차의 왼쪽으로 가라고 정해둠.", 4, em=["왼쪽"], em_color="yellow"),
        L("오른쪽으로 앞지르면 앞지르기 방법 위반으로 범칙금이랑 벌점이 붙음.", 5, sfx="pop", em=["앞지르기 방법 위반"]),
        L("오른쪽은 앞차 운전자가 잘 안 보는 쪽이라 사고가 잘 남.", 6),
        L("그럼 1차로 정속 주행 차는 괜찮냐, 그것도 아님.", 7, sfx="ding"),
        L("고속도로 1차로는 추월할 때만 쓰는 차로라, 계속 달리면 지정차로 위반임.", 8, em=["지정차로 위반"], em_color="yellow"),
        L("결국 둘 다 걸리는 거임.", 9),
        L("답답해도 상향등 한 번 깜빡이고, 비켜줄 때까지 기다리는 게 제일 안전함.", 10),
        L("님들은 1차로 정속 주행 차 만나면 어떻게 함?", 2), OUT],
    prompts={
        1: "a car overtaking another car on the right side on a multi-lane Korean expressway, rear view from a following car, daytime",
        2: "a slow sedan cruising in the leftmost lane of an empty Korean expressway with open road ahead, daytime",
        3: f"{M2} driving with a nervous face glancing at the left side mirror, view from passenger seat, daytime",
        4: "overhead view of a highway with a car passing another car on the left lane correctly, daytime",
        5: f"{POL} standing next to a stopped car on a highway shoulder writing a ticket, daytime",
        6: "view from a driver's seat showing the right side mirror with a car suddenly appearing close in the blind spot, daytime",
        7: "a sedan driving alone in the leftmost lane of a Korean expressway, rear view, daytime",
        8: "a long straight Korean expressway with three lanes and light traffic, wide shot, daytime",
        9: "two cars pulled over on a highway shoulder with a police car behind them, lights flashing, daytime",
        10: f"{M2} calmly driving with both hands on the wheel on a highway, relaxed face, daytime",
    })

# ── 6. 터널 전조등 ─────────────────────────────────────────
eps["tunnellight"] = dict(
    src="도로교통법 37조 1항 2호(터널 안 운행 시 전조등·차폭등·미등 점등), 시행령 별표8 등화점등 불이행 승용 범칙금 2만 원 ; 오토라이트 센서가 밝은 터널 조명에서 안 켜질 수 있음(차량 매뉴얼)",
    t1="터널 들어갈 때", t2="라이트 안 켜면?", bar="터널 안이 밝아서 라이트 안 켜고 달림", cnt=None,
    title="#터널 전조등 의무", shop="LED 전조등 전구, 차량용 블랙박스",
    desc=["터널 안이 밝아도 전조등은 무조건 켜야 하는 이유.",
          "도로교통법상 터널 운행 중 등화 점등은 의무, 안 켜면 범칙금.",
          "오토라이트만 믿으면 안 되는 이유."],
    tags="#shorts #터널 #전조등 #스텔스차량 #운전상식",
    comment="님들 차는 오토라이트 켜져 있음?",
    proof=[("터널 안 운행 시 전조등·차폭등·미등 점등", "도로교통법 37조 1항 2호"),
           ("등화점등 불이행 승용 범칙금 2만 원", "도로교통법 시행령 별표8"),
           ("오토라이트 조도 센서 한계", "차량 매뉴얼 일반")],
    lines=[
        L("터널 안이 대낮처럼 밝아서 라이트 안 켜고 달림.", 1),
        L("요즘 터널은 조명이 밝아서 라이트 꺼져 있는지도 모름.", 2, sfx="whoosh"),
        L("근데 터널 안에선 라이트 켜는 게 법으로 정해진 의무임.", 3, sfx="dudung", shake=False, em=["의무"], em_color="yellow"),
        L("도로교통법이 터널 안을 달릴 땐 전조등이랑 미등을 켜라고 정해둠.", 4, em=["전조등"]),
        L("안 켜면 범칙금 2만 원.", 5, sfx="pop", em=["2만 원"], em_color="yellow"),
        L("문제는 돈보다 뒤차임.", 6),
        L("라이트 꺼진 차는 뒤에서 미등도 안 보여서 터널 안에서 갑자기 나타남.", 7, em=["미등"], em_color="yellow"),
        L("특히 터널 들어가는 순간 눈이 어둠에 적응 못 해서 더 안 보임.", 8),
        L("오토라이트도 터널이 밝으면 안 켜질 때가 있어서 계기판 표시등을 꼭 봐야 함.", 9, sfx="ding", em=["계기판 표시등"]),
        L("터널 보이면 라이트부터 켜는 거, 이게 습관이 돼야 함.", 10),
        L("님들 차는 오토라이트 켜져 있음?", 1), OUT],
    prompts={
        1: "a car driving inside a brightly lit Korean highway tunnel with its headlights off, rear view, orange tunnel lights",
        2: "inside a modern bright white-lit highway tunnel in Korea, cars driving, long perspective",
        3: "a car entering a highway tunnel entrance on a sunny day, headlights glowing, mountain behind",
        4: "close-up of a car headlight switch stalk turned on with headlight indicator glowing on the dashboard, night tone",
        5: f"{POL} standing near a tunnel exit on a highway, cars passing, daytime",
        6: "view from a driver's seat inside a tunnel with a dark car without lights ahead barely visible, orange lighting",
        7: "rear of a dark gray car without tail lights inside a dim tunnel, almost invisible, orange lighting",
        8: "view through a windshield at the moment of entering a dark tunnel from bright sunlight, high contrast",
        9: "close-up of a car dashboard with a green headlight indicator icon glowing, no text",
        10: f"{W1} driving and turning on the headlight switch as a tunnel approaches, daytime, view from passenger seat",
    })

# ── 7. 안전거리 2초 ────────────────────────────────────────
eps["safedist"] = dict(
    src="도로교통법 19조 1항(앞차 정지 시 충돌 피할 거리 확보), 시행령 별표8 안전거리 미확보 승용 범칙금 2만 원, 시행규칙 별표28 벌점 10점 ; 2초 규칙·악천후 2배(도로교통공단 안전운전 안내)",
    t1="앞차랑 얼마나", t2="떨어져야 안전함?", bar="앞차 바짝 붙어 가다가 앞차가 급정거함", cnt=None,
    title="#안전거리 2초", shop="차량용 블랙박스 2채널, 비상삼각대",
    desc=["앞차랑 얼마나 떨어져야 안전한지 숫자 없이 아는 법.",
          "앞차가 지나간 표지판을 내가 2초 뒤에 지나가면 안전거리.",
          "안전거리 미확보는 범칙금 2만 원에 벌점 10점."],
    tags="#shorts #안전거리 #추돌사고 #운전상식 #교통법규",
    comment="님들은 앞차랑 몇 초 간격으로 다님?",
    proof=[("앞차 급정지 시 충돌 피할 거리 확보", "도로교통법 19조 1항"),
           ("승용 범칙금 2만 원·벌점 10점", "도로교통법 시행령 별표8·시행규칙 별표28"),
           ("2초 규칙, 빗길·눈길은 2배 이상", "도로교통공단 안전운전 안내")],
    lines=[
        L("앞차 바짝 붙어 가다가 앞차가 급정거함.", 1),
        L("뒤에서 박으면 웬만하면 뒤차 과실이 거의 다임.", 2, sfx="dudung", shake=False, em=["뒤차 과실"], em_color="yellow"),
        L("그럼 얼마나 떨어져야 하냐, 숫자 몰라도 되는 방법이 있음.", 3, sfx="whoosh"),
        L("앞차가 표지판이나 가로등을 지나는 순간 속으로 하나, 둘 셈.", 4, sfx="ding", em=["하나, 둘"], em_color="yellow"),
        L("둘 다 세기 전에 내가 거기 도착하면 너무 붙은 거임.", 5),
        L("이게 2초 규칙인데, 사람이 보고 브레이크 밟기까지 걸리는 시간을 생각한 거임.", 6, em=["2초 규칙"]),
        L("비 오거나 눈 오면 미끄러워서 두 배로 늘려야 함.", 7, em=["두 배"], em_color="yellow"),
        L("그리고 이거 법으로도 정해져 있음.", 8, sfx="pop"),
        L("안전거리 미확보로 걸리면 범칙금 2만 원에 벌점 10점.", 9, em=["벌점 10점"]),
        L("뒤에서 누가 끼어들어도 그냥 다시 벌리면 됨, 그게 내 차 지키는 거임.", 10),
        L("님들은 앞차랑 몇 초 간격으로 다님?", 4), OUT],
    prompts={
        1: "view from inside a car tailgating very close behind another car with bright red brake lights on a Korean city road, daytime",
        2: "a rear-end collision between two sedans on a Korean road, crumpled bumper, drivers stepping out, daytime",
        3: f"{M1} driving on a highway looking ahead thoughtfully, view from passenger seat, daytime",
        4: "view through a windshield of a car ahead passing a roadside lamp post on a highway, daytime",
        5: "close distance between two cars on a highway, rear view of the front car very close, daytime",
        6: "close-up of a driver's foot pressing the brake pedal, interior footwell",
        7: "two cars on a wet rainy highway with a long gap between them, spray from tires, overcast",
        8: f"{POL} directing traffic on a city road, daytime",
        9: "a traffic ticket paper on a car steering wheel, text blurred and unreadable",
        10: "wide shot of cars driving on a Korean expressway with comfortable spacing between them, sunny day",
    })

# ── 8. 공회전 과태료 ───────────────────────────────────────
eps["idling5"] = dict(
    src="대기환경보전법 59조(공회전 제한, 시·도 조례로 지정), 94조 과태료(공회전 제한 위반 5만 원) ; 시·도 조례: 일반적으로 경고 후 5분 초과 시 과태료 5만 원, 터미널·차고지 등 중점 제한구역은 경고 없이 단속, 기온 5℃ 이하·27℃ 이상(지역별 상이) 등 예외(경기도·서울시 안내)",
    t1="에어컨 켜고 기다리다", t2="과태료 5만 원", bar="주차해놓고 시동 켠 채 에어컨 틀고 기다림", cnt=None,
    title="#공회전 과태료 5만", shop="차량용 햇빛가리개, 차량용 USB 선풍기",
    desc=["시동 켜놓고 차 안에서 기다리기만 해도 과태료가 나올 수 있음.",
          "지자체 조례로 공회전 제한, 걸리면 과태료 5만 원.",
          "날씨가 아주 덥거나 추울 땐 예외도 있음."],
    tags="#shorts #공회전 #과태료 #운전상식 #차량관리",
    comment="님들은 차에서 기다릴 때 시동 켜둠?",
    proof=[("공회전 제한은 시·도 조례로 지정", "대기환경보전법 59조"),
           ("공회전 제한 위반 과태료 5만 원", "대기환경보전법 94조·시행령 별표"),
           ("경고 후 5분 초과, 중점구역은 경고 없이, 기온 예외", "서울시·경기도 공회전 제한 조례 안내")],
    lines=[
        L("주차해놓고 시동 켠 채 에어컨 틀고 기다리다 과태료 받을 수 있음.", 1),
        L("차 안에서 사람 기다리거나 폰 볼 때 다들 시동 켜두잖음.", 2, sfx="whoosh"),
        L("근데 이게 공회전이라서 단속 대상임.", 3, sfx="dudung", shake=False, em=["공회전"], em_color="yellow"),
        L("대기환경보전법에 따라 시도 조례로 공회전을 제한하고 있음.", 4),
        L("보통은 단속반이 먼저 경고하고, 그 뒤에도 5분 넘게 켜두면 과태료 5만 원.", 5, sfx="pop", em=["5만 원"], em_color="yellow"),
        L("터미널이나 차고지 같은 중점 제한구역은 경고 없이 바로 걸리기도 함.", 6, em=["경고 없이"]),
        L("대신 엄청 덥거나 추운 날은 예외라서 에어컨, 히터는 봐줌.", 7, sfx="ding", em=["예외"]),
        L("기준 온도는 지역마다 조금씩 다름.", 8),
        L("과태료 아니어도 공회전 10분이면 기름만 날리는 거임.", 9),
        L("오래 기다릴 거면 시동 끄고 창문 조금 열어두는 게 이득임.", 10),
        L("님들은 차에서 기다릴 때 시동 켜둠?", 2), OUT],
    prompts={
        1: "a parked car with its engine running and faint exhaust vapor from the tailpipe on a city street, daytime",
        2: f"{M2} sitting in the driver seat of a parked car looking at his smartphone with the air conditioner vent blowing, daytime",
        3: "close-up of a car exhaust tailpipe emitting faint vapor while parked, daytime",
        4: "a city bus terminal parking area in Korea with buses parked, daytime",
        5: "a municipal enforcement officer in a vest knocking on the window of an idling parked car, daytime",
        6: "a Korean intercity bus terminal with taxis and buses waiting, daytime",
        7: "a car parked under a scorching summer sun with heat haze over the road, Korea",
        8: "a car parked on a snowy street in winter with frost on the windows, morning",
        9: "close-up of a car fuel gauge needle near empty, dashboard, no text",
        10: f"{M2} sitting in a parked car with the engine off and the window slightly open, relaxed, daytime",
    })

# ── 9. 겨울 워셔액 ─────────────────────────────────────────
eps["washer25"] = dict(
    src="워셔액 제품별 어는점 표시(사계절·겨울용 약 -25℃ 전후 제품 다수, 여름용·발수 일반 제품은 영하에서 얼 수 있음) ; 물 희석 시 어는점 상승 ; 동결 시 분사구·호스·펌프 손상(차량 매뉴얼 일반) — 특정 수치는 제품 라벨 기준",
    t1="겨울 오기 전에", t2="워셔액 이거 바꿔야 함", bar="첫 추위에 워셔액 뿌렸더니 앞유리가 얼어붙음", cnt=None,
    title="#겨울 워셔액", shop="사계절 워셔액, 김서림 방지제",
    desc=["추운 날 워셔액 뿌렸더니 앞유리에 그대로 얼어서 앞이 안 보이는 상황.",
          "여름에 넣은 워셔액이나 물 섞은 워셔액은 영하에 얼 수 있음.",
          "겨울 오기 전에 워셔액 확인하는 법."],
    tags="#shorts #워셔액 #겨울철차관리 #운전상식 #차량관리",
    comment="님들 차엔 지금 무슨 워셔액 들어 있음?",
    proof=[("겨울용·사계절 워셔액 어는점 표시(예: -25℃)", "제품 라벨"),
           ("물 섞으면 어는점 올라감", "워셔액 제조사 안내 일반"),
           ("얼면 분사구·호스·펌프 손상 우려", "차량 매뉴얼 일반")],
    lines=[
        L("첫 추위에 워셔액 뿌렸더니 앞유리가 그대로 얼어붙음.", 1),
        L("유리에 닿자마자 살얼음이 돼서 와이퍼로 닦을수록 더 뿌예짐.", 2, sfx="dudung", shake=False, em=["살얼음"], em_color="yellow"),
        L("범인은 여름에 넣어둔 워셔액이었음.", 3, sfx="whoosh"),
        L("여름용이나 물을 많이 섞은 워셔액은 영하로 떨어지면 얼어버림.", 4, em=["물을 많이 섞은"]),
        L("통 안에서 얼면 분사가 안 되고, 심하면 펌프랑 호스까지 망가짐.", 5, sfx="pop", em=["펌프"]),
        L("그래서 겨울 오기 전에 워셔액을 바꿔줘야 함.", 6, sfx="ding"),
        L("라벨에 영하 몇 도까지 안 어는지 적혀 있으니 그거 보고 사계절용이나 겨울용으로.", 7, em=["라벨"], em_color="yellow"),
        L("남은 여름 워셔액은 최대한 써서 비우고 채우는 게 좋음.", 8),
        L("물을 섞으면 어는점이 올라가니까 원액 그대로 넣어야 함.", 9, em=["원액"], em_color="yellow"),
        L("추운 아침엔 차 좀 데운 다음에 뿌리면 덜 얼음.", 10),
        L("님들 차엔 지금 무슨 워셔액 들어 있음?", 3), OUT],
    prompts={
        1: "view from the driver seat of a windshield covered with a thin icy smear after spraying washer fluid on a freezing morning, blurry road",
        2: "close-up of wiper blades smearing a frozen film across a car windshield, frosty morning",
        3: f"{M4} standing next to his car with the hood open on a cold morning, puzzled face, breath visible",
        4: "close-up of a translucent washer fluid reservoir in a car engine bay with slushy frozen fluid inside",
        5: "close-up of a car windshield washer nozzle on the hood covered with ice, frosty morning",
        6: "a Korean apartment parking lot on a cold late autumn morning with frost on cars",
        7: f"{M4} holding a plain unlabeled blue bottle of washer fluid at a car supply store shelf, label text blurred",
        8: "a car washer fluid being sprayed onto a windshield on a mild day, droplets, close-up",
        9: f"{M4} pouring blue washer fluid from a bottle into the car reservoir under an open hood, daytime",
        10: "a car with its engine warming up on a frosty morning, headlights on, faint exhaust vapor, dawn light",
    })

# ── 10. 블박 메모리 포맷 ───────────────────────────────────
eps["dashsd"] = dict(
    src="블랙박스 제조사 매뉴얼 일반: 메모리카드는 소모품, 주기적 포맷 권장(2주~1개월), 상시녹화는 용량이 차면 오래된 파일부터 덮어씀, 충격 감지 영상은 이벤트 폴더 별도 저장(이 폴더도 가득 차면 덮어쓰는 제품 있음) ; 고온 환경에서 수명 단축",
    t1="사고 났는데", t2="블박에 영상이 없음", bar="사고 나서 블박 열었는데 영상이 하나도 없음", cnt=None,
    title="#블박 메모리 포맷", shop="블랙박스 메모리카드, 자동차 블랙박스 2채널",
    desc=["사고 났는데 블랙박스에 영상이 없거나 깨져 있는 이유.",
          "메모리카드는 소모품이라 오래 쓰면 저장이 안 되는 경우가 있음.",
          "블박 영상 지키는 포맷 주기와 사고 직후 할 일."],
    tags="#shorts #블랙박스 #메모리카드 #운전상식 #교통사고",
    comment="님들은 블박 메모리 마지막으로 언제 확인함?",
    proof=[("메모리카드는 소모품, 주기적 포맷 권장", "블랙박스 제조사 매뉴얼 일반"),
           ("상시녹화는 오래된 파일부터 덮어씀", "블랙박스 제조사 매뉴얼 일반"),
           ("충격 영상은 이벤트 폴더 별도 저장", "블랙박스 제조사 매뉴얼 일반")],
    lines=[
        L("사고 나서 블박 열어봤는데 영상이 하나도 없음.", 1),
        L("분명 불은 들어와 있었는데 파일이 깨져서 안 열림.", 2, sfx="dudung", shake=False, em=["깨져서"], em_color="yellow"),
        L("범인은 메모리카드였음.", 3, sfx="whoosh"),
        L("블박은 하루 종일 쓰고 지우기를 반복해서 메모리카드가 금방 닳는 소모품임.", 4, em=["소모품"], em_color="yellow"),
        L("여름엔 차 안이 뜨거워서 더 빨리 망가짐.", 5),
        L("그래서 제조사들은 2주에서 한 달에 한 번 포맷하라고 함.", 6, sfx="ding", em=["한 달에 한 번"]),
        L("그리고 상시 녹화는 꽉 차면 오래된 것부터 지워짐.", 7, sfx="pop", em=["오래된 것부터"]),
        L("사고 나면 바로 메모리를 빼서 폰이나 컴퓨터에 옮겨둬야 함.", 8, em=["바로"], em_color="yellow"),
        L("안 그러면 며칠 몰다가 그 영상 위에 덮어써질 수 있음.", 9),
        L("포맷하다가 에러 나면 그냥 새 카드로 바꾸는 게 답임.", 10),
        L("님들은 블박 메모리 마지막으로 언제 확인함?", 4), OUT],
    prompts={
        1: f"{M1} looking at a laptop screen in shock while a small memory card adapter is plugged in, screen content blurred, night",
        2: "a minor car accident scene with two cars on a Korean road, drivers checking damage, daytime",
        3: "close-up of a tiny microSD card held between fingers next to a dashcam, soft light",
        4: "a dashcam mounted behind a car rearview mirror with a small red recording light glowing, close-up",
        5: "a car parked under blazing summer sun with heat haze, windshield reflecting the sun",
        6: f"{M1} pressing buttons on a dashcam mounted on the windshield, close-up of hands, daytime",
        7: "a dashcam on a windshield recording a busy city road at night, light trails",
        8: f"{M1} pulling a microSD card out of a dashcam right after an accident, close-up of hands, daytime",
        9: "a car driving away on a city road at dusk, rear view, tail lights",
        10: "a brand-new microSD card in a sealed blister package on a car seat, packaging text blurred",
    })


# ── A. 고속도로 최저속도 ───────────────────────────────────
eps["minspeed50"] = dict(
    src="도로교통법 17조, 시행규칙 19조 1항(고속도로 최저속도 매시 50km, 편도 1차로 포함) ; 안전표지로 따로 정한 구간은 그 속도 ; 최저속도 위반은 범칙금 대상(시행령 별표8) ; 정체 등 부득이한 경우 예외(17조 3항 취지) ; 저속 차량은 오른쪽 차로(시행규칙 별표9)",
    t1="고속도로에서", t2="너무 느려도 걸림", bar="고속도로에서 안전하게 40으로 달렸는데 단속됨", cnt=None,
    title="#고속도로 최저속도", shop="차량용 블랙박스 2채널, 비상삼각대",
    desc=["고속도로는 빨리 달려서만 걸리는 게 아님.",
          "고속도로 최저속도는 시속 50km, 이보다 느리면 단속 대상.",
          "막힐 때는 예외, 느리게 가야 하면 맨 오른쪽 차로로."],
    tags="#shorts #고속도로 #최저속도 #교통법규 #운전상식",
    comment="님들은 고속도로에서 너무 느린 차 만나본 적 있음?",
    proof=[("고속도로 최저속도 매시 50km", "도로교통법 시행규칙 19조 1항"),
           ("최저속도 위반은 범칙금 대상", "도로교통법 시행령 별표8"),
           ("정체 등 부득이한 경우 예외", "도로교통법 17조 3항 취지"),
           ("느린 차는 오른쪽 차로", "도로교통법 시행규칙 별표9")],
    lines=[
        L("고속도로에서 안전하게 시속 40으로 달렸는데 단속 대상임.", 1),
        L("과속만 걸리는 줄 아는데 고속도로는 너무 느려도 걸림.", 2, sfx="whoosh", em=["너무 느려도"], em_color="yellow"),
        L("고속도로에는 최저속도가 있음.", 3, sfx="dudung", shake=False),
        L("법으로 정해진 고속도로 최저속도는 시속 50km.", 4, em=["시속 50km"], em_color="yellow"),
        L("이보다 느리게 달리면 최저속도 위반으로 범칙금 대상임.", 5, sfx="pop", em=["최저속도 위반"]),
        L("뒤차들이 다 100으로 오는데 혼자 40이면, 그게 오히려 사고를 부름.", 6),
        L("뒤차가 갑자기 브레이크 밟거나 급하게 차로를 바꾸게 되니까.", 7),
        L("대신 길이 막히거나 눈비가 와서 어쩔 수 없을 땐 예외임.", 8, sfx="ding", em=["예외"]),
        L("고속도로가 무서워서 천천히 가고 싶으면 맨 오른쪽 차로로 가면 됨.", 9, em=["맨 오른쪽"], em_color="yellow"),
        L("차가 이상해서 느려졌으면 비상등 켜고 갓길이나 휴게소로 빼야 함.", 10),
        L("님들은 고속도로에서 너무 느린 차 만나본 적 있음?", 2), OUT],
    prompts={
        1: "a small car driving slowly in the middle lane of a Korean expressway while other cars rush past on both sides, motion blur, daytime",
        2: f"{W1} driving nervously gripping the steering wheel with both hands on a highway, view from passenger seat, daytime",
        3: "a long straight Korean expressway with multiple lanes and green mountains, wide shot, daytime",
        4: "close-up of a car speedometer needle pointing low around forty, dashboard, no readable text",
        5: f"{POL} standing on a highway shoulder next to a pulled over small car, daytime",
        6: "rear view from a fast car approaching a very slow car ahead on a highway, brake lights, daytime",
        7: "a car swerving suddenly into another lane on a highway to avoid a slow car ahead, motion blur, daytime",
        8: "a congested Korean expressway in heavy rain with slow traffic and headlights on",
        9: "a small car driving calmly in the rightmost lane of a Korean expressway, rear view, daytime",
        10: "a car with hazard lights blinking pulled onto a highway shoulder, daytime",
    })

# ── B. 회전교차로 ──────────────────────────────────────────
eps["roundabout"] = dict(
    src="도로교통법 25조의2(회전교차로: 반시계방향 통행, 진입 시 서행 또는 일시정지, 이미 진행 중인 차에 진로 양보) ; 38조 1항 방향지시등(승용 범칙금 3만 원, 시행령 별표8) ; 국토교통부 회전교차로 통행방법 안내(양보·서행)",
    t1="회전교차로", t2="누가 먼저 감?", bar="회전교차로에서 들어가는 차랑 도는 차랑 부딪힘", cnt=None,
    title="#회전교차로 우선순위", shop="차량용 블랙박스 2채널, 광각 사이드미러",
    desc=["회전교차로에서 들어가려는 차와 이미 돌고 있는 차, 누가 먼저일까.",
          "도로교통법상 정답은 이미 돌고 있는 차.",
          "진입할 땐 서행·일시정지, 나갈 땐 오른쪽 깜빡이."],
    tags="#shorts #회전교차로 #교통법규 #운전상식 #과실비율",
    comment="님들 동네 회전교차로는 다들 잘 지킴?",
    proof=[("반시계방향 통행, 진입 시 서행 또는 일시정지", "도로교통법 25조의2 1·2항"),
           ("이미 진행 중인 차에 진로 양보", "도로교통법 25조의2 2항"),
           ("방향지시등 불이행 승용 범칙금 3만 원", "도로교통법 38조·시행령 별표8")],
    lines=[
        L("회전교차로에서 들어가는 차랑 도는 차랑 쾅 부딪힘.", 1),
        L("둘 다 내가 먼저라고 우기는데, 이건 법에 답이 정해져 있음.", 2, sfx="whoosh"),
        L("정답은 이미 돌고 있는 차가 먼저임.", 3, sfx="dudung", shake=False, em=["돌고 있는 차"], em_color="yellow"),
        L("도로교통법은 회전교차로에 들어갈 땐 서행하거나 일시정지하라고 정해둠.", 4, em=["일시정지"]),
        L("그리고 이미 안에서 돌고 있는 차한테 양보해야 함.", 5, em=["양보"], em_color="yellow"),
        L("내가 오른쪽에 있다고 먼저 들어가도 되는 게 아님.", 6, sfx="pop"),
        L("돌 때는 무조건 시계 반대 방향.", 7, sfx="ding", em=["시계 반대 방향"]),
        L("나갈 때는 오른쪽 깜빡이를 켜야 뒤에서 기다리는 차가 들어올 수 있음.", 8, em=["오른쪽 깜빡이"], em_color="yellow"),
        L("깜빡이 안 켜면 범칙금 3만 원.", 9),
        L("진입하는 쪽에 양보 표시랑 정지선이 있으면 일단 멈추는 게 정답임.", 10),
        L("님들 동네 회전교차로는 다들 잘 지킴?", 1), OUT],
    prompts={
        1: "a minor collision at the entrance of a small Korean roundabout between a car entering and a car circulating, drivers stepping out, daytime",
        2: f"{M2} and {M4} arguing beside their two cars at a roundabout, daytime",
        3: "aerial view of a small roundabout in a Korean suburban town with cars circulating counterclockwise, daytime",
        4: "a car slowing down and stopping at the yield line before entering a roundabout, view from behind, daytime",
        5: "view through a windshield waiting at a roundabout entry while another car passes in front inside the circle, daytime",
        6: "aerial view of a regular four-way intersection with traffic lights in a Korean city, daytime",
        7: "aerial drone view of a roundabout with light traffic flowing around a green central island, daytime",
        8: "close-up of a car side with the right turn signal blinking amber while exiting a roundabout, daytime",
        9: f"{POL} standing near a roundabout watching traffic, daytime",
        10: "a car stopped at a roundabout entrance with a triangular yield marking painted on the road surface, no text, daytime",
    })

# ── C. 겨울용 타이어 7도 ───────────────────────────────────
eps["wintertire"] = dict(
    src="한국타이어 겨울철 안전운행 안내: 겨울용 타이어는 영상 7℃ 이하에서도 잘 굳지 않는 컴파운드, 사계절 타이어는 저온에서 경화 ; 한국타이어 테스트 눈길 40km/h 제동거리 겨울용 18.49m vs 사계절 37.84m (hankooktire.com 미디어 자료) ; 겨울용 타이어 홈 깊이 4mm 이하면 겨울 성능 저하(업계 안내)",
    t1="눈 안 와도", t2="7도면 갈아야 함", bar="눈도 안 왔는데 벌써 겨울 타이어 끼라고 함", cnt=None,
    title="#겨울타이어 7도", shop="스노우체인, 스노우 브러쉬",
    desc=["겨울용 타이어는 눈 올 때 끼는 게 아니라 기온 7도가 기준.",
          "사계절 타이어는 추우면 고무가 딱딱해져서 미끄러짐.",
          "눈길 제동거리가 거의 두 배 차이 나는 이유."],
    tags="#shorts #겨울타이어 #스노우타이어 #겨울철차관리 #운전상식",
    comment="님들은 겨울에 타이어 바꿔 끼움?",
    proof=[("겨울용 타이어는 7℃ 이하에서도 경화가 덜함", "한국타이어 겨울철 안전운행 안내"),
           ("눈길 40km/h 제동 겨울용 18.49m vs 사계절 37.84m", "한국타이어 테스트(미디어 자료)")],
    lines=[
        L("눈도 안 왔는데 벌써 겨울 타이어 끼라고 함.", 1),
        L("겨울 타이어는 눈 와야 끼는 거 아니냐고 생각했는데 기준이 기온이었음.", 2, sfx="whoosh"),
        L("기준은 영상 7도.", 3, sfx="dudung", shake=False, em=["7도"], em_color="yellow"),
        L("사계절 타이어는 날이 추워지면 고무가 딱딱하게 굳음.", 4, em=["딱딱하게"]),
        L("고무가 굳으면 땅을 못 잡아서 마른 길에서도 덜 서고 덜 돌아감.", 5),
        L("겨울 타이어는 추워도 말랑한 고무를 써서 7도 밑에서 제 성능이 나옴.", 6, sfx="ding", em=["말랑한 고무"]),
        L("타이어 회사 실험에서 눈길 시속 40으로 달리다 밟았더니 사계절은 37m 넘게 밀림.", 7, sfx="pop", em=["37m"], em_color="yellow"),
        L("겨울 타이어는 18m 조금 넘어서 멈췄음, 거의 절반임.", 8, em=["절반"], em_color="yellow"),
        L("아침 기온이 7도 밑으로 떨어지기 시작하면 교체 시기로 보면 됨.", 9),
        L("봄에 다시 빼서 보관하면 두세 시즌은 거뜬히 씀.", 10),
        L("님들은 겨울에 타이어 바꿔 끼움?", 1), OUT],
    prompts={
        1: f"{M1} standing at a Korean tire shop looking at a stack of winter tires with deep tread, mechanic beside him, daytime",
        2: "a dry Korean city road on a chilly late autumn morning with bare trees and people in coats",
        3: "close-up of a car dashboard outside temperature display glowing at a cold morning, number blurred, frosty windshield edge",
        4: "close-up of a regular all-season tire tread on cold frosty asphalt, morning",
        5: "a car braking hard on a cold wet road with tires slightly skidding, motion blur, early morning",
        6: "close-up of a winter tire with deep zigzag sipes and tread blocks, studio-like light in a tire shop",
        7: "a car skidding on a snowy road while braking, snow spray, overcast winter day",
        8: "a car stopping safely on a snowy road with winter tires, snow-covered trees, daytime",
        9: f"{M1} scraping frost off his car windshield on a cold morning in an apartment parking lot",
        10: "a neat stack of four tires in storage bags in a tire hotel storage rack, soft light",
    })


def upload_md(s, e):
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    return (f"# {s} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n" + "\n".join(e["desc"]) +
            f"\n{e['tags']}\n\n## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop'] or '차량용 블랙박스 2채널, 차량용 휴대폰 거치대'}\n\n"
            f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")


for s, e in eps.items():
    os.makedirs(s, exist_ok=True)
    assert len(e["title"]) <= 12, (s, e["title"], len(e["title"]))
    sc = {"slug": s, "type": "란빵 자동차, 운전 상식·교통법", "source": e["src"], "title_line1": e["t1"], "title_line2": e["t2"],
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
