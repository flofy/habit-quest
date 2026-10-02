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
    <Card class="py-10">
      <CardContent class="text-center">
        <div class="mb-3 animate-bounce text-5xl" aria-hidden="true">{active.region.emoji}</div>
        <div class="text-sm font-bold text-secondary-foreground" role="status">
          Exploration de {active.region.name} en cours…
        </div>
        <div
          class="panel-inset mx-auto mt-4 h-2.5 w-full max-w-xs overflow-hidden rounded-full p-[2px]"
          role="progressbar"
          aria-label="Progression de l'expédition"
          aria-valuenow={Math.round(progress)}
          aria-valuemin="0"
          aria-valuemax="100"
        >
          <div
            class="h-full rounded-full bg-gradient-to-b from-[#f4cd6f] to-[#dda031] transition-all"
            style="width: {progress}%; box-shadow: inset 0 1px 0 rgba(255,255,255,.4);"
          ></div>
        </div>
      </CardContent>
    </Card>
  {:else}
    {#each REGIONS as region (region.id)}
      <Card>
        <CardContent class="flex items-center gap-3 p-3">
          <div class="panel-inset flex h-14 w-14 shrink-0 items-center justify-center rounded-xl text-3xl" aria-hidden="true">
            {region.emoji}
          </div>
          <div class="flex-1">
            <div class="font-display text-sm font-bold">{region.name}</div>
            <div class="mt-1 flex flex-wrap gap-1">
              <span class="chip chip-gold">{region.rewards.coins[0]}-{region.rewards.coins[1]} 🪙</span>
              <span class="chip chip-emerald">{region.rewards.xp[0]}-{region.rewards.xp[1]} XP</span>
            </div>
          </div>
          <Button
            variant="secondary"
            size="sm"
            disabled={$game.coins < region.cost}
            aria-label="Lancer une expédition vers {region.name} pour {region.cost} pièces"
            onclick={() => onStart(region)}
          >
            🪙 {region.cost}
          </Button>
        </CardContent>
      </Card>
    {/each}
  {/if}
</div>
