"""Primitives SVG et palettes de rareté pour les sprites d'objets.

Les palettes doivent rester alignées avec PALETTES de src/lib/game/data.js.
"""
OUT = "#1c2030"           # contour

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
