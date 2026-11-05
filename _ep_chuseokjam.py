#!/usr/bin/env python3
"""란빵 추석 고속도로 정체 이유 1편 (2026-09-25) — script.json / prompts.tsv / upload.md 생성. 이미지 전량 로컬 SDXL."""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
T = ("photorealistic DSLR photograph, 35mm lens, natural available light, shallow depth of field, "
     "Korean setting, no text no letters no signage no logos no brand marks no watermark")
W1 = "a Korean woman in her early 30s, shoulder-length dark brown hair, natural light makeup"
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

slug = "chuseokjam"
e = dict(
 t1='사고도 없는데', t2='추석 고속도로가 막히는 이유',
 hook='사고도 없는데 추석 고속도로가 꽉 막히는 진짜 이유', bar='사고도 공사도 없는데 명절 고속도로가 멈추는 이유',
 kw='#유령정체', tags='#shorts #유령정체 #추석귀경길 #고속도로정체 #차간거리', shop='없음',
 comment='님들 이번 추석 귀성길 몇 시간 걸렸음?',
 src='국토교통부 2026 추석 특별교통대책(9.23~27) — 고속도로 일평균 605만 대(전년 대비 11.8%↑)·추석 당일 684만 대, 귀성 최대 서울→부산 10시간30분, 통행료 면제 9.24~27 (아시아경제·데일리안·스타뉴스 2026-09-19~21) ; 유령 정체(Phantom Jam) — 2008 나고야대 원형 트랙 22대 시속 30km 실험에서 원인 없이 정체 발생, 서울양양고속도로 금남터널 페이스메이커 시스템 약 1년 운영 속도 저하 10% 이상 개선(한국건설기술연구원) (파이낸셜뉴스 2026-09-24)',
 desc='올해 추석 특별교통대책 기간(9월 23~27일) 고속도로 통행량은 하루 평균 605만 대, 추석 당일 684만 대로 예상됐고, 귀성길 최대 소요시간은 서울→부산 10시간 30분이었음(국토교통부).\n차가 많은 것만이 이유는 아님. 사고나 공사가 없는데도 한 차의 작은 감속이 뒤차로 갈수록 커지며 행렬이 멈추는 현상을 \'유령 정체\'라고 부름. 2008년 일본 나고야대 연구진은 원형 트랙에서 차 22대를 시속 30km로 달리게 했을 때 아무 원인 없이 정체가 생기는 것을 보여줬음.\n합류 구간의 끼어들기와 잦은 차선 변경은 정체를 키우고, 충분한 차간 거리와 일정한 속도가 정체를 줄임. 서울양양고속도로 금남터널에 속도 유도등(페이스메이커 시스템)을 설치한 뒤 속도 저하 현상이 10% 이상 개선됐음(한국건설기술연구원).',
 lines=[
  L("사고도 공사도 없는데 추석 고속도로가 꽉 막히는 데는 이유가 있음.",1),
  L("올해 추석 당일 고속도로엔 684만 대가 몰릴 걸로 예상됐음.",2,"tick",em="684만 대"),
  L("귀성길 서울에서 부산까지 최대 10시간 반이었음.",3,"thud",em="10시간 반",yellow=True),
  L("앞에 무슨 큰 사고라도 났나?!",4,"boing",dlg="sub2"),
  L("근데 한참 기어가다 보면 사고 난 차는 없고 갑자기 뻥 뚫림.",5,"whoosh",em="뻥 뚫림"),
  L("이걸 유령 정체라고 부름.",6,"ding",em="유령 정체",yellow=True),
  L("시작은 앞차 한 대가 브레이크를 살짝 밟는 거임.",7,"tick"),
  L("뒤차는 그보다 조금 더 세게, 그 뒤차는 더 세게 밟다가",8),
  L("수십 대 뒤에서는 아예 멈춰버림.",8,"thud",em="아예 멈춰버림"),
  L("2008년 일본 나고야대가 원형 트랙에 차 22대를 시속 30km로 똑같이 돌려봤는데,",9,"eng"),
  L("사고도 신호도 없는데 저절로 정체가 생겼음.",10,"ding",em="저절로",yellow=True),
  L("여기에 합류 구간 끼어들기랑 잦은 차선 변경까지 겹치면 병목이 터지는 거임.",11,"siren",em="병목"),
  L("그럼 우리는 그냥 갇혀 있어야 됨?!",12,"boing",dlg="sub1"),
  L("차간 거리 넉넉히 두고, 브레이크 대신 액셀을 살짝 떼는 것만으로도 줄어듦.",13,"pop",em="차간 거리",yellow=True),
  L("실제로 터널에 속도 유도등을 달았더니 속도 떨어지는 현상이 10% 넘게 줄었음.",14,"ding",em="10%"),
  L("귀경길 막히면 앞차 욕하기 전에 내 차간 거리부터 보셈.",15),
  OUTRO],
 prompts=[
  f"aerial view of a Korean expressway completely jammed with holiday traffic in both lanes, autumn afternoon, {T}",
  f"long line of cars with red brake lights stretching to the horizon on a Korean expressway at dusk, {T}",
  f"{M2} in a driver seat stuck in traffic, rubbing his tired eyes, family asleep in the car, {T}",
  f"{M2} in a driver seat leaning forward and squinting over the steering wheel at a traffic jam ahead, frustrated, {T}",
  f"view through a car windshield of a suddenly empty open expressway ahead, bright daylight, {T}",
  f"a ghostly misty Korean expressway with a slow line of cars fading into fog, eerie mood, {T}",
  f"close-up of a car red brake light turning on in daytime traffic on a highway, {T}",
  f"a chain of cars on a highway with brake lights lighting up one after another, rear view, telephoto compression, {T}",
  f"cars driving in a circle on a closed circular test track seen from above, experiment, {T.replace('Korean setting','Japanese setting')}",
  f"a cluster of stopped cars bunched together on a circular test track while the rest of the track is empty, aerial, {T.replace('Korean setting','Japanese setting')}",
  f"cars merging aggressively from an on-ramp into a crowded Korean expressway, top-down view, {T}",
  f"{W1} in a passenger seat throwing her hands up in frustration in a traffic jam, {T}",
  f"a car driving with a generous gap behind another car on a flowing Korean expressway, rear view, calm, {T}",
  f"interior of a Korean highway tunnel with rows of blue and green LED guide lights along the walls, cars driving, {T}",
  f"{M2} calmly driving on a flowing highway at sunset with both hands on the wheel, relieved, {T}"])

