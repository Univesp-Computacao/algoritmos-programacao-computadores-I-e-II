# Somar itens de todas linhas e colunas de uma matriz.

from random import randint

m = 7  # nr colunas
n = 5  # nr linhas
matriz = []  # matriz vazia
linha_soma = [0] * n  # lista apra guardar soma de linhas
coluna_soma = [0] * m  # lista para guardar soma da coluna

# criamos um laço para preencher a matriz com inteiros aleatórios de 0 a 3
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(randint(0, 3))
    # adicionamos cada linha na matriz
    matriz.append(linha)

# criamos um laço para fazer as somas dos elementos
for i in range(n):
    for j in range(m):
        linha_soma[i] += matriz[i][j]
        coluna_soma[j] += matriz[i][j]

for i in range(n):
    print(matriz[i], " | ", linha_soma[i])

print('-' * m * 4)
print(coluna_soma)
