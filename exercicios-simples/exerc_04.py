# Achar área de superfície de um cilindro.

from math import pi

altura = float(input('altura = '))


raio = float(input('raio = '))

area_base = 2 * (pi * raio**2)

# area do lado
area_lado = 2 * pi * raio * altura

# total
area_total = area_lado + area_base

print(f" A Area é : {round(area_total)}")
