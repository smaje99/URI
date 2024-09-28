"""Beecrowd exercise 1071.

See: https://judge.beecrowd.com/es/problems/view/1071
"""


x = int(input())
y = int(input())

min_value = min(x, y) + 1
max_value = max(x, y)

start = min_value + 1 if min_value % 2 == 0 else min_value
end = max_value

sum_odd = sum(range(start, end, 2))

print(sum_odd)
