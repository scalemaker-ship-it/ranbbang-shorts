#!/usr/bin/env python3
"""란빵 2026-10-04 배치 6편 — 자동차 법 (보배드림 베스트 원글).
firstcrash400·dump70·hydrant62·sleepdui·repairbill·crossroad37
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

B = "https://www.bobaedream.co.kr/view?code=best&No="

# ── 1. 첫 사고 수리비 400만 ────────────────────────────────────
eps["firstcrash400"] = dict(
    src=f"{B}1036943 (조회 3.4천) ; 손해배상은 사고와 인과관계 있는 손해만(기존 손상분 공제) ; 물적할증: 할증기준금액(보통 200만 원) 초과 시 1점(보험사 할증 기준 안내)",
    t1="5km로 살짝 박았는데", t2="수리비 400만?", bar="사회초년생 첫 사고, 5km로 박았는데 수리비 400만 원", cnt=22,
    title="#첫사고 수리비400만", shop="2채널 블랙박스, 차량용 블랙박스 SD카드",
    desc=["첫 차 모닝으로 정체 구간에서 5km로 살짝 박은 사회초년생.",
          "원래 금 가 있던 렉서스 범퍼까지 싹 갈아서 수리비 400만 원이 나옴.",
          "기존 손상은 내가 안 물어줘도 되는 이유와 할증 기준."],
    tags="#shorts #첫사고 #수리비 #자동차보험 #보험할증",
    comment="님들은 이거 400만 다 물어줘야 한다고 봄?",
    proof=[("모닝 첫 차, 정체 중 5km 미만 추돌, 34만km 렉서스, 수리비 400만, 원래 금 가 있던 것 상대 인정, 블박 확인", "원글 본문"),
           ("기존 손상분은 배상 범위에서 빠짐", "손해배상 인과관계 일반론"),
           ("200만 원 초과 물적사고 1점 할증", "보험사 할증기준 안내")],
    lines=[
        L("시속 5km로 살짝 박았는데 수리비가 400만 원이 나옴.", 1),
        L("첫 차로 중고 모닝을 산 사회초년생이 막히는 길에서 앞차를 콩 박았음.", 2, sfx="whoosh", em=["사회초년생"]),
        L("앞차는 34만 km 뛴 오래된 렉서스, 내 차는 멀쩡했음.", 3),
        L("죄송한 마음에 대물에 대인까지 다 접수해줬는데,", 4),
        L("보험사에서 연락 온 수리비가 400만 원이었음.", 5, sfx="dudung", shake=False, em=["400만 원"], em_color="yellow"),
        L("이상해서 블박을 돌려보니까 그 범퍼, 원래부터 금이 가 있었음.", 6, sfx="pop", em=["원래부터"]),
        L("상대도 원래 금 가 있었다고 인정했는데 더 심해졌다며 뒤쪽을 싹 다 갈았다고 함.", 7),
        L("근데 이거, 다 물어줄 필요가 없음.", 8, sfx="ding"),
        L("배상은 내가 낸 사고 때문에 생긴 손해까지만이라, 원래 있던 손상은 빼야 함.", 8, em=["원래 있던 손상"], em_color="yellow"),
        L("그래서 블박 영상이랑 수리 내역서를 보험사에 내고 기존 손상 빼달라고 이의를 걸어야 함.", 9, em=["이의"]),
        L("200만 원이 넘어가면 할증이 1점이라, 이거 깎는 게 3년 보험료를 지키는 거임.", 10, em=["1점"], em_color="yellow"),
        L("님들은 이거 400만 다 물어줘야 한다고 봄?", 5), OUT],
    prompts={
        1: "a small white compact hatchback lightly touching the rear bumper of an old dark gray luxury sedan in slow traffic on a Korean city road, daytime",
        2: f"{M1} sitting nervously in the driver seat of a small compact car in heavy traffic, hands on wheel, daytime",
        3: "close-up of an old dark gray luxury sedan rear bumper with a faint crack line, next to an undamaged small white car front bumper, daytime",
        4: f"{M1} bowing apologetically to {M4} on the roadside next to two stopped cars, daytime",
        5: f"{M1} looking shocked at his smartphone during a phone call at his office desk, daytime",
        6: f"{M1} watching dashcam footage on a laptop at night, leaning in closely, screen glow",
        7: "a car body shop with the rear bumper and tail parts removed from an old dark gray sedan, many new parts on the floor, workshop lighting",
        8: "a car repair invoice and a calculator on a desk, paper text blurred and unreadable, soft light",
        9: f"{M1} on a phone call holding printed repair documents, determined face, apartment living room, evening",
        10: "a car insurance renewal notice letter and a pen on a table, paper text blurred and unreadable, soft light",
    })

# ── 2. 끼어들고 멈춘 차 vs 덤프 70% ───────────────────────────
eps["dump70"] = dict(
    src=f"{B}1036895 (조회 3.2만, 추천 356, 댓글 103) ; 도로교통법 제19조(안전거리 확보: 앞차가 갑자기 정지해도 충돌 피할 거리) ; 제19조 제3항(진로변경 시 뒤차 정상 통행 방해 금지)",
    t1="덤프 앞에 끼어들고", t2="그냥 멈춤", bar="25.5톤 덤프 앞으로 끼어들더니 그대로 멈춘 차", cnt=103,
    title="#덤프 과실 70%", shop="2채널 블랙박스, 차량용 블랙박스",
    desc=["25.5톤 덤프트럭 앞으로 끼어들더니 그대로 멈춰버린 승용차.",
          "그런데 법원은 덤프트럭 과실을 70%로 봄.",
          "끼어든 차보다 뒤차 과실이 더 나오는 이유, 안전거리 규정."],
    tags="#shorts #과실비율 #덤프트럭 #끼어들기 #블랙박스",
    comment="님들은 이게 덤프 과실 70% 맞다고 봄?",
    proof=[("25.5톤 덤프 블박, 승용차 끼어든 뒤 정지, 보험사·법원 덤프 과실 70%, 한문철 변호사 재판 다시 조언", "원글 본문"),
           ("뒤차 안전거리 확보 의무", "도로교통법 19조 1항"),
           ("진로변경 시 뒤차 방해 금지", "도로교통법 19조 3항")],
    lines=[
        L("덤프트럭 앞으로 끼어들더니 그 자리에서 그냥 멈춰버린 차.", 1),
        L("25.5톤 덤프트럭이 달리는데 옆 차로 승용차가 갑자기 앞으로 파고듦.", 2, sfx="whoosh", em=["25.5톤"], em_color="yellow"),
        L("빠져나가려다 못 빠지니까 그대로 브레이크를 밟아버린 거임.", 3, sfx="dudung", shake=False),
        L("덤프가 아무리 밟아도 그 무게가 바로 설 리가 없음.", 4, em=["바로 설 리가"]),
        L("결국 쾅, 그런데 결과가 더 충격임.", 5, sfx="pop"),
        L("보험사도 법원도 덤프트럭 과실을 70%로 봤음.", 6, em=["70%"], em_color="yellow"),
        L("댓글은 저승사자 보였을 텐데 겁이 없다며 난리가 남.", 7),
        L("이게 왜 이렇게 나오냐면, 뒤차한테 안전거리 의무가 있기 때문임.", 8, sfx="ding"),
        L("앞차가 갑자기 서도 안 부딪힐 만큼 거리를 두라는 게 도로교통법 19조임.", 8, em=["19조"], em_color="yellow"),
        L("끼어든 차도 뒤차를 방해하면 안 되지만, 박은 쪽 책임을 먼저 크게 보는 거임.", 9),
        L("그래서 이런 건 블박 원본을 들고 소송까지 가서 다퉈봐야 함.", 10, em=["블박 원본"]),
        L("님들은 이게 덤프 과실 70% 맞다고 봄?", 6), OUT],
    prompts={
        1: "a large dump truck on a Korean highway with a white sedan suddenly stopped right in front of it, view from the truck cab, daytime",
        2: "a white sedan cutting into the lane right in front of a large dump truck on a multi-lane Korean road, side view, daytime",
        3: "close-up of a white sedan's red brake lights glowing on a highway, a big truck grille very close behind, daytime",
        4: "a heavy dump truck loaded with gravel braking hard on a highway, tire smoke, motion, daytime",
        5: "the front of a dump truck pressed against the crushed rear of a white sedan on a highway, debris on road, daytime",
        6: "a courtroom gavel on a wooden desk next to a toy dump truck and toy car, soft light",
        7: f"{M2} truck driver sitting in the cab of a dump truck holding his head with one hand, daytime",
        8: "wide aerial view of a Korean highway with trucks and cars keeping distance in lanes, daytime",
        9: "a large truck following a car on a highway with a long gap between them, rear view, daytime",
        10: "a dashcam memory card held between fingers above a truck dashboard, close-up, daytime",
    })

# ── 3. 소화전 신고 62건 ───────────────────────────────────────
eps["hydrant62"] = dict(
    src=f"{B}1036941 (조회 2.1천) ; 소화전 5m 이내 주정차 금지, 과태료 승용 8만·승합 9만 원 ; 안전신문고 1분 간격 사진 2장, 현장 단속 없이 부과 (정책브리핑 korea.kr 148901097)",
    t1="소화전 앞 주차", t2="신고 62건 결과", bar="두 달 동안 소화전 주차만 62건 신고한 사람", cnt=5,
    title="#소화전 주차 8만", shop="차량용 소화기, 차량용 소화기 거치대",
    desc=["8월부터 9월까지 소화전 앞 불법주차만 골라 62건을 신고한 사람.",
          "결과는 62건 전부 수용, 하루 만에 처리된 것도 있음.",
          "소화전 주차 과태료가 일반 주차의 2배인 이유."],
    tags="#shorts #소화전 #불법주차 #안전신문고 #과태료",
    comment="님들은 소화전 앞 주차 본 적 있음?",
    proof=[("8~9월 소화전 불법주차만 62건 신고, 62건 수용, 하루~1주일 내 처리", "원글 본문"),
           ("소화전 5m 이내 주정차 금지, 승용 8만·승합 9만", "정책브리핑 korea.kr"),
           ("안전신문고 1분 간격 사진 2장, 현장 출동 없이 부과", "정책브리핑 korea.kr")],
    lines=[
        L("소화전 앞 주차만 두 달 동안 62건을 신고했는데 결과가 나옴.", 1),
        L("한 보배 회원이 8월이랑 9월, 소화전 앞에 댄 차만 골라서 신고했음.", 2, sfx="whoosh"),
        L("결과는 62건 신고에 62건 전부 수용.", 3, sfx="dudung", shake=False, em=["62건 전부"], em_color="yellow"),
        L("빠르면 하루, 늦어도 일주일 안에 다 처리됐다고 함.", 4),
        L("같은 날 같은 자리에 앞뒤로 대는 차도 있어서 소화전 맛집이라고 부를 정도.", 5, sfx="pop", em=["소화전 맛집"]),
        L("빨간 연석에 소화전 표지판까지 있는데도 그냥 대는 거임.", 6),
        L("근데 소화전 주차는 다른 주차랑 급이 다름.", 7, sfx="ding"),
        L("소화전 5m 안은 주정차 금지라 승용차 과태료가 8만 원, 일반 주차의 두 배임.", 8, em=["8만 원"], em_color="yellow"),
        L("1분 간격으로 사진 두 장만 찍어 안전신문고에 올리면 단속반이 안 와도 바로 나옴.", 9, em=["사진 두 장"]),
        L("불나면 소방차가 그 차 때문에 물을 못 대니까 이렇게 센 거임.", 10),
        L("님들은 소화전 앞 주차 본 적 있음?", 6), OUT],
    prompts={
        1: "a white SUV parked right in front of a red fire hydrant on a Korean street curb painted red, daytime",
        2: "a hand holding a smartphone photographing a car parked next to a fire hydrant on a Korean street, daytime",
        3: "a smartphone screen showing a list of many report results with green check marks, text blurred and unreadable, close-up",
        4: "a parking violation notice envelope on a car seat, text blurred and unreadable, soft light",
        5: "two cars parked one after another in front of a red fire hydrant on a Korean residential street, evening",
        6: "close-up of a red painted curb and a fire hydrant sign pole next to a parked car tire, daytime",
        7: "a Korean fire truck stuck behind a car parked at a fire hydrant on a narrow street, firefighters looking, dusk",
        8: "a red fire hydrant with a measuring tape on the ground showing distance to a parked car, daytime",
        9: f"{M1} taking a photo of an illegally parked car with his smartphone on a Korean street, daytime",
        10: "firefighters connecting a hose to a red fire hydrant at night with smoke in the background, emergency lights",
    })

# ── 4. 차에서 자다가 음주 적발 ────────────────────────────────
eps["sleepdui"] = dict(
    src=f"{B}1036997 (조회 4.6천) ; 대법원 2004.4.23. 선고 2004도1109(운전 = 발진조작 완료 필요, 시동만으로는 부족) ; 시동 걸고 자다가 차가 움직이면 음주운전 성립 가능",
    t1="차에서 자고 있었는데", t2="음주운전?", bar="차에서 자다가 음주운전으로 걸린 20대", cnt=5,
    title="#차에서잠 음주운전", shop="차량용 무시동 히터, 차량용 담요",
    desc=["술 먹고 차에서 자다가 음주운전으로 적발된 20대.",
          "그런데 차에서 잔 것만으로는 음주운전이 아닐 수도 있음.",
          "시동만 켜고 자면 어떻게 되는지, 대법원 기준."],
    tags="#shorts #음주운전 #차박 #대리운전 #도로교통법",
    comment="님들은 술 먹고 차에서 자본 적 있음?",
    proof=[("차에서 자다 음주운전 적발된 20대, 적발 후 편의점 다녀옴", "원글 본문"),
           ("운전은 발진조작 완료가 필요, 시동만으로 부족", "대법원 2004도1109"),
           ("자다가 기어 건드려 차가 움직이면 문제", "판례 일반론(움직임 여부가 기준)")],
    lines=[
        L("차에서 자고 있었는데 음주운전으로 걸린 20대.", 1),
        L("술 마시고 차 안에서 잠들어 있다가 경찰한테 적발됐음.", 2, sfx="whoosh"),
        L("근데 이 사람, 적발되고 나서 담배 사겠다고 편의점까지 다녀옴.", 3, sfx="dudung", shake=False, em=["편의점까지"]),
        L("댓글은 그걸 또 보내줬냐며 어이없다는 반응.", 4),
        L("근데 진짜 궁금한 건 이거임, 차에서 자기만 해도 음주운전임?", 5, sfx="ding", em=["자기만 해도"], em_color="yellow"),
        L("대법원은 시동만 걸었다고 운전한 걸로 안 봄.", 6, em=["시동만"]),
        L("기어를 넣고 차를 실제로 움직여야 운전이라고 봤음.", 6, em=["실제로 움직여야"], em_color="yellow"),
        L("그래서 히터 틀고 자기만 했으면 원칙적으로 음주운전이 아님.", 7),
        L("문제는 자다가 발로 기어를 건드려 차가 조금이라도 굴러가는 경우.", 8, sfx="pop", em=["조금이라도"]),
        L("주차장 빼고 도로에서 차가 움직이면 그때부턴 얘기가 완전히 달라짐.", 9),
        L("그러니까 술 먹었으면 차 키는 아예 다른 사람한테 맡기는 게 답임.", 10, em=["차 키"]),
        L("님들은 술 먹고 차에서 자본 적 있음?", 2), OUT],
    prompts={
        1: f"{M1} sleeping in the reclined driver seat of a parked car at night, a police officer knocking on the window with a flashlight",
        2: "interior of a parked car at night with a young man asleep in the reclined driver seat, dashboard lights glowing, empty soju bottle on the floor",
        3: f"{M1} walking out of a Korean convenience store at night holding a pack of cigarettes, police car lights in background",
        4: "two Korean police officers standing next to a parked car at night talking, flashing lights, street",
        5: "close-up of a car key in the ignition with dashboard lights on at night, interior",
        6: "a judge's gavel on a desk next to a car key and a small toy car, soft light",
        7: "a car parked in a parking lot at night with engine exhaust vapor visible, interior light faintly on, cold weather",
        8: "close-up of a foot accidentally touching a gear shift lever inside a car at night, dim light",
        9: "a car slowly rolling out of a parking space onto a Korean street at night, blurred motion, headlights",
        10: f"{M2} handing a car key to a designated driver in a vest at night outside a restaurant",
    })

# ── 5. 카센터 10만 → 26만 ─────────────────────────────────────
eps["repairbill"] = dict(
    src=f"{B}1036986 (조회 1천) ; 자동차관리법 58조(견적서 발급·의뢰인 동의 없는 임의정비 금지) ; 수원지법 2019나63515(과다 수리비 감액) ; 한국소비자원 1372·시군구 자동차관리 부서 신고",
    t1="10만 원이라더니", t2="26만 원 청구", bar="카센터가 10만 원이라더니 끝나고 26만 원 달래요", cnt=17,
    title="#카센터 26만 청구", shop="차량용 부동액, 차량 공구세트",
    desc=["수리 전엔 부품값·공임·부동액까지 10만 원이라더니 끝나고 26만 원 청구.",
          "말한 10만 원은 공임비였다는 카센터, 근데 녹음이 있음.",
          "견적서 없이 맡겼을 때 대처법과 신고처."],
    tags="#shorts #카센터 #수리비 #과다청구 #자동차정비",
    comment="님들도 카센터에서 이런 적 있음?",
    proof=[("일반 35만 원짜리를 부품·공임·부동액 포함 10만 원 약속, 수리 후 공임만 10만이라며 26만 원 청구, 녹음 있음", "원글 본문"),
           ("견적서 발급·동의 없는 임의정비 금지", "자동차관리법 58조"),
           ("과다 수리비 법원 감액", "수원지법 2019나63515"),
           ("소비자원 1372·시군구 신고", "한국소비자원 안내")],
    lines=[
        L("카센터가 10만 원이라더니 고치고 나서 26만 원을 달라고 함.", 1),
        L("차가 고장 나서 카센터에 물어보니 원래 35만 원짜리를 10만 원에 해준다고 했음.", 2, sfx="whoosh"),
        L("부품값에 공임비, 부동액까지 다 해서 10만 원이라고 분명히 말했음.", 3, em=["다 해서 10만 원"], em_color="yellow"),
        L("근데 수리 끝나고 나니까 말이 바뀜.", 4, sfx="dudung", shake=False),
        L("아까 10만 원은 공임비였고, 다 합치면 26만 원이라는 거임.", 5, em=["26만 원"], em_color="yellow"),
        L("다행히 처음에 10만 원이라고 한 말이 녹음돼 있었음.", 6, sfx="pop", em=["녹음"]),
        L("이럴 때 알아둘 게 있음.", 7, sfx="ding"),
        L("자동차관리법상 카센터는 고치기 전에 견적서를 줘야 하고, 동의 없이 더 고치면 안 됨.", 8, em=["견적서"], em_color="yellow"),
        L("말로 한 약속도 녹음이 있으면 그 금액이 증거가 됨.", 9),
        L("우기면 소비자원 1372나 구청 자동차 관리 부서에 신고하면 됨.", 10, em=["1372"]),
        L("님들도 카센터에서 이런 적 있음?", 5), OUT],
    prompts={
        1: f"{M1} looking shocked at a repair invoice at the counter of a small Korean auto repair shop, daytime",
        2: "a small Korean neighborhood auto repair shop with a car on a lift, open garage door, daytime",
        3: f"{M4} mechanic in work clothes talking to a customer with an easy smile next to an open car hood, daytime",
        4: "a car with its hood closed parked in front of an auto repair shop, finished, late afternoon",
        5: "a mechanic's hand pointing at a printed repair bill on a counter, paper text blurred and unreadable, close-up",
        6: "a smartphone showing a voice recording app waveform held in a hand, close-up, shop background blurred",
        7: "an auto repair shop counter with a card payment terminal and papers, soft light",
        8: "a mechanic handing a written estimate sheet to a customer before repair, paper text blurred and unreadable, workshop",
        9: f"{M1} playing a recording on his phone toward a mechanic at a shop counter, tense, daytime",
        10: f"{M1} on a phone call outside an auto repair shop, serious face, daytime",
    })

# ── 6. 신호 없는 교차로 3:7 ───────────────────────────────────
eps["crossroad37"] = dict(
    src=f"{B}1036940 ; 과실비율 인정기준 차12-2 대로 직진 대 소로 직진 기본 30:70, 선진입 여부로 조정 (손해보험협회 accident.knia.or.kr) ; 도로교통법 제31조(무신호 교차로 서행) ; 분심위(구상금분쟁심의위원회)",
    t1="교차로에 먼저 들어갔는데", t2="내 과실 70%?", bar="신호 없는 교차로, 먼저 들어갔는데 상대 렌트카가 3:7 주장", cnt=18,
    title="#교차로 3대7", shop="2채널 블랙박스, 차량용 블랙박스",
    desc=["신호 없는 교차로에 먼저 진입했는데 대로에서 온 렌트카와 쾅.",
          "상대 보험사는 소로 차가 70%라며 3:7 주장.",
          "대로·소로 기본 과실과 소송 vs 분심위 계산."],
    tags="#shorts #과실비율 #교차로사고 #분심위 #자동차보험",
    comment="님들은 이거 몇 대 몇 같음?",
    proof=[("무신호 교차로, 소로 직진 차 선진입, 대로 렌트카(테슬라Y) 충돌, 상대 3:7 주장, 내 수리비 180만·상대 300~400만, 할증 30~40만 예상, 내 보험사 분심위만", "원글 본문"),
           ("대로 vs 소로 기본 30:70, 선진입 시 조정", "손해보험협회 과실비율 인정기준 차12-2"),
           ("무신호 교차로 서행 의무", "도로교통법 31조")],
    lines=[
        L("신호 없는 교차로에 먼저 들어갔는데 내 과실이 70%라고 함.", 1),
        L("골목에서 나와 신호 없는 교차로를 시속 11km로 천천히 건너고 있었음.", 2, sfx="whoosh", em=["시속 11km"]),
        L("거의 다 건넜을 때 오른쪽 큰길에서 렌트카 테슬라가 들어와서 쾅.", 3, sfx="dudung", shake=False, em=["렌트카"], em_color="yellow"),
        L("불법주차 차 때문에 상대가 보인 순간부터 부딪힐 때까지 1초밖에 없었음.", 4),
        L("근데 상대 보험사는 골목에서 나온 쪽이 70%라며 3:7을 주장함.", 5, em=["3:7"], em_color="yellow"),
        L("여기서 기준을 보면, 큰길 차랑 골목 차가 같이 들어가면 기본이 3:7이 맞음.", 6, sfx="ding"),
        L("근데 누가 먼저 들어갔냐에 따라 이 비율이 꽤 움직임.", 7, em=["먼저 들어갔냐"]),
        L("거기다 상대는 렌트카라 할증 걱정 없이 바로 병원부터 감.", 8, sfx="pop"),
        L("글쓴이는 3년 동안 보험료가 30~40만 원 더 오를 상황이라 소송할지 고민 중.", 9, em=["30~40만 원"], em_color="yellow"),
        L("이럴 땐 블박으로 먼저 진입한 장면을 증명해서 분심위나 소송에서 다퉈야 함.", 10, em=["먼저 진입"]),
        L("님들은 이거 몇 대 몇 같음?", 3), OUT],
    prompts={
        1: "top-down aerial view of an unsignalized intersection in a Korean residential area where a small car from a narrow side street and a white electric SUV from a wider road collide, daytime",
        2: "view from a car dashboard slowly entering an unsignalized intersection from a narrow Korean side street, parked cars on the right, daytime",
        3: "a white electric SUV hitting the side bumper of a gray compact car in the middle of an intersection, debris, daytime",
        4: "a car illegally parked at the corner of a narrow intersection blocking the view to the right, Korean residential street, daytime",
        5: "a phone call with an insurance agent shown as a man holding a phone with a frustrated face in a car, daytime",
        6: "a wide road meeting a narrow side street at an intersection without traffic lights in a Korean town, overhead view, daytime",
        7: "two damaged cars stopped at an intersection with drivers taking photos, daytime",
        8: f"{W1} walking into a Korean hospital entrance holding her neck, daytime",
        9: "a calculator, car insurance papers with blurred text and coins on a table, soft light",
        10: "a laptop showing dashcam footage of an intersection paused, room at night, screen glow",
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
