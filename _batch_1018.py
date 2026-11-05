#!/usr/bin/env python3
"""란빵 2026-10-18 — 사용자 지정 블로그 2건 → 2편. v2(Remotion), 실사 = 제조사 공식 사진만.
- byddahan: BYD 다한 EV 출시(blog.naver.com/mobility_trend/224441590610). 신차 공개형 구조(prd §4-6) 응용, 영상 대신 공식 사진.
  수치 교차확인 CnEVPost 10/13, electrive 10/16. 사진 = BYD 보도사진(CnEVPost 게재본).
- tasmandc: 기아 타스만 판매 반토막·10월 할인(blog.naver.com/ruddns8213/224430078193).
  판매·점유율 = 파이낸셜뉴스 10/5(2건) 확인. 할인 총액은 블로그 720만원 vs 뉴스와 760만원으로 달라 '700만원 넘게'로만 씀.
  사진 = kia.com 타스만 모델 페이지.
대본 중간 대화체 1줄 이상 필수.
"""
import json, os, re
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")
Y, W, R = "#FBFF56", "#fff", "#FF3B30"


def crop(src, out, cx=0.5, cy=0.5):
    """원본 전체 높이로 9:8 박스를 cx 중심에서 잘라 1080x960."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    cw = min(w, int(h * 9 / 8))
    ch = int(cw * 8 / 9)
    x = min(max(int(w * cx - cw / 2), 0), w - cw)
    y = min(max(int(h * cy - ch / 2), 0), h - ch)
    im.crop((x, y, x + cw, y + ch)).resize((1080, 960), Image.LANCZOS).save(out, quality=92)


def P(name, cr, at=None, s0=1.0, s1=1.1, fx=0.5, fy=0.5, punch=False):
    d = {"img": f"real/{name}.jpg", "s0": s0, "s1": s1, "fx": fx, "fy": fy, "credit": cr}
    if at:
        d["at"] = at
    if punch:
        d["punch"] = True
    return d


def L(text, sh, **k):
    d = {"text": text, "sh": sh}
    d.update(k)
    return d


def build(slug, lines, t1, t2, bar, title, source, proof, desc, comment, tags, extra, outro, cr):
    assert any(l.get("dialogue") for l in lines)
    for l in lines:
        assert not any(c.isdigit() for c in l.get("say", l["text"])), l["text"]
        if l.get("dialogue"):
            assert l.get("speaker", 1) != 1 and not l.get("em")
        for w in l.get("em", []):
            assert w in l["text"], w
    assert len(title) <= 12 and not RISKY.search(title + t1 + t2), title
    wk = os.path.join(ROOT, "work", slug)
    SK = ("sh", "fx", "pop", "shake", "info")
    sc_lines = [{**{k: v for k, v in l.items() if k not in SK}, "img": 1} for l in lines]
    sc_lines.append({"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": 1})
    sc = {"slug": slug, "type": "란빵 자동차, 신차 뉴스", "source": source,
          "title_line1": t1, "title_line2": t2, "hook": bar, "channel": "란빵",
          "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
          "style": {"sub_box": True, "bar": bar, "bar_count": None, "watermark": ""}, "lines": sc_lines}
    json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)
    texts = [l["text"].rstrip(".") for l in sc_lines]
    shot_lines = []
    for i, l in enumerate(lines):
        d = {"shots": l["sh"]}
        if l.get("fx"):
            d["sfx"] = [list(x) for x in l["fx"]]
        for k in ("pop", "shake", "info"):
            if l.get(k):
                d[k] = list(l[k]) if k == "pop" else l[k]
        ws = [s.get("at") for s in d["shots"]] + [x[1] for x in d.get("sfx", [])] + [d.get("shake")]
        ws += [d["pop"][2]] if "pop" in d else []
        if "info" in d:
            ws += [d["info"].get("at")] + [it.get("at") for it in d["info"]["items"]]
        for w in ws:
            if w and w.startswith("+1:"):
                w = w[3:]
            assert not w or w in texts[i], (i, w, texts[i])
        shot_lines.append(d)
    shot_lines.append({"shots": [{"img": f"real/{outro}.jpg", "s0": 1.0, "s1": 1.1, "credit": cr}],
                       "sfx": [["pop_long", "구독!"]], "pop": ["구독!", "#FFE629", "구독!"]})
    json.dump({"bgmVol": 0.09, "bgm": "bgm/sneaky-123.mp3", "lines": shot_lines},
              open(os.path.join(wk, "v2", "shots.json"), "w"), ensure_ascii=False, indent=1)
    rows = "\n".join(f"| {a} | {b} |" for a, b in proof)
    open(os.path.join(wk, "upload.md"), "w").write(
        f"# {slug}: 업로드 메타 (란빵)\n\n## 제목\n\n{title}\n\n## 설명\n\n{desc}\n\n"
        f"## 고정 댓글\n\n{comment}\n\n## 쇼핑태그\n\n{tags}\n\n"
        f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n{extra}\n")
    lk = os.path.expanduser(f"~/Desktop/kim/ssul/work/{slug}")
    if not os.path.lexists(lk):
        os.symlink(wk, lk)
    print("ok", slug, len(sc_lines), "lines")


# ───────────── byddahan ─────────────
S = "byddahan"
CB = "사진: BYD"
rd = os.path.join(ROOT, "work", S, "v2", "real")
for n, f, cx in [("b1", "2026101313074624", 0.45), ("b2", "2026101313075075", 0.5), ("b3", "2026101313075294", 0.45),
                 ("b4", "2026101313075572", 0.55), ("b5", "2026101313075851", 0.55), ("b6", "2026101313080241", 0.38),
                 ("b7", "2026101313080914", 0.5), ("outro", "2026101313075075", 0.5)]:
    crop(f"{rd}/src/{f}.jpg", f"{rd}/{n}.jpg", cx)

lines = [
    L("와, 이게 4700만원이라고?", [P("b2", CB, s0=1.05, s1=1.15), P("b1", CB, "4700만원이라고", s0=1.1, s1=1.2, punch=True)],
      say="와, 이게 사천칠백마넌이라고?", dialogue=True, speaker=3, emotion="toneup"),
    L("BYD가 그랜저보다 20센티 넘게 긴 전기 세단을 냈는데, 중국 시작 가격이 4700만원임.",
      [P("b4", CB), P("b1", CB, "시작", s0=1.0, s1=1.12, fx=0.45, fy=0.55, punch=True)],
      say="비와이디가 그랜저보다 이십 센티 넘게 긴 전기 세단을 냈는데, 중국 시작 가격이 사천칠백마넌임.",
      em=["4700만원"], em_color="yellow", fx=[("hit_trailer_epic", "4700만원임", 0.55)], pop=("4700만원?!", Y, "4700만원임")),
    L("배터리 10%에서 97%까지 충전하는 데 딱 9분 걸림.", [P("b3", CB, s0=1.0, s1=1.1), P("b3", CB, "9분", s0=1.6, s1=1.75, fx=0.3, fy=0.55, punch=True)],
      say="배터리 십 퍼센트에서 구십칠 퍼센트까지 충전하는 데 딱 구 분 걸림.", em=["9분"], em_color="yellow",
      fx=[("drop_futuristic", "9분", 0.5)], pop=("9분!!", Y, "9분")),
    L("한 번 충전에 1008km 간다는데, 이건 중국 기준이고 유럽 기준으론 816km임.",
      [P("b5", CB), P("b6", CB, "유럽", s0=1.12, s1=1.0)],
      say="한 번 충전에 천팔 키로 간다는데, 이건 중국 기준이고 유럽 기준으론 팔백십육 키로임.", em=["816km"],
      info={"kind": "compare", "at": "1008km", "title": "1회 충전 주행거리", "items": [
          {"label": "중국 기준", "color": W, "rows": [["CLTC", "1008km", Y]]},
          {"label": "유럽 기준", "color": Y, "at": "유럽", "rows": [["WLTP", "816km", R]]}]}),
    L("듀얼모터는 764마력에 제로백 3.3초라 포르쉐급 소리 나옴.", [P("b2", CB, s0=1.15, s1=1.0, fy=0.6), P("b4", CB, "3.3초", s0=1.5, s1=1.65, fx=0.35, fy=0.6, punch=True)],
      say="듀얼모터는 칠백육십사 마력에 제로백 삼 점 삼 초라 포르쉐급 소리 나옴.", em=["3.3초"], em_color="yellow",
      fx=[("boom_zoom_impact", "3.3초라", 0.5)], shake="3.3초라"),
    L("덩치가 5미터 넘는데 뒷바퀴까지 꺾여서 회전반경은 4.95미터임.", [P("b4", CB, s0=1.0, s1=1.12, fx=0.6), P("b5", CB, "뒷바퀴까지", s0=1.5, s1=1.65, fx=0.6, fy=0.65)],
      say="덩치가 오 미터 넘는데 뒷바퀴까지 꺾여서 회전 반경은 사 점 구오 미터임.", em=["뒷바퀴까지"]),
    L("실내는 40인치 헤드업 디스플레이에 스피커만 31개.", [P("b7", CB), P("b7", CB, "스피커만", s0=1.5, s1=1.65, fx=0.5, fy=0.4)],
      say="실내는 사십 인치 헤드업 디스플레이에 스피커만 삼십일 개.", em=["31개"], fx=[("notify_message_pop", "31개", 0.45)]),
    L("이 가격에 들어오면 국산 대형 세단들 긴장해야죠.", [P("b6", CB, s0=1.05, s1=1.15)],
      say="이 가격에 들어오면 국산 대형 세단들 긴장해야죠.", dialogue=True, speaker=2, emotion="toneup"),
    L("근데 국내 출시는 아직 미정이고, 들어오면 관세랑 인증 비용이 더 붙음.", [P("b1", CB, s0=1.12, s1=1.0), P("b2", CB, "관세랑", s0=1.0, s1=1.1)],
      say="근데 국내 출시는 아직 미정이고, 들어오면 관세랑 인증 비용이 더 붙음.", em=["미정"],
      fx=[("wrong_gameshow_buzz", "미정이고", 0.45)]),
    L("님들은 BYD 대형 세단 4700만원이면 살 거임?", [P("b5", CB, s0=1.0, s1=1.12)],
      say="님들은 비와이디 대형 세단 사천칠백마넌이면 살 거임?", fx=[("pop_bubble", "거임")]),
]
build(S, lines, "그랜저보다 큰 중국 전기차", "결국 9분 충전까지", "BYD 대형 전기 세단 '다한 EV' 출시",
      "#그랜저보다 큰 BYD", "모빌리티트렌드 블로그 + CnEVPost 2026-10-13 BYD 다한 EV 출시",
      [("BYD 다한 EV 10/13 중국 출시, 시작가 23만5900위안(약 4700만원)", "CnEVPost 2026-10-13, technode 2026-10-14"),
       ("전장 5256mm, 그랜저보다 20cm 이상 김", "모빌리티트렌드 블로그(BYD 제원), 그랜저 전장 5035mm"),
       ("102.3kWh 2세대 블레이드 배터리, 10%→97% 9분", "electrive 2026-10-16, 블로그"),
       ("주행거리 CLTC 1008km / WLTP 816km(후륜 싱글모터)", "블로그, CnEVPost"),
       ("듀얼모터 764마력, 제로백 3.3초", "블로그, CnEVPost"),
       ("후륜 조향, 최소 회전반경 4.95m", "블로그"),
       ("40인치 AR-HUD, 드비알레 31개 스피커", "블로그"),
       ("'국산 세단 중심 구도에 긴장감' 업계 관계자 발언", "블로그(의역)"),
       ("국내 출시 미정, 관세와 인증 비용 추가", "블로그")],
      "BYD가 그랜저보다 큰 대형 전기 세단 '다한 EV'를 중국에서 출시, 시작가 약 4700만원.\n"
      "9분 만에 10%에서 97% 충전, 듀얼모터 764마력 제로백 3.3초.\n"
      "주행거리 1008km는 중국 CLTC 기준(유럽 WLTP 816km), 국내 출시는 미정.\n사진: BYD\n"
      "#shorts #BYD #다한EV #전기차 #중국차",
      "님들은 BYD 대형 세단 4700만원이면 살 거임?",
      "전기차 충전 케이블, 차량용 휴대폰 거치대, 자동차 블랙박스 2채널, 차량용 무선충전기, 차량용 공기청정기",
      "원출처: https://blog.naver.com/mobility_trend/224441590610\n사진: BYD 보도사진(CnEVPost 게재본 https://cnevpost.com/2026/10/13/byd-launches-da-han-ev/)",
      "outro", CB)

# ───────────── tasmandc ─────────────
S = "tasmandc"
CK = "사진: 기아"
rd = os.path.join(ROOT, "work", S, "v2", "real")
for n, f, cx in [("t1", "tasman_exterior_front_pc", 0.42), ("t2", "tasman_exterior_best_selection_pc", 0.42),
                 ("t3", "tasman_exterior_best_selection_head_lamp_pc", 0.4), ("t4", "tasman_exterior_side_pc", 0.55),
                 ("t5", "tasman_exterior_best_selection_rear_lamp_pc", 0.55), ("t6", "tasman_x-pro_main_pc", 0.5),
                 ("t7", "tasman_x-pro_emblem_pc", 0.6), ("t8", "tasman_x-pro_specialization_offroad_pc", 0.45),
                 ("t9", "tasman_x-pro_specialization_rock-mode_pc", 0.6), ("t10", "tasman_x-pro_specialization_x-trek_pc", 0.45),
                 ("t11", "the_kia_tasman_feature_bg_pc", 0.4), ("t12", "tasman_exterior_rear_pc", 0.45),
                 ("t13", "tasman_interior_dash-board_pc", 0.5), ("outro", "tasman_x-pro_main_pc", 0.5)]:
    crop(f"{rd}/src/{f}.jpg", f"{rd}/{n}.jpg", cx)

lines = [
    L("지금 타스만 사면 600 빠진다던데?", [P("t11", CK, s0=1.05, s1=1.15), P("t1", CK, "600", s0=1.1, s1=1.2, punch=True)],
      say="지금 타스만 사면 육백 빠진다던데?", dialogue=True, speaker=3, emotion="toneup"),
    L("기아 픽업트럭 타스만이 9월에 404대 팔렸는데, 작년보다 반토막 났음.",
      [P("t6", CK), P("t7", CK, "반토막", s0=1.0, s1=1.12)],
      say="기아 픽업트럭 타스만이 구월에 사백사 대 팔렸는데, 작년보다 반토막 났음.", em=["반토막"], em_color="yellow",
      fx=[("wrong_gameshow_buzz", "반토막", 0.45)], pop=("반토막!!", R, "반토막"),
      info={"kind": "bars", "span": 1, "title": "타스만 9월 국내 판매", "items": [
          {"label": "작년 9월", "value": 1.0, "num": 777, "suffix": "대", "color": W},
          {"label": "올해 9월", "value": 0.52, "num": 404, "suffix": "대", "color": Y, "at": "404대", "flash": "반토막"}]}),
    L("출시 초엔 한 달에 1200대 넘게 팔리던 차임.", [P("t8", CK), P("t10", CK, "1200대", s0=1.1, s1=1.0)],
      say="출시 초엔 한 달에 천이백 대 넘게 팔리던 차임.", em=["1200대"]),
    L("국산 픽업 점유율도 37%에서 17.6%로 떨어졌고, 나머지는 거의 KGM 무쏘가 가져감.",
      [P("t9", CK), P("t4", CK, "무쏘가", s0=1.0, s1=1.12)],
      say="국산 픽업 점유율도 삼십칠 퍼센트에서 십칠 점 육 퍼센트로 떨어졌고, 나머지는 거의 케이지엠 무쏘가 가져감.",
      em=["17.6%"],
      info={"kind": "bars", "span": 1, "title": "국산 픽업 내수 점유율(타스만)", "items": [
          {"label": "작년", "value": 1.0, "num": 37.0, "dec": 1, "suffix": "%", "color": W},
          {"label": "올해 1~9월", "value": 0.48, "num": 17.6, "dec": 1, "suffix": "%", "color": Y, "at": "17.6%로", "flash": "떨어졌고"}]}),
    L("그래서 기아가 10월에 7월 생산분 재고를 600만원 깎아주기로 함.",
      [P("t2", CK), P("t3", CK, "600만원", s0=1.0, s1=1.15, punch=True)],
      say="그래서 기아가 시월에 칠월 생산분 재고를 육백마넌 깎아주기로 함.", em=["600만원"], em_color="yellow",
      fx=[("cash_register_fake", "600만원", 0.5)],
      info={"kind": "counter", "at": "600만원", "title": "10월 재고 할인(7월 생산분)",
            "items": [{"num": 600, "suffix": "만원", "label": "즉시 할인", "at": "600만원"}]}),
    L("트레이드인 같은 조건까지 다 채우면 할인이 700만원 넘게 붙음.", [P("t12", CK), P("t5", CK, "700만원", s0=1.0, s1=1.12)],
      say="트레이드인 같은 조건까지 다 채우면 할인이 칠백마넌 넘게 붙음.", em=["700만원"]),
    L("그러면 3500만원짜리 기본 트림이 2천만원대 후반까지 내려옴.", [P("t1", CK, s0=1.12, s1=1.0), P("t11", CK, "2천만원대", s0=1.0, s1=1.12)],
      say="그러면 삼천오백마넌짜리 기본 트림이 이천마넌대 후반까지 내려옴.", em=["2천만원대"], em_color="yellow",
      fx=[("drop_futuristic", "2천만원대", 0.5)],
      info={"kind": "compare", "at": "3500만원짜리", "title": "다이내믹 2WD", "items": [
          {"label": "정가", "color": W, "rows": [["가격", "3500만원"]]},
          {"label": "조건 다 채우면", "color": Y, "at": "2천만원대", "rows": [["가격", "2천만원대 후반", Y]]}]}),
    L("오픈베드는 빠지고요, 재고 끝나면 바로 종료예요.", [P("t13", CK, s0=1.05, s1=1.15)],
      say="오픈베드는 빠지고요, 재고 끝나면 바로 종료예요.", dialogue=True, speaker=2, emotion="normal"),
    L("님들은 281마력 픽업 2천만원대 후반이면 삼?", [P("t6", CK, s0=1.0, s1=1.12)],
      say="님들은 이백팔십일 마력 픽업 이천마넌대 후반이면 삼?", fx=[("pop_bubble", "삼")]),
]
build(S, lines, "판매 반토막 난 국산 픽업", "결국 600만원 깎아준다", "기아 타스만 10월 재고 할인",
      "#타스만 600 할인", "블로그 차쟁이 개발자 + 파이낸셜뉴스 2026-10-05",
      [("타스만 9월 국내 404대, 전년 동월 777대 대비 48.0% 감소", "파이낸셜뉴스 2026-10-05(2건)"),
       ("2025년 4~7월 국내 월 1200~1300대", "파이낸셜뉴스 2026-10-05"),
       ("국산 픽업 내수 점유율 37.0% → 17.6%(1~9월), 무쏘+무쏘EV 82.4%", "파이낸셜뉴스 2026-10-05(2건)"),
       ("10월 2026년 7월 생산분 600만원 할인, 오픈베드 제외, 재고 소진 시 종료", "블로그, 뉴스와 2026-10-03"),
       ("조건 합산 최대 할인 700만원대(블로그 720만원, 뉴스와 760만원)", "블로그, 뉴스와(합산 방식 차이)"),
       ("다이내믹 2WD 3500만원 → 2천만원대 후반", "블로그(2780만원), 뉴스와(2740만원)"),
       ("가솔린 2.5 터보 281마력", "블로그(기아 제원)")],
      "판매가 반토막 난 기아 타스만, 10월 7월 생산분 재고 600만원 할인.\n"
      "조건을 다 채우면 할인 700만원대, 다이내믹 2WD 실구매가 2천만원대 후반.\n"
      "오픈베드 제외, 재고 소진 시 종료. 계약 전 생산월과 트림 확인 필수.\n사진: 기아\n"
      "#shorts #기아 #타스만 #픽업트럭 #자동차할인",
      "님들은 281마력 픽업 2천만원대 후반이면 삼?",
      "픽업트럭 베드매트, 차량용 휴대폰 거치대, 자동차 블랙박스 2채널, 차량용 무선충전기, 차량용 루프박스",
      "원출처: https://blog.naver.com/ruddns8213/224430078193\n"
      "교차확인: https://www.fnnews.com/news/202610040903427503 , https://www.fnnews.com/news/202610051901155106 , "
      "https://www.news-wa.com/amp/automobiles/new-car/2026/10/03/20261003500044\n사진: kia.com 타스만 모델 페이지",
      "outro", CK)
