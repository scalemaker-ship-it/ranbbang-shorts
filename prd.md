# 란빵 자동차 썰 쇼츠 — PRD

> 2026-09-15 신설. **2026-09-24 `ssul/ranbbang/` → `shorts/ranbbang/` 으로 이전**(란빵 채널 자료는 shorts 쪽에 모음). `ssul/` 의 썰쇼츠 제작 파이프라인(대본·이미지·TTS·렌더·조립)을 그대로 쓰되,
> **업로드 계정과 소재 범위만 다른** 서브 프로젝트다. 이 문서가 란빵 썰쇼츠의 단일 출처다.

## 1. 계정

| 항목 | 값 |
|---|---|
| 채널 | **란빵🐣** `@eggbread0` |
| 채널 ID | `UCxQK4IBAJ1t-dPImmMinCng` |
| URL | https://www.youtube.com/channel/UCxQK4IBAJ1t-dPImmMinCng |
| 기존 용도 | 쇼핑쇼츠 (`shorts/`, 매일 19:00 예약 1편, 유튜브 쇼핑 태그) — 시청층 남성 74.6%·25~54세 |

썰푸는휴지(`@ssulltissue`, `ssul/prd.md`)와는 **다른 계정**이다. 업로드 시 계정을 반드시 확인한다.

## 2. 소재 — 자동차 관련 썰만 (+ 2026-10-05 기본 운전 상식)

란빵 채널에는 **자동차 썰만** 올린다. 다른 주제(심리·정책·국뽕 등)는 썰푸는휴지로.

- 자동차 사고 (블랙박스 사고·보험 분쟁·과실 비율 논란)
- 운전 빌런 참교육 (보복운전·끼어들기·주차 빌런 → 법조항·사이다 결말)
- 신차 출시 정보 (국산·수입 신모델, 가격·제원, 반응)
- 그 외 자동차 커뮤니티에서 터진 썰 전반 (정비·중고차·주유·전기차 등)
- **기본 운전 상식**(2026-10-05 사용자 지시): 타이어·김서림·배터리·와이퍼·빗길 감속처럼 누구나 겪는 상황 → 원리 → 방법. 원글이 없으니 흰 바 댓글 수(`bar_count`)는 비우고, 근거는 법령·매뉴얼·공단 안내. **쇼핑태그와 직결되는 소재**(공기주입기·김서림방지제·점프스타터·와이퍼)를 우선한다. 생성기 `_batch_1005.py`

채널 시청층(남성 25~54세)과 맞는 소재 우선. 형식은 `ssul/docs/script-guide.md` 의
F형(법조항 사이다)·E형(찬반 저울)·D형(뉴스 반전)을 그대로 쓴다.

## 3. 제작

> 편집 버전: `ssul/docs/edit-versions.md` — 버전1(기존)/버전3(10/10 Remotion, 기본). 사용자가 지정.

> **2026-10-09 사용자 지시 — 쇼츠 목소리 교체(롱폼은 이슬 tts_myvoice 유지): 휴지·란빵 쇼츠 = 이슈쿠키 목소리(GPT-SoVITS 세트 `issuecookie_1009`).**
> 설치 `~/Desktop/kim/issuecookie-voice`(github rudah77-png/issuecookie-voice, `./setup.sh`). 쇼츠 `pipeline/tts.py` 가
> 없는 문장을 `pipeline/tts_issuecookie.py` 로 먼저 채운다(타입캐스트로 되돌리기: `TTS_ENGINE=typecast`).
> 나레이션 01_narr_normal(줄 `"tone"` 으로 absurd·surprise·angry·sarcastic·serious), 여성 대사·아웃트로 12_female,
> 남성 대사(`sub2`) 감정→07/08/09 인물. 숫자는 `num_ko` 가 한글로 바꿔 읽는다(직접 쓰려면 줄 `"say"`).


`ssul/pipeline/` 명령을 그대로 사용한다. **실제 작업 폴더는 `shorts/ranbbang/work/<slug>/`**, 완성본은 `shorts/ranbbang/완성/`.
`ssul/pipeline` 은 경로가 `ssul/work/<slug>` 고정이라, 새 편은 `shorts/ranbbang/work/<slug>` 를 만들고
`ln -s ~/Desktop/kim/shorts/ranbbang/work/<slug> ~/Desktop/kim/ssul/work/<slug>` 로 링크한 뒤 파이프라인을 돌린다.
화면 규격·나레이션(민욱 1.3배속)·대사(소예/중현)·"구독!" 아웃트로·이미지 10장 이상·BGM 등
현행 표준은 `ssul/prd.md` 상단 표를 따른다.

## 3-1. 워터마크 없음

란빵 편은 `@썰푸는휴지` 워터마크를 찍지 않는다(2026-09-16 사용자 지시). `script.json` 의 `"style": { "watermark": "" }` 로 끈다(`render.py` 가 이 키를 읽어 `layout.py` 기본값을 덮어쓴다). 새 편마다 반드시 넣는다.

## 4. 발행 규칙 (2026-09-16 확정, 2026-09-26 하루 6편, 2026-09-29 시각 개정, **2026-10-05 하루 10편**)

| 항목 | 값 |
|---|---|
| 편수 | **하루 10편** (2026-10-05 사용자 지시 "휴지처럼 똑같이 하루 10개", 10/6 슬롯부터. 이전 하루 6편) |
| 시각 | **12:00 / 12:30 / 13:00 / 13:30 / 14:00 + 19:00 / 19:30 / 20:00 / 20:30 / 21:00 KST** (2026-10-05, 법대로해드림과 같은 10칸). 이전: 12:00 / 13:00 / 14:00 + 19:00 / 20:00 / 21:00 KST (2026-09-29 사용자 지시, 10/3 슬롯부터 적용 — 10/2까지는 이전 12:00/12:30/13:00/20:00/20:30/21:00 로 이미 예약됨). 이미 예약된 건 손대지 않고 빈 칸부터 채운다(Zernio `GET /posts?status=scheduled` + `work/_zernio_log.json` 대조) |
| 쇼핑 태그 | **모든 영상 필수, 편당 5개** (2026-09-30 사용자 지시 — 이전 '관련 제품 있을 때만' 폐기). 소재와 직결된 제품이 없으면 운전자 공용 차량용품(블랙박스·차량용 방향제·핸드폰 거치대 등)으로 채운다. Studio 수동(§4-2), Zernio 예약분은 공개 후 |
| 고정 댓글 | 썰푸는휴지와 동일 — 질문형 |

`upload.md` 에 `## 쇼핑태그` 항목을 두고 검색어(예: "블랙박스", "차량용 무선청소기")를 적어둔다. `없음` 은 쓰지 않는다(2026-09-30).

## 4-1. 소재 출처 (제안, 2026-09-16)

우선순위 순. 형식은 F형(법조항 사이다)이 기본이라 **"규정 하나 + 진상 상황"** 이 잡히는 곳 위주.

1. **보배드림 베스트글** `bobaedream.co.kr/list?code=best` — 블랙박스 사고·빌런·과실비율 논쟁의 본산. 댓글 많고 찬반 갈림. 원글 본문 충실(§4-2), 영상 캡처는 안 쓰고 재연 생성
2. **개드립 인기글 중 자동차 태그** — 기존 파이프라인 그대로(5시간 내·댓글 50+), 자동차·운전 글만 거른다
3. **경찰청·국토부·손해보험협회 보도자료** — 단속 신설·과태료 인상·보험 규정 개정. F형 ④ 법 조항의 1차 근거. 예: 보복운전 벌점 100점, 경상환자 4주 룰, 갓길 드론 단속
4. **신차 출시** — 현대·기아·제네시스·수입사 뉴스룸 + 오토뷰·모터그래프 시승 반응. 형식은 D형(반전) 또는 E형(찬반 저울: "이 가격에 살 사람?"). 쇼핑태그 없음
5. **한문철TV 류 사고 영상** — 영상·캡처는 절대 안 쓴다. 사건 구조만 참고해 재연 생성으로
6. **해외 블랙박스 영상 모음(2026-09-28 사용자 지시, §4-3)** — 국내 블박은 여전히 금지, 해외 틱톡 블박은 가져다 쓴다

중복 대조는 `ssul/docs/used-sources.md` 를 같이 쓴다(계정이 달라도 같은 소재 두 번 안 만든다).

## 4-2. 업로드 절차 (Studio, 2026-09-16 실측)

브라우저 = chrome-mcp-stdio. **란빵은 <관리자 구글 계정> 계정의 브랜드 채널**(관리자)이라
`youtube.com/account` 에서 채널 전환하면 된다. `authuser=1`(thestudy9193) 은 권한 없음.
업로드 URL: `https://studio.youtube.com/channel/UCxQK4IBAJ1t-dPImmMinCng/videos/upload?d=ud&authuser=0`
(`ssul/docs/upload-workflow.md` 의 제목·설명·아동용·예약 절차 그대로 + 아래 두 가지)

- **제목 위험 단어 금지 (2026-10-13 사용자 지시)**: 죽음·자살·사망·폭행 류(숨진·살인·살해·폭력·흉기·참사 등) 단어는 제목에 **항상** 넣지 않는다. 사망사고 소재라도 "돌진·사고·처벌" 같은 말로 바꾼다. `schedule_zernio.py` 의 `RISKY` 가 예약 직전에 막는다.

- **광고 적합성** 단계가 끼어 있다: `해당 사항 없음` 체크 → `평가 제출` → 다음
- **쇼핑태그는 업로드 흐름 안 "동영상 요소" 단계의 `제품 태그하기 › 추가`** 에서 붙인다.
  검색창(`#search-input`) 좌표 클릭 → 타이핑 → Enter. 검색이 퍼지라서(블랙박스 → 초콜릿박스)
  결과 텍스트로 골라 **`ytcp-icon-button`(+) 을 좌표 클릭**해야 붙는다(JS `.click()` 은 무시됨).
  보이는 요소만 잡을 것(숨은 중복 리스트가 있음). `태그된 제품 N개` 로 확인 후 `완료`.
- **이미 공개된 영상(Zernio 예약분 등)에 나중에 붙일 때** (2026-09-29 실측): `studio.youtube.com/video/<id>/edit` → 설명란 아래 `#products-description-button`("제품") 좌표 클릭 → 펼쳐진 툴바의 연필 `#shopping-toolbar-edit` 좌표 클릭 → 같은 `제품 태그하기` 대화상자. 검색창은 값이 누적되니 `select()` 후 Backspace 로 비우고 새 검색어. `완료` → 우상단 `저장` → 토스트 "변경사항이 저장됨". 새로고침 후 버튼 문구가 `태그된 제품 N개` 면 반영된 것.
- 예약 시각은 **날짜 먼저, 시간 나중**(순서 바꾸면 "미래의 시간을 선택하세요" 오류). 12:00 슬롯이 지났으면 그날은 20·21시만.

## 4-3. 해외 블랙박스 모음 포맷 (2026-09-28 신설)

"눈길 사고 → 눈길 운전 조심해야 하는 이유" 처럼 **주제 하나 + 해외 블박 사고 영상 3~4개**를 보여주는 포맷.

