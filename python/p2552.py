resultado = []


def cheese_breads_around(matriz, n, m):
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == 0:
                for ady in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                    try:
                        if -1 in ady:
                            continue
                        elif matriz[ady[0]][ady[1]] == 9:
                            matriz[i][j] += 1
                    except IndexError:
                        pass


if __name__ == '__main__':
    try:
        while True:
            n, m = map(int, input().split())
            if 1 <= n <= 100 and 1 <= m <= 100:
                matriz = [map(int, input().split()) for i in range(n)]
                matriz = [list(map(lambda cell: 9 if cell == 1 else cell, row)) for row in matriz]
                cheese_breads_around(matriz, n, m)
                resultado += [''.join(map(str, row)) for row in matriz]
    except EOFError:
        for i in resultado:
            print(i)
