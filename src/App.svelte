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
    <div class="pointer-events-none fixed inset-0 z-50 overflow-hidden">
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
      class="fixed bottom-20 left-1/2 z-50 -translate-x-1/2 rounded-xl border-2 border-primary/50 bg-card px-4 py-2 text-sm shadow-lg"
    >
      {toast}
    </div>
  {/if}

  <div class="mx-auto max-w-2xl px-3 pb-10 pt-4">
    <!-- Personnage -->
    <Card class="mb-3 bg-gradient-to-b from-indigo-950/60 to-card">
      <CardContent class="flex items-center gap-4 p-4">
        <div class="rounded-xl border-2 border-primary/30 bg-secondary p-2">
          <Avatar palette={avatar.palette} size={10} equipped={$game.equipped} />
        </div>
        <div class="flex-1">
          <div class="mb-1 flex items-center justify-between">
            <span class="font-bold tracking-wide text-primary">
              {avatar.name} · Nv {$game.level}
            </span>
            <span class="text-sm text-primary">🪙 {$game.coins}</span>
          </div>
          <Progress value={$game.xp} max={xpNeeded($game.level)} />
          <div class="mt-1 text-xs text-muted-foreground">
            {$game.xp} / {xpNeeded($game.level)} XP
          </div>
        </div>
      </CardContent>
    </Card>

    <Tabs bind:value={tab} class="mb-3">
      <TabsList>
        <TabsTrigger value="quests">⚔️ Quêtes</TabsTrigger>
        <TabsTrigger value="shop">🛒 Boutique</TabsTrigger>
        <TabsTrigger value="explore">🗺️ Expéditions</TabsTrigger>
        <TabsTrigger value="stats">📊 Stats</TabsTrigger>
      </TabsList>
    </Tabs>

    {#if tab === "quests"}
      <div class="space-y-2">
        <div class="flex items-center justify-between px-1">
          <span class="text-xs text-muted-foreground">
            {doneToday}/{dueHabits.length} accomplies aujourd'hui
          </span>
          <Button variant="accent" size="sm" onclick={() => (showForm = !showForm)}>
            {showForm ? "Annuler" : "+ Habitude"}
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
