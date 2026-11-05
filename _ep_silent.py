#!/usr/bin/env python3
"""란빵 블박 무나레이션형(2026-10-30, bigleft) — 블박 원본 + 상황 자막 + 효과음 + 슬로우 리플레이 + 투표 카드.

  python3 ranbbang/_ep_silent.py <slug>
입력: ranbbang/work/<slug>/story.json
  title:[흰 줄, 초록 줄], credit, src, crop(w:h:x:y), main:[a,b](원본초),
  subs:[{a,b,text}](원본초, *강조* 노랑), hand:[{a,b,text,x,y(crop 기준),size,color}],
  shake:[원본초], sfx:[{name: horn|screech|crash, at(원본초), vol}],
  replay:{a,b,slow,sub,impact}, end:{dur,lines:[흰 줄, 노랑 줄]}, bgm_vol
화면: 검은 배경, 2줄 제목·자막·의성어 모두 잘난고딕(자간 -2%, 흰 + 노랑 #FDF652, 2026-10-30 사용자 지정), 출처 1줄.
오디오: 나레이션 없음. 원본 소리 그대로(리플레이는 0.5배 늘림) + BGM 작게. sfx 는 비우면 합성음 안 넣음.
산출: ranbbang/work/<slug>/output.mp4
"""
import glob, json, os, random, subprocess, sys
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.expanduser("~/Library/Fonts")
F_TITLE = F_SUB = F_HAND = os.path.join(FONTS, "JalnanGothicTTF.ttf")
WHITE, YELLOW = (255, 255, 255), (253, 246, 82)
TRACK = -0.02          # 자간(글자 크기 대비)
F_CREDIT = os.path.join(FONTS, "Pretendard-Medium.otf")
BGM = os.path.expanduser("~/Desktop/kim/ssul/assets/bgm/sneaky-123.mp3")
SFX_IC = os.path.expanduser("~/Desktop/kim/ssul/assets/sfx/ic/boom_zoom_impact.wav")
W, H, FPS = 1080, 1920, 30
VID_Y = 600
CREDIT_Y = 1600

SLUG = sys.argv[1]
B = os.path.join(HERE, "work", SLUG)
WK = os.path.join(B, "build_silent")
SP = json.load(open(os.path.join(B, "story.json"), encoding="utf-8"))
CW, CH, CX, CY = map(int, SP["crop"].split(":"))
SCALE = W / CW
VID_H = int(CH * SCALE)
SUB_CY = VID_Y + VID_H + 90


def sh(*a):
    subprocess.run(a, check=True)


def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).decode())


def tlen(text, f):
    d = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    return sum(d.textlength(c, font=f) for c in text) + TRACK * f.size * (len(text) - 1)


def draw_tracked(d, xy, segs, f, stroke=0, anchor="mm"):
    """segs=[(text, color)]. 자간 적용해 글자 단위로 찍는다. anchor 는 mm(가운데) 또는 lm."""
    total = sum(tlen(t, f) for t, _ in segs) + TRACK * f.size * (len(segs) - 1)
    x = xy[0] - (total / 2 if anchor == "mm" else 0)
    for t, c in segs:
        for ch in t:
            d.text((x, xy[1]), ch, font=f, fill=c, stroke_width=stroke, stroke_fill=(0, 0, 0), anchor="lm")
            x += d.textlength(ch, font=f) + TRACK * f.size


def fit_font(path, size, text, maxw):
    f = ImageFont.truetype(path, size)
    while tlen(text, f) > maxw:
        size -= 4
        f = ImageFont.truetype(path, size)
    return f


def split_emph(text, base=WHITE):
    segs, on = [], False
    for part in text.split("*"):
        if part:
            segs.append((part, YELLOW if on else base))
        on = not on
    return segs


