n=int(input())
if n>0:
    l=[]
    i=0
    while i!=n:
        y,a=input().split()
        l.append((y,a))
        i+=1;
    i=0
    while i!=n:
        if l[i][1]=="hex":
            print("Case "+str(i+1)+":")
            print("{} dec".format(int(l[i][0],16)))
            print("{0:b} bin".format((int(l[i][0],16))))
            print()
        elif l[i][1]=="bin":
            print("Case "+str(i+1)+":")
            print("{} dec".format(int(l[i][0],2)))
            print("{:x} hex".format((int(l[i][0],2))))
            print()
        elif l[i][1]=="dec":
            print("Case "+str(i+1)+":")
            print("{:x} hex".format(int(l[i][0])))
            print("{:b} bin".format(int(l[i][0])))
            print()
        i+=1