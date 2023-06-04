import { DefaultTheme } from 'vitepress/theme'

export const sidebar: DefaultTheme.Config['sidebar'] = {
    // development related documents
    '/development/': [
        {
            text: 'Wiki Database',
            collapsed: false,
            items: [{ text: 'File Naming Convention', link: '/development/file-naming-convention' }],
        },
    ],

    // 写作
    '/write/': [
        {
            text: 'Write Part 1',
            collapsed: false,
            items: [
                {
                    text: 'Detail',
                    link: '/write/wp1/',
                },
            ],
        },
        {
            text: 'Write Part 2',
            collapsed: false,
            items: [
                {
                    text: 'Detail',
                    link: '/write/wp2/',
                },
            ],
        },
        {
            text: 'Synonymous Substitution',
            collapsed: false,
            items: [
                {
                    text: 'Detail',
                    link: '/write/sysu/',
                },
            ],
        },
    ]
}
