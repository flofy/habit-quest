<script>
  import { Card, CardContent, CardHeader, CardTitle } from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { game, totalStats, resetGame } from "$lib/game/state.js";

  const stats = $derived(totalStats($game));
</script>

<div class="space-y-2">
  <div class="grid grid-cols-3 gap-2">
    {#each [
      { label: "Niveau", value: $game.level },
      { label: "Complétions", value: stats.completions },
      { label: "Meilleure série", value: stats.bestStreak + " j" },
      { label: "XP", value: $game.xp },
      { label: "Pièces", value: $game.coins },
      { label: "Objets", value: $game.owned.length },
    ] as s (s.label)}
      <Card class="py-3 text-center">
        <CardContent class="p-2">
          <div class="text-xl font-bold text-primary">{s.value}</div>
          <div class="text-xs text-muted-foreground">{s.label}</div>
        </CardContent>
      </Card>
    {/each}
  </div>

  <Card>
    <CardHeader>
      <CardTitle class="text-sm">Journal d'aventure</CardTitle>
    </CardHeader>
    <CardContent class="space-y-1">
      {#if $game.log.length === 0}
        <p class="text-xs text-muted-foreground">Rien pour l'instant. Accomplis une quête !</p>
      {/if}
      {#each $game.log.slice(0, 15) as entry}
        <div class="flex justify-between gap-2 text-xs text-muted-foreground">
          <span class="truncate">{entry.t}</span>
          <span class="shrink-0">{entry.d}</span>
        </div>
      {/each}
    </CardContent>
  </Card>

  <Button variant="destructive" class="w-full" onclick={resetGame}>
    Réinitialiser la partie
  </Button>
</div>
