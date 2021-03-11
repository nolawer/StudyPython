# GIO 어드민에 접속하여 일자별 통계 가져오기
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

# 세션 시작하기
session = requests.session()

# 서버에 전달해 줄 data
login_info = {
    "_token" : "Lq18ocncw154NAVx1P8zJ0t6d0NjxEerEbcQ7Gv8",
    "email" : "admin@admin.com",
    "password" : "rootadmin"
}

# 서버에 로그인 정보 전달
url_login = "https://admin.globalieltsonline.com/login"
res = session.post(url_login, data=login_info)

# 메인 페이지 접속
url_home = "https://admin.globalieltsonline.com/home"
res = session.get(url_home)

# 데이터 수집
soup = BeautifulSoup(res.text, "html.parser")
print(res.text)
country = soup.select_one("div.inner h3")

print(country)




