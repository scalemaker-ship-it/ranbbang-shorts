#!/usr/bin/env python3
"""테슬라 날아다니는 로드스터 밈 모음 (나레이션 없음, 짤멍짤 jYoqaxhAZoY 레이아웃).

검정 배경 + 상단 2줄 타이틀(잘난체, 빨강/노랑) + 가운데 클립(1080x1033) + 하단 출처, 설명 1줄.
- 클립마다 3~4초가 되도록 배속(빨리감기), 소리는 각 원본 소리를 같은 배속(atempo, 음높이 유지)으로.
- 배경음 없음. 클립 소리는 -16 LUFS 로 맞추고 앞뒤 30ms 페이드로 끊김 소리 방지.
소스: shorts/work/teslameme/sources(틱톡, tikwm) + threads(스레드, 브라우저로 받은 원본)
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "..", "work", "teslameme")
OUT = os.path.join(ROOT, "work", "teslameme")
F_TITLE = os.path.expanduser("~/Library/Fonts/JalnanGothic.otf")  # 란빵 타이틀 폰트
F_CAP = os.path.expanduser("~/Library/Fonts/BookkGothic_Bold.ttf")  # 하단 설명(란빵 자막 폰트)
F_REACT = os.path.expanduser("~/Library/Fonts/온글잎 박다현체.ttf")  # 영상 속 반응 글씨
F_MED = os.path.expanduser("~/Library/Fonts/Pretendard-Medium.ttf")
EMOJI = "/System/Library/Fonts/Apple Color Emoji.ttc"

W, H, FPS = 1080, 1920, 30
# 레퍼런스 화면 비율(862x1512 캡처 → 1080x1920 환산)
TITLE_Y = (230, 351)  # 줄 간격 121px = 기존 란빵(layout.py TITLE_MID-TITLE_TOP)
BOX_Y, BOX_H = 476, 1033
HANDLE_Y, CAP_Y, CAP_MAXW = 1532, 1590, 900
TARGET = 3.6  # 클립당 화면 길이(초)
REALTIME = set()  # 이 번호의 클립은 빨리감기 없이 1배속(화면 길이 = 끝-시작)
TITLE = [("테슬라 로드스터", (237, 28, 36)), ("출시 후 근황", (255, 222, 0))]
# 전체 사운드: 이 소리로 클립 소리를 대체(None 이면 클립 원본 소리).
# 곡이 짧으면 MUSIC_JUMP(A, B): A초까지 틀고 B초로 되돌아가 곡 끝까지 → 인트로 재시작 없이 끝까지 이어짐.
# A-B 는 마디(4박) 배수여야 박자가 안 어긋난다. 남는 길이 차이는 atempo 로 미세 조정.
MUSIC = "bgm/oridalda.m4a"  # 체리필터 오리날다 (공식 채널 sgnjnNI5ktQ, 245초)
MUSIC_SS = 58.62  # 후렴 "날아올라" 시작점(whisper medium 단어 위치 58.76 + 보컬 음량 상승 58.70 기준)
MUSIC_LUFS = -16  # 배경음 크기. 클립 원본 소리를 주로 들려줄 땐 낮춘다
MUSIC_JUMP = None  # 곡이 짧을 때만: (A, B) 129.2BPM 예) p4cK89SC_AU (16.165, 3.162)

# (소스, 시작, 끝, 출처, 설명, 이모지, 원본 안 영상 영역 crop(w:h:x:y) 또는 None)
# 소스가 .png 면 끝-시작 = 화면 길이(초), 소리는 SILENT_AUDIO 에서 가져온다.
CLIPS = [
    ("threads/th_DekZUBSjd90.mp4", 1.8, 10.0, "@jeremylynchofficial", "이걸로 튀면 경찰도 답 없음", "🚓", None),
    ("threads/th_Dei14XIkyAn.mp4", 1.0, 9.9, "@iamneubert", "월요일 출근길, 다들 이 상상 해봤잖아", "☕", "720:450:0:405"),
    ("threads/th_DejYB7VmuW2.mp4", 4.0, 11.5, "@bankii_ii", "이륙은 성공했는데 치킨은 못 지킴", "🍗", None),
    ("sources/c10_tratamavie.mp4", 2.0, 8.3, "@tratamavie", "딱지 하나 떼려고 사다리까지 출동", "🪜", None),
    ("threads/th_DelLh1mie2O.mp4", 3.0, 11.0, "@dijeong81 (퍼옴)", "발표 영상이 애니보다 더 애니 같음", "🎬", None),
    ("threads/th_DelOef2mFBZ.mp4", 11.5, 21.5, "@rakesh_barotvalley", "인도에 출시하면 생기는 일", "⚡", "720:540:0:370"),
    ("threads/thr_spoon_1.mp4", 4.0, 10.5, "@story_spoon", "부산 출시되면 부캉이랑 바다 위 드라이브", "🦈", None),
    ("sources/c2_xander.sgc.mp4", 1.0, 10.0, "@xander.sgc", "날 수 있어도 안 나는 게 진짜 승자", "👴", None),
]
SILENT_AUDIO = ("sources/c2_youjinhyeok.mp4", 0.0)  # AI 컷 밑에 깔 현장 소리(부캉이 영상 앞부분)

# 원본 클립 속 효과음(엔진, 사이렌, 추진음 등): 클립 번호 → 살릴 구간(화면 기준 초).
# 컷별 스펙트로그램에서 음악(화음+박자 패턴)이 없는 구간만 골랐다. 없는 클립 = 원본 소리가 음악이라 뺌
# (애니화, 실제 부캉이). 배경음 아래로 작게(SFX_RMS).
SFX_RMS = -24  # 효과음 구간 RMS(dBFS, 채널당). 배경음 -16 LUFS 아래로 들리게
ORIG_SFX = {
    0: (1.3, 3.6),   # 앞부분 음악 → 이륙 뒤 사이렌, 추진음만
    1: (0.0, 3.6),   # 차 안 소리 + 이륙, 커피 쏟는 소리
    2: (0.0, 1.3),   # 방콕 길거리 경적 (뒤쪽은 음악성 지속음이라 뺌)
    3: (0.0, 3.6),   # 경찰차 주변 소리
    5: (2.2, 3.6),   # 앞부분 인도 음악 → 전깃줄 걸린 뒤 소리만
    7: (0.0, 3.6),   # 고속도로 주행음
}

# 원본 소리가 음악이라 못 쓰는 컷에 다른 클립의 효과음 구간을 빌려 깐다: 클립 번호 → [(소스, 시작, 끝, 화면 기준 초)]
ROAR = ("threads/th_DekZUBSjd90.mp4", 5.0, 9.0)    # 은행털이 이륙 뒤 추진 굉음(음악 없음)
BLAST = ("threads/th_Dei14XIkyAn.mp4", 5.0, 5.7)  # 월요일 출근 점화 폭발음
EXTRA_SFX = {}  # 2026-10-17 애니 4:(BLAST 1.95 + ROAR 6.0~7.65 @2.0), 인도 5:(ROAR 5.0~7.3 @0) 넣어봤다가 사용자 요청으로 뺌

# 영상 속 반응 글씨(박다현체): 클립 번호 → [(글, 시작초, 끝초, 박스 안 중심 x, y, 색, 기울기)]
# 위치는 컷별 프레임을 4x4 칸으로 나눠 보고 얼굴, 차, 주인공 동작을 피해서 잡았다.
YEL, WHT = (255, 230, 0), (255, 255, 255)
REACT = {
    0: [("아저씨 그 차\n뭐예요..?", 0.2, 1.4, 840, 840, WHT, 4), ("경찰: 저걸\n어떻게 잡냐고", 1.8, 3.6, 300, 190, YEL, -6)],
    1: [("5분 늦으면\n지각인데..", 0.2, 1.6, 850, 140, WHT, 5), ("커피는 포기한다", 2.4, 3.6, 800, 110, YEL, 4)],
    2: [("치킨파티\n어서오고~", 1.8, 3.6, 880, 130, YEL, 4)],
    3: [("어..? 저거\n잡아야 되는데", 0.2, 1.5, 820, 450, WHT, 5), ("딱지 떼러\n올라가는 중", 1.6, 3.6, 820, 640, YEL, 5)],
    4: [("이거 넷플 가자", 2.0, 3.6, 540, 930, YEL, -3)],
    5: [("전깃줄은\n생각 못 했지", 1.8, 3.6, 850, 130, YEL, 5)],
    6: [("부캉이 너\n면허는 있냐", 0.4, 3.6, 270, 150, YEL, -5)],
    7: [("응 니들은\n날어라잉~", 1.2, 3.6, 850, 330, YEL, 5)],
}


def emoji_img(ch, size):
    im = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((0, 0), ch, font=ImageFont.truetype(EMOJI, 160), embedded_color=True)
    im = im.crop(im.getbbox())
    return im.resize((size, int(size * im.height / im.width)), Image.LANCZOS)


def fit_font(d, path, texts, size, maxw):
    while size > 30:
        f = ImageFont.truetype(path, size)
        if max(d.textlength(t, font=f) for t in texts) <= maxw:
            return f
        size -= 2
    return ImageFont.truetype(path, size)


def overlay(handle, caption, emo, path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    d = ImageDraw.Draw(im)
    ft = fit_font(d, F_TITLE, [t for t, _ in TITLE], 118, 880)
    for (t, c), y in zip(TITLE, TITLE_Y):
        d.text((W // 2, y), t, font=ft, fill=c, anchor="mm")
    im.paste((0, 0, 0, 0), (0, BOX_Y, W, BOX_Y + BOX_H))  # 클립 자리 투명
    d.text((W // 2, HANDLE_Y), handle, font=ImageFont.truetype(F_MED, 26), fill=(110, 110, 110), anchor="mm")
    size = 60
    while True:  # 설명 + 이모지 폭이 CAP_MAXW 를 넘으면 글자 줄임
        fc = ImageFont.truetype(F_CAP, size)
        e = emoji_img(emo, int(size * 1.05))
        tw = d.textlength(caption, font=fc)
        if tw + 12 + e.width <= CAP_MAXW or size <= 44:
            break
        size -= 2
    x0 = (W - (tw + 12 + e.width)) / 2
    d.text((x0, CAP_Y), caption, font=fc, fill="white", anchor="lm")
    im.alpha_composite(e, (int(x0 + tw + 12), int(CAP_Y - e.height / 2)))
    im.save(path)


def react_png(text, x, y, color, rot, scale, path):
    """반응 글씨 한 장(1080x1920 투명). 검정 외곽선, 살짝 기울임."""
    f = ImageFont.truetype(F_REACT, int(76 * scale))  # 108 의 0.7배
    tmp = Image.new("RGBA", (1000, 300), (0, 0, 0, 0))
    ImageDraw.Draw(tmp).multiline_text((500, 150), text, font=f, fill=color, anchor="mm", align="center", spacing=4,
                             stroke_width=int(5.6 * scale), stroke_fill=(0, 0, 0))
    tmp = tmp.crop(tmp.getbbox()).rotate(rot, expand=True, resample=Image.BICUBIC)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cx = min(max(x, tmp.width // 2 + 20), W - tmp.width // 2 - 20)  # 박스 밖으로 안 나가게
    im.alpha_composite(tmp, (int(cx - tmp.width / 2), int(BOX_Y + y - tmp.height / 2)))
    im.save(path)


def decode(path, s0, s1, speed=1.0, sr=48000):
    """소스 s0~s1 구간을 speed 배속(음높이 유지)으로 풀어 (n,2) float32."""
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(s0), "-t", str(s1 - s0), "-i", path,
                          "-af", atempo(speed) if speed != 1.0 else "anull",
                          "-ac", "2", "-ar", str(sr), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def place(bed, x, at, sr, fi=0.05, fo=0.2):
    """x 를 RMS SFX_RMS 로 맞추고 앞뒤 페이드 후 bed 의 at 초에 더한다."""
    import numpy as np
    if not len(x):
        return
    x = x * (10 ** (SFX_RMS / 20) / (np.sqrt(np.mean(x ** 2)) + 1e-9))
    n = len(x)
    env = np.ones(n, np.float32)
    a, b = min(int(fi * sr), n), min(int(fo * sr), n)
    env[:a] = np.linspace(0, 1, a)
    env[n - b:] = np.linspace(1, 0, b)
    o = int(at * sr)
    m = max(0, min(n, len(bed) - o))
    bed[o:o + m] += (x * env[:, None])[:m]


def part_audio(i, f, a, b, dur, speed, path, sr=48000):
    """클립 소리 wav: 원본 효과음 구간(ORIG_SFX, 화면 기준 초) + 빌린 효과음(EXTRA_SFX).
    필터 그래프의 adelay/volume(t) 는 소리 위치가 밀리거나 통째로 빠져서 numpy 로 직접 놓는다."""
    import numpy as np, wave
    bed = np.zeros((int(dur * sr), 2), np.float32)
    w = ORIG_SFX.get(i)
    if w:
        x = decode(os.path.join(SRC, f), a, b, speed, sr)
        place(bed, x[int(w[0] * sr):int(w[1] * sr)], w[0], sr, 0.15, 0.15)
    for sf, s0, s1, at in EXTRA_SFX.get(i, []):
        place(bed, decode(os.path.join(SRC, sf), s0, s1, 1.0, sr), at, sr)
    pcm = (np.clip(bed, -1, 1) * 32767).astype("<i2")
    with wave.open(path, "wb") as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(sr); wf.writeframes(pcm.tobytes())


def atempo(s):
    """atempo 는 한 단에 0.5~2.0 → 곱으로 나눠 체인."""
    parts = []
    while s > 2.0:
        parts.append("atempo=2.0")
        s /= 2.0
    parts.append(f"atempo={s:.4f}")
    return ",".join(parts)


def render(i, clip):
    f, a, b, handle, cap, emo, area = clip
    ov = os.path.join(OUT, f"ov_{i}.png")
    overlay(handle, cap, emo, ov)
    part = os.path.join(OUT, f"part_{i}.mp4")
    pre = f"crop={area}," if area else ""
    # 박스 비율(1080:1033)로 가운데를 잘라 꽉 채움
    fit = (f"{pre}crop='min(iw,ih*{W}/{BOX_H})':'min(ih,iw*{BOX_H}/{W})',"
           f"scale={W}:{BOX_H},setsar=1")
    if f.endswith(".png"):
        dur = b - a
        speed = 1.0
        n = int(dur * FPS)
        af, sp = SILENT_AUDIO
        inputs = ["-loop", "1", "-t", str(dur), "-i", os.path.join(OUT, f),
                  "-ss", str(sp), "-t", str(dur), "-i", os.path.join(SRC, af)]
        vsrc = (f"[0:v]scale=2560:-2,zoompan=z='1.0+0.15*on/{n}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2'"
                f":d=1:s=1280x984:fps={FPS},{fit},trim=duration={dur}[v];")
    else:
        dur = (b - a) if i in REALTIME else TARGET
        speed = (b - a) / dur
        inputs = ["-ss", str(a), "-t", str(b - a), "-i", os.path.join(SRC, f)]
        vsrc = f"[0:v]{fit},setpts=(PTS-STARTPTS)/{speed:.4f},fps={FPS}[v];"
    ov_idx = 2 if f.endswith(".png") else 1  # 오버레이 PNG 입력 번호
    # 반응 글씨: 처음 0.1초는 1.25배로 크게 떴다가 원래 크기(팝)
    rins, rchain, last = [], "", f"[b{0}]"
    k = ov_idx + 1
    for j, (txt, t0, t1, x, y, col, rot) in enumerate(REACT.get(i, [])):
        for sc, a0, a1 in ((1.25, t0, t0 + 0.1), (1.0, t0 + 0.1, t1)):
            rp = os.path.join(OUT, f"react_{i}_{j}_{int(sc * 100)}.png")
            react_png(txt, x, y, col, rot, sc, rp)
            rins += ["-loop", "1", "-i", rp]
            nxt = f"[r{k}]"
            rchain += f"{last}[{k}:v]overlay=0:0:enable='between(t,{a0},{a1})'{nxt};"
            last, k = nxt, k + 1
    fc = (vsrc +
          f"color=black:s={W}x{H}:r={FPS}:d={dur}[bg];[bg][v]overlay=0:{BOX_Y}[b];"
          f"[b][{ov_idx}:v]overlay=0:0[b0];" + rchain +
          f"{last}format=yuv420p[vo]")
    wav = os.path.join(OUT, f"audio_{i}.wav")
    part_audio(i, f, a, b, dur, speed, wav)
    rins += ["-i", wav]
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-loop", "1", "-i", ov, *rins,
                    "-filter_complex", fc, "-map", "[vo]", "-map", f"{k}:a", "-t", f"{dur:.3f}",
                    "-r", str(FPS), "-c:v", "libx264", "-crf", "18", "-preset", "fast",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", part], check=True)
    return part, dur


def main():
    os.makedirs(OUT, exist_ok=True)
    parts, total = [], 0.0
    for i, clip in enumerate(CLIPS):
        p, d = render(i, clip)
        parts.append(p)
        total += d
    lst = os.path.join(OUT, "parts.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    final = os.path.join(OUT, "teslameme.mp4")
    if MUSIC:
        msrc = os.path.join(SRC, MUSIC)
        mdur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                              "-of", "csv=p=0", msrc]))
        tail = f"loudnorm=I={MUSIC_LUFS}:TP=-1.5,apad,atrim=0:{total:.3f}[m]"  # 곡 원래 끝으로 마무리
        if MUSIC_JUMP:
            ja, jb = MUSIC_JUMP
            mlen = ja + (mdur - jb)
            ins = ["-i", msrc]
            af = (f"[1:a]asplit[p][q];[p]atrim=0:{ja + 0.03},asetpts=PTS-STARTPTS[pa];"
                  f"[q]atrim={jb - 0.03}:{mdur},asetpts=PTS-STARTPTS[pb];"
                  f"[pa][pb]acrossfade=d=0.06,atempo={mlen / total:.4f},{tail}")
        elif mdur - MUSIC_SS >= total:
            ins = ["-ss", str(MUSIC_SS), "-i", msrc]  # 긴 곡은 시작점부터 그대로, 끝 1초 페이드아웃
            af = (f"[1:a]afade=t=in:d=0.08,afade=t=out:st={total - 1.0:.2f}:d=1.0,"
                  f"{tail}")
        else:
            ins = ["-i", msrc]
            af = f"[1:a]atempo={mdur / total:.4f},{tail}"
        af += (f";[0:a]aresample=48000:async=1:first_pts=0,apad,atrim=0:{total:.3f}[c];"
               f"[c][m]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.9[a]")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, *ins,
                        "-filter_complex", af, "-map", "0:v", "-map", "[a]", "-t", f"{total:.3f}",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", final], check=True)
    else:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", final], check=True)
    print(final, f"{total:.1f}s")


if __name__ == "__main__":
    main()
