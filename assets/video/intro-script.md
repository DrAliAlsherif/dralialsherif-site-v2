# Introductory Video — Production Script

**Subject:** Dr. Ali Fathy Alsherif
**Duration:** 60 seconds · **Aspect:** 16:9 (1280×720 design frame, scales to 1920×1080)
**Deliverable in repo:** [`intro.html`](../../intro.html) — a self-contained animated sequence that plays in any modern browser
**On the site:** the hero's **Watch Intro** button opens it in a modal (`intro.html?embed=1` in an iframe), so it plays without leaving the homepage
**Captions:** [`intro-captions.srt`](intro-captions.srt) — upload alongside the MP4 on YouTube/LinkedIn

All figures below match what the site already publishes — the hero counters in `index.html`
(23 years, 3 books, 15+ publications, 18+ workshops) and the data arrays in `assets/js/main.js`
(9 major projects, 13 conference appearances, 10 expertise areas, career start Nov 2003).
If those change, update this script, `intro-captions.srt` and `intro.html` together.

---

## Scene breakdown

| # | Time | Section | On-screen | Visual treatment |
|---|------|---------|-----------|------------------|
| 0 | 0:00–0:08 | Opening | Name (gradient wordmark), Arabic name, three role lines | Knowledge-network particles at high energy; name resolves from blur; gradient rule draws out |
| 1 | 0:08–0:20 | Professional profile | "Two decades engineering knowledge environments" + counters **23 years / 9 projects / 18+ workshops / 13 conferences** | Counters ease-count up over 1.4 s; network settles |
| 2 | 0:20–0:31 | Expertise | 10 chips, AI / Digital Transformation / Prompt Engineering highlighted in cyan | Chips stagger in at 90 ms intervals |
| 3 | 0:31–0:42 | Services | 6 glass cards with line icons | Grid staggers in; icons stroke-drawn |
| 4 | 0:42–0:52 | Publications & recognition | 3 book spines + **15+** peer-reviewed papers + **3** books with leading Arab academic publishers + Sharjah Award 2016 | Spines rise with depth shadow; gold award pill |
| 5 | 0:52–1:00 | Closing | "Let's build the future of knowledge." + URL + service tags | Network returns to high energy; gradient CTA |

---

## Voice-over script

Recommended read: measured, warm, authoritative. ~2.7 words/second.
Neutral international English (RP or General American both work).
Leave ~0.4 s of air at the head of each scene.

**0:00 — Opening**
> Doctor Ali Fathy Alsherif. Library and Information Science expert, artificial intelligence trainer, and digital transformation consultant.

**0:08 — Professional profile**
> For over twenty years he has built modern, data-driven knowledge environments across leading academic and government institutions in the Emirates — from digital repositories and large-scale digitization to AI-enabled information services.

**0:20 — Expertise**
> His expertise spans artificial intelligence and digital transformation, library automation, digital repositories, archives and preservation, metadata standards, research support, and prompt engineering for knowledge institutions.

**0:31 — Services**
> He delivers AI consulting, digital transformation strategy, repository development, and metadata governance — alongside professional training programmes, hands-on workshops, and capacity building for librarians and knowledge teams.

**0:42 — Publications & recognition**
> He is the author of three books, including *Artificial Intelligence Prompt Engineering in Libraries and Archives*, with more than fifteen published papers and a Sharjah Award for Library Literature.

**0:52 — Closing**
> Explore the full portfolio, connect, and let's build the future of knowledge together.

*Pronunciation:* **Ali** — "AH-lee" · **Fathy** — "FAT-hee" · **Alsherif** — "al-sha-REEF".

### Voice direction

| Aspect | Direction |
|---|---|
| Voice | Male or female, 30–50, neutral international English |
| Tone | Calm authority — a senior consultant, not an advertisement |
| Pace | ~2.7 words per second. Never rush the name |
| Delivery | Land the pause at each scene change; let the music breathe |
| Avoid | Upward inflection, hard sell, over-brightness |

---

## Music direction

`intro.html` synthesises its own ambient bed (Web Audio: three detuned oscillators through a
slow-sweeping low-pass filter, plus a pentatonic pluck every 1.9 s). It is deliberately subtle and
sits well under narration.

If you replace it with a licensed track, brief it as: **ambient electronic, 70–80 BPM, warm pad
foundation, sparse bell or pluck motif, no percussion until 0:40, gentle lift into the closing
card.** Duck the music to roughly −18 dB under the voice-over.

---

## Producing the MP4

The page is built to be screen-recorded cleanly — the stage is a fixed 16:9 area with no browser
chrome inside it.

1. Open `intro.html`, press **Captions** off if you plan to burn in the SRT later.
2. Set the browser window so the stage renders at 1280×720 or larger (it scales automatically).
3. Start your recorder (OBS, ScreenFlow, Xbox Game Bar, QuickTime), capture the stage region only.
4. Press **Play** — or the space bar. The sequence is exactly 60 s and ends on the closing card.
5. Lay the professionally recorded voice-over over the result using the timecodes above.

**Export presets**

| Platform | Resolution | Notes |
|----------|-----------|-------|
| Website / YouTube | 1920×1080, H.264, 8–12 Mbps | Upload `intro-captions.srt` as the caption track |
| LinkedIn | 1920×1080 or 1080×1080 | Keep under 10 min / 5 GB; captions strongly recommended — most feed views are muted |
| Instagram / TikTok | 1080×1920 | Requires a re-frame; the scenes are centre-weighted so a 9:16 crop of the middle works |

Because most social views are silent, the burned-in captions are doing the real work — keep them on
for any feed upload.

---

## Controls in `intro.html`

| Control | Action |
|---------|--------|
| **Play / Pause** | also bound to the space bar |
| **Restart** | also bound to `R` |
| **Voice-over** | browser speech synthesis — a preview stand-in, not a substitute for a recorded VO |
| **Music** | ambient bed on/off |
| **Captions** | show/hide burned-in captions |

> The built-in voice-over uses the Web Speech API, so its quality depends on the voices installed on
> the viewing machine. It is there so the timing can be auditioned end-to-end. For anything
> published, record the script above with a professional voice artist.
