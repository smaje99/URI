"""Beecrowd exercise 1074.

See: https://judge.beecrowd.com/es/problems/view/1074
"""

n = int(input())

if n < 10000:
    for _ in range(n):
        x = int(input())

        if -(10**7) < x < 10**7:
            if x == 0:
                print("NULL")
            else:
                parity = "EVEN" if x % 2 == 0 else "ODD"
                sign = "POSITIVE" if x > 0 else "NEGATIVE"
                print(f"{parity} {sign}")
