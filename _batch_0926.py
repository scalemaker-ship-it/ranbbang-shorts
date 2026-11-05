#!/usr/bin/env python3
"""란빵 개드립 자동차 4편 (2026-09-26) — script.json / prompts.tsv / upload.md / jobs.tsv 생성.
이미지: 로컬 SDXL. 원글 사진 중 얼굴 없는 것(충전기 앱 화면·벤츠 주차 사진)은 `ORIG` 로 직접 크롭해 쓴다(ssul/prd.md §5 예외)."""
import json, os
from PIL import Image, ImageFilter
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = "/private/tmp/claude-501/-Users-kimyiseul-Desktop-kim-shorts/e3032796-0001-4b3c-b9c3-896be7c56c6c/scratchpad/src"
T = ("photorealistic DSLR photograph, 35mm lens, natural available light, shallow depth of field, "
     "Korean setting, no text no letters no signage no logos no brand marks no watermark")
W1 = "a Korean woman in her early 30s, shoulder-length dark brown hair, natural light makeup"
M1 = "a Korean man in his early 30s, short black hair, clean-shaven, slim build"
M2 = "a Korean man in his mid 30s, short wavy black hair, light stubble, sturdy build"
OUTRO = {"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True}

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

EP = {}

EP["evcharge14"] = dict(
 type="F형 (법조항 사이다) — 란빵 자동차, 개드립",
 t1='명절 아파트 충전기에', t2='26시간째 꽂혀 있던 차',
 hook='명절 아파트 충전기에 26시간째 꽂혀 있던 차, 과태료 대상임', bar='아파트 완속충전기 14시간 넘기면 과태료 10만 원',
 kw='#전기차충전방해', tags='#shorts #전기차충전방해 #완속충전기 #전기차과태료 #아파트충전소', shop='없음',
 comment='님들 아파트 충전기에 밤새 꽂아두는 거 괜찮다고 봄?',
 src='https://www.dogdrip.net/dogdrip/726597769 (댓글 90) ; 친환경자동차법 시행령 개정(2021-04-27 국무회의 의결) — 완속충전기 14시간 이상 주차 시 과태료 10만 원, 100세대 미만 아파트·연립·다세대·단독주택 완속충전시설 제외 (대한민국 정책브리핑 2021-04-27) ; 급속충전기 1시간 초과 과태료 10만 원 (찾기쉬운 생활법령정보)',
 desc='명절 연휴 아파트 완속충전기 10대가 모두 사용 중이었고, 그중 5대는 14시간을 넘겨 최장 26시간 37분째 꽂혀 있었음.\n친환경자동차법 시행령상 전기차가 완속충전기에 14시간 이상 주차하면 충전방해로 과태료 10만 원을 부과할 수 있음(급속충전기는 1시간 초과 시 10만 원).\n단, 100세대 미만 아파트와 연립·다세대·단독주택에 설치된 완속충전시설은 이 단속에서 제외됨.',
 orig={1: ("726597769_0.png", None), 2: ("726597769_0.png", (0, 60, 546, 470)), 3: ("726597769_0.png", (0, 470, 546, 738))},
 lines=[
  L("명절 연휴에 아파트 전기차 충전소를 봤더니 10대 중에 빈자리가 한 대도 없었음.",1),
  L("근데 충전 시간을 보니까 14시간, 16시간, 17시간.",2,"tick",em="17시간"),
  L("제일 긴 건 26시간 37분째 꽂혀 있었음.",3,"thud",em="26시간 37분",yellow=True),
  L("명절이라 어차피 차 안 쓰는데 꽂아두면 어때!",4,"eng",dlg="sub2",emo="happy"),
  L("근데 이거 그냥 얌체가 아니라 과태료 대상임.",5,"tick"),
  L("친환경자동차법 시행령상 완속충전기에 14시간 넘게 세워두면 충전방해로 과태료 10만 원임.",6,"ding",em="14시간",yellow=True),
  L("급속충전기는 기준이 더 짧아서 1시간만 넘겨도 똑같이 10만 원.",7,"cash",em="1시간"),
  L("그럼 퇴근하고 밤새 꽂아두는 것도 걸림?!",8,"boing",dlg="sub1"),
  L("저녁 7시에 꽂았으면 다음 날 아침 9시 전엔 빼야 함.",9,"pop",em="아침 9시"),
  L("명절이라고 꽂아두고 고향 내려가면 딱 걸리는 거임.",10,"siren"),
  L("대신 100세대 미만 아파트나 연립, 단독주택 충전기는 이 단속에서 빠짐.",11,em="100세대 미만"),
  L("충전 끝나면 옆집 사람 위해서라도 차 좀 빼주셈.",12),
  OUTRO],
 prompts={
  4: f"{M2} happily loading luggage into the trunk of a white electric car plugged into a charger in a Korean apartment underground parking garage, holiday trip, {T}",
  5: f"a row of electric cars all plugged into wall-mounted slow chargers in a Korean apartment underground parking garage, every spot occupied, {T}",
  6: f"close-up of a charging cable plugged into the port of an electric car, green charging indicator light, dim parking garage, {T}",
  7: f"a large DC fast charging station at a Korean highway rest area with an electric car plugged in, daytime, {T}",
  8: f"{W1} standing in an apartment parking garage holding her car key, looking annoyed at fully occupied EV chargers, {T}",
  9: f"an electric car plugged into a charger in an apartment parking garage at night, then empty spot concept, quiet, cool lighting, {T}",
  10: f"an empty Korean apartment parking garage during a holiday with only electric cars left plugged into chargers, {T}",
  11: f"a small Korean villa building with a single electric car charger in its ground floor parking, evening, {T}",
  12: f"{M1} unplugging a charging cable from his electric car in an apartment parking garage and smiling politely, {T}"})

EP["fuel100"] = dict(
 type="E형 (찬반 저울) — 란빵 자동차, 개드립",
 t1='100원 싸다길래', t2='고속도로 주유소에 줄 선 사람들',
 hook='100원 싸다길래 고속도로 주유소에 줄 선 사람들, 이득일까', bar='리터당 100원 할인, 15분 줄 서면 이득일까',
 kw='#고속도로주유소', tags='#shorts #고속도로주유소 #기름값할인 #추석연휴 #휴게소', shop='없음',
 comment='님들은 5천 원 아끼려고 15분 줄 설 수 있음?',
 src='https://www.dogdrip.net/dogdrip/726475483 (댓글 140) ; 한국도로공사 재정고속도로 주유소 226곳 2026-09-24~27 리터당 100원 인하(9/17 판매가 기준), 같은 기간 고속도로 통행료 면제 (노컷뉴스·MBC 2026-09-24) ; 현장 인터뷰(15분 대기, 반대 방향에서 돌아와 주유, 휴게소 간식값 뽑았다)는 채널A 보도 내용 인용',
 desc='2026년 추석 연휴(9월 24~27일) 한국도로공사가 관리하는 고속도로 주유소 226곳이 9월 17일 판매가보다 리터당 100원 기름값을 내리면서 휴게소 주유소마다 줄이 길게 생겼음.\n50L를 넣으면 약 5,000원, 70L면 약 7,000원을 아끼는 셈. 대기 시간과 우회 주행까지 따지면 이득은 사람마다 다름.\n같은 기간 고속도로 통행료도 면제됨.',
 orig={},
 lines=[
  L("추석 연휴에 고속도로 휴게소 주유소 앞으로 차들이 줄을 쭉 서 있었음.",1),
  L("9월 24일부터 27일까지 도로공사 주유소 226곳이 기름값을 리터당 100원 내렸거든.",2,"ding",em="100원",yellow=True),
  L("반대 방향 가던 사람이 일부러 이쪽 휴게소로 돌아서 넣으러 왔다는 얘기까지 나왔음.",3,"whoosh"),
  L("15분 기다렸는데 제일 싸니까 넣어야지!",4,"eng",dlg="sub2",emo="happy"),
  L("근데 계산기 한번 두드려보면 얘기가 좀 달라짐.",5,"tick"),
  L("50리터 가득 채우면 아끼는 돈이 딱 5천 원임.",6,"cash",em="5천 원",yellow=True),
  L("70리터 들어가는 큰 SUV도 7천 원 정도.",7,em="7천 원"),
  L("15분 줄 서고, 일부러 돌아오느라 기름 더 쓰면 남는 게 거의 없음.",8,"thud",em="남는 게 거의 없음"),
  L("그럼 줄 선 사람들 다 손해 본 거임?!",9,"boing",dlg="sub1"),
  L("어차피 휴게소 들를 거였으면 5천 원 공짜로 번 거고,",10,"ding",em="공짜로"),
  L("연휴 동안 통행료까지 면제라 호두과자 값은 뽑았다는 사람도 있었음.",11,"pop",em="통행료까지 면제"),
  L("할인은 27일까지임. 님들은 5천 원 아끼려고 15분 줄 설 거임?",12),
  OUTRO],
 prompts={
  1: f"a long queue of cars waiting to enter a gas station at a Korean highway rest area, autumn holiday, aerial view, {T}",
  2: f"close-up of a gas station fuel price display board with glowing digits at a Korean highway rest area, digits only, {T.replace('no text no letters','no words')}",
  3: f"a car making a U-turn toward a highway rest area on a Korean expressway, daytime, {T}",
  4: f"{M2} in a driver seat waiting in a gas station queue, smiling and checking his watch, {T}",
  5: f"close-up of a hand holding a smartphone calculator inside a car, {T}",
  6: f"a gas pump nozzle filling a car fuel tank at a Korean highway gas station, close-up, {T}",
  7: f"a large black SUV being refueled at a Korean highway rest area gas station, {T}",
  8: f"a row of cars stuck in a long line at a gas station entrance with a traffic attendant waving a red light baton, {T}",
  9: f"{W1} in a passenger seat throwing her hands up in frustration in a gas station queue, {T}",
  10: f"a busy Korean highway rest area with people walking to the food court, autumn afternoon, {T}",
  11: f"close-up of freshly baked Korean walnut cakes in a paper bag at a highway rest area, {T}",
  12: f"a Korean expressway toll gate with open lanes and cars passing through during a holiday, {T}"})

EP["taxi28"] = dict(
 type="D형 (썰 + 요금 규정) — 란빵 자동차, 개드립",
 t1='"부산 가주세요" 만취 택시', t2='눈 떠보니 대구, 택시비 28만 원',
 hook='만취해서 택시 타고 부산 가자고 한 사람, 눈 떠보니 대구에 28만 원', bar='서울 택시가 시 경계를 넘으면 요금이 이렇게 붙음',
 kw='#택시비', tags='#shorts #택시비 #시계외할증 #심야할증 #택시요금', shop='없음',
 comment='님들 택시비 제일 많이 나온 게 얼마임?',
 src='https://www.dogdrip.net/dogdrip/726436291 (댓글 112, 원글은 X 게시물 캡처 — 사례는 원글 기준) ; 서울시 중형택시 요금(2023-02-01~) 기본 4,800원/1.6km, 131m당 100원, 시계외 할증 20%, 심야 할증 22~23·02~04시 20%·23~02시 40%, 심야+시계외 복합할증 최대 60% (서울시) ; 경범죄처벌법 제3조 제1항 제39호 무임승차 — 10만 원 이하 벌금·구류·과료',
 desc='서울에서 만취한 채 택시를 타고 부산에 가 달라고 했다가, 눈을 뜨니 대구 부근이었고 미터기가 283,830원이었다는 사연.\n서울 중형택시는 기본요금 4,800원(1.6km)에 131m당 100원이 오르고, 서울 시 경계를 벗어나면 시계외 할증 20%가 붙음. 22시~04시 심야 할증(20~40%)과 겹치면 최대 60%까지 할증됨(서울시).\n요금을 정당한 이유 없이 내지 않으면 경범죄처벌법상 무임승차로 10만 원 이하 벌금·구류·과료 대상임.',
 orig={},
 lines=[
  L("서울에서 술 마시다가 택시 잡고 부산 가주세요 한 사람이 있었음.",1),
  L("만취해서 갑자기 귀소본능이 생긴 거임.",2,"boing",em="귀소본능"),
  L("그리고 눈을 떴는데 택시가 대구 근처를 달리고 있었음.",3,"whoosh"),
  L("미터기를 봤더니 28만 3천8백 원.",4,"thud",em="28만 3천8백 원",yellow=True),
  L("기사님 이거 장난이죠?!",5,"boing",dlg="sub2"),
  L("근데 이게 장난이 아닌 이유가 있음.",6,"tick"),
  L("서울 택시는 기본 4천8백 원에 131미터마다 백 원씩 올라감.",7,"ding",em="131미터"),
  L("여기에 서울 경계를 넘는 순간부터 시계외 할증 20%가 붙음.",8,"cash",em="시계외 할증 20%",yellow=True),
  L("밤 10시에서 새벽 4시 사이면 심야 할증이랑 겹쳐서 최대 60%까지 올라감.",9,"siren",em="최대 60%"),
  L("그럼 돈 없다고 버티면 어떻게 됨?!",10,"boing",dlg="sub1"),
  L("정당한 이유 없이 요금 안 내면 경범죄처벌법상 무임승차로 10만 원 이하 벌금임.",11,"pop",em="무임승차"),
  L("술 마시고 택시 탈 땐 목적지부터 정신 차리고 말하셈.",12),
  OUTRO],
 prompts={
  1: f"{M1} drunk with flushed cheeks waving down a taxi on a Seoul street at night, neon lights, {T}",
  2: f"{M1} slumped asleep in the back seat of a Korean taxi at night, city lights through the window, {T}",
  3: f"view from the back seat of a taxi driving on a dark Korean expressway at dawn, road signs blurred, {T}",
  4: f"close-up of a glowing taxi meter display on a car dashboard at night, digits only, {T.replace('no text no letters','no words')}",
  5: f"{M1} in the back seat of a taxi waking up in shock, eyes wide, grabbing his head, dawn light, {T}",
  6: f"rear view of a Korean taxi driving on an empty highway at dawn, {T}",
  7: f"an orange Korean taxi driving through downtown Seoul at night, motion blur, {T}",
  8: f"a Korean expressway at night seen from a car with the city skyline behind, leaving the city, {T}",
  9: f"a taxi driving under highway lights late at night, long exposure light trails, {T}",
  10: f"{M1} in a taxi back seat nervously checking an empty wallet, {T}",
  11: f"a Korean police officer talking to a taxi driver and a passenger beside a taxi at dawn, {T}",
  12: f"{M1} sober in the back seat of a taxi calmly telling the driver the destination, daytime, {T}"})

EP["benz10x"] = dict(
 type="F형 (법조항 사이다) — 란빵 자동차, 개드립",
 t1='"손대면 죽을 줄 아세요"', t2='두 칸 차지한 벤츠의 경고문',
 hook='"손대면 죽을 줄 아세요" 두 칸 차지한 벤츠에 붙은 경고문', bar='손해배상 10배 청구, 법적으로 가능할까',
 kw='#주차빌런', tags='#shorts #주차빌런 #두칸주차 #손해배상 #아파트주차장', shop='없음',
 comment='님들은 이런 쪽지 붙은 차 옆에 주차하겠음?',
 src='https://www.dogdrip.net/dogdrip/726466242 (댓글 80) ; 민법 제393조(손해배상의 범위 — 통상의 손해 한도), 징벌적·배수 배상은 하도급법·개인정보보호법 등 일부 특별법에만 규정 ; 아파트 단지 내 주차장은 도로교통법상 도로가 아니어서 주정차 위반 단속 대상이 아님, 관리규약에 따른 경고 스티커 등으로 관리',
 desc='아파트 지하주차장에서 주차선을 가운데 두고 두 칸을 차지한 차량 앞유리에 "제 차에 손대면 죽을 줄 아세요, 손해배상 10배 청구" 쪽지가 붙어 있었음.\n우리 민법상 손해배상은 실제로 발생한 손해(통상손해)를 기준으로 하고, 몇 배를 물리는 징벌적 배상은 일부 특별법에만 있음. 쪽지에 10배라고 써도 효력은 없음.\n아파트 단지 내 주차장은 도로교통법상 도로가 아니라 주차 위반 단속 대상이 아니고, 관리규약에 따라 관리사무소가 경고 스티커 등으로 관리함.',
 orig={1: ("726466242_0.png", (0, 180, 1080, 855)), 2: ("726466242_2.png", (0, 0, 1080, 960))},
 lines=[
  L("아파트 지하주차장에 흰색 벤츠 한 대가 두 칸을 떡하니 차지하고 있었음.",1),
  L("뒤로 가보니 주차선이 차 한가운데를 딱 지나가고 있었음.",2,"thud",em="한가운데"),
  L("그리고 앞유리엔 쪽지가 하나 붙어 있었음.",3,"tick"),
  L("제 차에 손대면 죽을 줄 아세요! 손해배상 10배 청구!",4,"siren",dlg="sub2"),
  L("근데 여기서 법 얘기하면 좀 웃긴 게 있음.",5,"tick"),
  L("우리 민법은 실제로 난 손해만큼만 물어주게 돼 있음.",6,"ding",em="실제로 난 손해만큼"),
  L("쪽지에 10배라고 써놔도 법적으로는 아무 효력이 없음.",7,"thud",em="아무 효력이 없음",yellow=True),
  L("몇 배씩 물리는 징벌적 배상은 일부 특별법에만 있는 얘기임.",8,em="일부 특별법"),
  L("그럼 두 칸 차지한 건 처벌 못 함?!",9,"boing",dlg="sub1"),
  L("아파트 주차장은 도로교통법상 도로가 아니라서 주차 딱지는 못 뗌.",10,"cash",em="주차 딱지는 못 뗌",yellow=True),
  L("관리사무소가 관리규약으로 경고 스티커 붙이는 정도가 끝임.",11,"pop"),
  L("비싼 차일수록 한 칸에 반듯하게 대는 게 진짜 매너임.",12),
  OUTRO],
 prompts={
  3: f"close-up of a folded white paper note tucked behind the windshield of a white car in an underground parking garage, blank paper, {T}",
  4: f"{M2} with an arrogant expression pointing a finger while standing next to his white luxury sedan in an underground parking garage, {T}",
  5: f"{W1} in an underground parking garage covering her mouth to hold back laughter while looking at a car, {T}",
  6: f"a judge's wooden gavel on a desk next to legal documents, courtroom, {T}",
  7: f"a crumpled paper note lying on the hood of a white car, parking garage, {T}",
  8: f"stack of thick Korean law books on a wooden desk in a lawyer's office, {T}",
  9: f"{M1} standing in a parking garage with arms spread in disbelief next to an empty narrow parking space, {T}",
  10: f"wide view of a Korean apartment underground parking garage with pillars and parked cars, {T}",
  11: f"a Korean apartment security guard in uniform placing a warning sticker on a car window in a parking garage, {T}",
  12: f"a white sedan parked perfectly straight inside the lines of a single parking space in a clean underground garage, {T}"})


def cover(src, box, out):
    """원글 사진 → 1280x800. 비율이 안 맞으면 블러 배경 위에 가운데 배치."""
    im = Image.open(os.path.join(SRC, src)).convert("RGB")
    if box: im = im.crop(box)
    W, H = 1280, 800
    bg = im.resize((W, H)).filter(ImageFilter.GaussianBlur(30))
    s = min(W / im.width, H / im.height)
    fg = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    bg.save(out)

for slug, e in EP.items():
    wd = os.path.join(ROOT, "work", slug); os.makedirs(os.path.join(wd, "img"), exist_ok=True)
    nimg = max(l.get("img", 0) for l in e["lines"])
    assert set(e["prompts"]) | set(e["orig"]) == set(range(1, nimg + 1)), slug
    for n, (src, box) in e["orig"].items():
        cover(src, box, os.path.join(wd, "img", f"{n:02d}.png"))
    sj = {"slug": slug, "type": e["type"], "source": e["src"],
          "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["hook"], "channel": "란빵",
          "voice": "taesub", "style": {"sub_box": True, "bar": e["bar"], "watermark": ""},
          "lines": e["lines"]}
    json.dump(sj, open(os.path.join(wd, "script.json"), "w"), ensure_ascii=False, indent=2)
    with open(os.path.join(wd, "prompts.tsv"), "w") as f:
        for n in range(1, nimg + 1):
            f.write(f"{n:02d}\t{e['prompts'].get(n, 'ORIGINAL ' + str(e['orig'].get(n, ('',))[0]))}\n")
    title = f"{e['kw']} {e['hook']}"; assert len(title) <= 100, title
    up = (f"# {slug} — 업로드 메타\n\n## 제목\n\n{title}\n\n## 설명\n\n{e['desc']}\n\n"
          f"※ 원글 사진 외 이미지는 AI 연출 자료입니다. 기준일 2026-09-26.\n※ 근거: script.json 의 source 필드 참조.\n\n{e['tags']}\n\n"
          f"## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop']}\n")
    open(os.path.join(wd, "upload.md"), "w").write(up)
    with open(os.path.join(wd, "jobs.tsv"), "w") as f:
        for n, p in sorted(e["prompts"].items()):
            f.write(f"{os.path.join(wd, 'img', f'{n:02d}.png')}\t{p}\n")
    print(slug, len(e["lines"]), "lines", nimg, "imgs", len(e["prompts"]), "sdxl", len(title), "title chars")
