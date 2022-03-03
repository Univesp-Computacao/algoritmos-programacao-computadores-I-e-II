# Preencher uma lista com números entre dois valores, um máximo e outro mínimo.

from random import randint

# faça a definição da função preencherLista() e passo 04 argumentos necessários
# uma lista na qual será armazenado os números aleatórios
# uma quantidade que define o número máximo de elementos nessa lista
# um valor mínima e outra máximo, determinando uma faixa específica.
def preencherLista(lista, qtd, min, max ):
    for i in range(qtd):
        lista.append(randint(min,max))

num = int(input("Quantidade:"))
minimo = int(input("Mínimo:"))
maximo = int(input("Máximo:"))


lista_final = []

preencherLista(lista_final,num, minimo,maximo)

print(lista_final)