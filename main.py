import os

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "entry.txt"), "rb") as source:
    line = source.read()
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "wb") as target:
    target.write(line)
