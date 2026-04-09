import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'

const customComponents = import.meta.glob('../../**/.site/*.vue', { eager: true })

export default {
  extends: DefaultTheme,
  enhanceApp({ app, router, siteData }) {
    for (const [filepath, component] of Object.entries(customComponents)) {
      const name = filepath.match(/\/([^/]+)\.vue$/)[1];
      app.component(name, component.default);
    }
  }
} satisfies Theme
