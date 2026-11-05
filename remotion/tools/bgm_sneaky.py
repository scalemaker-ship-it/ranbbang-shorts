#!/usr/bin/env python3
"""란빵 BGM 합성 — '살금살금 장난스러운' 피치카토·마림바 루프 (2026-10-10 사용자 지시: youtube.com/shorts/2C3s9NbeLcc 배경음과 비슷하게)
레퍼런스 분석(demucs 로 음악만 분리 → librosa): D단조(화성단음계, C# 이끔음) · 123BPM · 8분음 스타카토 뜯는 소리 · Dm–A7–Gm 왕복 ·
A–A#–B–C–C# 반음 기어오르기 · 타악은 가볍게. 곡을 베끼지 않고 이 특징만 따서 코드로 합성 — 라이선스 문제 없음.

  python3 tools/bgm_sneaky.py [out.mp3]   # 기본 ~/Desktop/kim/ssul/assets/bgm/sneaky-123.mp3 (16마디 ≈ 31.2초, 이음매 없이 반복)
"""
import os, subprocess, sys, wave
import numpy as np

SR = 44100
BPM = 123
BEAT = 60 / BPM
E8 = BEAT / 2
BARS = 16
N = int(round(BARS * 4 * BEAT * SR))
rng = np.random.default_rng(7)


def hz(note):  # "D4", "A#3"
    names = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}
    return 440.0 * 2 ** ((names[note[:-1]] + 12 * (int(note[-1]) + 1) - 69) / 12)


def pluck(f, dur, bright=0.5):
    """Karplus-Strong 피치카토"""
    n = int(dur * SR)
    p = max(2, int(SR / f))
    buf = rng.uniform(-1, 1, p)
    out = np.empty(n)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = (buf[i % p] + buf[(i + 1) % p]) * 0.5 * (0.994 + 0.005 * bright)
    env = np.minimum(1, np.arange(n) / (0.002 * SR)) * np.exp(-np.arange(n) / (dur * SR * 0.35))
    return out * env


def marimba(f, dur):
    t = np.arange(int(dur * SR)) / SR
    tone = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * 40) + 0.1 * np.sin(2 * np.pi * f * 10 * t) * np.exp(-t * 80)
    return tone * np.exp(-t * 11) * np.minimum(1, t / 0.002)


def kick():
    t = np.arange(int(0.25 * SR)) / SR
    return np.sin(2 * np.pi * (50 + 90 * np.exp(-t * 30)) * t) * np.exp(-t * 18)


def noise_hit(dur, decay, hp):
    n = rng.uniform(-1, 1, int(dur * SR))
    n = n - np.convolve(n, np.ones(hp) / hp, mode="same")   # 간단 고역통과
    t = np.arange(len(n)) / SR
    return n * np.exp(-t * decay)


mix = np.zeros(N + SR)


def put(sig, at, gain):
    i = int(at * SR)
    mix[i:i + len(sig)] += sig[: max(0, len(mix) - i)] * gain


# 2마디 단위 화음: Dm | A7 | Dm | A7 | Gm | Dm | A7 | Dm  (×2 → 16마디)
PROG = ["Dm", "A7", "Dm", "A7", "Gm", "Dm", "A7", "Dm"]
CH = {"Dm": ["D3", "F3", "A3"], "A7": ["C#3", "E3", "G3"], "Gm": ["G2", "A#2", "D3"]}
BASS = {"Dm": ["D2", "A1"], "A7": ["A1", "E2"], "Gm": ["G1", "D2"]}
# 멜로디(8분음 8칸 = 1마디, None = 쉼) — 스타카토 + 반음 기어오르기
MEL = {
    "Dm": [["D5", None, "F5", None, "A5", "G#5", "A5", None], ["F5", None, "D5", None, "E5", "F5", "E5", None]],
    "A7": [["C#5", None, "E5", None, "A4", "A#4", "B4", "C5"], ["C#5", None, None, "E5", "G5", None, "E5", None]],
    "Gm": [["G5", None, "A#5", None, "D5", None, "A#4", None], ["A4", "A#4", "B4", "C5", "C#5", None, "D5", None]],
}

for bi in range(BARS):
    chord = PROG[(bi // 2) % len(PROG)]
    half = bi % 2
    t0 = bi * 4 * BEAT
    last_bar = bi == BARS - 1
    # 베이스 피치카토: 1·3박 + 4박 뒷박 살짝
    b1, b2 = BASS[chord]
    put(pluck(hz(b1), BEAT * 0.9, 0.2), t0, 0.55)
    put(pluck(hz(b2), BEAT * 0.9, 0.2), t0 + 2 * BEAT, 0.5)
    put(pluck(hz(b1), E8 * 0.9, 0.2), t0 + 3.5 * BEAT, 0.35)
    # 화음 스타카토(뒷박마다)
    for k in range(4):
        for nn in CH[chord]:
            put(pluck(hz(nn) * 2, E8 * 0.7, 0.8), t0 + k * BEAT + E8, 0.12)
    # 멜로디 마림바 — 8마디마다 앞 4마디는 멜로디, 뒤는 같은 패턴을 한 옥타브 아래 피치카토로(변화)
    pat = MEL[chord][half]
    for k, nn in enumerate(pat):
        if nn is None or (last_bar and k > 5):
            continue
        at = t0 + k * E8
        if (bi // 4) % 2 == 0:
            put(marimba(hz(nn), E8 * 1.6), at, 0.32)
        else:
            put(pluck(hz(nn), E8 * 1.2, 0.9), at, 0.30)
            put(marimba(hz(nn) * 2, E8 * 1.2), at, 0.08)
    # 타악: 킥 1·3박, 핑거스냅 2·4박, 셰이커 16분
    for k in range(4):
        if k in (0, 2):
            put(kick(), t0 + k * BEAT, 0.45)
        else:
            put(noise_hit(0.12, 45, 3), t0 + k * BEAT, 0.12)
        for s in range(4):
            put(noise_hit(0.05, 120, 2), t0 + k * BEAT + s * BEAT / 4, 0.035 if s % 2 else 0.05)

# 루프 이음매: 끝 꼬리를 앞에 더해 반복 시 끊김 없게
tail = mix[N:]
mix[: len(tail)] += tail
y = mix[:N]
y = y / np.max(np.abs(y)) * 0.9
st = np.stack([y, np.roll(y, int(0.004 * SR)) * 0.96], axis=1)   # 살짝 넓게
out = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Desktop/kim/ssul/assets/bgm/sneaky-123.mp3")
tmp = out + ".wav"
with wave.open(tmp, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype("<i2").tobytes())
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-af", "highpass=f=35,loudnorm=I=-26:TP=-3:LRA=11",
                "-ar", "44100", "-b:a", "192k", out], check=True)
os.remove(tmp)
print("✓", out, f"{N / SR:.1f}s")
