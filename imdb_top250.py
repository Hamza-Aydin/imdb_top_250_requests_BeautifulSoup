import requests
from bs4 import BeautifulSoup

k=float(input("Görmek İsteğiniz Minumum Puanı Giriniz:"))
url="https://www.imdb.com/chart/top/"

a=requests.get(url)

html_içeriği=a.content

b=BeautifulSoup(html_içeriği,"html.parser")

isimler=b.findAll("td",{"class":"titleColumn"})
puanlar=b.findAll("td",{"class":"ratingColumn imdbRating"})

#print(len(isimler),len(puanlar)) (250/250)

for i,j in zip(isimler,puanlar):
    i=i.text
    j=j.text

    i=i.strip()
    i=i.replace("\n","")
    j = j.strip()
    j= j.replace("\n", "")

    if float(j)>k:
        print("Filmin Numarası ve İsmi:",i)
        print("Filmin IMDb Puanı:",j)




