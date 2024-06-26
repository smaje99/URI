"""Beecrowd exercise 1146.

See: https://judge.beecrowd.com/es/problems/view/1146
"""


def main():
    """Main function."""
    while True:
        x = int(input())

        if x == 0:
            break

        print(" ".join([str(i) for i in range(1, x + 1)]))


if __name__ == "__main__":
    main()
