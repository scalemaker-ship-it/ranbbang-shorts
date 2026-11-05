#!/usr/bin/env python3
"""란빵 블박 사연형(몇대몇 블랙박스 채널 스타일, 2026-10-30) — 사건 하나를 실시간으로 따라가며 해요체로 설명.

  python3 ranbbang/_ep_story.py <slug>
입력: ranbbang/work/<slug>/story.json
  title:[흰 줄, 초록 줄], credit, src, crop(w:h:x:y), cuts:[[a,b],...](원본 초, 이어붙일 구간),
  lines:[{src: 원본초, text}], outro:{a, b, slow, lines:[...]},
  marks:[{type: circle|arrow|text, a, b(원본초), ...좌표는 crop 기준}],
  blur:[{a, b, keys:[[원본초, x, y, w, h], ...]}]  (crop 기준, 사이는 선형 보간)
화면: 베이지 배경 / 상단 2줄 제목(흰+초록) / 가운데 블박 / 영상 아래쪽 검은 박스 자막 / 아래 출처.
오디오: 원본 음성 안 씀. 태섭 나레이션(_ep_dashcam 과 같은 TTS 캐시) + BGM 덕킹.
산출: ranbbang/work/<slug>/output.mp4
"""
import glob, hashlib, json, os, random, re, subprocess, sys, time, urllib.request
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SHORTS = os.path.dirname(HERE)
FONTS = os.path.expanduser("~/Library/Fonts")
F_TITLE = os.path.join(FONTS, "BMJUA_ttf.ttf")
F_SUB = os.path.join(FONTS, "Pretendard-SemiBold.otf")
F_HAND = os.path.join(FONTS, "BMKIRANGHAERANG-TTF.ttf")
F_CREDIT = os.path.join(FONTS, "Pretendard-Medium.otf")
BGM = os.path.expanduser("~/Desktop/kim/ssul/assets/bgm/sneaky-123.mp3")
VOICE, TEMPO = "tc_62f223abb9d09c5b3131c7f2", 1.25   # 태섭
W, H, FPS = 1080, 1920, 30
BEIGE = (214, 205, 188)
VID_Y = 480
SUB_CY = 1385            # 자막 박스 중심 y (영상 아래쪽 안)
CREDIT_Y = 1600         # 레퍼런스: 영상 480~1470, 출처 1600

SLUG = sys.argv[1]
B = os.path.join(HERE, "work", SLUG)
WK = os.path.join(B, "build_story")
SP = json.load(open(os.path.join(B, "story.json"), encoding="utf-8"))
CW, CH, CX, CY = map(int, SP["crop"].split(":"))
SCALE = W / CW
VID_H = int(CH * SCALE)


def sh(*a):
    subprocess.run(a, check=True)


def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).decode())


def plain(s):
    return s.replace("*", "")


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


def chunks(text, n=15):
    """쉼표·마침표에서 끊고, 긴 조각은 어절 단위로 고르게 나눈다(*강조* 유지)."""
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
            sc = max(ln(x) for x in parts)
            if best is None or sc < best[0]:
                best = (sc, parts)
        out += [" ".join(x) for x in best[1]]
    fixed, open_ = [], False
    for c in out:
        c2 = ("*" if open_ else "") + c
        open_ = c2.count("*") % 2 == 1
        if open_:
            c2 += "*"
        fixed.append(c2.replace("**", "").rstrip(",."))
    return fixed


# ── 정적 레이어 ────────────────────────────────────────────────────
def paper_bg():
    random.seed(7)
    im = Image.new("RGB", (W, H), BEIGE)
    noise = Image.effect_noise((W, H), 18).convert("L")
    tex = Image.merge("RGB", [noise] * 3)
    im = Image.blend(im, Image.composite(tex, im, Image.new("L", (W, H), 40)), 0.25)
    return im


def stroke_text(d, xy, text, font, fill, sw, anchor="mm"):
    d.text(xy, text, font=font, fill=fill, stroke_width=sw, stroke_fill=(0, 0, 0), anchor=anchor)


