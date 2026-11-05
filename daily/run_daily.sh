#!/bin/zsh
# 란빵 하루 10편 — launchd(com.scalemaker.ranbbang-daily10)가 매일 15:00 KST 에 run_daily.command(Terminal 경유)로 실행. 다음 날 10칸 예약.
# 수동 실행: ./daily/run_daily.sh   (강제: FORCE=1, 날짜 지정: TARGET_DATE=2026-10-30, 추가 지시: EXTRA="...")
export PATH="$HOME/Desktop/kim/shorts/ranbbang/daily/bin:$HOME/.local/bin:$HOME/.npm-global/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export TZ=Asia/Seoul
cd "$(dirname "$0")/.." || exit 1
TARGET=${TARGET_DATE:-$(date -v+1d +%Y-%m-%d)}
LOG="daily/logs/$TARGET.log"; LOCK="daily/logs/.lock"
notify() { osascript -e "display notification \"$1\" with title \"란빵 하루 10편\"" 2>/dev/null; }
if [[ -z "$FORCE" ]] && (( $(grep -c "^$TARGET	" daily/log.tsv 2>/dev/null) >= 10 )); then
  echo "[$(date)] $TARGET 10편 이미 예약됨 → skip" >> "$LOG"; exit 0; fi
if [[ -f "$LOCK" ]] && (( $(date +%s) - $(stat -f %m "$LOCK") < 25200 )); then
  echo "[$(date)] 다른 실행 진행 중 → skip" >> "$LOG"; exit 0; fi
touch "$LOCK"; trap 'rm -f "$LOCK"' EXIT
echo "[$(date)] 시작 target=$TARGET" >> "$LOG"
caffeinate -i claude -p "$(cat daily/PROMPT.md)

지금은 $(date '+%Y-%m-%d %H:%M') ($(date +%A)) 이고, 예약 대상 날짜는 **$TARGET** 이다. 이미 daily/log.tsv 에 적힌 $TARGET 슬롯은 건너뛴다. 큐 파일 이름은 daily/queue_$TARGET.txt, 로그는 daily/logs/${TARGET}_{img,tts,build}.log 로 한다.
${EXTRA}" \
  --permission-mode bypassPermissions >> "$LOG" 2>&1
echo "[$(date)] 종료 code=$?" >> "$LOG"
N=$(grep -c "^$TARGET	" daily/log.tsv 2>/dev/null)
notify "$TARGET 예약 ${N:-0}/10 편 — daily/logs 확인"
