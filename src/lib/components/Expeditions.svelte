<script>
  import { Card, CardContent } from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { REGIONS } from "$lib/game/data.js";
  import { startExpedition, finishExpedition, game } from "$lib/game/state.js";

  let { ontoast } = $props();

  let active = $state(null); // { region, startedAt }
  let tick = $state(Date.now());

  $effect(() => {
    if (!active) return;
    const iv = setInterval(() => {
      tick = Date.now();
      if (tick >= active.startedAt + active.region.duration) {
        const rewards = finishExpedition(active.region);
        ontoast?.(active.region.emoji + " Trésor trouvé : +" + rewards.coins + " 🪙 +" + rewards.xp + " XP");
        active = null;
      }
    }, 250);
    return () => clearInterval(iv);
  });

  function onStart(region) {
    if (startExpedition(region)) {
      active = { region, startedAt: Date.now() };
    }
  }

  const progress = $derived(
    active ? Math.min(100, ((tick - active.startedAt) / active.region.duration) * 100) : 0
  );
</script>

<div class="space-y-2">
  {#if active}
    <Card class="py-8">
      <CardContent class="text-center">
        <div class="mb-2 animate-bounce text-4xl">{active.region.emoji}</div>
        <div class="text-sm text-muted-foreground">Exploration en cours…</div>
        <div class="mx-auto mt-3 h-2 w-full max-w-xs overflow-hidden rounded-full bg-muted">
          <div class="h-full bg-primary transition-all" style="width: {progress}%"></div>
        </div>
      </CardContent>
    </Card>
  {:else}
    {#each REGIONS as region (region.id)}
      <Card>
        <CardContent class="flex items-center gap-3 p-4">
          <span class="text-3xl">{region.emoji}</span>
          <div class="flex-1">
            <div class="text-sm font-bold">{region.name}</div>
            <div class="text-xs text-muted-foreground">
              Loot : {region.rewards.coins[0]}-{region.rewards.coins[1]} 🪙 ·
              {region.rewards.xp[0]}-{region.rewards.xp[1]} XP
            </div>
          </div>
          <Button
            variant="secondary"
            size="sm"
            disabled={$game.coins < region.cost}
            onclick={() => onStart(region)}
          >
            🪙 {region.cost}
          </Button>
        </CardContent>
      </Card>
    {/each}
  {/if}
</div>
