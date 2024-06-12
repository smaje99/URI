"""Beecrowd exercise 1118.

See: https://judge.beecrowd.com/es/problems/view/1118
"""


def main():
    """Main function."""
    while True:
        notas: list[float] = []

        while len(notas) < 2:
            nota = float(input())
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("nota invalida")

        media = sum(notas) / 2
        print(f"media = {media:.2f}")

        opcao = 0
        while (
            (opcao := int(input("novo calculo (1-sim 2-nao)\n"))) not in (1, 2)
        ):
            ...

        if opcao == 1:
            continue
        if opcao == 2:
            break


if __name__ == "__main__":
    main()
