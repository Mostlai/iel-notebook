import json
import requests
import config


def delete_element(txt: str) -> str:
    txt = txt.replace('<em class="keyword">', '')
    txt = txt.replace('</em>', '')
    return txt


def process_pic(txt: str) -> str:
    base_url = 'https://i1.hdslb.com/bfs/archive'
    final_url = base_url + txt.split('archive')[1]
    return final_url


def get_pubdate(page_size: str, keyword: str, list_name: str) -> list:
    final_data = list()
    url = config.search_by_tag(page_size, keyword)
    json_data = requests.get(url, headers=config.header).json()
    result = json_data["data"]["result"]
    for i in result:
        process_data = {
            'title': delete_element(i['title']),
            'url': i['arcurl'],
            'pic': process_pic(i['pic']),
            'author': i['author'],
            'play': i['play'],
            'favorites': i['favorites'],
            'duration': i['duration'],
            'pubdate': i['pubdate']
        }
        final_data.append(process_data)
    warp_data = [{list_name: final_data}]
    return warp_data


def write_json(json_data: list) -> None:
    file_url = '../docs/.vitepress/theme/components/public/data.json'
    with open(file_url, "w", encoding="utf-8") as f:
        content = json.dumps(json_data, indent=4, ensure_ascii=False)
        f.write(content)


if __name__ == '__main__':
    data1 = get_pubdate('10', 'Cookie☆ NYN', 'cookie')
    data2 = get_pubdate('10', '俊达萌', '俊达萌')
    w_data = data1 + data2
    write_json(w_data)
