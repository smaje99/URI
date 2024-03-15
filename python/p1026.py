l=[]
try:
    while True:
        a,b=input().split()
        l.append(int(a)^int(b))
except EOFError as error:
    for i in l:
        print(i)