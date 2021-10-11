import requests

from bs4 import BeautifulSoup


KEYWORDS = {'Дизайн', 'Фото', 'Web', 'Python'}

response = requests.get('https://habr.com/ru/all/')

if not response.ok:
    raise Exception('запрос неверный')

text = response.text

soup = BeautifulSoup(text, features="html.parser")

texts = soup.find_all('article')
for article in texts:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = {h.text.strip() for h in hubs}
    # HUB = []
    # words = []
    # for h in hubs:
    #     hb = h.text.strip()
    #     HUB.append(hb)
    # #     for w in HUB:
    # #         words.append(w.split())
    # #         for elements in
    # # print(words)
    # print(HUB)
    if hubs & KEYWORDS:
       data = article.find('time').attrs.get('title')
       title = article.find('h2').find('a').find('span')
       href = article.find('h2').find('a').attrs.get('href')
       print(data, '-', title.text, '-', href)

