#!/usr/bin/env python3
"""Convert a project's docs/TASKS.md into the dashboard `milestones` array (JSON on stdout).

Usage: tasks2dash.py <path/to/TASKS.md> [extra JSON fields to merge, e.g. '{"state":"active"}']
Prints a JSON object {"milestones": [...], "updatedAt": "..."} (+ extras) ready for ArtifactData update.
"""
import datetime, json, re, sys

ms, cur = [], None
for line in open(sys.argv[1], encoding="utf-8"):
    m = re.match(r"^## (M\d+)\s*[–-]\s*(.+)$", line.strip())
    if m:
        cur = {"code": m.group(1), "title": m.group(2).strip(), "tasks": []}
        ms.append(cur)
        continue
    t = re.match(r"^- \[([ x~])\]\s*(?:\*\*)?(T\d+\.\d+)\s+(.+?)(?:\*\*)?\s*(?:[–-]\s|$)", line.strip())
    if t and cur is not None:
        title = t.group(3).strip().rstrip("*").strip()
        cur["tasks"].append({"id": t.group(2), "title": title, "done": t.group(1) == "x"})
out = {"milestones": ms, "updatedAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
if len(sys.argv) > 2:
    out.update(json.loads(sys.argv[2]))
print(json.dumps(out, ensure_ascii=False))
