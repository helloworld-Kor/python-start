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
    last_id = 0 
    cnt = 0
    while True:
        cnt += 1
        results = []
        url = "https://api-manager.upbit.com/api/v1/notices?page=1&per_page=20&thread_name=general"
        req = requests.get(url)
        _json = req.json()
        lists=_json.get("data").get("list")[0]
        post_id = lists.get("id")
        date = lists.get("created_at")
        title = lists.get("title")
        results.append((post_id, date, title))
        print("@@@@@@@@@@@@@@@@@@@@@@@{}".format(cnt))
        if last_id != post_id:
            last_id = post_id
            print("새로운글 {}".format(results))
            URL = 'https://api.telegram.org/bot1480467875:AAFQsa0P93WmXfQ1airEjmXcSexzmrZHc-E/sendMessage?chat_id=1440556547%20&text={}'.format(results)
            requests.get(URL)
            
        time.sleep(30)   
    return results

def junggo(keyword):
    while True:
        ccnt = 1
        keyword = re.sub(" ", "%20", keyword)  # &od=1
        url = "https://apis.naver.com/cafe-web/cafe-search-api/v1.0/trade-search/all?query={}&page=1&size=30".format(
            keyword, ccnt)
        req = requests.get(url)
        _json = req.json()
        lists = _json.get("result").get("tradeArticleList")
        jungo = []
        # pprint.pprint(lists[0])
        articleId = "https://cafe.naver.com/joonggonara/"
        articleId += str(lists[0].get("articleId"))
        writeTime = lists[0].get("writeTime") / 1000
        post_id =lists[0].get("articleId")
        li = lists[0].get("productSale")
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
        
        jungo.append((post_id, str(s), cost, product, stats,juso,  articleId))
        

        URL = 'https://api.telegram.org/bot1480467875:AAFQsa0P93WmXfQ1airEjmXcSexzmrZHc-E/sendMessage?chat_id=1440556547%20&text={}'.format(jungo)
        response = requests.get(URL)
        time.sleep(10)

    return jungo

upbit()
