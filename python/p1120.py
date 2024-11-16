"""Beecrowd exercise 1120.
String

See: https://judge.beecrowd.com/es/problems/view/1120
"""

while True:
    try:
        d, n = input().split()

        if d == "0" and n == "0":
            break

        result = int(n.replace(d, "") or 0)
        print(result)
    except EOFError:
        break
