#!/usr/bin/env python3
"""Génère les sprites PNG des objets d'équipement dans src/lib/assets/items/.

Outil de dev OPTIONNEL : les PNG sont versionnés, il n'est pas lancé au build.
Dépendances : pip install cairosvg pillow
Usage : python3 scripts/build-item-sprites.py [--sheet /tmp/planche.png]

Chaque sprite est dessiné en SVG (contours sombres, dégradés, reflets), rendu en
PNG puis recadré au plus juste. Pour utiliser vos propres illustrations, il suffit
de déposer <id>.png dans src/lib/assets/items/ : le fichier remplace le sprite.
Les palettes ci-dessous doivent rester alignées avec PALETTES de src/lib/game/data.js.
"""
import io, sys, pathlib
import cairosvg
from PIL import Image

OUT_DIR = pathlib.Path(__file__).resolve().parent.parent / "src/lib/assets/items"
OUT = "#1c2030"           # contour
RENDER = 3                # facteur de rendu avant réduction (anti-crénelage)
MAX_SIDE = 160            # taille max (px) d'un sprite final
PAD = 6

PALETTES = {  # miroir de src/lib/game/data.js
    "common": dict(metal=("#e8edf2", "#b9c4ce", "#8b97a3"), trim="#c9a24a", gem="#4faf62"),
    "rare": dict(metal=("#e2efff", "#9cc4f5", "#5f8fc9"), trim="#8ec5ff", gem="#4f9fd8"),
    "epic": dict(metal=("#efe5ff", "#c19bff", "#8a5fd0"), trim="#e0c6ff", gem="#b06cf0"),
    "legendary": dict(metal=("#fff6d2", "#f4cd6f", "#d99a2b"), trim="#fff3b0", gem="#ee8174"),
    "mythic": dict(metal=("#ffe0f6", "#ff8fdc", "#c2409f"), trim="#9ff3ff", gem="#6ff0ff"),
}


def hx(c):
    c = c.lstrip("#")
    return [int(c[i:i + 2], 16) for i in (0, 2, 4)]


def mix(a, b, t):
    A, B = hx(a), hx(b)
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * t) for i in range(3))


def lighten(c, t): return mix(c, "#ffffff", t)
def darken(c, t): return mix(c, "#000000", t)


def defs(p):
    m0, m1, m2 = p["metal"]
    t, g = p["trim"], p["gem"]
    def lin(i, stops, x2=0, y2=1):
        s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
        return f'<linearGradient id="{i}" x1="0" y1="0" x2="{x2}" y2="{y2}">{s}</linearGradient>'
    return "<defs>" + "".join([
        lin("mv", [(0, m0), (0.5, m1), (1, m2)]),
        lin("mh", [(0, m2), (0.35, m0), (0.7, m1), (1, m2)], 1, 0),
        lin("gold", [(0, lighten(t, .5)), (0.5, t), (1, darken(t, .45))]),
        lin("goldh", [(0, darken(t, .4)), (0.4, lighten(t, .5)), (1, darken(t, .3))], 1, 0),
        lin("wood", [(0, "#c08a50"), (0.5, "#8a5a2b"), (1, "#5b3a1a")]),
        lin("leather", [(0, "#b98450"), (0.5, "#7a4a22"), (1, "#4a2c14")]),
        lin("ice", [(0, "#d9f6ff"), (0.45, "#8fdcff"), (1, "#3c92d6")], 1, 0),
        lin("bone", [(0, "#fffaf0"), (0.6, "#e7d9bd"), (1, "#b9a57c")]),
        lin("dark", [(0, "#4b3680"), (0.55, "#2a1f45"), (1, "#120e24")]),
        lin("glowv", [(0, "#ffffff"), (0.35, "#ffb3ea"), (1, "#d04bb0")]),
        f'<radialGradient id="gem" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="{lighten(g, .75)}"/>'
        f'<stop offset=".45" stop-color="{g}"/><stop offset="1" stop-color="{darken(g, .5)}"/></radialGradient>',
    ]) + "</defs>"


def st(w=5):
    return f'stroke="{OUT}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"'


S = st()
HI = 'fill="#fff" opacity=".5"'


def gem_circle(cx, cy, r):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gem)" {S}/>'
            f'<ellipse cx="{cx - r * .3}" cy="{cy - r * .35}" rx="{r * .3}" ry="{r * .2}" {HI}/>')


