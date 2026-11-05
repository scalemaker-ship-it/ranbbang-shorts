#!/usr/bin/env python3
"""란빵 2026-10-14 점심 3칸(13:00·13:30·14:00) — 최근 3일 주차 뉴스 3편, v2(Remotion), 경모 목소리(tts_myvoice).
ferrariuturn·hcpark1100·vegastoy
→ work/<slug>/script.json + upload.md + v2/ai_prompts.tsv
숫자가 든 줄은 "say" 에 한글로(금액은 마넌). 제목 위험 단어 금지(schedule_zernio.RISKY).
"""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
T = (", photorealistic candid smartphone photo, natural light, realistic setting, "
     "no text no letters no signage no logos no watermark, no readable license plates")
OUT = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")


def L(text, img, **k):
    d = {"text": text, "img": img}
    d.update(k)
    return d


eps = {}

# 1 ─────────────────────────────────────────────────────────────
CAR = "a red mid-engine Italian supercar with no badges or logos"
eps["ferrariuturn"] = dict(
    src="https://n.news.naver.com/mnews/article/421/0009220306",
    src_note="뉴스1 2026-10-11 '페라리는 소중하니까…유턴 차선에 떡 주차' + 뉴시스 2026-10-12(003/0014247876) + 아시아경제 2026-10-12(277/0005827130) — 원글 보배드림 '실시간 청주 현대백화점 앞 페라리 주차 상태'(10/10)",
    t1="백화점 앞 유턴 차로에", t2="페라리 세워두고 쇼핑", bar="유턴 차로 막고 황색 실선에 주차", cnt=None,
    title="#유턴차로 페라리",
    lines=[
        L("청주 현대백화점 앞, 주말이면 차가 꽉 막히는 도로였음.", 1),
        L("근데 유턴하는 차로에 빨간 페라리 한 대가 떡하니 서 있었음.", 2, em=["페라리"]),
        L("유턴하려던 차들이 그 차를 피해서 겨우겨우 돌아나감.", 3, em=["겨우겨우"]),
        L("바닥은 황색 실선, 원래 차를 세우면 안 되는 자리임.", 4, em=["황색 실선"], em_color="yellow"),
        L("근데 차주는 그냥 내려서 백화점으로 가버림.", 5),
        L("바로 옆에 백화점 주차장이 있는데도 말임.", 6, em=["주차장"], em_color="yellow"),
        L("글쓴이는 국민신문고로 신고했는데, 주말이라 그런지 견인은 안 됐음.", 7, em=["견인은 안 됐음"]),
        L("주정차 금지 위반은 승용차 과태료가 4만원임.", 8, say="주정차 금지 위반은 승용차 과태료가 사마넌임.",
          em=["4만원"], em_color="yellow"),
        L("페라리 주인한테 4만원이면 그냥 주차비 수준임.", 9, say="페라리 주인한테 사마넌이면 그냥 주차비 수준임.", em=["주차비"]),
        L("댓글에선 시간 간격 두고 계속 신고하면 과태료가 쌓인다는 말도 나왔는데,", 10, em=["쌓인다"], em_color="yellow"),
        L("지역마다 달라서 하루에 한 건만 받아주는 곳도 많다고 함.", 11, em=["한 건만"]),
        L("차는 명품인데 주차는 민폐라는 말이 딱 맞음.", 12, em=["민폐"]),
        L("님들은 이런 차 보면 신고함, 그냥 지나감?", 13),
        OUT],
    tags="주차번호판, 자동차 블랙박스 2채널, 차량용 휴대폰 거치대, 자동차 광택제, 차량용 방향제",
    desc="청주 현대백화점 앞 유턴 차로에 페라리가 황색 실선 주차하고 쇼핑하러 감.\n유턴 차들은 겨우 피해 돌아가고, 견인은 안 됨.\n주정차 과태료랑 반복 신고 얘기까지 정리함.\n#shorts #민폐주차 #페라리 #황색실선 #불법주차",
    cm="님들은 이런 차 보면 신고함, 그냥 지나감?",
    proof=[("청주 현대백화점 충청점 인근 유턴 구간, 황색 실선에 페라리 주차(10/10 보배드림)", "뉴스1 2026-10-11·뉴시스 2026-10-12"),
           ("유턴 차 통행 방해, 주말 혼잡 구간", "뉴시스·아시아경제 2026-10-12"),
           ("국민신문고 신고, 견인지역 표지 있었으나 견인 안 됨", "뉴스1 2026-10-11"),
           ("쇼핑몰 주차장이 있는데 왜 도로에", "누리꾼 반응(뉴스1)"),
           ("주정차 금지 위반 승용 과태료 4만원", "도로교통법 시행령 별표6"),
           ("간격 두고 반복 신고 → 과태료 누적 / 지역마다 달라 하루 1건만 받는 곳 많음", "뉴시스 2026-10-12 누리꾼 반응")],
    P={
        "a01": "a busy road in front of a large Korean department store on a weekend, heavy traffic, shoppers on the sidewalk, daytime",
        "a02": f"{CAR} parked inside a U-turn lane in the middle of a Korean city road, other cars around it, daytime, elevated view",
        "a03": f"cars slowly squeezing around {CAR} that blocks a U-turn lane, traffic jam forming behind, daytime",
        "a04": "close-up of a solid yellow line painted along a Korean road edge, a red supercar's rear tire right on it",
        "a05": "a well-dressed man with shopping bags walking away from a parked red supercar toward a department store entrance, back view, face not visible",
        "a06": "the entrance ramp of a Korean department store parking garage, nearly empty, cars entering, daytime",
        "a07": "close-up of a hand holding a smartphone photographing an illegally parked red supercar through a car windshield, screen blurred",
        "a08": "a Korean parking enforcement yellow ticket envelope tucked under the windshield wiper of a red supercar, close-up",
        "a09": "a red supercar parked on a road while a parking meter style receipt flutters, ironic mood, shallow depth of field, close-up of the car's sleek rear",
        "a10": "a person's hands typing a report on a smartphone in a parked car, a red supercar blurred through the windshield, evening",
        "a11": "a Korean district office traffic enforcement desk with stacked report papers and a monitor, text unreadable",
        "a12": f"wide street view of {CAR} blocking a lane while long traffic queue honks behind it, golden hour",
        "a13": "a Korean driver in his 30s inside his car glancing at a red supercar parked in the U-turn lane, deciding, side view",
    })

