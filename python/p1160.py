"""Beecrowd exercise 1160.

See: https://judge.beecrowd.com/es/problems/view/1160
"""


def main():
    """Main function."""
    t = int(input())

    for _ in range(t):
        data = input().split()

        pa = int(data[0])
        pb = int(data[1])
        g1 = float(data[2])
        g2 = float(data[3])

        years = 0
        while pa <= pb:
            pa += int(pa * g1 / 100)
            pb += int(pb * g2 / 100)
            years += 1

            if years > 100:
                print("Mais de 1 seculo.")
                break
        else:
            print(f"{years} anos.")


if __name__ == "__main__":
    main()
