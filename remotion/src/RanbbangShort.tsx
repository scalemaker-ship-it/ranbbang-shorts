// 란빵 쇼츠 v2 (2026-10-10) — 레퍼런스: 한입썰 「짐승 치우라던 할머니가…」(youtube.com/shorts/AoAK3YS2I8c)
// 검은 바탕 · 상단 2줄 고정 제목(노랑/흰) · 1080x960 이미지 박스(컷마다 켄번즈, 강조 컷은 펀치인·클로즈업)
// · 박스 하단 어절 단위 자막(검은 띠) · 효과음은 강조 지점에만(컷 전환음 없음) · 사고/반전은 흔들림+팝 글자.
// 데이터는 public/<slug>/data.json (tools/build_v2.py 가 만든다).
import React from "react";
import {
  AbsoluteFill,
  Audio,
  Easing,
  Img,
  OffthreadVideo,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
} from "remotion";
import { InfoView, type Info } from "./Info";

export type Shot = {
  src: string;
  from: number;
  dur: number;
  // 켄번즈: 시작·끝 배율과 초점(0~1). punch 면 처음 7프레임에 확 당긴다.
  s0: number;
  s1: number;
  fx: number;
  fy: number;
  fx1?: number;
  fy1?: number;
  punch?: boolean;
  credit?: string;
  vid?: boolean; // 영상 컷(무음 1080x960 클립) — vss 프레임부터 재생, 컷이 클립보다 길면 느리게
  vdur?: number;
  vss?: number;
};
export type Cap = { from: number; dur: number; png: string }; // 자막 = ssul render.py 로 그린 투명 PNG(애니메이션 없음)
export type Sfx = { src: string; from: number; vol: number };
export type Pop = { from: number; dur: number; text: string; color: string };
export type Shake = { from: number; dur: number; amp: number };
// いらすとや 캐릭터(2026-10-20) — 리얼 배경 앞에 서 있는 누끼 PNG(흰 테두리). 박스 아래 변에 발을 붙이고 좌/우에 선다
export type Char = { from: number; dur: number; src: string; side: "l" | "r"; h: number; pop: boolean; flip?: boolean };
export type Data = {
  fps: number;
  total: number;
  title: [string, string];
  titleSize: number; // 두 줄 같은 크기 — build_v2.py 가 PIL 로 폭(920px)에 맞춰 계산
  bar?: { text: string; size: number; until: number }; // 첫 문장 동안 제목 밑 흰 바
  narr: string;
  bgm: string;
  bgmVol: number;
  shots: Shot[];
  caps: Cap[];
  sfx: Sfx[];
  pops: Pop[];
  shakes: Shake[];
  infos?: Info[]; // 인포그래픽(Info.tsx) — 이미지 박스 위에 겹친다
  chars?: Char[];
};

// 세로 배치 = 기존 란빵 템플릿(ssul pipeline/layout.py) 값 그대로: 타이틀 0.127~0.269, 콘텐츠 0.275~0.710
const H = 1920;
const TITLE_TOP = Math.round(0.127 * H);
const TITLE_MID = Math.round(0.19 * H);
const BOX_Y = Math.round(0.275 * H);
const BOX_H = Math.round(0.71 * H) - BOX_Y;
const BAR_H = Math.round(0.055 * H);
const NEON = "#FBFF56";
const W = 1080;
const CLAMP = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const FONT = "Paperlogy";

