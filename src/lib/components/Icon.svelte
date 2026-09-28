<script>
  // Icônes vectorielles cohérentes (style Lucide, trait 2px, 24x24).
  // Remplacent les emojis dans les éléments structurels d'UI (nav, actions).
  const PATHS = {
    flag: [
      '<path d="M4 22V4c4-2 8 2 12 0v10c-4 2-8-2-12 0"/>',
    ],
    cart: [
      '<circle cx="8" cy="21" r="1"/>',
      '<circle cx="19" cy="21" r="1"/>',
      '<path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>',
    ],
    map: [
      '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2z"/>',
      '<path d="M9 4v14"/>',
      '<path d="M15 6v14"/>',
    ],
    chart: [
      '<path d="M3 3v18h18"/>',
      '<path d="M7 15v-3"/>',
      '<path d="M12 15V8"/>',
      '<path d="M17 15v-6"/>',
    ],
    plus: ['<path d="M5 12h14"/>', '<path d="M12 5v14"/>'],
    x: ['<path d="M18 6 6 18"/>', '<path d="m6 6 12 12"/>'],
    check: ['<path d="M20 6 9 17l-5-5"/>'],
    flame: [
      '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
    ],
    coin: [
      '<circle cx="12" cy="12" r="8"/>',
      '<circle cx="12" cy="12" r="3"/>',
    ],
    star: [
      '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
    ],
  };

  let { name, size = 20, class: cls = "", label = null } = $props();

  // label non nul = icône porteuse de sens (bouton icône seul) -> accessible
  // label nul + icône décorative -> masquée aux lecteurs d'écran
  const decorative = label === null;
</script>

<svg
  xmlns="http://www.w3.org/2000/svg"
  width={size}
  height={size}
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
  class={cls}
  aria-hidden={decorative ? "true" : undefined}
  role={decorative ? undefined : "img"}
  aria-label={decorative ? undefined : label}
>
  {#each PATHS[name] as d}
    {@html d}
  {/each}
</svg>
