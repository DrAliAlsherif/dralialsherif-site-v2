# Dr. Ali Fathy Alsherif — Personal Brand Website (v2)

A modern, premium, bilingual (English / Arabic + RTL) personal website presenting
Dr. Ali Fathy Alsherif as an academic lecturer, researcher, and consultant in
Library & Information Science, Digital Repositories, Archives, Knowledge Management
and Artificial Intelligence.

Hand-written **HTML5 + CSS3 + vanilla JavaScript**, no frameworks. There are now a
few small **Python helper scripts** under `tools/` that regenerate derived files
(the Arabic mirror, the workshop pages, optimised images) — the site itself still
ships as plain static files.

> This is the **working copy** (`dralialsherif-site-v2`). See **`IMPROVEMENTS.md`**
> for what changed versus the original and the list of `TODO(...)` items that need
> your accounts or content.

## File structure

```
.
├── index.html                 # Page markup + SEO / OG / JSON-LD + static SEO summary
├── ar/index.html              # GENERATED Arabic entry point (tools/build.py)
├── 404.html                   # Branded not-found page
├── robots.txt · sitemap.xml   # Crawl directives
├── site.webmanifest           # PWA manifest
├── CNAME.example              # Rename to CNAME when a custom domain is ready
├── media-kit.html             # Speaker / media kit
├── articles/                  # Blog: index.html + _template.html (add posts here)
├── workshops/                 # 14 GENERATED briefs + index.html — ar/ + en/ (tools/gen_workshops.py)
├── expertise/                 # 10 GENERATED area pages + index.html — ar/ + en/ (tools/gen_expertise.py)
├── services/                  # 8 GENERATED service pages + index.html — ar/ + en/ (tools/gen_services.py)
├── books/viewer.html          # Page-flip reader for the book sample PDFs (?src=&title=)
├── assets/
│   ├── css/styles.css         # Main design system: light/dark, RTL, responsive
│   ├── css/subpage.css        # Shared styles for articles/ and media-kit.html
│   ├── js/main.js             # Content data (EN/AR) + all interactivity
│   ├── vendor/pdfjs/          # pdf.js 3.11.174 (vendored) — used by books/viewer.html
│   ├── vendor/page-flip/      # StPageFlip 2.0.7 (vendored) — page-turn effect
│   ├── books/*.pdf            # Book "contents & introduction" samples
│   ├── docs/Ali-Fathy-CV.pdf
│   └── img/
│       ├── icons/             # GENERATED favicons / PWA icons (tools/optimize_images.py)
│       ├── partners/          # Drop partner logos here (optional)
│       ├── events/ · gallery/ · books/ · research/
│       └── hero-portrait.jpg
├── tools/
│   ├── _art.py                # Concept illustrations shared by the generators below
│   ├── _photos.py             # Shared crop/compress/sync for the two scripts below
│   ├── prepare_workshop_photos.py  # workshops/photos/ → assets/img/workshops/ (16:7.4)
│   ├── prepare_service_photos.py   # Consulting photos/ → assets/img/services/ (16:8.4)
│   ├── prepare_expertise_photos.py # Areas of expertise/ → assets/img/expertise/ (16:8.4)
│   ├── expertise-image-prompts.md  # prompts for the expertise card artwork
│   ├── prepare_project_photos.py   # Projects photos/ → assets/img/projects/ (16:6.6)
│   ├── project-image-prompts.md    # prompts for the project card artwork
│   ├── service-image-prompts.md    # prompts for the service card artwork
│   ├── logo-prompts.md        # brand-mark concepts; the chosen one is inline SVG
│   ├── workshop-image-prompts.md   # prompts + status for the workshop card artwork
│   ├── workshops_en.py        # English text for the workshop pages, keyed by slug
│   ├── gen_workshops.py       # → workshops/{,en/}*.html + both index.html
│   ├── gen_expertise.py       # → expertise/{,en/}*.html + both index.html (+ concept art)
│   ├── gen_services.py        # → services/{,en/}*.html + both index.html (+ concept art)
│   ├── build.py               # → ar/index.html + sitemap lastmod
│   └── optimize_images.py     # (re)compress assets/img + build icons
├── IMPROVEMENTS.md            # Change log + TODO tracker
└── README.md
```

## Languages

The home page is bilingual and switches in place (`#langToggle`, remembered in
`localStorage`); `/ar/` is a generated Arabic mirror of `/index.html` for
crawlers. Every sub-page exists twice — Arabic at `<section>/<slug>.html` and
English at `<section>/en/<slug>.html` — paired with `hreflang` and a switch
link in the header. `main.js` sends each card to the page in the active
language. The workshops themselves are delivered in Arabic; the English pages
say so in the meta box.

`media-kit.html` is deliberately one bilingual page (Arabic and English bios
side by side) rather than a pair — it is written for organisers who need both.

## Rebuilding derived files

```bash
python tools/gen_workshops.py   # after editing workshop content
python tools/gen_expertise.py   # after editing expertise content / area services
python tools/gen_services.py    # after editing consulting-service content
# each gen_* script writes BOTH languages; English text lives beside the Arabic
python tools/build.py           # after editing index.html (rebuilds ar/) — run the gen_* scripts first
python tools/optimize_images.py # after adding images  (--dry-run to preview)
```

## Features

- Light / dark mode (remembers choice, respects system preference)
- Full English ⇄ Arabic switch with automatic **RTL** layout (remembers choice)
- Mobile-first responsive design + accessible (skip link, ARIA, keyboard, focus states)
- Sticky glass navigation, scroll progress bar, active-section highlighting
- Scroll-reveal animations, animated hero counters, running keyword marquee
- Live site search (books, research, workshops, services, events) — `Ctrl/Cmd + K`
- Image lightbox with keyboard navigation (gallery, events, certificates)
- Filterable research/publications, interactive experience & education timelines
- Contact form — posts to Web3Forms when a key is set, otherwise falls back to
  the visitor's email client; supports `?ws=<slug>` pre-fill from workshop pages
- SEO: metadata, Open Graph / Twitter cards, Person + Course + ItemList + BlogPosting
  JSON-LD, `hreflang` EN/AR, `robots.txt`, `sitemap.xml`, and a static crawlable
  content summary for bots and link unfurlers
- PWA: web manifest + generated icon set + custom `404.html`
- Optimised, lazy-loaded images with intrinsic dimensions (no layout shift)

## Editing content

All text lives in **`assets/js/main.js`** in the `DATA` object (each item has `en`
and `ar` fields) and the `I18N` dictionary. To add a publication, book, workshop,
event or gallery photo, add an entry to the matching array — the page renders it
automatically. The architecture is intentionally **blog- and research-ready**:
new collections follow the same pattern.

## Running locally

Serve the repo root over HTTP (not `file://`):

```bash
python -m http.server 8220        # then open http://localhost:8220/
```

## Deploying

**GitHub Pages:** repo **Settings → Pages → Build and deployment → Deploy from a
branch → `main` / `/ (root)`**. The site is then at
`https://dralialsherif.github.io/dralialsherif-site-v2/`.

Any static host works too (Netlify / Cloudflare Pages / FTP) — upload the repo
root. Cloudflare Pages additionally gives you free analytics and response headers.

### Before promoting this to the main site
1. Work through the `TODO(...)` markers — see **`IMPROVEMENTS.md`** (Web3Forms key,
   analytics token, ORCID/Scholar links, partner logos, real impact numbers,
   booking link).
2. If moving to a custom domain, follow `CNAME.example` and re-run the origin
   find/replace, then `python tools/build.py`.
3. Re-run the three `tools/` scripts and commit the regenerated files.