def grip(cx, y, h, w=22):
    x = cx - w / 2
    wraps = "".join(f'<path d="M{x + 2} {y + 8 + i * 11} L{x + w - 2} {y + 14 + i * 11}" stroke="{OUT}" stroke-width="3" opacity=".55"/>' for i in range(max(1, int(h // 12) - 1)))
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="url(#leather)" {S}/>' + wraps


def star(cx, cy, ro, ri, n=5, rot=-90):
    import math
    pts = []
    for i in range(n * 2):
        r = ro if i % 2 == 0 else ri
        a = math.radians(rot + i * 180 / n)
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return " ".join(pts)


# ───────────────────────── Armes ─────────────────────────
def sword(p):
    return f"""
    <polygon points="128,10 145,50 145,176 111,176 111,50" fill="url(#mh)" {S}/>
    <rect x="124.5" y="48" width="7" height="112" rx="3.5" fill="{p['metal'][2]}" opacity=".55"/>
    <rect x="114" y="52" width="4" height="118" rx="2" {HI}/>
    <rect x="80" y="174" width="96" height="17" rx="8.5" fill="url(#gold)" {S}/>
    {gem_circle(128, 182.5, 6.5)}
    {grip(128, 191, 42)}
    <circle cx="128" cy="242" r="12.5" fill="url(#gold)" {S}/>
    <ellipse cx="124" cy="238" rx="4" ry="3" {HI}/>"""


def frostblade(p):
    pts = "128,6 151,40 143,62 153,86 144,110 154,136 145,160 145,180 111,180 111,160 102,136 112,110 103,86 113,62 105,40"
    right = "128,8 151,40 143,62 153,86 144,110 154,136 145,160 145,178 128,178"
    return f"""
    <polygon points="{pts}" fill="url(#ice)" {S}/>
    <polygon points="{right}" fill="#2f7fc0" opacity=".35"/>
    <path d="M128 18 V172" stroke="#e9fbff" stroke-width="3" opacity=".8"/>
    <path d="M116 60 L122 130" stroke="#fff" stroke-width="3" opacity=".6" stroke-linecap="round"/>
    <path d="M66 184 Q98 164 128 176 Q158 164 190 184 Q160 200 128 192 Q96 200 66 184 Z" fill="url(#gold)" {S}/>
    {gem_circle(128, 184, 8)}
    {grip(128, 194, 38)}
    <polygon points="128,228 142,242 128,256 114,242" fill="url(#gem)" {S}/>"""


def stellarblade(p):
    return f"""
    <polygon points="128,4 142,38 142,172 114,172 114,38" fill="url(#glowv)" {S}/>
    <rect x="125.5" y="26" width="5" height="142" rx="2.5" fill="{p['trim']}" opacity=".95"/>
    <polygon points="{star(128, 66, 7, 2.2, 4)}" fill="#fff"/>
    <polygon points="{star(128, 190, 40, 17, 5)}" fill="url(#mv)" {S}/>
    {gem_circle(128, 190, 10)}
    {grip(128, 214, 28, 18)}
    <circle cx="128" cy="252" r="11" fill="url(#gem)" {S}/>
    <polygon points="{star(160, 90, 9, 2.5, 4)}" fill="#fff" opacity=".9"/>
    <polygon points="{star(98, 126, 7, 2, 4)}" fill="#fff" opacity=".8"/>"""


# ───────────────────────── Boucliers ─────────────────────────
def shield(p):
    d = "M128 16 L214 44 V120 C214 174 172 216 128 240 C84 216 42 174 42 120 V44 Z"
    return f"""
    <path d="{d}" fill="url(#wood)" {st(16)}/>
    <path d="{d}" fill="none" stroke="url(#mv)" stroke-width="9"/>
    <path d="M96 40 V210 M160 40 V210" stroke="{OUT}" stroke-width="3" opacity=".25"/>
    <path d="M60 60 C60 100 70 150 100 200" stroke="#fff" stroke-width="4" opacity=".25" fill="none" stroke-linecap="round"/>
    <circle cx="128" cy="116" r="30" fill="url(#mh)" {S}/>
    <circle cx="128" cy="116" r="16" fill="url(#gold)" {st(4)}/>
    <ellipse cx="121" cy="108" rx="5" ry="3.5" {HI}/>
    {''.join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="url(#gold)" stroke="{OUT}" stroke-width="2.5"/>' for x, y in [(70, 52), (186, 52), (56, 112), (200, 112), (128, 224)])}"""


def aegis(p):
    return f"""
    <circle cx="128" cy="130" r="112" fill="url(#gold)" {st(8)}/>
    <circle cx="128" cy="130" r="94" fill="{darken(p['metal'][2], .3)}" {st(4)}/>
    <polygon points="{star(128, 130, 86, 52, 12)}" fill="url(#gold)" {st(4)}/>
    <circle cx="128" cy="130" r="46" fill="url(#mv)" {S}/>
    {gem_circle(128, 130, 30)}
    {''.join(f'<circle cx="{128 + 103 * __import__("math").cos(__import__("math").radians(a)):.1f}" cy="{130 + 103 * __import__("math").sin(__import__("math").radians(a)):.1f}" r="5" fill="{p["trim"]}" stroke="{OUT}" stroke-width="2.5"/>' for a in range(0, 360, 45))}
    <path d="M60 80 C72 56 92 40 116 34" stroke="#fff" stroke-width="6" opacity=".4" fill="none" stroke-linecap="round"/>"""
