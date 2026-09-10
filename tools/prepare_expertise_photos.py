# -*- coding: utf-8 -*-
"""Crop and compress the areas-of-expertise card photos.

    python tools/prepare_expertise_photos.py [n ...]

Reads "Areas of expertise/<n>. <anything>" — the leading number is the area's
position in AREAS (gen_expertise.py) — and writes
assets/img/expertise/<slug>.jpg at the .xart ratio. Pass numbers to redo only
those. All the real work is in tools/_photos.py.

The expertise card is the simplest of the three: 16:8.4 like the service card,
but with nothing overlapping it — no number, no icon badge — so these frames
need no dead corner. tools/expertise-image-prompts.md carries the prompts, and
explains why these read as places while the service images read as changes.

The same images open each expertise page; run tools/gen_expertise.py after
adding one so the page picks it up.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _photos import run  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Order must match AREAS in gen_expertise.py.
SLUGS = [
    "academic-libraries", "digital-repositories", "archives-preservation",
    "knowledge-management", "artificial-intelligence", "digital-transformation",
    "metadata-standards", "research-support", "training-capacity", "consulting",
]

# Slugs to keep off the site without deleting their source, each with a reason.
HOLD = {}

# Fraction of the source height to keep. These arrived clean, so nothing is
# trimmed before the ratio crop.
KEEP = {}

if __name__ == "__main__":
    run(
        src_dir=ROOT / "Areas of expertise",
        out_dir=ROOT / "assets" / "img" / "expertise",
        slugs=SLUGS, ratio=16 / 8.4,
        js_path=ROOT / "assets" / "js" / "main.js",
        js_marker="EXPERTISE_PHOTOS", js_const="EXPERTISE_PHOTOS",
        keep=KEEP, hold=HOLD, only=set(sys.argv[1:]),
    )
