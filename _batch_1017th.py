#!/usr/bin/env python3
"""란빵 2026-10-17 — rdthreads: 스레드에 사람들이 만든 테슬라 로드스터 이미지/영상 소개 1편.
사용자 지시: "스레드에 테슬라 날으는 자동차 관련해서 사람들이 만들어놓은 이미지나 영상 찾아다가 소개하는 영상 1개",
대본은 "테슬라에서 발표한 날으는 자동차 로드스터 / 이걸 본 사람들의 반응이 진짜 웃긴데 ㅋㅋ" 로 시작,
"엥? 이게 뭐죠? ㅋㅋㅋ 아놔" 말투로 하나씩 소개, 중간중간 대화체, 40초 이내.
소재 = 스레드 게시물 6개(work/_threads/, 화면마다 출처 @계정 표기). 테슬라 공식 영상 재업로드는 창작물이 아니라 제외.
"""
import json, os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
SLUG = "rdthreads"
Y, R = "#FBFF56", "#FF3B30"
TS = "영상: Tesla"


def V(name, credit, at=None, s0=1.0, s1=1.08, fx=0.5, fy=0.5, punch=False, ss=0):
    d = {"vid": f"vid/{name}.mp4", "s0": s0, "s1": s1, "fx": fx, "fy": fy, "credit": credit}
    if at: d["at"] = at
    if punch: d["punch"] = True
    if ss: d["ss"] = ss
    return d


def I(name, credit, at=None, s0=1.0, s1=1.1, fx=0.5, fy=0.5, punch=False):
    d = {"img": f"real/{name}", "s0": s0, "s1": s1, "fx": fx, "fy": fy, "credit": credit}
    if at: d["at"] = at
    if punch: d["punch"] = True
    return d


def L(text, sh, **k):
    d = {"text": text, "sh": sh}; d.update(k); return d


C_POL, C_TOLL, C_TUN = "스레드 @namul_34", "스레드 @lim.808", "스레드 @jayjay808bs"
C_DOG, C_BSN, C_GAME = "스레드 @solrr.aa", "스레드 @story_spoon", "스레드 @seonkangmin"

lines = [
  L("지금 테슬라 밈이 미쳤다는데 ㅋㅋ", [V("t_police", C_POL, ss=9.3, s0=1.0, s1=1.1), V("finfly", TS, "밈이", ss=1.0, punch=True)],
    say="지금 테슬라 밈이 미쳤다는데, 푸핰!", em=["밈이 미쳤다"], em_color="yellow", fx=[("hit_trailer_epic", "미쳤다는데", 0.5)]),
  L("엥? 이게 뭐죠? 경찰이 길을 다 막았더니 그냥 위로 넘어가 버림", [V("t_police", C_POL, ss=5.5, s0=1.0, s1=1.05), V("t_police", C_POL, "넘어가", ss=8.5, punch=True)],
    em=["위로 넘어가"],
    fx=[("boom_zoom_impact", "넘어가", 0.5)], shake="넘어가"),
  L("아놔, 이러면 경찰은 어떻게 쫓아갈까요?", [V("t_police", C_POL, ss=11.5, s0=1.05, s1=1.12)],
    dialogue=True, speaker=3, emotion="surprise", fx=[("drum_rimshot", "쫓아갈까요", 0.45)]),
  L("그래서 한국 톨게이트는 대비 끝남. 점프는 여기서 끝, 그물까지 쳐놨음 ㅋㅋ", [I("t_toll.jpg", C_TOLL, s0=1.0, s1=1.1, fy=0.4), I("t_toll.jpg", C_TOLL, "그물까지", s0=1.5, s1=1.6, fy=0.3)],
    say="그래서 한국 톨게이트는 대비 끝남. 점프는 여기서 끝, 그물까지 쳐놨음, 푸핰!", em=["그물"], em_color="yellow",
    fx=[("scratch_vinyl", "그물까지", 0.45)], pop=("그물 ㅋㅋ", Y, "그물까지")),
  L("아니 이건 또 뭐죠? 터널 천장에 로드스터 전용 차로가 생김.", [I("t_tunnel.jpg", C_TUN, s0=1.0, s1=1.1), I("t_tunnel.jpg", C_TUN, "천장에", s0=1.6, s1=1.7, fx=0.5, fy=0.2, punch=True)],
    em=["천장에"], em_color="yellow"),
  L("심지어 통행료가 7만원이라네 ㅋㅋ", [I("t_tunnel.jpg", C_TUN, s0=1.7, s1=1.8, fx=0.65, fy=0.5)],
    say="심지어 통행료가 칠마넌이라네, 푸핰!", em=["7만원"], em_color="yellow",
    fx=[("wrong_gameshow_buzz", "7만원", 0.45)], pop=("7만원?!", R, "7만원")),
  L("시승기도 올라왔는데, 출발하자마자 강아지랑 케이크가 같이 날아감.", [V("t_corgi_city", C_DOG, ss=6.0, s0=1.0, s1=1.05), V("t_corgi", C_DOG, "케이크가", ss=8.5, punch=True)],
    em=["케이크"], fx=[("glass_smash", "날아감", 0.4)], shake="날아감"),
  L("와, 내 케이크!", [V("t_corgi", C_DOG, ss=11.0, s0=1.05, s1=1.12)], dialogue=True, speaker=2, emotion="angry"),
  L("부산에선 부캉이랑 같이 바다 위를 날아다님.", [V("t_busan", C_BSN, ss=4.0, s0=1.0, s1=1.08)], em=["부캉이"], em_color="yellow"),
  L("급기야 로드스터 게임을 직접 만든 사람까지 등장했는데,", [V("t_game", C_GAME, ss=9.0, s0=1.0, s1=1.05), V("t_game", C_GAME, "게임을", ss=18.0)],
    em=["게임"], em_color="yellow", fx=[("drop_futuristic", "게임을", 0.5)]),
  L("님들은 이것 중에 뭐가 제일 웃김?", [V("t_police", C_POL, ss=9.0, s0=1.0, s1=1.1)], fx=[("pop_bubble", "웃김")]),
]

