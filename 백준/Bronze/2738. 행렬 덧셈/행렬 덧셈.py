n, m = map(int, input().split())
a, b = [], []

for _ in range(n):
    lists = list(map(int, input().split()))
    a.append(lists)

for _ in range(n):
    lists = list(map(int, input().split()))
    b.append(lists)

for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j], end = ' ')
    print()