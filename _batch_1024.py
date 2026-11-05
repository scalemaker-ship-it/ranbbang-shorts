#!/usr/bin/env python3
"""란빵 2026-10-24: 보배드림 베스트 6편 + 신차 출시 4편 (10/25 12:00~21:00 10칸).
- 화면 = GPT 리얼 배경(gen.sh luna, 사람 없음) + いらすとや 캐릭터. 헬퍼 _batch_1020.py, IR 추가분 _batch_1021.py.
- 보배드림 근거 = work/research_bobae_1024.md (조사 에이전트: 본문, 댓글 전체, 첨부 판독).
  golfclub 1041735 / tire80 1042025 / oildrain 1042351 / repair740 1042121 / outcar64 1042070 / leftturn91 1041751.
- 상호(타이어뱅크, 공임나라), 지점, 지역은 대본에 안 씀. 법 수치는 확인된 것만(도로교통법 32조, 형법 283조).
- 신차 4편 근거 = work/research_newcar_1024.md. 차 화면 = 제조사 공식 사진(P), AI 배경은 차 없는 장면만.
"""
import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1021 import B, C, L, build, IR, Y, W, R   # noqa: E402
from _batch_1020 import P   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))

IR.update({
    "golf": ("ゴルフ 男性", "golf_ojisan.png"), "oil_seibishi": ("オイル交換", "car_oil_koukan_seibishi.png"),
    "meiwaku": ("駐車違反 車", "car_meiwaku_chusya.png"), "photo_woman": ("スマートフォン 撮影 女性", "smartphone_photo_woman_tate.png"),
    "kousaten": ("交差点 車", "car_douro_kousaten_shingou.png"),
})


def real(slug, folder, picks):
    """picks = {이름: (원본 파일, 가로 중심 0~1)} → work/<slug>/v2/real/<이름>.jpg 1080x960(9:8)."""
    d = os.path.join(ROOT, "work", slug, "v2", "real")
    os.makedirs(d, exist_ok=True)
    for n, (src, cx) in picks.items():
        im = Image.open(os.path.join(ROOT, "work", "_photos", folder, src + ".jpg")).convert("RGB")
        w, h = im.size
        cw = int(h * 9 / 8)
        if cw > w:
            ch = int(w * 8 / 9); y = (h - ch) // 2
            im = im.crop((0, y, w, y + ch)); w, h = im.size; cw = w
        x = min(max(int(w * cx - cw / 2), 0), w - cw)
        im.crop((x, 0, x + cw, h)).resize((1080, 960), Image.LANCZOS).save(os.path.join(d, n + ".jpg"), quality=92)


# ───────────────────────── 보배드림 ─────────────────────────

