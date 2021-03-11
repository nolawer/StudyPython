from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


# html 소스 가져오기
url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
res = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web = urlopen(res).read()

# html 분석
soup = BeautifulSoup(web, "html.parser")

# 요소추출
asset = soup.select("div.cluster div.cluster_text > a")

# 제목,URL 추출
for result in asset:
    print("title : ", result.string)
    print("url : ", result.attrs['href'])

    url_article = Request(result.attrs['href'], headers={'User-Agent': 'Mozilla/5.0'})
    web_article = urlopen(url_article).read()
    soup_article = BeautifulSoup(web_article,"html.parser")

    content = soup_article.select_one("div#articleBodyContents")

    for i in content.contents:
        i = str(i).strip()

        if i == "":
            continue
        if "본문 내용" in i:
            continue
        if " TV플레이어" in i or "// TV플레이어" in i:
            continue
        if " 기자" in i:
            continue
        if "<" in i or "[" in i or "]" in i:
            continue
        if "@" in i or "ⓒ" in i or "▶" in i:
            break
        print(i)
    print()
    print()



