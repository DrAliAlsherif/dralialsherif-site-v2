# -*- coding: utf-8 -*-
"""Concept illustrations shared by the sub-page generators.

Ported from RART in assets/js/main.js — the SVG a card shows on the home page
and the one on its detail page must be the same drawing. Colours come from the
.ra-* classes in assets/css/styles.css and assets/css/subpage.css, so the art
follows the light/dark theme on its own.

Add a drawing here and to RART in main.js together, under the same key.
"""
import math


def _wrap(inner):
    return (f'<svg class="ra" viewBox="0 0 320 160" '
            f'preserveAspectRatio="xMidYMid slice" aria-hidden="true">{inner}</svg>')

def _ai():
    L = [(62, [46, 80, 114]), (158, [30, 66, 102, 130]), (254, [64, 100])]
    edges = nodes = ""
    for i in range(len(L) - 1):
        x1, a = L[i]
        x2, b = L[i + 1]
        for y1 in a:
            for y2 in b:
                edges += f'<line class="ra-edge" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'
    for li, (x, ys) in enumerate(L):
        for y in ys:
            c = "ra-node ra-node--b" if li == 1 else "ra-node ra-node--a"
            nodes += f'<circle class="{c}" cx="{x}" cy="{y}" r="{7 if li == 1 else 6}"/>'
    return _wrap(edges + nodes)

def _repository():
    def db(cx, top):
        s = ""
        for i in range(3):
            y = top + i * 22
            s += (f'<ellipse class="ra-stroke" cx="{cx}" cy="{y}" rx="42" ry="12"/>'
                  f'<path class="ra-stroke ra-dim" d="M{cx-42} {y} v18 a42 12 0 0 0 84 0 v-18"/>')
        return s
    return _wrap(
        db(96, 50)
        + '<circle class="ra-node ra-node--a" cx="96" cy="50" r="4"/>'
        + '<path class="ra-stroke ra-dim" stroke-dasharray="4 5" d="M150 96 H206"/>'
        + '<path class="ra-stroke" d="M214 96 q-6 0 -6 -12 a16 16 0 0 1 31 -4 a12 12 0 0 1 3 24 h-24 z"/>'
        + '<path class="ra-stroke ra-node--b" style="stroke:#a78bfa" d="M228 104 v-22 m-8 8 l8 -8 l8 8" fill="none"/>'
    )

def _manuscript():
    return _wrap(
        '<path class="ra-stroke" d="M160 44 C128 32 100 38 84 46 V118 C100 110 128 106 160 116 Z"/>'
        '<path class="ra-stroke" d="M160 44 C192 32 220 38 236 46 V118 C220 110 192 106 160 116 Z"/>'
        '<line class="ra-stroke ra-dim" x1="160" y1="46" x2="160" y2="115"/>'
        '<path class="ra-dim2" d="M100 60 h40 M100 72 h34 M100 84 h40 M180 60 h40 M186 72 h34 M180 84 h40"/>'
        '<rect class="ra-scan" x="76" y="76" width="168" height="5" rx="2.5"/>'
        '<rect class="ra-accent" x="196" y="44" width="7" height="7" rx="1.5"/>'
        '<rect class="ra-accent2" x="210" y="34" width="6" height="6" rx="1.5"/>'
        '<rect class="ra-accent" x="224" y="26" width="5" height="5" rx="1.5"/>'
    )

def _archive():
    def box(x, y):
        return (f'<rect class="ra-stroke" x="{x}" y="{y}" width="70" height="26" rx="3"/>'
                f'<line class="ra-stroke ra-dim" x1="{x}" y1="{y+9}" x2="{x+70}" y2="{y+9}"/>'
                f'<rect class="ra-dim2b" x="{x+27}" y="{y+3}" width="16" height="3" rx="1.5"/>')
    return _wrap(
        box(58, 48) + box(58, 78) + box(58, 108)
        + '<path class="ra-stroke" d="M226 46 l26 9 v20 c0 17 -13 26 -26 32 c-13 -6 -26 -15 -26 -32 v-20 z"/>'
        + '<path class="ra-stroke ra-check" d="M215 80 l8 8 l16 -18"/>'
    )

