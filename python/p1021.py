"""Beecrowd exercise 1021.

See: https://judge.beecrowd.com/es/problems/view/1021
"""

notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0]
moedas = [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]

n = float(input())
valor = (n * 100) + 0.05

print("NOTAS:")
for nota in notas:
    qtd = int(valor // (nota * 100))
    print(f"{qtd} nota(s) de R$ {nota:.2f}")
    valor %= nota * 100

print("MOEDAS:")
for moeda in moedas:
    qtd = int(valor // (moeda * 100))
    print(f"{qtd} moeda(s) de R$ {moeda:.2f}")
    valor %= moeda * 100
