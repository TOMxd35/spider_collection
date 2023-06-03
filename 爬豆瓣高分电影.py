import requests
import bs4
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"}
res = requests.get("https://movie.douban.com/top250?start=25&filter=",headers=headers)
soup=bs4.BeautifulSoup(res.text,"html.parser")
targets = soup.find_all("div",class_="hd")
for each in targets:
    print(each.a.span.text)

