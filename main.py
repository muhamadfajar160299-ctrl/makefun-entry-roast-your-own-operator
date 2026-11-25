"""Roast Your Own Operator in One Line — entry runner.

Reads the single roast line from entry.txt next to this file and copies
it byte-for-byte into MAKEFUN_OUTPUT_DIR/entry.txt, so the grader sees
exactly the submitted line and nothing else.
"""
import os

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "entry.txt"), "rb") as source:
    line = source.read()
if not line.strip():
    raise SystemExit("entry.txt is empty")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.txt")
try:
    with open(out_path, "wb") as target:
        target.write(line)
    os.chmod(out_path, 0o644)
except OSError as exc:
    raise SystemExit(f"failed to write output: {exc}")
