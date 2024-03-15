n=int(input())
if  1<n<1000:
    for i in range(0,n):
        print(str(i+1)+" "+str(((i+1)**2))+" "+str(((i+1)**3)))