# 2 ─────────────────────────────────────────────────────────────
GOLF = "a dark gray compact hatchback with no badges or logos"
eps["hcpark1100"] = dict(
    src="https://thedrive.co.kr/news/newsview.php?ncode=1065608480118003",
    src_note="더드라이브 2026-10-12 '장애인 주차구역 상습 주차했다가 1100만원 철퇴…폭스바겐 차주 파문' — 원글 에펨코리아 2026-10-11",
    t1="장애인 구역 상습 주차", t2="합쳐서 1100만원 나옴", bar="장애인 주차구역 상습 주차로 1100만원", cnt=None,
    title="#장애인칸 1100만",
    lines=[
        L("한 아파트 장애인 주차구역에 맨날 같은 골프가 서 있었음.", 1, em=["맨날"]),
        L("앞유리엔 장애인 보호자 운전용 표지가 붙어 있었음.", 2, em=["보호자 운전용"], em_color="yellow"),
        L("보호자용 표지는 장애인이 같이 탔을 때만 그 자리에 댈 수 있음.", 3, em=["같이 탔을 때만"]),
        L("근데 신고자가 보니까 장애인 없이 혼자 타고 다니는 거 같았음.", 4),
        L("더 웃긴 건, 일반 자리에 댈 땐 표지를 떼고 장애인 구역에 댈 땐 다시 붙였다는 거임.", 5, em=["다시 붙였다"]),
        L("신고자는 작년 10월에 여러 번 찍어서 신고함.", 6, say="신고자는 작년 시월에 여러 번 찍어서 신고함.", em=["여러 번"]),
        L("결과는 표지 부당 사용 과태료가 한 건에 200만원, 네 건이라 800만원.", 7,
          say="결과는 표지 부당 사용 과태료가 한 건에 이백마넌, 네 건이라 팔백마넌.", em=["800만원"], em_color="yellow"),
        L("여기에 공문서 부정행사로 검찰이 벌금 300만원 약식 청구까지 함.", 8,
          say="여기에 공문서 부정행사로 검찰이 벌금 삼백마넌 약식 청구까지 함.", em=["공문서 부정행사"]),
        L("합쳐서 1100만원임.", 9, say="합쳐서 천백마넌임.", em=["1100만원"], em_color="yellow"),
        L("참고로 그냥 자격 없이 대면 10만원, 앞을 막으면 50만원임.", 10,
          say="참고로 그냥 자격 없이 대면 십마넌, 앞을 막으면 오십마넌임."),
        L("표지를 잘못 쓰면 200만원이라 차원이 다름.", 11, say="표지를 잘못 쓰면 이백마넌이라 차원이 다름.", em=["차원이 다름"]),
        L("댓글에선 사진만으로 동승 여부를 어떻게 아냐는 말도 있었지만, 반복이면 세게 가야 한다는 말이 더 많았음.", 12),
        L("님들은 1100만원 과하다고 봄?", 13, say="님들은 천백마넌 과하다고 봄?"),
        OUT],
    tags="주차번호판, 자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 휴대폰 거치대, 차량용 햇빛가리개",
    desc="아파트 장애인 주차구역에 보호자용 표지 붙이고 상습 주차한 골프 차주.\n표지 부당 사용 과태료 4건에 공문서 부정행사 벌금까지 합쳐 1100만원.\n장애인 구역 과태료 기준도 정리함.\n#shorts #장애인주차구역 #과태료 #주차 #공문서부정행사",
    cm="님들은 1100만원 과하다고 봄?",
    proof=[("아파트 장애인전용주차구역 폭스바겐 골프 반복 주차, 보호자 운전용 표지", "더드라이브 2026-10-12"),
           ("장애인 미탑승 의심, 일반 구역에선 표지 떼고 장애인 구역에선 붙임(신고자 주장)", "더드라이브 2026-10-12"),
           ("2025년 10월 여러 차례 촬영·신고", "더드라이브 2026-10-12"),
           ("표지 부당 사용 과태료 건당 200만원 × 4건 = 800만원", "더드라이브 2026-10-12 / 장애인등편의법 시행령 별표3"),
           ("공문서 부정행사 검찰 구약식 벌금 300만원(확정 여부 미확인)", "더드라이브 2026-10-12"),
           ("자격 없이 주차 10만원, 주차 방해 50만원", "더드라이브 2026-10-12 / 장애인등편의법"),
           ("보호자용 표지는 장애인 동승 시에만 구역 이용", "보건복지부 장애인전용주차구역 안내")],
    P={
        "a01": f"{GOLF} parked in a blue-marked accessible parking space with a white wheelchair symbol painted on the ground, Korean apartment complex outdoor parking lot, morning",
        "a02": "close-up of a parking permit card placed on the dashboard behind a car windshield, the card text blurred and unreadable",
        "a03": "a caregiver helping a wheelchair user get into a car in an accessible parking space, faces not visible, warm light",
        "a04": f"a man in his 40s walking alone from {GOLF} parked in an accessible parking space, carrying only a coffee, back view",
        "a05": "a hand removing a parking permit card from a car dashboard, close-up, the card text blurred",
        "a06": "a smartphone camera viewfinder framing a car parked in an accessible parking space, night, screen slightly blurred",
        "a07": "several official fine notice envelopes spread on a table with a calculator, text unreadable, top-down view",
        "a08": "a Korean prosecutor's office building exterior, modern gray building, daytime, no signage readable",
        "a09": "a stack of Korean 50,000 won banknotes beside fine notice papers on a desk, dramatic lighting, close-up",
        "a10": "a wide view of a row of accessible parking spaces painted blue with wheelchair symbols in a Korean apartment lot, one car blocking the access aisle",
        "a11": "close-up of a parking permit card with a red prohibition mark overlay feeling, dramatic shadow, text unreadable",
        "a12": "a smartphone screen showing a busy online comment thread, text blurred, held in hand, evening",
        "a13": "an empty accessible parking space with a wheelchair symbol in a Korean apartment parking lot at dusk, quiet",
    })

