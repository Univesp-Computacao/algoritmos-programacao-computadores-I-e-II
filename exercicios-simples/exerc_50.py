# Busca Binária.
from random import randint


# a função abaixo identifica a posição inicial, a do meio e a posição final
# começamos por definir a função e receber dois parâmetros (lista e valor)
# a lista será gerada randomicamente mais abaixo, já o valor a ser buscado será inserido pelo usuário

def procurar(lista, item):
    meio = len(lista) // 2
    min = 0
    max = len(lista) - 1

    # o core da função compara os valores de posição, e percorre o loop fazendo acréscimos na variável
    # min e decréscimos na variável max, até encontrar a posição do valor na lista.

    while lista[meio] != item and min <= max:
        if item > lista[meio]:
            min = meio + 1
        else:
            max = meio - 1
        meio = (min + max) // 2
    if min > max:
        return print("O valor digitado não se encontra na lista")
    else:
        return print("O valor buscado se encontra na ",meio,"ª posição.")


# cria e imprime uma lista randômica
lista_randomica = []
for i in range(10):
    lista_randomica.append(randint(1, 20))
lista_randomica.sort()
print("A lista disponível é: \n", lista_randomica, "\n")

# captura o valor pelo usuário
valor = int(input("Digite um número para buscar: "))

# chama a função procurar() dentro da função print()
print(procurar(lista_randomica, valor))
