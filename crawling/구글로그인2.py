# 크롬 디버그모드를 통한 구글 로그인
# 참고 블로그 : https://krksap.tistory.com/1730
# 참고 블로그 : https://jakpentest.tistory.com/39

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import chromedriver_autoinstaller
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install() # 크롬 드라이버 자동 업데이트

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=chrome_options)

url = "https://analytics.google.com/analytics/web/?authuser=1#/dashboard/xSVVMpdKSZyTxqGNPJVhiw/a97177317w224305445p212665896/_u.date00=20210308&_u.date01=20210308"
browser.get(url)

print("브라우저를 실행합니다.")

browser.implicitly_wait(10)
html = browser.page_source
print("html을 불러옵니다.")

#user_total_select = browser.find_elements_by_css_selector('div#ID-layout-2 td')

soup = BeautifulSoup(html, "html.parser")

user_data_select = soup.select()