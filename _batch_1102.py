#!/usr/bin/env python3
"""란빵 2026-11-02 대상 10편 (11/1 15:00 launchd 가 ENOTFOUND 로 멈춰 11/2 낮에 수동 실행).
- 2026-11-02 사용자 지시 "블박에서 영상이 있으면 영상 녹화해서 일부는 영상으로": 보배드림 첨부 영상(movie.bobaedream.co.kr)
  을 vclip() 으로 1080x960 무음 클립으로 잘라 shots 의 "vid" 컷으로 쓴다(build_v2 의 vid 지원, 2026-10-16 roadster).
  영상 편 = busfall, leftcross, door73, wheelroad, flipcar.
- 보배드림 베스트 9편 + 아반떼 K세일페스타 할인 1편. 근거 = work/research_1102.md, 원본 = work/_photos/b1102/ (map.txt).
- 실명, 상호, 지명(지하차도 이름, 교차로 이름), 번호판 없음. 캐릭터 없음(NO_CHAR).
"""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _batch_1024 import B, C, L, build, IR, Y, W, R, P   # noqa: E402,F401
from _batch_1027 import cap as _cap   # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(ROOT, "work", "_photos", "b1102")
BB = "사진: 보배드림"
BV = "영상: 보배드림"
COMMON = "자동차 블랙박스 2채널, 블랙박스 메모리카드, 비상삼각대, 차량용 핸드폰 거치대, 차량용 방향제"
MAXC = 360


def cap(*a, **k):
    k.setdefault("ph", PH)
    return _cap(*a, **k)


def vclip(slug, name, src, ss, dur, cx=0.5, cy=0.5, zoom=1.0, eq="", blur=()):
    """보배드림 영상 → work/<slug>/v2/vid/<name>.mp4 (1080x960, 30fps, 무음). blur = 결과 좌표 (x,y,w,h) 고정 모자이크."""
    d = os.path.join(ROOT, "work", slug, "v2", "vid")
    os.makedirs(d, exist_ok=True)
    out = os.path.join(d, name + ".mp4")
    if os.path.exists(out):
        return
    p = os.path.join(PH, src)
    w, h = map(int, subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                             "stream=width,height", "-of", "csv=p=0", p]).decode().split(",")[:2])
    r = max(1080 / w, 960 / h) * zoom
    sw, sh = round(w * r / 2) * 2, round(h * r / 2) * 2
    x = min(max(int(sw * cx - 540), 0), sw - 1080)
    y = min(max(int(sh * cy - 480), 0), sh - 960)
    vf = f"scale={sw}:{sh},crop=1080:960:{x}:{y}" + (f",{eq}" if eq else "")
    if blur:
        chain = f"[0:v]{vf}[b0]"
        for i, (bx, by, bw, bh) in enumerate(blur):
            chain += f";[b{i}]split[m{i}][c{i}];[c{i}]crop={bw}:{bh}:{bx}:{by},scale={max(2, bw // 24)}:{max(2, bh // 24)},scale={bw}:{bh}:flags=neighbor[p{i}];[m{i}][p{i}]overlay={bx}:{by}[b{i + 1}]"
        args = ["-filter_complex", chain, "-map", f"[b{len(blur)}]"]
    else:
        args = ["-vf", vf]
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-t", str(dur), "-i", p, *args, "-r", "30", "-an",
                    "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p", out], check=True)
    print(f"  vclip {slug}/{name} {ss}+{dur}s")


def V(name, credit=BV, at=None, ss=0, s0=1.0, s1=1.06, fx=0.5, fy=0.5, punch=False):
    d = {"vid": f"vid/{name}.mp4", "s0": s0, "s1": s1, "fx": fx, "fy": fy, "credit": credit}
    if ss:
        d["ss"] = ss
    if at:
        d["at"] = at
    if punch:
        d["punch"] = True
    return d


def go(S, lines, *rest, **kw):
    n = sum(len(l["text"]) for l in lines)
    assert 10 <= len(lines) <= 12, (S, len(lines))
    assert n <= MAXC, (S, "글자", n)
    for l in lines:
        assert "—" not in l["text"] and "·" not in l["text"], l["text"]
    build(S, lines, *rest, **kw)
    print(f"  chars {S} = {n} ({len(lines)}줄)")


