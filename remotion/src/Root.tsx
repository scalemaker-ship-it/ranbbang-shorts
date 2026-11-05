import "./fonts";
import { Composition, staticFile } from "remotion";
import { RanbbangShort, type Data } from "./RanbbangShort";

// 편 데이터는 public/<slug>/data.json — 렌더 시 --props='{"slug":"yamujin"}'
export const RemotionRoot: React.FC = () => (
  <Composition
    id="Ranbbang"
    component={({ data }: { slug: string; data?: Data }) => (data ? <RanbbangShort data={data} /> : null)}
    fps={30}
    width={1080}
    height={1920}
    durationInFrames={30}
    defaultProps={{ slug: "yamujin" } as { slug: string; data?: Data }}
    calculateMetadata={async ({ props }) => {
      const data: Data = await (await fetch(staticFile(`${props.slug}/data.json`))).json();
      return { durationInFrames: data.total, props: { ...props, data } };
    }}
  />
);
