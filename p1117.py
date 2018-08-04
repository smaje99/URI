a=True
l=[]
c=0
while a:
    b=float(input())
    if b>=0 and b<=10:
        l.append(b)
    else:
        c+=1
    if len(l)==2:
        a=False
n=0
for i in range(c):
    print("nota invalida")
for i in l:
   n+=i
print("media = {0:.2f}".format(n/len(l)))