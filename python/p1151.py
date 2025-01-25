"""Beecrowd exercise 1151.
Easy Fibonacci.
Repetition.

See: https://judge.beecrowd.com/es/problems/view/1151
"""


def main():
    """Main function."""
    n = int(input())
    a, b = 0, 1
    s = ""
    for i in range(n):
        if i <= 46:
            s += f"{a} "
            a, b = b, a + b
        else:
            s += "0 "
    print(s[:-1])


if __name__ == "__main__":
    main()
