#!/usr/bin/env python3
"""Génère les sprites PNG des objets d'équipement dans src/lib/assets/items/.

Outil de dev OPTIONNEL : les PNG sont versionnés, il n'est pas lancé au build.
Dépendances : pip install cairosvg pillow
Usage : python3 scripts/build-item-sprites.py [--sheet /tmp/planche.png]

Les dessins sont dans scripts/item_shapes.py (armes, boucliers, casques,
accessoires) et scripts/item_shape_armor.py (armures, bottes) ; les primitives
et les palettes dans scripts/item_svg.py. Chaque sprite est dessiné en SVG
(contours sombres, dégradés, reflets), rendu en PNG puis recadré au plus juste.
Pour utiliser vos propres illustrations, il suffit de déposer <id>.png dans
src/lib/assets/items/ : le fichier remplace le sprite.
"""
import io, sys, pathlib
import cairosvg
from PIL import Image

from item_shape_armor import abyssal, armor, boots, winged
from item_shapes import (
    aegis, amulet, crown, dragonhelm, frostblade, helmet, shield, starheart, stellarblade, sword,
)
from item_svg import PALETTES, defs

OUT_DIR = pathlib.Path(__file__).resolve().parent.parent / "src/lib/assets/items"
RENDER = 3                # facteur de rendu avant réduction (anti-crénelage)
MAX_SIDE = 160            # taille max (px) d'un sprite final
PAD = 6

ITEMS = {  # id: (fonction de dessin, rareté)
    "sword": (sword, "rare"), "frostblade": (frostblade, "epic"), "stellarblade": (stellarblade, "mythic"),
    "shield": (shield, "rare"), "aegis": (aegis, "legendary"),
    "helmet": (helmet, "common"), "dragonhelm": (dragonhelm, "epic"), "crown": (crown, "mythic"),
    "amulet": (amulet, "epic"), "starheart": (starheart, "legendary"),
    "armor": (armor, "legendary"), "abyssal": (abyssal, "mythic"),
    "boots": (boots, "common"), "winged": (winged, "rare"),
}


def render(item_id):
    fn, rarity = ITEMS[item_id]
    p = PALETTES[rarity]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-40 -40 336 336" width="{336 * RENDER}" height="{336 * RENDER}">'
           f'{defs(p)}{fn(p)}</svg>')
    png = cairosvg.svg2png(bytestring=svg.encode())
    im = Image.open(io.BytesIO(png)).convert("RGBA")
    box = im.getbbox()
    im = im.crop((max(0, box[0] - PAD * RENDER), max(0, box[1] - PAD * RENDER), min(im.width, box[2] + PAD * RENDER), min(im.height, box[3] + PAD * RENDER)))
    scale = MAX_SIDE / max(im.size)
    im = im.resize((max(1, round(im.width * scale)), max(1, round(im.height * scale))), Image.LANCZOS)
    # palette 256 couleurs avec transparence : ~3x plus léger, indiscernable à cette taille
    return im.quantize(colors=256, method=Image.FASTOCTREE, dither=Image.NONE).convert("RGBA")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sprites = {}
    for item_id in ITEMS:
        im = render(item_id)
        im.quantize(colors=256, method=Image.FASTOCTREE, dither=Image.NONE).save(OUT_DIR / f"{item_id}.png", optimize=True)
        sprites[item_id] = im
        print(f"{item_id:13s} {im.width}x{im.height}")
    if "--sheet" in sys.argv:
        path = sys.argv[sys.argv.index("--sheet") + 1]
        cell, cols = MAX_SIDE + 24, 5
        rows = -(-len(sprites) // cols)
        sheet = Image.new("RGBA", (cols * cell, rows * cell), (36, 40, 56, 255))
        for i, im in enumerate(sprites.values()):
            sheet.alpha_composite(im, ((i % cols) * cell + (cell - im.width) // 2, (i // cols) * cell + (cell - im.height) // 2))
        sheet.save(path)


if __name__ == "__main__":
    main()
