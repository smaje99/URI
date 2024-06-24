"""Beecrowd exercise 1144.

See: https://judge.beecrowd.com/es/problems/view/1144
"""


def main():
    """Main function."""
    n = int(input())

    if 1 < n < 1000:
        for i in range(1, n + 1):
            print(f"{i} {i ** 2} {i ** 3}")
            print(f"{i} {i ** 2 + 1} {i ** 3 + 1}")


if __name__ == "__main__":
    main()
