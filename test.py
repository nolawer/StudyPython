from urllib import response
import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    tip = soup.select_one('ul.keyword_challenge_list._au_list')
    
    title = tip.select_one('li > div.content_area > div.user_box > div.info_group > div.group_inner > a.name')
    
    print(title.get_text())

else :
    print(response.status_code)
    
    
    
    
    