header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cookie": "buvid3=4B80DCE3-AD26-E0EF-EB46-D47F6E9DA3FC77994infoc; b_nut=1669387777; i-wanna-go-back=-1; CURRENT_FNVAL=4048; _uuid=DB34A6C8-1323-DEB5-7F26-C1010B5723D7CA15930infoc; buvid4=2BEC82E2-EA56-92AC-B900-293E56EA16AD15797-022112621-pBL8cDAn3mlXX0rpzgdsLw6oNeJTaqwhsBAEfQkr4jKK7wyrlGZbog%3D%3D; rpdid=0zbfVHhITS|bHtuF2Gb|MaG|3w1OYVrm; LIVE_BUVID=AUTO9816711916715044; header_theme_version=CLOSE; home_feed_column=5; DedeUserID=259464535; DedeUserID__ckMd5=583d4d22af13ff4b; CURRENT_PID=231d4080-d3be-11ed-9aab-a362deb8a318; CURRENT_QUALITY=80; b_ut=5; buvid_fp_plain=undefined; nostalgia_conf=-1; FEED_LIVE_VERSION=V8; PVID=1; browser_resolution=1920-1095; bp_video_offset_259464535=802508780928499700; SESSDATA=a71b9504%2C1701574033%2Ca9f43%2A61; bili_jct=f43d1ece5f41d8bad2cc89f42d1a4d19; fingerprint=1ded11fa8a2b6e1f2aaf81b0d0cb0a30; buvid_fp=1ded11fa8a2b6e1f2aaf81b0d0cb0a30",
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
