#!/usr/bin/env python3
"""란빵 2026-10-06 배치 10편 — 보배드림 베스트 24시간(10/5 23:37~10/6 23:37) 자동차 글.
tesladeliv·importins·dumpplate·benzac·dooropen·raypush·gatebar·pokelain·hwyreverse·grandeurhev
→ work/<slug>/script.json + prompts.tsv + upload.md   (10/7 12:00~21:00 10칸 Zernio 예약)
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
M6 = "a Korean man in his late 40s, short hair, black t-shirt, mechanic"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
eps = {}

B = "https://www.bobaedream.co.kr/view?code=best&No="

# ── 1. 부서진 채 온 테슬라 신차 ────────────────────────────────
eps["tesladeliv"] = dict(
    src=f"{B}1037550 (조회 3.5만, 추천 507, 댓글 84) ; MBN [사건추적] 2026-10-05 '새 차 가격을 줬는데 부서진 차를 주네요' (n.news.naver.com/mnews/article/057/0001972071) ; 국토부 답변: 임시번호판 부착은 고객의 선택권, 레몬법(자동차관리법 47조의2) 중재 가능",
    t1="새 차를 샀는데", t2="천장이 박살 나서 옴", bar="테슬라 신차가 천장 박살 난 채 탁송됨", cnt=84,
    title="#부서진 채 온 신차", shop="차량용 블랙박스, 신차 PPF 필름",
    desc=["수천만 원 주고 산 테슬라 신차가 천장 루프가 박살 난 채로 도착함.",
          "테슬라는 판매하면 끝, 탁송사는 고쳐 쓰고 합의금 받으라는 입장.",
          "새 차 받을 때 임시번호판이 중요한 이유."],
    tags="#shorts #테슬라 #신차탁송 #신차인수 #임시번호판",
    comment="님들이면 이 차 고쳐서 탐?",
    proof=[("천장 루프 파손·좌우 A필러 찍힘·실내 유리가루, 2층 구조물에 눌린 듯", "MBN 피해자 인터뷰"),
           ("탁송사: 저는 제 차 사고 나면 땡큐, 수리 후 합의금이 이득, 사고 이력 안 남음", "MBN 통화 녹취"),
           ("테슬라: 정식번호판 출고로 소유권 이전, 탁송사와 해결하라", "MBN 보도"),
           ("국토부: 임시번호판 부착은 고객의 선택권이자 권리, 레몬법도 있음", "MBN 보도")],
    lines=[
        L("새 차를 샀는데 천장이 박살 난 채로 도착함.", 1),
        L("수천만 원 주고 산 테슬라 신차, 운전대 한 번 잡기도 전에 받은 모습이 이거였음.", 2, sfx="whoosh", em=["신차"]),
        L("천장 유리 루프가 다 깨지고 양쪽 기둥은 찍히고, 실내엔 유리 가루가 쏟아져 있었음.", 3, sfx="dudung", shake=False, em=["유리 가루"], em_color="yellow"),
        L("탁송 트럭 2층 구조물이 차를 누른 걸로 보인다고 함.", 4),
        L("근데 탁송 회사 반응이 더 어이없음.", 5, sfx="pop"),
        L("자기는 자기 차가 오다가 사고 나면 땡큐라며, 고쳐 쓰고 합의금 받는 게 이득이라고 함.", 6, em=["땡큐"], em_color="yellow"),
        L("테슬라는 정식 번호판 달고 나간 순간 소유권이 넘어갔으니 탁송사랑 해결하라는 입장.", 7, em=["소유권"]),
        L("그래서 새 차 받을 땐 이게 중요함.", 8, sfx="ding"),
        L("임시 번호판으로 받아야 차 상태를 보고 인수할지 말지 고를 수 있음.", 9, em=["임시 번호판"], em_color="yellow"),
        L("국토부도 임시 번호판은 고객의 권리라고 했고, 이 건은 더 들여다보겠다고 함.", 10),
        L("님들이면 이 차 고쳐서 탐?", 3), OUT],
    prompts={
        1: "a brand-new white electric sedan with its glass roof completely shattered and caved in, parked in front of a car carrier truck, daytime",
        2: f"{M1} standing in shock with hands on his head in front of a new white sedan with a crushed roof, apartment parking lot, daytime",
        3: "interior of a new car with shattered glass fragments scattered all over the white leather seats and dashboard, close-up, daytime",
        4: "a two-level car carrier truck on a Korean highway with the upper deck ramp pressed low onto the roof of a white sedan below, daytime",
        5: f"{M1} angrily talking on his smartphone next to a damaged new car, daytime",
        6: "a car transport truck driver's hand holding a phone, back view, blurred carrier truck in background, daytime",
        7: "a new car key card and delivery documents on a car hood, paper text blurred and unreadable, close-up",
        8: f"{M1} carefully inspecting the body of a new car at a delivery center with a flashlight, daytime",
        9: "a new white car with a blank temporary paper license plate on its front bumper, plate text blurred and unreadable, daytime",
        10: "a desk with a laptop and printed consumer complaint documents, text blurred and unreadable, soft office light",
    })

# ── 2. 국산차 보험료로 외제차 보험금 ──────────────────────────
eps["importins"] = dict(
    src=f"{B}1037622 (조회 5천) ; 감사원 2021 보고서 [표15] 대물배상 보험료 및 보험금(2019년, 개인용 승용차, 보험개발원 제출자료): 국산차 보험료 28,675·보험금 22,491(78.4%), 수입차 보험료 4,653·보험금 11,253(241.8%)",
    t1="내 보험료로", t2="외제차 고쳐준다?", bar="국산차 보험료로 외제차 보험금 주는 구조", cnt=8,
    title="#외제차 보험금2.4배", shop="차량용 블랙박스, 2채널 블랙박스",
    desc=["감사원 보고서에 나온 대물배상 보험료와 보험금 표.",
          "국산차는 낸 보험료보다 덜 받아가고, 수입차는 2.4배를 받아감.",
          "외제차 피하고 싶은 이유가 숫자로 나옴."],
    tags="#shorts #자동차보험 #외제차 #대물배상 #보험료",
    comment="님들은 외제차 옆에 주차 피함?",
    proof=[("국산차 대물 보험료 대비 보험금 78.4%", "감사원 2021 보고서 표15(2019년, 보험개발원)"),
           ("수입차 대물 보험료 대비 보험금 241.8%", "감사원 2021 보고서 표15"),
           ("수입차 소형 204.7%·중형 261.4%·대형 232.4%", "감사원 2021 보고서 표15")],
    lines=[
        L("내가 낸 자동차 보험료로 외제차를 고쳐주고 있다는 표가 있음.", 1),
        L("감사원 보고서에 나온 2019년 대물배상 보험료랑 보험금 비교표임.", 2, sfx="whoosh", em=["감사원"]),
        L("국산차는 낸 보험료가 100이면 대물 보험금으로 나간 게 78 정도.", 3, em=["78"], em_color="yellow"),
        L("근데 수입차는 낸 보험료가 100이면 나간 보험금이 242임.", 4, sfx="dudung", shake=False, em=["242"], em_color="yellow"),
        L("낸 돈의 2.4배를 받아간 거고, 중형 수입차는 2.6배까지 나옴.", 5, em=["2.4배"]),
        L("모자란 돈은 결국 다 같이 낸 보험료에서 메워지는 구조임.", 6, sfx="pop"),
        L("댓글은 수입차 범퍼는 기본 200부터, 국산은 40부터라며 난리.", 7),
        L("그래서 사고 나면 상대가 외제차인지가 내 할증을 좌우함.", 8, sfx="ding"),
        L("대물 한도를 넉넉하게 잡아두는 게 그래서 중요함.", 9, em=["대물 한도"], em_color="yellow"),
        L("님들은 외제차 옆에 주차 피함?", 10), OUT],
    prompts={
        1: "a cheap compact car parked next to a shiny expensive black luxury sedan in a Korean parking lot, daytime",
        2: "a thick government audit report document on a desk with charts, text blurred and unreadable, soft light",
        3: "a small domestic hatchback in a body shop getting a simple bumper repair, workshop lighting",
        4: "a luxury imported sports sedan in a high-end body shop with many expensive parts laid out, workshop lighting",
        5: "a stack of Korean won banknotes next to a toy luxury car on a table, soft light",
        6: f"{M4} looking at a car insurance renewal notice with a frown at a kitchen table, paper text blurred and unreadable",
        7: "close-up of an expensive luxury car front bumper with a scratch, parking garage lighting",
        8: "a minor fender bender between a compact car and a luxury sedan at a Korean intersection, drivers stepping out, daytime",
        9: f"{M1} reviewing car insurance options on a laptop at home, evening, screen glow",
        10: f"{M1} carefully parking his compact car far away from luxury cars in an underground parking garage",
    })

# ── 3. 번호판 안 보이는 덤프트럭 ──────────────────────────────
eps["dumpplate"] = dict(
    src=f"{B}1037494 (조회 1만, 추천 92, 댓글 15) ; 자동차관리법 제10조 제5항(등록번호판을 가리거나 알아보기 곤란하게 하는 행위 금지), 과태료 1차 50만·2차 150만·3차 250만 원 (시행령 별표2) ; 고의로 가린 경우 1년 이하 징역 또는 1천만 원 이하 벌금(81조)",
    t1="번호판이", t2="아예 안 보이는 덤프", bar="번호판 일부러 안 닦고 무법 운전하는 덤프트럭", cnt=15,
    title="#덤프 번호판 신고", shop="차량용 블랙박스, 2채널 블랙박스",
    desc=["앞 번호판은 흙먼지로 뭉개지고 뒤 번호판은 아예 안 보이는 덤프트럭.",
          "운전도 막 하는데 번호를 못 읽으니 신고도 못 하는 상황.",
          "더러운 번호판도 과태료 대상인 이유."],
    tags="#shorts #덤프트럭 #번호판 #과태료 #안전신문고",
    comment="님들도 번호판 안 보이는 트럭 본 적 있음?",
    proof=[("앞 번호판 오염, 뒤 번호판 식별 불가, 무법 운전, 신고 가능 여부 질문, 사진 2장", "원글 본문·첨부 사진"),
           ("번호판을 알아보기 곤란하게 하는 행위 금지", "자동차관리법 10조 5항"),
           ("과태료 1차 50만·2차 150만·3차 250만", "자동차관리법 시행령 별표2")],
    lines=[
        L("번호판이 아예 안 보이는 덤프트럭이 도로를 막 휘젓고 다님.", 1),
        L("앞 번호판은 흙먼지에 뭉개져서 숫자가 겨우 보이는 수준이었음.", 2, sfx="whoosh", em=["흙먼지"]),
        L("뒤로 가보니 뒤 번호판은 아예 읽을 수가 없음.", 3, sfx="dudung", shake=False, em=["아예"], em_color="yellow"),
        L("글쓴이는 일부러 안 닦고 무법자처럼 운전한다며 신고되냐고 물음.", 4),
        L("댓글은 흙먼지가 많아도 번호가 안 보이냐며 다들 혀를 참.", 5, sfx="pop"),
        L("근데 이거 신고 됨.", 6, sfx="ding"),
        L("자동차관리법은 번호판을 가리는 것뿐 아니라 알아보기 어렵게 만드는 것도 금지함.", 7, em=["알아보기 어렵게"], em_color="yellow"),
        L("과태료는 처음 50만 원, 두 번째 150만 원, 세 번째는 250만 원까지 올라감.", 8, em=["250만 원"], em_color="yellow"),
        L("일부러 가린 게 확인되면 징역이나 천만 원 이하 벌금까지 갈 수 있음.", 9),
        L("앞 번호판이 찍힌 블박 영상이 있으면 그걸로 안전신문고에 신고하면 됨.", 10, em=["블박 영상"]),
        L("님들도 번호판 안 보이는 트럭 본 적 있음?", 3), OUT],
    prompts={
        1: "a large white dump truck covered in dust driving aggressively on a Korean road, low angle, daytime",
        2: "close-up of a dump truck front bumper with an orange license plate completely caked in dirt and dust, unreadable, daytime",
        3: "rear of a dusty dump truck where the license plate area is covered in thick mud and dirt, unreadable, view from a following car, daytime",
        4: f"{M1} driving a car and frowning at a dump truck ahead, view from passenger seat, daytime",
        5: "a dump truck tailgate and rear frame thickly coated in gray construction dust, close-up, daytime",
        6: "a smartphone held on a car dashboard recording the road ahead with a truck in front, screen content blurred, daytime",
        7: "a hand wiping dirt off a truck license plate with a cloth, plate characters blurred and unreadable, close-up",
        8: "a stack of traffic fine notice envelopes on a truck dashboard, paper text blurred and unreadable",
        9: "a judge's gavel on a desk next to a toy dump truck, soft light",
        10: "a dashcam mounted on a windshield with a dump truck visible through the glass ahead, daytime",
    })

# ── 4. 4년 된 벤츠 에어컨 280만 ───────────────────────────────
eps["benzac"] = dict(
    src=f"{B}1037675 (조회 4.6천, 댓글 12) ; 첨부 = 정비 유튜버 영상 캡처 17장: CLS 450, 출고 4년·1만6천km, 에어컨 찬바람 안 나옴, 전동식 컴프레서 커넥터 씰 오일 누설 → 기판까지 침투, 정품 280만 원, 쇳가루 돌면 1천만 원 이상, 하이브리드 컴프레서 동일 문제 다수, 애프터 제품 없음 ; 점검법: 기판 오일 유입·에어컨 라인 쇳가루",
    t1="1만 6천 km 탄 벤츠", t2="에어컨 수리비 280만", bar="거의 새 차 벤츠, 에어컨이 안 나옴", cnt=12,
    title="#벤츠 에어컨 280만", shop="차량용 에어컨 필터, 에어컨 탈취제",
    desc=["출고 4년에 1만 6천 km밖에 안 탄 벤츠 CLS, 에어컨을 켜도 찬바람이 안 나옴.",
          "열어보니 전동 컴프레서 기판까지 오일이 샘, 정품 280만 원.",
          "쇳가루까지 돌면 천만 원이 넘는 이유와 미리 점검하는 법."],
    tags="#shorts #벤츠 #에어컨고장 #컴프레서 #수입차수리비",
    comment="님들은 수입차 수리비 감당 가능함?",
    proof=[("CLS 450, 출고 4년·1만6천km, 에어컨 찬바람 안 나옴", "원글 첨부 캡처"),
           ("커넥터 씰에서 오일 누설, 단자 타고 기판까지 침투, 윤활 부족", "원글 첨부 캡처"),
           ("전동식 컴프레서 정품 280만 원, 애프터 제품 없음, 쇳가루 돌면 천만 원 이상", "원글 첨부 캡처"),
           ("하이브리드 컴프레서 동일 문제 다수", "원글 첨부 캡처(정비사 주장)")],
    lines=[
        L("1만 6천 km밖에 안 탄 벤츠, 에어컨 수리비가 280만 원이 나옴.", 1),
        L("출고 4년 된 벤츠 CLS, 와이퍼만 막 끝난 거의 새 차 수준임.", 2, sfx="whoosh", em=["거의 새 차"]),
        L("근데 에어컨을 켜도 찬바람이 하나도 안 나온다고 정비소에 들어옴.", 3, sfx="dudung", shake=False),
        L("열어보니 에어컨 컴프레서 커넥터에서 오일이 새고 있었음.", 4, em=["오일"], em_color="yellow"),
        L("그 오일이 선을 타고 기판까지 흘러 들어가서 회로가 다 젖어 있었음.", 5, sfx="pop", em=["기판까지"]),
        L("요즘 차는 컴프레서가 전동식이라 안에 전자 모듈까지 들어 있어서 통째로 갈아야 함.", 6),
        L("정품 가격만 280만 원이고, 싸게 대체할 애프터 제품도 없음.", 7, em=["280만 원"], em_color="yellow"),
        L("오일이 부족해서 안에서 쇳가루까지 돌았으면 수리비가 천만 원을 넘길 수도 있음.", 8, em=["천만 원"], em_color="yellow"),
        L("그래서 에어컨이 약해졌다 싶으면 바로 이것부터 봐야 함.", 9, sfx="ding"),
        L("컴프레서 기판에 오일이 들어갔는지, 에어컨 라인에 쇳가루가 보이는지 점검받는 거임.", 10, em=["쇳가루"]),
        L("님들은 수입차 수리비 감당 가능함?", 7), OUT],
    prompts={
        1: "a silver luxury four-door coupe parked inside a clean auto repair shop with the hood open, workshop lighting",
        2: "a nearly new silver luxury coupe with shiny paint and wheels in a garage, side view, workshop lighting",
        3: "a hand in front of a car dashboard air vent feeling for air, luxury car interior with ambient lighting, close-up",
        4: "close-up of an electric car air conditioning compressor connector with oily residue, engine bay, workshop lighting",
        5: "a disassembled circuit board from an air conditioning compressor covered in yellow oil, on a workbench, close-up",
        6: f"{M6} pointing at a disassembled electric air conditioning compressor on a workbench, workshop",
        7: "a new boxed car air conditioning compressor part on a shop counter, label text blurred and unreadable, close-up",
        8: "close-up of metal shavings and dirty oil inside a disassembled compressor housing, workshop lighting",
        9: f"{M1} driving on a hot summer day wiping sweat, car interior, bright sunlight",
        10: f"{M6} inspecting car air conditioning lines in an engine bay with a flashlight, workshop",
    })

# ── 5. 문 열어놨는데 출발한 옆차 ─────────────────────────────
eps["dooropen"] = dict(
    src=f"{B}1037625 (조회 1.9천, 추천 51, 댓글 28) ; 작성자 본문·댓글: 주차장, 아내가 문을 먼저 열고 아이를 카시트에 태우던 중 비어 있던 옆차에 차주가 뒤늦게 타서 출발하다 문과 긁힘, 앞뒤 차 블박 직접 확보, 상대가 경찰 신고·가해자 취급, 내 보험사는 거의 무과실 판단 ; 도로교통법 제49조 제1항 제7호(문 열 때 안전 확인 의무)·출발 시 주변 안전 확인",
    t1="문 열어놓고 아이 태우는데", t2="옆차가 그냥 출발", bar="문 열고 아이 태우는데 옆차가 출발해서 긁음", cnt=28,
    title="#문열림 사고 과실", shop="차량용 블랙박스, 도어가드 문콕방지",
    desc=["주차장에서 문 열고 아이를 카시트에 태우는데 옆차가 그냥 출발해서 긁고 감.",
          "상대는 오히려 경찰 부르고 가해자 취급.",
          "문 연 차가 무조건 가해자가 아닌 이유."],
    tags="#shorts #문콕 #개문사고 #과실비율 #주차장사고",
    comment="님들은 이거 누구 잘못 같음?",
    proof=[("문 먼저 열고 아이 태우던 중, 비어 있던 옆차에 차주가 뒤늦게 타서 출발, 긁힘", "원글 본문·작성자 댓글"),
           ("서로 블박엔 안 찍혀 앞뒤 차 블박 직접 확보", "원글 본문"),
           ("상대 경찰 신고·가해자 취급, 내 보험사는 거의 무과실", "원글 본문"),
           ("출발 전 주변 확인 의무, 문 열 때 안전 확인 의무", "도로교통법 49조 일반론")],
    lines=[
        L("문 열어놓고 아이를 태우는데 옆차가 그냥 출발해버림.", 1),
        L("주차장에서 아내가 차 문을 열고 아이를 카시트에 태우고 있었음.", 2, sfx="whoosh"),
        L("그때 옆차는 운전석에도 아무도 없고 시동도 안 걸려 있었음.", 3, em=["아무도 없고"]),
        L("근데 차주가 뒤늦게 와서 타더니 확인도 안 하고 그대로 출발함.", 4, sfx="dudung", shake=False, em=["확인도 안 하고"], em_color="yellow"),
        L("열린 문이랑 옆차가 그대로 긁힘, 하마터면 문에 사람이 낄 뻔했음.", 5, sfx="pop"),
        L("더 황당한 건 상대가 오히려 경찰을 부르고 아내를 가해자 취급했다는 것.", 6, em=["가해자 취급"]),
        L("보통 문 열다 난 사고는 문 연 쪽 책임이 크다고 알려져 있음.", 7, sfx="ding"),
        L("근데 문이 먼저 열려 있었고, 나중에 출발한 차가 옆을 안 봤으면 얘기가 달라짐.", 8, em=["먼저 열려"], em_color="yellow"),
        L("출발하는 차도 주변 안전을 확인할 의무가 있어서, 글쓴이 보험사도 거의 무과실로 봤음.", 9, em=["거의 무과실"], em_color="yellow"),
        L("이런 건 앞뒤 차 블박을 빨리 구해두는 게 제일 중요함, 글쓴이도 직접 구해서 냈음.", 10, em=["앞뒤 차 블박"]),
        L("님들은 이거 누구 잘못 같음?", 4), OUT],
    prompts={
        1: "two cars parked side by side in a Korean apartment parking lot, the rear door of one car wide open, the other car starting to pull out, daytime",
        2: f"{W1} leaning into the open rear door of a car buckling a toddler into a child car seat, parking lot, daytime, child seen from behind",
        3: "an empty parked car with no one inside next to another car with its rear door open, parking lot, daytime",
        4: f"{M4} getting into the driver seat of a parked car without looking to the side, parking lot, daytime",
        5: "close-up of a car's open rear door edge scraping against the side of another car pulling out, parking lot, daytime",
        6: "two Korean police officers talking with drivers next to two parked cars in an apartment parking lot, daytime",
        7: "close-up of a car door being opened into a narrow gap between parked cars, parking garage",
        8: "top-down aerial view of two parked cars, one with its rear door open, the other pulling forward out of its space, parking lot",
        9: "a car side mirror reflecting an open car door next to it, close-up, parking lot, daytime",
        10: "dashcams mounted on the windshields of several parked cars in a row, parking lot, daytime",
    })

# ── 6. 칼치기 레이, 항의하자 밀고 출발 ─────────────────────────
eps["raypush"] = dict(
    src=f"{B}1037578 (조회 1.3만, 추천 73, 댓글 21) ; 유튜브 @현장뷰 '미안하다는 말 대신…' (youtube.com/shorts/fd7ypZmxMRk, 2026-10-02, 조회 142만) 설명: 무리하게 칼치기로 끼어든 레이에 뒤차가 항의하자 레이가 가속 페달을 밟고 무리하게 출발하며 사고, 특수상해·보복운전 처벌 가능 ; 형법 258조의2 특수상해(1년 이상 10년 이하 징역)",
    t1="칼치기하고", t2="항의하니 밀고 출발", bar="칼치기한 레이, 항의하러 온 사람 앞에서 출발", cnt=21,
    title="#칼치기 레이 출발", shop="2채널 블랙박스, 차량용 블랙박스",
    desc=["초보운전 스티커 붙인 레이가 칼치기로 끼어들고 브레이크·액셀을 번갈아 밟음.",
          "참다못한 뒤차 운전자가 내려서 항의하자 레이가 그대로 가속해서 출발.",
          "자동차로 사람을 밀면 특수상해가 되는 이유."],
    tags="#shorts #칼치기 #보복운전 #특수상해 #블랙박스",
    comment="님들은 이럴 때 차에서 내림?",
    proof=[("레이 칼치기, 브레이크·액셀 번갈아, 항의하러 온 뒤차 운전자 앞에서 가속 출발해 사고", "원글 첨부·현장뷰 영상 설명"),
           ("자동차로 사람 미는 행위 = 특수상해·보복운전 처벌 가능", "현장뷰 영상 설명 ; 형법 258조의2"),
           ("특수상해 1년 이상 10년 이하 징역", "형법 258조의2")],
    lines=[
        L("칼치기로 끼어든 레이한테 항의했더니 사람 앞에서 그냥 밀고 출발함.", 1),
        L("뒤에 초보운전 스티커 붙인 레이가 차 사이로 갑자기 칼치기를 해서 들어옴.", 2, sfx="whoosh", em=["초보운전"]),
        L("그러더니 앞에서 브레이크랑 액셀을 번갈아 밟으면서 뒤차를 계속 위협함.", 3, em=["번갈아"], em_color="yellow"),
        L("참다못한 뒤차 운전자가 차에서 내려서 따지러 감.", 4, sfx="dudung", shake=False),
        L("근데 레이가 사과 대신 액셀을 밟고 그대로 출발해버림.", 5, sfx="pop", em=["사과 대신"], em_color="yellow"),
        L("댓글은 사람 앞에 두고 박아버리는 건 상상도 못 했다며 경악.", 6),
        L("이건 단순 접촉 사고가 아님.", 7, sfx="ding"),
        L("자동차는 법에서 위험한 물건으로 봐서, 차로 사람을 밀면 특수상해가 될 수 있음.", 8, em=["특수상해"], em_color="yellow"),
        L("특수상해는 벌금 없이 1년 이상 징역형만 있는 죄임.", 9, em=["1년 이상"]),
        L("그래도 이런 상대한텐 내리지 말고 문 잠그고 블박이랑 112로 해결하는 게 제일 안전함.", 10, em=["문 잠그고"]),
        L("님들은 이럴 때 차에서 내림?", 4), OUT],
    prompts={
        1: "a small boxy gray compact car abruptly pulling forward on a Korean urban expressway with a man standing in front of it, view from a car behind, daytime",
        2: "a small boxy gray compact car cutting sharply in between two cars on a busy Korean urban expressway, view from the car behind, daytime",
        3: "close-up of the red brake lights of a small boxy compact car right in front of the camera on a highway, daytime",
        4: f"{M2} getting out of his car on a highway lane and walking toward the car in front, angry, daytime",
        5: "a small boxy compact car accelerating forward with tire smoke while a man stands just beside its front bumper, highway, daytime",
        6: f"{M2} stumbling backward on a road next to a car that is speeding away, motion blur, daytime",
        7: "a car stopped diagonally across lanes on an urban expressway with hazard lights on, traffic behind, daytime",
        8: "a judge's gavel on a desk next to a small toy car, soft light",
        9: "a courtroom interior with empty wooden benches, soft light",
        10: f"{M1} inside his car pressing the door lock button and calling on his phone, worried, daytime",
    })

# ── 7. 차단기 때문에 차 망가졌다며 소송 ───────────────────────
eps["gatebar"] = dict(
    src=f"{B}1037395 (조회 1.2만, 추천 172, 댓글 30) ; 첨부 = JTBC 사건반장 2024-05-16 '주차장 차단기 파손…소송까지' 캡처: 아파트 차단기가 안 열린 상태에서 진입해 부딪힘, 입주민이 관리사무소 직원에게 언성, '바로 앞에 가면 당연히 열려야', '뒤에 차들 주르르 있는데 멈춰 서냐', 직원 '저는 매번 서거든요', 운전자 '차단기 때문에 차량 망가져' 입대위 상대 소송",
    t1="차단기에 박고", t2="아파트에 소송", bar="차단기 안 열렸는데 들어가서 박고 소송함", cnt=30,
    title="#차단기 박고 소송", shop="차량용 블랙박스, 하이패스 단말기",
    desc=["아파트 주차장 차단기가 안 열렸는데 그대로 들어가서 박은 입주민.",
          "관리사무소에 와서 바로 앞에 가면 당연히 열려야 한다며 언성.",
          "결국 차가 망가졌다며 입주자대표회의에 소송까지 건 사연."],
    tags="#shorts #차단기 #아파트주차장 #입주민 #소송",
    comment="님들은 차단기 앞에서 멈춤?",
    proof=[("차단기 안 열린 상태로 진입해 부딪힘, 관리사무소 직원에게 언성", "JTBC 사건반장 2024-05-16 캡처(원글 첨부)"),
           ("바로 앞에 가면 당연히 열려야, 뒤에 차 줄 서 있는데 멈춰 서냐", "JTBC 캡처 입주민 발언"),
           ("직원: 서야죠, 저는 매번 서거든요", "JTBC 캡처 직원 발언"),
           ("차단기 때문에 차량 망가져 입대위 상대 소송", "JTBC 캡처 자막")],
    lines=[
        L("아파트 차단기에 차를 박더니 아파트를 상대로 소송을 검.", 1),
        L("아파트 주차장 차단기가 아직 안 올라갔는데 차가 그대로 밀고 들어감.", 2, sfx="whoosh", em=["안 올라갔는데"]),
        L("당연히 차단기에 쾅 부딪힘.", 3, sfx="dudung", shake=False),
        L("그 입주민이 관리사무소에 찾아와서 한 말이 이거임.", 4, sfx="pop"),
        L("바로 앞에 가면 당연히 열려야 되는 건데, 안 열린 게 문제지 내가 지나간 게 문제냐고.", 5, em=["당연히 열려야"], em_color="yellow"),
        L("직원이 열리는 거 확인하고 들어가야 한다고 하니까, 뒤에 차가 줄 서 있는데 멈춰 서냐며 따짐.", 6),
        L("직원은 저는 매번 서거든요, 하고 담담하게 대답함.", 7, em=["매번 서거든요"]),
        L("결국 이 입주민은 차단기 때문에 차가 망가졌다며 입주자대표회의를 상대로 소송까지 걸었음.", 8, sfx="ding", em=["소송"], em_color="yellow"),
        L("댓글은 빨간불에 안 멈추고 사고 나면 신호등을 고소할 사람이라며 난리.", 9),
        L("차단기는 앞에서 한 번 멈추고, 올라간 걸 보고 지나가는 게 기본임.", 10, em=["한 번 멈추고"]),
        L("님들은 차단기 앞에서 멈춤?", 3), OUT],
    prompts={
        1: "a car stopped with its hood pressed against a lowered parking gate barrier arm at a Korean apartment complex entrance, daytime",
        2: "a sedan approaching a closed parking barrier gate at a Korean apartment entrance without slowing down, daytime",
        3: "close-up of a parking gate barrier arm bent and snapped against the front of a car, debris, daytime",
        4: "interior of a small apartment management office with a desk, filing cabinets and fire extinguishers, fluorescent light",
        5: f"{M4} in a yellow t-shirt with hands on his hips angrily talking in a small management office, back view, fluorescent light",
        6: "a line of cars waiting behind a parking barrier gate at a Korean apartment entrance, daytime",
        7: f"{M6} standing calmly in a management office with arms at his sides, listening, fluorescent light",
        8: "legal documents and a court complaint envelope on a desk next to a car key, text blurred and unreadable, soft light",
        9: "a red traffic light at a Korean intersection with a car crossing the stop line, dusk",
        10: "a car stopped politely before a rising parking gate barrier arm at an apartment entrance, daytime",
    })

# ── 8. 주차단속 불만에 포크레인 ───────────────────────────────
eps["pokelain"] = dict(
    src=f"{B}1037432 (조회 1.8만, 추천 168, 댓글 51) ; 첨부 = 2012-09-17 22:02 CCTV(부산일보) '진주서 주차단속 불만 40대, 포크레인 몰고 상대지구대서 난동' ; KNN·SBS·YTN·MBC 2012-09-18: 중장비업자 황씨, 낮 3시쯤 시청 주차단속팀 찾아가 폭력→공무집행방해 체포 후 석방, 밤에 굴착기로 지구대·순찰차 파손, 경찰 실탄 사용 제압, 다친 사람 없음",
    t1="주차 딱지 끊었다고", t2="포크레인 끌고 옴", bar="주차 단속에 앙심 품고 포크레인으로 지구대 부숨", cnt=51,
    title="#주차딱지 포크레인", shop="차량용 블랙박스, 주차번호판 알림판",
    desc=["불법주차 단속에 불만을 품은 40대 중장비업자.",
          "낮에 시청 단속팀에서 난동 부리다 체포됐다 풀려나더니 밤에 포크레인을 몰고 옴.",
          "지구대와 순찰차를 부수다 경찰 실탄에 제압된 실제 사건."],
    tags="#shorts #주차단속 #포크레인 #공무집행방해 #실제사건",
    comment="님들은 주차 딱지 몇 번 떼봄?",
    proof=[("2012-09-17 밤 진주 상대지구대, 주차단속 불만 40대가 포크레인으로 난동", "부산일보 CCTV(원글 첨부)"),
           ("낮 3시쯤 시청 주차단속팀 찾아가 폭력, 공무집행방해로 체포 후 석방", "KNN 2012-09-18"),
           ("지구대·순찰차 파손, 경찰 실탄 사용 후 멈춤, 다친 사람 없음", "YTN·MBC 2012-09-18")],
    lines=[
        L("주차 딱지 끊었다고 포크레인을 끌고 와서 경찰 지구대를 부숨.", 1),
        L("40대 중장비 업자가 불법주차로 단속을 당했음.", 2, sfx="whoosh", em=["불법주차"]),
        L("낮에 시청 단속팀에 찾아가서 폭력을 휘두르다 공무집행방해로 체포됐는데,", 3),
        L("풀려나자마자 그날 밤 포크레인을 몰고 지구대로 쳐들어옴.", 4, sfx="dudung", shake=False, em=["포크레인"], em_color="yellow"),
        L("집게로 지구대 앞을 찍고, 세워둔 순찰차를 들어서 내팽개침.", 5, sfx="pop", em=["순찰차"]),
        L("경찰이 몇 번이나 경고하고 테이저건까지 꺼냈는데도 안 멈췄음.", 6),
        L("결국 경찰이 실탄을 쏘고 나서야 포크레인이 멈춰 섬.", 7, sfx="dudung", shake=False, em=["실탄"], em_color="yellow"),
        L("다행히 다친 사람은 없었는데, 2012년 실제 CCTV가 다시 돌면서 화제가 됨.", 8, sfx="ding"),
        L("주차 과태료는 몇만 원인데, 이건 공무집행방해에 공용물건 손상까지 붙는 범죄임.", 9, em=["몇만 원"]),
        L("댓글은 순간의 화가 10년 후회가 된다며 혀를 참.", 10),
        L("님들은 주차 딱지 몇 번 떼봄?", 2), OUT],
    prompts={
        1: "a yellow excavator with its claw raised in front of a small Korean police box building at night, debris on the ground, street lights",
        2: "a parking violation ticket tucked under the windshield wiper of a parked truck, paper text blurred and unreadable, daytime",
        3: "a city hall parking enforcement office lobby with an overturned chair, fluorescent light",
        4: "a yellow tracked excavator driving down a Korean street at night toward a small police building, headlights glaring",
        5: "an excavator claw crushing the roof of a white police patrol car at night, flying debris, dramatic lighting",
        6: "police officers standing back at a distance shouting at an excavator at night, flashlights, Korean street",
        7: "an excavator stopped in front of a damaged building at night with bullet marks on its cab glass, police lights",
        8: "a grainy security camera view of a damaged patrol car and broken concrete at night, surveillance footage style",
        9: "a judge's gavel on a desk next to a toy excavator and a toy police car, soft light",
        10: f"{M4} sitting alone with his head down in a dim room, regretful, night",
    })

# ── 9. 고속도로 출구에서 후진 ─────────────────────────────────
eps["hwyreverse"] = dict(
    src=f"{B}1037651 (조회 6천, 추천 47) ; 보배드림 인스타 DM 제보: 10/3(토) 19:20경 세종포천고속도로 포천방면 중랑IC 출구에서 후진 시도 차량을 막음, 운전자가 내려 비켜달라 항의, '고속도로에서 후진하면 위험하니 앞으로 가시라', 이후 안전지대 볼라드 쪽으로 진입해 나감 ; 도로교통법 62조(고속도로 횡단·유턴·후진 금지), 범칙금 승용 4만·승합 5만 원",
    t1="고속도로 출구에서 후진", t2="막았더니 비켜달래", bar="고속도로에서 후진하려는 차를 막았더니 비켜달라고 함", cnt=8,
    title="#고속도로 후진 막음", shop="차량용 블랙박스, 비상삼각대",
    desc=["출구를 지나쳤는지 고속도로에서 후진하려던 차를 뒤에서 막아섬.",
          "그러자 운전자가 내려서 후진해야 하니 비켜달라고 항의.",
          "고속도로 후진이 금지인 이유와 범칙금."],
    tags="#shorts #고속도로 #후진 #도로교통법 #블랙박스",
    comment="님들이면 비켜줌?",
    proof=[("10/3 19:20경 고속도로 IC 출구에서 후진 시도 차 막음, 운전자 내려 비켜달라 항의, 볼라드 쪽으로 진입해 나감", "원글(보배드림 인스타 DM 제보)"),
           ("고속도로 횡단·유턴·후진 금지", "도로교통법 62조"),
           ("범칙금 승용 4만·승합 5만 원", "도로교통법 시행령 별표8")],
    lines=[
        L("고속도로에서 후진하려는 차를 막았더니 비켜달라고 함.", 1),
        L("연휴 저녁, 고속도로 출구 앞에서 앞차가 갑자기 뒤로 후진을 하려고 함.", 2, sfx="whoosh", em=["후진"], em_color="yellow"),
        L("나가는 길을 지나친 건지, 뒤에 차가 오는데도 그냥 뒤로 오려는 거임.", 3),
        L("제보자가 위험하니까 바로 뒤에 붙여서 막아버림.", 4, sfx="dudung", shake=False),
        L("그러자 운전자가 차에서 내려서 후진해야 하니까 비켜달라고 항의함.", 5, sfx="pop", em=["비켜달라고"]),
        L("제보자는 고속도로에서 후진하면 위험하니 그냥 앞으로 가시라고 함.", 6),
        L("결국 그 차는 안전지대 볼라드 쪽으로 밀고 들어가서 빠져나감.", 7, em=["볼라드"]),
        L("고속도로에선 후진이 아예 금지임.", 8, sfx="ding"),
        L("도로교통법상 고속도로에선 횡단, 유턴, 후진 다 안 되고 승용차는 범칙금이 나옴.", 9, em=["범칙금"], em_color="yellow"),
        L("출구 놓치면 그냥 다음 출구로 나가는 게 답, 뒤차가 피할 시간이 없음.", 10, em=["다음 출구"]),
        L("님들이면 비켜줌?", 5), OUT],
    prompts={
        1: "a car with its reverse lights on backing up at a Korean highway exit ramp at dusk, another car stopped close behind it",
        2: "a car slowing to a stop at a highway exit split with white reverse lights glowing, view from behind, dusk",
        3: "headlights of approaching cars on a Korean highway at dusk with a stopped car near the exit gore area",
        4: "view from inside a car stopped close behind another car at a highway exit at dusk, hazard lights on",
        5: f"{W2} getting out of her car on a highway exit and gesturing angrily toward the car behind, dusk",
        6: f"{M1} talking through his open car window calmly at dusk on a highway exit",
        7: "a car driving over the painted gore area between a highway and an exit ramp past plastic bollards, dusk",
        8: "a wide view of a Korean highway exit ramp with lane split and plastic bollards at dusk, traffic",
        9: "a traffic fine notice paper on a car dashboard, paper text blurred and unreadable, soft light",
        10: "a car continuing straight on a highway past an exit ramp toward the next exit, dusk",
    })

# ── 10. 신차 그랜저 시동 꺼짐, 부품 없음 ──────────────────────
eps["grandeurhev"] = dict(
    src=f"{B}1037603 (조회 1.7천, 추천 53) ; 작성자 본문: 그랜저 페이스리프트 하이브리드 익스클루시브 2026-08-24 인수, 9/24 크루즈 오류·엔진경고등, 9/25 주행 중 시동 꺼짐, 9/26 시동 꺼진 뒤 안 걸림, 견인·렌트, 부품 없어 1달 이상 ; 자동차관리법 47조의2(레몬법): 인도 1년·주행 2만km 이내, 중대하자 2회 이상 수리 후 재발 또는 누적 수리기간 30일 초과 시 교환·환불 중재 신청(자동차안전·하자심의위원회)",
    t1="뽑은 지 한 달 된 신차", t2="고속도로에서 시동 꺼짐", bar="신차 그랜저, 고속도로에서 시동 꺼졌는데 부품이 없대요", cnt=3,
    title="#신차 시동꺼짐 레몬법", shop="차량용 점프스타터, 비상삼각대",
    desc=["8월에 인수한 그랜저 하이브리드, 처음 올린 고속도로에서 시동이 꺼짐.",
          "견인까지 갔는데 신차인데 부품이 없어서 한 달 넘게 기다리래.",
          "신차 결함일 때 교환·환불받는 레몬법 조건."],
    tags="#shorts #그랜저 #시동꺼짐 #레몬법 #신차결함",
    comment="님들이면 교환 요구함?",
    proof=[("8/24 인수, 9/24 크루즈 오류·엔진경고등, 9/25 시동 꺼짐, 9/26 시동 불가·견인, 부품 1달 이상", "원글 본문"),
           ("가족 태우고 있었음, 교환·환불 원함", "원글 본문"),
           ("인도 1년·2만km 이내, 중대하자 2회 수리 후 재발 또는 누적 수리 30일 초과 시 교환·환불", "자동차관리법 47조의2")],
    lines=[
        L("뽑은 지 한 달 된 신차가 고속도로에서 시동이 꺼짐.", 1),
        L("8월 말에 그랜저 하이브리드를 새로 뽑고 한 달 동안 동네만 다녔음.", 2, sfx="whoosh"),
        L("추석 연휴에 처음으로 고속도로에 올려서 크루즈 켜고 100km로 달렸는데,", 3),
        L("첫날 크루즈 오류에 엔진 경고등이 들어옴.", 4, sfx="dudung", shake=False, em=["엔진 경고등"], em_color="yellow"),
        L("다음 날엔 달리다가 시동이 꺼지고, 그다음 날엔 아예 시동이 안 걸림.", 5, sfx="pop", em=["시동이 꺼지고"]),
        L("와이프랑 애까지 태우고 있었는데 결국 견인차 타고 여행은 엉망이 됨.", 6),
        L("근데 서비스센터에서 신차인데 부품이 없어서 한 달 넘게 걸린다고 함.", 7, em=["부품이 없어서"], em_color="yellow"),
        L("이럴 때 알아둘 게 레몬법임.", 8, sfx="ding"),
        L("산 지 1년, 2만 km 안에 시동 꺼짐 같은 중대 결함이 2번 고친 뒤 또 나면 교환이나 환불을 신청할 수 있음.", 9, em=["교환이나 환불"], em_color="yellow"),
        L("수리 기간이 합쳐서 30일을 넘겨도 대상이라, 입고 날짜랑 수리 내역을 다 챙겨둬야 함.", 10, em=["30일"]),
        L("님들이면 교환 요구함?", 5), OUT],
    prompts={
        1: "a new dark gray large sedan stopped on the shoulder of a Korean highway with hazard lights on, dusk",
        2: "a brand-new dark gray large sedan parked in front of a Korean apartment building, shiny, daytime",
        3: "view from the driver seat of a car cruising on a Korean highway during a holiday, hands lightly on the wheel, daytime",
        4: "close-up of a modern car digital instrument cluster with an amber warning light glowing, symbols only, no text",
        5: f"{M2} trying to start his car with a worried face, pressing the start button, car interior, daytime",
        6: "a tow truck loading a new dark gray sedan on a highway rest area, a woman and a child standing nearby seen from behind, dusk",
        7: "an auto service center reception desk with a service advisor shaking his head, blurred background, fluorescent light",
        8: "a lemon placed on top of a car key and a sales contract on a desk, paper text blurred and unreadable, soft light",
        9: f"{M2} filling out documents at a desk with a determined face, car key on the table, evening",
        10: "a calendar with many days crossed out next to car repair receipts on a table, text blurred and unreadable, close-up",
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
