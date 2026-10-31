"""python3 validate.py — every suite parses and matches the record format in README.md."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
bad = 0
for p in sorted(ROOT.rglob("eval.jsonl")):
    n = reviewed = 0
    for i, line in enumerate(open(p), 1):
        try:
            r = json.loads(line)
            m = r["messages"]
            assert [x["role"] for x in m] == ["user", "assistant"], "roles must be user, assistant"
            assert all(x["content"].strip() for x in m), "empty content"
            assert isinstance(r["reviewed"], bool), "reviewed must be true or false"
            reviewed += r["reviewed"]
        except (ValueError, KeyError, AssertionError, TypeError) as e:
            print(f"{p.relative_to(ROOT)}:{i}: {e}"); bad += 1
        n = i
    print(f"{p.relative_to(ROOT)}: {n} questions, {reviewed} human-reviewed")
sys.exit(bad > 0)
