"""Beecrowd exercise 1145.
Logical Sequence 2.
Repetition.

See: https://judge.beecrowd.com/es/problems/view/1145
"""


def main():
    """Main function."""
    x, y = map(int, input().split())
    for i in range(1, y + 1):
        print(i, end="\n" if i % x == 0 else " ")


if __name__ == "__main__":
    main()
