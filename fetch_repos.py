import csv
from time import sleep
import requests
from bs4 import BeautifulSoup


repos = []
page_num = 1
max_repos = 2950


search_url = 'https://github.com/search?q=fork%3A0&repo=&langOverride=&start_value={page_num}&type=Repositories&language=Python'


def get_repos_from_html(html):
    soup = BeautifulSoup(html)
    results = soup.find_all('div', {'class': 'result'})
    repos = []

    for res in results:
        repos.append(tuple(res.a.string.split(' / ')))

    return repos


print 'Starting'


while len(repos) < max_repos:
    print '  getting page {page_num}'.format(page_num=page_num)
    response = requests.get(search_url.format(page_num=page_num))
    repos += get_repos_from_html(response.text)
    page_num += 1

    print '  Got %s' % len(repos)
    sleep(5)


print 'Done'


with open('data/repos-all.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(repos)
