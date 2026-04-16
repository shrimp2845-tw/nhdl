from reportlab.pdfgen import canvas
from PIL import Image
import os
import shutil
from tqdm import tqdm
import re 

def __sanitize(filename: str):
    return re.sub(r'[\\/:*?"<>|]', '_', filename)

def to_pdf(name: str, gallery: dict):
    print("[Progress] Formatting into pdf")
    name = __sanitize(name)
    id = gallery['id']
    images = sorted(os.listdir(f'./temp_nhdl/{id}/'), key = lambda x: int(os.path.splitext(x)[0]))
    c = None
    for i, img_name in enumerate(tqdm(images)):      
        img = Image.open(f'./temp_nhdl/{id}/{img_name}')
        width, height = img.size
        if c is None:
            c = canvas.Canvas(name, pagesize = (width, height))
        else:
            c.setPageSize((width, height))
        c.drawImage(f'./temp_nhdl/{id}/{img_name}', 0, 0, width = width, height = height)
        c.showPage()
        img.close()
    print('')
    c.save()
    if os.path.exists(f'./temp_nhdl/{id}'):
        shutil.rmtree(f'./temp_nhdl/{id}')

def main():
    pass
    
if __name__ == "__main__":
    main()