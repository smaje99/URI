def josephus(ls, skip):
    skip -= 1
    idx = skip
    while len(ls) > 1:
        ls.pop(idx)
        idx = (idx + skip) % len(ls)
    return ls[0]

nc=int(input())
if 1<=nc<=30:
    l=[]
    for i in range(1,nc+1):
        n,k=input().split()
        if 1<=int(n)<=10000 and 1<=int(k)<=1000:
            l.append("Case "+str(i)+": "+str(josephus(list(range(1,int(n)+1)),int(k))))
    for i in l:
        print(i)