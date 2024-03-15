import math


def esPrime(n):
    if n % 2 == 0 and n > 2: return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


m = int(input())
if 1 <= m <= 100:
    for i in range(m):
        x = int(input())
        if 1 < x <= 10 ** 7:
            print(repr(x) + (' eh primo' if esPrime(x) else ' nao eh primo'))
