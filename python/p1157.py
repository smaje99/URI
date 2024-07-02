"""Beecrowd exercise 1157.

See: https://judge.beecrowd.com/es/problems/view/1157
"""


def main():
    """Main function."""
    n = int(input())

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


if __name__ == "__main__":
    main()
