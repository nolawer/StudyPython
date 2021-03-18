from analytics import *

# Google API 키파일(json format)
set_api_key('./global-ielts-online-907b5ea18a16.json')

# def get_results(metrics = 'users', dimensions = None, sdate = '7daysAgo', edate = '1daysAgo'):
# metrics = 숫자로 발생하는 카운트
# dimensions = 분석기준이 되는 객체
# sdate = 시작일 (YYYY-MM-DD)
# edate = 종료일 (YYYY-MM-DD)

# 국가별 사용자
print(get_results('users', 'country'))

# 국가별 사용자(날짜 임의 지정)
print('\n\n\n')
print(get_results('users', 'country', '2021-03-01', '2021-03-16'))

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