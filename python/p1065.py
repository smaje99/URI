"""Beecrowd exercise 1065.

See: https://judge.beecrowd.com/es/problems/view/1065
"""


# Reading input values in a more concise way
values = [int(input()) for _ in range(5)]

# Counting the even numbers using list comprehension
even_count = sum(value % 2 == 0 for value in values)

# Printing the result
print(f"{even_count} valores pares")
