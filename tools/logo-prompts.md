# Brand mark — concepts and generation prompts

The `AF` badge beside the name. It appears in three places, and the third one
decides everything:

| Where | Size | Files |
|---|---|---|
| Home page header and footer | 42 px | `index.html` |
| Every sub-page header | 40 px | ~78 pages |
| **Favicon** | **16 px** | inlined into all 78 pages |

## Read this before generating anything

**A logo has to be vector, and an image generator cannot give you one.**

Image tools return a 1024 px raster with soft glows, gradients and shadows.
At 16 px that becomes a smudge, and the mark also has to sit transparently on
the brand gradient rather than carry its own background. So:

* generate images to **explore a direction**, not to ship;
* whichever direction wins, I redraw it as SVG — a few hundred bytes, sharp at
  every size, inlined as the favicon exactly like the current one.

The mark also has to survive being **white on the indigo-to-cyan gradient**, so
it must work as a single flat colour with no interior shading.

## Test any candidate at 16 px first

If it does not read at 16, nothing else about it matters. Squint at it. Three
or four elements maximum, no thin hairlines, no small gaps.

---

# The six concepts

Rendered at 84 px, 42 px, 16 px and in the header lockup.

## A — Layered records ★ recommended

Three stacked plates seen in slight perspective, the top one solid and the two
beneath progressively fainter. Reads as deposited layers, an archive, a
repository — and it echoes the stacked-cylinder artwork already used across the
site's repository pages. Sharp at 16 px because it is three simple shapes.

> A minimal flat vector app icon: three stacked rhombus plates seen in slight
> isometric perspective, evenly spaced one above another, the topmost solid and
> the two below progressively more transparent. Pure white on a plain
> transparent background, single flat colour, no gradients, no shading, no
> outline, no glow, no shadow. Bold simple geometry with thick even weight,
> generous spacing, centred in a square frame with clear margin on all sides.
> Designed to stay legible at 16 pixels. Absolutely no text, no letters, no
> numbers, no watermark.

## B — Open book

Two facing pages. Honest and instantly legible, but it is the most expected
mark in the field; a search for library logos returns a thousand of these.

> A minimal flat vector app icon: an open book seen from the front, two facing
> pages curving away from a centre gutter, drawn as two clean strokes with even
> thickness. Pure white on a plain transparent background, single flat colour,
> no gradients, no shading, no glow, no shadow. Bold simple geometry, centred
> in a square frame with clear margin on all sides. Designed to stay legible at
> 16 pixels. Absolutely no text, no letters, no numbers, no watermark.

## C — Book and node

An open book with a single filled node rising from the gutter on a short stem.
Says library and artificial intelligence in one mark — closest to how the
practice actually describes itself. Slightly busier; at 16 px the node reads as
a dot, which still works.

> A minimal flat vector app icon: an open book with two facing pages, and
> directly above its centre gutter a single filled circle joined to the book by
> a short straight stem. Pure white on a plain transparent background, single
> flat colour, no gradients, no shading, no glow, no shadow. Bold simple
> geometry with even stroke weight, centred in a square frame with clear margin
> on all sides. Designed to stay legible at 16 pixels. Absolutely no text, no
> letters, no numbers, no watermark.

## D — Structured record

A tall bracket on each side with three dots stacked between them. Reads as a
delimited, structured record — metadata, cataloguing. Very sharp at small
sizes, but it reads more like code than like a library.

> A minimal flat vector app icon: two tall square brackets facing each other,
> one on the left and one on the right, with three evenly spaced filled circles
> stacked vertically between them. Pure white on a plain transparent
> background, single flat colour, no gradients, no shading, no glow, no shadow.
> Bold simple geometry with even stroke weight, centred in a square frame with
> clear margin on all sides. Designed to stay legible at 16 pixels. Absolutely
> no text, no letters, no numbers, no watermark.

## E — Shelf with one volume lit

Three book spines standing on a shelf line, the middle one taller and solid.
Warm and human, but at 16 px it collapses into something that reads as a bar
chart — an analytics icon, not a library one.

> A minimal flat vector app icon: three upright rounded rectangles of differing
> heights standing side by side on a horizontal base line, like book spines on
> a shelf, with the taller middle one filled solid and the outer two drawn as
> outlines. Pure white on a plain transparent background, single flat colour,
> no gradients, no shading, no glow, no shadow. Bold simple geometry, centred
> in a square frame with clear margin on all sides. Designed to stay legible at
> 16 pixels. Absolutely no text, no letters, no numbers, no watermark.

## F — The monogram, reset

Keep `AF`, but set in Sora at the right weight and tracking rather than the
current default. Cheapest option and perfectly legible — it just says nothing
about the work.

No prompt needed; this one is typography, and I set it directly.

---

## My recommendation

**A**, with **C** as the alternative if you want the AI half of the practice
stated openly rather than implied.

A wins on the thing that actually matters here: it is three shapes, so it holds
together at 16 px where B and C start to close up and E turns into a chart. It
is also the only one that is not a stock library symbol, and it already rhymes
with the repository artwork used across the site.

## What happens next

Tell me a letter and I will draw it as SVG and put it everywhere in one pass:
both marks on the home page, the mark on all 78 sub-page headers, and the
inlined favicon — which currently draws a serif `A` and would otherwise stay
out of step with the new mark.

If you would rather explore first, generate from a prompt above, send the
image, and I will redraw the winner as vector.
