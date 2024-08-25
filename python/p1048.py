"""Beecrowd exercise 1048.

See: https://judge.beecrowd.com/es/problems/view/1048
"""

s = float(input())

if 0.0 <= s <= 400.00:
    percentual = 15
elif 400.01 <= s <= 800.00:
    percentual = 12
elif 800.01 <= s <= 1200.00:
    percentual = 10
elif 1200.01 <= s <= 2000.00:
    percentual = 7
else:
    percentual = 4

reajuste = s * (percentual / 100)
novo_salario = s + reajuste

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
