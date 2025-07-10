n = int(input())

xy = [tuple(map(int,input().split())) for _ in range(n)]

xy.sort(key=lambda k: (k[1], k[0]))

for x, y in xy:
    print(x, y)