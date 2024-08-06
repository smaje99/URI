"""Beecrowd exercise 1044.

See: https://judge.beecrowd.com/es/problems/view/1044
"""

a, b = map(int, input().split())

print(
    "Sao Multiplos"
    if a % b == 0 or b % a == 0
    else "Nao sao Multiplos"
)
