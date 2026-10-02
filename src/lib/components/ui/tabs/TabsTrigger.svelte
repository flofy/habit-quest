<script>
  import { getContext } from "svelte";
  import { cn } from "$lib/utils.js";
  let { value, class: cls = "", children } = $props();
  const tabs = getContext("tabs");
  const active = $derived(tabs.value === value);
</script>

<button
  type="button"
  class={cn(
    "flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-1.5 rounded-lg px-2 py-2 text-sm transition-all duration-75",
    "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
    "active:translate-y-[2px]",
    active
      ? "bg-gradient-to-b from-[#f4cd6f] to-[#dda031] font-extrabold text-[#3a2a08] border border-[#8a5f16] shadow-[0_2px_0_#8a5f16,inset_0_1px_0_rgba(255,255,255,.4)]"
      : "border border-transparent bg-secondary/60 font-bold text-muted-foreground hover:bg-secondary hover:text-secondary-foreground shadow-[0_2px_0_#0a120d]",
    cls
  )}
  aria-pressed={active}
  onclick={() => (tabs.value = value)}
>
  {@render children?.()}
</button>
