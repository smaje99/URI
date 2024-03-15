n=int(input())
if 1<n<1000:
    for i in range(10):
        print(repr(i+1)+" x "+repr(n)+" = "+repr((i+1)*n))