#!/usr/bin/env python3
"""란빵 2026-10-09 배치 A 10편 — 보배드림 베스트 48시간(10/8~10/9) 자동차 글.
taxifare·escalade·hazarddump·g80tower·oilcap·theta2·drunkcop·cornerpark·lanecurve·phonedigit
→ work/<slug>/script.json + prompts.tsv + upload.md
"""
import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "work"))

T = (", photorealistic DSLR photograph, 35mm lens, natural available light, shallow depth of field, "
     "Korean setting, no text no letters no signage no logos no brand marks no watermark, no readable license plates")
M1 = "a Korean man in his early 30s, short black hair, clean-shaven, slim build"
M2 = "a Korean man in his mid 30s, short wavy black hair, light stubble, sturdy build"
W1 = "a Korean woman in her early 30s, shoulder-length dark brown hair, natural light makeup"
W2 = "a Korean woman in her late 50s, short permed hair, padded vest"
M4 = "a Korean man in his late 40s, short graying hair, casual jacket"
M5 = "a Korean man in his early 60s, short gray hair, work jacket, truck driver"
M6 = "a Korean man in his late 40s, short hair, black t-shirt, mechanic"
POL = "a Korean traffic police officer in a reflective yellow vest"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
eps = {}

B = "https://www.bobaedream.co.kr/view?code=best&No="

# ── 1. 차 막혀서 택시비 2만 원 ────────────────────────────────
eps["taxifare"] = dict(
    src=f"{B}1038349 (추천 538, 댓글 134) ; 본문: 40분 동안 전화했는데 안 받아 샵 예약 30분 미루다 택시 왕복, 2만 원 넘게 나온 택시비 요구 ; 첨부: 좁은 골목 담장 쪽 회색 세단 옆을 검정 세단이 막은 사진, 상대 문자 '말투도 안 이뻤어요, 왕복은 못 드려요', '돈 보내라면서요' ; 댓글 상위: '검정 차가 무조건 잘못', '2만원 안 주면 민사'",
    t1="40분 동안 전화했는데", t2="택시비 2만 원 달라 함", bar="내 차 막아놓고 전화도 안 받아서 택시비 청구함", cnt=134,
    title="#차 막고 택시비 거절", shop="차량용 주차번호판, 차량용 블랙박스",
    desc=["좁은 골목에 세워둔 내 차를 다른 차가 막아버림, 40분 동안 전화해도 안 받음.",
          "결국 택시 타고 다녀와서 왕복 택시비 2만 원을 달라고 했더니 돌아온 답.",
          "댓글은 막은 차가 무조건 잘못이라는 반응."],
    tags="#shorts #이중주차 #주차빌런 #택시비 #보배드림",
    comment="님들이면 택시비 달라고 함?",
    proof=[("40분 전화 부재, 예약 30분 미룸, 왕복 택시비 2만 원 넘게 요구", "원글 본문"),
           ("상대 답장: 말투도 안 이뻤다, 왕복은 못 준다, 돈 보내라면서요", "원글 첨부 문자 캡처"),
           ("댓글: 검정 차가 무조건 잘못(추천 135), 안 주면 민사(118)", "원글 댓글")],
    lines=[
        L("내 차 막아놓고 40분 동안 전화를 안 받은 차주가 있음.", 1),
        L("좁은 골목에 세워둔 내 차 옆을 검정 세단이 딱 막아버린 거임.", 2, sfx="whoosh", em=["딱 막아버린"]),
        L("전화를 40분 동안 했는데 계속 안 받음.", 3, sfx="dudung", shake=False, em=["40분"], em_color="yellow"),
        L("예약까지 30분 미루다가 결국 택시 타고 다녀옴.", 4),
        L("왕복 택시비가 2만 원 넘게 나와서 달라고 했더니 답장이 이럼.", 5, sfx="pop"),
        L("말투도 안 예뻤고, 왕복은 못 준다고.", 6, em=["왕복은 못 준다"], em_color="yellow"),
        L("그러면서 운전을 못해서 못 뺀 거 아니냐는 식으로 나옴.", 7),
        L("댓글은 막은 차가 무조건 잘못이라는 반응이 압도적.", 8, sfx="ding", em=["무조건 잘못"]),
        L("안 주면 소액이라도 민사로 받으면 된다는 댓글도 많음.", 9, em=["민사"], em_color="yellow"),
        L("차 댈 땐 연락처 남기고, 전화 오면 받는 게 기본임.", 10),
        L("님들이면 택시비 달라고 함?", 3), OUT],
    prompts={
        1: "a narrow Korean back alley where a black sedan is parked tightly beside a gray sedan, blocking it against a green wire fence, daytime",
        2: "close-up of a gray compact sedan boxed in by a black sedan and a utility pole in a narrow alley, cardboard boxes nearby, daytime",
        3: f"{W1} holding a smartphone to her ear with a frustrated face next to her blocked car in an alley, daytime",
        4: f"{W1} checking her wristwatch anxiously in an alley, daytime",
        5: f"{W1} getting into the back seat of an orange Korean taxi on a city street, daytime",
        6: "close-up of a smartphone screen showing a text message conversation, bubbles blurred and unreadable",
        7: f"{M2} smirking while typing on his smartphone in a cafe, screen content blurred",
        8: "a black sedan parked carelessly across a narrow alley entrance, wide angle, daytime",
        9: "a small claims court building exterior in Korea, daytime, no text",
        10: "a parking contact number card placed on a car dashboard, number blurred and unreadable, close-up",
    })

