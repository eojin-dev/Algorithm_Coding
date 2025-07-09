n = int(input())

count = 0
while n >= 5:
    n //= 5
    count += n

print(count)

# 팩토리얼의 끝자리 0의 개수는 곱해지는 2와 5의 쌍에서 발생
# 5의 배수가 더 적게 나오므로, 5의 배수 개수만 세면 됨
# 25는 5의 배수이므로 n >= 5