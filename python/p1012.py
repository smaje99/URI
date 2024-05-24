'''Beecrowd exercise 1012.

See: https://judge.beecrowd.com/es/problems/view/1012
'''

A, B, C = map(float, input().split())

print(f"TRIANGULO: {(A * C) / 2:.3f}")
print(f"CIRUCLO: {(C**2) * 3.14159:.3f}")
print(f"TRAPEZIO: {(((A + B) / 2) * C):.3f}")
print(f"QUADRADO: {(B**2):.3f}")
print(f"RETANGULO: {(A * B):.3f}")
