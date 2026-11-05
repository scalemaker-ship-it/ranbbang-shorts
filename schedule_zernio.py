#!/usr/bin/env python3
"""란빵 자동차 썰 → Zernio 예약 (란빵 전용 워크스페이스 키 = ~/.claude/skills/쇼핑쇼츠-업로드/.env).

  python3 ranbbang/schedule_zernio.py <slug>=<YYYY-MM-DDTHH:MM> [...] [--dry-run]

work/<slug>/<slug>.mp4 + upload.md(## 제목/## 설명/## 고정 댓글) 를 읽는다.
로그 ranbbang/work/_zernio_log.json 에 있는 slug 는 건너뛴다(중복 예약 방지).
"""
import os, sys, json, re, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pipeline"))
HERE = os.path.dirname(os.path.abspath(__file__))
for ln in open(os.path.expanduser("~/.claude/skills/쇼핑쇼츠-업로드/.env")):
    if "=" in ln and not ln.startswith("#"):
        k, v = ln.strip().split("=", 1); os.environ.setdefault(k, v)
os.environ["YT_CHANNEL_ID"] = "UCxQK4IBAJ1t-dPImmMinCng"
import importlib
z = importlib.import_module("8_upload_zernio")
LOG = os.path.join(HERE, "work", "_zernio_log.json")
# 2026-10-13 사용자 지시: 제목에 죽음·자살·사망·폭행 같은 위험 단어는 항상 제외 (노출 제한 방지)
RISKY = re.compile(r"죽음|죽었|죽인|죽여|죽는|사망|숨진|숨져|자살|극단적|폭행|폭력|구타|살인|살해|시신|흉기|학대|투신|참사|유서")

def section(md, name):
    m = re.search(rf"^## {name}\s*\n(.*?)(?=^## |\Z)", md, re.S | re.M)
    return m.group(1).strip() if m else ""

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    key, _ = z.env()
    done = json.load(open(LOG)) if os.path.exists(LOG) else []
    seen = {d["slug"] for d in done}
    acc = None if dry else z._yt_account(key)
    for a in args:
        slug, when = a.split("=")
        if slug in seen:
            print(f"⏭  {slug} 이미 예약됨"); continue
        wd = os.path.join(HERE, "work", slug)
        mp4 = os.path.join(wd, f"{slug}.mp4")
        md = open(os.path.join(wd, "upload.md")).read()
        title, desc, cm = section(md, "제목"), section(md, "설명"), section(md, "고정 댓글")
        assert os.path.exists(mp4), mp4
        assert title and len(title) <= 100
        assert not RISKY.search(title), f"제목 위험 단어: {slug} {title!r}"
        # 2026-10-16 사용자 지시: 영상은 40초 이내
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                    "-of", "csv=p=0", mp4], capture_output=True, text=True).stdout)
        assert dur < 40, f"40초 초과: {slug} {dur:.1f}s"
        print(f"▶ {slug} @ {when} KST | {title}")
        if dry: continue
        url = z.upload_media(key, mp4)
        payload = {"content": desc,
                   "platforms": [{"platform": "youtube", "accountId": acc,
                                  "platformSpecificData": {"title": title, "visibility": "public",
                                      "madeForKids": False, "containsSyntheticMedia": True,
                                      "categoryId": "22", "firstComment": cm}}],
                   "mediaItems": [{"url": url, "type": "video"}],
                   "scheduledFor": when + ":00", "timezone": "Asia/Seoul"}
        res = z.api("POST", "/posts", key, body=payload)
        pid = (res.get("post") or res).get("_id") if isinstance(res, dict) else None
        print(f"  ✔ postId={pid}")
        done.append({"slug": slug, "post_id": pid, "publish_at_kst": when, "title": title})
        json.dump(done, open(LOG, "w"), ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
