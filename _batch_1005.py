#!/usr/bin/env python3
"""란빵 2026-10-05 배치 10편 — 기본 운전 상식 (원글 없음, 법령·매뉴얼 근거).
tirepsi·treadcoin·fog1min·jumpcable·wiper6m·downhill·fuellight·mirrorset·highbeam·rainspeed
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

# ── 운전 상식 10편 (2026-10-06 하루 10편 첫 회차). 원글 없음 → bar_count 없음 ──

eps["tirepsi"] = dict(
    src="기온이 약 5.6℃(10℉) 내려가면 타이어 공기압 약 1psi 감소(타이어 제조사 안내 일반론) ; 적정 공기압은 운전석 문 안쪽 표지(차종별)",
    t1="아침마다 뜨는", t2="타이어 경고등", bar="날 추워지니까 아침마다 타이어 경고등이 뜸", cnt=None,
    title="#타이어 공기압 경고등", shop="휴대용 타이어 공기주입기, 디지털 타이어 공기압 게이지",
    desc=["날씨가 추워지면 아침마다 타이어 공기압 경고등이 뜨는 이유.",
          "펑크가 아니라 기온 때문에 공기압이 빠지는 것.",
          "내 차 적정 공기압 확인하는 곳과 넣는 법."],
    tags="#shorts #타이어공기압 #경고등 #운전상식 #겨울철차관리",
    comment="님들 차도 아침에 경고등 뜬 적 있음?",
    proof=[("기온 10℉(약 5.6℃) 하락 시 약 1psi 감소", "타이어 제조사 공기압 안내 일반론"),
           ("적정 공기압은 운전석 문 안쪽 표지", "차량 매뉴얼·도어 표지")],
    lines=[
        L("날씨 쌀쌀해지니까 아침마다 타이어 경고등이 뜸.", 1),
        L("펑크 난 줄 알고 정비소 갔는데 타이어는 멀쩡하다고 함.", 2, sfx="whoosh"),
        L("범인은 기온이었음.", 3, sfx="dudung", shake=False, em=["기온"], em_color="yellow"),
        L("공기는 차가워지면 줄어들어서, 기온이 5도쯤 떨어지면 공기압이 1psi 정도 빠짐.", 4, em=["1psi"]),
        L("밤새 추운 데 세워두면 아침에 경고등 기준 밑으로 내려가는 거임.", 5),
        L("그러다 낮에 달리면 타이어가 데워져서 경고등이 꺼지기도 함.", 6),
        L("근데 이걸 그냥 두면 연비 떨어지고 타이어 옆면이 빨리 닳음.", 7, sfx="pop", em=["연비"]),
        L("내 차 적정 공기압은 운전석 문 열면 안쪽에 스티커로 붙어 있음.", 8, sfx="ding", em=["운전석 문"], em_color="yellow"),
        L("주유소 공기주입기나 휴대용 주입기로 그 숫자에 맞춰 넣으면 끝.", 9),
        L("차가 식어 있는 아침에 재야 제일 정확함.", 10, em=["아침"]),
        L("님들 차도 아침에 경고등 뜬 적 있음?", 1), OUT],
    prompts={
        1: "close-up of a car dashboard instrument cluster at cold morning with an amber tire pressure warning light glowing, frosty windshield edge",
        2: f"{M1} talking with a mechanic who is kneeling and checking a car tire at a small Korean tire shop, morning",
        3: "a car parked outside on a frosty autumn morning in a Korean apartment parking lot, breath-like mist, cold blue light",
        4: "close-up of a tire pressure gauge pressed onto a car tire valve, gauge face reading visible but no text, daylight",
        5: "a row of cars parked overnight in an outdoor lot at dawn with frost on roofs, Korea",
        6: "a car driving on a sunny suburban Korean road at midday, warm light, motion",
        7: "close-up of a slightly underinflated car tire with a bulging sidewall touching the asphalt, daylight",
        8: "close-up of the inside of an open driver door frame showing a tire pressure information sticker, text blurred and unreadable",
        9: f"{M1} filling a car tire with a compact portable electric air pump in a parking lot, daytime",
        10: f"{M1} checking tire pressure with a gauge next to his car on a cold morning, coffee cup on the car roof",
    })

eps["treadcoin"] = dict(
    src="자동차 및 자동차부품의 성능과 기준에 관한 규칙 제12조(타이어 홈 깊이 1.6mm 이상) ; 100원 동전 거꾸로 넣어 이순신 감투가 보이면 교체 권장(타이어 업계 안내)",
    t1="100원짜리 하나로", t2="타이어 수명 체크", bar="타이어 갈 때 됐는지 100원짜리 하나면 앎", cnt=None,
    title="#100원 타이어 체크", shop="타이어 트레드 깊이 게이지, 휴대용 타이어 공기주입기",
    desc=["타이어 교체 시기, 정비소 안 가도 100원 동전 하나로 확인 가능.",
          "동전을 거꾸로 넣어서 이순신 장군 감투가 보이면 교체 신호.",
          "법으로 정한 타이어 마모 한계 1.6mm와 빗길 위험."],
    tags="#shorts #타이어교체 #타이어마모 #운전상식 #빗길운전",
    comment="님들 타이어 마지막으로 언제 갈았음?",
    proof=[("홈 깊이 1.6mm 이상", "자동차 및 자동차부품의 성능과 기준에 관한 규칙 12조"),
           ("100원 동전 감투 테스트", "타이어 업계 안내(일반 상식)")],
    lines=[
        L("타이어 갈 때 됐는지, 100원짜리 하나면 바로 앎.", 1),
        L("정비소 갈 때마다 타이어 바꿀 때 됐다는 소리 들어본 사람 많을 거임.", 2, sfx="whoosh"),
        L("진짜인지 확인하는 방법이 동전 하나임.", 3, em=["동전 하나"], em_color="yellow"),
        L("100원짜리를 이순신 장군 머리가 아래로 가게 거꾸로 해서 타이어 홈에 꽂음.", 4, sfx="ding", em=["거꾸로"]),
        L("이때 감투가 홈에 묻혀서 잘 안 보이면 아직 괜찮은 거임.", 5),
        L("근데 감투가 다 보이면 홈이 많이 닳은 거라 교체할 때가 된 거.", 6, sfx="dudung", shake=False, em=["감투가 다 보이면"], em_color="yellow"),
        L("법으로 정한 한계는 홈 깊이 1.6mm임.", 7, em=["1.6mm"]),
        L("홈이 얕으면 빗길에서 물을 못 빼서 차가 물 위에 뜨듯 미끄러짐.", 8, sfx="pop", em=["미끄러짐"]),
        L("안쪽 바깥쪽이 따로 닳기도 해서 여러 군데 꽂아봐야 함.", 9),
        L("비 오는 계절 오기 전에 한 번씩 꼭 해보셈.", 10),
        L("님들 타이어 마지막으로 언제 갈았음?", 1), OUT],
    prompts={
        1: "extreme close-up of a Korean 100 won coin inserted upside down into the tread groove of a car tire, daylight",
        2: f"{M1} listening skeptically to a mechanic pointing at his car tire at a Korean auto shop, daytime",
        3: "a single silver coin held between two fingers in front of a car wheel, shallow depth of field, daylight",
        4: "close-up of fingers pushing a coin into a tire tread groove, detailed rubber texture, daylight",
        5: "close-up of a new car tire with deep tread grooves, daylight, studio-like clarity",
        6: "close-up of a worn bald car tire with very shallow tread grooves, daylight",
        7: "a tire tread depth gauge measuring a car tire groove, close-up, no readable text",
        8: "a car tire spraying water on a flooded rainy road, low angle, motion blur, gray sky",
        9: "close-up of a car tire with the inner edge worn more than the outer edge, daylight",
        10: "a car parked under a gray sky before rain, wet asphalt beginning, Korean residential street",
    })

eps["fog1min"] = dict(
    src="김서림 제거: 에어컨(제습) 켜고 외기 유입·앞유리 송풍(완성차 매뉴얼·도로교통공단 안전운전 안내 일반론)",
    t1="김서림 1분 만에", t2="없애는 버튼", bar="비 오는 날 앞유리 김서림, 1분 만에 없애는 법", cnt=None,
    title="#김서림 1분 컷", shop="차량용 김서림 방지제, 유리 발수코팅제",
    desc=["비 오는 날 앞유리 김서림, 손으로 닦지 말고 버튼 두 개만 누르면 됨.",
          "에어컨이 여름용이 아니라 제습기라서 김서림에 제일 빠름.",
          "외기 모드까지 같이 켜야 하는 이유."],
    tags="#shorts #김서림 #앞유리김서림 #운전상식 #빗길운전",
    comment="님들은 김서림 생기면 뭐부터 누름?",
    proof=[("에어컨(제습) + 외기 유입 + 앞유리 송풍이 김서림 제거에 빠름", "완성차 매뉴얼·안전운전 안내 일반론")],
    lines=[
        L("비 오는 날 앞유리 김서림, 버튼 두 개면 1분 만에 사라짐.", 1),
        L("가을비 오는 날 출근길, 앞유리가 뿌옇게 변해서 앞이 하나도 안 보였음.", 2, sfx="whoosh"),
        L("급한 마음에 손으로 닦았는데 얼룩만 더 생김.", 3, sfx="dudung", shake=False),
        L("김서림은 차 안 습기가 차가운 유리에 맺히는 거라 습기를 빼야 함.", 4, em=["습기를 빼야"], em_color="yellow"),
        L("그래서 첫 번째가 에어컨 버튼임.", 5, sfx="ding", em=["에어컨"]),
        L("에어컨은 차갑게 하는 것보다 공기 속 물기를 빼는 제습기 역할을 함.", 6),
        L("두 번째는 외기 모드, 바깥 마른 공기를 들여와야 습기가 빠짐.", 7, em=["외기 모드"], em_color="yellow"),
        L("그리고 바람 방향을 앞유리 쪽으로 돌리면 금방 맑아짐.", 8),
        L("손으로 닦으면 기름 자국이 남아서 다음에 더 잘 서림.", 9, sfx="pop"),
        L("유리 안쪽을 미리 깨끗하게 닦아두면 애초에 덜 생김.", 10),
        L("님들은 김서림 생기면 뭐부터 누름?", 1), OUT],
    prompts={
        1: "view from a driver seat of a heavily fogged up car windshield on a rainy day, blurred city lights outside",
        2: "a car driving on a rainy Korean city road in the morning, headlights on, wet asphalt, gray sky",
        3: "a hand wiping a fogged car windshield from inside leaving streaks, rainy day",
        4: "close-up of water droplets condensed on the inside of a car windshield, cold rainy light",
        5: "close-up of a finger pressing an A/C button on a car climate control panel, no readable text",
        6: "dashboard air vents blowing air with visible faint mist clearing, car interior, rainy day",
        7: "close-up of a finger pressing the air recirculation toggle button on a car dashboard, no readable text",
        8: "a car windshield clearing from the bottom up as defrost air blows, rainy road visible ahead",
        9: "a smeared car windshield with greasy streaks seen from inside against sunlight",
        10: f"{W1} cleaning the inside of a car windshield with a microfiber cloth, daytime",
    })

eps["jumpcable"] = dict(
    src="점프 연결 순서: 방전차(+)→구조차(+)→구조차(-)→방전차 엔진 금속부(접지), 분리는 역순(완성차 매뉴얼·보험사 긴급출동 안내 일반론)",
    t1="배터리 방전됐을 때", t2="선 순서 틀리면?", bar="아침에 시동이 안 걸림, 점프 케이블 순서 아는 사람?", cnt=None,
    title="#점프 케이블 순서", shop="차량용 점프스타터, 점프 케이블",
    desc=["추워지면 늘어나는 배터리 방전, 점프 케이블 연결 순서가 있음.",
          "빨간 선 먼저, 검은 선은 마지막에 엔진 쪽 금속에.",
          "블박 상시녹화가 방전 원인일 때 대처법."],
    tags="#shorts #배터리방전 #점프케이블 #운전상식 #겨울철차관리",
    comment="님들은 방전되면 보험사 부름, 직접 함?",
    proof=[("방전차+ → 구조차+ → 구조차- → 방전차 금속부, 분리 역순", "완성차 매뉴얼·보험 긴급출동 안내 일반론")],
    lines=[
        L("배터리 방전됐을 때 점프 선, 순서 틀리면 큰일 남.", 1),
        L("추운 아침, 시동 버튼을 눌렀는데 틱틱 소리만 나고 안 걸림.", 2, sfx="whoosh", em=["틱틱"]),
        L("옆집 차랑 점프 케이블을 연결하려는데 순서를 몰라서 멈칫함.", 3, sfx="dudung", shake=False),
        L("순서는 빨간 선부터임.", 4, sfx="ding", em=["빨간 선부터"], em_color="yellow"),
        L("방전된 차 플러스에 빨간 집게, 반대쪽을 멀쩡한 차 플러스에 물림.", 5, em=["플러스"]),
        L("그다음 검은 선을 멀쩡한 차 마이너스에 물리고,", 6),
        L("마지막 검은 집게는 방전된 차 배터리 말고 엔진 쪽 맨 금속에 물림.", 7, em=["엔진 쪽 맨 금속"], em_color="yellow"),
        L("배터리 바로 옆에서 불꽃이 튀는 걸 막으려고 그러는 거임.", 8, sfx="pop", em=["불꽃"]),
        L("시동 걸리면 뺄 때는 거꾸로, 검은 선부터 빼면 됨.", 9),
        L("블랙박스 상시녹화 때문에 자주 방전되면 저전압 차단 설정부터 확인하셈.", 10, em=["저전압 차단"]),
        L("님들은 방전되면 보험사 부름, 직접 함?", 2), OUT],
    prompts={
        1: "two cars parked nose to nose with hoods open and red and black jumper cables connected between batteries, cold morning",
        2: f"{M1} sitting in a car pressing the start button with a frustrated face, frosty morning, dashboard lights dim",
        3: f"{M1} holding red and black jumper cables looking confused in front of an open car hood, morning",
        4: "close-up of a red jumper cable clamp in a hand, engine bay background blurred",
        5: "close-up of a red clamp attached to a car battery positive terminal with a red cover, engine bay",
        6: "close-up of a black clamp attached to the negative terminal of a car battery, engine bay",
        7: "close-up of a black jumper clamp attached to a bare metal bolt on an engine block away from the battery",
        8: "a small spark near a car battery terminal in a dim engine bay, dramatic close-up",
        9: f"{M1} smiling as his car engine starts, hood open, exhaust vapor in cold air, morning",
        10: "a dashcam mounted behind a car rearview mirror with a small status light on at night, interior",
    })

eps["wiper6m"] = dict(
    src="와이퍼 블레이드 교체 권장 6개월~1년(완성차·와이퍼 제조사 안내 일반론) ; 줄무늬·떨림·소음이 교체 신호",
    t1="와이퍼 드르륵", t2="이러면 바꿀 때", bar="와이퍼가 드르륵 소리 나면서 줄무늬 남김", cnt=None,
    title="#와이퍼 교체 시기", shop="자동차 와이퍼 블레이드, 유리 발수코팅제",
    desc=["와이퍼가 드르륵 떨리고 줄무늬를 남기면 고무가 굳은 것.",
          "와이퍼 교체 주기는 보통 6개월에서 1년.",
          "직접 갈면 5분, 길이 확인하는 법."],
    tags="#shorts #와이퍼 #와이퍼교체 #운전상식 #빗길운전",
    comment="님들 와이퍼 마지막으로 언제 바꿨음?",
    proof=[("교체 권장 6개월~1년, 줄무늬·떨림·소음이 신호", "와이퍼 제조사·완성차 안내 일반론")],
    lines=[
        L("와이퍼가 드르륵 소리 내면서 줄무늬를 남기면 바꿀 때 된 거임.", 1),
        L("비 오는 밤, 와이퍼를 켰는데 앞유리에 물줄기가 줄줄이 남음.", 2, sfx="whoosh"),
        L("맞은편 차 불빛이 번져서 차선도 잘 안 보였음.", 3, sfx="dudung", shake=False, em=["차선도"]),
        L("와이퍼 고무는 햇빛이랑 더위에 계속 굳어서 생각보다 빨리 닳음.", 4, em=["굳어서"]),
        L("그래서 보통 6개월에서 1년에 한 번은 바꾸라고 함.", 5, sfx="ding", em=["6개월에서 1년"], em_color="yellow"),
        L("줄무늬, 떨림, 드르륵 소리, 셋 중 하나만 있어도 교체 신호임.", 6, em=["교체 신호"]),
        L("가는 건 생각보다 쉬움, 와이퍼 세우고 고정 버튼 누르면 쏙 빠짐.", 7),
        L("살 때는 운전석 쪽이랑 조수석 쪽 길이가 달라서 꼭 확인해야 함.", 8, sfx="pop", em=["길이가 달라서"], em_color="yellow"),
        L("세워둘 땐 유리에 붙은 채로 얼지 않게 겨울엔 살짝 들어두면 좋음.", 9),
        L("비 오기 전에 한 번 켜서 줄무늬 남는지 체크해보셈.", 10),
        L("님들 와이퍼 마지막으로 언제 바꿨음?", 2), OUT],
    prompts={
        1: "a car windshield wiper leaving water streaks across the glass in the rain at night, view from inside",
        2: "view from driver seat on a rainy night with streaky windshield and blurred oncoming headlights, Korea",
        3: "glare of oncoming headlights smeared across a wet streaky windshield at night, lane lines barely visible",
        4: "close-up of a cracked hardened rubber wiper blade edge on a windshield, daylight",
        5: "a new wiper blade in a hand next to a car windshield, daylight, parking lot",
        6: "close-up of a wiper blade chattering across a wet windshield with uneven water streaks",
        7: f"{M1} lifting a car wiper arm and pressing the release clip to remove the blade, daytime",
        8: "two wiper blades of different lengths laid on a car hood side by side, daylight",
        9: "car wipers lifted up off the windshield on a snowy winter night, parking lot",
        10: f"{M1} testing the wipers with washer fluid spraying on the windshield, sunny day",
    })

eps["downhill"] = dict(
    src="긴 내리막 풋브레이크 과다 사용 시 페이드·베이퍼록 → 저단 기어(엔진브레이크) 사용 권장(한국도로공사·도로교통공단 안전운전 안내)",
    t1="단풍 구경 내리막길", t2="브레이크 밟으면?", bar="단풍 구경 가서 내리막길에 브레이크만 밟으면 생기는 일", cnt=None,
    title="#내리막 엔진브레이크", shop="2채널 블랙박스, 차량용 휴대폰 거치대",
    desc=["단풍철 산길 긴 내리막에서 브레이크만 계속 밟으면 브레이크가 밀림.",
          "브레이크가 뜨거워져서 생기는 페이드 현상.",
          "자동변속기 차에서 엔진브레이크 쓰는 법."],
    tags="#shorts #엔진브레이크 #내리막길 #운전상식 #단풍여행",
    comment="님들은 내리막에서 기어 내림?",
    proof=[("긴 내리막 풋브레이크 과열 → 페이드·베이퍼록, 저단 기어 권장", "한국도로공사·도로교통공단 안전운전 안내")],
    lines=[
        L("단풍 구경 가서 내리막길에 브레이크만 밟으면 이런 일이 생김.", 1),
        L("단풍 보러 산길을 올라갔다가 길고 구불구불한 내리막을 내려오는 중이었음.", 2, sfx="whoosh"),
        L("계속 브레이크를 밟고 내려가는데 점점 밟아도 잘 안 서는 느낌이 듦.", 3, sfx="dudung", shake=False, em=["잘 안 서는"], em_color="yellow"),
        L("탄 냄새까지 올라와서 갓길에 차를 세웠음.", 4, em=["탄 냄새"]),
        L("브레이크를 계속 쓰면 너무 뜨거워져서 제동력이 떨어지는데 이걸 페이드 현상이라고 함.", 5, sfx="ding", em=["페이드 현상"], em_color="yellow"),
        L("심하면 브레이크액이 끓어서 페달이 쑥 들어가 버림.", 6, sfx="pop"),
        L("그래서 긴 내리막에선 기어를 낮춰서 엔진이 속도를 잡게 해야 함.", 7, em=["기어를 낮춰서"]),
        L("자동변속기도 수동 모드나 L, 2 같은 낮은 단으로 바꾸면 됨.", 8),
        L("브레이크는 길게 밟지 말고 짧게 나눠서 밟는 게 좋음.", 9, em=["짧게 나눠서"]),
        L("내리막 시작 전에 미리 속도를 줄여두는 게 제일 안전함.", 10),
        L("님들은 내리막에서 기어 내림?", 2), OUT],
    prompts={
        1: "a car driving down a steep winding mountain road with colorful autumn foliage in Korea, aerial view",
        2: "view from a car dashboard descending a curvy mountain road lined with red and yellow autumn trees",
        3: "close-up of a foot pressing a brake pedal hard inside a car, dim footwell light",
        4: f"{M1} standing next to his car on a mountain road shoulder sniffing worried near the wheel, autumn leaves",
        5: "close-up of a car brake disc glowing hot through alloy wheel spokes, dramatic lighting",
        6: "close-up of a brake pedal pushed down to the floor, interior footwell, tense lighting",
        7: "close-up of a hand moving an automatic gear lever to manual mode, car interior, no readable text",
        8: "close-up of a gear shifter showing lower gear positions, car interior, letters blurred",
        9: "a car slowly descending a mountain road with brake lights briefly glowing, autumn dusk",
        10: "a road sign silhouette at the top of a steep downhill mountain road with autumn trees, no readable text",
    })

eps["fuellight"] = dict(
    src="주유 경고등 점등 후 주행 가능 거리는 차종·탱크 용량별 상이(차량 매뉴얼) ; 연료가 바닥나면 연료펌프 냉각·이물질 흡입 부담(정비업계 일반론)",
    t1="주유등 들어오고", t2="몇 km 갈 수 있음?", bar="주유등 들어왔는데 몇 km까지 버틸 수 있을까", cnt=None,
    title="#주유등 몇km", shop="차량용 휴대폰 거치대, 차량용 고속 충전기",
    desc=["주유 경고등이 들어와도 바로 서지는 않지만 차마다 남은 거리가 다름.",
          "계기판 주행가능거리와 매뉴얼에서 내 차 기준 확인하는 법.",
          "연료를 바닥까지 쓰면 안 좋은 이유."],
    tags="#shorts #주유경고등 #기름 #운전상식 #자동차관리",
    comment="님들은 주유등 들어오고 얼마나 버텨봄?",
    proof=[("경고등 후 주행 가능 거리는 차종별 상이", "차량 매뉴얼"),
           ("연료 바닥 시 연료펌프 부담", "정비업계 일반론")],
    lines=[
        L("주유등 들어왔을 때, 몇 km까지 갈 수 있는지 아는 사람?", 1),
        L("고속도로 한복판에서 주유 경고등이 딱 켜졌는데 다음 휴게소가 멀었음.", 2, sfx="whoosh", em=["주유 경고등"]),
        L("식은땀 흘리면서 겨우 주유소에 도착함.", 3, sfx="dudung", shake=False),
        L("경고등이 켜졌다고 바로 서는 건 아님, 탱크에 기름이 조금 남아 있을 때 켜짐.", 4, em=["바로 서는 건 아님"]),
        L("근데 몇 km를 더 가는지는 차마다 완전히 다름.", 5, sfx="ding", em=["차마다"], em_color="yellow"),
        L("그래서 남이 50km 갔다는 말 믿으면 안 되고 계기판 주행가능거리를 봐야 함.", 6, em=["주행가능거리"], em_color="yellow"),
        L("내 차 기준은 매뉴얼 연료 항목에 나와 있음.", 7),
        L("그리고 기름을 바닥까지 쓰는 습관은 좋지 않음.", 8, sfx="pop"),
        L("연료펌프가 기름 속에서 식는데, 바닥나면 펌프에 무리가 갈 수 있음.", 9, em=["연료펌프"]),
        L("장거리 가기 전엔 반 이상 채우고 출발하는 게 마음 편함.", 10),
        L("님들은 주유등 들어오고 얼마나 버텨봄?", 2), OUT],
    prompts={
        1: "close-up of a car dashboard fuel gauge needle on empty with an amber fuel warning light glowing, night",
        2: "a car driving alone on a Korean highway at dusk, long empty road ahead, tense atmosphere",
        3: f"{M1} gripping the steering wheel nervously, sweating, highway at dusk through windshield",
        4: "cutaway style photo of a car fuel tank with a small amount of fuel at the bottom, studio lighting",
        5: "several different cars lined up at a Korean gas station at night, bright canopy lights",
        6: "close-up of a digital car dashboard showing a range display, numbers blurred and unreadable",
        7: "a car owner's manual open on a passenger seat, pages blurred and unreadable, soft light",
        8: "a fuel nozzle inserted into a car's fuel filler, gas station, daytime",
        9: "close-up of an electric fuel pump part held in a mechanic's gloved hand, workshop",
        10: f"{M1} filling up his car at a Korean gas station before a road trip, sunny morning",
    })

eps["mirrorset"] = dict(
    src="사이드미러 조정: 운전석 쪽은 머리를 창문 쪽에 기울이고, 조수석 쪽은 가운데로 기울인 채 차체 옆면이 살짝 보이게 맞추면 사각지대 감소(SAE 권장 방식, 안전운전 안내 일반론)",
    t1="사이드미러에", t2="내 차가 보이면?", bar="사이드미러에 내 차 옆구리가 반이나 보임", cnt=None,
    title="#사이드미러 사각지대", shop="사각지대 보조 볼록미러, 광각 사이드미러",
    desc=["사이드미러에 내 차 옆면이 많이 보이면 그만큼 사각지대가 커짐.",
          "머리를 기울여서 맞추는 사각지대 줄이는 조정법.",
          "차선 바꿀 때 고개 돌려 확인해야 하는 이유."],
    tags="#shorts #사이드미러 #사각지대 #운전상식 #초보운전",
    comment="님들 사이드미러에 내 차 얼마나 보이게 해둠?",
    proof=[("머리 기울여 차체가 살짝 보이게 맞추는 방식이 사각지대 감소", "SAE 권장 미러 조정법·안전운전 안내 일반론")],
    lines=[
        L("사이드미러에 내 차 옆구리가 많이 보이면 사각지대가 커짐.", 1),
        L("차선 바꾸려고 미러 봤는데 아무것도 없어서 들어갔음.", 2, sfx="whoosh"),
        L("근데 빵 소리랑 함께 옆 차가 바로 옆에 있었음.", 3, sfx="dudung", shake=False, em=["바로 옆에"], em_color="yellow"),
        L("미러에 내 차 옆면이 반이나 보이게 해둬서 정작 옆 차로는 안 보였던 거임.", 4, em=["반이나"]),
        L("조정법은 간단함.", 5, sfx="ding"),
        L("운전석 미러는 머리를 창문에 붙일 듯 기울인 상태에서 내 차 끝이 살짝 보이게 맞춤.", 6, em=["머리를 창문"], em_color="yellow"),
        L("조수석 미러는 머리를 가운데로 기울인 채 똑같이 맞추면 됨.", 7),
        L("바로 앉으면 내 차는 거의 안 보이고 옆 차로가 넓게 보임.", 8, em=["옆 차로가 넓게"]),
        L("그래도 사각지대가 0이 되진 않아서 차선 바꿀 땐 고개 한 번 돌려 확인해야 함.", 9, sfx="pop", em=["고개 한 번"]),
        L("오늘 차 타면 한 번 바꿔보셈.", 10),
        L("님들 사이드미러에 내 차 얼마나 보이게 해둠?", 1), OUT],
    prompts={
        1: "close-up of a car side mirror showing mostly the car's own body side and very little of the road, daytime",
        2: "view from driver seat checking the left side mirror while changing lanes on a Korean city road, daytime",
        3: "a car suddenly very close beside another car in the next lane, slightly blurred motion, daytime traffic",
        4: "close-up of a side mirror reflecting the car's own door taking up half the mirror, empty lane edge",
        5: f"{M1} sitting in a driver seat reaching to the mirror adjustment control, daytime",
        6: f"{M1} leaning his head toward the driver window while adjusting the side mirror, daytime",
        7: f"{M1} leaning his head toward the center of the car while adjusting the passenger side mirror",
        8: "close-up of a side mirror reflecting a wide view of the adjacent lane with a car visible, daytime",
        9: f"{M1} turning his head over his shoulder to check the blind spot before changing lanes, daytime",
        10: "a car side mirror in sunny daylight with a clear reflection of the road behind",
    })

eps["highbeam"] = dict(
    src="도로교통법 제37조·시행령 제20조(마주 오는 차·앞차 뒤따를 때 전조등 밝기 줄이기) ; 안개 시 상향등은 빛 산란으로 시야 저하(도로교통공단 안내)",
    t1="상향등 켜면", t2="오히려 안 보이는 날", bar="안개 낀 날 상향등 켰더니 더 안 보임", cnt=None,
    title="#안개 상향등 금지", shop="차량용 LED 안개등, 차량용 비상 경고등",
    desc=["안개 낀 날 상향등을 켜면 빛이 안개에 반사돼서 더 안 보임.",
          "마주 오는 차 있을 때 상향등은 도로교통법 위반.",
          "안개 낀 날 켜야 하는 등과 속도 줄이는 기준."],
    tags="#shorts #상향등 #안개운전 #운전상식 #도로교통법",
    comment="님들은 상향등 언제 켬?",
    proof=[("마주 오는 차 있을 때 전조등 밝기 줄이기", "도로교통법 37조·시행령 20조"),
           ("안개 시 상향등은 산란으로 시야 저하", "도로교통공단 안전운전 안내"),
           ("안개 가시거리 100m 이내 최고속도 50% 감속", "도로교통법 시행규칙 19조")],
    lines=[
        L("안개 낀 날 상향등 켜면 오히려 더 안 보임.", 1),
        L("새벽 안개 낀 국도, 앞이 안 보여서 상향등을 켰음.", 2, sfx="whoosh"),
        L("근데 눈앞이 하얗게 번쩍하면서 더 안 보이게 됨.", 3, sfx="dudung", shake=False, em=["더 안 보이게"], em_color="yellow"),
        L("상향등 빛이 안개 물방울에 부딪혀서 다시 나한테 반사되는 거임.", 4, em=["반사"]),
        L("안개 낀 날은 하향등에 안개등, 그리고 비상등으로 내 위치를 알리는 게 맞음.", 5, sfx="ding", em=["하향등"]),
        L("상향등은 마주 오는 차가 있거나 앞차를 따라갈 때도 쓰면 안 됨.", 6, em=["마주 오는 차"]),
        L("도로교통법상 이럴 땐 전조등 밝기를 줄여야 해서 위반이 될 수 있음.", 7, sfx="pop", em=["위반"], em_color="yellow"),
        L("그리고 안개로 100m 앞도 안 보이면 최고속도의 절반으로 줄여야 함.", 8, em=["절반"], em_color="yellow"),
        L("상향등은 가로등 없는 길에 앞에 차가 없을 때만 쓰는 거.", 9),
        L("새벽 안개 많은 가을철에 꼭 기억해두셈.", 10),
        L("님들은 상향등 언제 켬?", 1), OUT],
    prompts={
        1: "a car with bright high beams on a thick foggy country road at dawn, light scattering in fog, Korea",
        2: "view from driver seat on a foggy rural Korean road at dawn, low visibility, headlights on",
        3: "a wall of glowing white fog in front of a windshield lit by high beams, blinding glare",
        4: "close-up of headlight beams scattering in dense fog droplets, night",
        5: "a car driving slowly in fog with low beams, fog lights and hazard lights blinking, dawn",
        6: "two cars approaching each other on a dark two-lane road, one with dazzling high beams, night",
        7: f"{M2} squinting and shielding his eyes from oncoming high beams while driving at night",
        8: "a long straight road disappearing into thick fog with barely visible lane lines, dawn",
        9: "a car with high beams on a dark empty rural road with no street lights, night, no other cars",
        10: "an autumn rural Korean road at early morning covered with low fog over fields",
    })

eps["rainspeed"] = dict(
    src="도로교통법 시행규칙 제19조 제2항(비로 노면이 젖은 경우 최고속도의 20/100 감속, 폭우·안개 가시거리 100m 이내·노면 결빙 시 50/100 감속) ; 수막현상은 타이어 홈 배수 한계 초과 시 발생",
    t1="비 오는 날", t2="100km로 달리면 위반?", bar="비 오는 날 고속도로 100km로 달리면 위반임?", cnt=None,
    title="#빗길 20% 감속", shop="유리 발수코팅제, 자동차 와이퍼 블레이드",
    desc=["비 와서 길이 젖으면 제한속도에서 20%를 줄여야 함.",
          "폭우나 안개로 100m 앞이 안 보이면 절반으로.",
          "빗길에 차가 물 위에 뜨는 수막현상 막는 법."],
    tags="#shorts #빗길운전 #수막현상 #운전상식 #도로교통법",
    comment="님들은 비 오면 속도 얼마나 줄임?",
    proof=[("젖은 노면 최고속도 20% 감속, 폭우·안개 100m 이내 50% 감속", "도로교통법 시행규칙 19조 2항"),
           ("수막현상: 타이어 홈 배수 한계", "타이어 업계 안내 일반론")],
    lines=[
        L("비 오는 날 고속도로를 제한속도 100km로 달리면, 그것도 과속임.", 1),
        L("비 오는 고속도로에서 제한속도 딱 맞춰 달리고 있었음.", 2, sfx="whoosh"),
        L("근데 웅덩이를 지나는 순간 핸들이 붕 뜨는 느낌이 들었음.", 3, sfx="dudung", shake=False, em=["붕 뜨는"], em_color="yellow"),
        L("타이어가 물을 다 못 빼서 물 위로 미끄러지는 수막현상임.", 4, em=["수막현상"]),
        L("그래서 법이 비 오는 날 속도를 따로 정해둠.", 5, sfx="ding"),
        L("비가 와서 길이 젖으면 제한속도에서 20%를 줄여야 함.", 6, em=["20%"], em_color="yellow"),
        L("100km 도로면 80km가 기준이 되는 거임.", 7, em=["80km"]),
        L("폭우나 안개로 100m 앞도 안 보이면 절반인 50km까지 줄여야 함.", 8, sfx="pop", em=["절반"], em_color="yellow"),
        L("미끄러질 땐 브레이크를 꽉 밟지 말고 핸들을 똑바로 잡고 발을 떼야 함.", 9, em=["발을 떼야"]),
        L("타이어 홈이 얕으면 더 잘 뜨니까 미리 확인해두셈.", 10),
        L("님들은 비 오면 속도 얼마나 줄임?", 2), OUT],
    prompts={
        1: "a car driving fast on a rainy Korean highway throwing up spray, gray sky, motion blur",
        2: "view from driver seat on a rainy highway with wipers moving and taillights ahead, daytime",
        3: "a car tire hitting a deep puddle on a highway sending a big splash, low angle, rain",
        4: "close-up of a tire riding on a thin film of water on a flooded road, spray, rain",
        5: "an overhead highway speed sign blurred and unreadable over a rainy Korean expressway",
        6: "a car dashboard speedometer during rain, needle visible, numbers blurred, wipers outside",
        7: "cars driving at a moderate distance from each other on a wet highway in the rain, daytime",
        8: "a highway in heavy rain and fog with visibility under a hundred meters, headlights glowing",
        9: f"{M1} holding the steering wheel straight with both hands, tense face, rain on windshield",
        10: "close-up of a car tire tread with water channels on wet asphalt, rain drops",
    })
def upload_md(s, e):
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    return (f"# {s} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n" + "\n".join(e["desc"]) +
            f"\n{e['tags']}\n\n## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop'] or '차량용 블랙박스 2채널, 차량용 휴대폰 거치대'}\n\n"
            f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")


for s, e in eps.items():
    os.makedirs(s, exist_ok=True)
    assert len(e["title"]) <= 12, (s, e["title"], len(e["title"]))
    sc = {"slug": s, "type": "란빵 자동차, 운전 상식", "source": e["src"], "title_line1": e["t1"], "title_line2": e["t2"],
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
