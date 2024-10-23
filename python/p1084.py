"""Beecrowd exercise 1084.

See: https://judge.beecrowd.com/es/problems/view/1084
"""

while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break

    t = n - d  # Número de dígitos deseado en el resultado
    stack: list[int] = []

    numbers = map(int, input())

    for i, current in enumerate(numbers):
        # Eliminar elementos del stack mientras el actual sea mayor y aún se
        # pueda completar la longitud `t`
        while stack and len(stack) + n - i > t and stack[-1] < current:
            stack.pop()

        # Agregar el número actual al stack si aún falta para
        # completar `t` dígitos
        if len(stack) < t:
            stack.append(current)

    # Mostrar el número más grande posible
    print("".join(map(str, stack)))
