a, b, c, d, e = map(int, input().split())

def cal(a, b, c, d, e):
    print((a**2 + b**2 + c**2 + d**2 + e**2)%10)

cal(a, b, c, d, e)