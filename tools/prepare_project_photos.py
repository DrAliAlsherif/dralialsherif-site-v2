# -*- coding: utf-8 -*-
"""Crop and compress the project card photos.

    python tools/prepare_project_photos.py [n ...]

Reads "Projects photos/<n>. <anything>" — the leading number is the project's
position in DATA.projects (assets/js/main.js) — and writes
assets/img/projects/<slug>.jpg at the .pcard-media ratio. Pass numbers to redo
only those. All the real work is in tools/_photos.py.

Note the number is the order in DATA.projects, not the order the cards appear:
the grid groups them under four headings.

The project card is the widest band on the site, 16:6.6, with nothing
overlapping it. Projects have no detail pages, so these images show on the
cards only. tools/project-image-prompts.md carries the prompts, including why
these scenes stay abstract — the cards name real institutions, and an image
must never read as a photograph of one.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _photos import run  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Order must match DATA.projects in assets/js/main.js.
SLUGS = [
    "jumeira-repository", "cat-ai", "correctional-library", "mawahib-library",
    "heritage-center-library", "ministry-of-culture", "national-library",
    "tabah-foundation", "rta-library",
]

# Slugs to keep off the site without deleting their source, each with a reason.
HOLD = {}

# Fraction of the source height to keep. These arrived clean, so nothing is
# trimmed before the ratio crop.
KEEP = {}

if __name__ == "__main__":
    run(
        src_dir=ROOT / "Projects photos",
        out_dir=ROOT / "assets" / "img" / "projects",
        slugs=SLUGS, ratio=16 / 6.6,
        js_path=ROOT / "assets" / "js" / "main.js",
        js_marker="PROJECT_PHOTOS", js_const="PROJECT_PHOTOS",
        keep=KEEP, hold=HOLD, only=set(sys.argv[1:]),
    )
