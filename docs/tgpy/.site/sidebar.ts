import {DefaultTheme} from 'vitepress'

const sidebar: DefaultTheme.SidebarItem[] = [
  {text: 'Overview', link: '/tgpy/'},
  {text: 'Installation', link: '/tgpy/installation'},
  {
    text: 'Beginner’s Guide',
    items: [
      {text: 'Running Code', link: '/tgpy/basics/code'},
      {text: 'Asyncio', link: '/tgpy/basics/asyncio'},
      {text: 'Messages', link: '/tgpy/basics/messages'},
      {text: 'Examples', link: '/tgpy/basics/examples'},
    ],
  },
  {
    text: 'Extensibility Guide',
    items: [
      {text: 'Context Data', link: '/tgpy/extensibility/context'},
      {text: 'Modules', link: '/tgpy/extensibility/modules'},
      {text: 'Module Examples', link: '/tgpy/extensibility/module-examples'},
      {text: 'Transformers & Hooks', link: '/tgpy/extensibility/transformers'},
      {text: 'Other API Features', link: '/tgpy/extensibility/api'},
    ],
  },
  {
    text: 'Reference',
    items: [
      {text: 'Builtins', link: '/tgpy/reference/builtins'},
      {text: 'Module Metadata', link: '/tgpy/reference/module-metadata'},
      {text: 'Code Detection', link: '/tgpy/reference/code-detection'},
    ],
  },
  {
    text: 'TGPy Recipes',
    items: [
      {text: 'About recipes', link: '/tgpy/recipes/about'},
      {text: 'Asking ChatGPT from TGPy', link: '/tgpy/recipes/chatgpt'},
      {text: 'Throwing dice (and faking the result)', link: '/tgpy/recipes/dice'},
      {text: 'Setting up reminders', link: '/tgpy/recipes/reminders'},
      {text: 'Auto-adding group members to contacts to see their stories', link: '/tgpy/recipes/contacts'},
      {text: 'Writing TGPy programs in code editors', link: '/tgpy/recipes/editors'},
    ],
  },
  {text: 'Russian Chat', link: 'tg://resolve?domain=tgpy_flood'},
]

export default sidebar