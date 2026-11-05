#!/usr/bin/env python3
"""란빵 2026-10-17 — 테슬라 로드스터 5편 (사용자 지시: 1 원리 / 2 따라 만든 밈 / 3 풀영상 / 4,5 자유, 대화체 중간중간, 40초 이내).
roadster26(공개 뉴스)·roadsterfly(커뮤니티 반응·가격 추측)와 겹치지 않는 각도:
  rdprinciple 원리(흡입 팬 2G + 1978 F1 팬카 + 압축공기 탱크) / rdmeme 해외 밈 / rdfull 시연 4종 이어보기
  rdcanyon 다음 목표 협곡 점프(이블 크니블) / rd081 0.81초가 얼마나 빠른가
영상 = Tesla 공식 'Roadster Event'(qt5p-_tE8d0) 클립 work/_videos/roadster/cuts/*.mp4 (9:8 1080x960 무음), 발언은 행사 받아쓰기(faster-whisper small.en)로 확인.
AI 이미지 = gen.sh square (v2/ai_prompts.tsv → work/_b1013_img.py 방식).
"""
import json, os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
CUTS = os.path.join(ROOT, "work/_videos/roadster/cuts")
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")
Y, W, R, G = "#FBFF56", "#fff", "#FF3B30", "#34C759"
CR = "영상: Tesla"
STYLE = ", realistic candid smartphone photo, natural lighting, photorealistic, no text no letters no logos no brand marks no watermark"


def V(name, at=None, s0=1.0, s1=1.08, fx=0.5, fy=0.5, punch=False, ss=0):
    d = {"vid": f"vid/{name}.mp4", "s0": s0, "s1": s1, "fx": fx, "fy": fy, "credit": CR}
    if at: d["at"] = at
    if punch: d["punch"] = True
    if ss: d["ss"] = ss
    return d


def A(name, at=None, s0=1.0, s1=1.1, fx=0.5, fy=0.5, punch=False):
    d = {"img": f"ai/{name}.png", "s0": s0, "s1": s1, "fx": fx, "fy": fy}
    if at: d["at"] = at
    if punch: d["punch"] = True
    return d


def L(text, sh, **k):
    d = {"text": text, "sh": sh}; d.update(k); return d


EP = {}

