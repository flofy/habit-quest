<script>
  import { Card, CardContent } from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import Icon from "$lib/components/Icon.svelte";
  import { DAYS } from "$lib/game/data.js";
  import { completeHabit, undoHabit, deleteHabit, streakOf, todayISO } from "$lib/game/state.js";

  let { habit, onfx } = $props();

  const today = todayISO();
  const done = $derived(habit.history.includes(today));
  const streak = $derived(streakOf(habit));

  const recLabel = $derived(
    habit.rec === "daily"
      ? "Quotidienne"
      : habit.rec === "weekly"
        ? "Hebdomadaire"
        : (habit.days || []).map((d) => DAYS[d]).join(" ")
  );

  function onComplete(e) {
    const levelUps = completeHabit(habit);
    onfx?.({
      el: e.currentTarget,
      texts: [
        { text: "+" + habit.xp + " XP", color: "#4ade80" },
        { text: "+" + habit.coins + " 🪙", color: "#f4d03f" },
      ],
      levelUps,
    });
  }
</script>

<Card class="mb-2 transition-opacity duration-200 {done ? 'opacity-60' : ''}">
  <CardContent class="flex items-center gap-3 p-4">
    <span class="text-2xl" aria-hidden="true">{habit.emoji}</span>
    <div class="min-w-0 flex-1">
      <div class="truncate text-sm font-bold {done ? 'line-through text-muted-foreground' : ''}">
        {habit.name}
      </div>
      <div class="flex items-center gap-1 text-xs text-muted-foreground">
        <span>{recLabel}</span>
        {#if streak > 0}
          <span class="inline-flex items-center gap-0.5" title="{streak} jours de série">
            <Icon name="flame" size={12} class="text-primary" label="" />
            <span>{streak} j</span>
          </span>
        {/if}
      </div>
    </div>
    <div class="mr-1 shrink-0 text-right text-xs">
      <div class="text-accent">+{habit.xp} XP</div>
      <div class="text-primary">+{habit.coins} 🪙</div>
    </div>
    {#if done}
      <Button
        variant="outline"
        size="icon"
        onclick={() => undoHabit(habit)}
        aria-label="Annuler « {habit.name} » pour aujourd'hui"
        title="Annuler"
      >
        <Icon name="check" label="" />
      </Button>
    {:else}
      <Button
        variant="accent"
        size="sm"
        onclick={onComplete}
        aria-label="Marquer « {habit.name} » comme accomplie : +{habit.xp} XP, +{habit.coins} pièces"
      >
        Terminer
      </Button>
    {/if}
    <Button
      variant="ghost"
      size="icon"
      class="text-muted-foreground hover:text-destructive"
      onclick={() => deleteHabit(habit.id)}
      aria-label="Supprimer l'habitude « {habit.name} »"
      title="Supprimer"
    >
      <Icon name="x" label="" />
    </Button>
  </CardContent>
</Card>
