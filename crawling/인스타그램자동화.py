from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# implictly_wait : 웹페이지가 로딩될때까지 기다리고 지정한 시간이 넘어가면 웹페이지 로딩여부와 관계없이 다음 명령어를 실행
# explicitly_wait : 필요한 그 부분이 표시될때까지 기다림
# (By.ID, ‘아이디이름’)
# (By.CLASS_NAME, ‘클래스명’)
# (By.XPATH, ‘xpath경로’)
# (By.NAME, ‘네임명’)
# (By.CSS_SELECTOR, ‘CSS셀렉터’)
# (By.PARTIAL_LINK_TEXT, ‘링크텍스트일부분’)
# (By.LINK_TEXT, ‘링크텍스트(전부일치)’)


# 크롬 드라이버 구동 -----------
options = Options()
browser = webdriver.Chrome('./chromedriver_win.exe', chrome_options=options)
browser.set_window_size(1400,900) # 크롬 드라이버 크기 조절
browser.implicitly_wait(5)

# 인스타그램 로그인 -----------
# 로그인 페이지 접속
login_url = "https://www.instagram.com/accounts/login/"
browser.get(login_url)
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "username"))) # name 값 username인 요소가 로딩될때 까지 기다림

# 아이디/패스워드 입력 후 로그인 버튼 클릭


# 인스타그램 태그 페이지 이동 -----------
# 검색하고자 하는 태그 입력
# 해당 태그의 페이지로 이동


# 인스타그램 좋아요 누르기 ------------





nolawer@naver.com
nomark08151!
https://www.instagram.com/accounts/login/