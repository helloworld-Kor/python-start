import requests
import pprint
import geohash2
import os
import time


def upbit():

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

    return results
# print(results[0])


def zipbang(context):
    print("**"*20)
    dong = context
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
            result.append((v, item.get("name"), item.get("description"), item.get(
                "id"), item.get("lat"), item.get("lng"), item.get("zoom")))
    return result


if __name__ == "__main__":
    # print(zipbang("대치동"))
    result = zipbang("대치동")
    print(result[0])
    # for i in result:
    #     print(i)

    # for i in range(len(result)):
    #     print(i)
