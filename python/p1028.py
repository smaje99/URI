"""Beecrowd exercise 1028.

See: https://judge.beecrowd.com/es/problems/view/1028
"""


def gcd(num1: int, num2: int) -> int:
    """Máximo común divisor."""
    x, y = 0, 1
    lx, ly = 1, 0

    while num2:
        q = num1 // num2
        num1, num2 = num2, num1 % num2
        x, lx = lx - q * x, x
        y, ly = ly - q * y, y

    return num1


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(gcd(a, b))
