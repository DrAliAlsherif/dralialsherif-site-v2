# Workshop card images — generation prompts

Artwork for the fourteen cards in the `#workshops` section. Six photos are live;
this file carries paste-ready prompts for the remaining eight.

## The one lesson from the first pass

Fourteen images came back and eight were rejected. The split was not random:

**Every prompt that described a *diagram* came back covered in words. Every
prompt that described a *scene* came back clean.**

The six that worked described objects and light — stacked cylinders, a
wireframe globe, book spines, coloured spheres, a manuscript under a camera,
a glowing vault. The eight that failed described charts and interfaces — a
value-versus-effort matrix, a timeline, a cycle-time meter, a hub of modules.
A chart has axes and axes have names, so the model wrote them: STRATEGIC
HORIZON PLANNING across the top of one, `E-COMMERCE` and `WORKFLOW & TICKETS`
on the library-systems one, and a misspelt *Potentialial Audience* on another.

It also drew the instructions. The words "shared style block" appeared as a
heading in this file, and the model painted a chrome bar reading SHARED STYLE
BLOCK along the bottom of eight images. One picked up the phrase *stage plane*
straight out of its own prompt and used it as a label.

So the eight prompts below are rewritten as **scenes, not diagrams**, each one
self-contained. Paste one whole and change nothing.

## Before you generate

| | |
|---|---|
| **Aspect** | Widest the tool offers — 21:9 if available, otherwise 16:9 |
| **Save as** | `workshops/photos/<number>. <anything>.jpg` — only the leading number matters |
| **Then run** | `python tools/prepare_workshop_photos.py` |

Two composition rules the prompts already carry, worth knowing why:

* **Both upper corners stay empty.** The card's number badge sits top-right in
  English and top-left in Arabic.
* **The bottom edge stays empty.** `prepare_workshop_photos.py` crops the lower
  part of the frame to reach the card's 16:7.4 ratio.

## Reject an image if

* it contains any writing at all — a headline, a label, a caption, a logo, or
  invented letter shapes;
* the background is white or light grey (it will glare inside the dark grid);
* the subject sits in a top corner or runs off the bottom edge;
* the content drifted out of the library and information world — generic
  business, e-commerce or software-project imagery.

Regenerate rather than accept. Cropping can rescue the bottom of a frame; it
can do nothing about a headline across the top.

---

# The eight prompts

## 1 — Smart Digital Transformation in Academic Event Management Using AI Tools
**التحول الرقمي الذكي في إدارة الفعاليات الأكاديمية باستخدام أدوات الذكاء الاصطناعي**

> A darkened lecture theatre viewed from a high angle. Rows of empty curved
> seating sweep around a single softly lit podium at the front. Above the
> podium a ribbon of luminous cyan light rises and curls forward through the
> air, dividing into four glowing translucent panes that hang suspended in the
> darkness. Faint violet particles drift between them. Dark cinematic 3D
> illustration on a deep navy-black background, lit only by glowing cyan and
> violet light, with soft volumetric haze and shallow depth of field. Subject
> centred, with empty space in both upper corners and along the bottom edge.
> Wide cinematic banner. Absolutely no text anywhere in the image — no words,
> letters, numbers, titles, captions, labels, legends, interface panels,
> buttons, logos or watermarks. Nothing written at all. Communicate only
> through shape, light and colour.

## 2 — Institutional Innovation with AI in Information & Research Centers
**الابتكار المؤسسي بالذكاء الاصطناعي في مراكز المعلومات والبحوث**

> A cluster of translucent glass cubes of varying size floating above a dark
> mirrored surface. The largest cubes glow bright cyan and hover highest; the
> smaller violet ones rest lower and half in shadow. To one side stands a
> laboratory flask made of light, releasing a slow stream of glowing particles
> that rise through the air and take the form of new cubes. Dark cinematic 3D
> illustration on a deep navy-black background, lit only by glowing cyan and
> violet light, with soft volumetric haze and shallow depth of field. Subject
> centred, with empty space in both upper corners and along the bottom edge.
> Wide cinematic banner. Absolutely no text anywhere in the image — no words,
> letters, numbers, titles, captions, labels, legends, interface panels,
> buttons, logos or watermarks. Nothing written at all. Communicate only
> through shape, light and colour.

## 3 — Developing Library Services Using AI & Machine Learning Tools
**تطوير خدمات المكتبات باستخدام أدوات الذكاء الاصطناعي والتعلم الآلي**

> An open book resting on a dark wooden desk, with a sphere of concentrated
> cyan light hovering just above its pages. Fine threads of light reach out
> from the sphere into the surrounding darkness, where they meet a graceful
> arc of translucent floating cards catching a violet glow. Deep shadow, soft
> haze. Dark cinematic 3D illustration on a deep navy-black background, lit
> only by glowing cyan and violet light, with soft volumetric haze and shallow
> depth of field. Subject centred, with empty space in both upper corners and
> along the bottom edge. Wide cinematic banner. Absolutely no text anywhere in
> the image — no words, letters, numbers, titles, captions, labels, legends,
> interface panels, buttons, logos or watermarks. Nothing written at all.
> Communicate only through shape, light and colour.

## 4 — Strategic Planning for Information Institutions in the Big-Data Era
**التخطيط الاستراتيجي لمؤسسات المعلومات في عصر البيانات الضخمة**

