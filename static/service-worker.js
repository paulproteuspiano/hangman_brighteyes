const CACHE_NAME = 'hangman-cache-v1';
const urlsToCache = [
  '/',
  '/static/style.css',  // your CSS
  '/static/manifest.json',
  '/static/icons/icon-192.png',
  '/static/icons/icon-512.png',
  // Add any .svg, .mp3, .gif used in game
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(resp => resp || fetch(event.request))
  );
});
