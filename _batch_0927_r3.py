#!/usr/bin/env python3
"""란빵 2026-09-27 배치 R3조 5편 대본·프롬프트 생성기 (보배드림 원글).
lanedodge·casperrust·x5engine·autolease·kbmileage → work/<slug>/script.json + prompts.tsv
"""
import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "work"))

T = (", photorealistic DSLR photograph, 35mm lens, natural available light, shallow depth of field, "
     "Korean setting, no text no letters no signage no logos no brand marks no watermark, no readable license plates")
M1 = "a Korean man in his early 30s, short black hair, clean-shaven, slim build"
M2 = "a Korean man in his mid 30s, short wavy black hair, light stubble, sturdy build"
W1 = "a Korean woman in her early 30s, shoulder-length dark brown hair, natural light makeup"
M4 = "a Korean man in his late 40s, short graying hair, casual jacket"


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
eps = {}

eps["lanedodge"] = dict(
    src="https://www.bobaedream.co.kr/view?code=accident&No=860129 (댓글 18) ; 과실비율 인정기준(손해보험협회 과실비율분쟁심의위원회 accident.knia.or.kr): 제한속도 10~20km/h 미만 초과 = 현저한 과실(10% 가산), 20km/h 초과 = 중대한 과실(20% 가산)",
    t1="깜빡이 없이 훅", t2="피했는데 내 과실?", bar="깜빡이 없이 끼어든 차 피하다 반파됐는데 내 과실", cnt=18,
    lines=[
        L("깜빡이도 없이 끼어든 차를 피하다가 내 차가 반파됐는데 내 과실까지 나옴.", 1),
        L("지난 19일 오후 3시쯤, 제한속도 50km 일반도로 2차로를 달리던 싼타페가 있었음.", 2, sfx="whoosh", em=["제한속도 50km"], em_color="yellow"),
        L("15년째 다니던 출근길이었는데 1차로 셀토스가 깜빡이도 없이 바로 앞으로 훅 들어왔음.", 3, sfx="dudung", shake=False, em=["깜빡이도 없이"]),
        L("피하려고 오른쪽으로 핸들을 꺾었더니 길가에 서 있던 화물차 적재함에 그대로 부딪혔음.", 4),
        L("셀토스랑은 닿지도 않은 비접촉 사고인데 수리비만 450만 원 정도 나온다고 함.", 9, sfx="cash", em=["450만 원"], em_color="yellow"),
        L("경찰은 셀토스 과실이 더 커 보인다고 했는데 문제는 내 보험사였음.", 5),
        L("비접촉이라 6대4에서 시작하고, 깜빡이 안 켠 걸 반영하면 7대3 정도로 협상해보겠다는 거.", 6, em=["7대3"]),
        L("근데 이 사고엔 운전자가 직접 적은 숫자가 하나 있었음.", 7, sfx="whoosh"),
        L("당시 속도가 60에서 65km 정도였다는 거.", 7, em=["60에서 65km"], em_color="yellow"),
        L("본인은 50km 도로에서 50 아래로 달리는 사람은 드물다고 했지만,", 8),
        L("과실비율 인정기준에선 제한속도를 10km 이상 20km 미만 넘기면 현저한 과실로 봄.", 10, sfx="ding", em=["현저한 과실"]),
        L("현저한 과실이면 10%가 더 붙을 수 있고, 20km를 넘기면 중대한 과실로 20%가 붙음.", 10, em=["10%"]),
        L("피할 시간이 모자랐던 게 그 10km 때문일 수도 있다는 얘기임.", 8),
        L("그래도 깜빡이 없이 들이민 쪽이 사고를 만든 건 달라지지 않음.", 6, sfx="pop"),
        L("님들은 이 사고, 몇 대 몇이 맞다고 봄?", 3), OUT],
    prompts={
        1: f"{M4} gripping the steering wheel of an SUV swerving to the right on a two-lane suburban Korean road, tense face, seen from passenger seat, afternoon",
        2: "a white midsize SUV driving in the second lane of a flat two-lane suburban road in Korea with low industrial buildings and power lines, clear afternoon sky, seen from behind",
        3: "view from inside a car of a small white compact SUV abruptly cutting in very close in front from the left lane, suburban road, afternoon",
        4: "a white SUV scraping against the rear corner of a parked small blue cargo truck's steel bed on the roadside shoulder, debris, afternoon",
        5: f"{M4} sitting in his parked car on the phone, frustrated expression, underground garage",
        6: "insurance claim documents and a calculator on a desk with a pen, papers blank without text, office lighting",
        7: "close-up of a car analog speedometer needle pointing around 62 km per hour, dashboard lights, afternoon sun",
        8: f"{M4} driving on his morning commute on a familiar suburban road, hands on wheel, calm but confident, side view",
        10: "a balance scale on a table with two small toy cars on each pan, one side heavier, soft studio light",
    })

