def fib(n):
    a, b = 0, 1
    s = ''
    for i in range(n):
        if i<=46:
            s += "{} ".format(a)
            a, b = b, a + b
        else:
            s += "{} ".format(0)
    return s


n = int(input())
fib=fib(n)
print(fib[:len(fib)-1])
