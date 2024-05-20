"""Beecrowd exercise 1101.

See: https://judge.beecrowd.com/es/problems/view/1101
"""


def main():
    """Main function."""
    while True:
        m, n = map(int, input().split())

        if m <= 0 or n <= 0:
            break

        if m > n:
            m, n = n, m

        m_n_iter = range(m, n + 1)

        print(f"{' '.join(map(str, m_n_iter))} Sum={sum(m_n_iter)}")


if __name__ == "__main__":
    main()
