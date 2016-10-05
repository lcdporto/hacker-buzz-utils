import os
import sys
import requests
import shutil
import argparse

from urllib.parse import urlparse

IMAGE_DIR = '/app/images'

def get_filename(url):
    """
    Returns last path segment to be used as filename
    """
    parsed = urlparse(url)
    return parsed.path.split('/')[-1:][0]

def download_image(url, folder=IMAGE_DIR, filename=None):
    """
    Downloads an image from an url
    """
    if not filename:
        filename = get_filename(url).strip()

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(IMAGE_DIR, filename), 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)

def download_from_file(f):
    """
    Reads urls from a file and downloads
    """
    with open(f, 'r') as file:
        for url in file:
            download_image(url)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hacker Buzz Utils')
    parser.add_argument('-f', '--file', help='File with list of images urls to download.')
    args = parser.parse_args()

    if args.file:
        download_from_file(args.file)
    else:
        try:
            url = sys.argv[1]
            download_image(url)
        except IndexError:
            print('Please provide the image url or a file with a list of urls.')
            sys.exit()
