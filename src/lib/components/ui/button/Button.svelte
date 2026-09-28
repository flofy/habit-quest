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

  // Tailles : cibles tactiles >= 44px (règle accessibilité tactile)
  const sizes = {
    default: "h-11 px-4 py-2 text-sm",
    sm: "h-11 px-3 text-sm",
    lg: "h-12 px-8 text-base",
    icon: "h-11 w-11",
  };
</script>

<button
  {type}
  {disabled}
  class={cn(
    "inline-flex cursor-pointer select-none items-center justify-center gap-2 rounded-lg font-medium transition-[background-color,filter,opacity] duration-100",
    "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
    "active:brightness-75 disabled:pointer-events-none disabled:opacity-40",
    variants[variant],
    sizes[size],
    cls
  )}
  {...rest}
>
  {@render children?.()}
</button>
