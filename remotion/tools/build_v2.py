#!/usr/bin/env python3
"""란빵 쇼츠 v2 빌더 — work/<slug>/v2/shots.json + work/<slug>/tts/ → remotion/public/<slug>/data.json (+ 소재 복사)

  python3 tools/build_v2.py <slug>            # data.json 만들기
  python3 tools/build_v2.py <slug> --render   # + Remotion 렌더 → work/<slug>/<slug>_v2.mp4

shots.json = {"title":[줄1,줄2], "tempo":1.3, "lines":[{ "shots":[...], "hl":[...], "sfx":[[이름,"어절"]], "pop":[글자,색,"어절"], "shake":"어절" }, ...]}
 - lines 순서 = script.json lines 순서(마지막 '구독!' 포함). 컷 shot = {"img": "ai/a01.png" | "real/sv1.jpg", "at": "어절"(없으면 줄 시작),
   "s0","s1","fx","fy"(,"fx1","fy1"), "punch":bool, "credit": "사진: …"}
 - "어절" 은 그 줄 대사 안의 단어 일부 — 그 단어가 읽히는 시점(글자 수 비례 추정)에 맞춘다.
 - 자막·강조는 script.json(em·em_color) 기준, ssul render.py 와 같은 모양의 정지 PNG(애니메이션 없음).
효과음은 강조 어절에만 건다(컷 전환음 없음 — 2026-10-10 사용자 지시).
"""
import json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
# 자막은 기존 란빵(ssul pipeline/render.py sub_box)과 픽셀 단위로 같게 — 그 함수들을 그대로 쓴다(2026-10-10 사용자 지시: 자막 애니메이션 없이 기존 스타일)
sys.path.insert(0, os.path.expanduser("~/Desktop/kim/ssul/pipeline"))
import render as R          # noqa: E402
import layout as L          # noqa: E402
import subs                 # noqa: E402
from PIL import Image, ImageDraw   # noqa: E402
RM = os.path.dirname(HERE)
RB = os.path.dirname(RM)
FPS = 30
SLUG = sys.argv[1]
WK = os.path.join(RB, "work", SLUG)
V2 = os.path.join(WK, "v2")
PUB = os.path.join(RM, "public", SLUG)
spec = json.load(open(os.path.join(V2, "shots.json"), encoding="utf-8"))
timing = json.load(open(os.path.join(WK, "tts", "timing.json"), encoding="utf-8"))
scj = json.load(open(os.path.join(WK, "script.json"), encoding="utf-8"))
TEMPO = spec.get("tempo", L.SPEED)   # 기존 란빵 배속(layout.SPEED) 그대로
assert len(spec["lines"]) == len(timing), (len(spec["lines"]), len(timing))
os.makedirs(PUB, exist_ok=True)
for _f in os.listdir(PUB):
    if _f.startswith("cap_"):
        os.remove(os.path.join(PUB, _f))

# 나레이션 배속
narr = os.path.join(PUB, "narr.wav")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(WK, "tts", "narration.wav"),
                "-af", f"atempo={TEMPO}", "-ar", "44100", narr], check=True)
ndur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                      "-of", "csv=p=0", narr]).decode())
# BGM — shots.json "bgm": "bgm/<파일>" 로 편마다 바꾼다(ssul/assets 기준, 2026-10-10 사용자 "bgm 다른걸로").
# 다른 곡은 기본곡과 같은 크기(-26 LUFS)로 맞춰서 bgmVol 을 그대로 쓴다.
bgm = os.path.join(PUB, "bgm.mp3")
# v2 기본곡 = bgm/sneaky-123.mp3(tools/bgm_sneaky.py 합성, 2026-10-10 사용자 확정)
_bsrc = os.path.expanduser(os.path.join("~/Desktop/kim/ssul/assets", spec.get("bgm", "bgm/sneaky-123.mp3")))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", _bsrc, "-af", "lowpass=f=6000,loudnorm=I=-26:TP=-3:LRA=11",
                "-ar", "44100", "-b:a", "192k", bgm], check=True)


def weight(word):
    w = 0.0
    for ch in word:
        if ch.isdigit():
            w += 1.7           # 숫자는 한글로 길게 읽힌다(1998 → 천구백구십팔)
        elif ch in "%":
            w += 2.5
        elif re.match(r"[가-힣A-Za-z]", ch):
            w += 1.0
        elif ch in ".,·":
            w += 0.4
    return max(w, 0.5)


