"""Beecrowd exercise 1095.

See: https://judge.beecrowd.com/es/problems/view/1095
"""


def main():
    """Main function."""
    i_iter = range(1, 40, 3)
    j_iter = range(60, -5, -5)

    for i, j in zip(i_iter, j_iter):
        print(f"I={i} J={j}")


if __name__ == "__main__":
    main()
