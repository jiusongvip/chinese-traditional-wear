/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // Primary palette — Chinese vermillion red
        vermillion: {
          50:  '#fdf2f2',
          100: '#fce4e4',
          200: '#f9c4c4',
          300: '#f39393',
          400: '#e85d5d',
          500: '#d93a3a',
          600: '#b5343a',  // brand primary
          700: '#972930',
          800: '#7e232b',
          900: '#6a2028',
          950: '#3b0d12',
        },
        // Secondary palette — muted jade green
        jade: {
          50:  '#f2f7f4',
          100: '#e0ede4',
          200: '#c2dbca',
          300: '#95bfa3',
          400: '#68a078',
          500: '#48855c',
          600: '#2d6a4f',  // brand secondary
          700: '#27563f',
          800: '#214533',
          900: '#1c392b',
          950: '#0e2017',
        },
        // Neutral palette — warm stone / ink
        warm: {
          50:  '#faf7f2',  // rice paper
          100: '#f3efe7',
          200: '#e8dfd1',
          300: '#d6c9b4',
          400: '#bfad93',
          500: '#a89074',
          600: '#8c735a',
          700: '#735d4a',
          800: '#5e4c3d',
          900: '#1a1714',  // ink black
          950: '#0f0d0b',
        },
      },
      fontFamily: {
        display: ['"Noto Serif SC"', 'Georgia', 'serif'],
        sans:   ['"Outfit"', 'system-ui', '-apple-system', 'sans-serif'],
      },
      animation: {
        'fade-up':    'fadeUp 0.6s ease-out both',
        'fade-in':    'fadeIn 0.5s ease-out both',
        'slide-left': 'slideLeft 0.5s ease-out both',
        'float':      'float 6s ease-in-out infinite',
        'shimmer':    'shimmer 2s ease-in-out infinite',
      },
      keyframes: {
        fadeUp: {
          '0%':   { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        fadeIn: {
          '0%':   { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideLeft: {
          '0%':   { opacity: '0', transform: 'translateX(30px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%':      { transform: 'translateY(-10px)' },
        },
        shimmer: {
          '0%':   { backgroundPosition: '-200% 0' },
          '100%': { backgroundPosition: '200% 0' },
        },
      },
      backgroundImage: {
        'ink-wash': 'radial-gradient(ellipse at 30% 50%, rgba(45,106,79,0.06) 0%, transparent 70%)',
        'warm-glow': 'radial-gradient(ellipse at 70% 30%, rgba(181,52,58,0.05) 0%, transparent 60%)',
      },
    },
  },
  plugins: [],
};
