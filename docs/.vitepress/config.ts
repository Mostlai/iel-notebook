import { defineConfig} from 'vitepress'
import { markdown } from './config/markdown'
import { metaData } from './config/constants'
import { head } from './config/head'
import { themeConfig } from './config/theme'

// import { SitemapStream } from 'sitemap'
// import { createWriteStream } from 'node:fs'
// import { resolve } from 'node:path'

const links: { url: string; lastmod: PageData['lastUpdated'] }[] = []

export default defineConfig({
    lang: metaData.lang, // i18n default english translation
    title: metaData.title, // title from metadata config
    description: metaData.description, // description from metadata config
    markdown: markdown, // markdown config
    lastUpdated: true, // whether enabling lastupdated or not
    head, // documentation head tag options
    base: '/iel-notebook/',
    themeConfig, // default exported theme config
    cleanUrls: true, // clean urls configs to remove standard genreated page file type extensions
    outDir: '../dist', // specify staic pages build output dir
    // vue template options for preventing katex build crashes
    // vue: {
    //     template: {
    //         compilerOptions: {
    //             isCustomElement: tag => customElements.includes(tag),
    //         },
    //     },
    // },
    // i18n localization config
    locales: {
        '/': {
            label: 'English',
            lang: 'en-US',
        },
    },
    ignoreDeadLinks: true,
    transformHtml: (_, id, { pageData }) => {
         if (!/[\\/]404\.html$/.test(id))
             links.push({
                 url: pageData.relativePath.replace(/((^|\/)index)?\.md$/, '$2'),
                 lastmod: pageData.lastUpdated,
             })
     },
    // buildEnd: async ({ outDir }) => {
    //     const sitemap = new SitemapStream({ hostname: 'https://mostlai.github.io/iel-notebook' })
    //     const writeStream = createWriteStream(resolve(outDir, 'sitemap.xml'))
    //     sitemap.pipe(writeStream)
    //     links.forEach(link => sitemap.write(link))
    //     sitemap.end()
    //     await new Promise(r => writeStream.on('finish', r))
    // },
})