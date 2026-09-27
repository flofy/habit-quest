<script>
  import { cn } from "$lib/utils.js";
  let { class: cls = "", variant = "default", children, ...rest } = $props();
  const variants = {
    default: "border-transparent bg-primary text-primary-foreground",
    secondary: "border-transparent bg-secondary text-secondary-foreground",
    outline: "text-foreground",
    success: "border-transparent bg-accent text-accent-foreground",
  };
</script>

<span
  class={cn("inline-flex items-center rounded-md border px-2 py-0.5 text-xs font-medium", variants[variant], cls)}
  {...rest}
>
  {@render children?.()}
</span>
