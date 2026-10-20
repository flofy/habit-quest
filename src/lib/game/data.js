// ---- Données de jeu ----

export const DAYS = ["L", "M", "M", "J", "V", "S", "D"];

export const RECURRENCES = [
  { id: "daily", label: "Quotidienne" },
  { id: "weekly", label: "Hebdomadaire" },
  { id: "custom", label: "Jours précis" },
];

// Personnages vectoriels lisses : un ton de robe clair/sombre par classe.
export const AVATARS = [
  {
    name: "Chevalier",
    skin: "#eebf9a",
    hair: "#6b4423",
    hood: "#3b4d63",
    robe: ["#5a7bd4", "#37529c"],
    belt: "#7a4a22",
    weapon: "sword",
  },
  {
    name: "Mage",
    skin: "#eebf9a",
    hair: "#e8e4d8",
    hood: "#4a3a6e",
    robe: ["#7b5fc0", "#5a4396"],
    belt: "#3a2b52",
    weapon: "staff",
  },
  {
    name: "Rôdeur",
    skin: "#eebf9a",
    hair: "#3e2a16",
    hood: "#2e4a2a",
    robe: ["#5f9448", "#3f6b31"],
    belt: "#6b4226",
    weapon: "bow",
  },
];

// Emplacements d'équipement (un objet par emplacement), dans l'ordre d'affichage
// du mannequin : colonne gauche puis colonne droite.
export const SLOTS = [
  { id: "helmet", label: "Tête" },
  { id: "amulet", label: "Accessoire" },
  { id: "armor", label: "Armure" },
  { id: "weapon", label: "Arme" },
  { id: "shield", label: "Bouclier" },
  { id: "boots", label: "Bottes" },
];

export const RARITIES = {
  common: { label: "Commun", color: "#b8c4a3" },
  rare: { label: "Rare", color: "#7db9ff" },
  epic: { label: "Épique", color: "#c19bff" },
  legendary: { label: "Légendaire", color: "#f4cd6f" },
  mythic: { label: "Mythique", color: "#ff7ad9" },
};

// Palettes de couleur par rareté, utilisées par les icônes et par les couches
// dessinées sur le héros : metal = [clair, moyen, sombre], trim = liserés, gem = gemmes.
export const PALETTES = {
  common: { metal: ["#e8edf2", "#b9c4ce", "#8b97a3"], trim: "#c9a24a", gem: "#4faf62", glow: null },
  rare: { metal: ["#e2efff", "#9cc4f5", "#5f8fc9"], trim: "#8ec5ff", gem: "#4f9fd8", glow: "#7db9ff" },
  epic: { metal: ["#efe5ff", "#c19bff", "#8a5fd0"], trim: "#e0c6ff", gem: "#b06cf0", glow: "#c19bff" },
  legendary: { metal: ["#fff6d2", "#f4cd6f", "#d99a2b"], trim: "#fff3b0", gem: "#ee8174", glow: "#f4cd6f" },
  mythic: { metal: ["#ffe0f6", "#ff8fdc", "#c2409f"], trim: "#9ff3ff", gem: "#6ff0ff", glow: "#ff7ad9" },
};

