import requests
from bs4 import BeautifulSoup
import re


def magnetSearch(keyword, startpage):
    start = ((startpage-1) * 10) + 10
    keyword = re.sub(" ", "+", keyword)  # &od=1
    result = ""
    for i in range(0, start, 10):
        # print("{}*********{}페이지입니다.".format(i, int(i/10+1)))
        url = "https://www.google.com/search?q={}+magnet:%3Fxt%3D&start={}".format(
            keyword, i)
        # print(url)
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        r = requests.get(url, headers=header)
        bs = BeautifulSoup(r.text, "lxml")
        links = bs.select("#rso")
        mapping = []
        for link in links:
            yur = link.select("div.g")
            for a in yur:
                newurl = a.select("div.yuRUbf > a")[0]['href']
                title = a.select("div.yuRUbf > a > h3")[0].text
                try:
                    r = requests.get(newurl)
                    bs = BeautifulSoup(r.text, "lxml")
                    magnets = bs.find_all(
                        "a",  href=re.compile(r'magnet:\?xt=*'))
                    if len(magnets) > 0:
                        magnet = magnets[0]["href"]
                        mapping.append(
                            (title, magnet, newurl))
                except:
                    pass
        for map in mapping:
            result += str(map)
            result += "\n"
    return result


if __name__ == "__main__":
    keyword = input("마그넷 검색어를 입력하시오 >>>>>>>>")
    startpage = int(input("페이지 수를 정하세요 >>>>>>>>"))
    result = magnetSearch(keyword, startpage)
    print(result)


# #print("***************{}번째 페이지***********".format(i+1))
