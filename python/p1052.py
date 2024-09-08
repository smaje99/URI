"""Beecrowd exercise 1052.

See: https://judge.beecrowd.com/es/problems/view/1052
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

m = int(input())

if 1 <= m <= 12:
    print(months[m - 1])
