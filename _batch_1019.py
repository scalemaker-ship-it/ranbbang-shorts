#!/usr/bin/env python3
"""란빵 2026-10-19: 사용자 지정 인스타 릴스 → 1편.
- fingerled: 차량용 LED 손가락 표시기(instagram.com/reel/DenJlGdCSIv, @the.flipbuddy 10/17, 좋아요 14만).
  릴스 11초를 4컷(unbox/glow/hwy/night)으로 잘라 1080x960, 위쪽 영어 문구는 크롭으로 뺌.
  법 근거 = 국가법령정보센터 원문 확인: 도로교통법 제42조 1항, 시행령 제27조 2호(욕설 표시, 혐오감 주는 그림ㆍ기호), 제154조 1호(30만원 이하 벌금이나 구류).
  모욕죄는 성립요건(특정성 등) 논란이 있어 대본에서 뺌.
helper(crop/P/L/build)는 _batch_1018.py 머리 부분을 그대로 씀.
"""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(ROOT, "_batch_1018.py")).read()
exec(_src[:_src.index("# ───────────── byddahan")])


def V(name, credit, at=None, s0=1.0, s1=1.08, fx=0.5, fy=0.5, punch=False, ss=0):
    d = {"vid": f"vid/{name}.mp4", "s0": s0, "s1": s1, "fx": fx, "fy": fy, "credit": credit}
    if at: d["at"] = at
    if punch: d["punch"] = True
    if ss: d["ss"] = ss
    return d


S = "fingerled"
CV = "영상: @the.flipbuddy"
rd = os.path.join(ROOT, "work", S, "v2", "real")
os.makedirs(rd, exist_ok=True)
os.system(f"ffmpeg -v error -y -ss 2.5 -i {ROOT}/work/{S}/v2/vid/night.mp4 -frames:v 1 -q:v 2 {rd}/outro.jpg")

lines = [
    L("와, 앞차 뒷유리에 이게 뜬다고?", [V("night", CV, ss=1.2, s0=1.1, s1=1.25, fx=0.45, fy=0.45)],
      dialogue=True, speaker=3, emotion="toneup"),
    L("요즘 미국에서 난리 난 차량용 LED 손가락 표시기임.",
      [V("unbox", CV), V("glow", CV, "LED", s0=1.0, s1=1.12, punch=True)],
      say="요즘 미국에서 난리 난 차량용 엘이디 손가락 표시기임.", em=["LED 손가락"], em_color="yellow",
      fx=[("hit_trailer_epic", "LED", 0.5)]),
    L("원래 영상 제목이 어른 돈으로 산 최고의 물건이래요ㅋㅋ", [V("glow", CV, ss=0.6, s0=1.15, s1=1.0)],
      say="원래 영상 제목이 어른 돈으로 산 최고의 물건이래요ㅋㅋ", em=["최고의 물건"]),
    L("빗길 고속도로에서 차 한 대가 앞으로 쑥 끼어들더니", [V("hwy", CV, s0=1.0, s1=1.1)],
      em=["끼어들더니"]),
    L("뒷유리에 가운데 손가락이 번쩍 켜짐.", [V("hwy", CV, ss=2.2, s0=1.1, s1=1.35, fx=0.55, fy=0.35, punch=True)],
      em=["번쩍"], em_color="yellow", fx=[("boom_zoom_impact", "번쩍", 0.5)], shake="번쩍"),
    L("밤에 신호 대기하다 켰더니 옆 차 운전자가 창문 밖으로 몸을 내밀어 버림.",
      [V("night", CV), V("night", CV, "옆", ss=1.7, s0=1.2, s1=1.4, fx=0.3, fy=0.5)],
      em=["몸을 내밀어"], fx=[("wrong_gameshow_buzz", "내밀어", 0.4)]),
    L("아니 이거 바로 싸움 나는 거 아님?", [V("night", CV, ss=2.4, s0=1.5, s1=1.7, fx=0.25, fy=0.45, punch=True)],
      dialogue=True, speaker=2, emotion="toneup"),
    L("근데 한국에서 이거 달고 다니면 바로 처벌 대상임.", [V("glow", CV, s0=1.0, s1=1.15)],
      em=["처벌 대상"], em_color="yellow", fx=[("drop_futuristic", "처벌", 0.5)], pop=("불법!", R, "처벌")),
    L("도로교통법상 욕설이나 혐오감 주는 그림, 기호를 차에 표시하면 안 되거든.",
      [V("hwy", CV, ss=2.6, s0=1.3, s1=1.15, fx=0.55, fy=0.35)], em=["혐오감"]),
    L("걸리면 30만원 이하 벌금이나 구류까지 받을 수 있음.", [V("glow", CV, ss=0.3, s0=1.2, s1=1.35, punch=True)],
      say="걸리면 삼십마넌 이하 벌금이나 구류까지 받을 수 있음.", em=["30만원"], em_color="yellow",
      fx=[("cash_register_fake", "30만원", 0.5)],
      info={"kind": "counter", "at": "30만원", "title": "도로교통법 제154조",
            "items": [{"num": 30, "suffix": "만원 이하", "label": "벌금 또는 구류", "at": "30만원"}]}),
    L("님들은 앞차에 이거 뜨면 어떻게 함?", [V("night", CV, ss=1.0, s0=1.0, s1=1.12)], fx=[("pop_bubble", "함")]),
]
build(S, lines, "앞차 뒷유리에 이게 뜨면", "한국에선 바로 벌금", "미국 유행 차량용 LED 손가락",
      "#앞차 손가락 LED", "인스타 릴스 @the.flipbuddy 2026-10-17 (instagram.com/reel/DenJlGdCSIv)",
      [("차량 뒷유리용 LED 손가락 표시기, 원본 문구 'The best thing I've bought with my adult money'", "원본 릴스 화면"),
       ("고속도로 끼어든 차 뒷유리에 손가락 점등, 밤 신호대기 중 옆 차 운전자 몸 내밈", "원본 릴스 화면"),
       ("욕설, 혐오감 주는 그림ㆍ기호를 한 자동차 운전 금지", "도로교통법 제42조 1항, 시행령 제27조 2호(국가법령정보센터)"),
       ("위반 시 30만원 이하 벌금이나 구류", "도로교통법 제154조 1호(국가법령정보센터)")],
      "앞차 뒷유리에 가운데 손가락이 뜨면? 미국에서 유행하는 차량용 LED 손가락 표시기, 한국에선 도로교통법 위반입니다.\n\n#자동차 #운전 #도로교통법 #LED #란빵",
      "님들은 앞차에 이거 뜨면 어떻게 함?",
      "없음 (불법 용품이라 쇼핑태그 안 붙임)",
      "원본 영상 출처: @the.flipbuddy 인스타 릴스. 화면에 출처 표기.", "outro", CV)
