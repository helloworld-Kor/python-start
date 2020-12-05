import requests
import pprint
import geohash2
import os


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
        print("{}. {} ({})".format(v, item.get("name"), item.get("description")))
    a = int(input("찾을려는 동네를 숫자로 입력하세요(숫자로만)"))
    data = _json.get("items")[a-1]
    _description = data.get("description")
    _id = data.get("id")
    _lat = data.get("lat")
    _lng = data.get("lng")
    _zoom = data.get("zoom")

    geohash = geohash2.encode(_lat, _lng, precision=5)
    # print("{}:::::::::;{}".format(geohash, keyword))
    url = "https://apis.zigbang.com/property/apartments/location/v3?e=&geohash={}&markerType=large&n=&q=type%3Dsales%2Cprice%3D0~-1%2CfloorArea%3D0~-1&s=&serviceType%5B0%5D=apt&serviceType%5B1%5D=offer&w=".format(
        geohash)
    _req_items = requests.get(url).json()
    filtereds = _req_items.get("filtered")
    bang_lists = []
    for filtered in filtereds:
        if filtered.get("id") == 23300:
            pprint.pprint(filtered)
        else:
            name = filtered.get("name") + filtered.get("real_type")
            key = filtered.get("id")
            rentPerArea = filtered.get("price").get("rent").get("perArea")
            salesPerArea = filtered.get("price").get("sales").get("perArea")
            buyangdate = filtered.get("분양년월")
            usedate = filtered.get("사용승인일")
            serviceTy = filtered.get("서비스구분")
            if rentPerArea is None or salesPerArea is None:
                result = 0
            else:
                result = salesPerArea / rentPerArea
            bang_lists.append(
                (key, name, rentPerArea, salesPerArea, result, buyangdate, usedate, serviceTy))
    Index = 1
    for bang_list in bang_lists:
        print(Index, bang_list)
        Index += 1
os.system("pause")
