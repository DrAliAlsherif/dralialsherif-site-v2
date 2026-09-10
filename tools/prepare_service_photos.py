# -*- coding: utf-8 -*-
"""Crop and compress the consulting service card photos.

    python tools/prepare_service_photos.py [n ...]

Reads "Consulting photos/<n>. <anything>" — the leading number is the service's
position in SERVICES (gen_services.py) — and writes
assets/img/services/<slug>.jpg at the .scard-art ratio. Pass numbers to redo
only those. All the real work is in tools/_photos.py.

Note the card geometry differs from the workshops': 16:8.4 rather than 16:7.4,
and the small round .sicon badge straddles the *bottom* edge of the picture on
the reading-start side, so these compositions keep their subject high and their
lower corners dark. tools/service-image-prompts.md carries the prompts.

The same images open each service page; run tools/gen_services.py after adding
one so the page picks it up.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _photos import run  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Order must match SERVICES in gen_services.py.
SLUGS = [
    "ai-consulting", "library-automation", "digital-repositories",
    "archive-consulting", "metadata-consulting", "training-programs",
    "research-consulting", "digital-transformation",
]

# Slugs to keep off the site without deleting their source, each with a reason.
HOLD = {}

# Fraction of the source height to keep. These arrived clean, so nothing is
# trimmed before the ratio crop.
KEEP = {}

if __name__ == "__main__":
    run(
        src_dir=ROOT / "Consulting photos",
        out_dir=ROOT / "assets" / "img" / "services",
        slugs=SLUGS, ratio=16 / 8.4,
        js_path=ROOT / "assets" / "js" / "main.js",
        js_marker="SERVICE_PHOTOS", js_const="SERVICE_PHOTOS",
        keep=KEEP, hold=HOLD, only=set(sys.argv[1:]),
    )
