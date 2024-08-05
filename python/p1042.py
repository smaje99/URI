"""Beecrowd exercise 1042.

See: https://judge.beecrowd.com/es/problems/view/1042
"""

numbers = map(int, input().split())

ordered = sorted(numbers)

for number in ordered:
    print(number)

print()

for number in numbers:
    print(number)
