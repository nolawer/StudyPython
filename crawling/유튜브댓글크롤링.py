from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('--start-fullscreen')
browser = webdriver.Chrome('./chromedriver_win.exe', chrome_options=options)
browser.maximize_window()

browser.implicitly_wait(5) #브라우저 로딩까지 5초 대기

url = 'https://www.youtube.com/watch?v=MSoBQSoiIT8'
browser.get(url)

browser.implicitly_wait(2) #브라우저 로딩까지 5초 대기

#스크롤 조금만 내리기
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)
#스크롤 끝까지 내리기
# browser.find_element_by_css_selector("html").send_keys(Keys.END)

browser.implicitly_wait(4)

comment = browser.find_elements_by_css_selector("yt-formatted-string#content-text")

idx = 0

while True:
    print(comment[idx].text)
    idx += 1

    if idx % 20 == 0:
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(3)
        comment = browser.find_elements_by_css_selector("yt-formatted-string#content-text")

