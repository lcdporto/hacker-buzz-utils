import os
import sys
import requests
import shutil
import argparse

from urllib.parse import urlparse
from requests import exceptions

IMAGE_DIR = '/app/images'

def get_filename(url):
    """
    Returns last path segment to be used as filename
    """
    parsed = urlparse(url)
    return parsed.path.split('/')[-1:][0]

def download_image(url, directory, filename=None):
    """
    Downloads an image from an url
    """
    if not os.path.exists(directory):
        os.mkdir(directory)

    if not filename:
        filename = get_filename(url).strip()

    try:
        response = requests.get(url, stream=True, timeout=5)
        if response.status_code == 200:
            with open(os.path.join(directory, filename), 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
    except exceptions.ConnectionError:
        sys.stdout.write("Connection problem skipping: %s   \r" % (url) )
    except exceptions.Timeout:
        sys.stdout.write("Connection timeout skipping: %s   \r" % (url) )
    except exceptions.TooManyRedirects:
        sys.stdout.write("Too many redirects skipping: %s   \r" % (url) )

def download_from_file(f, directory):
    """
    Reads urls from a file and downloads
    """
    with open(f, 'r', encoding='utf8') as file:
        for url in file:
            download_image(url, directory)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hacker Buzz Utils')
    parser.add_argument('-f', '--file', help='File with list of images urls to download.')
    parser.add_argument('-d', '--directory', default=IMAGE_DIR, help='Where to store the images, a subdirectory of IMAGE_DIR, created if does not exist.')
    args = parser.parse_args()

    if args.directory != IMAGE_DIR:
        directory = os.path.join(IMAGE_DIR, args.directory)
    else:
        directory = IMAGE_DIR

    if args.file:
        download_from_file(args.file, directory)
    else:
        try:
            url = sys.argv[1]
            download_image(url, directory)
        except IndexError:
            print('Please provide the image url or a file with a list of urls.')
            sys.exit()
