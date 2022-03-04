# Preencher uma array com números randômicos.

from random import randint

# quantidade de elementos na lista
n = 10

# declara uma array vazia
array = []

# a variável i irá assumir os valores de 0 a 9, gerando o índice da lista
for i in range(n):
    # é adicionado um número randômico no índice da iteração
    array.append(randint(1,99))

print(array)