# -*- coding: utf-8 -*-
"""One-off image optimisation for dralialsherif-site-v2.

    python tools/optimize_images.py            # compress in place
    python tools/optimize_images.py --dry-run  # just report

- JPEG/PNG under assets/img/ are downscaled to MAX_EDGE and re-encoded.
- EXIF/metadata is stripped.
- Generates the PWA / favicon PNGs under assets/img/icons/.
Re-running is safe (idempotent-ish): already-small files are skipped.
"""
import io
import sys
import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "assets" / "img"
ICON_DIR = IMG_DIR / "icons"
MAX_EDGE = 1600
JPEG_Q = 82
DRY = "--dry-run" in sys.argv


def human(n):
    for unit in ("B", "KB", "MB"):
        if n < 1024:
            return f"{n:.0f}{unit}"
        n /= 1024
    return f"{n:.1f}GB"


def optimise_one(p):
    before = p.stat().st_size
    try:
        im = Image.open(p)
    except Exception as e:
        print(f"  skip {p.name}: {e}")
        return 0, 0
    fmt = im.format
    w, h = im.size
    scale = min(1.0, MAX_EDGE / max(w, h))
    resized = scale < 1.0
    if resized:
        im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)

    if DRY:
        note = f"{w}x{h}" + (f" -> {im.size[0]}x{im.size[1]}" if resized else " (fits)")
        print(f"  {p.relative_to(ROOT)}  {human(before)}  {note}")
        return before, before

    if fmt == "JPEG":
        im = im.convert("RGB")
        save_kw = dict(format="JPEG", quality=JPEG_Q, optimize=True, progressive=True)
    elif fmt == "PNG":
        save_kw = dict(format="PNG", optimize=True)
    else:
        print(f"  skip {p.name}: unsupported format {fmt}")
        return before, before

    buf = io.BytesIO()
    im.save(buf, **save_kw)        # strips metadata by not passing exif
    data = buf.getvalue()
    if not resized and len(data) >= before:
        print(f"  {p.relative_to(ROOT)}  {human(before)} (already optimal, kept)")
        return before, before
    p.write_bytes(data)
    after = len(data)
    print(f"  {p.relative_to(ROOT)}  {human(before)} -> {human(after)}"
          + (f"  ({im.size[0]}x{im.size[1]})" if resized else ""))
    return before, after


def make_icons():
    ICON_DIR.mkdir(parents=True, exist_ok=True)
    for size, name in [(32, "favicon-32.png"), (180, "apple-touch-icon.png"),
                       (192, "favicon-192.png"), (512, "favicon-512.png")]:
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        r = round(size * 0.22)
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(79, 70, 229, 255))
        try:
            font = ImageFont.truetype("georgiab.ttf", int(size * 0.62))
        except Exception:
            try:
                font = ImageFont.truetype("arialbd.ttf", int(size * 0.58))
            except Exception:
                font = ImageFont.load_default()
        tb = d.textbbox((0, 0), "A", font=font)
        tw, th = tb[2] - tb[0], tb[3] - tb[1]
        d.text(((size - tw) / 2 - tb[0], (size - th) / 2 - tb[1]), "A", font=font, fill="white")
        if not DRY:
            img.save(ICON_DIR / name)
        print(f"  icon {name} ({size}px){' [dry]' if DRY else ''}")


def main():
    exts = {".jpg", ".jpeg", ".png"}
    files = [p for p in IMG_DIR.rglob("*") if p.suffix.lower() in exts and ICON_DIR not in p.parents]
    tot_b = tot_a = 0
    print(f"{'DRY RUN — ' if DRY else ''}optimising {len(files)} images under assets/img/ ...")
    for p in sorted(files):
        b, a = optimise_one(p)
        tot_b += b
        tot_a += a
    print(f"\ntotal: {human(tot_b)} -> {human(tot_a)}  (saved {human(max(0, tot_b - tot_a))})")
    print("\nicons:")
    make_icons()


if __name__ == "__main__":
    main()
