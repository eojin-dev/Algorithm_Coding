n = int(input())
num = list(map(int, input().split()))
sum = 0

for x in num:
    if x < 2:
        continue
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            break
    else:
        sum += 1

print(sum)