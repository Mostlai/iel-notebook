import { DefaultTheme } from 'vitepress/theme'

export const nav: DefaultTheme.Config['nav'] = [
    {
        text: 'Home',
        link: '/',
    },
    {
        text: 'Development',
        items:[
        	{text: 'Commit',link: '/development/conventional_commit'},
        ]
    },
    {
        text: 'Speak',
        link: '/speak/',
    },
    {
        text: 'Listen',
        link: '/listen/',
    },
    {
        text: 'Read',
        link: '/read/',
    },
    {
        text: 'Write',
        link: '/write/',
    },
]
