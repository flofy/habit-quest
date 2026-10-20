// Sprites PNG des objets : src/lib/assets/items/<id>.png (générés par
// scripts/build-item-sprites.py, ou remplacés par vos propres illustrations).
const modules = import.meta.glob("$lib/assets/items/*.png", {
  eager: true,
  query: "?url",
  import: "default",
});

export const itemSprite = (id) => modules["/src/lib/assets/items/" + id + ".png"] ?? null;

// Emplacement du sprite porté sur le héros vectoriel (viewBox 64×64) : [x, y, largeur, hauteur].
// Le sprite est ajusté dans cette boîte (preserveAspectRatio « meet »).
const WEAPON = [36.5, 22, 17, 32];
const SHIELD = [3.5, 29, 17, 21];
export const WORN = {
  sword: WEAPON, frostblade: WEAPON, stellarblade: WEAPON,
  shield: SHIELD, aegis: SHIELD,
  helmet: [20.6, 0.5, 22.4, 27],
  dragonhelm: [17, 1, 30, 27],
  crown: [23.5, 0.3, 17, 13.7],
  amulet: [26.8, 28.5, 10.4, 14],
  starheart: [27.1, 28.5, 9.8, 14],
  armor: [18.5, 24.5, 27, 20.1],
  abyssal: [18.5, 22.5, 27, 23.1],
  boots: [23.5, 48.5, 17, 12.1],
  winged: [21, 45, 22, 15],
};

// Ordre de superposition (du plus au fond au plus devant), par emplacement.
export const SLOT_Z = ["boots", "armor", "amulet", "shield", "helmet", "weapon"];
