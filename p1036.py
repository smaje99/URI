import math
a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
try:
    print("R1 = {:0.5f}".format(((b*-1)+math.sqrt(((b**2)-(4*a*c))))/(2*a)))
    print("R2 = {:0.5f}".format(((b*-1)-math.sqrt(((b**2)-(4*a*c))))/(2*a)))
except:
    print("Impossivel calcular")