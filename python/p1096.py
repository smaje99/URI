"""Beecrowd exercise 1096.

See: https://judge.beecrowd.com/es/problems/view/1096
"""

import itertools


def main():
    """Main function."""
    i_iter = range(1, 10, 2)
    j_iter = range(7, 4, -1)

    for i, j in itertools.product(i_iter, j_iter):
        print(f"I={i} J={j}")


if __name__ == "__main__":
    main()
