import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.naver.com")

bs = BeautifulSoup(r.text, "html.parser")

lists = bs.find_all("li", {"class": "ah_item"})  # li 태그에 클래스 ah_item
# find 함수로 크롤링
# find_all (전체를 가져옴) <> find 는 첫번째 항목을 하져옴

for li in lists:
    # print(li)     li > a > span
    title = li.find("span", {"class": "ah_k"}).text  # li 밑에 있는 span 테그 가져옴
    print(title)

# select 함수로 크롤링, select 는 리스트 형식으로 리턴
lists = bs.select("li.ah_item")
# select("li.클래스명")  ex) li.a
# select("li#id명")     ex) li#b
for li in lists:
    title = li.select("span.ah_k")[0].text
    print(title)
