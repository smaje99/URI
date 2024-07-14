"""Beecrowd exercise 1029.

See: https://judge.beecrowd.com/es/problems/view/1029
"""


def fib(num: int) -> tuple[int, int]:
    """Calculate the n-th Fibonacci number and the number of calls."""
    f = [0] * (num + 1)
    cl = [0] * (num + 1)
    f[1] = 1
    cl[1] = 0
    for i in range(2, num + 1):
        f[i] = f[i - 1] + f[i - 2]
        cl[i] = cl[i - 1] + cl[i - 2] + 2
    return cl[num], f[num]


T = int(input())
for _ in range(T):
    n = int(input())
    c, r = fib(n)
    print(f"fib({n}) = {c} calls = {r}")
