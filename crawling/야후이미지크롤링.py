from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
import os

if not os.path.exists("./이미지크롤링"):
    os.mkdir("./이미지크롤링")

keyword = input("키워드 입력 >> ")

if not os.path.exists("./이미지크롤링/{}".format(keyword)):
    os.mkdir("./이미지크롤링/{}".format(keyword))

encoded = par.quote(keyword) # 한글 --> 특수한 문자열

url = "https://images.search.yahoo.com/search/images;_ylt=Awr9IMn2k0lgMngAbQJXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p={}&fr2=piv-web&fr=yfp-t".format(encoded)

code = req.urlopen(url)
soup = BeautifulSoup(code, "html.parser")

img = soup.select("a > img")

print(img)

for i in img:
    img_url = i.attrs['data-src']
    print(img_url)
    req.urlretrieve(img_url, "./이미지크롤링/{}/{}.png".format(keyword, img.index(i)+1))
    print("{} 이미지 크롤링 완료 {}".format(keyword, img.index(i)+1))