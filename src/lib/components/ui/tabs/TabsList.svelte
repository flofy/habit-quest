<script>
  import { cn } from "$lib/utils.js";
  let { class: cls = "", children } = $props();
</script>

<div class={cn("inline-flex w-full items-center justify-center gap-2", cls)}>
  {@render children?.()}
</div>
