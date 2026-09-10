# Consulting service card images — generation prompts

Artwork for the eight cards in the `#services` section, to replace the SVG
diagrams they show now. Same approach that worked for the workshop cards; the
card geometry differs, so read the composition rules before generating.

## The rule that decides whether this works

**Describe a scene, not a diagram.**

On the workshop set, every prompt that described a chart came back covered in
burnt-in English — headlines, axis names, and in one case an invented
misspelling. Every prompt that described objects and light came back clean. A
chart has axes and axes have names, so the model writes them. The eight below
are written as scenes for that reason, and each one is self-contained: paste it
whole and change nothing.

## Before you generate

| | |
|---|---|
| **Aspect** | 1600 × 840 px (the card is `aspect-ratio: 16/8.4`) — or 16:9, close enough to crop |
| **Save as** | `workshops/photos3/<number>. <anything>.jpg` — only the leading number matters |
| **Then tell me** | I'll crop, compress and wire them into the cards |

## Composition — this differs from the workshop cards

The workshop cards keep their **top** corners clear for a number badge. Service
cards have no number. Instead a small round icon straddles the **bottom edge**
of the picture, about a fifth of the way in from the side — and which side
flips with the language, left in English and right in Arabic.

So: **keep both lower corners quiet.** Put the subject centred and in the upper
two-thirds of the frame, and leave the bottom strip calm and dark. Nothing
important in the bottom-left or bottom-right.

## Reject an image if

* it contains any writing at all — a headline, a label, a caption, a logo, or
  invented letter shapes;
* the background is white or light grey (it will glare inside the dark grid);
* the subject sits low enough that the icon badge would cover it;
* it drifts out of the library and information world into generic business,
  e-commerce or software-project imagery.

Regenerate rather than accept. Cropping can rescue an edge; it can do nothing
about a headline through the middle.

---

# The eight prompts

## 1 — AI Consulting
**استشارات الذكاء الاصطناعي**

*Scattered experimentation becoming structured, governed adoption.*

> A dark room in which dozens of small glowing fragments drift at random,
> scattered and unaligned. Drawn by some unseen order they gather toward the
> centre and settle into a single luminous ordered lattice, precise and calm.
> A faint translucent dome of light encloses the finished lattice, protecting
> it. Dark cinematic 3D illustration on a deep navy-black background, lit only
> by glowing cyan and violet light, with soft volumetric haze and shallow depth
> of field. Subject centred and sitting in the upper two-thirds of the frame,
> with the lower-left and lower-right corners left dark and empty. Wide
> cinematic banner. Absolutely no text anywhere in the image — no words,
> letters, numbers, titles, captions, labels, legends, interface panels,
> buttons, logos or watermarks. Nothing written at all. Communicate only
> through shape, light and colour.

## 2 — Library Automation
**أتمتة المكتبات**

*The card catalogue becoming the integrated system.*

> A dim library aisle between tall shelves of books, receding into shadow. In
> the foreground stands an old wooden card-catalogue cabinet with one drawer
> open. Out of that drawer a stream of glowing cyan light rises, carrying
> luminous translucent rectangles that flow down the aisle and settle into a
> softly glowing cylinder of light standing at the far end. Dark cinematic 3D
> illustration on a deep navy-black background, lit only by glowing cyan and
> violet light, with soft volumetric haze and shallow depth of field. Subject
> centred and sitting in the upper two-thirds of the frame, with the lower-left
> and lower-right corners left dark and empty. Wide cinematic banner.
> Absolutely no text anywhere in the image — no words, letters, numbers,
> titles, captions, labels, legends, interface panels, buttons, logos or
> watermarks. Nothing written at all. Communicate only through shape, light and
> colour.

## 3 — Digital Repository Development
**تطوير المستودعات الرقمية**

*Structured deposit, linked records, open access.*

> Tall translucent columns of light rising from a dark floor, each column built
> from many stacked glowing plates like strata. Fine threads of light run
> between the columns, connecting matching plates across them. From the tallest
> column a broad shaft of light rises freely into the darkness above and
> disperses. Dark cinematic 3D illustration on a deep navy-black background,
> lit only by glowing cyan and violet light, with soft volumetric haze and
> shallow depth of field. Subject centred and sitting in the upper two-thirds
> of the frame, with the lower-left and lower-right corners left dark and
> empty. Wide cinematic banner. Absolutely no text anywhere in the image — no
> words, letters, numbers, titles, captions, labels, legends, interface panels,
> buttons, logos or watermarks. Nothing written at all. Communicate only
> through shape, light and colour.

## 4 — Archive Consulting
**استشارات الأرشيف**

*The vault, and what comes out of it.*

> A long dark vault lined with rows of grey archival boxes receding into
> shadow on both sides. One box near the foreground stands open, and from it a
> slow column of glowing translucent documents rises into the air, each sheet
> catching a thin horizontal line of cyan light as it passes upward. Dark
> cinematic 3D illustration on a deep navy-black background, lit only by
> glowing cyan and violet light, with soft volumetric haze and shallow depth of
> field. Subject centred and sitting in the upper two-thirds of the frame, with
> the lower-left and lower-right corners left dark and empty. Wide cinematic
> banner. Absolutely no text anywhere in the image — no words, letters,
> numbers, titles, captions, labels, legends, interface panels, buttons, logos
> or watermarks. Nothing written at all. Communicate only through shape, light
> and colour.

