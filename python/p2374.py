"""Beecrowd exercise 2374.

See: https://judge.beecrowd.com/es/problems/view/2374
"""


def main():
    """Main function."""
    n_pressure = int(input())
    m_pressure = int(input())

    if 1 <= n_pressure <= 40 and 1 <= m_pressure <= 40:
        print(n_pressure - m_pressure)


if __name__ == "__main__":
    main()
