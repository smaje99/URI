"""Beecrowd exercise 1035.

See: https://judge.beecrowd.com/es/problems/view/1035
"""

A, B, C, D = map(int, input().split())

print(
    "Valores aceitos"
    if B > C > 0 and D > A >= 0 and C + D > A + B and A % 2 == 0
    else "Valores nao aceitos"
)
