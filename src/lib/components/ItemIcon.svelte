<script>
  // Visuel d'un objet d'équipement : sprite PNG si présent
  // (src/lib/assets/items/<id>.png), sinon icône vectorielle pour les objets
  // d'origine, sinon l'emoji de l'objet.
  import EquipmentIcon from "$lib/components/EquipmentIcon.svelte";
  import { itemById, paletteOf } from "$lib/game/data.js";
  import { itemSprite } from "$lib/game/sprites.js";

  let { id, size = 32, class: cls = "" } = $props();

  const VECTOR_IDS = ["sword", "shield", "helmet", "amulet", "armor", "boots"];
  const src = $derived(itemSprite(id));
  const glow = $derived(paletteOf(id).glow);
</script>

{#if src}
  <img
    {src}
    alt=""
    width={size}
    height={size}
    draggable="false"
    class="select-none object-contain {cls}"
    style="width: {size}px; height: {size}px;{glow ? ` filter: drop-shadow(0 0 4px ${glow}88);` : ''}"
  />
{:else if VECTOR_IDS.includes(id)}
  <EquipmentIcon {id} {size} class={cls} />
{:else}
  <span class="inline-flex items-center justify-center {cls}" style="width: {size}px; height: {size}px; font-size: {size * 0.8}px" aria-hidden="true">
    {itemById(id)?.emoji ?? "❔"}
  </span>
{/if}
