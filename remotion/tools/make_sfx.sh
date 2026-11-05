#!/bin/bash
# 란빵 v2 효과음 — 전부 ffmpeg 합성(라이선스 문제 없음). 사용: tools/make_sfx.sh → public/sfx/*.wav
cd "$(dirname "$0")/../public/sfx"
F="ffmpeg -y -loglevel error"
# boom: 저음 쿵(서브 드롭) — 반전·충격
$F -f lavfi -i "aevalsrc=0.95*sin(2*PI*(80*t-55*t*t))*exp(-3.2*t):s=44100:d=1.4" \
   -f lavfi -i "anoisesrc=d=0.25:c=brown:a=0.5:r=44100" \
   -filter_complex "[1]lowpass=f=400,afade=t=out:st=0:d=0.25[n];[0][n]amix=inputs=2:normalize=0,alimiter=limit=0.95" boom.wav
# hit: 휙-탁(공기 가르고 때림) — 강조 펀치인
$F -f lavfi -i "anoisesrc=d=0.32:c=pink:a=0.7:r=44100" -f lavfi -i "aevalsrc=sin(2*PI*(160*t-200*t*t))*exp(-18*t):s=44100:d=0.4" \
   -filter_complex "[0]highpass=f=900,lowpass=f=6000,afade=t=in:d=0.2,afade=t=out:st=0.2:d=0.1[w];[1]adelay=220|220[h];[w][h]amix=inputs=2:weights=0.8 1.3:normalize=0,alimiter=limit=0.95" hit.wav
# ding: 맑은 종 — 정보·정답
$F -f lavfi -i "aevalsrc=0.5*sin(2*PI*1568*t)*exp(-4*t)+0.3*sin(2*PI*2349*t)*exp(-6*t)+0.15*sin(2*PI*3136*t)*exp(-9*t):s=44100:d=1.2" ding.wav
# sting: 긴장 불협화음 — '무서운 현실'
$F -f lavfi -i "aevalsrc=0.28*(sin(2*PI*110*t)+sin(2*PI*116.5*t)+sin(2*PI*155.6*t)+0.5*sin(2*PI*233*t))*min(1\,t*8)*exp(-1.4*t):s=44100:d=2.0" -af "alimiter=limit=0.9" sting.wav
# crack: 금속 뚝 — 부서짐·결함
$F -f lavfi -i "anoisesrc=d=0.35:c=white:a=0.9:r=44100" -f lavfi -i "aevalsrc=0.8*sin(2*PI*420*t)*exp(-25*t)+0.5*sin(2*PI*1260*t)*exp(-30*t):s=44100:d=0.35" \
   -filter_complex "[0]bandpass=f=2500:w=2000,afade=t=out:st=0.01:d=0.2[n];[n][1]amix=inputs=2:normalize=0,alimiter=limit=0.95" crack.wav
# siren: 경찰 사이렌 짧게(우-웅 2번) — 단속
$F -f lavfi -i "aevalsrc=0.35*sin(2*PI*(700*t+180*sin(2*PI*1.6*t)/(2*PI*1.6))):s=44100:d=1.3" -af "afade=t=in:d=0.05,afade=t=out:st=1.0:d=0.3" siren.wav
# pop: 뽁 — 숫자·키워드 팝
$F -f lavfi -i "aevalsrc=0.8*sin(2*PI*(500*t+2500*t*t))*exp(-30*t):s=44100:d=0.18" pop.wav
# cash: 띠링(두 음) — 돈·가격
$F -f lavfi -i "aevalsrc=0.45*sin(2*PI*1319*t)*exp(-7*t)+0.45*sin(2*PI*1760*(t-0.09))*exp(-6*(t-0.09))*gte(t\,0.09):s=44100:d=0.9" cash.wav
ls
