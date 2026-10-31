"""python3 validate.py — every suite parses and matches the record format in README.md."""
import json
import sys
from pathlib import Path

bad = 0
for p in sorted(Path(__file__).parent.rglob("eval.jsonl")):
    n = 0
    for i, line in enumerate(open(p), 1):
        where = f"{p.relative_to(Path(__file__).parent)}:{i}"
        try:
            m = json.loads(line)["messages"]
            assert [x["role"] for x in m] == ["user", "assistant"], "roles must be user, assistant"
            assert all(x["content"].strip() for x in m), "empty content"
        except (ValueError, KeyError, AssertionError, TypeError) as e:
            print(f"{where}: {e}"); bad += 1
        n = i
    print(f"{p.relative_to(Path(__file__).parent)}: {n} questions")
sys.exit(bad > 0)
