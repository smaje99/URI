"""Beecrowd exercise 1037.

See: https://judge.beecrowd.com/es/problems/view/1037
"""

intervalos: dict[tuple[int, int], str] = {
    (0, 25): "Intervalo [0,25]",
    (25, 50): "Intervalo (25,50]",
    (50, 75): "Intervalo (50,75]",
    (75, 100): "Intervalo (75,100]",
}


def find_intervalo(number: float) -> str:
    """Determina en qué intervalo se encuentra un número dado."""
    for (inicio, fin), mensaje in intervalos.items():
        if inicio <= number <= fin:
            return mensaje
    return "Fora de intervalo"


n = float(input())
print(find_intervalo(n))
