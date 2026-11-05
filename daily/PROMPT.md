# 란빵 하루 10편 자동 제작, 예약 (2026-10-28 사용자 지시)

너는 launchd(`com.scalemaker.ranbbang-daily10`)가 매일 15:00 KST 에 띄우는 헤드리스 Claude 다.
작업 디렉토리는 `~/Desktop/kim/shorts/ranbbang`. **자동차 쇼츠 10편을 만들어 대상 날짜의 12:00, 12:30, 13:00, 13:30, 14:00, 19:00, 19:30, 20:00, 20:30, 21:00 KST 10칸에 YouTube Studio(chrome-mcp-stdio) 로 예약 업로드**하고 끝낸다(2026-10-29 사용자 지시로 Zernio 대신 크롬 MCP. 쇼핑태그 5개도 업로드 때 같이).
사람에게 질문하지 않는다. 막히면 원인을 출력하고 그 편은 건너뛴다(만든 편만 예약, 못 채운 칸은 비워 둔다). 끝나면 `daily/log.tsv` 에 `대상날짜<TAB>HH:MM<TAB>slug<TAB>영상ID` 를 한 편당 한 줄 적는다.

먼저 읽는다: `prd.md`(§2 소재, §4 발행, §4-4 v2 편집 규칙 표, §4-6 신차 대본 구조, §5 기록의 최근 항목), 생성기 예시 `_batch_1027.py` 전체(B/C/L/build/cap 사용법, 근거표, 설명란, 댓글, 쇼핑태그 형식), `work/research_1027.md`(조사 기록 형식), `ssul/docs/used-sources.md` 끝 60줄(중복 대조).

## 0. 소재 10편 고르기

세 종류를 섞는다. 그날 소재의 인기(추천, 댓글 수)로 고르되 기본 비율은 **보배드림 소식 5~6편, 신차 소식 2~3편, 자동차 용품 1~2편**. 좋은 게 없으면 다른 종류로 채운다.

- **보배드림 소식**: 베스트 목록 `https://www.bobaedream.co.kr/list?code=best&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=70&page=1~3` (curl, 브라우저 UA). 행은 `<tr` 로 나누고 `href="/view?code=best&No=(\d+)&vdate="` 로 글 번호. 본문 `https://www.bobaedream.co.kr/view?code=best&No=<번호>`, 첨부 사진은 `file1.bobaedream.co.kr`, 영상은 `movie.bobaedream.co.kr`(ffmpeg 로 정지 프레임). 댓글은 view HTML 에서 `(26\.\d\d\.\d\d \d\d:\d\d) (?:답글 )?신고 (.*?) (?:답글 \d+ )?추천 (\d+) 반대 (\d+)` 로 뽑는다. 교통사고/블박, 자유게시판, 국산차/수입차 게시판 글 중 **돈 피해 소비자 썰, 과실 논쟁, 판결, 황당 상황**이 히트 유형(prd §5 10/21 성과 분석).
- **신차 소식**: 보배드림 베스트 안의 신차 글 + 뉴스 검색(네이버 뉴스 `https://search.naver.com/search.naver?where=news&query=신차+출시&sort=1`, 현대 `https://www.hyundai.com/kr/ko/brand-journal`, 기아 `https://www.kia.com/kr/vehicles/all`, 제네시스, 테슬라 코리아, 수입차 브랜드 뉴스룸). 가격, 제원, 출시일은 공식 뉴스룸이나 기사 2곳 이상에서 확인한 숫자만. 사진은 **공식 뉴스룸, 기사 사진 캡처 + 출처 credit**(AI 생성 금지, prd 메모리 "신제품은 실제 이미지"). 대본 구조는 prd §4-6(반응 대사 훅, 감탄, 당사자 발언, 반전, 질문).
- **자동차 용품**: 보배드림, 개드립(`https://www.dogdrip.net/dogdrip?sort_index=popular&page=1~2`)에서 화제인 용품 글, 네이버 데이터랩 쇼핑인사이트 차량용품 인기 검색어 상위 제품, 쿠팡 차량용품 베스트. 영상은 **v2 형식**으로만(틱톡 소재 편집형은 사람 검수가 필요해 안 씀): 제품 공식 이미지, 상세페이지, 리뷰 캡처(얼굴, 닉네임 모자이크). 가격과 기능은 상세페이지에서 확인한 것만. 과장 효능(100%, 완전 차단 등) 금지. 설명란에 제휴 링크는 넣지 않는다(쇼핑태그는 업로드 때 Studio 에서 붙인다).
- 중복 대조: `ssul/docs/used-sources.md` 와 `work/*/script.json` 의 `source`(`grep -l "<글번호>" work/*/script.json`). 같은 사건의 후속 보도는 새 사실(판결, 리콜 확정 등)이 있을 때만.
- 금지: 사망, 살인, 폭행, 자살, 아동학대 소재. 실명, 상호, 번호판, 실존 인물 얼굴(기자, 유튜버 썸네일 포함). 실존 인물 입에 없는 말 넣지 않음.
- 조사는 `work/research_<YYMMDD>.md` 에 편별로 사실, 수치, 출처, 법령을 표로 남긴다. 법령은 `casenote.kr`, `nepla.ai`, 공식 보도자료로 확인(law.go.kr 은 JS 라 못 읽음). 확인 안 되면 숫자를 뺀다.

