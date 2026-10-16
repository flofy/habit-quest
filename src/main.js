import { mount } from "svelte";
import "./app.css";
import App from "./App.svelte";

const app = mount(App, {
  target: document.getElementById("app"),
});

export default app;

// PWA : enregistrement du service worker (production uniquement).
// Le chemin relatif suit le "base" de Vite ("/habit-quest/") et fonctionne
// donc aussi bien sur GitHub Pages qu'en local via `npm run preview`.
if ("serviceWorker" in navigator && import.meta.env.PROD) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("sw.js").catch(() => {
      // Échec silencieux : l'application reste pleinement utilisable.
    });
  });
}
