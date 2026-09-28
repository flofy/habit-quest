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
    "flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-1.5 rounded-lg px-2 py-2 text-sm font-medium transition-colors duration-100",
    "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
    "active:brightness-75",
    active
      ? "bg-primary text-primary-foreground"
      : "bg-secondary text-secondary-foreground hover:bg-secondary/70",
    cls
  )}
  aria-pressed={active}
  onclick={() => (tabs.value = value)}
>
  {@render children?.()}
</button>
