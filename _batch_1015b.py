#!/usr/bin/env python3
"""란빵 2026-10-15 배치 — 10/15 저녁·10/16 칸 채우기 11편 + omoda5 컷 구성. v2(Remotion), 경모 목소리(tts_myvoice).
보배드림 베스트(10/14~15) 8편 + 뉴스 3편.
  anseongdrift leftblinker g63leak autohold leftright seltos bikeban malibubus xt4stall v800brake haeundae6
→ work/<slug>/script.json + upload.md + v2/ai_prompts.tsv + v2/shots.json  (omoda5 는 shots.json 만)
줄 스펙에 컷·효과음·팝·흔들림·인포그래픽을 같이 적고, 기본 컷 = [원컷, 강조어에서 같은 사진 클로즈업].
숫자가 든 줄은 "say" 에 한글로(금액은 마넌). 제목 위험 단어 금지(schedule_zernio.RISKY).
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
T = (", photorealistic candid smartphone photo, natural light, realistic setting, "
     "no text no letters no signage no logos no watermark, no readable license plates")
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")
Y, W, R = "#FBFF56", "#fff", "#FF3B30"
SHOT_KEYS = ("sh", "fx", "pop", "shake", "info")
GEN_TAGS = "자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 휴대폰 거치대, 차량용 비상삼각대"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


def A(img, at=None, punch=False, close=False, fx=0.5, fy=0.5, zin=True, credit=None):
    s0, s1 = (1.6, 1.75) if close else ((1.0, 1.12) if zin else (1.12, 1.0))
    src = img if "/" in str(img) else f"ai/a{int(img):02d}.png"
    d = {"img": src, "s0": s0, "s1": s1, "fx": fx, "fy": fy}
    if at:
        d["at"] = at
    if punch:
        d["punch"] = True
    if credit:
        d["credit"] = credit
    return d


def shot_line(ln, i):
    if ln.get("outro"):
        return {"shots": [A(ln["img"])], "sfx": [["pop_long", "구독!"]], "pop": ["구독!", "#FFE629", "구독!"]}
    if "sh" in ln:
        shots = ln["sh"]
    else:
        em = ln.get("em") or []
        at = em[0] if em else None
        if not at:   # 강조어 없으면 문장 중간 어절에서 반대 방향 켄번즈
            ws = ln["text"].rstrip(".?!").split()
            at = ws[len(ws) // 2].strip(",") if len(ws) > 2 else None
        shots = [A(ln["img"], zin=(i % 2 == 0))]
        if at:
            shots.append(A(ln["img"], at, close=bool(em), punch=bool(ln.get("pop")), zin=(i % 2 == 1)))
    d = {"shots": shots}
    if ln.get("fx"):
        d["sfx"] = [list(x) for x in ln["fx"]]
    for k in ("pop", "shake", "info"):
        if ln.get(k):
            d[k] = list(ln[k]) if k == "pop" else ln[k]
    return d


def info_q(text, at):
    return {"kind": "quotes", "items": [{"text": text, "at": at}]}


def info_c(title, items, at=None):
    d = {"kind": "compare", "title": title, "items": items}
    if at:
        d["at"] = at
    return d


def info_n(title, num, suffix, label, at):
    return {"kind": "counter", "at": at, "title": title, "items": [{"num": num, "suffix": suffix, "label": label, "at": at}]}


def info_b(title, at, items):
    return {"kind": "bars", "at": at, "title": title, "items": items}


OUT = lambda img: {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": img}
eps = {}

# ───────────────────────── omoda5 (컷만 — 대본은 _batch_1015.py) ─────────────────────────
CAP = "중앙일보 기사 캡처"
FB = "사진: 페이스북 캡처 / 중앙일보"
OMODA_SHOTS = [
    {"sh": [A("real/cap.jpg", credit=CAP), A("real/r1.jpg", "통째", punch=True, credit=FB)],
     "fx": [("hit_trailer_epic", "통째", 0.55)], "pop": ("통째로?!", R, "통째"), "shake": "통째"},
    {"sh": [A(2), A(1, "도로에서", zin=False)], "fx": [("drop_switch", "말레이시아", 0.4)]},
    {"sh": [A(3), A("real/r1b.jpg", "오모다", credit=FB)], "fx": [("boom_zoom_impact", "체리자동차")]},
    {"sh": [A("real/r2.jpg", credit=FB), A(4, "바퀴", punch=True, close=True)],
     "fx": [("glass_smash", "떨어져", 0.5)], "pop": ("바퀴 2개 이탈", R, "바퀴"), "shake": "빠졌음"},
    {"sh": [A(5), A(5, "난리가", close=True)], "fx": [("notify_message_pop", "SNS에", 0.5)]},
    {"sh": [A(6), A(6, "신규", close=True, punch=True)], "fx": [("wrong_bass_buzzer", "막아버렸음", 0.45)],
     "pop": ("등록 중단", R, "막아버렸음")},
    {"sh": [A(7), A(12, "용접", close=True)], "fx": [("hit_glass_suspense", "용접", 0.55)],
     "info": info_q("“뒷차축 용접 강도 부족”", "용접")},
    {"sh": [A(8), A(9, "리콜임", zin=False)], "fx": [("count_counter", "8878대", 0.5)],
     "info": info_n("말레이시아 리콜", 8878, "대", "전부 리콜", "8878대")},
    {"sh": [A("real/r1.jpg", credit=FB), A("real/r1.jpg", "처음이", close=True, credit=FB)],
     "fx": [("hit_trailer_epic", "처음이", 0.55)]},
    {"sh": [A(10), A(10, "한 달", close=True)], "fx": [("riser_simple", "2024년", 0.35), ("drop_futuristic", "한 달", 0.45)]},
    {"sh": [A(11), A(11, "넘어갔음", zin=False)], "fx": [("drum_rimshot", "넘어갔음", 0.45)],
     "info": info_c("2024년 그때 조치", [{"label": "리콜", "color": W, "rows": [["대수", "600대", Y]]},
                                       {"label": "차축 교체", "color": Y, "at": "60대", "rows": [["대수", "60대", R]]}], "600대")},
    {"sh": [A(12), A("real/r2.jpg", "또", punch=True, credit=FB)], "fx": [("punch_thud", "또")], "pop": ("또?!", R, "또"), "shake": "또"},
    {"sh": [A(13), A("real/r3.jpg", "155만", credit="사진: 신화=연합뉴스 / 중앙일보")],
     "fx": [("riser_simple", "올해", 0.35), ("drop_futuristic", "155만", 0.5)],
     "info": info_n("체리 해외 수출 (1~9월)", 155, "만 대", "+65.6%", "155만")},
    {"sh": [A(14)], "fx": [("pop_bubble", "탈 거임")]},
    "OUT:real/r1.jpg",
]

# ───────────────────────── anseongdrift ─────────────────────────
eps["anseongdrift"] = dict(
    src="https://n.news.naver.com/mnews/article/001/0016379063",
    src_note="연합뉴스 2026-10-15 '굉음 내며 새벽 아파트 앞 전기차 드리프트 20대 2명 검거' (권준우 기자) + 보배드림 베스트 10/14 '안성시 아파트 앞 취침시간 드리프트 소음'",
    t1="새벽 2시 아파트 앞", t2="전기차 드리프트 결말", bar="새벽 아파트 앞 끼이익 드리프트", cnt=None,
    title="#새벽 드리프트 결말",
    lines=[
        L("새벽 2시, 안성 아파트 단지 앞 교차로에서 끼이익 소리가 계속 났음.", 1,
          say="새벽 두 시, 안성 아파트 단지 앞 교차로에서 끼이익 소리가 계속 났음.", em=["끼이익"], fx=[("sting_glitch", "끼이익", 0.5)]),
        L("처음엔 다들 엔진 굉음인 줄 알았음.", 2, em=["엔진 굉음"]),
        L("근데 범인은 전기차 두 대였고, 소리는 타이어 마찰음이었음.", 3, em=["전기차 두 대"], em_color="yellow",
          fx=[("hit_glass_suspense", "전기차", 0.5)], pop=("전기차?!", Y, "전기차")),
        L("급가속하고 급브레이크 밟아서 차를 미끄러뜨리며 빙글빙글 돌았음.", 4, em=["빙글빙글"],
          fx=[("slip_game_slide", "미끄러뜨리며", 0.5)], shake="빙글빙글"),
        L("5분쯤 돌고 편의점 가서 놀다가, 2시간 뒤 새벽 4시에 또 와서 돌았음.", 5,
          say="오 분쯤 돌고 편의점 가서 놀다가, 두 시간 뒤 새벽 네 시에 또 와서 돌았음.", em=["또 와서"],
          fx=[("wrong_gameshow_buzz", "또", 0.45)], pop=("또?!", R, "또")),
        L("주민 영상이 커뮤니티에 퍼지고 국민신문고 민원만 6건이 들어왔음.", 6,
          say="주민 영상이 커뮤니티에 퍼지고 국민신문고 민원만 여섯 건이 들어왔음.", em=["6건"], fx=[("notify_message_pop", "커뮤니티에", 0.5)]),
        L("경찰은 대포차나 외국인일 수도 있다고 보고 CCTV를 뒤졌음.", 7,
          say="경찰은 대포차나 외국인일 수도 있다고 보고 씨씨티비를 뒤졌음.", em=["CCTV"], fx=[("typing_electronic", "CCTV를", 0.4)]),
        L("편의점 동선까지 추적해서 잡고 보니 평범한 20대 직장인 동네 선후배였음.", 8,
          say="편의점 동선까지 추적해서 잡고 보니 평범한 이십 대 직장인 동네 선후배였음.", em=["평범한"], em_color="yellow",
          fx=[("hit_trailer_epic", "평범한", 0.5)]),
        L("이유를 물어보니 호기심에 한번 해봤다고 함.", 9, em=["호기심"], fx=[("drum_rimshot", "해봤다고", 0.45)],
          info=info_q("“호기심에 한번 해봤어요”", "호기심에")),
        L("두 대가 나란히, 앞뒤로 줄지어 달려서 공동위험행위가 적용됐음.", 10, em=["공동위험행위"], em_color="yellow",
          fx=[("punch_thud", "공동위험행위가")]),
        L("공동위험행위는 2년 이하 징역이나 500만원 이하 벌금임.", 11,
          say="공동위험행위는 이 년 이하 징역이나 오백마넌 이하 벌금임.", em=["2년 이하 징역"],
          fx=[("riser_simple", "공동위험행위는", 0.35), ("drop_futuristic", "500만원", 0.5)],
          info=info_c("공동위험행위 처벌", [{"label": "징역", "color": Y, "rows": [["최대", "2년", R]]},
                                          {"label": "벌금", "color": W, "at": "500만원", "rows": [["최대", "500만원", R]]}], "2년")),
        L("님들은 새벽 드리프트, 이 정도 처벌이면 충분하다고 봄?", 12, fx=[("pop_bubble", "봄")]),
        OUT(3)],
    tags=GEN_TAGS + ", 타이어 공기압 측정기",
    desc="새벽 2시와 4시, 안성 아파트 앞 교차로에서 전기차 두 대가 급가속·급제동으로 드리프트.\n굉음 정체는 타이어 마찰음, 잡고 보니 평범한 20대 직장인 선후배.\n공동위험행위 혐의 입건과 처벌 수위까지 정리함.\n#shorts #드리프트 #공동위험행위 #난폭운전 #안성",
    cm="님들은 새벽 드리프트, 이 정도 처벌이면 충분하다고 봄?",
    proof=[("9/28 오전 2시·4시 안성 아양동 아파트 인근 교차로, 20대 남성 2명 전기차 급가속·급제동·급선회, 약 200m 구간", "연합뉴스 2026-10-15"),
           ("소음 = 엔진 아닌 타이어 마찰음, 2시 5분여 후 편의점, 4시 다시 5~6분", "연합뉴스 2026-10-15"),
           ("주민 영상 커뮤니티 확산, 112 신고 1건 + 국민신문고 민원 6건", "연합뉴스 2026-10-15"),
           ("대포차·외국인 가능성 열어두고 CCTV·편의점 동선 추적, 평범한 직장인·동네 선후배", "연합뉴스 2026-10-15"),
           ("'호기심에 한번 해봤다' 진술, 음주 아님", "연합뉴스 2026-10-15"),
           ("2대 나란히·앞뒤 대열 → 공동위험행위 형사입건·송치 예정", "연합뉴스 2026-10-15"),
           ("공동위험행위 2년 이하 징역 또는 500만원 이하 벌금", "도로교통법 제46조·제150조")],
    P={
        "a01": "a Korean apartment complex next to an empty intersection at 2am, orange streetlights, a few lit windows, wide shot",
        "a02": "a Korean man in his 40s in pajamas looking out of an apartment window at night, annoyed, seen from behind",
        "a03": "two white electric sedans with no badges stopped at a dark empty intersection at night under streetlights, faint tire smoke",
        "a04": "a white electric sedan drifting sideways in a circle at a night intersection, tire smoke, motion blur",
        "a05": "a Korean convenience store at 3am seen from outside, two young men silhouettes inside, two white cars parked in front",
        "a06": "a hand holding a smartphone playing a shaky night video of a car drifting, viewed in a dark bedroom, screen text blurred",
        "a07": "Korean police officers watching many CCTV monitors with night street footage in a control room",
        "a08": "two Korean men in their 20s in plain office clothes sitting at a police station desk, seen from behind, faces not visible",
        "a09": "close-up of black circular tire skid marks on asphalt at a crossroad in daylight",
        "a10": "two white electric sedans driving side by side on an empty city road at night, motion blur, streetlights",
        "a11": "a judge's gavel on a desk with legal documents, dramatic light, text unreadable",
        "a12": "a quiet Korean apartment complex at dawn blue hour, empty road in front",
    })

# ───────────────────────── leftblinker ─────────────────────────
eps["leftblinker"] = dict(
    src="https://n.news.naver.com/mnews/article/018/0006388530",
    src_note="이데일리 2026-10-15 '좌회전 차로여도 깜빡이 안 켜면 과태료 4만원' (홍수현 기자)",
    t1="좌회전 차로에서", t2="깜빡이 안 켜면 4만원", bar="좌회전 기다릴 때도 깜빡이?", cnt=None,
    title="#좌회전 깜빡이 4만원",
    lines=[
        L("좌회전 차로에서 신호 기다릴 때 깜빡이 켜고 있음?", 1, em=["깜빡이"], fx=[("click_switch", "깜빡이", 0.5)]),
        L("어차피 좌회전만 되는 차로인데 굳이 왜 켜냐는 사람 많음.", 2, em=["굳이"],
          info=info_q("“어차피 좌회전 차로인데?”", "굳이")),
        L("근데 이거 안 켜면 과태료 4만원임.", 3, say="근데 이거 안 켜면 과태료 사마넌임.", em=["4만원"], em_color="yellow",
          fx=[("drop_futuristic", "4만원임", 0.5)], pop=("4만원", R, "4만원임")),
        L("경찰이 이달 1일부터 12월 31일까지 깜빡이 집중단속 중임.", 4,
          say="경찰이 이달 일 일부터 십이 월 삼십일 일까지 깜빡이 집중단속 중임.", em=["집중단속"], fx=[("hit_trailer_epic", "집중단속", 0.5)]),
        L("도로교통법상 좌회전, 우회전, 차로 변경 전엔 무조건 켜야 함.", 5, em=["무조건"]),
        L("일반도로는 30m 전, 고속도로는 100m 전부터 켜고 끝날 때까지 유지해야 함.", 6,
          say="일반도로는 삼십 미터 전, 고속도로는 백 미터 전부터 켜고 끝날 때까지 유지해야 함.", em=["끝날 때까지"],
          info=info_c("깜빡이 켜는 시점", [{"label": "일반도로", "color": W, "rows": [["회전 전", "30m", Y]]},
                                         {"label": "고속도로", "color": Y, "at": "100m", "rows": [["회전 전", "100m", R]]}], "일반도로는")),
        L("좌회전 전용차로에서 신호 기다리는 동안에도 예외 없음.", 7, em=["예외 없음"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "예외", 0.45)]),
        L("경찰한테 걸리면 범칙금 3만원, 블박 신고로 걸리면 과태료 4만원임.", 8,
          say="경찰한테 걸리면 범칙금 삼마넌, 블박 신고로 걸리면 과태료 사마넌임.", em=["블박 신고"],
          info=info_c("승용차 기준", [{"label": "현장 적발", "color": W, "rows": [["범칙금", "3만원", Y]]},
                                    {"label": "블박 신고", "color": Y, "at": "블박", "rows": [["과태료", "4만원", R]]}], "경찰한테")),
        L("근데 10월부터 새로 생긴 처벌이라는 말은 사실 아님.", 9, say="근데 시 월부터 새로 생긴 처벌이라는 말은 사실 아님.",
          em=["사실 아님"], fx=[("wrong_bass_buzzer", "사실", 0.45)], pop=("가짜뉴스", Y, "사실")),
        L("깜빡이 의무는 1961년 도로교통법 만들 때부터 있었음.", 10,
          say="깜빡이 의무는 천구백육십일 년 도로교통법 만들 때부터 있었음.", em=["1961년"], fx=[("drop_switch", "1961년", 0.4)]),
        L("교차로 좌회전 때 깜빡이 켜는 비율은 75.7%, 4대 중 1대는 안 켬.", 11,
          say="교차로 좌회전 때 깜빡이 켜는 비율은 칠십오 점 칠 퍼센트, 네 대 중 한 대는 안 켬.", em=["4대 중 1대"],
          fx=[("punch_thud", "4대")], pop=("4대 중 1대", R, "4대")),
        L("게다가 벌점 10점 신설도 추진 중이라 내년엔 더 아파질 수 있음.", 12,
          say="게다가 벌점 십 점 신설도 추진 중이라 내년엔 더 아파질 수 있음.", em=["벌점 10점"], em_color="yellow",
          fx=[("hit_trailer_epic", "벌점", 0.5)]),
        L("님들은 좌회전 차로에서도 깜빡이 켜고 기다림?", 13, fx=[("pop_bubble", "기다림")]),
        OUT(1)],
    tags="자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 휴대폰 거치대, 차량용 비상삼각대, 하이패스 단말기",
    desc="좌회전 전용차로에서 신호 기다릴 때도 깜빡이 안 켜면 과태료 4만원.\n경찰이 10/1~12/31 방향지시등 집중단속 중, 10월 신설 처벌은 아님.\n켜는 시점·범칙금·벌점 신설 추진까지 정리함.\n#shorts #깜빡이 #방향지시등 #좌회전 #과태료",
    cm="님들은 좌회전 차로에서도 깜빡이 켜고 기다림?",
    proof=[("10/1~12/31 방향지시등 미사용 등 기초법규 집중단속(8~9월 계도)", "이데일리 2026-10-15 (경찰청)"),
           ("좌·우회전·유턴·차로변경 시 방향지시등, 일반도로 30m·고속도로 100m 전부터, 끝날 때까지 유지", "도로교통법 제38조"),
           ("좌회전 전용차로 대기 중에도 켜야 함", "이데일리 2026-10-15"),
           ("현장 적발 범칙금 승용 3만원, 공익신고 과태료 승용 4만원", "이데일리 2026-10-15"),
           ("10월 신설 처벌 아님, 1961년 법 제정 때부터 의무·1973년부터 범칙금", "이데일리 2026-10-15"),
           ("교차로 좌회전 점등률 약 75.7%", "국토부·교통안전공단 2025 교통문화지수 (이데일리 인용)"),
           ("벌점 10점 도입 추진, 입법예고 완료·이르면 내년 중순", "이데일리 2026-10-15")],
    P={
        "a01": "a driver's hand pushing the turn signal lever in a car stopped at a left turn lane, dashboard turn signal light glowing, close-up",
        "a02": "a Korean man in his 30s driving with one hand on the wheel, relaxed, waiting at a red light, side view",
        "a03": "a traffic fine notice envelope and paper on a car seat next to car keys, text unreadable",
        "a04": "a Korean traffic police officer standing at a busy city intersection in daytime, cars waiting in a left turn lane",
        "a05": "a car changing lanes on a Korean city road with its turn signal blinking, seen from behind",
        "a06": "a Korean expressway with cars, one car blinking to change lanes, aerial view, daytime",
        "a07": "a line of cars waiting in a left turn lane at a Korean intersection, the first car without blinker, rear view",
        "a08": "a dashcam view from a car showing the car ahead in a left turn lane, timestamp style overlay without readable text",
        "a09": "a smartphone showing a viral social media post, many comments, screen text blurred, held in hand",
        "a10": "an old black and white photo style street in 1960s Korea with vintage cars, nostalgic",
        "a11": "a busy Korean intersection seen from above with many cars turning left, daytime",
        "a12": "a Korean driver's license and a traffic violation notice on a desk, text unreadable, close-up",
        "a13": "a driver's point of view waiting at a left turn lane at sunset, turn signal indicator on dashboard",
    })

# ───────────────────────── g63leak ─────────────────────────
G = "a black boxy luxury off-road SUV with round headlights and spare-wheel-free tailgate, no badges or logos"
eps["g63leak"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1040042",
    src_note="보배드림 베스트 2026-10-15 '27년형 벤츠 G63, 출고 2주 만에 실내 누수… 제조사는 정상 범위?'",
    t1="3억 주고 산 G63", t2="세차하니 천장에서 물", bar="출고 2주 G바겐 실내 누수", cnt=None,
    title="#3억 G63 누수",
    lines=[
        L("3억 가까이 주고 2027년형 벤츠 G63을 새로 뽑은 차주가 있음.", 1,
          say="삼억 가까이 주고 이천이십칠 년형 벤츠 지육십삼을 새로 뽑은 차주가 있음.", em=["3억"], em_color="yellow",
          fx=[("cash_register_fake", "3억", 0.45)]),
        L("출고 2주 만에 노터치 자동세차를 돌렸음.", 2, say="출고 이 주 만에 노터치 자동세차를 돌렸음.", em=["노터치"]),
        L("근데 세차 도중 천장이랑 선바이저에서 물방울이 뚝뚝 떨어졌음.", 3, em=["물방울"],
          fx=[("hit_glass_suspense", "물방울이", 0.55)], pop=("누수?!", R, "물방울이"), shake="뚝뚝"),
        L("세차 물이 실내로 그대로 들어온 거임.", 4, em=["실내로"]),
        L("제조사에 물어봤더니 돌아온 답은, 정상 범위라 교환 환불은 어렵다.", 5, em=["정상 범위"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "정상", 0.45)], info=info_q("“정상 범위입니다”", "정상")),
        L("그리고 고압세차는 피하라는 안내가 끝이었음.", 6, em=["고압세차"], fx=[("drum_rimshot", "끝이었음", 0.45)]),
        L("차주는 수리 말고 교환이나 환불을 원하고 있음.", 7, em=["교환이나 환불"]),
        L("이럴 때 쓰는 게 자동차 교환 환불 제도, 일명 한국형 레몬법임.", 8, em=["레몬법"], em_color="yellow",
          fx=[("hit_trailer_epic", "레몬법임", 0.5)]),
        L("새 차 인도 후 1년 이내, 주행 2만km 이내일 때만 해당함.", 9,
          say="새 차 인도 후 일 년 이내, 주행 이만 킬로미터 이내일 때만 해당함.", em=["1년 이내"],
          info=info_c("레몬법 조건", [{"label": "기간", "color": W, "rows": [["인도 후", "1년 이내", Y]]},
                                    {"label": "주행", "color": Y, "at": "주행", "rows": [["거리", "2만km 이내", Y]]}], "새 차")),
        L("엔진, 브레이크 같은 중대하자는 2번, 일반하자는 3번 고쳐도 또 생기면 교환 환불 대상임.", 10,
          say="엔진, 브레이크 같은 중대하자는 두 번, 일반하자는 세 번 고쳐도 또 생기면 교환 환불 대상임.", em=["교환 환불 대상"],
          info=info_c("수리했는데 또 생기면", [{"label": "중대하자", "color": W, "rows": [["수리", "2번 후 재발", R]]},
                                            {"label": "일반하자", "color": Y, "at": "일반하자는", "rows": [["수리", "3번 후 재발", R]]}], "중대하자는")),
        L("누수는 보통 일반하자라서, 수리 기록부터 차곡차곡 남겨야 함.", 11, em=["수리 기록"], em_color="yellow",
          fx=[("punch_thud", "수리 기록부터")]),
        L("님들은 3억짜리 새 차에 이 정도 누수면 정상 범위라고 봄?", 12,
          say="님들은 삼억짜리 새 차에 이 정도 누수면 정상 범위라고 봄?", fx=[("pop_bubble", "봄")]),
        OUT(3)],
    tags="차량용 제습제, 세차 타월, 카샴푸, 자동차 블랙박스 2채널, 차량용 휴대폰 거치대",
    desc="3억 가까이 주고 뽑은 2027년형 벤츠 G63, 출고 2주 만에 노터치 세차하다 천장에서 물이 샘.\n제조사 답은 정상 범위·고압세차 피하라는 안내뿐.\n한국형 레몬법 교환·환불 조건까지 정리함.\n#shorts #벤츠 #G63 #누수 #레몬법",
    cm="님들은 3억짜리 새 차에 이 정도 누수면 정상 범위라고 봄?",
    proof=[("약 3억원 2027년형 G63 신차 출고 2주, 노터치 자동세차 중 천장·선바이저 물방울", "보배드림 2026-10-15 글쓴이"),
           ("제조사 답변 '정상 범위, 교환·환불 어려움, 고압세차 피하라'", "보배드림 2026-10-15 글쓴이"),
           ("글쓴이는 수리보다 교환·환불 우선 요구", "보배드림 2026-10-15 글쓴이"),
           ("교환·환불: 인도 1년·2만km 이내, 중대하자 2회 이상·일반하자 3회 이상 수리 후 재발 등", "자동차관리법 제47조의2")],
    P={
        "a01": f"{G} brand new, parked in front of a luxury car dealership at dusk",
        "a02": f"{G} going through a touchless automatic car wash, water jets spraying, foam",
        "a03": "interior of a luxury SUV, water droplets dripping from the headliner near the sun visor, close-up, wet leather seat",
        "a04": "close-up of water drops on a dark leather car seat and dashboard inside a luxury SUV",
        "a05": "a Korean man in his 40s on a phone call with a frustrated face in a car showroom service center, face partly turned away",
        "a06": "a high pressure car wash nozzle spraying water on a black SUV, close-up",
        "a07": "a Korean man standing next to a black luxury SUV holding documents, arguing with a service advisor, faces partly hidden",
        "a08": "a fresh lemon placed on top of a car key and documents on a desk, symbolic, text unreadable",
        "a09": "a car odometer showing low mileage and a calendar on the dashboard, close-up, numbers blurred",
        "a10": "a mechanic inspecting the roof seal of a black luxury SUV in a service bay",
        "a11": "a folder of car repair receipts and service records on a car seat, text unreadable",
        "a12": f"{G} parked alone in an underground garage, moody light",
    })

# ───────────────────────── autohold ─────────────────────────
eps["autohold"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1039960",
    src_note="보배드림 베스트 2026-10-15 '추돌사고 후 상대방이 입원까지 하겠다는데 어떻게 해야 할까요?'",
    t1="오토홀드 꺼놓고 쿵", t2="앞차가 입원하겠대", bar="살짝 박았는데 입원하겠다는 앞차", cnt=None,
    title="#오토홀드 추돌 입원",
    lines=[
        L("빨간불에 멈춰 있다가 잠깐 딴 데 정신이 팔렸음.", 1, em=["딴 데"]),
        L("근데 오토홀드를 꺼놨던 거라 차가 슬금슬금 굴러가서 앞차를 박았음.", 2, em=["오토홀드"], em_color="yellow",
          fx=[("punch_thud", "박았음")], pop=("쿵!", R, "박았음"), shake="박았음"),
        L("100% 내 과실이라 이건 다툴 생각 없음.", 3, say="백 퍼센트 내 과실이라 이건 다툴 생각 없음.", em=["100%"]),
        L("근데 사고 직후엔 앞차 운전자가 아픈 기색이 전혀 없었음.", 4, em=["전혀 없었음"]),
        L("그러다 나중에 보험사 통해서 입원하겠다고 연락이 옴.", 5, em=["입원"],
          fx=[("sting_cartoon_surprise", "입원하겠다고", 0.5)], pop=("입원?!", Y, "입원하겠다고")),
        L("수리비랑 통원치료는 다 해주겠는데, 입원은 과하다고 거절했음.", 6, em=["거절"]),
        L("그러자 상대가 경찰에 고소까지 해버렸음.", 7, em=["고소"], fx=[("hit_trailer_epic", "고소까지", 0.55)], shake="고소까지"),
        L("근데 형사처벌 걱정은 크게 안 해도 됨.", 8, em=["크게 안 해도"], fx=[("correct_ding", "됨", 0.4)]),
        L("종합보험 들어 있고 12대 중과실이 아니면 공소를 못 거는 게 원칙임.", 9,
          say="종합보험 들어 있고 십이대 중과실이 아니면 공소를 못 거는 게 원칙임.", em=["12대 중과실"], em_color="yellow",
          info=info_c("교통사고처리특례법", [{"label": "종합보험", "color": W, "rows": [["가입", "O", Y]]},
                                           {"label": "12대 중과실", "color": Y, "at": "12대", "rows": [["해당", "X", R]]}], "종합보험")),
        L("입원비도 내 보험 대인배상에서 나가는 거라 직접 낼 돈은 아님, 할증은 붙겠지만.", 10, em=["대인배상"],
          fx=[("drum_joke_accent", "할증은", 0.45)]),
        L("게다가 2023년부터 경상환자는 4주 넘게 치료받으려면 진단서를 내야 함.", 11,
          say="게다가 이천이십삼 년부터 경상환자는 사 주 넘게 치료받으려면 진단서를 내야 함.", em=["진단서"], em_color="yellow",
          info=info_n("경상환자 치료", 4, "주", "넘으면 진단서 필수", "4주")),
        L("님들은 이 정도 추돌에 입원, 과하다고 봄 아님 당연하다고 봄?", 12, fx=[("pop_bubble", "당연하다고")]),
        OUT(2)],
    tags=GEN_TAGS + ", 경광봉",
    desc="빨간불 정차 중 오토홀드를 꺼놔서 앞차를 살짝 추돌, 상대는 나중에 입원하겠다며 고소까지.\n종합보험 가입 시 형사처벌 원칙, 입원비는 누가 내는지 정리함.\n경상환자 4주 진단서 규정까지.\n#shorts #오토홀드 #추돌사고 #입원 #교통사고처리특례법",
    cm="님들은 이 정도 추돌에 입원, 과하다고 봄 아님 당연하다고 봄?",
    proof=[("적색 정차 중 딴 데 정신, 오토홀드 꺼져 앞차 추돌, 100% 과실 인정", "보배드림 2026-10-15 글쓴이"),
           ("현장선 아픈 기색 없었고 나중에 보험사 통해 입원 요구, 입원비 거절하자 경찰 고소", "보배드림 2026-10-15 글쓴이"),
           ("종합보험 가입 + 12대 중과실 아니면 공소 제기 불가(업무상과실치상)", "교통사고처리특례법 제3조·제4조"),
           ("경상환자 4주 초과 치료 시 진단서 제출(2023.1.1 사고부터)", "자동차손해배상보장법 시행규칙 개정(국토부)")],
    P={
        "a01": "a Korean man in his 30s in a car stopped at a red light, glancing at the smartphone in the console, from the passenger seat angle, face partly hidden",
        "a02": "a white sedan slowly bumping into the rear of a gray hatchback at a red light, low speed, slight dent, daytime city",
        "a03": "close-up of a car center console with the auto hold button and its indicator light off",
        "a04": "two drivers talking calmly next to two cars after a minor rear-end collision on a Korean city street, seen from distance",
        "a05": "a smartphone screen with an incoming call from an insurance company, held in hand, text blurred",
        "a06": "a hospital room bed with a patient's hand holding a remote, Korean hospital, no faces",
        "a07": "a Korean police station exterior at daytime with patrol cars parked",
        "a08": "a Korean man in his 30s sitting on a sofa reading documents with a relieved face, face partly turned away",
        "a09": "car insurance policy documents and a car key on a table, close-up, text unreadable",
        "a10": "an insurance adjuster in a suit inspecting a minor dent on a car bumper with a clipboard",
        "a11": "a doctor's medical certificate document and a stethoscope on a desk, text unreadable",
        "a12": "a minor dent on the rear bumper of a gray hatchback, close-up",
    })

# ───────────────────────── leftright ─────────────────────────
eps["leftright"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1040028",
    src_note="보배드림 베스트 2026-10-15 '좌회전 신호 좌회전 중 우회전 차량과 충돌 - 진행사항'",
    t1="좌회전 신호 받고 갔는데", t2="우회전 차가 쾅 8대2?", bar="신호 받고 좌회전했는데 8대2?", cnt=None,
    title="#좌회전 중 쾅 8대2",
    lines=[
        L("좌회전 신호 받고 정상적으로 좌회전하고 있었음.", 1, em=["좌회전 신호"]),
        L("그런데 옆에서 우회전하던 차가 내 차 2열 조수석 뒤쪽을 들이받았음.", 2,
          say="그런데 옆에서 우회전하던 차가 내 차 이 열 조수석 뒤쪽을 들이받았음.", em=["들이받았음"],
          fx=[("glass_smash", "들이받았음", 0.5)], pop=("쾅!!", R, "들이받았음"), shake="들이받았음"),
        L("근데 상대가 오히려 자기가 피해자라고 우김.", 3, em=["피해자"], fx=[("wrong_gameshow_buzz", "피해자라고", 0.45)]),
        L("그래서 경찰에 신고했고, 조사 결과 상대가 가해자로 확정됐음.", 4, em=["가해자로 확정"], em_color="yellow",
          fx=[("correct_ding", "확정됐음", 0.45)]),
        L("근데 이걸로 끝이 아니었음.", 5, fx=[("hit_glass_suspense", "아니었음", 0.45)]),
        L("상대는 내가 과속했다면서 기본 과실 8대2를 주장함.", 6, say="상대는 내가 과속했다면서 기본 과실 팔 대 이를 주장함.", em=["8대2"],
          info=info_b("상대가 주장하는 과실", "과속했다면서", [
              {"label": "우회전 차", "value": 0.8, "num": 80, "suffix": "%", "color": W},
              {"label": "나 (좌회전)", "value": 0.2, "num": 20, "suffix": "%", "color": Y, "at": "8대2를", "flash": "8대2를"}])),
        L("과실 조정하려고 대인 접수 취소해달라 했는데 그것도 거절했음.", 7, em=["거절"]),
        L("글쓴이는 많이 잡아도 9대1이라며 결국 소송을 통보했음.", 8, say="글쓴이는 많이 잡아도 구 대 일이라며 결국 소송을 통보했음.",
          em=["소송"], fx=[("hit_trailer_epic", "소송을", 0.55)], pop=("소송", R, "소송을")),
        L("참고로 과실 비율은 경찰이 아니라 보험사끼리, 안 되면 법원이 정함.", 9, em=["법원"], em_color="yellow"),
        L("경찰 조사는 형사 책임을 따지는 거라, 과실 비율이랑은 별개임.", 10, em=["별개"], fx=[("punch_thud", "별개임")]),
        L("소송 가면 블랙박스 원본이랑 경찰 교통사고사실확인원이 제일 중요함.", 11, em=["블랙박스 원본"], em_color="yellow"),
        L("님들은 신호 받고 좌회전하다 박혔는데 내 과실 20%, 납득됨?", 12,
          say="님들은 신호 받고 좌회전하다 박혔는데 내 과실 이십 퍼센트, 납득됨?", fx=[("pop_bubble", "납득됨")]),
        OUT(2)],
    tags=GEN_TAGS + ", 경광봉",
    desc="좌회전 신호 받고 좌회전하다 옆 차로 우회전 차에 2열 뒤쪽을 받힘.\n경찰은 상대를 가해자로 확정했는데 상대 보험은 과속 주장하며 8대2.\n과실 비율은 누가 정하는지, 소송 준비물까지 정리함.\n#shorts #과실비율 #좌회전 #교통사고 #블랙박스",
    cm="님들은 신호 받고 좌회전하다 박혔는데 내 과실 20%, 납득됨?",
    proof=[("좌회전 신호 좌회전 중 우회전 차와 충돌, 2열 조수석 후방", "보배드림 2026-10-15 글쓴이"),
           ("상대 피해자 주장 → 경찰 신고 → 상대 가해자 확정", "보배드림 2026-10-15 글쓴이"),
           ("상대 과속 주장하며 기본 8:2, 대인 접수 취소 거절, 글쓴이 9:1 주장·소송 통보", "보배드림 2026-10-15 글쓴이"),
           ("과실비율은 보험사 협의·분쟁심의·법원 판단, 경찰 판단은 형사 책임", "일반 보험 처리 절차")],
    P={
        "a01": "a car turning left on a green arrow at a busy Korean intersection, dashcam perspective, daytime",
        "a02": "a silver SUV hitting the rear passenger side door of a white sedan during a turn at an intersection, crumpled door, daytime",
        "a03": "a Korean middle-aged man gesturing and arguing next to a silver SUV at an accident scene, face partly turned away",
        "a04": "Korean traffic police officers examining two cars at an intersection accident scene, taking notes",
        "a05": "two damaged cars parked at the roadside after an accident, hazard lights blinking",
        "a06": "an insurance adjuster showing a tablet with charts to a frustrated driver, faces partly hidden, office",
        "a07": "a smartphone showing a phone call with an insurance company, held in a hand, text blurred",
        "a08": "a lawyer's desk with a lawsuit document and a car key, text unreadable",
        "a09": "a Korean courthouse exterior, daytime, wide shot",
        "a10": "a police officer writing a report at a desk next to a car accident photo printout, text unreadable",
        "a11": "a dashcam memory card and a printed police accident report on a car seat, close-up, text unreadable",
        "a12": "a damaged rear passenger door of a white sedan, close-up",
    })

# ───────────────────────── seltos ─────────────────────────
S = "a brand new compact Korean crossover SUV in white, no badges or logos"
eps["seltos"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1039947",
    src_note="보배드림 베스트 2026-10-14 '마산 기아자동차 서비스 센터 단차결함 환불 시키려다 3.6%저금리 뺏기게 생긴…' (글쓴이 주장)",
    t1="새 차 받으러 갔는데", t2="단차 보상이 10만원?", bar="출고 첫날 인수 거부한 셀토스", cnt=None,
    title="#새 차 단차 10만원",
    lines=[
        L("새로 산 기아 셀토스를 받으러 지점에 갔음.", 1, em=["셀토스"]),
        L("근데 폰 플래시로 비춰보니 보닛 틈 좌우가 다르고, B필러 쪽이 툭 튀어나와 있었음.", 2,
          say="근데 폰 플래시로 비춰보니 보닛 틈 좌우가 다르고, 비필러 쪽이 툭 튀어나와 있었음.", em=["툭 튀어나와"],
          fx=[("hit_glass_suspense", "튀어나와", 0.5)], pop=("단차?!", Y, "튀어나와")),
        L("딜러도 만져보더니 볼록한 것 같다고 인정했음.", 3, em=["볼록한"], info=info_q("“어… 볼록한 거 같네”", "볼록한")),
        L("근데 해결책이 정비소에서 볼트 풀었다 다시 조이면 된다는 거였음.", 4, em=["볼트"], fx=[("drum_rimshot", "조이면", 0.45)]),
        L("한 번도 안 탄 새 차에 손대기 싫어서 그 자리에서 인수를 거부했음.", 5, em=["인수를 거부"], em_color="yellow",
          fx=[("punch_thud", "거부했음")]),
        L("다음 날엔 10만원 줄 테니 그냥 가져가라는 제안이 왔다고 함.", 6, say="다음 날엔 십마넌 줄 테니 그냥 가져가라는 제안이 왔다고 함.",
          em=["10만원"], fx=[("coin_drop", "10만원", 0.5)], pop=("10만원?!", R, "10만원")),
        L("명의가 넘어갔으니 차에 문제 생기면 고객 책임이라는 말까지 들었다고 함.", 7, em=["고객 책임"],
          fx=[("wrong_bass_buzzer", "고객", 0.45)]),
        L("나중엔 C필러 철판까지 튀어나온 걸 찾았는데, 실리콘 쏘면 된다는 답이 왔다고 함.", 8,
          say="나중엔 씨필러 철판까지 튀어나온 걸 찾았는데, 실리콘 쏘면 된다는 답이 왔다고 함.", em=["실리콘"],
          fx=[("scratch_vinyl", "실리콘", 0.5)]),
        L("결국 본사에 내용증명을 두 번 보내고 나서야 환불이 확정됐음.", 9, em=["환불이 확정"], em_color="yellow",
          fx=[("correct_ding", "확정됐음", 0.45)]),
        L("근데 이번엔 3.6% 저금리 할부랑 보험 할인이 날아가게 생겼음.", 10,
          say="근데 이번엔 삼 점 육 퍼센트 저금리 할부랑 보험 할인이 날아가게 생겼음.", em=["3.6%"],
          fx=[("hit_trailer_epic", "날아가게", 0.5)], pop=("금리 손해", R, "날아가게")),
        L("글쓴이는 그 손해까지 보전해주기 전엔 서류 못 준다고 버티는 중임.", 11, em=["서류 못 준다고"]),
        L("님들은 환불이면 끝이라고 봄, 금리 손해까지 받아내야 한다고 봄?", 12, fx=[("pop_bubble", "받아내야")]),
        OUT(2)],
    tags="차량용 LED 손전등, " + GEN_TAGS,
    desc="새 셀토스 인수하러 갔다가 보닛 틈·B필러 단차 발견, 그 자리에서 인수 거부.\n10만원 보상 제안, 실리콘 쏘면 된다는 답까지 들었다는 차주 주장.\n내용증명 두 번 만에 환불 확정, 그런데 저금리 할부는?\n#shorts #셀토스 #단차 #신차결함 #환불",
    cm="님들은 환불이면 끝이라고 봄, 금리 손해까지 받아내야 한다고 봄?",
    proof=[("9/17 셀토스 인수 시 보닛 갭 좌우 차이·B필러 단차, 카마스터 '볼록한 거 같다'", "보배드림 2026-10-14 글쓴이 주장"),
           ("정비소에서 볼트 풀고 조이면 된다 → 인수 거부·보류", "보배드림 2026-10-14 글쓴이 주장"),
           ("10만원 지급 제안, '명의 넘어가 파손·문제 생기면 고객 책임' 발언", "보배드림 2026-10-14 글쓴이 주장(녹취 있다고 함)"),
           ("C필러 철판 돌출 발견, 지점장 '실리콘 쏘면 된다'", "보배드림 2026-10-14 글쓴이 주장"),
           ("내용증명 2회(10/12 두 번째) 후 10/13 환불 확정 통보", "보배드림 2026-10-14 글쓴이 주장"),
           ("우리카드 오토할부 3.6% 우대금리·동일증권 보험 손해 보전 요구, 서류 제출 보류", "보배드림 2026-10-14 글쓴이 주장")],
    P={
        "a01": f"{S} parked at a Korean car dealership lot in the evening, delivery day, ribbon-free",
        "a02": "a smartphone flashlight shining on an uneven panel gap between the front and rear doors of a white SUV at night, close-up",
        "a03": "a car salesman in a suit touching the door panel of a white SUV with his fingers at night, face not visible",
        "a04": "a mechanic's wrench loosening a bolt near a car door hinge, close-up, workshop",
        "a05": f"a Korean woman and man standing away from {S} in a dealership parking lot at night, refusing, seen from behind",
        "a06": "a hand holding out a white envelope of money across a dealership desk, faces not visible",
        "a07": "a car key and registration documents on a dealership desk, tense mood, text unreadable",
        "a08": "a silicone sealant gun next to a raised metal panel on the rear pillar of a white car, close-up",
        "a09": "a certified mail envelope and documents on a desk, text unreadable, close-up",
        "a10": "a car loan document with a calculator and a credit card on a table, text unreadable",
        "a11": "a Korean woman in her 30s holding documents and a phone, determined, face partly turned away, at home",
        "a12": f"{S} parked alone in an outdoor lot at dusk",
    })

# ───────────────────────── bikeban ─────────────────────────
eps["bikeban"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1039904",
    src_note="보배드림 베스트 2026-10-14 '폭주족 참교육 방법 ( 돈 줄 끊기 )'",
    t1="폭주족 잡는 방법", t2="돈줄을 끊으면 된다?", bar="폭주족 배달 계정 정지하자", cnt=None,
    title="#폭주족 돈줄 끊기",
    lines=[
        L("국경일만 되면 천안에 폭주족이 떼로 몰려나와 난장판을 만듦.", 1, em=["폭주족"], fx=[("whoosh_cine_fast", "몰려나와", 0.4)]),
        L("근데 보배드림에 이걸 끝낼 방법이라며 글이 하나 올라왔음.", 2, em=["끝낼 방법"]),
        L("폭주족 상당수가 낮엔 배달 라이더라는 주장임.", 3, em=["배달 라이더"], em_color="yellow",
          fx=[("hit_glass_suspense", "배달", 0.5)]),
        L("그러니까 경찰이랑 배달앱이 손잡고 폭주 가담자 계정을 영구 정지시키자는 거임.", 4, em=["영구 정지"],
          fx=[("hit_trailer_epic", "영구", 0.55)], pop=("계정 정지", R, "영구"), shake="영구"),
        L("오토바이 압수는 절차가 복잡한데, 돈줄은 바로 막을 수 있다는 논리임.", 5, em=["돈줄"],
          info=info_c("글쓴이 논리", [{"label": "오토바이 압수", "color": W, "rows": [["절차", "복잡", R]]},
                                    {"label": "계정 정지", "color": Y, "at": "돈줄은", "rows": [["절차", "간단", Y]]}], "압수는")),
        L("가족이나 지인 명의로 몰래 가입하면 어쩌냐는 반론도 있음.", 6, em=["지인 명의"], fx=[("wrong_gameshow_buzz", "지인", 0.45)]),
        L("그래서 배달 시작할 때마다 얼굴 인증을 받게 하자고 함.", 7, em=["얼굴 인증"], em_color="yellow",
          fx=[("shutter_digital", "얼굴", 0.5)]),
        L("실제로 우버는 기사한테 셀카 인증으로 본인 확인을 시키고 있음.", 8, em=["셀카 인증"]),
        L("명의 빌려준 사람까지 같이 자격을 박탈하자는 얘기도 있음.", 9, em=["자격을 박탈"]),
        L("반대로 폭주랑 생계를 엮는 건 과하다는 의견도 만만치 않음.", 10, em=["과하다는"], fx=[("drum_joke_accent", "과하다는", 0.45)]),
        L("참고로 떼 지어 폭주하면 공동위험행위로 2년 이하 징역이나 500만원 이하 벌금임.", 11,
          say="참고로 떼 지어 폭주하면 공동위험행위로 이 년 이하 징역이나 오백마넌 이하 벌금임.", em=["공동위험행위"], em_color="yellow",
          fx=[("drop_futuristic", "500만원", 0.5)], info=info_n("공동위험행위 벌금", 500, "만원", "최대", "500만원")),
        L("님들은 폭주족 배달 계정 정지, 찬성임 반대임?", 12, fx=[("pop_bubble", "반대임")]),
        OUT(4)],
    tags=GEN_TAGS + ", 경광봉",
    desc="국경일마다 천안에 몰려나오는 폭주족, 낮엔 배달 라이더라면 배달앱 계정을 영구 정지하자는 제안.\n명의 도용 막는 얼굴 인증·명의 대여자 처벌까지.\n공동위험행위 처벌 수위도 정리함.\n#shorts #폭주족 #배달 #공동위험행위 #천안",
    cm="님들은 폭주족 배달 계정 정지, 찬성임 반대임?",
    proof=[("국경일마다 천안 대규모 폭주족", "보배드림 2026-10-14 글쓴이"),
           ("폭주족 다수가 낮엔 배달 라이더라는 주장, 경찰·플랫폼 연계 계정 영구 정지 제안", "보배드림 2026-10-14 글쓴이 주장"),
           ("명의 도용 대책: 안면 인증 로그인 의무화·명의 대여자 연대 처벌", "보배드림 2026-10-14 글쓴이 주장"),
           ("우버 기사 실시간 셀카 본인 확인(Real-Time ID Check)", "Uber 공식 안내"),
           ("공동위험행위 2년 이하 징역 또는 500만원 이하 벌금", "도로교통법 제46조·제150조")],
    P={
        "a01": "a large group of motorcycles riding at night on a Korean city road with headlights, motion blur, riders' faces covered by helmets",
        "a02": "a smartphone showing a community forum post with many comments, held in hand, text blurred",
        "a03": "a delivery motorcycle with a delivery box parked in front of a restaurant in daytime, Korean city, rider in helmet from behind",
        "a04": "a smartphone screen showing a delivery rider app with an account suspended style red warning icon, no readable text",
        "a05": "police officers standing next to a seized motorcycle in a police station yard",
        "a06": "two smartphones side by side with delivery app login screens, hands of different people, text blurred",
        "a07": "a delivery rider in a helmet holding a smartphone up to take a selfie for face verification, face covered by helmet visor",
        "a08": "a ride-hailing driver holding a phone for a selfie verification inside a car, face turned away, phone screen blurred",
        "a09": "an ID card being handed from one hand to another, close-up, text unreadable",
        "a10": "a tired delivery rider sitting on his motorcycle at night eating a snack, helmet on, from behind",
        "a11": "a judge's gavel on a desk with legal documents, dramatic light, text unreadable",
        "a12": "an empty Korean city road at night after motorcycles passed, tail light streaks",
    })

# ───────────────────────── malibubus ─────────────────────────
eps["malibubus"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1039958",
    src_note="보배드림 베스트 2026-10-14 '전세버스와 같이 좌회전 중 사고입니다. 병원치료 안 받고 100:0 제안하던데…'",
    t1="버스랑 좌회전하다 쾅", t2="병원 안 가면 100대0?", bar="병원 안 가면 100대0 해준대", cnt=None,
    title="#조건부 100대0",
    lines=[
        L("말리부를 몰고 전세버스랑 나란히 좌회전하다가 부딪혔음.", 1, em=["전세버스"],
          fx=[("glass_smash", "부딪혔음", 0.5)], shake="부딪혔음"),
        L("출동한 경찰도, 내 보험사 현장 직원도 버스 잘못 같다고 했음.", 2, em=["버스 잘못"]),
        L("근데 정작 보상 담당자는 나한테도 과실이 있을 수 있다고 함.", 3, em=["과실"], fx=[("wrong_gameshow_buzz", "과실이", 0.45)]),
        L("몇 퍼센트인지, 내가 뭘 잘못했는지는 설명도 없었음.", 4, em=["설명도 없었음"]),
        L("그러다 버스 쪽에서 조건을 하나 걸어왔음.", 5, em=["조건"], fx=[("hit_glass_suspense", "조건을", 0.45)]),
        L("내가 병원에 안 가면 100대0으로 해주겠다는 거임.", 6, say="내가 병원에 안 가면 백 대 영으로 해주겠다는 거임.", em=["100대0"],
          em_color="yellow", pop=("조건부?!", Y, "100대0으로"), info=info_q("“병원 안 가면 100:0 해줄게요”", "병원에")),
        L("경찰은 정식 접수하면 상대가 불이익 받는다며 굳이 하겠냐고 했다고 함.", 7, em=["정식 접수"],
          fx=[("drum_rimshot", "굳이", 0.45)]),
        L("근데 과실 비율이랑 치료받을 권리는 원래 따로 노는 거임.", 8, em=["따로"], em_color="yellow",
          fx=[("hit_trailer_epic", "따로", 0.5)]),
        L("상대가 100% 과실이면 내 치료비는 전부 상대 보험에서 나가는 게 맞음.", 9,
          say="상대가 백 퍼센트 과실이면 내 치료비는 전부 상대 보험에서 나가는 게 맞음.", em=["전부 상대 보험"]),
        L("그러니까 아픈데 이 조건 받으면 결국 나만 손해임.", 10, em=["나만 손해"], fx=[("punch_thud", "손해임")]),
        L("몸이 괜찮으면 받아도 되지만, 찜찜하면 진료부터 받고 과실은 따로 다투는 게 정석임.", 11, em=["진료부터"], em_color="yellow"),
        L("님들은 병원 포기하고 100대0 받음, 아님 치료받고 다툼?", 12, say="님들은 병원 포기하고 백 대 영 받음, 아님 치료받고 다툼?",
          fx=[("pop_bubble", "다툼")]),
        OUT(6)],
    tags=GEN_TAGS + ", 경광봉",
    desc="전세버스와 나란히 좌회전하다 충돌, 경찰·현장직원은 버스 잘못이라는데 보상담당은 내 과실 가능성 언급.\n버스 측 조건은 병원 안 가면 100:0.\n과실비율과 치료받을 권리가 왜 별개인지 정리함.\n#shorts #과실비율 #100대0 #교통사고 #보험",
    cm="님들은 병원 포기하고 100대0 받음, 아님 치료받고 다툼?",
    proof=[("2015년식 말리부 vs 전세버스 함께 좌회전 중 충돌", "보배드림 2026-10-14 글쓴이"),
           ("현장 경찰·보험사 현장직원 '버스 측 잘못' 취지, 보상담당자 '일부 과실 가능' 설명 없음", "보배드림 2026-10-14 글쓴이"),
           ("상대 측 '병원 안 가면 100:0' 제안", "보배드림 2026-10-14 글쓴이"),
           ("경찰 '정식 접수 시 상대 불이익' 취지 설명, 접수 보류", "보배드림 2026-10-14 글쓴이"),
           ("과실 100% 상대면 대인배상으로 내 치료비 전액", "자동차보험 대인배상 일반 원칙")],
    P={
        "a01": "a dark blue midsize sedan and a large white tour bus turning left side by side at a Korean intersection, the bus side scraping the sedan, daytime",
        "a02": "a Korean police officer and an insurance field agent in a vest looking at a scraped sedan next to a tour bus",
        "a03": "an insurance claims office desk with a phone and documents, a worker on the phone, face not visible",
        "a04": "a Korean man in his 40s looking puzzled at his phone in a car, face partly turned away",
        "a05": "a large white tour bus parked on the roadside with hazard lights on, overcast",
        "a06": "a hospital entrance in Korea with a sign shape blurred, a man hesitating at the door, from behind",
        "a07": "a Korean police officer talking to a driver at a roadside, both seen from behind",
        "a08": "a split image concept of a scale with a car on one side and a medical cross on the other, studio photo",
        "a09": "a hospital receipt and insurance documents on a table, text unreadable, close-up",
        "a10": "a man holding his stiff neck with one hand while driving, from behind, daytime",
        "a11": "a Korean clinic doctor examining a man's neck, faces partly hidden",
        "a12": "a scraped side of a dark blue sedan, close-up",
    })

# ───────────────────────── xt4stall ─────────────────────────
X = "a compact white American luxury crossover SUV with vertical LED headlights, no badges or logos"
eps["xt4stall"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1039945",
    src_note="보배드림 베스트 2026-10-15 '캐딜락 XT4 주행중 시동꺼짐'",
    t1="엄마 차가 달리다가", t2="시동이 그냥 꺼짐", bar="달리다 시동 꺼지는 캐딜락", cnt=None,
    title="#주행 중 시동꺼짐",
    lines=[
        L("3년 좀 넘은 캐딜락 XT4가 달리다가 갑자기 시동이 꺼졌음.", 1,
          say="삼 년 좀 넘은 캐딜락 엑스티포가 달리다가 갑자기 시동이 꺼졌음.", em=["시동이 꺼졌음"],
          fx=[("sting_glitch", "꺼졌음", 0.5)], pop=("시동 OFF", R, "꺼졌음"), shake="꺼졌음"),
        L("운전 경력 40년 넘은 어머니가 출퇴근용으로 타는 차였음.", 2, say="운전 경력 사십 년 넘은 어머니가 출퇴근용으로 타는 차였음.",
          em=["어머니"]),
        L("센터에 갔더니 기름 잘못 넣은 거 아니냐고 의심함.", 3, em=["기름 잘못"], info=info_q("“혼유 아니에요?”", "기름")),
        L("근데 어머니는 20년 가까이 직원이 넣어주는 주유소만 다녔음.", 4,
          say="근데 어머니는 이십 년 가까이 직원이 넣어주는 주유소만 다녔음.", em=["직원이 넣어주는"], fx=[("drum_rimshot", "다녔음", 0.45)]),
        L("2~3주 뒤 똑같이 또 꺼졌음.", 5, say="이삼 주 뒤 똑같이 또 꺼졌음.", em=["또 꺼졌음"],
          fx=[("wrong_bass_buzzer", "또", 0.45)], pop=("또?!", R, "또")),
        L("이번엔 부품 문제라며 해외에서 오는 데 한 달이 걸린다고 함.", 6, em=["한 달"]),
        L("한 달 기다려서 달았는데 시동이 안 걸림.", 7, em=["안 걸림"], fx=[("wrong_trombone", "안 걸림", 0.5)]),
        L("국내에서 구한 다른 부품으로 해봤는데 그것도 안 됨.", 8, em=["그것도 안 됨"]),
        L("주행 중 시동꺼짐은 레몬법에서 중대하자로 치는 원동기 결함임.", 9, em=["중대하자"], em_color="yellow",
          fx=[("hit_trailer_epic", "중대하자로", 0.5)]),
        L("근데 레몬법은 인도 1년, 2만km 이내 차만 돼서 이 차는 해당이 안 됨.", 10,
          say="근데 레몬법은 인도 일 년, 이만 킬로미터 이내 차만 돼서 이 차는 해당이 안 됨.", em=["해당이 안 됨"],
          fx=[("wrong_gameshow_buzz", "해당이", 0.45)],
          info=info_c("레몬법 대상", [{"label": "조건", "color": W, "rows": [["기간", "1년 이내", Y]]},
                                    {"label": "이 차", "color": R, "at": "이 차는", "rows": [["기간", "3년 넘음", R]]}], "레몬법은")),
        L("이럴 땐 수리 이력을 다 모아서 한국소비자원 분쟁조정을 신청하는 게 현실적임.", 11, em=["분쟁조정"], em_color="yellow"),
        L("님들은 달리다 시동 꺼지는 차, 고쳐서 계속 탈 거임?", 12, fx=[("pop_bubble", "탈 거임")]),
        OUT(1)],
    tags="점프스타터, " + GEN_TAGS,
    desc="출고 3년 조금 넘은 캐딜락 XT4, 주행 중 시동꺼짐이 두 번.\n센터는 혼유 의심, 해외 부품 한 달 기다려 달았는데도 안 걸림.\n레몬법 대상이 아닌 이유와 현실적인 대응까지 정리함.\n#shorts #캐딜락 #시동꺼짐 #레몬법 #차량결함",
    cm="님들은 달리다 시동 꺼지는 차, 고쳐서 계속 탈 거임?",
    proof=[("출고 3년 조금 넘은 XT4, 운전경력 40년+ 어머니 단거리 출퇴근용, 최근 1~2달 주행 중 시동꺼짐", "보배드림 2026-10-15 글쓴이"),
           ("센터 혼유 추측, 20년 가까이 유인 주유소만 이용", "보배드림 2026-10-15 글쓴이"),
           ("2~3주 뒤 같은 증상, 해외 부품 한 달 → 장착 후에도 시동 안 됨, 국내 부품도 안 됨(10/14)", "보배드림 2026-10-15 글쓴이"),
           ("교환·환불 대상: 인도 1년·2만km 이내, 원동기 등 중대하자", "자동차관리법 제47조의2·제47조의3"),
           ("한국소비자원 분쟁조정 신청", "한국소비자원 안내")],
    P={
        "a01": f"{X} stalled on the side of a Korean city road with hazard lights on, daytime",
        "a02": "an elderly Korean woman's hands on the steering wheel of a car, close-up, daytime",
        "a03": "a service advisor at a car service center counter talking to a customer, faces not visible",
        "a04": "a gas station attendant filling up a white SUV at a full-service gas station in Korea, from behind",
        "a05": "a car dashboard with warning lights on and the engine off, close-up",
        "a06": "an auto part in a shipping box with international shipping labels, text unreadable",
        "a07": f"a mechanic installing a new part in the engine bay of {X} in a service center",
        "a08": "a frustrated mechanic standing next to an open hood of a white SUV in a service bay, from behind",
        "a09": "close-up of an engine bay of a modern crossover with dramatic light",
        "a10": "a calendar and car service records on a desk showing a long period, text unreadable",
        "a11": "a person filling out a consumer dispute form with a pen on a desk, text unreadable",
        "a12": f"{X} parked in a service center lot, overcast",
    })

# ───────────────────────── v800brake ─────────────────────────
V = "a huge luxurious black Chinese electric MPV minivan with chrome grille, no badges or logos"
eps["v800brake"] = dict(
    src="https://n.news.naver.com/mnews/article/076/0004455848",
    src_note="스포츠조선 2026-10-14 '급제동 후 브레이크 페달 부러졌다…수억원짜리 中 전기차 3대 같은 부위 파손' (장종호 기자)",
    t1="2억짜리 중국 전기차", t2="브레이크 페달이 뚝", bar="급제동 몇 번에 부러진 페달", cnt=None,
    title="#2억 차 페달 뚝",
    lines=[
        L("최대 2억원짜리 중국 초호화 전기차의 브레이크 페달이 부러졌음.", 1,
          say="최대 이어권짜리 중국 초호화 전기차의 브레이크 페달이 부러졌음.", em=["브레이크 페달"],
          fx=[("glass_break", "부러졌음", 0.5)], pop=("뚝!", R, "부러졌음"), shake="부러졌음"),
        L("화웨이랑 장화이자동차가 같이 만든 대형 MPV, 존계 V800임.", 2,
          say="화웨이랑 장화이자동차가 같이 만든 대형 엠피브이, 존계 브이팔백임.", em=["화웨이"], em_color="yellow"),
        L("마이바흐를 뛰어넘는다는 말까지 나왔던 차임.", 3, em=["마이바흐"], fx=[("drum_joke_accent", "뛰어넘는다는", 0.4)]),
        L("중국 자동차 플랫폼이 시속 100km에서 급제동하는 테스트를 했음.", 4,
          say="중국 자동차 플랫폼이 시속 백 킬로미터에서 급제동하는 테스트를 했음.", em=["급제동"]),
        L("첫 번째 차는 세 번째 급제동에서 페달 지지대가 부러졌음.", 5, em=["세 번째"], fx=[("glass_break", "부러졌음", 0.45)]),
        L("한 대만 문제인가 싶어서 새 차로 다시 했는데, 네 번째에 또 부러짐.", 6, em=["또 부러짐"],
          fx=[("wrong_bass_buzzer", "또", 0.45)], pop=("또?!", R, "또")),
        L("세 번째 새 차까지 넣었는데 이것도 똑같이 부러졌음.", 7, em=["똑같이"],
          fx=[("hit_trailer_epic", "똑같이", 0.5)], info=info_n("테스트한 새 차", 3, "대", "전부 파손", "똑같이")),
        L("심지어 세 대 다 서로 다른 공장에서 만든 차였음.", 8, em=["다른 공장"], em_color="yellow"),
        L("뜯어보니 다른 차는 보강판이 2~3겹인데, 이 차는 한 겹이었다고 함.", 9,
          say="뜯어보니 다른 차는 보강판이 두세 겹인데, 이 차는 한 겹이었다고 함.", em=["한 겹"],
          info=info_c("페달 지지대 보강판", [{"label": "다른 차", "color": W, "rows": [["보강판", "2~3겹", Y]]},
                                           {"label": "V800", "color": R, "at": "이 차는", "rows": [["보강판", "1겹", R]]}], "보강판이")),
        L("다만 일반 주행보다 훨씬 센 힘으로 반복 테스트했다는 반론도 있음.", 10, em=["반론"]),
        L("그래도 영상 나온 날 장화이 주가는 하한가까지 떨어졌음.", 11, em=["하한가"], em_color="yellow",
          fx=[("drop_dramatic_bass", "하한가까지", 0.5)]),
        L("님들은 이거 결함이라고 봄, 테스트가 과했다고 봄?", 12, fx=[("pop_bubble", "과했다고")]),
        OUT(1)],
    tags=GEN_TAGS + ", 브레이크 패드 경고등 테스터",
    desc="화웨이·장화이 합작 초호화 전기 MPV 존계 V800, 시속 100km 급제동 시험에서 새 차 3대 모두 브레이크 페달 지지대 파손.\n세 대 다 다른 공장 생산, 보강판은 한 겹이었다는 주장.\n과도한 시험이라는 반론과 하한가까지 정리함.\n#shorts #중국차 #화웨이 #브레이크 #전기차",
    cm="님들은 이거 결함이라고 봄, 테스트가 과했다고 봄?",
    proof=[("존계 V800 = 화웨이·장화이 협력 초고급 MPV, 76.6만~101.6만 위안(약 1.5억~2억원)", "스포츠조선 2026-10-14"),
           ("'메르세데스-마이바흐를 뛰어넘는 성능이라더니' 논란", "스포츠조선 2026-10-14"),
           ("둥처디 10/8 시속 100km 긴급제동 시험, 1호차 3번째·2호차 4번째·3호차도 페달 지지대 파손, 서로 다른 공장", "스포츠조선 2026-10-14 (펑파이신문 등 인용)"),
           ("비교 차량 보강판 2~3개, V800 한 겹 구조라는 시험 측 주장", "스포츠조선 2026-10-14"),
           ("일반 주행보다 강한 반복 제동이라 결함 단정 어렵다는 반론, 제조사 사실관계 확인 중", "스포츠조선 2026-10-14"),
           ("장화이 주가 10/8 장중 하한가, 종가 -10.01%", "스포츠조선 2026-10-14")],
    P={
        "a01": "close-up of a broken car brake pedal arm snapped at the pivot, in a car footwell, dramatic light",
        "a02": f"{V} parked in front of a modern glass building in China, wide shot",
        "a03": f"luxurious rear cabin of {V} with captain seats and ambient lighting",
        "a04": f"{V} braking hard on a test track with cones, nose diving, motion blur, daytime",
        "a05": "a test driver's foot pressing a brake pedal hard, close-up, footwell",
        "a06": f"two identical {V} on a test track with technicians and cameras, overcast",
        "a07": "three broken brake pedal assemblies lined up on a workbench, close-up",
        "a08": "an aerial view of three different large car factories in China, industrial",
        "a09": "close-up comparison of two brake pedal brackets on a workbench, one with thick layered reinforcement plates and one with a single thin plate",
        "a10": "an automotive engineer with a clipboard watching a brake test from the side of a track, face not visible",
        "a11": "a stock trading screen with red falling chart lines, blurred numbers",
        "a12": f"{V} parked alone in a showroom, spotlight",
    })

# ───────────────────────── haeundae6 ─────────────────────────
eps["haeundae6"] = dict(
    src="https://n.news.naver.com/mnews/article/629/0000542270",
    src_note="더팩트 2026-10-15 '해운대서 승용차 추돌 뒤 400m 달려 또 쾅…6명 경상' (손연우 기자) + CBS노컷뉴스 같은 날",
    t1="신호 대기 차를 쾅", t2="400m 더 가서 또 쾅", bar="해운대 차 6대 연쇄 추돌", cnt=None,
    title="#400m 가서 또 쾅",
    lines=[
        L("14일 오후 5시 40분, 해운대 온천사거리 근처에서 사고가 났음.", 1,
          say="십사 일 오후 다섯 시 사십 분, 해운대 온천사거리 근처에서 사고가 났음.", em=["해운대"]),
        L("20대 운전자가 몰던 승용차가 신호 대기 중인 차를 들이받았음.", 2,
          say="이십 대 운전자가 몰던 승용차가 신호 대기 중인 차를 들이받았음.", em=["들이받았음"],
          fx=[("glass_smash", "들이받았음", 0.5)], pop=("쾅!!", R, "들이받았음"), shake="들이받았음"),
        L("맞은 차는 그 충격에 밀려서 맞은편 차로의 차 두 대를 또 박았음.", 3, em=["맞은편"], fx=[("punch_heavy", "박았음", 0.5)]),
        L("근데 이게 끝이 아니었음.", 4, fx=[("hit_glass_suspense", "아니었음", 0.45)]),
        L("처음 박은 차가 멈추지 않고 400m를 더 달렸음.", 5, say="처음 박은 차가 멈추지 않고 사백 미터를 더 달렸음.", em=["400m"],
          em_color="yellow", fx=[("riser_simple", "멈추지", 0.35)], pop=("400m?!", Y, "400m를")),
        L("그리고 또 신호 대기 중이던 차 두 대를 연달아 박고서야 멈췄음.", 6, em=["연달아"],
          fx=[("glass_smash", "박고서야", 0.5)], shake="박고서야"),
        L("차 6대가 부서지고 운전자 6명이 다쳤음, 다행히 모두 경상임.", 7,
          say="차 여섯 대가 부서지고 운전자 여섯 명이 다쳤음, 다행히 모두 경상임.", em=["모두 경상"],
          info=info_n("연쇄 추돌", 6, "대", "차량 파손", "6대가")),
        L("음주는 아니었고, 경찰이 블랙박스로 원인을 조사 중임.", 8, em=["음주는 아니었고"]),
        L("이런 연쇄 추돌에서 밀려서 박은 차는 보통 과실이 없음.", 9, em=["과실이 없음"], em_color="yellow",
          fx=[("correct_ding", "없음", 0.4)]),
        L("처음 원인을 만든 차가 뒤에 이어진 사고까지 책임지는 게 원칙임.", 10, em=["원칙"], fx=[("punch_thud", "원칙임")]),
        L("그래서 신호 대기 중에도 블랙박스 앞뒤가 다 찍히고 있어야 함.", 11, em=["앞뒤"], em_color="yellow"),
        L("님들은 400m 동안 왜 못 멈췄다고 봄?", 12, say="님들은 사백 미터 동안 왜 못 멈췄다고 봄?", fx=[("pop_bubble", "봄")]),
        OUT(2)],
    tags=GEN_TAGS + ", 경광봉",
    desc="부산 해운대 온천사거리 인근, 신호 대기 차를 들이받은 승용차가 400m를 더 달려 또 2대를 추돌.\n밀린 차가 맞은편 2대까지, 총 6대 파손·6명 경상, 음주 아님.\n연쇄 추돌 때 밀려서 박은 차 과실까지 정리함.\n#shorts #해운대 #연쇄추돌 #교통사고 #블랙박스",
    cm="님들은 400m 동안 왜 못 멈췄다고 봄?",
    proof=[("10/14 오후 5시40분 해운대구 중동 해운대온천사거리 인근, 20대 여성 운전 승용차가 신호대기 차 추돌", "더팩트·CBS노컷뉴스 2026-10-15"),
           ("밀린 차가 맞은편 주행 차 2대와 충돌", "더팩트·CBS노컷뉴스 2026-10-15"),
           ("가해 차 약 400m 더 주행 후 신호대기 차 2대 추돌", "더팩트·CBS노컷뉴스 2026-10-15"),
           ("6대 파손·운전자 6명 경상, 음주 아님, 블랙박스·진술로 조사 중", "더팩트·CBS노컷뉴스 2026-10-15"),
           ("연쇄추돌에서 밀린 차량은 원칙적으로 과실 없음(정상 정차 시)", "자동차사고 과실비율 인정기준 일반 원칙")],
    P={
        "a01": "a busy intersection in Haeundae Busan in the late afternoon, high-rise buildings, cars waiting at a red light",
        "a02": "a compact car crashing into the rear of a sedan waiting at a red light on a Korean city road, debris, late afternoon",
        "a03": "a pushed sedan crossing into the opposite lane and hitting oncoming cars, Korean city road, debris",
        "a04": "several damaged cars scattered on a Korean city road after a chain collision, hazard lights, people standing at a distance",
        "a05": "a compact car with a smashed front driving away down a city road, motion blur, rear view",
        "a06": "a compact car crashed into two cars stopped at a red light, crumpled metal, late afternoon city",
        "a07": "paramedics and police at a chain collision scene in a Korean city, ambulance, faces not visible",
        "a08": "a police officer holding a dashcam memory card next to a damaged car",
        "a09": "a stopped sedan with a crumpled rear and a crumpled front, sandwiched between two cars, close-up",
        "a10": "a traffic accident investigator drawing a diagram on a notepad at the scene, text unreadable",
        "a11": "a front and rear dashcam installed on a car windshield, close-up",
        "a12": "a long Korean city road at dusk with traffic lights, seen from a driver's seat",
    })


def write_shots(slug, spec_lines):
    sc = json.load(open(os.path.join(ROOT, "work", slug, "script.json")))
    assert len(spec_lines) == len(sc["lines"]), (slug, len(spec_lines), len(sc["lines"]))
    lines = []
    for i, ln in enumerate(spec_lines):
        if ln == "OUT:real/r1.jpg":
            d = shot_line({"outro": True, "img": "real/r1.jpg"}, i)
            d["shots"] = [A("real/r1.jpg", credit=FB)]
        else:
            base = dict(sc["lines"][i])
            base.update(ln)
            d = shot_line(base, i)
        lines.append(d)
    texts = [l["text"].rstrip(".") for l in sc["lines"]]

    def chk(li, w):
        if w:
            assert w in texts[li], (slug, li, w, texts[li])
    for li, l in enumerate(lines):
        for s in l["shots"]:
            chk(li, s.get("at"))
        for x in l.get("sfx", []):
            chk(li, x[1])
        if "pop" in l:
            chk(li, l["pop"][2])
        chk(li, l.get("shake"))
        inf = l.get("info")
        if inf:
            chk(li, inf.get("at"))
            for it in inf.get("items", []):
                chk(li, it.get("at"))
                chk(li, it.get("flash"))
    json.dump({"bgmVol": 0.09, "bgm": "bgm/sneaky-123.mp3", "lines": lines},
              open(os.path.join(ROOT, "work", slug, "v2", "shots.json"), "w"), ensure_ascii=False, indent=1)
    print("shots", slug, len(lines))


only = sys.argv[1:]
if not only or "omoda5" in only:
    write_shots("omoda5", OMODA_SHOTS)

for slug, e in eps.items():
    if only and slug not in only:
        continue
    wk = os.path.join(ROOT, "work", slug)
    os.makedirs(os.path.join(wk, "v2", "ai"), exist_ok=True)
    n_ai = len(e["P"])
    for ln in e["lines"]:
        assert 1 <= ln["img"] <= n_ai, (slug, ln)
        if not ln.get("outro"):
            assert not any(c.isdigit() for c in ln.get("say", ln["text"])), (slug, ln["text"])
            for w in ln.get("em", []):
                assert w in ln["text"], (slug, w)
    lines = [{k: v for k, v in ln.items() if k not in SHOT_KEYS} for ln in e["lines"]]
    sc = {"slug": slug, "type": "란빵 자동차", "source": e["src_note"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["bar"], "channel": "란빵",
          "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
          "style": {"sub_box": True, "bar": e["bar"], "bar_count": e["cnt"], "watermark": ""},
          "lines": lines}
    json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)
    assert len(e["title"]) <= 12, (slug, e["title"], len(e["title"]))
    assert not RISKY.search(e["title"] + e["t1"] + e["t2"]), (slug, e["title"])
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    open(os.path.join(wk, "upload.md"), "w").write(
        f"# {slug} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n{e['desc']}\n\n"
        f"## 고정 댓글\n\n{e['cm']}\n\n## 쇼핑태그\n\n{e['tags']}\n\n"
        f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")
    open(os.path.join(wk, "v2", "ai_prompts.tsv"), "w").write("".join(f"{k}\t{v}{T}\n" for k, v in e["P"].items()))
    write_shots(slug, e["lines"])
    print("ok", slug, len(lines), "lines", n_ai, "ai", e["title"])
