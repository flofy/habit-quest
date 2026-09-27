<script>
  import { setContext } from "svelte";
  let { value = $bindable(""), children } = $props();
  setContext("tabs", {
    get value() { return value; },
    set value(v) { value = v; },
  });
</script>

{@render children?.()}
