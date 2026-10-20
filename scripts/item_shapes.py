"""Dessins SVG des objets (une fonction par objet) et table ITEMS.

Utilisé par scripts/build-item-sprites.py ; les primitives et les palettes
vivent dans scripts/item_svg.py. Les palettes doivent rester alignées avec
PALETTES de src/lib/game/data.js.
"""
from item_svg import *  # noqa: F401,F403  (OUT, HI, S, st, gem_circle, grip, star, darken)


# ───── Armes ─────
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


# ───── Boucliers ─────
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


# ───── Casques ─────
SALLET = ("M54 190 L58 108 C60 62 90 28 128 28 C166 28 196 62 198 108 L202 190 "
          "L170 190 C166 150 156 112 128 106 C100 112 90 150 86 190 Z")
CLIP = f'<clipPath id="sal"><path d="{SALLET}"/></clipPath>'
BAND = f'<rect x="40" y="82" width="176" height="22" fill="#000" opacity=".28" clip-path="url(#sal)"/>'


def helmet(p):
    return f"""{CLIP}
    <path d="M128 40 C112 16 148 8 178 26 C158 28 146 36 142 52 Z" fill="#ee5a4a" {S}/>
    <path d="{SALLET}" fill="url(#mv)" {S}/>
    {BAND}
    <path d="M128 30 V82" stroke="{p['metal'][2]}" stroke-width="6" stroke-linecap="round" opacity=".7"/>
    <path d="M70 100 C72 66 94 44 120 38 C100 56 90 80 88 118 Z" {HI}/>
    {''.join(f'<circle cx="{x}" cy="{y}" r="3.5" fill="{p["trim"]}" stroke="{OUT}" stroke-width="2"/>' for x, y in [(66, 176), (190, 176), (70, 128), (186, 128)])}"""


def dragonhelm(p):
    horn_l = "M70 78 C34 70 16 38 30 4 C42 34 64 50 94 58 Z"
    horn_r = "M186 78 C222 70 240 38 226 4 C214 34 192 50 162 58 Z"
    spikes = "".join(f'<polygon points="{x - 9},40 {x},{y} {x + 9},40" fill="url(#gold)" {st(3.5)}/>' for x, y in [(108, 14), (128, 2), (148, 14)])
    return f"""{CLIP}
    <path d="{horn_l}" fill="url(#bone)" {S}/><path d="{horn_r}" fill="url(#bone)" {S}/>
    {spikes}
    <path d="{SALLET}" fill="url(#mv)" {S}/>
    {BAND}
    <path d="M64 120 L96 104 L96 122 Z M192 120 L160 104 L160 122 Z" fill="{p['gem']}" {st(3.5)}/>
    {gem_circle(128, 62, 13)}
    <path d="M70 100 C72 66 94 44 120 38 C100 56 90 80 88 118 Z" {HI}/>"""


def crown(p):
    pts = "46,170 36,74 86,118 128,52 170,118 220,74 210,170"
    return f"""
    <polygon points="{pts}" fill="url(#mv)" {S}/>
    <rect x="42" y="150" width="172" height="36" rx="11" fill="url(#goldh)" {S}/>
    {gem_circle(36, 68, 12)}{gem_circle(128, 44, 14)}{gem_circle(220, 68, 12)}
    {''.join(f'<polygon points="{x},156 {x + 12},168 {x},180 {x - 12},168" fill="url(#gem)" {st(3.5)}/>' for x in (82, 128, 174))}
    <path d="M60 140 L48 90 L78 118" stroke="#fff" stroke-width="5" opacity=".45" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <polygon points="{star(190, 28, 9, 2.5, 4)}" fill="#fff"/>"""


# ───── Accessoires ─────
CHAIN = "M52 10 C54 82 96 124 128 124 C160 124 202 82 204 10"


def chain(p):
    return (f'<path d="{CHAIN}" fill="none" stroke="{OUT}" stroke-width="15" stroke-linecap="round"/>'
            f'<path d="{CHAIN}" fill="none" stroke="url(#goldh)" stroke-width="7" stroke-linecap="round" stroke-dasharray="14 5"/>')


def amulet(p):
    return f"""{chain(p)}
    <circle cx="128" cy="170" r="60" fill="url(#gold)" {S}/>
    <circle cx="128" cy="170" r="46" fill="none" stroke="{darken(p['trim'], .45)}" stroke-width="4"/>
    <path d="M128 122 L166 170 L128 218 L90 170 Z" fill="url(#gem)" {S}/>
    <path d="M128 132 L152 168 L128 172 L104 168 Z" fill="#fff" opacity=".35"/>
    <circle cx="128" cy="122" r="9" fill="url(#gold)" {st(4)}/>"""


def starheart(p):
    return f"""{chain(p)}
    <polygon points="{star(128, 172, 70, 40, 8, -90)}" fill="url(#gold)" {S}/>
    <circle cx="128" cy="172" r="34" fill="url(#mv)" {S}/>
    {gem_circle(128, 172, 24)}
    {''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="url(#gem)" stroke="{OUT}" stroke-width="2.5"/>' for x, y in [(128, 112), (188, 172), (128, 232), (68, 172)])}"""
