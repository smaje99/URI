"""Beecrowd exercise 1072.

See: https://judge.beecrowd.com/es/problems/view/1072
"""


n = int(input())

if n < 10_000:
    inside_range = 0
    outside_range = 0

    for _ in range(n):
        x = int(input())
        if -10 ** 7 <= x <= 10 ** 7:
            if 10 <= x <= 20:
                inside_range += 1
            else:
                outside_range += 1

    print(f"{inside_range} in\n{outside_range} out")
