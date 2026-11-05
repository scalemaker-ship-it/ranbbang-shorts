// 인포그래픽 오버레이(2026-10-10 사용자 지시 "리모션으로 인포그래픽 그래프 효과 더") — 이미지 박스 안에 어둡게 깔고 그린다.
// 종류: quotes(말풍선) · flow(돈·계약 흐름도) · compare(두 카드 비교) · bars(막대그래프 카운트업) · counter(숫자 카운트업)
// 시간은 전부 info 시작 기준 프레임(at). build_v2.py 가 대사 어절 시점으로 계산해 넣는다.
import React from "react";
import { Easing, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

export type InfoItem = {
  at: number;
  label?: string;
  text?: string;
  value?: number; // bars: 0~1
  num?: number; // 카운트업 목표
  suffix?: string;
  dec?: number; // bars: 소수 자릿수(기본 0)
  color?: string;
  flash?: number; // 강조 순간(빨강 맥동)
  rows?: [string, string, string?][]; // compare: [항목, 값, 값 색]
  from?: string; // flow: 노드 이름
  to?: string;
  dashed?: boolean;
};
export type Info = {
  from: number;
  dur: number;
  kind: "quotes" | "flow" | "compare" | "bars" | "counter";
  title?: string;
  sub?: string;
  items: InfoItem[];
  nodes?: { name: string; x: number; y: number; color?: string }[];
};

const NEON = "#FBFF56";
const RED = "#FF3B30";
const CLAMP = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const F = "Paperlogy";
const STROKE = { WebkitTextStroke: "8px #000", paintOrder: "stroke fill" } as const;

const useSpring = (at: number) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: f - at, fps, config: { damping: 13, stiffness: 160 } });
};
const grow = (f: number, at: number, len = 18) =>
  interpolate(f, [at, at + len], [0, 1], { ...CLAMP, easing: Easing.out(Easing.cubic) });

const Title: React.FC<{ text: string; sub?: string }> = ({ text, sub }) => {
  const s = useSpring(0);
  return (
    <div style={{ position: "absolute", top: 46, left: 0, right: 0, textAlign: "center", transform: `scale(${0.6 + 0.4 * s})`, opacity: s }}>
      <div style={{ fontFamily: F, fontWeight: 900, fontSize: 62, color: NEON, ...STROKE }}>{text}</div>
      {sub ? <div style={{ fontFamily: F, fontWeight: 800, fontSize: 36, color: "rgba(255,255,255,0.7)", marginTop: 6 }}>{sub}</div> : null}
    </div>
  );
};

const Bubble: React.FC<{ it: InfoItem; y: number }> = ({ it, y }) => {
  const s = useSpring(it.at);
  return (
    <div
      style={{
        position: "absolute",
        left: 90,
        top: y,
        transform: `translateY(${(1 - s) * 60}px) scale(${0.7 + 0.3 * s})`,
        transformOrigin: "left center",
        opacity: Math.min(1, s * 1.5),
        background: "#fff",
        color: "#111",
        borderRadius: 44,
        borderTopLeftRadius: 8,
        padding: "26px 44px",
        fontFamily: F,
        fontWeight: 900,
        fontSize: 68,
        boxShadow: "0 10px 0 rgba(0,0,0,0.5)",
        whiteSpace: "nowrap",
      }}
    >
      {it.text}
    </div>
  );
};

const Quotes: React.FC<{ info: Info }> = ({ info }) => (
  <>
    {info.title ? (
      <div style={{ position: "absolute", left: 90, top: 70, background: RED, color: "#fff", fontFamily: F, fontWeight: 900, fontSize: 44, padding: "8px 22px", borderRadius: 12 }}>
        {info.title}
      </div>
    ) : null}
    {info.items.map((it, i) => (
      <Bubble key={i} it={it} y={190 + i * 190} />
    ))}
  </>
);