export const SHOP_ITEMS = [
  { id: "sword", slot: "weapon", rarity: "rare", bonus: { xp: 0.1 }, name: "Épée de Fer", type: "Arme", cost: 100, emoji: "⚔️", desc: "Une lame simple mais fiable." },
  { id: "shield", slot: "shield", rarity: "rare", bonus: { coins: 0.1 }, name: "Bouclier de Chêne", type: "Bouclier", cost: 120, emoji: "🛡️", desc: "Cerclé de fer, solide comme un vieux chêne." },
  { id: "helmet", slot: "helmet", rarity: "common", bonus: { xp: 0.05 }, name: "Casque d'Acier", type: "Tête", cost: 80, emoji: "⛑️", desc: "Protège la tête et impressionne les gobelins." },
  { id: "amulet", slot: "amulet", rarity: "epic", bonus: { coins: 0.15 }, name: "Amulette de Chance", type: "Accessoire", cost: 200, emoji: "📿", desc: "Une gemme qui murmure au hasard." },
  { id: "armor", slot: "armor", rarity: "legendary", bonus: { xp: 0.2 }, name: "Plastron Runique", type: "Armure", cost: 250, emoji: "🥼", desc: "Gravé de runes anciennes qui luisent la nuit." },
  { id: "boots", slot: "boots", rarity: "common", bonus: { coins: 0.05 }, name: "Bottes du Voyageur", type: "Bottes", cost: 60, emoji: "🥾", desc: "Faites pour les longues routes." },
  { id: "winged", slot: "boots", rarity: "rare", bonus: { coins: 0.1, xp: 0.05 }, name: "Bottes Ailées", type: "Bottes", cost: 150, emoji: "🪽", desc: "Légères comme une plume, rapides comme le vent." },
  { id: "dragonhelm", slot: "helmet", rarity: "epic", bonus: { xp: 0.1, coins: 0.05 }, name: "Heaume Draconique", type: "Tête", cost: 300, emoji: "🐲", desc: "Forgé dans l'écaille d'un jeune dragon." },
  { id: "frostblade", slot: "weapon", rarity: "epic", bonus: { xp: 0.15 }, name: "Lame de Givre", type: "Arme", cost: 350, emoji: "🧊", desc: "Taillée dans un glacier millénaire. Elle ne fond jamais." },
  { id: "aegis", slot: "shield", rarity: "legendary", bonus: { coins: 0.2 }, name: "Égide Solaire", type: "Bouclier", cost: 450, emoji: "☀️", desc: "Un soleil de poche qui éblouit les ennemis." },
  { id: "starheart", slot: "amulet", rarity: "legendary", bonus: { xp: 0.1, coins: 0.15 }, name: "Cœur d'Étoile", type: "Accessoire", cost: 500, emoji: "🌟", desc: "Une étoile tombée du ciel, encore tiède." },
  { id: "crown", slot: "helmet", rarity: "mythic", bonus: { xp: 0.15, coins: 0.15 }, name: "Couronne Astrale", type: "Tête", cost: 800, emoji: "👑", desc: "Seuls les plus assidus méritent de la porter." },
  { id: "stellarblade", slot: "weapon", rarity: "mythic", bonus: { xp: 0.25, coins: 0.1 }, name: "Lame Stellaire", type: "Arme", cost: 900, emoji: "🌠", desc: "Une lame de lumière pure, forgée entre deux constellations." },
  { id: "abyssal", slot: "armor", rarity: "mythic", bonus: { xp: 0.25, coins: 0.1 }, name: "Armure Abyssale", type: "Armure", cost: 1000, emoji: "🌌", desc: "Née du néant, elle absorbe la lumière." },
];

export const REGIONS = [
  { id: "forest", name: "Forêt d'Émeraude", cost: 20, emoji: "🌲", duration: 10000, rewards: { coins: [15, 40], xp: [5, 15] } },
  { id: "cave", name: "Cavernes Sombres", cost: 50, emoji: "🕳️", duration: 20000, rewards: { coins: [40, 90], xp: [15, 30] } },
  { id: "mountain", name: "Pic du Dragon", cost: 120, emoji: "🏔️", duration: 30000, rewards: { coins: [90, 180], xp: [30, 60] } },
];

export const TEMPLATES = [
  { name: "Boire 2L d'eau", emoji: "💧", rec: "daily", xp: 10, coins: 5 },
  { name: "Méditer 10 min", emoji: "🧘", rec: "daily", xp: 12, coins: 6 },
  { name: "Lire 20 pages", emoji: "📖", rec: "daily", xp: 15, coins: 8 },
  { name: "Courir 30 min", emoji: "🏃", rec: "weekly", xp: 25, coins: 15 },
  { name: "Faire du sport", emoji: "💪", rec: "custom", days: [1, 3, 5], xp: 20, coins: 12 },
];

export const XP_PER_LEVEL = (level) => 50 + (level - 1) * 30;

export const itemById = (id) => SHOP_ITEMS.find((i) => i.id === id);
export const paletteOf = (id) => PALETTES[itemById(id)?.rarity ?? "common"];
