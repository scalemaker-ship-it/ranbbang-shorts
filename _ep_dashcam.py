#!/usr/bin/env python3
"""란빵 해외 블랙박스 모음 — 범용 생성기 (2026-09-28, snowcrash 편 구조를 spec 으로 일반화).

  python3 ranbbang/_ep_dashcam.py <slug>
입력: ranbbang/work/<slug>/spec.json  {title:[줄1,줄2], outro_chip, clips:[{file,crop,impact,lo,hi,setup,after,origin}], outro:{file,crop,ss,slow,lines}}
구조: 클립마다 상황 설명 → (두둥) 결국?! → 사고 순간(쾅+흔들림+플래시+쾅!! 팝업) → 사고 설명, 아웃트로 = 교훈·법 근거·질문.
규칙: ranbbang/prd.md §4-3 (해외 영상만·편당 3개·지역명 금지·부크크고딕 자막·데드존 회피).
산출: ranbbang/work/<slug>/output.mp4  (TTS 는 문장 해시로 캐시 → 재실행 시 과금 없음)
"""
import hashlib, json, os, re, subprocess, sys, time, urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SHORTS = os.path.dirname(HERE)
FONT = os.path.join(SHORTS, "assets", "fonts", "Jalnan.ttf")
# 쇼츠 데드존: 하단 ~1500px 아래(채널명·설명)와 우측 x>940(좋아요·댓글 버튼 열)을 피한다
SUB_Y, SUB_SIZE, SUB_MAXW = 1330, 64, 780   # 자막 상단 y / 크기(80의 0.8배) / 최대 폭(x 150~930)
SUB_FONT = os.path.expanduser("~/Library/Fonts/BookkGothic_Bold.ttf")   # 하단 자막 = 부크크고딕(2026-09-28)
BGM = os.path.expanduser("~/Desktop/kim/ssul/assets/bgm/sneaky-123.mp3")   # calm-0831 은 삭제됨(2026-10-30), 란빵 v2 BGM
VOICE = "tc_62f223abb9d09c5b3131c7f2"   # 태섭
W, H = 1080, 1920
BOX_Y, BOX_H = 480, 810
POP_Y = 1400                 # 결국??!/쾅!! 팝업 중심 — 사고 장면을 가리지 않게 박스 아래(자막 자리)
TEMPO = 1.25
WHITE, YELLOW, RED = (255, 255, 255, 255), (255, 230, 0, 255), (255, 45, 45, 255)
SLUG = sys.argv[1]
B = os.path.join(HERE, "work", SLUG)
SRC = os.path.join(B, "sources")
WK = os.path.join(B, "build")
SPEC = json.load(open(os.path.join(B, "spec.json"), encoding="utf-8"))
TITLE = [[(SPEC["title"][0], WHITE)], [(SPEC["title"][1], YELLOW)]]
CLIPS = SPEC["clips"]      # file·crop·impact·lo·hi·setup·after(·origin)
OUTRO = SPEC["outro"]      # file·crop·ss·slow·lines
GYEOLGUK = "결국?!"


def sh(*a):
    subprocess.run(a, check=True)


def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
                                          "format=duration", "-of", "csv=p=0", p]).decode())


def plain(s):
    return s.replace("*", "")


# ── TTS (문장 해시 캐시) ─────────────────────────────────────────
_KEY = None


