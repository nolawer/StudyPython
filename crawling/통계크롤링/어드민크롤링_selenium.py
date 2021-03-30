from analytics import * # 구글 애널리틱스/광고 연동 함수(파일명 : analytics.py)
from gioadmin import * # GIO 어드민 크롤링 함수(파일명 : gioadmin.py)
# from googlesheet import * # 구글 시트 연동 함수(파일명 : googlesheet.py)
import gspread # 구글 스프레시트
# import pygsheets # 구글 스프레시트
from oauth2client.service_account import ServiceAccountCredentials # 구글 스프레시트 연동
from datetime import datetime


# 실행 전 운영체제에 맞춰 gioadmin.py 파일의 드라이버 윈/맥 설정 코드 변경 필요

sd_input = input("통계 시작일을 입력하세요(형식 = 20210301) : ")
ed_input = input("통계 종료일을 입력하세요(형식 = 20210302) : ")


# GIO 어드민 페이지 크롤링 ==================
# 타겟국가(인도,베트남,인도네시아,필리핀,방글라데시,기타국가) 카운트 수, 총 시험 응시자 수(리스트 마지막이 토탈), 총 시험 완료 수 리턴(리스트 마지막이 토탈)

daily_result = adminCrwling(sd_input, ed_input)

print("어드민 결과값 : ", daily_result)

# Google 애널리틱스/광고 API 연동 ===============
# def get_results(metrics = 'users', dimensions = None, sdate = '7daysAgo', edate = '1daysAgo'):
# metrics = 숫자로 발생하는 카운트
# dimensions = 분석기준이 되는 객체
# sdate = 시작일 (YYYY-MM-DD)
# edate = 종료일 (YYYY-MM-DD)


# Google API 키파일(json format)
set_api_key('./global-ielts-online-907b5ea18a16.json')

# 구글 애널리틱스 통계 ---------------

# 날짜별 사용자(날짜 임의 지정)

du_result = {}

for i in range(int(sd_input), int(ed_input)+1):
    # 입력받은 스트링을 날짜 형식으로 변환(2021-03-31)
    start_date = datetime.strptime(str(i), "%Y%m%d").date()

    user_daily_data = get_results('users', 'date', str(start_date), str(start_date))
    # print(user_daily_data)
    # print("{} 총 사용자 수 : ".format(i), user_daily_data['rows'][0][1]) # 사용자 수

    du_result[i] = [user_daily_data['rows'][0][1]]

print("일자별 총 사용자 결과값 : ", du_result)


# 국가별 사용자(날짜 임의 지정)

uc_result = {} # 아래 for문 결과값 딕셔너리 선언

for i in range(int(sd_input), int(ed_input)+1):
    # 입력받은 스트링을 날짜 형식으로 변환(2021-03-31)
    start_date = datetime.strptime(str(i), "%Y%m%d").date()

    user_country_data = get_results('users', 'country', str(start_date), str(start_date))
    # print("국가별 사용자 : ", user_country_data)

    user_country_data_total = user_country_data['totalsForAllResults'] # user_country_data 중 totalsForAllResults 딕셔너리를 받아옴
    uc_total = user_country_data_total.get('ga:users') # 위 딕셔너리 중 value를 받아옴

    user_country_data_dic = dict(user_country_data['rows']) # user_country_data 중 row를 딕셔너리형으로 변환

    uc_india = user_country_data_dic.get('India') # 해당 키의 value를 찾아옴
    uc_vietnam = user_country_data_dic.get('Vietnam')  # 해당 키의 value를 찾아옴
    uc_indonesia = user_country_data_dic.get('Indonesia')  # 해당 키의 value를 찾아옴
    uc_bangladesh = user_country_data_dic.get('Bangladesh')  # 해당 키의 value를 찾아옴
    uc_philippines = user_country_data_dic.get('Philippines')  # 해당 키의 value를 찾아옴
    uc_etc = int(uc_total) - (int(uc_india) + int(uc_vietnam) + int(uc_indonesia) + int(uc_bangladesh) + int(uc_philippines))

    uc_result[i] = [uc_india, uc_vietnam, uc_indonesia, uc_bangladesh, uc_philippines, uc_etc]

print("국가별 사용자 결과값 : ", uc_result)


