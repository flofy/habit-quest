# ⚔️ Habit Quest

Tracker d'habitudes RPG open source : chaque habitude accomplie donne de l'XP et de l'or à votre personnage pixel art.

Inspiré de Pixelio, développé par la communauté.

## ✨ Fonctionnalités

- Habitudes avec récurrence quotidienne, hebdomadaire ou jours précis
- XP et pièces d'or par habitude accomplie, montée de niveau avec bonus
- Avatar pixel art (3 classes) avec équipement visible
- Boutique d'équipement à acheter puis équiper
- Expéditions dans 3 régions avec récompenses aléatoires
- Séries (streaks), statistiques et journal d'aventure
- Sauvegarde automatique en localStorage — aucun backend
- Modèles d'habitudes pré-remplis pour démarrer

## 🛠 Stack

- Svelte 5 (runes)
- Vite 6
- Tailwind CSS v4 (plugin Vite officiel)
- Design system shadcn-svelte (tokens + composants ui/)

## 🚀 Démarrage

```bash
npm install
npm run dev
```

Build de production :

```bash
npm run build
npm run preview
```

## 🧩 À propos des composants UI

Le dossier src/lib/components/ui/ suit les conventions shadcn-svelte
(Button, Card, Badge, Progress, Tabs). Les composants inclus sont des
versions simplifiées sans dépendance à bits-ui, pour garder le projet léger.

Pour adopter l'ensemble complet de shadcn-svelte :

```bash
npx shadcn-svelte@latest add button card badge progress tabs dialog select
```

Le fichier components.json est déjà configuré.

## 🗂 Structure

```
src/
├── app.css                  # Tokens shadcn (thème sombre RPG)
├── main.js
├── App.svelte               # Layout, onglets, effets XP
└── lib/
    ├── utils.js             # cn() (clsx + tailwind-merge)
    ├── game/
    │   ├── data.js          # Avatars, boutique, régions, modèles
    │   └── state.js         # Store global, logique de jeu, persistance
    └── components/
        ├── Avatar.svelte
        ├── HabitCard.svelte
        ├── HabitForm.svelte
        ├── Shop.svelte
        ├── Expeditions.svelte
        ├── Stats.svelte
        └── ui/              # Composants shadcn-svelte
```

## 🤝 Contribuer

Les PR sont les bienvenues. Le projet est volontairement simple :
pas de backend, pas de compte, tout vit dans le navigateur.

## 📄 Licence

MIT — voir LICENSE.
