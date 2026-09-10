# -*- coding: utf-8 -*-
"""Shared machinery for turning generated artwork into card photos.

Both prepare_workshop_photos.py and prepare_service_photos.py are thin
configuration on top of this: a source folder of numbered images, a slug list
in card order, the card's aspect ratio, and where the photos go.

The number leading each source filename is the item's position in its section,
so the artwork can be reshot one at a time without renaming anything else.

Cards fall back to their generated SVG for any slug with no photo, so a partial
set ships safely — see dropMissingPhotos in assets/js/main.js.
"""
import pathlib
import re

from PIL import Image

MAX_BYTES = 180_000
SUFFIXES = (".jfif", ".jpg", ".jpeg", ".png", ".webp")


def discover(src_dir: pathlib.Path) -> dict:
    """Map the leading number of each image filename to its path."""
    found = {}
    if not src_dir.is_dir():
        return found
    for p in src_dir.iterdir():
        m = re.match(r"(\d+)", p.name)
        if m and p.suffix.lower() in SUFFIXES:
            found[int(m.group(1))] = p
    return found


def prepare(src: pathlib.Path, dst: pathlib.Path, ratio: float,
            keep: float = 1.0) -> tuple:
    """Crop `src` to `ratio` and write it to `dst` under MAX_BYTES.

    `keep` trims the bottom of the frame before anything else. The first batch
    of generated artwork carried a chrome bar along its lower edge — scaffolding
    the model read out of the prompt and drew — and this removes it. Clean
    artwork keeps the default 1.0.

    Whichever dimension is then in surplus is cropped: extra width comes off
    both sides evenly, extra height comes off the bottom, since these
    compositions put their subject in the upper part of the frame.
    """
    with Image.open(src) as im:
        im = im.convert("RGB")
        w, h = im.size
        if keep < 1.0:
            im = im.crop((0, 0, w, round(h * keep)))
            w, h = im.size
        target_w = round(h * ratio)
        if target_w <= w:
            x = (w - target_w) // 2
            im = im.crop((x, 0, x + target_w, h))
        else:
            im = im.crop((0, 0, w, round(w / ratio)))

        quality = 84
        dst.parent.mkdir(parents=True, exist_ok=True)
        while True:
            im.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
            if dst.stat().st_size <= MAX_BYTES or quality <= 60:
                return im.size, dst.stat().st_size, quality
            quality -= 4


def sync_js(js_path: pathlib.Path, marker: str, const: str, slugs: list) -> int:
    """Rewrite the `const` set between the marker comments in main.js.

    The card skips its <img> entirely for a slug not in the set, so an item
    still waiting for artwork costs no failed request.
    """
    text = js_path.read_text(encoding="utf-8")
    if slugs:
        listing = "".join('\n    "%s",' % s for s in slugs)
        body = "  const %s = new Set([%s\n  ]);" % (const, listing)
    else:
        body = "  const %s = new Set([]);" % const
    start, end = "  // %s:start\n" % marker, "  // %s:end" % marker
    i = text.index(start) + len(start)
    j = text.index(end)
    js_path.write_text(text[:i] + body + "\n" + text[j:], encoding="utf-8")
    return len(slugs)


def run(*, src_dir, out_dir, slugs, ratio, js_path, js_marker, js_const,
        keep=None, hold=None, only=None) -> None:
    """Prepare every image present, then point main.js at the results."""
    keep, hold = keep or {}, hold or {}
    found = discover(src_dir)
    if not found:
        raise SystemExit(f"no numbered images in {src_dir}")

    for n, slug in enumerate(slugs, 1):
        if n not in found or (only and str(n) not in only):
            continue
        if slug in hold:
            (out_dir / f"{slug}.jpg").unlink(missing_ok=True)
            print(f"{n:2d} {slug:40s} HELD - {hold[slug]}")
            continue
        size, nbytes, q = prepare(found[n], out_dir / f"{slug}.jpg",
                                  ratio, keep.get(n, 1.0))
        print(f"{n:2d} {slug:40s} {size[0]}x{size[1]}  {nbytes // 1024:3d}KB  q{q}")

    have = [s for s in slugs if (out_dir / f"{s}.jpg").exists()]
    sync_js(js_path, js_marker, js_const, have)
    print(f"main.js: {js_const} lists {len(have)} of {len(slugs)}")
