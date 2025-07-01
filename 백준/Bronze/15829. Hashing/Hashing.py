l = int(input())
s = input()

alpha = {chr(i): i - ord('a') + 1 for i in range (ord('a'), ord('z') + 1)}
mapping = [alpha[chr] for chr in s]

h = 0
for i in range(l):
    k = mapping[i] * 31**i
    h += k

print(h)