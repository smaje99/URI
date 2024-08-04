"""Beecrowd exercise 1041.

See: https://judge.beecrowd.com/es/problems/view/1041
"""

x, y = map(float, input().split())

match (x, y):
    case (0, 0):
        print("Origem")
    case (0, _):
        print("Eixo Y")
    case (_, 0):
        print("Eixo X")
    case (x, y) if x > 0 and y > 0:
        print("Q1")
    case (x, y) if x < 0 and y > 0:
        print("Q2")
    case (x, y) if x < 0 and y < 0:
        print("Q3")
    case (x, y) if x > 0 and y < 0:
        print("Q4")
    case _:
        print()
