# O Crivo de Eratóstenes

"""O Crivo de Eratóstenes é um algoritmo e um método simples e prático para encontrar
números primos até um certo valor  limite. Segundo a tradição, foi criado pelo matemático grego Eratóstenes
(a.c. 285-194 a.C.)[1], o terceiro bibliotecário-chefe da Biblioteca de Alexandria. (Wikipedia)"""

n = int(input("Digite o número máximo de elementos: "))

lista_numeros = []

for i in range(n + 1):
    lista_numeros.append(i)

# como o número "1" não é considerado primo, tonamos ele em zero
lista_numeros[1] = 0

# começamos com o terceiro elemento
i = 2


while i <= n:
    # compara a iteração atual zom zero
    if lista_numeros[i] != 0:
        # se for diferente de zero atribui-se a variável j a soma de i+i
        j = i + i
        while j <= n:
            # transformamos em zero os elementos que são o resultado de uma soma
            # pois eles não são primos
            lista_numeros[j] = 0
            j = j + i
    i += 1

# ao transformar a lista em set(), retiramos todos os zeros repetidos
lista_numeros = set(lista_numeros)

# retiramos o único zero que restou
lista_numeros.remove(0)

# imprimir lista com primos
print(lista_numeros)

"""
Digite o número máximo de elementos: 50
{2, 3, 5, 37, 7, 41, 11, 43, 13, 47, 17, 19, 23, 29, 31}
"""