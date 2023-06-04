import type { HeadConfig } from 'vitepress'
import { metaData } from './constants'

export const head: HeadConfig[] = [
    // stylesheets loaded from thrid-party cdns
    // <script src="https://fastly.jsdelivr.net/gh/stevenjoezhang/live2d-widget@latest/autoload.js"></script>

    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'author', content: 'Pldada' }],
    [
        'meta',
        {
            name: 'keywords',
            content:
                'Pldada',
        },
    ],
    ['meta', { name: 'HandheldFriendly', content: 'True' }],
    ['meta', { name: 'MobileOptimized', content: '320' }],
    ['meta', { name: 'theme-color', content: '#3c8772' }],

    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:locale', content: metaData.locale }],
    ['meta', { property: 'og:title', content: metaData.title }],
    ['meta', { property: 'og:description', content: metaData.description }],
    ['meta', { property: 'og:site', content: metaData.site }],
    ['meta', { property: 'og:site_name', content: metaData.title }],
    ['meta', { property: 'og:image', content: metaData.image }],
]
