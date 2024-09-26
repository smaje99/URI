"""Beecrowd exercise 1067.

See: https://judge.beecrowd.com/es/problems/view/1067
"""

x = int(input())

if 1 <= x <= 1000:
    for i in range(1, x + 1, 2):
        print(i)
