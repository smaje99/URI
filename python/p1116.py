"""Beecrowd exercise 1116.
Repetition

See: https://judge.beecrowd.com/es/problems/view/1116
"""

n = int(input())

for _ in range(n):
    a, b = map(float, input().split())

    if b == 0:
        print("divisao impossivel")
    else:
        print(f"{a / b:0.1f}")
