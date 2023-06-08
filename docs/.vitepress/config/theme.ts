import { DefaultTheme } from 'vitepress/theme'
import { nav } from './nav'
import { sidebar } from './sidebar'
import { footer } from './footer'

export const themeConfig: DefaultTheme.Config = {
    nav, // documentation navigation bar config
    sidebar, // documentation sidebar config
    footer, // site global footer config

    logo: 'https://cdn.jsdelivr.net/gh/mostlai/mostlai-cdn@latest/img/physic.png',
    outline: 'deep', // documentation outline header precedence
    outlineTitle: 'TOC', // documentation outline title text
    outlineBadges: false, // whether to show badge on outline
    lastUpdatedText: 'Last updated', // config for last updated footer text
    // documentation full text search config via algolia
    algolia: {
        appId: 'D4WCOH278L',
        apiKey: '0a81dea75b4bf4c78c42bdfd352cee91',
        indexName: 'pldocs',
    },
    // documentation edit link
    editLink: {
        pattern: 'https://github.com/mostlai/iel-notebook/edit/main/docs/:path',
        text: 'Edit this page on GitHub',
    },

    socialLinks: [
        { icon: 'github', link: 'https://github.com/mostlai' },
    ],
}
