"""Beecrowd exercise 1026.

See: https://judge.beecrowd.com/es/problems/view/1026
"""


xors: list[int] = []

try:
    while True:
        a, b = map(int, input().split())
        xors.append(a ^ b)
except EOFError:
    for i in xors:
        print(i)