# 효과음 — 기본은 이슈쿠키 효과음 라이브러리(ssul/assets/sfx/issuecookie, 141개, 2026-10-11 사용자 "이 효과음 저장하고 사용해줘").
# shots.json sfx = [이름, "어절"(, 볼륨)]. 이름 = 라이브러리 파일 이름(_목록.txt) 또는 아래 예전 짧은 이름(→ 라이브러리 곡으로 연결).
# "synth:boom" 처럼 쓰면 예전 ffmpeg 합성음(public/sfx/*.wav).
SFX_LIB = os.path.expanduser("~/Desktop/kim/ssul/assets/sfx/issuecookie")
SFX_ALIAS = {"boom": "boom_zoom_impact", "hit": "punch_strong", "ding": "correct_ding", "sting": "scratch_vinyl",
             "crack": "glass_break", "pop": "pop_bubble", "cash": "cash_register_fake", "siren": "synth:siren"}
SFX_VOL = {"boom": 0.9, "hit": 0.7, "ding": 0.55, "sting": 0.7, "crack": 0.8, "siren": 0.35, "pop": 0.6, "cash": 0.6}
SFX_CREDIT = {"cash_register", "heart_heavy"}   # 목록에 [표기 필요/권장] — 출처 표기 없이 쓰지 않는다
os.makedirs(os.path.join(RM, "public", "sfx", "ic"), exist_ok=True)


def sfx_src(name):
    name = SFX_ALIAS.get(name, name)
    if name.startswith("synth:"):
        n = name[6:]
        return f"sfx/{n}.wav", SFX_VOL.get(n, 0.6)
    assert name not in SFX_CREDIT, f"{name} 은 출처 표기가 필요한 효과음 — 다른 걸 고른다"
    f = os.path.join(SFX_LIB, name + ".wav")
    if not os.path.exists(f):   # 2026-10-13 wav 가 ssul/assets/sfx/ic/ 로 옮겨짐 — 두 곳 다 찾는다
        f = os.path.join(os.path.dirname(SFX_LIB), "ic", name + ".wav")
    assert os.path.exists(f), f"효과음 없음: {name} (ssul/assets/sfx/issuecookie/_목록.txt 참고)"
    dst = os.path.join(RM, "public", "sfx", "ic", name + ".wav")
    if not os.path.exists(dst):
        shutil.copy(f, dst)
    return f"sfx/ic/{name}.wav", 0.5   # 라이브러리는 피크 -1dBFS 로 맞춰 둠


