// ---- Données de jeu ----

export const DAYS = ["L", "M", "M", "J", "V", "S", "D"];

export const RECURRENCES = [
  { id: "daily", label: "Quotidienne" },
  { id: "weekly", label: "Hebdomadaire" },
  { id: "custom", label: "Jours précis" },
];

export const AVATARS = [
  { name: "Chevalier", palette: ["#3a2f2f", "#e8b796", "#c23b22", "#4a6da7", "#f4d03f", "#2c3e50"] },
  { name: "Mage", palette: ["#2d2440", "#e8b796", "#7b4fbf", "#4a6da7", "#f4d03f", "#1a1a2e"] },
  { name: "Rôdeur", palette: ["#2d3a2f", "#e8b796", "#3f7d20", "#8b5a2b", "#f4d03f", "#1e2d1f"] },
];

export const AVATAR_SPRITE = [
  [0, 0, 1, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 0],
  [0, 1, 2, 2, 2, 2, 1, 0],
  [0, 1, 2, 3, 3, 2, 1, 0],
  [0, 0, 1, 1, 1, 1, 0, 0],
  [0, 4, 4, 5, 5, 4, 4, 0],
  [0, 4, 4, 5, 5, 4, 4, 0],
  [0, 0, 6, 6, 6, 6, 0, 0],
];

export const SHOP_ITEMS = [
  { id: "sword", name: "Épée de Fer", type: "Arme", cost: 100, emoji: "⚔️" },
  { id: "shield", name: "Bouclier de Chêne", type: "Bouclier", cost: 120, emoji: "🛡️" },
  { id: "helmet", name: "Casque d'Acier", type: "Casque", cost: 80, emoji: "⛑️" },
  { id: "amulet", name: "Amulette de Chance", type: "Accessoire", cost: 200, emoji: "📿" },
  { id: "armor", name: "Plastron Runique", type: "Armure", cost: 250, emoji: "🥼" },
  { id: "boots", name: "Bottes du Voyageur", type: "Bottes", cost: 60, emoji: "🥾" },
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
