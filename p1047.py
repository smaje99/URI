a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if a==c:
    if b==d:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    elif b>d:
        print("O JOGO DUROU 23 HORA(S) E {} MINUTO(S)".format(60-(b-d)))
    else:
        print("O JOGO DUROU 0 HORA(S) E {} MINUTO(S)".format(d-b))
elif c>a:
    if b==d:
        print("O JOGO DUROU {} HORA(S) E 0 MINUTO(S)".format(c-a))
    elif b>d:
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(c-a-1,60-(b-d)))
    else:
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(c-a,d-b))
else:
    if b==d:
        print("O JOGO DUROU {} HORA(S) E 0 MINUTO(S)".format(24-a+c))
    elif b>d:
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24-a+c-1,60-(b-d)))
    else:
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24-a+c,d-b))