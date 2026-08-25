#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""Render 2ch thread JSON → filled viewer.html in one call.

One Bash call renders any count — use for few-hundred defaults without sequential loops.

Usage:
  python3 scripts/render_thread.py --input posts.json --output out/thread.html [--template assets/viewer.html] [--validate]
  python3 scripts/render_thread.py --beat-plan beats.json --output out/thread.html
  python3 scripts/render_thread.py --help
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path

# Invariant 2: bodies contain zero anchor substrings
ANCHOR_RE = re.compile(r">>\d+")

# Output contract: one file, filled slots, style untouched
TEMPLATE_DEFAULT = Path("assets/viewer.html")

def load_json(p: Path):
    return json.loads(Path(p).read_text(encoding="utf-8"))

def posts_from_data(data):
    if "posts" in data:
        return data["posts"]
    if "beats" in data:
        posts = []
        for beat in data["beats"]:
            posts.extend(beat.get("posts", []))
        return posts
    raise ValueError("input must contain 'posts' or 'beats' array")

def validate(posts):
    errs = []
    for idx, p in enumerate(posts, start=1):
        body = p.get("body", "")
        if ANCHOR_RE.search(body):
            m = ANCHOR_RE.search(body).group()
            errs.append(f"post {idx}: body contains anchor substring '{m}' — rewrite to name content in words per invariant 2")
        for field in ("body",):
            if field not in p:
                errs.append(f"post {idx}: missing field '{field}'; available: body, name, stamp, id")
        if not isinstance(body, str) or not body.strip():
            errs.append(f"post {idx}: body is empty")
    if not posts:
        errs.append("posts array is empty")
    return errs

def render(data, template_path: Path):
    posts = posts_from_data(data)
    tpl = template_path.read_text(encoding="utf-8")
    title = html.escape(data.get("title", ""))
    lang = html.escape(data.get("lang", "ko"))
    blocks = []
    for idx, p in enumerate(posts, start=1):
        name = html.escape(p.get("name", ""))
        # stamp: if not supplied, use placeholder with ID
        raw_stamp = p.get("stamp", f"2026/08/21(Fri) 00:00:00 ID:{p.get('id','anon')}")
        stamp = html.escape(raw_stamp)
        body = html.escape(p["body"])
        blocks.append(
            f'<article class="post">\n<p class="meta">{idx} ：<span class="name">{name}</span>：{stamp}</p>\n<div class="body">{body}</div>\n</article>'
        )
    out = tpl.replace("{{TITLE}}", title).replace("{{LANG}}", lang).replace("{{POSTS}}", "\n".join(blocks))
    # template may use {{TITLE}} twice; replace remaining
    out = out.replace("{{TITLE}}", title)
    return out, posts

def main():
    ap = argparse.ArgumentParser(description="Render posts/beats JSON → viewer.html (few-hundred in one call)")
    ap.add_argument("--input", help="posts JSON path ({title, lang, posts:[{name, body, stamp, id}]})")
    ap.add_argument("--beat-plan", help="beat plan JSON path ({title, lang, beats:[{goal, posts:[...]}]})")
    ap.add_argument("--template", default=str(TEMPLATE_DEFAULT), help="template HTML path")
    ap.add_argument("--output", required=True, help="output HTML path or '-' for stdout")
    ap.add_argument("--validate", action="store_true", help="validate before rendering; exit 2 on error")
    ap.add_argument("--json-summary", default="-", help="where to write JSON summary ('-' for stdout when output is file)")
    args = ap.parse_args()

    src = args.input or args.beat_plan
    if not src:
        ap.error("provide --input or --beat-plan")

    data = load_json(Path(src))
    posts = posts_from_data(data)
    errs = validate(posts)

    if args.validate and errs:
        summary = {"validated": False, "errors": errs, "post_count": len(posts)}
        print(json.dumps(summary, ensure_ascii=False), file=sys.stdout)
        sys.exit(2)

    template_path = Path(args.template)
    if not template_path.exists():
        # try relative to skill root when invoked from repo root
        alt = Path("skills/2ch-writer") / args.template
        if alt.exists():
            template_path = alt
        else:
            print(json.dumps({"validated": False, "errors": [f"template not found: {args.template}"]}, ensure_ascii=False))
            sys.exit(2)

    out_html, posts = render(data, template_path)

    if args.output == "-":
        sys.stdout.write(out_html)
        summary_dest = sys.stderr
    else:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out_html, encoding="utf-8")
        summary_dest = sys.stdout if args.json_summary == "-" else open(args.json_summary, "w", encoding="utf-8")

    summary = {
        "output": args.output,
        "title": data.get("title", ""),
        "lang": data.get("lang", "ko"),
        "post_count": len(posts),
        "validated": not errs,
        "errors": errs,
        "bytes": len(out_html.encode("utf-8")),
        "template": str(template_path),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2), file=summary_dest)

if __name__ == "__main__":
    main()
