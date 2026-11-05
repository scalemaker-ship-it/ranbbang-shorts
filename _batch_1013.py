#!/usr/bin/env python3
"""란빵 2026-10-13 저녁 5칸(19:00~21:00) — 보배드림 베스트 24시간 자동차 글 5편, v2(Remotion), **경모 목소리(tts_myvoice)**.
parkthreat·humanblock·alley73·garagetent·old90drive
→ work/<slug>/script.json + upload.md + v2/ai_prompts.tsv
경모 TTS 는 숫자를 못 읽으므로 숫자가 든 줄은 "say" 에 한글로 풀어 쓴다(자막은 "text" 그대로).
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
B = "https://www.bobaedream.co.kr/view?code=best&No="
T = (", photorealistic candid smartphone photo, natural light, realistic Korean setting, "
     "no text no letters no signage no logos no watermark, no readable license plates")
OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


eps = {}

# 1 ─────────────────────────────────────────────────────────────
M1 = "a Korean man in his mid 30s, short black hair, gray hoodie"
eps["parkthreat"] = dict(
    src=B + "1039419", src_note="보배드림 베스트 1039419 '불법주차 신고 후 살x협박을 받았습니다' (경주 황성동, 댓글 44) + 1039546",
    t1="불법주차 신고했더니", t2="번호판에 살해 협박", bar="불법주차 신고했더니 협박 문구가 붙음", cnt=44,
    title="#불법주차 신고 보복",
    lines=[
        L("경주의 한 어린이보호구역 교차로 모퉁이에 맨날 불법주차하는 차가 있었음.", 1, em=["맨날"]),
        L("참다 못해 안전신문고로 신고했음.", 2, em=["안전신문고"], em_color="yellow"),
        L("근데 며칠 뒤 그 차를 다시 봤더니 번호판에 종이가 붙어 있었음.", 3),
        L("앞 번호판, 뒤 번호판, 심지어 문짝에까지 살해 협박 문구를 붙여놓은 거임.", 4, em=["살해 협박"]),
        L("신고한 사람 보라고 대놓고 붙인 거임.", 5),
        L("근데 이거 스스로 죄를 두 개나 더 만든 거임.", 6, em=["두 개나"], em_color="yellow"),
        L("첫 번째, 번호판 가리기. 고의로 가리면 1년 이하 징역이나 1천만원 이하 벌금임.", 7,
          say="첫 번째, 번호판 가리기. 고의로 가리면 일 년 이하 징역이나 천마넌 이하 벌금임.", em=["1천만원"], em_color="yellow"),
        L("두 번째, 협박죄. 3년 이하 징역이나 500만원 이하 벌금임.", 8,
          say="두 번째, 협박죄. 삼 년 이하 징역이나 오백마넌 이하 벌금임.", em=["협박죄"]),
        L("원래 신고당한 불법주차도 그대로 남아있음.", 9),
        L("어린이보호구역 불법 주정차는 승용차 과태료가 12만원, 일반 도로의 세 배임.", 10,
          say="어린이보호구역 불법 주정차는 승용차 과태료가 십이마넌, 일반 도로의 세 배임.", em=["세 배"], em_color="yellow"),
        L("댓글에선 번호판 가린 건 112에 사진 보내면 현장 출동도 된다는 말까지 나옴.", 11,
          say="댓글에선 번호판 가린 건 일일이에 사진 보내면 현장 출동도 된다는 말까지 나옴."),
        L("신고 하나 막으려다 형사처벌 받게 생겼음.", 12, em=["형사처벌"]),
        L("님들 같으면 이거 또 신고함?", 13),
        OUT],
    tags="자동차 블랙박스 2채널, 주차번호판, 블랙박스 메모리카드, 차량용 휴대폰 거치대, 차량용 비상삼각대",
    desc="어린이보호구역 모퉁이 불법주차를 안전신문고로 신고했더니\n번호판이랑 문짝에 살해 협박 문구가 붙음.\n번호판 가림·협박죄·보호구역 과태료까지 정리함.\n#shorts #불법주차 #안전신문고 #번호판가림 #협박죄",
    cm="님들 같으면 이거 또 신고함?",
    proof=[("경주 어린이보호구역 교차로 모퉁이 상습 불법주차 → 안전신문고 신고, 앞뒤 번호판·문짝에 살x협박 문구", "보배드림 베스트 1039419 원글"),
           ("번호판 고의 가림 1년 이하 징역 또는 1천만원 이하 벌금", "자동차관리법 제10조 제5항·제81조"),
           ("협박죄 3년 이하 징역 또는 500만원 이하 벌금", "형법 제283조 제1항"),
           ("어린이보호구역 주정차 위반 승용 12만원(일반 4만원의 3배)", "도로교통법 시행령 별표6"),
           ("번호판 가림 112 신고·현장출동", "원글 댓글(추천 45)")],
    P={
        "a01": "an illegally parked silver sedan sitting right on the corner of an intersection inside a Korean elementary school zone, red-painted school zone road surface, yellow double lines on the curb, daytime",
        "a02": f"{M1} holding a smartphone and taking a photo of an illegally parked car on a street corner, view over his shoulder, screen blurred",
        "a03": "the rear of a parked silver sedan with a sheet of white paper taped over its license plate, handwritten scribbles on the paper too blurred to read, close-up",
        "a04": "a parked silver sedan with white paper notes taped on the front plate area and on the driver door, handwritten marks unreadable, menacing atmosphere, overcast day",
        "a05": "close-up of a car door with a crumpled white paper note taped on it with thick black handwritten marks that are illegible, harsh light",
        "a06": f"{M1} staring in disbelief at a parked car covered with paper notes, standing on the sidewalk, side view",
        "a07": "close-up of a car license plate fully covered with taped white paper, tape edges peeling, no characters visible",
        "a08": "a Korean courtroom interior with wooden benches and the judge's bench, empty, serious mood",
        "a09": "a Korean traffic enforcement officer in a reflective vest sticking a yellow parking ticket envelope on the windshield of a parked sedan, school zone, daytime",
        "a10": "a red-painted Korean school zone road with a crosswalk and yellow safety fence near an elementary school, children walking in the distance, wide view",
        "a11": "a Korean police patrol car with blue and red lights arriving next to an illegally parked sedan on a street corner, daytime",
        "a12": "close-up of a hand holding handcuffs next to a police report clipboard on a car hood, shallow depth of field",
        "a13": f"{M1} in a parked car looking at his smartphone and thinking, pondering whether to report again, evening, side view",
    })

# 2 ─────────────────────────────────────────────────────────────
W = "a Korean woman in her late 50s, short permed hair, sun visor cap, floral blouse"
M2 = "a Korean man in his late 30s, short black hair, polo shirt"
eps["humanblock"] = dict(
    src=B + "1039547", src_note="보배드림 베스트 1039547 '주차장 알박기 경험(사이다 ?)' (강화 석모도 보문사) + 1039476(머니투데이 2026-10-12 '빈 주차칸 앞 인간 알박기', n.news.naver.com/article/008/0005424782)",
    t1="빈 자리에서 팔 벌리고", t2="자리 맡는 인간 알박기", bar="주차 안내받은 자리에 아줌마가 서있음", cnt=None,
    title="#인간 알박기 주차",
    lines=[
        L("절 주차장에서 주차요원이 저 자리에 대라고 안내해줬음.", 1),
        L("근데 가보니 웬 아줌마가 빈자리에서 팔을 휘적휘적 흔들고 있었음.", 2, em=["휘적휘적"]),
        L("하는 말이 우리 아저씨가 무릎이 안 좋아서 여기 대야 된다는 거임.", 3, em=["무릎이 안 좋아서"], em_color="yellow"),
        L("안내받았다고 해도 무릎 얘기만 무한 반복함.", 4, em=["무한 반복"]),
        L("그 사이 남편 차가 역방향으로 들어와서 내 차 앞에 섬.", 5, em=["역방향"]),
        L("근데 주차요원은 아줌마 말고 나한테 차를 빼달라고 함.", 6, em=["나한테"], em_color="yellow"),
        L("결국 맞은편 자리가 나서 거기 댔는데, 2분 만에 뒤차가 줄줄이 밀렸음.", 7,
          say="결국 맞은편 자리가 나서 거기 댔는데, 이 분 만에 뒤차가 줄줄이 밀렸음."),
        L("이런 인간 알박기, 서울 한강공원 주차장에서도 터졌음.", 8, em=["한강공원"], em_color="yellow"),
        L("차가 먼저라고 하자 욕까지 했고, 안내원은 그런 안내 한 적 없다고 함.", 9, em=["욕까지"]),
        L("근데 몸으로 자리 맡는 걸 콕 집어 처벌하는 법은 따로 없음.", 10, em=["따로 없음"]),
        L("그렇다고 차로 밀어붙이면 오히려 내가 특수폭행으로 처벌받을 수 있음.", 11, em=["특수폭행"]),
        L("그래서 주차요원이나 관리자를 불러서 비켜달라고 하는 게 제일 안전함.", 12),
        L("님들은 저 상황이면 비켜줌, 버팀?", 13),
        OUT],
    tags="주차번호판, 자동차 블랙박스 2채널, 차량용 휴대폰 거치대, 차량용 방향제, 차량용 비상삼각대",
    desc="주차요원이 안내해준 자리에 아줌마가 서서 팔 흔들며 자리 맡는 중.\n우리 아저씨 무릎이 안 좋다는 말만 무한 반복.\n인간 알박기 대처법까지 정리함.\n#shorts #인간알박기 #주차빌런 #주차장 #자리맡기",
    cm="님들은 저 상황이면 비켜줌, 버팀?",
    proof=[("사찰 주차장, 안내받은 자리에서 여성이 팔 흔들며 자리 맡음 · '우리 아저씨가 무릎이 안 좋아서' 반복 · 남편 차 역방향 진입 · 주차요원이 글쓴이에게 차 빼달라 · 맞은편 자리에 주차, 약 2분", "보배드림 베스트 1039547 원글(강화 석모도 보문사)"),
           ("잠원 한강공원 주차장 인간 알박기, '차가 먼저'라 하자 욕설, 안내원은 그런 안내 한 적 없다", "머니투데이 2026-10-12 (n.news.naver.com/article/008/0005424782)"),
           ("자리 맡기 자체를 처벌하는 명문 규정 없음", "주차장법·도로교통법에 해당 조항 없음"),
           ("자동차로 사람을 밀어붙이면 특수폭행(위험한 물건 휴대)", "형법 제261조")],
    P={
        "a01": "a crowded small parking lot at a Korean mountain Buddhist temple, a parking attendant in a vest pointing a car toward an empty space, sunny weekend",
        "a02": f"{W} standing in the middle of an empty parking space waving both arms wide to block cars, temple parking lot, daytime",
        "a03": f"{W} talking through a car window with an awkward smile, gesturing to her knee, view from inside the driver seat",
        "a04": f"{W} repeating the same words with stubborn face, arms crossed in an empty parking spot, close-up",
        "a05": "an old silver Korean sedan driving the wrong way through a narrow parking lot aisle and stopping nose-to-nose in front of another car",
        "a06": "a Korean parking attendant in a reflective vest bending to talk to a driver through the window, sighing, temple parking lot",
        "a07": "a long line of cars backed up in a narrow parking lot aisle at a Korean temple, rear view, brake lights, sunny",
        "a08": "a riverside park parking lot along the Han River in Seoul with apartment towers in the background, cars parked, afternoon",
        "a09": f"a middle-aged Korean woman standing in an empty parking space at a Han River park lot shouting angrily at a driver, finger pointing",
        "a10": f"{M2} sitting in his car with both hands on the wheel, frustrated sigh, looking at a person blocking a parking space",
        "a11": "a car bumper slowly pushing toward a person's legs in a parking space, low angle, tense moment, motion blur",
        "a12": "a Korean parking attendant placing an orange traffic cone and talking to a woman blocking a parking spot, calm tone",
        "a13": f"{M2} shrugging inside his car, deciding whether to give up the spot, side view through window",
    })

# 3 ─────────────────────────────────────────────────────────────
M3 = "a Korean man in his early 40s, short black hair, glasses, navy windbreaker"
CAR = "a white Korean compact sedan"
eps["alley73"] = dict(
    src=B + "1039414", src_note="보배드림 베스트 1039414 '과실비율 판단 해주세요' (부산 금강로 교차로, 댓글 45, 글쓴이 댓글로 경찰 결과·보험사 7:3·자차 없음 추가)",
    t1="초록불에 출발했는데", t2="내 과실이 30%?", bar="신호 지켰는데 보험사가 7대3이래요", cnt=45,
    title="#초록불인데 7대3",
    lines=[
        L("초록불 받고 천천히 출발했는데 왼쪽 골목에서 차가 튀어나와 그대로 쾅 박았음.", 1, em=["쾅"]),
        L("그 골목은 신호등도 없는 길이었음.", 2, em=["신호등도 없는"], em_color="yellow"),
        L("근데 상대가 오히려 자기가 피해자라며 경찰에 사고 접수를 함.", 3, em=["자기가 피해자"]),
        L("경찰 조사 결과는 상대가 가해자, 안전운전 의무 위반이었음.", 4, em=["상대가 가해자"], em_color="yellow"),
        L("여기서 끝난 줄 알았는데 보험사가 7대3을 들고 옴.", 5, say="여기서 끝난 줄 알았는데 보험사가 칠 대 삼을 들고 옴.", em=["7대3"]),
        L("신호 지키고 천천히 간 내 과실이 30%라는 거임.", 6, say="신호 지키고 천천히 간 내 과실이 삼십 퍼센트라는 거임.", em=["30%"], em_color="yellow"),
        L("상대 차에는 블랙박스도 없었음.", 7),
        L("더 아픈 건 내가 자차 보험이 없다는 거임.", 8, em=["자차 보험이 없다"]),
        L("7대3이면 내 차 수리비 30%는 내 돈으로 내야 함.", 9, say="칠 대 삼이면 내 차 수리비 삼십 퍼센트는 내 돈으로 내야 함.", em=["내 돈"], em_color="yellow"),
        L("보험사 논리는 초록불이어도 교차로에선 좌우를 살폈어야 한다는 거임.", 10),
        L("억울하면 손해보험협회 과실비율 분쟁심의위원회에 심의를 신청할 수 있음.", 11, em=["분쟁심의위원회"], em_color="yellow"),
        L("댓글은 골목차 100이라는 쪽과, 신호 지켜도 100대0은 어렵다는 쪽으로 갈렸음.", 12,
          say="댓글은 골목차 백이라는 쪽과, 신호 지켜도 백 대 영은 어렵다는 쪽으로 갈렸음."),
        L("님들이 보기엔 몇 대 몇임?", 13),
        OUT],
    tags="자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 비상삼각대, 경광봉, 차량용 휴대폰 거치대",
    desc="초록불 받고 출발했는데 신호 없는 골목에서 나온 차랑 사고 남.\n경찰은 상대가 가해자라는데 보험사는 7대3.\n자차 없으면 30%는 내 돈, 분쟁심의 신청법까지 정리함.\n#shorts #과실비율 #교통사고 #블랙박스 #자동차보험",
    cm="님들이 보기엔 몇 대 몇임?",
    proof=[("부산 교차로, 블박차 신호대기 후 녹색 서행 출발 중 왼쪽 신호 없는 골목 차량과 충돌", "보배드림 베스트 1039414 원글"),
           ("상대가 피해자라며 경찰 접수 → 경찰: 상대 가해자(안전운전의무위반), 보험사 7:3 주장, 상대 블박 없음, 자차 없음", "원글 글쓴이 댓글"),
           ("과실비율 분쟁심의위원회 심의 신청", "손해보험협회 과실비율분쟁심의위원회(knia.or.kr)"),
           ("자차 미가입 시 본인 과실분 수리비는 본인 부담", "상대 대물배상은 과실 상계 후 지급"),
           ("댓글 '신호 없는 쪽 100' vs '신호위반도 100:0 아니란 얘기'", "원글 댓글")],
    P={
        "a01": f"{CAR} entering an intersection on green light in a Korean city while another car suddenly darts out from a narrow left alley, moment just before collision, dashcam-like view",
        "a02": f"{CAR} and a dark sedan collided at the mouth of a narrow alley at an intersection, front bumper crumpled, broken plastic on road, daytime",
        "a03": "a narrow Korean residential alley joining a main road with no traffic lights, parked scooters and shop fronts, daytime",
        "a04": f"a dark sedan driver pointing at {CAR} and arguing at an accident scene, hazard lights blinking, street",
        "a05": "a Korean police officer writing an accident report on a clipboard at an intersection beside two damaged cars",
        "a06": f"{M3} on the phone with an insurance company looking shocked, standing next to his damaged white sedan",
        "a07": "close-up of a hand holding a smartphone showing a long insurance message, text blurred and unreadable",
        "a08": f"{M3} pointing at a green traffic light in frustration, intersection behind him, daytime",
        "a09": "a car windshield with no dashcam mounted, empty spot behind rearview mirror, interior view",
        "a10": f"{M3} sitting at a kitchen table looking at an auto repair estimate paper with a calculator, worried, numbers unreadable",
        "a11": "a Korean auto body shop with a white compact sedan with front bumper removed on a lift, mechanic inspecting",
        "a12": "a car driver at an intersection turning head to look left and right carefully before going, green light ahead, interior view",
        "a13": "a modern Korean office meeting room with a long table and documents, an arbitration committee meeting, people seen from behind, faces not visible",
        "a14": f"{M3} sitting in his car at night, scrolling through comments on his phone, screen glow on face, thinking",
    })

# 4 ─────────────────────────────────────────────────────────────
M4 = "a Korean man in his early 30s, short black hair, black t-shirt"
eps["garagetent"] = dict(
    src=B + "1039473", src_note="보배드림 베스트 1039473 '아파트 지하주차장에 텐트를 쳤습니다.....' (댓글 34)",
    t1="아파트 지하주차장에", t2="텐트를 친 입주민", bar="아파트 지하주차장에 텐트를 쳤습니다", cnt=34,
    title="#지하주차장 텐트",
    lines=[
        L("아파트 지하주차장에 내려갔는데 텐트가 쳐져 있었음.", 1, em=["텐트"]),
        L("자세히 보니 텐트 안에 차가 들어가 있음.", 2, em=["차가"], em_color="yellow"),
        L("자기 차 위에 캠핑 텐트를 통째로 씌워놓은 거임.", 3, em=["통째로"]),
        L("캠핑 다녀와서 젖은 텐트를 말리는 걸로 보임.", 4, em=["말리는"], em_color="yellow"),
        L("댓글은 바로 둘로 갈렸음.", 5),
        L("자기 주차칸 안이고 주차장 널널할 때 말리는 거면 이해된다는 쪽.", 6, em=["이해된다"], em_color="yellow"),
        L("매연 가득한 공용 공간에 텐트 펼치는 건 민폐라는 쪽.", 7, em=["민폐"]),
        L("실제로 지하주차장은 입주민 공용 공간이라 관리규약으로 물건 쌓아두는 걸 막는 단지가 많음.", 8, em=["공용 공간"]),
        L("댓글에선 아파트 피크닉존을 예약해서 말린다는 사람도 있었음.", 9),
        L("아예 텐트 세탁하고 건조까지 해주는 업체에 택배로 맡기는 방법도 있음.", 10, em=["택배로"], em_color="yellow"),
        L("그래도 남의 칸까지는 안 넘어가게 자기 차 위에 쳤다는 게 반전임.", 11, em=["반전"]),
        L("님들은 이거 민폐임, 이해됨?", 12),
        OUT],
    tags="자동차 커버, 캠핑 타프, 차량용 방향제, 주차번호판, 자동차 블랙박스 2채널",
    desc="아파트 지하주차장에 텐트가 쳐져 있는데 안에 차가 있음.\n캠핑 텐트 말리는 걸로 보이는데 민폐냐 이해냐로 갈림.\n텐트 말리는 다른 방법까지 정리함.\n#shorts #지하주차장 #캠핑텐트 #아파트주차장 #민폐",
    cm="님들은 이거 민폐임, 이해됨?",
    proof=[("아파트 지하주차장에 텐트, 텐트 안에 자기 차", "보배드림 베스트 1039473 원글·댓글('텐트안에 차가 있어', '자기차 위로 텐트')"),
           ("텐트 말리는 중으로 보임", "원글 댓글 다수"),
           ("널널한 시간대면 이해 vs 매연 공용공간 민폐", "원글 댓글(추천 11·4)"),
           ("공용부분은 관리규약에 따라 사용", "공동주택관리법·각 단지 관리규약"),
           ("피크닉존 예약·텐트 세탁 건조 택배 업체", "원글 댓글")],
    P={
        "a01": "a Korean apartment underground parking garage with fluorescent lights and rows of parked cars, a large camping tent pitched in one parking space",
        "a02": "a big beige dome camping tent covering an entire car in an underground parking garage, the car's wheels visible below the tent edge",
        "a03": "close-up of tent fabric draped over a car roof, guy lines tied to the car's side mirrors, underground garage lighting",
        "a04": "wet camping tent fabric with water droplets and small puddles on the concrete floor beneath, underground parking garage",
        "a05": f"{M4} standing in an underground garage staring at a tent-covered car, holding car keys, puzzled face",
        "a06": "a nearly empty Korean apartment underground parking garage late at night with only a few cars, quiet, fluorescent light",
        "a07": "car exhaust fumes from a car starting in a dim underground parking garage, hazy air, tail lights glowing",
        "a08": "a notice board near the elevator in a Korean apartment underground parking lot with posted papers, text unreadable",
        "a09": "a camping tent drying on a rooftop picnic area of a Korean apartment complex on a sunny day, city skyline",
        "a10": "a packed camping tent bag in a cardboard delivery box at an apartment door, ready to be shipped",
        "a11": "wide shot of the tent-covered car neatly inside its own parking lines, neighboring spaces empty and untouched, underground garage",
        "a12": f"{M4} shrugging in an underground garage beside the tent-covered car, half smile",
    })

# 5 ─────────────────────────────────────────────────────────────
eps["old90drive"] = dict(
    src=B + "1039445", src_note="보배드림 베스트 1039445 '90대 운전자 차량 돌진에 1명 사망… 브레이크 먹통' (댓글 19) — MBC 뉴스데스크 2026-10-12 (n.news.naver.com/article/214/0001528558)",
    t1="브레이크가 안 들었다는", t2="90세 운전자의 돌진", bar="90대 운전자 차량 돌진에 1명 사망", cnt=19,
    title="#90세 운전자 돌진",
    lines=[
        L("서울 광진구 교차로, 신호 받은 차들이 천천히 출발하던 순간이었음.", 1),
        L("SUV 한 대가 갑자기 속도를 올리더니 오토바이랑 택시를 연달아 들이받았음.", 2, em=["연달아"]),
        L("시민들이 뛰어가 심폐소생술까지 했지만, 40대 오토바이 운전자는 끝내 숨졌음.", 3,
          say="시민들이 뛰어가 심폐소생술까지 했지만, 사십 대 오토바이 운전자는 끝내 숨졌음.", em=["끝내 숨졌음"]),
        L("택시 기사와 다른 오토바이 운전자도 다쳤음.", 4),
        L("사고 차는 우회전 전용 차로에서 직진하면서 속도를 높였다고 함.", 5, em=["우회전 전용"], em_color="yellow"),
        L("운전자는 90세 남성이었음.", 6, say="운전자는 구십 세 남성이었음.", em=["90세"]),
        L("진술은 브레이크를 밟았는데 말을 안 들었다는 거임.", 7, em=["말을 안 들었다"], em_color="yellow"),
        L("경찰은 사고기록장치로 브레이크를 진짜 밟았는지 확인하고 있음.", 8, em=["사고기록장치"], em_color="yellow"),
        L("90세 이상 운전자 사고는 작년 한 해에만 116건.", 9, say="구십 세 이상 운전자 사고는 작년 한 해에만 백십육 건.", em=["116건"]),
        L("4년 새 두 배 가까이 늘었고, 사망자는 6배가 됐음.", 10, say="사 년 새 두 배 가까이 늘었고, 사망자는 여섯 배가 됐음.", em=["6배"]),
        L("그래서 고령 운전자 면허 반납 얘기가 또 나옴.", 11, em=["면허 반납"]),
        L("근데 댓글에선 시골은 차 없으면 병원도 못 간다며 대책부터 내놓으라는 말도 나옴.", 12),
        L("님들은 나이로 면허를 제한해야 된다고 봄?", 13),
        OUT],
    tags="페달 블랙박스, 자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 비상삼각대, 경광봉",
    desc="서울 광진구 교차로에서 90세 운전자 SUV가 오토바이·택시를 연달아 들이받음.\n운전자는 브레이크가 안 들었다는 진술.\n90세 이상 운전자 사고 통계와 면허 반납 논쟁까지 정리함.\n#shorts #고령운전자 #교통사고 #면허반납 #급발진",
    cm="님들은 나이로 면허를 제한해야 된다고 봄?",
    proof=[("서울 광진구 교차로, 10/12 오전 11시 50분께 SUV 돌진, 오토바이·택시 충돌", "MBC 뉴스데스크 2026-10-12"),
           ("시민 CPR, 40대 오토바이 운전자 사망, 택시·다른 오토바이 운전자 부상", "MBC 2026-10-12"),
           ("우회전 전용 차선에서 직진하며 가속", "MBC 2026-10-12(경찰 조사)"),
           ("90세 남성 '브레이크를 밟았지만 말을 듣지 않았다'", "MBC 2026-10-12"),
           ("사고기록장치로 브레이크 여부 조사", "MBC 2026-10-12"),
           ("90세 이상 운전자 사고 작년 116건, 4년 새 2배 가까이, 사망자 6배", "MBC 2026-10-12"),
           ("면허 반납 전 이동 지원 대책 요구", "원글 댓글(추천 16)")],
    P={
        "a01": "a busy Seoul intersection with cars slowly starting to move on green light, motorcycles among them, midday, elevated street view",
        "a02": "a dark SUV speeding through a city intersection with motion blur heading toward a delivery motorcycle and a taxi, moment before impact",
        "a03": "aftermath of a crash at a Seoul intersection, a delivery motorcycle on its side on the road, a damaged orange taxi and a dark SUV, debris scattered",
        "a04": "bystanders kneeling on a road performing CPR on a fallen motorcyclist next to a toppled motorcycle, faces not visible, urgent atmosphere",
        "a05": "an ambulance with flashing lights arriving at an accident scene at a city intersection, paramedics running",
        "a06": "a Korean road with a right-turn-only lane marked by a white arrow on the asphalt, a car going straight from it, top-down view",
        "a07": "an elderly Korean man in his 90s with white hair in a beige jacket sitting on a curb after a car accident, back view, police nearby",
        "a08": "close-up of an elderly person's foot in a brown shoe pressing a car pedal, driver footwell, dim light",
        "a09": "close-up of a car event data recorder module being connected to a diagnostic laptop by a technician, screen blurred",
        "a10": "an elderly Korean man driving a car on a city road, both hands gripping the wheel tightly, seen from the passenger side",
        "a11": "elderly hands placing a driver's license card on a counter at a Korean community service center, card text blurred",
        "a12": "a rural Korean village road with a bus stop and a long empty road with mountains, an elderly woman waiting alone, afternoon",
        "a13": "a Korean hospital entrance with elderly patients arriving by car, drop-off zone, daytime",
    })

for slug, e in eps.items():
    wk = os.path.join(ROOT, "work", slug)
    os.makedirs(os.path.join(wk, "v2", "ai"), exist_ok=True)
    for ln in e["lines"]:
        if not ln.get("outro"):
            assert not any(c.isdigit() for c in ln.get("say", ln["text"])), (slug, ln["text"])
    sc = {"slug": slug, "type": "란빵 자동차, 보배드림", "source": e["src_note"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["bar"], "channel": "란빵",
          "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
          "style": {"sub_box": True, "bar": e["bar"], "bar_count": e["cnt"], "watermark": ""},
          "lines": e["lines"]}
    json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)
    assert len(e["title"]) <= 12, (slug, e["title"])
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    open(os.path.join(wk, "upload.md"), "w").write(
        f"# {slug} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n{e['desc']}\n\n"
        f"## 고정 댓글\n\n{e['cm']}\n\n## 쇼핑태그\n\n{e['tags']}\n\n"
        f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")
    open(os.path.join(wk, "v2", "ai_prompts.tsv"), "w").write("".join(f"{k}\t{v}{T}\n" for k, v in e["P"].items()))
    print("ok", slug, len(e["lines"]), "lines", len(e["P"]), "ai", e["title"])