def _library():
    return _wrap(
        '<path class="ra-stroke" d="M92 122 C118 110 150 110 160 118 C170 110 202 110 228 122 V132 C202 120 170 120 160 128 C150 120 118 120 92 132 Z"/>'
        '<line class="ra-stroke ra-dim" x1="160" y1="118" x2="160" y2="128"/>'
        '<circle class="ra-node ra-node--a" cx="160" cy="86" r="5"/>'
        '<path class="ra-signal" d="M144 78 a22 22 0 0 1 32 0"/>'
        '<path class="ra-signal" d="M134 68 a36 36 0 0 1 52 0"/>'
        '<path class="ra-signal" d="M124 58 a50 50 0 0 1 72 0"/>'
        '<circle class="ra-node ra-node--b" cx="112" cy="44" r="3.5"/>'
        '<circle class="ra-node ra-node--b" cx="208" cy="44" r="3.5"/>'
        '<path class="ra-edge" d="M112 44 L160 86 L208 44"/>'
    )

def _technical():
    def gear(cx, cy, r):
        teeth = ""
        a = 0
        while a < 360:
            rad = math.radians(a)
            c, s = math.cos(rad), math.sin(rad)
            teeth += (f'<line class="ra-stroke" x1="{cx + c*r:.1f}" y1="{cy + s*r:.1f}" '
                      f'x2="{cx + c*(r+7):.1f}" y2="{cy + s*(r+7):.1f}"/>')
            a += 45
        return (f'<circle class="ra-stroke" cx="{cx}" cy="{cy}" r="{r}"/>'
                f'<circle class="ra-stroke ra-dim" cx="{cx}" cy="{cy}" r="{r*0.42:.1f}"/>{teeth}')
    return _wrap(
        gear(120, 74, 28) + gear(198, 104, 20)
        + '<circle class="ra-node ra-node--a" cx="120" cy="74" r="5"/>'
        + '<circle class="ra-node ra-node--b" cx="198" cy="104" r="4"/>'
    )

def _metadata():
    ys = [56, 76, 96, 112]
    ws = [96, 120, 80, 108]
    rows = ""
    for i, y in enumerate(ys):
        rows += (f'<rect class="{"ra-accent2" if i % 2 else "ra-accent"}" x="92" y="{y}" width="10" height="10" rx="2"/>'
                 f'<line class="ra-dim2" x1="112" y1="{y+5}" x2="{112+ws[i]}" y2="{y+5}"/>')
    return _wrap(
        '<rect class="ra-stroke" x="78" y="40" width="164" height="88" rx="6"/>'
        '<line class="ra-stroke ra-dim" x1="78" y1="46" x2="242" y2="46"/>' + rows
    )

def _knowledge():
    cx, cy, R = 160, 80, 46
    pts = []
    a = 0
    while a < 360:
        rad = math.radians(a)
        pts.append((round(cx + math.cos(rad) * R, 1), round(cy + math.sin(rad) * R, 1)))
        a += 60
    edges = nodes = ""
    for i, p in enumerate(pts):
        n = pts[(i + 1) % len(pts)]
        edges += (f'<line class="ra-edge" x1="{cx}" y1="{cy}" x2="{p[0]}" y2="{p[1]}"/>'
                  f'<line class="ra-edge" x1="{p[0]}" y1="{p[1]}" x2="{n[0]}" y2="{n[1]}"/>')
        nodes += f'<circle class="ra-node {"ra-node--b" if i % 2 else "ra-node--a"}" cx="{p[0]}" cy="{p[1]}" r="5"/>'
    return _wrap(edges + nodes
                 + f'<circle class="ra-stroke" cx="{cx}" cy="{cy}" r="13"/>'
                 + f'<circle class="ra-accent2" cx="{cx}" cy="{cy}" r="5"/>')

def _training():
    return _wrap(
        '<path class="ra-stroke" d="M160 44 L232 66 L160 88 L88 66 Z"/>'
        '<path class="ra-stroke ra-dim" d="M112 75 V98 C112 110 208 110 208 98 V75"/>'
        '<line class="ra-stroke" x1="232" y1="66" x2="232" y2="92"/>'
        '<circle class="ra-accent" cx="232" cy="96" r="4"/>'
        '<circle class="ra-node ra-node--a" cx="120" cy="128" r="4.5"/>'
        '<circle class="ra-node ra-node--b" cx="160" cy="132" r="4.5"/>'
        '<circle class="ra-node ra-node--a" cx="200" cy="128" r="4.5"/>'
        '<path class="ra-signal" d="M120 122 q40 -18 80 0"/>'
        '<path class="ra-signal" d="M108 116 q52 -30 104 0"/>'
    )

