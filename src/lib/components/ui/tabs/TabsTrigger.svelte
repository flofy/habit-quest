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
    "flex-1 cursor-pointer rounded-lg px-3 py-1.5 text-sm font-medium transition-colors",
    active ? "bg-primary text-primary-foreground" : "bg-secondary text-secondary-foreground hover:bg-secondary/70",
    cls
  )}
  onclick={() => (tabs.value = value)}
>
  {@render children?.()}
</button>
