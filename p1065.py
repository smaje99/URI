a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
l=[a,b,c,d,e]
n=0
for i in l:
    if i%2==0:
        n+=1
print(n,"valores pares")