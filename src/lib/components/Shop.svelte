<script>
  import { Card, CardContent } from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { AVATARS, SHOP_ITEMS } from "$lib/game/data.js";
  import { buyItem, toggleEquip, cycleAvatar, game } from "$lib/game/state.js";

  let { ontoast } = $props();

  function onBuy(item) {
    if (buyItem(item)) ontoast?.(item.emoji + " " + item.name + " acheté !");
  }
</script>

<div class="space-y-2">
  <p class="px-1 text-xs text-muted-foreground">
    Équipement possédé : {$game.owned.length}/{SHOP_ITEMS.length}. Touchez un objet possédé pour
    l'équiper.
  </p>
  {#each SHOP_ITEMS as item (item.id)}
    {@const owned = $game.owned.includes(item.id)}
    {@const equipped = $game.equipped.includes(item.id)}
    <Card>
      <CardContent class="flex items-center gap-3 p-3">
        <div class="panel-inset flex h-12 w-12 shrink-0 items-center justify-center rounded-xl text-2xl" aria-hidden="true">
          {item.emoji}
        </div>
        <div class="flex-1">
          <div class="text-sm font-bold">{item.name}</div>
          <div class="text-xs text-muted-foreground">{item.type}</div>
        </div>
        {#if owned}
          <Button
            variant={equipped ? "default" : "secondary"}
            size="sm"
            aria-pressed={equipped}
            onclick={() => toggleEquip(item.id)}
          >
            {equipped ? "Équipé" : "Équiper"}
          </Button>
        {:else}
          <Button
            variant="outline"
            size="sm"
            disabled={$game.coins < item.cost}
            aria-label="Acheter {item.name} pour {item.cost} pièces"
            onclick={() => onBuy(item)}
          >
            🪙 {item.cost}
          </Button>
        {/if}
      </CardContent>
    </Card>
  {/each}
  <Card>
    <CardContent class="flex items-center gap-3 p-3">
      <div class="panel-inset flex h-12 w-12 shrink-0 items-center justify-center rounded-xl text-2xl" aria-hidden="true">
        🎭
      </div>
      <div class="flex-1 text-sm font-bold">Changer de personnage</div>
      <Button variant="secondary" size="sm" onclick={cycleAvatar}>
        {AVATARS[$game.avatar].name}
      </Button>
    </CardContent>
  </Card>
</div>
