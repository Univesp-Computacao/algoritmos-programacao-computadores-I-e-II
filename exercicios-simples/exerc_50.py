# Busca Binária.
from random import randint
def procurar(lista, item):
    meio = len(lista) //2
    min = 0
    max = len(lista) -1
    while lista[meio] != item and min <= max:
        if item > lista[meio]:
            min = meio + 1
        else:
            max = meio - 1
        meio = (min + max) // 2
    if min > max:
        return None
    else:
        return meio
a = []
for i in range(10):
    a.append(randint(1,20))
a.sort()
print(a)

valor = int(input("digite um número para buscar: "))
print(procurar(a,valor))
