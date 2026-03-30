import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    VitePWA({
       registerType: 'autoUpdate',
       manifest: {
         name: 'My App',
         short_name: 'App',
         description: 'My Awesome App',
         theme_color: '#ffffff',
         icons: [
           {
             src: 'icon.png',
             sizes: '192x192',
             type: 'image/png'
           }
         ]
       }
     })
  ],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
});