def sub_png(sub_text, spans, em_color, dialogue, out):
    """render.py build_overlay() 의 sub_box 분기를 그대로 옮김 — 투명 바탕에 검은 박스+자막만."""
    im = Image.new("RGBA", (L.W, L.H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx, inner = L.W // 2, L.W - L.SIDE_PAD * 2
    sub_font = L.F_DLG if dialogue else L.F_SUB
    sub_fill = (L.DLG_C + (255,)) if dialogue else (255, 255, 255, 255)
    sf = R.font(sub_font, int(L.SZ_SUB * L.EM_SIZE_R) if dialogue else L.SZ_SUB)
    while R.tracked_width(sub_text, sf, L.SUB_TRACK) > inner and sf.size > 32:
        sf = R.font(sub_font, sf.size - 2)
    b = sf.getbbox(sub_text)
    tw, th = R.tracked_width(sub_text, sf, L.SUB_TRACK), b[3] - b[1]
    pad_x, pad_y = 26, 18
    box_bot = L.px(L.CONTENT_BOT) - 24
    box_top = box_bot - th - pad_y * 2
    im.paste((0, 0, 0, 255), (int(cx - tw / 2 - pad_x), int(box_top), int(cx + tw / 2 + pad_x), int(box_bot)))
    y = box_top + pad_y - b[1]
    runs = R.split_runs(sub_text, spans)
    if not dialogue and any(e for _, e in runs):
        ef = R.font(L.F_EM, max(12, int(sf.size * L.EM_SIZE_R)))
        while R.runs_width(runs, sf, ef, L.SUB_TRACK) > inner and sf.size > 32:
            sf = R.font(L.F_SUB, sf.size - 2)
            ef = R.font(L.F_EM, max(12, int(sf.size * L.EM_SIZE_R)))
        R.draw_runs(d, cx, y + sf.getmetrics()[0], runs, sf, ef, (255, 255, 255, 255),
                    R.em_fill(em_color), L.SUB_TRACK, stroke=0)
    else:
        R.center_tracked(d, cx, y, sub_text, sf, sub_fill, L.SUB_TRACK, stroke=0)
    im.save(out)


fr = lambda sec: int(round(sec * FPS))
# 자막 덩어리 시간 = 실제 음성 기준(2026-10-16 사용자 지적 "자막이랑 나레이션이 안 맞음").
# 예전 subs.split_duration 은 화면 글자 수 비례라 숫자("0.81초" 5자 → "영 점 팔일 초")·쉼표 쉼에서 자막이 앞서갔다.
# → 덩어리마다 읽는 음절 수(num_ko 로 숫자를 한글로)로 나누고, line wav 의 무음 구간은 빼고 발화 구간에만 배분한다.
sys.path.insert(0, os.path.expanduser("~/Desktop/kim/ssul/pipeline"))
try:
    from tts_issuecookie import num_ko   # noqa: E402
except Exception:
    num_ko = lambda s: s


def speech_segs(wav):
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", wav]).decode())
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", wav, "-af", "silencedetect=n=-35dB:d=0.12", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    ss = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", err)]
    se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    se += [dur] * (len(ss) - len(se))
    segs, cur = [], 0.0
    for a, b in zip(ss, se):
        a = max(a, 0.0)
        if a > cur + 0.02:
            segs.append((cur, a))
        cur = max(cur, b)
    if dur > cur + 0.02:
        segs.append((cur, dur))
    return segs or [(0.0, dur)]


def spoken_split(i, chunks, total):
    wav = os.path.join(WK, "tts", f"line_{i:03d}.wav")
    if len(chunks) < 2 or not os.path.exists(wav):
        return subs.split_duration(chunks, total)
    w = [max(1, len(re.findall(r"[가-힣A-Za-z]", num_ko(c)))) for c in chunks]
    segs = speech_segs(wav)
    S = sum(b - a for a, b in segs)

    def at(f):   # 발화 시간 f 초 지점 → 실제 시각(쉼 구간 건너뜀, 경계면 다음 발화 시작)
        for a, b in segs:
            if f < (b - a) - 1e-6:
                return a + f
            f -= b - a
        return segs[-1][1]
    starts, acc = [0.0], 0
    for x in w[:-1]:
        acc += x
        starts.append(at(S * acc / sum(w)))
    ds = [round(starts[k + 1] - starts[k], 3) for k in range(len(starts) - 1)]
    ds.append(round(total - sum(ds), 3))
    return ds


shots, caps, sfx, pops, shakes, infos, chars = [], [], [], [], [], [], []


def word_time(li, word):
    """li 번째 줄에서 word 가 읽히는 시각(초). word 없으면 줄 시작."""
    tm = timing[li]
    st, du = tm["start"] / TEMPO, tm["dur"] / TEMPO
    if not word:
        return st
    text = tm["text"].rstrip(".")
    pos = text.find(word)
    assert pos >= 0, (li, word, text)
    pre = text[:pos]
    return st + du * weight(pre.replace(" ", "")) / max(weight(text.replace(" ", "")), 0.1) if pre.strip() else st


def at_time(li, ref):
    """인포그래픽 시점 — "어절" 은 그 줄, "+1:어절" 은 다음 줄."""
    if ref and re.match(r"^\+\d+:", ref):
        k, w = ref[1:].split(":", 1)
        return word_time(li + int(k), w)
    return word_time(li, ref)
