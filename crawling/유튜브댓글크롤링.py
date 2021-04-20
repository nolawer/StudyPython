from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


options = Options()
# options.add_argument('--start-fullscreen')
browser = webdriver.Chrome('./chromedriver_win.exe', chrome_options=options)
# browser.maximize_window()
browser.set_window_size(1400,900)

browser.implicitly_wait(5) #브라우저 로딩까지 5초 대기

url = 'https://www.youtube.com/watch?v=jXc3bAUMxLQ'
browser.get(url)

# browser.implicitly_wait(3) #브라우저 로딩까지 대기
time.sleep(3)

#------------- 키 제어 방식으로 크롤링 ---------------------

#스크롤 조금만 내리기
# browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)
# time.sleep(5)
#스크롤 끝까지 내리기
# browser.find_element_by_css_selector("html").send_keys(Keys.END)

# comment = browser.find_elements_by_css_selector("#content-text")
# idx = 0

# 키 제어로 스크롤 하며 크롤링
# while True:
#     try:
#         print(idx,"번 " + comment[idx].text)
#     except:
#         print("크롤링 끝!")
#         browser.close()
#         break
#     idx += 1
#     if idx % 20 == 0:
#         browser.find_element_by_css_selector("html").send_keys(Keys.END)
#         time.sleep(5)
#         comment = browser.find_elements_by_css_selector("#content-text")


#------------- 화면 사이즈 제어 방식으로 크롤링 ---------------------

# 스크롤 조금 내리기(바로 페이지 높이까지 스크롤 할 경우 로딩이 안되어 해당 코드 사용)
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

# 마지막 시점의 창 높이 저장
last_page_height = browser.execute_script("return document.documentElement.scrollHeight")
time.sleep(2)

# 무한 스크롤(화면 사이즈 기준 스크롤)
while True:
    # 창 높이까지 스크롤
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3)
    # 스크롤이 된 후의 창 높이를 새로운 높이로 저장
    new_page_height = browser.execute_script("return document.documentElement.scrollHeight")
    time.sleep(2.0)

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

print("스크롤 완료!")

html = browser.page_source
soup = BeautifulSoup(html, "lxml")

browser.close()

# print(soup)

comment = soup.select('#content-text')

print("파싱 완료!")

# print(comment)
for i in comment:
    print(i.text)

