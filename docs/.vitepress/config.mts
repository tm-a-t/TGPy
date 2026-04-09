import { defineConfig } from 'vitepress'
import sidebar from "../tgpy/.site/sidebar";

export default defineConfig({
  title: "TGPy Docs Preview",
  themeConfig: {
    sidebar,
  },
  cleanUrls: true,
})
