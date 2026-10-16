<script>
  import { Card, CardContent } from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Progress } from "$lib/components/ui/progress/index.js";
  import { Tabs, TabsList, TabsTrigger } from "$lib/components/ui/tabs/index.js";
  import { game, isDue, todayISO, xpNeeded, uid } from "$lib/game/state.js";
  import { AVATARS } from "$lib/game/data.js";
  import Avatar from "$lib/components/Avatar.svelte";
  import HabitCard from "$lib/components/HabitCard.svelte";
  import HabitForm from "$lib/components/HabitForm.svelte";
  import Shop from "$lib/components/Shop.svelte";
  import Expeditions from "$lib/components/Expeditions.svelte";
  import Stats from "$lib/components/Stats.svelte";
  import Icon from "$lib/components/Icon.svelte";

  const TABS = [
    { value: "quests", label: "Quêtes", icon: "flag" },
    { value: "shop", label: "Boutique", icon: "cart" },
    { value: "explore", label: "Expéditions", icon: "map" },
    { value: "stats", label: "Stats", icon: "chart" },
  ];

  let tab = $state("quests");
  let showForm = $state(false);
  let fx = $state([]);
  let toast = $state(null);
  let toastTimer;

  // Installation PWA : le navigateur annonce sa disponibilité via
  // beforeinstallprompt ; on capture l'événement pour proposer un vrai
  // bouton dans l'app (sur mobile, l'option est sinon enterrée dans le
  // menu du navigateur, et iOS ne la propose pas du tout).
  let installEvent = $state(null);
  let iosHint = $state(false);

  const avatar = $derived(AVATARS[$game.avatar]);
  const dueHabits = $derived($game.habits.filter(isDue));
  const doneToday = $derived($game.habits.filter((h) => h.history.includes(todayISO())).length);

  $effect(() => {
    // Déjà installée (lancée depuis l'écran d'accueil) : rien à proposer.
    const standalone =
      window.matchMedia("(display-mode: standalone)").matches ||
      window.navigator.standalone === true;
    if (standalone) return;

    // Safari iOS ne déclenche jamais beforeinstallprompt :
    // on affiche une astuce (Partager -> Sur l'écran d'accueil).
    if (/iphone|ipad|ipod/i.test(navigator.userAgent)) {
      iosHint = true;
      return;
    }

    function onPrompt(e) {
      e.preventDefault();
      installEvent = e;
    }
    window.addEventListener("beforeinstallprompt", onPrompt);
    return () => window.removeEventListener("beforeinstallprompt", onPrompt);
  });

  async function install() {
    if (!installEvent) return;
    installEvent.prompt();
    const { outcome } = await installEvent.userChoice;
    installEvent = null;
    if (outcome === "accepted") showToast("🎉 Habit Quest installée !");
  }

  function handleFx(detail) {
    const rect = detail.el.getBoundingClientRect();
    fx = detail.texts.map((t, i) => ({
      id: uid(),
      ...t,
      x: rect.left + rect.width / 2 + (i - 1) * 30,
      y: rect.top,
    }));
    setTimeout(() => (fx = []), 1500);
    if (detail.levelUps > 0) showToast("🎉 Niveau " + $game.level + " !");
  }

  function showToast(msg) {
    toast = msg;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => (toast = null), 2500);
  }
</script>

