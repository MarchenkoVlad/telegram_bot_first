
import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://yandex.ru/'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
          'accept': '*/*'}

HOST = 'https://yandex.ru/'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('ol', class_='list news__list').find_all('li', class_='list__item')
    
    title = []

    for item in items:
        title.append({
            'title': item.find('span', class_= 'news__item-content').get_text().replace('\xa0', ''),
            'link': item.find('a', class_='home-link list__item-content list__item-content_with-icon home-link_black_yes').get('href')
        })
    return title


def parse():
    
    html = get_html(URL)
    if html.status_code == 200:
        title = []
        title.extend(get_content(html.text))
        return title
    else:
        print('Error')