eps["casperrust"] = dict(
    src="https://www.bobaedream.co.kr/view?code=national&No=2417435 (댓글 60) ; 더드라이브 2026-09-23 '2022년식인데 벌써 녹이?' 캐스퍼 휀더 부식 ; 소비자분쟁해결기준(공정위 고시) 자동차 품질보증: 차체·일반부품 2년/4만km, 엔진·동력 3년/6만km, 외판 관통부식 5년(보증서가 더 유리하면 보증서 우선) ; 국토교통부 자동차리콜센터 결함신고 car.go.kr",
    t1="3년 된 경차에", t2="녹이 뚫고 나옴", bar="22년식 캐스퍼 휀다에 녹, AS 기간 지났다고 거절", cnt=60,
    lines=[
        L("22년식 캐스퍼 뒷문을 열었더니 휀다에서 녹이 뚫고 올라와 있었음.", 1),
        L("사고도 없고 흠집도 없는데 운전석 뒷문 쪽 같은 자리에만 녹이 핌.", 2, sfx="whoosh", em=["같은 자리"]),
        L("주로 22년, 23년식 차주들 사진이 줄줄이 올라오는 중임.", 3, em=["22년, 23년식"], em_color="yellow"),
        L("한 차주가 고객센터에 전화했더니 하이테크센터로 가보라고 해서 갔는데,", 4),
        L("AS 기간이 지나서 무료 수리는 절대 안 된다는 답만 돌아왔다고 함.", 5, sfx="dudung", shake=False, em=["절대 안 된다"]),
        L("유료로라도 고치겠다니까 차가 밀려 있으니 블루핸즈로 가라고 했다고 함.", 6),
        L("근데 녹은 보증 기간이 따로 있음.", 7, sfx="ding"),
        L("공정위 소비자분쟁해결기준에서 일반 부품은 2년, 엔진은 3년인데 외판 관통부식은 5년임.", 8, em=["관통부식은 5년"], em_color="yellow"),
        L("22년식이면 아직 5년이 안 지났다는 얘기가 됨.", 8, em=["5년이 안 지났다"]),
        L("다만 이 기준은 분쟁 해결용 권고라 바로 강제되진 않고, 안에서 뚫고 나온 관통부식인지 판정이 관건임.", 9),
        L("그래서 차주들은 국토부 자동차리콜센터에 사진이랑 같이 결함 신고를 하자고 모이는 중임.", 10, sfx="pop", em=["결함 신고"]),
        L("님들은 3년 만에 핀 녹, 제조사가 책임져야 한다고 봄?", 2), OUT],
    prompts={
        4: "exterior of a large modern car service center building in a Korean city with customer cars lined up in front, overcast day",
        5: f"{M1} standing at a car service reception counter looking frustrated while a staff member in uniform shakes his head, indoor fluorescent light",
        6: "a crowded small auto repair shop with several cars waiting on lifts and in line, mechanics working, evening",
        7: "a car owner's warranty booklet and car key on a car seat, booklet cover plain with no text, soft light",
        8: "a paper desk calendar and a small sage green model car on a desk, concept of years passing, soft window light",
        9: "extreme macro photo of bubbling paint and orange rust spots on a pale sage green car body panel near a wheel arch",
        10: f"{M1} crouching and photographing the rear wheel arch of a small boxy sage green city car with his smartphone in a parking lot, daytime",
    })

