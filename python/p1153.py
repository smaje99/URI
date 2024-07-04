"""Beecrowd exercise 1153.

See: https://judge.beecrowd.com/es/problems/view/1153
"""

from math import factorial


def main():
    """Main function."""
    n = int(input())

    if 0 < n < 13:
        print(factorial(n))


if __name__ == "__main__":
    main()
