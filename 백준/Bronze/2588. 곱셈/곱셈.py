A=int(input())
B=int(input())

C=A*(B%10)
D=A*(((B%100)-(B%10))//10)
E=A*(B//100)

print(C)
print(D)
print(E)
print(C+(D*10)+(E*100))