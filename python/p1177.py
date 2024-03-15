n=int(input())
if 2<=n<=50:
    i=0
    while i<1000:
        for a in range(0,n):
            if i==1000:
                break
            print("N["+str(i)+"] = "+str(a))
            i+=1