<script>
  // Héros : sprite PNG si présent dans src/lib/assets/heroes/, sinon vectoriel détaillé.
  // Convention de fichier : hero-sword.png, hero-staff.png, hero-bow.png
  const heroModules = import.meta.glob("$lib/assets/heroes/*.png", {
    eager: true,
    query: "?url",
    import: "default",
  });

  let { avatar, size = 96, equipped = [] } = $props();

  const gid = $derived("hero-" + avatar.weapon);
  const pngKey = $derived("/src/lib/assets/heroes/hero-" + avatar.weapon + ".png");
  const pngSrc = $derived(heroModules[pngKey] ?? null);
</script>

<div class="relative" style="width: {size}px; height: {size}px;">
  {#if pngSrc}
    <img
      src={pngSrc}
      alt="Personnage : {avatar.name}"
      class="h-full w-full object-contain drop-shadow-[0_4px_8px_rgba(0,0,0,0.4)]"
    />
  {:else}
    <svg viewBox="0 0 64 64" width={size} height={size} shape-rendering="geometricPrecision">
      <defs>
        <linearGradient id={gid + "-robe"} x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color={avatar.robe[0]} />
          <stop offset="1" stop-color={avatar.robe[1]} />
        </linearGradient>
        <linearGradient id={gid + "-metal"} x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="#e8edf2" />
          <stop offset="0.5" stop-color="#b9c4ce" />
          <stop offset="1" stop-color="#8b97a3" />
        </linearGradient>
        <radialGradient id={gid + "-orb"} cx="0.5" cy="0.4" r="0.6">
          <stop offset="0" stop-color="#eaffff" />
          <stop offset="0.5" stop-color="#9be8ff" />
          <stop offset="1" stop-color="#4f9fd8" />
        </radialGradient>
      </defs>

      <!-- ombre de contact -->
      <ellipse cx="32" cy="61" rx="17" ry="3.5" fill="rgba(0,0,0,0.35)" />

      <!-- arme de classe -->
      {#if avatar.weapon === "staff"}
        <rect x="50" y="16" width="3" height="42" rx="1.5" fill="#7a5a34" />
        <rect x="49.4" y="18" width="1" height="36" rx="0.5" fill="#9a7748" opacity="0.8" />
        <circle cx="51.5" cy="13" r="7" fill="#9be8ff" opacity="0.25" />
        <circle cx="51.5" cy="13" r="4.2" fill="url(#{gid}-orb)" />
        <path d="M49.5 9.5 L50.2 11 L48.6 11.2 Z" fill="#eaffff" opacity="0.9" />
      {/if}
      {#if avatar.weapon === "sword"}
        <rect x="10.5" y="24" width="3" height="24" rx="1" fill="url(#{gid}-metal)" />
        <rect x="11.2" y="25" width="0.8" height="20" rx="0.4" fill="#ffffff" opacity="0.55" />
        <rect x="7" y="48" width="10" height="3" rx="1.5" fill="#8a5f16" />
        <circle cx="12" cy="52.5" r="1.6" fill="#e9b44c" />
        <rect x="10.8" y="50" width="2.4" height="5" rx="1.2" fill="#6b4a1e" />
      {/if}
      {#if avatar.weapon === "bow"}
        <path d="M13 27 Q4.5 42 13 57" stroke="#8b5a2b" stroke-width="3" fill="none" stroke-linecap="round" />
        <path d="M13 27 Q4.5 42 13 57" stroke="#a9773f" stroke-width="1.2" fill="none" opacity="0.6" />
        <line x1="13" y1="27" x2="13" y2="57" stroke="#d8d0c0" stroke-width="1" />
      {/if}

      <!-- cape -->
      <path
        d="M20 29 C11 37 10 51 13 57 C24 55 40 55 51 57 C54 51 53 37 44 29 C36 33.5 28 33.5 20 29 Z"
        fill={avatar.hood}
        opacity="0.85"
      />
      <path d="M20 29 C15 36 14 45 15 52 C17 51 18.5 50 19 48 C17 41 18 34 22 30 Z" fill="#000" opacity="0.15" />

      <!-- bottes -->
      <rect x="25" y="50" width="6" height="9" rx="2" fill="#4a3524" />
      <rect x="33" y="50" width="6" height="9" rx="2" fill="#4a3524" />
      <rect x="25" y="56.5" width="6" height="2" rx="1" fill="#2e2115" />
      <rect x="33" y="56.5" width="6" height="2" rx="1" fill="#2e2115" />

      <!-- robe -->
      <path d="M20 52 C18 38 22 30 32 28 C42 30 46 38 44 52 Z" fill="url(#{gid}-robe)" />
      <!-- pli central de la robe -->
      <path d="M32 30 C32.5 38 32.5 45 32 51 C31.5 45 31.5 38 32 30 Z" fill="#000" opacity="0.12" />

      <!-- bras -->
      <rect x="16" y="30" width="6" height="16" rx="3" fill={avatar.robe[1]} />
      <rect x="42" y="30" width="6" height="16" rx="3" fill={avatar.robe[1]} />
      <!-- mains -->
      <circle cx="19" cy="46" r="2.4" fill={avatar.skin} />
      <circle cx="45" cy="46" r="2.4" fill={avatar.skin} />

      <!-- ceinture -->
      <rect x="21" y="42" width="22" height="4.5" rx="2" fill={avatar.belt} />
      <rect x="21" y="42" width="22" height="1.6" rx="0.8" fill="#000" opacity="0.18" />
      <rect x="29.5" y="41.5" width="5" height="5.5" rx="1.5" fill="#e9b44c" />
      <rect x="29.5" y="41.5" width="5" height="2" rx="1" fill="#f7df9a" opacity="0.8" />

      <!-- épaulières -->
      <rect x="16.5" y="26.5" width="7" height="5" rx="2.5" fill="url(#{gid}-metal)" />
      <rect x="40.5" y="26.5" width="7" height="5" rx="2.5" fill="url(#{gid}-metal)" />

      <!-- col -->
      <rect x="27" y="26" width="10" height="4" rx="2" fill={avatar.hood} />

      <!-- tête -->
      <circle cx="32" cy="18" r="9.5" fill={avatar.skin} />
      <!-- oreilles -->
      <circle cx="22.8" cy="18.5" r="1.4" fill={avatar.skin} />
      <circle cx="41.2" cy="18.5" r="1.4" fill={avatar.skin} />

      <!-- cheveux -->
      <path
        d="M22.5 16 C23 10 27 7.5 32 7.5 C37 7.5 41 10 41.5 16 C38 13 37 14.5 32 14.5 C27 14.5 26 13 22.5 16 Z"
        fill={avatar.hair}
      />
      <path d="M24 11.5 C26 9 29 8 32 8.5" stroke="#000" stroke-width="0.8" opacity="0.15" fill="none" />

      <!-- visage -->
      <path d="M26.5 16.4 L30.4 15.8" stroke={avatar.hair} stroke-width="1.2" stroke-linecap="round" />
      <path d="M33.6 15.8 L37.5 16.4" stroke={avatar.hair} stroke-width="1.2" stroke-linecap="round" />
      <circle cx="28.5" cy="19" r="1.4" fill="#2a2018" />
      <circle cx="35.5" cy="19" r="1.4" fill="#2a2018" />
      <circle cx="28.9" cy="18.6" r="0.45" fill="#fff" opacity="0.9" />
      <circle cx="35.9" cy="18.6" r="0.45" fill="#fff" opacity="0.9" />
      <ellipse cx="26.2" cy="21.8" rx="1.3" ry="0.8" fill="#d98a6a" opacity="0.35" />
      <ellipse cx="37.8" cy="21.8" rx="1.3" ry="0.8" fill="#d98a6a" opacity="0.35" />
      <path d="M29.5 23 Q32 25.2 34.5 23" stroke="#b5836a" stroke-width="1.2" fill="none" stroke-linecap="round" />
    </svg>
  {/if}

  <!-- équipement visible -->
  {#if equipped.includes("sword")}<span class="absolute -right-1 top-8 text-sm" aria-hidden="true">⚔️</span>{/if}
  {#if equipped.includes("shield")}<span class="absolute -left-1 top-8 text-sm" aria-hidden="true">🛡️</span>{/if}
  {#if equipped.includes("helmet")}<span class="absolute -top-1 left-1/2 -translate-x-1/2 text-sm" aria-hidden="true">⛑️</span>{/if}
  {#if equipped.includes("amulet")}<span class="absolute top-[46%] left-1/2 -translate-x-1/2 text-xs" aria-hidden="true">📿</span>{/if}
  {#if equipped.includes("boots")}<span class="absolute -bottom-1 left-2 text-xs" aria-hidden="true">🥾</span>{/if}
  {#if equipped.includes("armor")}<span class="absolute top-[42%] left-1/2 -translate-x-1/2 text-xs" aria-hidden="true">✨</span>{/if}
</div>