- **소재는 전부 해외 영상이어야 한다(2026-09-28 사용자 지시). 국내 영상은 한 컷도 섞지 않는다.** 틱톡 메타 `region`(tikwm) + 화면 단서(mph 계기판·영문 표지판·우측통행·지명 캡션)로 확인하고, 라벨에 나라를 적는다.
- 소재: 틱톡 `pipeline/2_search.py`(영문 키워드) → `2_download.py --contact` 로 콘택트시트 검수. **중국어·영어 화면자막이 영상 영역 위에 박힌 건 제외**, 위아래 검은 띠에만 제목이 있으면 영상 영역만 crop 해서 쓴다. 리액션(얼굴 PIP)·뉴스 티커·AI 생성 영상(날짜+지명 캡션 계정 drivewithme·kiddycatworld·curiousbastardss 등) 제외.
- 화면: 상단 2줄 타이틀(잘난체, 흰+노랑) / 가운데 1080x810 블박 박스(4:3 오버스캔 크롭, 배경은 같은 영상 블러) / 박스 좌상단 노란 CASE 칩 / 아래 나레이션 자막(1줄 순차).
- **하단 나레이션 자막 = 부크크고딕 Bold 64px(`~/Library/Fonts/BookkGothic_Bold.ttf`), 자간 0**(2026-09-28). **쇼츠 데드존 회피**: 하단 y>1500(채널명·설명)·우측 x>940(버튼 열)에 글자 금지 → 박스 y=480, 자막 y=1330·최대폭 780, 팝업 중심 y=1400.
- **편당 영상 3개**(2026-09-28 사용자 확정). **지역명(나라·주·도시) 언급 금지 — 나레이션·자막·라벨 모두.** 빨간 지역 라벨도 없음. 아웃트로 배경은 새 소스 대신 CASE 영상의 사고 장면 슬로우 리플레이(`slow`).
- 오디오: **원본 음성 안 씀**(영어 욕설·대화). 태섭 나레이션 1.25배속 + BGM 덕킹.
- **"결국?!" 은 필수 아님 — 사고 직전 팝업은 감탄사·의성어로 클립마다 다르게**(2026-09-28 사용자 지시): "헉!?"·"에에~?"·"어어어?!" 등, 쾅 팝업도 "쾅!!"·"콰광!!"·"쿵!!" 섞기. spec 의 `gasp`·`boom`(너무 짧게 읽히는 "헉" 은 `gasp_tts`="허억!?").
- 대본(2026-09-28 v2 사용자 지시): **영상 자체를 설명하는 반말 수다체.** 클립마다 `상황 설명("새벽 3시 출근길, 눈길이 엄청 미끄러운데…")` → **(두둥) "결국?!"** → **사고 순간(쾅 + 화면 흔들림 + 흰 플래시)** → `사고 설명("미끄러지면서 내 차선으로 들어와서 쾅!")`. 마지막 아웃트로에 교훈("눈 올 땐 브레이크도 살살") + 국내 법 근거 1개 + 질문형 CTA.
- 연출: 효과음(두둥·쾅·휙, ffmpeg 합성) + 자막 여러 종류(상단 고정 타이틀 / 흰 나레이션 자막 `*키워드*` 노랑 / 큰 팝업 "결국??!"(노랑)·"쾅!!"(빨강) 3단 크기 팝 / CASE 번호 칩 / 지역 라벨). **팝업은 박스 아래 자막 자리(POP_Y)** — 박스 가운데 두면 사고 장면을 가린다.
- 클립 타이밍은 원본의 **사고 순간(impact 초)** 에 맞춰 역산한다(`impact`·`lo`·`hi` 로 자막 박힌 구간 회피, 모자라면 첫/끝 프레임 정지). 사고 순간 없는 사후 현장 영상은 이 포맷에 안 맞는다.
- 생성기: **`_ep_dashcam.py <slug>`** — `work/<slug>/spec.json`(title·outro_chip·clips[file·crop·impact·lo·hi·setup·after·origin]·outro[file·crop·ss·slow·lines])만 쓰면 된다. crop 은 흐린 배경·위아래 글자 띠를 뺀 영상 영역, 사고가 화면 가장자리면 crop 을 그쪽으로 치우친다(4:3 박스라 좌우가 잘림). 설명 문장이 길어 impact 보다 길면 첫 프레임이 멈추니 문장을 줄인다. 소재 출처 URL 은 upload.md 근거표에만. (`_ep_snowcrash.py` 는 1편 원본)

## 4-4. 편집 규칙 — 버전1 / 버전2 (2026-10-10 사용자 지시로 구분)

| 버전 | 기간 | 엔진 | 한 줄 요약 | 상태 |
|---|---|---|---|---|
| **버전1 (v1)** | ~2026-10-09 (yamujin 이전 모든 편) | ssul PIL 파이프라인 `render.py`·`build.py` | 가로 이미지 넘김 슬라이드쇼 + 문장마다 전환 효과음 | 보관 — 말이 없으면 쓰지 않음 |
| **버전2 (v2)** | 2026-10-10~ (yamujin·teslatak) | Remotion `shorts/ranbbang/remotion/` | 줌·펀치인 컷 + 강조 효과음 + 인포그래픽 + 실사·리얼 AI 혼합 | **현재 기본** |

"버전1로" 라고 하면 아래 v1, 말이 없으면 v2. 두 버전 모두 **대본·TTS(이슈쿠키 목소리, 금액 마넌 발음)·타이틀·자막 모양·배속 1.2·워터마크 없음은 같다.**

### 버전1 (v1) — PIL 슬라이드쇼 (~2026-10-09)

| 항목 | 규칙 |
|---|---|
| 조립 | `ssul/pipeline/render.py <slug>` → `build.py <slug>` (ffmpeg), 결과 `work/<slug>/<slug>.mp4` |
| 타이틀·자막 | 잘난체 고딕 2줄(흰/`#FBFF56`)·첫 문장 흰 바 / `sub_box` 검은 박스 자막·을지로체 강조 — v2 와 같음 |
| 이미지 | 문장마다 1장(`script.json` `img` 번호), **10장 이상 가로 1280x800**(`prompts.tsv` → `gen_batch.sh`), 실사는 `burn()` 으로 출처 우상단 번인 |
| 움직임 | 이미지 넘김 위주(줌·펀치인·클로즈업 컷 없음) |
| 효과음 | 줄마다 `"sfx": whoosh·dudung·pop` — **슬라이드 넘어갈 때 소리**, 흔들림 `shake` |
| BGM | `ssul/assets/bgm.mp3`(8비트 루프, 2026-09-29 교체분) |
| 배속 | `layout.SPEED` 1.2 |
| 대표 편 | `yamujin_v1.mp4`·`tmaproute`(v1 그대로 보관, 다시 만들지 않음) |

**v2 로 바꾼 이유(2026-10-10 사용자):** 이미지 넘김 + 전환음이라 밋밋함 → 레퍼런스 한입썰(youtube.com/shorts/AoAK3YS2I8c)처럼 "영상처럼".

### 버전2 (v2) — Remotion (2026-10-10 사용자 확정, 이후 모든 란빵 썰 편 기본)

> 파일럿 `yamujin`(삼성 야무진, 10/13 12:00 예약) 승인 후 "앞으로 이 편집규칙으로" 확정. 레퍼런스 = 한입썰 youtube.com/shorts/AoAK3YS2I8c.
> 기존 PIL 파이프라인(`ssul/pipeline/render.py`·`build.py`)은 **대본·TTS 까지만** 쓰고, 영상 조립은 아래 Remotion 으로 한다.

| 항목 | 규칙 |
|---|---|
| 타이틀 | **기존 란빵 그대로** — 잘난체 고딕, 1행 흰/2행 `#FBFF56`, 검정 외곽선, 자간 -1, 두 줄 같은 크기(좌우 80px), 세로 배치 `layout.py` 값. 첫 문장 동안 흰 바(`style.bar`) |
| 자막 | **기존 란빵 그대로, 애니메이션 없음** — `render.py` sub_box 함수로 그린 정지 PNG(잘난체·검은 박스·이미지 안쪽 하단, 강조 = script.json `em`/`em_color` 을지로체). 덩어리·시간 = `subs.chunk`·`split_duration` |
| 배속 | `layout.SPEED`(현재 1.2) |
| 길이 | **40초 미만**(2026-10-16 사용자 "앞으로 영상은 40초 이내로"). 대본 단계에서 줄 수를 줄여 맞춘다(배속은 1.2 유지). 10/15 배치 16편 중 8편이 40~46초였음. `schedule_zernio.py` 가 40초 이상이면 예약을 막는다 |
| 컷 | 문장당 2~3컷, 평균 1.3~1.5초. 모든 컷 켄번즈 확대/축소, 강조어에서 **펀치인**(1.0→1.16, 6프레임), 같은 사진 **클로즈업 컷**(배율 1.6~1.9 + 초점) 섞기. 컷 사이 하드컷 |
| 이미지 | **캡처(실사) + AI 이미지 혼합.** AI 는 실제 사진처럼 리얼하게(스마트폰 캔디드 톤), **대본 그 장면 자체**를 그린다(예: 과적 → 배추를 2배로 쌓은 1톤 트럭). 편당 AI 12~15장 + 실사 2~4장. 실사는 박스 비율(9:8)로 미리 크롭, 출처는 컷 우상단(흰 바 떠 있으면 그 아래). 생성은 `gen.sh`(luna) 만 |
| **원글 캡처 + 얼굴 모자이크** | **(2026-10-27 사용자 지시 "사진이 있다면 캡처해서 활용하고, 얼굴이 있다면 모자이크")** 원글(보배드림·개드립·기사)에 사진·영상이 있으면 **캡처를 우선 쓴다**(첨부 사진, 기사 화면, 본문 영상 정지 프레임). 사람 얼굴은 **모자이크(픽셀화)** 하고 쓴다: `tools/mosaic.py`(YuNet 얼굴 검출 + `--box` 수동 영역, 모델 `tools/models/`) 또는 생성기의 `cap(slug, name, src, box, cx, cy, fit, boxes)`(`_batch_1027.py`, 크롭→모자이크→1080x960, `fit=True` 는 글자 캡처용 블러 배경). 검출 결과는 반드시 눈으로 확인하고 못 잡은 얼굴은 `boxes` 로 추가. 원글이 이미 가린(PutMask·블러) 얼굴도 한 번 더 모자이크. **실존 유명인·기자 얼굴 썸네일(김한용 MOCAR 등)은 모자이크해도 안 쓴다**(인물 특정). 번호판은 원글이 가린 상태 그대로, 안 가려졌으면 같이 가린다. 출처 credit = "사진: 보배드림" / "화면: KNN" 처럼 컷 우상단. 원본은 `work/_photos/b<날짜>/` + `map.txt`. 이 규칙이 §4-1 의 "영상 캡처는 안 쓰고 재연 생성" 보다 우선한다 |
| 효과음 | **강조 지점에만**(숫자·반전·충격·결론), **컷 전환음·문장 시작 휙 금지.** (2026-10-11) 소리는 **이슈쿠키 효과음 라이브러리** `ssul/assets/sfx/issuecookie/`(141개, 번호표 `_목록.txt`·`index.json`, 원본 `~/Downloads/_샘플러.m4a` 에서 잘라 피크 -1dBFS) — shots.json `sfx: [[파일이름, "어절"(, 볼륨 기본 0.5)]]`. 예전 짧은 이름(boom·hit·ding·sting·crack·pop·cash)은 라이브러리 곡으로 연결, 예전 합성음은 `"synth:<이름>"`. **[표기 필요] `cash_register`·`heart_heavy` 는 쓰지 않는다**(빌더가 막음). 장면에 맞춰 고른다: 말풍선 = notify_message_pop, 틀린 주장 = wrong_gameshow_buzz, 숫자 공개 = drop_futuristic(+막대 차오를 때 riser_simple), 충격 사실 = hit_trailer_epic, 사고 = glass_smash, 돈 = cash_register_fake·count_counter, 카드 넘김 = swipe_card, 황당 = drum_rimshot·scratch_vinyl (예시 work/teslatak/v2/shots.json) |
| 팝 글자·흔들림 | 결정타 1~3곳만 — 큰 글자("과적!!" 빨강 등) + 화면 흔들림 10프레임. 팝은 그 문장 안에서 끝낸다 |
| 인포그래픽 | (2026-10-10 추가, teslatak 첫 적용) 숫자·비교·흐름이 나오는 문장엔 `remotion/src/Info.tsx` 오버레이 — **quotes**(말풍선)·**flow**(돈·계약 화살표)·**compare**(두 카드 VS)·**bars**(막대 카운트업, flash=빨강 강조)·**counter**(금액 카운트업). shots.json 줄에 `"info": {kind, at:어절, span, title, sub, items[{at:어절 또는 "+1:어절"}]}`. 편당 3~5개, 이미지 위 어둡게 깔고 자막 위로는 안 올림 |
| 소리 | 나레이션 + BGM 0.09 + 효과음 → 렌더 후 loudnorm **-15 LUFS** |
| BGM | (2026-10-10 확정) 기본 = **`ssul/assets/bgm/sneaky-123.mp3`** — 레퍼런스 youtube.com/shorts/2C3s9NbeLcc 배경음 분석(D단조·123BPM·피치카토/마림바 살금살금)으로 `remotion/tools/bgm_sneaky.py` 가 코드 합성(라이선스 무관). 편마다 바꾸려면 shots.json `"bgm": "bgm/<파일>"`(-26 LUFS 로 자동 정규화) |
| **리얼 배경 + いらすとや 캐릭터 (2026-10-29 폐지)** | **2026-10-29 사용자 지시 "영상 속 이라스토야 캐릭터 없이, 앞으로 쭉": 캐릭터를 넣지 않는다.** `_batch_1020.py` 의 `NO_CHAR = True` 가 `ch` 와 아웃트로 캐릭터를 무시하고, 배경이 장면을 직접 보여준다(사람은 뒷모습, 손, 실루엣). 아래는 이전 규칙. **(2026-10-20 사용자 지시 "배경은 지피티 현실 느낌, 그 앞에 이라스토야 캐릭터")** 배경 = gen.sh(luna) 실사풍 장면, **사람 없는 빈 배경**으로 그린다(캐릭터가 주인공). 그 앞에 いらすとや 누끼(흰 테두리)가 박스 아래 변에 서서 튀어오른다: shots.json 줄 `"char": [{"name","side":"l"|"r","h","at","flip"}]`, 파일 `v2/ir/ir_<name>.png`, 같은 캐릭터가 이어지면 다시 안 튐(`RanbbangShort.tsx` CharView). **줄마다 캐릭터 1개, 한 편 20장 이하**(いらすとや 무료 조건). 받기 = `remotion/tools/ir_rb.py search/get`, 카탈로그(운전하는 남자 car_man01~12·정장 남자 business_man 12표정 등) = `_batch_1020.py` 의 `IR`, 원본 모음 `work/_ir_pool/`. 신차 편의 차 화면은 그대로 제조사 공식 사진/영상 정지 장면(AI 금지). 생성기 `_batch_1020.py`(보배드림)·`_batch_1020b.py`(신차·용품) |
| **대화체 1문장** | **(2026-10-16 사용자 지시 — "중간에 한 문장씩 대화체" 이전 지시가 10/5~10/15 배치에 하나도 적용 안 됐음)** 모든 편 대본 **중간에 대화체(대사) 줄을 최소 1문장** 넣는다 — 등장인물이 실제로 한 말처럼 따옴표 대사("아니 이걸 왜 제가 내요?" 류). script.json 줄에 `"dialogue": true, "speaker": 2`(또는 3) + `emotion` — 나레이션이 talk1 이라 speaker 1(기본)이면 목소리가 안 바뀐다 → 목소리가 바뀌고 자막도 을지로체 하늘색 `#7EC8FF`. 대사 줄엔 `em` 금지. 예시 형식 `ssul/work/abandoncar/script.json`. _batch 생성기에 `assert any(l.get("dialogue") for l in lines)` 가드를 넣는다 |
| 금액 | 자막은 붙여 씀 "20만원", 발음은 무조건 연음 "이십마넌" — `ssul/pipeline/tts_issuecookie.py` num_ko 가 만원→마넌·천원→처넌·백원→배권·억원→어권 자동 변환 |

