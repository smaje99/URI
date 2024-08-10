"""Beecrowd exercise 1047.

See: https://judge.beecrowd.com/es/problems/view/1047
"""

a, b, c, d = map(int, input().split())

# Convertir el tiempo de inicio y fin en minutos desde el inicio del día
start_time = a * 60 + b
end_time = c * 60 + d

# Si el tiempo de fin es menor o igual al de inicio, cruzamos la medianoche
if end_time <= start_time:
    end_time += 24 * 60

# Calcular la duración en minutos
duration_minutes = end_time - start_time

# Convertir de minutos a horas y minutos
hours = duration_minutes // 60
minutes = duration_minutes % 60

print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")
