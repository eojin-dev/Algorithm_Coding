while True:
    s = input()
    if s == '0':
        break

    tf = True   # 회문 여부 확인용 플래그

    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            tf = False
            break
    
    if tf:
        print("yes")
    else:
        print("no")