**명령**
```
# ① 대본·TTS 는 기존대로 (_batch_*.py → ssul/pipeline/tts.py <slug>)
# ② work/<slug>/v2/ai/*.png  (gen.sh, --orientation square 1080x1080) · v2/real/*.jpg (1080x960 크롭)
# ③ work/<slug>/v2/shots.json — 문장(lines, script.json 순서·'구독!' 포함)마다 shots/sfx/pop/shake 지정 (예시: work/yamujin/v2/shots.json · 인포그래픽·bgm 예시: work/teslatak/v2/shots.json)
cd shorts/ranbbang/remotion && python3 tools/build_v2.py <slug> --render   # → work/<slug>/<slug>_v2.mp4
# ④ 검수 후 <slug>.mp4 로 복사 → schedule_zernio.py <slug>=<시각>
```
엔진 = `shorts/ranbbang/remotion/`(`src/RanbbangShort.tsx`, node_modules 는 `ssul/templates/2` 링크 — 공유본 파일은 수정하지 않음). 편 소재는 `remotion/public/<slug>/`(gitignore).

## 4-4-1. 하루 10편 자동 제작 (2026-10-28 사용자 지시 "매일 오후 3시에 영상 10개 만들어서 업로드 예약")

- launchd `com.scalemaker.ranbbang-daily10`(`~/Library/LaunchAgents/`) 이 **매일 15:00 KST** 에 `open -a Terminal daily/run_daily.command` 로 `daily/run_daily.sh` 를 실행(launchd 의 zsh 는 macOS TCC 로 Desktop 을 못 읽어 Terminal 경유, 2026-10-29) → `caffeinate -i claude -p "$(cat daily/PROMPT.md)" --permission-mode bypassPermissions` 헤드리스. **대상 = 다음 날 10칸**(12:00~14:00, 19:00~21:00). 제작이 2~3시간 걸려 당일 칸은 못 맞추기 때문.
- 소재 비율: 보배드림 소식 5~6, 신차 2~3, 용품 1~2(인기순, 없으면 다른 종류로). 용품은 틱톡 편집형이 아니라 v2(공식 이미지 캡처, 캐릭터 없음). 규칙 전체 = `daily/PROMPT.md`(단일 출처).
- 러너: `daily/img_runner.py <queue>`(gen.sh 동시 5), `daily/tts_runner.sh <queue> <log>`(16GB 넘으면 재시작, 같은 줄 5회 막히면 TTS_FAIL), `daily/build_runner.sh <queue> <tts.log> <build.log>`. 큐는 `daily/queue_<날짜>.txt`(END 앞에 줄 추가 가능). 기록 `daily/log.tsv`(날짜, 슬롯, slug, 영상ID), 로그 `daily/logs/<날짜>*.log`.
- 수동: `./daily/run_daily.sh`(FORCE=1 강제, TARGET_DATE=YYYY-MM-DD). 중지: `launchctl bootout gui/$(id -u)/com.scalemaker.ranbbang-daily10`.
- **예약은 Zernio 가 아니라 chrome-mcp-stdio 로 YouTube Studio 예약 업로드**(2026-10-29 사용자 지시 "크롬 mcp로 해"). 업로드 흐름 안에서 쇼핑태그 5개까지 붙인다. `schedule_zernio.py` 는 `--dry-run` 검증(위험 단어, 40초)에만 쓴다. 고정 댓글은 공개 후 수동.
- 한계: 맥이 15:00 에 깨어 있고 Chrome(포트 12320 확장)이 켜져 있어야 한다. 15:00 에 Terminal 창이 떠 2~3시간 열려 있으니 닫지 말 것. 법푸는휴지 daily(02:00)와 TTS 가 겹치면 기다리도록 프롬프트에 넣음.

## 4-5. 커뮤니티 게시글 (2026-10-16 신설)

| 항목 | 규칙 |
|---|---|
| 신차 출시 소식 | **매일 1개** — 최근 국내 출시·공개 신차 뉴스. 사진은 제조사 공식 보도사진만(구글·방송·언론 워터마크 금지), 출처를 카드 우상단에 굽는다. 수치는 출시 당일 보도 2곳 이상 교차확인 |
| 운전상식·초보운전 꿀팁 | **주 2개만** (신차 뉴스와 별도 트랙, 추천 화·금) |
| 카드 | **1080x1080 5장 정도** — 표지(후킹 2줄)·가격/핵심표·성능·실내/제원·질문(댓글 유도). 잘난체 제목 + Pretendard 본문 + 연두 `#BEFF3C` 강조 |
| 본문 | 이모지 소제목 + 핵심 수치 + 마지막 질문 + 출처 한 줄 |
| 게시 | Zernio 는 커뮤니티 게시글 미지원(확인 안 됨) → chrome-mcp 로 `youtube.com/@eggbread0/posts` 작성창. 본문은 `#contenteditable-root` 에 `execCommand('insertText')`. **이미지: 첫 장은 '이미지' 버튼 → multiple input, 2장째부터는 dialog 안 multiple=false input 에 한 장씩**(multiple input 에 다시 올리면 기존 사진을 교체함). 게시 후 새로고침해 `ytd-backstage-image-renderer` 수 = 카드 수 확인 |
| 폴더 | `work/post_<MMDD>_<slug>/` — `make_cards.py`·`post.md`·`card*.jpg` 커밋, 원본 `src_*` 는 커밋 안 함 |

## 4-6. 신차 공개 영상형 대본 구조 (2026-10-16 사용자 지시 "이 대본구조 저장해줘")

> 기준 편 = `roadster26`(테슬라 로드스터 2세대 공개, zEKr2X0-C6s, 37.8초). 생성기 `_batch_1016b.py` 를 복사해 쓴다.
> 신차/신기술 **공개 행사 뉴스**에 쓴다. 화면은 제조사 공식 영상 클립(§4-4 v2 의 `"vid"` 컷), 출처 "영상: 제조사" 우상단.

| # | 역할 | 형식 | 예시(roadster26) | 화면 |
|---|---|---|---|---|
| 1 | **반응 대사 훅** | 구경꾼 탄성 대사 1줄(`dialogue`, `speaker: 3`), 2초 안 | "와우, 대박인데?" | 영상에서 제일 센 장면 2컷 |
| 2 | 무엇을 공개했나 + 가장 놀라운 점 | "[브랜드]가 [맥락] [차]를 공개했는데, [충격 기능]" + 팝 | "테슬라가 9년 미룬 로드스터를 드디어 공개했는데, 차가 하늘을 날아버림." / 팝 "날았다?!" | 등장 컷 → 기능 컷(펀치인) |
| 3 | 시연 디테일(숫자) | 눈으로 본 장면을 숫자로 | "주차된 차 다섯 대를 그냥 점프해서 넘어가 버림." | 시연 클립 |
| 4 | 비결 1(원리) | "비결은 [기술 출처]로 만든 [부품] [개수]" | "비결은 스페이스X 로켓 기술로 만든 압축공기 노즐 열 개임." | 기술 설명 애니 → 작동 컷 |
| 5 | 시연 2 + 비결 2 | "[믿기 힘든 장면]인데, [부품]이 [역할]" | "거꾸로 선 벽을 타도 안 떨어지는데, 흡입 팬이 차를 바닥에 꽉 붙잡아줌." | 시연 클립 2컷 |
| 6 | 핵심 수치 1개 | 숫자 하나로 끝내기 + 팝 + 효과음 | "시속 97킬로까지 걸린 시간은 고작 0.81초." / 팝 "0.81초!!" | 가속 컷 → 차 정면 |
| 7 | **당사자 발언 대사** | CEO/개발자 실제 발언을 대사체로(`speaker: 2`), 반전 있는 말 | "안전이 최우선인 차는 아닙니다. 대신 재미는 10점 만점에 11점이에요." | 발언자 컷 |
| 8 | **반전 "근데"** | 과거 약속 vs 현실, compare 인포그래픽 | "근데 이거 2017년에 공개하고 2020년에 낸다던 차임." | 차 디테일 컷 + 인포 |
| 9 | 대가를 치른 사람(숫자) | 기다린 사람/돈/기간 + 팝 | "한정판 예약자는 25만 달러를 내고 9년째 기다리는 중임." / 팝 "9년째" | 차 컷 클로즈업 |
| 10 | 새 약속 + 숨긴 것 | "이번엔 [새 약속]이라는데, [핵심 정보]는 또 비공개임." | "이번엔 2028년 양산이라는데, 가격이랑 주행거리는 또 비공개임." | 차 컷 |
| 11 | 질문 CTA | 믿을지 말지 묻기, **고정 댓글과 같은 문장** | "님들은 이번엔 진짜 2028년에 나온다고 봄?" | 마무리 시연 컷 |
| 12 | 구독! | 아웃트로 | | 정지 프레임 |