def tts(text):
    global _KEY
    text = plain(text)
    out = os.path.join(WK, "tts_" + hashlib.md5(f"{VOICE}{TEMPO}{text}".encode()).hexdigest()[:10] + ".wav")
    if os.path.exists(out):
        return out
    if _KEY is None:
        for ln in open(os.path.join(SHORTS, ".env"), encoding="utf-8"):
            if ln.startswith("TYPECAST_API_KEY="):
                _KEY = ln.split("=", 1)[1].strip().strip('"').strip("'")
    body = json.dumps({"voice_id": VOICE, "text": text, "model": "ssfm-v30",
                       "language": "kor", "emotion": "normal"}).encode()
    req = urllib.request.Request("https://api.typecast.ai/v1/text-to-speech", data=body,
                                 headers={"X-API-KEY": _KEY, "Content-Type": "application/json"})
    for a in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                open(out + ".raw.wav", "wb").write(r.read())
            break
        except Exception:
            if a == 2:
                raise
            time.sleep(2)
    f = ("silenceremove=start_periods=1:start_silence=0.02:start_threshold=-45dB,areverse,"
         "silenceremove=start_periods=1:start_silence=0.02:start_threshold=-45dB,areverse,"
         f"atempo={TEMPO},loudnorm=I=-16:TP=-1.5")
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", out + ".raw.wav", "-af", f, "-ar", "44100", "-ac", "1", out)
    os.remove(out + ".raw.wav")
    return out


# ── 효과음 합성 ───────────────────────────────────────────────────
def make_sfx():
    s = {}
    s["dudung"] = os.path.join(WK, "sfx_dudung.wav")   # 두-둥 (저음 히트 2번)
    h1 = "sin(2*PI*(70*t-30*t*t))*exp(-5*t)"
    h2 = "sin(2*PI*(55*(t-0.42)-30*(t-0.42)*(t-0.42)))*exp(-4*(t-0.42))"
    sh("ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
       f"aevalsrc=0.9*{h1}*lt(t\\,0.4)+1.0*{h2}*gte(t\\,0.42):s=44100:d=1.3".replace(",", "\\,")
       .replace("\\\\,", "\\,"),
       "-af", "volume=1.8", s["dudung"])
    s["crash"] = os.path.join(WK, "sfx_crash.wav")      # 쾅 (저음 쿵 + 노이즈 파열)
    sh("ffmpeg", "-y", "-loglevel", "error",
       "-f", "lavfi", "-i", "aevalsrc=sin(2*PI*(55*t-25*t*t))*exp(-6*t):s=44100:d=1.2",
       "-f", "lavfi", "-i", "anoisesrc=d=1.2:c=white:a=0.9:r=44100",
       "-filter_complex", "[1]lowpass=f=2500,afade=t=out:st=0.02:d=0.9[n];"
       "[0][n]amix=inputs=2:weights=1.4 0.9:normalize=0,alimiter=limit=0.95", s["crash"])
    s["screech"] = os.path.join(WK, "sfx_screech.wav")  # 끼익 (급정거, 안 박힌 아차사고용, spec 클립 "sfx": "screech")
    sh("ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anoisesrc=d=0.9:c=white:a=0.8:r=44100",
       "-af", "bandpass=f=2600:width_type=h:w=900,tremolo=f=38:d=0.6,afade=t=in:d=0.04,"
       "afade=t=out:st=0.45:d=0.45,volume=2.2,alimiter=limit=0.95", s["screech"])
    s["whoosh"] = os.path.join(WK, "sfx_whoosh.wav")    # 휙 (자막 팝)
    sh("ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anoisesrc=d=0.35:c=pink:a=0.6:r=44100",
       "-af", "highpass=f=700,lowpass=f=5000,afade=t=in:d=0.15,afade=t=out:st=0.15:d=0.2,volume=0.7",
       s["whoosh"])
    return s


# ── 텍스트 PNG ───────────────────────────────────────────────────
def parse_hl(text, base=WHITE, hl=YELLOW):
    segs, on = [], False
    for part in text.split("*"):
        if part:
            segs.append((part, hl if on else base))
        on = not on
    return segs


