import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("https://movie.naver.com/movie/point/af/list.nhn?&page=1")

bs = BeautifulSoup(r.text, "lxml")

trs = bs.select("table.list_netizen > tbody > tr")
results = []

# print(trs[0])
for tr in trs:
    # date = tr.select("td.num > br")[0]
    titles = tr.select("td.title")
    title = titles[0].select("a")[0].text
    jumsu = titles[0].select("div.list_netizen_score > em")[0].text
    number = tr.select("td")[0].text
    author = tr.select("td.num > a.author")[0].text
    # print(date)
    results.append([number, jumsu, title, author])

for result in results:
    print(result)
    print("***"*20)

column = ["접수번호", "평점", "제목", "작성자"]

# results = get_movie_point(1, 4)

dataframe = pandas.DataFrame(results, columns=column)

print(dataframe)
dataframe.to_excel("movie.xlsx",
                   sheet_name="네이버영화",
                   header=True,
                   startrow=1)
