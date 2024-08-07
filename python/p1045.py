"""Beecrowd exercise 1045.

See: https://judge.beecrowd.com/es/problems/view/1045
"""

sides = map(float, input().split())

C, B, A = sorted(sides)

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    A2 = A ** 2
    sum_BC2 = B ** 2 + C ** 2

    # Clasificar el triángulo por sus ángulos
    if A2 == sum_BC2:
        print("TRIANGULO RETANGULO")
    elif A2 > sum_BC2:
        print("TRIANGULO OBTUSANGULO")
    elif A2 < sum_BC2:
        print("TRIANGULO ACUTANGULO")

    # Clasificar el triángulo por sus lados
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")