## 1. 대본, 화면 규칙 (어기면 build() 가 assert 로 막는다)

- 생성기는 `_batch_<YYMMDD>.py` 하나로 쓴다. `from _batch_1024 import B, C, L, build, IR, Y, W, R, P` 와 `from _batch_1027 import cap` 를 쓰고 `cap(..., ph=PH)` 로 그날 사진 폴더 `work/_photos/b<YYMMDD>/`(+`map.txt` 에 파일별 출처) 를 넘긴다. 마지막에 `EPS` 리스트와 `if __name__ == "__main__"` 으로 slug 인자 선택 실행(`_batch_1027.py` 끝 부분 그대로).
- 음슴체, 시청자는 "님들". 줄 수 10~12줄 + 마지막 `구독!` outro. **대본 글자 수 합계 370자 이하**(약 10자/초, 40초 미만 필수). 대화체 대사 줄(speaker 2 또는 3) 1줄 이상, 질문형 마무리 댓글 유도.
- `say`(TTS 가 읽는 문장)에는 숫자를 쓰지 않는다: 한글로 푼다. 금액은 `칠마넌`, `백육십팔마넌` 식(마넌 발음), 영어 약자는 발음대로(`비엠`, `에프에스디`). `at` 단어는 `text` 의 부분 문자열이어야 한다. 강조(em) 단어는 text 에 있는 말만.
- 제목 `#키워드 …` **14자 이하**, 위험 단어(죽음, 사망, 폭행, 자살, 살인, 흉기, 참사 등 `schedule_zernio.py` RISKY) 금지. 설명란 = 3줄 + 해시태그만. 고정 댓글 = 님들에게 묻는 질문 1문장. 쇼핑태그 5개 검색어는 upload.md `## 쇼핑태그` 에 적고 업로드 때 붙인다.
- 화면: **원글 캡처 우선**(prd §4-4 "원글 캡처 + 얼굴 모자이크" 행). `cap()` 이 YuNet 으로 얼굴을 찾아 픽셀화한다. 결과 jpg 는 **반드시 Read 로 눈으로 확인**하고 못 잡은 얼굴은 `boxes=[(x,y,w,h)]` 로 추가, 이미 가려진 얼굴도 한 번 더. 번호판이 보이면 같이 가린다. credit 은 "사진: 보배드림", "화면: KNN" 식.
- 캡처가 없는 줄은 GPT 리얼 배경(ai_prompts.tsv, 프롬프트 끝에 "no faces, no text")만 쓴다. **いらすとや 캐릭터는 넣지 않는다**(2026-10-29 사용자 지시 "영상 속 이라스토야 캐릭터 없이, 앞으로 쭉". `_batch_1020.NO_CHAR=True` 가 `ch` 를 무시). 캐릭터가 없으니 배경이 그 줄 장면을 직접 보여줘야 한다: 사람이 필요하면 뒷모습, 손, 실루엣으로.
- 인포그래픽(`Info.tsx`): kinds = quotes, compare, bars, counter. **counter 는 소수점 불가, 1만 이상은 천 단위 반올림** → 소수나 정확한 큰 수는 bars 로. **`flash` 는 True 가 아니라 `at` 처럼 어절 문자열**이어야 한다(아니면 build_v2 가 TypeError).
- `—` 와 `·` 는 어떤 산출물에도 쓰지 않는다. 힉스필드 금지. 이미지 생성은 `~/.claude/skills/codex-image/scripts/gen.sh` 만(아래 러너가 호출).

