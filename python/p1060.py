"""Beecrowd exercise 1060.

See: https://judge.beecrowd.com/es/problems/view/1060
"""


nums = [float(input()) for _ in range(6)]
positives = sum(n >= 0 for n in nums)
print(f"{positives} valores positivos")
