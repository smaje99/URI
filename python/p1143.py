"""Beecrowd exercise 1143.
Squared and Cubic.
Repetition.

See: https://judge.beecrowd.com/es/problems/view/1143
"""


def main():
    """Main function."""
    n = int(input())
    if 1 < n < 1000:
        for i in range(1, n + 1):
            print(f"{i} {i ** 2} {i ** 3}")


if __name__ == "__main__":
    main()
