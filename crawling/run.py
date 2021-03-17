# from analytics import *
import datetime as dt

# Google API 키파일(json format)
# set_api_key('./global-ielts-online-907b5ea18a16.json')

# def get_results(metrics = 'users', dimensions = None, sdate = '7daysAgo', edate = '1daysAgo'):
# metrics = 숫자로 발생하는 카운트
# dimensions = 분석기준이 되는 객체
# sdate = 시작일 (YYYY-MM-DD)
# edate = 종료일 (YYYY-MM-DD)

# 국가별 사용자
# print(get_results('users', 'country'))

# 국가별 사용자(날짜 임의 지정)
# print('\n\n\n')

start_date_input = input("시작일 입력(ex : 20210317) : ")
end_date_input = input("종료일 입력(ex : 20210319) : ")

date_count = int(end_date_input) - int(start_date_input) # 시작일과 종료일의 차이 일수

print(date_count)

start_date_change = dt.datetime.strptime(start_date_input,"%Y%m%d").date()
end_date_change = dt.datetime.strptime(start_date_input,"%Y%m%d").date()

print(start_date_change)

print((end_date_change - start_date_change).days)



# start_date_input = '2021-03-08'
# end_date_input = '2021-03-09'


# user_country = get_results('users', 'country', start_date_input, end_date_input)
# print(user_country)

# 날짜별 사용자
# print('\n\n\n')
# print(get_results('users', 'date'))

# 날짜별 사용자(날짜 임의 지정)
# print('\n\n\n')
# print(get_results('users', 'date', '7daysAgo', '1daysAgo'))

# 날짜별 신규 사용자
# print('\n\n\n')
# print(get_results('newusers', 'date'))

# 날짜별 신규 사용자(날짜 임의 지정)
# print('\n\n\n')
# print(get_results('newusers', 'date', '1daysAgo', 'today'))

# 채널 그룹별 사용자
# print('\n\n\n')
# print(get_results('users', 'channelGrouping'))