<script>
  import { cn } from "$lib/utils.js";
  let { class: cls = "", children, ...rest } = $props();
</script>

<div class={cn("rounded-xl border border-border bg-card text-card-foreground shadow-sm", cls)} {...rest}>
  {@render children?.()}
</div>
