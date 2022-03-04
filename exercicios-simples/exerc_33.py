# Selection sort
# Encher uma lista com números randômicos, mostrá-la e depois
# organizá-la na ordem crescente com o método de selection sort

from random import randint

# número de elementos
n = 7
lista = []
for i in range(n):
    lista.append(randint(1, 20))
print(lista)

# as iterações são ao número de elemntos da lista menos um
j = n - 1
while j > 0:

    # a variável ind irá guardar o valor mais alto
    ind = 0

    for i in range(1, j + 1):
        # verifica se o elemento atual é maior
        if lista[i] > lista[ind]:
            ind = i
    b = lista[ind]
    lista[ind] = lista[j]
    lista[j] = b
    j -= 1
print(lista)
