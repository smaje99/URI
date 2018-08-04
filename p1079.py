n=int(input())
l=[]
while n!=0:
    a,b,c=input().split()
    l.append(((float(a)*2)/10)+((float(b)*3)/10)+((float(c)*5)/10))
    n-=1
for i in l:
    print("{:0.1f}".format(i))