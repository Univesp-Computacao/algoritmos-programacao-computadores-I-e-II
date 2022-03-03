# A soma de elementos da diagonal de uma matriz

from random import random

n = 5
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(random()*10))
    matriz.append(linha)

for linha in matriz:
    print(linha)

soma_principal = 0
soma_secundaria = 0
for i in range(n):
    soma_principal += matriz[i][i]
    soma_secundaria += matriz[i][n-i-1]

print("Soma principal: ", soma_principal)
print("Soma secundária: ", soma_secundaria)