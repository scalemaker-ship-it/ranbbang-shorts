#!/usr/bin/env python3
"""란빵 2026-10-21 (2/2): 셀토스 4 + 테슬라 3 + 자동차 관련법 6. 헬퍼는 _batch_1020.py, IR 추가분은 _batch_1021.py.
- 셀토스 차 화면 = 현대차그룹 뉴스룸 디 올 뉴 셀토스 보도사진(work/_photos/seltos/, map.txt 에 원본 URL), 출처 "사진: 기아".
  캐나다 리콜(1세대)과 중국형은 국내 신형 사진을 붙이지 않고 AI 배경만(오해 방지).
- 테슬라, 법 편 = GPT 리얼 배경(로고, 글자 없음) + いらすとや. 실존 인물 얼굴 없음.
- 수치 교차확인: 조사 에이전트 3건(research_seltos/tesla/law.md, 근거표에 출처). 법 조문은 국가법령정보센터 원문.
"""
import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1021 import B, C, L, build, Y, W, R   # noqa: E402
from _batch_1020 import P   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
KIA = "사진: 기아"


def real(slug, picks):
    """picks = {이름: (원본 파일, 가로 중심 0~1)} → work/<slug>/v2/real/<이름>.jpg 1080x960(9:8)."""
    d = os.path.join(ROOT, "work", slug, "v2", "real")
    os.makedirs(d, exist_ok=True)
    for n, (src, cx) in picks.items():
        im = Image.open(os.path.join(ROOT, "work", "_photos", "seltos", src + ".jpg")).convert("RGB")
        w, h = im.size
        cw = int(h * 9 / 8)
        x = min(max(int(w * cx - cw / 2), 0), w - cw)
        im.crop((x, 0, x + cw, h)).resize((1080, 960), Image.LANCZOS).save(os.path.join(d, n + ".jpg"), quality=92)


SEL = {"s_front": ("front", 0.68), "s_side": ("side", 0.62), "s_rear": ("rear", 0.38), "s_hall": ("hall", 0.42),
       "s_dash": ("dash", 0.4), "s_seat": ("seat", 0.5), "s_xline": ("xline", 0.4), "s_hev": ("hev", 0.43)}


# ───────────────────────── 셀토스 ─────────────────────────

