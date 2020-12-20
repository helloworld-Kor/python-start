import requests
import pprint
import geohash2
import os


# dong = input("동이름을 입력하세요(동단위)!!!!!")
url = "https://api-manager.upbit.com/api/v1/notices?page=1&per_page=20&thread_name=general"

req = requests.get(url)

_json = req.json()
pprint.pprint(_json)
# result = []
