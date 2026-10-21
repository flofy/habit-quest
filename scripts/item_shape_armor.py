"""Dessins SVG des armures et des bottes."""
from item_svg import *  # noqa: F401,F403  (OUT, HI, S, st, gem_circle)


def armor(p, abyssal=False):
    fill = "url(#dark)" if abyssal else "url(#mv)"
    edge = "#ff7ad9" if abyssal else p["metal"][2]
    glow = f'stroke="{edge}" stroke-width="3.5" fill="none"'
    body = "M76 50 C102 66 154 66 180 50 L200 66 V214 Q128 240 56 214 V66 Z"
    spikes = ""
    if abyssal:
        spikes = (f'<polygon points="18,70 4,18 62,46" fill="url(#dark)" {S}/>'
                  f'<polygon points="238,70 252,18 194,46" fill="url(#dark)" {S}/>')
    return f"""{spikes}
    <path d="{body}" fill="{fill}" {S}/>
    <circle cx="46" cy="92" r="40" fill="{fill}" {S}/><circle cx="210" cy="92" r="40" fill="{fill}" {S}/>
    <path d="M22 92 C26 70 44 56 64 56 M234 92 C230 70 212 56 192 56" {glow}/>
    <path d="M70 80 V196 M186 80 V196" {glow if abyssal else f'stroke="#fff" stroke-width="5" opacity=".35" fill="none" stroke-linecap="round"'}/>
    <path d="M62 188 Q128 208 194 188" stroke="{OUT}" stroke-width="4" opacity=".5" fill="none"/>
    <path d="M128 92 L160 134 L128 176 L96 134 Z" fill="{'url(#gem)' if abyssal else 'url(#gold)'}" {S}/>
    <path d="M128 108 L146 134 L128 142 L110 134 Z" fill="#fff" opacity=".35"/>"""


def abyssal(p):
    return armor(p, True)


def boot(cx, p, wing=False):
    l = cx - 42
    w = ""
    if wing:
        # éventail de 3 plumes partant de la cheville, vers l'extérieur de la botte
        side = 1 if cx < 128 else -1
        bx = l + 4 if side == 1 else l + 80
        feathers = "".join(
            f'<ellipse cx="-24" cy="0" rx="27" ry="11" transform="rotate({a})" fill="url(#bone)" {st(4)}/>'
            for a in (52, 26, 0)
        )
        w = f'<g transform="translate({bx} 84) scale({side} 1)">{feathers}</g>'
    return f"""{w}
    <path d="M{l + 8} 36 H{l + 76} L{l + 72} 104 C{l + 72} 112 {l + 84} 116 {l + 84} 134 C{l + 84} 154 {l + 70} 162 {cx} 162 C{l + 14} 162 {l} 154 {l} 134 C{l} 116 {l + 12} 112 {l + 12} 104 Z" fill="url(#leather)" {S}/>
    <path d="M{l} 138 C{l} 156 {l + 14} 166 {cx} 166 C{l + 70} 166 {l + 84} 156 {l + 84} 138 C{l + 72} 148 {l + 12} 148 {l} 138 Z" fill="#2e2115" {st(3.5)}/>
    <rect x="{l + 4}" y="28" width="76" height="28" rx="9" fill="url(#gold)" {S}/>
    <path d="M{l + 20} 70 L{l + 64} 84 M{l + 20} 88 L{l + 64} 102" stroke="{OUT}" stroke-width="3.5" opacity=".6" stroke-linecap="round"/>
    <path d="M{l + 16} 66 V108" stroke="#fff" stroke-width="4" opacity=".3" stroke-linecap="round"/>"""


def boots(p): return boot(70, p) + boot(186, p)
def winged(p): return boot(70, p, True) + boot(186, p, True)
