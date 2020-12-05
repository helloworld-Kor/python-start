import requests
import pprint
import geohash2
import pprint

keyword = "반곡동"
url = "https://apis.zigbang.com/search?q={}".format(keyword)

req = requests.get(url)

_json = req.json()
# pprint.pprint(_json)
result = []

if _json.get("code") == "200":
    data = _json.get("items")[0]
    _description = data.get("description")
    _id = data.get("id")
    _lat = data.get("lat")
    _lng = data.get("lng")
    _zoom = data.get("zoom")

    geohash = geohash2.encode(_lat, _lng, precision=5)
    print(geohash)
    url = "https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={}&rent_gteq=0&sales_type_in=전세%7C월세&service_type_eq=원룸".format(
        geohash)
    _req_items = requests.get(url).json()

    # json 데이터에서 items 값만 저장합니다.
    # items 값은 실제 매물 데이터의 인덱스 값입니다.
    _items = _req_items.get("items")

    # 위에서 취한 json 형태의 items 목록을
    # 파이썬 리스트 형태로 저장합니다.
    item_ids = []
    for item in _items:
        item_ids.append(item.get("item_id"))

    # 위에서 저장한 list 의 100개만
    # items_ids 라는 키의 값으로 설정합니다.
    # 최종적으로 이 값을 직방 api 에 요청합니다.
    items = {"item_ids": item_ids[:100]}
    # print(items)
    # 위에서 만든 items_ids: [매물인덱스] 를 아래 주소로 쿼리 한 후 json 형태로 받습니다.
    _results = requests.post(
        'https://apis.zigbang.com/v2/items/list', data=items).json()

    # pprint.pprint(_results)
