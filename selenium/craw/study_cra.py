from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests


# def get_news():


driver = webdriver.Chrome()
driver.get("http://hira.kacnet.co.kr/new_main/index.php")

driver.find_element_by_xpath(
    """//*[@id="wrap"]/div[2]/div[1]/ul/li[5]/a""").click()

time.sleep(1)
driver.find_element_by_xpath("""//*[@id="id"]""").send_keys('20180283')
time.sleep(1)
driver.find_element_by_xpath("""//*[@id="passwd"]""").send_keys('20180283')

driver.find_element_by_xpath(
    """//*[@id="form2"]/a[1]""").click()
time.sleep(2)
driver.find_element_by_xpath(
    """//*[@id="wrap"]/div[2]/div[1]/ul/li[2]/a""").click()
time.sleep(2)
driver.find_element_by_xpath(
    """//*[@id="wrap"]/div[2]/div[1]/ul/li[2]/ul/li[4]/a""").click()

# 페이지 소스 가져오기

time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
trs = soup.select("#tab3 > table > tbody > tr")
# tab3 > table > tbody > tr:nth-child(2) > td:nth-child(4) > span
print("***********"*10)
# print(trs[1].select("td")[0].text)
# print(trs[1].select("td")[0].text)
study_lists = []
cnt = 0
for tr in trs:
    if cnt != 0:
        td = tr.select("td")
        span = tr.select("td > span.col07")
        title = tr.select("td.course > a")
        study_lists.append(
            (td[0].text, span[0].text, title[0].text))
    cnt = cnt + 1

    # print(len(study_lists))
# jumping(study_lists)


# def jumping(study_lists):
#     for study in study_lists:
#         if study[1] != '수료':
# tab3 > table > tbody > tr:nth-child(2) > td:nth-child(6)
# tab3 > table > tbody > tr:nth-child(3) > td:nth-child(6) > a
# tab3 > table > tbody > tr:nth-child(4) > td:nth-child(6) > a
# print(td.text)
# tab3 > table > tbody > tr:nth-child(2) > td:nth-child(4) > span
# tab3 > table > tbody > tr:nth-child(2) > td.course > a
