import os
import sys
import requests
import shutil
from urllib.parse import urlparse

IMAGE_DIR = '/app/images'

def get_filename(url):
    """
    Returns the last path segment to be used as filename
    """
    parsed = urlparse(url)
    return parsed.path.split('/')[-1:][0]

def download_image(url, folder=IMAGE_DIR, filename=None):
    """
    Downloads an image from an url
    """
    if not filename:
        filename = get_filename(url)
        
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(IMAGE_DIR, filename), 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)  

if __name__ == '__main__':
    try:
        url = sys.argv[1]
        download_image(url)
    except IndexError:
        print('Provide the image url...')
        exit(1)

    

