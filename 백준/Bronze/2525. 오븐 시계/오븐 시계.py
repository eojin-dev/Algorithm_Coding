A, B = map(int, input().split())
C = int(input())

total = B + C
A += total // 60
B = total % 60
A %= 24

print(A, B)