# ───────────────────────── 1. 버스 뒷빵 채무부존재 ─────────────────────────
def EP_busfall():
    S = "busfall"
    vclip(S, "v1", "1044392_m0.mp4", 0, 10, cx=0.5, cy=0.42, zoom=1.3)
    cap(S, "post", "1044392_01.png", box=(0, 0, 775, 560), fit=True, nofaces=True)
    lines = [
        L("저희는 납득이 안 돼요. 버스회사가 직접 전화하세요.",
          [B("u01", "A Korean family sedan stopped at night on a city road, a large city bus right behind it, red tail lights, wet asphalt, no people visible", s0=1.0, s1=1.2)],
          None, dialogue=True, speaker=2, emotion="toneup"),
        L("7월 말 밤, 정차 중이던 승용차를 버스가 뒤에서 박았음.",
          [V("v1", s0=1.0, s1=1.08), V("v1", at="박았음", ss=6, s0=1.1, s1=1.2, punch=True)],
          None, say="칠월 말 밤, 정차 중이던 승용차를 버스가 뒤에서 박았음.", em=["뒤에서 박았음"],
          fx=[("hit_trailer_epic", "박았음", 0.45)]),
        L("버스 기사는 전방을 못 봤다고 인정하는 문자까지 보냄.",
          [V("v1", ss=3, s0=1.15, s1=1.25)], None, em=["인정하는 문자"]),
        L("뒷좌석에서 자던 작은애는 굴러떨어져 멍이 들었다고 함.",
          [B("u02", "Back seat of a Korean family car at night, a small child's blanket and a stuffed toy fallen on the car floor, dim interior light, no people")],
          None, em=["멍이"]),
        L("가족은 4박5일 입원하고, 9월부터는 주 1회 한방병원에 다님.",
          [B("u03", "Interior of a Korean oriental medicine clinic: acupuncture treatment beds with curtains, herbal medicine drawers on the wall, no people")],
          None, say="가족은 사박오일 입원하고, 구월부터는 주 일회 한방병원에 다님.", em=["4박5일"]),
        L("보험사가 제시한 4인 가족 합의금은 330, 늦으면 줄어든다는 문자도 옴.",
          [P("post", BB, s0=1.0, s1=1.15, fx=0.5, fy=0.6), P("post", BB, at="330", s0=1.6, s1=1.75, fx=0.4, fy=0.68, punch=True)],
          None, say="보험사가 제시한 사인 가족 합의금은 삼백삼십, 늦으면 줄어든다는 문자도 옴.", em=["330"], em_color="yellow",
          fx=[("drop_futuristic", "330", 0.5)]),
        L("그런데 석 달째, 버스회사가 채무부존재소송을 걸겠다고 함.",
          [V("v1", ss=5, s0=1.2, s1=1.3, fx=0.5, fy=0.5)],
          None, em=["채무부존재소송"], em_color="yellow", pop=("소송?!", R, "채무부존재소송"),
          info={"kind": "quotes", "at": "그런데", "title": "채무부존재 확인 소송", "items": [
              {"text": "더 줄 돈 없다", "at": "채무부존재소송"}, {"text": "법원에서 확인받는 소송", "at": "걸겠다고"}]}),
        L("글쓴이는 합의금보다 치료를 한 달이라도 더 받고 싶다고 함.",
          [B("u03", s0=1.2, s1=1.35)], None, em=["한 달이라도"]),
        L("퍼온 회원의 답은, 소장 받으면 피해를 입증하면 됨.",
          [P("post", BB, s0=1.0, s1=1.1, fx=0.5, fy=0.3)], None, em=["피해를 입증"],
          fx=[("correct_ding", "입증하면", 0.45)]),
        L("댓글은 저 정도에 석 달은 길다, 버스회사 응원한다는 쪽이 많았음.",
          [V("v1", ss=6, s0=1.0, s1=1.1)], None, em=["버스회사 응원"]),
        L("님들은 이 정도 뒷빵이면 병원 몇 달 다님?", [B("u01", s0=1.1, s1=1.2)], None, fx=[("pop_bubble", "다님")]),
    ]
    go(S, lines, "버스가 살짝 박았는데", "석 달째 한방병원", "버스 후방추돌 석 달 통원, 버스회사는 채무부존재소송",
       "#버스 뒷빵 석 달 통원", "보배드림 베스트 1044392 [펑하셨네] 재게시 (원글 교통사고/블박 2026-10-30 '채무부존재소송 질문드립니다', 베스트 추천 104, 댓글 10)",
       [("7월 말 정차 중 버스 후방추돌, 기사가 전방 못 봤다고 인정 문자, 경찰 출동, 사고접수 안 함", "원글 캡처 본문"),
        ("작은애가 안전벨트 한 채로 누워 자다 굴러떨어짐, 멍", "원글 캡처 본문"),
        ("사고 직후 4박5일 입원, 9월부터 주 1회 한방병원", "원글 캡처 본문"),
        ("보험사 4인 가족 합의금 330 제시, 시간 지나면 줄어든다는 문자", "원글 캡처 본문(단위 표기 없음, 330 그대로)"),
        ("버스회사가 채무부존재소송 제기하겠다고 보험사 통해 통보, 글쓴이 '버스회사가 직접 전화하라'", "원글 캡처 본문(대사체)"),
        ("합의금보다 치료를 한 달이라도 더 받고 싶다", "원글 캡처 본문"),
        ("펑 회원 '소장 받으면, 피해를 입증하시면 됩니다'", "1044392 본문"),
        ("댓글 '저 정도 사고로 3달 병원 다녔는데 한 달 더 다니고 싶다는 게 이해가 안 가', '버스회사 응원합니다'", "1044392 댓글")],
       "정차 중에 버스가 뒤에서 박았고, 가족은 석 달째 한방병원에 다니는 중입니다.\n버스회사는 채무부존재소송을 걸겠다고 합니다.\n님들 생각은 어떤가요?\n\n#블랙박스 #교통사고 #버스사고 #보배드림 #란빵",
       "님들은 이 정도 뒷빵이면 병원 몇 달 다님?",
       COMMON, "블박 영상은 원글 휴대폰 촬영본, 하단 자막(펑 회원 닉네임) 잘라냄. 번호판 안 보임.", [B("u02", s0=1.0, s1=1.1)])


