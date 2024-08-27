"""Beecrowd exercise 1050.

See: https://judge.beecrowd.com/es/problems/view/1050
"""

a = int(input())

ddd = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

print(ddd.get(a, "DDD nao cadastrado"))