def EP_golfclub():
    S = "golfclub"
    lines = [
        L("너무 무서워서 버스를 탈 수가 없어요.",
          [B("g01", "A Korean bus stop sign on a narrow sidewalk in an industrial complex street, a black sedan parked right beside the sign on the sidewalk, grey morning, no people", s0=1.1, s1=1.3)],
          C("photo_woman", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("버스 정류장 표지판 바로 옆 인도에 매일 차를 세우는 가게 사장이 있었음.",
          [B("g01", at="매일", s0=1.3, s1=1.5, fx=0.6, fy=0.5, punch=True)], C("meiwaku"), em=["매일"]),
        L("출퇴근마다 도로로 내려가서 버스를 타야 하니까 안전신문고에 신고함.",
          [B("g02", "A smartphone held up showing a civic report app with a photo upload screen, screen content blurred, a bus stop and a parked black sedan in the background, morning")],
          C("bag_woman", "r"), em=["안전신문고"], em_color="yellow", fx=[("notify_message_pop", "신고함", 0.5)]),
        L("신고 직후엔 주차를 안 하더니, 10월 초부터 그 사장이 골프채를 들고 도로를 돌아다님.",
          [B("g03", "A single golf driver club leaning against a shuttered small shop front on an empty industrial-area street, overcast daytime, no people"),
           B("g03", at="골프채를", s0=1.3, s1=1.55, fx=0.45, fy=0.5, punch=True)],
          C("golf", "r"), say="신고 직후엔 주차를 안 하더니, 시월 초부터 그 사장이 골프채를 들고 도로를 돌아다님.",
          em=["골프채를"], pop=("골프채?!", R, "골프채를"), fx=[("hit_trailer_epic", "골프채를", 0.5)]),
        L("골프채를 일부러 바닥에 끌면서 사람들 앞을 지나다님.",
          [B("g04", "Low angle of an asphalt road surface with a long fresh scratch line, an empty bus stop in the distance, dusk, no people")],
          C("golf", "r", flip=True), em=["끌면서"], fx=[("swipe_metal", "끌면서", 0.4)]),
        L("사진 찍고 다니는 게 당신이야?",
          [B("g04", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("rage", "r"), dialogue=True, speaker=3, emotion="toneup"),
        L("통화 중인 글쓴이 옆에서 전화가 끝날 때까지 기다리기까지 함.",
          [B("g05", "An empty bus stop bench in an industrial complex at dusk, long shadows, a factory wall behind, no people")],
          C("komatta"), em=["기다리기까지"]),
        L("경찰서에 갔더니 또 골프채 들고 그러면 연락 달라는 답만 들음.",
          [B("g06", "An empty police station front counter with a bell and forms on it, fluorescent light, Korean interior, no people")],
          C("police", "r"), em=["연락 달라는"], em_color="yellow", fx=[("wrong_gameshow_buzz", "답만", 0.45)]),
        L("정류장 10미터 안과 인도 주차는 도로교통법 32조 위반, 협박죄는 3년 이하 징역임.",
          [B("g01", s0=1.0, s1=1.15)], C("judge", "r"),
          say="정류장 십미터 안과 인도 주차는 도로교통법 삼십이조 위반, 협박죄는 삼년 이하 징역임.",
          em=["3년 이하 징역"], em_color="yellow", fx=[("drop_futuristic", "협박죄는", 0.5)],
          info={"kind": "compare", "at": "정류장", "title": "관련 법", "items": [
              {"label": "정류장 10m, 인도 주차", "color": W, "at": "정류장", "rows": [["도로교통법", "32조", Y]]},
              {"label": "협박죄", "color": R, "at": "협박죄는", "rows": [["형법 283조", "3년 이하", Y]]}]}),
        L("글쓴이는 지금 휴대폰 녹화를 켠 채 정류장에 나가고 있음.",
          [B("g05", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("photo_woman"), em=["녹화를"], fx=[("shutter_digital", "녹화를", 0.45)]),
        L("님들은 이럴 때 신고 계속함, 아니면 잠깐 멈춤?", [B("g02", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "멈춤")]),
    ]
    build(S, lines, "불법주차 신고했더니", "골프채 들고 나타난 사장", "정류장 옆 상습주차 신고 후 차주가 골프채 들고 배회",
          "#주차 신고하자 골프채", "보배드림 베스트 1041735 (2026-10-22, 추천 726, 댓글 113)",
          [("정류장 표지판 옆 인도에 상습 주차하는 인근 가게 사장 차, 글쓴이가 안전신문고 신고", "원글 본문, 사진 3장"),
           ("10월 초부터 차주가 '범인 잡겠다'며 골프채 들고 도로 배회, 바닥에 끌며 지나다님", "원글 본문"),
           ("10/21 '사진 찍고 다니냐' 위협적 질문, 통화 끝날 때까지 옆에서 대기", "원글 본문(대사는 간접인용을 대사체로 각색)"),
           ("경찰 '또 골프채 들고 그러면 연락 달라', CCTV, 목격자 없음(공단)", "원글 본문, 본인 댓글"),
           ("도로교통법 제32조 보도, 정류장 10m 이내 주정차 금지 / 형법 제283조 협박 3년 이하 징역 또는 500만원 이하 벌금", "국가법령정보센터 원문"),
           ("10/22 휴대폰 녹화 켠 채 정류장으로, 앞 가게 CCTV 신설", "원글 추가 본문"),
           ("'너무 무서워서, 버스를 탈 수가 없어요'", "원글 본문")],
          "버스정류장 옆 인도 상습주차를 신고했더니, 차주가 골프채를 들고 길을 돌아다닙니다.\n경찰은 또 그러면 연락 달라는 답만. 글쓴이는 녹화를 켠 채 정류장에 나갑니다.\n정류장 10m 안 주차는 도로교통법 32조 위반입니다.\n\n#불법주차 #안전신문고 #버스정류장 #보배드림 #란빵",
          "님들은 이럴 때 신고 계속함, 아니면 잠깐 멈춤?",
          "자동차 블랙박스 2채널, 보조배터리 블랙박스, 호신용 경보기, 차량용 핸드폰 거치대, 차량용 방향제",
          "댓글이 지역을 지목했으나 미확인, 대본엔 지역 없음. 폭행은 없었고 위협, 배회만.", [B("g03", s0=1.0, s1=1.1)])


def EP_tire80():
    S = "tire80"
    lines = [
        L("제일 저렴한 게 두 개 해서 50만 2천원입니다.",
          [B("t01", "Interior of a large franchise tire shop: racks of new tires with price tags blurred, a service bay in the background, bright lighting, no people", s0=1.1, s1=1.3)],
          C("sales", "r"), dialogue=True, speaker=2, emotion="normal", say="제일 저렴한 게 두 개 해서 오십만 이처넌입니다."),
        L("운전 경력 짧은 동생이 타이어가 터져서 근처 대형 타이어 매장에 들어감.",
          [B("t02", "An old silver Korean full-size sedan with a flat front tire pulled over at a roadside, a tire shop sign blurred in the background, daytime, no people")],
          C("drv_cry"), em=["터져서"], fx=[("boom_subby_kick", "터져서", 0.45)]),
        L("매장은 네 짝 교체를 권했고, 개당 26만 5천원, 네 개 하면 79만 5천원이라 함.",
          [B("t01", at="개당", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)], C("carshop", "r"),
          say="매장은 네 짝 교체를 권했고, 개당 이십육만 오처넌, 네 개 하면 칠십구만 오처넌이라 함.",
          em=["79만 5천원"], em_color="yellow", fx=[("drop_futuristic", "79만", 0.5)],
          info={"kind": "counter", "at": "79만", "title": "매장 견적 (타이어 4개)", "items": [{"num": 795000, "suffix": "원", "label": "전용 상품, 3+1", "at": "79만"}]}),
        L("정비업 하는 형이 전화해서, 앞 두 개만 제일 싼 걸로 해달라고 함.",
          [B("t03", "A smartphone lying on a steel workbench in a car repair shop showing a call screen, screen blurred, tools around, no people")],
          C("phone_man"), em=["제일 싼"]),
        L("그런데 가장 싼 게 두 개에 50만원이 넘는다는 답.",
          [B("t01", s0=1.4, s1=1.6, fx=0.5, fy=0.45)], C("bill_shock"), say="그런데 가장 싼 게 두 개에 오십마넌이 넘는다는 답.",
          pop=("50만원?!", R, "50만원이"), fx=[("wrong_gameshow_buzz", "50만원이", 0.45)]),
        L("거부하니까 매장은 원상복구하고 공임만 받겠다며 10만원을 받음.",
          [B("t04", "An old worn tire being remounted on a silver sedan's wheel hub in a shop bay, a lug wrench on the floor, no people")],
          C("seibishi", "r"), say="거부하니까 매장은 원상복구하고 공임만 받겠다며 십마넌을 받음.", em=["10만원"], em_color="yellow",
          fx=[("coin_drop", "10만원을", 0.45)]),
        L("그 차는 08년식 그랜저, 시세 100만원, 범퍼는 청테이프로 붙여 다니는 차였음.",
          [B("t05", "An old 2008-era Korean full-size sedan with a sagging front bumper held on with green duct tape, parked in a gravel lot, daytime, no people"),
           B("t05", at="청테이프로", s0=1.4, s1=1.6, fx=0.5, fy=0.6, punch=True)],
          C("ohagya"), say="그 차는 공팔년식 그랜저, 시세 백마넌, 범퍼는 청테이프로 붙여 다니는 차였음.",
          em=["시세 100만원"], pop=("시세 100만원", Y, "시세"), fx=[("drum_rimshot", "청테이프로", 0.4)],
          info={"kind": "compare", "at": "시세", "title": "차 값 vs 타이어 견적", "items": [
              {"label": "08년식 그랜저", "color": W, "at": "시세", "rows": [["시세", "약 100만원", W]]},
              {"label": "타이어 4개 견적", "color": R, "at": "범퍼는", "rows": [["매장", "79만 5천원", Y]]}]}),
        L("100만원짜리 차에 타이어 80만원을 쓰라는 게 정상이에요?",
          [B("t05", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("rage"), dialogue=True, speaker=3, emotion="toneup",
          say="백마넌짜리 차에 타이어 팔십마넌을 쓰라는 게 정상이에요?"),
        L("댓글은 그 매장은 가는 데가 아니라며, 같은 급 인터넷 장착가는 8만에서 16만원이라 함.",
          [B("t06", "A laptop on a desk showing an online tire shopping page with product photos, text blurred, a new tire leaning beside the desk, no people")],
          C("biz_think", "r"), say="댓글은 그 매장은 가는 데가 아니라며, 같은 급 인터넷 장착가는 팔만에서 십육마넌이라 함.",
          em=["8만에서 16만원"], em_color="yellow",
          info={"kind": "bars", "title": "타이어 1개 값", "items": [
              {"label": "매장 전용 상품", "value": 1.0, "num": 26.5, "dec": 1, "suffix": "만원", "color": R, "at": "8만에서"},
              {"label": "인터넷 장착가(댓글)", "value": 0.6, "num": 16, "suffix": "만원 이하", "color": W, "at": "8만에서"}]}),
        L("타이어 갈기 전에 사이즈 적고 인터넷 장착가부터 검색하는 게 답임.",
          [B("t06", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("drv_idea"), em=["인터넷 장착가부터"], fx=[("correct_ding", "답임", 0.5)]),
        L("님들은 타이어 어디서 갈아요?", [B("t02", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "갈아요")]),
    ]
    build(S, lines, "100만원짜리 차에", "타이어 80만원 권유", "08년식 그랜저에 79만원 견적, 공임 10만원 내고 탈출",
          "#80만원 타이어 견적", "보배드림 베스트 1042025 (2026-10-22, 추천 625, 댓글 76)",
          [("동생 타이어 펑크, 대형 타이어 프랜차이즈 매장 방문", "원글 본문(상호, 지점명은 대본에서 뺌)"),
           ("개당 26만 5천원, 4개 3+1 79만 5천원(매장 전용 상품)", "원글 본문"),
           ("'제일 저렴한게 두개 해서 50만2000원' / 거부하자 '원상복구 해드리고 공임만' 10만원", "원글 본문"),
           ("08년식 그랜저 TG, 시세 100만원, 앞범퍼 청테이프", "원글 본문"),
           ("'100만원돈 하는차에다가 ... 타이어만 80만원 쓰라고 파는놈이 정상적인 생각인건지'", "원글 본문(대사체로 다듬음)"),
           ("댓글 '거기는 가는게 아닙니다'(추천 114), '라우펜 8만원짤', 본인 댓글 '마제스티9 인터넷 장착가 16만원 정도'", "원글 댓글"),
           ("글쓴이 '차정비하는데' = 정비업 종사자", "원글 본문")],
          "시세 100만원짜리 08년식 그랜저에 타이어 4개 79만 5천원 견적.\n가장 싼 걸로 해달라니 두 개에 50만원, 거부하자 공임 10만원만 받고 원상복구.\n인터넷 장착가는 8만~16만원이었습니다.\n\n#타이어 #타이어교체 #자동차정비 #보배드림 #란빵",
          "님들은 타이어 어디서 갈아요?",
          "타이어 공기압 측정기, 차량용 공기주입기, 타이어 트레드 게이지, 자동차 블랙박스 2채널, 차량용 방향제",
          "프랜차이즈명, 지점명은 본문에 있으나 대본에서 뺌(전체 비방 리스크). 가격 자체는 위법 아님, 법조항 없음.", [B("t04", s0=1.0, s1=1.1)])


def EP_oildrain():
    S = "oildrain"
    lines = [
        L("그럼 그 앞에서 하루 종일 지켜보고 있으세요.",
          [B("o01", "A small franchise car repair shop bay with a compact sedan raised on a two-post lift, tool carts, fluorescent light, no people", s0=1.1, s1=1.3)],
          C("seibishi", "r"), dialogue=True, speaker=2, emotion="toneup"),
        L("경정비 프랜차이즈 가맹점에 엔진오일 바꾸러 간 글쓴이.",
          [B("o01", at="글쓴이", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("drv_smile"), em=["엔진오일"]),
        L("사장은 보닛도 안 열고 차를 리프트에 올리면서 이 차 돈 들어갈 데가 많다고 함.",
          [B("o02", "A car on a lift seen from below in a repair bay, the hood closed, dark underbody, drain pan on a stand, no people")],
          C("seibishi", "r"), em=["돈 들어갈 데"], fx=[("drum_rimshot", "많다고", 0.4)]),
        L("대기실에서 보니 오일이 다 안 빠졌는데 드레인 볼트를 그냥 조여버림.",
          [B("o03", "Close-up under a car on a lift: a thick stream of black used engine oil pouring from the drain plug hole into a metal drain pan, no people"),
           B("o03", at="그냥", s0=1.3, s1=1.55, fx=0.5, fy=0.45, punch=True)],
          C("drv_shock"), em=["그냥 조여버림"], pop=("아직 안 빠졌는데!!", R, "조여버림"), fx=[("hit_trailer_epic", "조여버림", 0.5)]),
        L("물어보니 다 빠진 거라고 함. 못 믿겠다고 볼트를 풀어보라 하자 오일이 쭉 샘.",
          [B("o03", s0=1.4, s1=1.6, fx=0.5, fy=0.5)], C("oil_seibishi", "r"), em=["쭉 샘"], em_color="yellow",
          fx=[("boing_hit", "쭉", 0.5)]),
        L("그래도 사장은 다 빠진 거라고 우기고, 뚝뚝 떨어질 때까지 기다리자니까 저 말을 함.",
          [B("o04", "Close-up of a metal drain pan under a car with slow drips of dark oil falling, shop floor, no people")],
          C("rage", "r"), em=["우기고"], fx=[("wrong_gameshow_buzz", "우기고", 0.45)]),
        L("글쓴이는 그 앞에서 동영상을 켜고 기다렸고, 사장은 본인이 안 하고 직원을 시킴.",
          [B("o05", "A smartphone propped on a red toolbox recording video in a repair bay, the screen shows a blurred car underside, no people")],
          C("biz_angry"), em=["직원을 시킴"], fx=[("shutter_digital", "동영상을", 0.4)]),
        L("사진을 보니 하부 커버도 볼트를 안 풀고 칼로 네모나게 오려놨음.",
          [B("o06", "View from below of a car's black plastic underbody cover with a roughly cut rectangular hole, jagged edges, on a lift, no people"),
           B("o06", at="오려놨음", s0=1.4, s1=1.6, fx=0.5, fy=0.5, punch=True)],
          C("drv_cry"), em=["오려놨음"], pop=("오려냄?!", Y, "오려놨음"), fx=[("scratch_vinyl", "오려놨음", 0.5)]),
        L("제가 안 지켜봤으면 더러운 오일 그대로 타고 다녔을 거 아니에요?",
          [B("o04", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("drv_angry"), dialogue=True, speaker=3, emotion="toneup"),
        L("앱 리뷰를 남겼더니 사장이 비아냥 댓글을 달았고, 그 글이 베스트에 감.",
          [B("o07", "A smartphone on a cafe table showing a shop review app screen with star ratings, text blurred, no people")],
          C("biz_shock", "r"), em=["비아냥"], fx=[("notify_message_pop", "댓글을", 0.5)]),
        L("님들은 엔진오일 갈 때 옆에서 지켜봄, 대기실에 있음?", [B("o01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "있음")]),
    ]
    build(S, lines, "엔진오일 다 안 빠졌는데", "볼트 조여버린 사장", "뚝뚝 떨어질 때까지 기다리자니 하루 종일 보고 있으래",
          "#엔진오일 덜 빼고 교환", "보배드림 베스트 1042351 (2026-10-24, 추천 452, 댓글 102)",
          [("경정비 프랜차이즈 가맹점 엔진오일 교환, 사장 '이 차가 돈 들어갈 때가 많은데'", "원글 본문(프랜차이즈명은 대본에서 뺌)"),
           ("오일 다 안 빠졌는데 드레인 볼트 조임, 풀어보니 쭉 샘, '다 빠진 거다' 반복", "원글 본문"),
           ("'그럼 그 앞에서 하루종일 지켜보고 있으라', '자긴 사무실에 가 있겠다'", "원글 본문(간접인용을 대사체로)"),
           ("글쓴이 동영상 촬영하며 대기, 뚝뚝 상태에서 사장은 직원 시킴", "원글 본문"),
           ("언더커버 볼트 안 풀고 오려낸 사진", "원글 첨부 1장 + 댓글 지적(LE블루 등)"),
           ("'대기실에서 지켜보고 있지 않았으면 기존의 오염된 오일 그대로 사용했을것 아닙니까'", "원글 본문(대사체로 다듬음)"),
           ("앱 리뷰에 사장 비아냥 댓글", "원글 본문(리뷰 페이지 원문은 JS 앱이라 미확인)")],
          "엔진오일이 다 안 빠졌는데 드레인 볼트를 조여버린 사장.\n풀어보니 오일이 쭉 새는데도 다 빠졌다고 우기고, 기다리자니 하루 종일 지켜보라는 답.\n하부 커버는 칼로 오려놨습니다.\n\n#엔진오일 #엔진오일교환 #자동차정비 #보배드림 #란빵",
          "님들은 엔진오일 갈 때 옆에서 지켜봄, 대기실에 있음?",
          "엔진오일 5W30, 엔진오일 필터, 오일 드레인 팬, 자동차 블랙박스 2채널, 차량용 방향제",
          "글쓴이 일방 주장. 법조항 없이 '지켜봐야 안다' 상식으로 마무리.", [B("o05", s0=1.0, s1=1.1)])


def EP_repair740():
    S = "repair740"
    lines = [
        L("아예 신차 컨디션으로 만들어서 전체적으로 다 수리하실래요?",
          [B("r01", "A grey German executive sedan on a lift in a tidy independent repair shop, hood open, bright LED lighting, no people", s0=1.1, s1=1.3)],
          C("sales", "r"), dialogue=True, speaker=3, emotion="normal"),
        L("15만 킬로 탄 아우디 A6 차주가 정비소에 차를 맡겼는데, 이런 카톡을 받음.",
          [B("r02", "A smartphone on a kitchen table showing a messenger chat with a repair shop, text blurred, a car key beside it, evening")],
          C("drv_think"), say="십오만 킬로 탄 아우디 에이식스 차주가 정비소에 차를 맡겼는데, 이런 카톡을 받음.",
          em=["카톡을"], fx=[("notify_message_pop", "카톡을", 0.5)]),
        L("하체, 엔진 마운트, 브레이크, 판금 도장, 타이어까지 해서 총 740만원을 냄.",
          [B("r03", "Several repair invoice sheets and a car key on a repair shop counter, stacks of Korean banknotes beside, text blurred, no people"),
           B("r03", at="740만원을", s0=1.3, s1=1.5, fx=0.5, fy=0.5, punch=True)],
          C("bill_shock"), say="하체, 엔진 마운트, 브레이크, 판금 도장, 타이어까지 해서 총 칠백사십마넌을 냄.",
          em=["740만원"], em_color="yellow", fx=[("drop_futuristic", "740만원을", 0.5)],
          info={"kind": "counter", "at": "740만원을", "title": "수리비 총액", "items": [{"num": 740, "suffix": "만원", "label": "하체, 마운트, 판금, 타이어", "at": "740만원을"}]}),
        L("근데 차를 돌려받은 그날, 멀쩡했던 오른쪽 헤드라이트가 안 켜지고 깜빡이도 고장.",
          [B("r04", "Front of a grey German sedan at night in a parking lot, the right headlight dark and fogged with condensation inside, the left headlight lit, no people"),
           B("r04", at="오른쪽", s0=1.4, s1=1.7, fx=0.3, fy=0.5, punch=True)],
          C("drv_shock"), em=["그날"], pop=("당일 고장!!", R, "그날"), shake="그날", fx=[("glass_break", "그날", 0.45)]),
        L("업체는 헤드라이트 근처는 작업한 적이 없다며 수리를 거절함.",
          [B("r01", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("seibishi", "r"), em=["거절함"], fx=[("wrong_gameshow_buzz", "거절함", 0.45)]),
        L("헤드라이트 쪽은 손도 안 댔어요. 저희 책임 아닙니다.",
          [B("r01", s0=1.35, s1=1.5, fx=0.5, fy=0.4)], C("biz_angry", "r"), dialogue=True, speaker=2, emotion="normal"),
        L("본사도 소비자원도 정비 내역과 무관하다는 답만 함.",
          [B("r05", "An empty customer service call center desk with a headset and a monitor, screen blurred, fluorescent light, no people")],
          C("komatta"), em=["무관하다는"], em_color="yellow"),
        L("근데 실내등이 안 켜진 건 조수석 라이트 배선 쇼트라며, 커넥터를 빼놓는 식으로 고쳐줬음.",
          [B("r06", "Close-up inside an engine bay of a headlight wiring harness with its connector unplugged and dangling, no people")],
          C("biz_think", "r"), em=["쇼트"], fx=[("hit_trailer_epic", "쇼트라며", 0.45)]),
        L("입고 때 헤드라이트가 정상이었단 건 업체도 인정했고, 통화 녹음도 있음.",
          [B("r07", "A smartphone on a car seat showing a call recording list screen, text blurred, daytime, no people")],
          C("drv_idea"), em=["통화 녹음"], fx=[("correct_ding", "있음", 0.5)]),
        L("댓글은 소비자가 입증해야 하는 게 문제라는 쪽과, 까마귀 날자 배 떨어진 거라는 쪽으로 갈림.",
          [B("r03", s0=1.0, s1=1.12)], C("biz_think"), em=["입증해야"],
          info={"kind": "compare", "at": "소비자가", "title": "댓글 반응", "items": [
              {"label": "소비자가 입증해야 하나", "color": W, "at": "소비자가", "rows": [["추천", "67", "#7CFF6B"]]},
              {"label": "까마귀 날자 배 떨어짐", "color": Y, "at": "까마귀", "rows": [["추천", "54", "#7CFF6B"], ["반대", "35", R]]}]}),
        L("님들은 740만원 수리 뒤 당일 고장, 업체 책임이라고 봄?", [B("r04", s0=1.0, s1=1.12)], C("biz_q"),
          say="님들은 칠백사십마넌 수리 뒤 당일 고장, 업체 책임이라고 봄?", fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "740만원 수리 맡겼더니", "당일 헤드라이트 고장", "입고 땐 정상, 출고 당일 고장, 업체는 무관",
          "#740만원 수리 후 고장", "보배드림 베스트 1042121 (2026-10-23, 추천 447, 댓글 74, 첨부 7장 판독)",
          [("아우디 A6 약 15만km(계기판 149,834km), 정비소 카톡 '아예 신차컨디션으로 만들어서 전체적으로 다 수리를할지'", "원글 첨부 카톡 캡처"),
           ("총 740만원(내역서: 하체, 엔진마운트, 브레이크, 판금도장, 타이어 4본 등)", "원글 본문, 내역서 3장"),
           ("출고 당일 우측 헤드라이트 습기, 미점등, 깜빡이 고장, 실내 표시등 미점등", "원글 본문, 계기판 경고 캡처"),
           ("업체 '헤드라이트 관련된 부분 근처에 작업한 적 없다, 수리해줄 수 없다' / 본사, 소비자원 '정비내역과 무관'", "원글 본문(대사는 대사체로 다듬음)"),
           ("'조수석라이트쪽 배선들이 쇼트나서 ... 커넥터 빼니까 불이 들어온다', 커넥터 뺀 상태로 반환", "원글 첨부 카톡 캡처"),
           ("입고 시 정상은 업체도 인정, 자동통화녹음 보유", "원글 본문"),
           ("댓글 '소비자가 입증해야한다는게 문제'(67) / '까마귀 날자 배 떨어질수 있어요'(54, 반대 35)", "원글 댓글. 댓글의 '32만km'는 블루투스 기기명 오독")],
          "15만km 아우디 A6를 740만원 들여 수리했는데, 돌려받은 당일 헤드라이트와 깜빡이가 고장.\n업체는 근처 작업 안 했다며 거절, 소비자원도 무관하다는 답.\n입고 땐 정상이었다는 통화 녹음이 있습니다.\n\n#자동차수리 #정비소 #아우디 #보배드림 #란빵",
          "님들은 740만원 수리 뒤 당일 고장, 업체 책임이라고 봄?",
          "자동차 헤드라이트 전구, 헤드라이트 복원제, 차량용 LED 전구, 자동차 블랙박스 2채널, 차량용 방향제",
          "정비소 상호, 지역 비공개. 글쓴이 일방 주장이라 '업체는 ~라 함' 서술 유지.", [B("r06", s0=1.0, s1=1.1)])


def EP_outcar64():
    S = "outcar64"
    lines = [
        L("저는 9대 1도 억울합니다.",
          [B("p01", "A hospital outdoor surface parking lot in Korea, a black sedan halfway backed out of a parking space into the aisle, daytime, no people", s0=1.1, s1=1.3)],
          C("drv_angry", "r"), dialogue=True, speaker=2, emotion="toneup", say="저는 구대 일도 억울합니다."),
        L("병원 지상 주차장에서 검정차가 주차칸에서 천천히 빠져나오던 중이었음.",
          [B("p01", at="천천히", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("drv_smile"), em=["천천히"]),
        L("그때 통로로 흰차가 우회전해 들어오는 걸 보고 검정차는 바로 멈춤.",
          [B("p02", "Dashcam-height view in a hospital parking lot: a white SUV turning right into the aisle toward the camera, parked cars on both sides, daytime, no people")],
          C("drv_surprise"), em=["바로 멈춤"], fx=[("boom_subby_kick", "멈춤", 0.45)]),
        L("근데 흰차는 그대로 진행해서 뒷문과 펜더를 쭉 긁고 나서야 멈춤.",
          [B("p03", "Close-up of a white SUV's scratched rear door and rear fender right next to the front bumper corner of a black sedan, a license plate lying on the asphalt, daytime"),
           B("p03", at="긁고", s0=1.3, s1=1.55, fx=0.5, fy=0.5, punch=True)],
          C("jiko_man", "r"), em=["긁고"], pop=("긁고 지나감", R, "긁고"), shake="긁고", fx=[("glass_break", "긁고", 0.45)]),
        L("검정차는 앞 범퍼 모서리가 긁히고 번호판이 떨어짐.",
          [B("p03", s0=1.4, s1=1.6, fx=0.6, fy=0.7)], C("drv_cry"), em=["번호판이"]),
        L("보험사가 법무법인에 자문했더니 결과는 출차 차량 6, 우회전 차량 4.",
          [B("p04", "A legal opinion document and a car insurance card on an office desk, text blurred, a pen, daytime, no people")],
          C("lawyer", "r"), say="보험사가 법무법인에 자문했더니 결과는 출차 차량 육, 우회전 차량 사.",
          em=["6"], em_color="yellow", fx=[("drop_futuristic", "출차", 0.5)],
          info={"kind": "compare", "at": "결과는", "title": "보험사 법률 자문", "items": [
              {"label": "출차하던 검정차", "color": R, "at": "출차", "rows": [["과실", "60%", Y]]},
              {"label": "우회전 흰차", "color": W, "at": "우회전", "rows": [["과실", "40%", W]]}]}),
        L("통로를 살피지 않고 출차한 과실이 더 무겁다는 이유였음.",
          [B("p04", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("biz_think", "r"), em=["더 무겁다는"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "무겁다는", 0.45)]),
        L("멈춰 있는 차를 긁고 간 건데 뭘 어쩌라고요? 흰차 100이죠.",
          [B("p02", s0=1.3, s1=1.5, fx=0.5, fy=0.5)], C("rage"), dialogue=True, speaker=3, emotion="toneup",
          say="멈춰 있는 차를 긁고 간 건데 뭘 어쩌라고요? 흰차 백이죠."),
        L("추천 141개 댓글이 그랬고, 양쪽이 같은 보험사라 글쓴이는 분심위에 올렸음.",
          [B("p05", "A smartphone showing a community comment thread with a thumbs-up icon highlighted, text blurred, held over a desk, no people")],
          C("biz_angry"), say="추천 백사십일개 댓글이 그랬고, 양쪽이 같은 보험사라 글쓴이는 분심위에 올렸음.",
          em=["분심위"], fx=[("notify_message_pop", "댓글이", 0.5)]),
        L("주차장 사고는 보통 출차 차 과실이 크게 잡히지만, 멈춘 뒤에 긁힌 거면 얘기가 달라짐.",
          [B("p02", s0=1.0, s1=1.15)], C("judge", "r"), em=["멈춘 뒤에"], fx=[("correct_ding", "달라짐", 0.5)]),
        L("님들은 이 사고 몇 대 몇이라고 봄?", [B("p01", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "멈춰 있던 출차 차량", "과실 6, 긁은 차가 4?", "보험사 자문 6:4, 댓글은 우회전차 100",
          "#주차장 출차 과실 6:4", "보배드림 베스트 1042070 (2026-10-23, 추천 413, 댓글 108, 영상은 본문, 댓글 묘사 기준)",
          [("병원 지상 주차장, 출차 중 검정차(글쓴이) vs 우회전 진입 흰차", "원글 본문, 추가글 '제 차가 검정색'"),
           ("검정차 흰차 진입 보고 즉시 정지, 흰차 그대로 진행해 긁고 멈춤", "추천 1위 댓글(141) 영상 묘사"),
           ("흰차 조수석 뒷문, 뒷펜더 긁힘 / 검정차 앞범퍼 왼쪽 모서리, 번호판 탈락", "원글 본문"),
           ("보험사 의뢰 법무법인 자문 '출차차량 6 : 우회전차량 4', '통로 차량 살피지 않고 출차한 과실이 중함'", "원글 본문 자문 원문"),
           ("'저는 9대1도 억울합니다', '같은 보험사라 ... 분심위에 올려달라고만'", "원글 본문"),
           ("댓글 '흰차 100'(141), '우회전 100%'(76), 유사 사례 한문철TV 15421회 언급", "원글 댓글"),
           ("'멈춰 있는 차를 긁고 간 건데' 대사", "추천 1위 댓글을 대사체로 다듬음")],
          "병원 주차장에서 출차 중 멈춘 검정차를 우회전 흰차가 긁고 지나갔습니다.\n보험사 법률 자문은 출차 차량 6, 우회전 차량 4. 댓글은 흰차 100이 압도적.\n같은 보험사라 분심위로 갔습니다.\n\n#과실비율 #주차장사고 #블랙박스 #보배드림 #란빵",
          "님들은 이 사고 몇 대 몇이라고 봄?",
          "자동차 블랙박스 2채널, 블랙박스 상시전원, 후방 주차 센서, 사이드미러 보조미러, 차량용 방향제",
          "과실비율 인정기준 기본과실 수치는 미확인이라 '보통 출차 차 과실이 크게 잡힘'으로만.", [B("p03", s0=1.0, s1=1.1)])


def EP_leftturn91():
    S = "leftturn91"
    lines = [
        L("책자에 나와 있는 대로 9대 1입니다. 더는 못 드려요.",
          [B("l01", "Dashcam view approaching a Korean urban intersection on a gentle downhill, green traffic light, an oncoming sedan waiting at the opposite stop line, daytime, no people visible", s0=1.1, s1=1.3)],
          C("biz_angry", "r"), dialogue=True, speaker=2, emotion="normal", say="책자에 나와 있는 대로 구대 일입니다. 더는 못 드려요."),
        L("직진 신호에 시속 38킬로로 교차로에 들어가던 글쓴이.",
          [B("l01", at="교차로에", s0=1.2, s1=1.35, fx=0.5, fy=0.5)], C("drv_smile"),
          say="직진 신호에 시속 삼십팔킬로로 교차로에 들어가던 글쓴이.", em=["38킬로"]),
        L("반대편 정지선에 서 있던 차가 갑자기 비보호 좌회전으로 밀고 들어옴.",
          [B("l02", "Dashcam view inside an intersection: a sedan cutting across from the opposite lane in a sudden left turn directly ahead, very close, slight motion blur, daytime"),
           B("l02", at="갑자기", s0=1.3, s1=1.6, fx=0.5, fy=0.5, punch=True)],
          C("drv_shock", "r"), em=["비보호 좌회전"], pop=("갑자기!!", R, "갑자기"), fx=[("hit_trailer_epic", "갑자기", 0.5)]),
        L("바로 브레이크를 밟았지만 내리막이라 정면으로 부딪힘.",
          [B("l03", "Two sedans with crumpled front ends stopped in the middle of an intersection, hazard lights on, broken plastic on the asphalt, daytime, no people")],
          C("jiko_man"), em=["정면으로"], shake="부딪힘", fx=[("glass_smash", "부딪힘", 0.45)]),
        L("상대는 좌회전 깜빡이도 없었고, 사고 사실 확인원엔 안전운전 의무 위반으로 적힘.",
          [B("l04", "A traffic accident report form on a police desk, text blurred, a pen and a stamp beside it, daytime, no people")],
          C("police", "r"), em=["안전운전 의무 위반"], em_color="yellow"),
        L("그런데 상대방은 연락처도 안 주고 10분 넘게 현장을 떠나버렸음.",
          [B("l05", "An intersection corner with a tow truck's amber lights flashing, a damaged sedan behind, late afternoon, no people")],
          C("komatta"), say="그런데 상대방은 연락처도 안 주고 십분 넘게 현장을 떠나버렸음.", em=["떠나버렸음"],
          fx=[("drum_rimshot", "떠나버렸음", 0.4)]),
        L("글쓴이는 5일 입원에 넉 달째 통원 중인데, 상대 보험사는 9대 1을 고집함.",
          [B("l06", "An empty hospital corridor with a wheelchair parked by the wall, daylight through windows, no people")],
          C("sick"), say="글쓴이는 오일 입원에 넉 달째 통원 중인데, 상대 보험사는 구대 일을 고집함.",
          em=["9대 1을"], em_color="yellow", fx=[("wrong_gameshow_buzz", "고집함", 0.45)],
          info={"kind": "compare", "at": "상대", "title": "과실 주장", "items": [
              {"label": "상대 보험사", "color": W, "at": "상대", "rows": [["좌회전차 : 직진차", "9 : 1", W]]},
              {"label": "글쓴이", "color": Y, "at": "9대", "rows": [["좌회전차 : 직진차", "10 : 0", Y]]}]}),
        L("무슨 자료를 내도 책자에 있는 9대 1만 말해요. 결국 소송 걸었어요.",
          [B("l04", s0=1.3, s1=1.45, fx=0.5, fy=0.5)], C("drv_angry"), dialogue=True, speaker=3, emotion="toneup",
          say="무슨 자료를 내도 책자에 있는 구대 일만 말해요. 결국 소송 걸었어요."),
        L("비보호 좌회전은 직진차에 방해가 안 될 때만 허용되고, 사고 나면 좌회전 차 과실이 기본으로 큼.",
          [B("l01", s0=1.0, s1=1.15)], C("judge", "r"), em=["좌회전 차 과실"], fx=[("correct_ding", "큼", 0.5)]),
        L("댓글은 상대 100이 압도적이고, 9대 1이면 잘 받았다는 댓글은 반대 58개를 먹음.",
          [B("l07", "A smartphone showing a community comment thread with a thumbs-down icon highlighted, text blurred, on a desk, no people")],
          C("biz_laugh"), say="댓글은 상대 백이 압도적이고, 구대 일이면 잘 받았다는 댓글은 반대 오십팔개를 먹음.",
          em=["반대 58개"], fx=[("crowd_laugh", "먹음", 0.4)],
          info={"kind": "compare", "at": "댓글은", "title": "댓글 반응", "items": [
              {"label": "상대방 100", "color": Y, "at": "댓글은", "rows": [["추천", "61", "#7CFF6B"]]},
              {"label": "9대 1이면 잘 받음", "color": W, "at": "9대", "rows": [["추천", "5", W], ["반대", "58", R]]}]}),
        L("님들은 이거 몇 대 몇이 맞다고 봄?", [B("l03", s0=1.0, s1=1.12)], C("biz_q"), fx=[("pop_bubble", "봄")]),
    ]
    build(S, lines, "정지선에 서 있던 차가", "비보호 좌회전으로 돌진", "직진 38km/h 중 정면충돌, 상대 보험사는 9:1 고집",
          "#비보호좌회전 9대1 소송", "보배드림 베스트 1041751 교통사고/블박 (2026-10-22, 추천 242, 댓글 74, 영상은 본문, 댓글 묘사 기준)",
          [("직진 신호, 제한 50 도로 38km/h, 내리막, 반대편 차 정지선 정차 확인 후 진입", "원글 본문"),
           ("반대편 차 비보호좌회전으로 진입, 정면충돌, 즉시 제동했으나 정지거리 부족", "원글 본문"),
           ("상대 좌회전 지시등 미점등(블박 기준), 사고사실확인원 '안전운전의무위반'", "원글 본문"),
           ("상대 연락처 미제공, 10분 넘게 현장 이탈 후 복귀", "원글 본문"),
           ("글쓴이 5일 입원, 4달째 통원 / 상대 보험사 90:10, 글쓴이 무과실 주장, 소송 제기", "원글 본문"),
           ("'어떠한 자료를 제시해도 무조건 보험 책자에 나와 있는 9:1만 고집'", "본인 댓글(대사체로 다듬음, 보험사 대사는 이를 뒤집어 각색)"),
           ("비보호좌회전은 녹색 신호에 직진차 통행 방해 없을 때만 허용, 2010년 이후 사고 시 신호위반 아닌 안전운전의무위반", "도로교통법 시행규칙 별표 6 신호 의미, 경찰청 안내. 댓글의 '12대 중과실' 주장은 대본에서 제외"),
           ("댓글 '상대방 100'(61), '91이면 잘받았네'(추천 5, 반대 58)", "원글 댓글")],
          "직진 신호에 38km/h로 교차로에 들어가는데, 정지선에 서 있던 차가 비보호 좌회전으로 밀고 들어와 정면충돌.\n상대 보험사는 9대 1만 고집해 소송까지 갔습니다.\n댓글은 상대 100이 압도적.\n\n#비보호좌회전 #과실비율 #교통사고 #보배드림 #란빵",
          "님들은 이거 몇 대 몇이 맞다고 봄?",
          "자동차 블랙박스 2채널, 블랙박스 메모리카드, 목 보호 쿠션, 차량용 핸드폰 거치대, 차량용 방향제",
          "기본과실 수치(80:20 추정)는 미확인이라 '기본으로 큼'으로만. 뺑소니 여부는 언급 안 함.", [B("l02", s0=1.0, s1=1.1)])


# ───────────────────────── 신차 (research_newcar_1024.md 확인 후 작성) ─────────────────────────

BOBAE = [EP_golfclub, EP_tire80, EP_oildrain, EP_repair740, EP_outcar64, EP_leftturn91]
NEWCAR = []

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in BOBAE + NEWCAR:
        if not want or f.__name__[3:] in want:
            f()
