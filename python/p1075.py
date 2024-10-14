"""Beecrowd exercise 1075.

See: https://judge.beecrowd.com/es/problems/view/1075
"""

n = int(input())

if 1 < n < 10000:  # Ajustamos el rango para que esté entre 1 y 10000
    for i in range(2, 10000, n):  # Comenzamos desde 2 y saltamos de n en n
        print(i)
