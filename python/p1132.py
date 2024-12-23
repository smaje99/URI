"""Beecrowd exercise 1120.
Multiples of 13.
Repetition

See: https://judge.beecrowd.com/es/problems/view/1120
"""

x = int(input())
y = int(input())

sum_of_non_multiples_of_13 = sum(
  multiple for multiple in range(min(x, y), max(x, y) + 1) if multiple % 13 != 0
)

print(sum_of_non_multiples_of_13)
