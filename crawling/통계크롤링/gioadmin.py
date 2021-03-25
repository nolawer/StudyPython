from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta


def adminCrwling(sd_input, ed_input):

    # 크롬창 열기

    # 헤드리스 모드
    opt = webdriver.ChromeOptions()
    opt.add_argument("headless")
    browser = webdriver.Chrome("./chromedriver_win.exe", options=opt) # 윈도우
    # browser = webdriver.Chrome("../chromedriver_mac", options=opt) # 맥

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

    daily_result = {} # 아래 for문 결과값 딕셔너리 선언

    # 시작일부터 종료일 반복문 실행

    for f in range(int(sd_input), int(ed_input)+1):

        # 날짜 url로 이동
        # format_date = f + 1
        url_date = "https://admin.globalieltsonline.com/home?date={}".format(f+1)
        browser.get(url_date)

        # 요소 선택
        sign_country = browser.find_elements_by_css_selector("div.card.bg-yellow-gradient div.card-body tbody td")
        exam_take = browser.find_elements_by_css_selector("div.card.bg-light-blue div.card-body tbody td")
        exam_complete = browser.find_elements_by_css_selector("div.card.bg-green div.card-body tbody td")
        print("{}요소를 불러옵니다.".format(f))

        countrylist = sign_country[0::2] # 짝수번째만 불러옴
        countList = sign_country[1::2] # 홀수번째만 불러옴

        signupList = dict(zip(countrylist, countList)) # 딕셔너리로 합침
        examtakeList = []
        examcompleteList = []

        sign_result = {}

        # signupList 딕셔너리에서 키와 밸류를 가져와서 sign_result 딕셔너리에 넣음
        for key, value in signupList.items():
            sign_result[key.text] = value.text

        # exam_take, exam_complete 요소를 리스트로 저장
        for i in exam_take:
            examtakeList.append(i.text)

        for i in exam_complete:
            examcompleteList.append(i.text)


        # 각 국가에 해당하는 변수에 카운트 값을 저장함(국가값이 total이 될때까지)
        # 수집 국가가 아닌경우 etc에 카운트 값을 저장

        etc_count = 0

        for key, value in sign_result.items():
            if key == 'India':
                india_count = value
                # print("India : ", value)
            elif key == 'Vietnam':
                vietnam_count = value
                # print("Vietnam : ", value)
            elif key == 'Indonesia':
                indonesia_count = value
                # print("Indonesia : ", value)
            elif key == 'Philippines':
                philippines_count = value
                # print("Philippines : ", value)
            elif key == 'Bangladesh':
                bangladesh_count = value
                # print("Bangladesh : ", value)
            elif key == 'total':
                break
            else:
                etc_count += int(value)

        # print("기타 : ", etc_count)
        # print(sign_result)
        # print("총 시험 응시 수 : ", examtakeList[-1])
        # print("총 시험 완료 수 : ", examcompleteList[-1])

        # 일자별 결과값 정리

        daily_result[f] = [india_count, vietnam_count, indonesia_count, philippines_count, bangladesh_count, etc_count, examtakeList[-1], examcompleteList[-1]]

    browser.close()

    # 타겟국가(인도,베트남,인도네시아,필리핀,방글라데시,기타국가) 카운트 수, 총 시험 응시자 수(리스트 마지막이 토탈), 총 시험 완료 수 리턴(리스트 마지막이 토탈)

    return daily_result