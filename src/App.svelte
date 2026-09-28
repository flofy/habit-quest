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
  <!-- Effets de récompense : purement décoratifs -->
  {#if fx.length > 0}
    <div class="pointer-events-none fixed inset-0 z-50 overflow-hidden" aria-hidden="true">
      {#each fx as f (f.id)}
        <span
          class="absolute text-lg font-bold"
          style="left: {f.x}px; top: {f.y}px; color: {f.color}; animation: float-up 1.2s ease-out forwards;"
        >
          {f.text}
        </span>
      {/each}
    </div>
  {/if}

  {#if toast}
    <div
      class="fixed bottom-8 left-1/2 z-50 -translate-x-1/2 rounded-xl border-2 border-primary/50 bg-card px-4 py-2 text-sm shadow-lg"
      role="status"
      aria-live="polite"
    >
      {toast}
    </div>
  {/if}

  <div class="mx-auto max-w-2xl px-4 pb-12 pt-6">
    <!-- Personnage -->
    <Card class="mb-4 bg-gradient-to-b from-indigo-950/60 to-card">
      <CardContent class="flex items-center gap-4 p-4">
        <div class="rounded-xl border-2 border-primary/30 bg-secondary p-2">
          <Avatar palette={avatar.palette} size={10} equipped={$game.equipped} />
        </div>
        <div class="flex-1">
          <div class="mb-1 flex items-center justify-between gap-2">
            <span class="truncate font-bold tracking-wide text-primary">
              {avatar.name} · Nv {$game.level}
            </span>
            <span class="shrink-0 text-sm font-bold text-primary" aria-label="Pièces d'or : {$game.coins}">
              🪙 {$game.coins}
            </span>
          </div>
          <Progress
            value={$game.xp}
            max={xpNeeded($game.level)}
            label="XP : {$game.xp} sur {xpNeeded($game.level)}"
          />
          <div class="mt-1 text-xs text-muted-foreground">
            {$game.xp} / {xpNeeded($game.level)} XP
          </div>
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
          <span class="text-xs text-muted-foreground" aria-live="polite">
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