<div class="min-h-screen">
  {#if fx.length > 0}
    <div class="pointer-events-none fixed inset-0 z-50 overflow-hidden" aria-hidden="true">
      {#each fx as f (f.id)}
        <span
          class="absolute text-lg font-extrabold"
          style="left: {f.x}px; top: {f.y}px; color: {f.color}; text-shadow: 0 1px 3px rgba(0,0,0,.6); animation: float-up 1.2s ease-out forwards;"
        >
          {f.text}
        </span>
      {/each}
    </div>
  {/if}

  {#if toast}
    <div
      class="panel fixed bottom-8 left-1/2 z-50 max-w-[calc(100vw-2rem)] -translate-x-1/2 px-4 py-2 text-center text-sm font-bold text-primary"
      role="status"
      aria-live="polite"
    >
      {toast}
    </div>
  {/if}

  <div class="mx-auto max-w-2xl px-4 pb-12 pt-6">
    <!-- Héros : scène vivante de crépuscule -->
    <Card class="mb-4 overflow-hidden">
      <div class="relative h-44 w-full overflow-hidden rounded-t-[15px]">
        <svg
          viewBox="0 0 640 220"
          preserveAspectRatio="xMidYMax slice"
          class="absolute inset-0 h-full w-full"
          aria-hidden="true"
        >
          <defs>
            <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#2c4763" />
              <stop offset="0.5" stop-color="#33506e" />
              <stop offset="0.78" stop-color="#7a5a6e" />
              <stop offset="1" stop-color="#c98a5a" />
            </linearGradient>
            <radialGradient id="moonglow">
              <stop offset="0" stop-color="#f5e9c9" stop-opacity="0.55" />
              <stop offset="1" stop-color="#f5e9c9" stop-opacity="0" />
            </radialGradient>
            <linearGradient id="mist" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#d9c9a8" stop-opacity="0" />
              <stop offset="1" stop-color="#d9c9a8" stop-opacity="0.22" />
            </linearGradient>
            <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#2c4f33" />
              <stop offset="1" stop-color="#1e3825" />
            </linearGradient>
            <radialGradient id="fireglow">
              <stop offset="0" stop-color="#ffb347" stop-opacity="0.5" />
              <stop offset="1" stop-color="#ffb347" stop-opacity="0" />
            </radialGradient>
            <linearGradient id="flame" x1="0" y1="1" x2="0" y2="0">
              <stop offset="0" stop-color="#e0521f" />
              <stop offset="0.55" stop-color="#f2913a" />
              <stop offset="1" stop-color="#ffd24a" />
            </linearGradient>
          </defs>

          <!-- ciel -->
          <rect width="640" height="220" fill="url(#sky)" />

          <!-- lune -->
          <circle cx="500" cy="52" r="46" fill="url(#moonglow)" />
          <circle cx="500" cy="52" r="15" fill="#f5e9c9" />
          <circle cx="495" cy="48" r="2.6" fill="#e3d5ae" opacity="0.7" />
          <circle cx="505" cy="57" r="1.8" fill="#e3d5ae" opacity="0.6" />
          <circle cx="502" cy="45" r="1.2" fill="#e3d5ae" opacity="0.5" />

          <!-- étoiles -->
          <circle cx="80" cy="30" r="1.5" fill="#dfe8f2" class="twinkle" />
          <circle cx="150" cy="55" r="1.1" fill="#dfe8f2" class="twinkle" style="animation-delay: 0.7s" />
          <circle cx="240" cy="26" r="1.3" fill="#dfe8f2" class="twinkle" style="animation-delay: 1.4s" />
          <circle cx="330" cy="48" r="1" fill="#dfe8f2" class="twinkle" style="animation-delay: 2.1s" />
          <circle cx="410" cy="24" r="1.2" fill="#dfe8f2" class="twinkle" style="animation-delay: 0.35s" />
          <circle cx="580" cy="30" r="1.4" fill="#dfe8f2" class="twinkle" style="animation-delay: 1.8s" />
          <circle cx="615" cy="60" r="1" fill="#dfe8f2" class="twinkle" style="animation-delay: 1.1s" />
          <circle cx="45" cy="62" r="1.1" fill="#dfe8f2" class="twinkle" style="animation-delay: 2.6s" />

          <!-- nuages -->
          <g class="drift" opacity="0.35">
            <ellipse cx="140" cy="66" rx="46" ry="9" fill="#8aa3bd" />
            <ellipse cx="168" cy="60" rx="26" ry="7" fill="#8aa3bd" />
          </g>
          <g class="drift" style="animation-duration: 52s" opacity="0.28">
            <ellipse cx="430" cy="38" rx="38" ry="7" fill="#8aa3bd" />
            <ellipse cx="452" cy="34" rx="20" ry="5" fill="#8aa3bd" />
          </g>

          <!-- oiseaux -->
          <g stroke="#1c2836" stroke-width="1.6" fill="none" stroke-linecap="round" opacity="0.8">
            <path d="M210 78 q4 -4 8 0 M218 78 q4 -4 8 0" />
            <path d="M248 64 q3 -3 6 0 M254 64 q3 -3 6 0" />
          </g>

          <!-- montagnes lointaines avec neige -->
          <path d="M-20 138 L60 84 L110 118 L190 66 L260 120 L330 92 L400 128 L470 96 L540 126 L620 100 L660 120 L660 220 L-20 220 Z" fill="#2a3d52" />
          <path d="M190 66 L203 76 L196 80 L186 76 Z M60 84 L72 93 L64 97 L54 92 Z M470 96 L480 104 L472 108 L462 103 Z" fill="#e8eef2" opacity="0.85" />

          <!-- château lointain -->
          <g fill="#22324a">
            <rect x="255" y="86" width="14" height="26" />
            <path d="M253 86 L262 74 L271 86 Z" />
            <rect x="276" y="96" width="10" height="16" />
            <path d="M275 96 L281 88 L287 96 Z" />
          </g>

          <!-- chaîne avant -->
          <path d="M-20 168 L70 126 L150 158 L250 116 L350 162 L450 130 L540 164 L660 138 L660 220 L-20 220 Z" fill="#22324a" />
          <path d="M250 116 L260 124 L252 128 L243 123 Z M70 126 L79 133 L72 136 L64 131 Z" fill="#d9e2ea" opacity="0.8" />

          <!-- brume entre les plans -->
          <rect x="-20" y="150" width="700" height="34" fill="url(#mist)" />

          <!-- forêt -->
          <g fill="#17251c">
            <path d="M-20 190 L20 156 L44 188 L-20 188 Z" />
            <path d="M30 190 L58 160 L82 190 Z" />
            <path d="M560 190 L592 158 L620 190 Z" />
            <path d="M610 190 L640 166 L660 190 Z" />
          </g>
          <g fill="#1e3226">
            <path d="M0 196 L26 170 L48 196 Z" />
            <path d="M594 196 L616 172 L640 196 Z" />
          </g>

          <!-- sol -->
          <rect y="192" width="640" height="28" fill="url(#ground)" />
          <ellipse cx="320" cy="200" rx="150" ry="16" fill="#2c4f33" />
          <ellipse cx="320" cy="198" rx="110" ry="10" fill="#35603e" opacity="0.8" />

          <!-- touffes d'herbe et fleurs -->
          <g stroke="#4a7a52" stroke-width="1.4" stroke-linecap="round" fill="none">
            <path d="M120 206 q2 -8 4 0 M126 206 q1 -6 5 -1 M132 207 q2 -7 5 0" />
            <path d="M500 208 q2 -8 4 0 M506 208 q1 -6 5 -1 M512 209 q2 -7 5 0" />
            <path d="M240 210 q1 -7 3 0 M245 210 q2 -5 4 -1" />
            <path d="M420 209 q1 -7 3 0 M425 209 q2 -5 4 -1" />
          </g>
          <circle cx="137" cy="204" r="1.8" fill="#e9b44c" />
          <circle cx="518" cy="206" r="1.8" fill="#d9a0c0" />
          <circle cx="243" cy="208" r="1.4" fill="#e9b44c" />
          <circle cx="428" cy="207" r="1.4" fill="#d9a0c0" />

          <!-- feu de camp -->
          <g>
            <ellipse cx="562" cy="212" rx="26" ry="8" fill="url(#fireglow)" />
            <rect x="550" y="208" width="24" height="4" rx="2" fill="#5a4026" />
            <rect x="554" y="210" width="18" height="3" rx="1.5" fill="#3d2b18" />
            <g class="flicker">
              <path d="M562 207 C556 200 558 194 562 189 C561 194 566 196 564 191 C568 197 566 203 562 207 Z" fill="url(#flame)" />
              <path d="M562 206 C559 202 560 198 562 195 C563 199 561 202 562 206 Z" fill="#fff3b0" opacity="0.9" />
            </g>
          </g>

          <!-- lucioles -->
          <circle cx="240" cy="180" r="1.6" fill="#ffe98a" class="firefly" />
          <circle cx="410" cy="170" r="1.4" fill="#ffe98a" class="firefly" style="animation-delay: 1.2s" />
          <circle cx="180" cy="150" r="1.3" fill="#ffe98a" class="firefly" style="animation-delay: 2.4s" />
          <circle cx="480" cy="185" r="1.6" fill="#ffe98a" class="firefly" style="animation-delay: 3.5s" />
          <circle cx="300" cy="160" r="1.2" fill="#ffe98a" class="firefly" style="animation-delay: 4.8s" />
        </svg>

        <div class="absolute bottom-3 left-1/2 -translate-x-1/2 drop-shadow-[0_4px_8px_rgba(0,0,0,0.45)]">
          <Avatar {avatar} size={96} equipped={$game.equipped} />
        </div>
      </div>
      <CardContent class="space-y-3 p-4">
        <div class="flex flex-wrap items-center justify-between gap-2">
          <div class="nameplate px-3 py-1 font-display text-sm font-bold">
            {avatar.name} · Niveau {$game.level}
          </div>
          <div class="flex items-center gap-2">
            {#if installEvent}
              <Button variant="secondary" size="sm" onclick={install}>
                <Icon name="download" size={16} label="" />
                Installer
              </Button>
            {/if}
            <span class="chip chip-gold" aria-label="Pièces d'or : {$game.coins}">
              🪙 {$game.coins}
            </span>
          </div>
        </div>
        {#if iosHint}
          <div
            class="flex items-center justify-between gap-2 rounded-lg border border-border/60 bg-secondary/40 px-3 py-2 text-xs text-muted-foreground"
          >
            <span>📱 iPhone : bouton Partager, puis « Sur l'écran d'accueil »</span>
            <button
              type="button"
              class="shrink-0 cursor-pointer rounded p-1 hover:text-foreground"
              aria-label="Masquer l'astuce d'installation"
              onclick={() => (iosHint = false)}
            >
              <Icon name="x" size={14} label="" />
            </button>
          </div>
        {/if}
        <Progress
          value={$game.xp}
          max={xpNeeded($game.level)}
          label="XP : {$game.xp} sur {xpNeeded($game.level)}"
        />
        <div class="text-xs font-bold text-muted-foreground">
          {$game.xp} / {xpNeeded($game.level)} XP
        </div>
      </CardContent>
    </Card>

    <Tabs bind:value={tab} class="mb-4">
      <TabsList>
        {#each TABS as t (t.value)}
          <TabsTrigger value={t.value}>
            <Icon name={t.icon} size={16} label="" />
            <span class="truncate">{t.label}</span>
          </TabsTrigger>
        {/each}
      </TabsList>
    </Tabs>

    {#if tab === "quests"}
      <div class="space-y-2">
        <div class="flex items-center justify-between px-1">
          <span class="text-xs font-bold text-muted-foreground" aria-live="polite">
            {doneToday}/{dueHabits.length} accomplies aujourd'hui
          </span>
          <Button
            variant="accent"
            size="sm"
            aria-expanded={showForm}
            onclick={() => (showForm = !showForm)}
          >
            <Icon name="plus" size={16} label="" />
            {showForm ? "Annuler" : "Habitude"}
          </Button>
        </div>

        {#if showForm}
          <HabitForm onclose={() => (showForm = false)} />
        {/if}

        {#if dueHabits.length === 0}
          <Card>
            <CardContent class="p-4 text-center text-sm text-muted-foreground">
              Aucune quête pour aujourd'hui. Repos bien mérité. 🌙
            </CardContent>
          </Card>
        {/if}

        {#each dueHabits as habit (habit.id)}
          <HabitCard {habit} onfx={handleFx} />
        {/each}
      </div>
    {:else if tab === "shop"}
      <Shop ontoast={showToast} />
    {:else if tab === "explore"}
      <Expeditions ontoast={showToast} />
    {:else if tab === "stats"}
      <Stats />
    {/if}
  </div>
</div>
