"""Beecrowd exercise 1133.

See: https://judge.beecrowd.com/es/problems/view/1133
"""


def main():
    """Main function."""
    x = int(input())
    y = int(input())

    for i in range(min(x, y) + 1, max(x, y)):
        if i % 5 in (2, 3):
            print(i)


if __name__ == "__main__":
    main()