# ── 1. 원리 ─────────────────────────────────────────────
EP["rdprinciple"] = dict(
 t1="천장에 붙는 테슬라", t2="원리는 의외로 단순함", bar="거꾸로 매달려 달리는 테슬라 로드스터",
 title="#테슬라 로드스터 원리", source="Tesla Roadster Event 2026-10-15(받아쓰기) + Brabham BT46B 기록",
 desc=("테슬라 로드스터가 천장에 거꾸로 붙어 달리는 원리는 차 바닥의 흡입 팬, 중력 2배 힘으로 차를 눌러 붙인다.\n"
       "1978년 F1 팬카도 같은 원리로 데뷔전 우승 뒤 한 경기 만에 사라졌다.\n"
       "공중 기동은 탄소섬유 탱크 2개에 담은 공기 250kg을 노즐 10개로 분사, 차가 스스로 다시 채운다.\n"
       "#shorts #테슬라 #로드스터 #전기차 #자동차원리"),
 comment="님들은 원리 알고 나니까 더 타고 싶음, 더 무서움?",
 shop="차량용 휴대폰 거치대, 자동차 블랙박스 2채널, 차량용 무선충전기, 타이어 공기주입기, 차량용 방향제",
 proof=[("차 바닥 팬 흡입, 최대 2G 로 거꾸로 주행", "Roadster Event 491초 'fan suction system ... pull up to 2G's'"),
        ("테니스공도 호스로 빨아들인다", "Roadster Event 505초 머스크 'suck a tennis ball through a hose pipe'(의역)"),
        ("1978년 F1 팬카 데뷔전 우승 후 한 경기 만에 퇴장", "Brabham BT46B, 1978 스웨덴 GP 라우다 우승, 경쟁팀 반발로 팀이 철수(Wikipedia BT46, Motorsport Magazine)"),
        ("탄소섬유 압력용기 2개 600L, 공기 약 250kg, 노즐 10개", "Roadster Event 727~742초"),
        ("차가 스스로 공기 탱크를 다시 채움, 특수 추진제 불필요", "Roadster Event 749~764초")],
 ai=[("p1", "underside view of a sleek white futuristic two-seat electric supercar driving upside down on a curved ceiling track, large circular suction fans glowing in the rear diffuser, dark studio"),
     ("p2", "a vintage 1970s Formula One race car with a huge round fan at the rear, on a racetrack, 1978 film photo grain, spectators behind fence"),
     ("p3", "cutaway view inside a futuristic sports car chassis showing two large black carbon fiber high pressure air tanks, studio lighting, engineering display")],
 lines=[
  L("아니 저게 어떻게 천장에 붙어 있어?", [V("wallunder", ss=1.2, s0=1.05, s1=1.2), V("walltop", "붙어", ss=1.0, punch=True)],
    dialogue=True, speaker=3, emotion="toneup"),
  L("비밀은 차 바닥에 달린 흡입 팬임.", [V("franz_fan", ss=0, s0=1.0, s1=1.1), A("p1", "흡입", punch=True)],
    em=["흡입 팬"], em_color="yellow", fx=[("drop_futuristic", "흡입", 0.5)]),
  L("팬이 차 밑 공기를 쫙 빨아내면, 바깥 공기가 차를 바닥에 꾹 눌러버림.", [A("p1", s0=1.15, s1=1.0, fy=0.6), V("wallclimb", "눌러버림", ss=3)]),
  L("그 힘이 중력의 2배라서, 거꾸로 매달려도 안 떨어지는 거임.", [V("wallunder", ss=1.5, s0=1.0, s1=1.15), V("walltop", "안", ss=1.5)],
    say="그 힘이 중력의 두 배라서, 거꾸로 매달려도 안 떨어지는 거임.", em=["2배"], em_color="yellow",
    fx=[("hit_trailer_epic", "2배라서", 0.55)], pop=("중력 2배!!", Y, "2배라서")),
  L("이 차는 테니스공도 호스로 빨아들일 수 있어요.", [V("musk_suck", ss=6.5, s0=1.05, s1=1.12, fy=0.35)],
    dialogue=True, speaker=2, emotion="toneup", fx=[("drum_rimshot", "있어요", 0.45)]),
  L("근데 이 방식, 1978년 F1에서 이미 나왔었음.", [A("p2", s0=1.0, s1=1.12), A("p2", "F1에서", s0=1.6, s1=1.7, fx=0.7, fy=0.55)],
    say="근데 이 방식, 천구백칠십팔 년 에프원에서 이미 나왔었음.", em=["1978년"], em_color="yellow"),
  L("데뷔전에서 바로 1등 했는데, 다른 팀들 반발에 딱 한 경기 뛰고 사라짐.", [A("p2", s0=1.12, s1=1.0), A("p2", "한 경기", s0=1.5, s1=1.6, fx=0.3)],
    say="데뷔전에서 바로 일 등 했는데, 다른 팀들 반발에 딱 한 경기 뛰고 사라짐.", em=["한 경기"],
    fx=[("wrong_gameshow_buzz", "사라짐", 0.45)], pop=("1경기 은퇴", R, "사라짐")),
  L("그럼 날아다니는 건 또 뭔데?", [V("kfside", ss=3.5, s0=1.0, s1=1.12)], dialogue=True, speaker=3, emotion="toneup"),
  L("탄소섬유 통 2개에 공기 250킬로를 꽉 눌러 담아서, 노즐 10개로 뿜는 거임.", [A("p3", s0=1.0, s1=1.1), V("wallthrust", "노즐", ss=3.2, punch=True)],
    say="탄소섬유 통 두 개에 공기 이백오십 킬로를 꽉 눌러 담아서, 노즐 열 개로 뿜는 거임.", em=["250킬로"], em_color="yellow",
    info={"kind": "counter", "at": "250킬로를", "title": "탄소섬유 탱크 2개", "items": [{"num": 250, "suffix": "kg", "label": "눌러 담은 공기", "at": "250킬로를"}]}),
  L("연료가 아니라 공기라서, 차가 알아서 다시 채움.", [V("finfly", ss=1.5, s0=1.0, s1=1.1)], em=["다시 채움"],
    fx=[("pop_bubble", "채움", 0.45)]),
  L("님들은 원리 알고 나니까 더 타고 싶음, 더 무서움?", [V("drift", ss=1.0, s0=1.0, s1=1.1)], fx=[("pop_bubble", "무서움")]),
 ])