# 채널 그룹별 사용자
ch_result = {} # 아래 for문 결과값 딕셔너리 선언

for i in range(int(sd_input), int(ed_input)+1):
    # 입력받은 스트링을 날짜 형식으로 변환(2021-03-31)
    start_date = datetime.strptime(str(i), "%Y%m%d").date()

    user_channel_data = get_results('users', 'channelGrouping', str(start_date), str(start_date))

    # print("{}채널별 데이터 : ".format(i), user_channel_data)

    user_channel_data_dic = dict(user_channel_data['rows'])  # user_channel_data 중 row를 딕셔너리형으로 변환

    ch_direct = user_channel_data_dic.get('Direct')  # 해당 키의 value를 찾아옴
    ch_email = user_channel_data_dic.get('Email')  # 해당 키의 value를 찾아옴
    ch_organic = user_channel_data_dic.get('Organic Search')  # 해당 키의 value를 찾아옴
    ch_paid = user_channel_data_dic.get('Paid Search')  # 해당 키의 value를 찾아옴
    ch_referral = user_channel_data_dic.get('Referral')  # 해당 키의 value를 찾아옴
    ch_social = user_channel_data_dic.get('Social')  # 해당 키의 value를 찾아옴
    ch_other = user_channel_data_dic.get('(Other)')  # 해당 키의 value를 찾아옴

    ch_result[i] = [ch_paid, ch_organic, ch_direct, ch_referral, ch_social, ch_email, ch_other]

print("채널별 사용자 결과값 : ", ch_result)



# 구글 광고 통계 ---------------

# 일별 CPC
ads_cpc_value = {}

for i in range(int(sd_input), int(ed_input)+1):
    # 입력받은 스트링을 날짜 형식으로 변환(2021-03-31)
    start_date = datetime.strptime(str(i), "%Y%m%d").date()

    ads_cpc_data = get_results('cpc', 'adwordsAdGroupID', str(start_date), str(start_date))

    # print(ads_cpc_data)

    ads_cpc_data_result = ads_cpc_data['totalsForAllResults']  # ads_cpc_data 중 totalsForAllResults 딕셔너리를 받아옴
    ads_cpc_value[i] = round(float(ads_cpc_data_result.get('ga:cpc')), 3)  # 위 딕셔너리 중 value를 받아옴, 소수점 2자리 반올림

print("cpc 결과값 : ", ads_cpc_value)

# 일별 키워드 클릭 수
ads_clicks_value = {}

for i in range(int(sd_input), int(ed_input)+1):
    # 입력받은 스트링을 날짜 형식으로 변환(2021-03-31)
    start_date = datetime.strptime(str(i), "%Y%m%d").date()

    ads_clicks_data = get_results('adClicks', 'adwordsAdGroupID', str(start_date), str(start_date))

    # print(ads_clicks_data)

    ads_clicks_data_result = ads_clicks_data['totalsForAllResults']  # ads_clicks_data 중 totalsForAllResults 딕셔너리를 받아옴
    ads_clicks_value[i] = int(ads_clicks_data_result.get('ga:adClicks')) # 위 딕셔너리 중 value를 받아옴

print("clicks 결과값 : ", ads_clicks_value)

# 일별 노출 수
ads_impressions_value = {}

for i in range(int(sd_input), int(ed_input)+1):
    # 입력받은 스트링을 날짜 형식으로 변환(2021-03-31)
    start_date = datetime.strptime(str(i), "%Y%m%d").date()

    ads_impressions_data = get_results('impressions', 'adwordsAdGroupID', str(start_date), str(start_date))

    # print(ads_impressions_data)

    ads_impressions_data_result = ads_impressions_data['totalsForAllResults']  # ads_impression_data 중 totalsForAllResults 딕셔너리를 받아옴
    ads_impressions_value[i] = ads_impressions_data_result.get('ga:impressions')  # 위 딕셔너리 중 value를 받아옴

print("impressions 결과값 : ", ads_impressions_value)



# Google 스프레시트 연동 ===============

scope = ['https://spreadsheets.google.com/feeds']
json_file_name = './global-ielts-online-907b5ea18a16.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1-Qy11dtRjGZ_gb9QlEiBAht4cufbOrZR2BCB9ZDxIJg/edit#gid=1534660144'

