#!/usr/bin/env python3
"""란빵 2026-10-03 신차 2편 (네이버 블로그 소재) — 실사만 사용(공식 사이트·커먼즈 CC) + 출처 번인.
scout16: 스카우트 트래블러(폭스바겐) 16만 명 대기 / glc9000: 벤츠 전기 GLC 9천만 원 사전계약 2천 대
script.json / upload.md / img/NN.png 생성 (prompts.tsv 없음 = 생성 이미지 0)."""
import json, os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos")
FONT = "/Users/kimyiseul/Desktop/kim/ssul/fonts/Pretendard-SemiBold.ttf"
OUTRO = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}
SC = "사진: Scout Motors"
A93 = "사진: Alexander-93 / Wikimedia Commons, CC BY-SA 4.0"
AMG = "사진: Alexander Migl / Wikimedia Commons, CC BY-SA 4.0"

def L(text, img, sfx=None, em=None, yellow=False, dlg=None, emo=None):
    d = {"text": text, "img": img}
    if em: d["em"] = [em]
    if yellow: d["em_color"] = "yellow"
    if sfx: d["sfx"] = sfx
    if dlg:
        d["dialogue"] = True
        if dlg == "sub2": d["voice"] = "sub2"
        d["emotion"] = emo or "angry"; d["intensity"] = 2.0
    return d

def P(rel, credit, anchor=0.5): return (rel, credit, anchor)
def S(n, a=0.5): return P(f"scout/{n}.jpg", SC, a)
def G(n, a=0.5): return P(f"glc/{n}.jpg", A93 if n in ("08","09","11","13","14","15","17","18","29","30") else AMG, a)

EP = {}
EP["scout16"] = dict(
 t1='GV90보다 큰 SUV가', t2='6천만 원대라고?',
 hook='GV90보다 큰 전기 SUV가 6천만 원대, 16만 명이 줄 섰음', bar='GV90보다 크다는 6천만 원대 SUV, 벌써 16만 명 대기',
 kw='#스카우트트래블러', tags='#shorts #스카우트트래블러 #폭스바겐 #전기SUV #신차',
 shop='2채널 블랙박스, 차량용 핸드폰 거치대, 차량용 방향제, 차량용 무선청소기, 트렁크 정리함',
 comment='님들은 이 덩치가 6천만 원대면 사겠음?',
 src='네이버 블로그 곰도라 2026-09-08 "이게 6천만원? GV90보다 크다 16만명 줄선 SUV"(https://blog.naver.com/gdora/224405035034) — 스카우트 트래블러 미국가 약 7,730만 원·전기차 혜택 포함 실구매 6천만 원 중후반 분석, 대기 16만 명+, 전장 5,281mm(스페어 캐리어 포함)/4,849mm(제외), 사다리꼴 프레임·지상고 30cm+·도하 90cm, 가속 3.5초대·견인 3.1톤+, 물리 버튼·토글, 예약자 87% EREV 하베스터(전기 563km·합산 805km), 차폭 2,029mm(미러 포함 2,326mm)·전고 1,938mm, 양산 2027년 ; 사진 scoutmotors.com 공식 사이트',
 desc='폭스바겐 산하 스카우트 모터스의 전기 SUV 트래블러, 미국 시작가 약 7,730만 원에 전기차 혜택을 더하면 6천만 원 중후반 실구매가 분석이 나오면서 예약 대기만 16만 명을 넘겼음.\n스페어타이어 포함 전장 5,281mm, 사다리꼴 프레임, 지상고 30cm 이상, 도하 90cm의 정통 오프로더 구성에 예약자 87%가 주행거리 연장형 하베스터(전기 563km·합산 805km)를 선택함.\n차폭 2m 이상, 양산 2027년이라 국내 출시는 아직 미정임.',
 lines=[
  L("GV90보다 큰 전기 SUV가 6천만 원대, 벌써 16만 명이 줄 섰음.",1),
  L("폭스바겐이 되살린 미국 브랜드, 스카우트 트래블러임.",2,"ding",em="스카우트 트래블러"),
  L("미국 시작가가 우리 돈으로 약 7,730만 원인데,",3,"tick"),
  L("전기차 혜택까지 더하면 실구매가 6천만 원 중후반까지 본다는 분석임.",4,"cash",em="6천만 원",yellow=True),
  L("같은 5.3미터급인 타호나 유콘이 9천만 원부터니까 확실히 싸긴 함.",5,"pop",em="9천만 원"),
  L("근데 전장 5,281mm는 뒤에 달린 스페어타이어까지 잰 거임.",6,"thud",em="스페어타이어"),
  L("그거 빼면 4,849mm라 싼타페랑 비슷해짐.",7,"tick",em="싼타페"),
  L("그래도 사다리꼴 프레임에 지상고 30cm, 물도 90cm 깊이까지 건너는 정통 오프로더임.",8,"whoosh",em="정통 오프로더"),
  L("제로백은 3.5초대고 견인은 3.1톤 넘게 끌음.",9,"eng",em="3.5초",yellow=True),
  L("실내는 장갑 끼고도 누르라고 큼직한 물리 버튼이랑 토글 스위치를 남겨놨음.",10,"pop",em="물리 버튼"),
  L("근데 전기차 사면서 왜 87%가 기름 넣는 걸 골랐대?!",11,"boing",dlg="sub2"),
  L("주행거리 연장형 하베스터가 전기로 563km, 기름까지 더하면 805km를 감.",12,"ding",em="805km",yellow=True),
  L("문제는 폭이 2m, 미러 포함 2.3m라 국내 주차장에선 좀 벅찰 수 있음.",13,"thud",em="2.3m"),
  L("양산이 2027년이라 국내 출시는 아직 멀었음.",14,"tick"),
  L("님들은 이 덩치가 6천만 원대면 사겠음?",15),
  OUTRO],
 imgs=[S("05"), S("12"), S("16"), S("33"), S("27"), S("32",0.7), S("16",0.3), S("33",0.3),
       S("05",0.3), S("02"), S("12",0.7), S("27",0.3), S("16",0.7), S("26"), S("05",0.6)])

