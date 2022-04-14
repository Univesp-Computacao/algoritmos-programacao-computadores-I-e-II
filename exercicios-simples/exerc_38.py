# A soma de elementos da diagonal de uma matriz

from random import random

# n se refere ao número de colunas
n = 5

# declaramos uma lista vazia
matriz = []


for i in range(n):
    # declaramos uma lista vazia, que se refere a cada linha da matriz
    linha = []
    for j in range(n):
        # como o valor retornado do método random() é decimal
        # multilicamos por 10 e transformamos em inteiro com a função int()
        linha.append(int(random()*10))
    matriz.append(linha)

# imprimir a matriz
for linha in matriz:
    print(linha)

soma_principal = 0
soma_secundaria = 0
for i in range(n):
    # este loop será executado de acordo com o n informado
    # a cada iteração teremos o valor [0][0], depois [1][1] e asism por diante [2][2] etc.
    # observe que o primeiro valor se refere à coluna e o segundo à linha
    soma_principal += matriz[i][i]
    # no caso da diagonal secundária, alteramos apenas o index da linha para
    # que seja feito da direita para esquerda
    # nesse caso teremos o loop retornando [0][4], [1][3], [2][2], [3][1], [4][0]
    soma_secundaria += matriz[i][n-i-1]

# principal se refere à diagonal da esquerda para à direita
print("Soma principal: ", soma_principal)

# principal se refere à diagonal da direita para à esquerda
print("Soma secundária: ", soma_secundaria)