def static_layer():
    im = paper_bg()
    d = ImageDraw.Draw(im)
    for i, (txt, col) in enumerate(zip(SP["title"], [(255, 255, 255), (64, 222, 64)])):
        size = 92
        f = ImageFont.truetype(F_TITLE, size)
        while d.textlength(txt, font=f) > W - 120:
            size -= 4
            f = ImageFont.truetype(F_TITLE, size)
        stroke_text(d, (W // 2, 300 + i * 104), txt, f, col, 9)
    fc = ImageFont.truetype(F_CREDIT, 34)
    d.text((W // 2, CREDIT_Y), SP["credit"], font=fc, fill=(246, 242, 232), anchor="mm")
    return im


def sub_png(text):
    """검은 반투명 박스 + 흰 글씨(*강조*는 노랑)."""
    f = ImageFont.truetype(F_SUB, 46)
    segs, on = [], False
    for part in text.split("*"):
        if part:
            segs.append((part, (255, 220, 40) if on else (255, 255, 255)))
        on = not on
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    tw = sum(tmp.textlength(t, font=f) for t, _ in segs)
    pw, ph = int(tw + 48), 76
    im = Image.new("RGBA", (pw, ph), (0, 0, 0, 185))
    d = ImageDraw.Draw(im)
    x = 24
    for t, c in segs:
        d.text((x, ph // 2 + 2), t, font=f, fill=c, anchor="lm")
        x += d.textlength(t, font=f)
    return im


def hand_png(text, size=96, color=(255, 226, 40)):
    f = ImageFont.truetype(F_HAND, size)
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    b = tmp.textbbox((0, 0), text, font=f, stroke_width=8)
    im = Image.new("RGBA", (b[2] - b[0] + 20, b[3] - b[1] + 20), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10 - b[0], 10 - b[1]), text, font=f, fill=color, stroke_width=8,
                            stroke_fill=(0, 0, 0))
    return im


def to_out(x, y):
    return x * SCALE, VID_Y + y * SCALE


def draw_mark(d, m):
    red = (235, 30, 30)
    if m["type"] == "circle":
        cx, cy = to_out(m["x"], m["y"])
        rx, ry = m["rx"] * SCALE, m["ry"] * SCALE
        d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], outline=red, width=9)
    elif m["type"] == "arrow":
        x0, y0 = to_out(*m["from"])
        x1, y1 = to_out(*m["to"])
        d.line([x0, y0, x1, y1], fill=red, width=16)
        import math
        ang = math.atan2(y1 - y0, x1 - x0)
        L = 52
        p1 = (x1 + L * math.cos(ang + 2.6), y1 + L * math.sin(ang + 2.6))
        p2 = (x1 + L * math.cos(ang - 2.6), y1 + L * math.sin(ang - 2.6))
        d.polygon([(x1 + 10 * math.cos(ang), y1 + 10 * math.sin(ang)), p1, p2], fill=red)


def blur_box(t):
    """원본 시각 t 에서 가릴 박스들(crop 기준)."""
    out = []
    for bl in SP.get("blur", []):
        if not (bl["a"] <= t <= bl["b"]):
            continue
        ks = bl["keys"]
        if t <= ks[0][0]:
            out.append(ks[0][1:])
            continue
        if t >= ks[-1][0]:
            out.append(ks[-1][1:])
            continue
        for k0, k1 in zip(ks, ks[1:]):
            if k0[0] <= t <= k1[0]:
                r = (t - k0[0]) / (k1[0] - k0[0])
                out.append([k0[i] + (k1[i] - k0[i]) * r for i in range(1, 5)])
                break
    return out


# ── 메인 ─────────────────────────────────────────────────────────
def main():
    os.makedirs(WK, exist_ok=True)
    fr = os.path.join(WK, "frames")
    os.makedirs(fr, exist_ok=True)
    src = os.path.join(B, "sources", SP["src"])
    a_all = min(c[0] for c in SP["cuts"] + [[SP["outro"]["a"]]])
    b_all = max(c[1] for c in SP["cuts"] + [[0, SP["outro"]["b"]]])
    if not glob.glob(os.path.join(fr, "*.jpg")):
        sh("ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a_all}", "-to", f"{b_all}", "-i", src,
           "-vf", f"fps={FPS},crop={SP['crop']}", "-q:v", "2", os.path.join(fr, "%05d.jpg"))
    nfr = len(glob.glob(os.path.join(fr, "*.jpg")))
    src_frame = lambda t: min(nfr, max(1, int(round((t - a_all) * FPS)) + 1))

    # 출력 프레임 → 원본 시각
    times = []
    for a, b in SP["cuts"]:
        n = int(round((b - a) * FPS))
        times += [a + i / FPS for i in range(n)]
    main_len = len(times) / FPS
    o = SP["outro"]

    # 오디오 배치
    audio, subs, T = [], [], 0.0
    t_of = lambda s: next(i for i, t in enumerate(times) if t >= s) / FPS   # 원본초 → 출력초

    def place(text, start):
        w = tts(text)
        d = dur(w)
        audio.append((w, start, 1.0))
        cs = chunks(text)
        L = sum(len(plain(x)) for x in cs)
        s = start
        for i, x in enumerate(cs):
            e = s + d * len(plain(x)) / L
            subs.append((x, s, e + (0.1 if i == len(cs) - 1 else 0)))
            s = e
        return start + d

    end = 0.0
    for ln in SP["lines"]:
        st = max(t_of(ln["src"]), end + 0.15)
        end = place(ln["text"], st)
    for sfx in SP.get("sfx", []):
        audio.append((os.path.join(WK, f"sfx_{sfx['name']}.wav"), t_of(sfx["src"]), sfx.get("vol", 1.0)))
    t_out = max(main_len, end + 0.2)
    o_start = t_out
    s = o_start + 0.2
    for ln in o["lines"]:
        s = place(ln, s) + 0.2
    total = s + 0.4
    # 아웃트로 프레임: 사고 장면 슬로우 → 마지막 프레임 정지. 본편이 나레이션보다 짧으면 본편 끝 프레임 정지
    times += [times[-1]] * int(round((o_start - main_len) * FPS))
    k = 0
    while len(times) < int(total * FPS):
        t = o["a"] + k / FPS * o["slow"]
        times.append(min(t, o["b"]))
        k += 1

    # 효과음 합성
    sh("ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anoisesrc=d=0.9:c=white:a=0.8:r=44100",
       "-af", "bandpass=f=2600:width_type=h:w=900,tremolo=f=38:d=0.6,afade=t=in:d=0.04,"
       "afade=t=out:st=0.45:d=0.45,volume=2.2,alimiter=limit=0.95", os.path.join(WK, "sfx_screech.wav"))
    sh("ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anoisesrc=d=0.35:c=pink:a=0.6:r=44100",
       "-af", "highpass=f=700,lowpass=f=5000,afade=t=in:d=0.15,afade=t=out:st=0.15:d=0.2,volume=0.7",
       os.path.join(WK, "sfx_whoosh.wav"))

    # 오디오 믹스
    ins, fc = [], []
    for i, (w, st, v) in enumerate(audio):
        ins += ["-i", w]
        ms = int(st * 1000)
        fc.append(f"[{i}]aformat=sample_rates=44100:channel_layouts=mono,volume={v},adelay={ms}|{ms}[a{i}]")
    fc.append("".join(f"[a{i}]" for i in range(len(audio))) +
              f"amix=inputs={len(audio)}:normalize=0,apad,atrim=0:{total:.3f}[fx]")
    ins += ["-stream_loop", "-1", "-i", BGM]
    nb = len(audio)
    fc.append(f"[{nb}:a]aformat=sample_rates=44100:channel_layouts=mono,volume=0.18,atrim=0:{total:.3f},"
              f"afade=t=out:st={total - 1.2:.3f}:d=1.2[bg]")
    fc.append("[fx]asplit[fx1][fx2]")
    fc.append("[bg][fx1]sidechaincompress=threshold=0.05:ratio=6:attack=20:release=300[duck]")
    fc.append("[duck][fx2]amix=inputs=2:normalize=0,alimiter=limit=0.95[aout]")
    mix = os.path.join(WK, "mix.wav")
    sh("ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fc), "-map", "[aout]", mix)

    # 영상 합성(프레임 단위)
    base = static_layer()
    # 레퍼런스처럼 자막이 비지 않게: 다음 자막 직전까지(최대 2.5초) 직전 자막 유지
    subs = [(x, s0, min(subs[i + 1][1], e0 + 2.5) if i + 1 < len(subs) else total)
            for i, (x, s0, e0) in enumerate(subs)]
    sub_imgs = [(sub_png(x), s0, e0) for x, s0, e0 in subs]
    marks = SP.get("marks", [])
    hand = {i: hand_png(m["text"], m.get("size", 96)) for i, m in enumerate(marks) if m["type"] == "text"}
    out = os.path.join(B, "output.mp4")
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", mix,
                          "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                          "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out],
                         stdin=subprocess.PIPE)
    cache = {}
    in_outro_from = int(round(o_start * FPS))
    for i, t in enumerate(times):
        ot = i / FPS
        idx = src_frame(t)
        if idx not in cache:
            cache.clear()
            v = Image.open(os.path.join(fr, f"{idx:05d}.jpg")).convert("RGB")
            for x, y, w, h in blur_box(t):
                box = tuple(int(q) for q in (x, y, x + w, y + h))
                v.paste(v.crop(box).filter(ImageFilter.GaussianBlur(9)), box[:2])
            cache[idx] = v.resize((W, VID_H), Image.LANCZOS)
        fimg = base.copy()
        fimg.paste(cache[idx], (0, VID_Y))
        d = ImageDraw.Draw(fimg)
        if i < in_outro_from:
            for k, m in enumerate(marks):
                if m["a"] <= t <= m["b"]:
                    if m["type"] == "text":
                        im = hand[k]
                        cx, cy = to_out(m["x"], m["y"])
                        fimg.paste(im, (int(cx - im.width / 2), int(cy - im.height / 2)), im)
                    else:
                        draw_mark(d, m)
        for im, s0, e0 in sub_imgs:
            if s0 <= ot < e0:
                fimg.paste(im, ((W - im.width) // 2, SUB_CY - im.height // 2), im)
                break
        p.stdin.write(fimg.tobytes())
    p.stdin.close()
    p.wait()
    d = dur(out)
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", out, "-vf", "fps=1,scale=216:-1,tile=10x4",
       "-frames:v", "1", os.path.join(B, "story_sheet.jpg"))
    json.dump({"subs": subs, "total": total}, open(os.path.join(B, "story_build.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"[done] {d:.1f}s → {out}")


if __name__ == "__main__":
    main()