## 5 — Metadata Consulting
**استشارات الميتاداتا**

*Disordered records resolving into clean, deduplicated rows.*

> A dark space filled with hundreds of small luminous shards floating at random
> angles, tumbled and uneven. Moving toward the right they turn and align,
> resolving into perfectly ordered parallel rows of light. Where two identical
> shards meet on the way they merge into a single brighter one. Dark cinematic
> 3D illustration on a deep navy-black background, lit only by glowing cyan and
> violet light, with soft volumetric haze and shallow depth of field. Subject
> centred and sitting in the upper two-thirds of the frame, with the lower-left
> and lower-right corners left dark and empty. Wide cinematic banner.
> Absolutely no text anywhere in the image — no words, letters, numbers,
> titles, captions, labels, legends, interface panels, buttons, logos or
> watermarks. Nothing written at all. Communicate only through shape, light and
> colour.

## 6 — Training Programs
**البرامج التدريبية**

*Capability that spreads and keeps spreading.*

> A dark space holding one sphere of warm cyan light. Fine threads reach out
> from it to a ring of smaller, dimmer spheres, and as each thread lands its
> sphere kindles into light and begins sending threads of its own outward into
> the darkness beyond. Dark cinematic 3D illustration on a deep navy-black
> background, lit only by glowing cyan and violet light, with soft volumetric
> haze and shallow depth of field. Subject centred and sitting in the upper
> two-thirds of the frame, with the lower-left and lower-right corners left
> dark and empty. Wide cinematic banner. Absolutely no text anywhere in the
> image — no words, letters, numbers, titles, captions, labels, legends,
> interface panels, buttons, logos or watermarks. Nothing written at all.
> Communicate only through shape, light and colour.

## 7 — Research Consulting
**الاستشارات البحثية**

*One piece of work finding its reach.*

> A vast dark expanse holding a slowly turning constellation of connected
> points of light, dense at the centre and thinning outward into the dark. One
> point near the foreground burns brighter than the rest, and fine luminous
> threads run from it outward, tracing paths through the whole constellation to
> the most distant points. Dark cinematic 3D illustration on a deep navy-black
> background, lit only by glowing cyan and violet light, with soft volumetric
> haze and shallow depth of field. Subject centred and sitting in the upper
> two-thirds of the frame, with the lower-left and lower-right corners left
> dark and empty. Wide cinematic banner. Absolutely no text anywhere in the
> image — no words, letters, numbers, titles, captions, labels, legends,
> interface panels, buttons, logos or watermarks. Nothing written at all.
> Communicate only through shape, light and colour.

## 8 — Digital Transformation
**التحول الرقمي**

*The heavy old thing becoming the light new one.*

> A dark plain on which a heavy structure of dull grey stone stands to one
> side. Its surface is dissolving into countless small particles of light that
> drift across the air and re-form on the other side into a lighter, luminous
> architecture of clean glowing lines. The two states stand together, mid
> transformation. Dark cinematic 3D illustration on a deep navy-black
> background, lit only by glowing cyan and violet light, with soft volumetric
> haze and shallow depth of field. Subject centred and sitting in the upper
> two-thirds of the frame, with the lower-left and lower-right corners left
> dark and empty. Wide cinematic banner. Absolutely no text anywhere in the
> image — no words, letters, numbers, titles, captions, labels, legends,
> interface panels, buttons, logos or watermarks. Nothing written at all.
> Communicate only through shape, light and colour.

---

## File names

Save each under its number below. The number is the service's position in the
`#services` grid, which is the order in `SERVICES` in `tools/gen_services.py` —
the same order the prompts appear above, so numbering is 1 to 8 straight down.

| # | Save as | Becomes |
|---|---|---|
| 1 | `1. AI Consulting.jpg` | `assets/img/services/ai-consulting.jpg` |
| 2 | `2. Library Automation.jpg` | `assets/img/services/library-automation.jpg` |
| 3 | `3. Digital Repository Development.jpg` | `assets/img/services/digital-repositories.jpg` |
| 4 | `4. Archive Consulting.jpg` | `assets/img/services/archive-consulting.jpg` |
| 5 | `5. Metadata Consulting.jpg` | `assets/img/services/metadata-consulting.jpg` |
| 6 | `6. Training Programs.jpg` | `assets/img/services/training-programs.jpg` |
| 7 | `7. Research Consulting.jpg` | `assets/img/services/research-consulting.jpg` |
| 8 | `8. Digital Transformation.jpg` | `assets/img/services/digital-transformation.jpg` |

## When they're ready

Put them in `workshops/photos3/` and say so. I'll add a `prepare_service_photos.py`
mirroring the workshop one — crop to 16:8.4, compress under 180 KB, and layer
each photo over the existing SVG on both the card and the service page, in both
languages. Any service still without a photo keeps its drawing, so the grid is
never half-finished.

Sources stay out of git: `.nojekyll` means anything committed is served
publicly, and full-frame originals have no use to the site.
