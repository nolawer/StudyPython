# bs를 사용하여 토큰,아이디,패스워드 데이터를 넘겨주는 방식으로 시도했으나 잘 안됨

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url_login = "https://admin.globalieltsonline.com/login"
url_home = "https://admin.globalieltsonline.com/home"

session = requests.session()

html_login = requests.get(url_login)

soup = BeautifulSoup(html_login.text, "html.parser")
auth = soup.find_all('input', attrs={'type':'hidden'})

auth_name = soup.select('input')[0]['name']
auth_value = soup.select('input')[0]['value']

header = {
    'Referer' : 'https://admin.globalieltsonline.com/login',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

data = {
     auth_name: auth_value,
     'email': 'admin@admin.com',
     'password': 'rootadmin'
}

response = session.post(url_login, headers=header, data=data)

# print(response.headers)
# print(session.cookies.get_dict())

res = session.get(url_home)
soup = BeautifulSoup(res.content, "html.parser")

data = soup.select('html')

print(data)


# response = requests.post(url_login, headers=header, data=data)
#
# response_home = session.get(url_home, headers=header, data=data)
#
# soup = BeautifulSoup(response_home.text, "html.parser")
#
# print(soup)

