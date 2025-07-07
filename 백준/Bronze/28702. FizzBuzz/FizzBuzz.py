for i in range(3, 0, -1):
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:   #숫자 형태의 문자열인 경우만 처리
        n = int(x) + i  #간격만큼 숫자 더해 다음 값 찾기

if n%3==0 and n%5==0:
    print('FizzBuzz')
elif n%3==0:
    print('Fizz')
elif n%5==0:
    print('Buzz')
else:
    print(n)