eps["x5engine"] = dict(
    src="https://www.bobaedream.co.kr/view?code=import&No=715111 (댓글 21) ; 소비자분쟁해결기준(공정위 고시) 자동차 엔진·동력전달장치 품질보증 3년/6만km ; 오일펌프 설계 문제는 사설업체 주장(미확인)",
    t1="1억짜리 SUV", t2="4년 만에 엔진 3천?", bar="1억 넘는 수입 SUV, 4년 만에 엔진 교체 3천만 원", cnt=21,
    lines=[
        L("1억 넘게 주고 산 수입 SUV가 4년 만에 엔진을 갈아야 할 수도 있다는 말을 들었음.", 1),
        L("22년 2월에 출고한 비엠더블유 엑스5 45e, 1년에 2만km씩 8만 1천km를 탔음.", 2, sfx="whoosh", em=["8만 1천km"], em_color="yellow"),
        L("며칠 전부터 우웅 소리가 나서 딜러한테 물었더니 그냥 타다가 고장 나면 들어오라고 했다고 함.", 3),
        L("그러다 아무리 밟아도 차가 안 나가는 일이 생김.", 4, sfx="dudung", shake=False, em=["차가 안 나가는"]),
        L("센터에 넣었더니 엔진오일이랑 필터에서 금속가루가 잔뜩 나왔고,", 5, em=["금속가루"]),
        L("엔진을 교체하게 되면 3천만 원 정도 든다는 말을 들었음.", 6, sfx="cash", em=["3천만 원"], em_color="yellow"),
        L("사설 업체에선 오일펌프 쪽 부품 때문에 원래 잘 고장 난다는 말까지 했다고 함.", 7),
        L("다만 이건 업체 한 곳의 말이고, 확인된 결함은 아님.", 7),
        L("여기서 문제는 보증 기간임.", 8, sfx="ding"),
        L("소비자분쟁해결기준에서 엔진이랑 동력계 보증은 3년 또는 6만km인데,", 8, em=["3년 또는 6만km"]),
        L("4년 7개월에 8만km를 넘겼으니 기본 기준으론 둘 다 넘은 거임.", 9),
        L("그래서 보증연장 상품에 들었는지, 리콜센터에 무상수리 공지가 있는지부터 확인해야 함.", 10, sfx="pop", em=["보증연장"]),
        L("천천히 몰았는데 억울하다는 쪽과, 보증 끝난 기계는 어쩔 수 없다는 쪽으로 갈림.", 1),
        L("님들은 이거 제조사가 책임져야 한다고 봄?", 9), OUT],
    prompts={
        1: f"{M2} standing beside a large dark luxury SUV in an underground parking garage, hands on hips, worried look",
        2: "a large dark gray luxury SUV driving on a Korean highway at dusk, side view, motion blur",
        3: f"{M2} driving and holding his phone to his ear at a red light, puzzled face, SUV interior",
        4: "interior view of a driver's foot pressing the accelerator pedal hard while the dashboard shows warning lights, tense mood",
        5: "a mechanic's gloved hand holding a used oil filter with shiny metal particles in dark engine oil in a drain pan, workshop light",
        6: "a large modern car engine removed and sitting on an engine stand in a clean service workshop",
        7: "close-up of an engine oil pump assembly with plastic and metal parts on a workbench, mechanic's tools around",
        8: "a car warranty booklet and a car key on a service center desk, booklet cover plain with no text",
        9: "close-up of an SUV digital odometer display showing about 81,000 km, dim dashboard light",
        10: f"{M2} sitting in a service center waiting lounge checking his smartphone seriously, glass wall and cars behind",
    })