# ── 2. 에스컬레이드 주차 빌런 ───────────────────────────────
eps["escalade"] = dict(
    src=f"{B}1038185 (추천 564, 댓글 65) ; 본문: 화가 났다고 지하주차장 입구에 주차, 이번엔 경차 주차칸에 주차, 20~30대로 보임, S63과 같이 다님 ; 첨부: 흰색 대형 SUV가 경차 구획(파란 선) 두 칸에 걸쳐 주차된 사진 ; 공동주택 단지 내 주차장은 도로교통법상 도로가 아니어서 경찰 단속이 어렵고 관리규약으로 제재(일반 상식)",
    t1="화났다고 주차장 입구 막더니", t2="이번엔 경차칸", bar="억대 SUV가 아파트 경차칸 두 칸을 차지함", cnt=65,
    title="#SUV 경차칸 주차", shop="차량용 주차번호판, 차량용 블랙박스",
    desc=["억대 대형 SUV가 아파트 지하주차장 경차 전용칸을 차지하고 서 있음.",
          "예전엔 화가 났다고 지하주차장 입구에 세워버린 적도 있다고 함.",
          "아파트 안 주차 빌런을 경찰이 단속하기 어려운 이유."],
    tags="#shorts #주차빌런 #경차칸 #아파트주차 #보배드림",
    comment="님들 아파트에도 이런 차 있음?",
    proof=[("화가 나서 지하주차장 입구에 주차, 이번엔 경차 칸 주차", "원글 본문"),
           ("흰색 대형 SUV가 경차 구획에 걸쳐 주차", "원글 첨부 사진"),
           ("아파트 단지 안은 도로가 아니라 경찰 단속이 어려움", "도로교통법 2조 도로 정의 관련 일반 상식")],
    lines=[
        L("억대 SUV가 아파트 경차 칸을 차지하고 서 있음.", 1),
        L("파란 선 경차 전용 칸에 집채만 한 SUV가 걸쳐 있는 거임.", 2, sfx="whoosh", em=["경차 전용 칸"], em_color="yellow"),
        L("근데 이 차주, 전과가 있었음.", 3, sfx="dudung", shake=False),
        L("예전엔 화가 났다고 지하주차장 입구에 차를 세워버렸다고 함.", 4, em=["입구"], em_color="yellow"),
        L("나이는 20대에서 30대로 보이고, 고성능 세단이랑 같이 몰려다닌다고 함.", 5),
        L("주민들은 무서워서 말도 못 걸겠다고.", 6, sfx="pop"),
        L("문제는 아파트 안은 도로가 아니라서 경찰이 딱지를 떼기 어렵다는 거임.", 7, em=["도로가 아니라서"], em_color="yellow"),
        L("그래서 관리사무소가 관리규약으로 경고장 붙이고 제재하는 수밖에 없음.", 8, sfx="ding", em=["관리규약"]),
        L("댓글은 차가 좋으면 뭐하냐, 사람이 문제라는 반응.", 9),
        L("이런 건 쌓이면 면허 다시 따게 해야 한다는 댓글까지 나옴.", 10),
        L("님들 아파트에도 이런 차 있음?", 2), OUT],
    prompts={
        1: "a huge white full-size luxury SUV parked across a small compact-car parking space with blue lines in a Korean apartment underground garage",
        2: "close-up of blue painted compact-car parking space lines on the floor under the wheels of a huge white SUV, underground garage",
        3: "a dim underground apartment parking garage with fluorescent lights and rows of cars, Korea",
        4: "a large white SUV parked blocking the entrance ramp of an underground parking garage, cars waiting behind, evening",
        5: "a black high-performance luxury sedan and a white full-size SUV parked side by side in an underground garage, moody light",
        6: f"{W2} looking warily at a large SUV in an apartment parking garage, holding shopping bags",
        7: "a Korean apartment complex entrance gate with a parking barrier arm, daytime",
        8: "a warning notice sticker being stuck on a car side window by a hand, notice text blurred and unreadable, garage light",
        9: f"{M4} shaking his head looking at a badly parked SUV in an underground garage",
        10: "close-up of a driver's license card on a table next to car keys, text blurred and unreadable",
    })

