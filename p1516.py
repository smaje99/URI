while True:
    n,m=input().split()
    n=int(n)
    m=int(m)
    if n==m==0:
        break;
    elif 1<=n<=50 and 1<=m<=50:
        l=[]
        for i in range(n):
            char=input()
            if len(char)==m:
                l.append(char)
        a,b=input().split()
        a=int(a)
        b=int(b)
        if n<a<=100 and m<b<=100 and a%n==0 and b%m==0:
            for i in l:
                for k in range(a/n):
                    for j in range(b/m):
                        print(i[int(j)]*(b/m),end="")
                    print()