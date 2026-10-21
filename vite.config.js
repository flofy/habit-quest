import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import tailwindcss from "@tailwindcss/vite";
import { fileURLToPath, URL } from "node:url";

// GitHub Pages héberge le projet sous /habit-quest/.
// Les previews Netlify et le développement local servent l'app à la racine.
const base = process.env.GITHUB_ACTIONS === "true" ? "/habit-quest/" : "/";

export default defineConfig({
  base,
  plugins: [tailwindcss(), svelte()],
  resolve: {
    alias: {
      $lib: fileURLToPath(new URL("./src/lib", import.meta.url)),
    },
  },
});
