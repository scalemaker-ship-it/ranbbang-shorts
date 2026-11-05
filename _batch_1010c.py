#!/usr/bin/env python3
"""란빵 2026-10-09 배치 C 10편 — 최근 2주 자동차 사고·교통 이슈 뉴스 (보도 기반, 실명·얼굴 없음).
towfall·teenrental·oldreverse·workzone·revenge931·pedalmiss·fsd6000·drunkwake·evdefect·insurfraud
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
M5 = "a Korean man in his mid 50s, short hair, dark windbreaker"
OLD = "a Korean man in his early 80s, thin white hair, cardigan"
TEEN = "Korean teenage boys around 17 years old, casual hoodies"
POL = "a Korean traffic police officer in a reflective yellow vest"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
eps = {}

# ── 1. 견인 중 뒤차 추돌, 고가 아래 추락 ───────────────────────
eps["towfall"] = dict(
    src="서울신문 2026-10-09 '고양 고가도로서 3중 추돌 후 사다리차 추락…1명 사망·2명 부상' (seoul.co.kr/news/society/accident/2026/10/09/20261009500076) — 10/9 오전 7시 40분 고양 덕양구 고가도로, 고장 사다리차를 견인차에 싣던 중 14톤 트럭이 뒤에서 충돌, 사다리차 고가 아래 추락, 견인차 기사(50대) 사망·2명 부상, 경찰·소방 원인 조사 중",
    t1="고장 난 차 싣다가", t2="뒤에서 14톤 트럭이", bar="고가도로에서 고장 차 견인하던 중 뒤에서 트럭이 덮침", cnt=None,
    title="#견인 중 뒤차 추돌", shop="비상삼각대, 차량용 LED 경광봉",
    desc=["한글날 아침 고가도로에서 고장 난 사다리차를 견인차에 싣던 중 사고.",
          "뒤에서 14톤 트럭이 들이받아 사다리차가 고가 아래로 떨어짐.",
          "도로 위에 멈춘 차 보이면 꼭 해야 할 것."],
    tags="#shorts #견인차 #추돌사고 #고가도로 #교통사고",
    comment="님들은 앞에 비상등 켠 차 보이면 바로 차로 바꿈?",
    proof=[("10/9 오전 7시 40분 고양 덕양구 고가도로, 고장 사다리차 견인 작업 중", "서울신문 2026-10-09"),
           ("14톤 트럭이 뒤에서 충돌, 사다리차 고가 아래 추락", "서울신문 2026-10-09"),
           ("견인차 운전자(50대) 사망, 사다리차·승용차 운전자 부상", "서울신문 2026-10-09"),
           ("경찰·소방 정확한 원인 조사 중", "서울신문 2026-10-09")],
    lines=[
        L("고장 난 차를 싣던 견인차 뒤로 14톤 트럭이 그대로 덮침.", 1),
        L("한글날 아침 7시 40분, 경기 고양의 한 고가도로에서 난 사고임.", 2, sfx="whoosh"),
        L("고장 나서 멈춘 작은 사다리차를 견인차에 올리던 중이었음.", 3),
        L("그때 뒤에서 오던 14톤 트럭이 그대로 들이받음.", 4, sfx="dudung", shake=False, em=["14톤 트럭"], em_color="yellow"),
        L("충격에 사다리차는 고가도로 아래로 떨어졌음.", 5, sfx="pop", em=["아래로"]),
        L("견인차 기사였던 50대 남성이 숨졌고 2명이 다쳤음.", 6, em=["숨졌고"], em_color="yellow"),
        L("정확한 원인은 경찰이 조사 중임.", 7),
        L("도로에 멈춘 차랑 그 옆에서 일하는 사람은 생각보다 훨씬 위험함.", 8, sfx="ding"),
        L("멀리서 비상등이나 견인차 불빛이 보이면 바로 속도 줄이고 옆 차로로 비켜야 함.", 9, em=["바로 속도 줄이고"], em_color="yellow"),
        L("특히 큰 차는 멈추는 데 훨씬 오래 걸리니까 앞을 더 멀리 봐야 함.", 10),
        L("님들은 앞에 비상등 켠 차 보이면 바로 차로 바꿈?", 9), OUT],
    prompts={
        1: "a tow truck loading a small broken-down ladder truck on an elevated Korean overpass road with a large cargo truck approaching from behind, early morning",
        2: "an elevated overpass road in a Korean city in the early morning with light traffic, wide shot",
        3: "a small ladder truck stopped on the side of an overpass with hazard lights blinking, early morning",
        4: "a large heavy cargo truck with a damaged front stopped on an overpass road, emergency lights, morning",
        5: "the edge of an elevated overpass with a broken guardrail, emergency vehicles below, morning",
        6: "ambulances and fire trucks at an overpass accident scene, flashing lights, morning",
        7: f"{POL} examining skid marks on an overpass road, morning",
        8: "a tow truck with flashing amber lights stopped behind a broken-down car on a road shoulder, morning",
        9: "view through a windshield of a tow truck with flashing amber lights ahead, car signaling to change lanes, daytime",
        10: "a large cargo truck driving on an overpass road, front view, morning haze",
    })

# ── 2. 텔레그램 렌터카 무면허 10대 ────────────────────────────
eps["teenrental"] = dict(
    src="머니투데이 2026-10-06 '텔레그램으로 차 빌렸다…무면허로 렌터카 몰다 사고 후 도주한 10대' (mt.co.kr/society/2026/10/06/2026100622283679292) ; 뉴스1·MBC 보도 ; 도로교통법 152조(무면허 1년 이하 징역 또는 300만 원 이하 벌금)·54조(사고 후 조치)",
    t1="신호 대기 중에", t2="갑자기 후진해서 쾅", bar="신호 대기 중 앞차가 갑자기 후진해서 박고 도망감", cnt=None,
    title="#무면허 렌터카 10대", shop="차량용 블랙박스 2채널, 후방 블랙박스",
    desc=["신호 대기 중이던 앞차가 갑자기 후진해서 들이받고 그대로 도망감.",
          "잡고 보니 무면허 10대 5명, 차는 텔레그램으로 빌린 렌터카.",
          "무면허 운전과 사고 후 도주, 어떻게 처리될까."],
    tags="#shorts #무면허운전 #렌터카 #뺑소니 #블랙박스",
    comment="님들은 렌터카 면허 확인 제대로 한다고 봄?",
    proof=[("10/4 오후 시흥, 신호 대기 중 후진해 뒤차 충돌 후 도주", "머니투데이 2026-10-06"),
           ("피해 차량이 추격하자 정지, 10대 5명 탑승", "머니투데이 2026-10-06"),
           ("텔레그램으로 차 빌렸다고 진술, 운전자 불구속 입건", "머니투데이·뉴스1 2026-10-06"),
           ("무면허 1년 이하 징역 또는 300만 원 이하 벌금", "도로교통법 152조")],
    lines=[
        L("신호 대기 중인데 앞차가 갑자기 후진해서 쾅 박음.", 1),
        L("그러고는 사과도 없이 그대로 도망가 버림.", 2, sfx="whoosh", em=["도망"], em_color="yellow"),
        L("피해 차가 끝까지 쫓아가니까 결국 멈춰 섰는데, 내린 사람들이 충격이었음.", 3, sfx="dudung", shake=False),
        L("10대 남자애들 5명이 타고 있었고 운전한 애는 면허가 없었음.", 4, em=["면허가 없었음"], em_color="yellow"),
        L("차는 텔레그램으로 빌린 렌터카였다고 함.", 5, sfx="pop", em=["텔레그램"]),
        L("경찰은 운전한 10대를 도로교통법 위반으로 입건했음.", 6),
        L("무면허 운전만 해도 1년 이하 징역이나 300만 원 이하 벌금임.", 7, em=["300만 원"], em_color="yellow"),
        L("사고 내고 그냥 가면 사고 후 미조치까지 붙음.", 8, sfx="ding", em=["사고 후 미조치"]),
        L("무면허 사고는 보험 처리도 복잡해져서 피해자가 제일 골치 아픔.", 9),
        L("뒤에 블박 있으면 앞차 번호부터 찍히니까 꼭 켜두셈.", 10),
        L("님들은 렌터카 면허 확인 제대로 한다고 봄?", 5), OUT],
    prompts={
        1: "view through a windshield as the car ahead suddenly reverses into the front bumper at a red light intersection, daytime, motion",
        2: "a white rental sedan speeding away from an intersection, rear view, daytime, motion blur",
        3: f"{M2} getting out of his car angrily on a roadside after a chase, daytime",
        4: f"{TEEN}, five of them standing awkwardly next to a white sedan on a roadside, faces turned away, daytime",
        5: "close-up of a smartphone on a car seat with a messaging app screen blurred and unreadable, car key beside it",
        6: f"{POL} talking to a teenage boy next to a white sedan, roadside, daytime",
        7: "a judge's gavel on a desk with a toy car next to it, soft light",
        8: "a dented front bumper of a sedan after a minor collision, close-up, daytime",
        9: f"{M2} on the phone with insurance looking at his damaged bumper, daytime",
        10: "a dashcam mounted behind the rearview mirror with an intersection visible ahead, daytime",
    })

# ── 3. 고령 운전자 역주행 ───────────────────────────────────
eps["oldreverse"] = dict(
    src="머니투데이 2026-10-08 '제발 면허 반납 고려를…고령 운전자 역주행에 일가족 날벼락' (mt.co.kr/society/2026/10/08/2026100722363534383) ; YTN 2026-09-30 '고속도로 역주행에 3명 다쳐…잡고 보니 치매 80대' (ytn.co.kr/_ln/0103_202609302247495479) ; 도로교통법 87조(75세 이상 적성검사 3년 주기)·73조(75세 이상 교통안전교육)",
    t1="반대편 차가", t2="중앙선 넘어서 정면으로", bar="추석 끝나고 집 가는데 반대편 차가 중앙선 넘어옴", cnt=None,
    title="#고령운전 역주행", shop="차량용 블랙박스 2채널, 비상삼각대",
    desc=["추석 끝나고 집 가던 가족 차에 중앙선 넘어온 차가 그대로 충돌.",
          "같은 주 인천공항고속도로에선 치매 진단 80대가 7km를 역주행.",
          "고령 운전자 사고 비중과 면허 반납률 2.2%."],
    tags="#shorts #고령운전자 #역주행 #면허반납 #교통사고",
    comment="님들 부모님은 아직 운전하심?",
    proof=[("추석 귀가 중 중앙선 넘은 1953년생 운전자 차량과 충돌, 딸 24바늘", "머니투데이 2026-10-08(커뮤니티 글)"),
           ("2024년 65세 이상 운전자 사고 4만2369건(21.6%), 면허 반납률 2.2%", "머니투데이 2026-10-08"),
           ("9/30 인천공항고속도로 경증 치매 80대 7km 역주행, 3명 부상, 가족 실종신고 상태", "YTN 2026-09-30"),
           ("75세 이상 적성검사 3년 주기·교통안전교육", "도로교통법 87조·73조")],
    lines=[
        L("추석 끝나고 집 가는데 반대편 차가 중앙선을 넘어 정면으로 옴.", 1),
        L("피할 새도 없이 그대로 부딪혔고 딸이 얼굴을 24바늘 꿰맸음.", 2, sfx="dudung", shake=False, em=["24바늘"], em_color="yellow"),
        L("상대 운전자는 1953년생이었다고 함.", 3, sfx="whoosh"),
        L("같은 주에 인천공항고속도로에선 더한 일도 있었음.", 4),
        L("80대 운전자가 중앙분리대를 넘어 7km를 역주행함.", 5, sfx="pop", em=["7km"], em_color="yellow"),
        L("마주 오던 승합차와 부딪혀 3명이 다쳤는데, 이분은 경증 치매 진단을 받은 상태였음.", 6, em=["치매"]),
        L("가족이 이미 실종 신고를 해둔 상황이었다고 함.", 7),
        L("65세 이상 운전자 사고가 전체의 21.6%인데, 면허 반납률은 2.2%뿐임.", 8, sfx="ding", em=["2.2%"], em_color="yellow"),
        L("75세가 넘으면 3년마다 적성검사랑 교통안전교육을 받아야 함.", 9, em=["3년마다"]),
        L("면허를 반납하면 지자체마다 교통카드 같은 지원도 있음.", 10),
        L("님들 부모님은 아직 운전하심?", 3), OUT],
    prompts={
        1: "view through a windshield of an oncoming car crossing the center line on a four-lane Korean road, headlights, dusk",
        2: "a family car with a crushed front after a head-on collision on a Korean road, emergency lights, dusk",
        3: f"{OLD} sitting in the driver seat of a car looking confused, side view through the window, daytime",
        4: "a Korean expressway to an airport at night with light traffic, long exposure light trails",
        5: "a car driving the wrong way on a highway at night, headlights facing oncoming traffic, dramatic",
        6: "a passenger van with a damaged side after a collision on a highway at night, police lights",
        7: "a worried middle-aged Korean woman holding a phone at home at night, dim light",
        8: f"{OLD} holding a car key and looking at it thoughtfully at a kitchen table, soft light",
        9: "an elderly Korean man taking a cognitive test at a desk in a driver license center, pen and paper blurred",
        10: "a hand placing a driver license card on a counter next to a public transit card, text blurred and unreadable",
    })

# ── 4. 고속도로 작업구간 ───────────────────────────────────
eps["workzone"] = dict(
    src="소비자와 함께(swn.kr) 2026-10-06 '고속도로 작업구간 사고 부상자, 올해 이미 41명… 지난해보다 57.7% 많아' — 한국도로공사 제출자료(국토위 의원실): 2023~2026.9.29 작업구간 사고 152건·사망 30·부상 125, 2026년 38건·부상 41명(작업자 부상 18명), 원인 전방주시 태만 70.4%·졸음 25.0%",
    t1="고속도로 공사 구간", t2="여기서 사람이 죽음", bar="고속도로 공사 구간에서 졸다가 작업 차량 들이받음", cnt=None,
    title="#고속도로 작업구간", shop="차량용 블랙박스 2채널, 졸음방지 껌",
    desc=["고속도로 공사 구간 사고 부상자가 올해 벌써 41명.",
          "작년 한 해보다 57.7% 많고, 원인 95%가 한눈팔기와 졸음.",
          "작업 차량 화살표 보이면 무조건 해야 할 것."],
    tags="#shorts #고속도로 #작업구간 #졸음운전 #교통사고",
    comment="님들은 고속도로 공사 구간 지날 때 속도 줄임?",
    proof=[("2023~2026.9.29 작업구간 사고 152건, 사망 30명·부상 125명", "도로공사 자료, swn.kr 2026-10-06"),
           ("2026년 38건·부상 41명, 전년 26명보다 57.7%↑, 작업자 부상 18명", "swn.kr 2026-10-06"),
           ("원인 전방주시 태만 70.4%·졸음 25.0%", "swn.kr 2026-10-06")],
    lines=[
        L("고속도로 공사 구간에서 졸다가 작업 차량을 그대로 들이받음.", 1),
        L("이런 작업 구간 사고로 올해만 벌써 41명이 다쳤음.", 2, sfx="whoosh", em=["41명"], em_color="yellow"),
        L("작년 한 해 부상자보다 57.7%나 많은 숫자임.", 3, sfx="dudung", shake=False, em=["57.7%"], em_color="yellow"),
        L("최근 4년 가까이 152건이 났고 30명이 목숨을 잃었음.", 4, em=["30명"]),
        L("다친 사람 중엔 도로에서 일하던 작업자도 18명이나 있었음.", 5, sfx="pop", em=["작업자"]),
        L("원인은 딱 두 개였음, 앞을 안 본 게 70%, 졸음이 25%.", 6, em=["졸음"], em_color="yellow"),
        L("공사 구간은 차로가 갑자기 줄어서 멍때리면 바로 사고임.", 7),
        L("멀리서 화살표 차나 라바콘 보이면 그때부터 속도 줄이고 미리 차로 바꿔야 함.", 8, sfx="ding", em=["미리 차로 바꿔야"]),
        L("졸리면 버티지 말고 졸음쉼터나 휴게소에서 10분이라도 눈 붙이셈.", 9),
        L("도로 위 작업자도 누군가의 가족임.", 10),
        L("님들은 고속도로 공사 구간 지날 때 속도 줄임?", 8), OUT],
    prompts={
        1: "a car crashed into the back of a highway maintenance truck with a lit arrow board, Korean expressway, daytime, debris",
        2: "a Korean expressway work zone with orange traffic cones closing a lane and a crash attenuator truck, daytime",
        3: "an ambulance and police at a highway work zone accident scene, daytime",
        4: "a damaged highway maintenance truck with a crumpled rear on the shoulder, daytime",
        5: "highway road workers in orange safety vests and helmets working behind cones on a Korean expressway, daytime",
        6: f"{M4} nodding off at the wheel on a highway, eyes half closed, view from passenger seat, afternoon",
        7: "a highway lane narrowing with cones and a merging arrow board ahead, view through a windshield, daytime",
        8: "a large flashing arrow board on a truck guiding cars to change lanes on a Korean expressway, daytime",
        9: f"{M4} resting with eyes closed in a reclined driver seat at a highway rest area, daytime",
        10: "a highway worker in a safety vest looking at passing traffic from behind cones, back view, sunset",
    })

# ── 5. 보복운전 931건, 면허취소 1건 ───────────────────────────
eps["revenge931"] = dict(
    src="위키트리 2026-10 '3년째 늘어난 보복운전, 면허취소는 단 1건' (wikitree.co.kr/articles/1162741) ; 포인트경제·파이낸셜투데이 동일 보도 — 경찰청 자료(국회의원실): 송치 2022 1570·2023 1705·2024 1717·2025 1726건, 2026 상반기 931건, 2022~2026.6 7649건 중 면허취소 7건 ; 보복운전 입건 시 벌점 100점(시행규칙 별표28), 구속 시 취소 ; 형법 284조 특수협박",
    t1="보복운전 7649건", t2="면허 취소는 단 7건", bar="보복운전 걸려도 면허는 거의 안 뺏긴다고?", cnt=None,
    title="#보복운전 면허취소", shop="차량용 블랙박스 2채널, 후방 블랙박스",
    desc=["보복운전으로 검찰에 넘겨진 사건은 3년째 계속 늘어나는 중.",
          "올해 상반기만 931건인데 면허 취소는 단 1건.",
          "보복운전 처벌 기준과 블박이 중요한 이유."],
    tags="#shorts #보복운전 #면허취소 #특수협박 #블랙박스",
    comment="님들은 보복운전 면허 취소해야 한다고 봄?",
    proof=[("송치 2022 1570·2023 1705·2024 1717·2025 1726건", "경찰청 자료, 위키트리 보도"),
           ("2026 상반기 931건, 면허취소 1건", "위키트리 보도"),
           ("2022~2026.6 7649건 중 면허취소 7건(0.09%)", "포인트경제·위키트리 보도"),
           ("입건 시 벌점 100점, 구속 시에만 취소", "도로교통법 시행규칙 별표28")],
    lines=[
        L("보복운전으로 걸려도 면허는 거의 안 뺏긴다는 통계가 나왔음.", 1),
        L("보복운전으로 검찰에 넘어간 사건이 3년째 계속 늘고 있음.", 2, sfx="whoosh"),
        L("올해 상반기에만 931건, 이 속도면 1년에 1800건 넘게 나옴.", 3, em=["931건"], em_color="yellow"),
        L("근데 면허가 취소된 건 딱 1건이었음.", 4, sfx="dudung", shake=False, em=["딱 1건"], em_color="yellow"),
        L("4년 반 동안 7649건 중에서도 면허 취소는 7건뿐.", 5, em=["7건"]),
        L("이유는 기준 때문임, 보복운전으로 입건되면 벌점 100점으로 100일 정지.", 6, sfx="pop", em=["100일 정지"]),
        L("면허 취소는 구속됐을 때만 되니까 대부분 100일 지나면 다시 운전함.", 7),
        L("그래서 국회에서도 처분 기준을 손봐야 한다는 말이 나옴.", 8, sfx="ding"),
        L("형사 처벌은 따로라서 특수협박이면 징역까지도 감.", 9, em=["특수협박"], em_color="yellow"),
        L("당하면 맞대응하지 말고 블박 영상 들고 신고하는 게 제일 셈.", 10),
        L("님들은 보복운전 면허 취소해야 한다고 봄?", 4), OUT],
    prompts={
        1: "an aggressive black SUV cutting sharply in front of a sedan on a Korean highway, view from the sedan, daytime",
        2: "a car brake-checking a following car on a highway, red brake lights close-up, daytime",
        3: "a stack of case files on a prosecutor's office desk, text blurred and unreadable, soft light",
        4: "close-up of a driver's license card on a desk next to a red stamp, text blurred and unreadable",
        5: "a bar chart printed on paper on a desk with a pen, numbers blurred, no readable text",
        6: f"{M2} sitting at a police station desk looking frustrated, daytime",
        7: f"{M2} driving again calmly on a city road, view from passenger seat, daytime",
        8: "the Korean National Assembly building exterior on a clear day, wide shot",
        9: "a judge's gavel on a wooden desk with a toy car, soft light",
        10: f"{W1} handing a small memory card to a police officer at a station counter, daytime",
    })

# ── 6. 급발진 주장 73%는 페달 ────────────────────────────────
eps["pedalmiss"] = dict(
    src="아시아경제 2026-09-23 '[단독]급발진 의심 사고 예방장치 2528대 보급…효과 검증은 아직' (view.asiae.co.kr/article/2026092308490378305) ; 농민신문 2026-01-19 '급발진 주장 사고 알고보니 73% 페달 오조작' (nongmin.com/article/20260119500460) — 60대 이상 75.2%",
    t1="급발진이라고 했는데", t2="10건 중 7건은 페달", bar="급발진이라 주장한 사고, 감정해 보니 대부분 페달", cnt=None,
    title="#급발진 73% 페달", shop="페달 블랙박스, 차량용 블랙박스 2채널",
    desc=["급발진이라고 주장한 사고를 감정해 보니 73%가 페달 오조작.",
          "운전자 4명 중 3명은 60대 이상.",
          "정부가 택시에 페달 오조작 방지장치 2528대를 달았는데 효과는 아직 모름."],
    tags="#shorts #급발진 #페달오조작 #페달블랙박스 #고령운전자",
    comment="님들은 페달 블랙박스 달 생각 있음?",
    proof=[("급발진 주장 사고 73% 페달 오조작, 60대 이상 75.2%", "농민신문 2026-01-19"),
           ("페달 오조작 방지장치 2528대 장착(목표 3260대, 77%)", "아시아경제 2026-09-23"),
           ("개인택시 2005·법인택시 680·소형화물 3대, 예산 8억8천만 원", "아시아경제 2026-09-23"),
           ("작동 데이터는 설치업체만 보유, 효과 지표 12월 개발 예정", "아시아경제 2026-09-23")],
    lines=[
        L("급발진이라고 주장한 사고, 감정해 보니 10건 중 7건은 페달이었음.", 1),
        L("지난해 급발진 주장 사고를 분석했더니 73%가 페달 오조작으로 나옴.", 2, sfx="dudung", shake=False, em=["73%"], em_color="yellow"),
        L("브레이크라고 생각하고 액셀을 꾹 밟은 거임.", 3, em=["액셀"], em_color="yellow"),
        L("운전자 4명 중 3명은 60대 이상이었음.", 4, sfx="whoosh"),
        L("그래서 정부가 택시랑 소형 화물차에 페달 오조작 방지장치를 달아줬음.", 5),
        L("저속에서 액셀을 갑자기 세게 밟으면 차가 출력을 막는 장치임.", 6, sfx="ding", em=["출력을 막는"]),
        L("올해 9월까지 2528대에 달았는데, 효과가 있는지는 아직 아무도 모름.", 7, sfx="pop", em=["아무도 모름"], em_color="yellow"),
        L("작동 기록을 설치 업체만 갖고 있고 정부는 데이터가 없다고 함.", 8),
        L("억울한 급발진이면 그걸 증명해 줄 게 페달 블랙박스뿐임.", 9, em=["페달 블랙박스"]),
        L("내 발이 뭘 밟았는지 찍혀 있어야 나중에 다툴 수 있음.", 10),
        L("님들은 페달 블랙박스 달 생각 있음?", 9), OUT],
    prompts={
        1: "a car that crashed into a storefront glass wall, front end inside the shop, Korean street, daytime",
        2: "an investigator in a work uniform examining the driver footwell of a crashed car with a flashlight",
        3: "close-up of a driver's foot in a shoe pressing the accelerator pedal hard, car interior footwell",
        4: "an elderly Korean man gripping a steering wheel tightly with a tense face, daytime, side view",
        5: "a row of taxis parked at a Korean taxi depot, daytime, no signage",
        6: "close-up of a small electronic module installed under a car dashboard near the pedals, wires",
        7: "a technician installing a device under a taxi dashboard, close-up of hands, daytime",
        8: "a laptop on an office desk showing an unreadable data chart, screen content blurred",
        9: "a small camera mounted in a car footwell pointing at the pedals, close-up",
        10: "a video playback on a tablet showing a foot on pedals, screen blurred, held in hands",
    })

# ── 7. 테슬라 FSD 국내 6천 대 ─────────────────────────────────
eps["fsd6000"] = dict(
    src="세계일보 2026-10-06 '[단독] 테슬라 FSD 국내 6000대… 정부 차원 안전성 시험은 전무' (v.daum.net/v/20261006171618363) ; 블로터·스트레이트뉴스 등 국감 보도 — 9월 기준 FSD 사용 5898대(라이트 1만6198대), 서비스센터 입고 사고 2건(3.9km/h 벽 측면 697만 원·2km/h 전방 3만 원), 국토부 안전성 시험 0건(한미 FTA·FMVSS 인증)",
    t1="국내에서 자율주행", t2="6천 대가 달리는데", bar="테슬라 FSD 국내 6천 대 달리는데 정부 시험은 0건", cnt=None,
    title="#FSD 국내 6천대", shop="차량용 블랙박스 2채널, 차량용 휴대폰 거치대",
    desc=["테슬라 FSD를 켜고 국내 도로를 달리는 차가 벌써 약 6천 대.",
          "FSD 켠 상태로 난 사고 2건, 수리비 최대 697만 원.",
          "그런데 국토부 차원의 안전성 시험은 한 번도 없었음."],
    tags="#shorts #테슬라 #FSD #자율주행 #국정감사",
    comment="님들은 FSD 켜고 국내 도로 달릴 수 있음?",
    proof=[("FSD 사용 5898대, 라이트 1만6198대(9월 기준)", "세계일보 2026-10-06"),
           ("FSD 사고 2건: 3.9km/h 벽 측면 697만 원, 2km/h 전방 3만 원", "세계일보·블로터 보도"),
           ("국토부 안전성 시험 0건, 한미 FTA·FMVSS 인증 이유", "세계일보 2026-10-06")],
    lines=[
        L("테슬라 자율주행 FSD를 켜고 국내 도로를 달리는 차가 벌써 6천 대 가까이 됨.", 1),
        L("9월 기준으로 5898대가 쓰고 있다고 국정감사에서 나왔음.", 2, sfx="whoosh", em=["5898대"], em_color="yellow"),
        L("FSD 켠 채로 난 사고도 2건 확인됐음.", 3, sfx="dudung", shake=False),
        L("하나는 시속 3.9km로 가다 벽에 옆을 긁었는데 수리비가 697만 원.", 4, em=["697만 원"], em_color="yellow"),
        L("다른 하나는 운전자가 액셀을 밟은 상태로 시속 2km에 앞을 박음.", 5),
        L("다행히 둘 다 저속 접촉이었음.", 6),
        L("근데 문제는 정부가 이 기능을 한 번도 직접 시험한 적이 없다는 거임.", 7, sfx="pop", em=["한 번도"], em_color="yellow"),
        L("미국 안전기준 인증을 받고 FTA로 들어와서 따로 시험을 안 했다는 설명임.", 8, em=["FTA"]),
        L("그리고 FSD는 여전히 운전자가 계속 보고 있어야 하는 기능이라, 사고 책임도 운전자임.", 9, sfx="ding", em=["운전자"], em_color="yellow"),
        L("켜놓고 딴짓하면 그 책임은 다 내가 지는 거임.", 10),
        L("님들은 FSD 켜고 국내 도로 달릴 수 있음?", 1), OUT],
    prompts={
        1: "a white electric sedan driving on a Seoul city road with the driver's hands hovering off the steering wheel, interior view, daytime",
        2: "rows of white and gray electric sedans parked in a Korean apartment parking garage, no logos",
        3: "an electric sedan in a service center bay with a scraped side panel, workshop lighting",
        4: "close-up of a long scrape along the side of a white electric car door against a concrete wall, parking garage",
        5: "a white electric sedan with a slightly dented front bumper touching another car's rear in a parking lot",
        6: "two cars stopped close together in an underground parking garage after a light bump, no damage visible",
        7: "a government office meeting room with documents on a table, text blurred, soft light",
        8: "cargo ships with car carriers at a Korean port, wide shot, daytime",
        9: f"{M1} holding the steering wheel of an electric car while watching the road attentively, daytime",
        10: f"{M1} looking down at his smartphone while driving, dangerous, view from passenger seat, daytime",
    })

# ── 8. 깨우자 순찰차 박은 만취 ────────────────────────────────
eps["drunkwake"] = dict(
    src="SBS 2026-10-09 '술취한 채 도로 위 차에서 잠든 40대…깨우자 순찰차 들이받기도' (news.sbs.co.kr/news/endPage.do?news_id=N1008788134) ; 대전일보 동일 보도 — 10/8 23:40 대전 대덕구, '경적 울려도 반응 없다' 신고, 깨우자 가속해 순찰차·구조물 충돌, 면허취소 수준 ; 도로교통법 148조의2 3항(0.08~0.2% 1~2년 징역 또는 500만~1천만 원 벌금)",
    t1="도로 한복판에서", t2="자던 운전자 깨웠더니", bar="도로 한복판에 차 세우고 자던 운전자, 깨우자 순찰차 박음", cnt=None,
    title="#깨우자 순찰차 쾅", shop="개인용 음주측정기, 차량용 블랙박스 2채널",
    desc=["도로 한복판에 멈춘 차, 경적을 울려도 반응이 없다는 신고.",
          "경찰이 가서 깨우자 갑자기 액셀을 밟아 순찰차와 건물을 들이받음.",
          "혈중알코올은 면허 취소 수준."],
    tags="#shorts #음주운전 #순찰차 #만취 #경찰",
    comment="님들은 이거 왜 갑자기 밟았다고 봄?",
    proof=[("10/8 오후 11시 40분 대전 대덕구, 도로 위 정차 차량 경적에도 무반응 신고", "SBS 2026-10-09"),
           ("깨우자 급가속해 순찰차·구조물 충돌, 운전자만 부상", "SBS 2026-10-09"),
           ("혈중알코올 면허취소 수준, 도로교통법 위반 입건", "SBS·대전일보 보도"),
           ("0.08~0.2% 1~2년 징역 또는 500만~1천만 원 벌금", "도로교통법 148조의2 3항")],
    lines=[
        L("도로 한복판에 차 세우고 자던 운전자, 깨웠더니 순찰차를 박음.", 1),
        L("밤 11시 40분쯤 대전, 도로에 차가 서 있는데 경적을 울려도 반응이 없다는 신고가 들어옴.", 2, sfx="whoosh"),
        L("경찰이 가 보니 40대 남성이 운전석에서 자고 있었음.", 3),
        L("깨우는 순간 갑자기 액셀을 콱 밟아버림.", 4, sfx="dudung", shake=False, em=["액셀"], em_color="yellow"),
        L("바로 앞 순찰차를 들이받고 옆 건물 구조물까지 박고서야 멈춤.", 5, sfx="pop", em=["순찰차"]),
        L("다친 사람은 다행히 운전자 본인뿐이었음.", 6),
        L("측정해 보니 혈중알코올이 면허 취소 수준이었음.", 7, em=["면허 취소"], em_color="yellow"),
        L("차를 도로에 세우고 잤어도 거기까지 술 먹고 몰고 온 거라 음주운전임.", 8, sfx="ding"),
        L("0.08%가 넘으면 1년에서 2년 징역이나 500만에서 천만 원 벌금임.", 9, em=["천만 원"], em_color="yellow"),
        L("술 마셨으면 차 근처에도 가지 말고 대리를 부르셈.", 10),
        L("님들은 이거 왜 갑자기 밟았다고 봄?", 4), OUT],
    prompts={
        1: "a sedan crashed into the front of a police patrol car on a city road at night, flashing lights, debris",
        2: "a car stopped in the middle of a lane on an empty city road at night with hazard lights off, street lights",
        3: f"{M5} slumped asleep in the driver seat with his head against the window, night, viewed from outside",
        4: "close-up of a foot slamming the accelerator pedal in a dark car footwell, motion blur",
        5: "a police patrol car with a crushed side after being hit by a sedan, night, flashing lights",
        6: "paramedics helping a man out of a car at night, back view, flashing lights",
        7: f"{POL} holding a breathalyzer near a man standing by a car at night",
        8: "a soju bottle and a car key on a bar table at night, warm light",
        9: "a judge's gavel on a desk next to a car key, soft light",
        10: "a designated driver in a vest getting into a car while the owner sits in the passenger seat, night, Korean city",
    })

# ── 9. 전기차 결함 신고 3.6배 ─────────────────────────────────
eps["evdefect"] = dict(
    src="국민일보 2026-09-30 '[단독] 성장통 겪나… 결함 신고 5년여간 5462건' (kmib.co.kr/article/view.asp?arcid=9000018788) — 한국교통안전공단 국토위 제출자료: 2021~2026.8 전기차 결함 신고 5462건, 2021 428→2025 1525건(3.6배), 같은 기간 신규 등록 2.2배, 2026 1~8월 716건 ; 자동차리콜센터 car.go.kr 결함 신고",
    t1="전기차 결함 신고", t2="5년 새 3.6배", bar="전기차 늘어난 것보다 결함 신고가 더 빨리 늘었음", cnt=None,
    title="#전기차 결함 3.6배", shop="차량용 블랙박스 2채널, 차량용 소화기",
    desc=["전기차 결함 신고가 5년여 동안 5462건.",
          "신규 등록은 2.2배 늘었는데 결함 신고는 3.6배 늘었음.",
          "내 차 결함 의심될 때 신고하는 곳."],
    tags="#shorts #전기차 #결함신고 #리콜 #자동차리콜센터",
    comment="님들 전기차 타면서 이상한 증상 있었음?",
    proof=[("2021~2026.8 전기차 결함 신고 5462건", "교통안전공단 자료, 국민일보 2026-09-30"),
           ("2021 428건→2025 1525건(3.6배), 신규 등록 2.2배", "국민일보 2026-09-30"),
           ("2026년 1~8월 716건, 중복·동일부품 반복 신고 포함", "국민일보 2026-09-30")],
    lines=[
        L("전기차가 늘어난 속도보다 결함 신고가 더 빨리 늘었음.", 1),
        L("최근 5년여 동안 전기차 결함 신고가 5462건 들어왔음.", 2, sfx="whoosh", em=["5462건"], em_color="yellow"),
        L("2021년엔 428건이었는데 작년엔 1525건.", 3, sfx="dudung", shake=False, em=["1525건"]),
        L("같은 기간 새로 등록된 전기차는 2.2배 늘었는데 신고는 3.6배 늘어난 거임.", 4, em=["3.6배"], em_color="yellow"),
        L("올해도 8월까지 벌써 716건이 들어왔음.", 5),
        L("물론 같은 부품을 여러 번 신고한 것도 섞여 있다고 함.", 6, sfx="pop"),
        L("그래도 신고가 쌓여야 정부가 조사하고 리콜로 이어짐.", 7, sfx="ding", em=["리콜"], em_color="yellow"),
        L("내 차에 이상한 증상이 있으면 자동차리콜센터 홈페이지에서 결함 신고를 할 수 있음.", 8, em=["자동차리콜센터"]),
        L("증상 나올 때 영상이랑 경고등 사진을 찍어두면 훨씬 잘 받아들여짐.", 9),
        L("내 차가 이미 리콜 대상인지도 차 번호만 넣으면 바로 조회됨.", 10),
        L("님들 전기차 타면서 이상한 증상 있었음?", 1), OUT],
    prompts={
        1: "an electric car parked at a service center with its hood open and a technician with a diagnostic tablet, workshop lighting",
        2: "rows of new electric cars parked at a vehicle export lot in Korea, wide shot, daytime",
        3: "a stack of complaint forms on an office desk, text blurred and unreadable, soft light",
        4: "an electric car charging at a Korean apartment parking garage charger at night, cable plugged in",
        5: f"{M1} frowning at a warning light on an electric car dashboard, interior, daytime",
        6: "close-up of car parts laid out on a workbench in a repair shop, workshop light",
        7: "a line of cars entering a service center for recall repairs, daytime",
        8: f"{M1} filling out an online form on a laptop at home, screen content blurred, evening",
        9: f"{M1} taking a photo of his car dashboard with a smartphone, screen blurred, daytime",
        10: "a smartphone on a car seat showing a vehicle lookup screen, content blurred and unreadable",
    })

# ── 10. 조폭 낀 고의사고 보험사기 ─────────────────────────────
eps["insurfraud"] = dict(
    src="머니투데이 2026-10-02 '전남경찰청, MZ조폭 연루된 보험사기 일당 11명 검거' (mt.co.kr/policy/2026/10/02/2026100209410748200) ; 뉴스핌 2026-10-02 — 2021.4~2025.10 차선 위반 차량 노려 고의사고 11차례, 약 8천만 원, 11명 불구속 송치, 국과수·도로교통공단 감정 ; 보험사기방지특별법 8조(10년 이하 징역 또는 5천만 원 이하 벌금)",
    t1="차선 잘못 바꾸면", t2="일부러 박는 사람들", bar="차선 위반한 차만 골라서 일부러 박은 일당", cnt=None,
    title="#고의사고 보험사기", shop="차량용 블랙박스 2채널, 후방 블랙박스",
    desc=["차선을 잘못 바꾸는 차만 골라 일부러 들이받은 보험사기 일당 11명.",
          "4년 반 동안 11번 사고 내고 보험금 약 8천만 원.",
          "고의사고 표적이 안 되는 법."],
    tags="#shorts #보험사기 #고의사고 #블랙박스 #교통사고",
    comment="님들은 사고 나고 고의 같았던 적 있음?",
    proof=[("목포 지역 조직원 포함 11명, 2021.4~2025.10 고의사고 11차례", "머니투데이 2026-10-02"),
           ("차선 위반 차량 골라 충돌, 상해 과장 입원, 약 8천만 원 편취", "머니투데이·뉴스핌 2026-10-02"),
           ("국과수·도로교통공단 감정, 보험금 분배 계좌 분석, 불구속 송치", "머니투데이 2026-10-02"),
           ("보험사기 10년 이하 징역 또는 5천만 원 이하 벌금", "보험사기방지특별법 8조")],
    lines=[
        L("차선 잘못 바꾸는 차만 골라서 일부러 박은 사람들이 잡혔음.", 1),
        L("전남 목포 지역 조직원이 낀 일당 11명 얘기임.", 2, sfx="whoosh", em=["11명"], em_color="yellow"),
        L("역할을 나눠서 운전하고 동승하다가 차선 위반한 차가 보이면 그대로 들이받았음.", 3, sfx="dudung", shake=False, em=["차선 위반"], em_color="yellow"),
        L("상대가 법규를 어겼으니 과실을 크게 물릴 수 있다는 걸 노린 거임.", 4),
        L("그렇게 4년 반 동안 11번 사고를 냄.", 5, sfx="pop"),
        L("다친 걸 부풀려서 입원까지 하고 보험금 약 8천만 원을 받아 챙김.", 6, em=["8천만 원"], em_color="yellow"),
        L("경찰은 사고 감정이랑 돈 나눈 계좌까지 뒤져서 11명을 넘겼음.", 7, sfx="ding"),
        L("보험사기는 10년 이하 징역이나 5천만 원 이하 벌금임.", 8, em=["10년 이하"]),
        L("표적이 안 되려면 실선에서 차선 바꾸지 말고 깜빡이부터 켜야 함.", 9, em=["깜빡이"], em_color="yellow"),
        L("사고가 이상하다 싶으면 블박 영상 지키고 보험사에 고의 의심이라고 꼭 말하셈.", 10),
        L("님들은 사고 나고 고의 같았던 적 있음?", 3), OUT],
    prompts={
        1: "a sedan deliberately bumping into the side of another car changing lanes on a Korean city road, daytime, motion",
        2: "a group of young Korean men in dark clothes standing around a parked car at night, faces in shadow, back view",
        3: "view from a following car of a car crossing a solid lane line while another car speeds up beside it, daytime",
        4: "two cars stopped after a side collision on a city road with drivers arguing, daytime",
        5: "a wall calendar with several dates circled, no readable text, soft light",
        6: "a man lying in a hospital bed with a neck brace scrolling his phone, back view, soft light",
        7: "police investigators examining bank statements and a laptop at an office desk, documents blurred",
        8: "a judge's gavel on a desk next to an insurance document, text blurred and unreadable",
        9: "close-up of a car side with the turn signal blinking amber before changing lanes, daytime",
        10: "a dashcam on a windshield recording a city intersection, daytime",
    })


def upload_md(s, e):
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    return (f"# {s} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n" + "\n".join(e["desc"]) +
            f"\n{e['tags']}\n\n## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop'] or '차량용 블랙박스 2채널, 차량용 휴대폰 거치대'}\n\n"
            f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")


for s, e in eps.items():
    os.makedirs(s, exist_ok=True)
    assert len(e["title"]) <= 12, (s, e["title"], len(e["title"]))
    sc = {"slug": s, "type": "란빵 자동차, 사고 이슈", "source": e["src"], "title_line1": e["t1"], "title_line2": e["t2"],
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
