import requests
from bs4 import BeautifulSoup


dataLink = []

url         = 'https://www.tokopedia.com/sepatulokalid/product?perpage=5'
user_agent  = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'}

request = requests.get(url, headers=user_agent)

soup = BeautifulSoup(request.content, "html.parser")

page = soup.find('div', 'css-8atqhb')
produk = page.find_all('div', 'css-1sn1xa2')
for p in produk:
    judul = p.find('div', 'css-zimbi')
    link = judul.find('a')['href']
    dataLink.append(link)

print(dataLink)
for d in dataLink:
    req = requests.get(d, headers=user_agent)
    print(req)