## 2. 제작 순서

1. 디스크 확인 `df -h /`. 여유 10GB 미만이면 `find ~/.codex/generated_images -type f -mmin +360 -delete` 와 `find ~/.codex/sessions -type f -mtime +7 -delete` 로 비운다. `pgrep -f tts_myvoice` 가 다른 프로젝트(법푸는휴지 daily) 것이면 끝날 때까지 기다린다(TTS 동시 2개는 메모리 초과).
2. 소재 10개 → 조사 md → 사진 다운로드(`work/_photos/b<YYMMDD>/`) → `_batch_<YYMMDD>.py` 작성 → `python3 _batch_<YYMMDD>.py` 실행해 10편 모두 `ok` 가 나올 때까지 assert 를 고친다. 글자 수는 생성기 출력의 chars 로 확인.
3. 큐 파일 `daily/queue_<대상날짜>.txt` 에 slug 10줄 + `END`. 러너 3개를 nohup 으로 띄운다(각각 `</dev/null &`):
   - `nohup python3 daily/img_runner.py daily/queue_<대상날짜>.txt > daily/logs/<대상날짜>_img.log 2>&1 </dev/null &`
   - `nohup caffeinate -i daily/tts_runner.sh $PWD/daily/queue_<대상날짜>.txt $PWD/daily/logs/<대상날짜>_tts.log </dev/null > /dev/null 2>&1 &`
   - `nohup caffeinate -i daily/build_runner.sh $PWD/daily/queue_<대상날짜>.txt $PWD/daily/logs/<대상날짜>_tts.log $PWD/daily/logs/<대상날짜>_build.log </dev/null > /dev/null 2>&1 &`
4. 기다리는 동안 10분마다 로그를 본다(`until grep -q BUILD_DONE <build.log>; do sleep 120; done` 를 timeout 600000 Bash 로 반복). TTS 는 편당 8~15분, 전체 2~3시간.
   - `FAIL <slug>/<key>` 가 img 로그에 남고 IMG_DONE 뒤에도 png 가 없으면 `python3 daily/img_runner.py` 를 그 slug 큐로 다시.
   - `TTS_FAIL <slug>`(같은 줄에서 메모리 폭주 반복): 그 줄의 `say` 를 더 짧은 두 문장으로 고쳐 `python3 _batch_<YYMMDD>.py <slug>` 로 재생성(text 는 그대로, tts 폴더의 만든 줄은 유지), 큐 파일의 `END` 앞에 slug 를 한 줄 더 넣는다(tts_runner 가 이어서 처리). build_runner 는 큐를 처음에 읽지 않고 줄 단위로 읽으므로 같이 따라온다.
   - `BUILD_FAIL <slug>`: `work/<slug>/_build.log` 끝을 읽고 shots 를 고친 뒤 `cd remotion && python3 tools/build_v2.py <slug> --render && cp ../work/<slug>/<slug>_v2.mp4 ../work/<slug>/<slug>.mp4`.
5. 검수: 편마다 `ffprobe` 길이 40초 미만 확인, `ffmpeg -i <mp4> -vf "fps=1/4,scale=270:-1,tile=5x2" -frames:v 1 sheet.jpg` 로 프레임 시트를 만들어 Read 로 본다(얼굴 모자이크 됐는지, 자막 잘림, 깨진 이미지). 문제 있는 편은 고쳐 재렌더, 못 고치면 뺀다.

