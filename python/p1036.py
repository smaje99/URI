"""Beecrowd exercise 1036.

See: https://judge.beecrowd.com/es/problems/view/1036
"""

import math

a, b, c = map(float, input().split())

try:
    r1 = ((b * -1) + math.sqrt(((b**2) - (4 * a * c)))) / (2 * a)
    r2 = ((b * -1) - math.sqrt(((b**2) - (4 * a * c)))) / (2 * a)

    print(f"R1 = {r1:0.5f}\nR2 = {r2:0.5f}")
except ValueError:
    print("Impossivel calcular")