def static_layer():
    im = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(im)
    for i, (txt, col) in enumerate(zip(SP["title"], [WHITE, YELLOW])):
        f = fit_font(F_TITLE, 112, txt, W - 120)
        draw_tracked(d, (W // 2, 380 + i * 128), [(txt, col)], f)
    d.text((W // 2, CREDIT_Y), SP["credit"], font=ImageFont.truetype(F_CREDIT, 32),
           fill=(150, 150, 150), anchor="mm")
    return im


def sub_png(text, size=72):
    f = fit_font(F_SUB, size, text.replace("*", ""), W - 160)
    im = Image.new("RGBA", (W, int(size * 1.6)), (0, 0, 0, 0))
    draw_tracked(ImageDraw.Draw(im), (W // 2, im.height // 2), split_emph(text), f)
    return im


def hand_png(text, size=96, color=YELLOW):
    f = ImageFont.truetype(F_HAND, size)
    w = int(tlen(text, f) + 40)
    im = Image.new("RGBA", (w, int(size * 1.5)), (0, 0, 0, 0))
    draw_tracked(ImageDraw.Draw(im), (w // 2, im.height // 2), [(text, tuple(color))], f, stroke=9)
    return im


def end_png(lines):
    """투표 카드: 영상 영역 위 검은 반투명 판 + 흰/노랑 2줄(줄간격 좁게)."""
    im = Image.new("RGBA", (W, VID_H), (0, 0, 0, 170))
    d = ImageDraw.Draw(im)
    f = fit_font(F_TITLE, 124, max(lines, key=len), W - 160)
    gap = int(f.size * 1.05)
    for i, (txt, col) in enumerate(zip(lines, [WHITE, YELLOW])):
        draw_tracked(d, (W // 2, VID_H / 2 + (i - 0.5) * gap), [(txt, col)], f)
    return im


def make_sfx():
    out = {}
    p = os.path.join(WK, "sfx_horn.wav")     # 승용차 경적: 두 음 + 약간 거친 배음
    sh("ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "sine=f=415:d=1.1", "-f", "lavfi",
       "-i", "sine=f=500:d=1.1", "-filter_complex",
       "[0][1]amix=inputs=2,asetrate=44100,aformat=sample_rates=44100,"
       "acrusher=bits=6:mode=log:aa=1,lowpass=f=2400,afade=t=in:d=0.02,afade=t=out:st=0.95:d=0.15,volume=2.0",
       "-ac", "1", p)
    out["horn"] = p
    p = os.path.join(WK, "sfx_screech.wav")
    sh("ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anoisesrc=d=0.9:c=white:a=0.8:r=44100",
       "-af", "bandpass=f=2600:width_type=h:w=900,tremolo=f=38:d=0.6,afade=t=in:d=0.04,"
       "afade=t=out:st=0.45:d=0.45,volume=2.2,alimiter=limit=0.95", p)
    out["screech"] = p
    p = os.path.join(WK, "sfx_crash.wav")    # 저음 임팩트 + 금속 찌그러짐 노이즈
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", SFX_IC, "-f", "lavfi", "-i",
       "anoisesrc=d=0.5:c=brown:a=0.9:r=44100", "-filter_complex",
       "[0]aformat=sample_rates=44100:channel_layouts=mono[a];"
       "[1]highpass=f=300,lowpass=f=4500,afade=t=out:st=0.08:d=0.4,volume=1.6[b];"
       "[a][b]amix=inputs=2:normalize=0,alimiter=limit=0.95", "-ac", "1", p)
    out["crash"] = p
    return out


def main():
    os.makedirs(WK, exist_ok=True)
    fr = os.path.join(WK, "frames")
    os.makedirs(fr, exist_ok=True)
    src = os.path.join(B, "sources", SP["src"])
    a0, a1 = SP["main"]
    if not glob.glob(os.path.join(fr, "*.jpg")):
        sh("ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a0}", "-to", f"{a1}", "-i", src,
           "-vf", f"fps={FPS},crop={SP['crop']}", "-q:v", "2", os.path.join(fr, "%05d.jpg"))
    nfr = len(glob.glob(os.path.join(fr, "*.jpg")))
    src_frame = lambda t: min(nfr, max(1, int(round((t - a0) * FPS)) + 1))

    # 출력 프레임 → (원본초, 구간). 본편 → 슬로우 리플레이 → 투표 카드(마지막 프레임 정지)
    times = [(a0 + i / FPS, "main") for i in range(int(round((a1 - a0) * FPS)))]
    rp = SP["replay"]
    rp_start = len(times) / FPS
    k = 0
    while rp["a"] + k / FPS * rp["slow"] <= rp["b"]:
        times.append((rp["a"] + k / FPS * rp["slow"], "replay"))
        k += 1
    end_start = len(times) / FPS
    times += [(rp["b"], "end")] * int(round(SP["end"]["dur"] * FPS))
    total = len(times) / FPS
    rp_out = lambda t: rp_start + (t - rp["a"]) / rp["slow"]   # 리플레이 원본초 → 출력초

    # 오디오: 원본 소리(본편 그대로 + 리플레이 구간 0.5배 늘림) + 합성 효과음(있으면) + BGM 작게
    ins = ["-ss", f"{a0}", "-to", f"{a1}", "-i", src,
           "-ss", f"{rp['a']}", "-to", f"{rp['b']}", "-i", src]
    fc = ["[0:a]aformat=sample_rates=44100:channel_layouts=mono[o0]",
          f"[1:a]aformat=sample_rates=44100:channel_layouts=mono,atempo={rp['slow']},"
          f"adelay={int(rp_start * 1000)}|{int(rp_start * 1000)}[o1]"]
    srcs = ["[o0]", "[o1]"]
    sfx = make_sfx() if SP.get("sfx") else {}
    for i, s in enumerate(SP.get("sfx", [])):
        ins += ["-i", sfx[s["name"]]]
        ms = int((s["at"] - a0) * 1000)
        fc.append(f"[{i + 2}:a]aformat=sample_rates=44100:channel_layouts=mono,volume={s.get('vol', 1.0)},"
                  f"adelay={ms}|{ms}[s{i}]")
        srcs.append(f"[s{i}]")
    fc.append("".join(srcs) + f"amix=inputs={len(srcs)}:normalize=0,apad,atrim=0:{total:.3f}[fx]")
    nb = 2 + len(SP.get("sfx", []))
    ins += ["-stream_loop", "-1", "-i", BGM]
    fc.append(f"[{nb}:a]aformat=sample_rates=44100:channel_layouts=mono,volume={SP.get('bgm_vol', 0.07)},"
              f"atrim=0:{total:.3f},afade=t=out:st={total - 1.2:.3f}:d=1.2[bg]")
    fc.append("[bg][fx]amix=inputs=2:normalize=0,alimiter=limit=0.95[aout]")
    mix = os.path.join(WK, "mix.wav")
    sh("ffmpeg", "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fc), "-map", "[aout]", mix)

    # 자막(출력초 기준)
    subs = [(s["text"], s["a"] - a0, s["b"] - a0) for s in SP["subs"]]
    subs.append((rp["sub"], rp_start, end_start))
    sub_imgs = [(sub_png(x), s0, e0) for x, s0, e0 in subs]
    hands = [(hand_png(h["text"], h.get("size", 96), h.get("color", YELLOW)), h) for h in SP["hand"]]
    shakes = [s - a0 for s in SP.get("shake", [])] + [rp_out(rp["impact"])]
    endcard = end_png(SP["end"]["lines"])

    base = static_layer()
    out = os.path.join(B, "output.mp4")
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", mix,
                          "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
                          "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out],
                         stdin=subprocess.PIPE)
    cache = {}
    rnd = random.Random(3)
    for i, (t, seg) in enumerate(times):
        ot = i / FPS
        idx = src_frame(t)
        if idx not in cache:
            cache.clear()
            v = Image.open(os.path.join(fr, f"{idx:05d}.jpg")).convert("RGB")
            cache[idx] = v.resize((W, VID_H), Image.LANCZOS)
        v = cache[idx]
        if seg == "end":
            v = ImageEnhance.Brightness(v).enhance(0.6)
        # 충돌 흔들림: 0.35초 동안 줄어드는 확대+이동
        dx = dy = 0
        for s in shakes:
            if 0 <= ot - s < 0.35:
                amp = 22 * (1 - (ot - s) / 0.35)
                dx, dy = rnd.uniform(-amp, amp), rnd.uniform(-amp, amp)
        if dx or dy:
            z = 1.06
            vz = v.resize((int(W * z), int(VID_H * z)))
            ox = int((vz.width - W) / 2 + dx)
            oy = int((vz.height - VID_H) / 2 + dy)
            v = vz.crop((ox, oy, ox + W, oy + VID_H))
        fimg = base.copy()
        fimg.paste(v, (0, VID_Y))
        if seg == "main":
            for im, h in hands:
                if h["a"] - a0 <= ot < h["b"] - a0:
                    cx, cy = h["x"] * SCALE, VID_Y + h["y"] * SCALE
                    fimg.paste(im, (int(cx - im.width / 2), int(cy - im.height / 2)), im)
        if seg == "end":
            fimg.paste(endcard, (0, VID_Y), endcard)
        else:
            for im, s0, e0 in sub_imgs:
                if s0 <= ot < e0:
                    fimg.paste(im, ((W - im.width) // 2, SUB_CY - im.height // 2), im)
                    break
        p.stdin.write(fimg.tobytes())
    p.stdin.close()
    p.wait()
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", out, "-vf", "fps=2,scale=216:-1,tile=8x5",
       "-frames:v", "1", os.path.join(B, "silent_sheet.jpg"))
    print(f"[done] {dur(out):.1f}s → {out}")


if __name__ == "__main__":
    main()
