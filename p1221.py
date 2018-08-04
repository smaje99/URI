from math import sqrt


def isPrime(x):
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append("Prime" if isPrime(x) else "Not Prime")
for i in l:
    print(i)