# 3 ─────────────────────────────────────────────────────────────
eps["vegastoy"] = dict(
    src="https://view.asiae.co.kr/article/2026101214402055074",
    src_note="아시아경제 2026-10-12 '주차 위반 딱지, 벌금 대신 이것 내세요…이색 프로그램 실시한 美' (FOX5 라스베이거스 10/9 인용)",
    t1="주차 딱지 벌금을", t2="장난감으로 내는 도시", bar="주차 위반 벌금 대신 장난감 기부", cnt=None,
    title="#딱지 대신 장난감",
    lines=[
        L("미국 라스베이거스에선 주차 딱지를 돈 말고 장난감으로 낼 수 있음.", 1, em=["장난감"], em_color="yellow"),
        L("올해 10월 1일부터 11월 13일 사이에 끊긴 딱지가 대상임.", 2,
          say="올해 시월 일일부터 십일월 십삼일 사이에 끊긴 딱지가 대상임."),
        L("조건은 딱 하나, 벌금보다 비싼 새 장난감이어야 함.", 3, em=["새 장난감"]),
        L("포장 안 뜯은 걸로 영수증까지 챙겨서 주차 사무소에 내면 끝.", 4, em=["영수증"], em_color="yellow"),
        L("딱지 받은 날부터 30일 안에 내야 함.", 5, say="딱지 받은 날부터 삼십 일 안에 내야 함.", em=["30일"]),
        L("벌금은 20달러에서 250달러, 우리 돈 3만원 안쪽에서 33만원 정도임.", 6,
          say="벌금은 이십 달러에서 이백오십 달러, 우리 돈 삼마넌 안쪽에서 삼십삼마넌 정도임.", em=["250달러"]),
        L("정지 표지판 근처나 연석에서 너무 떨어져 대면 50달러임.", 7, say="정지 표지판 근처나 연석에서 너무 떨어져 대면 오십 달러임."),
        L("모인 장난감은 집이 불안한 가정 아이들한테 감.", 8, em=["아이들"], em_color="yellow"),
        L("보드게임, 기프트카드, 6개월부터 18살 아이 장난감까지 다 됨.", 9,
          say="보드게임, 기프트카드, 육 개월부터 열여덟 살 아이 장난감까지 다 됨.", em=["보드게임"]),
        L("이게 2016년에 시의회 통과돼서 매년 하는 거임.", 10, say="이게 이천십육 년에 시의회 통과돼서 매년 하는 거임.", em=["매년"]),
        L("앨라배마 터스컬루사도 19달러 딱지를 10달러 넘는 장난감으로 받아줬음.", 11,
          say="앨라배마 터스컬루사도 열아홉 달러 딱지를 십 달러 넘는 장난감으로 받아줬음.", em=["10달러"]),
        L("벌금은 내는데 기분은 좋아지는 구조임.", 12, em=["기분은 좋아지는"]),
        L("님들은 우리나라도 이거 하면 좋겠음?", 13),
        OUT],
    tags="자동차 블랙박스 2채널, 주차번호판, 차량용 휴대폰 거치대, 차량용 방향제, 차량용 쓰레기통",
    desc="미국 라스베이거스는 주차 위반 딱지를 새 장난감 기부로 대신 낼 수 있음.\n벌금보다 비싼 새 장난감에 영수증 챙겨서 30일 안에 내면 끝.\n모인 장난감은 형편 어려운 가정 아이들한테 감.\n#shorts #주차위반 #과태료 #라스베이거스 #장난감기부",
    cm="님들은 우리나라도 이거 하면 좋겠음?",
    proof=[("라스베이거스, 주차 위반 과태료를 새 장난감 기부로 대체(연례)", "아시아경제 2026-10-12 / FOX5 10/9"),
           ("대상 2026-10-01~11-13 발부 일부 딱지, 접수 마감 12/14", "아시아경제 2026-10-12"),
           ("벌금 이상 가격의 미개봉 새 장난감 + 영수증, 주차 서비스 사무소, 발부 30일 이내", "아시아경제 2026-10-12"),
           ("벌금 20~250달러(약 2만7천~33만4천원), 정지 표지판·연석 이격 50달러", "아시아경제 2026-10-12"),
           ("기부처 치카노스 포 라 카우사(노숙·주거 불안 가정 지원)", "아시아경제 2026-10-12"),
           ("보드게임·기프트카드·생후 6개월~18세 장난감", "아시아경제 2026-10-12"),
           ("2016년 7월 시의회 승인 도입", "아시아경제 2026-10-12"),
           ("앨라배마 터스컬루사 19달러 딱지 → 10달러 이상 장난감", "아시아경제 2026-10-12")],
    P={
        "a01": "a parking ticket envelope tucked under the windshield wiper of a car on a Las Vegas street, palm trees and casino hotels blurred in background, daytime",
        "a02": "a parking enforcement officer writing a ticket next to a parked car on a sunny Las Vegas downtown street, face not visible",
        "a03": "a brand-new boxed toy set still in shrink wrap held in two hands next to a parking ticket, close-up, text unreadable",
        "a04": "a person handing a wrapped new toy box and a paper receipt across a counter at a city parking services office, faces not visible",
        "a05": "a wall calendar with a month page and a red circle around a date, a parking ticket pinned beside it, text unreadable",
        "a06": "US dollar bills and a parking ticket on a car dashboard, close-up, shallow depth of field",
        "a07": "a car parked too far from the curb near a red stop sign shape without letters on a suburban American street, daytime",
        "a08": "a cardboard donation box overflowing with new toys and board games at a community center, warm light",
        "a09": "an assortment of new board games, plush toys and gift cards arranged on a table, colorful, top-down view, no readable text",
        "a10": "an American city council chamber interior with wooden desks and microphones, empty, daytime",
        "a11": "a quiet small Southern US town street with parked cars and a toy donation bin by a city hall door, autumn",
        "a12": "a smiling driver in his 30s holding a toy box in a parking lot, holiday mood, daytime",
        "a13": "a Korean man in his 30s looking at a parking ticket on his windshield in a Seoul street, thinking, side view",
    })

