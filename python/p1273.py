n = 0
align = 0
le = 0
names=[]
i=0
while True:
    n=int(input())
    align=0
    if n==0:
        break
    else:
        if i!=0:
            print("")
        names=[]
        for j in range(n):
            names.append(input())
            le=len(names[j])
            if le>align:
                align=le
        for j in range(n):
            print(names[j].rjust(align," "))
    i+=1