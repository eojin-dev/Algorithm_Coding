l = int(input())
s = input()

alpha = {chr(i): i - ord('a') + 1 for i in range (ord('a'), ord('z') + 1)}
mapping = [alpha[chr] for chr in s]

h = 0
mod = 1234567891

for i in range(l):
    h += mapping[i] * 31**i
    h %= mod

print(h)