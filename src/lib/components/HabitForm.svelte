<script>
  import { Card, CardContent } from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { DAYS, RECURRENCES } from "$lib/game/data.js";
  import { addHabit } from "$lib/game/state.js";

  let { onclose } = $props();

  let name = $state("");
  let emoji = $state("⭐");
  let rec = $state("daily");
  let days = $state([]);
  let xp = $state(10);
  let coins = $state(5);

  function submit() {
    if (!name.trim()) return;
    addHabit({ name: name.trim(), emoji, rec, days: [...days], xp, coins });
    onclose();
  }
</script>

<Card class="mb-3">
  <CardContent class="space-y-2 p-4">
    <input
      bind:value={name}
      placeholder="Nom de l'habitude…"
      class="w-full rounded-lg border border-border bg-secondary px-3 py-2 text-sm outline-none focus:border-ring"
    />
    <div class="flex items-center gap-2">
      <input
        bind:value={emoji}
        class="w-14 rounded-lg border border-border bg-secondary px-2 py-2 text-center text-sm"
      />
      <input
        type="number"
        min="1"
        max="50"
        bind:value={xp}
        class="w-20 rounded-lg border border-border bg-secondary px-2 py-2 text-sm"
        title="XP"
      />
      <input
        type="number"
        min="1"
        max="50"
        bind:value={coins}
        class="w-20 rounded-lg border border-border bg-secondary px-2 py-2 text-sm"
        title="Pièces"
      />
    </div>
    <div class="flex gap-2">
      {#each RECURRENCES as r}
        <Button
          size="sm"
          variant={rec === r.id ? "default" : "secondary"}
          class="flex-1"
          onclick={() => (rec = r.id)}
        >
          {r.label}
        </Button>
      {/each}
    </div>
    {#if rec === "custom"}
      <div class="flex gap-1">
        {#each DAYS as d, i}
          <button
            class="h-9 w-9 cursor-pointer rounded-lg text-sm {days.includes(i)
              ? 'bg-primary text-primary-foreground font-bold'
              : 'bg-secondary text-muted-foreground'}"
            onclick={() => (days = days.includes(i) ? days.filter((x) => x !== i) : [...days, i])}
          >
            {d}
          </button>
        {/each}
      </div>
    {/if}
    <div class="flex gap-2">
      <Button variant="accent" class="flex-1 font-bold" onclick={submit}>Créer la quête</Button>
      <Button variant="outline" onclick={onclose}>Annuler</Button>
    </div>
  </CardContent>
</Card>
