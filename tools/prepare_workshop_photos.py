# -*- coding: utf-8 -*-
"""Crop and compress the workshop card photos.

    python tools/prepare_workshop_photos.py [n ...]

Reads workshops/photos/<n>. <anything> — the leading number is the workshop's
position in WORKSHOPS (gen_workshops.py) — and writes
assets/img/workshops/<slug>.jpg at the .wcard-media ratio. Pass numbers to
redo only those. All the real work is in tools/_photos.py.

The same images open each workshop page; run tools/gen_workshops.py after
adding one so the page picks it up.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _photos import run  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Order must match WORKSHOPS in gen_workshops.py.
SLUGS = [
    "smart-event-management-ai", "institutional-innovation-ai",
    "ai-prompt-engineering-libraries", "digital-repositories-standards",
    "library-services-ai-ml", "strategic-planning-big-data",
    "technical-operations-digital-library", "marc21-advanced-cataloging",
    "rda-lcsh-cataloging", "integrated-library-systems", "digital-collections",
    "information-document-security", "digital-preservation-manuscripts",
    "repositories-archiving-ai-open-access",
]

# Slugs to keep off the site without deleting their source. Empty now: the
# first pass had eight rejects (English wording burnt into images that also
# render on the Arabic page, prompt scaffolding drawn as UI chrome, white
# grounds inside a dark grid, wrong-domain subject matter) and all eight were
# reshot from the rewritten prompts in workshop-image-prompts.md.
HOLD = {}

# Only the four survivors of that first batch still carry the generator's
# chrome bar along their bottom edge; everything else keeps its full frame.
KEEP = {3: .74, 4: .74, 8: .74, 9: .74}

if __name__ == "__main__":
    run(
        src_dir=ROOT / "workshops" / "photos",
        out_dir=ROOT / "assets" / "img" / "workshops",
        slugs=SLUGS, ratio=16 / 7.4,
        js_path=ROOT / "assets" / "js" / "main.js",
        js_marker="WORKSHOP_PHOTOS", js_const="WORKSHOP_PHOTOS",
        keep=KEEP, hold=HOLD, only=set(sys.argv[1:]),
    )