# ── 2. 따라 만든 밈 ──────────────────────────────────────
EP["rdmeme"] = dict(
 t1="테슬라가 날자마자", t2="전세계 밈 대폭발", bar="차 5대 뛰어넘은 테슬라, 몇 분 만에 밈 됨",
 title="#테슬라 로드스터 밈", source="AOL/dnyuz 2026-10-16 'Tesla's flying car is here, and so are the memes', Twitchy 2026-10-16",
 desc=("테슬라 로드스터가 차 5대를 날아서 넘자 몇 분 만에 해외에서 밈이 쏟아졌다.\n"
       "1차로 느린 차 넘기, 출근길 정체 탈출, 쏟아진 커피, 새 도로표지판, 보험사 반응까지.\n"
       "시연 차량은 사람 없이 자율 주행으로 날았다.\n"
       "#shorts #테슬라 #로드스터 #밈 #전기차"),
 comment="님들이 뽑은 최고 밈은 뭐임?",
 shop="차량용 컵홀더, 자동차 블랙박스 2채널, 차량용 휴대폰 거치대, 차량용 방향제, 차량용 무선충전기",
 proof=[("공개 직후 밈 확산", "AOL/dnyuz 2026-10-16, Twitchy 2026-10-16"),
        ("면허증 보여주시... 오 마이 갓(경찰)", "@ProblyHQ 'Sir let me see your drivers license and registratiooooohhh my god'"),
        ("1차로 느린 차 넘기", "@HeyyBigGuy 'When the Karen in the left lane is going 10 under', @GingerBeardGage 'Slow driver in left lane'"),
        ("출근길 정체", "@jarvis_best 'Me stuck in traffic next week as people zip by me'"),
        ("교차로 넘고 10달러 커피 쏟음", "@MrSwitz71 'My $10 coffee after I skipped the intersection'"),
        ("새 도로표지판", "@thexercisedude 'New road signs in the making'"),
        ("보험사 반응", "@Weyne_west 'Cars insurers right now'"),
        ("시연 차는 무인, 자율 주행", "Roadster Event 279~285초 'technically autonomous for this demo', AI타임스 '공중 기동 시연 차량에는 사람이 타지 않았다'"),
        ("밈 이미지", "원본 밈은 쓰지 않고 내용만 AI 재현(gen.sh)")],
 ai=[("m1", "an American highway patrol officer at night on a highway shoulder holding a notepad, looking up at the sky with jaw dropped in shock, flashing police lights behind"),
     ("m2", "a slow grey sedan driving in the left lane of a multi-lane highway while a sleek white futuristic sports car flies right over it trailing white vapor jets, daytime, shot from behind"),
     ("m3", "a jammed city expressway at morning rush hour full of cars, one sleek white futuristic sports car flying above the traffic with white vapor jets"),
     ("m4", "inside a car, an iced coffee cup tipped over with coffee splashed all over the dashboard, steering wheel and driver's pants, messy, close-up"),
     ("m5", "a yellow diamond-shaped highway warning road sign with a black pictogram of a car flipping upside down in the air, roadside, blue sky"),
     ("m6", "a car insurance claims adjuster in a shirt and tie at an office desk holding his head with both hands, staring at his monitor in disbelief, monitor screen blurred"),
     ("m7", "a crash test dummy with yellow and black markings sitting alone in the driver's seat of a sleek white futuristic sports car, studio")],
 lines=[
  L("면허증 좀 보여주시... 오 마이 갓!", [A("m1", s0=1.0, s1=1.1), A("m1", "갓", s0=1.4, s1=1.5, fy=0.35, punch=True)],
    say="면허증 좀 보여주시... 오, 마이 갓!", dialogue=True, speaker=2, emotion="surprise", fx=[("hit_trailer_epic", "갓", 0.5)]),
  L("테슬라 로드스터가 차 5대를 날아서 넘자, 몇 분 만에 전 세계 밈이 쏟아짐.", [V("kfjump", ss=1.0), V("kfside", "몇", ss=3.5, punch=True)],
    say="테슬라 로드스터가 차 다섯 대를 날아서 넘자, 몇 분 만에 전 세계 밈이 쏟아짐.", em=["몇 분 만에"], em_color="yellow"),
  L("1등은 단연 1차로 거북이 참교육 밈임.", [A("m2", s0=1.0, s1=1.12)],
    say="일 등은 단연 일 차로 거북이 참교육 밈임.", em=["1차로 거북이"], em_color="yellow", fx=[("boom_zoom_impact", "참교육", 0.5)]),
  L("앞에서 10킬로 느리게 가면, 그냥 위로 넘어가면 되잖아?", [A("m2", s0=1.3, s1=1.45, fy=0.35)],
    say="앞에서 십 킬로 느리게 가면, 그냥 위로 넘어가면 되잖아?", dialogue=True, speaker=3, emotion="toneup"),
  L("꽉 막힌 출근길도 이제 남 얘기라는 밈도 터짐.", [A("m3", s0=1.0, s1=1.12)], em=["출근길"]),
  L("근데 현실 버전도 있음. 교차로 하나 넘었더니 10달러짜리 커피가 다 쏟아짐.", [A("m4", s0=1.0, s1=1.08), A("m4", "커피가", s0=1.3, s1=1.45, punch=True)],
    say="근데 현실 버전도 있음. 교차로 하나 넘었더니 십 달러짜리 커피가 다 쏟아짐.", em=["커피"],
    fx=[("glass_smash", "쏟아짐", 0.4)], shake="쏟아짐"),
  L("고속도로엔 킥플립 주의 표지판이 새로 생길 거라는 밈까지 나옴.", [A("m5", s0=1.0, s1=1.12)], em=["킥플립 주의"], em_color="yellow"),
  L("이거 사고 나면 과실은 몇 대 몇으로 잡아요?", [A("m6", s0=1.0, s1=1.1), A("m6", "몇 대 몇", s0=1.35, s1=1.45, fy=0.35)],
    dialogue=True, speaker=2, emotion="angry", fx=[("wrong_gameshow_buzz", "잡아요", 0.45)]),
  L("그리고 다들 진짜 궁금해한 건, 시연할 때 사람이 탔냐는 거였음.", [A("m7", s0=1.0, s1=1.1), V("reveal", "사람이", ss=5)]),
  L("정답은 무인. 시연 차는 사람 없이 스스로 날았음.", [V("finfly", ss=1.0, s0=1.0, s1=1.12)], em=["무인"], em_color="yellow",
    pop=("무인!", Y, "무인")),
  L("님들이 뽑은 최고 밈은 뭐임?", [V("kfangle", ss=4, s0=1.0, s1=1.1)], fx=[("pop_bubble", "뭐임")]),
 ])

