import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))

#유클리드 호제법

# def gcd(a, b):
#     while b!=0:
#         a, b = b, a%b   #b가 0이 될 때까지 a % b를 반복
#     return a
    
# def lcm(a, b):
#     return a*b // gcd(a, b) #공식

# a, b = map(int, input().split())

# print(gcd(a, b))
# print(lcm(a, b))
