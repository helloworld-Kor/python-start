import requests
from bs4 import BeautifulSoup


url = "https://search.naver.com/search.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B0%95%EC%A2%8C&nso=&where=blog&sm=tab_viw.all"
r = requests.get(url)
bs = BeautifulSoup(r.text, "lxml")

result = []

lis = bs.select("li.bx")

# print(lis[0])

# for li in lis:
for li in lis:
    div = li.select("div.api_ani_send")[0]
    ass = div.select("a")[4]

    print(ass.text)
    print("**********"*10)
