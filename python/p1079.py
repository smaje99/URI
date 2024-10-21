"""Beecrowd exercise 1079.

See: https://judge.beecrowd.com/es/problems/view/1079
"""

n = int(input())
resultados: list[float] = []

for _ in range(n):
    a, b, c = map(float, input().split())

    promedio_ponderado = (a * 2 + b * 3 + c * 5) / 10
    resultados.append(promedio_ponderado)

for resultado in resultados:
    print(f"{resultado:.1f}")
