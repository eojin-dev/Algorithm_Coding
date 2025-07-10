n = int(input())

xy = [tuple(map(int,input().split())) for _ in range(n)]

xy.sort(key=lambda k: (k[0], k[1])) # x 먼저, x 같으면 y 정렬

for x, y in xy:
    print(x, y)