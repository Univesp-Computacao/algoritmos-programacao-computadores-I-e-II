# Achar uma equação quadrática que tenha soluções em uma faixa específica de coeficientes.

from math import sqrt

a1 = int(input('a1: '))
a2 = int(input('a2: '))
b1 = int(input('b1: '))
b2 = int(input('b2: '))
c1 = int(input('c1: '))
c2 = int(input('c2: '))

a = range (a1, a2 +1)
b = range (b1, b2 +1)
c = range (c1, c2 +1)

for i in a:
    if i == 0:
        continue
    for j in b:
        for k in c:
            print (i, j, k, end=' ')
            d = j * j - 4 * i * k
            if d>=0:
                x1 = (-j -sqrt(d))/(2*i)
                x2 = (-j +sqrt(d))/(2*i)
                x1 = round(x1, 2)
                x2 = round(x2, 2)
                print("Sim", x1, x2)
            else:
                print("Não")
