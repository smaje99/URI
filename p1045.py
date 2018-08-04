A,B,C=input().split()
tupla=[float(A),float(B),float(C)]
tupla.sort()
A=tupla[2]
B=tupla[1]
C=tupla[0]
if A>=B+C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == (B**2)+(C**2):
        print("TRIANGULO RETANGULO")
    if A**2 > (B**2)+(C**2):
        print("TRIANGULO OBTUSANGULO")
    if A**2 < (B**2)+(C**2):
        print("TRIANGULO ACUTANGULO")
    if A==B==C:
        print("TRIANGULO EQUILATERO")
    if (A==B!=C) or (B==C!=A) or (C==A!=B):
        print("TRIANGULO ISOSCELES")