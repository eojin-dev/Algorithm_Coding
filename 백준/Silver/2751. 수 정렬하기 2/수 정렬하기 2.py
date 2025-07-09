import sys
input=sys.stdin.readline

n = int(input())
lst= []

for _ in range(n):
    s = input()
    lst.append(int(s))

for i in sorted(lst):
    print(i)