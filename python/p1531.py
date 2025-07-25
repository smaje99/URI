"""Beecrowd exercise 1531.
Fibonacci Again!.
Mathematics.
Linear Recurrences.

See: https://judge.beecrowd.com/es/problems/view/1531
"""


import sys


# Pre-computar Fibonacci para n <= 70
FIB_CACHE: list[int] = [0, 1]
FIB_CACHE.extend(FIB_CACHE[-1] + FIB_CACHE[-2] for _ in range(2, 71))


def fast_fib(n: int, mod: int) -> int:
    """Calcula FIB(n) % mod de manera óptima:
    - Usa una lista pre-computada para n <= 70.
    - Usa exponenciación de matrices para n > 70.

    Args:
        n (int): Indice del número de Fibonacci (n >= 0).
        mod (int): Módulo para la operación.

    Returns:
        int: FIB(n) % mod.
    """
    if n < 70:
        return FIB_CACHE[n] % mod
    return 0 if mod == 1 else matrix_fib_mod(n, mod)


def matrix_fib_mod(n: int, mod: int) -> int:
    """
    Calcula FIB(n) % mod usando exponenciación de matrices.

    Args:
        n (int): Indice del número de Fibonacci (n >= 0).
        mod (int): Módulo para la operación.

    Returns:
        int: FIB(n) % mod.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1 % mod
    matrix = [[1, 1], [1, 0]]
    res = matrix_pow(matrix, n - 1, mod)
    return res[0][0]


def matrix_multiply(a: list[list[int]], b: list[list[int]], mod: int) -> list[list[int]]:
    """
    Multiplica dos matrices 2x2 bajo un módulo.

    Args:
        a (list): Matriz 2x2 representada como lista de listas.
        b (list): Matriz 2x2 representada como lista de listas.
        mod (int): Módulo para realizar las operaciones.

    Returns:
        list: Resultado de la multiplicación a * b módulo mod.
    """
    return [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod,
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod,
        ],
    ]


def matrix_pow(matrix: list[list[int]], n: int, mod: int) -> list[list[int]]:
    """
    Calcula la potencia n-ésima de una matriz 2x2 bajo un módulo,
    usando exponenciación rápida.

    Args:
        matrix (list): Matriz 2x2 base.
        n (int): Exponente (entero no negativo).
        mod (int): Módulo para las operaciones.

    Returns:
        list: Matriz 2x2 resultante de matrix^n % mod.
    """
    result = [[1, 0], [0, 1]]  # Matriz identidad
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        n //= 2
    return result


pisano_cache: dict[int, int] = {}

def pisano_period(m: int) -> int:
    """
    Calcula el período de Pisano para el módulo m.

    El período de Pisano π(m) es el período con el cual se repite
    la secuencia de Fibonacci módulo m. La secuencia Fib(n) mod m
    siempre es periódica para m ≥ 2.

    Args:
        m (int): Módulo (m ≥ 2).

    Returns:
        int: Longitud del período de Pisano π(m).
    """
    if m in pisano_cache:
        return pisano_cache[m]
    prev, curr = 0, 1
    for i in range(m * 6):  # Límite superior teórico: π(m) ≤ 6*m
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            pisano_cache[m] = i + 1
            return i + 1
    return -1  # No debería alcanzarse si m ≥ 2


def main():
    lines = sys.stdin.read().split()
    output = ""  # StringBuilder para almacenar resultados

    it = iter(lines)
    for n_str, m_str in zip(it, it):
        n, m = int(n_str), int(m_str)

        if m == 1:
            output += "0\n"
            continue

        period = pisano_period(m)
        fib_n_mod_period = fast_fib(n, period)
        fib_n_mod_m = fast_fib(fib_n_mod_period, m)

        output += f"{fib_n_mod_m}\n"

    sys.stdout.write(output)


if __name__ == '__main__':
    main()
