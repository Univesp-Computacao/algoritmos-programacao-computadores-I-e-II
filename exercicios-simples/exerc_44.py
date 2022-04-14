# Preencher uma lista com números entre dois valores, um máximo e outro mínimo.

# importa do módulo random o método randint
from random import randint


# define função preencherLista() com 04 argumentos necessários
# uma lista na qual será armazenado os números aleatórios
# uma quantidade que define o número máximo de elementos nessa lista
# um valor mínima e outra máximo, determinando uma faixa específica.
def preencherLista(lista, qtd, min, max):
    # percorre o retorno da função range() com a quantidade máxima de elemntos que
    # desejamos em nossa lista
    for i in range(qtd):
        # a cada iteração adicionamos ao final da lista com o método append()
        # um valor de inteiro randômico entre um máximo e um mínimo, com o método randint()
        lista.append(randint(min, max))


# capturamos as entradas do usuário
num = int(input("Quantidade:"))
minimo = int(input("Mínimo:"))
maximo = int(input("Máximo:"))

# criamos uma  lista vazia
lista_final = []

# chamamos a função e passamos seus 04 argumentos
preencherLista(lista_final, num, minimo, maximo)

# imprimir lista_final
print(lista_final)
