# Calcular a duração de anos de um planeta.

# importar a constante pi do módulo math
from math import pi

# Pegando as entradas e as trasnformando em tipo float
raio = float(input("Raio da órbita (milhões km): "))
velocidade = float(input("Velocidade da órbita (km/s):"))

# transformando milhões de km em apenas km
raio *= 1000000

# um ano em segundos:
ano = (2*pi*raio)/velocidade

# transformando o ano em dias:
ano = ano / (60*60*24)

#arredondando o resultado com função round()
print(round(ano))

#por exemplo a terra está a 29.78 km/s e tem 150 milhões de km de raio
