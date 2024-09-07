"""Beecrowd exercise 1051.

See: https://judge.beecrowd.com/es/problems/view/1051
"""

income = float(input())

if 0 <= income <= 2000:
    print("Isento")
else:
    tax: float = 0
    if income > 4500:
        tax += (income - 4500) * 0.28
        income = 4500
    if income > 3000:
        tax += (income - 3000) * 0.18
        income = 3000
    if income > 2000:
        tax += (income - 2000) * 0.08

    print(f"R$ {tax:.2f}")
