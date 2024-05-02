"""Beecrowd exercise 1098.

See: https://judge.beecrowd.com/es/problems/view/1098
"""


def main():
    """Main function."""
    i_seq = range(0, 22, 2)
    j_seq = range(1, 4)

    for i in i_seq:
        for j in j_seq:
            if i % 10 == 0:
                i_num = i // 10
                print(f"I={i_num} J={j + i_num}")
            else:
                i_num = i / 10
                print(f"I={i_num:.1f} J={j + i_num:.1f}")


if __name__ == "__main__":
    main()
