"""Beecrowd exercise 1259.

See: https://judge.beecrowd.com/es/problems/view/1259
"""

n = int(input())

if 1 <= n <= 10**5:
    even: list[int] = []
    odd: list[int] = []

    for _ in range(n):
        number = int(input())
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    even.sort()
    odd.sort(reverse=True)

    for number in even + odd:
        print(number)
