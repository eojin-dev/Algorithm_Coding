lst = [i for i in range(1,31)]

for i in range(28):
    n = int(input())
    lst.remove(n)

print(*lst)