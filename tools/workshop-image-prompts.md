# Workshop card images — generation prompts

Prompts for the 14 images that replace the repeated SVG diagrams on the
`#workshops` cards. Today the art is chosen by keyword (`workshopTheme()` in
`assets/js/main.js`), so only **7 drawings** cover 14 workshops — four of them
share the same neural-net. One image per workshop fixes that.

## How to use this

1. Generate each image with the prompt below.
2. Save it as **exactly** the filename given, into `assets/img/workshops/`.
3. Tell me they're in — I'll wire them into the cards (both languages), with
   `width`/`height` set, `loading="lazy"`, and the current SVG kept as the
   fallback for any image that isn't there yet.
4. Run `python tools/optimize_images.py` to compress before committing.

## Output spec — the same for all 14

| | |
|---|---|
| **Size** | 1600 × 740 px (the card is `aspect-ratio: 16/7.4`) |
| **Format** | JPG, quality ~82, aim under 180 KB |
| **Folder** | `assets/img/workshops/` |

## Two hard rules

**No text, letters, numbers or logos anywhere in the image.** The cards render
in both Arabic and English from the same file, so any baked-in wording would be
wrong in one of them — and the card already overlays its own number badge.

**Keep both top corners quiet.** The number badge (01, 02, …) sits in the top
*right* in English and the top *left* in Arabic, because it is positioned with
`inset-inline-end`. Leave roughly 15% clear at the top on both sides — put the
subject centred or slightly low.

## What went wrong on the first pass — read this before regenerating

Fourteen images came back; **six shipped, eight were held**. The failures were
not random, and two causes account for all of them.

**1. The generator drew the instructions.** It read the words "shared style
block" as a thing to depict and painted a chrome bar labelled SHARED STYLE
BLOCK along the bottom of eight images. Image 1 got a "SYSTEM KEY & STYLE
GUIDE" legend and a label reading *stage plane* — a phrase lifted straight out
of its own prompt. So: **never paste the style block as prose the model can
read as content.** Paste it as plain adjectives, or generate first and restyle
after. The heading "shared style block" must not appear in the box you type
into.

**2. "No text" has to be repeated at the end, not just the start.** Models
weight the tail of a prompt. Twelve of fourteen came back with English wording
burnt in — headlines like STRATEGIC HORIZON PLANNING, axis labels, and in one
case a misspelling (*Potentialial Audience*) and a wrong year (2024). On a page
that also renders in Arabic, none of that can be corrected later.

Also worth checking every time:

* **Ground colour.** Four came back on white and glared inside the dark card
  grid. Say *dark navy background* twice.
* **Domain.** The ILS image labelled its modules E-COMMERCE and WORKFLOW &
  TICKETS. Name the real ones — circulation, acquisitions, serials, OPAC — and
  reject anything generic.
* **Cropping saves the bottom, never the top.** `prepare_workshop_photos.py`
  trims the lower part of the frame, which removed the chrome bar from four
  otherwise good images. A headline across the top cannot be rescued.

### The line to append to every prompt

> Absolutely no text of any kind: no titles, headings, captions, labels,
> annotations, legends, axis names, UI panels, logos or watermarks. No letters
> or numbers anywhere in the frame. Dark navy background. Communicate entirely
> through shape, colour and composition.

## Shared style block

Append this to every prompt so the 14 read as one set — **as description
only**. Do not include the words "shared style block"; the generator drew that
heading into eight of the first fourteen images.

