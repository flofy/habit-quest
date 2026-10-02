<script>
  import { Card, CardContent, CardHeader, CardTitle } from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { game, totalStats, resetGame } from "$lib/game/state.js";

  const stats = $derived(totalStats($game));
</script>

<div class="space-y-2">
  <div class="grid grid-cols-3 gap-2">
    {#each [
      { label: "Niveau", value: $game.level, chip: "gold" },
      { label: "Complétions", value: stats.completions, chip: "emerald" },
      { label: "Série max", value: stats.bestStreak + " j", chip: "gold" },
      { label: "XP", value: $game.xp, chip: "emerald" },
      { label: "Pièces", value: $game.coins, chip: "gold" },
      { label: "Objets", value: $game.owned.length, chip: "emerald" },
    ] as s (s.label)}
      <Card class="py-4 text-center">
        <CardContent class="p-2">
          <div class="chip {s.chip === 'gold' ? 'chip-gold' : 'chip-emerald'} mx-auto font-display text-base">
            {s.value}
          </div>
          <div class="mt-2 text-xs font-bold text-muted-foreground">{s.label}</div>
        </CardContent>
      </Card>
    {/each}
  </div>

  <Card>
    <CardHeader>
      <CardTitle>Journal d'aventure</CardTitle>
    </CardHeader>
    <CardContent class="space-y-1.5">
      {#if $game.log.length === 0}
        <p class="text-xs text-muted-foreground">Rien pour l'instant. Accomplis une quête !</p>
      {/if}
      {#each $game.log.slice(0, 15) as entry}
        <div class="flex justify-between gap-2 border-b border-border/40 pb-1.5 text-xs text-muted-foreground">
          <span class="truncate">{entry.t}</span>
          <span class="shrink-0 text-border">{entry.d}</span>
        </div>
      {/each}
    </CardContent>
  </Card>

  <Button variant="destructive" class="w-full" onclick={resetGame}>
    Réinitialiser la partie
  </Button>
</div>
