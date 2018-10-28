def Fib(n):
    a, b, c = 0, 1, 0
    for i in range(n):
        a, b = b, a + b
    return a


while True:
    try:
        n, m = map(int, input().split())
        print(Fib(Fib(n)) % m)
    except EOFError:
        break