# ── 3. 풀영상 ────────────────────────────────────────────
EP["rdfull"] = dict(
 t1="테슬라 로드스터", t2="시연 풀영상", bar="벽타기부터 차 5대 점프, 0.81초까지",
 title="#테슬라 로드스터 시연", source="Tesla 공식 'Roadster Event'(qt5p-_tE8d0) 시연 4종",
 desc=("테슬라 로드스터 공개 행사 시연 4가지를 순서대로.\n"
       "수직 벽을 타고 올라가 거꾸로 달리고, 세미트럭까지 차 5대를 킥플립으로 넘고, 시속 97km까지 0.81초.\n"
       "마지막은 연기를 뿜으며 차들 위로 비행.\n"
       "#shorts #테슬라 #로드스터 #킥플립 #전기차"),
 comment="님들은 이 중에 뭐가 제일 미쳤음?",
 shop="자동차 블랙박스 2채널, 차량용 휴대폰 거치대, 차량용 무선충전기, 차량용 방향제, 비상삼각대",
 proof=[("수직 벽 주행, 거꾸로 주행, 공중 회전 착지", "Roadster Event 6:05~7:55 영상"),
        ("세미트럭 포함 차량 위 킥플립", "Roadster Event 11:06~11:48 영상, AI타임스(사이버캡, 사이버트럭, 세미, 모델Y, 모델3 5대)"),
        ("'토니 호크도 자랑스러워할 것, 우린 이걸 킥플립이라 부른다'", "Roadster Event 693~696초(의역)"),
        ("0~60마일(약 97km/h) 0.81초", "Roadster Event 1112초 발표, 외부 검증 없음(AI타임스)"),
        ("마지막 비행", "Roadster Event 22:40~22:48 영상")],
 ai=[],
 lines=[
  L("와, 이걸 진짜 차가 한다고?", [V("wallrear", ss=1.5, s0=1.0, s1=1.1)], dialogue=True, speaker=3, emotion="toneup"),
  L("첫 번째 시연, 차가 수직 벽을 그대로 타고 올라감.", [V("wallclimb", ss=0.5, s0=1.0, s1=1.05)], em=["수직 벽"], em_color="yellow"),
  L("꼭대기에선 아예 거꾸로 매달려서 달림.", [V("wallunder", ss=1.0, s0=1.0, s1=1.15), V("walltop", "거꾸로", ss=1.0)], em=["거꾸로"],
    fx=[("drop_futuristic", "거꾸로", 0.5)]),
  L("그대로 벽에서 뛰어내려서, 공중에서 한 바퀴 돌고 착지함.", [V("walljump", ss=1.5, s0=1.0, s1=1.05)], em=["한 바퀴"],
    fx=[("boom_zoom_impact", "착지함", 0.5)], shake="착지함"),
  L("미친, 착지까지 한다고?", [V("wallthrust", ss=6, s0=1.0, s1=1.1)], dialogue=True, speaker=3, emotion="surprise"),
  L("두 번째는 세미트럭까지 차 5대를 일렬로 세워둠.", [V("kfline", ss=3, s0=1.0, s1=1.08)],
    say="두 번째는 세미트럭까지 차 다섯 대를 일렬로 세워둠.", em=["5대"], em_color="yellow"),
  L("전속력으로 달려가더니, 몸을 비틀면서 차들 위를 넘어버림.", [V("kfjump", ss=0.5, s0=1.0, s1=1.05), V("kfside", "몸을", ss=3.3, punch=True)],
    fx=[("hit_trailer_epic", "넘어버림", 0.55)], pop=("킥플립!!", Y, "넘어버림")),
  L("토니 호크도 자랑스러워할걸요. 우린 이걸 킥플립이라 불러요.", [V("kfangle", ss=3, s0=1.0, s1=1.08)],
    dialogue=True, speaker=2, emotion="toneup"),
  L("세 번째는 제로백. 시속 97킬로까지 단 0.81초.", [V("dragfront", ss=0.3), V("dragside", "0.81초", ss=1.0, punch=True)],
    say="세 번째는 제로백. 시속 구십칠 키로까지 단 영 점 팔일 초.", em=["0.81초"], em_color="yellow",
    fx=[("hit_trailer_epic", "0.81초", 0.55)], pop=("0.81초!!", Y, "0.81초")),
  L("마지막엔 연기를 뿜으면서 차들 위로 날아가 버림.", [V("finfly", ss=0, s0=1.0, s1=1.08)], em=["날아가"]),
  L("님들은 이 중에 뭐가 제일 미쳤음?", [V("drift", ss=2, s0=1.0, s1=1.1)], fx=[("pop_bubble", "미쳤음")]),
 ])

