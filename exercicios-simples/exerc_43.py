# Achar média de dois números usando funções

# Define uma função que recebe dois valores numéricos e calcula a média,
# somando os dois e dividindo a soma por dois
def media(n1, n2):
    media = (n1 + n2) / 2
    return media

# Recebe os valores numéricos através do prompt
a = int(input("A : "))
b = int(input("B : "))

# Aplica a função com os valores recebidos
resultado_media = media(a, b)

# Imprime o resultado da função arredondado com a funcção round()
print(round(resultado_media, 2))
