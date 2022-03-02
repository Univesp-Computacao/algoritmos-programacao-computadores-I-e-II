# Achar perímetro e área de um círculo.

import math

raio = float(input("Raio= "))

perimetro = 2 * math.pi * raio
area = math.pi * math.pow(raio, 2)

print(f' perímetro: {perimetro}'
      f' área: {area}')