## 3. 예약 업로드 (YouTube Studio, chrome-mcp-stdio)

브라우저는 **chrome-mcp-stdio 만**(이 레포 `.mcp.json`, CHROME_PORT 12320). 절차 단일 출처는 `prd.md` §4-2 + `~/Desktop/kim/ssul/docs/upload-workflow.md`(제목, 설명 execCommand, 아동용, 예약 §3-2). 먼저 읽는다.

- **`youtube.com/logout` 절대 열지 않는다.** 란빵은 <관리자 구글 계정> 계정의 브랜드 채널이다. 시작 전에 `youtube.com/account` 에서 활성 채널이 란빵🐣 `@eggbread0` 인지 확인하고, 아니면 거기서 채널 전환. 업로드 URL `https://studio.youtube.com/channel/UCxQK4IBAJ1t-dPImmMinCng/videos/upload?d=ud&authuser=0`.
- 먼저 `python3 schedule_zernio.py --dry-run <slug>=<대상날짜>T12:00 ...` 로 제목 위험 단어, 40초 미만만 검증한다(실제 Zernio 예약은 하지 않는다).
- 한 편씩: `chrome_upload_file`(input[type=file]) → 영상 ID 기록 → 제목, 설명(upload.md 그대로, execCommand) → 아동용 아님 → 다음 → **광고 적합성 `해당 사항 없음` → `평가 제출`** → **동영상 요소의 `제품 태그하기 › 추가` 에서 upload.md 쇼핑태그 5개**(검색창 좌표 클릭, 타이핑, Enter, 결과 텍스트 확인 후 보이는 `ytcp-icon-button`(+) 좌표 클릭, `태그된 제품 5개` 확인 후 `완료`. 검색이 퍼지라 "블랙박스" 대신 "자동차 블랙박스 2채널" 식으로) → 검토 → 공개 상태에서 **예약: 날짜 먼저, 시간 나중**.
- 함정(ssul daily 10/28 실측): 스튜디오 탭이 백그라운드면 달력 칸이 0개로 잡히고 스크린샷이 타임아웃 → 날짜 고르기 전에 `chrome_switch_tab` 으로 앞에 띄운다. 시간 항목(`TP-YT-PAPER-ITEM`)은 shadowRoot 까지 훑어 textContent 로 찾아 `.click()`, 남은 backdrop 때문에 날짜 트리거 첫 클릭이 먹힐 수 있으니 한 번 더. `#done-button` 뒤 `document.body.innerText` 에 "동영상 예약됨 YYYY년 M월 D일 HH:MM" 이 있는지로 확인하고, **타임아웃이 나도 재업로드 전에 Studio 콘텐츠 목록에서 같은 제목이 있는지 먼저 본다**(중복 업로드 방지).
- 고정 댓글은 예약 상태에선 못 단다. upload.md 의 질문 1문장은 그대로 두고, 공개 후 사람이 단다(마지막 출력에 안내).
- 칸 배정: 돈 피해 소비자 썰이나 판결 편을 12:00 과 19:00 에, 신차는 13:00 과 20:00 근처, 용품은 14:00 또는 21:00. 대상 날짜 슬롯 중 Studio 에 이미 예약된 칸(콘텐츠 목록)은 건너뛴다.
- 한 편이 3번 실패하면 그 편은 건너뛰고 다음 편.
- 기록: `ssul/docs/used-sources.md` 에 `- slug [란빵] | 출처 URL | #제목 | 대상날짜 HH:MM Studio 예약 영상ID`, `daily/log.tsv`, `prd.md` §5 기록에 날짜 1줄(편 목록, 사고, 배운 것).
- 끝나면 `work/<slug>/tts/raw_*.wav` 와 `work/<slug>/tts/_sil_*.wav` 는 지운다(mp4, script.json, upload.md, v2/ 는 남김).

## 4. 마지막 출력

표로 `슬롯 | slug | 제목 | 길이 | 영상ID | 쇼핑태그 수` 10줄, 건너뛴 편과 이유, 고정 댓글은 공개 후 수동 안내, 디스크 여유.
