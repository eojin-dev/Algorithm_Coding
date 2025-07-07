n = int(input())
lst = []

for _ in range(n):
    s = input()
    lst.append(s)

lst2 = list(set(lst))
sort_lst2 = sorted(lst2, key=lambda x: (len(x), x))   #lambda: 익명함수

print(*sort_lst2, sep='\n')