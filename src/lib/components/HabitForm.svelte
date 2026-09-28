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
  <CardContent class="space-y-3 p-4">
    <div class="space-y-1">
      <label for="habit-name" class="text-xs font-medium text-muted-foreground">Nom</label>
      <input
        id="habit-name"
        bind:value={name}
        placeholder="Ex : Marcher 30 min"
        class="h-11 w-full rounded-lg border border-input bg-secondary px-3 text-sm outline-none focus:border-ring"
      />
    </div>
    <div class="flex items-end gap-2">
      <div class="space-y-1">
        <label for="habit-emoji" class="text-xs font-medium text-muted-foreground">Icône</label>
        <input
          id="habit-emoji"
          bind:value={emoji}
          class="h-11 w-14 rounded-lg border border-input bg-secondary px-2 text-center text-sm"
        />
      </div>
      <div class="space-y-1">
        <label for="habit-xp" class="text-xs font-medium text-muted-foreground">XP</label>
        <input
          id="habit-xp"
          type="number"
          min="1"
          max="50"
          bind:value={xp}
          class="h-11 w-20 rounded-lg border border-input bg-secondary px-2 text-sm"
        />
      </div>
      <div class="space-y-1">
        <label for="habit-coins" class="text-xs font-medium text-muted-foreground">Pièces</label>
        <input
          id="habit-coins"
          type="number"
          min="1"
          max="50"
          bind:value={coins}
          class="h-11 w-20 rounded-lg border border-input bg-secondary px-2 text-sm"
        />
      </div>
    </div>
    <div class="space-y-1">
      <span class="text-xs font-medium text-muted-foreground">Récurrence</span>
      <div class="flex gap-2">
        {#each RECURRENCES as r}
          <Button
            size="sm"
            variant={rec === r.id ? "default" : "secondary"}
            class="flex-1"
            aria-pressed={rec === r.id}
            onclick={() => (rec = r.id)}
          >
            {r.label}
          </Button>
        {/each}
      </div>
    </div>
    {#if rec === "custom"}
      <div class="space-y-1">
        <span class="text-xs font-medium text-muted-foreground">Jours</span>
        <div class="flex gap-1">
          {#each DAYS as d, i}
            <button
              type="button"
              class="h-11 w-11 cursor-pointer rounded-lg text-sm transition-colors duration-100 {days.includes(i)
                ? 'bg-primary font-bold text-primary-foreground'
                : 'bg-secondary text-muted-foreground hover:bg-secondary/70'}"
              aria-pressed={days.includes(i)}
              aria-label="Le {['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'][i]}"
              onclick={() =>
                (days = days.includes(i) ? days.filter((x) => x !== i) : [...days, i])}
            >
              {d}
            </button>
          {/each}
        </div>
      </div>
    {/if}
    <div class="flex gap-2 pt-1">
      <Button variant="accent" class="flex-1 font-bold" onclick={submit}>
        Créer la quête
      </Button>
      <Button variant="outline" onclick={onclose}>Annuler</Button>
    </div>
  </CardContent>
</Card>
