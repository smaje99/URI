"""Beecrowd exercise 1131.

See: https://judge.beecrowd.com/es/problems/view/1131
"""


def main():
    """Main function."""
    gremio = inter = empates = 0

    while True:
        inter_goals, gremio_goals = map(int, input().split())

        if inter_goals > gremio_goals:
            inter += 1
        elif gremio_goals > inter_goals:
            gremio += 1
        else:
            empates += 1

        opcao = 0
        while (
          (opcao := int(input("Novo grenal (1-sim 2-nao)\n"))) not in (1, 2)
        ):
            ...

        if opcao == 2:
            break

    print(f"{inter + gremio + empates} grenais")
    print(f"Inter:{inter}")
    print(f"Gremio:{gremio}")
    print(f"Empates:{empates}")

    if inter > gremio:
        print("Inter venceu mais")
    elif gremio > inter:
        print("Gremio venceu mais")
    else:
        print("Nao houve vencedor")


if __name__ == "__main__":
    main()
