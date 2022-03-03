# Resolver equação de segundo grau
# importando o método sqrt do módulo math
from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# calcular delta
delta = b * b - 4 * a * c

if delta > 0:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'x1 = {x1} e x2 = {x2}')
elif delta == 0:
    x1 = -b / (2 * a)
    print(f"A única raiz é {x1}")
else:
    print("Não há raíz")
