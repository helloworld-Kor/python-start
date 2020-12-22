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
def bithumb():
    last_id = "" 
    cnt = 0
    while True:
        cnt += 1 
        # results = []
        url = "https://cafe.bithumb.com/view/boards/43"
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")
        links = bs.select("#dataTables > tbody > tr:nth-child(5) > td.invisible-mobile.small-size")
        link = links[0].text
        results = bs.select("#dataTables > tbody > tr:nth-child(5) > td.one-line > a")
        result = results[0].text
        print(link)
        print(result)
        post_id = link
        if last_id != post_id:
            last_id = post_id
            print("새로운글 {}".format(result))
            URL = 'https://api.telegram.org/bot1480467875:AAFQsa0P93WmXfQ1airEjmXcSexzmrZHc-E/sendMessage?chat_id=1440556547%20&text={}'.format(result)
            requests.get(URL)
        
        time.sleep(10)   
    # return results
bithumb()
