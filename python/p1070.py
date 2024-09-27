"""Beecrowd exercise 1070.

See: https://judge.beecrowd.com/es/problems/view/1070
"""

xn = int(input())

start = xn + 1 if xn % 2 == 0 else xn

for i in range(start, start + 12, 2):
    print(i)
