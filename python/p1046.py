a,b=input().split()
a=int(a)
b=int(b)
if a==b:
    print("O JOGO DUROU 24 HORA(S)")
elif a==b-12 or a-12==b:
    print("O JOGO DUROU 12 HORA(S)")
elif b>a:
    print("O JOGO DUROU {} HORA(S)".format(b-a))
else:
    print("O JOGO DUROU {} HORA(S)".format(24-a+b))