EP["glc9000"] = dict(
 t1='9천만 원 벤츠 전기 SUV', t2='벌써 2천 명 줄섰다',
 hook='제네시스 잡겠다는 9천만 원 벤츠 전기 SUV, 벌써 2천 명 넘게 계약함', bar='9천만 원 전기 GLC, 사전계약 2천 대 넘었다',
 kw='#전기GLC', tags='#shorts #전기GLC #벤츠 #전기SUV #신차',
 shop='전기차 충전 케이블, 차량용 핸드폰 거치대, 2채널 블랙박스, 차량용 방향제, 차량용 햇빛가리개',
 comment='님들은 9천만 원이면 제네시스 대신 이거 가겠음?',
 src='네이버 블로그 로드로그 "벌써 2,000명 줄 섰어요 제네시스 잡겠다 한국 왔다는 9천만 원 SUV"(https://blog.naver.com/roadlog_99/224428647678) — 벤츠 디 올-뉴 일렉트릭 GLC 국내 인증 상온 448km(도심 467·고속 424)/저온 395km(도심 378·고속 415), 유지율 88.2%, 800V·최대 330kW·10→80% 약 22분, 310kW 4MATIC, MB.OS, 가격 AMG 라인 9,000만 원·AMG 라인+ 9,480만 원, 사전계약 2천 대 초과(3천 대 근접), 인도 2026년 4분기 ; 비교가 볼보 ES90 7,294만 원·BMW iX3 7,990만 원(같은 블로그 연관글) ; 사진 Wikimedia Commons CC BY-SA 4.0',
 desc='메르세데스-벤츠 디 올 뉴 일렉트릭 GLC 국내 가격이 AMG 라인 9,000만 원, AMG 라인 플러스 9,480만 원으로 나왔고 사전계약은 2천 대를 넘어 3천 대에 가까워지고 있음.\n국내 인증 주행거리는 상온 448km, 저온 395km로 유지율 약 88%, 800V 시스템에 최대 330kW 충전으로 10%에서 80%까지 약 22분.\n최고출력 310kW 사륜구동, MB.OS 적용, 고객 인도는 2026년 4분기 예정임.',
 lines=[
  L("9천만 원짜리 벤츠 전기 SUV에 벌써 2천 명 넘게 줄 섰음.",1),
  L("국내 출시 앞둔 디 올 뉴 일렉트릭 GLC임.",2,"ding",em="일렉트릭 GLC"),
  L("가격은 AMG 라인 9,000만 원, AMG 라인 플러스 9,480만 원 두 가지임.",3,"cash",em="9,000만 원",yellow=True),
  L("전기 SUV 고를 때 제일 궁금한 거, 겨울에 얼마나 줄어드냐임.",4,"tick",em="겨울"),
  L("국내 인증 주행거리가 상온 448km, 저온 395km임.",5,"pop",em="395km",yellow=True),
  L("53km 줄어드는 건데, 상온 대비 88% 유지라 전기차 중엔 괜찮은 편임.",6,"ding",em="88%"),
  L("근데 세부로 보면 저온 도심은 378km로 떨어지고, 고속도로는 415km로 오히려 김.",7,"thud",em="378km"),
  L("그래서 충전은?!",8,"boing",dlg="sub2"),
  L("800V 시스템에 최대 330kW, 10%에서 80%까지 약 22분이면 채움.",9,"whoosh",em="22분",yellow=True),
  L("최고출력 310kW 사륜구동에 새 운영체제 MB.OS도 들어감.",10,"eng",em="310kW"),
  L("사전계약은 3천 대에 가까워지고 있고, 인도는 올해 4분기부터임.",11,"pop",em="3천 대"),
  L("볼보 ES90이 7,294만 원, BMW iX3가 7,990만 원이라 벤츠가 제일 비싼 건 맞음.",12,"thud",em="제일 비싼"),
  L("님들은 9천만 원이면 제네시스 대신 이거 가겠음?",13),
  OUTRO],
 imgs=[G("17"), G("13"), G("25"), G("19"), G("27"), G("11"), G("23"), G("08"), G("09"), G("15"), G("18",0.4), G("29"), G("14")])

