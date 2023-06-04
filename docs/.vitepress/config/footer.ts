import { DefaultTheme } from 'vitepress/theme'

export const footer: DefaultTheme.Config['footer'] = {
    copyright: `Copyright © 2023-${new Date().getFullYear()} <a href="https://github.com/mostlai">Pldada</a>, <a href="https://github.com/mostlai">Mostlai</a> present <br /><span id="siteruntime_span"></span>`,
    message: `Wrote with <i class="heart fa fa-heart fa-xs fa-beat"></i> and <i class="coffee fa fa-coffee fa-xs" aria-hidden="true"></i> by <a href="https://mostlai.github.io">Pldada</a> at <code>./usr/local</code>`,
}
