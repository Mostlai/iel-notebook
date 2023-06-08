header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cookie": "buvid3=E9F8C58B-5A00-44AC-B4C7-6C1A038CD75B143085infoc; CURRENT_FNVAL=4048; blackside_state=0; PVID=1; fingerprint=350a108308a27bd722140d2ff5892422; buvid_fp=85a44c79b3c597ec64079fe615d7dccd; buvid_fp_plain=undefined; LIVE_BUVID=AUTO6216366229422943; i-wanna-go-back=-1; buvid4=FA0B2633-6D53-E7C5-7482-CC66EB4C3B7E64110-022012811-NH7Qrg7XI9IMGNEs9Y0PSQ%3D%3D; CURRENT_BLACKGAP=0; SESSDATA=d59c2f22%2C1701702318%2Cede29%2A61; bili_jct=f06584eccab8c23c75bcf3c432434412; DedeUserID=259464535; DedeUserID__ckMd5=583d4d22af13ff4b; b_nut=100; CURRENT_QUALITY=80; _uuid=E93D1110B-6741-977A-F58A-931AE5717611077413infoc; rpdid=|(JR)m)m|~J0J'uYY)lm|muR; header_theme_version=CLOSE; home_feed_column=5; hit-new-style-dyn=1; CURRENT_PID=8661f860-cf0f-11ed-8d11-5de673290a14; sid=gfbl1coj; b_ut=5; FEED_LIVE_VERSION=V8; browser_resolution=1920-1086; bp_video_offset_259464535=802508780928499700; b_lsid=410B29C39_188966407DA; bsource=search_baidu",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}


def search_by_keyword(page_size: str, keyword: str) -> str:
    api_url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?page_size=' + page_size + '&keyword=' + keyword + '&search_type=video&order=pubdate'
    return api_url


def search_by_tag(page_size: str, tag: str) -> str:
    api_url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?page_size=' + page_size + '&keyword=' + tag + '&search_type=video&order=pubdate&from_source=video_tag'
    return api_url
