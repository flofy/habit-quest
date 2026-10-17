// Service worker Habit Quest.
// Objectif : rendre l'application installable et utilisable hors ligne.
// Stratégie :
// - navigations : réseau d'abord (pour servir les nouvelles versions après
//   déploiement), repli sur le cache hors ligne ;
// - ressources same-origin (JS/CSS/icônes) et polices Google : cache d'abord,
//   mise à jour en arrière-plan.
// Les données du jeu vivent dans localStorage et ne passent pas par ici.

const CACHE = "habit-quest-v1";
const CACHE_PREFIX = "habit-quest-";
const SHELL = ["./"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open(CACHE)
      .then((cache) => cache.addAll(SHELL))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys
            .filter((key) => key.startsWith(CACHE_PREFIX) && key !== CACHE)
            .map((key) => caches.delete(key))
        )
      )
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (request.method !== "GET") return;

  const url = new URL(request.url);

  // Navigation : réseau d'abord, cache de secours.
  if (request.mode === "navigate") {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const copy = response.clone();
          caches.open(CACHE).then((cache) => cache.put(request, copy));
          return response;
        })
        .catch(() =>
          caches.match(request).then((cached) => cached || caches.match("./"))
        )
    );
    return;
  }

  // Cache d'abord pour nos ressources et les polices Google.
  const sameOrigin = url.origin === self.location.origin;
  const googleFonts =
    url.hostname === "fonts.googleapis.com" ||
    url.hostname === "fonts.gstatic.com";
  if (!sameOrigin && !googleFonts) return;

  event.respondWith(
    caches.match(request).then((cached) => {
      const network = fetch(request)
        .then((response) => {
          if (response && (response.ok || response.type === "opaque")) {
            const copy = response.clone();
            caches.open(CACHE).then((cache) => cache.put(request, copy));
          }
          return response;
        })
        .catch(() => cached);
      return cached || network;
    })
  );
});
