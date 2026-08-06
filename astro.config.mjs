import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://chinese-traditional-wear.com',
  trailingSlash: 'never',
  integrations: [tailwind(), sitemap()],
});