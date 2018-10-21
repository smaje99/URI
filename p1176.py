fib = [0]
a, b = 0, 1
for i in range(60):
    fib.append(b)
    a, b = b, a + b
t = int(input())
for i in range(t):
    n = int(input())
    if 0 <= n <= 60:
        print("Fib({0}) = {1}".format(n, fib[n]))
