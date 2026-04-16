import os
import sys
from .utils import download_all, to_pdf, get_info, compress_all
import re
import shutil


VERSION = '0.2.1'


def __extract_id(url: str) -> str:
    print('[API] Extracting url')
    pattern = r"^https://nhentai\.net/g/(\d+)/?$"
    match = re.match(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError('invalid url')
    
def download(book: str, compress: bool = False, rest: float = 2.0, retry: int = 3):
    """
    Download an nhentai doujin
    book -> url or id
    compress -> whether to compress the file
    rest -> time interval between downloading two pages
    retry -> times to retry if disconnect while downloading a page
    """
    print(f'[API] Program start up ({VERSION})')
    if not book.isdigit():
        id = __extract_id(book)
    else:
        id = book
    try:
        gallery_info = get_info(id)
        download_all(gallery_info, rest, retry)
        if compress:
            compress_all(gallery_info)
        to_pdf(f'{gallery_info["title"]}.pdf', gallery_info)
        print(f'[API] Successfully downloaded "{gallery_info["title"]}.pdf"')
    except Exception as e:
        if os.path.exists(f'./temp_nhdl/{id}'):
            shutil.rmtree(f'./temp_nhdl/{id}')
        print(f'\033[31m [ERROR] {e} \033[0m')
        sys.exit()
           
def main():
    pass
    
if __name__ == "__main__":
    main()