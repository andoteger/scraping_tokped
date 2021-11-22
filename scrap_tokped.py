import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.tokopedia.com/sepatulokalid/product/page/'
user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'}

write = csv.writer(open('hasil.xlsx', 'w', newline=''))
header = ['', 'nama', 'deskripsi', 'kategori', 'berat', 'minimal pesan', 'nomor etalase', 'waktu proses order', 'kondisi', 'gambar1', 'gambar2', 'gambar3', 'gambar4', 'gambar5', 'url1', 'url2', 'ul3', 'sku name', 'status', 'jumlah stok', 'harga', 'asuransi']
write.writerow(header)

for halaman in range(10, 12):
    req = requests.get(url+str(halaman)+'?perpage=10', headers=user_agent)
    print("halaman ke: ", halaman, req)
    soup = BeautifulSoup(req.content, "html.parser")
    semuaProduk = soup.find('div', 'css-tjjb18')
    produk = semuaProduk.find_all('div', 'css-1sn1xa2')
    for l in produk:
        link = l.find('div', 'css-zimbi')
        linkItem = link.find('a')['href']
        req1 = requests.get(linkItem, headers=user_agent)
        print(req1, linkItem)
        soup1 = BeautifulSoup(req1.content, "html.parser")
        # ==========================================================
        container = soup1.find(id='main-pdp-container')
        # nama produk
        namaProduk = container.find('h1', 'css-1wtrxts').get_text()
        # deskripsi
        deskPro = container.find('div', 'css-1k1relq').get_text()

        detail  = container.find('ul', 'css-1ijyj3z e1iszlzh2')
        det     = detail.find_all('li', 'css-1dmo88g')
        # kategori
        kategori= det[2].find('a').get_text()
        # berat
        berat   = det[1].find('span', 'main').get_text().replace(' Gram', '').replace('.', '')
        # minimal order
        minPesan= 1
        # kondisi
        kondisi = det[0].find('span', 'main').get_text()
        # gambar
        gambar1 = container.find('div', 'css-1y5a13')
        # link gambar1
        gambar  = gambar1.find('img')['src'].replace('?ect=4g', '')
        # harga
        harga   = container.find('div', 'price').text.replace('Rp', '').replace('.', '')
        data = [
            '',
            namaProduk,
            deskPro,
            kategori,
            berat,
            minPesan,
            '',
            '',
            kondisi,
            gambar,
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            'Nonaktif',
            '100',
            harga,
            'ya'
        ]
        write = csv.writer(open('hasil.xlsx', 'a', newline=''))
        write.writerow(data)