# ── 3. 비상등 켠 덤프 후미 추돌 ─────────────────────────────
eps["hazarddump"] = dict(
    src=f"{B}1038302 (추천 385, 댓글 41) ; 보배드림 인스타 DM 제보: 저녁 시간 2차로에 비상등 켜고 정차한 덤프와 추돌 사고 목격, 70km/h 구간단속 구간 ; 댓글 상위 '크루즈 켜놓고 딴짓 한 듯'(82) ; 정차 차량 추돌은 뒤차 기본과실이 크고, 주정차 금지 장소·야간 등화 등 사정에 따라 앞차 과실 가감(손해보험협회 과실비율 인정기준 일반)",
    t1="비상등 켜고 서 있는", t2="덤프를 그대로 박음", bar="비상등 켜고 2차로에 선 덤프를 뒤차가 그대로 들이받음", cnt=41,
    title="#비상등 덤프 추돌", shop="차량용 블랙박스 2채널, 비상삼각대",
    desc=["저녁 2차로에 비상등 켜고 서 있던 덤프트럭을 뒤차가 그대로 들이받은 사고.",
          "시속 70km 구간단속 구간이었고, 댓글은 크루즈 켜고 딴짓한 것 같다는 반응.",
          "앞에 멈춘 차를 박으면 과실이 어떻게 나오는지."],
    tags="#shorts #후미추돌 #비상등 #덤프트럭 #블랙박스",
    comment="님들은 크루즈 켜고 다닐 때 앞 잘 봄?",
    proof=[("저녁 2차로 비상등 정차 덤프 추돌, 70km/h 구간단속 구간", "원글(보배드림 인스타 제보)"),
           ("댓글: 크루즈 켜놓고 딴짓 한 듯(추천 82)", "원글 댓글"),
           ("정차 차량 추돌은 뒤차 기본과실, 장소·야간 등에 따라 가감", "손해보험협회 과실비율 인정기준 일반")],
    lines=[
        L("비상등 켜고 서 있는 덤프를 뒤차가 그대로 박아버림.", 1),
        L("저녁 시간, 2차로에 덤프트럭이 비상등을 켜고 멈춰 있었음.", 2, sfx="whoosh", em=["비상등"]),
        L("시속 70km 구간단속 구간이라 다들 일정하게 달리던 상황.", 3),
        L("근데 뒤에서 오던 차가 속도를 하나도 안 줄이고 그대로 들어감.", 4, sfx="dudung", shake=False, em=["그대로"], em_color="yellow"),
        L("댓글은 크루즈 켜놓고 딴짓한 것 같다는 반응이 제일 많음.", 5, em=["크루즈"], em_color="yellow"),
        L("멈춘 차를 뒤에서 박으면 기본적으로 뒤차 과실이 큼.", 6, sfx="pop", em=["뒤차 과실"]),
        L("다만 정차 금지 장소였거나 밤에 표시를 제대로 안 했으면 앞차에도 과실이 붙을 수 있음.", 7),
        L("이 덤프는 비상등을 켜고 있었으니 뒤차가 피할 여지가 있었던 거임.", 8),
        L("크루즈를 켜도 앞에 멈춘 차는 못 알아보는 경우가 있어서 결국 눈으로 봐야 함.", 9, sfx="ding", em=["눈으로"], em_color="yellow"),
        L("차가 서야 하면 비상등 켜고 뒤에 삼각대까지 세우는 게 내 목숨 지키는 거임.", 10, em=["삼각대"]),
        L("님들은 크루즈 켜고 다닐 때 앞 잘 봄?", 5), OUT],
    prompts={
        1: "a sedan crashed into the rear of a large dump truck stopped in the second lane of a Korean urban expressway at dusk, hazard lights blinking",
        2: "a large dump truck stopped in the second lane of a multi-lane road at dusk with amber hazard lights on, rear view",
        3: "a Korean urban expressway at dusk with steady traffic flow and headlights, wide shot",
        4: "view from inside a car approaching the back of a stopped dump truck at speed at dusk, hazard lights glowing ahead",
        5: f"{M1} driving while looking down at a smartphone with the steering wheel loosely held, dusk, view from passenger seat",
        6: "the crumpled front of a sedan wedged under the rear bumper of a dump truck, evening, emergency lights",
        7: "a dump truck parked on the side of a dark road at night with no lights, barely visible",
        8: "close-up of a dump truck rear lights blinking amber hazard lights at dusk",
        9: "close-up of a car steering wheel with adaptive cruise control buttons, hands resting, dusk light, no text",
        10: "a red reflective warning triangle placed on the road behind a stopped truck at dusk",
    })

# ── 4. G80은 주차타워 못 들어가는데 ─────────────────────────
eps["g80tower"] = dict(
    src=f"{B}1038488 (추천 271, 조회 4천, 댓글 18) ; 본문: 오피스텔 입주민, G80이 주차타워 규격상 못 들어가 지상에 주차 → 그랑 콜레오스 차주가 '지상은 SUV 전용'이라며 따짐, 경비원도 동조, 다음 날 새벽 5시 30분 이중주차로 차를 못 빼 지하철 출근(차 15분→30분), 차에 주차 스티커 ; 안내문: 주차타워 구조상 SUV 불가, 지상은 SUV용, 지상 부족 시 타워 이용 ; 글쓴이 질문: 관리규약·관리단 의결 없이 SUV 전용 지정이 가능한지",
    t1="주차타워엔 못 들어가는데", t2="지상은 SUV 전용?", bar="주차타워 못 들어가는 G80, 지상에 댔더니 이중주차로 가둠", cnt=18,
    title="#타워 못 가는 G80", shop="차량용 주차번호판, 차량용 블랙박스",
    desc=["오피스텔 주차타워에 규격상 못 들어가는 G80, 지상에 댔더니 SUV 전용이라며 시비.",
          "다음 날 새벽엔 앞에 이중주차로 막혀 지하철 타고 출근, 차엔 주차 스티커까지.",
          "공식 규정 없이 SUV 전용 자리를 강제할 수 있을까."],
    tags="#shorts #오피스텔주차 #이중주차 #주차갈등 #보배드림",
    comment="님들은 이거 누가 잘못한 거 같음?",
    proof=[("G80은 주차타워 규격 초과, 지상 주차했다가 SUV 전용이라는 항의", "원글 본문"),
           ("새벽 5시 30분 이중주차로 차 못 뺌, 부재중, 지하철 출근, 주차 스티커", "원글 본문"),
           ("안내문: 타워는 SUV 불가, 지상은 SUV용, 지상 부족 시 타워 이용", "원글 첨부 안내문")],
    lines=[
        L("주차타워에 못 들어가는 차인데 지상에 대지 말라고 함.", 1),
        L("오피스텔 사는 G80 차주, 차가 커서 주차타워 규격에 안 맞음.", 2, sfx="whoosh", em=["주차타워"]),
        L("그래서 지상에 댔는데 SUV 차주가 지상은 SUV 전용이라고 따짐.", 3, sfx="dudung", shake=False, em=["SUV 전용"], em_color="yellow"),
        L("승용차는 길가에 대든지 월 정기권을 끊으라고.", 4),
        L("경비원까지 SUV 자리가 맞다고 거듦.", 5),
        L("진짜 문제는 다음 날 새벽 5시 반이었음.", 6, sfx="pop"),
        L("출근하려고 내려왔더니 차 앞에 이중주차가 돼 있고 전화는 계속 부재중.", 7, em=["이중주차"], em_color="yellow"),
        L("결국 15분이면 갈 길을 지하철로 30분 걸려 출근했는데, 차엔 주차 스티커까지 붙어 있었음.", 8, em=["주차 스티커"]),
        L("안내문엔 지상은 SUV용이라면서, 지상이 모자라면 타워를 쓰라고 적혀 있음.", 9, sfx="ding"),
        L("글쓴이는 관리규약 같은 공식 근거가 있는지부터 묻는 상황.", 10, em=["공식 근거"], em_color="yellow"),
        L("님들은 이거 누가 잘못한 거 같음?", 3), OUT],
    prompts={
        1: "a black luxury sedan parked on an outdoor ground-level parking space next to a mechanical parking tower of a Korean officetel building, daytime",
        2: "the entrance of a mechanical car parking tower with a narrow platform, Korean building, daytime",
        3: f"{W2} pointing and arguing next to a white SUV in an outdoor parking lot of an officetel, daytime",
        4: "cars parked along a narrow city street curb in Korea, daytime",
        5: "an elderly Korean security guard in uniform standing in a parking lot with arms crossed, daytime",
        6: "an officetel parking lot at dawn with dim street lights and a blue sky, quiet",
        7: "a white SUV double-parked directly in front of a black sedan in a parking lot at dawn, blocking it",
        8: f"{M1} in a suit hurrying down the stairs into a Seoul subway station at dawn",
        9: "a printed parking notice taped on a wall near a parking tower, text blurred and unreadable",
        10: "close-up of a yellow parking violation sticker stuck on a black car's side window, text blurred and unreadable",
    })