const Flow: React.FC<{ info: Info }> = ({ info }) => {
  const f = useCurrentFrame();
  const R = 105;
  const node = (n: string) => info.nodes!.find((x) => x.name === n)!;
  return (
    <>
      <svg width={1080} height={835} style={{ position: "absolute", left: 0, top: 0 }}>
        <defs>
          {["y", "w", "r"].map((k) => (
            <marker key={k} id={`ah-${k}`} viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto">
              <path d="M0,0 L10,5 L0,10 z" fill={k === "y" ? NEON : k === "r" ? RED : "#fff"} />
            </marker>
          ))}
        </defs>
        {info.items.map((it, i) => {
          const a = node(it.from!);
          const b = node(it.to!);
          const dx = b.x - a.x;
          const dy = b.y - a.y;
          const len = Math.hypot(dx, dy);
          const ux = dx / len;
          const uy = dy / len;
          const x1 = a.x + ux * (R + 10);
          const y1 = a.y + uy * (R + 10);
          const x2 = b.x - ux * (R + 22);
          const y2 = b.y - uy * (R + 22);
          const p = grow(f, it.at, 14);
          const col = it.color ?? "#fff";
          const k = col === NEON ? "y" : col === RED ? "r" : "w";
          return p > 0 ? (
            <line
              key={i}
              x1={x1}
              y1={y1}
              x2={x1 + (x2 - x1) * p}
              y2={y1 + (y2 - y1) * p}
              stroke={col}
              strokeWidth={14}
              strokeLinecap="round"
              strokeDasharray={it.dashed ? "4 28" : undefined}
              markerEnd={p > 0.95 ? `url(#ah-${k})` : undefined}
            />
          ) : null;
        })}
      </svg>
      {info.nodes!.map((n, i) => {
        const at = Math.min(...info.items.filter((it) => it.from === n.name || it.to === n.name).map((it) => it.at), 0);
        const s = spring({ frame: f - at - i * 3, fps: 30, config: { damping: 12 } });
        return (
          <div
            key={n.name}
            style={{
              position: "absolute",
              left: n.x - R,
              top: n.y - R,
              width: R * 2,
              height: R * 2,
              borderRadius: R,
              background: n.color ?? "#fff",
              border: "8px solid #000",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontFamily: F,
              fontWeight: 900,
              fontSize: 54,
              color: "#111",
              transform: `scale(${s})`,
            }}
          >
            {n.name}
          </div>
        );
      })}
      {info.items.map((it, i) => {
        const a = node(it.from!);
        const b = node(it.to!);
        const s = spring({ frame: f - it.at - 10, fps: 30, config: { damping: 12 } });
        const col = it.color ?? "#fff";
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: (a.x + b.x) / 2 - 300,
              width: 600,
              top: (a.y + b.y) / 2 - 38 + (it.dashed ? 50 : 0),
              textAlign: "center",
              transform: `scale(${s})`,
            }}
          >
            <span style={{ background: "#000", color: col, border: `4px solid ${col}`, borderRadius: 14, padding: "6px 18px", fontFamily: F, fontWeight: 900, fontSize: 44, whiteSpace: "nowrap" }}>
              {it.text}
            </span>
          </div>
        );
      })}
    </>
  );
};

const Card: React.FC<{ it: InfoItem; x: number }> = ({ it, x }) => {
  const s = useSpring(it.at);
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: 80,
        width: 450,
        transform: `translateY(${(1 - s) * 80}px) rotate(${(1 - s) * (x < 500 ? -6 : 6)}deg)`,
        opacity: Math.min(1, s * 1.5),
        background: "#16161a",
        border: `6px solid ${it.color}`,
        borderRadius: 28,
        overflow: "hidden",
      }}
    >
      <div style={{ background: it.color, color: "#111", fontFamily: F, fontWeight: 900, fontSize: 58, textAlign: "center", padding: "18px 0" }}>{it.label}</div>
      {it.rows!.map(([k, v, c], j) => (
        <div key={j} style={{ padding: "22px 20px 8px", textAlign: "center" }}>
          <div style={{ fontFamily: F, fontWeight: 800, fontSize: 36, color: "rgba(255,255,255,0.6)" }}>{k}</div>
          <div style={{ fontFamily: F, fontWeight: 900, fontSize: 58, color: c ?? "#fff", whiteSpace: "nowrap" }}>{v}</div>
        </div>
      ))}
      <div style={{ height: 22 }} />
    </div>
  );
};

const Compare: React.FC<{ info: Info }> = ({ info }) => (
  <>
    {info.items.map((it, i) => (
      <Card key={i} it={it} x={i === 0 ? 60 : 570} />
    ))}
    {info.items.length > 1 ? (
      <div style={{ position: "absolute", left: 490, top: 300, width: 100, textAlign: "center", fontFamily: F, fontWeight: 900, fontSize: 64, color: NEON, ...STROKE }}>VS</div>
    ) : null}
  </>
);

