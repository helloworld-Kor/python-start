
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession  # 자바스크립트를 지원함


response = requests.get("https://www.naver.com")
bs = BeautifulSoup(response.text, "html.parser")  # text 파일을 파서를 통해 분석

for img in bs.select("a"):
    print(img)

# print(response)

# print(response.status_code)

# print(response.headers)

# print(response.text)