# 문서 불러오기
doc = gc.open_by_url(spreadsheet_url)
# 시트 불러오기
worksheet = doc.worksheet('통계(21/03월)')


# 시작일, 종료일 날짜 변환
gs_st_date = datetime.strptime(sd_input, "%Y%m%d").date()
gs_ed_date = datetime.strptime(ed_input, "%Y%m%d").date()

# 시작일과 종료일의 차이(일수)
# date_interval = (ed_input - sd_input).days

# print(admin_daily_result)


k = int(ed_input) - int(sd_input) + 1 # 시작일과 종료일의 일수 차이
r = int(sd_input[6:]) + 3 # 추가할 행 : 일자의 마지막  + 2

for i in range(0,k):
    sday_result = int(sd_input) + i # 날짜 : 시작일에서 하루씩 증가
    admin_daily_result = daily_result.get(int(sd_input) + i) # 어드민 결과 : 해당일자를 키 값으로 value 리스트 받아오기, 일자 하루씩 증가
    ga_du_result = du_result.get(int(sd_input) + i) # GA 일자별 총 사용자 결과 : 상동
    ga_uc_result = uc_result.get(int(sd_input) + i)  # GA 국가별 사용자 결과 : 상동
    ga_ch_result = ch_result.get(int(sd_input) + i)  # GA 채널별 사용자 결과 : 상동
    gads_cpc_result = ads_cpc_value.get(int(sd_input) + i)  # 구글 ADS CPC 결과 : 상동 | 실수형 변환, 소수점 2자리 변
    gads_clicks_result = ads_clicks_value.get(int(sd_input) + i)  # 구글 ADS 클릭수 결과 : 상동
    gads_impressions_result = ads_impressions_value.get(int(sd_input) + i)  # 구글 ADS 노출수 결과 : 상동

    # 총 회원가입자 수 = 국가별 회원가입 수 합계
    total_signup = int(admin_daily_result[0]) + int(admin_daily_result[1]) + int(admin_daily_result[2]) + int(admin_daily_result[3]) + int(admin_daily_result[4]) + int(admin_daily_result[5])

    # 마케팅비용 = 클릭수 * CPC
    total_ads_pay = gads_clicks_result * gads_cpc_result

    # 구글 스프레시트 열 추가
    worksheet.insert_row([
        sday_result, # 날짜
        int(ga_du_result[0]), # 총 사용자
        int(total_signup), # 총 회원가입
        float(total_ads_pay), # 마케팅 비용
        '', # 여백
        int(gads_clicks_result), # 키워드 클릭수
        int(gads_impressions_result), # 키워드 노출수
        float(gads_cpc_result), # 키워드 CPC
        '', # 여백
        ga_ch_result[0], # 유입채널 : Paid search
        ga_ch_result[1], # 유입채널 : Organic Search
        ga_ch_result[2], # 유입채널 : Direct
        ga_ch_result[3], # 유입채널 : Referral
        ga_ch_result[4], # 유입채널 : Social
        ga_ch_result[5], # 유입채널 : Email
        ga_ch_result[6], # 유입채널 : Other
        '', # 여백
        ga_uc_result[0], # 사용자국가 : India
        ga_uc_result[1], # 사용자국가 : Vietnam
        ga_uc_result[2], # 사용자국가 : Indonesia
        ga_uc_result[3], # 사용자국가 : Bangladesh
        ga_uc_result[4], # 사용자국가 : Philippines
        ga_uc_result[5], # 사용자국가 : 기타
        '', # 여백
        admin_daily_result[0], # 회원가입국가 : India
        admin_daily_result[1], # 회원가입국가 : Vietnam
        admin_daily_result[2], # 회원가입국가 : Indonesia
        admin_daily_result[3], # 회원가입국가 : Bangladesh
        admin_daily_result[4], # 회원가입국가 : Philippines
        admin_daily_result[5], # 기타
        '', # 여백
        int(admin_daily_result[6]), # 시험응시수
        int(admin_daily_result[7]), # 시험완료수
        ], r+i) # 시트에서 추가할 행 번호

    print("{} 통계를 {}행 기록완료 했습니다.".format(sday_result, r+i))


print("통계 기록을 완료하였습니다.")