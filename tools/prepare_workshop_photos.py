# -*- coding: utf-8 -*-
"""Crop and compress workshop card photos.

    python tools/prepare_workshop_photos.py

Reads workshops/photos/<n>. <anything>.jfif|jpg|png — the leading number is the
workshop's position in WORKSHOPS (gen_workshops.py) — and writes
assets/img/workshops/<slug>.jpg at the card's aspect ratio.

Two things happen on the way in:

* the frame is cropped to 16:7.4, the .wcard-media ratio, so the browser is
  never asked to letterbox or squash;
* KEEP trims the bottom of the frame first. The image generator parked a
  "SHARED STYLE BLOCK" chrome bar along the bottom edge of several images —
  scaffolding from the prompt, not artwork — and this removes it. An image
  that arrives clean should be listed at 1.0.

Cards fall back to the generated SVG for any slug with no file here, so it is
safe to ship a partial set (see dropMissingPhotos in assets/js/main.js).
"""
import pathlib
import re
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "workshops" / "photos"
OUT = ROOT / "assets" / "img" / "workshops"
OUT.mkdir(parents=True, exist_ok=True)

RATIO = 16 / 7.4
MAX_BYTES = 180_000

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

# Images held back from the site. They are generated fine but carry defects the
# crop cannot fix — burnt-in English wording on a page that also renders in
# Arabic, prompt scaffolding the generator drew as UI chrome, a white ground
# that glares inside the dark card grid, or subject matter from the wrong
# domain. Their cards fall back to the generated SVG until the art is redone.
# Drop a slug from here once its replacement lands in workshops/photos/.
HOLD = {
    "smart-event-management-ai":
        "English labels throughout; 'SYSTEM KEY & STYLE GUIDE' scaffolding; "
        "misspelt 'Potentialial Audience'; dated 'ACADEMIC CONFERENCE 2024'",
    "institutional-innovation-ai":
        "matrix is labelled with software-backlog terms (Quick Win, Bug Fix, "
        "Maintenance Task) — not information-centre initiatives",
    "library-services-ai-ml":
        "English node labels burnt in",
    "strategic-planning-big-data":
        "large English headline burnt across the top",
    "technical-operations-digital-library":
        "white ground; English headline and stage labels",
    "integrated-library-systems":
        "white ground; modules read E-COMMERCE / WORKFLOW & TICKETS — wrong "
        "domain for an ILS workshop (should be circulation, acquisitions, "
        "serials, OPAC)",
    "digital-collections":
        "white ground; English headline",
    "information-document-security":
        "white ground; English headline; carries the caption from image 11",
}

# Fraction of the source height to keep, per workshop number.
KEEP = {1: .90, 2: .94, 3: .74, 4: .74, 5: .74, 6: 1.0, 7: .88,
        8: .74, 9: .74, 10: .86, 11: .86, 12: .86, 13: 1.0, 14: 1.0}


def prepare(src: pathlib.Path, dst: pathlib.Path, keep: float) -> tuple:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    im = im.crop((0, 0, w, round(h * keep)))
    w, h = im.size
    tw = round(h * RATIO)
    if tw <= w:                                   # centre-crop the width
        x = (w - tw) // 2
        im = im.crop((x, 0, x + tw, h))
    else:                                         # too tall: trim height
        im = im.crop((0, 0, w, round(w / RATIO)))
    quality = 84
    while True:
        im.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
        if dst.stat().st_size <= MAX_BYTES or quality <= 60:
            return im.size, dst.stat().st_size, quality
        quality -= 4


def sync_main_js():
    """Point main.js at exactly the photos that exist on disk.

    The cards skip the <img> entirely for a slug not in this set, so a
    workshop still waiting for its photo costs no failed request.
    """
    js = ROOT / "assets" / "js" / "main.js"
    text = js.read_text(encoding="utf-8")
    have = [s for s in SLUGS if (OUT / f"{s}.jpg").exists()]
    if have:
        listing = "".join('\n    "%s",' % s for s in have)
        body = "  const WORKSHOP_PHOTOS = new Set([%s\n  ]);" % listing
    else:
        body = "  const WORKSHOP_PHOTOS = new Set([]);"
    start = "  // WORKSHOP_PHOTOS:start\n"
    end = "  // WORKSHOP_PHOTOS:end"
    i = text.index(start) + len(start)
    j = text.index(end)
    js.write_text(text[:i] + body + "\n" + text[j:], encoding="utf-8")
    print("main.js: WORKSHOP_PHOTOS lists %d of %d workshops" % (len(have), len(SLUGS)))


def main():
    wanted = set(sys.argv[1:])                    # optional: only these numbers
    found = {}
    for p in SRC.iterdir():
        m = re.match(r"(\d+)", p.name)
        if m and p.suffix.lower() in (".jfif", ".jpg", ".jpeg", ".png"):
            found[int(m.group(1))] = p
    if not found:
        sys.exit(f"no numbered images in {SRC}")

    for n, slug in enumerate(SLUGS, 1):
        if n not in found or (wanted and str(n) not in wanted):
            continue
        if slug in HOLD:
            (OUT / f"{slug}.jpg").unlink(missing_ok=True)
            print(f"{n:2d} {slug:40s} HELD — {HOLD[slug]}")
            continue
        size, nbytes, q = prepare(found[n], OUT / f"{slug}.jpg", KEEP.get(n, 1.0))
        print(f"{n:2d} {slug:40s} {size[0]}x{size[1]}  {nbytes // 1024:3d}KB  q{q}")
    sync_main_js()


if __name__ == "__main__":
    main()
