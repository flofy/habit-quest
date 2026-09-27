<script>
  import { AVATAR_SPRITE } from "$lib/game/data.js";
  let { palette, size = 10, equipped = [] } = $props();
</script>

<div class="relative" style="width: {size * 8}px; height: {size * 8}px;">
  <svg width={size * 8} height={size * 8} viewBox="0 0 8 8" shape-rendering="crispEdges">
    {#each AVATAR_SPRITE as row, y}
      {#each row as c, x}
        {#if c > 0 && palette[c - 1]}
          <rect x={x} y={y} width="1" height="1" fill={palette[c - 1]} />
        {/if}
      {/each}
    {/each}
  </svg>
  {#if equipped.includes("sword")}<span class="absolute -right-2 top-6 text-xs">⚔️</span>{/if}
  {#if equipped.includes("shield")}<span class="absolute -left-2 top-6 text-xs">🛡️</span>{/if}
  {#if equipped.includes("helmet")}<span class="absolute -top-2 left-1/2 -translate-x-1/2 text-xs">⛑️</span>{/if}
  {#if equipped.includes("amulet")}<span class="absolute top-8 left-1/2 -translate-x-1/2 text-[10px]">📿</span>{/if}
  {#if equipped.includes("boots")}<span class="absolute -bottom-1 left-3 text-[10px]">🥾</span>{/if}
  {#if equipped.includes("armor")}<span class="absolute top-9 left-1/2 -translate-x-1/2 text-[10px]">✨</span>{/if}
</div>
