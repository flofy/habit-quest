<script>
  // Icônes d'équipement vectorielles (remplacent les emojis).
  // Dessinées sur une grille 32x32, style cohérent avec le héros : métal clair,
  // bois, liserés dorés.
  // Les couleurs métal / liserés / gemmes dépendent de la rareté de l'objet.
  import { paletteOf } from "$lib/game/data.js";

  let { id, size = 32, class: cls = "" } = $props();

  const pal = $derived(paletteOf(id));
  const [, m1, m2] = $derived(pal.metal);
</script>

<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 32 32"
  width={size}
  height={size}
  class={cls}
  aria-hidden="true"
  shape-rendering="geometricPrecision"
  style={pal.glow ? `filter: drop-shadow(0 0 3px ${pal.glow}aa)` : undefined}
>
  {#if id === "sword"}
    <path d="M24.5 3 L28 3.5 L27.5 7 L14 20.5 L11.5 18 Z" fill={m1} />
    <path d="M25 4.2 L26.8 4.5 L26.5 6 L13.5 19 L12.6 18.1 Z" fill="#fff" opacity="0.6" />
    <rect x="7.5" y="17.5" width="10" height="3" rx="1.5" transform="rotate(45 12.5 19)" fill={pal.trim} />
    <rect x="6.5" y="21" width="3" height="7" rx="1.5" transform="rotate(45 8 24.5)" fill="#6b4a1e" />
    <circle cx="5.5" cy="27.5" r="2" fill={pal.trim} />
  {:else if id === "shield"}
    <path d="M16 3 L27 6.5 V15 C27 22 21.5 26.5 16 29 C10.5 26.5 5 22 5 15 V6.5 Z" fill="#8a5a2b" stroke={m1} stroke-width="2" stroke-linejoin="round" />
    <path d="M16 6 L24 8.6 V15 C24 20 20.5 23.5 16 25.8 Z" fill="#a9773f" opacity="0.6" />
    <path d="M16 6 V25.8" stroke={m1} stroke-width="1.2" opacity="0.7" />
    <circle cx="16" cy="14.5" r="3.4" fill={pal.trim} stroke="#8a5f16" stroke-width="1" />
  {:else if id === "helmet"}
    <path d="M5 21 C5 11 9.5 5 16 5 C22.5 5 27 11 27 21 V24 H21 V19 H11 V24 H5 Z" fill={m1} stroke={m2} stroke-width="1.2" stroke-linejoin="round" />
    <path d="M8 16 C9 10 12 7 16 7 C14 9 12.5 12 12.5 16 Z" fill="#fff" opacity="0.5" />
    <rect x="14.5" y="8" width="3" height="11" rx="1.2" fill={m2} />
    <path d="M16 2.5 C18 4 18 5.5 16 7 C14 5.5 14 4 16 2.5 Z" fill="#ee8174" />
  {:else if id === "amulet"}
    <path d="M7 4 C8 14 12 18 16 18 C20 18 24 14 25 4" stroke={pal.trim} stroke-width="1.8" fill="none" stroke-linecap="round" />
    <circle cx="16" cy="22" r="7" fill={pal.trim} stroke="#8a5f16" stroke-width="1.2" />
    <path d="M16 15.8 L21 22 L16 28.2 L11 22 Z" fill={pal.gem} stroke="#1b291d" stroke-width="1" stroke-linejoin="round" />
    <path d="M16 17.5 L18.6 21 L16 21.8 L13.4 21 Z" fill="#cdf5d4" opacity="0.8" />
  {:else if id === "armor"}
    <path d="M9 4 C11 6 13.5 7 16 7 C18.5 7 21 6 23 4 L29 8 L26 14 L24 13 V28 H8 V13 L6 14 L3 8 Z" fill={m1} stroke={m2} stroke-width="1.2" stroke-linejoin="round" />
    <path d="M10 10 H14 V26 H10 Z" fill="#fff" opacity="0.35" />
    <path d="M16 12 L19.5 17 L16 22 L12.5 17 Z" fill={pal.trim} stroke="#8a5f16" stroke-width="1" stroke-linejoin="round" />
    <path d="M12 25 H20" stroke={m2} stroke-width="1.4" stroke-linecap="round" />
  {:else if id === "boots"}
    <path d="M9 4 H17 V16 C17 18 20 19 24 21 C27 22.5 28 24 28 26 V28 H8 C7 28 6.5 27.5 6.5 26.5 L8 8 Z" fill="#8a5a2b" stroke="#4a3524" stroke-width="1.2" stroke-linejoin="round" />
    <rect x="8" y="4" width="9" height="4" rx="1" fill={pal.trim} />
    <path d="M6.5 25 H28" stroke="#2e2115" stroke-width="2.4" />
    <path d="M10.5 10 V15" stroke="#fff" stroke-width="1.2" stroke-linecap="round" opacity="0.35" />
  {/if}
</svg>