eps["autolease"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1034814 (댓글 32) ; 작성자 본문(정정 포함): 8/10 첫 문의, 9/3 재문의, 9/4 반납·인수만 안내, 9/15 외부업체 통해 상사 이전 인지, 안내문 '리스승계는 만기일로부터 1개월 전까지', 9/23 이의제기·금감원 민원 ; 카드사 측 입장은 작성자 전언",
    t1="리스 만기 2달 전", t2="미리 물었는데 끝?", bar="리스 만기 두 달 전부터 물어봤는데 놓친 방법", cnt=32,
    lines=[
        L("리스 만기 두 달 전부터 상담했는데, 단어 하나 몰라서 기회를 놓쳤다는 사람이 있음.", 1),
        L("5년 동안 리스료를 낸 차고, 만기는 10월 12일인데 본인은 9월 29일에 해외로 나가야 했음.", 2, sfx="whoosh", em=["10월 12일"], em_color="yellow"),
        L("신용이 나빠져서 연장이 될지 몰라 8월 10일쯤 먼저 카드사에 전화했는데,", 3),
        L("아직 시간 있으니 한 달 전에 다시 연락하라는 안내를 받았다고 함.", 4),
        L("9월 4일 담당자 답은 연장은 어렵고, 반납이나 직접 인수 두 가지뿐이라는 거.", 5, sfx="dudung", shake=False, em=["두 가지뿐"]),
        L("다른 방법은 정말 없냐고 여러 번 물었는데도 그 두 개만 안내받았다고 함.", 5),
        L("근데 9월 15일, 외부 업체한테서 상사 이전이라는 방법이 있다는 걸 처음 들음.", 6, sfx="ding", em=["상사 이전"], em_color="yellow"),
        L("카드사에 다시 물었더니 이미 처리 기한이 지나서 안 된다는 답이 돌아왔음.", 7),
        L("안내문엔 승계는 만기 1개월 전까지라고 돼 있었고, 9월 3일은 그보다 9일 앞선 날이었음.", 8, em=["1개월 전까지"]),
        L("카드사 입장은 고객이 승계라는 말을 먼저 안 해서 물어본 연장만 답했다는 거임.", 9),
        L("결국 금융감독원에 민원을 넣고, 출국 전에 수리해서 반납할 준비도 하는 중임.", 10, sfx="pop", em=["금융감독원"]),
        L("용어를 몰랐던 고객 책임이라는 쪽과, 상담이면 가능한 방법은 다 알려줬어야 한다는 쪽으로 갈림.", 3),
        L("님들은 이거 누구 책임이라고 봄?", 9), OUT],
    prompts={
        1: f"{W1} sitting in her parked sedan holding a folded letter, worried expression, evening parking lot",
        2: "a packed carry-on suitcase and a car key on a table in an apartment, departure mood, soft light",
        3: f"{W1} on the phone at a kitchen table with a laptop open, explaining earnestly, daytime",
        4: "a smartphone lying on a table next to a cup of coffee, screen dark, soft morning light",
        5: f"{W1} frowning while listening on the phone, pen and notepad in hand, home office",
        6: f"{W1} surprised while talking to {M2} at a used car dealership lot, rows of cars behind",
        7: f"{W1} holding her head in her hands at a desk with papers, dim room",
        8: "a lease contract document and envelope on a desk with a highlighter, paper text blurred and unreadable, top-down view",
        9: "a call center office with headset-wearing staff at desks, blurred background, fluorescent light",
        10: f"{W1} handing a car key to a staff member in a car return area of a leasing company lot, overcast day",
    })