# ── 4. 협곡 점프 ─────────────────────────────────────────
EP["rdcanyon"] = dict(
 t1="차 5대 넘은 테슬라", t2="다음 목표는 협곡", bar="이블 크니블 협곡 점프 다시 하겠다는 테슬라",
 title="#테슬라 협곡 점프", source="Tesla Roadster Event 2026-10-15(받아쓰기) + 이블 크니블 1974 스네이크 리버 캐니언",
 desc=("테슬라가 로드스터 다음 시연으로 이블 크니블의 스네이크 리버 캐니언 점프 재도전을 예고했다.\n"
       "1974년 로켓 바이크 도전은 낙하산이 먼저 펴져 협곡 아래로 떨어졌다.\n"
       "최고속도 시속 370km 이상, 목표는 음속의 절반, 양산은 2028년.\n"
       "#shorts #테슬라 #로드스터 #일론머스크 #전기차"),
 comment="님들은 협곡 점프 성공한다고 봄?",
 shop="자동차 블랙박스 2채널, 차량용 휴대폰 거치대, 비상삼각대, 차량용 무선충전기, 차량용 방향제",
 proof=[("이블 크니블 협곡 점프 다시 시도", "Roadster Event 1199~1213초 'Evel Knievel's attempt to jump the Snake River canyon. Let's give it another shot.'"),
        ("1974년 로켓 바이크(스카이사이클 X-2), 낙하산 조기 전개로 협곡 아래 착지", "Wikipedia Evel Knievel, Time, Cycle News"),
        ("최고속도 230mph(약 370km/h) 이상", "Roadster Event 1229초, Tesla 사양 '>230mph (Rocket)'"),
        ("음속의 절반은 넘겨야", "Roadster Event 1238~1250초 'crack halfway to the speed of sound ... Mach 0.5'(의역)"),
        ("음속 절반 = 시속 600km 이상", "마하 0.5 ≈ 612km/h(해수면 15도 기준)"),
        ("2028년 양산, '이번엔 진짜'", "Roadster Event 1272~1282초 'production in 2028, actually. For real.'"),
        ("협곡 이미지", "AI 생성(gen.sh), 실제 1974년 사진 아님")],
 ai=[("k1", "a 1970s stunt rocket-powered motorcycle vehicle sitting on a tall steep steel launch ramp at the edge of a deep rocky river canyon, crowd of spectators, vintage 1974 color film photo"),
     ("k2", "a small rocket vehicle hanging under an opened parachute drifting down into a deep rocky river canyon, river below, vintage 1974 color film photo"),
     ("k3", "aerial wide view of a deep rocky river canyon with steep cliffs and a river at the bottom, clear daylight")],
 lines=[
  L("이블 크니블의 협곡 점프, 한 번 더 해봅시다.", [V("musk_canyon", ss=0.3, s0=1.05, s1=1.12, fy=0.35), A("k3", "협곡", s0=1.0, s1=1.1)],
    dialogue=True, speaker=2, emotion="toneup", fx=[("hit_trailer_epic", "점프", 0.5)]),
  L("차 5대를 날아서 넘은 테슬라가, 다음 목표로 협곡 점프를 예고함.", [V("kfjump", ss=0.5), V("kfside", "협곡", ss=3.5, punch=True)],
    say="차 다섯 대를 날아서 넘은 테슬라가, 다음 목표로 협곡 점프를 예고함.", em=["협곡 점프"], em_color="yellow"),
  L("이 협곡은 1974년에 한 스턴트맨이 로켓 바이크로 넘으려던 곳임.", [A("k1", s0=1.0, s1=1.12)],
    say="이 협곡은 천구백칠십사 년에 한 스턴트맨이 로켓 바이크로 넘으려던 곳임.", em=["1974년"], em_color="yellow"),
  L("근데 출발하자마자 낙하산이 먼저 펴져서, 협곡 아래로 떨어져 버림.", [A("k2", s0=1.0, s1=1.1), A("k2", "협곡", s0=1.4, s1=1.55, fy=0.6)],
    em=["낙하산이 먼저"], fx=[("scratch_vinyl", "펴져서", 0.45)], pop=("낙하산?!", R, "펴져서")),
  L("그걸 이번엔 자동차로 하겠다고?", [A("k3", s0=1.1, s1=1.0)], dialogue=True, speaker=3, emotion="surprise"),
  L("그러려면 엄청 빨라야 하는데, 이 차 최고속도는 시속 370킬로가 넘음.", [V("dragside", ss=0.5), V("dragtop", "370킬로가", ss=0.5)],
    say="그러려면 엄청 빨라야 하는데, 이 차 최고속도는 시속 삼백칠십 킬로가 넘음.", em=["370킬로"], em_color="yellow"),
  L("그걸론 부족하죠. 음속의 절반은 찍어야죠.", [V("musk_mach", ss=4.5, s0=1.05, s1=1.12, fy=0.35)],
    dialogue=True, speaker=2, emotion="toneup", fx=[("drum_rimshot", "찍어야죠", 0.45)]),
  L("음속의 절반이면 시속 600킬로가 넘음.", [V("dragfront2", ss=0.2, s0=1.0, s1=1.12)],
    say="음속의 절반이면 시속 육백 킬로가 넘음.", em=["600킬로"], em_color="yellow",
    fx=[("hit_trailer_epic", "600킬로가", 0.55)], pop=("시속 600!!", Y, "600킬로가"),
    info={"kind": "bars", "span": 1, "title": "최고속도", "items": [
        {"label": "로드스터 지금", "value": 0.6, "num": 370, "suffix": "km/h", "color": W},
        {"label": "음속 절반", "value": 1.0, "num": 612, "suffix": "km/h", "color": Y, "at": "음속의", "flash": "절반이면"}]}),
  L("양산은 2028년인데, 머스크가 이번엔 진짜라고 한 번 더 강조함.", [V("musk_forreal", ss=3, s0=1.05, s1=1.12, fy=0.35)],
    say="양산은 이천이십팔 년인데, 머스크가 이번엔 진짜라고 한 번 더 강조함.", em=["이번엔 진짜"],
    pop=("진짜로?", Y, "진짜라고")),
  L("님들은 협곡 점프 성공한다고 봄?", [V("finfly", ss=1.0, s0=1.0, s1=1.1)], fx=[("pop_bubble", "봄")]),
 ])

