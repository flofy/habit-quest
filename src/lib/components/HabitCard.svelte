<script>
  import { Card, CardContent } from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { DAYS } from "$lib/game/data.js";
  import { completeHabit, undoHabit, deleteHabit, streakOf, todayISO } from "$lib/game/state.js";

  let { habit, onfx } = $props();

  const today = todayISO();
  const done = $derived(habit.history.includes(today));
  const streak = $derived(streakOf(habit));

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

<Card class="mb-2 transition-opacity {done ? 'opacity-60' : ''}">
  <CardContent class="flex items-center gap-3 p-4">
    <span class="text-2xl">{habit.emoji}</span>
    <div class="min-w-0 flex-1">
      <div class="truncate text-sm font-bold {done ? 'line-through text-muted-foreground' : ''}">
        {habit.name}
      </div>
      <div class="text-xs text-muted-foreground">
        {habit.rec === "daily"
          ? "Quotidienne"
          : habit.rec === "weekly"
            ? "Hebdomadaire"
            : (habit.days || []).map((d) => DAYS[d]).join(" ")}
        {#if streak > 0}<span> · 🔥 {streak} j</span>{/if}
      </div>
    </div>
    <div class="mr-1 text-right text-xs">
      <div class="text-accent">+{habit.xp} XP</div>
      <div class="text-primary">+{habit.coins} 🪙</div>
    </div>
    {#if done}
      <Button variant="outline" size="sm" onclick={() => undoHabit(habit)} title="Annuler">✓</Button>
    {:else}
      <Button variant="accent" size="sm" onclick={onComplete}>Terminer</Button>
    {/if}
    <button
      class="cursor-pointer px-1 text-sm text-muted-foreground hover:text-destructive"
      onclick={() => deleteHabit(habit.id)}
      title="Supprimer"
    >
      ✕
    </button>
  </CardContent>
</Card>
