x,y=input().split()
x=int(x)
y=int(y)
a=1
if x<y:
    while a<=y:
        i=0
        for j in range(x):
            if a<=y:
                if j==x-1:
                    print(a)
                else:
                    print(a,"",end="")
            a+=1