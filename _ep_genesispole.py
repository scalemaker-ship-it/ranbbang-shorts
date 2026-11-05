#!/usr/bin/env python3
"""란빵 2026-10-19: 제네시스 WEC 바르셀로나 첫 폴포지션. 무나레이션 + 댓글 반응형.
소스: SPOTV 오리지널 쇼츠 CFl2ChMQn4E(2026-10-18) 가운데 중계 화면만 잘라 씀. 원본 중계 해설 소리 그대로.
댓글: 같은 영상 실제 댓글(yt-dlp --write-comments)을 짧게 다듬고 아이디는 지어서 바꿈(사용자 지시).
사실 확인: 오토레이싱 10/17 예선 기사, 스포티비뉴스, 아시아투데이 10/18. 데뷔 시즌 제7전에서 팀 첫 폴(1분30초166, #17 조베르 21세).
레이아웃: 검정 1080x1920, 위 잘난체 2줄 타이틀, 가운데 16:9 중계 화면, 아래 댓글이 하나씩 쌓임.
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "..", "work", "yt_CFl2ChMQn4E", "src.mp4")
OUT = os.path.join(ROOT, "work", "genesispole")
os.makedirs(OUT, exist_ok=True)
F_TITLE = os.path.expanduser("~/Library/Fonts/JalnanGothic.otf")
F_ID = os.path.expanduser("~/Library/Fonts/Pretendard-SemiBold.otf")
F_TXT = os.path.expanduser("~/Library/Fonts/Pretendard-Bold.otf")
POP = os.path.expanduser("~/Desktop/kim/ssul/assets/sfx/ic/notify_message_pop.wav")

SS, DUR = 43.0, 38.6          # 원본 43.0~81.6초: 마지막 랩 → 1분30초166 → 폴 포지션 → 파크페르메
TITLE = [("경험 삼아 나왔다던 제네시스", (255, 255, 255)), ("첫 시즌만에 폴포지션", (255, 222, 0))]
TITLE_Y = (230, 351)
VID_Y = 470                   # 1080x608
CM_Y0, CM_Y1 = 1125, 1860     # 댓글 영역
# (나오는 시각, 아이디, 댓글, 아바타 색)
COMMENTS = [
    (2.0, "@corner_maniac", "코너 탈출할 때 치고 나오는 거\n진짜 장난 아니네 와~", (231, 76, 60)),
    (13.4, "@pitwall_kim", "도요타가 14년 걸린 걸\n첫 시즌에 해버림ㅋㅋ", (52, 152, 219)),
    (18.5, "@lap0930", "폴 먹은 선수가 21살 최연소라는 게\n더 무서움", (155, 89, 182)),
    (24.2, "@hypercar_kr", "올해는 데이터 수집하러 나온 거라며ㅋㅋ", (26, 188, 156)),
    (28.0, "@podium_plz", "진짜 포디엄 기대해도 되는 거냐??", (230, 126, 34)),
    (32.0, "@sixhours_", "근데 6시간 가면 피트에서\n시간 다 까먹음", (127, 140, 141)),
    (35.3, "@rookie_team", "신생팀은 피트스탑이 늘 문제ㅋ", (241, 196, 15)),
]


def fit(path, text, size, maxw):
    while ImageFont.truetype(path, size).getlength(text) > maxw:
        size -= 2
    return ImageFont.truetype(path, size)


def background(path):
    im = Image.new("RGB", (1080, 1920), (0, 0, 0))
    d = ImageDraw.Draw(im)
    size = min(fit(F_TITLE, t, 120, 1080 - 120).size for t, _ in TITLE)
    f = ImageFont.truetype(F_TITLE, size)
    for (t, col), y in zip(TITLE, TITLE_Y):
        d.text((540, y), t, font=f, fill=col, anchor="mm")
    d.text((1060, VID_Y + 608 + 10), "영상: SPOTV", font=ImageFont.truetype(F_ID, 24), fill=(150, 150, 150), anchor="ra")
    im.save(path)


def card(id_, txt, col):
    fi, ft = ImageFont.truetype(F_ID, 34), ImageFont.truetype(F_TXT, 46)
    lines = txt.split("\n")
    h = 62 + 60 * len(lines) + 24
    im = Image.new("RGBA", (1000, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, 999, h - 1), 28, fill=(32, 32, 32, 235))
    d.ellipse((24, 24, 100, 100), fill=col)
    d.text((62, 62), id_[1].upper(), font=ImageFont.truetype(F_TXT, 40), fill="white", anchor="mm")
    d.text((124, 22), id_, font=fi, fill=(170, 170, 170))
    for i, l in enumerate(lines):
        d.text((124, 66 + 60 * i), l, font=ft, fill="white")
    return im


def panel(k, path):
    """k번째 댓글까지 보이는 상태. 영상 바로 아래부터 위에서 아래로 쌓고, 넘치면 오래된 것부터 뺌."""
    im = Image.new("RGBA", (1080, CM_Y1 - CM_Y0), (0, 0, 0, 0))
    cards = [card(i, t, c) for _, i, t, c in COMMENTS[:k + 1]]
    while sum(c.height + 18 for c in cards) > im.height:
        cards.pop(0)
    y = 0
    for c in cards:
        im.alpha_composite(c, (40, y))
        y += c.height + 18
    im.save(path)


def main():
    bg = os.path.join(OUT, "bg.png")
    background(bg)
    inputs = ["-loop", "1", "-t", str(DUR), "-i", bg, "-ss", str(SS), "-t", str(DUR), "-i", SRC]
    fc = ["[1:v]crop=1030:580:25:670,scale=1080:608,setsar=1[v]", "[0:v][v]overlay=0:%d[b0]" % VID_Y]
    for k, (t, *_r) in enumerate(COMMENTS):
        p = os.path.join(OUT, f"cm_{k}.png")
        panel(k, p)
        inputs += ["-loop", "1", "-t", str(DUR), "-i", p]
        end = COMMENTS[k + 1][0] if k + 1 < len(COMMENTS) else DUR
        y = f"if(lt(t-{t},0.18),{CM_Y0}+60*(1-(t-{t})/0.18),{CM_Y0})"   # 새 댓글 들어올 때 살짝 올라오며 등장
        fc.append(f"[b{k}][{k + 2}:v]overlay=0:'{y}':enable='between(t,{t},{end})'[b{k + 1}]")
    n = len(COMMENTS)
    pops = []
    for k, (t, *_r) in enumerate(COMMENTS):
        inputs += ["-i", POP]
        ms = int(t * 1000)
        fc.append(f"[{n + 2 + k}:a]volume=0.35,adelay={ms}|{ms}[p{k}]")
        pops.append(f"[p{k}]")
    fc.append(f"[1:a]volume=1.0[o];[o]{''.join(pops)}amix=inputs={n + 1}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5[a]")
    out = os.path.join(OUT, "genesispole.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc),
                    "-map", f"[b{n}]", "-map", "[a]", "-t", str(DUR), "-r", "30", "-c:v", "libx264", "-crf", "18",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out], check=True)
    print(out)


if __name__ == "__main__":
    main()
