import requests
import pprint
import geohash2
import os
import time


# dong = input("동이름을 입력하세요(동단위)!!!!!")

url = "https://api-manager.upbit.com/api/v1/notices?page=1&per_page=20&thread_name=general"

req = requests.get(url)

_json = req.json()
# pprint.pprint(_json)
# result = []

results = []

if str(_json.get("success")) == "True":
    for lists in _json.get("data").get("list"):
        if "에어" in str(lists.get("title")):
            id_ = lists.get("id")
            date = lists.get("created_at")
            title = lists.get("title")
            results.append((id_, date, title))
# print(lists.get("created_at"))


# print(results[0])
for result in results:
    print(result)

# if __name__ == "__main__":
#     # btn_shw()