for slug, e in eps.items():
    wk = os.path.join(ROOT, "work", slug)
    os.makedirs(os.path.join(wk, "v2", "ai"), exist_ok=True)
    for ln in e["lines"]:
        if not ln.get("outro"):
            assert not any(c.isdigit() for c in ln.get("say", ln["text"])), (slug, ln["text"])
            for w in ln.get("em", []):
                assert w in ln["text"], (slug, w)
    sc = {"slug": slug, "type": "란빵 자동차, 주차 뉴스", "source": e["src_note"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["bar"], "channel": "란빵",
          "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
          "style": {"sub_box": True, "bar": e["bar"], "bar_count": e["cnt"], "watermark": ""},
          "lines": e["lines"]}
    json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)
    assert len(e["title"]) <= 12, (slug, e["title"])
    assert not RISKY.search(e["title"] + e["t1"] + e["t2"]), (slug, e["title"])
    rows = "\n".join(f"| {a} | {b} |" for a, b in e["proof"])
    open(os.path.join(wk, "upload.md"), "w").write(
        f"# {slug} — 업로드 메타 (란빵)\n\n## 제목\n\n{e['title']}\n\n## 설명\n\n{e['desc']}\n\n"
        f"## 고정 댓글\n\n{e['cm']}\n\n## 쇼핑태그\n\n{e['tags']}\n\n"
        f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n원출처: {e['src']}\n")
    open(os.path.join(wk, "v2", "ai_prompts.tsv"), "w").write("".join(f"{k}\t{v}{T}\n" for k, v in e["P"].items()))
    print("ok", slug, len(e["lines"]), "lines", len(e["P"]), "ai", e["title"])
