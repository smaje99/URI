"""Beecrowd exercise 1156.

See: https://judge.beecrowd.com/es/problems/view/1156
"""


def main():
    """Main function."""
    s = 1
    b = 2

    for n in range(3, 40, 2):
        s += n / b
        b *= 2

    print(f"{s:.2f}")


if __name__ == "__main__":
    main()