- 흐름 = **감탄(1~6) → 반전(7~10) → 질문(11)**. 앞 절반은 영상의 볼거리, 뒤 절반은 "근데 믿어도 되냐"로 댓글을 유도한다.
- 대사 줄 2개(1번 구경꾼 speaker 3, 7번 당사자 speaker 2)로 목소리가 세 가지가 된다. 대사 줄엔 `em` 금지.
- 나레이션은 음슴체(~함/~임/~버림), 숫자는 `say` 에 한글로. 40초 미만(12줄 기준 약 38초).
- 타이틀 = "[맥락] [브랜드] 신차 / 결국 [충격 기능]" (예: "9년 미룬 테슬라 신차 / 결국 하늘을 날았다"), 흰 바 = 시연 한 줄 요약.
- 컷이 클립보다 길면 느리게 재생되니, 클립은 컷보다 넉넉히(3~5초) 자른다. 대사 컷은 해당 장면이 끝나기 전에 다음 클립으로 넘긴다.

## 5. 기록

- 2026-09-15: 프로젝트 신설. 란빵 계정 = 자동차 썰 전용으로 확정.
- 2026-09-16: 1편 revengedrive 20:00 (pkxtG-uHHFU), 2편 whiplash4w 21:00 (_BTGeXgSyi4) 예약, 3편 doording 9/17 12:00 예정. codex 한도 소진(9/19 17시 리셋)이라 3편 이미지는 로컬 SDXL.
- 2026-09-17: 자동차 썰 9편(tailgate·jagibudam·school20·avante336·crosswalk·lawsuit4x·gv90·kickboard·evwait) 제작 완료, 완성본은 `shorts/ranbbang/완성/` 에 모아둠. tailgate·jagibudam 2편은 예약했다가 **사용자 지시로 비공개 전환**(공개된 적 없음), 나머지 7편은 미업로드. 이미지는 codex 한도+로컬 SDXL 모델 분실로 **힉스필드 z_image**(장당 0.15크레딧, 114장) 사용.
- 2026-09-16: 발행 12/20/21시 3편·쇼핑태그 규칙 확정. 1편 `revengedrive`(보복운전 급정거 3번 → 특수협박·벌점 100점) 제작. (당시 구조: 실폴더 `ssul/work/<slug>` + `ssul/ranbbang/work` 링크 — 2026-09-24 이전 후 방향 반대로 바뀜, §3 참고)
- 2026-09-25: 추석 5편(triangle·backbelt·daeri5m·lane1·onlyme) 9/25 20:00~22:00, 일반 5편(rightturn·blinker·fineorpoint·drunkhelp·plateseize) 9/26 20:00~22:00 **Zernio 예약**(란빵 워크스페이스 키 `~/.claude/skills/쇼핑쇼츠-업로드/.env`). 예약 도구 = `shorts/ranbbang/schedule_zernio.py <slug>=<시각>`(로그 `work/_zernio_log.json` 으로 중복 차단). 대본 생성기 `_batch_0924.py`. Zernio 예약이라 Studio 에는 공개 시각 전까지 안 보이고, triangle 쇼핑태그(비상삼각대)는 공개 후 수동.
- 2026-09-25: 자동차 이슈 10편 → **점심 12:00/12:30 하루 2편**(9/26~9/30, 저녁 20~22시 슬롯과 별도) Zernio 예약. 생성기 `_batch_0925.py` — 실사(`work/_photos/`, 현대차그룹 뉴스룸 `asset_library` 정적 파싱 + Wikimedia API)를 1280x800 크롭하고 **출처를 우상단**(원본 x≤1141, 1번 컷은 흰 바 아래 y=118)에 굽는다. ⚠️ 우하단은 화면 cover 크롭(원본 x 123~1157만 보임)과 자막 박스에 가려져 안 보인다.
- 2026-09-25: `chuseokjam`(추석 고속도로가 막히는 이유 — 유령 정체) 1편 제작, 생성기 `_ep_chuseokjam.py`, 이미지 로컬 SDXL. 9/25 22:30 Zernio 예약(6ab62fb0faebf14bf0a71dc8).
- 2026-09-26: **발행 리듬 하루 6편(12:00/12:30/13:00 + 20:00/20:30/21:00)으로 변경.** 개드립 자동차 4편 제작·Zernio 예약 — fuel100(9/27 13:00)·evcharge14(20:00)·benz10x(20:30)·taxi28(21:00). 생성기 `_batch_0926.py`. 이미지는 로컬 SDXL + 원글 무얼굴 사진(충전기 앱 화면·벤츠 주차 사진)은 `orig` 로 블러 배경 1280x800 배치.
- 2026-09-26: **첫 롱폼(16:9) `long_carrepair`** — "정비소에서 과다청구 당했다면?"(2:08, 수원지법 2019나63515). 제작은 `ssul/pipeline/long_tts.py`→`long_build.py`, 우상단 이름은 script.json `"channel": "란빵"`. 사용자 지시로 **즉시 공개**(Zernio 19:55, postId 6ab7a2ac1eaf2789ff3dd918, https://www.youtube.com/watch?v=uCYK52RbJi4). 차량 소재 롱폼은 란빵으로 올린다.
- 2026-09-26: **예외 — 비자동차 소재** `bukangi3`(부캉이 부산 특수·밈, 인스타 @yeomi.travel 게시물 기반, 머니투데이·서울신문 확인) 사용자 지시로 란빵에 올림. 워터마크 끔, 23:04 Zernio 즉시 공개(6ab7d0111ab261162fe9c053). 원본은 ssul/work/bukangi3 (여기는 링크).
- 2026-09-26: **해외 노출 설정** — 자동 더빙 허용은 원래 켜져 있었으나 '게시 전에 직접 더빙 검토'를 **껐다**(실험 언어 더빙도 바로 게시). Zernio 업로드분은 **동영상 언어가 비어 있어 더빙이 안 붙고 있었음** → 쇼츠 334개 일괄 수정 '동영상 언어=한국어' 적용, 롱폼은 long_carrepair 만 지정(구채널 롱폼은 노래 영상 섞여 제외). 자동 더빙은 영어 음성 + 영어 제목·설명까지 자동 게시됨(정비소 편 확인). **Zernio 로 새로 올린 편은 언어가 비므로 올린 뒤 Studio 일괄 수정으로 한국어 지정**해야 더빙이 붙는다. 쇼츠는 언어별 썸네일 불가(쇼츠 맞춤 썸네일 업로드 자체 없음·번역 표에 썸네일 칸 없음).
- 2026-09-27: **설명란 규칙 — 출처·근거·AI 고지 문구 금지, 검색용 3줄 + 해시태그 한 줄만**(사용자 지시, 모든 채널). 근거는 upload.md 근거표에만.
- 2026-09-28: **해외 블랙박스 모음 포맷 첫 편 `snowcrash`**(눈길 운전 조심해야 하는 이유, v3 32.7s) — 새벽 출근길·눈 덮인 교차로·눈 쌓인 밤길 3클립(전부 US), 지역명·빨간 라벨 제거. v1(설명형 나레이션)은 사용자 피드백으로 폐기 → v2 영상 설명형+효과음+흔들림. 생성기 `_ep_snowcrash.py`, 완성본 `완성/snowcrash_눈길운전조심해야하는이유.mp4`. 미업로드.
- 2026-09-28: snowcrash **19:09 Zernio 공개**(postId 6aba3c73fc6cc9a262292581, https://www.youtube.com/watch?v=IJZJ7t96Fsg). 같은 포맷 3편(감탄사 버전) Zernio 예약: `rainslide` 10/2 13:00(6aba40b69768a6960f67cce3)·`redlight` 10/2 20:00(6aba410779ef768c67e3b095)·`tailgate2` 10/2 20:30(6aba4159d0b4a49f846a580f). 소재 전부 해외(US 8·CZ 1). 쇼핑태그·동영상 언어(한국어)는 공개 후 Studio 에서.
- 2026-09-29: 공개 후 쇼핑태그 수동 부착 — `triangle`(19-zOZr8gfM) 비상삼각대 4 + 비상망치 겸용 경광봉 1, `snowcrash`(IJZJ7t96Fsg) 2채널 블랙박스 2·스노우체인 2·성에제거 스프레이 1. 둘 다 5개 저장 확인. snowcrash 동영상 언어(한국어)는 아직.
- 2026-09-29: 발행 시각 12/13/14·19/20/21시로 변경(10/3~). 보배드림 10편(`_batch_0929.py`) 대본·TTS 완료, codex 한도 소진(리셋 9/30 10:09)이라 `work/_b0929_after_reset.sh`(caffeinate) 가 리셋 후 이미지→render→build→Zernio 예약(10/3 6편·10/4 4편)까지 자동. 로그 `work/_b0929_after_reset.log`.
- 2026-10-03: 사용자 지정 네이버 블로그 2건 → 신차 2편(`_batch_1003.py`, **이미지 전부 실사**·출처 우상단 번인, 생성 이미지 0). `scout16`(스카우트 트래블러 16만 명·6천만 원대, 사진 scoutmotors.com 공식 사이트 Contentful 원본 8장을 anchor 달리해 15컷) **10/3 01:25 Zernio 즉시 공개**, `glc9000`(벤츠 전기 GLC 9천만 원·사전계약 2천 대, 커먼즈 CC BY-SA 4.0 Alexander-93·Alexander Migl) **10/4 20:00 예약**(10/4 빈 칸 20·21시 중 앞칸). 실사 폴더 `work/_photos/scout/`(map.txt 에 원본 URL)·`work/_photos/glc/`(glc_meta.json 에 저작자·라이선스). 공식 사이트의 webp 는 썸네일 해상도(≤416px)라 못 쓰고 뉴스룸 jpg 만 1920px. 쇼핑태그·동영상 언어(한국어)는 공개 후 Studio.
- 2026-10-04: **자동차 법 6편**(보배드림 베스트 10/4, 생성기 `_batch_1004.py`, 자동 마무리 `work/_b1004.sh`) 10/5 Zernio 예약 — hydrant62 12:00(6ac2133d…)·firstcrash400 13:00(6ac212f4…)·sleepdui 14:00(6ac2135a…)·dump70 19:00(6ac21386…)·repairbill 20:00(6ac213a9…)·crossroad37 21:00(6ac213cd…). 예약 중 Zernio 업로드 BrokenPipe 1회 → `schedule_zernio.py` 재실행으로 복구(로그가 중복 차단). 쇼핑태그·동영상 언어는 공개 후 Studio.
- 2026-10-03: **차량용품 쇼핑쇼츠 파일럿 `rb_scratch`**(제휴 누적 1위 '#자동차기스 마법같이 없애는 방법' 구조 복제: 무나레이션·화면 글자+BGM·"있었는데요/없었습니다"를 실제 전후 컷에 맞춤). v1 `sRy8YhsH4gA` 10/3 23:43 공개(쇼핑태그 미부착). v2 `shorts/work/rb_scratch2/output_v2.mp4`(페이퍼로지 자막·해외 키잉 훅) 미업로드 — v1 처리 방침 사용자 답 대기.
- 2026-10-05: **발행 리듬 하루 10편으로 변경**(법대로해드림과 같은 10칸). 첫 회차 **운전 상식 10편**(생성기 `_batch_1005.py`, 자동 마무리 `work/_b1005.sh`, 업로드 3회 재시도 포함) 10/6 Zernio 예약 — fog1min 12:00·tirepsi 12:30·jumpcable 13:00·treadcoin 13:30·mirrorset 14:00·rainspeed 19:00·downhill 19:30·highbeam 20:00·wiper6m 20:30·fuellight 21:00. 원글 없는 상식 편이라 bar_count 없음. 쇼핑태그·동영상 언어는 공개 후 Studio.
- 2026-10-06: **보배드림 베스트 24시간 자동차 글 10편**(10/5 23:37~10/6 23:37, 베스트 14페이지에서 자동차 게시판·운전 키워드로 거르고 추천·댓글·조회순, 기존 편과 겹치는 우회전 깜빡이·번호판 가림은 제외). 생성기 `_batch_1007.py`, 자동 마무리 `work/_b1007.sh`(로그 `_b1007.log`) → 10/7 Zernio 예약 — tesladeliv 12:00·importins 12:30·dumpplate 13:00·benzac 13:30·dooropen 14:00·raypush 19:00·gatebar 19:30·pokelain 20:00·hwyreverse 20:30·grandeurhev 21:00. 이미지 원본 대부분이 뉴스 캡처·GIF라 사실은 원 보도(MBN·KNN/YTN/MBC 2012·JTBC 2024·현장뷰 영상 설명)로 대조. 쇼핑태그·동영상 언어는 공개 후 Studio.
- 2026-10-07 01시: 공개분 쇼핑태그 일괄 부착 — 10/6 운전상식 10편 + 10/5 firstcrash400·sleepdui·repairbill·crossroad37 각 5개 저장 확인(hydrant62 5개·dump70 6개는 이미 붙어 있어 건너뜀). 영상 ID 는 Zernio `GET /posts/<postId>` 의 platformPostUrl. ⚠️ MCP 작업 창이 다른 창에 가려지면 `visibilityState=hidden` 이 돼 iron-collapse 애니메이션이 안 끝나 연필이 0px 로 남고 스크린샷이 타임아웃 남 → `osascript` 로 해당 Chrome 창을 앞으로 올리면 해결. 완료·저장 버튼은 JS `.click()` 으로 되고, 연필과 + 는 좌표 클릭만 먹힘.
- 2026-10-07 새벽: **최근 40편(10/1 합류사고 ~ 10/6) 쇼핑태그 일괄 점검** — 36편에 5개씩 부착(도로 체인은 1개→5개 보충 포함). 이미 5개 이상: 소화전·덤프70·횡단보도 주차. `sRy8YhsH4gA`(자동차기스 rb_scratch v1)는 Studio 가 `tagging-blocked`("문제 검토")라 부착 불가. 소재 직결 제품이 없는 사고·과실 편은 블랙박스 2종+메모리카드+비상삼각대+경광봉 묶음. ⚠️ 검색이 퍼지라 "2채널 블랙박스"가 오토바이용으로 바뀌기도 함 → "자동차 블랙박스 2채널"/"아이트로닉스 블랙박스"로 검색. 검색어는 JS 로 input 값 넣고 Enter 만 키보드로 보내면 됨.
- 2026-10-07: **운전 상식·교통법 10편**(원글 없음, 생성기 `_batch_1008.py`, 자동 마무리 `work/_b1008.sh`, 로그 `_b1008.log`) 10/8 Zernio 예약 — minspeed50 12:00·inspect60 12:30·roundabout 13:00·wintertire 13:30·rightpass 14:00·tunnellight 19:00·safedist 19:30·idling5 20:00·washer25 20:30·dashsd 21:00. ⚠️ 처음 고른 숙취운전·갓길·하이패스는 썰푸는휴지에서 이미 다룬 소재(sukchwi·gatgil·hipass10)라 교체했고, **슬러그가 `ssul/work/` 의 실폴더와 겹치면 링크가 안 걸려 파이프라인이 썰 편을 다시 돈다**(hipass10·washer TTS 가 재생성됨, 같은 대본이라 내용 동일) → 새 슬러그는 `ls ~/Desktop/kim/ssul/work` 로 먼저 대조할 것. 쇼핑태그·동영상 언어는 공개 후 Studio.
- 2026-10-09: **30편 일괄 제작·예약(10/10~10/12, 하루 10칸)** — 보배드림 베스트 10(`_batch_1010a.py`: taxifare·escalade·hazarddump·g80tower·oilcap·theta2·drunkcop·cornerpark·lanecurve·phonedigit) + 운전 상식·교통법 10(`_batch_1010b.py`: fireext·petlap·leafslip·blackice·license30·lightcar30·uturn6·doublepark·parkdrain·smartkey) + 사고 이슈 뉴스 10(`_batch_1010c.py`: teenrental·oldreverse·workzone·revenge931·pedalmiss·fsd6000·drunkwake·evdefect·insurfraud·towfall). 세 갈래를 하루씩 섞어 배치(`work/_b1010_slots.txt`). 제작 `work/_b1010_make.sh <tag> <slugs>`(예약 분리, ssul 실폴더 충돌 시 COLLIDE 로 건너뜀), 예약 `work/_b1010_sched.sh <slugs>`. 뉴스 copdrag 는 보배드림 drunkcop 과 같은 사건(순천 경찰관 매달고 74km)이라 towfall 로 교체. 쇼핑태그·동영상 언어는 공개 후 Studio.
- 2026-10-09 밤: 10/7·10/8 공개 20편 쇼핑태그 5개씩 부착(20/20 저장 확인, 건너뜀 0). 소재 직결품(에어컨필터·하이패스·주차번호판·광각미러·스노우체인·LED전조등·햇빛가리개·워셔액·SD리더기 등) + 공용 묶음(드림아이 2채널 블박·아톰 메모리카드·비상삼각대·충전 거치대·점프스타터). ⚠️ MCP 창이 가려져 `visibilityState=hidden` 이면 접힘 애니메이션·대화상자 페이드가 멈춰 연필/대화상자가 안 잡힘 → 클릭 직후 `chrome_screenshot`(savePng/storeBase64 false, 타임아웃 나도 됨)으로 렌더를 한 번 깨우면 열린다. 숨은 탭에선 JS 의 setTimeout 대기가 멈추니 대기는 도구(wait)로, JS 는 동기 코드만. 검색은 input 에 execCommand insertText + JS Enter 이벤트로 됨. 대화상자의 '최근 태그된 제품' 목록에서 바로 + 가능.
- 2026-10-10: **편집 규칙 v2(§4-4) 확정** — 사용자 지정 유튜브 레퍼런스 2건(얘봐라 야무진·이것만 티맵)으로 `yamujin`·`tmaproute` 대본(`_batch_1010e.py`), yamujin 을 Remotion v2 파일럿으로 제작(컷 25·실사 3+AI 14·효과음 15) → 사용자 승인, **10/13 12:00 Zernio 예약**(postId 6aca296ff43617e4b020de35). 구버전은 `work/yamujin/yamujin_v1.mp4`. tmaproute 는 구방식 빌드만 있음(미예약). — tmaproute 는 v2 로 다시 만들지 않기로 함(2026-10-10 사용자 "다시 만들지는 마").
- 2026-10-10 teslatak(테슬라 탁송사고·인수 거부 불가, 연합뉴스TV 10/8 기사) v2 규칙 첫 신규 편(`_batch_1010f.py`, 38.5s·컷 26·AI 16+커먼즈 3·독일 번호판 흐림·인포그래픽 5·새 BGM sneaky-123) → **10/11 11:00 Zernio 예약 postId 6aca49f5da5937868c15390c**(사용자 지정 시각, 기본 슬롯 밖). 렌더 폰트 delayRender 시간초과 1회 → build_v2 동시 4·timeout 90초
- 2026-10-13: **보배드림 베스트 24시간 5편, v2(Remotion) + 경모 목소리(tts_myvoice, `myvoice: 경모`·`myvoice_narration: talk1`, 사용자 지시)** — 생성기 `_batch_1013.py`, 이미지 `work/_b1013_img.py`(gen.sh 동시 5), 컷 `work/_b1013_shots.py`. Zernio 예약: parkthreat 10/13 20:00(6ace07b1…)·humanblock 20:30(6ace07b9…)·alley73 21:00(6ace07bf…)·garagetent 10/14 12:00(6ace07c5…)·old90drive 12:30(6ace07cc…). 실사 0·AI 전부. ⚠️ 경모 TTS 는 다른 세션의 이슈쿠키 TTS 와 동시에 돌면 줄당 70초→4~13분으로 느려짐(19시 첫 칸 놓침). ⚠️ `ssul/assets/sfx/issuecookie/*.wav` 가 `sfx/ic/` 로 옮겨지고 `bgm/sneaky-123.mp3` 가 사라져 있었음 → build_v2 가 ic/ 도 찾게 보강, BGM 은 `tools/bgm_sneaky.py` 로 재합성.
- 2026-10-15: **사용자 지정 중앙일보 기사(체리 오모다5 뒷축 이탈) `omoda5` 즉시 공개**(15:28, fu4hMl5JJb8, 기사 화면 캡처+기사 사진 사용 — 사용자 허락, 기자 얼굴 흐림, 흰 바에 제목 안 가리게 캡처 위 210px 여백) + **10/15 저녁 5칸·10/16 10칸 Zernio 예약**. 10/13 미완성 4편(sooltagi·ferrariuturn·hcpark1100·vegastoy) 재사용 + 보배드림 베스트 8편·뉴스 3편 신규(`_batch_1015.py`·`_batch_1015b.py` — 줄 스펙에 컷·효과음·팝·인포를 같이 적어 script.json+shots.json 한 번에 생성). TTS 큐 러너 `work/_b1015_tts.sh`(큐 파일 `_b1015_queue.txt` 순서), 빌드 러너 `_b1015_build.sh`, 슬롯 `_b1015_slots.txt`. ⚠️ **Info.tsx 버그 2건 수정**: counter 가 무조건 천 단위 반올림(4주→0주, 8878대→9,000대) → 1만 미만은 그대로 / bars 이름 칸 230px 고정이라 긴 이름이 막대에 가림·숫자가 인포 끝나기 전에 덜 참(800→791) → 이름 폭 자동·끝나기 10프레임 전까지 다 차게. **omoda5 공개본은 수정 전 렌더라 9,000대·0만 대로 나감**→ 수정본(8,878대·155만 대 확인)을 `omoda5b` 로 **10/17 12:00 Zernio 예약**(postId 6ad0e9cdd19f578ac1e8ccd4). 기존 공개본 fu4hMl5JJb8 은 삭제 안 함(되돌릴 수 없어 사용자 확인 필요), alley73(10/13) 30% 카운터도 0% 로 나갔을 가능성.
- 2026-10-16: **커뮤니티 게시글 첫 건** — 렉서스 8세대 올 뉴 ES 국내 출시(10/13), 카드 5장(Toyota 글로벌 뉴스룸 공식 사진) 공개 게시. `work/post_1016_lexus_es/`. 같은 날 "대본 중간 대화체 1문장" 미적용 지적 → §4-4 규칙 추가.
- 2026-10-16: 보배드림 베스트 `spikeroad`(맛집 진입로 쇠말뚝 → 일반교통방해 대법원 2001도6903) 1편 제작, 36.6초, **대화체 대사 줄 첫 적용**(땅주인 대사, `speaker: 2` — 나레이션이 talk1 이라 기본 대사(speaker 1)는 목소리가 안 바뀜). 생성기 `_batch_1016.py`(대사 줄 없으면 assert). 미예약.
- 2026-10-16: 사용자 지정 매일경제 기사(테슬라 로드스터 2세대 공개, 10/15 현지) → `roadster26` 1편(⚠️ 처음엔 슬러그 `roadster` 로 만들어 9/26 공개된 같은 슬러그 편의 로컬 파일 script.json·upload.md·mp4·tts 를 덮어씀, 복구 불가 → **새 편 만들기 전 `work/<slug>` 와 `_zernio_log.json` 에 같은 슬러그가 있는지 확인**), **이미지 대신 영상 컷 첫 적용**. Tesla 공식 유튜브 4편(The Kickflip·The Ramp·Last Best Driver's Car·Roadster Event, `work/_videos/roadster/`)을 9:8 크롭 1080x960 무음 클립으로 잘라(`work/roadster/v2/vid/`) shots.json 에 `"vid": "vid/v01.mp4"`(선택 `"ss"` 초)로 넣는다. `build_v2.py`·`RanbbangShort.tsx`(OffthreadVideo) 에 영상 컷 지원 추가: 컷이 클립보다 길면 느리게 재생. 출처 "영상: Tesla" 우상단. 생성기 `_batch_1016b.py`, 35.5초, 대사 줄 = 머스크 발언(speaker 2) + 사용자 추가 지시로 **첫 줄을 구경꾼 반응 대사 "와우, 대박인데?"(speaker 3, 다른 목소리)로 시작**, 34.1초. 37.8초. ⚠️ **`tts_myvoice.py` 는 `line_NNN.wav` 를 줄 번호로 캐시(있으면 건너뜀)** → 줄을 끼우거나 순서를 바꾸면 음성이 한 칸씩 밀려 자막과 다른 문장이 나온다(이번 편에서 실제로 발생). 줄 구성을 바꾸면 `tts/line_*.wav` 를 전부 지우고 다시 만든다. 받아쓰기로 재검증하고, 발음이 뭉개진 줄은 say 띄어쓰기만 바꿔 그 줄 wav 를 지우고 재생성(시드 고정이라 그대로 지우면 같은 결과). 자막 덩어리 시간은 `build_v2.py` spoken_split 이 실제 발화 구간·읽는 음절 수 기준으로 나눈다. **10/16 15:27 Zernio 즉시 공개** zEKr2X0-C6s(postId 6ad1c297ae8e8791beb71fbc), 쇼핑태그 미부착.
- 2026-10-16: 사용자 지시 "최근 자동차 출시 뉴스로 1개" → **BMW iX4 세계 최초 공개(10/8) `ix4`, §4-6 신차 공개 구조 첫 적용**(GV80 하이브리드 9/28 `gv80hev`·투싼 9/20 `tucson` 은 이미 있어 제외). BMW 공식 유튜브 QTqKzj-uP5I(필름)·EaT9LWne1eQ(워크어라운드) 클립, 출처 "영상: BMW". 7번 대사는 BMW 임원 발언을 못 찾아 가상 구매자 대사(근거표에 명시). 수치 오토뷰·오토트리뷴·Electrek 교차확인(트렁크 150L 는 최대 적재 1750→1600L 기준). 37.1초, 생성기 `_batch_1016c.py`, 미예약. ⚠️ 워크어라운드 영상은 `-ss` 를 `-i` 앞에 두면(빠른 탐색) 시트 시각이 실제와 약 29초 어긋났다 → 장면 찾기 시트도 `-i` 뒤 `-ss`(정확 탐색)로 뽑는다.
- 2026-10-17: 사용자 지시 "테슬라 날으는 차, 반응·원리·가격추측 개드립에서" → `roadsterfly`(커뮤니티 반응형, roadster26 과 같은 사건 다른 각도). 개드립 로드스터 글 11건 본문·댓글 수집(729904706·729951481·729893101·729858990·729911991 등), 수치는 Electrek 10/15(트림 3종 0-60 1.6/0.9/0.59초 미만·예약금 5만 달러·로켓 공도 불가·냉가스 추진기 COPV·흡입 팬) + Supercar Blondie(쓰러스트 예약 25만 달러). 대사 2줄(구경꾼 "AI 아냐? 진짜라고?" speaker 3, 회의론 "어따 씀? 3억이잖아" speaker 2). 클립은 roadster26 재사용. **Info.tsx bars 에 `dec`(소수 자릿수) 추가**(0.59초가 1초로 반올림되던 문제). 32.4초, 생성기 `_batch_1017.py`, 미예약. ⚠️ 커뮤니티 댓글 대사 컷에 실존 인물(머스크)이 보이면 그 사람 발언처럼 읽히니 차 컷만 쓴다.
- 2026-10-17 21:35: `roadsterfly` 화면 타이틀을 사용자 선택 C안 `"이거 AI 아님?"` / `진짜 나는 로드스터` 로 바꿔 재렌더(경모 TTS 가 4/14줄에서 끊겨 있던 것 이어서 생성, 38.8초) → **Zernio 즉시 공개** BBYe-pSYnu4 (postId 6ad36af41d00339efc1bb9e8). 테모TV 쇼츠 통째 재업로드 요청은 저작권 문제로 거절하고 이 편으로 대체. rdthreads(17:09)와 각도 겹침은 사용자 인지 후 진행. 쇼핑태그 미부착.
- 2026-10-17: **무나레이션 밈 모음 포맷 첫 편 `teslameme`**(레퍼런스 짤멍짤 jYoqaxhAZoY 레이아웃: 검정 배경, 상단 잘난체 빨강/노랑 2줄(줄 간격 121px), 가운데 1080x1033 클립, 하단 부크크고딕 설명 + 이모지, 클립 안 박다현체 반응 글씨(76px, 얼굴 피해 배치)). 틱톡 2 + 스레드 6 클립을 컷당 3.6초로 빨리감기, 노래 체리필터 '오리날다' 58.6초(첫 후렴)부터, 원본 클립 소리는 음악 없는 효과음 구간만 살림. 생성기 `_ep_teslameme.py`, 28.8초. **21:35 Zernio 즉시 공개** https://www.youtube.com/watch?v=ryOlikkZHTw (postId 6ad36b6f071122131bec7127). 동영상 언어=한국어 Studio 저장 완료. **쇼핑태그 불가**: 공개 직후 오리날다(CHERRYFILTER) Content ID 소유권 주장 → "YouTube Shopping 사용 중지됨, 제품 태그 허용 안 됨"(도달범위, 수익, 채널 영향은 없음으로 표시). 상업 음원을 쓰면 쇼핑태그 규칙과 충돌한다. → 같은 날 사용자 "실수, 란빵에서 삭제하고 휴지 채널로" → 란빵 ryOlikkZHTw **비공개 전환**(영구 삭제는 사용자 직접), 법푸는휴지에 Studio 브라우저 업로드 공개 https://www.youtube.com/watch?v=qQLXdniYKjE (AI 변경 콘텐츠 예, 언어 한국어). 고정 댓글 미등록(작업 탭이 닫힘). ⚠️ 스레드 영상은 yt-dlp 미지원 → 로그인된 브라우저에서 글 페이지 HTML 의 `video_versions` URL 을 fetch 해 받는다. ⚠️ ffmpeg 필터의 adelay/volume(t) 로 클립 소리 구간을 자르면 소리가 밀리거나 통째로 빠짐 → numpy 로 직접 배치.
- 2026-10-18: 밈 모음 2일차 `teslameme2`(제목 '출시 2일차 근황'). 틱톡 검색 14개 받아 8컷 선정(정체 탈출, 서울 버스, 아프리카 오너, 파키스탄 시장, 2030 음주단속, 뉴욕 옥상, 출고 첫날, 운전석 비었음). 생성기 `_ep_teslameme2.py` 는 1편 모듈을 import 해 소스, 문구, 타이틀만 덮어씀. 같은 날 사용자 지시로 배경음을 오리날다에서 sneaky-123(-26 LUFS)으로 바꾸고 8컷 모두 원본 소리 전체 구간을 살림(SFX_RMS -18, `_ep_teslameme.py` 에 MUSIC_LUFS 변수 추가). 28.8초, -15.0 LUFS, 미업로드. ⚠️ 원본 소리 안에 상업 음원이 섞여 있는지는 확인 안 함. 이어서 사용자 "반응이 영상과 안 맞음, 영상 설명하면서 반응" → 컷마다 0.4초 간격 프레임을 보고 그 순간 장면을 설명하는 반응 문구로 전면 교체(컷당 2~4개). **밈 모음 반응 글씨 규칙: 막연한 드립 말고 지금 화면에서 일어나는 일(무엇이 어떻게 되는지)을 말하면서 반응, 그 장면이 나오는 시각에 맞춰 띄운다.** 이어서 사용자 "마지막 컷 빼고 1배속" → `_ep_teslameme.py` 에 REALTIME(1배속 컷 번호) 추가, 7컷을 핵심 5~5.5초만 1배속으로 잘라 39.6초(40초 미만), 배경음은 sneaky-123 2번 이어붙인 `work/teslameme2/bgm_sneaky_x2.m4a`, -14.6 LUFS. **10/18 23:10 란빵 Zernio 즉시 공개** https://www.youtube.com/watch?v=Bj5VC0sDb2Q (postId 6ad4d2e163d9a6ce984d2ff1, 사용자 지시로 휴지 아닌 란빵). 쇼핑태그 미부착.
- 2026-10-18: 사용자 지정 블로그 2건 → 2편(`_batch_1018.py`, 실사 = 제조사 공식 사진만, AI 0). `byddahan`(BYD 다한 EV 출시, 신차 공개형 §4-6 응용, BYD 보도사진 7장(CnEVPost 게재본), 1008km 는 CLTC 라 WLTP 816km 와 compare 인포로 같이 표기, 37.9초) → **10/19 12:00 Zernio 예약** 6ad4db4bf8cadfc0992e81c3. `tasmandc`(기아 타스만 9월 404대 반토막·10월 7월 생산분 600만원 할인, 판매·점유율은 파이낸셜뉴스 10/5 2건 확인, 할인 총액은 블로그 720 vs 뉴스와 760 으로 달라 '700만원 넘게'로만, 사진 kia.com 모델 페이지 _pc.jpg 1920x800, 31.9초) → **10/19 12:30 Zernio 예약** 6ad4db7599a0e9f91c1eb0e2. ⚠️ Info counter 에 7자리 금액(6,000,000원)을 넣으면 화면 왼쪽이 잘림 → num 600 + suffix '만원' 으로. counter 와 pop 을 같은 어절에 겹치면 글자가 포개지니 하나만.
- 2026-10-19 fingerled: 사용자 지정 인스타 릴스(@the.flipbuddy, LED 손가락 표시기) 11초를 4컷 영상 컷으로 재활용 + 도로교통법 42조/시행령 27조/154조(30만원 이하 벌금, 구류) 원문 확인. 30.2s, **10/19 13:00 Zernio 예약** 6ad4f1889f636215153f4719. 원본 11초라 일부 컷 슬로우 재생됨
- 2026-10-19 genesispole: 사용자 지정 SPOTV 쇼츠(CFl2ChMQn4E) 가운데 중계 화면 43.0~81.6초 + 원본 해설 소리, 위 2줄 타이틀, 아래 원본 실제 댓글을 다듬어 아이디 바꿔 하나씩 쌓는 댓글 반응형(신규 포맷, `_ep_genesispole.py`). 38.6초, 미예약. 사용자 문구 '첫회만에 풀포지션'은 데뷔 시즌 7전이라 '첫 시즌만에 폴포지션'으로 고침
- 2026-10-21: **20편 일괄 제작, 10/22~10/23 Zernio 예약(하루 10칸)**. 보배드림 베스트 7(`_batch_1021.py`: taxicop, gmdash, torresblock, rtrevenge, hornrage, resowheel, rbout100) + 셀토스 4, 테슬라 3, 자동차 관련법 6(`_batch_1021b.py`: seltosup, seltosfire, seltoscn, seltosvs / teslaygrand, teslafsdkr, teslarobot / alcolock, drunkassist, drugdrive, pedalguard, licrenew, yellowlight). 셀토스 차 화면 = 현대차그룹 뉴스룸 보도사진(`work/_photos/seltos/map.txt`), 캐나다 리콜(1세대)과 중국형엔 국내 신형 사진을 안 씀. 러너 `work/_b1021_img.py`, `_b1021_tts2.sh`, `_b1021_build.sh`. ⚠️ 함정 5건: ① **Info quotes 말풍선은 nowrap 68px 라 한 줄 12자 안팎**, 긴 인용은 title + 짧은 item 여러 개로 쪼갠다 ② compare 카드 값도 10자 안팎("1월 1일~12월 31일" 잘림) ③ bars 에서 at 없는 항목은 바로 뜨고 at 있는 항목은 늦게 떠서 순서가 뒤집힌다, 같이 띄우려면 모두 같은 at ④ **tts_myvoice 는 줄마다 메모리가 쌓여 12~18GB, 스왑 포화 시 줄당 5분+ 또는 멈춤**, `_b1021_tts2.sh` 처럼 16GB 넘으면 끄고 다시 돌린다(만든 줄은 건너뜀). say 55자 넘는 줄은 그 자리에서 멈췄으니 대본 단계에서 둘로 나눈다 ⑤ zsh 에서 `for s in $L` 은 안 쪼개진다(큐 파일에 13편이 한 줄로 들어감), 슬러그 목록은 파이썬이나 bash 로 쓴다. 메모리 압박 때 Remotion 폰트 delayRender 시간초과 2회(teslafsdkr, licrenew), 재렌더로 해결.
- 2026-10-26: `airporttaxi`(인천공항 택시 시외 할증, 공동사업구역 규정, JTBC 사건반장 쇼츠 5jolpOUIXv0 + 아이뉴스24) — ssul 파이프라인으로 만들어 처음엔 법푸는휴지용이었으나 **사용자 지시로 란빵에 게시**. 워터마크 끔(`style.watermark=""`, `channel: 란빵`), 설명란 3줄+해시태그로 교체. 12:51 Zernio 즉시 공개 https://youtube.com/shorts/irW_lIhY24A (첫 댓글 Zernio 자동). 원본은 `ssul/work/airporttaxi/`. 쇼핑태그 5개·동영상 언어(한국어)는 공개 직후 Studio 에서 처리.
- 2026-10-27: **자동차 이슈 13편**(사용자 "말한거 모두 만들어서 업로드") — 보배드림 베스트 10/24~26 11편(bbox168 블랙박스 168만원 할부·rinse0 대법 입헹굼물·bmwchase 10분 추격·cle11 벤츠 결함 11개·spark6s 신호 6초 뒤 충돌·z4light 경차칸 Z4·autop 자동 P 조건·sojucourt 술타기 선고·uninsured 책임보험만·cheapimport 아반떼 값 수입차·tucson95 투싼 고급유) + 개드립 fsdapply(테슬라 FSD 승인 신청) + 헤럴드 marathon(마라톤 완주 후 운전). 생성기 `_batch_1027.py`(조사 `work/research_1027.md`, 실사 `work/_photos/b1027/`), 러너 `work/_b1027_img.py`·`_b1027_tts2.sh`·`_b1027_build.sh`. **원글 캡처 + 얼굴 모자이크 첫 적용**(`tools/mosaic.py`, 위 표). ⚠️ 글자 수 기준 길이 예측: 기존 편 실측이 **약 10자/초**(taxicop 360자 36.5초, gmdash 288자 28.7초) → 대본 합계 **370자 이하**로 맞춰야 40초 안에 든다(초안 420~440자였음). ⚠️ `Info.tsx` counter 는 소수점(dec) 미지원·1만 이상 천 단위 반올림 → 0.081%, 42.195km, 16,200원은 bars 로. ⚠️ 디스크 가득(여유 258MB)으로 gen.sh "No space left" 실패 → `~/.codex/generated_images`(6시간 지난 사본 14GB)와 `~/.codex/sessions`(7일 지난 로그 약 30GB) 삭제로 44GB 확보. 10/24 배치 6편(golfclub·tire80·oildrain·repair740·outcar64·leftturn91)은 대본·shots 만 있고 TTS·이미지·렌더가 안 된 채 남아 있음(10/25 칸은 비었음). **결과(10/27 03:50)**: 13편 전부 33.9~38.7초로 렌더, Zernio 예약 10/27 12:00~21:00 10칸(bbox168 6adfa097… rinse0 6adfa138… bmwchase 6adfa4cb… cle11 6adfa4d3… spark6s 6adfa4da… z4light 6adfa4e2… autop 6adfa4eb… sojucourt 6adfa4f1… uninsured 6adfa8b8… cheapimport 6adfa8be…) + 10/28 12:00~13:00 3칸(tucson95 6adfa8c5… fsdapply 6adfa8cb… marathon 6adfa8dd…), 전체 id 는 `work/_zernio_log.json`·`ssul/docs/used-sources.md`. ⚠️ 사고 2건: (1) Info bars 의 `"flash": True` 는 안 됨 → flash 는 `at` 처럼 **어절 문자열**(build_v2 at_time 이 str 기대, rinse0 BUILD_FAIL). (2) tts_myvoice 가 특정 문장(bmwchase 2번째 줄 '…비엠더블유가 급제동하더니, …')에서 매번 18GB 폭주 → 30회 재시작 실패. `say` 를 두 문장으로 쪼개고('…비엠이 급제동을 했음. 그리고 …') 큐 끝에 다시 넣어 통과. 한 줄이 반복 실패하면 문장을 고쳐야지 재시도로는 안 됨. Zernio POST 는 600초 타임아웃, broken pipe 가 나도 서버엔 생성돼 있을 수 있음 → 재실행 전 `GET /posts` 로 확인하고 로그에 수동 추가(bbox168 그렇게 처리). 쇼핑 태그 5개는 공개 후 Studio 수동.
- 2026-10-28: **하루 10편 자동 제작 launchd 설치**(§4-4-1). `daily/` 폴더(run_daily.sh, PROMPT.md, 러너 3개, log.tsv). `_batch_1027.cap()` 에 `ph=` 인자 추가해 다른 날짜 배치에서 재사용. 첫 자동 실행 = 10/28 15:00 → 10/29 10칸. 10/28 은 전날 배치 3편(12:00~13:00)만 예약돼 있고 나머지 7칸은 비어 있음.
- 2026-10-29: 10/28 15:00 첫 자동 실행이 `/bin/zsh: can't open input file`(TCC, Desktop 접근 차단)로 실패해 10/29 칸 0편. launchd 를 Terminal 경유(`daily/run_daily.command`)로 바꾸고, 예약을 Zernio 에서 chrome-mcp Studio 업로드(쇼핑태그 동시 부착)로 전환. 헤드리스 claude 에서 chrome-mcp-stdio 연결 확인.
- 2026-10-29: **いらすとや 캐릭터 폐지**(사용자 "앞으로 쭉"). `_batch_1020.NO_CHAR=True`. 진행 중이던 10/29 daily 10편도 shots.json 재생성, 이미 렌더된 selffall, trench55, benzfire 는 재렌더.
- 2026-10-29 daily(09:44 수동 실행, 대상 10/29): 10편 Studio 예약 완료, 생성기 `_batch_1029.py`, 조사 `work/research_1029.md`·`research_1029_newcar.md`. 12:00 selffall(gJARm0qrDYE)·12:30 trench55(OjmlZdTJesw)·13:00 glbev(3OieaxhitAc)·13:30 benzfire(vXPwrbXqPZc)·14:00 air5000(AS6NsMBGGSA)·19:00 sonatadisc(DlMRHW2qOMo)·19:30 bunsim91(4twME9YZ7Vs)·20:00 golfr(-6kf4E00WCw)·20:30 fsdtalok(AKQHe69obnE)·21:00 cayennecp(wS4w8J5P0QA), 전부 쇼핑태그 5개. ⚠️ 사고/배운 것: (1) launchd PATH 의 python3 가 homebrew 3.14(PIL·cv2 없음)라 러너가 전부 실패할 뻔 → `daily/bin/python3`(→/usr/bin/python3) 심을 run_daily.sh PATH 맨 앞에 추가. (2) img_runner.py 가 chdir 뒤 상대경로 큐를 열어 FileNotFoundError → 절대경로화 수정. (3) tts_myvoice 가 15GB(재시작 기준 16GB 미만)에서 마지막 '구독!' 줄에 1시간 47분 멈춤(golfr) → 수동 kill 로 복구. tts_runner 에 '줄 수가 N분 안 늘면 kill' 가드가 필요. (4) 대본 355자인데 40.1초(cayennecp, 신차 숫자 많은 줄) → 한 줄 빼고 tts 파일 번호를 당겨 재렌더 37.4초. 숫자 많은 편은 340자 이하로. (5) 같은 날 10:41 캐릭터 폐지(NO_CHAR) 전에 렌더·업로드한 selffall·trench55·benzfire 3편은 いらすとや 캐릭터가 들어간 채 예약됨(파일 교체 불가, 재렌더본은 work/ 에 있음, 교체 여부는 사용자 판단). (6) Studio 쇼핑태그 검색창은 JS value 설정만으로는 검색이 안 되고, 띄어쓰기 없는 검색어를 chrome_keyboard 로 쳐야 안정적. 탭이 자주 hidden 이 돼 chrome_switch_tab 을 단계마다 다시 호출. 업로드 마지막에 'YouTube에서 아직 동영상 검사 중' 확인창이 뜸. 소재 중복: 워셔액은 washer25(10/8)와 겹쳐 카이엔 쿠페로 교체.
- 2026-10-30 daily(10/29 15:06 실행이 중간에 멈춰 22:42 이어하기, 대상 10/30): 10편 Studio 예약 완료, 생성기 `_batch_1030.py`. 12:00 teslafsd89(edTmqEN5-gU), 12:30 stalkmis(4jsMvXcjFMM), 13:00 gv90tech(1OXrA7_a9xk), 13:30 disabled3(TNG7oEeHbqE), 14:00 ureaend(G8Hm5mYq4JQ), 19:00 dealervat(J3JZEKInstc), 19:30 brakecheck(oWIcWNSKCNM), 20:00 zeekr7x(d7c6fQhI1Ew), 20:30 doorscrape(F6Z5-ueps9U), 21:00 caymancut(IxPDFdAZGfE), 길이 29.7~34.1초. ⚠️ 사고/배운 것: (1) **쇼핑태그 0개**: 태그 5개를 붙이고 `완료`/`저장`해도 서버가 "태그된 제품 5개를 찾을 수 없습니다. 판매자가 삭제했거나 만료된 제품"으로 되돌림(쿠팡, 에이블리 상품 모두, 편집 화면 재시도도 동일). 10/29 예약분(selffall, cayennecp)도 지금 보면 태그 0개라 채널 단위 문제로 추정(원인 확인 안 됨, 쇼핑 탭엔 경고 없음). 3편(teslafsd89, stalkmis, gv90tech)에서 시도 후 나머지는 태그 없이 예약. (2) 이전 실행이 teslafsd89 를 **초안**으로 올려 두고 멈춤 → 콘텐츠 목록 `초안 수정`으로 이어서 예약(재업로드 안 함). (3) 업로드 흐름에 **`수익 창출` 단계가 새로 생김**(보기 페이지 광고 `사용` 선택 후 완료). 이 단계 뒤 `다음`이 드롭다운 backdrop 에 먹히니 stepper 의 `광고 적합성`/`공개 상태` 제목을 직접 눌러 이동하는 게 빠름. (4) **자정을 넘기면 예약 날짜 기본값이 다음 날**(10/31)로 바뀜 → 00시 이후 업로드는 달력 pick('2026년 10월', 30)으로 날짜를 반드시 다시 고름. (5) 탭이 hidden 이면 chrome_keyboard 가 60초 타임아웃 → chrome_computer type/key + 매 단계 screenshot(리페인트)으로 진행.
- 2026-10-30: **해외 블박 모음 `fraudcam`**(끼어들고 급브레이크, 보험사기 수법 조심, 28.1s, 미업로드). 틱톡 후보 10개 중 화면에 영어 자막, 얼굴, 폰 촬영이 없는 2계정 3장면만 통과(oof.cam 2장면, stargazerlily.y). 세 장면 모두 박는 장면이 아니라 급정거라 `_ep_dashcam.py` 에 클립별 `"sfx": "screech"`(끼익) 옵션 추가. 한 원본에 장면이 여러 개면 장면 경계에서 미리 잘라 별도 파일로(tpad 정지가 다음 장면으로 안 넘어가게), 얼굴 나오는 뒷부분과 원본 편집의 주황 전환 프레임(32.2초)도 미리 잘라냄. BGM `calm-0831.mp3` 가 삭제돼 있어 `sneaky-123.mp3` 로 교체. 근거: 보험사기방지 특별법 제8조(10년 이하 징역 또는 5천만원 이하 벌금).
- 2026-10-30: **fraudcam 재제작, 블박 사연형 포맷 신설**(사용자 "@1-footstep 채널 영상처럼, 다시"). 레퍼런스 채널은 SBS 몇대몇 블랙박스(국내 방송) 재가공이라 소재는 계속 해외 블박만 쓰고 화면과 말투만 따옴. 생성기 **`_ep_story.py <slug>`** + `work/<slug>/story.json`: 베이지 종이 배경, 상단 2줄 제목(흰+초록, 배민주아, 검은 외곽선), 영상 가로 꽉(480~1470), 영상 아래쪽 검은 반투명 박스 자막(Pretendard SemiBold 46, `*강조*` 노랑, 다음 자막까지 유지), 빨간 원/화살표, 노란 손글씨(기랑해랑) 의성어, 출처 1줄(y 1600), 번호판은 원본초 키프레임 보간 블러. 사건 하나를 실시간으로 따라가며 해요체 나레이션(태섭 1.25), 끝에 사고 장면 0.5배 슬로우 + 교훈, 법 근거, 질문. 3클립 모음본(output 덮어씀)은 폐기. 35.4초.
- 2026-10-30: **`bigleft` 국내 블박 1회 예외**(사용자 "국내 블박 이번에만 예외로"). 원본 = JTBC 한블리 인스타 선공개 릴스(@jtbc.insta, 대좌회전 후 급정거 vs 경적 블박차). 상단 JTBC 제목, 하단 한블리 로고는 crop 으로 빼고 블박 영역(1080:575:0:658)만 사용, 번호판은 원본에서 이미 모자이크. **나레이션 없는 포맷** 생성기 `_ep_silent.py <slug>`(story.json: subs 원본초, hand 의성어, sfx horn/screech/crash 합성, 0.5배 리플레이, 투표 카드). 타이틀 "상대차 vs 블박차 / 과실 몇대몇?", 끝 "누가 더 잘못? 블박차 vs 상대차". v2(사용자 수정): **검은 배경, 모든 글자 잘난고딕 자간 -2%, 흰 + 노랑 #FDF652, 원본 소리 그대로 + BGM 0.07, 자막은 원본 장면에 맞춰 6개로 재배치**(경적은 원본 6.8~7.4초 650Hz로 확인). 18.7초, 미업로드. ⚠️ 방송사 영상이라 Content ID 클레임 위험. ⚠️ 배민주아에 ①② 글리프 없음(빈칸).
- 2026-10-30: **bigleft v2**(사용자 수정 지시): 검은 배경, 글자 전부 잘난고딕(JalnanGothicTTF, 자간 -2%, 흰 + 노랑 #FDF652, 참고 이미지 실측), **원본 소리 그대로**(리플레이는 0.5배 atempo) + BGM 0.07, 합성 효과음 뺌. 자막을 원본 단서로 다시 맞춤(흰 SUV 등장 5.6초, 경적 650Hz 6.8~7.5초, 충돌음 9.2~9.5초): 블박차 우회전 중 / 상대차가 크게 돌아서 쑥 / 빠앙~ / 갑자기 급정거;; / 결국 쿵! / 다시 보면. 끝 카드는 "누가 더 잘못? / 댓글로 투표!" 2줄 좁은 줄간격(블박차 vs 상대차 줄 삭제). 18.7초.
- 2026-10-30 21:47 KST: bigleft Zernio 즉시 공개 예약(postId 6ae491181d37c2ab9fc4f4de). 쇼핑태그 5개는 공개 후 Studio 수동.
- 2026-10-31 daily(10/30 15:00 실행, 대상 10/31): 10편 Studio 예약 완료, 전부 쇼핑태그 5개. 12:00 bbox142(2tVcb9OQ_2U), 12:30 busrage(IvOqHxbiHVQ), 13:00 minioxford(x3bRup-rS0k), 13:30 armytruck(XjY9TeV8Cqo), 14:00 parksafe(eVyMBtVya_Q), 19:00 ebikeseat(_DjS328dBBQ), 19:30 dumpmerge(et1GcJRFcIg), 20:00 missions(-bhmj1XwwLY), 20:30 slopepark(JOnCP-3P_Bg), 21:00 lane82(wNUySzlC9MQ), 길이 29.0~33.9초. ⚠️ 사고/배운 것: (1) 헤드리스 실행이 `API Error: ENOTFOUND`(네트워크 끊김)로 중간에 멈춰 6편만 예약됨. 남은 4편은 10/31 03시대 수동 이어하기: minioxford 는 BUILT 로그가 있는데 mp4 가 없어 재렌더, dumpmerge 는 첫 TTS_FAIL(메모리 18G 6회) 뒤 큐 재시도로 TTS_OK 됐지만 build_runner 가 이미 BUILD_DONE 이라 빌드 안 됨 → 수동 build_v2. (2) 10/30 의 '서버가 태그 삭제' 문제는 이번엔 재현 안 됨(편집 화면에서 태그된 제품 5개 유지 확인). (3) youtube.com/account 의 '내 채널'은 계정 기본 채널(법푸는휴지)로 표시돼 활성 채널 확인에 못 씀 → 우상단 아바타나 Studio 채널명으로 확인. (4) 광고 적합성 화면은 상단 배너가 늦게 떠 레이아웃이 밀림 → 좌표는 스크린샷 직후 다시 계산.
- 2026-11-01 daily(10/31 15:00 실행, 대상 11/1): 10편 Studio 예약 완료, 전부 쇼핑태그 5개, 길이 28.5~34.3초. 생성기 `_batch_1101.py`, 조사 `work/research_1101.md`. 12:00 carrotdeal(fOcjaKUCAQk), 12:30 parkseat(sImCWyg1AnU), 13:00 tucson5(AnpJqTmpM1Y), 13:30 bumperall(tRWzHjIf_3M), 14:00 antifreeze(ikyrbhLvbQ0), 19:00 oring50(3hH6WZVBM90), 19:30 hiddencam(yejnnH5oko0), 20:00 gtimoss(rY3097eHY_4), 20:30 g90park(nFaetubbVEQ), 21:00 usedavante(ssXTbv8WyiQ). ⚠️ 사고/배운 것: (1) **tts_myvoice 가 12GB 근처(16GB 재시작 기준 미만)에서 스왑 포화로 한 줄에 15~30분 멈춤**(g90park, tucson5, usedavante, gtimoss) → '새 line_*.wav 가 6분간 안 생기면 kill' 감시 스크립트(`/tmp/rb1101/watchdog.sh`)로 해결. tts_runner.sh 에 이 가드를 넣어야 함. (2) 러너 프로세스의 `sleep 20` 이 9분 넘게 안 깨는 일이 생겨(메모리 압박 추정, 원인 확인 안 됨) 마지막 2편은 러너를 끄고 수동(TTS→tts.py→build_v2). 같은 편 TTS 를 두 번 띄우지 않게 pgrep 확인 필수. (3) 생성기 수정 후 이미 만든 편을 재생성 안 해서 carrotdeal shots.json 이 옛 compare 형식으로 남아 BUILD_FAIL → **Info compare 는 items[{label,color,at,rows:[[항목,값,색]]}], counter 도 items[{num,suffix}]** 형식. 고친 뒤엔 모든 편을 다시 돌릴 것. (4) 검수에서 잡은 화면 오류 2건: g90park 대사 줄 AI 배경이 다른 브랜드 세단으로 그려짐, usedavante '8월 신형' 줄에 2023년 더 뉴 아반떼 보도사진 → 원글 사진/중고차 매장 배경으로 교체 재렌더. 차종이 특정되는 줄엔 AI 차 그림을 쓰지 말 것. (5) Studio '동영상 요소'에서 제품 태그하기 칸이 회색(추가 버튼 없음)일 때 `뒤로`→`다음`하면 다시 뜸. (6) antifreeze 쇼핑태그는 '사계절 부동액, 겨울용 워셔액' 검색 결과가 엉뚱해 부동액, 점프스타터, 성에제거 스프레이, 블랙박스 2채널, 방향제로 붙임.
- 2026-11-04 daily(11/3 15:00 실행, 대상 11/4): 10편 Studio 예약 완료, 전부 쇼핑태그 5개, 길이 28.9~37.1초. 생성기 `_batch_1104.py`, 조사 `work/research_1104.md`. 12:00 kgm1600(9FgQDI7MS6U), 12:30 deerslip(yoAODQ6hCTk), 13:00 filnoir(Fp97O27ein0), 13:30 stealthrain(JISwb_OBYMo), 14:00 jumpcold(04TyoIzPm_o), 19:00 benzew337(Pvb_b2RTo34), 19:30 truckback(ORwopqcv4O4), 20:00 genline(bEMpkZmIrrs), 20:30 gasblock(nXmT5BpLNb0), 21:00 bikelane(pX18UQXBNE4). ⚠️ 사고/배운 것: (1) **Studio 업로드에 '수익 창출' 단계가 새로 생김**: 세부정보 다음 드롭다운 → '사용' → 완료, 그 뒤 스테퍼 '광고 적합성' 버튼 → '해당 사항 없음' 체크 → 평가 제출 → 다음. 상단 배너 유무에 따라 좌표가 약 60px 밀림. (2) 제품 태그하기 칸이 회색이면(SD 처리 전) 스테퍼에서 광고 적합성 → 동영상 요소로 오가면 활성화됨. (3) 제품 검색은 chrome_keyboard 입력이 타임아웃 나서 JS 헬퍼로 처리: `#search-input` 에 native value setter + Enter keydown/keypress/keyup 디스패치, 결과 행 y 좌표를 읽어 + 버튼(x≈680) 클릭. (4) 페이지 JS 안의 setTimeout/await 는 백그라운드 탭에서 스로틀돼 타임아웃 나므로 JS 는 즉시 반환형으로만 쓰고 대기는 도구 호출 사이에서. (5) 모자이크 `pixelate` 가 박스를 가로 25%, 세로 30% 키워서 benzew337 서류 캡처에서 지점명이 드러나거나 금액이 가려짐 → 박스를 작게 다시 잡음. (6) stealthrain 첫 업로드가 반영 안 된 것처럼 보여 재업로드, 콘텐츠 목록에서 중복 없음 확인. (7) bikelane 에서 upload.md 에 없는 검색어를 잘못 보냄, 태그 전에 바로잡음: 쇼핑태그는 반드시 upload.md 목록과 대조.
- 2026-11-04n 수동(11/3 22:45 사용자 지시 "10개 만들어서 10분 간격으로 지금부터 업로드"): 예약 대신 완성, 검수 즉시 공개. 10편 전부 공개, 쇼핑태그 5개, 광고 적합성 제출, 고정 댓글. 길이 29.4~34.0초. 생성기 `_batch_1103n.py`, 조사 `work/research_1103n.md`, 큐 `daily/queue_2026-11-04n.txt`. 23:11 tirewheel(_a8Z8-TckwU), 23:24 exportscam(i61qpRyWSwc), 23:36 sidescrape(sBd7JN6fEdA), 23:48 armyins(dMVD3L_60x4), 00:00 spitcar(4XZ1BIrqPLU), 00:12 newcar5(9EXE0z_OZoo), 00:24 pedalspace(06dwihPRQrU), 00:36 cybercab(Bbpaq4luRtM), 00:49 h2carnival(-CZ2sMLT0Ls), 00:59 aircare(3578zITbfmA). 실제 간격은 업로드, 태그 작업 시간 때문에 10~13분. ⚠️ 배운 것: (1) Studio 를 다녀오면 활성 채널이 법푸는휴지로 되돌아감, 댓글 전 매번 youtube.com/channel_switcher 에서 @eggbread0 선택 후 simplebox 아바타(노란 차) 확인. (2) exportscam AI 배경에 현대 엠블럼이 생성돼 블러 처리 후 재렌더, pedalspace 원본 영상 자막이 보여 크롭 재렌더, h2carnival 수동 모자이크 박스가 기사 제목을 가려 제거: AI 배경과 캡처는 프레임 시트로 상표, 자막, 가림을 매번 확인. (3) tunnelcut(1044967) 은 영상만으로 누가 끼어드는 쪽인지 판독 안 돼 newcar5 로 교체. (4) 쇼핑태그 검색이 '검색 중에 문제 발생'이면 검색어를 바꿈(블랙박스 메모리카드 → 블랙박스 SD카드). (5) 댓글 ⋮ 메뉴 좌표가 스크롤 위치에 따라 바뀌어 추천 영상을 잘못 누른 적 있음, `ytd-comment-thread-renderer #action-menu button` 셀렉터 클릭이 안전.
