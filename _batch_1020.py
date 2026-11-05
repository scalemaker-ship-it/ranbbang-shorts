#!/usr/bin/env python3
"""란빵 2026-10-20: 10편(보배드림 + 신차 + 자동차용품). 새 화면 = GPT 리얼 배경(gen.sh luna) 앞에 いらすとや 캐릭터(사용자 지시).
- 배경: 사람 없는 실사풍 장면(캐릭터가 주인공). 신차 편의 차 자체는 제조사 공식 사진(메모리 규칙: 신차 AI 금지).
- 캐릭터: shots.json 줄 "char" → remotion CharView(박스 아래 변에 서서 튀어오름). 한 편 20장 이하(いらすとや 무료 조건).
- 대본 중간 대화체 1줄 이상, 40초 미만, 숫자는 say 에 한글.
보배드림 4편 근거 = 베스트 1040923 / 1041030 / 1040990 / 1041125 (2026-10-19, 조사 에이전트가 본문·댓글 확인).
"""
import json, os, re, shutil, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "remotion", "tools"))
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")
Y, W, R = "#FBFF56", "#fff", "#FF3B30"
SUF = (" Photorealistic candid smartphone photo taken in South Korea, natural light, realistic detail, 1:1."
       " Empty background plate: no people, no faces, no hands. No text, no captions, no readable signs, no logos, no watermark.")

# いらすとや 카탈로그: 이름 → (검색어, 파일명). 받은 원본은 work/_ir_pool/ 에 모아 두고 편마다 복사
IR = {
    "drv_smile": ("車を運転している男性", "car_man01_smile.png"), "drv_angry": ("車を運転している男性", "car_man02_angry.png"),
    "drv_cry": ("車を運転している男性", "car_man03_cry.png"), "drv_laugh": ("車を運転している男性", "car_man04_laugh.png"),
    "drv_idea": ("車を運転している男性", "car_man05_idea.png"), "drv_shock": ("車を運転している男性", "car_man06_shock.png"),
    "drv_surprise": ("車を運転している男性", "car_man07_surprise.png"), "drv_think": ("車を運転している男性", "car_man08_think.png"),
    "drv_q": ("車を運転している男性", "car_man09_question.png"), "drv_heart": ("車を運転している男性", "car_man10_heart.png"),
    "biz_smile": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man1_1_smile.png"),
    "biz_angry": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man1_2_angry.png"),
    "biz_cry": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man1_3_cry.png"),
    "biz_laugh": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man1_4_laugh.png"),
    "biz_idea": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man2_1_idea.png"),
    "biz_shock": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man2_2_shock.png"),
    "biz_surprise": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man2_3_surprise.png"),
    "biz_think": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man2_4_think.png"),
    "biz_q": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man3_1_question.png"),
    "biz_heat": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man3_2_heat.png"),
    "biz_tehe": ("いろいろな表情のスーツを着た人のイラスト（男性）", "business_man3_4_tehe.png"),
    "wow": ("驚く男性", "pose_english_wow_man.png"), "rage": ("怒る男性", "pose_sugoi_okoru_man.png"),
    "police_angry": ("怒る男性", "police_angry_man.png"), "komatta": ("困る男性", "komatta_man2.png"),
    "banzai": ("喜ぶ男性", "seikou_banzai_man.png"), "success": ("ガッツポーズ", "money_success_man.png"),
    "bill_shock": ("請求書", "seikyuusyo_shock.png"), "lawyer": ("弁護士", "job_bengoshi_man.png"),
    "hoken": ("保険会社", "building_hoken_gaisya.png"), "seiri": ("交通誘導", "koutsu_seiri.png"),
    "umbrella": ("傘をさす", "summer_higasa5_man.png"), "bag_woman": ("買い物袋", "shopping_bag_temochi_woman.png"),
    "ignore": ("無視", "mushi_people.png"), "daikou": ("代行運転", "job_unten_daikou_car.png"),
    "busdrv": ("タクシー運転手", "job_bus_driver_man.png"), "busdrv_bow": ("タクシー運転手", "job_bus_driver_man_ojigi.png"),
    "taxi": ("タクシー運転手", "taxi_driver_untensyu3.png"), "taxi_black": ("運転手", "car_taxi_black_driver.png"),
    "ebike": ("電動アシスト自転車", "jintesya_dendou.png"), "bike_slip": ("転倒", "jiko_manhole_jitensya.png"),
    "dealer": ("車を買う", "car_dealer_man.png"), "parkguard": ("駐車違反", "job_chusya_kanshiin_man.png"),
    "aori": ("煽り運転", "hyouhen_car_drive.png"), "jiko_man": ("交通事故", "koutsu_jiko_car_man.png"),
    "recorder": ("ドライブレコーダー", "car_drive_recorder.png"), "ev": ("電気自動車", "car_denki.png"),
    "gas_self": ("ガソリン", "gas_station_kyuuyu_self.png"), "ijihi": ("ガソリン", "money_car_ijihi.png"),
    "hydro": ("タイヤ", "car_jiko_hydroplaning.png"), "sensya": ("洗車", "sensya_man.png"),
    "shinpai": ("考える男性", "shinpai_ojisan.png"), "ohagya": ("ショック", "money_ohagya.png"),
    "hakusyu": ("拍手", "hakusyu.png"), "syachu": ("車中泊", "car_travel_syachuhaku.png"),
    "samui": ("ながら運転", "car_winter_samui.png"), "navi": ("カーナビ", "unten_car_navigation.png"),
    "keitai": ("車を運転している男性", "car_unten_keitai.png"), "open_man": ("オープンカー", "car_sports_open_man.png"),
    "sick": ("ショック", "sick_kaoiro_man.png"), "carshop": ("カー用品", "building_car_youhin_tire.png"),
}
POOL = os.path.join(ROOT, "work", "_ir_pool")


