# Calcular média aritmética de uma lista de elementos.

def calcularMedia(lista):
    tam_lista = len(lista)
    soma = 0
    for i in lista:
        soma += i
    return soma / tam_lista


numeros_str = input("Digite inteiros separados por espaço para descobrir \n a média aritmética deles:")
print(type(numeros_str))
# converte inteiros a uma lista
numeros_lst = numeros_str.split()
# transforma string em inteiros
for i in range(len(numeros_lst)):
    numeros_lst[i] = int(numeros_lst[i])

# a variavel abaixo irá receber e armazenar o valor de retorno da função calcularMédia()
media = calcularMedia(numeros_lst)

print("A média é :", round(media, 2))