def burn(src, dst, credit, anchor, first=False):
    im = Image.open(os.path.join(PH, src)).convert("RGB")
    tw, th = 1280, 800
    w, h = im.size; s = max(tw / w, th / h)
    im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    W, H = im.size
    left = int((W - tw) * anchor); top = (H - th) // 2
    im = im.crop((left, top, left + tw, top + th)).convert("RGBA")
    f = ImageFont.truetype(FONT, 26)
    bb = ImageDraw.Draw(im).textbbox((0, 0), credit, font=f)
    tw2, th2 = bb[2] - bb[0], bb[3] - bb[1]
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    x1 = 1157 - 16; y0 = 118 if first else 18
    x0, y1 = x1 - tw2 - 24, y0 + th2 + 18
    d.rectangle([x0, y0, x1, y1], fill=(0, 0, 0, 150))
    d.text((x0 + 12, y0 + 9 - bb[1]), credit, font=f, fill=(255, 255, 255, 235))
    Image.alpha_composite(im, ov).convert("RGB").save(dst)

for slug, e in EP.items():
    wd = os.path.join(ROOT, "work", slug); os.makedirs(os.path.join(wd, "img"), exist_ok=True)
    nimg = max(l.get("img", 0) for l in e["lines"])
    assert nimg == len(e["imgs"]), (slug, nimg, len(e["imgs"]))
    for i, (rel, credit, anchor) in enumerate(e["imgs"], 1):
        burn(rel, os.path.join(wd, "img", f"{i:02d}.png"), credit, anchor, first=(i == 1))
    open(os.path.join(wd, "prompts.tsv"), "w").write("")
    sj = {"slug": slug, "type": "D형 (뉴스) — 란빵 자동차 이슈", "source": e["src"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["hook"], "channel": "란빵",
          "voice": "taesub", "style": {"sub_box": True, "bar": e["bar"], "watermark": ""},
          "lines": e["lines"]}
    json.dump(sj, open(os.path.join(wd, "script.json"), "w"), ensure_ascii=False, indent=2)
    title = f"{e['kw']} {e['hook']}"; assert len(title) <= 100
    up = (f"# {slug} — 업로드 메타\n\n## 제목\n\n{title}\n\n## 설명\n\n{e['desc']}\n\n{e['tags']}\n\n"
          f"## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop']}\n\n## 근거\n\n{e['src']}\n")
    open(os.path.join(wd, "upload.md"), "w").write(up)
    print(f"{slug:9s} lines={len(e['lines'])} imgs={nimg} title={len(title)}")