const ShotView: React.FC<{ s: Shot; creditTop: number }> = ({ s, creditTop }) => {
  const f = useCurrentFrame();
  const t = interpolate(f, [0, s.dur], [0, 1], CLAMP);
  let scale = interpolate(t, [0, 1], [s.s0, s.s1], { easing: Easing.inOut(Easing.quad) });
  if (s.punch) {
    // 펀치인: 컷 시작 6프레임 동안 1.0→1.16 으로 확 당긴다(축소에서 시작하면 박스 가장자리가 비어 검은 테두리가 보인다)
    const p = interpolate(f, [0, 6], [1, 1.16], { ...CLAMP, easing: Easing.bezier(0.34, 1.5, 0.64, 1) });
    scale *= p;
  }
  const fx = interpolate(t, [0, 1], [s.fx, s.fx1 ?? s.fx]);
  const fy = interpolate(t, [0, 1], [s.fy, s.fy1 ?? s.fy]);
  // 초점(fx,fy)이 박스 중앙에 오도록 이동하되, 이미지 가장자리가 박스 안으로 들어오지 않게 제한
  const iw = W * scale;
  const ih = BOX_H * scale;
  let tx = W / 2 - fx * iw;
  let ty = BOX_H / 2 - fy * ih;
  tx = Math.min(0, Math.max(W - iw, tx));
  ty = Math.min(0, Math.max(BOX_H - ih, ty));
  return (
    <AbsoluteFill style={{ overflow: "hidden", backgroundColor: "#000" }}>
      {s.vid ? (
        <OffthreadVideo
          src={staticFile(s.src)}
          muted
          startFrom={s.vss ?? 0}
          playbackRate={Math.min(1, ((s.vdur ?? s.dur) - (s.vss ?? 0)) / s.dur)}
          style={{ position: "absolute", left: tx, top: ty, width: iw, height: ih, objectFit: "cover" }}
        />
      ) : (
        <Img
          src={staticFile(s.src)}
          style={{
            position: "absolute",
            left: tx,
            top: ty,
            width: iw,
            height: ih,
            objectFit: "cover",
          }}
        />
      )}
      {s.credit ? (
        <div
          style={{
            position: "absolute",
            right: 160,
            top: creditTop,
            padding: "4px 10px",
            background: "rgba(0,0,0,0.55)",
            color: "rgba(255,255,255,0.9)",
            fontFamily: FONT,
            fontWeight: 800,
            fontSize: 22,
          }}
        >
          {s.credit}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};

const CharView: React.FC<{ c: Char }> = ({ c }) => {
  const f = useCurrentFrame();
  // 등장: 아래에서 튀어오르며 커진다(같은 캐릭터가 이어지면 pop=false 로 그대로 서 있음). 서 있는 동안 살짝 들썩
  const sc = c.pop ? interpolate(f, [0, 8], [0.55, 1], { ...CLAMP, easing: Easing.bezier(0.34, 1.6, 0.64, 1) }) : 1;
  const fin = Math.max(4, c.dur - 3);
  const op = c.pop ? interpolate(f, [0, 3, fin, fin + 3], [0, 1, 1, 0], CLAMP) : interpolate(f, [fin, fin + 3], [1, 0], CLAMP);
  const bob = Math.sin(f / 7) * 5;
  return (
    <Img
      src={staticFile(c.src)}
      style={{
        position: "absolute",
        bottom: -18 + bob,
        height: c.h,
        ...(c.side === "l" ? { left: 24 } : { right: 150 }),
        opacity: op,
        transform: `scale(${sc}) ${c.flip ? "scaleX(-1)" : ""}`,
        transformOrigin: "50% 100%",
        filter: "drop-shadow(0 12px 16px rgba(0,0,0,0.45))",
      }}
    />
  );
};

const CapView: React.FC<{ c: Cap }> = ({ c }) => (
  <Img src={staticFile(c.png)} style={{ position: "absolute", left: 0, top: 0, width: W, height: H }} />
);

const PopView: React.FC<{ p: Pop }> = ({ p }) => {
  const f = useCurrentFrame();
  const sc = interpolate(f, [0, 6], [2.2, 1], { ...CLAMP, easing: Easing.bezier(0.34, 1.4, 0.64, 1) });
  const op = interpolate(f, [0, 3, p.dur - 4, p.dur], [0, 1, 1, 0], CLAMP);
  const rot = interpolate(f, [0, 6], [-8, -4], CLAMP);
  return (
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: BOX_Y + BOX_H / 2 - 100,
        textAlign: "center",
        opacity: op,
        transform: `scale(${sc}) rotate(${rot}deg)`,
        fontFamily: FONT,
        fontWeight: 900,
        fontSize: 150,
        color: p.color,
        WebkitTextStroke: "10px #000",
        paintOrder: "stroke fill",
        textShadow: "0 8px 0 rgba(0,0,0,0.6)",
      }}
    >
      {p.text}
    </div>
  );
};

export const RanbbangShort: React.FC<{ data: Data }> = ({ data }) => {
  const f = useCurrentFrame();
  // 흔들림: 활성 shake 구간이면 감쇠 진동
  let dx = 0;
  let dy = 0;
  for (const s of data.shakes) {
    if (f >= s.from && f < s.from + s.dur) {
      const k = 1 - (f - s.from) / s.dur;
      dx += Math.sin(f * 2.7) * s.amp * k;
      dy += Math.cos(f * 3.3) * s.amp * k;
    }
  }
  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      {/* 이미지 박스 */}
      <div
        style={{
          position: "absolute",
          left: 0,
          top: BOX_Y,
          width: W,
          height: BOX_H,
          overflow: "hidden",
          transform: `translate(${dx}px, ${dy}px)`,
        }}
      >
        {data.shots.map((s, i) => (
          <Sequence key={i} from={s.from} durationInFrames={s.dur} layout="none">
            <ShotView s={s} creditTop={data.bar && s.from < data.bar.until ? BAR_H + 12 : 14} />
          </Sequence>
        ))}
        {(data.chars ?? []).map((c, i) => (
          <Sequence key={`c${i}`} from={c.from} durationInFrames={c.dur} layout="none">
            <CharView c={c} />
          </Sequence>
        ))}
        {(data.infos ?? []).map((info, i) => (
          <Sequence key={`i${i}`} from={info.from} durationInFrames={info.dur} layout="none">
            <InfoView info={info} />
          </Sequence>
        ))}
      </div>
      {/* 상단 고정 제목 — 기존 란빵: 잘난체 고딕·1행 흰/2행 형광노랑·검정 외곽선 10·자간 -1 */}
      {[data.title[0], data.title[1]].map((t, i) => (
        <div
          key={i}
          style={{
            position: "absolute",
            left: 0,
            right: 0,
            top: i === 0 ? TITLE_TOP : TITLE_MID,
            height: TITLE_MID - TITLE_TOP,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontFamily: "JalnanGothic",
            fontSize: data.titleSize,
            letterSpacing: -1,
            lineHeight: 1,
            whiteSpace: "nowrap",
            color: i === 0 ? "#fff" : NEON,
            WebkitTextStroke: "20px #000",
            paintOrder: "stroke fill",
          }}
        >
          {t}
        </div>
      ))}
      {/* 흰 바 — 첫 문장 동안만 이미지 상단에 걸친다 */}
      {data.bar && f < data.bar.until ? (
        <div
          style={{
            position: "absolute",
            left: 0,
            right: 0,
            top: BOX_Y,
            height: BAR_H,
            background: "#fff",
            color: "#111",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontFamily: "Pretendard",
            fontWeight: 600,
            fontSize: data.bar.size,
            whiteSpace: "nowrap",
          }}
        >
          {data.bar.text}
        </div>
      ) : null}
      {data.caps.map((c, i) => (
        <Sequence key={i} from={c.from} durationInFrames={c.dur} layout="none">
          <CapView c={c} />
        </Sequence>
      ))}
      {data.pops.map((p, i) => (
        <Sequence key={i} from={p.from} durationInFrames={p.dur} layout="none">
          <PopView p={p} />
        </Sequence>
      ))}
      <Audio src={staticFile(data.narr)} />
      <Audio src={staticFile(data.bgm)} volume={data.bgmVol} loop />
      {data.sfx.map((s, i) => (
        <Sequence key={i} from={s.from} layout="none">
          <Audio src={staticFile(s.src)} volume={s.vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
