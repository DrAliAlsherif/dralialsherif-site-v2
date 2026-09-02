# Improvements — status

Working copy of the site (`../site` → repo `dralialsherif-site-v2`) with the
review suggestions applied. Legend: ✅ done · 🟡 scaffolded, needs your input ·
⏳ needs an external account/content you provide.

Public URL for this copy: `https://dralialsherif.github.io/dralialsherif-site-v2/`
(enable **Settings → Pages → Deploy from branch: `main` / root**).

| # | Suggestion | Status | Where |
|---|------------|--------|-------|
| 1 | Crawlable content (JS-rendered pages) | ✅ | `index.html` → `<section class="seo-index">` + `<noscript>`; keep it in sync with `DATA` in `assets/js/main.js` |
| 2 | Bilingual SEO: `/ar/`, hreflang, sitemap, robots | ✅ | `ar/index.html` (built by `tools/build.py`), `hreflang` in `<head>`, `robots.txt`, `sitemap.xml` |
| 3 | Image compression + dedupe + dimensions | ✅ | `tools/optimize_images.py` (16 MB → 9.4 MB); gallery already ships intrinsic `width/height` via `GALLERY_DIMS` |
| 4 | Real contact-form delivery | 🟡 | `index.html` form posts to Web3Forms; `assets/js/main.js` does `fetch` + mailto fallback. **Set `#cf-access-key`** from https://web3forms.com |
| 5 | Privacy-friendly analytics | 🟡 | Commented Plausible / Cloudflare snippet in `<head>` — uncomment one and fill the token |
| 6 | Custom domain | 🟡 | `CNAME.example` (rename → `CNAME`), then run a find/replace of the `github.io/...` origin (see the file) |
| 7 | Testimonials | ✅ (already had 5) | `DATA.testimonials` in `assets/js/main.js` — add more entries |
| 8 | Articles / blog | 🟡 | `#articles` section, `articles/` (index + `_template.html`), `DATA.articles = []`. Add posts to publish |
| 9 | Research identifiers (ORCID / Scholar / ResearchGate) | 🟡 | `TODO(research-identifiers)` in `index.html` JSON-LD `sameAs` — paste the profile URLs |
| 10 | Workshop pages polish | ✅ | Nav link + section CTA; each page now has `Course` JSON-LD, OG tags, and an "اطلب هذه الورشة" button that pre-fills the contact form (`?ws=<slug>`). `workshops/index.html` has `ItemList` JSON-LD |
| 11 | Media / speaker kit | ✅ | `media-kit.html` (bios AR+EN, speaking topics, downloads). **TODO:** export a workshop-catalog PDF |
| 12 | Favicons + PWA manifest | ✅ | `assets/img/icons/*` (generated), `site.webmanifest`, `<head>` links |
| 13 | Custom 404 page | ✅ | `404.html` |
| 14 | Arabic-default for Arabic browsers | ✅ | `assets/js/main.js` — `navigator.language` starts with `ar` → Arabic (remembered choice still wins) |
| 15 | Impact figures + partner logos | 🟡 | `#partners` section: impact `<li>` numbers are **placeholders** — confirm them. Drop logos in `assets/img/partners/` and fill `DATA.partners` (text-chip fallback shows meanwhile) |
| 16 | Booking embed | 🟡 | `services.book` button + `data-cal-link="TODO"` — create a Cal.com/Calendly link and swap the `href` |
| 17 | Real book covers | ✅ (already wired) | `DATA.books[*].img` already points at real cover files in `assets/img/books/` |

## Build commands

```bash
python tools/gen_workshops.py     # regenerate the 14 workshop pages + workshops/index.html
python tools/build.py             # regenerate ar/index.html + refresh sitemap lastmod
python tools/optimize_images.py   # (re)compress assets/img + regenerate icons  [--dry-run to preview]
```

Run `gen_workshops.py` then `build.py` after editing `index.html` or workshop
content, and commit the generated files.

## Remaining TODO markers in code

Search the repo for `TODO(` — every placeholder is tagged:
`TODO(custom-domain)`, `TODO(research-identifiers)`, `TODO(partners)`,
`TODO(impact)`, `TODO(booking)`, `TODO(og-image)`, `TODO(articles)`,
`TODO(workshop-catalog-pdf)`, and the Web3Forms / analytics placeholders.
