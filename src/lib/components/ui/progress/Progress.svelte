<script>
  import { cn } from "$lib/utils.js";
  let { value = 0, max = 100, label = "Progression", class: cls = "" } = $props();
  const pct = $derived(Math.min(100, (value / max) * 100));
</script>

<div
  class={cn("panel-inset h-3.5 w-full overflow-hidden rounded-full p-[2px]", cls)}
  role="progressbar"
  aria-label={label}
  aria-valuenow={Math.round(value)}
  aria-valuemin="0"
  aria-valuemax={max}
>
  <div
    class="h-full rounded-full bg-gradient-to-b from-[#a5edb2] to-[#3f9c53] transition-all"
    style="width: {pct}%; box-shadow: inset 0 1px 0 rgba(255,255,255,.4);"
  ></div>
</div>
