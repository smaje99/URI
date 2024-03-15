n=int(input())
a=1
for i in range(n):
    for j in range(4):
        if j==3:
            print("PUM")
        else:
            print(a,"",end="")
        a+=1