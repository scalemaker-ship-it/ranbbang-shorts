#!/usr/bin/env python3
"""v2 AI 배경 생성 — gen.sh(luna) square, 동시 5, 없는 것만 최대 3라운드.
  python3 daily/img_runner.py <queue.txt>      (큐 = slug 한 줄씩, END 로 끝)
work/<slug>/v2/ai_prompts.tsv → work/<slug>/v2/ai/<key>.png. 끝나면 IMG_DONE."""
import os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
QF = os.path.abspath(sys.argv[1])   # chdir 전에 절대경로로(상대경로 큐가 FileNotFoundError 나던 문제, 2026-10-29)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.join(ROOT, "work"))
GEN = os.path.expanduser("~/.claude/skills/codex-image/scripts/gen.sh")
SL = [l.strip() for l in open(QF) if l.strip() and l.strip() != "END"]
def run(j):
    s, k, p = j; out = os.path.abspath(f"{s}/v2/ai/{k}.png")
    r = subprocess.run([GEN, "--prompt", p, "--out", out, "--orientation", "square"], capture_output=True, text=True, stdin=subprocess.DEVNULL)
    ok = os.path.exists(out) and os.path.getsize(out) > 0 and r.returncode == 0
    print(("ok " if ok else "FAIL ") + f"{s}/{k}" + ("" if ok else " " + (r.stderr or r.stdout)[-200:].replace("\n", " ")), flush=True)
for rnd in range(3):
    jobs = []
    for s in SL:
        os.makedirs(f"{s}/v2/ai", exist_ok=True)
        for ln in open(f"{s}/v2/ai_prompts.tsv"):
            k, p = ln.rstrip("\n").split("\t", 1)
            if not os.path.exists(f"{s}/v2/ai/{k}.png"): jobs.append((s, k, p))
    print(f"round {rnd+1} todo {len(jobs)}", flush=True)
    if not jobs: break
    with ThreadPoolExecutor(5) as ex: list(ex.map(run, jobs))
print("IMG_DONE", flush=True)
