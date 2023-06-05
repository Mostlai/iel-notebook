import type { MarkdownOptions } from 'vitepress'
//import mdTasklist from 'markdown-it-task-lists'
//import mdLink from 'markdown-it-link-preview'

export const markdown: MarkdownOptions = {
    html: true,
    theme: {
        light: 'one-dark-pro',
        dark: 'material-theme-palenight',
    },
    lineNumbers: true,
    config: md => {
        // use more markdown-it plugins!
        // md.use(mdkatex), md.use(mdTasklist), md.use(mdCaption), md.use(mdLink)
    },
}
