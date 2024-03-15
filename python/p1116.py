n = int(input())
for i in range(n):
    a, b = input().split()
    a = float(a)
    b = float(b)
    if b == 0:
        print("divisao impossivel")
    else:
        print("{:0.1f}".format(a / b))