def EP_seltosup():
    S = "seltosup"
    real(S, SEL)
    lines = [
        L("출시 1년도 안 됐는데 100 가까이 올려버렸네요.",
          [P("s_front", KIA, s0=1.05, s1=1.2, punch=True)], C("biz_angry", "r"), dialogue=True, speaker=3, emotion="toneup",
          say="출시 일년도 안 됐는데 백 가까이 올려버렸네요."),
        L("기아가 1월에 낸 신형 셀토스를 8개월 만에 2027년형으로 바꿔서 내놓음.",
          [P("s_hall", KIA), P("s_side", KIA, at="2027년형", s0=1.0, s1=1.12)], C("dealer"),
          say="기아가 일월에 낸 신형 셀토스를 팔개월 만에 이천이십칠년형으로 바꿔서 내놓음.", em=["8개월 만에"], em_color="yellow"),
        L("가솔린 기본 트림이 2477만원에서 2575만원이 됨.",
          [P("s_side", KIA, s0=1.2, s1=1.35, fx=0.55, fy=0.5)], C("bill_shock"),
          say="가솔린 기본 트림이 이천사백칠십칠마넌에서 이천오백칠십오마넌이 됨.", em=["2575만원"], em_color="yellow",
          fx=[("drop_futuristic", "2575만원이", 0.5)],
          info={"kind": "bars", "title": "셀토스 트렌디 가솔린", "items": [
              {"label": "1월 출시", "value": 0.96, "num": 2477, "suffix": "만원", "color": W, "at": "2477만원에서"},
              {"label": "2027년형", "value": 1.0, "num": 2575, "suffix": "만원", "color": Y, "at": "2575만원이"}]}),
        L("체감으로는 98만원이 오른 셈.",
          [P("s_rear", KIA, s0=1.0, s1=1.15, punch=True)], C("ohagya"), say="체감으로는 구십팔마넌이 오른 셈.",
          pop=("+98만원", R, "98만원이"), shake="98만원이", fx=[("hit_trailer_epic", "98만원이", 0.5)]),
        L("그중 60만원은 연식변경 인상, 38만원은 개소세 인하가 끝난 몫임.",
          [P("s_dash", KIA, s0=1.0, s1=1.12)], C("biz_think"),
          say="그중 육십마넌은 연식변경 인상, 삼십팔마넌은 개소세 인하가 끝난 몫임.", em=["60만원"],
          info={"kind": "compare", "at": "60만원은", "title": "98만원 내역", "items": [
              {"label": "연식변경 인상", "color": Y, "at": "60만원은", "rows": [["", "60만원", Y]]},
              {"label": "개소세 인하 종료", "color": W, "at": "38만원은", "rows": [["", "38만원", W]]}]}),
        L("근데 셀토스는 1월 풀체인지 때도 이미 211만원을 올렸었음.",
          [P("s_xline", KIA, s0=1.0, s1=1.15)], C("drv_shock"),
          say="근데 셀토스는 일월 풀체인지 때도 이미 이백십일마넌을 올렸었음.", em=["211만원"], em_color="yellow",
          pop=("또?!", R, "이미"), fx=[("scratch_vinyl", "이미", 0.45)]),
        L("그래서 아반떼랑 시작가 차이가 415만원에서 177만원까지 좁혀짐.",
          [P("s_hall", KIA, s0=1.3, s1=1.45, fx=0.45, fy=0.55)], C("graph_down", "r"),
          say="그래서 아반떼랑 시작가 차이가 사백십오마넌에서 백칠십칠마넌까지 좁혀짐.", em=["177만원"],
          info={"kind": "bars", "title": "아반떼와 시작가 차이", "items": [
              {"label": "1월", "value": 1.0, "num": 415, "suffix": "만원", "color": W, "at": "415만원에서"},
              {"label": "지금", "value": 0.43, "num": 177, "suffix": "만원", "color": R, "at": "177만원까지", "flash": "177만원까지"}]}),
        L("하이브리드는 연말에 세제혜택 끝나면 내년에 또 오를 거란 전망까지 나옴.",
          [P("s_hev", KIA, s0=1.0, s1=1.15)], C("shinpai"), em=["또 오를"], fx=[("drum_rimshot", "전망까지", 0.4)]),
        L("님들은 2575만원 셀토스, 아직 가성비라고 봄?", [P("s_front", KIA, s0=1.0, s1=1.12)], C("biz_q"),
          say="님들은 이천오백칠십오마넌 셀토스, 아직 가성비라고 봄?", fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "8개월 만에 또 올린", "신형 셀토스 가격", "2027년형 셀토스 10월 15일 출시",
          "#셀토스 가격 또 인상", "2027년형 셀토스 출시 2026-10-15 (헤럴드경제 10904364, 10904878, 오토클립 2026-10-16)",
          [("1월 말 출시 2세대를 약 8개월 만에 2027년형으로, 10/15 출시", "헤럴드경제, 오토클립"),
           ("트렌디 가솔린 2,477 → 2,575만원, 체감 +98만원", "헤럴드경제, 오토클립 일치"),
           ("98만원 = 연식변경 60만원 + 개소세 인하 종료 38만원", "헤럴드경제(단일, 순수 인상폭은 매체별 60~64만원)"),
           ("1월 풀체인지 때 2,266 → 2,477만원(+211만원)", "헤럴드경제, 헤이딜러"),
           ("아반떼 2.0 모던과 시작가 차이 1월 415만원 → 177만원", "오토클립(단일)"),
           ("하이브리드 세제혜택 연말 종료 시 내년 1월 추가 인상 전망", "헤럴드경제 전망(단일, 대본은 '전망'으로)"),
           ("'출시 1년 채 안되서 년식변경에 100정도를 올려버렸네요'", "클리앙 굴러간당 2026-10-17 댓글(대사체로 다듬음)"),
           ("화면", "현대차그룹 뉴스룸 디 올 뉴 셀토스 보도사진(work/_photos/seltos/map.txt)")],
          "1월에 나온 신형 셀토스가 8개월 만에 2027년형으로 바뀌며 가격이 또 올랐습니다.\n가솔린 트렌디 2477만원에서 2575만원, 아반떼와 시작가 차이는 177만원까지 좁혀졌습니다.\n님들은 아직 가성비라고 보시나요?\n\n#셀토스 #기아 #신차 #자동차 #란빵",
          "님들은 2575만원 셀토스, 아직 가성비라고 봄?",
          "셀토스 전용 카매트, 셀토스 트렁크 정리함, 자동차 블랙박스 2채널, 차량용 무선충전 거치대, 차량용 방향제",
          "", [P("s_side", KIA, s0=1.0, s1=1.1)], typ="란빵 자동차, 신차")


def EP_seltosfire():
    S = "seltosfire"
    lines = [
        L("시동 꺼놨는데 불이 날 수 있다고?",
          [B("f01", "A compact SUV parked alone in an outdoor parking lot at night under a single street lamp, snow on the ground, away from buildings, no logos visible", s0=1.1, s1=1.3)],
          C("drv_shock", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("캐나다에서 셀토스 4만8070대가 화재 위험으로 리콜됨.",
          [B("f02", "A snowy Canadian suburban street in winter with several compact SUVs parked along the curb, overcast daylight, no logos visible"),
           B("f02", at="리콜됨", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("biz_shock"), say="캐나다에서 셀토스 사만팔천칠십대가 화재 위험으로 리콜됨.", em=["4만8070대"], em_color="yellow",
          fx=[("hit_trailer_epic", "리콜됨", 0.5)],
          info={"kind": "counter", "at": "4만8070대", "title": "캐나다 리콜", "items": [{"num": 48070, "suffix": "대", "label": "2024~2026년식 AWD", "at": "4만8070대"}]}),
        L("대상은 2024년식부터 2026년식까지 사륜구동 모델.",
          [B("f02", s0=1.0, s1=1.15)], C("biz_think"), say="대상은 이천이십사년식부터 이천이십육년식까지 사륜구동 모델.",
          em=["사륜구동"]),
        L("운전석 시트 밑 사륜 제어 장치에 제설용 염화칼슘이랑 습기가 들어가 부식되는 게 원인.",
          [B("f03", "Close-up under a car driver seat showing a small black electronic control module with corroded white salt crust on its connector, carpet with road salt stains")],
          C("seibishi", "r"), em=["염화칼슘"], em_color="yellow"),
        L("그러면 합선이 나서, 시동 끄고 세워둔 상태에서도 불이 날 수 있음.",
          [B("f03", at="합선이", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True), B("f01", at="세워둔", s0=1.0, s1=1.15)],
          C("fire119", "r"), em=["시동 끄고"], em_color="yellow", pop=("주차 중에도?!", R, "세워둔"), shake="세워둔",
          fx=[("boom_zoom_impact", "세워둔", 0.55)]),
        L("그래서 고치기 전까진 건물이나 다른 차랑 떨어진 야외에 세우라고 권고함.",
          [B("f04", "A compact SUV parked far away from a house and other cars in an empty open-air gravel lot, winter afternoon, wide shot")],
          C("komatta"), em=["떨어진 야외"]),
        L("더 황당한 건 같은 결함으로 2024년 2월에도 4만4478대를 리콜했었음.",
          [B("f02", s0=1.3, s1=1.5, fx=0.4, fy=0.5)], C("drv_surprise"),
          say="더 황당한 건 같은 결함으로 이천이십사년 이월에도 사만사천사백칠십팔대를 리콜했었음.", em=["같은 결함"],
          fx=[("scratch_vinyl", "같은", 0.45)]),
        L("합치면 9만 대가 넘음.",
          [B("f04", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("ohagya"), say="합치면 구만 대가 넘음.", em=["9만 대"], em_color="yellow",
          info={"kind": "bars", "title": "같은 결함 리콜", "items": [
              {"label": "2024년 2월", "value": 0.48, "num": 44478, "suffix": "대", "color": W},
              {"label": "2026년 10월", "value": 0.52, "num": 48070, "suffix": "대", "color": W},
              {"label": "합계", "value": 1.0, "num": 92548, "suffix": "대", "color": R, "at": "9만", "flash": "9만"}]}),
        L("다만 이건 캐나다 1세대 모델 얘기고, 국내 신형에 같은 문제가 있다는 발표는 아직 없음.",
          [B("f05", "An empty Korean car dealership showroom floor at night with lights dimmed, glossy floor, no cars and no logos")],
          C("biz_idea"), say="다만 이건 캐나다 일세대 모델 얘기고, 국내 신형에 같은 문제가 있다는 발표는 아직 없음.", em=["캐나다 1세대"],
          em_color="yellow", fx=[("correct_ding", "아직", 0.45)]),
        L("님들은 같은 결함 리콜 두 번 나온 차, 그래도 삼?", [B("f01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "삼")]),
    ]
    build(S, lines, "시동 꺼도 불날 수 있다", "셀토스 4만8천대 리콜", "캐나다 셀토스 AWD 화재 위험 리콜",
          "#셀토스 4만8천대 리콜", "기아 캐나다 셀토스 AWD 리콜 2026-10-09 (CP24, 한국신용신문 31603, Auto123)",
          [("2024~2026년식 셀토스 AWD 48,070대 리콜", "CP24 2026-10-09, 한국신용신문 2026-10-11, Auto123"),
           ("운전석 시트 아래 4WD 제어 유닛에 염분, 습기 침투 부식, 합선", "CP24, 한국신용신문, Auto123"),
           ("시동 꺼진 주차 상태에서도 화재 위험, 수리 전 건물, 다른 차에서 떨어진 야외 주차 권고", "CP24, Auto123"),
           ("같은 결함 2024년 2월 2021~2023년식 44,478대 리콜, 합산 92,548대", "Transport Canada 2024093(이전 리콜 존재), 합산은 한국신용신문(단일)"),
           ("리콜 대상은 북미 1세대로 추정, 국내 신형 동일 부품 여부 확인 안 됨", "조사 에이전트 추정. 대본은 '국내 신형 발표 없음'까지만"),
           ("대사 '시동 꺼놨는데 불이 날 수 있다고?'", "창작 반응 대사(실제 인용 아님)")],
          "캐나다에서 셀토스 사륜구동 4만8070대가 화재 위험으로 리콜됐습니다.\n시동을 끄고 세워둔 상태에서도 위험할 수 있어 야외 주차를 권고했고, 같은 결함 리콜은 두 번째입니다.\n국내 신형에 같은 문제가 있다는 발표는 아직 없습니다.\n\n#셀토스 #리콜 #기아 #자동차 #란빵",
          "님들은 같은 결함 리콜 두 번 나온 차, 그래도 삼?",
          "차량용 소화기, 자동차 블랙박스 2채널, 차량용 하부 코팅제, 자동차 카매트, 블랙박스 메모리카드",
          "국내 신형 사진은 리콜 대상 오해 소지가 있어 쓰지 않음.", [B("f05", s0=1.0, s1=1.1)])


def EP_seltoscn():
    S = "seltoscn"
    real(S, {"s_front": ("front", 0.68), "s_side": ("side", 0.62), "s_dash": ("dash", 0.4), "s_hev": ("hev", 0.43)})
    lines = [
        L("뭐? 중국 셀토스는 1600만원대라고?",
          [B("c01", "A bright modern car dealership showroom in a Chinese city with a new compact SUV on display under spotlights, big glass windows, no readable text, no logos", s0=1.1, s1=1.3)],
          C("wow", "r"), dialogue=True, speaker=3, emotion="toneup", say="뭐? 중국 셀토스는 천육백마넌대라고?"),
        L("신형 셀토스가 8월 26일 중국에서 나왔는데, 시작가가 7만9900위안임.",
          [B("c01", at="시작가가", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("sales"),
          say="신형 셀토스가 팔월 이십육일 중국에서 나왔는데, 시작가가 칠만구천구백위안임.", em=["7만9900위안"]),
        L("우리 돈으로 약 1640만원.",
          [B("c02", "Chinese yuan banknotes and a car key on a glass table in a car showroom, close-up, shallow focus")],
          C("bill_shock"), say="우리 돈으로 약 천육백사십마넌.", em=["1640만원"], em_color="yellow",
          fx=[("drop_futuristic", "1640만원", 0.5)],
          info={"kind": "bars", "title": "시작가 단순 비교", "items": [
              {"label": "중국형", "value": 0.64, "num": 1640, "suffix": "만원", "color": Y, "at": "1640만원"},
              {"label": "국내 2027년형", "value": 1.0, "num": 2575, "suffix": "만원", "color": W}]}),
        L("국내 2027년형 시작가 2575만원이랑 900만원 넘게 차이 남.",
          [P("s_front", KIA, s0=1.0, s1=1.15)], C("drv_shock"),
          say="국내 이천이십칠년형 시작가 이천오백칠십오마넌이랑 구백마넌 넘게 차이 남.", em=["900만원"], em_color="yellow",
          pop=("900만원?!", R, "900만원"), fx=[("hit_trailer_epic", "900만원", 0.5)]),
        L("심지어 중국형은 27인치 와이드 화면이 전 트림 기본.",
          [B("c03", "Interior of a modern compact SUV with a very wide panoramic dashboard display stretching across the whole dash, screen showing abstract colorful wallpaper, no readable text")],
          C("drv_surprise"), say="심지어 중국형은 이십칠인치 와이드 화면이 전 트림 기본.", em=["27인치"], em_color="yellow"),
        L("근데 반전, 이건 이름만 같은 다른 차임.",
          [B("c01", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)], C("biz_idea"), em=["다른 차"], em_color="yellow",
          pop=("다른 차?!", Y, "다른"), shake="다른", fx=[("scratch_vinyl", "반전", 0.5)]),
        L("중국형은 1.5 엔진에 115마력이나 200마력이고, 하이브리드가 아예 없음.",
          [B("c04", "Open engine bay of a compact SUV showing a small four-cylinder engine, clean, workshop lighting, no logos")],
          C("seibishi", "r"), say="중국형은 일점오 엔진에 백십오마력이나 이백마력이고, 하이브리드가 아예 없음.", em=["하이브리드가 아예 없음"]),
        L("국내형은 1.6 터보 193마력이랑 하이브리드로 나옴.",
          [P("s_hev", KIA, s0=1.0, s1=1.15), P("s_dash", KIA, at="하이브리드로")], C("dealer"),
          say="국내형은 일점육 터보 백구십삼마력이랑 하이브리드로 나옴.", em=["1.6 터보"],
          info={"kind": "compare", "at": "국내형은", "title": "같은 이름, 다른 차", "items": [
              {"label": "중국형", "color": W, "at": "국내형은", "rows": [["엔진", "1.5 / 1.5터보", W], ["하이브리드", "없음", R]]},
              {"label": "국내형", "color": Y, "at": "하이브리드로", "rows": [["엔진", "1.6터보", Y], ["하이브리드", "있음", "#7CFF6B"]]}]}),
        L("세금이랑 인증 기준도 달라서 가격을 그대로 비교하긴 어려움.",
          [P("s_side", KIA, s0=1.2, s1=1.35, fx=0.55, fy=0.5)], C("biz_think"), em=["그대로 비교"]),
        L("님들은 하이브리드 빼고 1600만원이면 중국형 삼?", [B("c03", s0=1.0, s1=1.12)], C("biz_q"),
          say="님들은 하이브리드 빼고 천육백마넌이면 중국형 삼?", fx=[("pop_bubble", "삼")]),
    ]
    build(S, lines, "중국 셀토스 1640만원", "근데 반전이 있음", "8월 26일 중국 출시, 7만9900위안부터",
          "#중국 셀토스 1640만원", "신형 셀토스 중국 출시 2026-08-26 (신화망 2026-09-02, 더구루 106304, 뉴스와 2026-08-13)",
          [("8/26 중국 출시, 7.99만~11.99만 위안", "신화망, 더구루 일치"),
           ("원화 약 1,640만원", "더구루 환산(단일)"),
           ("국내 2027년형 트렌디 2,575만원, 차이 900만원 넘음(약 935만원)", "헤럴드경제, 오토클립 / 차이는 환율, 세금, 사양 무시한 단순 계산"),
           ("27인치 와이드 디스플레이 전 트림 기본", "더구루 2건, 뉴스와"),
           ("중국형 1.5 자연흡기 115마력 / 1.5 터보 200마력, 하이브리드 없음", "신화망, 더구루"),
           ("국내형 1.6 터보 193마력 / 1.6 하이브리드", "현대차그룹 뉴스룸, 오토클립"),
           ("화면", "중국형 공식 사진 미확보라 중국 장면은 AI 배경(로고 없음), 국내형만 기아 보도사진")],
          "중국에서 신형 셀토스가 7만9900위안, 우리 돈 약 1640만원부터 나왔습니다.\n하지만 중국형은 1.5 엔진에 하이브리드가 없고, 세금과 인증도 달라 단순 비교는 어렵습니다.\n님들은 중국형 사시겠어요?\n\n#셀토스 #기아 #중국차 #자동차 #란빵",
          "님들은 하이브리드 빼고 1600만원이면 중국형 삼?",
          "셀토스 전용 카매트, 차량용 대시보드 커버, 자동차 블랙박스 2채널, 차량용 무선충전 거치대, 차량용 방향제",
          "", [P("s_front", KIA, s0=1.0, s1=1.1)], typ="란빵 자동차, 신차")


def EP_seltosvs():
    S = "seltosvs"
    real(S, SEL)
    lines = [
        L("신형 셀토스 판매량이 거의 롤러코스터임.",
          [P("s_front", KIA, s0=1.05, s1=1.2, punch=True)], C("graph_up"), em=["롤러코스터"], em_color="yellow",
          fx=[("hit_trailer_epic", "롤러코스터임", 0.4)]),
        L("7월엔 7427대 팔아서 쏘렌토까지 제치고 기아 국내 1위를 찍음.",
          [P("s_xline", KIA), P("s_side", KIA, at="1위를", s0=1.0, s1=1.15)], C("banzai"),
          say="칠월엔 칠천사백이십칠대 팔아서 쏘렌토까지 제치고 기아 국내 일위를 찍음.", em=["1위"], em_color="yellow"),
        L("근데 8월엔 3307대로 절반 넘게 빠짐.",
          [P("s_rear", KIA, s0=1.0, s1=1.15)], C("graph_down", "r"), say="근데 팔월엔 삼천삼백칠대로 절반 넘게 빠짐.",
          em=["절반 넘게"], fx=[("wrong_gameshow_buzz", "빠짐", 0.45)]),
        L("그리고 9월엔 다시 5422대로 올라옴.",
          [P("s_hall", KIA, s0=1.0, s1=1.15)], C("graph_up"), say="그리고 구월엔 다시 오천사백이십이대로 올라옴.",
          info={"kind": "bars", "title": "셀토스 국내 판매", "items": [
              {"label": "7월", "value": 1.0, "num": 7427, "suffix": "대", "color": Y},
              {"label": "8월", "value": 0.45, "num": 3307, "suffix": "대", "color": R},
              {"label": "9월", "value": 0.73, "num": 5422, "suffix": "대", "color": W, "at": "5422대로"}]}),
        L("같은 달 라이벌 코나는 1872대, 셀토스가 약 3배를 판 셈.",
          [P("s_side", KIA, s0=1.2, s1=1.35, fx=0.55, fy=0.5)], C("wow", "r"),
          say="같은 달 라이벌 코나는 천팔백칠십이대, 셀토스가 약 세 배를 판 셈.", em=["약 3배"], em_color="yellow",
          pop=("약 3배!!", Y, "3배를"), fx=[("drop_futuristic", "3배를", 0.5)]),
        L("연식변경 전엔 하이브리드 시작가도 코나랑 딱 2만원 차이였음.",
          [P("s_hev", KIA, s0=1.0, s1=1.15)], C("biz_think"), say="연식변경 전엔 하이브리드 시작가도 코나랑 딱 이마넌 차이였음.",
          em=["2만원"], em_color="yellow"),
        L("근데 커뮤니티 반응이 마냥 좋진 않음.",
          [P("s_dash", KIA, s0=1.0, s1=1.12)], C("biz_q", "r"), fx=[("drum_rimshot", "마냥", 0.4)]),
        L("DCT에 140마력이라, 지금 사기엔 좀 그래요.",
          [P("s_hev", KIA, s0=1.3, s1=1.45, fx=0.45, fy=0.55)], C("drv_think", "r"), dialogue=True, speaker=2, emotion="normal",
          say="디씨티에 백사십마력이라, 지금 사기엔 좀 그래요."),
        L("게다가 10월엔 연식변경으로 가격까지 올랐음.",
          [P("s_seat", KIA, s0=1.0, s1=1.15)], C("bill_shock"), say="게다가 시월엔 연식변경으로 가격까지 올랐음.", em=["가격까지"]),
        L("님들은 셀토스랑 코나 하이브리드 중에 뭐 삼?", [P("s_front", KIA, s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "삼")]),
    ]
    build(S, lines, "7월 1등 8월 반토막", "셀토스 판매 롤러코스터", "9월엔 코나보다 약 3배",
          "#셀토스 판매 롤러코스터", "기아 월별 판매 실적 2026-08-03, 09-01, 10-01 (현대차그룹 뉴스룸) + 현대차 9월 실적",
          [("7월 국내 7,427대, 기아 국내 1위(쏘렌토 6,153대)", "현대차그룹 뉴스룸 2026-08-03, 위드뉴스"),
           ("8월 국내 3,307대", "현대차그룹 뉴스룸 2026-09-01, 오토뷰(감소 원인 확인 안 됨, 대본에 원인 안 씀)"),
           ("9월 국내 5,422대", "현대차그룹 뉴스룸 2026-10-01, 카가이"),
           ("9월 코나 국내 1,872대, 셀토스 약 2.9배", "현대차 9월 판매 보도자료(배수는 계산값)"),
           ("하이브리드 시작가 코나 2,938 vs 셀토스 2,940만원(연식변경 전)", "뉴스와 2026-09-11(단일)"),
           ("'dct에 140마력이라..좀 그래요 지금 사기엔..'", "클리앙 굴러간당 2026-10-16 댓글"),
           ("10/15 2027년형 가격 인상", "헤럴드경제, 오토클립")],
          "신형 셀토스 판매가 7월 7427대로 기아 국내 1위, 8월 3307대, 9월 5422대로 오르내렸습니다.\n9월엔 코나의 약 3배를 팔았지만 커뮤니티 반응은 엇갈립니다.\n님들은 셀토스와 코나 중 뭘 고르시겠어요?\n\n#셀토스 #코나 #기아 #자동차 #란빵",
          "님들은 셀토스랑 코나 하이브리드 중에 뭐 삼?",
          "셀토스 전용 카매트, 셀토스 트렁크 정리함, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 방향제",
          "", [P("s_xline", KIA, s0=1.0, s1=1.1)], typ="란빵 자동차, 신차")


# ───────────────────────── 테슬라 ─────────────────────────
TS = " The car is a sleek white minimalist electric crossover with no badges and no logos."


def EP_teslaygrand():
    S = "teslaygrand"
    lines = [
        L("수입차가 국산차 1등을 먹었다고?",
          [B("y01", "A long row of new white minimalist electric crossovers parked at a vehicle delivery center in Korea, sunny day, wide shot." + TS, s0=1.1, s1=1.3)],
          C("wow", "r"), dialogue=True, speaker=3, emotion="toneup", say="수입차가 국산차 일등을 먹었다고?"),
        L("9월 국내에서 제일 많이 팔린 승용차가 그랜저가 아니라 테슬라 모델Y였음.",
          [B("y01", at="그랜저가", s0=1.0, s1=1.15), B("y02", "A white minimalist electric crossover driving on a Seoul city expressway at sunset, motion blur." + TS, at="모델Y였음")],
          C("biz_surprise"), say="구월 국내에서 제일 많이 팔린 승용차가 그랜저가 아니라 테슬라 모델와이였음.", em=["모델Y"], em_color="yellow",
          pop=("1위!!", Y, "모델Y였음"), fx=[("hit_trailer_epic", "모델Y였음", 0.5)]),
        L("모델Y가 1만1천여 대, 그랜저는 8898대.",
          [B("y03", "A Korean car registration office parking lot with many new cars with temporary plates, daytime, no readable text")],
          C("graph_up"), say="모델와이가 만천여 대, 그랜저는 팔천팔백구십팔대.", em=["1만1천여 대"],
          info={"kind": "bars", "title": "9월 국내 승용 판매", "items": [
              {"label": "모델Y", "value": 1.0, "num": 11421, "suffix": "대", "color": Y, "at": "1만1천여"},
              {"label": "그랜저", "value": 0.78, "num": 8898, "suffix": "대", "color": W, "at": "8898대"},
              {"label": "아반떼", "value": 0.64, "num": 7305, "suffix": "대", "color": W},
              {"label": "쏘렌토", "value": 0.61, "num": 6957, "suffix": "대", "color": W}]}),
        L("테슬라 브랜드 전체로는 1만2372대, 수입 승용차 셋 중 하나가 테슬라였음.",
          [B("y02", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("biz_shock"),
          say="테슬라 브랜드 전체로는 만이천삼백칠십이대, 수입 승용차 셋 중 하나가 테슬라였음.", em=["셋 중 하나"], em_color="yellow"),
        L("같은 달 국산 5사 내수는 20% 가까이 줄었는데, 테슬라는 36% 늘었음.",
          [B("y04", "An empty quiet Korean car dealership showroom in the afternoon with a few sedans on display and no customers, no logos")],
          C("graph_down", "r"), say="같은 달 국산 오사 내수는 이십퍼센트 가까이 줄었는데, 테슬라는 삼십육퍼센트 늘었음.", em=["36%"],
          fx=[("wrong_gameshow_buzz", "줄었는데", 0.4)]),
        L("근데 반전, 6인승 모델Y L만 따로 보면 8690대로 그랜저보다 적음.",
          [B("y05", "Interior of a white minimalist electric SUV showing three rows of seats with six captain chairs, bright daylight, no logos")],
          C("biz_idea"), say="근데 반전, 육인승 모델와이 엘만 따로 보면 팔천육백구십대로 그랜저보다 적음.", em=["그랜저보다 적음"],
          pop=("반전?!", Y, "반전"), fx=[("scratch_vinyl", "반전", 0.5)]),
        L("1월부터 9월까지 누적은 쏘렌토 7만4933대, 모델Y 7만3123대로 1810대 차이.",
          [B("y03", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_think", "r"),
          say="일월부터 구월까지 누적은 쏘렌토 칠만사천구백삼십삼대, 모델와이 칠만삼천백이십삼대로 천팔백십대 차이.", em=["1810대"], em_color="yellow",
          info={"kind": "compare", "at": "쏘렌토", "title": "1~9월 누적", "items": [
              {"label": "쏘렌토", "color": W, "at": "쏘렌토", "rows": [["누적", "74,933대", W]]},
              {"label": "모델Y", "color": Y, "at": "7만3123대로", "rows": [["누적", "73,123대", Y]]}]}),
        L("견적 내보니까 모Y 비싸서 못 삽니다. 절대 싼 차 아니던데요.",
          [B("y04", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("saifu", "r"), dialogue=True, speaker=2, emotion="normal",
          say="견적 내보니까 모와이 비싸서 못 삽니다. 절대 싼 차 아니던데요."),
        L("님들은 연말에 모델Y가 쏘렌토 잡는다고 봄?", [B("y02", s0=1.0, s1=1.12)], C("biz_q"),
          say="님들은 연말에 모델와이가 쏘렌토 잡는다고 봄?", fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "그랜저 제친 수입차", "9월 판매 1위 모델Y", "산업부 9월 자동차산업 동향",
          "#그랜저 제친 모델Y", "9월 국내 승용차 판매(산업통상부 2026-10-19 발표, KAIDA 10/6)",
          [("9월 모델Y 11,421대, 그랜저 8,898, 아반떼 7,305, 쏘렌토 6,957", "뉴스스페이스 2026-10-20, 오토센티널 2026-10-19 일치(서울경제는 11,157대, 대본은 '1만1천여 대')"),
           ("테슬라 9월 12,372대, 수입 승용 점유율 35.5%", "아시아경제, 쿠키뉴스, 서울경제(KAIDA)"),
           ("국산 5사 9월 내수 19.8% 감소, 테슬라 전년 동월 대비 36.4% 증가", "경향신문 2026-10-07"),
           ("모델Y L 단독 8,690대(그랜저보다 208대 적음)", "쿠키뉴스, 아시아경제 2026-10-06"),
           ("1~9월 누적 쏘렌토 74,933 / 모델Y 73,123, 차이 1,810대", "뉴스스페이스, 오토센티널"),
           ("'견적 내보니까 모y 비싸서 못삽니다. 절대 싼 차 아니던데요.'", "클리앙 굴러간당 2026-10-18 댓글"),
           ("화면", "AI 배경, 차는 로고 없는 흰색 전기 크로스오버(특정 차 사진 아님)")],
          "9월 국내 승용차 판매 1위는 그랜저가 아니라 테슬라 모델Y였습니다.\n1~9월 누적은 쏘렌토와 1810대 차이.\n님들은 연말에 모델Y가 연간 1위까지 갈 거라고 보시나요?\n\n#테슬라 #모델Y #그랜저 #자동차 #란빵",
          "님들은 연말에 모델Y가 쏘렌토 잡는다고 봄?",
          "모델Y 전용 카매트, 모델Y 트렁크 정리함, 테슬라 무선충전 패드, 자동차 블랙박스 2채널, 차량용 방향제",
          "", [B("y01", s0=1.0, s1=1.1)], typ="란빵 자동차, 테슬라")


def EP_teslafsdkr():
    S = "teslafsdkr"
    lines = [
        L("테슬라코리아가 그냥 놀고 있는 거죠.",
          [B("q01", "Inside a white minimalist electric car on a Korean highway at dusk, large center touchscreen showing a blurred driving visualization, hands-free steering wheel, no people visible." + TS, s0=1.1, s1=1.3)],
          C("biz_angry", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("국내 테슬라 약 24만 대 중에 FSD를 쓸 수 있는 차는 5만3천여 대뿐.",
          [B("q02", "Aerial view of a large Korean apartment complex underground parking entrance area with many white electric crossovers parked, daytime." + TS)],
          C("biz_shock"), say="국내 테슬라 약 이십사만 대 중에 에프에스디를 쓸 수 있는 차는 오만삼천여 대뿐.", em=["5만3천여 대"], em_color="yellow"),
        L("4대 중 3대 넘게, 77.6%는 못 씀.",
          [B("q02", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], C("ohagya"), say="네 대 중 세 대 넘게, 칠십칠점육퍼센트는 못 씀.",
          pop=("77.6% 불가", R, "못"), shake="못", fx=[("hit_trailer_epic", "못", 0.5)],
          info={"kind": "bars", "title": "국내 테슬라 FSD", "items": [
              {"label": "사용 가능", "value": 0.29, "num": 53477, "suffix": "대", "color": "#7CFF6B"},
              {"label": "사용 불가", "value": 1.0, "num": 185491, "suffix": "대", "color": R, "at": "77.6%는"}]}),
        L("못 쓰는 차 대부분이 중국에서 만든 모델3랑 모델Y임.",
          [B("q03", "A car carrier ship unloading rows of new white electric crossovers at a Korean port, daytime, wide shot." + TS)],
          C("biz_think"), say="못 쓰는 차 대부분이 중국에서 만든 모델쓰리랑 모델와이임.", em=["중국에서 만든"]),
        L("미국산은 한미 FTA 특례로 되지만, 중국산은 국내 안전기준을 따로 맞춰야 해서임.",
          [B("q03", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("lawyer"), say="미국산은 한미 에프티에이 특례로 되지만, 중국산은 국내 안전기준을 따로 맞춰야 해서임.",
          em=["국내 안전기준"],
          info={"kind": "compare", "at": "미국산은", "title": "왜 못 쓰나", "items": [
              {"label": "미국산", "color": "#7CFF6B", "at": "미국산은", "rows": [["FSD", "가능", "#7CFF6B"]]},
              {"label": "중국산", "color": R, "at": "중국산은", "rows": [["FSD", "불가", R]]}]}),
        L("근데 10월 8일 국정감사에서 테슬라코리아 대표가 정부에 검증 신청한 적이 없다고 답함.",
          [B("q04", "An empty Korean National Assembly committee hearing room with rows of desks, microphones and name plates, nameplates unreadable, soft light")],
          C("biz_tehe", "r"), say="근데 시월 팔일 국정감사에서 테슬라코리아 대표가 정부에 검증 신청한 적이 없다고 답함.", em=["신청한 적이 없다고"],
          em_color="yellow", pop=("신청 0번?!", Y, "없다고"), fx=[("scratch_vinyl", "없다고", 0.5)]),
        L("국토부랑 교통안전공단도 FSD를 따로 시험해 본 적이 없음.",
          [B("q05", "An empty vehicle test track with traffic cones and a closed course, overcast day, no cars")],
          C("komatta"), say="국토부랑 교통안전공단도 에프에스디를 따로 시험해 본 적이 없음.", em=["시험해 본 적이 없음"],
          fx=[("drum_rimshot", "없음", 0.4)]),
        L("그 와중에 같은 주 유럽 일부 나라에선 FSD 이름을 테슬라 어시스티드 드라이빙으로 바꿈.",
          [B("q01", s0=1.4, s1=1.6, fx=0.5, fy=0.45)], C("biz_surprise"),
          say="그 와중에 같은 주 유럽 일부 나라에선 에프에스디 이름을 테슬라 어시스티드 드라이빙으로 바꿈.", em=["이름을"]),
        L("독일 교통부가 이름이 오해를 부른다고 지적한 뒤였음.",
          [B("q05", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("judge", "r"), em=["오해를"], em_color="yellow"),
        L("님들은 FSD 안 되는 거 알고도 테슬라 삼?", [B("q02", s0=1.0, s1=1.12)], C("biz_q"),
          say="님들은 에프에스디 안 되는 거 알고도 테슬라 삼?", fx=[("pop_bubble", "삼")]),
    ]
    build(S, lines, "국내 테슬라 4대 중 3대", "FSD 못 쓰는 이유", "10월 8일 국정감사, 검증 신청 0건",
          "#FSD 못 쓰는 테슬라", "국토위 국정감사 2026-10-08 (MTN, 블로터 675303, 뉴스핌, 유카포스트) + 유럽 명칭 변경(TechCrunch, Electrek 10/9)",
          [("9월 말 국내 등록 테슬라 238,968대 중 FSD 가능 53,477(22.4%), 불가 185,491(77.6%)", "MTN, 블로터, 유카포스트 일치"),
           ("불가 차량 대부분 중국산 모델3, 모델Y 183,407대", "블로터, MTN"),
           ("미국산은 한미 FTA 안전기준 특례, 중국산은 국내 기준 충족 필요", "서영득 대표 국감 설명(MTN, 뉴스핌 발췌, 대본은 직접인용 아님)"),
           ("국감에서 감독형 FSD 검증을 국토부 등에 공식 신청한 적 없다고 답", "MTN, 뉴스핌, 블로터 2026-10-08"),
           ("국토부, 교통안전공단 FSD 별도 시험 실적 없음", "MTN 2026-10-08"),
           ("10/8~9 유럽 일부 국가 명칭 'Tesla Assisted Driving'으로 변경, 독일 교통부 지적 뒤", "TechCrunch, Electrek 2026-10-09"),
           ("'테슬라 코리아가 그냥 놀고 있는건데 설명이 길죠.'", "클리앙 굴러간당 2026-10-08 댓글(대사체로 줄임)")],
          "국내 테슬라 약 24만 대 중 FSD를 쓸 수 있는 차는 5만3천여 대, 77.6%는 못 씁니다.\n국정감사에서 테슬라코리아는 정부에 검증 신청을 한 적이 없다고 답했습니다.\n님들은 그래도 테슬라 사시겠어요?\n\n#테슬라 #FSD #자율주행 #자동차 #란빵",
          "님들은 FSD 안 되는 거 알고도 테슬라 삼?",
          "테슬라 무선충전 패드, 모델Y 전용 카매트, 테슬라 센터콘솔 정리함, 자동차 블랙박스 2채널, 차량용 방향제",
          "", [B("q03", s0=1.0, s1=1.1)], typ="란빵 자동차, 테슬라")


def EP_teslarobot():
    S = "teslarobot"
    lines = [
        L("테슬라 가치의 대부분은 옵티머스와 사이버캡이 될 겁니다.",
          [B("o01", "A sleek white humanoid robot standing in a clean modern factory hall next to a two-seat futuristic robotaxi with no steering wheel, dramatic lighting, no logos", s0=1.1, s1=1.3)],
          C("robot", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("머스크가 10월 17일 X에 직접 올린 말임.",
          [B("o02", "A smartphone lying on a desk at night showing a social media app feed, screen blurred and unreadable, city lights in the background")],
          C("biz_surprise"), say="머스크가 시월 십칠일 엑스에 직접 올린 말임.", em=["직접"]),
        L("차 회사 사장이 차가 아니라 로봇이랑 로보택시가 본업이라고 한 셈.",
          [B("o01", at="로봇이랑", s0=1.3, s1=1.5, fx=0.35, fy=0.5, punch=True)], C("wow", "r"), em=["로봇이랑 로보택시"],
          em_color="yellow", pop=("차가 아니라?!", Y, "아니라"), fx=[("hit_trailer_epic", "아니라", 0.5)]),
        L("실제로 3분기 차 인도량은 48만6532대로 예상은 넘었는데,",
          [B("o03", "Rows of brand-new white minimalist electric cars lined up in a huge outdoor factory lot at dawn, wide shot, no logos")],
          C("graph_up"), say="실제로 삼분기 차 인도량은 사십팔만육천오백삼십이대로 예상은 넘었는데,", em=["48만6532대"]),
        L("작년 같은 분기보단 2.1% 줄었음.",
          [B("o03", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("graph_down", "r"), say="작년 같은 분기보단 이점일퍼센트 줄었음.",
          em=["2.1% 줄었음"], em_color="yellow", fx=[("wrong_gameshow_buzz", "줄었음", 0.45)],
          info={"kind": "bars", "title": "3분기 인도량", "items": [
              {"label": "작년 3분기", "value": 1.0, "num": 497099, "suffix": "대", "color": W},
              {"label": "올해 3분기", "value": 0.98, "num": 486532, "suffix": "대", "color": R, "at": "2.1%"}]}),
        L("반면 운전대랑 페달이 아예 없는 사이버캡은,",
          [B("o04", "Interior of a futuristic two-seat robotaxi cabin with no steering wheel and no pedals, a single screen, clean white seats, no logos")],
          C("jidou"), em=["운전대랑 페달이"]),
        L("텍사스 등록이 하룻밤에 169대에서 319대로 늘었음.",
          [B("o05", "A small fleet of identical futuristic two-door robotaxis with no logos parked in a sunny Texas parking lot, wide shot")],
          C("graph_up"), say="텍사스 등록이 하룻밤에 백육십구대에서 삼백십구대로 늘었음.", em=["319대"],
          em_color="yellow", fx=[("drop_futuristic", "319대로", 0.5)]),
        L("근데 미국 도로교통안전국은 사이버캡 안전기준 자체인증 절차를 조사 중임.",
          [B("o05", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("judge", "r"), em=["조사 중"], em_color="yellow",
          fx=[("scratch_vinyl", "조사", 0.45)]),
        L("옵티머스는 아직 생산량이나 가격 같은 공식 숫자가 하나도 없음.",
          [B("o01", s0=1.4, s1=1.6, fx=0.65, fy=0.45)], C("robot", "r"), em=["공식 숫자"], fx=[("drum_rimshot", "없음", 0.4)]),
        L("님들은 테슬라가 차 회사라고 봄, 로봇 회사라고 봄?", [B("o01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "로봇")]),
    ]
    build(S, lines, "머스크가 한 말", "테슬라는 차 회사가 아니다?", "옵티머스와 사이버캡이 가치의 대부분",
          "#테슬라 본업은 로봇?", "일론 머스크 X 게시 2026-10-17 PT (Teslanorth 10/18, FinanceFeeds 10/19) + 테슬라 3분기 인도 IR(10/2)",
          [("'Optimus and Cybercab will be the vast majority of Tesla's value.'", "머스크 X 2026-10-17, Teslanorth, FinanceFeeds 교차"),
           ("3분기 인도 486,532대, 예상치(약 46만2천) 상회, 전년 497,099대 대비 2.1% 감소", "테슬라 IR, CNBC, TIKR"),
           ("사이버캡 텍사스 등록 하룻밤 169 → 319대(10/9~10)", "Teslanorth 2026-10-09, Tech Insider 인용 위키백과"),
           ("사이버캡 운전대, 페달 없음, NHTSA 9/4 자체인증 절차 조사 착수", "위키백과(로이터 2026-09-04 인용)"),
           ("옵티머스 생산량, 단가 공식 수치 없음", "FinanceFeeds 명시"),
           ("화면", "AI 배경(로고 없는 로봇, 로보택시), 실존 인물 사진 없음")],
          "머스크가 테슬라 가치의 대부분은 옵티머스와 사이버캡이 될 거라고 했습니다.\n3분기 차 인도량은 전년보다 2.1% 줄었고, 사이버캡 등록은 하룻밤에 319대로 늘었습니다.\n님들은 테슬라가 차 회사라고 보시나요?\n\n#테슬라 #머스크 #옵티머스 #로보택시 #란빵",
          "님들은 테슬라가 차 회사라고 봄, 로봇 회사라고 봄?",
          "테슬라 무선충전 패드, 모델Y 전용 카매트, 테슬라 센터콘솔 정리함, 자동차 블랙박스 2채널, 차량용 방향제",
          "3분기 실적(한국 10/22 아침 발표) 숫자는 넣지 않음.", [B("o05", s0=1.0, s1=1.1)], typ="란빵 자동차, 테슬라")


# ───────────────────────── 자동차 관련법 ─────────────────────────

def EP_alcolock():
    S = "alcolock"
    lines = [
        L("선생님, 이 차는 숨부터 불어야 시동이 걸립니다.",
          [B("a01", "Close-up of a small handheld breath alcohol ignition interlock device with a mouthpiece, mounted near a car steering wheel, dashboard lights on, night", s0=1.1, s1=1.3)],
          C("police", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("10월 24일부터 음주운전 방지장치 조건부 면허 첫 대상자가 나옴.",
          [B("a02", "A car parked in a quiet residential street at night with the driver door open and the interior dome light on, a breath test device on the seat")],
          C("biz_surprise"), say="시월 이십사일부터 음주운전 방지장치 조건부 면허 첫 대상자가 나옴.", em=["10월 24일"], em_color="yellow",
          fx=[("hit_trailer_epic", "첫", 0.45)]),
        L("5년 안에 음주운전으로 또 걸려서 면허가 취소된 사람이 대상임.",
          [B("a03", "A police checkpoint on a Korean road at night with orange traffic cones and a lit sign, cars waiting, no people visible")],
          C("police_angry", "r"), say="오년 안에 음주운전으로 또 걸려서 면허가 취소된 사람이 대상임.", em=["또 걸려서"]),
        L("차에 단 장치에 숨을 불어서 술이 나오면 시동이 안 걸림.",
          [B("a01", at="술이", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)], C("drv_shock"), em=["시동이 안 걸림"], em_color="yellow",
          pop=("시동 잠금!!", R, "안"), fx=[("wrong_gameshow_buzz", "안", 0.45)]),
        L("다는 기간은 면허 결격기간이랑 같아서, 결격 2년이면 그 뒤 2년을 달고 다녀야 함.",
          [B("a04", "A wall calendar with many pages flipped, a car key hanging on a hook next to it, morning light")],
          C("biz_think"), say="다는 기간은 면허 결격기간이랑 같아서, 결격 이년이면 그 뒤 이년을 달고 다녀야 함.", em=["2년"]),
        L("장치 값은 200만원에서 300만원, 전부 본인 부담.",
          [B("a05", "Korean banknotes and an invoice next to a small breath interlock device box on a counter at a car service shop, text blurred")],
          C("bill_shock"), say="장치 값은 이백마넌에서 삼백마넌, 전부 본인 부담.", em=["본인 부담"], em_color="yellow",
          fx=[("drop_futuristic", "300만원", 0.5)]),
        L("장치를 뜯거나 조작하면 3년 이하 징역이나 3천만원 이하 벌금.",
          [B("a01", s0=1.0, s1=1.15)], C("judge", "r"), say="장치를 뜯거나 조작하면 삼년 이하 징역이나 삼천마넌 이하 벌금.",
          em=["3천만원"], em_color="yellow", shake="조작하면", fx=[("boom_zoom_impact", "조작하면", 0.5)],
          info={"kind": "bars", "title": "처벌 (도로교통법)", "items": [
              {"label": "장치 조작", "value": 1.0, "num": 3000, "suffix": "만원 이하", "color": R, "at": "조작하면"},
              {"label": "장치 없이 운전", "value": 0.1, "num": 300, "suffix": "만원 이하", "color": W},
              {"label": "대신 불어주기", "value": 0.1, "num": 300, "suffix": "만원 이하", "color": W}]}),
        L("야, 내가 대신 불어줄게.",
          [B("a02", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("drv_laugh", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("이러면 대신 분 친구도 1년 이하 징역이나 300만원 이하 벌금임.",
          [B("a01", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("police", "r"), say="이러면 대신 분 친구도 일년 이하 징역이나 삼백마넌 이하 벌금임.",
          em=["친구도"], em_color="yellow", pop=("친구도 처벌!!", R, "친구도"), fx=[("scratch_vinyl", "친구도", 0.5)]),
        L("님들은 이 장치면 음주운전 줄어든다고 봄?", [B("a03", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "10월 24일부터", "숨 불어야 시동 걸리는 차", "음주운전 방지장치 조건부 면허 첫 적용",
          "#음주 시동잠금 첫 적용", "도로교통법 제80조의2 음주운전 방지장치 조건부 면허, 최초 적용 2026-10-24 (경찰청, KTV, 매일신문 2026-09-22)",
          [("최초 적용일 2026-10-24(법 시행 2024-10-25, 최소 결격 2년 경과)", "경찰청 2026 달라지는 도로교통법령 보조자료, KTV 카드뉴스"),
           ("5년 이내 재위반으로 면허 취소된 사람 등 대상", "도로교통법 제80조의2 제1항(국가법령정보센터)"),
           ("부착 기간 = 결격기간과 같은 기간, 결격 2년이면 이후 2년", "제80조의2 제2항, 경찰청 예시"),
           ("비용 200만~300만원 본인 부담", "매일신문 2026-09-22(경찰청 자료는 약 300만원)"),
           ("장치 해체, 조작 3년 이하 징역 또는 3천만원 이하 벌금", "제148조의3 제1항"),
           ("장치 없는 차 운전 1년/300만원(제152조 제1호의2), 대신 불어주기 1년/300만원(제148조의3 제3항)", "법령 원문 기준. 경찰청 보조자료, 정책브리핑의 '3년/3천만원' 표기는 원문과 다름"),
           ("대사 2줄", "경찰, 친구 대사는 상황 예시(창작)")],
          "10월 24일부터 음주운전 방지장치 조건부 면허 첫 대상자가 나옵니다.\n5년 안에 다시 걸려 면허가 취소된 사람은 숨을 불어야 시동이 걸리는 장치를 본인 돈으로 달아야 합니다.\n대신 불어준 친구도 처벌됩니다.\n\n#음주운전 #도로교통법 #방지장치 #자동차 #란빵",
          "님들은 이 장치면 음주운전 줄어든다고 봄?",
          "음주측정기, 개인용 음주측정기, 자동차 블랙박스 2채널, 블랙박스 메모리카드, 차량용 방향제",
          "", [B("a04", s0=1.0, s1=1.1)], typ="란빵 자동차, 교통법")


def EP_drunkassist():
    S = "drunkassist"
    lines = [
        L("야, 키 여기 있다. 나 좀 집까지 태워줘.",
          [B("d01", "A car key held out over a restaurant table covered with soju bottles and glasses at night, Korean pub interior, close-up, no faces", s0=1.1, s1=1.3)],
          C("drv_laugh", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("술 취한 친구한테 이렇게 말하면, 내년 6월 3일부터는 그 자체로 범죄임.",
          [B("d01", at="범죄임", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)], C("police_angry", "r"),
          say="술 취한 친구한테 이렇게 말하면, 내년 유월 삼일부터는 그 자체로 범죄임.", em=["그 자체로 범죄"], em_color="yellow",
          pop=("범죄!!", R, "범죄임"), shake="범죄임", fx=[("hit_trailer_epic", "범죄임", 0.5)]),
        L("올해 6월 도로교통법에 음주운전 조장 금지 조항이 새로 생겼음.",
          [B("d02", "A thick Korean law book open on a desk with a highlighter and car keys, pages blurred, desk lamp")],
          C("lawyer"), say="올해 유월 도로교통법에 음주운전 조장 금지 조항이 새로 생겼음.", em=["새로"]),
        L("술 취한 걸 알면서 차를 내주거나,",
          [B("d03", "A car key being handed across the hood of a car at night in a pub parking lot, close-up of hands-free key on the hood, no people")],
          C("drv_idea"), em=["차를 내주거나"]),
        L("운전하라고 부추기거나,",
          [B("d04", "Night view of a car driver seat through an open door, engine start button glowing, soju bottle on the passenger seat floor")],
          C("biz_laugh", "r"), em=["부추기거나"]),
        L("태워달라고 해서 같이 타면 처벌 대상.",
          [B("d05", "View of an empty passenger seat in a car at night with the seat belt fastened across it, city lights outside")],
          C("busdrv", "r"), em=["처벌 대상"], em_color="yellow", fx=[("wrong_gameshow_buzz", "처벌", 0.45)]),
        L("처벌은 3년 이하 징역이나 1천만원 이하 벌금.",
          [B("d02", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("judge", "r"), say="처벌은 삼년 이하 징역이나 천마넌 이하 벌금.",
          em=["3년 이하"], em_color="yellow", fx=[("drop_futuristic", "1천만원", 0.5)],
          info={"kind": "counter", "at": "1천만원", "title": "음주운전 조장", "items": [{"num": 1000, "suffix": "만원 이하", "label": "또는 3년 이하 징역", "at": "1천만원"}]}),
        L("단, 그냥 같이 탄 것만으론 안 되고, 태워달라고 요구해서 탄 경우임.",
          [B("d05", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_idea"), em=["요구해서"], fx=[("correct_ding", "단", 0.45)]),
        L("지금까진 따로 조항이 없어서, 동승자는 방조죄로만 처벌해 왔음.",
          [B("d02", s0=1.0, s1=1.15)], C("biz_think"), em=["방조죄"]),
        L("님들은 친구가 술 먹고 운전한다 하면 말림?", [B("d01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "말림")]),
    ]
    build(S, lines, "나 좀 태워줘 한마디가", "내년부터 범죄", "도로교통법 제44조의2 신설, 2027년 6월 3일 시행",
          "#태워줘 한마디에 징역", "도로교통법 제44조의2(술에 취한 상태에서의 운전행위 조장 금지) 2026-06-02 신설, 시행 2027-06-03",
          [("제44조의2 신설 2026.6.2, 시행 2027.6.3", "국가법령정보센터 도로교통법 원문 [시행일: 2027. 6. 3.]"),
           ("취한 걸 알면서 ① 자동차 제공 ② 운전 권유, 독려 ③ 운송 요구해 동승", "제44조의2 원문"),
           ("3년 이하 징역 또는 1천만원 이하 벌금", "제148조의2 제7항 신설"),
           ("단순 동승은 해당 안 됨('운송을 요구하여 동승')", "조문 문구(조사 에이전트 해석)"),
           ("그동안 별도 조항 없이 형법상 방조로 처벌", "국회 행안위 소위 통과 보도(2026-03-24), 을왕리 사건 1심 동승자 방조 유죄(뉴시스 2021-04-01)"),
           ("첫 줄 대사", "상황 예시(창작)")],
          "술 취한 친구에게 차 키를 주거나, 운전을 부추기거나, 태워달라고 해서 같이 타면 내년 6월 3일부터 처벌됩니다.\n3년 이하 징역 또는 1천만원 이하 벌금.\n님들은 친구가 술 먹고 운전한다면 말리시나요?\n\n#음주운전 #도로교통법 #동승자 #자동차 #란빵",
          "님들은 친구가 술 먹고 운전한다 하면 말림?",
          "음주측정기, 개인용 음주측정기, 대리운전 차키 케이스, 자동차 블랙박스 2채널, 차량용 방향제",
          "", [B("d03", s0=1.0, s1=1.1)], typ="란빵 자동차, 교통법")


def EP_drugdrive():
    S = "drugdrive"
    lines = [
        L("어제 잠 안 와서 수면제 하나 먹은 게 다인데요?",
          [B("g01", "A small orange prescription pill bottle and a few white tablets on a car center console at night, dashboard lights glowing, close-up", s0=1.1, s1=1.3)],
          C("drv_q", "r"), dialogue=True, speaker=3, emotion="normal"),
        L("약물운전 단속에 제일 많이 걸린 건 마약이 아니라 수면제 졸피뎀이었음.",
          [B("g01", at="졸피뎀이었음", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)], C("biz_shock"),
          em=["수면제 졸피뎀"], em_color="yellow", pop=("수면제?!", Y, "수면제"), fx=[("hit_trailer_epic", "수면제", 0.5)]),
        L("국과수가 분석한 약물운전 1046건 중 졸피뎀이 370건으로 1위.",
          [B("g02", "A forensic laboratory bench with test tubes, a centrifuge and sample vials under bright white light, no people")],
          C("graph_up"), say="국과수가 분석한 약물운전 천사십육건 중 졸피뎀이 삼백칠십건으로 일위.", em=["370건"],
          info={"kind": "bars", "title": "약물운전 검출 (국과수 2023~2025)", "items": [
              {"label": "졸피뎀", "value": 1.0, "num": 370, "suffix": "건", "color": R, "at": "1046건", "flash": "370건으로"},
              {"label": "알프라졸람", "value": 0.39, "num": 144, "suffix": "건", "color": W, "at": "1046건"},
              {"label": "플루니트라제팜", "value": 0.34, "num": 126, "suffix": "건", "color": W, "at": "1046건"}]}),
        L("병원에서 받는 의료용 마약류가 55%, 불법 마약은 4%뿐이었음.",
          [B("g03", "A pharmacy paper bag and prescription medicine boxes on a kitchen table, morning light, labels unreadable")],
          C("biz_surprise"), say="병원에서 받는 의료용 마약류가 오십오퍼센트, 불법 마약은 사퍼센트뿐이었음.", em=["55%"], em_color="yellow"),
        L("그리고 올해 4월부터 약물운전은 5년 이하 징역이나 2천만원 이하 벌금으로 세짐.",
          [B("g04", "A police checkpoint at night on a Korean road with a patrol car's flashing lights, traffic cones, no people visible")],
          C("police", "r"), say="그리고 올해 사월부터 약물운전은 오년 이하 징역이나 이천마넌 이하 벌금으로 세짐.", em=["5년 이하"], em_color="yellow",
          shake="세짐", fx=[("boom_zoom_impact", "세짐", 0.5)]),
        L("최고형이 혈중알코올 0.2% 넘는 만취 운전이랑 같아진 거임.",
          [B("g04", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("judge", "r"), say="최고형이 혈중알코올 영점이퍼센트 넘는 만취 운전이랑 같아진 거임.",
          em=["만취 운전"]),
        L("입 좀 벌려주세요. 침으로 약물 검사합니다.",
          [B("g05", "Close-up of a saliva drug test kit cartridge held over the open window of a car at night, police flashlight light, no faces")],
          C("police", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("이 검사를 거부해도 똑같이 5년 이하 징역이나 2천만원 이하 벌금.",
          [B("g05", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], C("police_angry", "r"),
          say="이 검사를 거부해도 똑같이 오년 이하 징역이나 이천마넌 이하 벌금.", em=["거부해도"], em_color="yellow",
          pop=("거부해도!!", R, "거부해도"), fx=[("scratch_vinyl", "거부해도", 0.5)]),
        L("약 먹은 것 자체가 아니라, 정상 운전이 어려운 상태로 운전하면 처벌임.",
          [B("g03", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_idea"), em=["정상 운전이 어려운"], fx=[("correct_ding", "자체가", 0.45)]),
        L("님들은 수면제 먹은 다음 날 운전, 괜찮다고 생각했음?", [B("g01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "생각했음")]),
    ]
    build(S, lines, "약물운전 1위는", "마약이 아니라 수면제", "국과수 분석 1046건 중 졸피뎀 370건",
          "#약물운전 1위 수면제", "도로교통법 제148조의2 개정(2026-04-02 시행) + 국과수 약물운전 분석(디지털데일리 2026-04-05, 경향신문 2026-05-21)",
          [("국과수 2023~2025 약물운전 의뢰 1,046건, 졸피뎀 370 / 알프라졸람 144 / 플루니트라제팜 126", "디지털데일리, 경향신문 교차"),
           ("의료용 마약류 55%, 비마약류 41%, 불법 마약류 4%", "디지털데일리, 경향신문"),
           ("2026.4.2부터 약물운전 5년 이하 징역 또는 2천만원 이하 벌금", "제148조의2 제5항, KTV, 정책브리핑"),
           ("음주 0.2% 이상 2~5년 징역 또는 1천만~2천만원(최고형 같음)", "제148조의2 제3항 제1호"),
           ("약물 측정 불응죄 신설 5년/2천만원, 타액 간이시약검사", "제148조의2 제6항, 제45조 제2항, 시행규칙 제28조의2"),
           ("처벌 대상은 '정상 운전이 곤란한 상태에서 운전'", "제45조 제1항 문구, 경찰 설명"),
           ("대사 2줄", "상황 예시(창작)")],
          "약물운전으로 가장 많이 걸린 건 마약이 아니라 수면제 졸피뎀이었습니다.\n올해 4월부터 약물운전과 약물검사 거부 모두 5년 이하 징역 또는 2천만원 이하 벌금입니다.\n님들은 수면제 먹은 다음 날 운전, 괜찮다고 생각하셨나요?\n\n#약물운전 #도로교통법 #수면제 #자동차 #란빵",
          "님들은 수면제 먹은 다음 날 운전, 괜찮다고 생각했음?",
          "차량용 목베개, 졸음방지 껌, 자동차 블랙박스 2채널, 차량용 공기청정기, 차량용 방향제",
          "감기약 운전 처벌 여부는 확인 안 돼 대본에 안 넣음.", [B("g02", s0=1.0, s1=1.1)], typ="란빵 자동차, 교통법")


def EP_pedalguard():
    S = "pedalguard"
    lines = [
        L("브레이크 밟았다니까요! 차가 혼자 튀어나갔어요!",
          [B("p01", "Low close-up of a car driver footwell showing the accelerator and brake pedals, a foot-shaped shadow, dim interior light", s0=1.1, s1=1.3)],
          C("drv_shock", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("2024년 시청역 역주행 사고, 대법원 결론은 급발진이 아니라 운전자 과실이었음.",
          [B("p02", "An empty Korean supreme court courtroom with wooden benches and a judge's bench, soft daylight, no people")],
          C("judge", "r"), say="이천이십사년 시청역 역주행 사고, 대법원 결론은 급발진이 아니라 운전자 과실이었음.", em=["운전자 과실"],
          em_color="yellow", fx=[("hit_trailer_epic", "운전자", 0.45)]),
        L("가속페달은 끝까지 밟혀 있었고, 브레이크 밟은 흔적은 없었음.",
          [B("p01", at="끝까지", s0=1.4, s1=1.6, fx=0.4, fy=0.6, punch=True)], C("biz_shock"), em=["흔적은 없었음"],
          pop=("브레이크 0", R, "없었음"), shake="없었음", fx=[("wrong_gameshow_buzz", "없었음", 0.45)]),
        L("그래서 나온 게 페달 오조작 방지장치.",
          [B("p03", "A small black aftermarket electronic module with a cable connector installed under a car dashboard near the pedals, close-up, workshop light")],
          C("biz_idea"), em=["페달 오조작 방지장치"], em_color="yellow", fx=[("correct_ding", "방지장치", 0.5)]),
        L("8월 27일부터 인증 기준이 생겨서, 타던 차에도 합법으로 달 수 있음.",
          [B("p04", "A clean Korean car service bay with a hatchback car inside, hood closed, a technician's tablet on a stand, no people")],
          C("seibishi", "r"), say="팔월 이십칠일부터 인증 기준이 생겨서, 타던 차에도 합법으로 달 수 있음.", em=["타던 차에도"]),
        L("시속 30킬로 안쪽에서 가속페달을 순식간에 끝까지 밟으면,",
          [B("p01", s0=1.0, s1=1.15)], C("drv_surprise"), say="시속 삼십킬로 안쪽에서 가속페달을 순식간에 끝까지 밟으면,",
          em=["순식간에"]),
        L("차가 알아서 속도를 30% 넘게 줄여줌.",
          [B("p03", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("biz_idea"), say="차가 알아서 속도를 삼십퍼센트 넘게 줄여줌.",
          em=["30% 넘게"], em_color="yellow",
          info={"kind": "counter", "at": "30%", "title": "오조작 감지 시 감속", "items": [{"num": 30, "suffix": "% 이상", "label": "시속 30km 이내", "at": "30%"}]}),
        L("단, 인증 안 받은 장치를 달면 불법튜닝, 1년 이하 징역이나 1천만원 이하 벌금.",
          [B("p03", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("police_angry", "r"),
          say="단, 인증 안 받은 장치를 달면 불법튜닝, 일년 이하 징역이나 천마넌 이하 벌금.", em=["불법튜닝"], em_color="yellow",
          fx=[("scratch_vinyl", "불법튜닝", 0.5)]),
        L("2029년부터 나오는 새 승용차엔 아예 의무로 들어감.",
          [B("p05", "Rows of brand-new compact cars in a factory final inspection line under bright lights, no logos, no people")],
          C("dealer"), say="이천이십구년부터 나오는 새 승용차엔 아예 의무로 들어감.", em=["의무"], em_color="yellow"),
        L("올해는 65세 넘은 택시랑 소형 화물차 기사한테 설치비도 지원 중.",
          [B("p04", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("taxi", "r"), say="올해는 육십오세 넘은 택시랑 소형 화물차 기사한테 설치비도 지원 중.",
          em=["설치비"]),
        L("님들은 내 차에 이 장치 달 생각 있음?", [B("p01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "있음")]),
    ]
    build(S, lines, "급발진이라더니", "이제 장치로 막는다", "페달 오조작 방지장치 인증 기준 시행",
          "#급발진 막는 장치 합법", "국토부 페달 오조작 방지장치 튜닝부품 인증기준 2026-08-27 시행 + 대법원 2025도13707",
          [("시청역 역주행 사고 대법원 2025.12.4 선고 2025도13707 금고 5년 확정, 급발진 아닌 운전자 과실", "헤럴드경제, 한국경제 교차"),
           ("국과수: 가속페달 끝까지 밟힘, 브레이크 작동 흔적 없음", "헤럴드경제, 한국경제"),
           ("2026.8.27 인증기준 시행, 기존 운행차 설치 가능", "국토부 보도자료"),
           ("정지 또는 30km/h 이내 오조작 감지 시 30% 이상 감속", "국토부 보도자료"),
           ("인증 없는 장치 = 불법튜닝, 1년 이하 징역 또는 1천만원 이하 벌금", "국토부 보도자료, 자동차관리법 제81조 제19호"),
           ("2029.1.1 이후 제작, 수입 승용차 의무화", "국토부 2025.10.23 입법예고, 정책브리핑"),
           ("2026 보급사업 만 65세 이상 택시, 1.4톤 이하 화물 3,260대 설치비 지원", "정책브리핑 2026-02-10"),
           ("첫 줄 대사", "상황 예시(창작)")],
          "급발진이라는 주장이 많지만 시청역 역주행 사고의 대법원 결론은 운전자 과실이었습니다.\n8월 27일부터 페달 오조작 방지장치 인증 기준이 생겨 타던 차에도 합법으로 달 수 있고, 2029년부터 새 승용차엔 의무입니다.\n님들은 이 장치 다실 건가요?\n\n#급발진 #페달오조작 #자동차관리법 #자동차 #란빵",
          "님들은 내 차에 이 장치 달 생각 있음?",
          "자동차 블랙박스 2채널, 페달 블랙박스, 블랙박스 메모리카드, 차량용 발판 매트, 운전화",
          "희생자 수 등 사고 피해 묘사는 넣지 않음.", [B("p05", s0=1.0, s1=1.1)], typ="란빵 자동차, 교통법")


def EP_licrenew():
    S = "licrenew"
    lines = [
        L("면허 조회해 보니까 취소로 뜨는데요?",
          [B("l01", "A Korean driver's license card lying on the dashboard of a police patrol car at night next to a handheld terminal, text unreadable", s0=1.1, s1=1.3)],
          C("police", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("면허 갱신 기간이 올해부터 연말까지가 아니라 생일 기준으로 바뀌었음.",
          [B("l02", "A desk calendar with a birthday date circled in red, a driver's license card beside it, warm morning light, text unreadable")],
          C("biz_surprise"), em=["생일 기준"], em_color="yellow", fx=[("hit_trailer_epic", "생일", 0.45)]),
        L("갱신하는 해의 생일 앞뒤로 6개월씩, 딱 1년임.",
          [B("l02", at="앞뒤로", s0=1.4, s1=1.6, fx=0.45, fy=0.5, punch=True)], C("biz_idea"),
          say="갱신하는 해의 생일 앞뒤로 육개월씩, 딱 일년임.", em=["6개월씩"],
          info={"kind": "compare", "at": "앞뒤로", "title": "면허 갱신 기간", "items": [
              {"label": "예전", "color": W, "at": "갱신하는", "rows": [["기간", "1월~12월", W]]},
              {"label": "올해부터", "color": Y, "at": "앞뒤로", "rows": [["기간", "생일 앞뒤 6개월", Y]]}]}),
        L("예를 들어 4월 17일생이면, 작년 10월 17일부터 올해 10월 17일까지였음.",
          [B("l03", "A wall calendar turned to October with one date crossed out, a car key on a hook, evening light, numbers unreadable")],
          C("drv_shock"), say="예를 들어 사월 십칠일생이면, 작년 시월 십칠일부터 올해 시월 십칠일까지였음.", em=["10월 17일"], em_color="yellow",
          pop=("이미 지남?!", R, "까지였음"), fx=[("scratch_vinyl", "까지였음", 0.5)]),
        L("갱신 안 하면 과태료 2만원, 적성검사 안 받으면 3만원.",
          [B("l04", "A fine notice envelope on a doormat in front of an apartment door, text unreadable")],
          C("bill_shock"), say="갱신 안 하면 과태료 이마넌, 적성검사 안 받으면 삼마넌.", em=["3만원"]),
        L("근데 진짜 무서운 건 1종 면허.",
          [B("l01", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("shinpai"), say="근데 진짜 무서운 건 일종 면허.", em=["1종"], em_color="yellow",
          fx=[("drum_rimshot", "무서운", 0.4)]),
        L("적성검사 기간 끝나고 1년 넘게 안 받으면 면허가 취소됨.",
          [B("l01", at="취소됨", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)], C("ohagya"),
          say="적성검사 기간 끝나고 일년 넘게 안 받으면 면허가 취소됨.", em=["취소됨"], em_color="yellow",
          pop=("면허 취소!!", R, "취소됨"), shake="취소됨", fx=[("boom_zoom_impact", "취소됨", 0.55)]),
        L("네? 저 사고 한 번도 안 냈는데요?",
          [B("l03", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("drv_q", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("2종도 70세가 넘으면 적성검사 대상이라 똑같이 챙겨야 함.",
          [B("l04", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("shinpai"), say="이종도 칠십세가 넘으면 적성검사 대상이라 똑같이 챙겨야 함.", em=["70세"]),
        L("님들은 내 면허 갱신 언제인지 앎?", [B("l02", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "앎")]),
    ]
    build(S, lines, "면허 갱신 기간", "이제 생일이 기준", "2026년부터 생일 앞뒤 6개월",
          "#면허 갱신 생일 기준", "도로교통법 제87조 개정(2025-08-14), 시행 2026-01-01 (경찰청, KTV, 세계일보 2026-01-12)",
          [("갱신기간 = 해당 연도 생일 전후 각 6개월", "도로교통법 제87조 제1항, KTV 카드뉴스, 경찰청 보조자료"),
           ("예시 4월 17일생 → 2025.10.17~2026.10.17", "경찰청 보조자료 예시(1975.4.17생)"),
           ("개정 후 첫 갱신자는 종전 기간(1.1~12.31)도 인정", "도로교통공단 발표(세계일보 2026-01-12, 부칙 원문 확인 안 됨). 대본에서는 '이미 지남' 팝만, 첫 갱신 특례 언급 없음"),
           ("갱신 미이행 과태료 2만원, 정기 적성검사 미이행 3만원", "시행령 별표 6"),
           ("적성검사 기간 만료 후 1년 초과 시 면허 취소", "제93조 제1항 제9호, 시행규칙 별표 28"),
           ("정기 적성검사 대상 1종 전원, 2종은 70세 이상", "제87조 제2항"),
           ("대사 2줄", "상황 예시(창작)")],
          "운전면허 갱신 기간이 올해부터 연말이 아니라 생일 앞뒤 6개월로 바뀌었습니다.\n1종이나 70세 넘은 2종은 적성검사를 1년 넘게 안 받으면 면허가 취소됩니다.\n님들은 내 갱신 기간 알고 계신가요?\n\n#운전면허 #면허갱신 #도로교통법 #자동차 #란빵",
          "님들은 내 면허 갱신 언제인지 앎?",
          "운전면허증 케이스, 차량용 서류 보관함, 자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 차량용 방향제",
          "첫 갱신자 특례는 부칙 원문 미확인이라 '4월 17일생 예시'를 경찰청 예시 그대로만 씀.", [B("l04", s0=1.0, s1=1.1)], typ="란빵 자동차, 교통법")


def EP_yellowlight():
    S = "yellowlight"
    lines = [
        L("노란불에 서면 뒤차가 박잖아요!",
          [B("n01", "Driver's view approaching a Korean city intersection at night, the traffic light just turned yellow, white stop line very close ahead, motion blur", s0=1.1, s1=1.3)],
          C("drv_angry", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("정지선 8미터 앞에서 신호가 노란불로 바뀜.",
          [B("n01", at="8미터", s0=1.4, s1=1.6, fx=0.5, fy=0.4, punch=True)], C("drv_surprise"), say="정지선 팔미터 앞에서 신호가 노란불로 바뀜.",
          em=["8미터"], em_color="yellow", fx=[("hit_trailer_epic", "노란불로", 0.45)]),
        L("제한 40인 길을 61킬로로 달려서,",
          [B("n02", "Close-up of a car speedometer needle at about 60 km/h at night, dashboard lights, blurred road through the windshield")],
          C("drv_surprise"), say="제한 사십인 길을 육십일킬로로 달려서,", em=["61킬로"]),
        L("급브레이크를 밟아도 30미터 넘게 밀리는 거리였음.",
          [B("n02", s0=1.3, s1=1.5, fx=0.5, fy=0.5)],
          C("drv_shock"), say="급브레이크를 밟아도 삼십미터 넘게 밀리는 거리였음.", em=["30미터"],
          info={"kind": "compare", "at": "급브레이크를", "title": "멈출 수 있었나", "items": [
              {"label": "정지선까지", "color": Y, "at": "급브레이크를", "rows": [["거리", "약 8m", Y]]},
              {"label": "정지거리", "color": R, "at": "30미터", "rows": [["거리", "30m 넘음", R]]}]}),
        L("그대로 지나가다 교차로 안에서 오토바이랑 부딪힘.",
          [B("n03", "A fallen delivery motorcycle on its side in the middle of a city intersection at night, a car stopped nearby with hazard lights, no people visible")],
          C("jiko_man"), em=["오토바이"], shake="부딪힘", fx=[("glass_smash", "부딪힘", 0.35)]),
        L("1심이랑 2심은 못 서는 거리였다며 무죄.",
          [B("n04", "An empty Korean courtroom with wooden benches, soft daylight, no people")],
          C("banzai"), say="일심이랑 이심은 못 서는 거리였다며 무죄.", em=["무죄"], em_color="yellow"),
        L("근데 대법원은 신호위반이라고 뒤집음.",
          [B("n04", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], C("judge", "r"), em=["신호위반"], em_color="yellow",
          pop=("유죄 취지!!", R, "뒤집음"), shake="뒤집음", fx=[("boom_zoom_impact", "뒤집음", 0.55)]),
        L("교차로 들어가기 전에 노란불이 켜지면, 멈출 수 있든 없든 서야 한다는 거.",
          [B("n01", s0=1.0, s1=1.15)], C("lawyer"), em=["멈출 수 있든 없든"],
          info={"kind": "quotes", "title": "대법원 2024도1195", "items": [{"text": "정지거리가 더 길어도", "at": "교차로"}, {"text": "교차로 직전 안 서면", "at": "멈출"}, {"text": "신호위반", "at": "서야"}]}),
        L("현장 단속이면 범칙금 6만원에 벌점 15점.",
          [B("n05", "A traffic ticket book and a pen on the hood of a police car at night, flashing lights reflected, text unreadable")],
          C("police", "r"), say="현장 단속이면 범칙금 육마넌에 벌점 십오점.", em=["벌점 15점"]),
        L("사람이 다치면 12대 중과실이라 종합보험이 있어도 형사처벌될 수 있음.",
          [B("n05", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_shock"), say="사람이 다치면 십이대 중과실이라 종합보험이 있어도 형사처벌될 수 있음.",
          em=["12대 중과실"], em_color="yellow", fx=[("scratch_vinyl", "종합보험이", 0.45)]),
        L("님들은 노란불 보이면 무조건 섬?", [B("n01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "섬")]),
    ]
    build(S, lines, "못 서는 거리의 노란불", "대법원은 신호위반", "정지선 8m 앞 황색신호, 대법원 2024도1195",
          "#노란불 못 서도 위반", "대법원 2024.4.12 선고 2024도1195 (세계일보 2024-05-13, 매일신문 2026-10-15, 로톡)",
          [("2021.7.25 부천IC 인근 교차로, 제한 40km/h 도로 61.51km/h, 황색 시 정지선까지 약 8.3m, 정지거리 30.72~35.85m", "세계일보, 매일신문, 로톡 판례 정리"),
           ("교차로 안에서 오토바이와 충돌", "같은 출처"),
           ("1, 2심 무죄 → 대법원 파기환송(신호위반)", "대법원 2024도1195"),
           ("진입 전 황색이면 정지거리가 더 길어도 교차로 직전 정지 안 하면 신호위반", "대법원 2024도1195 요지"),
           ("신호위반 범칙금 승용 6만원, 벌점 15점(카메라 과태료는 7만원)", "시행령 별표 8, 별표 6, 시행규칙 별표 28"),
           ("신호위반 사고 = 교특법 12대 중과실, 종합보험 있어도 형사처벌 가능", "교통사고처리 특례법 제3조 제2항 제1호"),
           ("첫 줄 대사", "상황 예시(창작)")],
          "정지선 8m 앞에서 바뀐 노란불, 급브레이크를 밟아도 못 서는 거리였는데 대법원은 신호위반이라고 봤습니다.\n교차로 진입 전 황색이면 멈출 수 있든 없든 서야 한다는 판단입니다.\n님들은 노란불 보이면 무조건 서시나요?\n\n#노란불 #신호위반 #대법원 #도로교통법 #란빵",
          "님들은 노란불 보이면 무조건 섬?",
          "자동차 블랙박스 2채널, 블랙박스 메모리카드, 후방 블랙박스, 차량용 핸드폰 거치대, 차량용 방향제",
          "", [B("n02", s0=1.0, s1=1.1)], typ="란빵 자동차, 교통법")


if __name__ == "__main__":
    for name in sys.argv[1:] or [k[3:] for k in list(globals()) if k.startswith("EP_")]:
        globals()["EP_" + name]()
