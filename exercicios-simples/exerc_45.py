# Calcular média aritmética de uma lista de elementos.

def calcularMedia(lista):
    tam_lista = len(lista)
    soma = 0
    for i in lista:
        soma += i
    return soma / tam_lista


print("Digite inteiros separados por espaço para descobrir \n a média aritmética deles:")
numeros_str = input()
print(type(numeros_str))
numeros_lst = numeros_str.split()
for i in range(len(numeros_lst)):
    numeros_lst[i] = int(numeros_lst[i])

media = calcularMedia(numeros_lst)

print("A média é :", round(media, 2))