# ───────────────────────── 2. 차선 4개 가로질러 추돌 ─────────────────────────
def EP_leftcross():
    S = "leftcross"
    vclip(S, "v1", "1044433_m0.mp4", 22, 12, cx=0.55, cy=0.55, zoom=1.15, eq="eq=brightness=0.06:gamma=1.35")
    lines = [
        L("온다 온다 온다, 자 드가자!",
          [V("v1", ss=4, s0=1.0, s1=1.1)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("신호 있는 교차로에서 유도선 따라 좌회전하던 블박차.",
          [V("v1", s0=1.0, s1=1.06)], None, em=["좌회전"]),
        L("오른쪽 길에서 차 한 대가 차선 4개를 한 번에 가로질러 옴.",
          [V("v1", ss=4, s0=1.05, s1=1.15)], None, say="오른쪽 길에서 차 한 대가 차선 네 개를 한 번에 가로질러 옴.",
          em=["차선 4개"], em_color="yellow"),
        L("경적을 울렸지만 그대로 조수석 문 쪽을 들이받음.",
          [V("v1", ss=7, s0=1.1, s1=1.25, punch=True)], None, em=["조수석 문"],
          shake="들이받음", fx=[("hit_trailer_epic", "들이받음", 0.5)]),
        L("바로 좌회전 차로로 들어가려던 걸로 보인다고 함.",
          [V("v1", ss=8, s0=1.2, s1=1.3, fx=0.6)], None, em=["좌회전 차로"]),
        L("과실 비율은 내일쯤 나올 예정이라 미리 물어본 글.",
          [B("l01", "An insurance claim form and a car key on a dark desk next to a smartphone showing a blurred dashcam video, desk lamp, no people")],
          None, em=["과실 비율"]),
        L("댓글 대부분은 100대0, 정상 진입이 아니라는 의견.",
          [V("v1", ss=9, s0=1.0, s1=1.1)], None, say="댓글 대부분은 백대영, 정상 진입이 아니라는 의견.", em=["100대0"], em_color="yellow",
          info={"kind": "quotes", "at": "댓글", "title": "추천 많은 댓글", "items": [
              {"text": "차로 준수 위반, 100", "at": "100대0"}, {"text": "정상 진입이 아님", "at": "정상"}]}),
        L("차 오는 타이밍에 움직인다, 고의 아니냐는 댓글도 있었음.",
          [V("v1", ss=6, s0=1.2, s1=1.35, fx=0.55)], None, em=["고의 아니냐"]),
        L("다만 사고 예측 의무로 과실이 잡힐 수 있다는 말도 나옴.",
          [B("l02", "A night city intersection seen from a driver's seat, many lanes, traffic lights, light trails, no people")], None, em=["사고 예측 의무"]),
        L("그래서 싸우기 귀찮으면 대인 없이 100 받으란 조언까지.",
          [B("l01", s0=1.2, s1=1.3)], None, say="그래서 싸우기 귀찮으면 대인 없이 백 받으란 조언까지.", em=["대인 없이"]),
        L("님들이 보기엔 몇 대 몇임?", [V("v1", ss=7, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "몇임")]),
    ]
    go(S, lines, "좌회전 중인데", "옆에서 가로질러 쾅", "신호 교차로 좌회전 중 차선 4개를 가로지른 차와 충돌",
       "#4차로 가로질러 쾅", "보배드림 베스트 1044433 교통사고/블박 (2026-11-01, 추천 25, 댓글 29)",
       [("신호 있는 교차로, 유도선 따라 신호 맞춰 좌회전 중 오른쪽 길에서 차가 거의 가로로 횡단, 조수석 문쪽 추돌", "원글 본문, 블박 영상"),
        ("바로 좌회전 차선으로 진입하려고 4개 차선을 한꺼번에 들어오려 한 것 같음", "원글 본문"),
        ("상대 차가 다가오는 거 느끼자마자 경적, 피하지 못함", "원글 본문"),
        ("과실 비율 내일쯤 나올 예정", "원글 본문"),
        ("댓글 '도로교통법 14조, 19조 차로준수위반 진로변경방법위반 100, 정상적인 진입이 아님'(11), '고의사고인가 차 오는 타이밍에 움직이네요'(12), '당연히 100대 0, 온다 온다 온다 자 드가자'", "원글 댓글(대사는 댓글 인용)"),
        ("'사고예측의무 관련 과실 나오겠는걸, 싸우기 귀찮으니 대인 없이 100 추천'(9)", "원글 댓글")],
       "신호 받고 좌회전하던 중, 오른쪽 길에서 차가 차선 4개를 한 번에 가로질러 들이받았습니다.\n댓글은 대부분 100대0이었습니다.\n님들은 몇 대 몇으로 보나요?\n\n#블랙박스 #교통사고 #과실비율 #보배드림 #란빵",
       "님들이 보기엔 몇 대 몇임?",
       COMMON, "교차로 이름(댓글의 지명) 안 씀. 야간 영상이라 밝기만 보정, 번호판 판독 불가.", [V("v1", ss=7, s0=1.0, s1=1.05)])


# ───────────────────────── 3. 개문사고 7:3 ─────────────────────────
def EP_door73():
    S = "door73"
    vclip(S, "v1", "1044550_m0.mp4", 3, 9, cx=0.5, cy=0.5, zoom=1.0)
    vclip(S, "v2", "1044550_m1.mp4", 0, 6.9, cx=0.5, cy=0.5, zoom=1.0)
    cap(S, "law", "1044550_00.jpg", box=(0, 100, 590, 1050), fit=True, nofaces=True)
    cap(S, "wheel", "1044550_02.jpg", nofaces=True)
    lines = [
        L("블박차도 30은 잡아야죠.",
          [V("v1", ss=5, s0=1.2, s1=1.3)], None, dialogue=True, speaker=3, emotion="normal", say="블박차도 삼십은 잡아야죠."),
        L("좌회전해서 골목으로 들어가는데 황색 실선 위에 불법 주차된 SUV가 있었음.",
          [V("v1", s0=1.0, s1=1.06)], None, em=["불법 주차"], say="좌회전해서 골목으로 들어가는데 황색 실선 위에 불법 주차된 에스유브이가 있었음."),
        L("지나가는 순간 운전석 문이 확 열리며 조수석 옆을 긁음.",
          [V("v1", ss=5, s0=1.05, s1=1.2, punch=True)], None, em=["운전석 문이"],
          shake="열리며", fx=[("hit_trailer_epic", "열리며", 0.5)]),
        L("당시 속도는 시속 10에서 20km 정도였다고 함.",
          [V("v1", ss=6, s0=1.0, s1=1.1)], None, say="당시 속도는 시속 십에서 이십 킬로 정도였다고 함.", em=["10에서 20km"]),
        L("헤드라이트, 범퍼, 문 두 짝, 미러, 휠까지 교환 목록이 한가득.",
          [V("v2", s0=1.0, s1=1.08), P("wheel", BB, at="휠까지", s0=1.0, s1=1.12)], None, em=["한가득"]),
        L("우리 보험사는 10대0, 상대 보험사는 7대3을 주장함.",
          [B("d01", "Two insurance documents side by side on an office desk with a calculator and a toy car, daylight, no people")],
          None, say="우리 보험사는 십대영, 상대 보험사는 칠대삼을 주장함.", em=["7대3"], em_color="yellow",
          info={"kind": "compare", "at": "우리", "title": "과실 주장", "items": [
              {"label": "블박차 보험사", "color": W, "at": "우리", "rows": [["주장", "10:0", Y]]},
              {"label": "상대 보험사", "color": R, "at": "상대", "rows": [["주장", "7:3", Y]]}]}),
        L("교통사고 변호사 채널 답변은, 블박차 잘못은 하나도 없어야 옳다는 소견.",
          [P("law", BB, s0=1.0, s1=1.12, fx=0.5, fy=0.6)], None, em=["하나도 없어야"],
          fx=[("correct_ding", "옳다는", 0.45)]),
        L("도로교통법 49조, 안전 확인 없이 차 문을 열면 안 됨.",
          [B("d02", "Close-up of a car door opening into a city street, side mirror, a blurred car passing by, daylight, no people visible")],
          None, say="도로교통법 사십구조, 안전 확인 없이 차 문을 열면 안 됨.", em=["차 문을 열면"],
          info={"kind": "quotes", "at": "도로교통법", "title": "도로교통법 49조 1항 7호", "items": [
              {"text": "안전 확인 없이", "at": "안전"}, {"text": "문 열기 금지", "at": "열면"}]}),
        L("댓글은 백대영은 힘들고 1대9라는 쪽과 무과실이라는 쪽으로 갈림.",
          [V("v1", ss=6, s0=1.2, s1=1.35, fx=0.6)], None, say="댓글은 백대영은 힘들고 일대구라는 쪽과 무과실이라는 쪽으로 갈림.",
          em=["1대9"]),
        L("글쓴이는 7대3은 못 받겠다며 소송을 준비 중임.",
          [V("v2", ss=3, s0=1.1, s1=1.2)], None, say="글쓴이는 칠대삼은 못 받겠다며 소송을 준비 중임.", em=["소송"]),
        L("님들은 이거 몇 대 몇 봄?", [V("v1", ss=5, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "불법주차 차가", "문을 확 열었는데 7:3?", "불법 주차 차량 개문사고, 상대 보험사 7:3 주장",
       "#개문사고 7:3 주장", "보배드림 베스트 1044550 교통사고/블박 (2026-11-01, 추천 22, 댓글 35)",
       [("10/16 개문사고, 좌회전 중 황색 실선, 횡단보도 위 불법 주정차 QM6 운전석 문이 열리며 조수석 측면 충돌", "원글 본문, 블박 영상"),
        ("주행 속도 약 10~20km/h", "원글 본문"),
        ("피해: 조수석 헤드라이트, 앞범퍼, 휀다, 사이드미러, 앞뒤문, 손잡이, 사이드스텝, 뒷범퍼, 휠", "원글 본문, 사진"),
        ("자기 보험사 10:0, 상대 보험사 10/27 7:3 주장, 소송 진행 예정", "원글 본문(대사는 상대 보험사 주장을 대사체로)"),
        ("변호사 채널 명예답변위원 '블박차의 잘못은 1도 없어야 옳겠다는 소견'", "원글 첨부 캡처"),
        ("도로교통법 49조 1항 7호: 안전 확인 없이 차 문을 열거나 내려서는 안 됨", "casenote 도로교통법 49조"),
        ("댓글 '백대영은 사실상 힘들고 1:9'(15), '블박 무과실 나와야죠'(9)", "원글 댓글")],
       "불법 주차한 SUV가 지나가는 순간 문을 확 열었는데, 상대 보험사는 7대3을 주장합니다.\n도로교통법 49조는 안전 확인 없이 문 여는 걸 금지합니다.\n님들은 몇 대 몇으로 보나요?\n\n#개문사고 #과실비율 #블랙박스 #보배드림 #란빵",
       "님들은 이거 몇 대 몇 봄?",
       COMMON, "변호사 사이트 캡처의 상단 로고(실명) 잘라냄. 상호(가게 이름) 안 씀.", [V("v2", ss=2, s0=1.0, s1=1.08)])


# ───────────────────────── 4. 차도 달리는 전동휠체어 ─────────────────────────
def EP_wheelroad():
    S = "wheelroad"
    vclip(S, "v1", "1044548_m0.mp4", 9.5, 11, cx=0.5, cy=0.42, zoom=1.0)
    lines = [
        L("인도도 있는데 왜 차도로 다니세요?",
          [V("v1", ss=2, s0=1.1, s1=1.2)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("왕복 2차선 도로가 이상하게 막혀서 봤더니.",
          [V("v1", s0=1.0, s1=1.06)], None, say="왕복 이차선 도로가 이상하게 막혀서 봤더니.", em=["막혀서"]),
        L("전동휠체어가 차도 한가운데를 천천히 달리는 중.",
          [V("v1", ss=2, s0=1.05, s1=1.2, punch=True)], None, em=["전동휠체어"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "차도", 0.4)]),
        L("바로 옆엔 인도가 따로 있었다고 함.",
          [V("v1", ss=4, s0=1.0, s1=1.1, fx=0.7)], None, em=["인도가"]),
        L("뒤차들은 추월도 못 하고 줄줄이 따라감.",
          [V("v1", ss=6, s0=1.0, s1=1.08)], None, em=["줄줄이"]),
        L("도로교통법상 보행보조용 의자차를 탄 사람은 보행자임.",
          [B("w01", "A mobility scooter parked on a Korean city sidewalk next to a curb and a road, daylight, no people")],
          None, em=["보행자"], em_color="yellow",
          info={"kind": "quotes", "at": "도로교통법상", "title": "도로교통법 2조", "items": [
              {"text": "보행보조용 의자차", "at": "의자차를"}, {"text": "= 보행자", "at": "보행자임"}]}),
        L("보도와 차도가 나뉜 길에선 보행자는 언제나 보도로 다녀야 함.",
          [B("w02", "A Korean road with a clearly separated sidewalk and curb, empty lanes, trees, daylight, no people")],
          None, em=["언제나 보도로"],
          info={"kind": "quotes", "at": "보도와", "title": "도로교통법 8조 1항", "items": [
              {"text": "보도로 통행", "at": "보도로"}, {"text": "공사 등 부득이하면 예외", "at": "다녀야"}]}),
        L("공사 같은 부득이한 경우만 예외.", [B("w02", s0=1.2, s1=1.3)], None, em=["부득이한 경우"]),
        L("댓글은 인도는 사람 많아서 차도로 다니는 거라는 말이 나옴.",
          [V("v1", ss=8, s0=1.0, s1=1.1)], None, em=["사람 많아서"]),
        L("사고 나면 보행자 사고가 돼서 운전자만 억울하다는 반응도.",
          [V("v1", ss=5, s0=1.15, s1=1.25, fx=0.6)], None, em=["운전자만 억울"]),
        L("님들 동네도 이런 거 자주 봄?", [V("v1", ss=3, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "왕복 2차선이 막힌 이유", "차도 위 전동휠체어", "인도 두고 차도로 달리는 전동휠체어",
       "#차도 위 전동휠체어", "보배드림 베스트 1044548 교통사고/블박 (2026-11-01, 추천 26, 댓글 7)",
       [("왕복 2차선 막히는 이유, 인도도 있는데 차도로 다님", "원글 본문, 영상"),
        ("보도 정의: 보행자(유모차, 보행보조용 의자차, 노약자용 보행기 등 포함)", "casenote 도로교통법 2조 10호"),
        ("보행자는 보도와 차도가 구분된 도로에서 언제나 보도로 통행, 차도 횡단, 공사 등 부득이한 경우 예외", "casenote 도로교통법 8조 1항"),
        ("댓글 '인도로 다니면 사람도 많고 하니까 그냥 차도를'(2), '저거 탄 순간 사람 신체로 여겨집니다'(0)", "원글 댓글"),
        ("'사고 나면 운전자만 억울' 은 댓글 요지 정리", "원글 댓글")],
       "왕복 2차선이 막혀서 보니 전동휠체어가 차도를 달리고 있었습니다.\n도로교통법상 전동휠체어를 탄 사람은 보행자라 보도로 다녀야 합니다.\n님들 동네도 이런 거 자주 보나요?\n\n#전동휠체어 #도로교통법 #블랙박스 #보배드림 #란빵",
       "님들 동네도 이런 거 자주 봄?",
       COMMON, "지하차도 이름이 보이는 앞부분(0~9초)은 안 씀. 탑승자는 뒷모습만.", [V("v1", ss=4, s0=1.0, s1=1.05)])


# ───────────────────────── 5. 밭에 뒤집힌 차 ─────────────────────────
def EP_flipcar():
    S = "flipcar"
    vclip(S, "v1", "1044306_m0.mp4", 22, 14, cx=0.72, cy=0.55, zoom=1.15)
    vclip(S, "v2", "1044306_m0.mp4", 50, 10, cx=0.62, cy=0.55, zoom=1.1)
    lines = [
        L("안에 사람 있어요? 괜찮으세요?",
          [V("v2", s0=1.1, s1=1.2)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("아침에 동네를 나가는데 전봇대가 부러져 있었음.",
          [B("f01", "A broken wooden utility pole leaning over a narrow Korean countryside road, telephone wires hanging low, morning sun, no people")],
          None, em=["전봇대가"]),
        L("그 옆 밭에 차 한 대가 완전히 뒤집혀 있었음.",
          [V("v1", s0=1.0, s1=1.08, punch=True)], None, em=["뒤집혀"], em_color="yellow",
          fx=[("hit_trailer_epic", "뒤집혀", 0.45)]),
        L("주변에 아무도 없어서 사고 난 지 얼마 안 된 줄 알았다고 함.",
          [V("v1", ss=6, s0=1.1, s1=1.2)], None, em=["아무도 없어서"]),
        L("혹시 안에 사람이 있을까 봐 밭으로 직접 내려감.",
          [V("v2", ss=3, s0=1.0, s1=1.1)], None, em=["직접 내려감"]),
        L("썬팅이 진해서 밖에서는 안이 하나도 안 보였음.",
          [V("v1", ss=9, s0=1.3, s1=1.45, fx=0.6)], None, em=["썬팅"]),
        L("문을 열어 보니 다행히 아무도 없었음.",
          [V("v2", ss=6, s0=1.1, s1=1.25)], None, em=["아무도 없었음"], fx=[("correct_ding", "다행히", 0.4)]),
        L("댓글은 통신 전주에 밭 손상 비용까지 나오겠다는 걱정.",
          [B("f01", s0=1.2, s1=1.3)], None, em=["밭 손상 비용"]),
        L("졸음이었나 보다, 음주는 아니길 바란다는 말도 나옴.",
          [V("v1", ss=11, s0=1.0, s1=1.08)], None, em=["음주는 아니길"]),
        L("시골에선 서너 달에 한 번꼴로 이런 걸 본다는 댓글도 있었음.",
          [B("f02", "A tow truck parked on a narrow Korean rural road next to harvested fields, mountains in the background, sunny morning, no people")],
          None, em=["서너 달에"]),
        L("님들은 저런 차 보면 직접 내려가 봄?", [V("v1", ss=4, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "봄")]),
    ]
    go(S, lines, "아침 출근길", "밭에 뒤집힌 차", "전봇대 부러뜨리고 밭에 뒤집힌 차, 직접 내려가 확인",
       "#밭에 뒤집힌 차", "보배드림 베스트 1044306 교통사고/블박 (2026-10-31, 추천 71, 댓글 8)",
       [("동네 나가는 길, 차량이 전화선 전봇대 부러뜨리고 밭에 전복, 아무도 없음", "원글 본문, 영상(2026-10-31 09:31)"),
        ("사고 난 지 얼마 안 돼서 차 안에 사람 있는 줄 알고 내려가 살펴봄, 다행히 사람 없음", "원글 본문"),
        ("썬팅이 진해 밖에서 안 보임, 문 열어보고 없는 줄 앎", "원글 본문"),
        ("댓글 '통신전주 + 밭 손상비용까지', '졸렸나봅니다', '음주운전자가 아니길', '시골에 3~4달에 한 번꼴로 봅니다'", "원글 댓글")],
       "아침에 동네를 나가는데 전봇대가 부러져 있고, 차 한 대가 밭에 뒤집혀 있었습니다.\n혹시 사람이 있을까 내려가 문을 열어 봤는데 다행히 아무도 없었습니다.\n님들은 이런 차 보면 직접 내려가 보나요?\n\n#전복사고 #블랙박스 #교통사고 #보배드림 #란빵",
       "님들은 저런 차 보면 직접 내려가 봄?",
       COMMON, "글쓴이 얼굴이 나오는 1분 20초 이후 구간은 안 씀. 밭 안의 사람은 멀리 작은 뒷모습만.", [V("v1", ss=5, s0=1.0, s1=1.05)])


# ───────────────────────── 6. 번호판 반사 스티커 ─────────────────────────
def EP_reflplate():
    S = "reflplate"
    cap(S, "p1", "1044543_00.jpg", nofaces=True, cx=0.5)
    cap(S, "p2", "1044543_01.jpg", nofaces=True, cx=0.5)
    lines = [
        L("이거 불법 맞죠?",
          [P("p1", BB, s0=1.0, s1=1.1)], None, dialogue=True, speaker=2, emotion="normal"),
        L("지하주차장에서 유독 번쩍이는 번호판이 하나 있었음.",
          [B("r01", "A Korean underground parking garage, rows of parked cars, fluorescent lights reflecting on the floor, no people, no readable license plates")],
          None, em=["번쩍이는 번호판"]),
        L("가까이 가 보니 판 위에 반사 스티커를 오려 붙인 것 같았다고 함.",
          [P("p1", BB, s0=1.1, s1=1.3, fx=0.4), P("p2", BB, at="반사", s0=1.0, s1=1.15)], None, em=["반사 스티커"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "반사", 0.4)]),
        L("빛을 받으면 숫자가 하얗게 날아가 보이는 식.",
          [P("p2", BB, s0=1.2, s1=1.4, fx=0.6)], None, em=["숫자가"]),
        L("댓글은 단속 피하고 사고 나면 도망가려는 거라는 반응.",
          [B("r02", "A speed enforcement camera on a pole above a Korean highway at dusk, motion blurred cars below, no people")],
          None, em=["단속 피하고"]),
        L("자동차관리법 10조, 번호판을 가리거나 알아보기 곤란하게 하면 안 됨.",
          [B("r01", s0=1.2, s1=1.3)], None, say="자동차관리법 십조, 번호판을 가리거나 알아보기 곤란하게 하면 안 됨.", em=["알아보기 곤란하게"],
          info={"kind": "quotes", "at": "자동차관리법", "title": "자동차관리법 10조 5항", "items": [
              {"text": "가리거나 알아보기 곤란", "at": "가리거나"}, {"text": "그런 차 운행도 금지", "at": "안"}]}),
        L("그런 차를 몰기만 해도 위반임.", [P("p1", BB, s0=1.0, s1=1.1)], None, em=["몰기만 해도"]),
        L("고의로 그랬다면 1년 이하 징역 또는 1천만원 이하 벌금.",
          [B("r03", "A Korean courtroom bench and gavel, wooden interior, soft light, no people")],
          None, say="고의로 그랬다면 일년 이하 징역 또는 천마넌 이하 벌금.", em=["1천만원"], em_color="yellow",
          fx=[("drop_futuristic", "징역", 0.5)]),
        L("바로 신고했더니 나중에 떼고 다니더라는 경험담도 있었음.",
          [B("r02", s0=1.2, s1=1.35)], None, em=["바로 신고"], fx=[("correct_ding", "떼고", 0.4)]),
        L("사진만으론 확인 안 된다고 할 수 있으니 영상으로 찍으라는 팁도.",
          [P("p2", BB, s0=1.0, s1=1.1)], None, em=["영상으로"], say="사진만으론 확인이 안 될 수 있음. 그래서 영상으로 찍으라는 팁도."),
        L("님들 주차장에도 이런 번호판 있음?", [P("p1", BB, s0=1.1, s1=1.2)], None, fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "지하주차장에서", "번쩍이는 번호판", "번호판에 반사 스티커, 자동차관리법 위반",
       "#번호판 반사 스티커", "보배드림 베스트 1044543 교통사고/블박 (2026-11-02, 추천 68, 댓글 14)",
       [("지하주차장에서 유독 반사가 잘되길래 보니 인위적으로 오린 듯, 불법 맞나요?", "원글 본문, 사진 2장"),
        ("자동차관리법 10조 5항: 누구든지 등록번호판을 가리거나 알아보기 곤란하게 하여서는 아니 되며, 그러한 자동차를 운행하여서도 아니 됨", "casenote 자동차관리법 10조"),
        ("81조 1의2호: 10조 5항 위반해 고의로 가리거나 알아보기 곤란하게 한 자, 1년 이하 징역 또는 1천만원 이하 벌금", "casenote 자동차관리법 81조"),
        ("댓글 '바로 신고했더니 나중에 제거한 상태'(13), '번호판 장난질은 상습 위반과 뺑소니를 위한 거'(5), '사진만으로 하면 확인 안 된다고 할 수 있으니 동영상 찍으세요'(3)", "원글 댓글"),
        ("'빛을 받으면 숫자가 하얗게 보이는 식' 은 원글 사진(플래시 반사)으로 설명", "원글 사진")],
       "지하주차장에서 유독 번쩍이는 번호판이 있었는데, 반사 스티커를 오려 붙인 것 같다는 제보입니다.\n자동차관리법은 번호판을 알아보기 어렵게 하는 걸 금지하고, 고의면 1년 이하 징역 또는 1천만원 이하 벌금입니다.\n님들 주차장에도 이런 차 있나요?\n\n#번호판 #반사스티커 #자동차관리법 #보배드림 #란빵",
       "님들 주차장에도 이런 번호판 있음?",
       COMMON, "사진엔 번호판 앞 두 자리만 보임(전체 번호 판독 불가).", [P("p2", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 7. 초4 자전거 쪽지 ─────────────────────────
def EP_kidnote():
    S = "kidnote"
    cap(S, "note", "1044193_00.jpg", fit=True, nofaces=True)
    cap(S, "msg", "1044193_01.jpg", fit=True, nofaces=True)
    cap(S, "bump", "1044193_02.jpg", nofaces=True, cx=0.6)
    lines = [
        L("제가 이런 일이 처음이라 편지를 남깁니다.",
          [P("note", BB, s0=1.0, s1=1.12)], None, dialogue=True, speaker=2, emotion="normal"),
        L("아파트 지상 주차장, 초등학교 4학년이 자전거를 타다 중심을 잃었음.",
          [B("k01", "A child's bicycle lying on its side on the paved ground of a Korean apartment outdoor parking lot, morning light, no people")],
          None, say="아파트 지상 주차장, 초등학교 사학년이 자전거를 타다 중심을 잃었음.", em=["4학년"]),
        L("자전거 뒷바퀴가 세워진 차 왼쪽 앞 범퍼 쪽에 닿음.",
          [P("bump", BB, s0=1.0, s1=1.12)], None, em=["앞 범퍼"]),
        L("그냥 가지 않고 연락처를 적은 쪽지를 남기고 학교에 감.",
          [P("note", BB, s0=1.2, s1=1.4, fx=0.5, fy=0.3)], None, em=["쪽지를 남기고"], em_color="yellow",
          fx=[("correct_ding", "쪽지를", 0.45)]),
        L("아빠는 학교 선생님 연락을 받고서야 알았다고 함.",
          [B("k02", "A Korean elementary school hallway with lockers and a window, morning light, no people")], None, em=["선생님 연락"]),
        L("차주는 앞 범퍼 긁힌 곳 사진을 보내옴.",
          [P("msg", BB, s0=1.0, s1=1.1), P("bump", BB, at="사진을", s0=1.3, s1=1.5, fx=0.6, fy=0.7)], None, em=["긁힌 곳"]),
        L("아빠는 그 자국은 원래 있던 걸 차주가 몰랐던 것 같다고 봄.",
          [P("bump", BB, s0=1.5, s1=1.7, fx=0.6, fy=0.75)], None, em=["원래 있던"]),
        L("CCTV 확인에, 그때 앞에 차가 있어서 거긴 들어갈 수도 없다고 설명함.",
          [B("k03", "A CCTV camera mounted on a pillar overlooking a Korean apartment parking lot, cars parked in rows, no people")],
          None, say="씨씨티비 확인에, 그때 앞에 차가 있어서 거긴 들어갈 수도 없다고 설명함.", em=["들어갈 수도 없다고"]),
        L("그러자 차주가 없던 일로 하자고 함.", [P("msg", BB, s0=1.1, s1=1.2)], None, em=["없던 일로"],
          fx=[("pop_bubble", "없던", 0.4)]),
        L("댓글은 아이 잘 키우셨다, 내일 로또는 당신이라는 반응.",
          [P("note", BB, s0=1.0, s1=1.08)], None, em=["로또는 당신"]),
        L("님들은 초4 때 이런 쪽지 쓸 수 있었음?", [B("k01", s0=1.1, s1=1.2)], None, say="님들은 초사 때 이런 쪽지 쓸 수 있었음?"),
    ]
    go(S, lines, "초4가 남긴 쪽지", "차주 반응이 반전", "자전거로 차 박은 초4의 쪽지, 차주는 긁힌 사진을 보냈는데",
       "#초4가 남긴 쪽지", "보배드림 베스트 1044193 자유게시판 (2026-10-30, 추천 110, 댓글 3)",
       [("작은아들 등굣길 아파트 지상 주차 차를 살짝 부딪힘, 왼쪽 바퀴쪽 휀다에 자전거 뒷바퀴 고무", "원글 본문"),
        ("쪽지 '초등학교 4학년, 자전거 타다가 중심을 잃고 넘어졌는데 왼쪽 앞범퍼 쪽을 박았습니다, 제가 이런 일이 처음이라 편지를 남깁니다'", "원글 첨부 쪽지(개인정보는 원글이 가림)"),
        ("학교 선생님 연락으로 알게 됨", "글쓴이 댓글"),
        ("차주가 긁힌 사진 보냄, 글쓴이는 차주가 평소 모르던 자국으로 봄", "원글 본문, 사진"),
        ("CCTV 확인, 당시 앞에 주차된 차가 있어 들어가지도 못한다고 하니 없던 일로", "원글 본문"),
        ("댓글 '내일 로또는 당신입니다'(2)", "원글 댓글")],
       "초등학교 4학년이 자전거로 주차된 차를 살짝 박고, 그냥 가지 않고 쪽지를 남겼습니다.\n차주는 긁힌 사진을 보냈지만 CCTV와 설명 뒤 없던 일로 하자고 했습니다.\n님들은 초4 때 이런 쪽지 쓸 수 있었나요?\n\n#자전거사고 #주차장 #쪽지 #보배드림 #란빵",
       "님들은 초4 때 이런 쪽지 쓸 수 있었음?",
       COMMON, "쪽지의 학교명, 이름, 연락처는 원글이 이모지로 가린 상태 그대로.", [P("note", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 8. 빌라 주차칸 오토바이 ─────────────────────────
def EP_villabike():
    S = "villabike"
    cap(S, "bike", "1044429_00.jpg", nofaces=True, cx=0.5)
    cap(S, "bikew", "1044429_00.jpg", fit=True, nofaces=True)
    lines = [
        L("나도 관리비 내는데...",
          [P("bikew", BB, s0=1.0, s1=1.1)], None, dialogue=True, speaker=2, emotion="sad"),
        L("빌라 필로티 주차장, 자동차 칸에 오토바이 세 대가 서 있음.",
          [P("bike", BB, s0=1.0, s1=1.12)], None, em=["오토바이 세 대"], em_color="yellow"),
        L("글 제목은 우리 빌라 주차장 멋집니다, 이래도 되나요.",
          [P("bikew", BB, s0=1.1, s1=1.2)], None, em=["멋집니다"]),
        L("배달하는 사람들 숙소냐는 댓글엔 그건 아니라고 함.",
          [B("v01", "Delivery scooters with rear boxes parked in a row on a Korean street at dusk, no people, no readable plates")],
          None, em=["숙소"]),
        L("주인이 본가에 갔다 오면 그 자리에 자기 차를 넣는다고.",
          [P("bike", BB, s0=1.3, s1=1.45, fx=0.7)], None, em=["자기 차를"]),
        L("결국 1년 365일 그 칸은 그 사람 자리인 셈.",
          [B("v02", "An empty parking space in a Korean villa ground-floor parking lot with a scooter parked across it, evening light, no people")],
          None, say="결국 일년 삼백육십오일 그 칸은 그 사람 자리인 셈.", em=["365일"], em_color="yellow",
          fx=[("wrong_gameshow_buzz", "자리인", 0.45)]),
        L("댓글 추천 1위는 옆에 같이 오토바이, 자전거를 세우라는 것.",
          [P("bikew", BB, s0=1.0, s1=1.1)], None, em=["같이 오토바이"], say="댓글 추천 일위는 옆에 같이 오토바이, 자전거를 세우라는 것."),
        L("중고 오토바이 하나 사서 똑같이 자리 차지하라는 말도.",
          [B("v01", s0=1.2, s1=1.3)], None, em=["똑같이"]),
        L("거울치료에, 함부로 옮기면 재물손괴로 조치한다는 메모까지 붙이라고.",
          [B("v03", "A handwritten paper note taped to the seat of a parked scooter, close-up, blurred parking lot behind, no people")],
          None, em=["거울치료"]),
        L("주차칸 알박기에 다들 칼같이 반응함.",
          [P("bike", BB, s0=1.0, s1=1.08)], None, em=["알박기"]),
        L("님들은 이런 알박기 어떻게 대응함?", [P("bikew", BB, s0=1.1, s1=1.2)], None, fx=[("pop_bubble", "대응함")]),
    ]
    go(S, lines, "빌라 주차장에", "오토바이 알박기", "빌라 자동차 주차칸을 오토바이로 365일 알박기",
       "#주차칸 오토바이 알박기", "보배드림 베스트 1044429 자유게시판 (2026-11-01, 추천 652, 댓글 66)",
       [("'우리 빌라 주차장!! 멋집니다 이래도되나요???!!', 사진 1장(필로티 주차칸에 오토바이 3대)", "원글 제목, 사진"),
        ("'딸배들 숙소인가' 댓글에 글쓴이 '아녀 그건 아닙니다'", "원글 댓글"),
        ("글쓴이 '본가 갔다가 돌아오면 자기차 넣습니다, 1년 365일 자기자리네요, 나두 관리비 내는데'", "글쓴이 댓글(대사 인용)"),
        ("'옆에 같이 오토바이 주차, 자전거 주차'(13), '중고 오토방구 하나 사서 똑같이'(3), '거울치료, 임의 이동 시 재물손괴로 법적조치 메모'(3)", "원글 댓글")],
       "빌라 주차장 자동차 칸에 오토바이가 서 있고, 주인은 본가에 갔다 오면 그 칸에 자기 차를 넣는다고 합니다.\n1년 365일 그 사람 자리인 셈입니다.\n님들은 이런 알박기 어떻게 대응하나요?\n\n#주차장 #알박기 #빌라주차 #보배드림 #란빵",
       "님들은 이런 알박기 어떻게 대응함?",
       COMMON, "제목이 14자 넘어 '#주차칸 오토바이 알박기' 로 줄임. 오토바이 번호판 판독 안 됨.", [P("bike", BB, s0=1.0, s1=1.05)])


# ───────────────────────── 9. 벤츠에 침 ─────────────────────────
def EP_spit4():
    S = "spit4"
    lines = [
        L("꼭 도와주세요, 참교육 하고 싶습니다.",
          [B("s01", "A dark luxury sedan parked in front of a small Korean villa building on a narrow alley, evening, no people, no readable plates")],
          None, dialogue=True, speaker=2, emotion="toneup"),
        L("뽑은 지 2년 안 된 벤츠 E클래스, 빌라 앞에만 대면 일이 생김.",
          [B("s01", s0=1.1, s1=1.2)], None, say="뽑은 지 이년 안 된 벤츠 이클래스, 빌라 앞에만 대면 일이 생김.", em=["빌라 앞에만"]),
        L("누군가 운전석 창문에 침을 뱉고 감.",
          [B("s02", "Close-up of a car driver's side window with a wet splash mark on the glass, alley background blurred, no people")],
          None, em=["침을 뱉고"], em_color="yellow", fx=[("wrong_gameshow_buzz", "침을", 0.45)]),
        L("벌써 4번째, 3번째와 4번째엔 경찰에 신고하고 사진도 남김.",
          [B("s02", s0=1.3, s1=1.45)], None, say="벌써 네번째, 세번째와 네번째엔 경찰에 신고하고 사진도 남김.", em=["4번째"]),
        L("블박은 앞만 찍혀서 옆 창문은 안 나왔다고 함.",
          [B("s03", "A dashcam mounted behind a car windshield at night, the side window visible and dark, no people")], None, em=["안 나왔다고"]),
        L("의심 가는 사람은 최근 이사 온 50대로 추정.",
          [B("s04", "A narrow Korean residential alley at night with villa buildings and a few parked cars, streetlight, no people")],
          None, say="의심 가는 사람은 최근 이사 온 오십대로 추정.", em=["50대"]),
        L("그 집 앞에 차를 대면 그 사람이 자기 집 앞에 못 댄다고.",
          [B("s04", s0=1.2, s1=1.3)], None, em=["자기 집 앞에"]),
        L("경찰은 침으로 차가 망가지지 않으면 재물손괴 처벌이 어렵다고 함.",
          [B("s05", "A Korean police station front desk with forms and a pen, fluorescent light, no people")],
          None, em=["재물손괴"]),
        L("그런데 댓글 추천 1위는 그냥 불법주차 아니냐는 반응.",
          [B("s01", s0=1.3, s1=1.4)], None, em=["불법주차"], em_color="yellow", pop=("반전", R, "불법주차"), say="그런데 댓글 추천 일위는 그냥 불법주차 아니냐는 반응."),
        L("그 사람이 자기 집 앞에 댈 수 있게 해 주면 된다는 댓글도.",
          [B("s04", s0=1.0, s1=1.08)], None, em=["댈 수 있게"]),
        L("님들은 이거 누구 편임?", [B("s02", s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "편임")]),
    ]
    go(S, lines, "빌라 앞에 세울 때마다", "벤츠 창문에 침", "빌라 앞 주차할 때마다 벤츠 창문에 침, 댓글은 반전",
       "#벤츠 창문에 침 4번", "보배드림 베스트 1044422 자유게시판 (2026-11-01, 추천 26, 댓글 6)",
       [("뽑은 지 2년 안 된 벤츠 E클래스, 특정 구역 주차하면 반복적으로 운전석 창문에 침", "원글 본문"),
        ("블박엔 정면만 찍혀 안 찍힘, CCTV 달 예정", "원글 본문"),
        ("4회 정도, 3, 4회 때 경찰 신고 및 사진", "원글 본문"),
        ("이사 온 지 얼마 안 된 50대 추정, 빌라 앞에 주차하면 그 사람은 자기집 앞에 주차 못 함", "원글 본문"),
        ("경찰 '물질적 피해가 없으면 재물손괴 처벌이 힘들 수도'", "원글 본문"),
        ("'꼭 도와주세요, 꼭 참교육 하고싶습니다'", "원글 본문(대사 인용)"),
        ("댓글 '말이 빌라앞주차지 그냥 불법주차 아녜요?'(11), '그 사람이 자기집 앞에 주차를 할 수 있도록 차를 대면 됩니다'(9)", "원글 댓글")],
       "빌라 앞에 차를 댈 때마다 누군가 벤츠 운전석 창문에 침을 뱉고 간다는 제보입니다.\n경찰은 재물손괴 처벌이 어렵다고 했고, 댓글은 그냥 불법주차 아니냐는 반응이었습니다.\n님들은 누구 편인가요?\n\n#주차갈등 #빌라주차 #재물손괴 #보배드림 #란빵",
       "님들은 이거 누구 편임?",
       COMMON, "첨부 사진 없음, 화면 전부 AI 배경(번호판, 엠블럼 없음).", [B("s04", s0=1.0, s1=1.05)])


# ───────────────────────── 10. 아반떼 100만원 할인 ─────────────────────────
def EP_avantesale():
    S = "avantesale"
    cap(S, "promo", "1044462_00.webp", box=(0, 0, 1080, 340), fit=True, nofaces=True)
    cap(S, "cockpit", "1044462_00.webp", box=(35, 690, 1045, 1330), nofaces=True)
    cap(S, "news", "1044466_00.jpg", fit=True, nofaces=True)
    lines = [
        L("볶음밥 시키면 짜장 소스를 특별히 준다고?",
          [P("cockpit", BB, s0=1.0, s1=1.12)], None, dialogue=True, speaker=2, emotion="toneup"),
        L("현대차가 K세일페스타로 아반떼 가솔린을 100만원 기본 할인함.",
          [P("news", BB, s0=1.0, s1=1.12, fx=0.5, fy=0.3)], None, say="현대차가 케이세일페스타로 아반떼 가솔린을 백마넌 기본 할인함.",
          em=["100만원"], em_color="yellow", pop=("100만원 할인", Y, "100만원")),
        L("모던 가솔린엔 9.9인치 슬림 디스플레이를 무상으로 달아 줌.",
          [P("promo", BB, s0=1.0, s1=1.15)], None, say="모던 가솔린엔 구쩜구인치 슬림 디스플레이를 무상으로 달아 줌.", em=["무상으로"]),
        L("보배에선 옵션이던 계기판을 공짜로 준다며 와 소리가 나옴.",
          [P("cockpit", BB, s0=1.1, s1=1.3, fx=0.4)], None, em=["공짜로"], fx=[("correct_ding", "공짜로", 0.4)]),
        L("그런데 댓글 반응은 차가웠음.", [P("news", BB, s0=1.2, s1=1.35)], None, em=["차가웠음"]),
        L("원래 주던 걸 빼놓고 이제 와서 선심 쓰냐는 것.",
          [P("cockpit", BB, s0=1.3, s1=1.45, fx=0.6)], None, em=["선심 쓰냐"]),
        L("국산차 시작 가격이 너무 비싸졌다는 댓글이 추천 1위.",
          [B("a01", "A Korean car dealership showroom with a compact sedan on display under bright lights, price tag stand blurred, no people")],
          None, em=["너무 비싸졌다"], em_color="yellow", say="국산차 시작 가격이 너무 비싸졌다는 댓글이 추천 일위."),
        L("6단 수동 넣어 주면 더 팔리겠다는 농담도 나옴.",
          [B("a02", "Close-up of a six-speed manual gear shifter in a car interior, soft light, no people")],
          None, say="육단 수동 넣어 주면 더 팔리겠다는 농담도 나옴.", em=["6단 수동"]),
        L("그랜저와 싼타페도 할인하고, 현대차 행사는 12월 31일까지.",
          [P("promo", BB, s0=1.1, s1=1.2)], None, say="그랜저와 싼타페도 할인하고, 현대차 행사는 십이월 삼십일일까지.", em=["12월 31일까지"]),
        L("기아는 11월 한 달 동안 할인함.",
          [B("a01", s0=1.2, s1=1.3)], None, say="기아는 십일월 한 달 동안 할인함.", em=["11월 한 달"]),
        L("님들은 계기판 없는 차 탈 수 있음?", [P("cockpit", BB, s0=1.0, s1=1.1)], None, fx=[("pop_bubble", "있음")]),
    ]
    go(S, lines, "아반떼 100만원 할인", "계기판 공짜라는데", "K세일페스타 아반떼 100만원 할인, 디스플레이 무상 장착",
       "#아반떼 100만원 할인", "보배드림 베스트 1044462, 1044466 국산차 + 현대차그룹 11/1 K세일페스타 발표 (머니투데이 469/0000962927, 한국일보 A2026110114520002437, 메트로 20261101500215)",
       [("현대차 11/1~12/31, 기아 11월 한 달 K세일페스타 프로모션", "한국일보, 메트로(일치)"),
        ("아반떼 가솔린 100만원 기본 할인, 모던 가솔린 9.9인치 슬림 디스플레이 + 컨비니언스I, 모던 하이브리드 9.9인치 + 컨비니언스II 무상", "한국일보, 메트로"),
        ("그랜저 프리미엄 스마트센스I, 익스클루시브 스마트센스II 무상, 싼타페 100만원 할인", "한국일보, 메트로"),
        ("보배 글 '전면 계기판(옵션)을 무료로 준다고!!!'", "1044462 첨부(옵션 가격은 확인 안 돼 대본에 안 씀)"),
        ("댓글 '볶음밥을 시키면 특별히 짜장쏘스와 짬뽕국물을 준다고?'(7), '국산차 초기값이 너무 비싸짐'(75), '6단수동 넣어주면 좀더 팔리겠네'(33)", "1044462, 1044466 댓글")],
       "현대차가 K세일페스타로 아반떼 가솔린을 100만원 할인하고, 9.9인치 슬림 디스플레이를 무상으로 달아 줍니다.\n보배드림 반응은 원래 주던 걸 이제 와서 선심 쓰냐는 쪽이었습니다.\n행사는 12월 31일까지입니다.\n\n#아반떼 #현대차할인 #K세일페스타 #보배드림 #란빵",
       "님들은 계기판 없는 차 탈 수 있음?",
       "자동차 블랙박스 2채널, 차량용 핸드폰 거치대, 자동차 시트커버, 차량용 방향제, 자동차 햇빛가리개",
       "35만원 옵션가는 보배 글에만 있고 공식 확인이 안 돼 안 씀.", [P("promo", BB, s0=1.0, s1=1.05)], typ="란빵 자동차, 신차")


EPS = [EP_busfall, EP_leftcross, EP_door73, EP_wheelroad, EP_flipcar, EP_reflplate, EP_kidnote, EP_villabike, EP_spit4, EP_avantesale]

if __name__ == "__main__":
    want = sys.argv[1:]
    for f in EPS:
        if not want or f.__name__[3:] in want:
            f()