assert sum(1 for l in lines if l.get("dialogue")) >= 2
for l in lines:
    s = l.get("say", l["text"])
    assert not any(c.isdigit() for c in s), s
    if l.get("dialogue"): assert l.get("speaker", 1) != 1 and not l.get("em")
    for w in l.get("em", []): assert w in l["text"], w
    assert "—" not in l["text"] and "·" not in l["text"]

t1, t2, bar = "지금 테슬라 밈이", "미쳤다는데 ㅋㅋ", "하늘 나는 테슬라 보고 사람들이 만든 것들"
title = "#로드스터 스레드 반응"
assert len(title) <= 12

wk = os.path.join(ROOT, "work", SLUG)
SK = ("sh", "fx", "pop", "shake", "info")
sc_lines = [{**{k: v for k, v in l.items() if k not in SK}, "img": 1} for l in lines]
sc_lines.append({"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": 1})
sc = {"slug": SLUG, "type": "란빵 자동차, 테슬라 로드스터 시리즈(스레드 창작물 소개)",
      "source": "스레드 @namul_34 @lim.808 @jayjay808bs @solrr.aa @story_spoon @seonkangmin (2026-10-16~17)",
      "title_line1": t1, "title_line2": t2, "hook": bar, "channel": "란빵",
      "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
      "style": {"sub_box": True, "bar": bar, "bar_count": None, "watermark": ""}, "lines": sc_lines}
json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)

texts = [l["text"].rstrip(".") for l in sc_lines]
out = []
for i, l in enumerate(lines):
    d = {"shots": l["sh"]}
    if l.get("fx"): d["sfx"] = [list(x) for x in l["fx"]]
    for k in ("pop", "shake"):
        if l.get(k): d[k] = list(l[k]) if k == "pop" else l[k]
    ws = [s.get("at") for s in d["shots"]] + [x[1] for x in d.get("sfx", [])] + [d.get("shake")] + ([d["pop"][2]] if "pop" in d else [])
    for w in ws: assert not w or w in texts[i], (i, w)
    for s in d["shots"]:
        p = os.path.join(wk, "v2", s.get("vid") or s.get("img"))
        assert os.path.exists(p), p
    out.append(d)
out.append({"shots": [{"img": "real/outro.jpg", "s0": 1.0, "s1": 1.1, "credit": TS}],
            "sfx": [["pop_long", "구독!"]], "pop": ["구독!", "#FFE629", "구독!"]})
json.dump({"bgmVol": 0.09, "bgm": "bgm/sneaky-123.mp3", "lines": out},
          open(os.path.join(wk, "v2", "shots.json"), "w"), ensure_ascii=False, indent=1)

desc = ("테슬라가 공개한 하늘 나는 로드스터를 보고 스레드 사람들이 만든 이미지와 영상 모음.\n"
        "경찰 바리케이드 점프, 톨게이트 점프 방지 그물, 터널 천장 전용 차로, 케이크 날아간 시승기, 부캉이와 부산 바다, 직접 만든 로드스터 게임까지.\n"
        "님들이 뽑은 최고는?\n"
        "#shorts #테슬라 #로드스터 #밈 #전기차")
proof = "\n".join(f"| {a} | {b} |" for a, b in [
    ("경찰 바리케이드 점프 AI 영상", "https://www.threads.com/@namul_34/post/DelfoxNgC2H"),
    ("톨게이트 점프 방지 그물 이미지", "https://www.threads.com/@lim.808/post/Dei8qsBkXui"),
    ("터널 천장 로드스터 전용 차로, 통행료 7만원 이미지", "https://www.threads.com/@jayjay808bs/post/DelhFBdATW8 (게시물 내 'Photo by 소소한 발견' 표기, 원작자 별도일 수 있음)"),
    ("시승 1일차 AI 영상(강아지, 케이크)", "https://www.threads.com/@solrr.aa/post/DelgxK5k4VY (AI 콘텐츠 표기)"),
    ("부캉이 + 로드스터 부산 AI 영상", "https://www.threads.com/@story_spoon/post/DelSP0nDJkN"),
    ("로드스터 시뮬레이터 게임", "https://www.threads.com/@seonkangmin/post/Dek8QwagAO2"),
    ("도입부 시연 영상", "Tesla 공식 Roadster Event qt5p-_tE8d0")])
open(os.path.join(wk, "upload.md"), "w").write(
    f"# {SLUG}: 업로드 메타 (란빵)\n\n## 제목\n\n{title}\n\n## 설명\n\n{desc}\n\n"
    f"## 고정 댓글\n\n님들은 이 중에 뭐가 제일 웃김?\n\n"
    f"## 쇼핑태그\n\n자동차 블랙박스 2채널, 차량용 휴대폰 거치대, 차량용 컵홀더, 차량용 방향제, 하이패스 단말기\n\n"
    f"## 근거표\n\n| 화면 | 출처 |\n|---|---|\n{proof}\n\n"
    f"⚠️ 남의 창작물(스레드 게시물) 사용 편. 화면마다 출처 @계정 표기. 원작자 요청 시 바로 내릴 것.\n")
print("ok", SLUG, len(sc_lines), "lines")
