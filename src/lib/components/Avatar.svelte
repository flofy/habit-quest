<script>
  // Personnage vectoriel lisse (fini le sprite 8x8) — style fantasy réaliste.
  let { avatar, size = 96, equipped = [] } = $props();
  const gid = $derived("robe-" + avatar.weapon);
</script>

<div class="relative" style="width: {size}px; height: {size}px;">
  <svg viewBox="0 0 64 64" width={size} height={size} shape-rendering="geometricPrecision">
    <defs>
      <linearGradient id={gid} x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color={avatar.robe[0]} />
        <stop offset="1" stop-color={avatar.robe[1]} />
      </linearGradient>
    </defs>

    <!-- ombre au sol -->
    <ellipse cx="32" cy="61" rx="17" ry="3.5" fill="rgba(0,0,0,.35)" />

    <!-- arme de classe -->
    {#if avatar.weapon === "staff"}
      <rect x="50" y="16" width="3" height="42" rx="1.5" fill="#7a5a34" />
      <circle cx="51.5" cy="13" r="6" fill="#9be8ff" opacity="0.35" />
      <circle cx="51.5" cy="13" r="4" fill="#bfefff" />
    {/if}
    {#if avatar.weapon === "sword"}
      <rect x="10.5" y="26" width="3" height="22" rx="1" fill="#cfd6dd" />
      <rect x="7" y="48" width="10" height="3" rx="1.5" fill="#8a5f16" />
      <rect x="10.5" y="50" width="3" height="5" rx="1.5" fill="#7a4a22" />
    {/if}
    {#if avatar.weapon === "bow"}
      <path d="M13 28 Q5 42 13 56" stroke="#8b5a2b" stroke-width="2.5" fill="none" stroke-linecap="round" />
      <line x1="13" y1="28" x2="13" y2="56" stroke="#d8d0c0" stroke-width="1" />
    {/if}

    <!-- bottes -->
    <rect x="25" y="50" width="6" height="9" rx="2" fill="#4a3524" />
    <rect x="33" y="50" width="6" height="9" rx="2" fill="#4a3524" />

    <!-- robe -->
    <path d="M20 52 C18 38 22 30 32 28 C42 30 46 38 44 52 Z" fill="url(#{gid})" />

    <!-- bras -->
    <rect x="16" y="30" width="6" height="16" rx="3" fill={avatar.robe[1]} />
    <rect x="42" y="30" width="6" height="16" rx="3" fill={avatar.robe[1]} />

    <!-- ceinture -->
    <rect x="21" y="42" width="22" height="4" rx="2" fill={avatar.belt} />
    <rect x="30" y="42" width="4" height="4" rx="1" fill="#e9b44c" />

    <!-- épaules / capuche tombante -->
    <rect x="20" y="27" width="24" height="6" rx="3" fill={avatar.hood} />

    <!-- tête -->
    <circle cx="32" cy="18" r="9.5" fill={avatar.skin} />
    <!-- cheveux -->
    <path
      d="M22.5 16 C23 10 27 7.5 32 7.5 C37 7.5 41 10 41.5 16 C38 13 37 14.5 32 14.5 C27 14.5 26 13 22.5 16 Z"
      fill={avatar.hair}
    />
    <!-- visage -->
    <circle cx="28.5" cy="19" r="1.3" fill="#2a2018" />
    <circle cx="35.5" cy="19" r="1.3" fill="#2a2018" />
    <path d="M29.5 23 Q32 25 34.5 23" stroke="#b5836a" stroke-width="1.2" fill="none" stroke-linecap="round" />
  </svg>

  <!-- équipement visible -->
  {#if equipped.includes("sword")}<span class="absolute -right-1 top-8 text-sm" aria-hidden="true">⚔️</span>{/if}
  {#if equipped.includes("shield")}<span class="absolute -left-1 top-8 text-sm" aria-hidden="true">🛡️</span>{/if}
  {#if equipped.includes("helmet")}<span class="absolute -top-1 left-1/2 -translate-x-1/2 text-sm" aria-hidden="true">⛑️</span>{/if}
  {#if equipped.includes("amulet")}<span class="absolute top-[46%] left-1/2 -translate-x-1/2 text-xs" aria-hidden="true">📿</span>{/if}
  {#if equipped.includes("boots")}<span class="absolute -bottom-1 left-2 text-xs" aria-hidden="true">🥾</span>{/if}
  {#if equipped.includes("armor")}<span class="absolute top-[42%] left-1/2 -translate-x-1/2 text-xs" aria-hidden="true">✨</span>{/if}
</div>