> Dark editorial tech illustration on a deep navy background (#060814 to
> #101534 vertical gradient). Thin luminous line-work, 2px strokes, generous
> negative space, subtle dot-grid texture. Accent palette only: indigo #6d5efc,
> violet #a78bfa, cyan #22d3ee, with a soft cyan glow on focal points. Flat
> vector / isometric-diagram feel — no photorealism, no 3-D render, no
> gradients inside shapes, no people's faces, no text, no letters, no numbers,
> no logos, no watermarks. Composition centred and calm, clear of the top-left
> and top-right corners. Wide banner, 16:7.4.

---

## 1. Smart Digital Transformation in Academic Event Management Using AI Tools
**التحول الرقمي الذكي في إدارة الفعاليات الأكاديمية باستخدام أدوات الذكاء الاصطناعي**

`assets/img/workshops/smart-event-management-ai.jpg`

> An abstract academic conference seen as a system: a shallow curved auditorium
> of empty seat-arcs facing a lit stage plane on the left; from the stage a
> glowing ribbon timeline flows right and branches into four floating rounded
> session panels; above them a small radial gauge cluster pulses with live
> registration and attendance arcs; a lanyard badge outline drifts at the lower
> right. + shared style block

## 2. Institutional Innovation with AI in Information & Research Centers
**الابتكار المؤسسي بالذكاء الاصطناعي في مراكز المعلومات والبحوث**

`assets/img/workshops/institutional-innovation-ai.jpg`

> A value-versus-effort decision matrix drawn as a luminous two-axis grid, with
> six rounded initiative cards plotted across it at different sizes and glow
> intensities, the brightest clustered in the high-value quadrant; a small
> laboratory flask icon sits beside the grid emitting three rising particles
> that turn into a stepped upward path leading off to the right. + shared style
> block

## 3. AI Prompt Engineering for Libraries: From Fundamentals to Practical Models
**هندسة أوامر الذكاء الاصطناعي للمكتبات: من الأساسيات إلى النماذج التطبيقية**

`assets/img/workshops/ai-prompt-engineering-libraries.jpg`

> A structured prompt shown as architecture: four stacked rounded blocks of
> different widths on the left, connected by a bright cyan channel into a
> glowing hexagonal core in the centre; out of the core three refined output
> streams fan to the right and settle onto a row of upright book spines. Blocks
> are blank plates — suggest structure through shape and rhythm, never through
> writing. + shared style block

## 4. Planning & Building Digital Repositories Based on Global Standards
**تخطيط وبناء المستودعات الرقمية وفق المعايير العالمية**

`assets/img/workshops/digital-repositories-standards.jpg`

> Three stacked translucent database cylinders on the left, rising like strata;
> a deposit workflow of four small chevron gates flows into them from below; on
> the right a thin wireframe globe is encircled by an orbiting harvest ring that
> throws light lines back toward the cylinders; a single open padlock outline
> floats above the stack, glowing cyan. + shared style block

## 5. Developing Library Services Using AI & Machine Learning Tools
**تطوير خدمات المكتبات باستخدام أدوات الذكاء الاصطناعي والتعلم الآلي**

`assets/img/workshops/library-services-ai-ml.jpg`

> A library service counter reduced to a simple lit plane on the left, with a
> rounded speech-bubble outline hovering above it pulsing cyan; from the bubble
> a recommendation fan spreads right — five rounded resource tiles at graded
> brightness arranged in an arc; beneath the fan a soft usage curve rises with
> three node points. + shared style block

## 6. Strategic Planning for Information Institutions in the Big-Data Era
**التخطيط الاستراتيجي لمؤسسات المعلومات في عصر البيانات الضخمة**

`assets/img/workshops/strategic-planning-big-data.jpg`

> A wide strategic horizon: a low grid plane in perspective with four ascending
> bars on the left; from the tallest bar a bright path travels right and forks
> into two divergent scenario branches, each ending in a small ringed target;
> a dense field of tiny data particles drifts beneath the plane, condensing into
> the bars. A thin compass rose sits low and centred. + shared style block

## 7. Managing Technical Operations in the Modern Digital Library
**إدارة العمليات الفنية في بيئة المكتبة الرقمية**

`assets/img/workshops/technical-operations-digital-library.jpg`

> A horizontal processing pipeline: rounded record plates travel left to right
> along a lit rail through four station gates, each gate marked by a different
> simple geometric head — a funnel, a pair of interlocking gears, a check
> diamond, an outbound arrow; above the rail a slim cycle-time meter runs the
> full width with one bright marker. + shared style block

## 8. Automated Cataloging Using MARC 21: Advanced Applications
**الفهرسة الآلية باستخدام مارك 21: تطبيقات متقدمة**

`assets/img/workshops/marc21-advanced-cataloging.jpg`

> A dense bibliographic record rendered as pure structure: three tall columns of
> short horizontal bars at varying lengths and brightness, like fields and
> subfields, standing side by side; graceful curved link arcs spring between
> bars across the columns; a translucent bright band sweeps horizontally across
> all three columns, suggesting a batch edit passing through. Bars are abstract
> marks, never characters. + shared style block

## 9. Descriptive & Subject Cataloging According to RDA & LCSH
**الفهرسة الوصفية والموضوعية وفق معياري RDA وLCSH**

`assets/img/workshops/rda-lcsh-cataloging.jpg`

> An entity constellation on the left: four labelled-looking but blank circular
> nodes of graded size connected by clean relationship lines into a small
> lattice, one node haloed cyan as the controlled access point; on the right a
> subject heading string drawn as five beads of decreasing size threaded on a
> single luminous line, each bead separated by a small connector dash. + shared
> style block

## 10. Using & Managing Integrated Library Systems (ILS)
**استخدام وإدارة نظم المكتبات المتكاملة**

`assets/img/workshops/integrated-library-systems.jpg`

> A hub-and-spoke system diagram: a central rounded database core glowing
> cyan, ringed by five evenly spaced module panels connected by clean spokes,
> each panel carrying one simple pictogram — a circulating arrow loop, a
> shopping cart outline, a stacked-issues fan, a magnifier, a shield. Faint
> concentric rings expand behind the core. + shared style block

## 11. Building & Developing Digital Collections in Libraries
**بناء وتطوير المجموعات الرقمية في المكتبات**

`assets/img/workshops/digital-collections.jpg`

> A mosaic wall assembling itself: on the right a neat grid of rounded tiles of
> mixed proportions, each a plain outlined placeholder for a different medium —
> a photo frame, a document sheet, a folded map, a film strip, an audio wave;
> on the left several loose tiles drift inward toward their slots, trailing
> faint motion lines; a bright selection frame highlights one tile mid-flight.
> + shared style block

## 12. Information & Document Security in Digital Environments
**أمن المعلومات والوثائق في البيئات الرقمية**

`assets/img/workshops/information-document-security.jpg`

> A layered stack of three document sheets seen at a slight angle, held under a
> broad translucent shield arc that glows cyan along its rim; a fine lattice of
> access-control lines crosses in front of the sheets with two nodes lit and one
> dimmed; along the bottom edge a thin audit-trail line runs the full width,
> ticked at irregular intervals. + shared style block

## 13. Digital Preservation & Digitization of Manuscripts & Heritage
**الحفظ الرقمي ورقمنة المخطوطات والتراث**

`assets/img/workshops/digital-preservation-manuscripts.jpg`

> An open manuscript resting in a V-shaped conservation book cradle, lit from
> above by a slim overhead camera rig on a vertical column; a bright cyan scan
> line sweeps across the open spread; the pages carry only abstract decorative
> stroke texture and an ornamental border — flowing marks that suggest
> calligraphy without forming any readable letters in any script. To the right,
> three archival boxes recede into shadow, and a small colour calibration strip
> lies flat beside the cradle as plain grey and colour squares. + shared style
> block

## 14. Digital Repositories, Archiving & Preservation in the Age of AI & Open Access
**المستودعات الرقمية والأرشفة والحفظ في عصر الذكاء الاصطناعي والوصول الحر**

`assets/img/workshops/repositories-archiving-ai-open-access.jpg`

> A repository core as a glowing rounded vault cylinder at centre, with an open
> padlock outline floating above it; on the left a stream of small particles
> flows into the core and reorganises into neat ordered rows as it enters,
> suggesting AI enrichment; on the right three concentric identifier orbits
> circle the core, each carrying a single small ring node; a faint long-term
> preservation arc encloses the whole scene. + shared style block

---

## Two notes

**On workshop 13** — the manuscript is the one image where a generator may try
to invent Arabic-looking script. The prompt says decorative strokes only.
Check the output and reject anything that renders letter shapes; garbled
pseudo-Arabic on a heritage page would undercut the very expertise it advertises.

**Optional extension** — the workshop *detail* pages currently have no artwork
at all (they open with the meta box). The same 14 images would work as a hero
band there, exactly as the services and expertise pages use their SVGs. Say the
word and I'll add that when I wire the cards.

---

## Status

| # | Workshop | State |
|---|---|---|
| 1 | Smart Digital Transformation in Academic Event Management | held — burnt-in labels, scaffolding, typo, wrong year |
| 2 | Institutional Innovation with AI | held — software-backlog wording, wrong domain |
| 3 | AI Prompt Engineering for Libraries | **live** |
| 4 | Planning & Building Digital Repositories | **live** |
| 5 | Developing Library Services Using AI & ML | held — burnt-in labels |
| 6 | Strategic Planning in the Big-Data Era | held — English headline |
| 7 | Managing Technical Operations | held — white ground, headline |
| 8 | Automated Cataloging Using MARC 21 | **live** |
| 9 | Descriptive & Subject Cataloging (RDA/LCSH) | **live** |
| 10 | Using & Managing ILS | held — white ground, wrong domain |
| 11 | Building & Developing Digital Collections | held — white ground, headline |
| 12 | Information & Document Security | held — white ground, wrong caption |
| 13 | Digital Preservation & Digitization of Manuscripts | **live** |
| 14 | Digital Repositories in the Age of AI & Open Access | **live** |

The held eight keep their generated SVG on the card, so the grid is complete
either way. To bring one in: drop the new file into `workshops/photos/` under
the same leading number, remove its slug from `HOLD` in
`tools/prepare_workshop_photos.py`, and run that script — it re-crops, compresses
and updates the list in `main.js` in one go.
