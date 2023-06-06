import { DefaultTheme } from 'vitepress/theme'

export const sidebar: DefaultTheme.Config['sidebar'] = {

    // 写作
    '/write/': [
        {
            text: 'Write Part 1',
            collapsed: false,
            items: [
                {
                    text: 'WP1 Detail',
                    link: '/write/wp1/witre_p1',
                },
            ],
        },
        {
            text: 'Write Part 2',
            collapsed: false,
            items: [
                {
                    text: 'WP2 Detail',
                    link: '/write/wp2/witre_p2',
                },
            ],
        },
        {
            text: 'Vocabulary',
            collapsed: false,
            items: [
                {
                    text: 'Vocabulary Detail',
                    link: '/write/vocabulary',
                },
            ],
        },
        {
            text: 'Synonymous Substitution',
            collapsed: false,
            items: [
                {
                    text: 'SS Detail',
                    link: '/write/sysu',
                },
            ],
        },
    ]
}
