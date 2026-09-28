<script>
  import { cn } from "$lib/utils.js";
  let { value = 0, max = 100, label = "Progression", class: cls = "" } = $props();
  const pct = $derived(Math.min(100, (value / max) * 100));
</script>

<div
  class={cn("h-3 w-full overflow-hidden rounded-full border border-border bg-muted", cls)}
  role="progressbar"
  aria-label={label}
  aria-valuenow={Math.round(value)}
  aria-valuemin="0"
  aria-valuemax={max}
>
  <div class="h-full bg-gradient-to-r from-accent to-primary transition-all" style="width: {pct}%"></div>
</div>
