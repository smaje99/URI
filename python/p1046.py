"""Beecrowd exercise 1046.

See: https://judge.beecrowd.com/es/problems/view/1046
"""

a, b = map(int, input().split())

if a == b:
    print("O JOGO DRON 24 HORA(S)")
elif b > a:
    print(f"O JOGO DUROU {b - a} HORA(S)")
else:
    print(f"O JOGO DUROU {24 - a + b} HORA(S)")
