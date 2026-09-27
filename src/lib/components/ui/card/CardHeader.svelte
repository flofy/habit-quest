<script>
  import { cn } from "$lib/utils.js";
  let { class: cls = "", children, ...rest } = $props();
</script>

<div class={cn("flex flex-col space-y-1.5 p-4", cls)} {...rest}>
  {@render children?.()}
</div>
