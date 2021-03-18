from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def adminCrwling():

    global start_date
    global end_date

    # 크롬창 열기

    # 헤드리스 모드
    opt = webdriver.ChromeOptions()
    opt.add_argument("headless")
    browser = webdriver.Chrome("./chromedriver_win.exe", options=opt) # 윈도우
    #browser = webdriver.Chrome("../chromedriver_mac", options=opt) # 맥

    # 일반모드
    # options = Options()
    # options.add_argument('--start-fullscreen')
    # browser = webdriver.Chrome('./chromedriver_mac.exe', chrome_options=options)
    # browser = webdriver.Chrome('./chromedriver_mac.exe') # 윈도우
    # browser = webdriver.Chrome('./chromedriver_mac') # 맥
    # browser.maxmize_window()

    browser.implicitly_wait(5) # 브라우저가 로딩될때까지 최소 5초 기다

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

    # sign_country = browser.find_elements_by_css_selector("div.card-body tbody td:nth-child(1)")
    # sign_count = browser.find_elements_by_css_selector("div.card-body tbody td:nth-child(2)")

    # 날짜 url로 이동
    # url_date = "***"
    # browser.get(url_date)

    # 요소 선택
    sign_country = browser.find_elements_by_css_selector("div.card.bg-yellow-gradient div.card-body tbody td")
    exam_take = browser.find_elements_by_css_selector("div.card.bg-light-blue div.card-body tbody td")
    exam_complete = browser.find_elements_by_css_selector("div.card.bg-green div.card-body tbody td")
    print("요소를 불러옵니다.")

    countrylist = sign_country[0::2] # 짝수번째만 불러옴
    countList = sign_country[1::2] # 홀수번째만 불러옴

    signupList = dict(zip(countrylist, countList)) # 딕셔너리로 합침
    examtakeList = []
    examcompleteList = []

    sign_result = {}

    for key, value in signupList.items():
        sign_result[key.text] = value.text

    for i in exam_take:
        examtakeList.append(i.text)

    for i in exam_complete:
        examcompleteList.append(i.text)


    etc_count = 0

    for key, value in sign_result.items():
        if key == 'India':
            india_count = value
            print("India : ", value)
        elif key == 'Vietnam':
            vietnam_count = value
            print("Vietnam : ", value)
        elif key == 'Indonesia':
            indonesia_count = value
            print("Indonesia : ", value)
        elif key == 'Philippines':
            philippines_count = value
            print("Philippines : ", value)
        elif key == 'Bangladesh':
            bangladesh_count = value
            print("Bangladesh : ", value)
        elif key == 'total':
            break
        else:
            etc_count += int(value)


    print("기타 : ", etc_count)
    print(sign_result)
    print("총 시험 응시 수 : ", examtakeList[-1])
    print("총 시험 완료 수 : ", examcompleteList[-1])

    browser.close()