# 크롬 디버그모드를 통한 구글 로그인
# 참고 블로그 : https://krksap.tistory.com/1730
# 참고 블로그 : https://jakpentest.tistory.com/39

# 크롬 디버깅모드 열기
# 윈도우 : Win + r(실행창)
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"
# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"
# 맥 : 터미널
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"

# 크롬 브라우저 열린 후 사용하고자 하는 계정으로 로그인

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import chromedriver_autoinstaller
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install() # 크롬 드라이버 자동 업데이트

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=chrome_options)

url = "https://ads.google.com/aw/overview?ocid=413354561&euid=232781013&__u=7146045037&uscid=413354561&__c=8361127289&authuser=1&subid=kr-ko-ha-aw-bk-a-h00!o3~EAIaIQobChMIi5qEgPDL6AIVzKmWCh0sAg9EEAAYASAAEgI61_D_BwE~105136867328~kwd-516691694765~7918679986-4279865"

# url = "https://www.naver.com/"
browser.get(url)
print("브라우저를 실행합니다.")
browser.implicitly_wait(10) # 브라우저 로딩완료까지 10초 대기
print("html을 불러옵니다.")

# element = browser.find_element_by_id("galaxyIframe")
# browser.switch_to.frame(element)
# browser.switch_to.frame("galaxy")

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

print(soup)