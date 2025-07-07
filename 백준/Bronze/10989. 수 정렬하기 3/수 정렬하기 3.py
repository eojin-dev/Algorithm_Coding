# n = int(input())
# lst = []

# for _ in range(n):
#     k = int(input())
#     lst.append(k)

# lst.sort()
# print(*lst, sep='\n')   #리스트의 요소를 하나씩 꺼내고 한줄씩 출력
# # 메모리 초과

import sys
input = sys.stdin.readline

#계수정렬
n = int(input())
arr = [0] * (10000+1)

for _ in range(n):
    arr[int(input())] += 1  #각 입력값에 해당하는 인덱스의 값 증가

for i in range(len(arr)):
    if arr[i] != 0: #0이 아닌 데이터, 즉 입력받은 데이터들을 출력
        for _ in range(arr[i]):
            print(i)