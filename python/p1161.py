from math import factorial as fac
l=[]
try:
    while True:
        a,b=input().split()
        l.append(fac(int(a))+fac(int(b)))
except EOFError as error:
    for i in l:
        print(i)