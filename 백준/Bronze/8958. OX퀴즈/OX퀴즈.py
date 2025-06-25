t = int(input())

for _ in range(t):
    sum = 0
    total = 0
    s = input()
    for i in range(len(s)):
        if s[i] == 'O':
            sum += 1
            total += sum
        else:
            sum = 0
    print(total)