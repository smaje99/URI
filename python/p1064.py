"""Beecrowd exercise 1064.

See: https://judge.beecrowd.com/es/problems/view/1064
"""

# Leer los valores en una lista
values = [float(input()) for _ in range(6)]

# Filtrar valores positivos
positives = [v for v in values if v >= 0.0]

# Contar y calcular el promedio de los valores positivos
count = len(positives)
average = sum(positives) / count if count > 0 else 0.0

# Imprimir resultados
print(f"{count} valores positivos")
print(f"{average:.1f}")