def ir_fetch(slug, names):
    import ir_rb as I
    import io, urllib.request
    from PIL import Image
    os.makedirs(POOL, exist_ok=True)
    d = os.path.join(ROOT, "work", slug, "v2", "ir")
    os.makedirs(d, exist_ok=True)
    assert len(names) <= 20, f"{slug}: いらすとや {len(names)}장 > 20"
    credits = []
    for n in sorted(names):
        q, fn = IR[n]
        src = os.path.join(POOL, fn)
        if not os.path.exists(src):
            title, url = next((t, u) for t, u in I.search(q, 12) if u.endswith("/" + fn))
            im = Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(url, headers=I.UA), timeout=30).read())).convert("RGBA")
            im = im.crop(im.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox())
            I.outline(im).save(src)
        shutil.copy(src, os.path.join(d, f"ir_{n}.png"))
        credits.append(fn)
    return credits


AIP = {}   # 지금 만드는 편의 배경 프롬프트(키 → 프롬프트), build 가 ai_prompts.tsv 로 쓰고 비운다


def B(key, prompt=None, at=None, s0=1.0, s1=1.1, fx=0.5, fy=0.5, punch=False):
    if prompt:
        assert key not in AIP, key
        AIP[key] = prompt.strip() + SUF
    d = {"img": f"ai/{key}.png", "s0": s0, "s1": s1, "fx": fx, "fy": fy}
    if at:
        d["at"] = at
    if punch:
        d["punch"] = True
    return d


def P(name, credit, at=None, s0=1.0, s1=1.1, fx=0.5, fy=0.5, punch=False):
    """실사(제조사 공식 사진) — v2/real/<name>.jpg (1080x960)."""
    d = {"img": f"real/{name}.jpg", "s0": s0, "s1": s1, "fx": fx, "fy": fy, "credit": credit}
    if at:
        d["at"] = at
    if punch:
        d["punch"] = True
    return d


def C(name, side="l", h=None, at=None, flip=False):
    d = {"name": name, "side": side}
    if h:
        d["h"] = h
    if at:
        d["at"] = at
    if flip:
        d["flip"] = True
    return d


def L(text, sh, ch, **k):
    d = {"text": text, "sh": sh, "ch": ch}
    d.update(k)
    return d


# 2026-10-29 사용자 지시 "영상 속 이라스토야 캐릭터 없이, 앞으로 쭉": ch 와 아웃트로 캐릭터를 shots.json 에 넣지 않는다.
NO_CHAR = True


