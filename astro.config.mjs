import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.chinese-traditional-wear.com',
  trailingSlash: 'always',
  build: { inlineStylesheets: 'always' },
  integrations: [tailwind(), sitemap({
    filter: (url) => !url.endsWith('/qipao') && !url.endsWith('/tang'),
  })],
});