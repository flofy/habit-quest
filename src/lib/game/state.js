import { writable, get } from "svelte/store";
import { TEMPLATES, XP_PER_LEVEL, AVATARS } from "./data.js";

const KEY = "habit-quest-save";

export const uid = () => Math.random().toString(36).slice(2, 10);
export const todayISO = () => new Date().toISOString().slice(0, 10);
export const dayIndex = () => (new Date().getDay() + 6) % 7; // 0 = lundi

function load() {
  try {
    return JSON.parse(localStorage.getItem(KEY));
  } catch {
    return null;
  }
}

const initial =
  load() ??
  {
    habits: TEMPLATES.map((t) => ({ id: uid(), ...t, history: [] })),
    xp: 0,
    level: 1,
    coins: 30,
    equipped: [],
    owned: [],
    avatar: 0,
    log: [],
  };

export const game = writable(initial);
game.subscribe((g) => localStorage.setItem(KEY, JSON.stringify(g)));

export const xpNeeded = (level) => XP_PER_LEVEL(level);

export function isDue(habit) {
  if (habit.rec === "daily" || habit.rec === "weekly") return true;
  return (habit.days || []).includes(dayIndex());
}

export function streakOf(habit) {
  const days = [...(habit.history || [])].sort().reverse();
  if (days.length === 0) return 0;
  const t = todayISO();
  const y = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
  let cursorTime;
  let streak = 0;
  if (days[0] === t) {
    streak = 1;
    cursorTime = Date.now();
  } else if (days[0] === y) {
    streak = 1;
    cursorTime = Date.now() - 86400000;
  } else {
    return 0;
  }
  for (let i = 1; i < days.length; i++) {
    cursorTime -= 86400000;
    const iso = new Date(cursorTime).toISOString().slice(0, 10);
    if (days[i] === iso) streak++;
    else break;
  }
  return streak;
}

function gain(g, xp, coins, label) {
  g.xp += xp;
  g.coins += coins;
  let levelUps = 0;
  while (g.xp >= XP_PER_LEVEL(g.level)) {
    g.xp -= XP_PER_LEVEL(g.level);
    g.level++;
    g.coins += 25;
    levelUps++;
  }
  g.log = [{ t: label, d: todayISO() }, ...g.log].slice(0, 30);
  return levelUps;
}

export function completeHabit(habit) {
  const today = todayISO();
  let levelUps = 0;
  game.update((g) => {
    const h = g.habits.find((x) => x.id === habit.id);
    if (!h || h.history.includes(today)) return g;
    h.history = [...h.history, today];
    levelUps = gain(g, habit.xp, habit.coins, "+" + habit.xp + " XP · +" + habit.coins + " 🪙 · " + habit.name);
    return g;
  });
  return levelUps;
}

export function undoHabit(habit) {
  const today = todayISO();
  game.update((g) => {
    const h = g.habits.find((x) => x.id === habit.id);
    if (!h || !h.history.includes(today)) return g;
    h.history = h.history.filter((d) => d !== today);
    g.xp = Math.max(0, g.xp - habit.xp);
    g.coins = Math.max(0, g.coins - habit.coins);
    return g;
  });
}

export function addHabit(data) {
  game.update((g) => ({
    ...g,
    habits: [...g.habits, { id: uid(), history: [], ...data }],
  }));
}

export function deleteHabit(id) {
  game.update((g) => ({ ...g, habits: g.habits.filter((h) => h.id !== id) }));
}

export function buyItem(item) {
  const g = get(game);
  if (g.coins < item.cost || g.owned.includes(item.id)) return false;
  game.update((s) => ({
    ...s,
    coins: s.coins - item.cost,
    owned: [...s.owned, item.id],
    log: [{ t: item.emoji + " " + item.name + " acheté", d: todayISO() }, ...s.log].slice(0, 30),
  }));
  return true;
}

export function toggleEquip(id) {
  game.update((g) => ({
    ...g,
    equipped: g.equipped.includes(id) ? g.equipped.filter((i) => i !== id) : [...g.equipped, id],
  }));
}

export function cycleAvatar() {
  game.update((g) => ({ ...g, avatar: (g.avatar + 1) % AVATARS.length, equipped: [] }));
}

export function startExpedition(region) {
  const g = get(game);
  if (g.coins < region.cost) return false;
  game.update((s) => ({ ...s, coins: s.coins - region.cost }));
  return true;
}

export function finishExpedition(region) {
  const roll = ([min, max]) => Math.floor(min + Math.random() * (max - min));
  const coins = roll(region.rewards.coins);
  const xp = roll(region.rewards.xp);
  let levelUps = 0;
  game.update((g) => {
    levelUps = gain(g, xp, coins, region.emoji + " Expédition : +" + coins + " 🪙 +" + xp + " XP");
    return g;
  });
  return { coins, xp, levelUps };
}

export function totalStats(g) {
  return {
    completions: g.habits.reduce((a, h) => a + (h.history?.length || 0), 0),
    bestStreak: Math.max(0, ...g.habits.map(streakOf), 0),
  };
}

export function resetGame() {
  localStorage.removeItem(KEY);
  location.reload();
}
