from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 크롬창 열기

# 헤드리스 모드
# opt = webdriver.ChromeOptions()
# opt.add_argument("headless")
# browser = webdriver.Chrome("./chromedriver", options=opt)

# 일반모드
# options = Options()
# options.add_argument('--start-fullscreen')
# browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
browser = webdriver.Chrome('./chromedriver.exe')
# browser.maxmize_window()
browser.implicitly_wait(5)

# 로그인 페이지 접근
url_login = "https://admin.globalieltsonline.com/login"
browser.get(url_login)
print("GIO 어드민 로그인 페이지에 접근합니다.")

# 로그인
USER = "admin@admin.com"
PASS = "rootadmin"
e = browser.find_element_by_id("email") #이메일 영역 선택
e.clear() # 해당 칸의 내용을 지움
e.send_keys(USER) # 계정 입력
e = browser.find_element_by_id("password")
e.clear()
e.send_keys(PASS)
browser.find_element_by_css_selector(".login-box-body button").click() # 버튼 선택
print("로그인 버튼을 클릭합니다.")

sign_country = browser.find_elements_by_css_selector("div.card-body tbody td:nth-child(1)")
sign_count = browser.find_elements_by_css_selector("div.card-body tbody td:nth-child(2)")

print("요소를 불러옵니다.")

signup = {}

for i in sign_country:
    signup['country'] = i.text

for i in sign_count:
    signup['count'] = i.text

browser.close()