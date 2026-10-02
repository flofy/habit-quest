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

  const avatar = $derived(AVATARS[$game.avatar]);
  const dueHabits = $derived($game.habits.filter(isDue));
  const doneToday = $derived($game.habits.filter((h) => h.history.includes(todayISO())).length);

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
      class="panel fixed bottom-8 left-1/2 z-50 -translate-x-1/2 px-4 py-2 text-sm font-bold text-primary"
      role="status"
      aria-live="polite"
    >
      {toast}
    </div>
  {/if}

  <div class="mx-auto max-w-2xl px-4 pb-12 pt-6">
    <!-- Héros : scène de crépuscule avec personnage -->
    <Card class="mb-4 overflow-hidden">
      <div class="relative h-40 w-full overflow-hidden rounded-t-[15px]">
        <svg
          viewBox="0 0 640 200"
          preserveAspectRatio="xMidYMax slice"
          class="absolute inset-0 h-full w-full"
          aria-hidden="true"
        >
          <defs>
            <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#33506e" />
              <stop offset="0.55" stop-color="#274258" />
              <stop offset="1" stop-color="#1c3145" />
            </linearGradient>
            <radialGradient id="moonglow">
              <stop offset="0" stop-color="#f5e9c9" stop-opacity="0.5" />
              <stop offset="1" stop-color="#f5e9c9" stop-opacity="0" />
            </radialGradient>
          </defs>
          <rect width="640" height="200" fill="url(#sky)" />
          <circle cx="500" cy="52" r="42" fill="url(#moonglow)" />
          <circle cx="500" cy="52" r="15" fill="#f5e9c9" />
          <circle cx="120" cy="34" r="1.4" fill="#dfe8f2" opacity="0.9" />
          <circle cx="200" cy="58" r="1.1" fill="#dfe8f2" opacity="0.7" />
          <circle cx="320" cy="30" r="1.2" fill="#dfe8f2" opacity="0.8" />
          <circle cx="430" cy="76" r="1" fill="#dfe8f2" opacity="0.6" />
          <circle cx="70" cy="70" r="1" fill="#dfe8f2" opacity="0.6" />
          <path d="M0 130 L80 78 L150 118 L230 60 L330 128 L410 92 L500 130 L570 100 L640 132 L640 200 L0 200 Z" fill="#2a3d52" />
          <path d="M0 160 L90 118 L180 152 L290 108 L400 156 L500 126 L640 162 L640 200 L0 200 Z" fill="#22324a" />
          <path d="M0 176 L60 156 L120 174 L200 150 L280 172 L360 152 L440 174 L520 154 L640 176 L640 200 L0 200 Z" fill="#17251c" />
          <rect y="186" width="640" height="14" fill="#24402a" />
          <ellipse cx="320" cy="192" rx="120" ry="12" fill="#2c4f33" />
        </svg>
        <div class="absolute bottom-2 left-1/2 -translate-x-1/2">
          <Avatar {avatar} size={84} equipped={$game.equipped} />
        </div>
      </div>
      <CardContent class="space-y-3 p-4">
        <div class="flex flex-wrap items-center justify-between gap-2">
          <div class="nameplate px-3 py-1 font-display text-sm font-bold">
            {avatar.name} · Niveau {$game.level}
          </div>
          <span class="chip chip-gold" aria-label="Pièces d'or : {$game.coins}">
            🪙 {$game.coins}
          </span>
        </div>
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
            <span>{t.label}</span>
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
