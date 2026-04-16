## About

- **Author:** shrimp2845  
- **Version:** 0.2.0  
- **License:** MIT

**nhdl** is a lightweight Python tool for downloading galleries from nhentai and converting them into PDF files.

This project is designed for learning purposes.(No one is going to believe me though XD)

## Dependencies

This project uses the following open-source libraries:

- [requests](https://github.com/psf/requests)
- [tqdm](https://github.com/tqdm/tqdm)
- [Pillow](https://github.com/python-pillow/Pillow)
- [reportlab](https://www.reportlab.com/)

## Feature 
- Downloading by gallery ID or URL
- Progress display using tqdm
- Converting images into a PDF
- Optional compression to reduce file size

## Installation & Usage

### Install
Requires Python 3.8+
```bash
pip install nhdl
```
### Usage
```bash
python -c "from nhdl import download; download('id or url')"
```

## Docs

```
methods
----------------------
download(book, compress = False, rest=2.0, retry=3)
Download a nhentai doujin from url or id
book -> url or id
rest -> optional arg, time interval between downloading two pages
retry -> optional arg, times to retry if disconnect while downloading a page

```





