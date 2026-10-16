<script>
  import { cn } from "$lib/utils.js";
  let { class: cls = "", children } = $props();
</script>

<!-- Grille 2x2 sur mobile (les libellés ne tiennent pas sur une seule ligne
     sous ~400px), une seule ligne centrée sur écrans plus larges -->
<div class={cn("grid w-full grid-cols-2 gap-2 sm:inline-flex sm:items-center sm:justify-center", cls)}>
  {@render children?.()}
</div>
