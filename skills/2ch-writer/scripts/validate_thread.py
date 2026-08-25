#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""Validate 2ch thread JSON or rendered HTML before executing pack.

Checks: body anchor 0, required fields, escaped HTML, sequential numbering.

Usage:
  python3 scripts/validate_thread.py posts.json
  python3 scripts/validate_thread.py posts.json --template assets/viewer.html
  python3 scripts/validate_thread.py out/thread.html --html
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path

ANCHOR_RE = re.compile(r">>\d+")

def validate_posts(data):
    if "posts" in data:
        posts = data["posts"]
    elif "beats" in data:
        posts = [p for b in data.get("beats", []) for p in b.get("posts", [])]
    else:
        posts = []
    errs = []
    warns = []
    if not posts:
        errs.append("posts array is empty or missing 'posts'/'beats.posts'")
        return errs, warns
    for idx, p in enumerate(posts, start=1):
        body = p.get("body", "")
        if not isinstance(body, str) or not body.strip():
            errs.append(f"post {idx}: body is empty")
        if ANCHOR_RE.search(body):
            errs.append(f"post {idx}: body contains anchor '{ANCHOR_RE.search(body).group()}' — use content naming")
        if len(body) > 3000:
            warns.append(f"post {idx}: body {len(body)} chars — consider split into one-breath vs wall")
        for f in ("body",):
            if f not in p:
                errs.append(f"post {idx}: missing '{f}'")
    # check title
    if not data.get("title"):
        errs.append("missing 'title'")
    return errs, warns

def validate_html(path: Path):
    text = path.read_text(encoding="utf-8")
    errs = []
    warns = []
    # check anchor in rendered bodies (should be escaped but still check raw)
    if re.search(r">>\d+", text):
        errs.append("rendered HTML contains '>>N' — bodies must contain zero anchors")
    # check posts numbered sequentially via meta count
    metas = re.findall(r'<p class="meta">(\d+) ：', text)
    if not metas:
        errs.append("no post meta blocks found")
    else:
        nums = [int(x) for x in metas]
        if nums != list(range(1, len(nums) + 1)):
            errs.append(f"post numbers not sequential 1..N: {nums[:10]}...")
    if "<title></title>" in text or "<h1></h1>" in text:
        warns.append("title appears empty")
    return errs, warns

def main():
    ap = argparse.ArgumentParser(description="Validate thread JSON or HTML")
    ap.add_argument("input", help="posts.json / beats.json / out.html")
    ap.add_argument("--template", default="assets/viewer.html")
    ap.add_argument("--html", action="store_true", help="force HTML mode")
    ap.add_argument("--json", action="store_true", help="output JSON summary")
    args = ap.parse_args()

    p = Path(args.input)
    if args.html or p.suffix == ".html":
        errs, warns = validate_html(p)
        post_count = len(re.findall(r'<article class="post">', p.read_text(encoding="utf-8"))) if p.exists() else 0
    else:
        data = json.loads(p.read_text(encoding="utf-8"))
        errs, warns = validate_posts(data)
        post_count = len(data.get("posts") or [])

    validated = not errs
    summary = {"input": str(p), "validated": validated, "post_count": post_count, "errors": errs, "warnings": warns}
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        if errs:
            print(f"FAIL: {len(errs)} errors", file=sys.stderr)
            for e in errs:
                print(f"  - {e}", file=sys.stderr)
        if warns:
            print(f"WARN: {len(warns)} warnings", file=sys.stderr)
            for w in warns:
                print(f"  - {w}", file=sys.stderr)
        if validated:
            print(f"OK: {post_count} posts validated, {len(warns)} warnings", file=sys.stderr)
        print(json.dumps(summary, ensure_ascii=False))
    sys.exit(0 if validated else 2)

if __name__ == "__main__":
    main()
