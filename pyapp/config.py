header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cookie": "buvid3=E9F8C58B-5A00-44AC-B4C7-6C1A038CD75B143085infoc; CURRENT_FNVAL=4048; PVID=2; fingerprint=8a956b274e62abf91f8d2024ee0f593c; buvid_fp=42e5ac614167233fb95370e1213b2996; buvid_fp_plain=undefined; LIVE_BUVID=AUTO6216366229422943; i-wanna-go-back=-1; buvid4=FA0B2633-6D53-E7C5-7482-CC66EB4C3B7E64110-022012811-NH7Qrg7XI9IMGNEs9Y0PSQ%3D%3D; SESSDATA=7e98ef6c%2C1711033368%2Cddeb4%2A91CjDDsKEW8wP09VahCb4VxSAJKF_TbuCIdSHV5WxK44uskSocK4-r-xyEtNms44yeOa8SVmZuUDVUajhHc291LWxXWTA0NEp3MlYwUU9EMndUTGU3Ymw2VFBxV0lFZElIblBWdlBoLU9VSU1JS2lnSGRVT1BXeW16OHdRSkhhMTVuNVJfekFDLW1nIIEC; bili_jct=aebe894c17bdbfee168d74ec0ba0c5f8; DedeUserID=259464535; DedeUserID__ckMd5=583d4d22af13ff4b; CURRENT_QUALITY=80; _uuid=E93D1110B-6741-977A-F58A-931AE5717611077413infoc; rpdid=|(JR)m)m|~J0J'uYY)lm|muR; header_theme_version=CLOSE; home_feed_column=5; hit-new-style-dyn=1; CURRENT_PID=8661f860-cf0f-11ed-8d11-5de673290a14; b_ut=5; FEED_LIVE_VERSION=V8; browser_resolution=1408-687; bp_video_offset_259464535=844502445733183561; b_nut=100; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTU3NDA1ODQsImlhdCI6MTY5NTQ4MTMyNCwicGx0IjotMX0.vejjYyNVc0qqXoDdvQcJfVs4ZatpxJxjZn3sn8BU84w; bili_ticket_expires=1695740524",
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
