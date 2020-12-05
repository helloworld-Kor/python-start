import requests
from bs4 import BeautifulSoup

# ajax 통신으로 변경 됨

json = requests.get('https://www.naver.com/srchrank?frm=main').json()

ranks = json.get("data")

for r in ranks:
    rank = r.get("rank")
    keyword = r.get("keyword")
    print(rank, keyword)
