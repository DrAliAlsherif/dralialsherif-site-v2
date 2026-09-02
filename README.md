# Dr. Ali Fathy Alsherif — Personal Brand Website

A modern, premium, bilingual (English / Arabic + RTL) personal website presenting
Dr. Ali Fathy Alsherif as an academic lecturer, researcher, and consultant in
Library & Information Science, Digital Repositories, Archives, Knowledge Management
and Artificial Intelligence.

Built with hand-written **HTML5 + CSS3 + vanilla JavaScript** — no build step, no
frameworks, no dependencies. Just open it or upload it.

## File structure

```
site/
├── index.html                 # All page markup + SEO / Open Graph / JSON-LD
├── assets/
│   ├── css/styles.css         # Design system: light/dark, RTL, responsive, animations
│   ├── js/main.js             # Content data (EN/AR) + all interactivity
│   ├── docs/Ali-Fathy-CV.pdf  # Downloadable CV
│   └── img/
│       ├── hero-portrait.jpg
│       ├── events/            # Award / book-signing / symposium / certificates
│       └── gallery/           # 39 conference & networking photos
└── README.md
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
- Contact form (opens the visitor's email client, pre-filled — no backend needed)
- SEO metadata, Open Graph / Twitter cards, and Person JSON-LD structured data
- Lazy-loaded images for fast loading

## Editing content

All text lives in **`assets/js/main.js`** in the `DATA` object (each item has `en`
and `ar` fields) and the `I18N` dictionary. To add a publication, book, workshop,
event or gallery photo, add an entry to the matching array — the page renders it
automatically. The architecture is intentionally **blog- and research-ready**:
new collections follow the same pattern.

## Running locally

Because the site loads assets, open it through a local web server (not `file://`):

- **VS Code:** install the *Live Server* extension → "Go Live".
- **Any static server** pointed at the `site/` folder works.

## Deploying (free options)

Upload the **contents of the `site/` folder** to any static host:

- **Netlify / Vercel / Cloudflare Pages:** drag-and-drop the `site` folder.
- **GitHub Pages:** push `site/` to a repo and enable Pages.
- **Any web host:** upload via FTP to the public web root.

### Before going live — quick checklist
1. Replace the LinkedIn placeholder `href="#"` in `index.html` (Contact + footer)
   with the real profile URL.
2. Confirm the public contact email/phone in `index.html` and `main.js`
   (currently `a.elsherif79@gmail.com` / `+971 50 2233519`).
3. Update the `og:url` / `canonical` domain in `index.html` to the final domain,
   and add real book-cover images if available (currently elegant typographic covers).
4. Optional: compress the large gallery JPEGs for even faster loading.