copied = set()
for li, (ln, tm) in enumerate(zip(spec["lines"], timing)):
    st, du = tm["start"] / TEMPO, tm["dur"] / TEMPO
    text = tm["text"].rstrip(".")

    def when(word):
        if not word:
            return st
        pos = text.find(word)
        assert pos >= 0, (li, word, text)
        pre = text[:pos]
        return st + du * weight(pre.replace(" ", "")) / max(weight(text.replace(" ", "")), 0.1) if pre.strip() else st

    # 자막 — ssul render.py main() 과 같은 덩어리·시간 배분·강조(script.json em/em_color)
    sl = scj["lines"][tm.get("i", li)]
    sl = sl if isinstance(sl, dict) else {}
    norm = " ".join(tm["text"].split())
    spans = R.em_spans(norm, sl.get("em"))
    rch = subs.chunk(tm["text"], L.SUB_CHUNK)
    rdu = spoken_split(tm.get("i", li), rch, tm["dur"])
    t0, pos = st, 0
    for c, d in zip(rch, rdu):
        off = norm.find(c, pos)
        off = pos if off < 0 else off
        pos = off + len(c)
        png = os.path.join(PUB, f"cap_{len(caps):03d}.png")
        sub_png(c, R.chunk_spans(c, off, spans), sl.get("em_color"), bool(sl.get("dialogue")), png)
        caps.append({"from": fr(t0), "dur": max(1, fr(t0 + d / TEMPO) - fr(t0)), "png": f"{SLUG}/{os.path.basename(png)}"})
        t0 += d / TEMPO
    # 컷
    for si, s in enumerate(ln["shots"]):
        a = when(s.get("at")) if si else st
        # 영상 컷(2026-10-16 roadster): "vid": "vid/v01.mp4" — 1080x960 무음으로 미리 잘라 둔 클립. 컷이 클립보다 길면 느리게 재생
        src = s.get("vid") or s["img"]
        key = src.replace("/", "_")
        if key not in copied:
            shutil.copy(os.path.join(V2, src), os.path.join(PUB, key)); copied.add(key)
        sh = {"src": f"{SLUG}/{key}", "from": fr(a), "s0": s.get("s0", 1.0), "s1": s.get("s1", 1.08),
              "fx": s.get("fx", 0.5), "fy": s.get("fy", 0.5), "fx1": s.get("fx1"), "fy1": s.get("fy1"),
              "punch": s.get("punch", False), "credit": s.get("credit")}
        if s.get("vid"):
            sh["vid"] = True
            sh["vdur"] = int(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                                            "-of", "csv=p=0", os.path.join(V2, src)]).decode()) * FPS) - 1
            sh["vss"] = fr(s.get("ss", 0))
        shots.append(sh)
    for e in ln.get("sfx", []):
        name, word = e[0], e[1]
        src, vol = sfx_src(name)
        sfx.append({"src": src, "from": max(0, fr(when(word)) - 2), "vol": e[2] if len(e) > 2 else vol})
    if ln.get("pop"):
        t, col, word = ln["pop"]
        a = fr(when(word))
        pops.append({"from": a, "dur": max(12, min(24, fr(st + du) - a + 6)), "text": t, "color": col})   # 다음 문장 컷까지 넘어가지 않게
    # いらすとや 캐릭터(2026-10-20): "char": "ir_x" | {"name","side":"l"|"r","h":픽셀,"at":"어절","flip"} | [그런 것 여러 개]
    # 파일 = v2/ir/<name>.png. 다음 캐릭터가 나올 때까지 서 있고, 같은 캐릭터·같은 자리면 다시 튀어오르지 않는다
    cl = ln.get("char")
    for c in (cl if isinstance(cl, list) else [cl] if cl else []):
        c = {"name": c} if isinstance(c, str) else dict(c)
        key = f"ir_{c['name'].removeprefix('ir_')}.png"
        if key not in copied:
            shutil.copy(os.path.join(V2, "ir", key), os.path.join(PUB, key)); copied.add(key)
        chars.append({"from": fr(when(c.get("at"))), "src": f"{SLUG}/{key}", "side": c.get("side", "r"),
                      "h": c.get("h", 560), "flip": bool(c.get("flip"))})
    if ln.get("shake"):
        shakes.append({"from": fr(when(ln["shake"])), "dur": 10, "amp": 18})
    # 인포그래픽 — "at" 어절부터 span 줄 끝까지. 항목 at/flash 는 info 시작 기준 프레임으로 바꾼다
    if ln.get("info"):
        inf = dict(ln["info"])
        a = fr(at_time(li, inf.pop("at", None)))
        last = timing[li + inf.pop("span", 1) - 1]
        end = fr((last["start"] + last["dur"]) / TEMPO)
        items = []
        for it in inf.pop("items"):
            it = dict(it)
            it["at"] = max(0, fr(at_time(li, it.get("at"))) - a)
            if "flash" in it:
                it["flash"] = fr(at_time(li, it["flash"])) - a
            items.append(it)
        infos.append({"from": a, "dur": max(15, end - a), "items": items, **inf})

