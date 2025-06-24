list1 = []
for _ in range(9):
    list1.extend(map(int, input().split()))

print(max(list1))
print(list1.index(max(list1)) + 1)