def text_png(lines, size, y, out, stroke=10, scale=1.0, cy=None, font_path=FONT, max_w=W - 70):
    """lines=[[(seg,color),...], ...] 중앙정렬, 자간 0(조각 단위 렌더). cy 주면 그 y를 중심으로."""
    size = int(size * scale)
    stroke = max(2, int(stroke * scale))
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shd = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d, sd = ImageDraw.Draw(img), ImageDraw.Draw(shd)
    font = ImageFont.truetype(font_path, size)
    width = lambda segs: sum(d.textlength(t, font=font) for t, _ in segs)
    widest = max(width(segs) for segs in lines)
    if widest > max_w:                      # 폭 넘으면 글자 크기 자동 축소
        size = int(size * max_w / widest)
        font = ImageFont.truetype(font_path, size)
    lh = int(size * 1.18)
    if cy is not None:
        y = cy - lh * len(lines) // 2
    for segs in lines:
        x = (W - width(segs)) / 2
        for t, c in segs:
            sd.text((x, y + 6), t, font=font, fill=(0, 0, 0, 170), stroke_width=stroke, stroke_fill=(0, 0, 0, 170))
            d.text((x, y), t, font=font, fill=c, stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
            x += d.textlength(t, font=font)
        y += lh
    Image.alpha_composite(shd.filter(ImageFilter.GaussianBlur(6)), img).save(out)


def chip_png(case, out):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f1 = ImageFont.truetype(FONT, 46)
    x0, y0 = 30, BOX_Y + 24
    if case:
        b = d.textbbox((0, 0), case, font=f1)
        d.rounded_rectangle([x0, y0, x0 + b[2] - b[0] + 36, y0 + 66], 12, fill=(255, 230, 0, 245))
        d.text((x0 + 18 - b[0], y0 + 33 - (b[1] + b[3]) / 2), case, font=f1, fill=(0, 0, 0, 255))
    img.save(out)


def chunks(text, n=13):
    """*강조* 유지. 쉼표·마침표로 끊고, 긴 조각은 어절 단위로 줄 길이가 가장 고르게 되도록 나눈다."""
    import itertools, math
    out = []
    for part in [p.strip() for p in re.split(r"(?<=[,.?!])\s+", text) if p.strip()]:
        words = part.split()
        ln = lambda ws: len(plain("".join(ws)))
        k = min(len(words), max(1, math.ceil(ln(words) / n)))
        best = None
        for cuts in itertools.combinations(range(1, len(words)), k - 1):
            idx = (0, *cuts, len(words))
            parts = [words[idx[i]:idx[i + 1]] for i in range(k)]
            score = max(ln(x) for x in parts)
            if best is None or score < best[0]:
                best = (score, parts)
        out += [" ".join(x) for x in best[1]]
    fixed, open_ = [], False            # 청크 경계에서 끊긴 *강조* 를 닫고 다시 연다
    for c in out:
        c2 = ("*" if open_ else "") + c
        if c2.count("*") % 2:
            c2 += "*"
            open_ = True
        else:
            open_ = False
        fixed.append(c2.replace("**", "").rstrip(",."))
    return fixed


# ── 메인 ─────────────────────────────────────────────────────────
def main():
    os.makedirs(WK, exist_ok=True)
    sfx = make_sfx()
    audio = []      # (wav, start, vol)
    ovl = []        # (png, start, end)
    subs = []       # (text, start, end)
    segs = []
    T = 0.0

    def seg_video(ci, c, ss, pre_freeze, seg_dur, impact_local):
        out = os.path.join(WK, f"seg{ci}.mp4")
        FG_W, FG_H = int(W * 1.08) // 2 * 2, int(BOX_H * 1.08) // 2 * 2
        shake, flash = "", ""
        if impact_local is not None:
            t0 = impact_local
            env = f"gte(t\\,{t0:.3f})*lte(t\\,{t0 + 0.9:.3f})*exp(-4*(t-{t0:.3f}))"
            shake = (f":x=(iw-ow)/2+34*sin(2*PI*17*t)*{env}"
                     f":y=(ih-oh)/2+26*cos(2*PI*23*t)*{env}")
            flash = f",eq=brightness=0.55*gte(t\\,{t0:.3f})*lte(t\\,{t0 + 0.12:.3f}):eval=frame"
        pad = f",tpad=start_duration={pre_freeze:.3f}:start_mode=clone" if pre_freeze > 0 else ""
        slow = f",setpts=PTS/{c['slow']}" if c.get("slow") else ""
        vf = (f"[0:v]crop={c['crop']}{slow},fps=30{pad},tpad=stop_duration=8:stop_mode=clone,"
              f"setpts=PTS-STARTPTS,split[a][b];"
              f"[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
              f"boxblur=30:2,eq=brightness=-0.3[bg];"
              f"[b]scale={FG_W}:{FG_H}:force_original_aspect_ratio=increase,crop={FG_W}:{FG_H},"
              f"crop={W}:{BOX_H}{shake}{flash}[fg];"
              f"[bg][fg]overlay=0:{BOX_Y},trim=0:{seg_dur:.3f},setpts=PTS-STARTPTS[v]")
        sh("ffmpeg", "-y", "-loglevel", "error", "-ss", f"{ss:.3f}", "-i", os.path.join(SRC, c["file"]),
           "-filter_complex", vf, "-map", "[v]", "-an", "-c:v", "libx264", "-preset", "fast",
           "-crf", "18", "-pix_fmt", "yuv420p", "-r", "30", out)
        segs.append(out)

    def add_line(text, start):
        w = tts(text)
        d = dur(w)
        audio.append((w, start, 1.0))
        cs = chunks(text)
        L = sum(len(plain(x)) for x in cs)
        s = start
        for i, x in enumerate(cs):
            e = s + d * len(plain(x)) / L
            subs.append((x, s, e + (0.08 if i == len(cs) - 1 else 0)))
            s = e
        return d

    for ci, c in enumerate(CLIPS):
        c["t0"] = T
        ls = dur(tts(c["setup"]))
        gasp, boom = c.get("gasp", GYEOLGUK), c.get("boom", "쾅!!")   # 감탄사·의성어(클립마다 다르게)
        gasp_tts = c.get("gasp_tts", gasp)   # 화면 글자와 읽는 소리를 따로(짧은 감탄사는 길게 읽힌다)
        lg = dur(tts(gasp_tts))
        la = dur(tts(c["after"]))
        # 로컬 타임라인: 설명 → 두둥+결국?! → 사고(쾅·흔들림) → 사고 설명
        t_setup = 0.15
        t_dudung = t_setup + ls + 0.1
        impact_local = t_dudung + max(lg, 1.0) + 0.1
        t_after = impact_local + 0.6
        seg_dur = t_after + la + 0.45
        ss = c["impact"] - impact_local
        pre_freeze = max(0.0, c["lo"] - ss)
        ss = max(ss, c["lo"])
        c["ss"], c["dur"] = round(ss, 2), round(seg_dur, 2)
        seg_video(ci, c, ss, pre_freeze, seg_dur, impact_local)

        add_line(c["setup"], T + t_setup)
        audio.append((sfx["dudung"], T + t_dudung, 0.9))
        audio.append((tts(gasp_tts), T + t_dudung + 0.05, 1.0))
        for k, sc in enumerate((1.35, 1.12, 1.0)):          # 결국??! 팝업
            p = os.path.join(WK, f"gg{ci}_{k}.png")
            text_png([[(gasp, YELLOW)]], 170, 0, p, stroke=14, scale=sc, cy=POP_Y)
            s0 = T + t_dudung + k * 0.06
            ovl.append((p, s0, s0 + 0.06 if k < 2 else T + impact_local))
        audio.append((sfx[c.get("sfx", "crash")], T + impact_local, 1.0))
        for k, sc in enumerate((1.5, 1.2, 1.0)):            # 쾅!! 팝업
            p = os.path.join(WK, f"kw{ci}_{k}.png")
            text_png([[(boom, RED)]], 220, 0, p, stroke=16, scale=sc, cy=POP_Y)
            s0 = T + impact_local + k * 0.05
            ovl.append((p, s0, s0 + 0.05 if k < 2 else T + impact_local + 0.58))
        add_line(c["after"], T + t_after)
        p = os.path.join(WK, f"chip{ci}.png")
        chip_png(f"CASE {ci + 1}", p)
        ovl.append((p, T, T + seg_dur))
        audio.append((sfx["whoosh"], T, 0.8))
        T += seg_dur

    # 아웃트로: 교훈 + 법 근거 + 질문
    o = OUTRO
    t_local, starts = 0.2, []
    for ln in o["lines"]:
        starts.append(t_local)
        t_local += dur(tts(ln)) + 0.2
    o_dur = t_local + 0.5
    seg_video(len(CLIPS), o, o["ss"], 0, o_dur, None)
    for ln, s in zip(o["lines"], starts):
        add_line(ln, T + s)
    p = os.path.join(WK, "chip_outro.png")
    chip_png(SPEC.get("outro_chip", "안전수칙"), p)
    ovl.append((p, T, T + o_dur))
    audio.append((sfx["whoosh"], T, 0.8))
    T += o_dur
    total = T

    lst = os.path.join(WK, "segs.txt")
    open(lst, "w").write("".join(f"file '{s}'\n" for s in segs))
    base = os.path.join(WK, "base.mp4")
    sh("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base)

    tp = os.path.join(WK, "title.png")
    text_png(TITLE, 104, 170, tp, stroke=12)
    ovl.insert(0, (tp, 0, total))
    for i, (x, s, e) in enumerate(subs):
        p = os.path.join(WK, f"sub{i}.png")
        text_png([parse_hl(x)], SUB_SIZE, SUB_Y, p, stroke=7, font_path=SUB_FONT, max_w=SUB_MAXW)
        ovl.append((p, s, e))

    # 오디오: 나레이션·효과음 배치 → BGM 덕킹
    ins, fc = [], []
    for i, (w, s, v) in enumerate(audio):
        ins += ["-i", w]
        ms = int(s * 1000)
        fc.append(f"[{i}]aformat=sample_rates=44100:channel_layouts=mono,volume={v},adelay={ms}|{ms}[a{i}]")
    fc.append("".join(f"[a{i}]" for i in range(len(audio))) +
              f"amix=inputs={len(audio)}:normalize=0,apad,atrim=0:{total:.3f}[fx]")
    ins += ["-stream_loop", "-1", "-i", BGM]
    nb = len(audio)
    fc.append(f"[{nb}:a]aformat=sample_rates=44100:channel_layouts=mono,volume=0.2,atrim=0:{total:.3f},"
              f"afade=t=out:st={total - 1.2:.3f}:d=1.2[bg]")
    fc.append("[fx]asplit[fx1][fx2]")
    fc.append("[bg][fx1]sidechaincompress=threshold=0.05:ratio=6:attack=20:release=300[duck]")
    fc.append("[duck][fx2]amix=inputs=2:normalize=0,alimiter=limit=0.95[aout]")
    mix = os.path.join(WK, "mix.wav")
    sh("ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fc), "-map", "[aout]", mix)

    ins, fc, prev = ["-i", base], [], "0:v"
    for i, (p, s, e) in enumerate(ovl, 1):
        ins += ["-i", p]
        fc.append(f"[{prev}][{i}:v]overlay=0:0:enable='between(t,{s:.3f},{e:.3f})'[v{i}]")
        prev = f"v{i}"
    ins += ["-i", mix]
    out = os.path.join(B, "output.mp4")
    sh("ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fc),
       "-map", f"[{prev}]", "-map", f"{len(ovl) + 1}:a", "-c:v", "libx264", "-preset", "medium",
       "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
       "-t", f"{total:.3f}", "-movflags", "+faststart", out)
    json.dump({"clips": [{k: c.get(k) for k in ("file", "origin", "impact", "ss", "t0", "dur")}
                         for c in CLIPS], "subs": subs},
              open(os.path.join(B, "build.json"), "w"), ensure_ascii=False, indent=2)
    d = dur(out)
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", out, "-vf", f"fps=12/{d},scale=270:-1,tile=6x2",
       "-frames:v", "1", os.path.join(B, "preview_sheet.png"))
    print(f"[done] {d:.1f}s → {out}")
    for c in CLIPS:
        print(f"  {c['file']:28s} t0={c['t0']:.1f} dur={c['dur']:.1f} ss={c['ss']:.1f}")


if __name__ == "__main__":
    main()