# ── 5. 엔진오일 뚜껑 안 닫은 카센터 ─────────────────────────
eps["oilcap"] = dict(
    src=f"{B}1038277 (추천 106, 댓글 12) ; 본문: 1톤 화물트럭(가구배송) 단골 카센터에서 엔진오일 교환 → 약 일주일 뒤 고속도로 출력 저하·소음, 오일 주입구 뚜껑 미체결로 오일 분출, 공업사 확인 시 잔량 약 500ml, 시동 불가 → 카센터가 뚜껑 사과 후 보링업체로 보냄 → 보링업체 '피스톤 상단 용융은 엔진오일과 무관' → 인젝터 교체·보링 480만 원 청구, 400만 원으로 협의, 100만 원 카드 결제 ; 댓글 'A와 B가 짰네, 제3의 업체로 가셨어야'",
    t1="엔진오일 갈고 나서", t2="엔진이 퍼졌음", bar="카센터가 엔진오일 뚜껑 안 닫아서 엔진 퍼짐", cnt=12,
    title="#오일뚜껑 안 닫음", shop="엔진오일 교환 세트, 차량용 블랙박스",
    desc=["엔진오일 갈고 일주일 뒤, 고속도로에서 1톤 트럭 엔진에서 연기가 남.",
          "열어보니 오일 주입구 뚜껑이 안 닫혀 있었고 오일은 500ml만 남아 있었음.",
          "그런데 수리비 400만 원은 차주가 내게 된 사연."],
    tags="#shorts #엔진오일 #카센터 #정비사고 #보배드림",
    comment="님들이면 이거 그냥 냄?",
    proof=[("오일 교환 후 뚜껑 미체결, 고속도로에서 오일 분출, 잔량 약 500ml", "원글 본문"),
           ("보링업체: 피스톤 상단 용융은 엔진오일과 무관 판단", "원글 본문"),
           ("480만 원 청구 → 400만 원 협의, 100만 원 결제", "원글 본문"),
           ("댓글: 제3의 업체에서 다시 진단 받았어야", "원글 댓글")],
    lines=[
        L("엔진오일 갈고 일주일 만에 엔진이 퍼졌는데 수리비는 차주가 냄.", 1),
        L("가구 배송하는 아버지의 1톤 트럭, 단골 카센터에서 엔진오일을 갈았음.", 2, sfx="whoosh"),
        L("일주일 뒤 고속도로에서 힘이 빠지고 소리가 나서 갓길에 세움.", 3, sfx="dudung", shake=False),
        L("보닛을 열어보니 오일 넣는 구멍 뚜껑이 안 닫혀 있었음.", 4, em=["뚜껑"], em_color="yellow"),
        L("오일이 다 뿜어져 나와서 엔진에 남은 게 500ml 정도.", 5, em=["500ml"], em_color="yellow"),
        L("카센터는 뚜껑은 사과하면서 엔진 전문 업체로 차를 보냈음.", 6),
        L("근데 그 업체가 피스톤이 녹은 건 엔진오일이랑 상관없다고 판정함.", 7, sfx="pop", em=["상관없다"]),
        L("결국 인젝터 교체랑 보링에 480만 원, 깎아서 400만 원이 차주 몫이 됨.", 8, em=["400만 원"], em_color="yellow"),
        L("댓글은 처음 카센터랑 그 업체가 한편이라며, 다른 곳에서 다시 진단받았어야 한다는 반응.", 9, sfx="ding", em=["다시 진단"]),
        L("정비 사고 나면 사진부터 남기고, 제3의 업체 소견을 꼭 받아둬야 함.", 10),
        L("님들이면 이거 그냥 냄?", 4), OUT],
    prompts={
        1: "a white one-ton Korean cargo truck stopped on a highway shoulder with smoke rising from under the cab, daytime",
        2: f"{M5} standing proudly next to his white one-ton cargo truck loaded with furniture boxes, daytime",
        3: "a small white cargo truck pulled over on a highway shoulder with hazard lights blinking, daytime",
        4: "close-up of an open engine oil filler hole without its cap on a dirty engine, oil splattered around",
        5: "a mechanic holding a small measuring container with a little dark engine oil inside, workshop light",
        6: f"{M6} talking with an older man in a small Korean auto repair shop, apologetic gesture",
        7: "close-up of a damaged engine piston with a melted top surface on a workbench, workshop light",
        8: "a repair invoice paper and a calculator on a garage counter, text blurred and unreadable",
        9: f"{M5} sitting worried on a bench at a repair shop holding a phone, workshop background",
        10: "a smartphone taking a photo of an open engine bay with oil leaks, close-up, daytime",
    })