wd = os.path.join(ROOT, "work", slug); os.makedirs(os.path.join(wd, "img"), exist_ok=True)
nimg = max(l.get("img", 0) for l in e["lines"])
assert nimg == len(e["prompts"]), (nimg, len(e["prompts"]))
sj = {"slug": slug, "type": "D형 (뉴스 반전) — 란빵 자동차 추석", "source": e["src"],
      "title_line1": e["t1"], "title_line2": e["t2"], "hook": e["hook"], "channel": "란빵",
      "voice": "taesub", "style": {"sub_box": True, "bar": e["bar"], "watermark": ""},
      "lines": e["lines"]}
json.dump(sj, open(os.path.join(wd, "script.json"), "w"), ensure_ascii=False, indent=2)
with open(os.path.join(wd, "prompts.tsv"), "w") as f:
    for i, p in enumerate(e["prompts"], 1): f.write(f"{i:02d}\t{p}\n")
title = f"{e['kw']} {e['hook']}"; assert len(title) <= 100
up = (f"# {slug} — 업로드 메타\n\n## 제목\n\n{title}\n\n## 설명\n\n{e['desc']}\n\n"
      f"※ 이미지는 AI 연출 자료입니다. 기준일 2026-09-25.\n※ 근거: script.json 의 source 필드 참조.\n\n{e['tags']}\n\n"
      f"## 고정 댓글\n\n{e['comment']}\n\n## 쇼핑태그\n\n{e['shop']}\n")
open(os.path.join(wd, "upload.md"), "w").write(up)
# SDXL joblist (out<TAB>prompt, 줄 구분)
with open(os.path.join(wd, "jobs.tsv"), "w") as f:
    for i, p in enumerate(e["prompts"], 1): f.write(f"{os.path.join(wd, 'img', f'{i:02d}.png')}\t{p}\n")
print(slug, len(e["lines"]), "lines", nimg, "imgs", len(title), "title chars")
