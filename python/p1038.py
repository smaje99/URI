"""Beecrowd exercise 1038.

See: https://judge.beecrowd.com/es/problems/view/1038
"""

x, y = map(int, input().split())

values: dict[int, int | float] = {
    1: 4,
    2: 4.5,
    3: 5,
    4: 2,
    5: 1.5,
}

print(f"Total: R$ {values[x] * y:0.2f}")
