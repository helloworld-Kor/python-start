import requests
from bs4 import BeautifulSoup
import re

"리눅스 magent:?xt="


def search_google(keyword, start_page, end_page=None):
    url = "https://www.google.com/search?q={0}+magnet%3A%3Fxt%3D&oq={0}+magnet%3A%3Fxt%3D&start={1}".format(
        keyword, start_page)
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36,gzip(gfe)"}
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, "lxml")

    # 기존의 코드에서 div 단계가 하나 생략 되었습니다.
    links = bs.select("div.g > div.rc > div.r > a")

    results = []

    if end_page is None:
        # 페이징 될 경우 검색결과 약 100,000개 중 2페이지 (0.50초) 이런 형식으로 결과가 출력됩니다.
        # 그래서 "검색결과 약" 과 "개" 사이의 결과 갯수를 파싱하기 위해서 아래처럼 작업합니다.
        parse_text_1 = "검색결과 약"
        parse_text_2 = "개"
        # 최초의 검색 결과를 div 태그의 ID가 result-stats 인 요소의 text 값을 구합니다.
        # 기존의 코드에서 ID 이름이 변경되었습니다.
        text = bs.select("div#result-stats")[0].text

        # "검색결과 약" 에서부터 맨 뒤까지 문자열을 슬라이싱 해서 text에 다시 담습니다.
        text = text[text.find(parse_text_1) + len(parse_text_1):]
        # "검색결과 약" 이 제거된 text 에서 "개" 를 찾아 그곳까지 슬라이싱해서 다시 text에 담습니다.
        text = text[:text.find(parse_text_2)]
        # 최종적으로 , 를 제거하고 공백제거 후 counts 변수에 담으면 숫자만 담겨 집니다.
        counts = text.replace(",", "").strip()

        # 이전코드
        # counts = bs.select("div#result-stats")[0].text.replace("검색결과 약", "").replace("개", "").replace(",", "").split("(")[0].strip()

        print(counts)
        end_page = int(int(counts) / 10)
        if end_page > 20:
            end_page = 20

    for a in links:
        href = a["href"]
        text = a.select("h3")
        if len(text) <= 0:
            continue
        title = text[0].text

        try:
            r = requests.get(href)
            bs = BeautifulSoup(r.text, "lxml")
            magnets = bs.find_all("a", href=re.compile(r'magnet:\?xt=*'))

            if len(magnets) > 0:
                magnet = magnets[0]["href"]
                results.append((title, magnet))
        except:
            pass
    if start_page < end_page:
        start_page += 10
        results.extend(search_google(keyword, start_page, end_page=end_page))

    return results


results = search_google("리눅스", 1)

for r in results:
    print(r)
