import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool

def get_page(offset):
    params = {
        'format' :'json',
        'keyword' : '街拍',
        'autoload': 'true',
        'count' :'20',
        'cur_tab' : '1',
        'from':'search_tab',
        'pd':'synthesis',
        'offset':offset
     }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images:
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get('https:' + item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download',file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool()
    groups = [x * 20 for x in range(GROUP_START, GROUP_END)]
    pool.map(main,groups)
    pool.close()
    pool.join()

