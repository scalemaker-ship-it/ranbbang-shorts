#!/bin/bash
# 경모 목소리 TTS 러너 — tts_myvoice 가 줄마다 메모리가 쌓여(16GB+, 스왑 포화) 느려지는 문제:
# 16GB 넘으면 프로세스를 끄고 같은 편을 다시 돌린다(이미 만든 줄은 건너뜀, 최대 30회).
# 같은 줄에서 계속 터지면(try 5 넘게 같은 line 수) 그 편은 TTS_FAIL → 프롬프트 쪽에서 say 문장을 고쳐 큐 끝에 다시 넣는다.
#   daily/tts_runner.sh <queue.txt> <log>     큐는 slug 한 줄씩, END 로 끝(END 전에 줄을 더 넣으면 이어서 처리)
cd /Users/kimyiseul/Desktop/kim/ssul
PY=~/Desktop/kim/myvoice-tts/.venv/bin/python
Q=$1; LOG=$2; i=1
while true; do
  s=$(sed -n "${i}p" $Q)
  [ -z "$s" ] && { sleep 15; continue; }
  [ "$s" = "END" ] && break
  echo "== $s $(date +%T)" >> $LOG
  ok=0; stuck=0; last=-1
  for try in $(seq 1 30); do
    $PY pipeline/tts_myvoice.py $s > /dev/null 2>&1 &
    pid=$!; t0=$(date +%s)
    while kill -0 $pid 2>/dev/null; do
      mem=$(top -l 1 -pid $pid -stats mem 2>/dev/null | tail -1 | tr -d ' ')
      case "$mem" in *G) g=${mem%G}; g=${g%%.*}; [ "${g:-0}" -ge 16 ] && { kill $pid; echo "  restart $s try$try mem=$mem $(date +%T)" >> $LOG; } ;; esac
      # 2026-11-01 교훈: 12GB 근처 스왑 포화로 한 줄에 15~30분 멈춤 → 새 line_*.wav 가 6분간 안 생기면 kill
      nw=$(stat -f %m work/$s/tts/line_*.wav 2>/dev/null | sort -n | tail -1); ref=$(( ${nw:-0} > t0 ? ${nw:-0} : t0 ))
      [ $(( $(date +%s) - ref )) -gt 360 ] && kill -0 $pid 2>/dev/null && { kill $pid; echo "  watchdog kill $s try$try $(date +%T)" >> $LOG; }
      sleep 20
    done
    wait $pid && { ok=1; break; }
    n=$(ls work/$s/tts/line_*.wav 2>/dev/null | wc -l | tr -d ' ')
    [ "$n" = "$last" ] && stuck=$((stuck+1)) || stuck=0
    last=$n
    [ $stuck -ge 5 ] && { echo "  stuck at line $n" >> $LOG; break; }
  done
  [ $ok = 1 ] && python3 pipeline/tts.py $s > /dev/null 2>&1 && echo "TTS_OK $s $(date +%T)" >> $LOG || echo "TTS_FAIL $s $(date +%T)" >> $LOG
  i=$((i+1))
done
echo "TTS_DONE $(date +%T)" >> $LOG