def build(slug, lines, t1, t2, bar, title, source, proof, desc, comment, tags, extra, outro_sh, typ="란빵 자동차, 보배드림"):
    global AIP
    assert any(l.get("dialogue") for l in lines), "대화체 줄 없음"
    for l in lines:
        assert not any(c.isdigit() for c in l.get("say", l["text"])), l["text"]
        if l.get("dialogue"):
            assert l.get("speaker", 1) != 1 and not l.get("em")
        for w in l.get("em", []):
            assert w in l["text"], w
    assert len(title) <= 14 and not RISKY.search(title + t1 + t2 + bar), title
    wk = os.path.join(ROOT, "work", slug)
    assert not os.path.exists(os.path.join(wk, "script.json")) or json.load(open(os.path.join(wk, "script.json")))["source"] == source, f"{slug} 슬러그 충돌"
    lk = os.path.expanduser(f"~/Desktop/kim/ssul/work/{slug}")
    assert not os.path.exists(lk) or os.path.islink(lk), f"{slug}: ssul/work 실폴더와 겹침"
    os.makedirs(os.path.join(wk, "v2", "ai"), exist_ok=True)
    SK = ("sh", "ch", "fx", "pop", "shake", "info")
    sc_lines = [{**{k: v for k, v in l.items() if k not in SK}, "img": 1} for l in lines]
    sc_lines.append({"text": "구독!", "emotion": "toneup", "intensity": 2.0, "outro": True, "img": 1})
    sc = {"slug": slug, "type": typ, "source": source,
          "title_line1": t1, "title_line2": t2, "hook": bar, "channel": "란빵",
          "voice": "main", "tts_engine": "myvoice", "myvoice": "경모", "myvoice_narration": "talk1",
          "style": {"sub_box": True, "bar": bar, "bar_count": None, "watermark": ""}, "lines": sc_lines}
    json.dump(sc, open(os.path.join(wk, "script.json"), "w"), ensure_ascii=False, indent=2)
    texts = [l["text"].rstrip(".") for l in sc_lines]
    shot_lines, names = [], set()
    for i, l in enumerate(lines):
        d = {"shots": l["sh"]}
        if l.get("ch") and not NO_CHAR:
            d["char"] = l["ch"] if isinstance(l["ch"], list) else [l["ch"]]
            names |= {c["name"] for c in d["char"]}
        if l.get("fx"):
            d["sfx"] = [list(x) for x in l["fx"]]
        for k in ("pop", "shake", "info"):
            if l.get(k):
                d[k] = list(l[k]) if k == "pop" else l[k]
        ws = [s.get("at") for s in d["shots"]] + [x[1] for x in d.get("sfx", [])] + [d.get("shake")]
        ws += [c.get("at") for c in d.get("char", [])]
        ws += [d["pop"][2]] if "pop" in d else []
        if "info" in d:
            ws += [d["info"].get("at")] + [it.get("at") for it in d["info"]["items"]]
        for w in ws:
            if w and w.startswith("+1:"):
                w = w[3:]
            assert not w or w in texts[i], (slug, i, w, texts[i])
        for s in d["shots"]:
            k = s.get("img", "")
            assert not k.startswith("ai/") or k[3:-4] in AIP, (slug, k)
        shot_lines.append(d)
    outro = {"shots": outro_sh, "sfx": [["pop_long", "구독!"]], "pop": ["구독!", "#FFE629", "구독!"]}
    if not NO_CHAR:
        outro["char"] = [C("hakusyu", "l")]
        names.add("hakusyu")
    shot_lines.append(outro)
    json.dump({"bgmVol": 0.09, "bgm": "bgm/sneaky-123.mp3", "lines": shot_lines},
              open(os.path.join(wk, "v2", "shots.json"), "w"), ensure_ascii=False, indent=1)
    with open(os.path.join(wk, "v2", "ai_prompts.tsv"), "w") as f:
        for k, p in AIP.items():
            f.write(f"{k}\t{p}\n")
    AIP = {}
    irc = ir_fetch(slug, names)
    chs = f"いらすとや {len(irc)}장({', '.join(irc)})" if irc else "없음"
    rows = "\n".join(f"| {a} | {b} |" for a, b in proof)
    open(os.path.join(wk, "upload.md"), "w").write(
        f"# {slug}: 업로드 메타 (란빵)\n\n## 제목\n\n{title}\n\n## 설명\n\n{desc}\n\n"
        f"## 고정 댓글\n\n{comment}\n\n## 쇼핑태그\n\n{tags}\n\n"
        f"## 근거표\n\n| 대본 내용 | 근거 |\n|---|---|\n{rows}\n\n{extra}\n\n"
        f"화면: 배경 = codex(gen.sh luna) 실사풍 생성, 캐릭터 = {chs}.\n")
    if not os.path.lexists(lk):
        os.symlink(wk, lk)
    print("ok", slug, len(sc_lines), "lines,", len(irc), "chars,", len(json.load(open(os.path.join(wk, "v2", "shots.json")))["lines"]), "shot lines")


