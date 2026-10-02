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

  // Boutons RPG : dégradé + profondeur 3D, enfoncement à l'appui.
  const variants = {
    default:
      "bg-gradient-to-b from-[#f4cd6f] to-[#dda031] text-[#3a2a08] border border-[#8a5f16] shadow-[0_3px_0_#8a5f16,0_6px_12px_rgba(0,0,0,.35),inset_0_1px_0_rgba(255,255,255,.4)] active:shadow-[0_0_0_#8a5f16,inset_0_1px_0_rgba(255,255,255,.4)]",
    secondary:
      "bg-gradient-to-b from-[#3b5640] to-[#2c4230] text-secondary-foreground border border-[#55763f] shadow-[0_3px_0_#1b291d,0_6px_12px_rgba(0,0,0,.3),inset_0_1px_0_rgba(255,255,255,.1)] active:shadow-[0_0_0_#1b291d,inset_0_1px_0_rgba(255,255,255,.1)]",
    accent:
      "bg-gradient-to-b from-[#8fe3a0] to-[#4faf62] text-accent-foreground border border-[#2c6b3a] shadow-[0_3px_0_#2c6b3a,0_6px_12px_rgba(0,0,0,.35),inset_0_1px_0_rgba(255,255,255,.4)] active:shadow-[0_0_0_#2c6b3a,inset_0_1px_0_rgba(255,255,255,.4)]",
    outline:
      "bg-transparent text-primary border border-primary/70 hover:bg-primary/10",
    ghost: "hover:bg-secondary",
    destructive:
      "bg-gradient-to-b from-[#ee8174] to-[#c14a3d] text-destructive-foreground border border-[#7a2a20] shadow-[0_3px_0_#7a2a20,0_6px_12px_rgba(0,0,0,.35),inset_0_1px_0_rgba(255,255,255,.3)] active:shadow-[0_0_0_#7a2a20,inset_0_1px_0_rgba(255,255,255,.3)]",
  };

  const sizes = {
    default: "h-11 px-4 py-2 text-sm font-bold",
    sm: "h-11 px-3 text-sm font-bold",
    lg: "h-12 px-8 text-base font-bold",
    icon: "h-11 w-11",
  };
</script>

<button
  {type}
  {disabled}
  class={cn(
    "inline-flex cursor-pointer select-none items-center justify-center gap-2 rounded-lg transition-all duration-75",
    "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background",
    "active:translate-y-[3px] disabled:pointer-events-none disabled:opacity-40",
    variants[variant],
    sizes[size],
    cls
  )}
  {...rest}
>
  {@render children?.()}
</button>
