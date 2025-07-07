n, k = map(int, input().split())

def factorial(p):
    fac = 1
    for i in range(1, p+1):
        fac *= i
    return fac

result = factorial(n)//(factorial(n-k) * factorial(k))

print(result)