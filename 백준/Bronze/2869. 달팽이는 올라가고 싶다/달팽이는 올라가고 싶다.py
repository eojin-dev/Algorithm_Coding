# a, b, v = map(int, input().split())
# m, day = 0, 0

# while True:
#     m += a
#     m -= b
#     if m < v:
#         day += 1
#     else:
#         break

# print(day)
# 시간초과...

import math

a, b, v = map(int, input().split())

# 마지막 날에는 미끄러지지 않기 때문에 (v - b) 기준
day = math.ceil((v - b) / (a - b))  #소수점 이하 올림
print(day)