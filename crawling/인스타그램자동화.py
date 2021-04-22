from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random

# implictly_wait : 웹페이지가 로딩될때까지 기다리고 지정한 시간이 넘어가면 웹페이지 로딩여부와 관계없이 다음 명령어를 실행
# explicitly_wait : 필요한 그 부분이 표시될때까지 기다림
# (By.ID, ‘아이디이름’)
# (By.CLASS_NAME, ‘클래스명’)
# (By.XPATH, ‘xpath경로’)
# (By.NAME, ‘네임명’)
# (By.CSS_SELECTOR, ‘CSS셀렉터’)
# (By.PARTIAL_LINK_TEXT, ‘링크텍스트일부분’)
# (By.LINK_TEXT, ‘링크텍스트(전부일치)’)


# 검색할 해시태그 입력 -----------
hash_tag = input("검색할 해시태그를 입력해주세요 >>> ")

# 크롬 드라이버 구동 -----------
options = Options()
browser = webdriver.Chrome('./chromedriver_win.exe', chrome_options=options)
browser.set_window_size(1400,900) # 크롬 드라이버 크기 조절
browser.implicitly_wait(5)

# 인스타그램 로그인 -----------
# 로그인 페이지 접속
login_url = "https://www.instagram.com/accounts/login/"
browser.get(login_url)
# WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "username"))) # name 값 username인 요소가 로딩될때 까지 기다림
time.sleep(3)

# 아이디/패스워드 입력 후 로그인 버튼 클릭
user_id = "nolawer@naver.com"
user_pw = "nomark08151!"

browser.find_element_by_name("username").send_keys(user_id)
time.sleep(1)
browser.find_element_by_name("password").send_keys(user_pw)
time.sleep(1)
browser.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF").click()
time.sleep(3)

# 인스타그램 태그 페이지 이동 -----------
# 검색하고자 하는 태그의 페이지 이동
tag_url = "https://www.instagram.com/explore/tags/" + hash_tag
browser.get(tag_url)
# WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "div._9AhH0"))) # class 값 div._9AhH0인 요소(사진)가 로딩될때 까지 기다림
browser.implicitly_wait(7) #브라우저 로딩까지 대기

# 첫번째 사진 클릭
browser.find_element_by_css_selector("div._9AhH0").click()
time.sleep(3)

# 게시물 좋아요 누르기 ---------------
# 좋아요 판단 후 클릭, 다음페이지 버튼 클릭

idx = 0

while True:
    like = browser.find_element_by_css_selector("span.fr66n svg._8-yf5") # 좋아요 요소 선택
    like_value = like.get_attribute("aria-label") # 좋아요/좋아요취소 값 가져오기
    next_button = browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow") # 다음페이지 버튼 요소 선택

    idx += 1

    if like_value == "좋아요": # 좋아요 버튼이 안눌러져 있다면
        like.click() # 좋아요 클릭
        time.sleep(random.randint(2,6) + random.random()) # randint 랜덤 정수 + random 0~1 소수
        next_button.click() # 다음페이지 클릭
        time.sleep(random.randint(2, 6) + random.random())
        print("좋아요 클릭", idx)
    elif like_value =="좋아요 취소": # 좋아요 버튼이 눌러져 있다면
        next_button.click()  # 다음페이지 클릭
        time.sleep(random.randint(2, 6) + random.random())