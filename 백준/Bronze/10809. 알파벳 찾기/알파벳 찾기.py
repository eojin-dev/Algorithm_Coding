s = input()
alpha = [-1]*26
#문자열에 등장하지 않은 알파벳의 인덱스(요소)는 처음 설정한 -1 값 그대로 유지

for i in range(len(s)):
    ch = s[i]
    index = ord(ch) - ord('a')
    #0~25 사이 숫자로 변환(a와의 차이로 a->0, b->1...)
    if alpha[index] == -1:
        alpha[index] = i
    #여러번 등장 시 값이 변하지 않도록

print(*alpha)
#리스트를 공백으로 나눠 한 줄로 출력

#s = input()
#alpha = [chr(c) for c in range(ord('a'),ord('z')+1)]
#result = [str(s.find(ch)) for ch in alpha]
#.find(ch)는: 문자가 처음 등장하는 인덱스를 반환 / 없으면 -1을 반환

#print(*result)
