"""Beecrowd exercise 1097.

See: https://judge.beecrowd.com/es/problems/view/1097
"""


from typing import Sequence


def main():
    """Main function."""
    i_iter = range(1, 10, 2)

    def j_iter(i: int) -> Sequence[int]:
        return range(i + 6, i + 3, -1)

    for i in i_iter:
        for j in j_iter(i):
            print(f"I={i} J={j}")


if __name__ == "__main__":
    main()
