<script>
  import { Card, CardContent } from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import Avatar from "$lib/components/Avatar.svelte";
  import ItemIcon from "$lib/components/ItemIcon.svelte";
  import Icon from "$lib/components/Icon.svelte";
  import { AVATARS, SHOP_ITEMS, SLOTS, RARITIES } from "$lib/game/data.js";
  import { buyItem, toggleEquip, cycleAvatar, bonusOf, game } from "$lib/game/state.js";

  let { ontoast } = $props();

  const FILTERS = [
    { id: "all", label: "Tout" },
    { id: "owned", label: "Possédés" },
    { id: "todo", label: "À acheter" },
  ];
  let filter = $state("all");
  let slotFilter = $state(null); // id d'emplacement, ou null = tous

  const leftSlots = SLOTS.slice(0, 3);
  const rightSlots = SLOTS.slice(3);
  const slotIndex = (id) => SLOTS.findIndex((s) => s.id === id);

  const avatar = $derived(AVATARS[$game.avatar]);
  const visible = $derived(
    SHOP_ITEMS.filter((item) => {
      const owned = $game.owned.includes(item.id);
      if (filter === "owned" && !owned) return false;
      if (filter === "todo" && owned) return false;
      return !slotFilter || item.slot === slotFilter;
    }).sort((a, b) => slotIndex(a.slot) - slotIndex(b.slot) || a.cost - b.cost)
  );

  // Bonus actifs (équipement porté) et mise en forme « +10 % XP »
  const active = $derived(bonusOf($game));
  const pct = (v) => "+" + Math.round(v * 100) + " %";
  const bonusChips = (bonus = {}) => [
    ...(bonus.xp ? [{ text: pct(bonus.xp) + " XP", cls: "chip-emerald" }] : []),
    ...(bonus.coins ? [{ text: pct(bonus.coins) + " pièces", cls: "chip-gold" }] : []),
  ];

  // Objet équipé dans un emplacement (ou undefined)
  const equippedIn = (slotId) =>
    SHOP_ITEMS.find((i) => i.slot === slotId && $game.equipped.includes(i.id));

  const pickSlot = (id) => (slotFilter = slotFilter === id ? null : id);

  function onBuy(item) {
    if (buyItem(item)) ontoast?.(item.emoji + " " + item.name + " acheté !");
  }
</script>

