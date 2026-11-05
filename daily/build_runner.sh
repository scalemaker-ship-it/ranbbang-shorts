#!/bin/bash
# Remotion v2 빌드 러너 — 큐 순서대로 TTS_OK + AI 이미지가 다 생기면 렌더 → work/<slug>/<slug>.mp4
#   daily/build_runner.sh <queue.txt> <tts.log> <build.log>
cd /Users/kimyiseul/Desktop/kim/shorts/ranbbang/work
Q=$1; TL=$2; LOG=$3; i=1
while true; do
  s=$(sed -n "${i}p" $Q)
  [ -z "$s" ] && { sleep 15; continue; }
  [ "$s" = "END" ] && break
  i=$((i+1))
  [ -f $s/$s.mp4 ] && [ $s/$s.mp4 -nt $s/v2/shots.json ] && { echo "SKIP_DONE $s" >> $LOG; continue; }
  need=$(wc -l < $s/v2/ai_prompts.tsv | tr -d ' ')
  until grep -q "TTS_OK $s\|TTS_FAIL $s" $TL && [ "$(ls $s/v2/ai/*.png 2>/dev/null | wc -l | tr -d ' ')" -ge "$need" ]; do sleep 20; done
  grep -q "TTS_OK $s" $TL || { echo "SKIP_TTS $s" >> $LOG; continue; }
  echo "== build $s $(date +%T)" >> $LOG
  (cd ../remotion && python3 tools/build_v2.py $s --render > ../work/$s/_build.log 2>&1) && cp $s/${s}_v2.mp4 $s/$s.mp4 && echo "BUILT $s $(date +%T)" >> $LOG || echo "BUILD_FAIL $s $(date +%T)" >> $LOG
done
echo "BUILD_DONE $(date +%T)" >> $LOG
