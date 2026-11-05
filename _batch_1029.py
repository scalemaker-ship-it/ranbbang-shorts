#!/usr/bin/env python3
"""란빵 2026-10-29: 자동 10편 (daily launchd 첫 Studio 예약 회차). 대상 칸 = 2026-10-29 12:00~21:00.
- 보배드림 베스트 10/27~28 6편(selffall, sonatadisc, trench55, benzfire, bunsim91, air5000) + 뉴스 fsdtalok
  + 신차/용품(research_1029_newcar.md, 아래 EP_ 추가분).
- 근거 = work/research_1029.md. 실사 원본 = work/_photos/b1029/ (map.txt). 캡처는 _batch_1027.cap() 로 얼굴 모자이크.
- 상호(제과점 지점, 블루핸즈 지점)와 주소는 대본에 안 쓰고 캡처에서도 가린다. 실명, 번호판 없음.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1024 import B, C, L, build, IR, Y, W, R, P   # noqa: E402
from _batch_1027 import cap as _cap   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos", "b1029")
BB = "사진: 보배드림"
COMMON = "자동차 블랙박스 2채널, 블랙박스 메모리카드, 비상삼각대, 차량용 핸드폰 거치대, 차량용 방향제"
MAXC = 370


def cap(*a, **k):
    k.setdefault("ph", PH)
    return _cap(*a, **k)


def px(slug, name, boxes):
    """cap() 결과(1080x960) 위 좌표로 추가 모자이크(번호판, 블랙박스 날짜 등)."""
    import cv2
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import mosaic as M
    p = os.path.join(ROOT, "work", slug, "v2", "real", name + ".jpg")
    arr = cv2.imread(p)
    for b in boxes:
        M.pixelate(arr, *b, 14)
    cv2.imwrite(p, arr, [cv2.IMWRITE_JPEG_QUALITY, 92])


def go(S, lines, *rest):
    n = sum(len(l["text"]) for l in lines)
    assert 10 <= len(lines) <= 12, (S, len(lines))
    assert n <= MAXC, (S, "글자", n)
    for l in lines:
        assert "—" not in l["text"] and "·" not in l["text"], l["text"]
    build(S, lines, *rest)
    print(f"  chars {S} = {n} ({len(lines)}줄)")


# ───────────────────────── 1. 혼자 넘어지고 6천 요구 ─────────────────────────
def EP_selffall():
    S = "selffall"
    cap(S, "sum", "1043343_00.jpg", box=(0, 0, 1080, 450), fit=True, nofaces=True)
    cap(S, "doc1", "1043343_00.jpg", box=(0, 470, 1080, 1300), fit=True, nofaces=True, boxes=[(60, 380, 1010, 110)])
    cap(S, "doc2", "1043343_01.jpg", box=(0, 230, 1080, 1520), fit=True, nofaces=True)
    cap(S, "cctv1", "1043343_03_f1.jpg", fit=True)
    cap(S, "cctv2", "1043343_03_f3.jpg", fit=True)
    lines = [
        L("치료비 4천에 위자료 2천, 그렇게 주세요.",
          [P("cctv2", BB, s0=1.0, s1=1.2, fx=0.6, fy=0.4)], C("sagi", "r"), dialogue=True, speaker=3, emotion="toneup",
          say="치료비 사천에 위자료 이천, 그렇게 주세요."),
        L("경북 김천, 막힌 차들 사이로 무단횡단하던 사람이 차 앞에서 혼자 넘어짐.",
          [P("cctv1", BB, s0=1.0, s1=1.15), P("cctv2", BB, at="혼자", s0=1.3, s1=1.5, fx=0.6, fy=0.4, punch=True)],
          C("bike_slip"), em=["혼자 넘어짐"], fx=[("drum_rimshot", "넘어짐", 0.45)]),
        L("그러고는 운전자에게 치료비 4천에 위자료 2천을 요구함.",
          [P("sum", BB, s0=1.0, s1=1.15)], C("bill_shock", "r"), say="그러고는 운전자에게 치료비 사천에 위자료 이천을 요구함.",
          em=["위자료 2천"], em_color="yellow", pop=("6천?!", R, "요구함"), fx=[("hit_trailer_epic", "요구함", 0.5)],
          info={"kind": "bars", "at": "치료비", "title": "보행자 요구액", "items": [
              {"label": "치료비", "num": 4000, "suffix": "만원", "at": "치료비"}, {"label": "위자료", "num": 2000, "suffix": "만원", "at": "위자료"}]}),
        L("담당 경찰은 형사합의를 권했고, 민간심의위원회도 운전자 과실을 인정함.",
          [B("f01", "A Korean police station traffic investigation desk with case folders and a desk phone, fluorescent light, no people")],
          C("police"), em=["운전자 과실"], fx=[("wrong_gameshow_buzz", "인정함", 0.45)]),
        L("결론은 보행자 과실이 많지만 차량 과실도 없다고 할 수 없다는 것.",
          [P("doc1", BB, s0=1.0, s1=1.15), P("doc1", BB, at="없다고", s0=1.4, s1=1.6, fx=0.6, fy=0.85, punch=True)],
          C("komatta", "r"), em=["없다고 할 수 없다"]),
        L("그래서 있다는 거예요, 없다는 거예요?",
          [P("doc1", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.8)], C("biz_q"), dialogue=True, speaker=2, emotion="normal"),
        L("결국 검사가 증거 불충분, 혐의 없음으로 불기소를 결정함.",
          [P("doc2", BB, s0=1.0, s1=1.15), P("doc2", BB, at="혐의", s0=1.4, s1=1.6, fx=0.4, fy=0.45, punch=True)],
          C("judge", "r"), em=["혐의 없음"], em_color="yellow", pop=("불기소!", Y, "결정함"), fx=[("correct_ding", "결정함", 0.5)]),
        L("예견하기 어려운 이례적인 상황까지 대비할 의무는 없다는 것.",
          [P("doc2", BB, s0=1.3, s1=1.5, fx=0.5, fy=0.9)], C("lawyer"), em=["이례적인 상황"]),
        L("치료비를 먼저 냈던 보험사는 반환 소송으로 1년 만에 돌려받음.",
          [B("f02", "A Korean civil court document envelope and a stamped insurance claim refund form on a desk, soft light, no people")],
          C("hoken", "r"), say="치료비를 먼저 냈던 보험사는 반환 소송으로 일년 만에 돌려받음.", em=["돌려받음"], fx=[("drop_futuristic", "돌려받음", 0.5)]),
        L("예전 사건이 다시 돌면서 추천 700개를 넘김.",
          [P("cctv1", BB, s0=1.1, s1=1.25)], C("wow"), say="예전 사건이 다시 돌면서 추천 칠백개를 넘김."),
        L("님들은 이런 심의 결과, 믿을 수 있음?", [P("doc1", BB, s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "혼자 넘어져 놓고", "치료비 6천 요구", "무단횡단하다 넘어진 보행자, 심의위는 운전자 과실 인정",
       "#혼자 넘어지고 6천 요구", "보배드림 베스트 1043343 자유게시판 (2026-10-28, 추천 736, 댓글 84)",
       [("무단횡단 중 스스로 넘어짐, 치료비 4천+위자료 2천 요구, 경찰 형사합의 종용, 민간심의위 운전자 과실 인정", "원글 첨부 정리 이미지"),
        ("'보행자의 과실이 많으나, 차량의 과실도 없다고 할 수 없는 것으로 심의 의결'", "경북지방경찰청 심의 결과 공문 캡처"),
        ("교통사고처리특례법위반(치상) 증거불충분 혐의없음, '이례적인 사태까지 대비할 주의의무 없다'", "대구지검 김천지청 불기소결정서 캡처"),
        ("치료비 지급 보험사가 반환 청구소송으로 1년 만에 받아냄", "원글 첨부 이미지"),
        ("대사 '있다는 거예요, 없다는 거예요?'", "댓글 '있다고 보지 않을 수 없다... 헷갈리네' 를 대사체로"),
        ("예전 사건 재게시(공문 번호 19-372), 연도는 추정이라 대본에 안 씀", "제작 메모")],
       "무단횡단하다 혼자 넘어진 보행자가 치료비와 위자료로 6천을 요구했습니다.\n민간심의위원회는 운전자 과실도 있다고 봤지만 검사는 혐의 없음으로 불기소했습니다.\n보험사는 소송으로 치료비를 돌려받았습니다.\n\n#무단횡단 #교통사고 #불기소 #보배드림 #란빵",
       "님들은 이런 심의 결과, 믿을 수 있음?", COMMON,
       "공문 속 주소와 제과점 지점명은 모자이크. CCTV 속 사람은 원본이 작고 추가 모자이크.", [P("cctv1", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 2. 쏘나타 옵션 디스크 ─────────────────────────
def EP_sonatadisc():
    S = "sonatadisc"
    lines = [
        L("어? 이 옵션이면 대구경 디스크가 들어가야 하는데요?",
          [B("d01", "Close-up of a car wheel hub with the wheel removed on a service lift, a plain brake disc and caliper visible, workshop light, no people", s0=1.1, s1=1.3)],
          C("seibishi", "r"), dialogue=True, speaker=3, emotion="normal"),
        L("올해 6월에 쏘나타 디 엣지 N라인 풀옵션을 뽑은 글쓴이.",
          [B("d02", "A dark grey midsize sports sedan parked in a Korean apartment underground parking lot, three-quarter front view, no badges visible, no people")],
          C("dealer"), say="올해 유월에 쏘나타 디엣지 엔라인 풀옵션을 뽑은 글쓴이."),
        L("밤에 고속도로에서 돌덩이를 밟아 휠이랑 타이어가 박살 남.",
          [B("d03", "A cracked black alloy wheel with a torn flat tire on a highway shoulder at night, hazard lights glow, no people"),
           B("d03", at="박살", s0=1.3, s1=1.5, fx=0.5, fy=0.55, punch=True)],
          C("drv_shock", "r"), em=["박살 남"], pop=("쾅!!", R, "박살"), shake="박살", fx=[("glass_smash", "박살", 0.5)]),
        L("가까운 공식 정비소에 맡겼는데, 담당자가 이상한 걸 발견함.",
          [B("d04", "Inside a car dealership service bay, a sedan on a two-post lift with its front wheels removed, tools on a cart, no people")],
          C("seibishi"), em=["이상한 걸"]),
        L("옵션대로면 대구경 디스크가 달려야 하는데, 출고 때부터 기본 디스크였던 것.",
          [B("d01", at="기본", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)],
          C("drv_surprise", "r"), em=["기본 디스크"], em_color="yellow", fx=[("hit_trailer_epic", "기본", 0.5)],
          info={"kind": "compare", "at": "옵션대로면", "title": "들어가야 할 것 vs 달린 것", "items": [
              {"label": "옵션표", "color": W, "at": "옵션대로면", "rows": [["브레이크", "대구경 디스크", Y]]},
              {"label": "실제 장착", "color": R, "at": "기본", "rows": [["브레이크", "기본 디스크", W]]}]}),
        L("보증 덕분에 무료로 싹 교체는 받았음.",
          [B("d05", "A brand new large drilled brake disc in its box on a workbench in a car service center, close-up, no people")],
          C("biz_smile"), em=["무료로"], fx=[("correct_ding", "교체는", 0.45)]),
        L("근데 사고 안 났으면 평생 모르고 탔을 거라, 따로 배상이 되는지 물어본 글.",
          [B("d02", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("drv_think", "r"), em=["평생 모르고"]),
        L("추천 131개 1등 댓글은, 골 때리긴 해도 배상 같은 건 안 해준다는 말.",
          [B("d06", "A smartphone on a car seat showing an online community comment thread, text blurred, evening light")],
          C("biz_laugh"), say="추천 백삼십일개 일등 댓글은, 골 때리긴 해도 배상 같은 건 안 해준다는 말.",
          em=["배상 같은 건"], fx=[("wrong_gameshow_buzz", "안", 0.45)]),
        L("엔진오일 무료 교환권으로 회유하겠죠.",
          [B("d07", "A bottle of engine oil and a printed service coupon on a service center reception counter, no people")],
          C("sales", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("2등 댓글은 모르고 타는 차주가 더 많을 거라는 말.",
          [B("d04", s0=1.2, s1=1.4, fx=0.5, fy=0.5)], C("shinpai"), say="이등 댓글은 모르고 타는 차주가 더 많을 거라는 말.", em=["더 많을"]),
        L("님들은 이거 보상 따로 요구함, 교체로 끝냄?", [B("d01", s0=1.0, s1=1.12)], C("biz_q", "r"), fx=[("pop_bubble", "끝냄")]),
    ]
    go(S, lines, "풀옵션 쏘나타 뽑았는데", "디스크가 기본이었다", "N라인 풀옵션, 휠 수리하다 기본 디스크 발견",
       "#옵션 빠진 채 출고", "보배드림 베스트 1043387 자유게시판 (2026-10-28, 추천 624, 댓글 85)",
       [("2026-06 쏘나타 디 엣지 N라인 2.5T 풀옵션(N퍼포먼스 패키지 포함) 출고", "원글 본문"),
        ("야간 고속도로 돌덩이로 휠, 타이어 파손, 공식 정비점 입고", "원글 본문"),
        ("'들어간 옵션에 의하면 하이브리드 대구경 디스크가 장착되어야 하는데 기본 디스크가 장착된 채 출고'", "원글 본문(정비 담당자 설명을 대사체로)"),
        ("보증으로 무료 교체, 추가 배상 가능 여부 질문", "원글 본문"),
        ("댓글 1위(131) 배상은 안 해줌, 2위(114) 모르고 타는 차주 많을 듯, 3위(98) 엔진오일 무료교환권으로 회유", "원글 댓글(3위는 대사체)")],
       "풀옵션 쏘나타 N라인을 뽑았는데 휠 수리하다가 옵션 디스크 대신 기본 디스크가 달려 출고된 걸 알았습니다.\n보증으로 무료 교체는 받았습니다.\n댓글은 배상은 기대하기 어렵다는 반응입니다.\n\n#쏘나타 #신차옵션 #출고검수 #보배드림 #란빵",
       "님들은 이거 보상 따로 요구함, 교체로 끝냄?",
       "자동차 브레이크 패드, 차량용 공기주입기, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 방향제",
       "정비점 지점명 미표기. 디스크 사양, 패키지 가격은 미확인이라 숫자 안 씀. 원글 사진 없음 → 배경 전부 생성(차는 로고 없는 일반 세단).",
       [B("d05", s0=1.0, s1=1.1)])


# ───────────────────────── 3. 공영주차장 덮개 5:5 ─────────────────────────
def EP_trench55():
    S = "trench55"
    cap(S, "t1", "1043342_01.jpg", fit=False, nofaces=True)
    cap(S, "t2", "1043342_02.jpg", fit=False, nofaces=True)
    cap(S, "t5", "1043342_05.jpg", cx=0.5, cy=0.45, nofaces=True)
    cap(S, "t6", "1043342_06.jpg", nofaces=True)
    cap(S, "t7", "1043342_07.jpg", nofaces=True, boxes=[(0, 0, 330, 160)])
    cap(S, "bb", "1043342_10.jpg", box=(0, 0, 800, 560), fit=True, nofaces=True)
    cap(S, "cc", "1043342_09.jpg", box=(0, 500, 800, 1067), fit=True, nofaces=True, boxes=[(330, 250, 160, 90)])
    cap(S, "dash", "1043342_11_f3.jpg", nofaces=True)
    px(S, "dash", [(330, 690, 190, 110)])
    lines = [
        L("주차장 시설물에 박았는데 제 과실이 반이라고요?",
          [P("t5", BB, s0=1.0, s1=1.2)], C("drv_angry", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("10월 5일, 도시공사가 운영하는 공영주차장 2층에서 3층 올라가는 램프.",
          [P("dash", BB, s0=1.0, s1=1.15)], C("drv_smile"), say="시월 오일, 도시공사가 운영하는 공영주차장 이층에서 삼층 올라가는 램프."),
        L("바닥 배수로 덮개가 툭 튀어나와 있었고, 범퍼랑 하부가 같이 깨짐.",
          [P("t1", BB, s0=1.0, s1=1.2), P("t7", BB, at="범퍼랑", s0=1.1, s1=1.3)],
          C("drv_shock", "r"), em=["툭 튀어나와"], pop=("돌출!", R, "튀어나와"), shake="깨짐", fx=[("glass_smash", "깨짐", 0.5)]),
        L("주차장은 어두웠고 덮개 색이 바닥이랑 비슷해서 동승자도 못 봤음.",
          [P("bb", BB, s0=1.0, s1=1.15), P("t2", BB, at="덮개", s0=1.2, s1=1.4, fx=0.4, fy=0.5, punch=True)],
          C("komatta"), em=["동승자도"]),
        L("다음 날 도시공사는 보상해 준다고 했고, 내 보험사도 과실이 없을 거라 했음.",
          [B("p01", "An empty municipal parking garage office counter with a desk phone and forms, fluorescent light, Korea, no people")],
          C("phone_man", "r"), em=["보상해 준다고"], fx=[("notify_message_pop", "보상해", 0.45)]),
        L("그런데 22일 뒤 공제회 손해사정 담당이 통보한 과실은 5대5.",
          [P("t6", BB, s0=1.0, s1=1.2), P("t6", BB, at="5대5", s0=1.4, s1=1.6, fx=0.6, fy=0.6, punch=True)],
          C("bill_shock"), say="그런데 이십이일 뒤 공제회 손해사정 담당이 통보한 과실은 오대오.",
          em=["5대5"], em_color="yellow", pop=("5:5?!", R, "5대5"), fx=[("hit_trailer_epic", "5대5", 0.5)],
          info={"kind": "compare", "at": "22일", "title": "과실 비율", "items": [
              {"label": "처음 안내", "color": W, "at": "22일", "rows": [["운전자", "과실 없음", W]]},
              {"label": "22일 뒤 통보", "color": R, "at": "5대5", "rows": [["운전자", "50%", Y]]}]}),
        L("근거는 내려오는 쪽 덮개가 튀어나와 있었으니 봤어야 한다는 것.",
          [P("cc", BB, s0=1.0, s1=1.15)], C("hoken", "r"), em=["봤어야 한다"], fx=[("wrong_gameshow_buzz", "것", 0.45)]),
        L("국가배상법 5조는 공공시설 관리에 하자가 있으면 지자체가 배상하게 함.",
          [P("t2", BB, s0=1.0, s1=1.15)], C("judge"), say="국가배상법 오조는 공공시설 관리에 하자가 있으면 지자체가 배상하게 함.",
          em=["관리에 하자"], em_color="yellow", fx=[("drop_futuristic", "국가배상법", 0.5)],
          info={"kind": "quotes", "at": "국가배상법", "title": "국가배상법 5조", "items": [
              {"text": "공공시설 설치, 관리 하자", "at": "공공시설"}, {"text": "지자체가 배상", "at": "배상하게"}]}),
        L("비슷한 사고에서 60대40을 거절하고 소송해 100대0으로 이겼다는 댓글도 있음.",
          [B("p02", "A Korean courthouse corridor with wooden benches and a case number board, daylight, no people")],
          C("lawyer", "r"), say="비슷한 사고에서 육십대사십을 거절하고 소송해 백대영으로 이겼다는 댓글도 있음.",
          em=["100대0"], fx=[("correct_ding", "이겼다는", 0.5)]),
        L("님들은 이거 5대5 받아들임, 소송 감?", [P("t1", BB, s0=1.0, s1=1.12)], C("biz_q"), say="님들은 이거 오대오 받아들임, 소송 감?",
          fx=[("pop_bubble", "감")]),
    ]
    go(S, lines, "공영주차장 덮개에 박았는데", "내 과실이 반이라고?", "튀어나온 배수로 덮개에 범퍼 파손, 22일 뒤 과실 5:5 통보",
       "#공영주차장 과실 5:5", "보배드림 베스트 1043342 교통사고/블박 (2026-10-28, 추천 263, 댓글 103)",
       [("10/5 도시공사 운영 공영주차장 2층→3층 램프, 돌출된 트렌치 커버와 충돌, 범퍼, 하부커버 파손", "원글 본문, 사진 1~2"),
        ("주차장 내부 어두움, 덮개 색이 바닥과 유사, 동승자도 식별 못 함", "원글 본문"),
        ("10/6 도시공사 '보상 내부 결재 예정', 내 보험사 '과실 없을 것' → 접수 취소", "원글 본문"),
        ("10/14 한국지방재정공제회 위임 손해사정 담당 연락, 10/27 과실 5:5 통보(22일 뒤)", "원글 본문"),
        ("과실 근거 = 내려오는 방향 트렌치커버 돌출", "원글 본문, 사진 3"),
        ("국가배상법 5조 1항 공공 영조물 설치, 관리 하자 시 국가나 지자체 배상", "casenote 국가배상법 원문"),
        ("댓글 2위(69) 경기도 유사 사고 60:40 거절 후 소송으로 100:0", "원글 댓글")],
       "공영주차장 램프에 튀어나온 배수로 덮개에 범퍼와 하부가 깨졌습니다.\n처음엔 보상해 준다더니 22일 뒤 과실 5대5 통보가 왔습니다.\n국가배상법 5조는 공공시설 관리 하자를 지자체가 배상하게 합니다.\n\n#공영주차장 #과실비율 #국가배상 #보배드림 #란빵",
       "님들은 이거 5대5 받아들임, 소송 감?",
       "자동차 블랙박스 2채널, 차량용 범퍼 가드, 자동차 언더커버, 차량용 핸드폰 거치대, 차량용 방향제",
       "도시공사 이름, 지역 미표기. 사진 7 상단 번호판 자리, CCTV 출력물 번호판 모자이크.", [P("t5", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 4. 대각선 주차 벤츠 ─────────────────────────
def EP_benzfire():
    S = "benzfire"
    cap(S, "full", "1043386_00.jpg", fit=True, nofaces=True)
    cap(S, "car", "1043386_00.jpg", box=(200, 720, 900, 1250), fit=False, nofaces=True)
    cap(S, "sign", "1043386_00.jpg", box=(0, 820, 900, 1400), fit=False, nofaces=True)
    cap(S, "top", "1043386_00.jpg", box=(300, 480, 900, 1050), fit=False, nofaces=True)
    lines = [
        L("장애인 구역 방해로 신고요!",
          [P("full", BB, s0=1.0, s1=1.2)], C("rage", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("어느 아파트 주차장, 매일 주차칸을 넘어 이중주차하던 검은 벤츠.",
          [P("top", BB, s0=1.0, s1=1.15)], C("meiwaku"), em=["이중주차"]),
        L("오늘은 아침부터 장애인 구역 옆 노란 빗금 위에 대각선으로 걸쳐 세움.",
          [P("car", BB, s0=1.0, s1=1.2), P("car", BB, at="대각선으로", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("drv_shock", "r"), em=["대각선으로"], pop=("대각선?!", R, "대각선으로"), fx=[("hit_trailer_epic", "대각선으로", 0.5)]),
        L("뒤쪽 바닥엔 소방차 구역 글씨까지 있음.",
          [P("sign", BB, s0=1.0, s1=1.2, fx=0.2, fy=0.6), P("sign", BB, at="소방차", s0=1.4, s1=1.6, fx=0.15, fy=0.6, punch=True)],
          C("fire119"), em=["소방차 구역"], fx=[("drum_rimshot", "있음", 0.4)]),
        L("관리실에 말해도 해결이 안 됐다는 글에 추천이 832개.",
          [P("full", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.6)], C("komatta", "r"), say="관리실에 말해도 해결이 안 됐다는 글에 추천이 팔백삼십이개.",
          em=["추천이 832개"]),
        L("2등 댓글은 SNS 올릴 시간에 신고부터 하라는 말.",
          [B("b01", "A smartphone held over a car hood showing a civic safety report app camera screen, screen content blurred, apartment parking lot, daytime")],
          C("photo_woman"), say="이등 댓글은 에스엔에스 올릴 시간에 신고부터 하라는 말.", em=["신고부터"], fx=[("notify_message_pop", "신고부터", 0.45)]),
        L("장애인 구역에 그냥 세우면 10만원, 통행로를 막아 주차를 방해하면 50만원.",
          [P("sign", BB, s0=1.0, s1=1.15, fx=0.6, fy=0.6)], C("judge", "r"), say="장애인 구역에 그냥 세우면 십마넌, 통행로를 막아 주차를 방해하면 오십마넌.",
          em=["50만원"], em_color="yellow", fx=[("drop_futuristic", "방해하면", 0.5)],
          info={"kind": "bars", "at": "장애인", "title": "장애인 구역 과태료", "items": [
              {"label": "주차", "num": 10, "suffix": "만원", "at": "10만원"}, {"label": "주차 방해", "num": 50, "suffix": "만원", "at": "50만원", "flash": "50만원"}]}),
        L("소방차 전용구역을 가로막으면 1차 50만원, 최대 100만원 과태료.",
          [B("b02", "A red-and-yellow painted fire engine only zone on the asphalt of a Korean apartment complex, empty, daytime, no people, no text")],
          C("police"), say="소방차 전용구역을 가로막으면 일차 오십마넌, 최대 백마넌 과태료.", em=["최대 100만원"], fx=[("correct_ding", "과태료", 0.5)]),
        L("벤츠 타면 이 정도는 해도 되나요?",
          [P("car", BB, s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("biz_angry", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("님들 아파트에도 이런 차 있음?", [P("full", BB, s0=1.0, s1=1.1)], C("biz_q"), fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "매일 칸 넘던 벤츠", "오늘은 대각선 주차", "장애인 구역 옆 빗금 위 대각선, 뒤엔 소방차 구역",
       "#대각선 주차 벤츠", "보배드림 베스트 1043386 자유게시판 (2026-10-28, 추천 832, 댓글 201)",
       [("아파트 지상 주차장, 매일 칸 넘어 이중주차, 오늘은 대각선 주차, 관리실도 해결 못 함", "원글 본문, 사진"),
        ("댓글 1위(439) '장애인 주차구역 방해로 신고요', 2위(314) 'sns 올릴 시간에 신고부터'", "원글 댓글(1위는 대사체)"),
        ("장애인 전용구역 표지 없는 주차 금지(17조 4항), 통행로 가로막는 등 주차방해 금지(17조 5항)", "casenote 장애인등편의법 17조"),
        ("과태료 주차 10만원, 주차방해 50만원", "노컷뉴스 2026-10-25, 금강일보 2026-09-29(당진시)"),
        ("소방차 전용구역 방해 1차 50만원, 2차 이상 100만원(소방기본법 56조, 100만원 이하)", "새전북신문 2026-09-22(익산소방서), 충남일보(아산소방서)"),
        ("대사 '벤츠 타면 이 정도는 해도 되나요?'", "원글 제목")],
       "매일 주차칸을 넘던 벤츠가 오늘은 장애인 구역 옆 빗금 위에 대각선으로 섰습니다.\n장애인 구역 주차방해는 과태료 50만원, 소방차 전용구역 방해는 최대 100만원입니다.\n댓글은 신고부터 하라는 반응입니다.\n\n#주차빌런 #장애인주차구역 #소방차전용구역 #보배드림 #란빵",
       "님들 아파트에도 이런 차 있음?",
       "차량용 주차번호판, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 방향제, 자동차 도어가드",
       "번호판은 사진상 안 보임(위에서 찍음). 아파트 이름, 지역 미표기. 빗금이 장애인 구역 통행로인지는 사진만으로 확정 못 해 '옆 노란 빗금'으로만 씀.",
       [P("top", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 5. 이중실선 끼어들기 9:1 ─────────────────────────
def EP_bunsim91():
    S = "bunsim91"
    cap(S, "v1", "1043173_00_f1.jpg", box=(0, 0, 1700, 1000), nofaces=True)
    cap(S, "v2", "1043173_00_f3.jpg", box=(0, 0, 1700, 1000), cx=0.7, nofaces=True)
    cap(S, "v3", "1043173_00_f5.jpg", box=(0, 0, 1700, 1000), cx=0.7, nofaces=True)
    cap(S, "m1", "1043173_01_f1.jpg", box=(0, 0, 1750, 1000), cx=0.6)
    cap(S, "m2", "1043173_01_f3.jpg", box=(0, 0, 1750, 1000), cx=0.75)
    px(S, "v3", [(860, 550, 100, 60)])
    for n in ("v1", "v2", "v3", "m1", "m2"):
        px(S, n, [(660, 700, 420, 260)])   # 블랙박스 날짜 표시(기기 시계가 실제와 달라 가림)
    lines = [
        L("브레이크를 밟았어야죠.",
          [P("v2", BB, s0=1.0, s1=1.2)], C("biz_think", "r"), dialogue=True, speaker=3, emotion="normal", say="브레이크를 밟았어야죠."),
        L("8월 초 양화대교 끝, 맨 오른쪽을 달리던 모하비가 이중실선에서 갑자기 들어옴.",
          [P("v1", BB, s0=1.0, s1=1.15), P("v3", BB, at="이중실선에서", s0=1.2, s1=1.4, fx=0.75, fy=0.5, punch=True)],
          C("aori"), say="팔월 초 양화대교 끝, 맨 오른쪽을 달리던 모하비가 이중실선에서 갑자기 들어옴.",
          em=["이중실선에서"], pop=("끼어들기!", R, "들어옴"), shake="들어옴", fx=[("boom_subby_kick", "들어옴", 0.45)]),
        L("그걸 피하던 글쓴이가 왼쪽 뒤에서 오던 오토바이와 부딪힘.",
          [P("m1", BB, s0=1.0, s1=1.2), P("m2", BB, at="오토바이와", s0=1.2, s1=1.4, fx=0.8, fy=0.4, punch=True)],
          C("jiko_man", "r"), em=["오토바이와"], fx=[("glass_smash", "부딪힘", 0.5)]),
        L("모하비는 6대4를 주장했고, 결국 분쟁심의위원회까지 감.",
          [B("q01", "A Korean car insurance dispute committee meeting room with an empty long table and name placards turned away, no people")],
          C("hoken"), say="모하비는 육대사를 주장했고, 결국 분쟁심의위원회까지 감.", em=["6대4를"]),
        L("결과는 9대1, 모하비 과실 90.",
          [P("v3", BB, s0=1.0, s1=1.2, fx=0.7, fy=0.5)], C("banzai", "r"), say="결과는 구대일, 모하비 과실 구십.",
          em=["9대1"], em_color="yellow", pop=("9:1!", Y, "9대1"), fx=[("hit_trailer_epic", "9대1", 0.5)],
          info={"kind": "compare", "at": "결과는", "title": "과실 비율", "items": [
              {"label": "모하비 주장", "color": W, "at": "결과는", "rows": [["모하비:나", "6:4", W]]},
              {"label": "분심위 결과", "color": R, "at": "9대1", "rows": [["모하비:나", "9:1", Y]]}]}),
        L("글쓴이 과실 10은 브레이크 없이 피하기만 한 점 때문.",
          [P("m2", BB, s0=1.1, s1=1.3, fx=0.7, fy=0.5)], C("drv_think"), say="글쓴이 과실 십은 브레이크 없이 피하기만 한 점 때문.",
          em=["브레이크 없이"], fx=[("wrong_gameshow_buzz", "때문", 0.45)]),
        L("도로교통법 14조, 진로변경 금지 표시가 있는 곳에선 차로를 바꾸면 안 됨.",
          [B("q02", "A Korean multi-lane bridge road with solid double white lane lines, daytime, light traffic far away, no people")],
          C("judge", "r"), say="도로교통법 십사조, 진로변경 금지 표시가 있는 곳에선 차로를 바꾸면 안 됨.",
          em=["진로변경 금지"], em_color="yellow", fx=[("drop_futuristic", "도로교통법", 0.5)]),
        L("경찰 사실확인원에도 이중실선 급차로변경 사고라고 적혀 있었음.",
          [B("q03", "A Korean police traffic accident confirmation document on a desk with an official stamp, text unreadable, no people")],
          C("police"), em=["급차로변경"]),
        L("글쓴이는 이제 이중실선도 안 믿고 다른 차선으로 피해 다닌다고 함.",
          [P("v1", BB, s0=1.2, s1=1.35)], C("drv_smile", "r"), em=["안 믿고"]),
        L("님들은 무과실 못 받은 이 결과, 납득 감?", [P("v2", BB, s0=1.0, s1=1.1)], C("biz_q"), fx=[("pop_bubble", "납득")]),
    ]
    go(S, lines, "이중실선에서 끼어든 차", "피했는데 내 과실 10%", "양화대교 이중실선 급차로변경, 분심위 결과 9:1",
       "#이중실선 끼어들기 9:1", "보배드림 베스트 1043173 교통사고/블박 (2026-10-27, 추천 106, 댓글 14)",
       [("8월 초 양화대교 끝단, 가장 우측 모하비 이중실선 급 차로변경 → 피하다 왼쪽 후방 오토바이와 사고", "원글 본문, 블랙박스 영상 2개"),
        ("모하비 6:4 주장 → 분심위 9(모하비):1(글쓴이)", "원글 본문"),
        ("'브레이크를 밟았어야 했다' 의견이 적용돼 과실 1", "원글 본문(대사체)"),
        ("교통사고 사실확인원 '이중실선에서 급차로변경으로 인한 사고'", "원글 본문"),
        ("도로교통법 14조 5항 안전표지로 진로변경이 금지된 곳에서 진로변경 금지", "casenote 도로교통법 14조"),
        ("오토바이 운전자 부상 여부는 원글에 없어 안 씀", "제작 메모")],
       "양화대교에서 이중실선을 넘어 들어온 모하비를 피하다 오토바이와 부딪혔습니다.\n모하비는 6대4를 주장했지만 분쟁심의위원회 결과는 9대1입니다.\n이중실선은 진로변경 금지 표시입니다.\n\n#이중실선 #과실비율 #분심위 #보배드림 #란빵",
       "님들은 무과실 못 받은 이 결과, 납득 감?", COMMON,
       "번호판은 화면상 판독 불가(모니터 촬영본). 오토바이 운전자 얼굴 안 보임.", [P("v1", BB, s0=1.0, s1=1.1)])


# ───────────────────────── 6. 타이어 바람 5천원 ─────────────────────────
def EP_air5000():
    S = "air5000"
    lines = [
        L("벽에 5천원이라고 써 놨잖아요.",
          [B("a01", "A small car repair shop corner in an office building basement, an air compressor hose hanging on the wall, a handwritten price sign blurred, fluorescent light, no people", s0=1.1, s1=1.3)],
          C("seibishi", "r"), dialogue=True, speaker=3, emotion="normal", say="벽에 오천원이라고 써 놨잖아요."),
        L("날이 추워져 회사 차 타이어 바람이 약해지자, 건물 지하 정비소에 넣어 달라고 한 글쓴이.",
          [B("a02", "A company sedan parked in an office building basement garage next to a small repair shop entrance, cold morning, no people")],
          C("samui"), em=["바람이 약해지자"]),
        L("처음 보는 정비사가 바람을 채우더니 5천원을 달라고 함.",
          [B("a03", "Close-up of a tire air chuck attached to a car tire valve, a pressure gauge in view, workshop floor, no faces"),
           B("a03", at="5천원을", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("drv_surprise", "r"), say="처음 보는 정비사가 바람을 채우더니 오천원을 달라고 함.",
          em=["5천원을"], em_color="yellow", pop=("5천원?!", R, "5천원을"), fx=[("hit_trailer_epic", "5천원을", 0.5)]),
        L("7년 동안 돈 낸 적이 없었다며, 직원들에게 그 정비소 쓰지 말라고 지시함.",
          [B("a04", "An office desk with a company car key, a stack of papers and a desk phone, window light, no people")],
          C("biz_angry"), say="칠년 동안 돈 낸 적이 없었다며, 직원들에게 그 정비소 쓰지 말라고 지시함.",
          em=["쓰지 말라고"], fx=[("wrong_gameshow_buzz", "지시함", 0.45)]),
        L("근데 댓글 반응은 정반대.",
          [B("a05", "A smartphone lying on a car dashboard showing a busy comment thread, text blurred, daylight")],
          C("biz_shock", "r"), em=["정반대"], fx=[("scratch_vinyl", "정반대", 0.45)]),
        L("추천 96개 1등 댓글은, 무료는 서비스였을 뿐이고 불편하면 공기주입기를 사라는 말.",
          [B("a06", "A compact portable cordless tire inflator with a digital display on a car trunk floor, close-up, no logo, no people")],
          C("biz_laugh"), say="추천 구십육개 일등 댓글은, 무료는 서비스였을 뿐이고 불편하면 공기주입기를 사라는 말.",
          em=["공기주입기"], em_color="yellow",
          info={"kind": "bars", "at": "추천", "title": "댓글 추천", "items": [
              {"label": "돈 받는 게 맞다", "num": 96, "suffix": "개", "at": "추천"}, {"label": "개진상", "num": 63, "suffix": "개", "at": "추천"},
              {"label": "셀프여야 무료", "num": 49, "suffix": "개", "at": "추천"}]}),
        L("셀프로 넣어야 무료 아닌가요?",
          [B("a01", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("drv_q", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("기온이 떨어지면 타이어 공기압도 같이 떨어짐.",
          [B("a07", "A car dashboard at a frosty winter morning showing a tire pressure warning light glowing amber, no people")],
          C("drv_think"), em=["같이 떨어짐"], fx=[("drop_futuristic", "떨어짐", 0.5)]),
        L("그래서 날이 추워지면 경고등 뜨기 전에 공기압부터 보는 게 좋음.",
          [B("a03", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("drv_idea", "r"), em=["공기압부터"], fx=[("correct_ding", "좋음", 0.5)]),
        L("님들은 바람 넣는 데 5천원, 낼 만함?", [B("a06", s0=1.0, s1=1.12)], C("biz_q"), say="님들은 바람 넣는 데 오천원, 낼 만함?",
          fx=[("pop_bubble", "만함")]),
    ]
    go(S, lines, "타이어 바람 넣었더니", "5천원 내라는 정비소", "7년 무료였던 공기 주입, 처음 보는 정비사가 5천원",
       "#타이어 바람 5천원", "보배드림 베스트 1043277 자유게시판 (2026-10-27, 추천 81, 댓글 113)",
       [("근무 건물 지하 정비소, 회사차 관리, 날 추워져 바람 넣어 달라 함", "원글 본문"),
        ("처음 보는 정비사가 바람 채운 뒤 5천원 요구, '벽에 5천원이라고 써 놨다'", "원글 본문(대사체)"),
        ("사무실 7년차, 대꾸 없이 내고 직원들에게 이용 금지 지시", "원글 본문"),
        ("댓글 1위(96) 서비스였을 뿐 돈 받는 게 잘못 아님, 공기주입기 사면 됨, 2위(63) 개 진상, 3위(49) 셀프로 넣어야 무료 아닌가요", "원글 댓글(3위는 대사체)"),
        ("기온 하락 시 공기압 하락(약 5.6℃당 1psi)", "타이어 공기압 일반 안내(tirepsi 편 근거표), 대본엔 숫자 안 씀")],
       "날이 추워져 타이어 바람을 넣었더니 처음 보는 정비사가 5천원을 달라고 했습니다.\n댓글은 무료는 서비스였을 뿐이라는 반응이 1등입니다.\n기온이 떨어지면 공기압도 떨어집니다.\n\n#타이어공기압 #정비소 #공기주입기 #보배드림 #란빵",
       "님들은 바람 넣는 데 5천원, 낼 만함?",
       "차량용 무선 공기주입기, 타이어 공기압 측정기, 차량용 에어컴프레서, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대",
       "정비소 위치, 이름 미표기. 원글 사진 없음 → 배경 전부 생성.", [B("a06", s0=1.0, s1=1.1)])


# ───────────────────────── 7. 테슬라 FSD 탈옥 80명 송치 ─────────────────────────
def EP_fsdtalok():
    S = "fsdtalok"
    cap(S, "tv", "1043402_00.png", box=(20, 262, 862, 742), fit=True, nofaces=True)
    lines = [
        L("지금 FSD 돈 안 내도 쓸 수 있단 얘기, 루머 아닙니다.",
          [B("e01", "A phone screen showing a social media video of a car interior with hands off the steering wheel, screen content blurred, night", s0=1.1, s1=1.3)],
          C("sagi", "r"), dialogue=True, speaker=3, emotion="toneup", say="지금 에프에스디 돈 안 내도 쓸 수 있단 얘기, 루머 아닙니다."),
        L("이런 영상 보고 테슬라 자율주행을 몰래 푼 차주 80명이 송치됨.",
          [P("tv", "화면: TV조선", s0=1.0, s1=1.2)], C("police"), say="이런 영상 보고 테슬라 자율주행을 몰래 푼 차주 팔십명이 송치됨.",
          em=["80명이"], pop=("80명!", R, "송치됨"), fx=[("hit_trailer_epic", "송치됨", 0.5)]),
        L("서울경찰청은 비인가 장치 21개를 압수하고 자동차관리법 위반으로 넘김.",
          [P("tv", "화면: TV조선", at="비인가", s0=1.3, s1=1.55, fx=0.55, fy=0.6, punch=True)], C("police_angry", "r"),
          say="서울경찰청은 비인가 장치 이십일개를 압수하고 자동차관리법 위반으로 넘김.", em=["자동차관리법 위반"], em_color="yellow",
          fx=[("drop_futuristic", "압수하고", 0.5)]),
        L("국내 테슬라 24만 대 중 18만 대는 FSD를 아예 못 씀.",
          [B("e02", "Rows of new white electric sedans parked at a vehicle import port lot in Korea, overcast, no people, no logos")],
          C("ev"), say="국내 테슬라 이십사만 대 중 십팔만 대는 에프에스디를 아예 못 씀.", em=["아예 못 씀"],
          info={"kind": "bars", "at": "국내", "title": "국내 테슬라", "items": [
              {"label": "전체", "num": 24, "suffix": "만 대", "at": "국내"}, {"label": "FSD 불가", "num": 18, "suffix": "만 대", "at": "18만", "flash": "18만"}]}),
        L("대부분 중국산이라서고, 미국산도 월 15만원 구독을 해야 쓸 수 있음.",
          [B("e03", "A minimalist electric car center touchscreen showing a subscription payment screen, text blurred, interior, no people")],
          C("saifu", "r"), say="대부분 중국산이라서고, 미국산도 월 십오마넌 구독을 해야 쓸 수 있음.", em=["월 15만원"], em_color="yellow",
          fx=[("cash_register_fake", "15만원", 0.45)]),
        L("그래서 해외에서 산 장치나 직접 만든 장치를 꽂아 기능을 풀었음.",
          [P("tv", "화면: TV조선", s0=1.2, s1=1.4, fx=0.6, fy=0.6)], C("robot"), em=["직접 만든"]),
        L("반전은 테슬라가 3월에 무단 활성화 사례를 국토부에 넘겼다는 것.",
          [B("e04", "A government ministry building entrance in Sejong, Korea, glass facade, overcast, no people")],
          C("biz_surprise", "r"), say="반전은 테슬라가 삼월에 무단 활성화 사례를 국토부에 넘겼다는 것.",
          em=["테슬라가"], pop=("테슬라가 신고?!", Y, "넘겼다는"), fx=[("hit_trailer_epic", "넘겼다는", 0.5)]),
        L("비인가 장치로 활성화하면 소프트웨어 오류가 날 가능성도 높아요.",
          [B("e05", "Close-up of a small unbranded circuit board with wires plugged into a car's interior wiring harness under the dashboard, no people")],
          C("biz_think"), dialogue=True, speaker=2, emotion="normal"),
        L("사고가 나면 보험 처리를 못 받을 수도 있다고 함.",
          [B("e06", "A car insurance claim form and a car key on a table, soft light, no people")],
          C("hoken", "r"), em=["보험 처리를"], fx=[("wrong_gameshow_buzz", "있다고", 0.45)]),
        L("님들은 월 15만원 내고 FSD 쓸 거임?", [P("tv", "화면: TV조선", s0=1.0, s1=1.1)], C("biz_q"),
          say="님들은 월 십오마넌 내고 에프에스디 쓸 거임?", fx=[("pop_bubble", "거임")]),
    ]
    go(S, lines, "FSD 몰래 풀었다가", "테슬라 차주 80명 송치", "비인가 장치로 FSD 활성화, 장치 21개 압수",
       "#테슬라 FSD 탈옥 송치", "보배드림 베스트 1043402 + TV조선 2026-10-27 (n.news.naver.com/article/448/0000647344)",
       [("서울경찰청 교통범죄수사팀, FSD 불법 활성화 80명 자동차관리법 위반 혐의 공소청 송치, 장치 21개 압수", "TV조선, 연합뉴스TV, 동아일보, 경향신문 2026-10-27~28"),
        ("SNS 영상 '지금 테슬라 FSD 돈 안 내도 쓸 수 있단 얘기 그냥 루머 아닙니다'", "TV조선 리포트(대사로 인용)"),
        ("국내 테슬라 24만 대 중 18만 대 FSD 불가, 미국산은 한미 FTA로 가능, 월 15만원 구독", "TV조선, 문화일보 제목, fsdapply 근거(238,968대 중 185,491대)"),
        ("중국, 유럽에서 산 장치나 직접 제작한 장치 연결", "연합뉴스TV, 엠투데이"),
        ("테슬라코리아가 3월 무단 활성화 사례를 국토부에 전달 → 수사 의뢰", "TV조선"),
        ("이호근 대덕대 교수 '비인가 장치를 이용해서 FSD를 활성화했을 경우에는 소프트웨어에서 어떤 오류가 발생할 가능성도 높고요'", "TV조선(대사로 다듬어 인용)"),
        ("사고 시 보험처리 못 받을 수 있음", "TV조선 리포트"),
        ("처벌 수위, 20달러 장치는 1곳 보도라 대본에서 뺌", "제작 메모")],
       "테슬라 FSD를 비인가 장치로 몰래 활성화한 차주 80명이 자동차관리법 위반으로 송치됐습니다.\n국내 테슬라 대부분은 중국산이라 FSD를 못 씁니다.\n무단 활성화 사례를 국토부에 넘긴 건 테슬라였습니다.\n\n#테슬라 #FSD #자율주행 #자동차관리법 #란빵",
       "님들은 월 15만원 내고 FSD 쓸 거임?",
       "차량용 무선충전 거치대, 테슬라 모델Y 액세서리, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 방향제",
       "TV조선 화면 캡처는 운전대와 장치 장면만(기자 얼굴 영역 잘라냄). 실존 인물 발언은 교수 인용 1개만, 원문 취지 그대로.",
       [B("e05", s0=1.0, s1=1.1)])


# ───────────────────────── 8. 벤츠 전기 GLB ─────────────────────────
MB = "사진: 메르세데스-벤츠 코리아"


def EP_glbev():
    S = "glbev"
    cap(S, "g1", "benzglbev_1.jpg", cx=0.45, nofaces=True)
    cap(S, "g2", "benzglbev_2.jpg", cx=0.55, nofaces=True)
    cap(S, "g3", "benzglbev_3.jpg", cx=0.7, nofaces=True)
    cap(S, "g4", "benzglbev_4.jpg", cx=0.45, nofaces=True)
    lines = [
        L("벤츠 전기 SUV가 6천만원대라고?",
          [P("g1", MB, s0=1.0, s1=1.2)], C("wow", "r"), dialogue=True, speaker=3, emotion="toneup", say="벤츠 전기 에스유브이가 육천만원대라고?"),
        L("벤츠가 전기 GLB 사전계약을 열었는데, 가격이 6990만원.",
          [P("g2", MB, s0=1.0, s1=1.15), P("g1", MB, at="6990만원", s0=1.3, s1=1.5, fx=0.45, fy=0.55, punch=True)],
          C("dealer"), say="벤츠가 전기 지엘비 사전계약을 열었는데, 가격이 육천구백구십마넌.",
          em=["6990만원"], em_color="yellow", pop=("6990만원!", Y, "6990만원"), fx=[("drop_futuristic", "6990만원", 0.5)],
          info={"kind": "counter", "at": "가격이", "title": "전기 GLB 국내 가격", "items": [{"num": 6990, "suffix": "만원", "label": "부가세 포함", "at": "6990만원"}]}),
        L("실내엔 화면이 세 개, 조수석 앞까지 14인치 화면이 깔림.",
          [P("g3", MB, s0=1.0, s1=1.2), P("g3", MB, at="조수석", s0=1.3, s1=1.55, fx=0.75, fy=0.45, punch=True)],
          C("drv_heart", "r"), say="실내엔 화면이 세 개, 조수석 앞까지 십사인치 화면이 깔림.", em=["화면이 세 개"], fx=[("shutter_digital", "깔림", 0.4)]),
        L("보닛을 열면 앞 트렁크가 127리터, 뒤 트렁크는 540리터.",
          [P("g4", MB, s0=1.0, s1=1.2, fx=0.45, fy=0.4)], C("drv_surprise"), say="보닛을 열면 앞 트렁크가 백이십칠리터, 뒤 트렁크는 오백사십리터.",
          em=["앞 트렁크"],
          info={"kind": "bars", "at": "보닛을", "title": "트렁크 용량", "items": [
              {"label": "앞 트렁크", "num": 127, "suffix": "L", "at": "127리터"}, {"label": "뒤 트렁크", "num": 540, "suffix": "L", "at": "540리터"}]}),
        L("10분 충전하면 260킬로를 간다고 함.",
          [P("g2", MB, s0=1.2, s1=1.4, fx=0.55, fy=0.5)], C("ev", "r"), say="십분 충전하면 이백육십킬로를 간다고 함.", em=["10분 충전"], fx=[("correct_ding", "간다고", 0.5)]),
        L("GLB 특유의 강인한 SUV 디자인에 한층 진보한 전동화 기술을 결합했습니다.",
          [P("g1", MB, s0=1.2, s1=1.35, fx=0.4, fy=0.5)], C("sales"), dialogue=True, speaker=2, emotion="normal",
          say="지엘비 특유의 강인한 에스유브이 디자인에 한층 진보한 전동화 기술을 결합했습니다."),
        L("근데 1회 충전 631킬로는 유럽 기준 숫자임.",
          [P("g2", MB, s0=1.0, s1=1.15)], C("biz_think", "r"), say="근데 일회 충전 육백삼십일킬로는 유럽 기준 숫자임.",
          em=["유럽 기준"], em_color="yellow", pop=("유럽 기준?!", R, "유럽"), fx=[("wrong_gameshow_buzz", "유럽", 0.45)],
          info={"kind": "compare", "at": "근데", "title": "1회 충전 주행거리", "items": [
              {"label": "유럽 WLTP", "color": W, "at": "근데", "rows": [["주행거리", "631km", Y]]},
              {"label": "국내 인증", "color": R, "at": "유럽", "rows": [["주행거리", "미공개", W]]}]}),
        L("국내 인증 주행거리는 차를 넘겨줄 때 공개한다고 함.",
          [B("z01", "A Korean electric car charging station at a highway rest area in late autumn, cables hanging, overcast, no people, no cars")],
          C("biz_q"), em=["넘겨줄 때"]),
        L("계약은 지금 받는데, 국내에서 몇 킬로 가는지는 아직 모르는 셈.",
          [P("g4", MB, s0=1.2, s1=1.35, fx=0.45, fy=0.45)], C("komatta", "r"), em=["아직 모르는"]),
        L("인도는 11월 말부터 시작함.",
          [P("g1", MB, s0=1.0, s1=1.12)], C("drv_smile"), say="인도는 십일월 말부터 시작함."),
        L("님들은 주행거리 모르고 계약함, 기다림?", [P("g3", MB, s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "기다림")]),
    ]
    go(S, lines, "6천만원대 벤츠 전기 SUV", "근데 국내 주행거리는?", "전기 GLB 사전계약 6990만원, 11월 말 인도",
       "#전기 GLB 6990만원", "벤츠코리아 2026-10-28 사전계약 발표 (오토데일리 601580, 이코노믹리뷰 755232, 노컷뉴스 6598577, 뉴시스 NISX20261028_0003844233)",
       [("10/28 사전계약, GLB 250+ 일렉트릭, 6990만원(부가세 포함, 개소세 5%), 11월 말 인도", "오토데일리, 이코노믹리뷰, 노컷뉴스, 뉴시스"),
        ("MBUX 슈퍼스크린 10.25+14+14인치(동승석 14인치)", "이코노믹리뷰, 노컷뉴스, 뉴시스"),
        ("프렁크 127L, 트렁크 540L", "이코노믹리뷰, 노컷뉴스, 뉴시스"),
        ("85kWh, WLTP 최대 631km, 320kW 급속, 10분 260km(WLTP)", "오토데일리, 이코노믹리뷰, 노컷뉴스, 뉴시스"),
        ("국내 인증 주행거리, 세부 제원은 차량 인도 시점에 공개", "오토데일리"),
        ("관계자 'GLB 특유의 강인한 SUV 디자인에 한층 진보한 전동화 기술과 디지털 경험을 결합했다'", "뉴시스(대사는 앞부분만, 어미 다듬음)")],
       "벤츠 전기 GLB가 6990만원에 국내 사전계약을 시작했습니다.\n화면 3개, 앞 트렁크 127L, 10분 충전 260km입니다.\n631km는 유럽 기준이고 국내 인증 주행거리는 인도 때 공개됩니다.\n\n#벤츠 #GLB #전기차 #신차 #란빵",
       "님들은 주행거리 모르고 계약함, 기다림?",
       "전기차 충전구 커버, 차량용 트렁크 정리함, 전기차 충전 케이블 가방, 차량용 뒷좌석 태블릿 거치대, 차량용 열선 방석",
       "차 화면은 전부 벤츠코리아 제공 보도사진(지피코리아 게재본, 1280px). 독일 보도용 번호판 그대로. AI 배경은 차 없는 충전소 1장.",
       [P("g4", MB, s0=1.0, s1=1.1)])


# ───────────────────────── 9. 골프 R 복귀 ─────────────────────────
VW = "사진: 폭스바겐"


def EP_golfr():
    S = "golfr"
    cap(S, "r1", "vwgolfr333_1.jpg", cx=0.6, cy=0.65, nofaces=True)
    cap(S, "r2", "vwgolfr333_2.jpg", cx=0.45, cy=0.7, nofaces=True)
    cap(S, "r3", "vwgolfr333_3.jpg", cx=0.5, nofaces=True)
    cap(S, "r4", "vwgolfr333_4.jpg", cx=0.5, nofaces=True)
    cap(S, "r5", "vwgolfr333_5.jpg", cx=0.55, cy=0.6, nofaces=True)
    cap(S, "r6", "vwgolfr333_6.jpg", cx=0.55, cy=0.55, nofaces=True)
    lines = [
        L("해치백이 333마력이라고?",
          [P("r1", VW, s0=1.0, s1=1.2)], C("wow", "r"), dialogue=True, speaker=3, emotion="toneup", say="해치백이 삼백삼십삼마력이라고?"),
        L("폭스바겐이 골프 R을 12년 만에 국내에 다시 들여온다고 공개함.",
          [P("r2", VW, s0=1.0, s1=1.15), P("r5", VW, at="12년", s0=1.1, s1=1.3)],
          C("dealer"), say="폭스바겐이 골프 알을 십이년 만에 국내에 다시 들여온다고 공개함.", em=["12년 만에"], fx=[("hit_trailer_epic", "12년", 0.5)]),
        L("2리터 터보에 사륜구동, 최고출력은 333마력.",
          [P("r6", VW, s0=1.0, s1=1.2), P("r1", VW, at="333마력", s0=1.3, s1=1.55, fx=0.6, fy=0.65, punch=True)],
          C("drv_laugh", "r"), say="이리터 터보에 사륜구동, 최고출력은 삼백삼십삼마력.",
          em=["333마력"], em_color="yellow", pop=("333마력!", Y, "333마력"), shake="333마력", fx=[("boom_subby_kick", "333마력", 0.5)]),
        L("제로백은 4.6초, 배기구는 좌우 두 개씩 네 개.",
          [P("r5", VW, s0=1.0, s1=1.2, fx=0.55, fy=0.6)], C("drv_surprise"), say="제로백은 사점육초, 배기구는 좌우 두 개씩 네 개.",
          em=["4.6초"],
          info={"kind": "bars", "at": "제로백은", "title": "골프 R", "items": [
              {"label": "0→100km/h", "num": 4.6, "dec": 1, "suffix": "초", "at": "4.6초", "flash": "4.6초"}]}),
        L("같이 공개한 GTI 다크 모스는 100대 한정, 5425만원.",
          [P("r3", VW, s0=1.0, s1=1.2)], C("sales", "r"), say="같이 공개한 지티아이 다크 모스는 백대 한정, 오천사백이십오마넌.",
          em=["100대 한정"], fx=[("drop_futuristic", "100대", 0.5)]),
        L("가격은 아직 안 정해졌지만, 6천만원 중반대로 살 수 있게 노력하고 있습니다.",
          [P("r4", VW, s0=1.0, s1=1.2)], C("biz_smile"), dialogue=True, speaker=2, emotion="normal",
          say="가격은 아직 안 정해졌지만, 육천만원 중반대로 살 수 있게 노력하고 있습니다."),
        L("근데 이건 가격이 아니라 목표라는 게 함정.",
          [P("r2", VW, s0=1.2, s1=1.4, fx=0.45, fy=0.7)], C("biz_think", "r"), em=["목표라는"], em_color="yellow",
          pop=("목표?!", R, "목표라는"), fx=[("wrong_gameshow_buzz", "함정", 0.45)],
          info={"kind": "compare", "at": "근데", "title": "골프 R 국내 가격", "items": [
              {"label": "확정 가격", "color": R, "at": "근데", "rows": [["가격", "미정", W]]},
              {"label": "회사 목표", "color": W, "at": "목표라는", "rows": [["가격", "6천만원 중반", Y]]}]}),
        L("국내 인증도 아직이라, 출시는 내년 1분기 예상일 뿐임.",
          [B("y01", "A Korean vehicle certification test center garage with an empty dynamometer bay, fluorescent light, no people, no cars")],
          C("police"), say="국내 인증도 아직이라, 출시는 내년 일분기 예상일 뿐임.", em=["예상일 뿐"]),
        L("전시된 차도 독일 본사에서 들여온 차였음.",
          [P("r5", VW, s0=1.2, s1=1.35, fx=0.55, fy=0.6)], C("drv_think", "r"), em=["독일 본사에서"]),
        L("님들은 6천 중반이면 골프 R 삼?", [P("r1", VW, s0=1.0, s1=1.1)], C("biz_q"), say="님들은 육천 중반이면 골프 알 삼?",
          fx=[("pop_bubble", "삼")]),
    ]
    go(S, lines, "12년 만에 돌아온 골프 R", "근데 가격이 없다", "333마력 사륜 해치백, 내년 1분기 출시 예상",
       "#골프R 12년 만에 복귀", "폭스바겐코리아 골프 R 카페 오픈하우스 2026-10-27~28 (소비자가만드는신문 767023, 직썰 151111, 현대경제신문 264854)",
       [("골프 R 국내 출시 2015년 7세대 이후 약 12년 만, 2027년 예정", "소비자가만드는신문, 현대경제신문"),
        ("2.0 터보 + 7단 DSG, 333마력, 4MOTION", "소비자가만드는신문, 직썰, 현대경제신문"),
        ("0→100km/h 4.6초, 배기구 좌우 2개씩 4개", "직썰, 현대경제신문, 뉴스투데이"),
        ("GTI 다크 모스 245마력, 100대 한정, 5425만원", "OSEN, 뉴스투데이, 시사온"),
        ("폭스바겐코리아 '내년 1분기 출시 예상, 국내 인증 거쳐 확정', '가격은 아직 정해지지 않았지만 6000만원 중반대에 구매할 수 있도록 노력하고 있다'", "직썰(대사는 어미만 다듬음)"),
        ("전시차는 독일 본사에서 들여온 차, 국내 가격, 최종 사양 미공개", "현대경제신문, 소비자가만드는신문"),
        ("사진은 2024 글로벌 공개 차량(국내 전시차는 흰색)", "폭스바겐 글로벌 뉴스룸")],
       "폭스바겐 골프 R이 12년 만에 국내 복귀를 예고했습니다.\n333마력 사륜구동, 제로백 4.6초입니다.\n가격은 미정이고 6천만원 중반대가 목표, 출시는 내년 1분기 예상입니다.\n\n#골프R #폭스바겐 #핫해치 #신차 #란빵",
       "님들은 6천 중반이면 골프 R 삼?",
       "차량용 버킷시트 쿠션, 스티어링 휠 커버, 휴대용 타이어 공기주입기, 자동차 블랙박스 2채널, 겨울용 와이퍼",
       "차 화면은 폭스바겐 글로벌 뉴스룸 공식 사진(2024 공개 차량). 최고속도 270km/h, 슈퍼카 타이어 건은 1곳 보도라 뺌. AI 배경은 차 없는 인증 시험장 1장.",
       [P("r6", VW, s0=1.0, s1=1.1)])


# ───────────────────────── 10. 카이엔 쿠페 일렉트릭 ─────────────────────────
PO = "사진: 포르쉐"


def EP_cayennecp():
    S = "cayennecp"
    cap(S, "c1", "cayennecoupe_1.jpg", cx=0.5, cy=0.6, nofaces=True)
    cap(S, "c2", "cayennecoupe_2.jpg", cx=0.5, cy=0.6, nofaces=True)
    cap(S, "c3", "cayennecoupe_3.jpg", cx=0.5, cy=0.5, nofaces=True)
    cap(S, "c4", "cayennecoupe_4.jpg", cx=0.5, cy=0.6, nofaces=True)
    cap(S, "c5", "cayennecoupe_5.jpg", cx=0.5, cy=0.6, nofaces=True)
    lines = [
        L("이게 제로백 2.5초짜리 SUV라고?",
          [P("c4", PO, s0=1.0, s1=1.2)], C("wow", "r"), dialogue=True, speaker=3, emotion="toneup", say="이게 제로백 이점오초짜리 에스유브이라고?"),
        L("포르쉐가 카이엔 쿠페 일렉트릭을 국내에 내놨는데, 터보는 순간 최고 1156마력.",
          [P("c1", PO, s0=1.0, s1=1.15), P("c3", PO, at="1156마력", s0=1.2, s1=1.45, fx=0.5, fy=0.5, punch=True)],
          C("drv_laugh"), say="포르쉐가 카이엔 쿠페 일렉트릭을 국내에 내놨는데, 터보는 순간 최고 천백오십육마력.",
          em=["1156마력"], em_color="yellow", pop=("1156마력!", Y, "1156마력"), shake="1156마력", fx=[("boom_subby_kick", "1156마력", 0.5)]),
        L("지붕만 24밀리 낮췄고, 길이랑 폭은 SUV랑 똑같음.",
          [P("c2", PO, s0=1.0, s1=1.2)], C("drv_think", "r"), say="지붕만 이십사밀리 낮췄고, 길이랑 폭은 에스유브이랑 똑같음.", em=["지붕만"]),
        L("가격은 기본형 1억4830만원부터, 터보는 1억9240만원.",
          [P("c5", PO, s0=1.0, s1=1.2)], C("bill_shock"), say="가격은 기본형 일억사천팔백삼십마넌부터, 터보는 일억구천이백사십마넌.",
          em=["1억9240만원"], fx=[("drop_futuristic", "기본형", 0.5)],
          info={"kind": "compare", "at": "가격은", "title": "국내 가격", "items": [
              {"label": "기본형", "color": W, "at": "가격은", "rows": [["시작가", "1억4830만원", W]]},
              {"label": "터보", "color": R, "at": "터보는", "rows": [["시작가", "1억9240만원", Y]]}]}),
        L("같은 SUV형보다 기본형 기준 600만원 더 비쌈.",
          [P("c1", PO, s0=1.2, s1=1.4, fx=0.5, fy=0.6)], C("ohagya", "r"), say="같은 에스유브이형보다 기본형 기준 육백마넌 더 비쌈.", em=["600만원 더"]),
        L("국내 인증 주행거리는 기본형이 530킬로.",
          [B("n01", "A premium electric car fast charging hub in Seoul at dusk, empty charging bays with glowing chargers, no people, no cars")],
          C("ev"), say="국내 인증 주행거리는 기본형이 오백삼십킬로.", em=["530킬로"], fx=[("correct_ding", "530킬로", 0.45)]),
        L("카이엔에 대한 강력한 팬덤을 기반으로, 전동화 성장을 이끄는 핵심 기수가 될 겁니다.",
          [P("c4", PO, s0=1.2, s1=1.35, fx=0.5, fy=0.6)], C("biz_smile", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("근데 기본형부터 8천만원을 훌쩍 넘어서, 법인 명의로 사면 연두색 번호판을 달아야 함.",
          [B("n02", "A plain light green blank vehicle license plate lying on a dark desk, close-up, no text, no people")],
          C("biz_shock"), say="근데 기본형부터 팔천만원을 훌쩍 넘어서, 법인 명의로 사면 연두색 번호판을 달아야 함.",
          em=["연두색 번호판"], em_color="yellow", pop=("연두색!", R, "연두색"), fx=[("hit_trailer_epic", "연두색", 0.5)]),
        L("그래서 고가 수입차는 법인 구매를 꺼린다는 분석까지 나옴.",
          [P("c5", PO, s0=1.2, s1=1.35, fx=0.5, fy=0.6)], C("biz_think", "r"), em=["법인 구매를"]),
        L("님들은 이 차 법인으로 사서 연두색 달고 탐?", [P("c3", PO, s0=1.0, s1=1.1)], C("biz_q", "r"), fx=[("pop_bubble", "탐")]),
    ]
    go(S, lines, "제로백 2.5초 SUV 쿠페", "근데 번호판이 연두색?", "카이엔 쿠페 일렉트릭 국내 출시, 1억4830만원부터",
       "#1156마력 카이엔 쿠페", "포르쉐코리아 2026-10-15 국내 출시 (위키트리 1166387, 동아일보 20261015/134849546, 지피코리아 147628)",
       [("10/15 카이엔 쿠페 일렉트릭 국내 출시, 국내 4번째 순수전기차", "동아일보, 위키트리"),
        ("가격 1억4830만 / S 1억6860만 / 터보 1억9240만원", "위키트리, 동아일보, 지피코리아"),
        ("SUV형 대비 기본형 600만원 비쌈(SUV 1억4230만원)", "지피코리아, 한국경제"),
        ("터보 857마력, 오버부스트 1156마력, 0→100km/h 2.5초", "위키트리, 동아일보, 지피코리아"),
        ("전장, 전폭 SUV와 동일, 전고 24mm 낮음", "위키트리, 동아일보, 한국경제"),
        ("113kWh, 국내 인증 상온 복합 기본형 530km", "동아일보, 신아일보"),
        ("부세 대표 '카이엔에 대한 강력한 팬덤을 기반으로 이번 신차가 포르쉐코리아의 전동화 성장을 이끄는 핵심 기수가 될 것'", "데일리카(네이버 검색 미리보기 2건, 본문 403), 대사는 어미만 다듬음"),
        ("법인 업무용 승용차 취득가 8000만원 이상 연두색 번호판(2024-01-01 시행), 고가 수입차 법인 구매 기피 관측", "국토부 번호판 고시 개정(원문 미확인), 뉴스프리존 2026-10-26"),
        ("인도 터보 → S → 기본형 순", "위키트리, 동아일보"),
        ("저온 주행거리 416km 는 1곳 보도라 뺌", "제작 메모")],
       "포르쉐 카이엔 쿠페 일렉트릭이 국내에 나왔습니다.\n터보는 순간 최고 1156마력, 제로백 2.5초, 가격은 1억4830만원부터입니다.\n법인 명의로 사면 연두색 번호판 대상입니다.\n\n#포르쉐 #카이엔 #전기차 #신차 #란빵",
       "님들은 이 차 법인으로 사서 연두색 달고 탐?",
       "차량용 열선 방석, 전기차 충전구 커버, 차량용 성에제거 스크래퍼, 휴대용 타이어 공기주입기, 차량용 무선충전 거치대",
       "차 화면은 포르쉐 뉴스룸 공식 보도사진(독일 번호판 그대로). AI 배경은 차 없는 충전소, 빈 번호판 2장.",
       [P("c4", PO, s0=1.0, s1=1.1)])

EPS = [EP_selffall, EP_sonatadisc, EP_trench55, EP_benzfire, EP_bunsim91, EP_air5000, EP_fsdtalok,
       EP_glbev, EP_golfr, EP_cayennecp]

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in EPS:
        if not want or f.__name__[3:] in want:
            f()
