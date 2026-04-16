import os
import requests as r
import time
from tqdm import tqdm

BASE = 'https://i.nhentai.net'
HEADERS = {"User-Agent": "Mozilla/5.0",
                       "Referer": "https://nhentai.net/"}
                                        
def __download(url: str, id: str, name: str):   
    data = r.get(f'{BASE}/{url}', headers = HEADERS)
    ext = os.path.splitext(url)[1]
    with open(f'./temp_nhdl/{id}/{name+ext}', 'wb') as f:
        f.write(data.content)
        
def download_all(gallery: dict, rest: float = 2.0, retry: int = 3):
    title, pages, id = gallery['title'], gallery['pages'], gallery['id']
    if not os.path.exists('./temp_nhdl'):
        os.mkdir('./temp_nhdl')
    os.mkdir(f'./temp_nhdl/{id}')
    load_list = pages
    print(f'[Progress] Downloading "{title}"')
    for i, pic in enumerate(tqdm(pages), start = 1):
        for a in range(retry):
            try:      
                __download(pic, id, str(i))
                break
            except Exception as e:              
                time.sleep(1)
             
     
def main():
    pass
    
    
if __name__ == "__main__":
    main()