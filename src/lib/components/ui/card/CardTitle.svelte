<script>
  import { cn } from "$lib/utils.js";
  let { class: cls = "", children, ...rest } = $props();
</script>

<h3 class={cn("font-bold leading-none tracking-wide", cls)} {...rest}>
  {@render children?.()}
</h3>
