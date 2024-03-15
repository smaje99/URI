l=[]
try:
    while True:
        a,b=input().split()
        a=int(a)
        b=int(b)
        if a<=2**32 and b<=2**32:
            if a==b:
                l.append(0)
            else:
                l.append(max((a,b))-min((a,b)))
except EOFError as error:
    for i in l:
        print(i)