"""Beecrowd exercise 1149.

See: https://judge.beecrowd.com/es/problems/view/1149
"""

from functools import reduce


def main():
    """Main function."""
    an = map(int, input().split())
    a = next(an)
    n = next(an)

    while n <= 0:
        n = next(an, 1)

    sum_reduce = reduce(lambda x, y: x + y + a, range(n), 0)

    print(sum_reduce)


if __name__ == "__main__":
    main()