<div class="space-y-3">
  <!-- Mannequin : le héros entouré de ses 6 emplacements (un tap filtre la liste) -->
  <Card>
    <CardContent class="p-4">
      <div class="mb-3 flex items-center justify-between">
        <h2 class="font-display text-sm font-bold">Équipement</h2>
        <span class="chip chip-emerald">{$game.owned.length}/{SHOP_ITEMS.length} possédés</span>
      </div>

      <div class="grid grid-cols-[auto_1fr_auto] items-center gap-3">
        {#each [leftSlots, rightSlots] as column, c}
          <div class="flex flex-col gap-2" style="grid-column: {c === 0 ? 1 : 3}; grid-row: 1;">
            {#each column as slot (slot.id)}
              {@const item = equippedIn(slot.id)}
              <button
                type="button"
                class="panel-inset relative flex h-[60px] w-[60px] cursor-pointer flex-col items-center justify-center gap-0.5 transition-transform active:scale-95 {slotFilter === slot.id ? 'ring-2 ring-primary' : ''}"
                style={item ? `border-color: ${RARITIES[item.rarity].color}; box-shadow: inset 0 2px 6px rgba(0,0,0,.45), 0 0 10px ${RARITIES[item.rarity].color}55;` : ""}
                aria-pressed={slotFilter === slot.id}
                aria-label={item ? `${slot.label} : ${item.name}. Voir les objets de cet emplacement` : `${slot.label} : vide. Voir les objets de cet emplacement`}
                onclick={() => pickSlot(slot.id)}
              >
                {#if item}
                  <ItemIcon id={item.id} size={32} />
                {:else}
                  <span class="h-6 w-6 rounded-full border-2 border-dashed border-border/70"></span>
                {/if}
                <span class="text-[9px] font-bold uppercase tracking-wide text-muted-foreground">{slot.label}</span>
              </button>
            {/each}
          </div>
        {/each}

        <div class="flex items-end justify-center" style="grid-column: 2; grid-row: 1;">
          <Avatar {avatar} size={128} equipped={$game.equipped} />
        </div>
      </div>

      <div class="mt-3 flex flex-wrap items-center justify-center gap-2" aria-label="Bonus actifs">
        {#each bonusChips(active) as b (b.text)}
          <span class="chip {b.cls}">{b.text}</span>
        {:else}
          <span class="text-xs text-muted-foreground">Équipe des objets pour gagner des bonus d'XP et de pièces.</span>
        {/each}
      </div>
    </CardContent>
  </Card>

  <!-- Filtres : possession + emplacement -->
  <div class="flex gap-2" role="group" aria-label="Filtrer par possession">
    {#each FILTERS as f (f.id)}
      <Button
        variant={filter === f.id ? "default" : "secondary"}
        size="sm"
        class="flex-1"
        aria-pressed={filter === f.id}
        onclick={() => (filter = f.id)}
      >
        {f.label}
      </Button>
    {/each}
  </div>
  <div class="-mx-1 flex gap-2 overflow-x-auto px-1 pb-1" role="group" aria-label="Filtrer par emplacement">
    <Button variant={slotFilter === null ? "default" : "secondary"} size="sm" class="shrink-0" aria-pressed={slotFilter === null} onclick={() => (slotFilter = null)}>
      Tous
    </Button>
    {#each SLOTS as slot (slot.id)}
      <Button variant={slotFilter === slot.id ? "default" : "secondary"} size="sm" class="shrink-0" aria-pressed={slotFilter === slot.id} onclick={() => pickSlot(slot.id)}>
        {slot.label}
      </Button>
    {/each}
  </div>

  <!-- Grille d'objets -->
  <div class="grid grid-cols-2 gap-3">
    {#each visible as item (item.id)}
      {@const owned = $game.owned.includes(item.id)}
      {@const equipped = $game.equipped.includes(item.id)}
      {@const rarity = RARITIES[item.rarity]}
      {@const missing = item.cost - $game.coins}
      {@const swap = !equipped && equippedIn(item.slot)}
      <Card class={equipped ? "ring-2 ring-primary/80" : ""}>
        <CardContent
          class="flex h-full flex-col gap-2 rounded-[inherit] p-3"
          style="background: linear-gradient(180deg, {rarity.color}1f, transparent 55%);"
        >
          <div class="flex items-center justify-between gap-1">
            <span class="text-[10px] font-extrabold uppercase tracking-wider" style="color: {rarity.color}">
              {rarity.label}
            </span>
            {#if equipped}
              <span class="flex items-center gap-0.5 text-[10px] font-bold text-accent">
                <Icon name="check" size={12} /> Équipé
              </span>
            {/if}
          </div>

          <div
            class="panel-inset mx-auto flex h-20 w-20 items-center justify-center"
            style="border-color: {rarity.color}99; background: radial-gradient(circle at 50% 42%, {rarity.color}38, transparent 72%); box-shadow: inset 0 2px 6px rgba(0,0,0,.45), 0 0 14px {rarity.color}33;"
          >
            <ItemIcon id={item.id} size={60} class={owned ? "" : "opacity-85"} />
          </div>

          <div class="flex-1 text-center">
            <div class="text-sm font-bold leading-tight">{item.name}</div>
            <div class="text-[11px] text-muted-foreground">{item.type}</div>
            <p class="mt-1 text-[11px] leading-snug text-muted-foreground">{item.desc}</p>
            <div class="mt-1.5 flex flex-wrap justify-center gap-1">
              {#each bonusChips(item.bonus) as b (b.text)}
                <span class="chip {b.cls}">{b.text}</span>
              {/each}
            </div>
          </div>

          {#if owned}
            <Button
              variant={equipped ? "default" : "secondary"}
              size="sm"
              class="w-full"
              aria-pressed={equipped}
              onclick={() => toggleEquip(item.id)}
            >
              {equipped ? "Retirer" : swap ? "Remplacer" : "Équiper"}
            </Button>
          {:else}
            <Button
              variant="outline"
              size="sm"
              class="w-full"
              disabled={missing > 0}
              aria-label="Acheter {item.name} pour {item.cost} pièces"
              onclick={() => onBuy(item)}
            >
              <Icon name="coin" size={16} /> {item.cost}
            </Button>
            {#if missing > 0}
              <div class="-mt-1 text-center text-[11px] text-muted-foreground">Il manque {missing} pièces</div>
            {/if}
          {/if}
        </CardContent>
      </Card>
    {:else}
      <p class="col-span-2 px-1 py-6 text-center text-sm text-muted-foreground">
        {filter === "owned" ? "Rien dans ton sac pour cette sélection." : "Aucun objet ne correspond à ce filtre."}
      </p>
    {/each}
  </div>

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
