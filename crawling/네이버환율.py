#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url).read().decode('euc-kr')

soup = BeautifulSoup(res,"html.parser")

title = soup.select("ul#exchangeList span.blind")
price = soup.select("ul#exchangeList span.value")

for i in range(0,len(price)):
    print(title[i].string)
    print(price[i].string)




