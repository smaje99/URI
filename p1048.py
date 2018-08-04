s=float(input())
if 0.0<=s<=400.00:
    print("Novo salario: {:0.2f}".format(s+(s*0.15)))
    print("Reajuste ganho: {:0.2f}".format(s*0.15))
    print("Em percentual: 15 %")
elif 400.01<=s<=800.0:
    print("Novo salario: {:0.2f}".format(s+(s*0.12)))
    print("Reajuste ganho: {:0.2f}".format(s*0.12))
    print("Em percentual: 12 %")
elif 800.01<=s<=1200.0:
    print("Novo salario: {:0.2f}".format(s+(s*0.1)))
    print("Reajuste ganho: {:0.2f}".format(s*0.1))
    print("Em percentual: 10 %")
elif 1200.01<=s<=2000.0:
    print("Novo salario: {:0.2f}".format(s+(s*0.07)))
    print("Reajuste ganho: {:0.2f}".format(s*0.07))
    print("Em percentual: 7 %")
else:
    print("Novo salario: {:0.2f}".format(s+(s*0.04)))
    print("Reajuste ganho: {:0.2f}".format(s*0.04))
    print("Em percentual: 4 %")