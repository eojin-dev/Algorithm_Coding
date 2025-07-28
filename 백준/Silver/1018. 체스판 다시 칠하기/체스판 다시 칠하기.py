n, m = map(int, input().split())
chess =[list(input()) for _ in range(n)] # chess라는 변수에 보드값을 리스트로 저장
cnt = []
#시작점 8x8 크기의 보드를 만들 수 있는 모든 경우 계산하는 for문
for i in range(n - 7):
    for j in range(m - 7):
        w_cnt, b_cnt = 0, 0
        for k in range(i, i+8): #시작점을 기준으로 8칸씩 모두 체크
            for l in range(j, j+8):
                if (k+l) % 2 == 0: #현재행의 번호 k,l의 합이 짝수이면 시작점과 색 같아야함
                    if chess[k][l] != 'W': #화이트 먼저 시작인 보드
                        w_cnt += 1
                    if chess[k][l] != 'B': #블랙이 먼저 시작인 보드
                        b_cnt += 1
                else:   #현재행의 번호 k,l의 합이 홀수이면 시작점과 색이 달라야함
                    if chess[k][l] != 'B':
                        w_cnt += 1
                    if chess[k][l] != 'W':
                        b_cnt += 1
        cnt.append(w_cnt) #두개의 수를 cnt에 넣고 작은값 출력
        cnt.append(b_cnt)
print(min(cnt))