# ── 6. 세타2 평생보증인데 거절 ──────────────────────────────
eps["theta2"] = dict(
    src=f"{B}1038248 (추천 28, 댓글 11) ; 본문: 그랜저 HG 2.4 2015년식, 2026-05-25 영동고속도로 마성터널에서 시동 꺼짐, 비상통로 대피, 블루핸즈 진단 커넥팅로드 베어링 고착 엔진 파손, 자비 수리 후 청구 → 3년치 오일 교환 내역 요구, P1326 에러코드가 안 떠서 보상 불가 답변(글쓴이 주장), KSDS 2019년 업데이트 ; 사실관계: 현대·기아 2019-10-11 세타2 GDi 52만 대 KSDS 적용·엔진 평생보증 발표, 대상에 그랜저 HG 포함(연합뉴스 AKR20191011105451003, 세계경제 보도)",
    t1="평생보증 엔진이라더니", t2="에러코드 없어서 거절", bar="터널에서 시동 꺼졌는데, 에러코드 안 떴다고 보상 거절", cnt=11,
    title="#세타2 보상 거절", shop="차량용 블랙박스 2채널, 비상삼각대",
    desc=["2015년식 그랜저, 고속도로 터널 안에서 갑자기 시동이 꺼짐.",
          "평생보증 받는 세타2 엔진인데, 에러코드가 안 떴다고 보상이 안 된다는 답.",
          "2019년 평생보증 발표 내용과 차주 주장."],
    tags="#shorts #세타2 #엔진결함 #평생보증 #보배드림",
    comment="님들은 이거 보상해줘야 한다고 봄?",
    proof=[("2015 그랜저 HG 2.4, 터널 내 시동 꺼짐, 커넥팅로드 베어링 고착", "원글 본문"),
           ("P1326 코드 미발생으로 보상 불가 답변(글쓴이 주장)", "원글 본문"),
           ("2019-10-11 세타2 GDi 52만 대 KSDS·엔진 평생보증, 그랜저 HG 포함", "연합뉴스·세계경제 보도")],
    lines=[
        L("평생 보증해준다던 엔진이 터널 안에서 꺼졌는데 보상을 거절당함.", 1),
        L("2015년식 그랜저, 고속도로 터널 안을 달리다 갑자기 시동이 꺼짐.", 2, sfx="dudung", shake=False, em=["터널 안"], em_color="yellow"),
        L("비상등 켜고 트렁크 열고 비상통로로 겨우 대피했다고 함.", 3),
        L("진단해보니 엔진 속 베어링이 들러붙어서 엔진이 망가진 거였음.", 4, sfx="whoosh"),
        L("이 엔진, 2019년에 현대차가 평생 보증하겠다고 발표한 세타2 엔진임.", 5, em=["평생 보증"], em_color="yellow"),
        L("그래서 자비로 고치고 수리비를 청구했는데 거절당함.", 6, sfx="pop"),
        L("차주 말로는 3년 치 오일 교환 내역까지 내라더니, 특정 에러코드가 안 떠서 안 된다고 했다고 함.", 7, em=["에러코드"]),
        L("그 코드는 엔진 진동을 감지하면 뜨는 경고인데, 차주는 센서 문제 아니냐고 반박함.", 8),
        L("발표 때는 에러코드가 있어야 한다는 말은 없었다는 게 차주 주장.", 9, sfx="ding", em=["차주 주장"], em_color="yellow"),
        L("이런 분쟁은 정비 기록이랑 견인 기록을 다 챙겨두는 게 제일 중요함.", 10),
        L("님들은 이거 보상해줘야 한다고 봄?", 1), OUT],
    prompts={
        1: "a dark gray sedan stopped inside a long Korean highway tunnel with hazard lights blinking and trunk open, orange tunnel lights",
        2: "view from a driver's seat inside a highway tunnel with dashboard warning lights on, orange lighting",
        3: f"{M4} walking quickly toward a green emergency exit door inside a highway tunnel, orange lighting",
        4: "close-up of a damaged engine crankshaft and connecting rod bearing on a workbench, workshop light",
        5: "a large engine block on a stand in a clean car service center, soft light, no logos",
        6: f"{M4} sitting at a car service center counter with documents, frustrated face, documents text blurred",
        7: "a stack of car maintenance receipts and service records on a table, text blurred and unreadable",
        8: "close-up of an OBD diagnostic scanner plugged into a car under the dashboard, screen blurred",
        9: f"{M4} talking on the phone angrily in his living room, evening",
        10: "a tow truck towing a sedan out of a highway tunnel exit, daytime",
    })

