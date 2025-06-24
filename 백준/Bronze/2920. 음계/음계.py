n = list(map(int, input().split()))

if n == sorted(n):  #오름차순
    print('ascending')
elif n == sorted(n, reverse=True):  #내림차순
    print('descending')
else:
    print('mixed')