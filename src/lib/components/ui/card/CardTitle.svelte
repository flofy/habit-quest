<script>
  import { cn } from "$lib/utils.js";
  let { class: cls = "", children, ...rest } = $props();
</script>

<h3 class={cn("font-display text-base font-bold leading-none tracking-wide text-foreground", cls)} {...rest}>
  {@render children?.()}
</h3>