# ── 7. 경찰관 매달고 74km ───────────────────────────────────
eps["drunkcop"] = dict(
    src=f"{B}1038205 (추천 56, 댓글 19) ; 연합뉴스TV 2026-10-07 '경찰관 차 매달고 시속 74㎞까지 질주…만취 운전 50대 실형'(n.news.naver.com/article/422/0000913344): 광주고법 전주재판부 형사1부 항소 기각, 징역 1년 6개월 원심 유지, 지난해 1월 26일 오후 8시 20분께 순천시 효자동, 면허취소 수치 만취 벤츠, 음주단속 경찰관 매달고 200m 넘게 달아남, 최고 74km/h, 다른 차량 들이받음, 경찰관 팔·다리 부상, 과거 3차례 음주 처벌 전력, 합의 주장에도 형 유지",
    t1="음주 단속 경찰을", t2="차에 매달고 74km", bar="음주 단속하던 경찰관을 차에 매달고 달아남", cnt=19,
    title="#경찰 매달고 74km", shop="개인용 음주측정기, 차량용 블랙박스",
    desc=["음주 단속하던 경찰관을 차 문에 매단 채 시속 74km로 달아난 만취 운전자.",
          "다른 차까지 들이받고, 떨어진 경찰관은 팔다리를 다침.",
          "음주 전력 3번, 항소심에서도 실형 1년 6개월."],
    tags="#shorts #음주운전 #음주단속 #실형 #보배드림",
    comment="님들은 1년 6개월이 적당하다고 봄?",
    proof=[("음주단속 경찰관 매달고 200m 넘게, 최고 74km/h", "연합뉴스TV 2026-10-07"),
           ("면허취소 수치 만취, 다른 차량 들이받음, 경찰관 팔·다리 부상", "연합뉴스TV 2026-10-07"),
           ("과거 음주 처벌 3회, 항소 기각·징역 1년 6개월 유지", "연합뉴스TV 2026-10-07")],
    lines=[
        L("음주 단속하던 경찰관을 차에 매단 채 시속 74km로 달림.", 1),
        L("밤 8시쯤 음주 단속에 걸린 50대 운전자, 면허 취소 수치의 만취 상태였음.", 2, sfx="whoosh", em=["만취"]),
        L("측정하자는 경찰관을 무시하고 그대로 출발해버림.", 3, sfx="dudung", shake=False),
        L("경찰관이 차 문을 붙잡고 있는 걸 알면서도 200m 넘게 달렸음.", 4, em=["200m"], em_color="yellow"),
        L("속도는 최고 시속 74km까지 올라감.", 5, em=["74km"], em_color="yellow"),
        L("도망치다 다른 차를 들이받았고, 경찰관은 도로에 떨어져 팔다리를 다침.", 6, sfx="pop"),
        L("옆에 탄 사람이 세우라고 소리쳐도 욕하면서 계속 몰았다고 함.", 7),
        L("알고 보니 음주운전으로 처벌받은 게 이번이 처음이 아니었음, 무려 3번.", 8, sfx="ding", em=["3번"], em_color="yellow"),
        L("피해자랑 합의했다고 형을 줄여달라 했지만 항소심도 징역 1년 6개월 그대로.", 9, em=["1년 6개월"]),
        L("재판부는 경찰관 생명에 중대한 위험을 초래했다고 못 박음.", 10),
        L("님들은 1년 6개월이 적당하다고 봄?", 9), OUT],
    prompts={
        1: f"{POL} clinging to the open door of a moving dark sedan on a city road at night, motion blur, red and blue lights",
        2: "a police sobriety checkpoint on a Korean city road at night with glowing traffic batons and police car lights",
        3: f"{POL} leaning toward a dark sedan driver window with a breathalyzer at night",
        4: "rear view of a dark sedan speeding away on a night road with a figure holding onto the driver door, motion blur",
        5: "close-up of a car speedometer needle rising at night, dashboard glow, no readable text",
        6: "a collision between a dark sedan and another car on a night road, police lights in the background",
        7: "interior of a car at night with a passenger shouting and reaching toward the driver, blurred motion",
        8: "a pile of court documents with a gavel on a desk, text blurred and unreadable, soft light",
        9: "exterior of a Korean high court building, daytime, no text",
        10: "a police officer with an arm bandage sitting in an ambulance at night, emergency lights",
    })