# ── 5. 0.81초 ────────────────────────────────────────────
EP["rd081"] = dict(
 t1="테슬라 제로백 0.81초", t2="얼마나 빠른 거냐면", bar="시속 97km까지 0.81초 찍은 테슬라 로드스터",
 title="#제로백 0.81초", source="Tesla Roadster Event 2026-10-15(받아쓰기) + 현대차 아이오닉 5 N 공식 제원",
 desc=("테슬라 로드스터가 시연에서 시속 97km까지 0.81초를 기록했다(테슬라 발표, 외부 검증 전).\n"
       "아이오닉 5 N 3.4초의 4배 빠르기, 몸에 중력 3배가 넘는 힘이 걸린다.\n"
       "타이어 접지력 한계를 넘기 위해 공기를 음속보다 빠르게 뿜어 약 8톤의 힘으로 민다.\n"
       "#shorts #테슬라 #로드스터 #제로백 #전기차"),
 comment="님들은 0.81초 체험해볼 거임?",
 shop="자동차 블랙박스 2채널, 타이어 공기주입기, 차량용 휴대폰 거치대, 차량용 무선충전기, 차량용 목쿠션",
 proof=[("0~60마일(약 97km/h) 0.81초", "Roadster Event 1112초 발표, 외부 기관 검증 없음(AI타임스)"),
        ("아이오닉 5 N 0~100km/h 3.4초(N 그린 부스트)", "현대자동차그룹 뉴스룸 아이오닉 5 N 월드 프리미어, 카탈로그"),
        ("중력 3배 이상", "26.8m/s ÷ 0.81초 ≈ 33m/s², 약 3.4G(계산)"),
        ("항공모함 전투기 사출 3~4G", "SlashGear 'How Fast Do Fighter Jets Take Off From An Aircraft Carrier?', migflug"),
        ("타이어 접지 한계 보통 1~1.6G", "Roadster Event 918~925초 'traction that goes beyond the tires, which is typically one to 1.6 Gs'"),
        ("음속보다 빠른 분사, 80kN 이상(약 8톤힘)", "Roadster Event 1081~1093초 'faster than the speed of sound ... over 80 kilonewtons'"),
        ("망막이 떨어지지 않을 한계까지", "Roadster Event 1144~1154초 'ride the limit of don't detach the retina of the human'(의역)")],
 ai=[("f1", "a fighter jet launching off an aircraft carrier deck catapult with steam billowing, dramatic low angle, ocean, daytime"),
     ("f2", "close-up of a performance car rear tire spinning in place with thick white smoke on asphalt, night track lighting")],
 lines=[
  L("어? 방금 출발한 거 맞아?", [V("dragfront", ss=0.2, s0=1.0, s1=1.08)], dialogue=True, speaker=3, emotion="surprise"),
  L("테슬라 로드스터가 시속 97킬로까지 찍은 시간, 단 0.81초.", [V("dragtop", ss=0.3), V("dragside", "0.81초", ss=1.0, punch=True)],
    say="테슬라 로드스터가 시속 구십칠 키로까지 찍은 시간, 단 영 점 팔일 초.", em=["0.81초"], em_color="yellow",
    fx=[("hit_trailer_epic", "0.81초", 0.55)], pop=("0.81초!!", Y, "0.81초")),
  L("아이오닉 5 N이 시속 100킬로까지 3.4초니까, 4배는 빠른 거임.", [V("dragrear", ss=3.5, s0=1.0, s1=1.08)],
    say="아이오닉 오 엔이 시속 백 킬로까지 삼 점 사 초니까, 네 배는 빠른 거임.", em=["4배"], em_color="yellow",
    info={"kind": "bars", "span": 1, "title": "제로백", "items": [
        {"label": "아이오닉 5 N", "value": 1.0, "num": 3.4, "suffix": "초", "color": W},
        {"label": "로드스터", "value": 0.24, "num": 0.81, "suffix": "초", "color": Y, "at": "4배는", "flash": "빠른"}]}),
  L("몸엔 중력의 3배가 넘게 걸리는데, 항공모함에서 전투기가 튕겨 나갈 때랑 비슷함.", [A("f1", s0=1.0, s1=1.1), A("f1", "전투기가", s0=1.3, s1=1.45, punch=True)],
    say="몸엔 중력의 세 배가 넘게 걸리는데, 항공모함에서 전투기가 튕겨 나갈 때랑 비슷함.", em=["전투기"], em_color="yellow",
    fx=[("boom_zoom_impact", "튕겨", 0.5)], shake="튕겨"),
  L("그 정도면 타이어가 못 버티지 않아?", [A("f2", s0=1.0, s1=1.12)], dialogue=True, speaker=3, emotion="toneup"),
  L("맞음. 타이어가 땅을 붙잡는 힘은 보통 중력의 1.6배가 한계임.", [A("f2", s0=1.3, s1=1.45, fy=0.6)],
    say="맞음. 타이어가 땅을 붙잡는 힘은 보통 중력의 일 점 육 배가 한계임.", em=["한계"]),
  L("그래서 뒤에서 공기를 소리보다 빠르게 뿜어서, 약 8톤 힘으로 밀어버림.", [V("dragside", ss=2.5), V("dragtop", "8톤", ss=1.0, punch=True)],
    say="그래서 뒤에서 공기를 소리보다 빠르게 뿜어서, 약 팔 톤 힘으로 밀어버림.", em=["8톤"], em_color="yellow",
    fx=[("hit_trailer_epic", "8톤", 0.55)], pop=("8톤!!", Y, "8톤")),
  L("탑승자 망막이 안 떨어지는 선까지만 밀어붙일게요.", [V("musk_retina", ss=0.5, s0=1.05, s1=1.12, fy=0.35)],
    dialogue=True, speaker=2, emotion="toneup", fx=[("drum_rimshot", "밀어붙일게요", 0.45)]),
  L("다만 이건 테슬라가 무대에서 잰 기록이고, 외부 검증은 아직 없음.", [V("dragfront2", ss=0.2, s0=1.1, s1=1.0)], em=["외부 검증"],
    fx=[("scratch_vinyl", "없음", 0.4)]),
  L("님들은 0.81초 체험해볼 거임?", [V("dragfront", ss=2.0, s0=1.0, s1=1.1)],
    say="님들은 영 점 팔일 초 체험해볼 거임?", fx=[("pop_bubble", "거임")]),
 ])


