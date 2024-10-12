"""Beecrowd exercise 1073.

See: https://judge.beecrowd.com/es/problems/view/1073
"""

n = int(input())

if 5 < n < 2000:
    for i in range(2, n + 1, 2):  # Solo recorre los pares
        square = i ** 2
        print(f"{i}^2 = {square}")
