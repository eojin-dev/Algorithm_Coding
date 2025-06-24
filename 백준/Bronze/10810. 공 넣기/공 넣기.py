n, m = map(int, input().split())
list1 = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1,j):
        list1[idx] = k

print(' '.join(map(str, list1)))