# ── 8. 모퉁이 5m 주차 신고 결과 ─────────────────────────────
eps["cornerpark"] = dict(
    src=f"{B}1038397 (추천 28, 댓글 6) ; 본문: 도로교통법 32조 2호 '교차로의 가장자리나 도로의 모퉁이로부터 5미터 이내' 주정차 금지, 표지판·황색선 없어도 법정 금지구역 ; 첨부: 안전신문고 처리 결과 '주민이 안전신문고 앱을 통해 신고 가능한 지역(모퉁이 5m 이내)으로 과태료 부과 절차 진행' ; 주민신고제 대상(소화전·교차로 모퉁이·버스정류소·횡단보도·어린이보호구역·인도), 승용 과태료 4만 원(시행령 별표6 일반 주정차 위반)",
    t1="노란 선도 없는데", t2="과태료 나온 자리", bar="노란 선도 없는 골목 모퉁이 주차, 신고하니 바로 과태료", cnt=6,
    title="#모퉁이 5m 신고", shop="차량용 주차번호판, 차량용 블랙박스",
    desc=["노란 선도 표지판도 없는 골목 모퉁이, 여기 차 대면 과태료 나옴.",
          "도로교통법상 교차로 모퉁이 5m 안은 원래 주정차 금지구역.",
          "안전신문고 앱으로 주민이 바로 신고할 수 있는 자리."],
    tags="#shorts #불법주정차 #안전신문고 #모퉁이주차 #과태료",
    comment="님들 동네 모퉁이에도 차 대는 사람 있음?",
    proof=[("교차로 가장자리·도로 모퉁이 5m 이내 주정차 금지", "도로교통법 32조 2호"),
           ("안전신문고 처리 결과: 모퉁이 5m 이내 주민신고 가능, 과태료 부과", "원글 첨부 처리결과"),
           ("일반 주정차 위반 과태료 승용 4만 원", "도로교통법 시행령 별표6")],
    lines=[
        L("노란 선도 없는 골목 모퉁이에 주차했다가 과태료 나옴.", 1),
        L("한 회원이 교차로 모퉁이에 세운 차를 안전신문고로 신고해봤음.", 2, sfx="whoosh", em=["안전신문고"]),
        L("결과는 과태료 부과.", 3, sfx="dudung", shake=False, em=["과태료 부과"], em_color="yellow"),
        L("도로교통법은 교차로 가장자리나 도로 모퉁이에서 5m 안에는 차를 못 세우게 함.", 4, em=["5m"], em_color="yellow"),
        L("노란 선이나 표지판이 없어도 법으로 원래 금지된 자리임.", 5, em=["원래 금지"]),
        L("모퉁이에 차가 서 있으면 꺾어 들어오는 차가 보행자를 못 봐서 위험함.", 6),
        L("그래서 소화전, 버스정류장, 횡단보도처럼 주민이 바로 신고하는 대상에 들어가 있음.", 7, sfx="ding", em=["주민이 바로"]),
        L("앱으로 시간 간격 두고 사진 두 장만 찍어 올리면 됨.", 8),
        L("승용차 기준 과태료 4만 원.", 9, sfx="pop", em=["4만 원"], em_color="yellow"),
        L("잠깐이라도 모퉁이엔 차 대지 않는 게 답임.", 10),
        L("님들 동네 모퉁이에도 차 대는 사람 있음?", 1), OUT],
    prompts={
        1: "a sedan parked right at the corner of a narrow Korean residential intersection with no painted lines, daytime",
        2: f"{M1} taking a photo of an illegally parked car at a street corner with his smartphone, daytime",
        3: "close-up of a smartphone screen showing a report result notification, text blurred and unreadable",
        4: "overhead view of a small Korean street intersection with a car parked at the corner, daytime",
        5: "a narrow alley corner with plain asphalt and no yellow lines, a car parked tightly at the edge, daytime",
        6: "a car turning a corner where a parked car blocks the view of a pedestrian stepping out, daytime",
        7: "a Korean street with a fire hydrant, a bus stop and a crosswalk in view, daytime",
        8: "a hand holding a smartphone photographing a parked car at a corner, close-up, daytime",
        9: "a parking fine notice envelope in a mailbox, text blurred and unreadable",
        10: "a clear residential street corner in Korea with no parked cars and a pedestrian crossing safely, daytime",
    })

# ── 9. 교차로 곡선 차로 80:20 ───────────────────────────────
eps["lanecurve"] = dict(
    src=f"{B}1038274 (추천 17, 조회 1.1천, 댓글 16) ; 본문: 같은 방향 나란히 직진, 교차로 지나며 차로가 곡선으로 이어지는 구조, 유도선 없는 구간, 글쓴이는 상대가 교차로 진입 전부터 붙어 정지선 넘기 전 접촉했다고 주장, 영상 후반 글쓴이 차가 상대 차선으로 간 건 충돌 후 밀린 것이라 주장, 보험사 글쓴이 80·상대 20, 상대 블박은 카메라가 꺾여 하늘만 촬영 ; 과실 분쟁은 손해보험협회 과실비율분쟁심의위원회 심의 청구 가능",
    t1="나란히 가다 쿵", t2="내가 80이라고?", bar="교차로에서 옆 차랑 닿았는데 보험사가 나보고 80이래", cnt=16,
    title="#교차로 80대20", shop="차량용 블랙박스 2채널, 광각 사이드미러",
    desc=["교차로를 나란히 지나다 옆 차랑 닿았는데 보험사 판단은 내 과실 80.",
          "글쓴이는 상대가 정지선 전부터 붙어 왔다고 억울해함.",
          "상대 블박은 카메라가 꺾여 하늘만 찍혔다는 상황."],
    tags="#shorts #과실비율 #교차로사고 #측면접촉 #보배드림",
    comment="님들이 보기엔 80대20 맞음?",
    proof=[("같은 방향 나란히 직진, 곡선 차로, 유도선 없음", "원글 본문"),
           ("보험사 글쓴이 80·상대 20, 상대 블박 하늘만 촬영", "원글 본문"),
           ("과실비율 분쟁 심의 청구 가능", "손해보험협회 과실비율분쟁심의위원회")],
    lines=[
        L("교차로를 나란히 가다 옆 차랑 닿았는데, 보험사가 나보고 80이래.", 1),
        L("같은 방향으로 두 차가 나란히 직진하던 상황.", 2, sfx="whoosh"),
        L("교차로를 지나면 차로가 휘어지는데, 안에는 유도선이 없는 구간이었음.", 3, em=["유도선"], em_color="yellow"),
        L("그러다 운전석 뒤쪽을 쿵 하고 맞음.", 4, sfx="dudung", shake=False),
        L("근데 보험사 판단은 내 과실 80, 상대 20.", 5, sfx="pop", em=["80"], em_color="yellow"),
        L("영상 끝에 내 차가 상대 차로로 넘어가 있는 게 찍혀서임.", 6),
        L("글쓴이는 정지선 넘기도 전에 상대가 먼저 붙어 와서 닿은 거고, 그 뒤에 밀린 거라고 주장함.", 7, em=["정지선"]),
        L("상대 블박은 카메라가 꺾여서 하늘만 찍혔다고 함.", 8, em=["하늘만"], em_color="yellow"),
        L("이럴 땐 충돌 직후 위치보다 처음 닿기 직전 위치가 중요함.", 9, sfx="ding"),
        L("보험사 판단이 억울하면 손해보험협회 과실비율 분쟁 심의를 청구할 수 있음.", 10, em=["분쟁 심의"]),
        L("님들이 보기엔 80대20 맞음?", 2), OUT],
    prompts={
        1: "two sedans side by side touching each other inside a Korean city intersection, slight scrape, daytime",
        2: "two cars driving side by side in adjacent lanes approaching an intersection, rear view, daytime",
        3: "overhead view of a Korean intersection where the lanes curve after crossing with no guide lines painted inside, daytime",
        4: "close-up of a scrape on the rear driver-side door of a gray sedan, daytime",
        5: f"{M2} on the phone with an insurance agent, looking shocked, standing beside his car, daytime",
        6: "a dashcam view of a car drifting into the adjacent lane inside an intersection, daytime, wide angle",
        7: f"{M2} pointing at a stop line on the road at an intersection, explaining, daytime",
        8: "a dashcam mounted crookedly on a windshield pointing at the sky, close-up, daytime",
        9: "two cars stopped at an intersection after a side collision with drivers inspecting damage, daytime",
        10: "a desk with accident report documents and a laptop, text blurred and unreadable, soft office light",
    })

