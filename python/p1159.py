"""Beecrowd exercise 1159.
Sum of Consecutive Even Numbers.
Repetition.

See: https://judge.beecrowd.com/es/problems/view/1159
"""


def main():
    """Main function."""
    while True:
        n = int(input())

        if n == 0:
            break

        if n % 2 != 0:
            n += 1  # Make n even

        # n + (n+2) + (n+4) + (n+6) + (n+8) = 5n + 20
        total = 5 * n + 20

        print(total)


if __name__ == "__main__":
    main()
