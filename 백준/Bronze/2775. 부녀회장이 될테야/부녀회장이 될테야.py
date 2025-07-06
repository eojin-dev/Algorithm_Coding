t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    arr = [list(range(1, n+1))] # 0층 초기화 (1부터 n까지)

    for i in range(1, k+1): # 1층부터 k층까지(입력한 층까지만)
        floor = []
        for j in range(n):
            if j == 0:
                floor.append(1) # 첫 번째 호는 항상 1
            else:
                floor.append(floor[j-1] + arr[i-1][j])
        arr.append(floor)   # 전체 arr에 해당 층을 추가

    print(arr[k][n-1])  # k층 n호