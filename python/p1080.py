"""Beecrowd exercise 1080.

See: https://judge.beecrowd.com/es/problems/view/1080
"""

max_value = 0
index_of_max = 0

for i in range(1, 101):
    value = int(input())
    if value > max_value:
        max_value = value
        index_of_max = i

print(max_value)
print(index_of_max)
