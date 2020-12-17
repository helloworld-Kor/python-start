import requests
import pprint
import geohash2
import os


def dong():

    dong = input("동이름을 입력하세요(동단위)!!!!!")
    url = "https://apis.zigbang.com/v2/search?q={}&serviceType=%EC%95%84%ED%8C%8C%ED%8A%B8".format(
        dong)

    req = requests.get(url)

    _json = req.json()
    # pprint.pprint(_json)
    result = []

    if _json.get("code") == "200":
        v = 0
        for item in _json.get("items"):
            v += 1
            print("{}. {} ({})".format(v, item.get(
                "name"), item.get("description")))