> A vast dark plain made of countless tiny glowing points of light stretching
> back to a distant horizon. Out of that field a single luminous cyan path
> rises and sweeps forward, then divides into two diverging routes of light,
> each ending at a softly glowing violet ring that floats above the horizon.
> Dark cinematic 3D illustration on a deep navy-black background, lit only by
> glowing cyan and violet light, with soft volumetric haze and shallow depth of
> field. Subject centred, with empty space in both upper corners and along the
> bottom edge. Wide cinematic banner. Absolutely no text anywhere in the image
> — no words, letters, numbers, titles, captions, labels, legends, interface
> panels, buttons, logos or watermarks. Nothing written at all. Communicate
> only through shape, light and colour.

## 5 — Managing Technical Operations in the Modern Digital Library
**إدارة العمليات الفنية في بيئة المكتبة الرقمية الحديثة**

> A row of tall dark arches receding into haze, each lit from within by a
> different colour of light — cyan, violet, pale blue. Along the floor a
> luminous rail runs through every arch, carrying a line of glowing
> translucent glass plates that travel from the foreground into the distance,
> each plate catching the colour of the arch it passes under. Dark cinematic
> 3D illustration on a deep navy-black background, lit only by glowing cyan
> and violet light, with soft volumetric haze and shallow depth of field.
> Subject centred, with empty space in both upper corners and along the bottom
> edge. Wide cinematic banner. Absolutely no text anywhere in the image — no
> words, letters, numbers, titles, captions, labels, legends, interface panels,
> buttons, logos or watermarks. Nothing written at all. Communicate only
> through shape, light and colour.

## 6 — Using & Managing Integrated Library Systems (ILS)
**استخدام وإدارة نظم المكتبات المتكاملة**

> A glowing cylindrical core of cyan light standing at the centre of a dark
> circular space. Floating around it at even intervals, lit by its glow, are
> five objects: a stack of books, a ring of light turning on itself, a fan of
> open journals, a polished glass lens, and a brass key. Fine beams of light
> connect each object back to the central core. Dark cinematic 3D illustration
> on a deep navy-black background, lit only by glowing cyan and violet light,
> with soft volumetric haze and shallow depth of field. Subject centred, with
> empty space in both upper corners and along the bottom edge. Wide cinematic
> banner. Absolutely no text anywhere in the image — no words, letters,
> numbers, titles, captions, labels, legends, interface panels, buttons, logos
> or watermarks. Nothing written at all. Communicate only through shape, light
> and colour.

*The five objects are the system's modules — circulation, acquisitions,
serials, discovery, permissions. Keep them as objects. The first attempt drew
labelled boxes and named two of them E-COMMERCE and WORKFLOW & TICKETS.*

## 7 — Building & Developing Digital Collections in Libraries
**بناء وتطوير المجموعات الرقمية في المكتبات**

> A tall dark wall of softly glowing translucent tiles arranged in a neat grid,
> with a few slots still empty. Out of the surrounding darkness several loose
> tiles drift through the air toward those empty places, trailing faint light.
> One tile caught in mid-flight glows brilliant cyan, far brighter than the
> rest. Dark cinematic 3D illustration on a deep navy-black background, lit
> only by glowing cyan and violet light, with soft volumetric haze and shallow
> depth of field. Subject centred, with empty space in both upper corners and
> along the bottom edge. Wide cinematic banner. Absolutely no text anywhere in
> the image — no words, letters, numbers, titles, captions, labels, legends,
> interface panels, buttons, logos or watermarks. Nothing written at all.
> Communicate only through shape, light and colour.

## 8 — Information & Document Security in Digital Environments
**أمن المعلومات والوثائق في البيئات الرقمية**

> A stack of translucent glowing sheets of paper floating in darkness, seen at
> a slight angle. Curving over them like a canopy is a broad, thin arc of cyan
> light. In front of the sheets hangs a fine web of crossing light beams, two
> of its nodes burning bright and one left dim. A small brass key rests below
> in deep shadow. Dark cinematic 3D illustration on a deep navy-black
> background, lit only by glowing cyan and violet light, with soft volumetric
> haze and shallow depth of field. Subject centred, with empty space in both
> upper corners and along the bottom edge. Wide cinematic banner. Absolutely no
> text anywhere in the image — no words, letters, numbers, titles, captions,
> labels, legends, interface panels, buttons, logos or watermarks. Nothing
> written at all. Communicate only through shape, light and colour.

---

## Numbering

`prepare_workshop_photos.py` reads the leading number as the workshop's
position in `WORKSHOPS` (`tools/gen_workshops.py`). The eight above are **not**
numbered 1–8 — save each under the number in this column:

| Prompt above | Save as number | Slug |
|---|---|---|
| 1 Academic Event Management | **1** | `smart-event-management-ai` |
| 2 Institutional Innovation | **2** | `institutional-innovation-ai` |
| 3 Library Services with AI & ML | **5** | `library-services-ai-ml` |
| 4 Strategic Planning | **6** | `strategic-planning-big-data` |
| 5 Technical Operations | **7** | `technical-operations-digital-library` |
| 6 Integrated Library Systems | **10** | `integrated-library-systems` |
| 7 Digital Collections | **11** | `digital-collections` |
| 8 Document Security | **12** | `information-document-security` |

Numbers 3, 4, 8, 9, 13 and 14 are the six already live — leave those alone.

## When an image is ready

1. Put it in `workshops/photos/` under its number from the table.
2. Delete that slug from `HOLD` in `tools/prepare_workshop_photos.py`.
3. Run `python tools/prepare_workshop_photos.py`.

It crops to the card ratio, compresses under 180 KB, and updates the photo list
in `main.js`. Until then the card shows its drawn illustration, so the grid is
never incomplete.
