#!/usr/bin/env python3
"""란빵 2026-10-09 배치 B 10편 — 운전 상식·교통법 (원글 없음, 법령·공단·제조사 안내 근거).
fireext·petlap·leafslip·blackice·license30·lightcar30·uturn6·doublepark·parkdrain·smartkey
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
POL = "a Korean traffic police officer in a reflective yellow vest"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
eps = {}

# ── 1. 차량용 소화기 의무 ──────────────────────────────────
eps["fireext"] = dict(
    src="소방시설 설치 및 관리에 관한 법률 11조(2024.12.1 시행: 5인승 이상 승용차 차량용 소화기 비치 의무), 2024.12.1 이후 제작·수입·판매 또는 소유권 이전 등록 차량부터 적용(소급 없음) ; '자동차 겸용' 표시 소화기 (서울시 미디어허브 mediahub.seoul.go.kr/archives/2015996, 경기도 소방 안내)",
    t1="내 차에 이거", t2="없으면 법 위반?", bar="중고차 샀는데 소화기 없으면 안 된다고 함", cnt=None,
    title="#차량용 소화기 의무", shop="차량용 소화기, 차량용 소화기 거치대",
    desc=["2024년 12월부터 5인승 이상 승용차도 차량용 소화기가 의무.",
          "새 차뿐 아니라 이후 명의 이전한 중고차도 해당.",
          "집에 있는 소화기 말고 '자동차 겸용' 표시가 있어야 함."],
    tags="#shorts #차량용소화기 #소화기의무 #운전상식 #중고차",
    comment="님들 차에 소화기 있음?",
    proof=[("2024.12.1부터 5인승 이상 승용차 소화기 비치 의무", "소방시설법 11조·서울시 안내"),
           ("이후 제작·판매·소유권 이전 등록 차량부터, 소급 없음", "서울시 미디어허브 안내"),
           ("'자동차 겸용' 표시 소화기", "소방청·지자체 안내")],
    lines=[
        L("중고차 샀는데 소화기 없으면 안 된다고 함.", 1),
        L("예전엔 7인승 이상만 소화기가 의무였음.", 2, sfx="whoosh"),
        L("근데 2024년 12월부터 5인승 승용차까지 넓어졌음.", 3, sfx="dudung", shake=False, em=["5인승"], em_color="yellow"),
        L("그날 이후에 새로 나온 차나, 중고로 명의를 넘겨받은 차가 대상임.", 4, em=["명의"]),
        L("그 전에 산 차는 소급 안 됨, 그래도 하나 있으면 든든함.", 5),
        L("여기서 중요한 게 아무 소화기나 넣으면 안 됨.", 6, sfx="pop"),
        L("집에서 쓰는 소화기는 차 안 열기랑 진동을 못 버틸 수 있음.", 7),
        L("통에 '자동차 겸용'이라고 적힌 걸 사야 함.", 8, sfx="ding", em=["자동차 겸용"], em_color="yellow"),
        L("트렁크 깊숙이 말고 운전석에서 손 닿는 데 둬야 쓸 수 있음.", 9, em=["손 닿는 데"]),
        L("차에 불 나면 몇 분 만에 번지니까, 이건 진짜 보험임.", 10),
        L("님들 차에 소화기 있음?", 1), OUT],
    prompts={
        1: f"{M1} standing at a used car lot next to a sedan, looking surprised while a salesman points inside the car, daytime",
        2: "a large seven-seat van parked in a parking lot with its side door open, daytime",
        3: "a compact red car fire extinguisher lying on the floor mat of a five-seat sedan, close-up, no readable text",
        4: "two people exchanging car keys and documents at a used car dealership desk, paper text blurred and unreadable",
        5: "an older silver sedan parked in a Korean apartment parking lot, daytime",
        6: f"{M1} holding a large household fire extinguisher and looking at his car trunk, puzzled, daytime",
        7: "interior of a car parked under hot summer sun with heat haze on the dashboard",
        8: "close-up of a small car fire extinguisher with a gauge, label text blurred and unreadable, soft light",
        9: "a small fire extinguisher mounted in a bracket under the driver seat of a car, close-up",
        10: "smoke rising from the hood of a car stopped on a roadside, firefighter arriving, daytime",
    })

# ── 2. 반려견 안고 운전 ────────────────────────────────────
eps["petlap"] = dict(
    src="도로교통법 39조 5항(동물을 안고 운전하거나 운전석 주위에 안전 지장 우려 상태로 두고 운전 금지), 범칙금 승용 4만 원·승합 5만 원·이륜 3만 원(시행령 별표8) ; 이동장·반려동물 카시트 뒷좌석 고정 권장",
    t1="강아지 안고", t2="운전하면 4만 원", bar="강아지 무릎에 앉히고 운전하다 단속됨", cnt=None,
    title="#강아지 안고 운전", shop="강아지 카시트, 반려동물 이동장",
    desc=["강아지를 무릎에 앉히거나 안고 운전하면 범칙금 대상.",
          "도로교통법 39조 5항, 승용차 범칙금 4만 원.",
          "반려동물 태울 땐 이동장이나 카시트를 뒷좌석에."],
    tags="#shorts #반려견 #강아지 #운전상식 #교통법규",
    comment="님들은 강아지 차에 태울 때 어떻게 함?",
    proof=[("동물을 안고 운전 금지", "도로교통법 39조 5항"),
           ("범칙금 승용 4만 원·승합 5만 원", "도로교통법 시행령 별표8")],
    lines=[
        L("강아지 무릎에 앉히고 운전하다 단속됨.", 1),
        L("창밖 보는 거 좋아해서 운전석 창문 쪽에 안고 다녔음.", 2, sfx="whoosh"),
        L("근데 이거 법으로 금지된 거임.", 3, sfx="dudung", shake=False, em=["금지"], em_color="yellow"),
        L("도로교통법은 동물을 안고 운전하는 걸 막아둠.", 4, em=["안고 운전"]),
        L("걸리면 승용차 범칙금 4만 원.", 5, sfx="pop", em=["4만 원"], em_color="yellow"),
        L("강아지가 갑자기 움직이면 핸들이 꺾이거나 브레이크 밑으로 들어갈 수 있음.", 6),
        L("에어백 터지면 무릎 위 강아지가 제일 크게 다침.", 7, em=["에어백"], em_color="yellow"),
        L("그래서 정답은 이동장이나 강아지 카시트.", 8, sfx="ding"),
        L("뒷좌석에 놓고 안전벨트나 고리로 고정하면 됨.", 9, em=["뒷좌석"]),
        L("창문 밖으로 머리 내미는 것도 돌 튀면 위험하니까 조금만 열어두기.", 10),
        L("님들은 강아지 차에 태울 때 어떻게 함?", 1), OUT],
    prompts={
        1: f"{W1} driving a car with a small white dog sitting on her lap, view from passenger seat, daytime",
        2: "a small dog sticking its head near the driver side window of a moving car, daytime",
        3: f"{POL} stopping a car at a roadside checkpoint and looking through the driver window, daytime",
        4: "close-up of a small dog's paws resting on a car steering wheel, daytime",
        5: "a traffic ticket slip on a car dashboard, text blurred and unreadable",
        6: "close-up of a small dog near the brake pedal area of a car footwell, daytime",
        7: "a deployed white airbag inside a car after a minor collision, close-up",
        8: "a small dog sitting calmly in a pet car seat booster on the back seat of a car, daytime",
        9: "close-up of a pet carrier strapped with a seat belt on a car back seat",
        10: "a happy dog looking out of a slightly open rear car window on a sunny day",
    })

# ── 3. 젖은 낙엽길 ─────────────────────────────────────────
eps["leafslip"] = dict(
    src="가을철 낙엽 노면 미끄럼 주의(한국도로교통공단·지자체 가을철 안전운전 안내: 젖은 낙엽은 빗길처럼 미끄럽고 제동거리 증가) ; 낙엽 밑 배수구·차선 가림 — 수치 미사용",
    t1="가을에 제일", t2="미끄러운 길", bar="낙엽 쌓인 길에서 브레이크 밟았는데 차가 밀림", cnt=None,
    title="#낙엽길 미끄럼", shop="차량용 블랙박스 2채널, 타이어 트레드 게이지",
    desc=["가을 낙엽, 특히 비 온 뒤 젖은 낙엽은 빗길만큼 미끄러움.",
          "커브와 내리막 낙엽 구간은 미리 속도를 줄여야 함.",
          "낙엽 쌓인 차선·과속방지턱도 조심."],
    tags="#shorts #낙엽 #가을운전 #운전상식 #미끄럼",
    comment="님들 동네도 낙엽 많이 쌓임?",
    proof=[("젖은 낙엽 노면은 미끄러워 제동거리 증가", "도로교통공단·지자체 가을철 안전운전 안내"),
           ("커브·내리막 사전 감속", "도로교통공단 안전운전 안내")],
    lines=[
        L("낙엽 쌓인 길에서 브레이크 밟았는데 차가 쭉 밀림.", 1),
        L("가을 단풍길 예쁘다고 그냥 달리면 이렇게 됨.", 2, sfx="whoosh"),
        L("낙엽이 비나 이슬에 젖으면 빗길처럼 미끄러워짐.", 3, sfx="dudung", shake=False, em=["빗길처럼"], em_color="yellow"),
        L("잎이 타이어랑 바닥 사이에 끼어서 바퀴가 땅을 못 잡는 거임.", 4),
        L("마른 낙엽도 아래쪽은 축축한 경우가 많음.", 5, em=["아래쪽"]),
        L("특히 커브랑 내리막 낙엽 구간이 제일 위험함.", 6, sfx="pop", em=["커브"], em_color="yellow"),
        L("그리고 낙엽이 차선이랑 과속방지턱을 가려서 잘 안 보임.", 7),
        L("그래서 낙엽 보이면 들어가기 전에 미리 속도를 줄여야 함.", 8, sfx="ding", em=["미리"], em_color="yellow"),
        L("낙엽 위에서 급브레이크, 급핸들은 절대 금지.", 9),
        L("타이어 홈이 닳았으면 더 미끄러우니 가을에 한 번 확인하기.", 10),
        L("님들 동네도 낙엽 많이 쌓임?", 2), OUT],
    prompts={
        1: "a car sliding slightly on a road covered with wet fallen autumn leaves, motion blur, overcast",
        2: "a scenic Korean mountain road lined with red and yellow autumn trees, car driving, daytime",
        3: "close-up of wet fallen leaves stuck flat on asphalt after rain, glossy surface",
        4: "close-up of a car tire rolling over a pile of wet yellow ginkgo leaves",
        5: "a pile of dry brown leaves on a roadside with damp dark leaves underneath, close-up",
        6: "a downhill curve on a Korean mountain road covered with fallen leaves, autumn",
        7: "a speed bump and lane markings half covered by fallen leaves on a residential road, autumn",
        8: f"{M2} driving carefully on an autumn road covered with leaves, view from passenger seat",
        9: "close-up of a foot pressing a brake pedal gently, car interior footwell",
        10: "close-up of a worn car tire tread with fallen leaves around it, autumn",
    })

# ── 4. 다리 위 블랙아이스 ──────────────────────────────────
eps["blackice"] = dict(
    src="교량은 아래로 바람이 통하고 지열 영향이 적어 같은 기온에서도 노면이 더 빨리 식고 결빙이 오래감(위키트리·경향신문 2025.12 블랙아이스 보도, 도로공사 안내) ; 블랙아이스 사고 치사율 일반 사고보다 높음(뉴시스 2024.1.3 '치사율 1.5배') ; 교량·터널 출입구·그늘진 곳 주의",
    t1="겨울엔 다리 위가", t2="먼저 언다", bar="멀쩡한 길 달리다 다리 위에서 차가 미끄러짐", cnt=None,
    title="#다리 위 블랙아이스", shop="스노우체인, 2채널 블랙박스",
    desc=["겨울 아침, 일반 도로는 멀쩡한데 다리 위만 얼어 있는 이유.",
          "다리는 아래로 찬바람이 지나가고 땅의 열을 못 받아 먼저 얼음.",
          "블랙아이스 조심해야 할 구간과 대처법."],
    tags="#shorts #블랙아이스 #겨울운전 #교량결빙 #운전상식",
    comment="님들도 블랙아이스에서 미끄러져 본 적 있음?",
    proof=[("교량은 지열 영향 적고 바람이 통해 먼저 얼고 오래감", "위키트리·경향신문 블랙아이스 보도"),
           ("블랙아이스 사고 치사율 일반 사고의 약 1.5배", "뉴시스 2024.1.3 보도"),
           ("교량·터널 출입구·그늘 구간 주의", "한국도로공사 겨울철 안전운전 안내")],
    lines=[
        L("멀쩡한 길 달리다가 다리 위에서 차가 미끄러짐.", 1),
        L("다리 들어가기 전까진 아무렇지 않았음.", 2, sfx="whoosh"),
        L("겨울엔 다리 위가 일반 도로보다 먼저 얼음.", 3, sfx="dudung", shake=False, em=["먼저"], em_color="yellow"),
        L("일반 도로는 땅의 열을 받는데 다리는 아래가 비어 있음.", 4, em=["땅의 열"]),
        L("위아래로 찬바람이 지나가서 노면이 훨씬 빨리 식는 거임.", 5),
        L("그렇게 생긴 얇은 얼음이 블랙아이스, 그냥 젖은 길처럼 보임.", 6, sfx="pop", em=["블랙아이스"], em_color="yellow"),
        L("보도에 따르면 블랙아이스 사고는 치사율이 일반 사고의 1.5배 정도라고 함.", 7, em=["1.5배"]),
        L("다리, 터널 출입구, 그늘진 길이 대표 구간임.", 8, sfx="ding", em=["터널 출입구"]),
        L("겨울 새벽엔 다리 들어가기 전에 미리 속도를 줄이고, 브레이크는 살살.", 9),
        L("미끄러지면 핸들 크게 꺾지 말고 가고 싶은 방향만 보기.", 10),
        L("님들도 블랙아이스에서 미끄러져 본 적 있음?", 1), OUT],
    prompts={
        1: "a car skidding sideways on an icy bridge over a river on a cold winter dawn, motion blur",
        2: "a dry road leading onto a bridge on a cold winter morning, frost on guardrails, Korea",
        3: "a long concrete bridge over a Korean river on a freezing winter morning with a thin glossy sheen on the road",
        4: "underside of a highway bridge with open space and a river below, winter, cold blue light",
        5: "cold wind blowing snow dust across a bridge deck, winter morning",
        6: "close-up of a dark asphalt road with a nearly invisible thin layer of clear ice, looks just wet",
        7: "a car crashed into a guardrail on an icy road in winter, emergency lights, early morning",
        8: "a shaded road section next to a tunnel entrance with patches of ice, winter",
        9: f"{M4} driving cautiously with both hands on the wheel on a frosty winter morning, view from passenger seat",
        10: "view from a driver seat looking straight ahead through the windshield on an icy road, winter dawn",
    })

# ── 5. 면허 갱신 과태료 ────────────────────────────────────
eps["license30"] = dict(
    src="도로교통법 87조(정기적성검사·면허증 갱신), 160조 과태료: 갱신 기간 경과 시 1종 3만 원·2종 2만 원 ; 1종 정기적성검사 기간 경과 후 1년 초과 시 면허 취소(93조 1항) ; 만료 면허증은 신분증 효력 없음 ; 온라인(안전운전 통합민원) 갱신 가능",
    t1="면허증 뒷면", t2="날짜 확인해봄?", bar="면허증 기간 지난 줄 모르고 은행 갔다가 퇴짜", cnt=None,
    title="#면허 갱신 과태료", shop="차량용 블랙박스, 차량용 휴대폰 거치대",
    desc=["운전면허증에도 유효기간이 있음, 지나면 과태료.",
          "1종은 3만 원, 2종은 2만 원, 1종은 1년 넘기면 면허 취소까지.",
          "기간 확인하는 법과 온라인 갱신."],
    tags="#shorts #운전면허 #면허갱신 #과태료 #운전상식",
    comment="님들 면허증 갱신 날짜 알고 있음?",
    proof=[("갱신 기간 경과 과태료 1종 3만 원·2종 2만 원", "도로교통법 160조·시행령"),
           ("1종 적성검사 1년 초과 미필 시 면허 취소", "도로교통법 93조 1항"),
           ("만료 면허증은 신분증 효력 없음", "경찰청·도로교통공단 안내")],
    lines=[
        L("면허증 기간 지난 줄 모르고 은행 갔다가 퇴짜 맞음.", 1),
        L("운전면허증에도 유효기간이 있음, 대부분 10년.", 2, sfx="whoosh", em=["유효기간"]),
        L("기간 지나면 신분증으로도 안 받아줌.", 3, sfx="dudung", shake=False, em=["신분증"], em_color="yellow"),
        L("그리고 과태료가 나옴.", 4),
        L("2종은 2만 원, 1종은 3만 원.", 5, sfx="pop", em=["3만 원"], em_color="yellow"),
        L("1종은 더 무서운 게 있음.", 6),
        L("적성검사 기간 지나고 1년을 넘기면 면허가 아예 취소됨.", 7, em=["취소"], em_color="yellow"),
        L("갱신 기간은 면허증 앞면 아래쪽에 적혀 있음.", 8, sfx="ding", em=["앞면 아래쪽"]),
        L("갱신은 경찰서나 면허시험장 말고 온라인으로도 신청 가능함.", 9, em=["온라인"]),
        L("연말엔 시험장 줄이 엄청 기니까 미리 하는 게 이득.", 10),
        L("님들 면허증 갱신 날짜 알고 있음?", 8), OUT],
    prompts={
        1: f"{M1} at a Korean bank counter looking embarrassed while a teller hands back a card, daytime",
        2: "close-up of a plastic ID card in a wallet, text and photo blurred and unreadable",
        3: f"{M1} staring at a card in his hand with a confused face, office lobby",
        4: "a fine notice envelope on a table, text blurred and unreadable",
        5: "Korean 10000 won banknotes laid out on a table, close-up",
        6: "a large truck parked at a logistics yard, daytime",
        7: "a pair of scissors next to a plastic card on a desk, text blurred and unreadable, dramatic light",
        8: "close-up of a finger pointing at the bottom area of a plastic card, text blurred and unreadable",
        9: f"{M1} filling out an online form on a laptop at home, screen content blurred, evening",
        10: "a crowded waiting room at a Korean driver license center with people sitting in rows, daytime",
    })

# ── 6. 경차 혜택 ───────────────────────────────────────────
eps["lightcar30"] = dict(
    src="경차 유류세 환급(1세대 1경차, 휘발유·경유 리터당 250원·LPG 161원, 연 한도 30만 원, 2026.12.31까지 연장, 경차사랑카드) ; 고속도로 통행료 50% 감면(유료도로법 시행령) ; 취득세 감면(지방세특례제한법, 75만 원 한도) (카드고릴라·기재부 안내)",
    t1="경차 사면", t2="연 30만 원 돌려받음", bar="경차 샀는데 기름값 돌려받는 거 모르고 1년 탐", cnt=None,
    title="#경차 기름값 환급", shop="차량용 휴대폰 거치대, 차량용 블랙박스",
    desc=["경차 타면 기름값을 1년에 최대 30만 원 돌려받는 제도가 있음.",
          "휘발유·경유 리터당 250원, 경차사랑카드로 주유해야 적용.",
          "고속도로 통행료 50%, 취득세 감면까지."],
    tags="#shorts #경차 #유류세환급 #경차사랑카드 #운전상식",
    comment="님들은 경차 탈 의향 있음?",
    proof=[("유류세 환급 리터당 250원(LPG 161원), 연 30만 원 한도", "기재부 경차 유류세 환급 안내"),
           ("2026년 12월 31일까지 연장", "카드고릴라 2026 경차사랑카드 정리"),
           ("1세대 1경차 원칙", "기재부 안내"),
           ("고속도로 통행료 50%, 취득세 75만 원까지 감면", "유료도로법 시행령·지방세특례제한법")],
    lines=[
        L("경차 샀는데 기름값 돌려받는 거 모르고 1년을 그냥 탐.", 1),
        L("경차는 기름 넣을 때마다 세금 일부를 돌려줌.", 2, sfx="whoosh", em=["돌려줌"], em_color="yellow"),
        L("휘발유랑 경유는 리터당 250원.", 3, sfx="dudung", shake=False, em=["250원"], em_color="yellow"),
        L("1년에 최대 30만 원까지 돌려받을 수 있음.", 4, sfx="pop", em=["30만 원"], em_color="yellow"),
        L("대신 경차사랑카드라는 전용 카드로 주유해야 적용됨.", 5, em=["경차사랑카드"]),
        L("그리고 집에 차가 경차 하나여야 하는 1세대 1경차 조건이 있음.", 6),
        L("이 제도는 2026년 말까지 연장돼 있음.", 7),
        L("고속도로 통행료도 절반만 냄.", 8, sfx="ding", em=["절반"]),
        L("차 살 때 취득세도 75만 원까지 깎아줌.", 9),
        L("경차 탄다면 카드부터 만들어야 손해 안 봄.", 10),
        L("님들은 경차 탈 의향 있음?", 1), OUT],
    prompts={
        1: f"{W1} standing next to a small cute compact car in an apartment parking lot, smiling, daytime",
        2: "a small compact car at a Korean gas station being refueled, daytime",
        3: "close-up of a fuel nozzle in a small car fuel tank, daytime",
        4: "Korean 50000 won banknotes fanned out on a car seat, close-up",
        5: f"{W1} handing a plain credit card to a gas station attendant, card face blurred, daytime",
        6: "a single small compact car parked in front of a Korean family house, daytime",
        7: "a calendar on a wall with the last page of the year, no readable text, soft light",
        8: "a small compact car passing through a Korean expressway toll gate, daytime",
        9: "a new small compact car in a dealership showroom under bright lights",
        10: f"{W1} driving a small compact car happily on a city road, view from passenger seat, daytime",
    })

# ── 7. 불법 유턴 ──────────────────────────────────────────
eps["uturn6"] = dict(
    src="도로교통법 18조(횡단 등의 금지)·13조(중앙선 침범), 유턴구역선(흰색 점선)·유턴 허용 신호에서만 ; 불법 유턴 범칙금 승용 6만 원·벌점 30점, 무인카메라 과태료 9만 원 ; 사고 시 중앙선 침범·신호위반은 교통사고처리특례법 3조 2항 12대 중과실 (로톡 '유턴 관련 민·형사상 책임', 겟차 유턴 상식)",
    t1="여기서 유턴하면", t2="벌점 30점", bar="노란 중앙선 넘어서 그냥 유턴함", cnt=None,
    title="#불법유턴 벌점 30", shop="차량용 블랙박스 2채널, 차량용 휴대폰 거치대",
    desc=["유턴 표시 없는 곳에서 중앙선 넘어 유턴하면 범칙금 6만 원·벌점 30점.",
          "유턴은 흰 점선 유턴구역선과 허용 신호에서만.",
          "사고 나면 12대 중과실이라 보험 있어도 형사처벌."],
    tags="#shorts #불법유턴 #중앙선침범 #교통법규 #12대중과실",
    comment="님들 동네에도 불법 유턴 자주 보임?",
    proof=[("불법 유턴 범칙금 승용 6만 원·벌점 30점, 무인 과태료 9만 원", "로톡·겟차 유턴 상식 정리"),
           ("유턴은 흰색 점선 유턴구역선에서", "도로교통법·노면표시 규칙"),
           ("중앙선 침범 사고는 12대 중과실", "교통사고처리특례법 3조 2항")],
    lines=[
        L("차 없길래 노란 중앙선 넘어서 그냥 유턴함.", 1),
        L("유턴 표시까지 가기 귀찮아서 다들 한 번쯤 해봤을 거임.", 2, sfx="whoosh"),
        L("근데 이거 걸리면 꽤 셈.", 3, sfx="dudung", shake=False),
        L("불법 유턴은 범칙금 6만 원에 벌점 30점.", 4, sfx="pop", em=["벌점 30점"], em_color="yellow"),
        L("카메라에 찍히면 과태료 9만 원으로 나옴.", 5, em=["9만 원"]),
        L("유턴은 바닥에 흰 점선이 그려진 곳에서만 할 수 있음.", 6, sfx="ding", em=["흰 점선"], em_color="yellow"),
        L("신호도 봐야 함, 유턴 표지판 밑에 적힌 조건이 있으면 그때만.", 7),
        L("진짜 무서운 건 사고 났을 때임.", 8),
        L("중앙선 침범 사고는 12대 중과실이라 보험 있어도 형사처벌 받을 수 있음.", 9, em=["12대 중과실"], em_color="yellow"),
        L("조금 돌아가도 유턴 구역까지 가는 게 제일 싸게 먹힘.", 10),
        L("님들 동네에도 불법 유턴 자주 보임?", 1), OUT],
    prompts={
        1: "a car making an illegal U-turn across a double yellow center line on a Korean city road, aerial-ish view, daytime",
        2: f"{M2} turning the steering wheel sharply while looking left, view from passenger seat, daytime",
        3: f"{POL} waving a car to pull over on a city road, daytime",
        4: "a traffic ticket and a pen on a police clipboard, text blurred and unreadable",
        5: "a roadside traffic enforcement camera on a pole over a Korean road, daytime",
        6: "close-up of white dashed U-turn lane markings next to a yellow center line on asphalt, daytime",
        7: "a car waiting at a Korean intersection U-turn lane with traffic lights ahead, daytime",
        8: "a side collision between a U-turning car and an oncoming car on a city road, daytime",
        9: "a judge's gavel on a desk next to a toy car, soft light",
        10: "aerial view of a car correctly making a U-turn at a designated U-turn area on a wide Korean road",
    })

# ── 8. 이중주차 기어 N ─────────────────────────────────────
eps["doublepark"] = dict(
    src="아파트·상가 이중주차 관행: 기어 중립(N)·주차 브레이크 해제로 밀 수 있게 두는 것이 통상 매너(관리사무소 안내) ; 전자식 변속기·EPB 차량은 시동 끄면 자동 P·브레이크가 걸리는 차종이 있어 차량 매뉴얼의 'N 유지' 방법 확인 ; 경사로에선 이중주차 피하기 — 수치·법 조항 미사용",
    t1="이중주차할 때", t2="이거 안 하면 민폐", bar="이중주차한 차가 안 밀려서 30분째 못 나감", cnt=None,
    title="#이중주차 기어 N", shop="주차번호판, 차량용 블랙박스",
    desc=["이중주차할 땐 기어 N, 사이드 브레이크 풀어두는 게 기본.",
          "요즘 전자식 기어 차는 시동 끄면 P로 바뀌어서 N 유지법을 따로 알아야 함.",
          "연락처 남기기와 경사로 주의까지."],
    tags="#shorts #이중주차 #주차매너 #운전상식 #아파트주차",
    comment="님들 아파트도 이중주차 많이 함?",
    proof=[("이중주차는 N·주차 브레이크 해제가 통상 매너", "아파트 관리사무소 안내 일반"),
           ("전자식 변속기는 시동 끄면 자동 P 전환, N 유지 방법 별도", "차량 매뉴얼 일반")],
    lines=[
        L("이중주차한 차가 안 밀려서 30분째 못 나감.", 1),
        L("밀어보니 꿈쩍도 안 함, 기어가 P에 걸려 있었음.", 2, sfx="dudung", shake=False, em=["P"], em_color="yellow"),
        L("이중주차할 땐 기어를 N에 두고 사이드 브레이크를 풀어야 함.", 3, sfx="ding", em=["N"], em_color="yellow"),
        L("그래야 앞 차가 손으로 밀고 나갈 수 있음.", 4),
        L("근데 요즘 차는 함정이 있음.", 5, sfx="pop"),
        L("버튼식 기어나 전자식 사이드 브레이크 차는 시동 끄면 자동으로 P가 걸리는 경우가 많음.", 6, em=["자동으로 P"]),
        L("차마다 N으로 두는 방법이 따로 있으니 매뉴얼에서 한 번 확인해야 함.", 7, em=["매뉴얼"], em_color="yellow"),
        L("그리고 앞 유리에 전화번호는 꼭 보이게.", 8),
        L("경사진 곳은 차가 굴러갈 수 있어서 이중주차 자체를 피하는 게 맞음.", 9),
        L("밀 때는 범퍼 말고 차 옆 기둥 쪽을 밀어야 안 찌그러짐.", 10),
        L("님들 아파트도 이중주차 많이 함?", 1), OUT],
    prompts={
        1: "a Korean apartment underground parking garage with a car double-parked in front of parked cars at night",
        2: f"{M2} pushing hard against the side of a double-parked car that won't move, underground parking garage",
        3: "close-up of a car gear lever being moved into neutral position, interior, soft light",
        4: f"{M2} easily pushing a double-parked sedan sideways in a parking garage",
        5: "close-up of a modern car center console with a rotary gear dial and electronic parking brake button, no text",
        6: "close-up of a push-button gear selector in a modern car with P highlighted by light, no readable text",
        7: "a car owner's manual book open on a car seat, pages blurred and unreadable",
        8: "a small phone number parking card on a car dashboard, digits blurred and unreadable",
        9: "a car double-parked on a sloped section of a parking garage ramp, dim lighting",
        10: "close-up of hands pushing on the door pillar of a car, parking garage",
    })

# ── 9. 블박 주차녹화 방전 ──────────────────────────────────
eps["parkdrain"] = dict(
    src="블랙박스 제조사 매뉴얼 일반: 주차녹화는 상시 전원 사용, 저전압 차단(컷오프) 설정·주차녹화 시간 설정으로 배터리 보호, 겨울엔 배터리 성능 저하로 차단 기준을 높게 권장 ; 보조배터리(블랙박스 전용) 대안 — 특정 전압 수치 미사용",
    t1="아침에 시동이", t2="안 걸리는 이유", bar="아침에 시동 안 걸려서 보니 블박이 밤새 켜져 있었음", cnt=None,
    title="#블박 주차녹화 방전", shop="블랙박스 보조배터리, 휴대용 점프스타터",
    desc=["블랙박스 주차녹화가 밤새 배터리를 먹어서 아침에 시동이 안 걸리는 경우.",
          "저전압 차단 설정과 주차녹화 시간만 바꿔도 막을 수 있음.",
          "겨울엔 차단 기준을 높게, 장기 주차는 보조배터리."],
    tags="#shorts #블랙박스 #배터리방전 #주차녹화 #겨울철차관리",
    comment="님들 블박 주차녹화 켜두고 다님?",
    proof=[("주차녹화는 차 배터리를 계속 사용", "블랙박스 제조사 매뉴얼 일반"),
           ("저전압 차단·녹화 시간 설정으로 방전 방지", "블랙박스 제조사 매뉴얼 일반"),
           ("겨울엔 배터리 성능 저하", "배터리 제조사 안내 일반")],
    lines=[
        L("아침에 시동이 안 걸려서 보니 블박이 밤새 켜져 있었음.", 1),
        L("주차녹화는 시동 꺼진 동안 차 배터리로 계속 돌아감.", 2, sfx="whoosh", em=["차 배터리"]),
        L("그래서 오래 세워두면 배터리가 바닥남.", 3, sfx="dudung", shake=False, em=["바닥"], em_color="yellow"),
        L("막는 방법은 블박 설정에 있음.", 4, sfx="ding"),
        L("저전압 차단이라는 메뉴가 있는데, 배터리가 이 밑으로 내려가면 블박이 스스로 꺼짐.", 5, em=["저전압 차단"], em_color="yellow"),
        L("이 기준을 높게 잡아두면 시동 걸 힘은 남겨둠.", 6),
        L("겨울엔 배터리 힘이 약해지니까 기준을 한 단계 더 올리는 게 좋음.", 7, sfx="pop", em=["겨울"]),
        L("주차녹화 시간도 무제한 말고 정해두면 됨.", 8),
        L("며칠씩 세워둘 땐 블박 전용 보조배터리를 다는 게 제일 확실함.", 9, em=["보조배터리"], em_color="yellow"),
        L("한 번 방전되면 배터리 수명도 줄어드니 미리 설정해두기.", 10),
        L("님들 블박 주차녹화 켜두고 다님?", 1), OUT],
    prompts={
        1: f"{M1} in a car on a cold morning pressing the start button with a frustrated face, dashboard dark",
        2: "a dashcam with a small glowing light recording inside a parked car at night in a parking garage",
        3: "close-up of a car battery under the open hood, cold morning light",
        4: f"{M1} adjusting settings on a dashcam mounted behind the rearview mirror, close-up of hands",
        5: "close-up of a dashcam screen showing a settings menu, screen content blurred and unreadable",
        6: "a car engine starting on a frosty morning with headlights turning on, faint exhaust",
        7: "a car covered in frost parked outdoors on a freezing winter morning, Korea",
        8: "a car parked in a dark residential parking lot at night, quiet, single street light",
        9: "a compact auxiliary battery pack box installed under a car seat with a cable, close-up",
        10: "a mechanic testing a car battery with a handheld tester under the hood, workshop",
    })

# ── 10. 스마트키 방전 ──────────────────────────────────────
eps["smartkey"] = dict(
    src="차량 매뉴얼 일반: 스마트키 배터리 방전 시 기계식 비상키로 문 열고, 스마트키를 시동 버튼(또는 지정 위치)에 직접 대고 버튼을 누르면 시동 가능(차종별 위치 상이) ; 스마트키 배터리는 동전형 리튬 전지(차종별 규격 확인) — 수치 미사용",
    t1="스마트키 죽어도", t2="시동 거는 법", bar="스마트키 배터리 나가서 차 앞에서 30분 서 있었음", cnt=None,
    title="#스마트키 방전 시동", shop="스마트키 배터리, 스마트키 케이스",
    desc=["스마트키 배터리가 나가도 차 문 열고 시동 거는 방법이 있음.",
          "키 안에 숨은 비상키로 문 열고, 키를 시동 버튼에 대고 누르기.",
          "배터리 교체는 동전 배터리 하나면 끝."],
    tags="#shorts #스마트키 #배터리방전 #운전상식 #차량관리",
    comment="님들 스마트키 배터리 갈아본 적 있음?",
    proof=[("방전 시 기계식 비상키로 문 열기", "차량 매뉴얼 일반"),
           ("스마트키를 시동 버튼에 대고 누르면 시동(차종별 위치 상이)", "차량 매뉴얼 일반"),
           ("스마트키 배터리는 동전형 리튬 전지", "차량 매뉴얼 일반")],
    lines=[
        L("스마트키 배터리 나가서 차 앞에서 30분 서 있었음.", 1),
        L("버튼 눌러도 문이 안 열리고, 보험사 부르려다 이걸 알게 됨.", 2, sfx="whoosh"),
        L("스마트키 안에 비상용 쇠 열쇠가 숨어 있음.", 3, sfx="ding", em=["쇠 열쇠"], em_color="yellow"),
        L("키 옆 작은 버튼 누르고 당기면 빠지고, 운전석 손잡이 열쇠 구멍에 꽂으면 됨.", 4),
        L("손잡이에 구멍이 안 보이면 작은 덮개 안에 숨어 있는 차가 많음.", 5, em=["덮개"]),
        L("그럼 시동은 어떻게 거냐.", 6, sfx="pop"),
        L("스마트키를 시동 버튼에 직접 대고 버튼을 누르면 걸리는 차가 많음.", 7, em=["시동 버튼에 직접"], em_color="yellow"),
        L("차마다 대는 위치가 다르니 매뉴얼에서 한 번 봐두기.", 8),
        L("배터리는 동전 모양 전지 하나라 마트나 편의점에서도 팔음.", 9, em=["동전 모양"]),
        L("버튼 반응이 느려지면 그게 교체 신호임.", 10, sfx="dudung", shake=False),
        L("님들 스마트키 배터리 갈아본 적 있음?", 1), OUT],
    prompts={
        1: f"{M4} standing next to his car in a parking lot pressing a car key fob repeatedly, frustrated, evening",
        2: f"{M4} looking at his smartphone next to his locked car, about to call, evening",
        3: "close-up of a hand pulling a small metal emergency key out of a black smart key fob, no logos",
        4: "close-up of a metal key being inserted into a car door handle keyhole, evening light",
        5: "close-up of a car door handle with a small removable cap revealing a hidden keyhole",
        6: "close-up of a car engine start stop button glowing in a dark interior, no readable text",
        7: "close-up of a smart key fob held against a car engine start button while a finger presses it",
        8: "a car owner's manual open on a passenger seat, pages blurred and unreadable",
        9: "close-up of a small coin-shaped lithium battery next to an opened car key fob on a table",
        10: f"{M4} pressing a car key fob button while pointing it at a car, slightly annoyed, daytime",
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
