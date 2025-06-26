n = int(input())

for m in range(int(n/2), n):
    if m + sum(map(int, str(m))) == n:
        print(m)
        break
else:
    print(0)