def EP_daisohazard():
    S = "daisohazard"
    lines = [
        L("폭우 쏟아지는 다이소 주차장 한가운데, 비상등 켠 그랜저가 서 있음.",
          [B("d01", "A dark gray Korean full-size sedan stopped in the middle of the driving aisle of a crowded outdoor supermarket parking lot during heavy rain, orange hazard lights blinking, wet asphalt reflections, overcast day, seen from the driver seat of a car behind through a rainy windshield"),
           B("d01", at="비상등", s0=1.5, s1=1.7, fx=0.55, fy=0.55, punch=True)],
          C("drv_shock"), em=["비상등"], em_color="yellow", fx=[("hit_trailer_epic", "비상등", 0.4)]),
        L("차 안엔 아무도 없고, 뒤에 차 네 대가 갇혀서 꼼짝도 못 함.",
          [B("d02", "Four cars waiting in a line inside a narrow parking lot aisle in heavy rain, headlights on, a sedan with hazard lights blocking the front, wide shot from slightly above"),
           B("d02", at="네 대", s0=1.3, s1=1.45, fx=0.4, fy=0.6)],
          C("drv_angry"), em=["네 대"], fx=[("wrong_gameshow_buzz", "꼼짝도", 0.4)]),
        L("남편은 아내가 차를 갖고 나갔다는데, 비 맞으며 5분 넘게 기다림.",
          [B("d03", "A smartphone mounted on a car dashboard during an outgoing phone call, screen blurred, heavy rain streaming down the windshield, wipers moving, hazy hazard lights ahead"),
           B("d04", "Close-up of rain pouring on a car windshield with wiper blades, blurry orange hazard lights of a blocking sedan ahead, gloomy", at="5분")],
          C("drv_cry"), say="남편은 아내가 차를 갖고 나갔다는데, 비 맞으며 오분 넘게 기다림.", em=["5분"], em_color="yellow"),
        L("아내 차주가 장 본 걸 들고 와서 아무 말 없이 조수석에 던지고 탐.",
          [B("d05", "Plastic shopping bags full of household goods thrown onto the passenger seat of a car, door open, rain outside, interior shot"),
           B("d05", at="던지고", s0=1.4, s1=1.6, fx=0.5, fy=0.55, punch=True)],
          C("bag_woman", "r"), em=["아무 말 없이"], fx=[("drum_rimshot", "던지고", 0.4)]),
        L("사과할 줄 모르세요?", [B("d02", s0=1.2, s1=1.35, fx=0.6, fy=0.5)], C("drv_angry"),
          dialogue=True, speaker=2, emotion="toneup"),
        L("뭐요? 제가 왜요?", [B("d01", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("ignore", "r"),
          dialogue=True, speaker=3, emotion="toneup", fx=[("scratch_vinyl", "제가", 0.5)], pop=("제가 왜요?", R, "제가")),
        L("그러고는 주차도 못 하고 왔다 갔다 하면서 또 길을 막음.",
          [B("d06", "A dark gray sedan awkwardly half-turned across a parking aisle trying to park, blocking other cars, heavy rain, reverse lights on"),
           B("d06", at="또 길을", s0=1.3, s1=1.5, fx=0.5, fy=0.5)],
          C("drv_surprise"), em=["또 길을 막음"]),
        L("참다못한 글쓴이가 우산 쓰고 그 차 앞을 딱 막아섬.",
          [B("d07", "Low angle view: a black umbrella held in front of a sedan's glowing headlights in pouring rain in a parking lot, umbrella seen from behind, dramatic"),
           B("d07", at="막아섬", s0=1.0, s1=1.2, punch=True)],
          C("umbrella"), em=["막아섬"], em_color="yellow", pop=("막아섬!!", Y, "막아섬"), shake="막아섬",
          fx=[("boom_zoom_impact", "막아섬", 0.6)]),
        L("그리고 수신호로 갇혀 있던 차들을 전부 먼저 빼줌.",
          [B("d08", "Cars driving out of a rainy parking lot one after another toward the exit, headlights and wet reflections, calm"),
           B("d08", at="전부", s0=1.2, s1=1.35, fx=0.6, fy=0.5)],
          C("seiri"), em=["전부 먼저"], fx=[("correct_ding", "전부", 0.5)]),
        L("근데 댓글은 사이다라는 쪽이랑, 차 앞 막은 것도 잘못이라는 쪽으로 갈림.",
          [B("d07", s0=1.3, s1=1.15, fx=0.5, fy=0.4)], C("biz_think", "r"),
          info={"kind": "compare", "at": "사이다", "title": "댓글 반응", "items": [
              {"label": "사이다", "color": Y, "at": "사이다", "rows": [["추천", "402", "#7CFF6B"]]},
              {"label": "막은 것도 잘못", "color": W, "at": "잘못이라는", "rows": [["추천", "6", R]]}]}),
        L("님들은 차 앞 막아선 거 잘했다고 봄?", [B("d01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "비 오는 주차장 한가운데", "비상등 켜고 사라진 차주", "다이소 주차장, 차 4대 가둔 그랜저",
          "#주차장 비상등 빌런", "보배드림 베스트 1040923 (2026-10-19, 추천 1,294, 댓글 122)",
          [("서울 동작구 다이소 주차장, 폭우 속 주차장 한가운데 비상등 켠 그랜저, 차 안에 사람 없음", "원글 본문"),
           ("뒤에 4대 출차 못 함, 5분 넘게 대기, 남편이 '아내가 갖고 나갔다'", "원글 본문"),
           ("아내가 물건을 조수석에 던지고 탐, '사과할 줄 모르세요?' / '뭐요? 제가 왜요?'", "원글 본문"),
           ("우산 쓰고 차 앞을 막고 수신호로 다른 차를 먼저 뺌", "원글 본문"),
           ("댓글 추천 402 '사과할 인성이면 애초에…' vs 추천 6 '차 막은 남도 도찐개찐'", "원글 댓글")],
          "비 오는 날 주차장 한가운데 비상등만 켜고 사라진 차주.\n차 4대가 갇혔는데 돌아온 한마디는 \"제가 왜요?\"\n님들은 차 앞을 막아선 게 맞다고 보시나요?\n\n#주차장 #주차빌런 #비상등 #보배드림 #란빵",
          "님들은 차 앞 막아선 거 잘했다고 봄?",
          "차량용 우산꽂이, 주차번호판, 자동차 블랙박스 2채널, 블랙박스 메모리카드, 김서림방지제",
          "", [B("d08", s0=1.0, s1=1.1)])


def EP_ebike500():
    S = "ebike500"
    lines = [
        L("휀더 살짝 찍힌 거, 렌트비까지 500만원 주세요.", [B("e02", "Extreme close-up of a small dent above the headlight on the front fender of an old black American full-size sedan, several older scratches around, parking lot daylight", s0=1.3, s1=1.5, fx=0.5, fy=0.45)],
          C("rage", "r"), dialogue=True, speaker=2, emotion="toneup", say="휀더 살짝 찍힌 거, 렌트비까지 오백마넌 주세요."),
        L("아내가 전기자전거 타다 넘어지면서 07년식으로 보이는 크라이슬러 300C를 찍었음.",
          [B("e01", "An electric bicycle fallen on its side on asphalt right next to the front fender of a parked old black Chrysler 300C style sedan, roadside daytime"),
           B("e01", at="300C", s0=1.3, s1=1.5, fx=0.6, fy=0.5, punch=True)],
          C("bike_slip"), say="아내가 전기자전거 타다 넘어지면서 공칠년식으로 보이는 크라이슬러 삼백씨를 찍었음.",
          em=["300C"], fx=[("glass_smash", "찍었음", 0.35)]),
        L("찍힌 자국은 헤드램프 위에 손톱만 한데, 원래 긁힌 자국도 여기저기 있었음.",
          [B("e02", s0=1.0, s1=1.15), B("e02", at="원래", s0=1.5, s1=1.7, fx=0.35, fy=0.55)],
          C("biz_think"), em=["손톱만 한데"]),
        L("근데 차주가 렌트비 포함 합의금 500만원을 요구함.",
          [B("e03", "Korean 50000 won banknotes fanned out on a car hood next to a car key, close-up, daylight")],
          C("bill_shock"), say="근데 차주가 렌트비 포함 합의금 오백마넌을 요구함.", em=["500만원"], em_color="yellow",
          fx=[("drop_futuristic", "500만원", 0.5)],
          info={"kind": "counter", "at": "500만원", "title": "요구 합의금",
                "items": [{"num": 500, "suffix": "만원", "label": "렌트비 포함", "at": "500만원"}]}),
        L("견적서는? 서비스센터에 전화해서 너희가 직접 뽑아보라고 함.",
          [B("e04", "Empty reception counter of an imported car service center, clean showroom floor, waiting chairs"),
           B("e04", at="너희가", s0=1.3, s1=1.45, fx=0.5, fy=0.55)],
          C("ignore", "r"), em=["너희가 직접"], fx=[("scratch_vinyl", "너희가", 0.45)]),
        L("댓글에선 그 연식이면 차값이랑 비슷하겠다는 말까지 나옴.",
          [B("e05", "An old black American full-size sedan parked in a Korean used car lot among other used cars, slightly faded paint, daytime"),
           B("e05", at="차값", s0=1.3, s1=1.5, fx=0.5, fy=0.55, punch=True)],
          C("wow", "r"), em=["차값"], em_color="yellow", pop=("차값?!", Y, "차값")),
        L("게다가 전기자전거라 일상생활 배상책임보험도 안 된다고 들었다고 함.",
          [B("e06", "An insurance policy booklet and contract papers on a desk with a pen and calculator, close-up, documents blurred, no readable text")],
          C("biz_shock"), em=["배상책임보험"]),
        L("근데 손해배상은 원래 통상의 손해까지만 물어주는 게 원칙임.",
          [B("e06", s0=1.3, s1=1.45, fx=0.4, fy=0.5)], C("lawyer"), em=["통상의 손해"], em_color="yellow",
          info={"kind": "quotes", "items": [{"text": "“손해배상은 통상의 손해를 그 한도로 한다”", "at": "통상의"}]}),
        L("심지어 300C는 휀더 부품값이 유독 싸다는 댓글까지 올라옴.",
          [B("e07", "A new unpainted car front fender panel lying on a workbench in an auto body repair shop, tools around"),
           B("e07", at="유독", s0=1.3, s1=1.45, fx=0.5, fy=0.5)],
          C("biz_idea"), say="심지어 삼백씨는 휀더 부품값이 유독 싸다는 댓글까지 올라옴.", em=["유독 싸다"], fx=[("correct_ding", "유독", 0.5)]),
        L("님들은 이거 얼마 물어주는 게 맞다고 봄?", [B("e01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "전기자전거로 찍힌 300C", "합의금 500만원 요구", "자국은 손톱만 한데 합의금이",
          "#자전거로 찍힌 300C", "보배드림 베스트 1041030 (2026-10-19, 추천 709, 댓글 143)",
          [("아내가 전기자전거 타다 넘어져 크라이슬러 300C(글쓴이 추정 07년식) 앞 휀더를 찍음", "원글 본문"),
           ("자국 작고 기존 긁힘 여러 개", "원글 첨부 사진"),
           ("렌트비 포함 합의금 500만원 요구, 견적서는 서비스센터에 전화해 직접 뽑으라 함", "원글 본문"),
           ("전기자전거라 일상생활배상책임보험 적용 안 된다고 들음", "원글 본문(글쓴이 주장, 약관 확인 안 됨, 대본도 '들었다고 함')"),
           ("'저 차량 가격이 500은 할 듯' (추천 186), '300c 휀다 부품 저렴' (추천 166)", "원글 댓글"),
           ("손해배상은 통상의 손해를 그 한도로 한다", "민법 제393조 1항(제763조로 불법행위에 준용), 국가법령정보센터")],
          "전기자전거가 넘어지며 찍은 손톱만 한 자국.\n차주가 요구한 합의금은 렌트비 포함 500만원.\n님들은 얼마 물어주는 게 맞다고 보시나요?\n\n#전기자전거 #합의금 #자동차사고 #보배드림 #란빵",
          "님들은 이거 얼마 물어주는 게 맞다고 봄?",
          "자전거 헬멧, 자동차 스크래치 리무버, 차량용 컴파운드, 자동차 블랙박스 2채널, 블랙박스 메모리카드",
          "", [B("e05", s0=1.0, s1=1.1)])


def EP_daerifault():
    S = "daerifault"
    lines = [
        L("손님 때문에 경로 벗어났으니까, 손님 과실도 50%예요.",
          [B("f03", "Close-up of a scraped and scuffed silver alloy wheel and bumper corner of a car stopped against a concrete curb at night, street light", s0=1.2, s1=1.4)],
          C("busdrv", "r"), dialogue=True, speaker=2, emotion="toneup", say="손님 때문에 경로 벗어났으니까, 손님 과실도 오십 퍼센트예요."),
        L("새벽에 술 마시고 대리를 불렀는데, 동승자 먼저 내려준다고 미리 말해 뒀음.",
          [B("f01", "View from the back seat of a car driving through a Korean city street at night, neon lights blurred through the windshield, driver seat out of focus and empty"),
           B("f01", at="미리", s0=1.3, s1=1.45, fx=0.5, fy=0.45)],
          C("daikou"), em=["미리 말해"]),
        L("동승자가 가방을 두고 내렸다는 전화에, 기사가 먼저 가져다주자고 함.",
          [B("f02", "A woman's handbag left on the back seat of a car at night, dim interior light, close-up")],
          C("busdrv", "r"), em=["기사가 먼저"]),
        L("그런데 내비 찍으려고 갓길에 세우다가 휠이랑 범퍼를 연석에 쫙 긁음.",
          [B("f04", "A car pulling over to the roadside at night with hazard lights on, its front wheel touching a high concrete curb"),
           B("f03", at="연석", s0=1.0, s1=1.25, punch=True)],
          C("drv_shock"), em=["연석"], em_color="yellow", shake="긁음", fx=[("glass_smash", "긁음", 0.4)]),
        L("처음엔 죄송하다, 보험처리 해주겠다고 했음.",
          [B("f04", s0=1.2, s1=1.35, fx=0.4, fy=0.5)], C("busdrv_bow", "r"), em=["보험처리"]),
        L("근데 다음 날 온 문자는 손님 과실 50%, 휠 복원비 8만원 줄 테니 끝내자.",
          [B("f05", "A smartphone lying on a bedside table in the morning light showing a new text message notification, screen blurred and unreadable"),
           B("f05", at="8만원", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)],
          C("bill_shock"), say="근데 다음 날 온 문자는 손님 과실 오십 퍼센트, 휠 복원비 팔마넌 줄 테니 끝내자.",
          em=["8만원"], em_color="yellow", fx=[("notify_message_pop", "다음", 0.5), ("drop_futuristic", "8만원", 0.5)],
          info={"kind": "counter", "at": "8만원", "title": "기사 측 제안", "items": [{"num": 8, "suffix": "만원", "label": "휠 복원비만", "at": "8만원"}]}),
        L("하룻밤 사이에 말이 완전히 바뀐 거임.",
          [B("f03", s0=1.5, s1=1.7, fx=0.45, fy=0.55)], C("drv_angry"), em=["완전히"], pop=("말 바꿈?!", R, "바뀐"),
          fx=[("scratch_vinyl", "바뀐", 0.5)]),
        L("댓글은 연석 긁은 건 운전한 기사 책임이라는 의견이 압도적.",
          [B("f04", s0=1.1, s1=1.2)], C("biz_angry", "r"), em=["기사 책임"]),
        L("그래서 기사 말고 대리업체 보험으로 접수하라는 조언이 1위였음.",
          [B("f06", "Car insurance claim forms and a car key on an office desk, close-up, text blurred")],
          C("hoken"), say="그래서 기사 말고 대리업체 보험으로 접수하라는 조언이 일위였음.", em=["대리업체 보험"], em_color="yellow",
          fx=[("correct_ding", "대리업체", 0.5)]),
        L("민법도 사람을 써서 일 시킨 쪽에 배상 책임을 물림.",
          [B("f06", s0=1.3, s1=1.45, fx=0.45, fy=0.5)], C("lawyer"), em=["일 시킨 쪽"]),
        L("님들은 8만원 받고 끝냄, 아니면 끝까지 감?", [B("f01", s0=1.0, s1=1.12)], C("biz_q"),
          say="님들은 팔마넌 받고 끝냄, 아니면 끝까지 감?", fx=[("pop_bubble", "감")]),
    ]
    build(S, lines, "대리기사가 휠 긁고", "하룻밤 만에 손님 과실 50%", "보험처리 해준다더니 다음 날 문자",
          "#대리기사 말 바꾸기", "보배드림 베스트 1040990 (2026-10-19, 추천 237, 댓글 33)",
          [("새벽 음주 후 대리 호출, 동승자 먼저 내린다고 콜센터에 미리 알림", "원글 본문"),
           ("동승자 가방 두고 내림, 기사가 먼저 가져다주겠다고 함", "원글 본문"),
           ("내비 찍으려 갓길 정차 중 옆범퍼, 휠을 연석에 긁음, 처음엔 사과하고 보험처리 약속", "원글 본문"),
           ("일행이 '손님 때문에 경로 벗어남, 손님 과실' 주장, 다음 날 문자 '손님 과실 50%, 휠 복원비 8만원'", "원글 본문"),
           ("'대리업체랑 얘기하세요 사고접수 보험처리' (추천 36), 기사 100% 과실 의견 다수", "원글 댓글"),
           ("타인을 사용해 사무에 종사하게 한 자는 피용자가 사무집행에 관해 가한 손해 배상 책임", "민법 제756조 1항, 국가법령정보센터(대리업체와 기사가 사용관계인지는 사안마다 다름, 확인 안 됨)")],
          "대리기사가 연석에 휠을 긁고 처음엔 보험처리 해주겠다던 상황.\n하룻밤 만에 온 문자는 손님 과실 50%, 8만원 줄 테니 끝내자.\n님들은 이 제안 받으시나요?\n\n#대리운전 #대리기사 #자동차사고 #보배드림 #란빵",
          "님들은 8만원 받고 끝냄, 아니면 끝까지 감?",
          "휠 기스 복원 키트, 휠 프로텍터, 자동차 블랙박스 2채널, 블랙박스 메모리카드, 음주측정기",
          "", [B("f01", s0=1.0, s1=1.1)])


def EP_taxibox():
    S = "taxibox"
    lines = [
        L("블랙박스에 사고 장면이 안 찍혔네요.",
          [B("g03", "A dashcam memory card next to a laptop on a desk at night, video player window on screen blurred, desk lamp", s0=1.2, s1=1.35)],
          C("biz_tehe", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("부산 개금사거리 근처, 아버지가 2차로로 멀쩡히 달리고 있었음.",
          [B("g01", "Driver's point of view on a busy multi-lane city road in Busan, South Korea, daytime, apartment buildings and hills in the background, lane markings visible")],
          C("drv_smile"), say="부산 개금사거리 근처, 아버지가 이차로로 멀쩡히 달리고 있었음.", em=["2차로"]),
        L("그런데 우회전으로 들어온 택시가 2차로까지 확 끼어들며 옆을 들이받음.",
          [B("g02", "A Korean taxi cutting sharply from the right lane into the next lane and scraping the side of a sedan, motion blur, city road daytime, seen from the sedan's driver window"),
           B("g02", at="들이받음", s0=1.2, s1=1.4, punch=True)],
          C("drv_shock"), say="그런데 우회전으로 들어온 택시가 이차로까지 확 끼어들며 옆을 들이받음.",
          em=["2차로까지"], em_color="yellow", shake="들이받음", fx=[("boom_zoom_impact", "들이받음", 0.6)]),
        L("택시는 아버지가 3차로로 차선 바꾸던 중이었다며 6대 4를 주장함.",
          [B("g04", "A Korean taxi stopped far down the road with hazard lights on after an accident, city street daytime")],
          C("taxi", "r"), say="택시는 아버지가 삼차로로 차선 바꾸던 중이었다며 육대사를 주장함.", em=["6대 4"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "6대", 0.45)]),
        L("황당한 건 우리 보험사 직원까지 택시 영상만 보고 똑같이 말함.",
          [B("g05", "An insurance company office desk with a monitor showing a blurred dashcam video, empty chair, fluorescent light")],
          C("biz_shock"), em=["우리 보험사"], pop=("우리 편이?!", R, "우리"), fx=[("scratch_vinyl", "똑같이", 0.45)]),
        L("결국 타지 사는 아들이 부산까지 내려가서 블박을 직접 뒤져봄.",
          [B("g03", s0=1.0, s1=1.15), B("g06", "Close-up of a hand-free car dashcam mounted behind the rear-view mirror, with the memory card slot open, morning light", at="직접")],
          C("biz_think", "r"), em=["직접"]),
        L("사고 영상은 바로 나왔고, 아버지는 처음부터 끝까지 2차로였음.",
          [B("g01", s0=1.2, s1=1.35, fx=0.45, fy=0.6), B("g02", at="처음부터", s0=1.0, s1=1.15)],
          C("banzai"), say="사고 영상은 바로 나왔고, 아버지는 처음부터 끝까지 이차로였음.", em=["2차로였음"], em_color="yellow",
          fx=[("correct_ding", "바로", 0.5)]),
        L("그러자 택시는 슬쩍 8대 2로 말을 바꿈.",
          [B("g04", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("taxi", "r"), say="그러자 택시는 슬쩍 팔대이로 말을 바꿈.",
          em=["8대 2"], em_color="yellow",
          info={"kind": "bars", "title": "택시 측 주장", "items": [
              {"label": "처음", "value": 0.6, "num": 6, "suffix": " : 4", "color": "#fff"},
              {"label": "블박 나온 뒤", "value": 0.8, "num": 8, "suffix": " : 2", "color": Y, "at": "8대"}]}),
        L("8대 2로 하시든지, 자차로 처리하고 구상하세요.",
          [B("g05", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_tehe", "r"), dialogue=True, speaker=3, emotion="normal",
          say="팔대이로 하시든지, 자차로 처리하고 구상하세요."),
        L("그런데 이건 우리 보험사가 한 말임.", [B("g05", s0=1.5, s1=1.7, fx=0.4, fy=0.5)], C("drv_angry"),
          em=["우리 보험사"], em_color="yellow", fx=[("hit_trailer_epic", "우리", 0.45)]),
        L("님들은 이거 몇 대 몇 나와야 한다고 봄?", [B("g01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "택시가 들이받았는데", "우리 보험사가 8대 2 하래", "아들이 블박 직접 뒤져서 찾아냄",
          "#우리 보험사 맞음?", "보배드림 베스트 1041125 (2026-10-19, 추천 26, 댓글 16)",
          [("10/12 부산 개금사거리 부근, 아버지 2차로 주행 중 우회전 진입 택시가 2차로까지 끼어들며 충돌", "원글 본문"),
           ("아버지 측 보험 담당자 '블박에 사고 장면 안 찍힘', 택시 '3차로 변경 중' 6:4 주장, 우리 보험사 직원도 동조", "원글 본문"),
           ("아들이 부산에 내려가 블박 확인, 사고 영상 바로 나옴, 계속 2차로", "원글 본문"),
           ("택시 측 8:2 주장, 우리 보험사 '8:2로 하든지 자차 처리하고 구상'", "원글 본문")],
          "택시가 끼어들며 들이받았는데 우리 보험사까지 상대 편을 든 상황.\n아들이 직접 블박을 뒤져 2차로 주행 영상을 찾아냈지만 돌아온 답은 8대 2.\n님들은 몇 대 몇이 맞다고 보시나요?\n\n#과실비율 #블랙박스 #택시사고 #보배드림 #란빵",
          "님들은 이거 몇 대 몇 나와야 한다고 봄?",
          "자동차 블랙박스 2채널, 블랙박스 메모리카드 128GB, 블랙박스 보조배터리, SD카드 리더기, 사이드미러 광각거울",
          "반응 수치(추천 26)는 낮지만 반전 구조로 선정.", [B("g02", s0=1.0, s1=1.1)])


if __name__ == "__main__":
    for name in sys.argv[1:] or [k[3:] for k in list(globals()) if k.startswith("EP_")]:
        globals()["EP_" + name]()
