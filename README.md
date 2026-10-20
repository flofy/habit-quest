# ⚔️ Habit Quest

Tracker d'habitudes RPG open source : chaque habitude accomplie donne de l'XP et de l'or à votre personnage.

Inspiré de Pixelio (Lux Studio), avec un univers de fantasy traité en vectoriel lisse plutôt qu'en pixel art.

## ✨ Fonctionnalités

- Habitudes avec récurrence quotidienne, hebdomadaire ou jours précis
- XP et pièces d'or par habitude accomplie, montée de niveau avec bonus
- Personnage vectoriel (3 classes) avec équipement visible
- Boutique d'équipement à acheter puis équiper
- Expéditions dans 3 régions avec récompenses aléatoires
- Séries (streaks), statistiques et journal d'aventure
- Sauvegarde automatique en localStorage — aucun backend
- Modèles d'habitudes pré-remplis pour démarrer
- Installation en application (PWA) : manifeste, icônes, service worker offline

## 🎨 Design

Univers RPG de fantasy rendu de façon moderne et lisse :

- Scène vivante derrière le héros : ciel de crépuscule avec lune et halo,
  étoiles scintillantes, nuages à la dérive, oiseaux, deux plans de montagnes
  enneigées, château lointain, brume, forêt, herbe et fleurs, feu de camp
  animé, lucioles
- Personnages vectoriels détaillés : cape, épaulières métalliques, visage
  (sourcils, sourire, pommettes), plis de robe, armes avec reflets
- Panneaux en relief façon bois avec grain subtil, boutons 3D à enfoncement,
  jetons or/émeraude
- Typographie Cinzel (titres) + Nunito (texte), chargées via Google Fonts
- Accessibilité : cibles tactiles >= 44px, ARIA complet, contrastes >= 4.5:1,
  support prefers-reduced-motion, icônes SVG (aucun emoji structurel)

## 🖼 Sprites PNG (optionnel)

Le héros vectoriel suffit pour démarrer, mais tu peux utiliser de vrais sprites :
dépose des PNG dans src/lib/assets/heroes/ et ils remplacent le vectoriel
automatiquement, sans toucher au code :

- hero-sword.png — Chevalier
- hero-staff.png — Mage
- hero-bow.png — Rôdeur

PNG à fond transparent recommandé (rendu en object-contain avec ombre portée douce).

### Équipement

Chaque objet de la boutique a son sprite dans src/lib/assets/items/<id>.png (14 fournis).
Il sert à la fois d'icône dans la boutique et de pièce portée sur le héros vectoriel
(emplacement réglé dans src/lib/game/sprites.js). Déposer un PNG du même nom le remplace.
Les sprites fournis sont générés par `python3 scripts/build-item-sprites.py`
(outil optionnel : pip install cairosvg pillow) ; ils ne sont pas régénérés au build.
Un seul objet par emplacement (tête, accessoire, armure, arme, bouclier, bottes) ;
chaque objet donne un bonus d'XP et/ou de pièces, affiché dans la boutique.

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

## 📱 Installation en PWA

Habit Quest est installable comme une application, avec fonctionnement hors
ligne (les données restent en localStorage) :

- Chrome / Edge desktop : icône d'installation dans la barre d'adresse
- Android (Chrome) : bannière « Ajouter à l'écran d'accueil » ou menu du navigateur
- iOS (Safari) : Partager → « Sur l'écran d'accueil »

Un bouton « Installer » apparaît directement dans la carte du héros quand le
navigateur le permet (Chrome, Edge, Samsung Internet…). Sur iPhone/iPad, une
astuce s'affiche à la place (Partager → « Sur l'écran d'accueil »), car Safari
ne fournit pas d'API d'installation.

Les icônes PNG (192, 512, maskables, 180 pour iOS) sont générées au build par
`scripts/generate-pwa-icons.mjs` (aucune dépendance) et ne sont pas versionnées.
`npm run icons` les regénère à la main. La version vectorielle
(`public/icons/icon.svg`) sert aussi de favicon.

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
├── app.css                  # Thème RPG (tokens, panneaux, grain, animations de scène)
├── main.js
├── App.svelte               # Scène du héros, onglets, effets XP, bouton d'installation
└── lib/
    ├── utils.js             # cn() (clsx + tailwind-merge)
    ├── game/
    │   ├── data.js          # Personnages, boutique, régions, modèles
    │   └── state.js         # Store global, logique de jeu, persistance
    ├── assets/heroes/       # Sprites PNG optionnels (hero-<arme>.png)
    ├── assets/items/        # Sprites PNG des objets d'équipement (<id>.png)
    └── components/
        ├── Avatar.svelte    # Héros : PNG si présent, sinon vectoriel détaillé
        ├── Icon.svelte      # Icônes SVG cohérentes (style Lucide)
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
