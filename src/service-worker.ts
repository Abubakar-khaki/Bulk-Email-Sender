/// <reference lib="webworker" />

declare const self: ServiceWorkerGlobalScope;

import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { CacheFirst, NetworkFirst, StaleWhileRevalidate } from 'workbox-strategies';
import { ExpirationPlugin } from 'workbox-expiration';

// Precache static assets
precacheAndRoute(self.__WB_MANIFEST);

// Cache API responses with Network First strategy
registerRoute(
  ({ url }) => url.pathname.startsWith('/api/'),
  new NetworkFirst({
    cacheName: 'api-cache',
    plugins: [
      new ExpirationPlugin({
        maxEntries: 50,
        maxAgeSeconds: 5 * 60, // 5 minutes
      }),
    ],
  })
);

// Cache images with Cache First strategy
registerRoute(
  ({ request }) => request.destination === 'image',
  new CacheFirst({
    cacheName: 'image-cache',
    plugins: [
      new ExpirationPlugin({
        maxEntries: 100,
        maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
      }),
    ],
  })
);

// Cache fonts with Cache First strategy
registerRoute(
  ({ request }) => request.destination === 'font',
  new CacheFirst({
    cacheName: 'font-cache',
    plugins: [
      new ExpirationPlugin({
        maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
      }),
    ],
  })
);

// Handle background sync for offline emails
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-emails') {
    event.waitUntil(syncPendingEmails());
  }
});

async function syncPendingEmails() {
  const cache = await caches.open('api-cache');
  const pendingEmails = await cache.match('/api/emails/pending');
  
  if (pendingEmails) {
    const data = await pendingEmails.json();
    for (const email of data) {
      try {
        await fetch('/api/emails/send', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(email),
        });
      } catch (error) {
        console.error('Failed to sync email:', error);
      }
    }
  }
}

// Push notifications
self.addEventListener('push', (event) => {
  const options: NotificationOptions = {
    badge: '/icons/badge-72.png',
    icon: '/icons/icon-192.png',
    body: event.data?.text() || 'Email campaign update',
    tag: 'campaign-notification',
    requireInteraction: false,
  };

  event.waitUntil(
    self.registration.showNotification('Bulk Email Sender', options)
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  event.waitUntil(
    clients.matchAll({ type: 'window' }).then((clientList) => {
      for (const client of clientList) {
        if (client.url === '/' && 'focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow('/');
      }
    })
  );
});
