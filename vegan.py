import requests
from bs4 import BeautifulSoup


def get_recipes(q):
    url = 'https://tudoreceitas/pesquisa/q/{}/alimentacion_veganos/1'.format(q)
    res = requests.get(url)
    if res.status_code != 200:
        return
    return parse(res.content)


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    results = soup.find_all('div', {'class': 'resultado link'})
    return [{'titulo': i.find('a').text,
             'intro': i.find('div', {'class': 'intro'}),
             'link': i.find('a')['href']} for i in results]
