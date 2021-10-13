import requests

import re

from bs4 import BeautifulSoup


KEYWORDS = {'дизайн', 'фото', 'web', 'python'}


def find_text(keywords):
    response = requests.get('https://habr.com/ru/all/')

    if not response.ok:
        raise Exception('запрос неверный')

    text = response.text

    soup = BeautifulSoup(text, features="html.parser")

    text = soup.find_all('article')

    for article in text:
        hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
        hubs = [h.text.strip() for h in hubs]
        previews = article.find_all(class_="article-formatted-body article-formatted-body_version-2")
        previews = [p.text.strip() for p in previews]
        titles = article.find_all(class_='tm-article-snippet__title tm-article-snippet__title_h2')
        titles = {t.text.strip() for t in titles}

        for keys in keywords:
            pattern = re.compile(f'{keys}[а-я]?', re.IGNORECASE)
            for hu in previews:
                resault = re.findall(pattern, hu)
                for element in resault:
                    new_list = []
                    new_list.append(element)
                    for e in new_list:
                        e = article.find('time').attrs.get('title')
                        title = article.find('h2').find('a').find('span')
                        href = article.find('h2').find('a').attrs.get('href')
                        print(e, '-', title.text, '-', href)



print(find_text(KEYWORDS))