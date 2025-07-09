n = int(input())

# 튜플(Tuple): 여러 개의 값을 한꺼번에 묶어서 저장(리스트와 달리 수정 불가)
people = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    rank = 1    # i번째 사람 기본순위 1등
    for j in range(n):
        if i == j:
            continue    # 자기 자신과 비교하지 않음
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    print(rank, end=' ')