def _consulting():
    return _wrap(
        '<path class="ra-stroke" d="M96 44 h128 a14 14 0 0 1 14 14 v40 a14 14 0 0 1 -14 14 h-70 l-26 20 v-20 h-6 a14 14 0 0 1 -14 -14 v-40 a14 14 0 0 1 14 -14 z"/>'
        '<path class="ra-check" d="M128 78 l14 14 l28 -30"/>'
        '<circle class="ra-node ra-node--b" cx="70" cy="120" r="4"/>'
        '<circle class="ra-node ra-node--a" cx="250" cy="60" r="4"/>'
        '<path class="ra-edge" d="M78 116 L104 104 M232 64 L214 72"/>'
    )

def _strategy():
    bars = ""
    for x, y in [(64, 96), (98, 80), (132, 60), (166, 42)]:
        bars += f'<rect class="ra-stroke ra-dim" x="{x}" y="{y}" width="22" height="{120-y}" rx="2"/>'
    return _wrap(
        '<line class="ra-stroke" x1="56" y1="120" x2="252" y2="120"/>' + bars
        + '<polyline class="ra-signal" points="70,102 104,86 140,66 178,48"/>'
        + '<circle class="ra-accent" cx="178" cy="48" r="4"/>'
        + '<circle class="ra-stroke" cx="238" cy="70" r="22"/>'
        + '<circle class="ra-stroke ra-dim" cx="238" cy="70" r="13"/>'
        + '<circle class="ra-accent2" cx="238" cy="70" r="5"/>'
    )

def _ils():
    return _wrap(
        '<rect class="ra-stroke" x="58" y="42" width="80" height="78" rx="7"/>'
        '<line class="ra-stroke ra-dim" x1="58" y1="68" x2="138" y2="68"/>'
        '<line class="ra-stroke ra-dim" x1="58" y1="94" x2="138" y2="94"/>'
        '<circle class="ra-accent" cx="72" cy="55" r="3.5"/>'
        '<circle class="ra-accent2" cx="72" cy="81" r="3.5"/>'
        '<circle class="ra-accent" cx="72" cy="107" r="3.5"/>'
        '<path class="ra-dim2" d="M86 55 h40 M86 81 h30 M86 107 h40"/>'
        '<path class="ra-stroke ra-dim" stroke-dasharray="4 5" d="M146 81 H184"/>'
        '<line class="ra-stroke" x1="188" y1="122" x2="266" y2="122"/>'
        '<rect class="ra-stroke" x="194" y="72" width="16" height="48" rx="2"/>'
        '<rect class="ra-stroke" x="214" y="58" width="16" height="62" rx="2"/>'
        '<rect class="ra-stroke ra-dim" x="234" y="80" width="16" height="40" rx="2"/>'
        '<rect class="ra-accent" x="197" y="79" width="10" height="3" rx="1.5"/>'
        '<rect class="ra-accent2" x="217" y="65" width="10" height="3" rx="1.5"/>'
        '<rect class="ra-accent" x="237" y="87" width="10" height="3" rx="1.5"/>'
    )

def _research():
    return _wrap(
        '<path class="ra-stroke" d="M62 38 h66 l22 22 v68 a6 6 0 0 1 -6 6 h-82 a6 6 0 0 1 -6 -6 v-84 a6 6 0 0 1 6 -6 z"/>'
        '<path class="ra-stroke ra-dim" d="M128 38 v22 h22"/>'
        '<path class="ra-dim2" d="M78 74 h52 M78 88 h40 M78 102 h52 M78 116 h32"/>'
        '<circle class="ra-stroke" cx="196" cy="74" r="27"/>'
        '<line class="ra-stroke" x1="215" y1="93" x2="238" y2="116"/>'
        '<polyline class="ra-signal" points="181,82 190,70 200,78 211,60"/>'
        '<circle class="ra-accent" cx="211" cy="60" r="3.5"/>'
        '<circle class="ra-node ra-node--b" cx="256" cy="48" r="4"/>'
        '<circle class="ra-node ra-node--a" cx="270" cy="84" r="3.5"/>'
        '<path class="ra-edge" d="M220 56 L256 48 M224 84 L270 84"/>'
    )


ART = {
    "ai": _ai,
    "repository": _repository,
    "manuscript": _manuscript,
    "archive": _archive,
    "library": _library,
    "technical": _technical,
    "metadata": _metadata,
    "knowledge": _knowledge,
    "training": _training,
    "consulting": _consulting,
    "strategy": _strategy,
    "ils": _ils,
    "research": _research,
}
