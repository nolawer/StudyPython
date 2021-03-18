from analytics import *
from gioadmin import *
from datetime import datetime

sd_input = input("통계 시작일을 입력하세요(형식 = 20210301) : ")
ed_input = input("통계 종료일을 입력하세요(형식 = 20210302) : ")

start_date = str(datetime.strptime(sd_input, "%Y%m%d").date())
end_date = str(datetime.strptime(ed_input, "%Y%m%d").date())

print(start_date, end_date)


# ====================== GIO 어드민 페이지 크롤링 ==========================

adminCrwling()


# ====================== GIO 어드민 페이지 크롤링(끝) ==========================

# Google API 키파일(json format)
set_api_key('./global-ielts-online-907b5ea18a16.json')

# 국가별 사용자
print(get_results('users', 'country'))

# 국가별 사용자(날짜 임의 지정)
print('\n\n\n')
print(get_results('users', 'country', start_date, end_date))

# 날짜별 사용자
print('\n\n\n')
print(get_results('users', 'date'))

# 날짜별 사용자(날짜 임의 지정)
print('\n\n\n')
print(get_results('users', 'date', '7daysAgo', '1daysAgo'))

# 날짜별 신규 사용자
print('\n\n\n')
print(get_results('newusers', 'date'))

# 날짜별 신규 사용자(날짜 임의 지정)
print('\n\n\n')
print(get_results('newusers', 'date', '1daysAgo', 'today'))

# 채널 그룹별 사용자
print('\n\n\n')
print(get_results('users', 'channelGrouping'))

# Ads 통계
print('\n\n\n')
print('==========================ADS')
print(get_results('cpc', 'adwordsAdGroupID', '2021-03-01', '2021-03-02'))
print(get_results('adClicks', 'adwordsAdGroupID', '2021-03-01', '2021-03-02'))
print(get_results('impressions', 'adwordsAdGroupID', '2021-03-01', '2021-03-02'))