# ── 10. 번호 한 자리 빼고 주차 ──────────────────────────────
eps["phonedigit"] = dict(
    src=f"{B}1038146 (추천 54, 댓글 14) ; 본문: 지식산업센터 진입로 코너에 주차된 차 때문에 트럭이 회전하기 힘들어 연락하려 했는데 연락처 번호 하나를 빼놓고 주차, 트럭 기사가 한숨 쉬며 수차례 왔다 갔다 해서 겨우 진입 ; 첨부: 코너 주차 차량·번호판 사진",
    t1="연락처 남겨놨길래 걸었더니", t2="번호가 한 자리 없음", bar="코너에 차 대놓고 연락처는 번호 하나 빼놓음", cnt=14,
    title="#번호 빼고 주차", shop="차량용 주차번호판, 차량용 블랙박스",
    desc=["좁은 진입로 코너에 세운 차 때문에 트럭이 못 꺾는 상황.",
          "차 빼달라고 연락하려 보니 연락처가 번호 한 자리 빠진 채 놓여 있음.",
          "결국 트럭 기사가 수차례 왔다 갔다 해서 겨우 들어감."],
    tags="#shorts #주차빌런 #주차번호 #트럭 #보배드림",
    comment="님들은 이거 실수라고 봄 일부러라고 봄?",
    proof=[("진입로 코너 주차로 트럭 회전 곤란", "원글 본문"),
           ("주차 연락처 번호 하나 빠짐", "원글 본문·첨부 사진"),
           ("트럭 기사가 수차례 전후진해 진입", "원글 본문")],
    lines=[
        L("연락처를 남겨놨길래 전화하려 했더니 번호가 한 자리 없음.", 1),
        L("지식산업센터 올라가는 좁은 진입로, 코너에 차 한 대가 딱 서 있었음.", 2, sfx="whoosh", em=["코너"]),
        L("올라오자마자 바로 꺾어야 하는 구조라 트럭이 회전을 못 함.", 3, sfx="dudung", shake=False),
        L("트럭 기사님이 차 좀 빼달라고 연락해 달라고 부탁함.", 4),
        L("그래서 차 앞에 가서 번호를 보는데 뭔가 이상함.", 5, sfx="pop"),
        L("연락처가 한 자리가 빠진 채로 놓여 있던 거임.", 6, em=["한 자리"], em_color="yellow"),
        L("떨어진 건지 일부러 뺀 건지, 0부터 9까지 열 번을 다 걸어볼까 고민함.", 7, em=["열 번"], em_color="yellow"),
        L("결국 기사님이 한숨 쉬고 수차례 앞뒤로 왔다 갔다 해서 겨우 들어감.", 8, sfx="ding"),
        L("댓글은 어디에나 있는 주차 빌런이라는 반응.", 9),
        L("코너에 댈 거면 최소한 전화는 받을 수 있게 번호는 제대로 둬야 함.", 10, em=["번호는 제대로"]),
        L("님들은 이거 실수라고 봄 일부러라고 봄?", 6), OUT],
    prompts={
        1: f"{M1} holding a smartphone and looking confused at a parking contact card on a car dashboard, daytime",
        2: "a narrow concrete access ramp of a Korean industrial office building with a car parked right at the sharp corner, daytime",
        3: "a medium delivery truck struggling to turn at a tight corner because of a parked car, daytime",
        4: f"{M5} leaning out of a truck cab window asking for help, daytime",
        5: f"{M1} bending down to look through a car windshield at a contact card, daytime",
        6: "close-up of a parking phone number display on a car dashboard with one digit slot empty, digits blurred and unreadable",
        7: f"{M1} staring at his smartphone dial pad with a puzzled face, screen blurred",
        8: "a truck carefully reversing and turning multiple times at a tight corner next to a parked car, daytime",
        9: "a sedan parked badly across a corner of an access road, wide angle, daytime",
        10: "a parking contact number holder on a car dashboard showing a full number, digits blurred and unreadable, close-up",
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
