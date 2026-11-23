"""news-image-20261124 entry: write the day's news image to /output/entry.png."""
import os
import shutil

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(__file__.replace("main.py", "entry.png"), os.path.join(OUT, "entry.png"))
print("entry.png written to", OUT)
