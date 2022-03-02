# Achar a área e o perímetro de um triângulo reto.

import math

AB = float(input("Comprimento do primeiro cateto: "))
AC = float(input("Comprimento do segundo cateto: "))

# calculo hipotenusa
BC = math.sqrt(AB**2 + AC**2)

area = (AB*AC)/2
perimetro = AB + AC + BC

print(f'Area do triângulo: {area}'
      f'Perímetro: {perimetro}')
