<script>
  import { cn } from "$lib/utils.js";
  let { class: cls = "", children, ...rest } = $props();
</script>

<div class={cn("p-4 pt-0", cls)} {...rest}>
  {@render children?.()}
</div>
