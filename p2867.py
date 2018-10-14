c=int(input())
for i in range(c):
    m,n=input().split()
    m=int(m)
    n=int(n)
    if 1<=n<=100 and 1<=m<=100:
        print(len(str(m**n)))