def build(slug, e):
    lines = e["lines"]
    assert sum(1 for l in lines if l.get("dialogue")) >= 2, slug
    for l in lines:
        assert not any(c.isdigit() for c in l.get("say", l["text"])), (slug, l["text"])
        if l.get("dialogue"):
            assert l.get("speaker", 1) != 1 and not l.get("em"), l["text"]
        for w in l.get("em", []):
            assert w in l["text"], (slug, w)
        assert "—" not in l["text"] and "·" not in l["text"]
    assert len(e["title"]) <= 12, e["title"]
    assert not RISKY.search(e["title"] + e["t1"] + e["t2"] + e["bar"])
    wk = os.path.join(ROOT, "work", slug)
    os.makedirs(os.path.join(wk, "v2", "vid"), exist_ok=True)
    os.makedirs(os.path.join(wk, "v2", "ai"), exist_ok=True)
    os.makedirs(os.path.join(wk, "v2", "real"), exist_ok=True)
    shutil.copy(os.path.join(ROOT, "work/roadster26/v2/real/outro.jpg"), os.path.join(wk, "v2/real/outro.jpg"))
    used = {s["vid"][4:-4] for l in lines for s in l["sh"] if "vid" in s}
    for n in used:
        shutil.copy(os.path.join(CUTS, n + ".mp4"), os.path.join(wk, "v2", "vid", n + ".mp4"))
    if e["ai"]:
        with open(os.path.join(wk, "v2", "ai_prompts.tsv"), "w") as f:
            for k, p in e["ai"]:
                f.write(f"{k}\t{p}{STYLE}\n")
    SK = ("sh", "fx", "pop", "shake", "info")
    sc_lines = [{**{k: v for k, v in l.items() if k not in SK}, "img": 1} for l in lines]
    sc_lines.append({"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": 1})
    sc = {"slug": slug, "type": "란빵 자동차, 테슬라 로드스터 시리즈", "source": e["source"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["bar"], "channel": "란빵",
          "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
          "style": {"sub_box": True, "bar": e["bar"], "bar_count": None, "watermark": ""}, "lines": sc_lines}
    json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)
    texts = [l["text"].rstrip(".") for l in sc_lines]
    shot_lines = []
    for i, l in enumerate(lines):
        d = {"shots": l["sh"]}
        if l.get("fx"): d["sfx"] = [list(x) for x in l["fx"]]
        for k in ("pop", "shake", "info"):
            if l.get(k): d[k] = list(l[k]) if k == "pop" else l[k]
        ws = [s.get("at") for s in d["shots"]] + [x[1] for x in d.get("sfx", [])] + [d.get("shake")]
        ws += [d["pop"][2]] if "pop" in d else []
        if "info" in d:
            ws += [d["info"].get("at")] + [str(it.get("at", "")).replace("+1:", "") for it in d["info"]["items"]]
            ws += [str(it.get("flash", "")).replace("+1:", "") for it in d["info"]["items"]]
        for w in ws:
            assert not w or w in texts[i], (slug, i, w, texts[i])
        shot_lines.append(d)
    shot_lines.append({"shots": [{"img": "real/outro.jpg", "s0": 1.0, "s1": 1.1, "credit": CR}],
                       "sfx": [["pop_long", "구독!"]], "pop": ["구독!", "#FFE629", "구독!"]})
    json.dump({"bgmVol": 0.09, "bgm": "bgm/sneaky-123.mp3", "lines": shot_lines},
              open(os.path.join(wk, "v2", "shots.json"), "w"), ensure_ascii=False, indent=1)
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    md = (f"# {slug}: 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n{e['desc']}\n\n"
          f"## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop']}\n\n"
          f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n"
          f"영상: Tesla 공식 유튜브 qt5p-_tE8d0(Roadster Event), 클립 work/_videos/roadster/cuts/\n")
    assert "—" not in md and "·" not in md, slug
    open(os.path.join(wk, "upload.md"), "w").write(md)
    print("ok", slug, len(sc_lines), "lines,", sum(1 for l in lines if l.get("dialogue")), "dialogue,", len(e["ai"]), "ai")


for s, e in EP.items():
    build(s, e)
