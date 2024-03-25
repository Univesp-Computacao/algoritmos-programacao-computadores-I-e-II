# Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por
# linha, os valores negativos na lista. A função não deverá retornar nada.
# >>> negatives([4, 0, −1, −3, 6, −9])

def negativos(args):
    "Retorna os elementos negativos em uma lista passada como paramêtro"
    filtered = list(filter(lambda x: x < 0,args))
    print(filtered)
    return filtered

negativos([4, 0, -1, -3, 6, -9])
    # Output => [-1, -3, -9]
