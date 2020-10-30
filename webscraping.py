import requests
from bs4 import BeautifulSoup



resp = requests.get('https://www.moviebuff.com/directory/movies?language=242&page=1&sort=asc&year=2020')
#res = requests.get('https://learncodeonline.in')

print(resp)


jsoup = BeautifulSoup(resp.content)
div = jsoup.find('div', attrs = {'class': 'full-container directory'})
for row in div.find_all('div', attrs={'class': "row filter-row"}):
    row.decompose()

for row in div.find_all('div', class_='row'):
    print(row)
    break