a = int(input())
b = int(input())
c = int(input())

n = a*b*c
l = list(map(int, str(n)))

for i in range(10):
    print(l.count(i))