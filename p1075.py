n=int(input())
if n<10000:
    for i in range(1,10001):
        if i%n==2:
            print(i)