n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
shirt = 0

for i in range(len(size)):
    if size[i] % t == 0:
        shirt += (size[i] // t)
    else:
        shirt += size[i] // t + 1

pens = n // p
pen = n % p

print(shirt)
print(pens, pen, end = ' ')