from datetime import datetime
import io
import sys
import re
from bs4 import BeautifulSoup
import requests
import pprint
import geohash2
import os
import time


def upbit():
    url = "https://api-manager.upbit.com/api/v1/notices?page=1&per_page=20&thread_name=general"
    req = requests.get(url)
    _json = req.json()

    results = []

    if str(_json.get("success")) == "True":
        for lists in _json.get("data").get("list"):
            if "에어" in str(lists.get("title")):
                id_ = lists.get("id")
                date = lists.get("created_at")
                title = lists.get("title")
                results.append((id_, date, title))

    return results


def zipbang(context):
    dong = context
    url = "https://apis.zigbang.com/v2/search?q={}&serviceType=%EC%95%84%ED%8C%8C%ED%8A%B8".format(
        dong)

    req = requests.get(url)
    _json = req.json()
    result = []

    if _json.get("code") == "200":
        v = 0
        for item in _json.get("items"):
            v += 1
            result.append((v, item.get("name"), item.get("description")))
    return result


def zipbangFinal(context, index):
    url = "https://apis.zigbang.com/v2/search?q={}&serviceType=%EC%95%84%ED%8C%8C%ED%8A%B8".format(
        context)
    req = requests.get(url)

    _json = req.json()
    result = []

    if _json.get("code") == "200":
        v = 0
        for item in _json.get("items"):
            v += 1
            # print("{}. {} ({})".format(v, item.get(
            #     "name"), item.get("description")))
        a = index
        data = _json.get("items")[a-1]
        _description = data.get("description")
        _id = data.get("id")
        _lat = data.get("lat")
        _lng = data.get("lng")
        _zoom = data.get("zoom")

        geohash = geohash2.encode(_lat, _lng, precision=5)
        url = "https://apis.zigbang.com/property/apartments/location/v3?e=&geohash={}&markerType=large&n=&q=type%3Dsales%2Cprice%3D0~-1%2CfloorArea%3D0~-1&s=&serviceType%5B0%5D=apt&serviceType%5B1%5D=offer&w=".format(
            geohash)
        _req_items = requests.get(url).json()
        filtereds = _req_items.get("filtered")
        bang_lists = []
        for filtered in filtereds:
            if filtered.get("id") == 23300:
            else:
                name = filtered.get("name") + filtered.get("real_type")
                key = filtered.get("id")
                rentPerArea = filtered.get("price").get("rent").get("perArea")
                salesPerArea = filtered.get(
                    "price").get("sales").get("perArea")
                buyangdate = filtered.get("분양년월")
                usedate = filtered.get("사용승인일")
                serviceTy = filtered.get("서비스구분")
                if rentPerArea is None or salesPerArea is None:
                    result = 0
                else:
                    result = salesPerArea / rentPerArea
                bang_lists.append(
                    (key, name, rentPerArea, salesPerArea, result, buyangdate, usedate, serviceTy))
    return bang_lists

# magnetSearch()  크롤링 안에 크롤링을 하는 거라서 페이지는 3로 고정시킴


def magnetSearch(keyword):
    start = ((3-1) * 10) + 10
    keyword = re.sub(" ", "+", keyword)  # &od=1
    result = ""
    for i in range(0, start, 10):
        url = "https://www.google.com/search?q={}+magnet:%3Fxt%3D&start={}".format(
            keyword, i)
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


# 텔레그램 속도가 느려서 30개로 한정


def junggo(keyword):
    ccnt = 30
    keyword = re.sub(" ", "%20", keyword)  # &od=1
    url = "https://apis.naver.com/cafe-web/cafe-search-api/v1.0/trade-search/all?query={}&page=1&size=30".format(
        keyword, ccnt)
    req = requests.get(url)
    _json = req.json()
    lists = _json.get("result").get("tradeArticleList")
    jungo = []
    for li in lists:
        articleId = "https://cafe.naver.com/joonggonara/"
        articleId += str(li.get("articleId"))
        writeTime = li.get("writeTime") / 1000
        li = li.get("productSale")
        cost = li.get("cost")
        product = li.get("productName")
        stats = li.get("saleStatus")
        juso = ""
        s = datetime.fromtimestamp(writeTime)
        for region in li.get("regionList"):
            # cnt += 1
            juso = str(region['regionName1'])
            juso += " " + str(region['regionName2'])
            juso += " "+str(region['regionName3'])
        jungo.append(
            (str(s), cost, product, stats, juso, articleId))
    return jungo


if __name__ == "__main__":
    keyword = input("찾고싶은 물건을 말하시오::::::::::::::>")
    # ccnt = input("몇개의 물량을 보시겠습니까:::::::::::>")
    result = magnetSearch(keyword)
    for i in result:
        print(i)
