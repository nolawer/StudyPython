from datetime import datetime, timedelta
from test2 import *

sd_input = "20210301"
ed_input = "20210315"

start_date2 = datetime.strptime(sd_input, "%Y%m%d").date()
end_date2 = datetime.strptime(ed_input, "%Y%m%d").date()

re = timetest(start_date2, end_date2)

print("이거슨 : ", re.days)

f = {}

for i in range(int(sd_input), int(ed_input)):
    f[i] = [sd_input, ed_input]

print(f)

#
#
# print(start_date2, end_date2)
#
# min = end_date2 - start_date2
#
# print(min.days)
#
# a = min.days
#
# print(type(a))
#
# next_time = start_date2 + timedelta(days=7) # 7일 더하기
#
# print(next_time)
#
# print(type(next_time))
#
# timetest()

# for i in range(a):
#     print(i)