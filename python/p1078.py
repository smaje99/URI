"""Beecrowd exercise 1078.

See: https://judge.beecrowd.com/es/problems/view/1078
"""

n = int(input())
if 1 < n < 1000:
    for i in range(1, 11):
        print(f"{i} x {n} = {i * n}")
