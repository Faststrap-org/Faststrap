const CACHE_NAME = 'faststrap-app-v1';
const ASSETS_TO_CACHE = [
    // Faststrap Core
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css',
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js',
    'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css',
    // Local Assets (if any)
    '/static/css/faststrap-fx.css',
    '/static/css/faststrap-layouts.css',
    // Fallback Offline Page
    '/offline'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ASSETS_TO_CACHE);
        })
    );
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

self.addEventListener('fetch', (event) => {
    // Only handle GET requests
    if (event.request.method !== 'GET') return;

    // Strategy: Network First, falling back to Cache
    // Ideally we want fresh content (HTMX), but if offline, show cached or offline page
    event.respondWith(
        fetch(event.request)
            .then((response) => {
                // If it's a valid response, verify if we should cache it (e.g. assets)
                if (!response || response.status !== 200 || response.type !== 'basic') {
                    return response;
                }
                
                // Optional: Dynamic caching logic here if needed
                return response;
            })
            .catch(() => {
                // Network failed, try cache
                return caches.match(event.request)
                    .then((cachedResponse) => {
                        if (cachedResponse) {
                            return cachedResponse;
                        }
                        // If not in cache and it's a navigation request, show offline page
                        if (event.request.mode === 'navigate') {
                            return caches.match('/offline');
                        }
                        return null;
                    });
            })
    );
});
