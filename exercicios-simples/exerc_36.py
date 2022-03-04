# Preencher uma matrix com números randômicos.
from random import randint

# número de linhas
n = 5

# número de colunas
m = 10

# declara um array vazio
a = []

# Durante essa primeira iteração é criado a linha
for i in range(n):
    # cria uma variável para injetar valores randômicos
    b = []
    # usando a função randint do módulo random
    for j in range(m):
        b.append(randint(1, 9))
    # adicionando à Matriz
    a.append(b)

# Mostrando a Matriz
for i in a:
    for j in i:
        print("3%d" % j, end=' ')
    print()
