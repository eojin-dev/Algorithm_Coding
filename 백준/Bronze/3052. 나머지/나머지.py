lst = []

for i in range (10):
    n = int(input())
    lst.append(n%42)

set_lst = set(lst)
print(len(set_lst))