eps["kbmileage"] = dict(
    src="https://www.bobaedream.co.kr/view?code=best&No=1034839 (댓글 13) ; 작성자 첨부 정산 화면: 최초 사진 접수 2025.09.11·최초 운행거리 1km, 최종 2026.09.26·76,450km, 연간 환산 73,431km, 환급금 0원 ; 마일리지 특약은 가입 시·만기 시 계기판 사진 등록으로 주행거리 산정(보험사 안내)",
    t1="3천km 탔는데", t2="환급금 0원?!", bar="3천km 탔는데 마일리지 환급금 0원", cnt=13,
    lines=[
        L("1년에 3천km밖에 안 탔는데 자동차보험 마일리지 환급금이 0원이 나왔음.", 1),
        L("갱신하면서 15,000km 이하면 돌려준다는 문구까지 확인했는데 말임.", 2, sfx="whoosh", em=["15,000km"], em_color="yellow"),
        L("부모님 차는 다른 보험사에서 적게 탔다고 환급금을 받았는데 내 차만 0원임.", 3),
        L("작년에도 3천km 탔는데 그때도 못 받았다고 함.", 4, sfx="dudung", shake=False, em=["그때도 못 받았다"]),
        L("근데 올린 정산 화면을 자세히 보면 숫자가 좀 이상함.", 5, sfx="ding"),
        L("최초 사진 접수일은 작년 9월 11일, 최초 운행거리는 1km로 찍혀 있음.", 6, em=["1km"], em_color="yellow"),
        L("최종 운행거리는 76,450km.", 6, em=["76,450km"]),
        L("그러니까 1년에 73,431km를 탄 걸로 계산돼서 환급 대상에서 빠진 거임.", 7, sfx="cash", em=["73,431km"], em_color="yellow"),
        L("새 차가 아니었다면 처음 등록할 때 계기판 숫자가 제대로 안 들어간 걸로 보임.", 8),
        L("마일리지 특약은 처음 한 번, 만기 때 한 번 계기판 사진을 올려서 그 차이로 계산함.", 9, em=["그 차이로 계산"]),
        L("그래서 첫 숫자가 잘못 들어가면 아무리 적게 타도 환급이 안 나올 수 있음.", 9),
        L("이럴 땐 처음 올린 계기판 사진 기록부터 확인해서 보험사에 정정을 요청해보는 게 먼저임.", 10, sfx="pop", em=["정정을 요청"]),
        L("님들은 마일리지 환급 제대로 받고 있음?", 8), OUT],
    prompts={
        1: f"{M1} staring at his laptop in shock at a desk at night, car key beside",
        2: f"{M1} reading on his smartphone in his parked car, relaxed, daytime",
        3: "an older Korean couple in their 60s smiling at a smartphone together in their living room, warm light",
        4: f"{M1} frowning and scratching his head at a home desk, daytime",
        5: "close-up of a laptop screen with a blurred web table of numbers, finger pointing at it, no readable text",
        6: "close-up of a car digital odometer display showing a very small number, dark dashboard",
        7: "close-up of a car digital odometer showing about 76,000 km, dashboard lights",
        8: f"{M1} taking a photo of his car dashboard odometer with his smartphone from the driver's seat",
        9: "two printed photos of a car dashboard odometer laid side by side on a table, top-down view, numbers blurred",
        10: f"{M1} calling customer service on his smartphone, holding a printed photo, determined expression, apartment interior",
    })

for s, e in eps.items():
    sc = {"slug": s, "type": "란빵 자동차, 보배드림", "source": e["src"], "title_line1": e["t1"], "title_line2": e["t2"],
          "hook": e["bar"], "channel": "란빵", "voice": "taesub",
          "style": {"sub_box": True, "bar": e["bar"], "bar_count": e["cnt"], "watermark": ""}, "lines": e["lines"]}
    json.dump(sc, open(f"{s}/script.json", "w"), ensure_ascii=False, indent=2)
    with open(f"{s}/prompts.tsv", "w") as f:
        for k in sorted(e["prompts"]):
            f.write(f"{k:02d}\t{e['prompts'][k]}{T}\n")
    imgs = sorted({l["img"] for l in e["lines"] if "img" in l})
    print(s, len(e["lines"]) - 1, "imgs", imgs, "prompts", len(e["prompts"]))
