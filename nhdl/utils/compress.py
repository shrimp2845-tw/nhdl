import os
from PIL import Image
from tqdm import tqdm

def __compress(name: str, id: str):
    img = Image.open(f'./temp_nhdl/{id}/{name}')
    img = img.resize((int(img.width*0.8), int(img.height*0.8)))
    img = img.convert("RGB")
    img.save(f'./temp_nhdl/{id}/{os.path.splitext(name)[0]}.jpg', "JPEG", quality = 60, optimize = True)
    if os.path.splitext(name)[1] == '.jpg':
        return
    os.remove(f'./temp_nhdl/{id}/{name}')
    
def compress_all(gallery: dict):
    print('[Progress] Compressing pages')
    id = gallery['id']
    pages = os.listdir(f'./temp_nhdl/{id}')
    for i in tqdm(pages):
        __compress(i, id)
    print('')
        
def main():
    pass
    
if __name__ == "__main__":
    main()