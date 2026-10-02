<script>
  import { cn } from "$lib/utils.js";
  let { class: cls = "", children, ...rest } = $props();
</script>

<div class={cn("panel", cls)} {...rest}>
  {@render children?.()}
</div>