// LW = 이름 칸 폭(가장 긴 이름에 맞춤), dur = 인포 길이(숫자가 사라지기 전에 다 차도록)
const BarRow: React.FC<{ it: InfoItem; y: number; LW: number; dur: number }> = ({ it, y, LW, dur }) => {
  const f = useCurrentFrame();
  const s = useSpring(it.at);
  const g = grow(f, it.at + 4, Math.max(8, Math.min(22, dur - 10 - (it.at + 4))));
  const X0 = 50 + LW + 24;
  const TW = 1030 - X0;
  const w = TW * (it.value ?? 0) * g;
  const n = ((it.num ?? 0) * g).toFixed(it.dec ?? 0);
  let pulse = 1;
  let col = it.color ?? NEON;
  if (it.flash !== undefined && f >= it.flash) {
    pulse = 1 + 0.35 * Math.max(0, 1 - (f - it.flash) / 8);
    col = RED;
  }
  return (
    <div style={{ position: "absolute", left: 0, top: y, width: 1080, height: 120, opacity: s, transform: `translateX(${(1 - s) * -80}px)` }}>
      <div style={{ position: "absolute", left: 50, width: LW, top: 22, textAlign: "right", fontFamily: F, fontWeight: 900, fontSize: 58, color: "#fff", whiteSpace: "nowrap" }}>{it.label}</div>
      <div style={{ position: "absolute", left: X0, top: 14, width: TW, height: 92, borderRadius: 16, background: "rgba(255,255,255,0.13)" }} />
      <div style={{ position: "absolute", left: X0, top: 14, width: w, height: 92, borderRadius: 16, background: col }} />
      <div
        style={{
          position: "absolute",
          // 막대가 길면 막대 안 오른쪽 끝에 맞춰(넘치지 않게), 짧으면 막대 바로 옆에
          ...(w > 260 ? { left: X0, width: w - 26, textAlign: "right" as const, transformOrigin: "right center" } : { left: X0 + w + 24, transformOrigin: "left center" }),
          top: 8,
          fontFamily: F,
          fontWeight: 900,
          fontSize: 76,
          color: w > 260 ? "#111" : col,
          transform: `scale(${pulse})`,
          whiteSpace: "nowrap",
          ...(w > 260 ? {} : STROKE),
        }}
      >
        {n}
        {it.suffix}
      </div>
    </div>
  );
};

const Bars: React.FC<{ info: Info }> = ({ info }) => {
  // 한글 58px ≈ 글자당 56px. 이름이 길면 칸을 넓히되 막대가 너무 짧아지지 않게 400px 까지
  const LW = Math.min(400, Math.max(230, ...info.items.map((it) => (it.label ?? "").length * 56)));
  return (
    <>
      {info.title ? <Title text={info.title} sub={info.sub} /> : null}
      {info.items.map((it, i) => (
        <BarRow key={i} it={it} y={250 + i * 170} LW={LW} dur={info.dur} />
      ))}
    </>
  );
};

const Counter: React.FC<{ info: Info }> = ({ info }) => {
  const f = useCurrentFrame();
  const it = info.items[0];
  const s = useSpring(it.at);
  const g = grow(f, it.at, 20);
  // 큰 금액(1만 이상)만 천 단위로 굴린다 — 작은 수(4주·6대·500만원의 500)는 그대로 세야 0 이 안 나온다
  const raw = (it.num ?? 0) * g;
  const n = (it.num ?? 0) >= 10000 ? Math.round(raw / 1000) * 1000 : Math.round(raw);
  const land = f >= it.at + 20 ? 1 + 0.25 * Math.max(0, 1 - (f - it.at - 20) / 8) : 1;
  return (
    <>
      {info.title ? <Title text={info.title} sub={info.sub} /> : null}
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 260,
          textAlign: "center",
          fontFamily: F,
          fontWeight: 900,
          fontSize: 190,
          color: it.color ?? NEON,
          opacity: s,
          transform: `scale(${(0.5 + 0.5 * s) * land})`,
          WebkitTextStroke: "14px #000",
          paintOrder: "stroke fill",
          letterSpacing: -4,
        }}
      >
        {n.toLocaleString("ko-KR")}
        <span style={{ fontSize: 120 }}>{it.suffix}</span>
      </div>
      {it.label ? (
        <div style={{ position: "absolute", left: 0, right: 0, top: 520, textAlign: "center", opacity: grow(f, it.at + 18, 6) }}>
          <span style={{ background: RED, color: "#fff", fontFamily: F, fontWeight: 900, fontSize: 50, padding: "10px 26px", borderRadius: 14 }}>{it.label}</span>
        </div>
      ) : null}
    </>
  );
};

export const InfoView: React.FC<{ info: Info }> = ({ info }) => {
  const f = useCurrentFrame();
  const bg = interpolate(f, [0, 6, info.dur - 5, info.dur], [0, 0.8, 0.8, 0], CLAMP);
  const fade = interpolate(f, [info.dur - 5, info.dur], [1, 0], CLAMP);
  const Body = { quotes: Quotes, flow: Flow, compare: Compare, bars: Bars, counter: Counter }[info.kind];
  return (
    <div style={{ position: "absolute", inset: 0 }}>
      <div style={{ position: "absolute", inset: 0, background: `rgba(8,8,12,${bg})` }} />
      <div style={{ position: "absolute", inset: 0, opacity: fade }}>
        <Body info={info} />
      </div>
    </div>
  );
};
