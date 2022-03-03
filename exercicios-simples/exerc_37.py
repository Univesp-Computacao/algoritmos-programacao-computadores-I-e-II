# Somar itens de todas linhas e colunas de uma matriz.

from random import randint

m = 7
n = 5
matriz =[]
linha_soma = [0] * n
coluna_soma = [0] * m

for i in range(n):
    linha = []
    for j in range(m):
        linha.append(randint(0,3))
    matriz.append(linha)

for i in range(n):
    for j in range(m):
        linha_soma[i] += matriz[i][j]
        coluna_soma[j] += matriz[i][j]

for i in range(n):
    print(matriz[i], " | ", linha_soma[i])

print('-'* m * 4 )
print(coluna_soma)
