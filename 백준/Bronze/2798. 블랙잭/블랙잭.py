from itertools import combinations

n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = []

for comb in combinations(l1, 3):
    if sum(comb) <= m:
        l2.append(sum(comb))

print(max(l2))