#!/usr/bin/env python3
"""란빵 v2 いらすとや 캐릭터 받기(2026-10-20) → work/<slug>/v2/ir/ir_<이름>.png (투명 + 흰 테두리)

  python3 tools/ir_rb.py search 運転手            # 후보(번호, 제목, 파일명)
  python3 tools/ir_rb.py get <slug> driver 運転手 [번호]

검색, 테두리는 ssul/pipeline/irasutoya.py 그대로. いらすとや 무료 조건: 한 편에 20장 이하(get 이 막는다).
"""
import io, os, sys, urllib.request
sys.path.insert(0, os.path.expanduser("~/Desktop/kim/ssul/pipeline"))
from irasutoya import outline, UA   # noqa: E402
import json, re, urllib.parse   # noqa: E402


def search(q, n=8):
    """ssul 판과 달리 글 하나의 PNG 를 전부 후보로 낸다(표정 여러 장짜리 글: car_man01_smile/angry/…)."""
    u = "https://www.irasutoya.com/feeds/posts/default?alt=json&max-results=%d&q=%s" % (n, urllib.parse.quote(q))
    j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=20))
    out = []
    for e in j["feed"].get("entry", []):
        for im in dict.fromkeys(re.findall(r'src="([^"]+\.png)"', e["content"]["$t"])):
            out.append((e["title"]["$t"], re.sub(r"/s\d+(-c)?/", "/s800/", im)))
    return out
from PIL import Image                         # noqa: E402

RB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def get(slug, name, q, idx=0):
    d = os.path.join(RB, "work", slug, "v2", "ir")
    os.makedirs(d, exist_ok=True)
    dst = os.path.join(d, f"ir_{name}.png")
    have = [f for f in os.listdir(d) if f.startswith("ir_") and f != os.path.basename(dst)]
    assert len(have) < 20, f"{slug}: いらすとや 20장 초과"
    c = search(q)
    title, url = next((t, u) for t, u in c if u.endswith("/" + idx)) if isinstance(idx, str) else c[idx]
    im = Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read())).convert("RGBA")
    im = im.crop(im.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox())
    outline(im).save(dst)
    print(f"✓ {slug}/ir_{name}.png ← {title} ({url.split('/')[-1]})")
    return title


if __name__ == "__main__":
    if sys.argv[1] == "search":
        for i, (t, u) in enumerate(search(sys.argv[2])):
            print(i, t, u.split("/")[-1])
    else:
        get(sys.argv[2], sys.argv[3], sys.argv[4], (int(sys.argv[5]) if sys.argv[5].isdigit() else sys.argv[5]) if len(sys.argv) > 5 else 0)
