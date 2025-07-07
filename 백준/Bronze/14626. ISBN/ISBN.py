isbn = input()
lst = list(isbn)

for a in range(10): # *에 들어갈 숫자는 0~9 정수
    total = 0
    for i in range(len(lst)):
        if lst[i] =='*':
            val = a
        else:
            val = int(lst[i])

        if i % 2 == 0:
            total += val
        else:
            total += 3 * val

    if total % 10 == 0:
        print(a)
        break