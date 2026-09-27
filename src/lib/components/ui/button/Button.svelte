<script>
  import { cn } from "$lib/utils.js";
  let {
    class: cls = "",
    variant = "default",
    size = "default",
    type = "button",
    disabled = false,
    children,
    ...rest
  } = $props();

  const variants = {
    default: "bg-primary text-primary-foreground hover:bg-primary/90",
    secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
    accent: "bg-accent text-accent-foreground hover:bg-accent/90",
    outline: "border border-border bg-transparent hover:bg-secondary",
    ghost: "hover:bg-secondary",
    destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
  };

  const sizes = {
    default: "h-9 px-4 py-2 text-sm",
    sm: "h-8 rounded-lg px-3 text-xs",
    lg: "h-11 rounded-lg px-8",
    icon: "h-9 w-9",
  };
</script>

<button
  {type}
  {disabled}
  class={cn(
    "inline-flex items-center justify-center gap-2 rounded-lg font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-40 cursor-pointer",
    variants[variant],
    sizes[size],
    cls
  )}
  {...rest}
>
  {@render children?.()}
</button>
