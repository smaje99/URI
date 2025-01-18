"""Beecrowd exercise 1142.
PUM.
Repetition.

See: https://judge.beecrowd.com/es/problems/view/1142
"""

from itertools import product


def main():
    """Main function."""
    n = int(input())
    for a, _ in enumerate(product(range(n), range(4)), start=1):
        if a % 4 != 0:
            print(a, end=" ")
        else:
            print("PUM")


if __name__ == "__main__":
    main()