total = fr(ndur) + 15
for i, s in enumerate(shots):   # 컷 길이 = 다음 컷 시작까지
    nxt = shots[i + 1]["from"] if i + 1 < len(shots) else total
    s["dur"] = max(1, nxt - s["from"])
    if s.get("vid") and s["dur"] > s["vdur"] - s["vss"]:
        print(f"  ⚠ 영상 컷 {s['src']} 길이 부족: 컷 {s['dur']}f > 클립 {s['vdur'] - s['vss']}f → 느리게 재생")
    for k in ("fx1", "fy1", "credit"):
        if s[k] is None:
            del s[k]
for i, c in enumerate(chars):   # 캐릭터 = 다음 캐릭터 시작까지(마지막은 끝까지)
    nxt = chars[i + 1]["from"] if i + 1 < len(chars) else total
    c["dur"] = max(1, nxt - c["from"])
    prev = chars[i - 1] if i else None
    c["pop"] = not (prev and prev["src"] == c["src"] and prev["side"] == c["side"] and prev["from"] + prev["dur"] == c["from"])
for i, c in enumerate(caps):    # 자막 사이 빈틈 없이 다음 자막까지 유지
    if i + 1 < len(caps):
        c["dur"] = max(c["dur"], caps[i + 1]["from"] - c["from"])
# 타이틀 크기 — ssul render.py fit_tracked 와 같은 방식(두 줄 중 작은 쪽, 폭 1080-80*2, 상한 120, 자간 -1)
from PIL import ImageFont
JAL = os.path.expanduser("~/Desktop/kim/ssul/fonts/JalnanGothic.otf")


def tracked_w(text, size, track=-1):
    f = ImageFont.truetype(JAL, size)
    return sum(f.getlength(c) for c in text) + track * (len(text) - 1)


def fit(text, cap=120, inner=1080 - 160):
    return max(s for s in range(12, cap + 1) if tracked_w(text, s) <= inner)


title = spec.get("title") or [scj["title_line1"], scj["title_line2"]]
t_size = min(fit(t) for t in title)
bar = None
bar_text = (scj.get("style") or {}).get("bar")
if bar_text:
    pf = os.path.expanduser("~/Desktop/kim/ssul/fonts/Pretendard-SemiBold.ttf")
    bsz = max(s for s in range(12, 65) if ImageFont.truetype(pf, s).getlength(bar_text) <= 1080 - 80)
    bar = {"text": bar_text, "size": bsz, "until": fr((timing[0]["start"] + timing[0]["dur"]) / TEMPO)}
data = {"fps": FPS, "total": total, "title": title, "titleSize": t_size, "bar": bar, "narr": f"{SLUG}/narr.wav", "bgm": f"{SLUG}/bgm.mp3",
        "bgmVol": spec.get("bgmVol", 0.1), "shots": shots, "caps": caps, "sfx": sfx, "pops": pops, "shakes": shakes, "infos": infos, "chars": chars}
json.dump(data, open(os.path.join(PUB, "data.json"), "w"), ensure_ascii=False, indent=1)
avg = total / FPS / len(shots)
print(f"{SLUG}: {total / FPS:.1f}s · 컷 {len(shots)}개(평균 {avg:.2f}s) · 자막 {len(caps)} · 효과음 {len(sfx)} · 팝 {len(pops)} · 인포 {len(infos)} · 캐릭터 {len(chars)}")

if "--render" in sys.argv:
    out = os.path.join(WK, f"{SLUG}_v2.mp4")
    subprocess.run(["npx", "remotion", "render", "Ranbbang", out, f"--props={json.dumps({'slug': SLUG})}",
                    "--concurrency=4", "--timeout=90000", "--log=error"], cwd=RM, check=True)   # 폰트 delayRender 28초 초과로 가끔 실패 → 동시 4·제한 90초
    # 음량을 쇼츠 기준(-15 LUFS)으로 — Remotion 믹스는 -20 안팎으로 작게 나온다
    tmp = out + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", out, "-c:v", "copy", "-af",
                    "loudnorm=I=-15:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", tmp], check=True)
    os.replace(tmp, out)
    print("✓", out)
