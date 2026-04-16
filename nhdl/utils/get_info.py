import requests as r
import json

BASE = 'https://nhentai.net/api/v2/galleries'

def __get_dict(id: str) -> dict:
    if not id.isdigit():
        raise ValueError('invalid id')
    headers = {'User-Agent': 'nhdl/https://github.com/shrimp2845-tw/nhdl'}
    data = r.get(f'{BASE}/{str(id)}', headers = headers)
    return data.json()

def get_info(id: str) -> dict:
    gallery = __get_dict(id)
    info = {'title' : gallery['title']['pretty'],
            'pages' :  [i['path'] for i in gallery['pages']],
            'id' : str(gallery['id'])}
    print(f'[Progress] Getting info for "{info["title"]}"')
    return info
    
def main():
    pass
    
if __name__ == "__main__":
    main()