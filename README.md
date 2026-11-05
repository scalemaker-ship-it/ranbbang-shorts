# 란빵 자동차 쇼츠 제작 스킬

유튜브 채널 **란빵 (@eggbread0)** 의 자동차 썰 / 신차 / 차량용품 쇼츠를 하루 10편씩 사람 없이 만들어 예약 업로드하는 Claude Code 워크플로우입니다.
매일 15:00 KST 에 launchd 가 Claude Code 를 헤드리스로 띄우고, 소재 수집부터 YouTube Studio 예약까지 2~3시간 안에 끝냅니다.

```
보배드림 베스트 / 신차 뉴스 / 용품 글 10개 선정
→ 사실 조사표 (work/research_YYMMDD.md)
→ 원글 사진, 영상 캡처 + 얼굴 모자이크 (tools/mosaic.py, YuNet)
→ 부족한 장면은 GPT 실사풍 배경 생성 (codex-image gen.sh)
→ 음슴체 대본 10~12줄 + "구독!" (_batch_YYMMDD.py 생성기, 370자 이하)
→ GPT-SoVITS TTS (daily/tts_runner.sh)
→ Remotion 조립: 컷, 줌, 효과음, 인포그래픽 (remotion/tools/build_v2.py)
→ 1.2배속, 40초 미만 검수
→ 다음 날 10칸 YouTube Studio 예약 + 쇼핑태그 5개 (chrome-mcp)
```

## 단일 출처

| 파일 | 내용 |
|---|---|
| `prd.md` | 계정, 소재 범위, 발행 규칙, v2 편집 규칙 표, 신차 대본 구조, 날짜별 기록 |
| `daily/PROMPT.md` | 헤드리스 Claude 에게 주는 전체 지시문 (소재 선정, 대본 규칙, 제작 순서, 예약 업로드 절차) |
| `제작과정_공유본.md` | 2026-11-02 기준 재현용 설명서. 수치는 코드에서 확인한 값 |

## 폴더 구성

```
daily/            launchd 진입점(run_daily.sh), 지시문(PROMPT.md), 이미지/TTS/빌드 러너 3개, 큐 파일, 발행 로그(log.tsv)
_batch_YYMMDD.py  날짜별 대본 생성기. 최신 파일이 B/C/L/build/cap 헬퍼를 가지고 있고 다음 날 파일이 import 한다
_ep_*.py          단편 생성기 (초기 버전)
remotion/         v2 조립. src/RanbbangShort.tsx(컷, 줌), src/Info.tsx(인포그래픽), tools/build_v2.py(shots → 렌더)
tools/            mosaic.py(얼굴 픽셀화), models/ YuNet onnx
schedule_zernio.py  제목 위험 단어, 40초 미만 검증 (--dry-run)
work/<slug>/      편별 script.json, upload.md (영상, 이미지, TTS 산출물은 제외)
work/research_*.md  편별 사실, 수치, 출처, 법령 조사표
work/post_*/      커뮤니티 게시글 카드
제작과정_img/      설명서 그림
```

## 의존하는 다른 레포

- **ssul-shorts** (`~/Desktop/kim/ssul`): 대본 가이드, 레이아웃, 자막, TTS, 업로드 절차 문서. 란빵은 이 파이프라인을 그대로 쓰고 계정과 소재만 다릅니다. `work/<slug>` 를 `ssul/work/<slug>` 로 심볼릭 링크해 돌립니다.
- **issuecookie-voice**: GPT-SoVITS 목소리 세트. `ssul/pipeline/tts_issuecookie.py` 가 호출합니다.
- **codex-image 스킬** (`~/.claude/skills/codex-image/scripts/gen.sh`): 배경 이미지 생성.
- **chrome-mcp-stdio**: YouTube Studio 예약 업로드용 브라우저 MCP.

## 실행

```bash
# 수동 실행 (대상 날짜 = 내일)
./daily/run_daily.sh
# 날짜 지정, 강제 실행, 추가 지시
TARGET_DATE=2026-11-07 FORCE=1 EXTRA="신차 편은 2편만" ./daily/run_daily.sh

# 생성기 단독 실행 (해당 날짜 전 편 또는 slug 하나)
python3 _batch_1105.py
python3 _batch_1105.py <slug>

# 러너 3개 (큐 파일 = slug 한 줄씩 + END)
nohup python3 daily/img_runner.py daily/queue_2026-11-07.txt > daily/logs/2026-11-07_img.log 2>&1 &
nohup caffeinate -i daily/tts_runner.sh $PWD/daily/queue_2026-11-07.txt $PWD/daily/logs/2026-11-07_tts.log &
nohup caffeinate -i daily/build_runner.sh $PWD/daily/queue_2026-11-07.txt $PWD/daily/logs/2026-11-07_tts.log $PWD/daily/logs/2026-11-07_build.log &

# Remotion 단독 렌더
cd remotion && npm install && python3 tools/build_v2.py <slug> --render
```

launchd 등록 파일은 `daily/com.scalemaker.ranbbang-daily10.plist` 입니다. `~/Library/LaunchAgents/` 에 복사하고 `launchctl load` 하면 매일 15:00 KST 에 돕니다.

## 제작 규칙 요약 (상세는 prd.md, daily/PROMPT.md)

- 소재 비율: 보배드림 소식 5~6, 신차 2~3, 용품 1~2. 사망, 폭행, 자살 등은 소재와 제목 모두 금지
- 대본: 음슴체, 시청자 호칭 "님들", 대화체 대사 줄 1개 이상, 질문형 고정 댓글, 합계 370자 이하
- TTS 가 읽는 `say` 에는 숫자 없음 (금액은 "칠마넌" 식 한글)
- 화면: 원글 캡처 우선, 얼굴과 번호판 모자이크, 캐릭터 없음, 신차는 공식 뉴스룸 사진 + 출처
- 제목 14자 이하, 설명란 3줄 + 해시태그, 쇼핑태그 5개 필수
- 예약 칸: 12:00 / 12:30 / 13:00 / 13:30 / 14:00 / 19:00 / 19:30 / 20:00 / 20:30 / 21:00 KST

## 공개본에서 뺀 것

영상, 이미지, TTS 산출물(`work/<slug>/` 의 mp4, png, wav), `remotion/public/`, `work/_photos/`, 실행 로그, 관리자 구글 계정 주소(`<관리자 구글 계정>` 으로 치환). 폰트와 BGM 은 ssul-shorts 안내대로 직접 받습니다.
