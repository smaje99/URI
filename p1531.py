def Fib(n):
    a, b = 0, 1
    while b < n:
        yield a
        a, b = b, a + b


table = list(Fib(10000))
while True:
    try:
        n, m = map(int, input().split())
        print(table[(table[n])] % m)
    except EOFError:
        break
