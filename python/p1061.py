"""Beecrowd exercise 1061.

See: https://judge.beecrowd.com/es/problems/view/1061
"""

# Leer el primer día y la hora
dia1 = int(input().split()[1])
h1, m1, s1 = map(int, input().split(':'))

# Leer el segundo día y la hora
dia2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(':'))

# Calcular diferencias
total_seconds1 = (dia1 * 86400) + (h1 * 3600) + (m1 * 60) + s1
total_seconds2 = (dia2 * 86400) + (h2 * 3600) + (m2 * 60) + s2

# Obtener la diferencia total en segundos
delta_seconds = total_seconds2 - total_seconds1

# Calcular días, horas, minutos y segundos
dia, delta_seconds = divmod(delta_seconds, 86400)
h, delta_seconds = divmod(delta_seconds, 3600)
m, s = divmod(delta_seconds, 60)

# Imprimir resultados
print(f"{dia} dia(s)\n{h} hora(s)\n{m} minuto(s)\n{s} segundo(s)")
