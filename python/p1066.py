a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
l=[a,b,c,d,e]
par=0
impar=0
p=0
n=0
for i in l:
    if i%2==0:
        par+=1
    if i%2!=0:
        impar+=1
    if i>0:
        p+=1
    if i<0:
        n+=1
print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(p,"valor(es) positivo(s)")
print(n,"valor(es) negativo(s)")