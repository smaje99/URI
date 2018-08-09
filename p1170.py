n=int(input())
if 1<=n<=1000:
    l=[]
    while not n==0:
        x=float(input())
        if 1<=x<=1000:
            i=0
            while x>1:
                x/=2
                i+=1
            l.append(i)
        n-=1
    for i in l:
        print(i,"dias")