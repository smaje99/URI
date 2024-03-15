i=0
l=[]
alto=0
ind=i
while i!=100:
    b=int(input())
    i+=1
    if b>alto:
        alto=b
        ind=i
print(alto)
print(ind)