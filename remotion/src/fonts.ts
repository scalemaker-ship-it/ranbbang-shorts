// 폰트: Paperlogy(OFL) — public/fonts/ (ssul templates/2 에서 복사)
import { continueRender, delayRender, staticFile } from "remotion";

const FONTS = [
  { family: "Paperlogy", file: "Paperlogy-8ExtraBold.ttf", weight: "800" },
  { family: "Paperlogy", file: "Paperlogy-9Black.ttf", weight: "900" },
  // 란빵 기존 타이틀(ssul pipeline/layout.py) — 잘난체 고딕 / 흰 바 Pretendard SemiBold
  { family: "JalnanGothic", file: "JalnanGothic.otf", weight: "400" },
  { family: "Pretendard", file: "Pretendard-SemiBold.ttf", weight: "600" },
];
const handle = delayRender("fonts");
Promise.all(
  FONTS.map((f) => {
    const face = new FontFace(f.family, `url(${staticFile(`fonts/${f.file}`)})`, { weight: f.weight });
    return face.load().then(() => document.fonts.add(face));
  }),
).finally(() => continueRender(handle));
