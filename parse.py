
import requests
from bs4 import BeautifulSoup
import csv
import os

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
            'title': item.find('span', class_= 'news__item-content ').get_text()
        })
        
    return title

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        title = []
        title.extend(get_content(html.text))
        print(title)
    else:
        print('Error')

parse()